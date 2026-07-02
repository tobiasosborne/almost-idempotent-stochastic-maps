<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md` (scope + the north-star theorem + reduction chain), then `CLAUDE.md` (== `AGENTS.md`, how
   to work — esp. the L0 rigour ladder and Rule 13 dead routes).
2. Run `fr board` (the live portfolio + FRONTIER) and `bd ready` (available work).
3. Skim `argument/DAG.md` (the seeded knowledge DAG) and `argument/INDEX.md`; read `FINDINGS.md` before
   touching anything flagged or a dead route; read `docs/ingest/README.md` for the honest re-tag map of the
   inherited work.
4. Gate before committing: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-02) — day-1 stand-up

- **Infra green.** Governance docs, the layered architecture, and the local-CI gates are in place;
  `scripts/check-all.sh` passes on the scaffold and the LaTeX report builds. `fr` campaign initialised.
- **Knowledge seeded, nothing rigorous.** The classical-portfolio is ingested (`docs/ingest/`) and its
  reduction chain codified in `argument/` with honest status (`proved-mod-audit` / `conjecture` /
  `numerical` / `open`). Only `lem-classical-equiv` was `af`-validated upstream; it re-enters as
  `proved-mod-audit` until re-validated here. **No in-repo result is rigorous (L0).**
- **`af` designed-in but opt-in** (`af: none` everywhere). Binary at `AF=${AF:-/home/tobias/Projects/vibefeld/af}`
  (also `~/go/bin/af` on PATH); `codex` present for prover/verifier workers.
- **Git:** local-only (no remote by user decision). **beads:** to be initialised (`bd init`, prefix `aism`).

## The frontier

The single live open question (the `fr` FRONTIER): **the Kernel / (EX) conjecture** — the one input that,
via `HLC ⇐ op-exposed-hull ⇐ op-classical`, closes the classical result. Geometric form: hidden row vertex
with `σ̃_v > √δ` has height `≤ B√δ`. Working (EX) form: rank-≥3 signed idempotent has a θ-½ chart with
`max_s Φ_s ≤ C₀·δ` (`C₀=1` empirically), composing with the factorization `S*≤2Φ+6δ` to `C_sf=8`.

## Next steps (ranked) — RESUME HERE

1. **Finish + verify the day-1 content** (in flight): confirm `docs/ingest/` (curated core + re-tag map),
   the seed `definitions/` (9 core shards), and `refs/manifest/` are populated and consistent; regenerate
   `definitions/INDEX.md` + `argument/{INDEX,DAG}.md`; run `sh scripts/check-all.sh` green; commit.
2. **`bd init`** (prefix `aism`), mirror the argument DAG into beads (`python3 scripts/argument.py
   --sync-beads`), and file the first work issues from the fr arms.
3. **Re-home the numerical record** as a `runs/<date>-ex-enumeration/` bundle (README + exact-arithmetic
   re-run script + invariant) so the (EX) evidence is L3-disciplined, not just prose in `docs/ingest/`.
4. **First `af` elevation** (Phase 8, decided): `seed-af-workspaces.py lem-classical-equiv`, then
   `af-orchestrate.py lem-classical-equiv` (fresh codex prover/verifier per node) → on clean `validated`,
   flip to `af: validated` and register the `fr verify` banking oracle. This is the first genuinely
   in-repo-rigorous result.
5. **Open the primary arms** (A: (EX) at rank≥3; B: frame-free `lem-dual-localization`) with `fr` waves.

## Recipes / commands

```bash
sh scripts/check-all.sh                          # the gate
python3 scripts/argument.py                       # linker: check + regen INDEX/DAG + print ready/blocked frontier
python3 scripts/argument.py --show <id>           # one result's neighbourhood
python3 scripts/check-defs.py --generate-index    # regen definitions/INDEX.md
fr board ; fr status                              # the portfolio
AF=${AF:-/home/tobias/Projects/vibefeld/af}       # af binary (opt-in Layer 2)
python3 scripts/seed-af-workspaces.py <id>        # seed one af workspace from a registry contract
python3 scripts/af-orchestrate.py <id> --workers N --max-rounds M   # run in background; orchestrator NEVER judges
```

## What is intentionally NOT here

- Any rigorous mathematical claim (day 1 — the DAG is seeded, not verified).
- The general positive-maps / Jordan (JB) Layer-1 structure theorem (that stays in
  `../almost-idempotent-positive-maps`; here only its commutative/stochastic shadow).
- A git remote / remote CI (local-only by decision; `check-all.sh` is the only gate).
- `cited` definitions whose `refs/` source isn't yet pinned (deferred — the seed defs are
  `consensus`/`original`, source `internal`).
