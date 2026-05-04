import pytest

from app.config import settings
from app.services.rag.ingest import ingest_documents
from app.services.rag.retriever import retrieve
from app.services.rag.qa import generate_cited_answer

pytestmark = [pytest.mark.integration, pytest.mark.asyncio]


@pytest.fixture(scope="module")
async def ingested():
    """Ingest docs once for all tests in this module."""
    result = await ingest_documents("../data/processed/")
    yield result


async def test_ingest_creates_chunks(ingested):
    """Ingesting Stripe docs should produce chunks in ChromaDB."""
    assert ingested.num_docs >= 10
    assert ingested.num_chunks >= 50
    assert ingested.collection_name == settings.chroma_collection_name


async def test_chunks_have_complete_metadata(ingested):
    """Every retrieved chunk must have all required metadata fields."""
    chunks = await retrieve("webhook signature verification")
    for chunk in chunks:
        assert chunk.chunk_id, "chunk_id must not be empty"
        assert chunk.source_url.startswith("http"), f"Bad URL: {chunk.source_url}"
        assert chunk.source_title, "source_title must not be empty"
        assert chunk.doc_category in [
            "webhooks", "payments", "api", "refunds", "config", "general"
        ]


async def test_retrieve_returns_relevant_chunks(ingested):
    """Webhook query should return webhook-related content."""
    chunks = await retrieve("How to verify Stripe webhook signatures")
    assert len(chunks) == 5
    content_combined = " ".join(c.content.lower() for c in chunks)
    assert "webhook" in content_combined
    assert "signature" in content_combined


async def test_category_filter_narrows_results(ingested):
    """Filtering by category should only return matching docs."""
    chunks = await retrieve("authentication error", doc_category="api")
    assert all(c.doc_category == "api" for c in chunks)


async def test_retrieval_diversity(ingested):
    """Results should come from at least 2 different source pages."""
    chunks = await retrieve("payment failed")
    unique_sources = set(c.source_url for c in chunks)
    assert len(unique_sources) >= 2, f"Only {len(unique_sources)} unique source(s)"


async def test_cited_answer_has_valid_markers(ingested):
    """Answer should contain [n] markers mapping to real chunks."""
    chunks = await retrieve("How to handle webhook retries")
    answer = await generate_cited_answer("How to handle webhook retries", chunks)
    assert "[1]" in answer.answer
    assert len(answer.citations) > 0
    valid_ids = {c.chunk_id for c in chunks}
    for citation in answer.citations:
        assert citation.chunk_id in valid_ids, f"Citation {citation.marker} maps to unknown chunk"


async def test_irrelevant_query_flags_insufficient(ingested):
    """Off-topic query should be flagged as insufficient retrieval."""
    chunks = await retrieve("how to cook pasta")
    answer = await generate_cited_answer("how to cook pasta", chunks)
    assert answer.retrieval_sufficient is False
