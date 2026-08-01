# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "molabel",
#     "mohtml",
#     "pandas",
#     "pyyaml==6.0.3",
# ]
# ///

import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # CITE-mode eval review

    Review the golden-set queries for AskWRI CITE (Citation) mode. For
    each query, step through its `expected_document_ids` and confirm
    whether each document is actually a correct match, using the
    `molabel` widget.

    Data sources (read-only):

    - `source_evalsets/golden-dataset.json` — queries + expected
      document ids
    - `kp-docs/markdown/{doc_id}.md` — per-document context
      (title, authors, summary, etc.) via YAML frontmatter
    """)
    return


@app.cell
def _():
    import copy
    import datetime
    import json
    import re
    from pathlib import Path

    import yaml
    import marimo as mo
    from molabel import SimpleLabel
    from mohtml import div, p, span, a


    return SimpleLabel, a, copy, datetime, div, json, mo, p, re, span, yaml


@app.cell
def _(mo):
    REPO_ROOT = mo.notebook_dir().parent

    # Everything under source_evalsets/ is read-only reference data, tracked as plain files.
    EVALSET_DIR = REPO_ROOT / "source_evalsets"

    # TODO this will be selected by the user in the future from available evalsets in EVALSET_DIR
    sel_evalset = "golden-dataset.json"
    SELECTED_EVALSET_PATH = EVALSET_DIR / sel_evalset

    EVALSET_NAME = SELECTED_EVALSET_PATH.stem
    MARKDOWN_DIR = REPO_ROOT / "kp-docs" / "markdown"
    REVIEW_OUTPUT_DIR = REPO_ROOT / "review-output"

    return (
        EVALSET_DIR,
        EVALSET_NAME,
        MARKDOWN_DIR,
        REPO_ROOT,
        REVIEW_OUTPUT_DIR,
        SELECTED_EVALSET_PATH,
        sel_evalset,
    )


@app.cell
def _(EVALSET_DIR):
    for _entry in sorted(EVALSET_DIR.iterdir()):
        print(_entry.name)
    return


@app.cell
def _(SELECTED_EVALSET_PATH, json):
    evalset = json.loads(SELECTED_EVALSET_PATH.read_text())
    test_cases = evalset["test_cases"]
    #test_cases[:1]
    return evalset, test_cases


@app.cell
def _(mo, test_cases):
    query_dropdown = mo.ui.dropdown(
        options={tc["question"]: tc for tc in test_cases},
        value=test_cases[0]["question"],
        label="Select a query to review",
    )
    query_dropdown
    return (query_dropdown,)


@app.cell(hide_code=True)
def _(selected_query):
    print(f"""

    Investigate why this field is here and what is it's purpose. 

    **task_description:** {selected_query["task_description"]}

    """)
    return


@app.cell(hide_code=True)
def _(mo, query_dropdown):
    selected_query = query_dropdown.value

    mo.md(f"""

    **Selected Query:** "{selected_query["question"]}"


    **id:** `{selected_query["id"]}`&nbsp;&nbsp;|&nbsp;&nbsp;
    **query_type:** `{selected_query["query_type"]}`&nbsp;&nbsp;|&nbsp;&nbsp;
    **difficulty:** `{selected_query["difficulty"]}`&nbsp;&nbsp;


    {f"**note:** {selected_query['note']}" if selected_query.get("note") else ""}
    """)
    return (selected_query,)


@app.cell(hide_code=True)
def _(SimpleLabel, doc_contexts, mo, render_molabel_card):
    widget = mo.ui.anywidget(SimpleLabel(examples=doc_contexts, render=render_molabel_card))
    widget

    return (widget,)


@app.cell(hide_code=True)
def _(mo):
    reviewer_name_input = mo.ui.text(label="Reviewer name", value="reviewer", placeholder="reviewer")
    save_button = mo.ui.run_button(label="Save")
    mo.vstack([
        mo.hstack(
        [reviewer_name_input, save_button], justify="start", gap=1),
        mo.md("*Providing your name is optional -- it helps us track reviews and reach out if we have any questions.*")
    ])


    return reviewer_name_input, save_button


@app.cell(hide_code=True)
def _(
    EVALSET_NAME,
    REPO_ROOT,
    REVIEW_OUTPUT_DIR,
    doc_contexts,
    json,
    mo,
    re,
    reviewer_name_input,
    save_button,
    saved_annot_paths,
    selected_query,
    widget,
):
    mo.stop(not save_button.value, mo.md("**Saved Results**: None. <br>_Click the button above to save your review for this query._"))

    _reviewer = re.sub(r"[^\w\-]+", "_", reviewer_name_input.value.strip()) or "reviewer"
    _annotations = widget.get_annotations()
    _records = [
        {
            "doc_id": doc_contexts[a["index"]]["doc_id"],
            "label": a["_label"],
            "notes": a["_notes"],
            "timestamp": a["_timestamp"],
        }
        for a in _annotations
    ]

    REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    _annotations_path = REVIEW_OUTPUT_DIR / f"annot-{EVALSET_NAME}-{selected_query['id']}-by-{_reviewer}.json"
    _annotations_path.write_text(json.dumps(
        {
            "query_id": selected_query["id"],
            "question": selected_query["question"],
            "task_description": selected_query["task_description"],
            "reviewer": _reviewer,
            "reviewed_documents": _records,
        },
        indent=2,
    ))
    saved_annot_paths.add(_annotations_path)

    mo.md(f"""
    Saved!

    Annotations file:\n`{_annotations_path.relative_to(REPO_ROOT)}`
    """)

    return


@app.cell(hide_code=True)
def _(
    div,
    json,
    mo,
    re,
    save_button,
    saved_annot_paths,
    sel_evalset,
    test_cases,
):
    _ = save_button.value  # dependency: refresh whenever Save is clicked

    _rejected_by_query = {}
    for _path in sorted(saved_annot_paths):
        _data = json.loads(_path.read_text())
        _qid = _data["query_id"]
        _rejected = {d["doc_id"] for d in _data["reviewed_documents"] if d["label"] == "no"}
        _rejected_by_query.setdefault(_qid, set()).update(_rejected)

    _total_expected = sum(len(tc["expected_document_ids"]) for tc in test_cases)
    _total_current = sum(
        len(tc["expected_document_ids"]) - len(_rejected_by_query.get(tc["id"], set()))
        for tc in test_cases
    )
    _total_rejected = _total_expected - _total_current


    def _chip(tc):
        _n = re.match(r"q(\d+)", tc["id"]).group(1)
        _done = tc["id"] in _rejected_by_query
        return div(
            _n, " ", "\u2705" if _done else "\u2b1c",
            title=tc["question"],
            style=(
                "display:inline-flex; align-items:center; justify-content:center; gap:0.3rem; "
                "padding:0.4rem 0.75rem; border-radius:8px; "
                "font-size:1rem; font-weight:600; "
                + ("background:#d4edda; color:#155724;" if _done else "background:#f1f3f5; color:#495057;")
            ),
        )


    _checklist_html = str(div(
        *[_chip(tc) for tc in test_cases],
        style="display:grid; grid-template-columns:repeat(10, auto); gap:0.4rem; margin-top:0.75rem;",
    ))

    mo.vstack([
        mo.hstack(
            [
                mo.stat(value=_total_expected, label="Total expected matches (all queries)", bordered=True),
                mo.stat(
                    value=_total_current,
                    label="Total current matches (after review)",
                    caption=f"{_total_rejected} rejected" if _total_rejected else "No rejections yet",
                    direction="decrease" if _total_current < _total_expected else None,
                    target_direction="increase",
                    bordered=True,
                ),
            ],
            gap=2,
        ),
        mo.md(f"Queries reviewed in this eval set **'{sel_evalset}'**"),
        mo.Html(_checklist_html),
    ])

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Export
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    submit_button = mo.ui.run_button(label="Submit / Export")
    mo.vstack([
        submit_button,
        mo.md("*Creates an updated eval set reflecting all your annotations.*"),
    ])

    return (submit_button,)


@app.cell(hide_code=True)
def _(
    EVALSET_NAME,
    REPO_ROOT,
    REVIEW_OUTPUT_DIR,
    build_updated_evalset,
    datetime,
    evalset,
    json,
    mo,
    saved_annot_paths,
    submit_button,
    test_cases,
):
    mo.stop(not submit_button.value, mo.md("_Click the button above to export the aggregated evalset._"))
    mo.stop(not saved_annot_paths, mo.md("**No saved reviews found.** Save at least one query's annotations before exporting."))

    _rejected_by_query = {}
    for _path in sorted(saved_annot_paths):
        _data = json.loads(_path.read_text())
        _qid = _data["query_id"]
        _rejected = {d["doc_id"] for d in _data["reviewed_documents"] if d["label"] == "no"}
        _rejected_by_query.setdefault(_qid, set()).update(_rejected)

    _updated_evalset = build_updated_evalset(evalset, _rejected_by_query)

    _timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _evalset_path = REVIEW_OUTPUT_DIR / f"{EVALSET_NAME}-{_timestamp}.json"
    _evalset_path.write_text(json.dumps(_updated_evalset, indent=2))

    mo.md(f"""
    Exported!

    Queries covered: {len(_rejected_by_query)} / {len(test_cases)}

    Updated evalset:\n`{_evalset_path.relative_to(REPO_ROOT)}`
    """)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utilities
    """)
    return


@app.cell
def _():
    saved_annot_paths = set()
    return (saved_annot_paths,)


@app.cell
def _(MARKDOWN_DIR, selected_query, yaml):
    def _parse_frontmatter(doc_id):
        text = (MARKDOWN_DIR / f"{doc_id}.md").read_text()
        _, frontmatter, _ = text.split("---", 2)
        return yaml.safe_load(frontmatter)


    doc_contexts = [
        {
            "doc_id": doc_id,
            "title": (meta := _parse_frontmatter(doc_id)).get("title", doc_id),
            "authors": meta.get("authors", ""),
            "date_published": meta.get("date_published", ""),
            "article_type": meta.get("article_type", ""),
            "sub_tag": meta.get("sub_tag", ""),
            "url": meta.get("url", ""),
            "summary": meta.get("summary", ""),
        }
        for doc_id in selected_query["expected_document_ids"]
    ]

    return (doc_contexts,)


@app.cell
def _(a, div, p, span):
    _badge_style = (
        "background:#f1f3f5; color:#495057; border-radius:999px; "
        "padding:0.15rem 0.6rem; font-size:0.75rem; font-weight:500;"
    )


    def render_doc_info(example):
        return str(
            div(
                p(example["title"],
                  style="font-size:1.25rem; font-weight:600; color:#1a1a1a; margin:0 0 0.25rem 0; line-height:1.3;"),
                p(example["authors"],
                  style="font-size:0.85rem; color:#6c757d; margin:0 0 0.6rem 0;"),
                p(f"Date Published: {example['date_published']}",
                  style="font-size:0.85rem; color:#495057; margin:0 0 0.5rem 0;"),
                div(
                    span(example["article_type"], style=_badge_style),
                    span(example["sub_tag"], style=_badge_style),
                    style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:0.6rem;",
                ),
                p(example["summary"],
                  style="font-size:0.95rem; color:#333; line-height:1.55; margin:0 0 0.75rem 0; max-width:65ch;"),
                a("\U0001F4C4 View document", href=example["url"], target="_blank",
                  style=("display:inline-block; background:#e9ecef; color:#495057; "
                         "text-decoration:none; font-size:0.85rem; font-weight:500; "
                         "padding:0.4rem 0.9rem; border-radius:6px;")),
                klass="molabel-doc-context",
            )
        )


    return (render_doc_info,)


@app.cell
def _(div, p, render_doc_info):
    def render_molabel_card(example):
        return str(
            div(
                render_doc_info(example),
                p("Is this document a correct result for the query?",
                  style="font-size:0.95rem; font-weight:600; color:#1a1a1a; margin:0.75rem 0 0 0; padding-top:0.5rem; border-top:1px solid #e9ecef;"),
            )
        )


    return (render_molabel_card,)


@app.cell
def _(copy):
    def build_updated_evalset(source_evalset, rejected_by_query):
        """rejected_by_query: {query_id: set(rejected_doc_ids)}"""
        updated_evalset = copy.deepcopy(source_evalset)
        for tc in updated_evalset["test_cases"]:
            rejected_doc_ids = rejected_by_query.get(tc["id"])
            if rejected_doc_ids:
                tc["expected_document_ids"] = [
                    doc_id
                    for doc_id in tc["expected_document_ids"]
                    if doc_id not in rejected_doc_ids
                ]
        return updated_evalset


    return (build_updated_evalset,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
