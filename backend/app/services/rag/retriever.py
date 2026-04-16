from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config import settings
from app.models.kb import RetrievedChunk


def _get_vectorstore() -> tuple[Chroma, OpenAIEmbeddings]:
    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )
    vectorstore = Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=embeddings,
        persist_directory=settings.chroma_persist_dir,
    )
    return vectorstore, embeddings


async def retrieve(
    query: str,
    top_k: int = 5,
    doc_category: str | None = None,
) -> list[RetrievedChunk]:
    """
    Cosine similarity search over Stripe doc embeddings.

    Uses similarity_search_with_relevance_scores (LangChain Chroma wrapper),
    which returns cosine-based relevance scores in [-1, 1]. Scores below 0.3
    indicate off-topic queries and trigger retrieval_sufficient=False in qa.py.

    Diversity (≥2 unique source_urls in results) is achieved through clean
    ingest rather than algorithmic retrieval tricks:
      - Large files (>50KB) pre-split by H2 section (ingest.py Fix 2)
      - Chunks <100 chars and table separator rows dropped (ingest.py Fix 1)
      - Intra-document exact duplicates removed (ingest.py dedup)
    These three measures prevent any single oversized document from dominating
    the embedding space, so cosine similarity naturally returns diverse sources.

    Args:
        query: natural language query
        top_k: number of chunks to return (default 5)
        doc_category: optional metadata filter ("webhooks", "payments", etc.)

    Returns list of RetrievedChunk with relevance_score.
    """
    vectorstore, _ = _get_vectorstore()
    filter_dict: dict | None = {"doc_category": doc_category} if doc_category else None

    results = vectorstore.similarity_search_with_relevance_scores(
        query, k=top_k, filter=filter_dict
    )

    return [
        RetrievedChunk(
            chunk_id=doc.metadata.get("chunk_id", ""),
            content=doc.page_content,
            source_url=doc.metadata.get("source_url", ""),
            source_title=doc.metadata.get("source_title", ""),
            doc_category=doc.metadata.get("doc_category", "general"),
            relevance_score=float(score),
        )
        for doc, score in results
    ]
