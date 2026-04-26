from datetime import datetime
from pydantic import BaseModel, Field

from app.models.kb import CitedAnswer

VALID_CATEGORIES = [
    "Webhook Issues",
    "Payment Failures",
    "API Authentication",
    "Refund & Disputes",
    "Account & Configuration",
]

SEVERITY_LEVELS = [
    "P1 - Critical",
    "P2 - High",
    "P3 - Medium",
    "P4 - Low",
]


class TicketInput(BaseModel):
    subject: str
    body: str
    user_email: str | None = None


class TicketClassification(BaseModel):
    category: str          # one of VALID_CATEGORIES
    severity: str          # one of SEVERITY_LEVELS
    confidence: float = Field(ge=0.0, le=1.0)
    keywords: list[str]    # extracted key terms for retrieval boost
    needs_more_info: bool = False  # True when ticket lacks enough detail to diagnose


class SimilarTicket(BaseModel):
    ticket_id: str
    subject: str
    similarity_score: float = Field(ge=0.0, le=1.0)
    resolution: str | None = None


class WorkflowStep(BaseModel):
    node: str                          # "classify", "retrieve", "draft", "route"
    status: str                        # "completed", "skipped", "failed"
    duration_ms: int | None = None
    output_summary: str | None = None


class TicketAnalysis(BaseModel):
    ticket_id: str
    classification: TicketClassification
    answer: CitedAnswer
    draft_reply: str
    action: str        # "auto_reply" | "needs_review" | "needs_info" | "escalate"
    similar_tickets: list[SimilarTicket]
    workflow_trace: list[WorkflowStep]
    persisted_ticket_id: str | None = None
    clarification_question: str | None = None


class TicketRecord(BaseModel):
    """Persisted ticket stored in PostgreSQL."""
    id: str
    subject: str
    body: str
    user_email: str | None = None
    category: str | None = None
    severity: str | None = None
    action: str | None = None
    status: str = "open"          # "open" | "resolved" | "escalated"
    draft_reply: str | None = None
    created_at: datetime
    updated_at: datetime
