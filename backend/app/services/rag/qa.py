import re

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from app.config import settings
from app.models.kb import Citation, CitedAnswer, RetrievedChunk

_llm = ChatOpenAI(
    model=settings.llm_model,
    api_key=settings.openai_api_key,
    temperature=0,
)

CITED_QA_PROMPT = """You are a technical support assistant for a SaaS product using Stripe.
Answer the user's question using ONLY the provided sources.

CITATION RULES:
- Add citation markers [1], [2], etc. after each factual claim
- Each marker MUST correspond to one of the numbered sources below
- You may cite multiple sources for one claim: [1][3]
- If the sources don't contain enough information, say:
  "I don't have enough information in our knowledge base to fully answer this.
   This ticket may need escalation to a senior engineer."
- NEVER fabricate information not found in the sources
- NEVER invent source numbers beyond what is provided

Sources:
{formatted_sources}

User question: {query}

Respond in a professional, concise support tone. Start with the direct answer."""


def format_sources(chunks: list[RetrievedChunk]) -> str:
    lines = []
    for i, chunk in enumerate(chunks, 1):
        lines.append(
            f"[{i}] {chunk.content}\n"
            f"    (Source: {chunk.source_title} — {chunk.source_url})"
        )
    return "\n\n".join(lines)


def parse_citations(answer_text: str, chunks: list[RetrievedChunk]) -> list[Citation]:
    markers = set(re.findall(r'\[(\d+)\]', answer_text))
    citations = []
    for m in sorted(markers, key=int):
        idx = int(m) - 1
        if 0 <= idx < len(chunks):
            chunk = chunks[idx]
            citations.append(Citation(
                marker=f"[{m}]",
                chunk_id=chunk.chunk_id,
                source_url=chunk.source_url,
                source_title=chunk.source_title,
                excerpt=chunk.content[:150] + "...",
            ))
    return citations


async def generate_cited_answer(
    query: str,
    chunks: list[RetrievedChunk],
) -> CitedAnswer:
    """
    Generate source-first cited answer.

    Steps:
    1. Format chunks as numbered sources [1]-[n]
    2. Call LLM with CITED_QA_PROMPT
    3. Parse [n] markers from response → map to chunk_ids
    4. Compute retrieval_sufficient based on avg relevance_score

    If avg relevance < 0.3 → retrieval_sufficient = False
    """
    avg_score = sum(c.relevance_score for c in chunks) / len(chunks) if chunks else 0.0
    retrieval_sufficient = avg_score >= 0.3

    formatted_sources = format_sources(chunks)
    prompt = CITED_QA_PROMPT.format(
        formatted_sources=formatted_sources,
        query=query,
    )

    response = await _llm.ainvoke([HumanMessage(content=prompt)])
    answer_text = response.content

    return CitedAnswer(
        answer=answer_text,
        citations=parse_citations(answer_text, chunks),
        confidence=avg_score,
        retrieval_sufficient=retrieval_sufficient,
    )
