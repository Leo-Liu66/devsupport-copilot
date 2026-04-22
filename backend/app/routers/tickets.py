import re

from fastapi import APIRouter, HTTPException

from app.models.ticket import TicketAnalysis, TicketInput
from app.services.workflow import analyze_ticket

router = APIRouter(prefix="/tickets", tags=["tickets"])

_SECRET_RE = re.compile(r"sk-[A-Za-z0-9]{10,}")
_MAX_ERR_LEN = 120


def _sanitize_error(exc: Exception) -> str:
    raw = f"{type(exc).__name__}: {exc}"
    sanitized = _SECRET_RE.sub("sk-***", raw)
    if len(sanitized) > _MAX_ERR_LEN:
        sanitized = sanitized[:_MAX_ERR_LEN] + "..."
    return sanitized


@router.post("/analyze", response_model=TicketAnalysis)
async def analyze(ticket: TicketInput) -> TicketAnalysis:
    if not ticket.subject.strip() or not ticket.body.strip():
        raise HTTPException(status_code=422, detail="subject and body must be non-empty")

    try:
        return await analyze_ticket(ticket)
    except Exception as exc:
        summary = _sanitize_error(exc)
        raise HTTPException(status_code=500, detail=f"Processing failed: {summary}")
