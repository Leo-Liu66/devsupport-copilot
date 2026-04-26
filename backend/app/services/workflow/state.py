from typing import Annotated, TypedDict
import operator

from app.models.kb import CitedAnswer, RetrievedChunk
from app.models.ticket import (
    SimilarTicket,
    TicketClassification,
    TicketInput,
    WorkflowStep,
)


class TicketState(TypedDict, total=False):
    # -- input (set before graph runs) --
    ticket: TicketInput
    ticket_id: str

    # -- classify_node output --
    classification: TicketClassification

    # -- retrieve_node output --
    chunks: list[RetrievedChunk]
    answer: CitedAnswer

    # -- draft_node output --
    draft_reply: str

    # -- branch node output (Task 08: await_human_review | ask_clarification | escalate | draft) --
    action: str  # "auto_reply" | "needs_review" | "needs_info" | "escalate"

    # -- ask_clarification_node output (Task 08) --
    clarification_question: str | None

    # -- investigate_node output --
    similar_tickets: list[SimilarTicket]

    # -- persist_node output --
    persisted_ticket_id: str | None

    # -- accumulated across all nodes (operator.add appends each node's step) --
    workflow_trace: Annotated[list[WorkflowStep], operator.add]
