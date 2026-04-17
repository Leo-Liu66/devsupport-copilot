import uuid

from langgraph.graph import END, StateGraph

from app.models.ticket import TicketAnalysis, TicketInput
from app.services.workflow.nodes import classify_node, draft_node, retrieve_node, route_node
from app.services.workflow.state import TicketState

workflow = StateGraph(TicketState)
workflow.add_node("classify", classify_node)
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("draft", draft_node)
workflow.add_node("route", route_node)

workflow.add_edge("classify", "retrieve")
workflow.add_edge("retrieve", "draft")
workflow.add_edge("draft", "route")
workflow.add_edge("route", END)
workflow.set_entry_point("classify")

graph = workflow.compile()


async def analyze_ticket(ticket: TicketInput) -> TicketAnalysis:
    """Run the full classify→retrieve→draft→route workflow."""
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
        similar_tickets=result["similar_tickets"],
        workflow_trace=result["workflow_trace"],
    )
