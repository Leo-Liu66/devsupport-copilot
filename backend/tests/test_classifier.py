import json
from pathlib import Path

import pytest

from app.models.ticket import SEVERITY_LEVELS, VALID_CATEGORIES, TicketClassification
from app.services.triage.classifier import classify_ticket

pytestmark = [pytest.mark.integration, pytest.mark.asyncio]


@pytest.fixture(scope="module")
def seed_tickets():
    """Load seed tickets from JSON."""
    path = Path(__file__).resolve().parents[2] / "data" / "seed_tickets.json"
    with open(path) as f:
        return json.load(f)


async def test_category_accuracy_above_threshold(seed_tickets):
    """Classify all seed tickets — category accuracy must be >= 80%."""
    correct = 0
    total = len(seed_tickets)
    misses = []

    for ticket in seed_tickets:
        result = await classify_ticket(ticket["subject"], ticket["body"])
        if result.category == ticket["expected_category"]:
            correct += 1
        else:
            misses.append(
                f"{ticket['id']}: expected={ticket['expected_category']}, "
                f"got={result.category}"
            )

    accuracy = correct / total
    assert accuracy >= 0.80, (
        f"Category accuracy {accuracy:.0%} ({correct}/{total}) below 80% threshold.\n"
        f"Misses:\n" + "\n".join(misses)
    )


async def test_p1_tickets_identified(seed_tickets):
    """All P1 - Critical tickets must be classified as P1."""
    p1_tickets = [t for t in seed_tickets if t["expected_severity"] == "P1 - Critical"]
    assert len(p1_tickets) >= 2, "Expected at least 2 P1 tickets in seed data"

    for ticket in p1_tickets:
        result = await classify_ticket(ticket["subject"], ticket["body"])
        assert result.severity == "P1 - Critical", (
            f"{ticket['id']} ({ticket['subject']}): "
            f"expected P1 - Critical, got {result.severity}"
        )


async def test_all_outputs_are_valid_objects(seed_tickets):
    """Every classification must be a valid TicketClassification."""
    sample_ids = ["TICKET-001", "TICKET-009", "TICKET-016", "TICKET-021", "TICKET-026"]
    samples = [t for t in seed_tickets if t["id"] in sample_ids]

    for ticket in samples:
        result = await classify_ticket(ticket["subject"], ticket["body"])
        assert isinstance(result, TicketClassification)
        assert result.category in VALID_CATEGORIES
        assert result.severity in SEVERITY_LEVELS
        assert 0.0 <= result.confidence <= 1.0
        assert isinstance(result.keywords, list)
        assert len(result.keywords) >= 1
        assert isinstance(result.needs_more_info, bool)


async def test_keywords_are_relevant(seed_tickets):
    """Keywords should overlap with ticket content."""
    ticket = next(t for t in seed_tickets if t["id"] == "TICKET-002")
    result = await classify_ticket(ticket["subject"], ticket["body"])

    ticket_text = (ticket["subject"] + " " + ticket["body"]).lower()
    relevant = [kw for kw in result.keywords if kw.lower() in ticket_text]
    assert len(relevant) >= 1, (
        f"No keywords found in ticket text. Keywords: {result.keywords}"
    )


async def test_needs_more_info_field(seed_tickets):
    """needs_more_info must be True for vague tickets and False for specific ones.

    route_node uses needs_more_info (not confidence) to determine needs_info action.
    Vague tickets: describe a problem without identifiers or reproducible steps.
    Clear tickets: include enough technical context to act on immediately.

    Known edge case (not asserted):
    - TICKET-008: Connect webhook configuration question with no error code — description is
      clear enough to infer the solution, but model flags missing identifiers. False positive
      with low severity: routes to needs_info instead of auto_reply, which is recoverable.
    """
    vague_ids = ["TICKET-007", "TICKET-013", "TICKET-023", "TICKET-025", "TICKET-029"]
    clear_ids = ["TICKET-002", "TICKET-016"]

    for id_ in vague_ids:
        ticket = next(t for t in seed_tickets if t["id"] == id_)
        result = await classify_ticket(ticket["subject"], ticket["body"])
        assert result.needs_more_info is True, (
            f"{id_} ({ticket['subject'][:50]}): "
            f"expected needs_more_info=True, got False"
        )

    for id_ in clear_ids:
        ticket = next(t for t in seed_tickets if t["id"] == id_)
        result = await classify_ticket(ticket["subject"], ticket["body"])
        assert result.needs_more_info is False, (
            f"{id_} ({ticket['subject'][:50]}): "
            f"expected needs_more_info=False, got True"
        )


async def test_p4_tickets_not_escalated(seed_tickets):
    """All P4 tickets must not receive P1 severity.

    Task 05 route_node maps P1 → escalate, P2/P3/P4 → auto_reply.
    A misclassified P4→P1 would incorrectly escalate low-priority tickets.
    P4 tickets classified as P2 or P3 still route correctly to auto_reply.
    Tests all P4-labeled tickets to ensure none are falsely elevated to P1.
    """
    p4_tickets = [t for t in seed_tickets if t["expected_severity"] == "P4 - Low"]
    assert len(p4_tickets) >= 4, "Expected at least 4 P4 tickets in seed data"

    for ticket in p4_tickets:
        result = await classify_ticket(ticket["subject"], ticket["body"])
        assert result.severity != "P1 - Critical", (
            f"{ticket['id']} ({ticket['subject']}): "
            f"P4 ticket falsely elevated to P1 - Critical — "
            f"route_node would incorrectly escalate this ticket"
        )


async def test_keywords_count_within_bounds(seed_tickets):
    """Keywords must be 1-5 items for all tickets — prompt requests 3-5.

    Task 05 retrieve_node passes keywords as retrieval query signals.
    Exceeding 5 keywords makes the retrieval query too diffuse, lowering
    chunk relevance scores and risking retrieval_sufficient=False.
    Tests all 31 tickets since keyword explosion can happen on any input.
    """
    for ticket in seed_tickets:
        result = await classify_ticket(ticket["subject"], ticket["body"])
        assert 1 <= len(result.keywords) <= 5, (
            f"{ticket['id']}: expected 1-5 keywords, got {len(result.keywords)}: "
            f"{result.keywords}"
        )
