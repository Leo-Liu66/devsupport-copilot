"""
Convert raw markdown downloads → processed markdown files with YAML frontmatter.

Cleaning pipeline:
  Standard files:
    1. Remove fenced code blocks for non-Python languages
    2. Deduplicate repeated ## sections (keep Python version)
    3. Remove ### sub-sections naming a non-Python language
    4. Replace template placeholders and example Stripe keys
  Large files (>50KB raw body):
    Whitelist approach — keep only headings, tables, prose, and
    fenced Python/bash code blocks. All bare code is dropped.

Usage:
    python scripts/preprocess_docs.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw_docs"
PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"

VALID_CATEGORIES = {"webhooks", "payments", "api", "refunds", "config"}

LARGE_FILE_THRESHOLD = 50_000  # bytes of raw body text

# ---------- metadata ----------
META_RE = re.compile(
    r"^<!--\s*source_url:\s*(\S+)\s+doc_category:\s*(\S+)\s*-->",
)

# ---------- fenced code block removal ----------
_NON_PYTHON_BLOCK_RE = re.compile(
    r"```(?:ruby|php|java(?:script)?|typescript|node(?:js)?|go|dotnet|csharp|net|c#)\b[^\n]*\n.*?```",
    re.IGNORECASE | re.DOTALL,
)
_NON_PYTHON_H4_RE = re.compile(
    r"\n####\s+(?:Ruby|PHP|Java(?:Script)?|TypeScript|Node(?:\.js)?|Go|\.NET|C#)\s*\n",
    re.IGNORECASE,
)

# ---------- ### sub-section heading with explicit language name ----------
_NON_PYTHON_LANG_NAMES = {
    "node", "node.js", "ruby", "php", "java", "javascript",
    "typescript", "go", ".net", "c#", "dotnet",
}

# ---------- placeholders ----------
_PLACEHOLDER_RE = re.compile(r"<<[A-Z_]+>>")
_STRIPE_KEY_RE = re.compile(
    r"\b(sk_test_|pk_test_|rk_test_)[A-Za-z0-9]{10,}\b"
)


# ===================================================================
# Standard cleaning (small/medium files)
# ===================================================================

def remove_fenced_non_python(body: str) -> str:
    """Remove ```language ... ``` blocks and orphaned #### headings."""
    body = _NON_PYTHON_BLOCK_RE.sub("", body)
    body = _NON_PYTHON_H4_RE.sub("\n", body)
    return body


def deduplicate_heading_sections(body: str) -> str:
    """When the same ## heading appears N times (one per language tab),
    keep only the version whose body mentions 'Python'; drop the rest."""
    lines = body.split("\n")

    h2_positions: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            h2_positions.append((i, line.strip()))

    if not h2_positions:
        return body

    sections: list[tuple[int, int, str]] = []
    for idx, (pos, heading) in enumerate(h2_positions):
        end = h2_positions[idx + 1][0] if idx + 1 < len(h2_positions) else len(lines)
        sections.append((pos, end, heading))

    groups: dict[str, list[tuple[int, int, str]]] = defaultdict(list)
    for sec in sections:
        groups[sec[2]].append(sec)

    # Language keywords used to detect non-Python-only sections
    non_python_markers = {
        "ruby", "php", "java", "node.js", ".net", "go library", "go ",
        "stripe::stripeerror", "stripeexception", "stripe.key",
        "rescue", "nil", "stripe.error",
    }

    remove_ranges: list[tuple[int, int]] = []
    for heading, group in groups.items():
        if len(group) > 1:
            # Duplicate headings: keep the Python version
            python_idx = None
            for i, (start, end, _) in enumerate(group):
                chunk = "\n".join(lines[start:end]).lower()
                if "python" in chunk:
                    python_idx = i
                    break
            keep = python_idx if python_idx is not None else 0
            for i, (start, end, _) in enumerate(group):
                if i != keep:
                    remove_ranges.append((start, end))
        else:
            # Unique heading: remove if it's exclusively about a non-Python language
            start, end, _ = group[0]
            chunk = "\n".join(lines[start:end]).lower()
            has_non_python = any(m in chunk for m in non_python_markers)
            has_python = "python" in chunk
            if has_non_python and not has_python:
                remove_ranges.append((start, end))

    if not remove_ranges:
        return body

    remove_ranges.sort()
    keep_lines: list[str] = []
    prev_end = 0
    for start, end in remove_ranges:
        keep_lines.extend(lines[prev_end:start])
        prev_end = end
    keep_lines.extend(lines[prev_end:])
    return "\n".join(keep_lines)


def remove_non_python_subsections(body: str) -> str:
    """Remove ### sub-sections whose heading names a non-Python language."""
    lines = body.split("\n")
    result: list[str] = []
    skip_until_next_heading = False

    for line in lines:
        is_heading = line.startswith("## ") or line.startswith("### ")

        if is_heading:
            heading_lower = line.lower()
            has_non_python_lang = any(
                f" {lang}" in heading_lower or heading_lower.endswith(f" {lang}")
                for lang in _NON_PYTHON_LANG_NAMES
            )
            if line.startswith("#### "):
                pkg_mgr = line.strip().lower().replace("#### ", "")
                if pkg_mgr in {"npm", "composer", "maven", "gradle", "nuget",
                               "bundler", "dotnet", "terminal"}:
                    has_non_python_lang = True

            if has_non_python_lang and "python" not in heading_lower:
                skip_until_next_heading = True
                continue
            else:
                skip_until_next_heading = False

        if skip_until_next_heading:
            continue

        result.append(line)

    return "\n".join(result)


# ===================================================================
# Large-file cleaning (>50KB) — whitelist approach
# ===================================================================

def _is_prose_line(line: str) -> bool:
    """Return True if line is prose, markdown formatting, or blank."""
    stripped = line.strip()
    if not stripped:
        return True
    # JS-style // comments and escaped \# code comments are NOT prose
    if stripped.startswith("//") or stripped.startswith("\\#"):
        return False
    # Markdown headings
    if stripped.startswith("#"):
        return True
    # Blockquotes, tables, images, bold/italic markers
    if stripped[0] in ">|![":
        return True
    # List items
    if stripped.startswith("- ") or stripped.startswith("* "):
        return True
    # Numbered list
    if re.match(r"^\d+\.\s", stripped):
        return True
    # Links on their own line
    if stripped.startswith("[") and "](" in stripped:
        return True
    # Enough natural-language words (≥4 alphabetic tokens, no code endings)
    words = stripped.split()
    alpha = sum(1 for w in words if any(c.isalpha() for c in w))
    if alpha >= 4 and stripped[-1] not in "{};)":
        return True
    return False


def clean_large_file(body: str) -> str:
    """Whitelist strategy for large files.

    Keep:
      - All prose / markdown formatting lines
      - Fenced code blocks tagged as python or bash (or untagged)
      - Tables (lines starting with |)
    Drop:
      - Fenced code blocks for non-Python languages
      - All bare (unfenced) code
    """
    lines = body.split("\n")
    result: list[str] = []
    in_fence = False
    keep_fence = False

    # Languages to KEEP in fenced blocks
    keep_langs = {"python", "py", "bash", "sh", "shell", "console", "text", ""}

    for line in lines:
        stripped = line.strip()

        # Handle code fence boundaries
        if stripped.startswith("```"):
            if not in_fence:
                # Opening fence — check language
                lang = stripped[3:].strip().split()[0].lower() if len(stripped) > 3 else ""
                keep_fence = lang in keep_langs
                in_fence = True
                if keep_fence:
                    result.append(line)
            else:
                # Closing fence
                if keep_fence:
                    result.append(line)
                in_fence = False
                keep_fence = False
            continue

        if in_fence:
            if keep_fence:
                result.append(line)
            continue

        # Outside fences: keep prose, drop bare code
        if _is_prose_line(line):
            result.append(line)
        # else: bare code line → drop

    return "\n".join(result)


# ===================================================================
# Common utilities
# ===================================================================

def remove_placeholders(body: str) -> str:
    """Replace template tokens and example Stripe keys."""
    body = _PLACEHOLDER_RE.sub("[YOUR_VALUE]", body)
    body = _STRIPE_KEY_RE.sub(r"\1[REDACTED]", body)
    return body


def collapse_blank_lines(body: str) -> str:
    """Collapse 3+ consecutive blank lines into 2."""
    return re.sub(r"\n{3,}", "\n\n", body)


def extract_h1(content: str) -> str:
    """Return the first H1 heading from markdown, or empty string."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


# ===================================================================
# File processing
# ===================================================================

def process_file(path: Path) -> tuple[Path | None, str]:
    """Process a single raw markdown file. Returns (output_path, status_msg)."""
    raw = path.read_text(encoding="utf-8")
    first_line, _, body = raw.partition("\n")

    match = META_RE.match(first_line.strip())
    if not match:
        return None, f"SKIP {path.name}: missing metadata comment"

    source_url, doc_category = match.group(1), match.group(2)

    if doc_category not in VALID_CATEGORIES:
        return None, f"SKIP {path.name}: unknown category '{doc_category}'"

    body = body.strip()
    if len(body) < 200:
        return None, f"SKIP {path.name}: content too short ({len(body)} chars)"

    original_len = len(body)

    # Always apply structural cleaning first
    body = remove_fenced_non_python(body)
    body = deduplicate_heading_sections(body)
    body = remove_non_python_subsections(body)

    if len(body.encode("utf-8")) > LARGE_FILE_THRESHOLD:
        # Still large after structural cleaning → whitelist bare code
        body = clean_large_file(body)
        strategy = "large"
    else:
        strategy = "standard"

    body = remove_placeholders(body)
    body = collapse_blank_lines(body)

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

    reduction = (1 - len(body) / original_len) * 100 if original_len else 0
    return out_path, f"→ {path.name} [{strategy}] ({reduction:.0f}% reduced)"


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    raw_files = sorted(RAW_DIR.glob("*.md"))

    if not raw_files:
        print(f"No .md files found in {RAW_DIR}. Run download_stripe_docs.py first.")
        return

    saved = []
    for path in raw_files:
        result, msg = process_file(path)
        print(f"  {msg}")
        if result:
            saved.append(result)

    print(f"\nProcessed {len(saved)} / {len(raw_files)} files → {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
