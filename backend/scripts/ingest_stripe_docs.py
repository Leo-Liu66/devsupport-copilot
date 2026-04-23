"""
Ingest Stripe documentation markdown files into ChromaDB as 'stripe_docs'.

Run once after cloning. Re-running recreates the collection (idempotent).
Estimated cost: ~$0.10 in OpenAI embedding calls (962 chunks).
"""
import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from app.services.rag.ingest import ingest_documents

DOC_DIR = ROOT / "data" / "processed"


async def main() -> None:
    if not DOC_DIR.exists() or not list(DOC_DIR.glob("*.md")):
        print(f"ERROR: No markdown files found in {DOC_DIR}")
        sys.exit(1)

    print(f"Ingesting Stripe docs from {DOC_DIR} ...")
    result = await ingest_documents(str(DOC_DIR))
    print(f"Done. {result.num_chunks} chunks stored in 'stripe_docs' collection.")


if __name__ == "__main__":
    asyncio.run(main())
