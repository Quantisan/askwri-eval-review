# Query Expansion Plan — Cite Mode

Status: planning, 2026-08-12. Captures the plan agreed on for step 4 ("Expand
expected matches") of the eval-generation process described in the top-level
`README.md`, focused on Cite mode.

## Background

### qmd infrastructure (done)

The corpus grew from 169 to 195 markdown files (169 legacy + 26 new CN/ES
docs), but qmd's index and embeddings only covered the earlier set of
documents.

Fixed by:
* Obtaining a psql dump with document full text for the newly processed
  documents.
* Writing a script to generate markdown files from the document full text.
  These markdown files are placed in `kp-docs/markdown/` (flat directory).
* Updating `.qmd/index.yml` to include all markdown files.
* `qmd update` — re-indexed, found all expected files.
* `qmd embed -f` — full re-embed using `Qwen/Qwen3-Embedding-0.6B-GGUF`
  (Vulkan GPU backend).
* Verified via `qmd status`.
* Sanity-checked with `qmd vsearch` runs against known-answer queries from
  `evalset_cite_02.json` — correct expected documents consistently ranked
  in the top 2 results, including correct cross-lingual retrieval (English
  query surfacing a Chinese-titled source document).

### Embedding model choice

AskWRI production uses `cohere-embed-v4` (via AWS Bedrock). qmd is
configured to use `Qwen/Qwen3-Embedding-0.6B` (GGUF, local, via
llama.cpp). Comparison:

| | Cohere embed-v4.0 | Qwen3-Embedding-0.6B |
|---|---|---|
| Dimensions | 256/512/1024/1536 | 32-1024 (MRL) |
| Context length | 128k tokens | 32k tokens |
| Modality | text + images + mixed | text only |
| Languages | 100+ | 100+ |
| MTEB Multilingual (mean task) | v3.0: 61.12 (v4.0 score not verified) | 64.33 |
| Deployment | proprietary API (Bedrock) | local, open weight |

Decision: keep Qwen3-Embedding-0.6B. Using a different embedding model than
the system under evaluation is arguably a feature, not a bug, for building
ground truth — it avoids circularity (ground truth ends up independent of
whatever cohere-embed-v4 happens to retrieve or miss).

## Key insight: Cite-mode queries are currently Answer-mode-shaped

The 16 existing test cases in `evalsets/evalset_cite_02.json` are all
precise fact-lookup queries (e.g. "What is the projected market penetration
rate of new energy heavy-duty trucks in China through 2035?"). This is a
better fit for **Answer mode** (retrieve + synthesize a specific answer)
than for **Cite mode**.

The actual Cite-mode use case is closer to a junior researcher building an
annotated bibliography: "What's already there on this topic?" / "Has WRI
written anything about X?" / "What Cities KPs discuss X?" — literature
discovery, not fact retrieval.

This was empirically confirmed: running `qmd vsearch` with a discovery-style
query ("Which WRI knowledge products discuss new energy heavy-duty trucks in
China?") against the same corpus as the original fact-lookup query produced
a meaningfully broader, differently-ranked candidate set — several
documents that correctly score low for the fact-lookup query (they don't
contain the specific 2035 projection figure) score respectably for the
discovery query (they do substantively discuss the topic).

## New Cite-mode query taxonomy

Single tier, five `query_type` values. `topic_discovery` is reserved for the
*general* case (topic only, no place/time filter); `geography_constrained`
and `date_constrained` are discovery queries that add a specific filter
dimension on top of the topic. This distinction was added 2026-08-12 mid-way
through cluster review — see "Parked / open items" for retroactive
relabeling of the first two clusters.

| query_type | Description | Example | Relevance standard | Expected volume |
|---|---|---|---|---|
| `topic_discovery` | "What's already there on X?" — topic only, no place/time filter | "What has WRI published on financing mechanisms for public transport?" | Topically substantive — doc meaningfully discusses the topic | Many (cluster-sized, e.g. 4-8+) — **majority of new queries** |
| `geography_constrained` | Discovery query scoped to a specific place | "What has WRI published on zero-emission heavy-duty truck adoption in China?" | Topically substantive + place-scoped — docs on-topic but set elsewhere must be excluded | Many (cluster-sized) |
| `date_constrained` | Discovery query scoped to a time window (e.g. "since YYYY") | "What has WRI published on electric buses since 2022?" (illustrative — no vetted example yet) | Topically substantive + date-scoped — docs on-topic but outside the window must be excluded | TBD — watching for a well-populated (multi-year) topic as clusters are reviewed |
| `binary_presence` | "Is there anything about X?" | "Has WRI Cities written about bike-sharing's climate impact in China?" | Same as topic_discovery, but framed as existence-check | Few — mostly positive (topic exists), with a smaller number of deliberate negative cases (topic plausibly relevant but absent from this corpus, expecting an empty result) |
| `fact_lookup` | Precise fact/figure retrieval — actually better suited to Answer mode | (existing 16 queries) | Answer-bearing — doc contains the specific fact/figure | Few (1-2) — **retained for coverage** (users may not distinguish Cite from Answer mode) but no new additions planned this round |

## Versioning decision

- `evalsets/evalset_cite_02.json` — **frozen as-is**. Existing 16
  `fact_lookup` queries kept for Answer-style-query-in-Cite-mode coverage.
- `evalsets/evalset_cite_03.json` — **new file**, where `topic_discovery`
  and `binary_presence` queries are developed.
- `evalsets/evalset_answer_*.json` — untouched. New Cite-only query types
  (`topic_discovery`, `binary_presence`) do not get Answer-mode
  counterparts (no single synthesizable answer for "what's already there on
  X?"). Each such test case includes a `note` explaining why there's no
  Answer-mode pair, mirroring the existing pattern for fact_lookup queries
  with no drafted answer yet.

## Schema notes for evalset_cite_03.json

- `source_document_id` / `source_language`: kept as the original reviewed
  document when a new query is a *variation* on that review session (i.e.
  the human was inspecting that document when the related original query
  was drafted). Left empty for genuinely new topics not tied to any single
  prior review session.
- `expected_external_ids` / `expected_document_ids`: same parallel-array
  structure as `evalset_cite_02.json`.
- New queries are Cite-only; no `retrieval_ground_truth`/Answer-mode
  counterpart is created.

## Per-query workflow

1. **Search**: run `qmd vsearch "<verbatim question>" -n 10 --format json
   --no-rerank`. qmd auto-expands the verbatim query into vector-search
   variations and a HyDE-style hypothetical document internally — no need
   to hand-write query variants.
2. **Gather candidates**: take the ranked JSON output, exclude docs already
   in `expected_*` (if any), map filenames to `external_id`/`document_id`
   via `eval-generation-notes/documents-list-207_*.txt`.
3. **Review**: done together in chat (not the marimo notebook) — titles,
   snippets, and translations (zh/es/pt) are reviewed live, applying the
   relevance standard appropriate to the query's type (topically-substantive
   for `topic_discovery`/`binary_presence`, answer-bearing for
   `fact_lookup`). No fixed score threshold — a sanity check showed a flat
   0.68 cutoff (used in a prior project) would pull in topically-adjacent
   but non-answer-bearing docs for fact_lookup queries; discovery-type
   queries use top-K human review instead of a threshold, since the "right"
   number of relevant docs varies a lot by topic breadth.
   - **Below-threshold sweep (standard, not optional)**: after the initial
     top-K review, re-run with `--all --min-score 0.5` (or similar) and
     review the additional lower-scoring candidates too. Cluster 1's
     initial review (cutoff ~0.67) missed 2 directly-on-topic docs that
     scored 0.59-0.61, plus surfaced a judgment call (a multi-country doc
     with a substantive but brief China-specific passage) resolved by
     pulling the full document text via `qmd get` to check for a real
     substantive passage vs. a passing mention.
4. **Apply**: add approved documents to `expected_external_ids` /
   `expected_document_ids` in `evalset_cite_03.json`.

## Draft topic_discovery queries (4, one per existing doc-review cluster)

| Cluster | Draft query | source_document_id | source_language |
|---|---|---|---|
| Zero-emission HD trucks, China (q1-q4's doc) | "What has WRI published on zero-emission heavy-duty truck adoption in China?" | `00be4a1d-33cc-4b56-a4d5-d15af0a5cc27` | zh |
| Dockless bike-sharing, China (q5-q7's doc) | "What research has WRI done on dockless bike-sharing in Chinese cities?" | `98cc253e-8d96-4499-b67a-38baffe2f3f2` | zh |
| Yantian Port / container ports (q8-q10's doc) | "What has WRI written about decarbonizing container port and drayage operations in China?" | `e36cae4c-c6fb-441b-adf0-f43e2aec9ad9` | zh |
| Mexico public transport financing (q11-q16's docs) | "What has WRI published on financing mechanisms for public transport in Mexico?" | `987353ab-9454-473f-8f00-eb767750dd24` (or `2e5d79b9-...`, both source the same cluster) | es |

Cluster 1 is complete — see `evalset_cite_03.json` (test case
`d1_zero-emission-heavy-duty-trucks-discovery`, 11 expected docs, full
rationale in its `note` field). Clusters 2-4 pending.

## binary_presence plan

- Positive queries (topic known to exist in corpus): count TBD, expected to
  be a small set, developed after the 4 topic_discovery queries above.
- Negative queries (topic plausibly relevant to WRI Cities but absent from
  this 207-doc corpus): target ~4 across the eval set eventually. Each
  candidate topic must be verified via `qmd vsearch` (confirming
  consistently low scores across the corpus) before being locked in as an
  expected-empty-result test case. Deferred until positive queries are
  done.

## Parked / open items

- Verify the two twin-pair hypotheses confirmed during cluster 1's review
  (see `evalset_cite_03.json`'s note field: `61d7d9a2`/`d79ef747` and
  `6a5e424b`/`adafe321`) against `issuelog_20260807.md` and update that log
  from "less probable" to confirmed.
- Design negative binary_presence topics + verification pass.
