"""
Download Stripe documentation pages as markdown.

Stripe officially supports appending `.md` to any docs URL to return
clean markdown designed for LLM consumption.

Usage:
    cd /path/to/project
    pip install httpx
    python scripts/download_stripe_docs.py
"""

import time
from pathlib import Path

import httpx

RAW_DIR = Path(__file__).parent.parent / "data" / "raw_docs"

# Target pages by category — prioritise troubleshooting-heavy pages.
STRIPE_PAGES: list[dict] = [
    # Webhooks
    {"url": "https://docs.stripe.com/webhooks", "category": "webhooks"},
    {"url": "https://docs.stripe.com/webhooks/signature", "category": "webhooks"},
    {"url": "https://docs.stripe.com/webhooks/process-undelivered-events", "category": "webhooks"},
    {"url": "https://docs.stripe.com/webhooks/handle-irrecoverable-events", "category": "webhooks"},
    {"url": "https://docs.stripe.com/webhooks/quickstart", "category": "webhooks"},
    {"url": "https://docs.stripe.com/event-destinations", "category": "webhooks"},
    {"url": "https://docs.stripe.com/api/events/types", "category": "webhooks"},
    {"url": "https://docs.stripe.com/billing/subscriptions/webhooks", "category": "webhooks"},
    {"url": "https://docs.stripe.com/testing", "category": "webhooks"},
    # API / Auth
    {"url": "https://docs.stripe.com/api/errors", "category": "api"},
    {"url": "https://docs.stripe.com/error-handling", "category": "api"},
    {"url": "https://docs.stripe.com/error-low-level", "category": "api"},
    {"url": "https://docs.stripe.com/keys", "category": "api"},
    {"url": "https://docs.stripe.com/api/versioning", "category": "api"},
    {"url": "https://docs.stripe.com/upgrades", "category": "api"},
    {"url": "https://docs.stripe.com/api", "category": "api"},
    {"url": "https://docs.stripe.com/security/guide", "category": "api"},
    # Payments
    {"url": "https://docs.stripe.com/declines", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/payment-methods", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/quickstart", "category": "payments"},
    {"url": "https://docs.stripe.com/checkout/fulfillment", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/checkout", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/cards/overview", "category": "payments"},
    {"url": "https://docs.stripe.com/payments/subscriptions", "category": "payments"},
    # Refunds & Disputes
    {"url": "https://docs.stripe.com/refunds", "category": "refunds"},
    {"url": "https://docs.stripe.com/disputes", "category": "refunds"},
    {"url": "https://docs.stripe.com/radar/reviews", "category": "refunds"},
    {"url": "https://docs.stripe.com/payouts", "category": "refunds"},
    # Account & Config
    {"url": "https://docs.stripe.com/get-started/account/teams", "category": "config"},
    {"url": "https://docs.stripe.com/security", "category": "config"},
    {"url": "https://docs.stripe.com/sdks", "category": "config"},
]

MIN_CONTENT_CHARS = 200
RATE_LIMIT_SECONDS = 1.0


def fetch_md(client: httpx.Client, url: str) -> str | None:
    """Fetch clean markdown by appending .md to the URL."""
    md_url = url.rstrip("/") + ".md"
    try:
        r = client.get(md_url, follow_redirects=True, timeout=20)
        r.raise_for_status()
        content = r.text.strip()
        if len(content) >= MIN_CONTENT_CHARS:
            return content
        print(f"  WARN: {md_url} returned only {len(content)} chars")
    except Exception as exc:
        print(f"  ERROR .md fetch {url}: {exc}")
    return None


def fetch_jina(client: httpx.Client, url: str) -> str | None:
    """Fallback: use r.jina.ai/ prefix to get markdown."""
    jina_url = "https://r.jina.ai/" + url.lstrip("https://")
    try:
        r = client.get(jina_url, follow_redirects=True, timeout=30)
        r.raise_for_status()
        content = r.text.strip()
        if len(content) >= MIN_CONTENT_CHARS:
            return content
        print(f"  WARN: jina {url} returned only {len(content)} chars")
    except Exception as exc:
        print(f"  ERROR jina fetch {url}: {exc}")
    return None


def url_to_slug(url: str) -> str:
    """Convert URL to a safe filename slug."""
    path = url.replace("https://docs.stripe.com/", "").strip("/")
    return path.replace("/", "-") or "index"


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    headers = {"User-Agent": "DevSupport-Copilot-Demo/1.0 (LLM RAG pipeline)"}

    saved = []
    failed = []

    with httpx.Client(headers=headers) as client:
        for i, page in enumerate(STRIPE_PAGES):
            url = page["url"]
            category = page["category"]
            slug = url_to_slug(url)
            out_path = RAW_DIR / f"{category}-{slug}.md"

            print(f"[{i+1}/{len(STRIPE_PAGES)}] {url}")

            content = fetch_md(client, url)
            if content is None:
                print(f"  → fallback jina.ai")
                content = fetch_jina(client, url)

            if content is None:
                print(f"  SKIP {url}: both methods failed")
                failed.append(url)
            else:
                # Prepend minimal frontmatter so preprocess.py knows the source
                raw = f"<!-- source_url: {url} doc_category: {category} -->\n{content}"
                out_path.write_text(raw, encoding="utf-8")
                saved.append(out_path.name)
                print(f"  → {out_path.name} ({len(content)} chars)")

            if i < len(STRIPE_PAGES) - 1:
                time.sleep(RATE_LIMIT_SECONDS)

    print(f"\nSaved {len(saved)} pages → {RAW_DIR}")
    if failed:
        print(f"Failed ({len(failed)}): {failed}")


if __name__ == "__main__":
    main()
