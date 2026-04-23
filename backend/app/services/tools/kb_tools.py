from langchain_core.tools import tool
from langchain_openai import OpenAIEmbeddings

from app.config import settings
from app.models.ticket import SimilarTicket

HISTORICAL_COLLECTION = "historical_tickets"


def _get_historical_vectorstore():
    import chromadb

    client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )
    collection = client.get_collection(HISTORICAL_COLLECTION)
    return collection, embeddings


@tool
def search_similar_tickets(query: str, top_k: int = 3) -> list[dict]:
    """Search the historical incident database for tickets similar to the given query.
    Use when the current ticket describes a specific technical incident where past
    resolutions would help diagnose the issue. Do NOT use for vague queries,
    general how-to questions, or off-topic requests."""
    collection, embeddings = _get_historical_vectorstore()

    query_embedding = embeddings.embed_query(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    similar: list[dict] = []
    if not results["ids"] or not results["ids"][0]:
        return similar

    for doc_id, distance, metadata in zip(
        results["ids"][0],
        results["distances"][0],
        results["metadatas"][0],
    ):
        # Chroma returns L2 distances; convert to similarity score [0, 1]
        similarity_score = max(0.0, 1.0 - distance / 2.0)
        ticket = SimilarTicket(
            ticket_id=metadata.get("ticket_id", doc_id),
            subject=metadata.get("subject", ""),
            similarity_score=round(similarity_score, 4),
            resolution=metadata.get("resolution") or None,
        )
        similar.append(ticket.model_dump())

    return similar
