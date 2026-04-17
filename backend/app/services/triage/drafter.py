from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.config import settings
from app.models.ticket import TicketInput, TicketClassification
from app.models.kb import CitedAnswer

DRAFTER_PROMPT = """You are a professional support agent for a SaaS product that uses Stripe.
Draft a customer-facing reply to the support ticket below.

## REPLY STRUCTURE

1. **Greeting**: Address the customer professionally (use "Hi" or "Hello", not "Dear")
2. **Acknowledge the issue**: Briefly restate what the customer is experiencing, showing you understand their problem
3. **Answer with citations**: Provide the technical answer. PRESERVE all [1], [2], etc. citation markers from the Answer section EXACTLY as they appear — do not remove, renumber, or add new markers
4. **Next steps**: Give 1-2 concrete actionable steps the customer can take
5. **Closing**: End with an offer to help further (e.g., "Let us know if you have any questions" or "Feel free to reach out if you need further assistance")

## SEVERITY-SPECIFIC BEHAVIOR

{severity_instruction}

## CITATION RULES

- The Answer section below contains [1], [2], etc. markers referencing specific documentation sources
- You MUST preserve these markers in your reply exactly where they appear
- Do NOT invent new citation markers beyond what exists in the Answer
- Do NOT remove or renumber existing markers
- Place the markers naturally within your sentences, keeping them attached to the relevant claim

## TONE AND LENGTH

- Professional, empathetic, concise
- Use "we" (team voice), not "I"
- Target: 50-300 words
- Do NOT use markdown headers or bullet lists in the reply — write in natural paragraphs
- Do NOT include a subject line or "Re:" prefix — just the reply body

## REFERENCES

The following sources were cited in the answer (for your context only — do not reproduce this list in the reply):
{citations_block}

---

**Ticket subject:** {subject}

**Ticket body:** {body}

**Category:** {category}

**Severity:** {severity}

**Answer:**
{answer_text}"""

SEVERITY_INSTRUCTIONS = {
    "P1 - Critical": (
        "This is a CRITICAL (P1) ticket. The customer's production system is currently impacted.\n"
        "- Open with urgency acknowledgment: convey that you understand this is critical and affecting their production\n"
        "- Mention that this has been flagged as high priority\n"
        "- If applicable, mention that the issue will be escalated to a senior engineer for immediate attention"
    ),
    "P2 - High": (
        "This is a HIGH priority (P2) ticket. The customer is experiencing significant impact.\n"
        "- Acknowledge the seriousness of the issue\n"
        "- Convey that you are treating this with priority\n"
        "- Focus on providing a thorough technical answer"
    ),
    "P3 - Medium": (
        "This is a MEDIUM priority (P3) ticket.\n"
        "- Use standard professional tone\n"
        "- No urgency language needed\n"
        "- Focus on being helpful and thorough"
    ),
    "P4 - Low": (
        "This is a LOW priority (P4) ticket — likely a general inquiry or test-mode issue.\n"
        "- Use friendly, helpful tone\n"
        "- No urgency language\n"
        "- Can be more educational/explanatory in style"
    ),
}


def format_citations_block(answer: CitedAnswer) -> str:
    """Format citations as a numbered reference list for the prompt."""
    if not answer.citations:
        return "(No citations available)"
    lines = []
    for citation in answer.citations:
        lines.append(f"{citation.marker} {citation.source_title} — {citation.source_url}")
    return "\n".join(lines)


async def draft_reply(
    ticket: TicketInput,
    classification: TicketClassification,
    answer: CitedAnswer,
) -> str:
    """
    Generate a professional support reply for a classified ticket.

    Combines classification context (category, severity) with the RAG-cited
    answer into a customer-facing reply. Preserves [n] citation markers from
    CitedAnswer.answer verbatim.

    Severity-aware behavior:
    - P1: opens with urgency acknowledgment, mentions escalation/priority handling
    - P2: acknowledges seriousness, conveys priority treatment (no escalation promise)
    - P3/P4: standard professional tone, no urgency language

    Insufficient retrieval handling:
    - When answer.retrieval_sufficient is False, the reply acknowledges the
      limitation and mentions escalation to a senior engineer.

    Args:
        ticket: original ticket (subject, body, user_email)
        classification: category, severity, confidence, keywords
        answer: RAG-generated answer with [n] citation markers and citations list

    Returns:
        Professional support reply as plain text string (50-300 words).
        Contains [n] citation markers matching CitedAnswer.citations.
    """
    severity_instruction = SEVERITY_INSTRUCTIONS.get(
        classification.severity,
        SEVERITY_INSTRUCTIONS["P3 - Medium"],
    )

    answer_text = answer.answer
    if not answer.retrieval_sufficient:
        answer_text += (
            "\n\nNote: Our knowledge base did not have sufficient information "
            "to fully address this issue. This ticket may need escalation to "
            "a senior engineer for further investigation."
        )

    prompt = DRAFTER_PROMPT.format(
        severity_instruction=severity_instruction,
        citations_block=format_citations_block(answer),
        subject=ticket.subject,
        body=ticket.body,
        category=classification.category,
        severity=classification.severity,
        answer_text=answer_text,
    )

    llm = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )

    response = await llm.ainvoke([HumanMessage(content=prompt)])
    return response.content
