from pydantic import BaseModel


class IngestResult(BaseModel):
    num_docs: int
    num_chunks: int
    collection_name: str

class RetrievedChunk(BaseModel):
    chunk_id: str          # e.g. "stripe-webhooks-overview-chunk-003"
    content: str
    source_url: str
    source_title: str
    doc_category: str      # "webhooks" | "payments" | "api" | "refunds" | "config"
    relevance_score: float

class Citation(BaseModel):
    marker: str            # "[1]", "[2]"
    chunk_id: str          # binds to RetrievedChunk.chunk_id
    source_url: str
    source_title: str
    excerpt: str           # first 150 chars of chunk

class CitedAnswer(BaseModel):
    answer: str            # text containing [1], [2] markers
    citations: list[Citation]
    confidence: float
    retrieval_sufficient: bool  # False → triggers escalation hint