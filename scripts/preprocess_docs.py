"""
Convert raw JSON doc downloads → markdown files with frontmatter.

Usage:
    python scripts/preprocess_docs.py
"""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

RAW_DIR = Path(__file__).parent.parent / "data" / "raw_docs"
PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"

VALID_CATEGORIES = {"webhooks", "payments", "api", "refunds", "config"}


def html_to_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    # Promote headings
    for level in range(1, 7):
        for h in soup.find_all(f"h{level}"):
            h.replace_with(f"\n{'#' * level} {h.get_text(strip=True)}\n")

    # Code blocks
    for pre in soup.find_all("pre"):
        code = pre.get_text()
        pre.replace_with(f"\n```\n{code}\n```\n")

    # Links
    for a in soup.find_all("a", href=True):
        a.replace_with(f"[{a.get_text(strip=True)}]({a['href']})")

    main = soup.find("main") or soup.find("article") or soup.body
    text = main.get_text(separator="\n") if main else soup.get_text(separator="\n")

    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def process_file(path: Path) -> Path | None:
    data = json.loads(path.read_text())
    category = data.get("category", "")
    if category not in VALID_CATEGORIES:
        print(f"  SKIP {path.name}: unknown category '{category}'")
        return None

    markdown = html_to_markdown(data["html"])
    if len(markdown) < 200:
        print(f"  SKIP {path.name}: content too short")
        return None

    stem = path.stem  # e.g. "webhooks-signatures"
    out_path = PROCESSED_DIR / f"{stem}.md"
    frontmatter = (
        f"---\n"
        f"source_url: {data['url']}\n"
        f"source_title: {data['title']}\n"
        f"doc_category: {category}\n"
        f"---\n\n"
    )
    out_path.write_text(frontmatter + markdown)
    return out_path


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    raw_files = list(RAW_DIR.glob("*.json"))
    if not raw_files:
        print(f"No JSON files found in {RAW_DIR}. Run download_stripe_docs.py first.")
        return

    saved = []
    for path in sorted(raw_files):
        result = process_file(path)
        if result:
            saved.append(result)
            print(f"  → {result.name}")

    print(f"\nProcessed {len(saved)} files → {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
