"""Convert Postgres document text into markdown for documents whose source PDF
lives in S3/MinIO (s3_key = "documents/<name>.pdf") rather than under a local
kp-docs/CN-KPs-PDF or kp-docs/ES-KPs-PDF folder.

Companion to scripts/db_text_to_markdown.py, which is scoped to the CN/ES
corpus and finds source PDFs by scanning those two local folders. This script
covers the complementary case: documents ingested through the normal
worker/S3 pipeline (mistral-parsed, document_texts.full_text already present
in Postgres) that db_text_to_markdown.py's local-PDF-folder scan can never
find, because there is no local PDF for them to match against.

Selection: every documents+document_texts row with parse_backend='mistral'
whose external_id is NOT already covered by a local PDF under --pdf-dirs.

Source of truth: Postgres `documents` + `document_texts` (via `docker exec
askwri-pg psql`), same as db_text_to_markdown.py.

Usage:
  python3 scripts/db_text_to_markdown_s3_docs.py                # write new files
  python3 scripts/db_text_to_markdown_s3_docs.py --dry-run
  python3 scripts/db_text_to_markdown_s3_docs.py --overwrite
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_text_to_markdown import (  # noqa: E402
    build_frontmatter,
    find_local_pdf_ids,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KP_DOCS_DIR = REPO_ROOT / "kp-docs"
DEFAULT_PDF_DIRS = [
    DEFAULT_KP_DOCS_DIR / "CN-KPs-PDF",
    DEFAULT_KP_DOCS_DIR / "ES-KPs-PDF",
]
DEFAULT_OUTPUT_DIR = DEFAULT_KP_DOCS_DIR / "markdown"

DB_QUERY = """
SELECT json_agg(row_to_json(t)) FROM (
  SELECT
    d.external_id, d.title, d.title_en, d.authors, d.doi, d.url,
    d.date_published, d.year_published, d.publication_title,
    d.article_type, d.wri_primary_office, d.language, d.languages,
    d.status, d.s3_key,
    dt.full_text, dt.char_count, dt.parse_backend, dt.parse_model
  FROM documents d
  JOIN document_texts dt ON dt.document_id = d.id
  WHERE dt.parse_backend = 'mistral'
) t;
""".strip()


def fetch_mistral_docs(container: str, db: str, user: str) -> list[dict[str, Any]]:
    cmd = ["docker", "exec", container, "psql", "-U", user, "-d", db, "-t", "-A", "-c", DB_QUERY]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        sys.exit(f"docker exec psql failed (exit {result.returncode}):\n{result.stderr}")
    raw = result.stdout.strip()
    if not raw:
        return []
    return json.loads(raw)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pdf-dirs", type=Path, nargs="+", default=DEFAULT_PDF_DIRS,
                         help="Local CN/ES PDF directories to EXCLUDE (already handled by db_text_to_markdown.py)")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Where to write .md files")
    parser.add_argument("--container", default="askwri-pg", help="Postgres docker container name")
    parser.add_argument("--db", default="qa", help="Postgres database name")
    parser.add_argument("--user", default="askwri", help="Postgres user")
    parser.add_argument("--overwrite", action="store_true", help="Re-write .md files that already exist")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write any files")
    args = parser.parse_args()

    local_pdf_ids = find_local_pdf_ids(args.pdf_dirs)
    print(f"Excluding {len(local_pdf_ids)} docs already covered by local CN/ES PDF folders")

    print(f"Fetching mistral-parsed docs from {args.container}/{args.db} ...")
    db_docs = fetch_mistral_docs(args.container, args.db, args.user)
    print(f"  {len(db_docs)} mistral-parsed rows in DB")

    targets = [d for d in db_docs if d["external_id"] not in local_pdf_ids]
    print(f"  {len(targets)} are S3/MinIO-sourced (no local CN/ES PDF match)")

    args.output_dir.mkdir(parents=True, exist_ok=True)

    written, skipped_exists = [], []
    for doc in sorted(targets, key=lambda d: d["external_id"]):
        doc_id = doc["external_id"]
        out_path = args.output_dir / f"{doc_id}.md"
        if out_path.exists() and not args.overwrite:
            skipped_exists.append(doc_id)
            continue
        source_pdf = doc.get("s3_key") or f"documents/{doc_id}.pdf"
        frontmatter = build_frontmatter(doc, source_pdf)
        full_text = doc.get("full_text") or ""
        body = f"{full_text}\n"
        if args.dry_run:
            print(f"  [dry-run] would write {out_path}")
            written.append(doc_id)
            continue
        out_path.write_text(f"{frontmatter}\n\n{body}", encoding="utf-8")
        written.append(doc_id)

    print()
    print(f"Done: {len(written)} written, {len(skipped_exists)} skipped (already exist)")
    if skipped_exists:
        print(f"  already exist (use --overwrite to re-write): {skipped_exists}")


if __name__ == "__main__":
    main()
