"""
One-shot LLM synthesis of resolutions for the 31 seed tickets.

Reads:  data/seed_tickets.json
Writes: data/seed_tickets_with_resolutions.json

Idempotent — skips if output file already exists.
Estimated cost: ~$0.01 at gpt-4o-mini rates.
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "backend"))

from openai import OpenAI

from app.config import settings

INPUT_PATH = ROOT / "data" / "seed_tickets.json"
OUTPUT_PATH = ROOT / "data" / "seed_tickets_with_resolutions.json"

RESOLUTION_PROMPT = """You are a Stripe support engineer writing concise resolution notes.
Given a support ticket, write a 2-4 sentence resolution describing how this type of issue is typically resolved.
Be specific and actionable. Reference Stripe features or documentation where relevant.
Do NOT add preamble — return only the resolution text.

Ticket subject: {subject}
Ticket category: {category}
Ticket severity: {severity}
Ticket body:
{body}"""


def synthesize_resolution(client: OpenAI, ticket: dict) -> str:
    prompt = RESOLUTION_PROMPT.format(
        subject=ticket["subject"],
        category=ticket["expected_category"],
        severity=ticket["expected_severity"],
        body=ticket["body"],
    )
    response = client.chat.completions.create(
        model=settings.llm_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()


def main() -> None:
    if OUTPUT_PATH.exists():
        print(f"Output already exists at {OUTPUT_PATH}. Skipping synthesis.")
        return

    tickets = json.loads(INPUT_PATH.read_text())
    client = OpenAI(api_key=settings.openai_api_key)

    enriched = []
    for i, ticket in enumerate(tickets, 1):
        print(f"  [{i}/{len(tickets)}] {ticket['id']}: {ticket['subject'][:60]}...")
        resolution = synthesize_resolution(client, ticket)
        enriched.append({**ticket, "resolution": resolution})

    OUTPUT_PATH.write_text(json.dumps(enriched, indent=2))
    print(f"\nWrote {len(enriched)} tickets with resolutions to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
