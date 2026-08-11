# AskWRI Eval Review

Tools and datasets for building and reviewing evaluation sets for AskWRI's
two query modes:

- **Cite mode** - given a question, retrieve the correct source document(s).
- **Answer mode** - given a question, retrieve the correct passages *and*
  synthesize a correct answer.

## Directory layout

- `kp-docs/` - the underlying corpus documents (PDFs plus generated
  markdown).
- `notebooks/` - marimo notebook(s) for human review of eval sets (e.g.
  `review_eval_answers_citemode.py`, a `molabel`-based tool for confirming
  whether each `expected_document_ids` entry is actually a correct match).
- `review-output/` - saved output from the review notebook(s) above.
- `source_evalsets/` - the original ("generation 1") golden datasets:
  `cite-golden-dataset.json` and `answer-golden-dataset.json`. Read-only
  reference data, covering the original 169-document corpus.
- `evalsets/` - newer eval sets, built from the manual doc-review process
  described below (e.g. `evalset_cite_02.json`, `evalset_answer_02.json`).
  This is where newly generated eval sets will be added.
- `eval-generation-notes/` - working notes from manual document review,
  tracked in git for diffability. Includes:
  - `docreview_*.md` - human-authored notes per document reviewed (query +
    draft answer), the raw input to the eval-generation process below.
  - `documents-list-207_*.txt` - mapping between each document's UUID
    (`document_id`), stable slug (`external_id`), title, and language, for
    the full 207-document cross-lingual corpus (151 en, 15 es, 4 pt, 37 zh).
  - `issuelog_*.md` - known corpus issues (e.g. suspected duplicate/twin
    documents across languages) to check or validate later.

## Eval-generation process (generation 2+)

The corpus grew from 169 documents to a 207-document cross-lingual corpus
(English, Chinese, Spanish, Portuguese). New eval sets are being built as
follows:

1. A human reviewer works through the corpus one document (or
   cross-lingual twin-pair) at a time, recording notes in
   `eval-generation-notes/docreview_*.md`:
   - The document's `document_id` (UUID) and `external_id` (slug).
   - A high-level English-language query whose expected answer is that
     document (queries are always written in English, regardless of the
     source document's language).
   - A draft answer to that query, as bullet points, based on the source
     document's content.
   - No chunk/passage-level excerpts are captured at this stage.
2. An LLM (Claude Sonnet 5) converts each doc-review entry into a matching
   pair of test cases - one in `evalsets/evalset_cite_NN.json` and one in
   `evalsets/evalset_answer_NN.json` - sharing the same `id` and
   `question`, so the two files stay 1:1 aligned per doc-review entry. This
   includes:
   - Resolving `external_id`/`document_id` for the source document, using
     `documents-list-207_*.txt`.
   - **Writing the `canonical_answer` and `key_facts` fields for Answer
     mode.** These are synthesized by the LLM from the reviewer's bullet
     notes (reformatted into prose / verbatim-ish bullets). **This content
     has not yet been human-reviewed or fact-checked against the source
     document**, and should be treated as a first draft pending review.
   - `difficulty` and `query_type` are partially LLM-inferred.
3. A human reviews the generated test cases (starting with the Cite-mode
   file, since it's simpler) and edits directly as needed - e.g. simplifying
   `description`/`note` fields - before moving on to review the Answer-mode
   file.

### Schema notes (generation 2 vs. generation 1)

Relative to the `source_evalsets/*-golden-dataset.json` schema, the new
`evalsets/` files:

- Replace a single `expected_document_ids` list (of `external_id` strings)
  with **two parallel arrays**, `expected_external_ids` and
  `expected_document_ids` (now a list of UUIDs) - same index refers to the
  same document, so they can be used together or independently. 
- Add `source_document_id` and `source_language` - the UUID and language of
  the specific document the reviewer was reading when the query was
  drafted (useful for traceability).
- Keep the `task_description` field in **Cite mode** test cases (only),
  kept for consistency with generation 1's Cite schema but not populated. 
- Leave `expected_passages` empty in Answer mode test cases - chunk/passage
  -level ground truth is not captured during this round of doc review.

**Caveat:** `canonical_answer`/`key_facts` values in `evalsets/evalset_answer_*.json`
files are LLM-drafted (Claude Sonnet 5) from human notes, not
human-authored or human-verified. Treat them as provisional until reviewed.
