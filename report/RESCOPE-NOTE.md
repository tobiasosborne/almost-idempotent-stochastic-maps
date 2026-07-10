# RESCOPE-NOTE — proposed CLAUDE.md §5 edit (for the orchestrator to apply)

Bead: `aism-t4p` (lab-book overhaul). This file records the proposed replacement for the `report/`
description in **CLAUDE.md §5 "Architecture — layers of the exploration"** (and the identical text in
`AGENTS.md`). Rationale: the report was implicitly treated as a registry mirror; it is now explicitly
re-scoped as the **paper-track** (af-validated results + a thin open-conjecture spine), so the guidance
should say so. Also update the same bullet in `report/README.md` if it drifts.

## FIND (current CLAUDE.md §5 bullet)

> - **Sharded lab book — `report/`** (rigorous narrative, LaTeX, one ≤~200-line shard per `\section`,
>   with a `% SHARD-ID/TITLE/SUMMARY/KEYWORDS` header, indexed by `report/SHARD_CATALOG.md` +
>   `report/PROVENANCE.md`) + **`runs/`** (numerical experiments, bundle-per-run) + **`INDEX.md`** (the
>   evidence-layer manifest). Gates: `check-report-shards.sh`, `check-provenance.py`, `check-runs.py`.

## REPLACE WITH

> - **Sharded lab book — `report/` (the PAPER-TRACK, not a registry mirror)**: the rigorous narrative
>   reproduces the **af-validated (T0) results** of `argument/` plus a **thin spine of open conjectures**
>   that orients them; every non-rigorous registry result (inherited `proved-mod-audit`, `conjecture`,
>   `numerical`, `heuristic`) is anchored **once** in the status ledger (`sections/13_discussion.tex`),
>   never restated as a theorem. Registry ids intentionally left off the paper-track are whitelisted in
>   `report/UNWIRED.md` (an unanchored id not listed there is a hard `check-provenance` error). LaTeX,
>   one ≤~200-line shard per `\section` (hard guard 280) with a `% SHARD-ID/TITLE/SUMMARY/KEYWORDS`
>   header and **properly typeset mathematics** (`amsthm` theorem environments, real
>   `equation`/`align`, semantic macros — not ASCII math in prose); indexed by `report/README.md`
>   (order) + `report/SHARD_CATALOG.md` (search) + `report/PROVENANCE.md` (ledger). Then **`runs/`**
>   (numerical experiments, bundle-per-run) + **`INDEX.md`** (the evidence-layer manifest). Gates:
>   `check-report-shards.sh`, `check-provenance.py`, `check-runs.py`.

## Also worth a one-line touch (router, top of CLAUDE.md)

The router already points to the proof-sketch as the most dynamic artifact; no change needed there. If
desired, the "sharded lab-book" mention can gain the parenthetical "(paper-track: T0 + open spine)".
