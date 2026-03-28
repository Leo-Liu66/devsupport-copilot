"""
Download Stripe documentation pages as raw HTML.

Usage:
    cd /path/to/project
    pip install httpx beautifulsoup4
    python scripts/download_stripe_docs.py
"""

import asyncio
import json
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

RAW_DIR = Path(__file__).parent.parent / "data" / "raw_docs"

STRIPE_PAGES: list[dict] = [
    # Webhooks
    {"url": "https://docs.stripe.com/webhooks", "category": "webhooks"},
    {"url": "https://docs.stripe.com/webhooks/signatures", "category": "webhooks"},
    {"url": "https://docs.stripe.com/webhooks/best-practices", "category": "webhooks"},
    # Payments
    {"url": "https://docs.stripe.com/payments/payment-intents", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/accept-a-payment", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/payment-methods", "category": "payments"},
    # API / Auth
    {"url": "https://docs.stripe.com/keys", "category": "api"},
    {"url": "https://docs.stripe.com/api/errors", "category": "api"},
    {"url": "https://docs.stripe.com/api", "category": "api"},
    # Refunds & Disputes
    {"url": "https://docs.stripe.com/refunds", "category": "refunds"},
    {"url": "https://docs.stripe.com/disputes", "category": "refunds"},
    {"url": "https://docs.stripe.com/disputes/responding", "category": "refunds"},
    # Account & Config
    {"url": "https://docs.stripe.com/account", "category": "config"},
    {"url": "https://docs.stripe.com/dashboard/basics", "category": "config"},
    {"url": "https://docs.stripe.com/development/get-started", "category": "config"},
]


def extract_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body
    return main.get_text(separator="\n", strip=True) if main else ""


async def download_page(client: httpx.AsyncClient, page: dict) -> dict | None:
    try:
        r = await client.get(page["url"], follow_redirects=True, timeout=15)
        r.raise_for_status()
        title_tag = BeautifulSoup(r.text, "html.parser").find("title")
        title = title_tag.get_text(strip=True) if title_tag else page["url"]
        return {
            "url": str(r.url),
            "category": page["category"],
            "title": title.replace(" | Stripe Documentation", "").strip(),
            "html": r.text,
        }
    except Exception as exc:
        print(f"SKIP {page['url']}: {exc}")
        return None


async def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": "Mozilla/5.0 DevSupport-Copilot-Demo/1.0"}
    async with httpx.AsyncClient(headers=headers) as client:
        tasks = [download_page(client, p) for p in STRIPE_PAGES]
        results = await asyncio.gather(*tasks)

    saved = []
    for result in results:
        if result is None:
            continue
        slug = result["url"].rstrip("/").split("/")[-1] or "index"
        path = RAW_DIR / f"{result['category']}-{slug}.json"
        path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
        saved.append(path.name)
        print(f"  saved {path.name}")

    print(f"\nDownloaded {len(saved)} pages → {RAW_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
