import time
from datetime import datetime

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_openai import ChatOpenAI

from app.config import settings
from app.models.ticket import SimilarTicket, WorkflowStep
from app.services.rag.qa import generate_cited_answer
from app.services.rag.retriever import retrieve
from app.services.tools.kb_tools import search_similar_tickets
from app.services.tools.ticket_tools import persist_ticket
from app.services.triage.classifier import classify_ticket
from app.services.triage.drafter import draft_reply
from app.services.workflow.state import TicketState

INVESTIGATE_SYSTEM = """You triage support tickets. If the ticket describes a \
concrete technical incident, you MAY call search_similar_tickets with a focused \
query combining the subject and key symptoms. Call AT MOST ONCE. \
If the ticket is vague, a general how-to question, or off-topic, do NOT call \
any tool — just respond with an empty message."""

ASK_CLARIFICATION_SYSTEM = (
    "You are a support agent. The user's ticket lacks enough detail to diagnose. "
    "Write ONE clarifying question (max 2 sentences) that asks for the single most "
    "important missing detail. The question MUST end with a '?'. Do not write a reply, "
    "do not apologise, do not repeat the ticket. Just the question."
)

AWAIT_HUMAN_REVIEW_REPLY = (
    "This ticket has been escalated for engineering review. "
    "A human engineer will respond within 1 business hour."
)

ESCALATE_REPLY = (
    "Thank you for reaching out. An engineer will review this "
    "ticket and reply directly."
)

# Lazy-initialized at first use to avoid requiring OPENAI_API_KEY at import time
_investigate_llm = None
_clarification_llm = None


def _get_clarification_llm():
    global _clarification_llm
    if _clarification_llm is None:
        _clarification_llm = ChatOpenAI(
            model=settings.llm_model,
            api_key=settings.openai_api_key,
            temperature=0.2,
        )
    return _clarification_llm


def _get_investigate_llm():
    global _investigate_llm
    if _investigate_llm is None:
        _investigate_llm = ChatOpenAI(
            model=settings.llm_model,
            api_key=settings.openai_api_key,
            temperature=0,
        ).bind_tools([search_similar_tickets])
    return _investigate_llm

async def classify_node(state: TicketState) -> dict:
    """Classify the ticket into category, severity, confidence, and keywords."""
    ticket = state["ticket"]
    t0 = time.perf_counter()
    try:
        result = await classify_ticket(ticket.subject, ticket.body)
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="classify",
            status="completed",
            duration_ms=elapsed,
            output_summary=f"{result.severity} | {result.category} | needs_more_info={result.needs_more_info}",
        )
        return {"classification": result, "workflow_trace": [step]}
    except Exception as e:
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="classify",
            status="failed",
            duration_ms=elapsed,
            output_summary=str(e),
        )
        return {"workflow_trace": [step]}


async def retrieve_node(state: TicketState) -> dict:
    """Retrieve relevant Stripe doc chunks and generate a cited answer."""
    ticket = state["ticket"]
    classification = state["classification"]
    query = f"{ticket.subject} {' '.join(classification.keywords)}"
    t0 = time.perf_counter()
    try:
        chunks = await retrieve(query, top_k=5)
        answer = await generate_cited_answer(query, chunks)
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="retrieve",
            status="completed",
            duration_ms=elapsed,
            output_summary=f"{len(chunks)} chunks | {len(answer.citations)} citations | sufficient={answer.retrieval_sufficient}",
        )
        return {"chunks": chunks, "answer": answer, "workflow_trace": [step]}
    except Exception as e:
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="retrieve",
            status="failed",
            duration_ms=elapsed,
            output_summary=str(e),
        )
        return {"workflow_trace": [step]}


async def draft_node(state: TicketState) -> dict:
    """Draft a professional support reply using classification + cited answer."""
    ticket = state["ticket"]
    classification = state["classification"]
    answer = state["answer"]
    t0 = time.perf_counter()
    try:
        reply = await draft_reply(ticket, classification, answer)
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="draft",
            status="completed",
            duration_ms=elapsed,
            output_summary=f"{len(reply.split())} words",
        )
        return {"draft_reply": reply, "action": "auto_reply", "workflow_trace": [step]}
    except Exception as e:
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="draft",
            status="failed",
            duration_ms=elapsed,
            output_summary=str(e),
        )
        return {"action": "auto_reply", "workflow_trace": [step]}


def branch_after_investigate(state: TicketState) -> str:
    """Conditional edge target selector (Task 08). Pure; no LLM call."""
    classification = state["classification"]
    answer = state["answer"]

    # Rule 1: P1 always needs human review
    if classification.severity == "P1 - Critical":
        return "await_human_review"
    # Rule 2: Classifier flagged ticket as too vague to diagnose
    if classification.needs_more_info:
        return "ask_clarification"
    # Rule 3: KB has no relevant content — don't draft with garbage
    if not answer.retrieval_sufficient:
        return "escalate"
    # Rule 4: Default — sufficient detail + sufficient retrieval
    return "draft"


async def await_human_review_node(state: TicketState) -> dict:
    """P1 HITL synthetic pause. No LLM call."""
    t0 = time.perf_counter()
    similar_count = len(state.get("similar_tickets", []))
    elapsed = int((time.perf_counter() - t0) * 1000)
    step = WorkflowStep(
        node="await_human_review",
        status="completed",
        duration_ms=elapsed,
        output_summary=f"P1 review pending | similar_count={similar_count}",
    )
    return {
        "action": "needs_review",
        "draft_reply": AWAIT_HUMAN_REVIEW_REPLY,
        "workflow_trace": [step],
    }


async def escalate_node(state: TicketState) -> dict:
    """Low-retrieval escalation. No LLM call."""
    t0 = time.perf_counter()
    retrieval_conf = state["answer"].confidence
    elapsed = int((time.perf_counter() - t0) * 1000)
    step = WorkflowStep(
        node="escalate",
        status="completed",
        duration_ms=elapsed,
        output_summary=f"low retrieval (conf={retrieval_conf:.2f})",
    )
    return {
        "action": "escalate",
        "draft_reply": ESCALATE_REPLY,
        "workflow_trace": [step],
    }


async def ask_clarification_node(state: TicketState) -> dict:
    """Generate a 1-2 sentence clarifying question for vague tickets."""
    t0 = time.perf_counter()
    ticket = state["ticket"]
    try:
        llm = _get_clarification_llm()
        ai = await llm.ainvoke([
            SystemMessage(content=ASK_CLARIFICATION_SYSTEM),
            HumanMessage(content=f"Subject: {ticket.subject}\nBody: {ticket.body}"),
        ])
        question = (ai.content or "").strip()
        if not question.endswith("?"):
            question = f"{question.rstrip('.')}?"
        status = "completed"
        summary = f"{len(question.split())} words"
    except Exception as e:
        question = "Could you share the specific error message or ticket ID you're seeing?"
        status = "failed"
        summary = f"{type(e).__name__} — used fallback question"
    elapsed = int((time.perf_counter() - t0) * 1000)
    step = WorkflowStep(
        node="ask_clarification",
        status=status,
        duration_ms=elapsed,
        output_summary=summary,
    )
    return {
        "action": "needs_info",
        "draft_reply": question,
        "clarification_question": question,
        "workflow_trace": [step],
    }


async def investigate_node(state: TicketState) -> dict:
    """Agentic node: LLM decides whether to call search_similar_tickets (max 2 iterations)."""
    import json as _json

    ticket = state["ticket"]
    t0 = time.perf_counter()
    messages = [
        SystemMessage(content=INVESTIGATE_SYSTEM),
        HumanMessage(content=f"Subject: {ticket.subject}\nBody: {ticket.body}"),
    ]
    similar: list[SimilarTicket] = []
    tool_calls_total = 0

    try:
        llm = _get_investigate_llm()
        for _ in range(2):  # HARD CAP per D5
            ai = await llm.ainvoke(messages)
            messages.append(ai)
            if not getattr(ai, "tool_calls", None):
                break
            for tc in ai.tool_calls:
                tool_calls_total += 1
                if tc["name"] == "search_similar_tickets":
                    raw_results = search_similar_tickets.invoke(tc["args"])
                    messages.append(ToolMessage(
                        content=_json.dumps(raw_results),
                        tool_call_id=tc["id"],
                    ))
                    for item in raw_results:
                        if isinstance(item, dict):
                            try:
                                similar.append(SimilarTicket.model_validate(item))
                            except Exception:
                                pass
        status = "completed"
    except Exception:
        status = "failed"
        tool_calls_total = 0

    elapsed = int((time.perf_counter() - t0) * 1000)
    step = WorkflowStep(
        node="investigate",
        status=status,
        duration_ms=elapsed,
        output_summary=f"tool_calls={tool_calls_total} | similar_count={len(similar)}",
    )
    return {"similar_tickets": similar, "workflow_trace": [step]}


async def persist_node(state: TicketState) -> dict:
    """Deterministic persistence: always writes the ticket to Postgres. Soft-fail."""
    from app.models.ticket import TicketRecord

    t0 = time.perf_counter()
    result_id: str | None = None
    try:
        record = TicketRecord(
            id=state["ticket_id"],
            subject=state["ticket"].subject,
            body=state["ticket"].body,
            user_email=state["ticket"].user_email,
            category=state["classification"].category,
            severity=state["classification"].severity,
            action=state["action"],
            status="open",
            draft_reply=state.get("draft_reply"),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        result_id = await persist_ticket(record)
        step_status = "completed"
        summary = f"persisted id={result_id}"
    except Exception as e:
        step_status = "failed"
        summary = f"{type(e).__name__}: {str(e)[:80]}"

    elapsed = int((time.perf_counter() - t0) * 1000)
    step = WorkflowStep(
        node="persist",
        status=step_status,
        duration_ms=elapsed,
        output_summary=summary,
    )
    return {"persisted_ticket_id": result_id, "workflow_trace": [step]}
