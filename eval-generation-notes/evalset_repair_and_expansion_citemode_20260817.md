# Evalset Repair & Expansion — Cite Mode (2026-08-17 corpus refresh)

Status: repair (steps 1-3) complete, 2026-08-17. Covers reconciling
`evalsets/evalset_cite_02.json` (v4.1 → v4.2) against the corpus refresh
described in `issuelog_20260817.md`, then handing off to a fresh session for
step 4 of the eval-generation process
(`expected_doc_expansion_plan_citemode_20260812.md`) against the *new*
documents added in this refresh.

## Why this was needed

`issuelog_20260817.md` documents a corpus refresh: 207 → 206 total documents
(new snapshot `qa_corpus_20260817`), `documents-list-207_20260807.txt`
superseded by `documents-list_20260817.txt`. Diffing every `external_id`
referenced in `evalset_cite_02.json` against the new doc-list found:

- **68 of 79** referenced external_ids kept the same `external_id` but got a
  **new `document_id` UUID** (re-ingest reassigned UUIDs even for
  unchanged/carried-forward documents; 74 counting per-test-case
  duplicates, since some docs are referenced by more than one test case).
  Only 8 referenced external_ids with legacy sequential-style suffixes
  (e.g. `_00006`, `_0070`, `_00123`) kept their original UUID:
  `2019_en-electric-bus-adoption-guide_00123`,
  `2020_acciones-federales-planeacion-urbana_0152`,
  `2020_dockless-bike-sharing_00124`,
  `2021_seizing-chinas-urban-opportunity_00015`,
  `2022_china-road-transport-decarbonization_00145`,
  `2022_impactos-economicos-pandemia-covid19-transporte-publico_0070`,
  `2024_zero-emission-trucks-guangdong_00006`,
  `2025_zero-emission-heavy-duty-trucks_00015`.
- **1** referenced external_id no longer exists in the corpus **at all** —
  not even as `withdrawn`, just gone from `documents-list_20260817.txt`
  entirely: `2021_mexico-frontrunners-creating-safe-affordable-and_6429`
  (confirmed duplicate of `..._5127`, which remains). This is unrelated to
  any of the "new to this refresh" documents discussed below — it's a
  document that *disappeared*, not one that was added.
- **2** referenced external_ids flipped to `status: withdrawn`. The corpus
  has 5 withdrawn documents total (206 = 201 `searchable` + 5 `withdrawn`,
  all still listed as rows in `documents-list_20260817.txt` — withdrawn
  just means excluded from `kp-docs/markdown/` and therefore unreachable by
  qmd), but only 2 of those 5 happen to be referenced by
  `evalset_cite_02.json`, so only those 2 needed pruning here:
  `2017_global-review-of-finance-for-sustainable-urban_8290`,
  `2018_resilient-and-affordable-housing-for-all-lessons_6969`. (The other
  3 withdrawn docs — `2020_the-economic-case-for-greening-the-global_5627`,
  `2022_toward-credible-transport-carbon-dioxide_5852`,
  `2023_electric-school-bus-us-market-study-and-buyers_5598` — were never
  referenced by this evalset, so no action was needed for them.)

Separately (not part of the pruning above, just background from
`issuelog_20260817.md`): this refresh also **added** a brand-new document,
`2026_fortaleciendo-sinergias-electromovilidad-calidad-aire_XXXX` (status
`searchable` in the new list, but with a placeholder-only markdown body —
see issuelog, "Missing text" section — do not confuse this with the
`_6429` *removed* document above, they're unrelated), and **renamed** one
existing document's external_id,
`2025_technical-note-for-a-dataset-of-electric-school_9675` →
`26_tech_esb-adoption_version-10` (same content, same
document_id/document_text, id-scheme change only). Neither of these two
new-to-this-refresh identifiers is referenced by `evalset_cite_02.json` —
expanding onto those (and the other 12 newly-surfaced
S3-hosted docs) is out of scope for this repair pass; see "Handoff to
step 4" below.

## 1. qmd re-index

```
mise exec -- npx qmd update
mise exec -- npx qmd embed
mise exec -- npx qmd status
```

`qmd update` output: `Indexed: 13 new, 0 updated, 188 unchanged, 7 removed`
— matches the issuelog's accounting exactly (12 new S3-doc markdown files +
1 metadata-only placeholder for `2026_fortaleciendo-...` = 13 new; 5
withdrawn + 2 orphaned/renamed = 7 removed).

Incremental `qmd embed` (no `-f`) was used, not a full re-embed:
`Embedded 1209 chunks from 13 documents in 3m 42s`. The 188 carried-forward
files kept their existing embeddings — total vector count went from 15,905
(pre-refresh) to 17,114 (15,905 preserved + 1,209 new). `qmd status`
confirmed 201 files indexed, 17,114 vectors embedded, no pending
embeddings after the run. `-f` was not needed.

## 2. Backup before editing

`evalsets/evalset_cite_02.json` copied as-is to
`evalsets/evalset_cite_02_bkup02.json` before any edits (plain snapshot,
not a rename/retirement like `_bkup01.json` was — the working filename
stays `evalset_cite_02.json`).

## 3. Document ID remap + pruning

Applied directly to `evalsets/evalset_cite_02.json` via a one-off script
(not committed) that:
1. Parsed `documents-list-207_20260807.txt` and `documents-list_20260817.txt`
   into `external_id → {document_id, status}` maps.
2. For every `(expected_external_ids[i], expected_document_ids[i])` pair in
   every test case, looked up the external_id in the new map:
   - Missing, or `status != searchable` → **drop** the pair (from both
     arrays).
   - Present with a different UUID → **update** `expected_document_ids[i]`.
   - Present with the same UUID → no change (the 8 legacy-suffix ids).
3. Did the same lookup for `source_document_id` (via a reverse
   old-UUID→external_id map), for test cases that have one.

### Dropped (no longer resolvable)

| Test case | external_id                                                   | Reason              |
| --------- | -------------------------------------------------------------- | ------------------- |
| `d11`     | `2018_resilient-and-affordable-housing-for-all-lessons_6969`   | withdrawn           |
| `d11`     | `2017_global-review-of-finance-for-sustainable-urban_8290`     | withdrawn           |
| `d11`     | `2021_mexico-frontrunners-creating-safe-affordable-and_6429`   | removed (duplicate) |
| `d15`     | `2018_resilient-and-affordable-housing-for-all-lessons_6969`   | withdrawn           |

`d11`: 26 → 23 expected docs. `d15`: 3 → 2 expected docs. `d15`'s `note`
updated to drop the now-stale "Kochi/Trivandrum duplicate-ingest twin"
framing (only one twin of that pair, `_5955`, remains after `_6969`'s
withdrawal — no longer a twin-pair question to track).

### source_document_id updates

| Test case | Old UUID                              | New UUID                              |
| --------- | -------------------------------------- | -------------------------------------- |
| `d3`      | `e36cae4c-c6fb-441b-adf0-f43e2aec9ad9` | `add211a7-3919-48f6-bf21-c1b55f889dfb` |
| `d4`      | `2e5d79b9-7077-43a2-bc48-3661e7d3fd36` | `76039c19-d7e5-45f3-b543-88302b6034fa` |
| `d5`      | `2e5d79b9-7077-43a2-bc48-3661e7d3fd36` | `76039c19-d7e5-45f3-b543-88302b6034fa` |

(`d1`, `d2` unchanged — their source docs happened to be in the 8-doc
legacy-suffix set whose UUID didn't change.)

### UUID remap (68 unique external_ids, some referenced by >1 test case)

| external_id | old UUID | new UUID | test cases |
|---|---|---|---|
| `2014_the-trillion-dollar-question_3289` | `dfd40e6c-4782-4160-b1ca-4dbbfd8923d3` | `3b6fb2d4-9970-407e-99b9-57dbc92bf09c` | d4 |
| `2017_connected-urban-growth-public-private_1272` | `6e3d951f-ce03-478a-adeb-dcba755abe7a` | `e6efadef-a9d8-4c6a-b9de-e2d486ed46db` | d11 |
| `2017_global-review-of-finance-for-sustainable-urban_8997` | `5a0b3d8f-492d-40b3-8fd3-73c8bfaa9643` | `b5039121-22b1-438d-95e8-e093560747ef` | d11 |
| `2017_integrating-national-policies-to-deliver-compact_5239` | `82c1a437-41bf-4155-81bb-e6629a3b321b` | `1b555d62-ff50-4b7d-8576-bee7f6cc78fa` | d11 |
| `2018_developing-prosperous-and-inclusive-cities-in_3356` | `ea0f67d4-418c-43d0-98e3-4c2111b8e088` | `dd92ba27-3deb-4fb9-b503-1369bb557f93` | d11 |
| `2018_prepared-communities-implementing-the-urban_2922` | `ec468eb4-eec2-4d60-bf68-5ae9866fc62c` | `a048729d-02bb-4a04-8fa2-a9e2782a662d` | d12 |
| `2018_resilient-and-affordable-housing-for-all-lessons_5955` | `0d9a5319-78a1-4333-94b8-55fe68b15a48` | `5db22bba-99dc-43be-8fb4-fd21ec98f4e7` | d11, d15 |
| `2019_barriers-to-adopting-electric-buses_4116` | `c6bc2a1e-cc7a-4438-a583-6f1e195b1320` | `cfe63045-b7f5-422d-a2b9-9d8ba91abf0a` | d4, d7 |
| `2019_climate-emergency-urban-opportunity_4461` | `d327889b-9615-40f4-8582-40f13764c97e` | `dfcb9c66-209a-448a-ae0a-d05bbe8b9650` | d11 |
| `2019_costs-and-emissions-appraisal-tool-for-transit_4706` | `7fdfb5e2-9a3c-4911-a577-a7520ee2d670` | `0fcfd147-dca7-415f-8b27-93f03073f224` | d7 |
| `2019_financing-electric-and-hybrid-electric-buses-10_6301` | `c90ba063-883b-4989-be8a-e140ae8eb748` | `f47b4397-15e1-4802-a9a4-26f52f34a847` | d4, d7 |
| `2019_how-to-enable-electric-bus-adoption-in-cities_4136` | `d13b6c24-d6db-493e-95a5-d4fd041c1f3a` | `32d89e5e-618d-48a7-a275-90e91f50ead8` | d7 |
| `2019_overcoming-the-operational-challenges-of-electric_2317` | `d428f0c7-cc06-4c50-b94e-df5183deed11` | `5928fa8b-0536-4454-95b9-a715e758ee74` | d7 |
| `2019_scaling-up-investment-for-sustainable-urban_2716` | `3a4f79a4-f3d9-4832-b1a1-c0862dc66836` | `0e47113a-790b-49fc-b851-787d99b59807` | d11 |
| `2019_the-evolution-of-bike-sharing-10-questions-on-the_1977` | `ab12bcae-8d37-47c2-8bdf-8b265df59961` | `aa3afd35-3fbd-40c8-af80-b1f7cd8c11ef` | d2 |
| `2019_toward-net-zero-emissions-in-the-road-transport_1735` | `afe53e4b-f8b7-42cf-9e13-e713d95429e0` | `f346f47c-03f7-436a-9ae5-a0f06b175636` | d1 |
| `2019_unlocking-the-potential-for-transformative_9741` | `504c3435-b0ff-4454-b9bd-e388edb5c92b` | `233b09da-402e-404b-9758-d23652c63d98` | d12 |
| `2020_acciones-federales-para-la-planeacion-urbana_3682` | `7bc8edfa-e5ad-4613-b9b9-f10fa8aabd23` | `cd491d2f-fe3f-4f47-a985-33d1cb45e26e` | d11 |
| `2020_housing-policies-for-sustainable-and-inclusive_3963` | `2b012351-39d3-49b7-808c-8c51c2c45779` | `78bceec7-ee2c-401f-a700-95fac0b6fbe4` | d11 |
| `2020_how-dockless-bike-sharing-changes-lives-an_2277` | `416a01af-1c79-4db1-a356-182f0577f844` | `950b35ab-743f-41de-8212-0a1f75250453` | d2 |
| `2020_impactar-tool-valuing-air-quality-health-impacts_1028` | `16019c11-c9b1-434c-b585-648c388430f8` | `dd0fe27a-531b-4c1b-8cc0-6dce1fe87823` | d7 |
| `2020_the-costs-and-benefits-appraisal-tool-for-transit_6714` | `0184c892-9912-4af7-b205-7d5337d9132f` | `ea68cada-65af-492b-b7fb-fabd8f2e49a4` | d7 |
| `2020_the-future-of-urban-mobility-the-case-for_6259` | `a572c8d6-e688-4d1d-b441-cd7b785c3293` | `c1c6eff7-7e9d-4d66-873a-c1d18fdfae1b` | d7 |
| `2021_10-questions-to-ask-about-planning-financing-and_8828` | `56edad43-9124-4874-9ac3-5ae7f6ea2870` | `ee6bc3a5-78a9-4355-9493-ea97a68907c0` | d4 |
| `2021_el-costo-de-la-expansion-urbana-en-mexico_2705` | `607b0a9b-4adc-482c-a408-d8350f103955` | `68a76968-e10a-4119-98af-f14f3f349e27` | d11 |
| `2021_el-costo-de-la-expansion-urbana-en-mexico_9471` | `4e8e07e7-f2ae-4f0c-8863-32cbd80f7332` | `4dca417f-a8fd-43c3-8ab1-38d9db116dbd` | d11 |
| `2021_medindo-mp25-com-sensores-de-baixo-custo_6821` | `fb609d32-b9a0-4d30-af42-658dce515f90` | `146b57be-4e67-4952-9957-4ccd28e45641` | d13 |
| `2021_mexico-frontrunners-adapting-to-climate-change-in_8904` | `ec0bd5db-197c-4533-b4ed-2968bfe5ca8c` | `7c980340-3d1e-42f4-a092-f45e06e4908b` | d11, d12 |
| `2021_mexico-frontrunners-creating-safe-affordable-and_5127` | `15faec69-be41-4b2d-ad99-8d43be3e5345` | `6bf845bb-fe9b-4fb8-aa5b-194ac57e483a` | d11 |
| `2021_mexico-frontrunners-sustainable-mobility-for_2332` | `f99a0200-7655-416f-8bd5-fb4415338dba` | `cfb24eb0-a4c6-481e-88c7-71fc140bfd93` | d11 |
| `2021_seizing-brazils-urban-opportunity_3268` | `4c1aba65-11e8-4954-bbc3-cb5abc92b668` | `b3becd32-259f-4fda-8f0c-1dc895773176` | d6, d11 |
| `2021_seizing-chinas-urban-opportunity_9025` | `efabf9bb-9f66-4727-a021-c497edab8f22` | `82645c0f-4b9a-41fd-81c6-99b680622adf` | d6, d11 |
| `2021_seizing-indias-urban-opportunity_1949` | `cf12c06f-51a7-421f-bfe1-191da4d6dc1c` | `3a94fabf-0587-4230-a996-52a2d2ba1e22` | d6, d11 |
| `2021_seizing-indonesias-urban-opportunity_3408` | `b848befb-8900-4465-a446-9ff58cb09c58` | `9900e40d-453f-446e-9f36-339bca5bb1e7` | d6, d11 |
| `2021_seizing-mexicos-urban-opportunity_3303` | `d640b2cb-4e88-401d-89bd-05fba70e61b3` | `f47a7fde-3219-4e75-a115-1dbb819c5335` | d6, d11 |
| `2021_seizing-south-africas-urban-opportunity_4664` | `597935f7-c542-491c-bde3-a9e3de990416` | `5123ef1c-3236-4d4d-9be1-a640f5c366c7` | d6, d11 |
| `2021_seizing-the-urban-opportunity_8690` | `dca3fd44-bfec-4d4f-9e2b-f5896491ebb2` | `3d2d04e6-b0a9-4c78-b8b7-0045a051a9f0` | d6, d11 |
| `2021_water-resilience-in-a-changing-urban-context_8364` | `693d9e5c-343c-4b47-9e1f-d818c01f4114` | `9a107830-918b-446e-b5ee-4e95f1867045` | d12 |
| `2021_zero-emission-logistic-vehicles-promotion_1319` | `64342098-ff08-4d30-840b-6ac7d0deff6e` | `721c2661-65ed-4078-bc08-e74da3743553` | d1 |
| `2022_decarbonizing-chinas-road-transport-sector_2101` | `adafe321-99f8-4ebd-8a9c-f4752459fd13` | `7eb680c2-db98-429a-b404-1d0324f05fcf` | d1 |
| `2022_impactar-tool-valuing-air-quality-health-impacts_4741` | `a3334c0d-9349-4c8e-bd7e-8d939c92cdd2` | `01829576-ced9-45a7-83d4-4cf2deb3e9e2` | d7 |
| `2022_nature-based-solutions-in-sub-saharan-africa-for_1106` | `0bcb1016-83f3-419e-95b3-d44e71b9b1a5` | `6d705c39-d2d3-4e86-9425-530dffc722e8` | d12 |
| `2022_rolling-out-electric-buses-a-guidebook-on-route_8515` | `57f1a3a5-9595-4907-82a7-d50dccb300f0` | `20e4cc09-add5-4535-91d4-79a548649b0f` | d7, d14 |
| `2023_accelerating-the-production-and-use-of-green_9683` | `c9e4deee-ca0c-4456-860e-e0dd6defe541` | `a05fe526-9948-4023-9667-8add7988f841` | d14 |
| `2023_analisis-de-los-mecanismos-financieros-para-la_3765` | `2e5d79b9-7077-43a2-bc48-3661e7d3fd36` | `76039c19-d7e5-45f3-b543-88302b6034fa` | d4, d5 |
| `2023_assessing-the-viability-of-using-autorickshaws_2146` | `221667a3-181b-48ea-9c1f-1aee335b759e` | `5bed6c1f-674c-4d54-a9cf-0b7ca09007e0` | d14 |
| `2023_ciencia-participativa-accion-para-un-aire-limpio_6722` | `7009a0f3-2f87-4c92-bacf-490b3cde7e09` | `7f8a32fc-6de5-45de-b340-e0778bc1a595` | d13 |
| `2023_estimating-future-local-climate-hazard_4480` | `66ec635b-1731-4c60-9359-a1dff731f18a` | `a4c86569-d1d8-4cf3-8c70-46d9bc9b98cb` | d12 |
| `2023_financial-analysis-of-charging-station-fact_2082` | `3d31df40-4d1e-4110-a334-8603d6125ebe` | `ce884819-c3c3-489a-b0e3-b7ccf1a47386` | d14 |
| `2023_supporting-the-energy-transition-by-addressing_6756` | `17d3d0cc-1733-496f-b4b4-ddb6e15767c4` | `920fa327-eb75-4a10-a895-761eabbeba50` | d14 |
| `2023_visioning-to-implementation-national-transport_8631` | `02603294-1f0e-406a-896a-3f6c44666b0b` | `cbeae4dd-c970-4697-88a4-6388c069c0a5` | d1 |
| `2024_a-fare-look-funding-urban-public-transport_7541` | `02eb81cc-9359-4b1f-b01a-cc6cb3b775f7` | `f08f0762-7ba0-4f87-b5f2-bb5c63455a91` | d4, d5 |
| `2024_accelerating-zero-emission-truck-adoption-in_6287` | `b4aa3e77-d14b-4efd-a281-04c490a58b27` | `c59c544a-b1db-4610-abd5-1a57f61ca362` | d1 |
| `2024_access-to-climate-finance-in-low-and-middle_4708` | `104d4074-8931-4a10-a520-42e074273cff` | `aa613e3b-9c05-4a65-ab10-8837dd2ed8ee` | d4, d5 |
| `2024_assessing-financing-challenges-for-implementing_4732` | `4bdbed99-9ea1-4970-8572-46cc0de51465` | `0ae23d7a-5801-4bf2-95c4-a6e45311fae6` | d4, d5, d7, d14 |
| `2024_city-scale-city-relevant-climate-hazard_3175` | `ee5cc94b-d61a-4b1e-a05a-84a0124a13a2` | `1a65b36e-8fe4-4ae3-aaef-5b6e796d450b` | d12 |
| `2024_climate-resilient-cities-assessing-differential_1543` | `0540a282-59d9-4040-9a03-e592ab48140d` | `b5c503bc-31ce-4f79-b80d-4598be2411a3` | d12 |
| `2024_feasibility-of-zero-emission-freight-zones_1267` | `751b772e-6903-4c56-aeb0-09a72ff54360` | `1ad345fb-edbd-40a9-89d4-d967367ca230` | d1 |
| `2024_open-e-bus-blueprint_4307` | `a2935bf9-f8fb-4312-88e8-e1b2b56de1bd` | `49c0b8b9-28e2-47e0-ba9f-d645ae99d208` | d7, d14 |
| `2024_optimizing-container-ports-transportation-and_9894` | `e36cae4c-c6fb-441b-adf0-f43e2aec9ad9` | `add211a7-3919-48f6-bf21-c1b55f889dfb` | d3 |
| `2024_real-world-electric-bus-operation-trend-in_3497` | `efda7d35-7dc2-4d09-9421-aedba634439e` | `011e3390-85a1-4169-9be8-4e8c5f28e95b` | d7, d14 |
| `2024_techno-economic-feasibility-analysis-of-zero_7051` | `d79ef747-9490-461c-b9da-27c7a96ee033` | `0e3a739a-bc93-4c8e-aab6-21f63443e5c9` | d1 |
| `2025_aire-limpio-en-barrios-vitales_9425` | `7f874e0e-1c87-483d-8802-1c0c1bc46773` | `36c083e5-5439-466c-be92-b95ca0d6f293` | d13 |
| `2025_calculating-indicators-from-global-geospatial_3765` | `b27e589f-28e6-4a2e-bd79-3003b2a3d165` | `15831ee5-42b4-43c9-8297-02e474534d30` | d12 |
| `2025_charging-toward-2035-policies-to-accelerate-zero_7455` | `7c2e200e-9c01-4acd-b5ef-a18041a7f258` | `4281889f-338a-4997-88f9-36635930d447` | d1 |
| `2025_financial-impact-assessment-for-zero-emission_8156` | `ce8572d8-0ba6-4424-a9a6-e87a4b56e4fd` | `b9f983c5-f35c-49dc-a161-2de24a3854b7` | d14 |
| `2025_multilevel-action-for-community-led-climate_7058` | `e313372e-4880-4a0f-bd30-5fd66ec0740c` | `5e71b477-deca-4144-aade-ef9236fc62c2` | d12, d15 |
| `2025_toward-a-framework-to-support-better-decision_4539` | `71d8b96a-2b04-4d5c-ac13-aaad1ca2fe63` | `77f1de27-60e9-4aa9-8869-c99902b61336` | d14 |

## 4. Version bump

`evalset_cite_02.json`: `"version": "4.1"` → `"4.2"`, `"updated"`:
`"2026-08-13"` → `"2026-08-17"`, `description` extended with a sentence
noting the 2026-08-17 document-id reconciliation and the 4 dropped entries.

## Handoff to step 4 (new LLM session)

Corpus repair (steps 1-3 above) is orthogonal to *expanding* coverage onto
new documents. That's step 4 of the generation-2+ process (`README.md`)
and should follow the existing session working agreement in
`expected_doc_expansion_plan_citemode_20260812.md` ("one question block at
a time"). Start a fresh session with:

> Continue the Cite-mode eval expansion work described in
> `eval-generation-notes/expected_doc_expansion_plan_citemode_20260812.md`.
> The corpus was refreshed on 2026-08-17 (see
> `eval-generation-notes/issuelog_20260817.md` and
> `eval-generation-notes/evalset_repair_and_expansion_citemode_20260817.md`
> for what changed) and `evalsets/evalset_cite_02.json` has already been
> reconciled against the new document ids (v4.2) — that repair work is
> done, don't redo it. What's *not* done yet: checking whether any of the
> newly-added corpus documents from this refresh warrant new
> `expected_document_ids` entries (existing test cases) or new test cases
> entirely. Candidates to look at first: the 12 documents newly surfaced
> via `scripts/db_text_to_markdown_s3_docs.py` (previously untapped
> `document_texts` rows with S3-hosted source PDFs) and
> `2026_fortaleciendo-sinergias-electromovilidad-calidad-aire_XXXX` (likely
> not yet searchable — check if its placeholder/TEXT-PENDING markdown file
> has been replaced with real body text; if not, skip it as unevaluable
> for now). Per the working agreement, start by asking what to work on
> first rather than surveying everything at once.
