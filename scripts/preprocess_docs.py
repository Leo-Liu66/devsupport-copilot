"""
Convert raw markdown downloads → processed markdown files with YAML frontmatter.

Usage:
    python scripts/preprocess_docs.py
"""

import re
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw_docs"
PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"

VALID_CATEGORIES = {"webhooks", "payments", "api", "refunds", "config"}

# Regex to parse the metadata comment written by download_stripe_docs.py
META_RE = re.compile(
    r"^<!--\s*source_url:\s*(\S+)\s+doc_category:\s*(\S+)\s*-->",
)


def extract_h1(content: str) -> str:
    """Return the first H1 heading from markdown, or empty string."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def process_file(path: Path) -> Path | None:
    raw = path.read_text(encoding="utf-8")
    first_line, _, body = raw.partition("\n")

    match = META_RE.match(first_line.strip())
    if not match:
        print(f"  SKIP {path.name}: missing metadata comment")
        return None

    source_url, doc_category = match.group(1), match.group(2)

    if doc_category not in VALID_CATEGORIES:
        print(f"  SKIP {path.name}: unknown category '{doc_category}'")
        return None

    body = body.strip()
    if len(body) < 200:
        print(f"  SKIP {path.name}: content too short ({len(body)} chars)")
        return None

    source_title = extract_h1(body) or path.stem.replace("-", " ").title()

    out_path = PROCESSED_DIR / path.name
    frontmatter = (
        f"---\n"
        f"source_url: {source_url}\n"
        f"source_title: {source_title}\n"
        f"doc_category: {doc_category}\n"
        f"---\n\n"
    )
    out_path.write_text(frontmatter + body, encoding="utf-8")
    return out_path


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    raw_files = sorted(RAW_DIR.glob("*.md"))

    if not raw_files:
        print(f"No .md files found in {RAW_DIR}. Run download_stripe_docs.py first.")
        return

    saved = []
    for path in raw_files:
        result = process_file(path)
        if result:
            saved.append(result)
            print(f"  → {result.name}")
        else:
            print(f"  skipped {path.name}")

    print(f"\nProcessed {len(saved)} / {len(raw_files)} files → {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
