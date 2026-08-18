# Query Expansion Plan — Cite Mode

Captures the plan agreed on for step 4 ("Expand expected matches") of the
eval-generation process described in the top-level `README.md`, focused on
Cite mode.

This plan continues and corrects the WIP in 
expected_doc_expansion_plan_citemode_20260812.md


## background

### Corpus

As before, but the corpus has changed. there are now 200 documents. Status
report: 
* I now have a corpus with 206 documents with updated metadata and IDs. 
* (There are 5 docs with "withdrawn" stastus. These are in the document list that you sent me, but I won't use them in any evalsets.)
* I have document content (in markdown format) for all of this corpus but one. 
* The one KP for which I'm missing document text is 2026_fortaleciendo-sinergias-electromovilidad-calidad-aire_XXXX

So evals will use up to 200 documents:
  en: 148
  zh: 34
  es: 14
  pt: 3
  id: 1

I was surprised to see one in Indonesian:
2025_panduan-pelaksanaan-inventarisasi-pohon-perkotaan_4324 . This is not a
new doc; it was previously labeled as en-lang, instead of id-lang. I
confirmed that the markdown content is in Bahasa. We should write
an eval query that targets this one.

### qmd infrastructure

Done: 
* script to generate markdown files from the document full text.
  These markdown files are placed in `kp-docs/markdown/` (flat directory).
* `.qmd/index.yml` to include all markdown files.
* `qmd update` — re-indexed, found all expected files.
* Verified via `qmd status`.

Follow this template to invoke qmd: 
`mise exec -- npx qmd vsearch "example query" -n 10 --format json --no-rerank 2>&1 | head -5`


## Cite Mode evalset files

See note from before (`expected_doc_expansion_plan_citemode_20260812.md`).
In particular the key evalset file we are developing is: 
- `evalsets/evalset_cite_02.json` (v4.2) - updated version reflects corpus
  update in: `evalset_repair_and_expansion_citemode_20260817.md`


## Session working agreement (added 2026-08-13)

**One question block at a time.** When picking up a new round of query
expansion, agree on scope with the human first — a single cluster/topic/
query_type to work on next — before doing any research (catalog scanning,
`qmd vsearch` sanity checks, etc.) or drafting a multi-item plan. Do not
survey the whole "Parked / open items" backlog, propose several new test
cases at once, and fire off a multi-part question block unprompted — that
gets ahead of the human and is harder to steer. Concretely:

1. Ask what to work on next (or confirm a specific item the human already
   named).
2. Do the research/search for *that one thing* only.
3. Review results together in chat (per "Per-query workflow" below).
4. Apply, commit if asked, *then* ask what's next.

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
  - skip the below-threshold sweep we were doing earlier unless returned
    candidates is very few. Then let's discuss. 
4. **Apply**: add approved documents to `expected_external_ids` /
   `expected_document_ids` in `evalset_cite_02.json`.


## open items

- ~~review current queries in Cite-01 and Cite-02 to ensure no new expected_document* needed to be
  added to existing queries. Since new documents are now available, we can
  focus our inspection on those new documents
  (evalset_repair_and_expansion_citemode_20260817.md)~~ **Done 2026-08-18** — see
  "2026-08-18: survey of new-refresh documents against existing queries" below.
- review cite_01 (Anne's queries) to reflect the new corpus (new IDs, etc) —
  **partially done**: q4 (`climate_brazil`) got 2 new documents with resolved
  `expected_document_ids` (2026-08-18, see below), but the file's other 10
  test cases still have empty-string `expected_document_ids` placeholders —
  the full UUID-reconciliation pass (per `evalset_cite_01.json`'s own
  `description` field) is still open.
- Add new queries to the eval set to
   - ~~for coverage on the new id-lang doc.~~ **Done 2026-08-18** — see
     "2026-08-18: new query for the id-lang doc" below.
   - for better coverage over the `query_type` -- discuss together and
     decide. We don't need an even distribution, this is a subjective call. 

### 2026-08-18: new query for the id-lang doc

Added `d16_urban-tree-inventory-discovery` to `evalset_cite_02.json`,
targeting `2025_panduan-pelaksanaan-inventarisasi-pohon-perkotaan_4324`
(`document_id: ed7cc7fe-de63-4015-ba74-fe0cd84fe05f`) — the doc flagged in
the background section above as previously mislabeled `en`-lang instead of
`id` (Bahasa Indonesia). Content: a WRI Indonesia guidebook on urban tree
inventory methodology (field measurement + GIS), piloted in Jakarta,
Denpasar, Medan, Pekanbaru, and Makassar.

- Question: "What has WRI published on urban tree inventory methods?"
- `query_type: topic_discovery`, single expected doc. Checked via 3 `qmd
  vsearch` phrasings (with/without "Indonesian cities", broader "urban
  forestry/tree canopy" wording) — this is a genuine single-doc topic in the
  current corpus; every phrasing gives one strong hit (0.73–0.76) then a
  sharp drop to generic-urban noise (~0.6, nothing else actually about
  trees). Geography constraint doesn't change the result set, so classified
  as plain `topic_discovery` rather than `geography_constrained`, per the
  `d3` (container ports) precedent.
- No version bump this round (per human instruction) — `evalset_cite_02.json`
  stays at 4.3 with 16 test cases (`d1`–`d16`).

### 2026-08-18: survey of new-refresh documents against existing queries

The 2026-08-17 corpus refresh (`evalset_repair_and_expansion_citemode_20260817.md`)
added 12 non-standard-id ("S3-pipeline") documents, 11 of which are
genuinely new content (the 12th, `26_tech_esb-adoption_version-10`, is a
same-content rename of an already-known doc). Checked all 11 against every
existing Cite-01/Cite-02 query via `qmd vsearch` + reading the actual
document content (not just titles/scores — a few high-scoring hits turned
out to be false positives on inspection).

**Added** (4 documents, to 3 test cases):
- `evalset_cite_02.json` `d12` (`climate-hazards-heat-resilience-discovery`):
  `mapping-scenarios-and-estimating-the-potential-for-heat-resilient-infrastructure-in-cities-technical-note`,
  `modeling-hyperlocal-heat-exposure-with-open-source-data` (both were
  explicitly named in d12's own prior `note` as "not yet indexed, could not
  be evaluated" — now indexed and confirmed on-topic), and
  `wri_brasil-root_causes_2024_disaster_rs` (flood-disaster root causes in
  Brazil — climate-hazard content).
- `evalset_cite_02.json` `d15` (`flooding-risk-informal-settlements-intersection`):
  `flooding-nairobi-informal-settlements` — direct title/executive-summary
  match, top `qmd vsearch` hit (0.72).
- `evalset_cite_01.json` `q4` (`climate_brazil`):
  `bridging-national-and-local-climate-adaptation-in-brazil-india-and-indonesia`
  (top hit, 0.75) and `wri_brasil-root_causes_2024_disaster_rs` (cross-listed
  with d12 above) — both substantively about Brazil-specific climate
  adaptation/vulnerability, not tangential mentions.

**Checked and excluded** (6 documents) — high vector-similarity score but
not actually on-topic once the content was read:
- `climate-readiness-urban-transformation-wri-ross-center-prize-for-cities-cycle-2023-2024`
  and `using-flexible-funding-in-long-horizon-urban-transformation-work-...`
  both scored highest for `d11`'s Coalition for Urban Transitions query
  (0.74, 0.72) but contain **zero** mentions of "Coalition for Urban
  Transitions" anywhere — false positive on generic "urban transformation"
  phrasing, not the named partnership `d11` actually requires.
- `wri-india-nup-report` — a ~1M-char omnibus India national-urbanization-
  policy report. Scored in the top 15 for `d12`, `d15`, and `d11`'s queries,
  but climate resilience / flooding / finance are each just one of ~7
  thematic chapters — passing coverage, not primary focus (same standard as
  `d11`'s existing "excludes docs that only cite/acknowledge in passing").
- `FINAL_Working Paper_Just Transition_1905` (EV supply-chain labor
  practices, India) — scored in `d7`'s (electric buses) top 15, but is about
  automotive-manufacturing workforce/supply-chain equity broadly, not buses.
  Also checked against `d14` (Pawan Mulukutla authorship): he appears only
  in the acknowledgments, not the `authors:` field, so excluded per d14's
  own stated standard.
- `25May_Battery Aadhaar For India_Expert Note` (battery data-management
  framework) — no defensible match to any existing query; also an
  acknowledgments-only mention of Pawan Mulukutla, excluded from `d14` same
  as above.
- `assessing-urban-road-networks-using-geospatial-metrics_c` — checked
  against cite_01 `q2` (Bangalore): Bengaluru is 1 of 4 example cities in a
  cross-city methodology paper, not primary geographic focus.

No action needed for `26_tech_esb-adoption_version-10` (the rename) — same
school-bus-specific content as before, correctly still excluded from `d7`.

**Leftover, no existing-query match at all** (candidates for a possible
future net-new-`topic_discovery`-queries round, not actioned this pass):
`wri-india-nup-report`, `assessing-urban-road-networks-using-geospatial-metrics_c`,
`using-flexible-funding-in-long-horizon-urban-transformation-work-...`,
`25May_Battery Aadhaar For India_Expert Note`,
`FINAL_Working Paper_Just Transition_1905`,
`climate-readiness-urban-transformation-wri-ross-center-prize-for-cities-cycle-2023-2024`.

Version bumps: `evalset_cite_02.json` 4.2 → 4.3, `evalset_cite_01.json` 3.1 → 3.2.

The evalset currently has 15 questions across 7 query_types:
 4  topic_discovery
 3  membership
 3  binary_presence
 2  geography_constrained
 1  date_constrained
 1  topic_exclusion
 1  thematic_intersection

Here are the queries
* What has WRI published on zero-emission heavy-duty truck adoption in China?
* What research has WRI done on dockless bike-sharing in Chinese cities?
* What has WRI written about decarbonizing container port and drayage operations?
* What has WRI published on financing mechanisms for public transport?
* What has WRI published on financing mechanisms for public transport since 2022?
* Give me all the papers WRI published as part of the 'Seizing the Urban Opportunity' report series.
* What has WRI published on electric bus adoption and operations, excluding anything specific to school buses?
* Has WRI written about using surveillance technologies to increase climate resilience in cities?
* Has WRI written about urban vertical farming or rooftop agriculture in cities?
* Has WRI published research on nuclear microreactors for city-level power grids?
* What has WRI written with the Coalition for Urban Transitions?
* What has WRI published on climate hazards and heat resilience in cities?
* What has WRI published on low-cost air quality sensors and monitoring in cities?
* What has WRI published that was authored or co-authored by Pawan Mulukutla?
* What has WRI published on flooding risk in informal settlements?amanqa  [5:46 PM]

I'm thinking of reorganizing the Cite evalsets into these evalsets / files 
* 1 evalset / 1 file for the previous (Anne-written) goldenset. This is
  already the case. The current filename is Cite-01. 
* Aman's new queries --> `Cite-02`.  This is already the case. 
* A new separate one for the "weirdo" cases, such as null result (negative
  binary query_type), and queries that are targetting filters / metadata -->
  `Cite-03` (currently doesn't exist, is mixed with Cite-02). 

