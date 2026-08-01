"""Convert the existing search-service plain-text cache into markdown files
that qmd can index.

Source of truth:
  kp-docs/askwri-kps/cache/texts/*.json  - one file per doc, has a `full_text`
                                    field (plain text already extracted from
                                    the PDF by the search-service's own
                                    pipeline).
  kp-docs/askwri-kps/kp_metadata.csv - per-doc metadata (title, authors, url,
                                    ...) keyed by `file_path`
                                    (== "{doc_id}.pdf"). Preferred over
                                    documents.csv: its "Published title" column
                                    is complete (documents.csv's "Article
                                    Title" is a placeholder/blank for 34/169
                                    docs).

Output:
  kp-docs/markdown/cache-text/{doc_id}.md - YAML frontmatter (metadata) +
                                    full_text body, one file per doc.

This is a *fast, no-GPU* path to get a working qmd collection so retrieval can
be exercised end-to-end before spending time on higher-fidelity PDF -> markdown
conversion (e.g. via Marker). If retrieval quality against this plain-text
corpus is insufficient, swap/augment the collection with Marker output later
(see scripts/convert_pdfs_marker.py, planned).

Usage:
  python3 scripts/cache_to_markdown.py
  python3 scripts/cache_to_markdown.py --limit 5   # smoke test on a few docs
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KP_DOCS_DIR = REPO_ROOT / "kp-docs"
DEFAULT_KPS_DIR = DEFAULT_KP_DOCS_DIR / "askwri-kps"
DEFAULT_TEXTS_DIR = DEFAULT_KPS_DIR / "cache" / "texts"
DEFAULT_METADATA_CSV = DEFAULT_KPS_DIR / "kp_metadata.csv"
DEFAULT_OUTPUT_DIR = DEFAULT_KP_DOCS_DIR / "markdown" / "cache-text"

# kp_metadata.csv column -> frontmatter key (order preserved in output)
METADATA_FIELD_MAP = {
    "Published title": "title",
    "Authors": "authors",
    "Date published": "date_published",
    "Article Type": "article_type",
    "Sub-tag": "sub_tag",
    "WRI Office affiliation (primary)": "wri_primary_office",
    "Program(s)": "wri_programs",
    "Language(s)": "language",
    "URL": "url",
    "DOI": "doi",
    "summary": "summary",
}


def load_metadata_csv(csv_path: Path) -> dict[str, dict[str, Any]]:
    """Return {file_path: metadata_dict} keyed by the PDF filename."""
    by_file_path: dict[str, dict[str, Any]] = {}
    with csv_path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            by_file_path[row["file_path"]] = row
    return by_file_path


def yaml_escape(value: Any) -> str:
    """Minimal YAML scalar quoting: quote if it needs it, escape embedded quotes."""
    s = str(value).replace("\r\n", " ").replace("\n", " ").strip()
    if s == "":
        return '""'
    needs_quoting = any(ch in s for ch in [":", "#", '"', "'", "\n"]) or s[0] in "-?[]{}&*!|>%@`"
    if needs_quoting:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def build_frontmatter(doc_id: str, source_pdf: str, char_count: int, meta: dict[str, Any]) -> str:
    lines = ["---"]
    lines.append(f"doc_id: {yaml_escape(doc_id)}")
    lines.append(f"source_pdf: {yaml_escape(source_pdf)}")
    lines.append("extraction_method: cache-plaintext")
    lines.append(f"char_count: {char_count}")
    for src_key, out_key in METADATA_FIELD_MAP.items():
        if src_key in meta and meta[src_key] not in (None, ""):
            lines.append(f"{out_key}: {yaml_escape(meta[src_key])}")
    lines.append("---")
    return "\n".join(lines)


def convert_one(text_json_path: Path, doc_meta_by_file_path: dict[str, dict[str, Any]], output_dir: Path) -> tuple[str, int]:
    data = json.loads(text_json_path.read_text(encoding="utf-8"))
    doc_id = data["doc_id"]
    full_text = data.get("full_text", "")
    char_count = data.get("char_count", len(full_text))
    source_pdf = f"kp-docs/askwri-kps/{doc_id}.pdf"

    meta = doc_meta_by_file_path.get(f"{doc_id}.pdf", {})
    title = meta.get("Published title") or doc_id

    frontmatter = build_frontmatter(doc_id, source_pdf, char_count, meta)
    body = f"# {title}\n\n{full_text}\n"
    out_path = output_dir / f"{doc_id}.md"
    out_path.write_text(f"{frontmatter}\n\n{body}", encoding="utf-8")
    return doc_id, char_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--texts-dir", type=Path, default=DEFAULT_TEXTS_DIR, help="Dir of cache/texts/*.json")
    parser.add_argument("--metadata-csv", type=Path, default=DEFAULT_METADATA_CSV, help="kp_metadata.csv path")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Where to write .md files")
    parser.add_argument("--limit", type=int, default=None, help="Only convert the first N docs (smoke test)")
    args = parser.parse_args()

    if not args.texts_dir.is_dir():
        sys.exit(f"texts dir not found: {args.texts_dir}")
    if not args.metadata_csv.is_file():
        sys.exit(f"kp_metadata.csv not found: {args.metadata_csv}")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading metadata from {args.metadata_csv} ...")
    doc_meta_by_file_path = load_metadata_csv(args.metadata_csv)
    print(f"  {len(doc_meta_by_file_path)} metadata rows")

    text_files = sorted(args.texts_dir.glob("*.json"))
    if args.limit:
        text_files = text_files[: args.limit]
    print(f"Converting {len(text_files)} cached text files -> {args.output_dir} ...")

    converted = 0
    total_chars = 0
    missing_meta = []
    for text_json_path in text_files:
        try:
            doc_id, char_count = convert_one(text_json_path, doc_meta_by_file_path, args.output_dir)
        except Exception as e:
            print(f"  ! failed on {text_json_path.name}: {e}", file=sys.stderr)
            continue
        if f"{doc_id}.pdf" not in doc_meta_by_file_path:
            missing_meta.append(doc_id)
        converted += 1
        total_chars += char_count

    print(f"Done: {converted}/{len(text_files)} converted, {total_chars:,} total chars")
    if missing_meta:
        print(f"  {len(missing_meta)} docs had no metadata row: {missing_meta[:5]}{'...' if len(missing_meta) > 5 else ''}")


if __name__ == "__main__":
    main()
