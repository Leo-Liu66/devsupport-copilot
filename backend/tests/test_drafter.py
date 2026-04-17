import pytest

from app.models.ticket import TicketInput, TicketClassification
from app.models.kb import CitedAnswer, Citation
from app.services.triage.drafter import draft_reply

pytestmark = [pytest.mark.integration, pytest.mark.asyncio]


@pytest.fixture
def sample_ticket():
    """A typical webhook issue ticket."""
    return TicketInput(
        subject="Webhook endpoint returns 500 after payment_intent.succeeded event",
        body=(
            "Our webhook handler started throwing 500 errors for "
            "payment_intent.succeeded events. The signature verification passes "
            "but our database update fails. Events are being retried every hour."
        ),
        user_email="dev@acmecorp.com",
    )


@pytest.fixture
def p1_classification():
    return TicketClassification(
        category="Webhook Issues",
        severity="P1 - Critical",
        confidence=0.95,
        keywords=["webhook", "500 error", "payment_intent.succeeded"],
    )


@pytest.fixture
def p4_classification():
    return TicketClassification(
        category="Account & Configuration",
        severity="P4 - Low",
        confidence=0.85,
        keywords=["test mode", "configuration"],
    )


@pytest.fixture
def cited_answer_sufficient():
    """A CitedAnswer with citations and sufficient retrieval."""
    return CitedAnswer(
        answer=(
            "When your webhook handler returns a 500 error, Stripe will retry "
            "the event delivery [1]. To prevent data inconsistencies, implement "
            "idempotency by checking the event ID before processing [2]. You can "
            "also use the Stripe Dashboard to monitor failed webhook deliveries [1]."
        ),
        citations=[
            Citation(
                marker="[1]",
                chunk_id="stripe-webhooks-retry-chunk-001",
                source_url="https://docs.stripe.com/webhooks#retries",
                source_title="Stripe Webhook Retries",
                excerpt="Stripe will retry webhook delivery up to...",
            ),
            Citation(
                marker="[2]",
                chunk_id="stripe-webhooks-best-practices-chunk-003",
                source_url="https://docs.stripe.com/webhooks/best-practices",
                source_title="Webhook Best Practices",
                excerpt="To safely handle duplicate events, make your...",
            ),
        ],
        confidence=0.75,
        retrieval_sufficient=True,
    )


@pytest.fixture
def cited_answer_insufficient():
    """A CitedAnswer where retrieval was insufficient."""
    return CitedAnswer(
        answer=(
            "I don't have enough information in our knowledge base to fully "
            "answer this. This ticket may need escalation to a senior engineer."
        ),
        citations=[],
        confidence=0.15,
        retrieval_sufficient=False,
    )


async def test_reply_contains_citation_markers(
    sample_ticket, p1_classification, cited_answer_sufficient
):
    """Citation markers [1] and [2] from CitedAnswer must appear in the reply."""
    reply = await draft_reply(sample_ticket, p1_classification, cited_answer_sufficient)
    assert "[1]" in reply, f"Missing [1] in reply:\n{reply}"
    assert "[2]" in reply, f"Missing [2] in reply:\n{reply}"


async def test_p1_reply_mentions_urgency(
    sample_ticket, p1_classification, cited_answer_sufficient
):
    """P1 ticket reply should contain urgency/priority/escalation language."""
    reply = await draft_reply(sample_ticket, p1_classification, cited_answer_sufficient)
    reply_lower = reply.lower()
    urgency_terms = ["critical", "urgent", "priority", "escalat", "immediate"]
    has_urgency = any(term in reply_lower for term in urgency_terms)
    assert has_urgency, (
        f"P1 reply missing urgency language. Reply:\n{reply}"
    )


async def test_p4_reply_no_urgency(
    sample_ticket, p4_classification, cited_answer_sufficient
):
    """P4 ticket reply should NOT contain urgency/escalation language."""
    reply = await draft_reply(sample_ticket, p4_classification, cited_answer_sufficient)
    reply_lower = reply.lower()
    urgency_terms = ["critical", "urgent", "immediate", "escalat"]
    has_urgency = any(term in reply_lower for term in urgency_terms)
    assert not has_urgency, (
        f"P4 reply should not have urgency language. Found in reply:\n{reply}"
    )


async def test_reply_word_count_in_range(
    sample_ticket, p1_classification, cited_answer_sufficient
):
    """Reply should be between 50 and 300 words."""
    reply = await draft_reply(sample_ticket, p1_classification, cited_answer_sufficient)
    word_count = len(reply.split())
    assert 50 <= word_count <= 300, (
        f"Reply word count {word_count} outside 50-300 range. Reply:\n{reply}"
    )


async def test_reply_has_greeting_and_closing(
    sample_ticket, p1_classification, cited_answer_sufficient
):
    """Reply should start with a greeting and end with an offer to help."""
    reply = await draft_reply(sample_ticket, p1_classification, cited_answer_sufficient)
    reply_lower = reply.lower()
    first_line = reply_lower.split("\n")[0]
    greetings = ["hi", "hello", "thank"]
    has_greeting = any(g in first_line for g in greetings)
    assert has_greeting, f"Reply missing greeting in first line: {first_line}"
    last_chunk = reply_lower[-200:]
    closings = ["help", "question", "assist", "reach out", "let us know", "hesitate"]
    has_closing = any(c in last_chunk for c in closings)
    assert has_closing, f"Reply missing closing offer. Last 200 chars: {last_chunk}"


async def test_insufficient_retrieval_mentions_escalation(
    sample_ticket, p4_classification, cited_answer_insufficient
):
    """When retrieval is insufficient, reply should mention escalation even for P4."""
    reply = await draft_reply(sample_ticket, p4_classification, cited_answer_insufficient)
    reply_lower = reply.lower()
    escalation_terms = ["escalat", "senior engineer", "further investigation", "team"]
    has_escalation = any(term in reply_lower for term in escalation_terms)
    assert has_escalation, (
        f"Insufficient retrieval reply missing escalation mention. Reply:\n{reply}"
    )
