import numpy as np
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


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    a_arr = np.array(a)
    b_arr = np.array(b)
    norm = np.linalg.norm(a_arr) * np.linalg.norm(b_arr)
    if norm == 0:
        return 0.0
    return float(np.dot(a_arr, b_arr) / norm)


def _docs_to_chunks(docs_with_scores: list[tuple]) -> list[RetrievedChunk]:
    chunks = []
    for doc, score in docs_with_scores:
        meta = doc.metadata
        chunks.append(RetrievedChunk(
            chunk_id=meta.get("chunk_id", ""),
            content=doc.page_content,
            source_url=meta.get("source_url", ""),
            source_title=meta.get("source_title", ""),
            doc_category=meta.get("doc_category", "general"),
            relevance_score=float(score),
        ))
    return chunks


async def retrieve(
    query: str,
    top_k: int = 5,
    doc_category: str | None = None,
) -> list[RetrievedChunk]:
    """
    Semantic search over Stripe doc embeddings.

    Primary path (Option A): similarity_search_with_relevance_scores.
    Gives real cosine-based scores; works correctly when the index is clean.

    The ingest pipeline (Fix 2 + Fix 1) removes the root causes that
    previously forced Option B:
      - Fix 2: large files pre-split by H2 section → breaks up oversized docs
      - Fix 1: chunks < 100 chars dropped → removes orphan headers/table rows
      - Intra-doc dedup: repeated code blocks kept only once

    Fallback path (Option B / MMR): activated only when Option A returns all
    results from a single source_url, meaning the cleaned index still can't
    provide diversity for this specific query. MMR's penalty term forces
    results from other semantic clusters. Requires extra per-chunk embed calls
    for post-hoc scoring.

    Args:
        query: natural language query
        top_k: number of chunks to return (default 5)
        doc_category: optional metadata filter ("webhooks", "payments", etc.)

    Returns list of RetrievedChunk with relevance_score.
    """
    vectorstore, embeddings = _get_vectorstore()
    filter_dict: dict | None = {"doc_category": doc_category} if doc_category else None

    # Option A: similarity search with real scores
    results = vectorstore.similarity_search_with_relevance_scores(
        query, k=top_k, filter=filter_dict
    )
    chunks = _docs_to_chunks(results)

    # Check diversity; fall back to MMR only if all results share one source
    unique_sources = {c.source_url for c in chunks}
    if len(chunks) < 2 or len(unique_sources) >= 2:
        return chunks

    # Option B fallback: MMR + post-hoc cosine scores
    mmr_retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": top_k,
            "fetch_k": 20,
            "lambda_mult": 0.7,
            **({"filter": filter_dict} if filter_dict else {}),
        },
    )
    docs = await mmr_retriever.ainvoke(query)
    query_emb = embeddings.embed_query(query)
    mmr_chunks: list[RetrievedChunk] = []
    for doc in docs:
        doc_emb = embeddings.embed_query(doc.page_content)
        score = _cosine_similarity(query_emb, doc_emb)
        meta = doc.metadata
        mmr_chunks.append(RetrievedChunk(
            chunk_id=meta.get("chunk_id", ""),
            content=doc.page_content,
            source_url=meta.get("source_url", ""),
            source_title=meta.get("source_title", ""),
            doc_category=meta.get("doc_category", "general"),
            relevance_score=score,
        ))
    return mmr_chunks
