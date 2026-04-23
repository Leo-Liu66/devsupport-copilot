import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.models.ticket import TicketAnalysis

pytestmark = pytest.mark.integration


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="module")
def seed_tickets() -> list[dict]:
    path = Path(__file__).resolve().parents[2] / "data" / "seed_tickets.json"
    with open(path) as f:
        return json.load(f)


@pytest.fixture(scope="module")
def ticket_001(seed_tickets: list[dict]) -> dict:
    return next(t for t in seed_tickets if t["id"] == "TICKET-001")


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------


def test_valid_request_returns_200(client: TestClient, ticket_001: dict) -> None:
    resp = client.post(
        "/tickets/analyze",
        json={"subject": ticket_001["subject"], "body": ticket_001["body"]},
    )
    assert resp.status_code == 200
    data = resp.json()
    analysis = TicketAnalysis.model_validate(data)
    assert analysis.ticket_id.startswith("TICKET-")
    assert analysis.classification is not None
    assert analysis.draft_reply


def test_response_includes_workflow_trace(client: TestClient, ticket_001: dict) -> None:
    resp = client.post(
        "/tickets/analyze",
        json={"subject": ticket_001["subject"], "body": ticket_001["body"]},
    )
    assert resp.status_code == 200
    trace = resp.json()["workflow_trace"]
    assert len(trace) == 6
    nodes = {step["node"] for step in trace}
    assert nodes == {"classify", "retrieve", "investigate", "draft", "route", "persist"}


# ---------------------------------------------------------------------------
# Input validation — 422
# ---------------------------------------------------------------------------


def test_empty_subject_returns_422(client: TestClient) -> None:
    resp = client.post("/tickets/analyze", json={"subject": "", "body": "Some body"})
    assert resp.status_code == 422


def test_empty_body_returns_422(client: TestClient) -> None:
    resp = client.post("/tickets/analyze", json={"subject": "Some subject", "body": ""})
    assert resp.status_code == 422


def test_missing_field_returns_422(client: TestClient) -> None:
    resp = client.post("/tickets/analyze", json={"subject": "Missing body field"})
    assert resp.status_code == 422


def test_whitespace_only_subject_returns_422(client: TestClient) -> None:
    resp = client.post("/tickets/analyze", json={"subject": "   ", "body": "Some body"})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# Full-suite tests (slow — hit real OpenAI + ChromaDB)
# ---------------------------------------------------------------------------


def test_all_31_tickets_no_500(client: TestClient, seed_tickets: list[dict]) -> None:
    for raw in seed_tickets:
        resp = client.post(
            "/tickets/analyze",
            json={"subject": raw["subject"], "body": raw["body"]},
        )
        assert resp.status_code < 500, (
            f"{raw['id']} returned HTTP {resp.status_code}: {resp.text[:200]}"
        )


def test_category_accuracy_on_31_tickets(client: TestClient, seed_tickets: list[dict]) -> None:
    correct = 0
    for raw in seed_tickets:
        resp = client.post(
            "/tickets/analyze",
            json={"subject": raw["subject"], "body": raw["body"]},
        )
        if resp.status_code == 200:
            got = resp.json()["classification"]["category"]
            if got == raw["expected_category"]:
                correct += 1

    accuracy = correct / len(seed_tickets)
    assert accuracy >= 0.80, (
        f"Category accuracy {accuracy:.1%} ({correct}/{len(seed_tickets)}) is below 80%"
    )


# ---------------------------------------------------------------------------
# Security: 500 response must not leak secrets
# ---------------------------------------------------------------------------


def test_500_response_has_no_secrets(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_key = "sk-test1234567890abcdefghijklmnop"

    async def _raise(_):
        raise ValueError(f"AuthenticationError with key {fake_key} invalid")

    monkeypatch.setattr("app.routers.tickets.analyze_ticket", _raise)

    local_client = TestClient(app)
    resp = local_client.post(
        "/tickets/analyze",
        json={"subject": "Test subject", "body": "Test body"},
    )
    assert resp.status_code == 500
    body = resp.text
    assert fake_key not in body, "API key leaked in 500 response"
    assert "Traceback" not in body, "Traceback leaked in 500 response"
    assert "detail" in resp.json()
