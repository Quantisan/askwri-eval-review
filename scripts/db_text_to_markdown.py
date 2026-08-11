"""Convert already-extracted Postgres document text into markdown files that
qmd can index, for the newer CN/ES knowledge-product PDFs.

Unlike scripts/cache_to_markdown.py (which wraps raw pypdf plaintext for the
legacy 169-doc corpus), this script's source text is already real markdown:
document_texts.full_text for the CN/ES batch was produced by Mistral OCR and
already contains headings, bold, bullet lists, pipe-tables, and
"![img-N.jpeg](img-N.jpeg)" image placeholders. So there is no plaintext
cleanup step here - we just wrap full_text with a YAML frontmatter block.

IMPORTANT: this script never triggers any PDF parsing/extraction/OCR. It only
reads text that is *already* sitting in document_texts (parse_backend =
'mistral'). PDFs in kp-docs/CN-KPs-PDF/ or kp-docs/ES-KPs-PDF/ that don't yet
have a matching document_texts row are reported as skipped, not processed.

Source of truth:
  Postgres `documents` + `document_texts` tables (via `docker exec askwri-pg
  psql`), filtered to parse_backend = 'mistral' and cross-referenced against
  local PDF filenames under kp-docs/CN-KPs-PDF/ and kp-docs/ES-KPs-PDF/.

Output:
  kp-docs/markdown/{external_id}.md - YAML frontmatter (metadata) + full_text
  body, one file per doc, same flat layout/naming as the legacy corpus.

Usage:
  python3 scripts/db_text_to_markdown.py                # write new files
  python3 scripts/db_text_to_markdown.py --dry-run       # preview only
  python3 scripts/db_text_to_markdown.py --overwrite     # re-write existing
  python3 scripts/db_text_to_markdown.py --container my-pg --db qa --user me
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KP_DOCS_DIR = REPO_ROOT / "kp-docs"
DEFAULT_PDF_DIRS = [
    DEFAULT_KP_DOCS_DIR / "CN-KPs-PDF",
    DEFAULT_KP_DOCS_DIR / "ES-KPs-PDF",
]
DEFAULT_OUTPUT_DIR = DEFAULT_KP_DOCS_DIR / "markdown"

# documents/document_texts column -> frontmatter key (order preserved in output)
FRONTMATTER_FIELD_MAP = {
    "title": "title",
    "title_en": "title_en",
    "authors": "authors",
    "date_published": "date_published",
    "year_published": "year_published",
    "publication_title": "publication_title",
    "article_type": "article_type",
    "wri_primary_office": "wri_primary_office",
    "language": "language",
    "doi": "doi",
    "url": "url",
    "status": "status",
}

DB_QUERY = """
SELECT json_agg(row_to_json(t)) FROM (
  SELECT
    d.external_id, d.title, d.title_en, d.authors, d.doi, d.url,
    d.date_published, d.year_published, d.publication_title,
    d.article_type, d.wri_primary_office, d.language, d.languages,
    d.status,
    dt.full_text, dt.char_count, dt.parse_backend, dt.parse_model
  FROM documents d
  JOIN document_texts dt ON dt.document_id = d.id
  WHERE dt.parse_backend = 'mistral'
) t;
""".strip()


def fetch_mistral_docs(container: str, db: str, user: str) -> list[dict[str, Any]]:
    """Fetch all documents+document_texts rows with parse_backend='mistral'
    via `docker exec ... psql`, returned as a JSON array over stdout."""
    cmd = [
        "docker", "exec", container,
        "psql", "-U", user, "-d", db, "-t", "-A", "-c", DB_QUERY,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        sys.exit(f"docker exec psql failed (exit {result.returncode}):\n{result.stderr}")
    raw = result.stdout.strip()
    if not raw or raw == "":
        return []
    return json.loads(raw)


def find_local_pdf_ids(pdf_dirs: list[Path]) -> dict[str, Path]:
    """Return {external_id: pdf_dir} for every *.pdf found under pdf_dirs."""
    by_id: dict[str, Path] = {}
    for pdf_dir in pdf_dirs:
        if not pdf_dir.is_dir():
            print(f"  ! PDF dir not found, skipping: {pdf_dir}", file=sys.stderr)
            continue
        for pdf_path in sorted(pdf_dir.glob("*.pdf")):
            by_id[pdf_path.stem] = pdf_dir
    return by_id


def yaml_escape(value: Any) -> str:
    """Minimal YAML scalar quoting: quote if it needs it, escape embedded quotes."""
    s = str(value).replace("\r\n", " ").replace("\n", " ").strip()
    if s == "":
        return '""'
    needs_quoting = any(ch in s for ch in [":", "#", '"', "'", "\n"]) or s[0] in "-?[]{}&*!|>%@`"
    if needs_quoting:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def build_frontmatter(doc: dict[str, Any], source_pdf: str) -> str:
    lines = ["---"]
    lines.append(f"doc_id: {yaml_escape(doc['external_id'])}")
    lines.append(f"source_pdf: {yaml_escape(source_pdf)}")
    lines.append("extraction_method: postgres-full-text")
    lines.append(f"parse_backend: {yaml_escape(doc.get('parse_backend'))}")
    if doc.get("parse_model"):
        lines.append(f"parse_model: {yaml_escape(doc['parse_model'])}")
    lines.append(f"char_count: {doc.get('char_count', 0)}")
    for src_key, out_key in FRONTMATTER_FIELD_MAP.items():
        value = doc.get(src_key)
        if value not in (None, "") and not (src_key == "title_en" and value == doc.get("title")):
            lines.append(f"{out_key}: {yaml_escape(value)}")
    lines.append("---")
    return "\n".join(lines)


def convert_one(doc: dict[str, Any], pdf_dir: Path, output_dir: Path) -> tuple[str, int]:
    doc_id = doc["external_id"]
    full_text = doc.get("full_text") or ""
    char_count = doc.get("char_count") or len(full_text)
    source_pdf = f"kp-docs/{pdf_dir.name}/{doc_id}.pdf"

    frontmatter = build_frontmatter(doc, source_pdf)
    body = f"{full_text}\n"
    out_path = output_dir / f"{doc_id}.md"
    out_path.write_text(f"{frontmatter}\n\n{body}", encoding="utf-8")
    return doc_id, char_count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pdf-dirs", type=Path, nargs="+", default=DEFAULT_PDF_DIRS,
                         help="Local PDF directories to scope conversion to")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Where to write .md files")
    parser.add_argument("--container", default="askwri-pg", help="Postgres docker container name")
    parser.add_argument("--db", default="qa", help="Postgres database name")
    parser.add_argument("--user", default="askwri", help="Postgres user")
    parser.add_argument("--overwrite", action="store_true", help="Re-write .md files that already exist")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write any files")
    parser.add_argument("--min-chars", type=int, default=1000,
                         help="Flag docs with full_text shorter than this many chars")
    args = parser.parse_args()

    print(f"Scanning local PDFs under: {[str(p) for p in args.pdf_dirs]} ...")
    local_pdf_ids = find_local_pdf_ids(args.pdf_dirs)
    print(f"  {len(local_pdf_ids)} local PDFs found")

    print(f"Fetching mistral-parsed docs from {args.container}/{args.db} ...")
    db_docs = fetch_mistral_docs(args.container, args.db, args.user)
    print(f"  {len(db_docs)} mistral-parsed rows in DB")
    db_docs_by_id = {d["external_id"]: d for d in db_docs}

    target_ids = sorted(local_pdf_ids.keys())
    matched_ids = [i for i in target_ids if i in db_docs_by_id]
    missing_ids = [i for i in target_ids if i not in db_docs_by_id]

    args.output_dir.mkdir(parents=True, exist_ok=True)

    written = []
    skipped_exists = []
    flagged_short = []
    for doc_id in matched_ids:
        out_path = args.output_dir / f"{doc_id}.md"
        if out_path.exists() and not args.overwrite:
            skipped_exists.append(doc_id)
            continue
        doc = db_docs_by_id[doc_id]
        char_count = doc.get("char_count") or 0
        if char_count < args.min_chars:
            flagged_short.append((doc_id, char_count))
        if args.dry_run:
            print(f"  [dry-run] would write {out_path}")
            written.append(doc_id)
            continue
        pdf_dir = local_pdf_ids[doc_id]
        wrote_id, chars = convert_one(doc, pdf_dir, args.output_dir)
        written.append(wrote_id)

    print()
    print(f"Done: {len(written)} written, {len(skipped_exists)} skipped (already exist), "
          f"{len(missing_ids)} skipped (no DB text yet)")
    if skipped_exists:
        print(f"  already exist (use --overwrite to re-write): {skipped_exists}")
    if missing_ids:
        print(f"  no document_texts row with parse_backend='mistral' yet ({len(missing_ids)}):")
        for i in missing_ids:
            print(f"    - {i}")
    if flagged_short:
        print(f"  ! {len(flagged_short)} docs with full_text shorter than {args.min_chars} chars:")
        for doc_id, count in flagged_short:
            print(f"    - {doc_id}: {count} chars")


if __name__ == "__main__":
    main()
