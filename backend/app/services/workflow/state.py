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

    # -- route_node output --
    action: str  # "auto_reply" | "escalate" | "needs_info"

    # -- investigate_node output --
    similar_tickets: list[SimilarTicket]

    # -- persist_node output --
    persisted_ticket_id: str | None

    # -- accumulated across all nodes (operator.add appends each node's step) --
    workflow_trace: Annotated[list[WorkflowStep], operator.add]
