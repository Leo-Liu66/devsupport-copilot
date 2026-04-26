import uuid

from langgraph.graph import END, StateGraph

from app.models.ticket import TicketAnalysis, TicketInput
from app.services.workflow.nodes import (
    ask_clarification_node,
    await_human_review_node,
    branch_after_investigate,
    classify_node,
    draft_node,
    escalate_node,
    investigate_node,
    persist_node,
    retrieve_node,
)
from app.services.workflow.state import TicketState

workflow = StateGraph(TicketState)
workflow.add_node("classify", classify_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("investigate", investigate_node)
workflow.add_node("draft", draft_node)
workflow.add_node("await_human_review", await_human_review_node)
workflow.add_node("ask_clarification", ask_clarification_node)
workflow.add_node("escalate", escalate_node)
workflow.add_node("persist", persist_node)

workflow.set_entry_point("classify")
workflow.add_edge("classify", "retrieve")
workflow.add_edge("retrieve", "investigate")

workflow.add_conditional_edges(
    "investigate",
    branch_after_investigate,
    {
        "draft": "draft",
        "await_human_review": "await_human_review",
        "ask_clarification": "ask_clarification",
        "escalate": "escalate",
    },
)

workflow.add_edge("draft", "persist")
workflow.add_edge("await_human_review", "persist")
workflow.add_edge("ask_clarification", "persist")
workflow.add_edge("escalate", "persist")
workflow.add_edge("persist", END)

graph = workflow.compile()


async def analyze_ticket(ticket: TicketInput) -> TicketAnalysis:
    """Run the full classify→retrieve→investigate→[branch]→persist workflow."""
    ticket_id = f"TICKET-{uuid.uuid4().hex[:8].upper()}"

    initial_state: TicketState = {
        "ticket": ticket,
        "ticket_id": ticket_id,
        "similar_tickets": [],
        "workflow_trace": [],
    }

    result = await graph.ainvoke(initial_state)

    return TicketAnalysis(
        ticket_id=result["ticket_id"],
        classification=result["classification"],
        answer=result["answer"],
        draft_reply=result["draft_reply"],
        action=result["action"],
        similar_tickets=result.get("similar_tickets", []),
        workflow_trace=result["workflow_trace"],
        persisted_ticket_id=result.get("persisted_ticket_id"),
        clarification_question=result.get("clarification_question"),
    )
