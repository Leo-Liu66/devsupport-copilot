"""
Ingest seed_tickets_with_resolutions.json into ChromaDB as 'historical_tickets'.

Run AFTER synthesize_resolutions.py.
Idempotent via collection recreation.
"""
import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from app.services.rag.ingest import ingest_historical_tickets

INPUT_PATH = ROOT / "data" / "seed_tickets_with_resolutions.json"


async def main() -> None:
    if not INPUT_PATH.exists():
        print(f"ERROR: {INPUT_PATH} not found. Run synthesize_resolutions.py first.")
        sys.exit(1)

    print(f"Ingesting historical tickets from {INPUT_PATH}...")
    result = await ingest_historical_tickets(str(INPUT_PATH))
    print(f"Done. Ingested {result} tickets into 'historical_tickets' collection.")


if __name__ == "__main__":
    asyncio.run(main())
