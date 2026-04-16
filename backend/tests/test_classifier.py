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


async def test_keywords_are_relevant(seed_tickets):
    """Keywords should overlap with ticket content."""
    ticket = next(t for t in seed_tickets if t["id"] == "TICKET-002")
    result = await classify_ticket(ticket["subject"], ticket["body"])

    ticket_text = (ticket["subject"] + " " + ticket["body"]).lower()
    relevant = [kw for kw in result.keywords if kw.lower() in ticket_text]
    assert len(relevant) >= 1, (
        f"No keywords found in ticket text. Keywords: {result.keywords}"
    )


async def test_vague_ticket_gets_moderate_confidence(seed_tickets):
    """Vague/ambiguous tickets should get lower confidence (< 0.9)."""
    ticket = next(t for t in seed_tickets if t["id"] == "TICKET-029")
    result = await classify_ticket(ticket["subject"], ticket["body"])
    assert result.confidence < 0.9, (
        f"Vague ticket got unexpectedly high confidence: {result.confidence}"
    )
