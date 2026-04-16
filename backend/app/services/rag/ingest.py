import glob
import re
from pathlib import Path

import frontmatter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config import settings
from app.models.kb import IngestResult

# Chunks shorter than this are dropped: isolated headers, single-cell rows
# that carry no semantic content on their own.
MIN_CHUNK_LEN = 100

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n## ", "\n### ", "\n\n", "\n", " "],
)


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


async def ingest_documents(doc_dir: str) -> IngestResult:
    """
    Load Stripe markdown docs from doc_dir, chunk, embed, store in ChromaDB.

    Steps:
    1. List all .md files in doc_dir
    2. For each file: parse frontmatter → extract metadata + body
    3. Chunk body with RecursiveCharacterTextSplitter, filtering out
       short chunks (<100 chars) and table separator rows
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
        raw_chunks = splitter.split_text(body)
        idx = 0
        for chunk_text in raw_chunks:
            if len(chunk_text.strip()) < MIN_CHUNK_LEN:
                continue
            if _is_table_separator(chunk_text):
                continue
            chunk_id = f"{doc_slug}-chunk-{idx:03d}"
            all_texts.append(chunk_text)
            all_metadatas.append({
                "chunk_id": chunk_id,
                "source_url": metadata["source_url"],
                "source_title": metadata["source_title"],
                "doc_category": metadata["doc_category"],
            })
            all_ids.append(chunk_id)
            idx += 1

        num_docs += 1

    vectorstore.add_texts(texts=all_texts, metadatas=all_metadatas, ids=all_ids)

    return IngestResult(
        num_docs=num_docs,
        num_chunks=len(all_texts),
        collection_name=settings.chroma_collection_name,
    )
