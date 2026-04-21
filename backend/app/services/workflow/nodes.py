import time

from app.models.ticket import WorkflowStep
from app.services.rag.qa import generate_cited_answer
from app.services.rag.retriever import retrieve
from app.services.triage.classifier import classify_ticket
from app.services.triage.drafter import draft_reply
from app.services.workflow.state import TicketState

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
        return {"draft_reply": reply, "workflow_trace": [step]}
    except Exception as e:
        elapsed = int((time.perf_counter() - t0) * 1000)
        step = WorkflowStep(
            node="draft",
            status="failed",
            duration_ms=elapsed,
            output_summary=str(e),
        )
        return {"workflow_trace": [step]}


async def route_node(state: TicketState) -> dict:
    """Determine routing action based on severity + needs_more_info + retrieval quality."""
    classification = state["classification"]
    answer = state["answer"]
    t0 = time.perf_counter()

    severity = classification.severity
    retrieval_ok = answer.retrieval_sufficient

    # Rule 1: P1 always escalates
    if severity == "P1 - Critical":
        action = "escalate"
    # Rule 2: KB has no relevant content — don't auto-reply with garbage
    elif not retrieval_ok:
        action = "escalate"
    # Rule 3: Classifier flagged ticket as too vague to diagnose
    elif classification.needs_more_info:
        action = "needs_info"
    # Rule 4: Default — sufficient detail + sufficient retrieval
    else:
        action = "auto_reply"

    elapsed = int((time.perf_counter() - t0) * 1000)
    step = WorkflowStep(
        node="route",
        status="completed",
        duration_ms=elapsed,
        output_summary=f"action={action} (severity={severity}, needs_more_info={classification.needs_more_info}, retrieval_ok={retrieval_ok})",
    )
    return {"action": action, "workflow_trace": [step]}
