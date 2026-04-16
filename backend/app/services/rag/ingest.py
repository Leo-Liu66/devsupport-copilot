import glob
import os
import re
from pathlib import Path

import frontmatter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config import settings
from app.models.kb import IngestResult

# Files larger than this threshold are pre-split by H2 section before chunking.
# Prevents oversized docs (e.g. 254KB error-handling.md) from dominating the
# embedding space with 400+ chunks vs single-topic docs with 10 chunks.
LARGE_FILE_THRESHOLD_BYTES = 50_000

# Chunks shorter than this are dropped: isolated headers, single-cell rows.
MIN_CHUNK_LEN = 100


def _is_table_separator(chunk: str) -> bool:
    """
    Returns True when a chunk is primarily markdown table separator rows.

    Stripe docs contain wide tables whose separator rows (| --- | --- |)
    exceed MIN_CHUNK_LEN after splitting, so length filtering alone won't
    catch them. A chunk is a separator if >50% of its non-empty lines
    consist only of pipes, spaces, dashes, and colons.
    """
    lines = [l for l in chunk.strip().splitlines() if l.strip()]
    if not lines:
        return True
    sep_lines = sum(1 for l in lines if re.match(r"^\|[\s|:\-]+\|?\s*$", l))
    return (sep_lines / len(lines)) > 0.5

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n## ", "\n### ", "\n\n", "\n", " "],
)


def load_document(filepath: str) -> tuple[dict, str]:
    """Returns (metadata_dict, markdown_body)."""
    post = frontmatter.load(filepath)
    metadata = {
        "source_url": post.metadata.get("source_url", ""),
        "source_title": post.metadata.get("source_title", ""),
        "doc_category": post.metadata.get("doc_category", "general"),
    }
    return metadata, post.content


def make_doc_slug(filepath: str) -> str:
    """'data/processed/stripe-webhooks-overview.md' → 'stripe-webhooks-overview'"""
    return Path(filepath).stem


def _split_into_sections(body: str) -> list[str]:
    """
    Pre-split a large document body into H2-level sections.

    Uses lookahead so each section retains its own ## header. Keeps the
    preamble (content before the first ## ) as its own section.
    """
    sections = re.split(r"(?=\n## )", body)
    return [s for s in sections if s.strip()]


def _chunk_body(body: str, filepath: str) -> list[str]:
    """
    Chunk a document body, applying pre-splitting for large files.

    Fix 2 (pre-split): Large files are split by H2 section first so the
    splitter operates on topically coherent pieces, preventing a single
    section header from becoming its own orphan chunk.

    Fix 1 (min-length filter): Chunks shorter than MIN_CHUNK_LEN are dropped
    (isolated headers, table fragments, single-pipe rows).

    Fix 3 (MMR): Applied in retriever.py only as a fallback if the cleaned
    index still produces non-diverse similarity results for a given query.

    Intra-document dedup: exact-duplicate chunks within the same file are
    kept only once (handles repeated multi-language code blocks in Stripe docs).
    """
    file_size = os.path.getsize(filepath)

    if file_size > LARGE_FILE_THRESHOLD_BYTES:
        sections = _split_into_sections(body)
    else:
        sections = [body]

    seen: set[str] = set()
    result: list[str] = []
    for section in sections:
        for chunk in splitter.split_text(section):
            if len(chunk.strip()) < MIN_CHUNK_LEN:
                continue
            if _is_table_separator(chunk):
                continue
            if chunk in seen:
                continue
            seen.add(chunk)
            result.append(chunk)
    return result


async def ingest_documents(doc_dir: str) -> IngestResult:
    """
    Load Stripe markdown docs from doc_dir, chunk, embed, store in ChromaDB.

    Steps:
    1. List all .md files in doc_dir
    2. For each file: parse frontmatter → extract metadata + body
    3. Chunk body: pre-split large files by H2, filter short chunks, dedup
    4. Assign chunk_id: f"{doc_slug}-chunk-{index:03d}"
    5. Store chunks + metadata in ChromaDB (clear collection first)

    Returns IngestResult with counts.
    """
    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )

    # Delete existing collection and recreate (full re-ingest, demo-grade)
    vectorstore = Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=embeddings,
        persist_directory=settings.chroma_persist_dir,
    )
    vectorstore.delete_collection()
    vectorstore = Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=embeddings,
        persist_directory=settings.chroma_persist_dir,
    )

    md_files = sorted(set(
        glob.glob(f"{doc_dir}/**/*.md", recursive=True)
        + glob.glob(f"{doc_dir}/*.md")
    ))
    num_docs = 0
    all_texts: list[str] = []
    all_metadatas: list[dict] = []
    all_ids: list[str] = []

    for filepath in md_files:
        metadata, body = load_document(filepath)
        if not body.strip():
            continue

        doc_slug = make_doc_slug(filepath)
        chunks = _chunk_body(body, filepath)

        for idx, chunk_text in enumerate(chunks):
            chunk_id = f"{doc_slug}-chunk-{idx:03d}"
            all_texts.append(chunk_text)
            all_metadatas.append({
                "chunk_id": chunk_id,
                "source_url": metadata["source_url"],
                "source_title": metadata["source_title"],
                "doc_category": metadata["doc_category"],
            })
            all_ids.append(chunk_id)

        num_docs += 1

    vectorstore.add_texts(texts=all_texts, metadatas=all_metadatas, ids=all_ids)

    return IngestResult(
        num_docs=num_docs,
        num_chunks=len(all_texts),
        collection_name=settings.chroma_collection_name,
    )
