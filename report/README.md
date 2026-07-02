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
| _(none yet)_ | | |
