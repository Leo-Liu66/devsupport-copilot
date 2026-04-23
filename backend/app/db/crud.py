from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import TicketORM
from app.models.ticket import TicketRecord


class DuplicateTicketError(Exception):
    pass


async def insert_ticket(session: AsyncSession, record: TicketRecord) -> str:
    row = TicketORM(**record.model_dump())
    session.add(row)
    try:
        await session.commit()
    except IntegrityError as e:
        await session.rollback()
        raise DuplicateTicketError(record.id) from e
    return record.id


async def get_by_id(session: AsyncSession, ticket_id: str) -> TicketRecord | None:
    result = await session.get(TicketORM, ticket_id)
    if result is None:
        return None
    return TicketRecord(
        id=result.id,
        subject=result.subject,
        body=result.body,
        user_email=result.user_email,
        category=result.category,
        severity=result.severity,
        action=result.action,
        status=result.status,
        draft_reply=result.draft_reply,
        created_at=result.created_at,
        updated_at=result.updated_at,
    )
