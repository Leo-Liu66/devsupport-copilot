import uuid
from datetime import datetime

from langchain_core.tools import tool

from app.db.crud import insert_ticket
from app.db.database import async_session
from app.models.ticket import TicketRecord


@tool
def create_ticket(
    subject: str,
    body: str,
    category: str,
    severity: str,
    action: str,
    user_email: str | None = None,
) -> str:
    """Persist an analysed support ticket to the database. Returns the ticket_id.
    Use only when you have a fully classified ticket with category, severity, and action."""
    import asyncio

    ticket_id = f"TICKET-{uuid.uuid4().hex[:8].upper()}"
    record = TicketRecord(
        id=ticket_id,
        subject=subject,
        body=body,
        user_email=user_email,
        category=category,
        severity=severity,
        action=action,
        status="open",
        draft_reply=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    return asyncio.run(persist_ticket(record))


async def persist_ticket(record: TicketRecord) -> str:
    """Async helper called directly by persist_node (bypasses @tool sync wrapper)."""
    async with async_session() as session:
        return await insert_ticket(session, record)
