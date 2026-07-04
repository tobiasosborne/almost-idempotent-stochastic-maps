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
| 00 | `AISM-00-OVERVIEW` | `report/sections/00_overview.tex` |
| 01 | `AISM-01-CLASSICAL-EQUIV` | `report/sections/01_classical_equiv.tex` |
| 02 | `AISM-02-HEIGHT-COLLAPSE` | `report/sections/02_height_collapse.tex` |
| 03 | `AISM-03-MASS-SPLIT` | `report/sections/03_mass_split.tex` |
| 04 | `AISM-04-RESIDUAL-LOWER` | `report/sections/04_residual_lower.tex` |
| 05 | `AISM-05-RESIDUAL-UPPER` | `report/sections/05_residual_upper.tex` |
| 06 | `AISM-06-HALO-COLLAPSE` | `report/sections/06_halo_collapse.tex` |
| 07 | `AISM-07-FACTORIZATION` | `report/sections/07_factorization.tex` |
| 08 | `AISM-08-ZEROSUM-TRIANGLE` | `report/sections/08_zerosum_triangle.tex` |
| 09 | `AISM-09-WEIGHTED-MIN` | `report/sections/09_weighted_min.tex` |
| 10 | `AISM-10-FAN-PAYMENT` | `report/sections/10_fan_payment.tex` |
| 11 | `AISM-11-NEGPART-SUBADDITIVE` | `report/sections/11_negpart_subadditive.tex` |
| 12 | `AISM-12-FAN-PAYMENT-RESTRICTED` | `report/sections/12_fan_payment_restricted.tex` |
| 13 | `AISM-13-STATUS-LEDGER` | `report/sections/13_discussion.tex` |
