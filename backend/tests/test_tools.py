"""
Integration tests for Task 07 tools.

Prerequisites (must be true before running):
  - docker compose up -d postgres  (healthy)
  - python backend/scripts/synthesize_resolutions.py
  - python backend/scripts/ingest_historical_tickets.py
"""
import json
import uuid
from datetime import datetime
from pathlib import Path

import pytest
import pytest_asyncio

from app.db.crud import DuplicateTicketError, get_by_id, insert_ticket
from app.db.database import async_session, init_db
from app.models.ticket import SimilarTicket, TicketInput, TicketRecord
from app.services.tools.kb_tools import search_similar_tickets
from app.services.tools.ticket_tools import persist_ticket
from app.services.workflow.nodes import investigate_node
from app.services.workflow.state import TicketState

pytestmark = [pytest.mark.integration, pytest.mark.asyncio]


@pytest_asyncio.fixture
async def db_session():
    """Ensure schema exists, clear tickets table, yield a fresh session."""
    from sqlalchemy import text

    await init_db()
    async with async_session() as session:
        await session.execute(text("DELETE FROM tickets"))
        await session.commit()
        yield session


def _make_record(ticket_id: str | None = None) -> TicketRecord:
    return TicketRecord(
        id=ticket_id or f"TICKET-{uuid.uuid4().hex[:8].upper()}",
        subject="Test webhook signature failure",
        body="Webhook signature verification fails after key rotation.",
        user_email=None,
        category="Webhook Issues",
        severity="P2 - High",
        action="auto_reply",
        status="open",
        draft_reply="Please update your signing secret.",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


def _build_ticket_001_state() -> TicketState:
    data = json.loads(
        (Path(__file__).resolve().parents[2] / "data" / "seed_tickets.json").read_text()
    )
    t = next(t for t in data if t["id"] == "TICKET-001")
    ticket = TicketInput(subject=t["subject"], body=t["body"], user_email=t.get("user_email"))
    return {
        "ticket": ticket,
        "ticket_id": "TICKET-001",
        "similar_tickets": [],
        "workflow_trace": [],
    }


# ---------------------------------------------------------------------------
# search_similar_tickets tool tests
# ---------------------------------------------------------------------------

async def test_search_similar_tickets_returns_results() -> None:
    """Concrete incident query must return ≥1 result with similarity_score > 0.3."""
    results = search_similar_tickets.invoke(
        {"query": "webhook signature failing in production after key rotation", "top_k": 3}
    )
    assert isinstance(results, list), "Expected list of results"
    assert len(results) >= 1, "Expected at least 1 similar ticket for a specific incident query"
    top = SimilarTicket.model_validate(results[0])
    assert top.similarity_score > 0.3, f"Top similarity_score {top.similarity_score:.3f} is too low"
    assert top.resolution, "resolution field should be non-empty"


async def test_search_similar_tickets_off_topic_empty_or_low_score() -> None:
    """Off-topic query must return either empty list or all scores < 0.3."""
    results = search_similar_tickets.invoke({"query": "what's the weather today", "top_k": 3})
    if results:
        tickets = [SimilarTicket.model_validate(r) for r in results]
        assert all(t.similarity_score < 0.3 for t in tickets), (
            f"Off-topic query returned high-scoring results: {[t.similarity_score for t in tickets]}"
        )


async def test_llm_invokes_tool_on_incident_query() -> None:
    """TICKET-001 (concrete webhook error) must trigger the search_similar_tickets tool."""
    state = _build_ticket_001_state()
    result = await investigate_node(state)

    similar = result.get("similar_tickets", [])
    trace = result.get("workflow_trace", [])
    assert trace, "investigate_node must emit a WorkflowStep"
    step = trace[0]
    tool_calls_count = int(step.output_summary.split("tool_calls=")[1].split(" ")[0])
    assert tool_calls_count >= 1, f"Expected tool_calls>=1, got output_summary: {step.output_summary}"
    assert tool_calls_count <= 2, f"max_iterations=2 cap violated, tool_calls={tool_calls_count}"
    assert len(similar) >= 1, f"Expected similar_tickets to be populated, got: {similar}"


async def test_llm_skips_tool_on_vague_query() -> None:
    """Vague ticket must NOT trigger the tool call."""
    ticket = TicketInput(subject="something broken", body="stuff broken help pls")
    state: TicketState = {
        "ticket": ticket,
        "ticket_id": "TICKET-VAGUE",
        "similar_tickets": [],
        "workflow_trace": [],
    }
    result = await investigate_node(state)

    trace = result.get("workflow_trace", [])
    assert trace, "investigate_node must emit a WorkflowStep"
    step = trace[0]
    assert "tool_calls=0" in step.output_summary, (
        f"Vague ticket should NOT invoke tool, got: {step.output_summary}"
    )
    assert result.get("similar_tickets", []) == [], "similar_tickets must be empty for vague query"


# ---------------------------------------------------------------------------
# persist_ticket / crud tests
# ---------------------------------------------------------------------------

async def test_create_ticket_persists_row(db_session) -> None:
    """persist_ticket must write a row readable by get_by_id."""
    record = _make_record()
    returned_id = await persist_ticket(record)
    assert returned_id == record.id

    row = await get_by_id(db_session, returned_id)
    assert row is not None, "Row should be present in DB after persist_ticket"
    assert row.subject == record.subject
    assert row.category == record.category
    assert row.severity == record.severity
    assert row.action == record.action


async def test_persist_is_idempotent_on_pk_collision(db_session) -> None:
    """Inserting the same ticket_id twice must raise DuplicateTicketError."""
    ticket_id = f"TICKET-{uuid.uuid4().hex[:8].upper()}"
    record = _make_record(ticket_id)

    await insert_ticket(db_session, record)
    # Re-open a fresh session because the first commit closed the transaction
    async with async_session() as session2:
        with pytest.raises(DuplicateTicketError):
            await insert_ticket(session2, record)


# ---------------------------------------------------------------------------
# ChromaDB collection check
# ---------------------------------------------------------------------------

async def test_historical_collection_has_31_tickets() -> None:
    """historical_tickets collection must have exactly 31 entries with non-empty resolutions."""
    import chromadb
    from app.config import settings

    client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
    collection = client.get_collection("historical_tickets")
    count = collection.count()
    assert count == 31, f"Expected 31 historical tickets, found {count}"

    sample = collection.get(limit=5, include=["metadatas"])
    for meta in sample["metadatas"]:
        assert meta.get("resolution"), f"Missing resolution in metadata: {meta}"
