<!--
ROLE: ORDER map + conventions for the sharded lab-book. Lists every shard file and its SHARD-ID in
  include order. scripts/check-report-shards.sh requires every included shard's file path AND its
  AISM-NN-LABEL id to appear here (and its title/keywords/summaries in SHARD_CATALOG.md).
UPDATE POLICY: append a row in the same commit that adds a shard (CLAUDE.md Rule 9). Not generated.
-->

# report/ — the internal RIGOROUS lab-book (sharded)

`report/main.tex` (+ `sections/NN_<slug>.tex`) is the internal LaTeX lab-book that reproduces the
**rigorous spine** of the argument: each Definition/Theorem here is either byte-matched to a `refs/`
source or `af`-validated (L0), and carries a row in `PROVENANCE.md`. This is **not** where numerics or
heuristics go — those live in `runs/` (numerical, L3) and the `argument/` shard bodies, tagged
non-rigorous. The ingested classical-portfolio (`docs/ingest/`) is the object of re-establishment, not
reproduced here until a result clears L0.

- `main.tex` — master; preamble + macros + an ordered `\include{sections/NN_<slug>}` list ONLY (no body
  prose; `check-report-shards.sh` enforces master purity).
- `sections/NN_<slug>.tex` — one shard per result/topic (~≤200 lines, hard guard 280), each opening with a
  header block:

  ```
  % SHARD-ID: AISM-NN-SOME-LABEL
  % SHARD-TITLE: Human title
  % SHARD-SUMMARY: sentence 1 (mirrored verbatim in SHARD_CATALOG.md)
  % SHARD-SUMMARY: sentence 2
  % SHARD-KEYWORDS: comma, separated, keywords
  \section{Human title}\label{sec:...}
  ```

- `SHARD_CATALOG.md` — the search index (id + title + summaries + keywords per shard); gated.
- `PROVENANCE.md` — the audit ledger (source registry + per-claim rows); gated by `check-provenance.py`.
- `Makefile` — `make` → `latexmk -pdf main.tex` → `main.pdf`.

Build: `cd report && make`. The gate compiles into `report/.build/` so `main.pdf` is never mutated
mid-check.

## Shard order (id → file)

| # | SHARD-ID | file |
|---|----------|------|
<!-- Shard-order rows for report/README.md ("Shard order (id -> file)" table).
     Replace the existing table body with these 23 rows, in this order. -->

| # | SHARD-ID | file |
|---|----------|------|
| 00 | `AISM-00-OVERVIEW` | `report/sections/00_overview.tex` |
| 01 | `AISM-01-CLASSICAL-EQUIV` | `report/sections/01_classical_equiv.tex` |
| 02 | `AISM-02-PRH` | `report/sections/02_prh.tex` |
| 03 | `AISM-03-COMPCB-AMPLIFICATION-NATURALITY` | `report/sections/03_compcb_amplification_naturality.tex` |
| 04 | `AISM-04-COMPCB-AMPLIFIED-COMPRESSION` | `report/sections/04_compcb_amplified_compression.tex` |
| 05 | `AISM-05-COMPCB-AMPLIFIED-COMPRESSION-IDENTITIES` | `report/sections/05_compcb_amplified_compression_identities.tex` |
| 06 | `AISM-06-COMPCB-ENTRYWISE-COMPRESSION-NATURALITY` | `report/sections/06_compcb_entrywise_compression_naturality.tex` |
| 07 | `AISM-07-COMPCB-RECTANGULAR-PRODUCT` | `report/sections/07_compcb_rectangular_product.tex` |
| 08 | `AISM-08-COMPCB-AMPLIFIED-ALMOST-CONTAINMENT` | `report/sections/08_compcb_amplified_almost_containment.tex` |
| 09 | `AISM-09-COMPCB-COMPRESSED-UNIT-NORM` | `report/sections/09_compcb_compressed_unit_norm.tex` |
| 10 | `AISM-10-HCB2-AMPLIFIED-ADJOINTNESS` | `report/sections/10_hcb2_amplified_adjointness.tex` |
| 11 | `AISM-11-COMPCB-COMPRESSED-UNIT-ACTION` | `report/sections/11_compcb_compressed_unit_action.tex` |
| 12 | `AISM-12-COMPCB-ROW-COLUMN-PRODUCT` | `report/sections/12_compcb_row_column_product.tex` |
| 13 | `AISM-13-HCB0-COMPRESSED-ASSOCIATOR` | `report/sections/13_hcb0_compressed_associator.tex` |
| 14 | `AISM-14-COMPCB-CORNER-ALGEBRA` | `report/sections/14_compcb_corner_algebra.tex` |
| 15 | `AISM-15-HCB-COLUMN-HILBERT-SQUARED` | `report/sections/15_hcb_column_hilbert_squared.tex` |
| 16 | `AISM-16-COMPCB-SINGLE-COMPRESSION-TRANSFER` | `report/sections/16_compcb_single_compression_transfer.tex` |
| 17 | `AISM-17-HCB1-VARIATIONAL-IDENTITY` | `report/sections/17_hcb1_variational_identity.tex` |
| 18 | `AISM-18-HCB1-COLUMN-ACTION` | `report/sections/18_hcb1_column_action.tex` |
| 19 | `AISM-19-HCB2-PRODUCT-DEFECT` | `report/sections/19_hcb2_product_defect.tex` |
| 20 | `AISM-20-HCB3-DIAGONAL-UNIT` | `report/sections/20_hcb3_diagonal_unit.tex` |
| 21 | `AISM-21-HCB3-DIAGONAL-UPPER-NORM` | `report/sections/21_hcb3_diagonal_upper_norm.tex` |
| 22 | `AISM-22-STATUS-OUTLOOK` | `report/sections/22_status_outlook.tex` |
