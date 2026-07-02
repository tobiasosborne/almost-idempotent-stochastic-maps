<!--
ROLE: append-only narrative session history (the accreting counterpart to the always-"now" HANDOFF.md).
UPDATE POLICY: APPEND a dated entry each session close; never rewrite past entries. HOW-to-work is CLAUDE.md.
-->

# Worklog — append-only session history

## 2026-07-02 — repository stand-up (day 1)

Stood up the scientific-exploration infrastructure, synthesised from the sister repos
(`perturbation-frontier-explorer` skeleton + rigour ladder; `extension-property` CI + `af` orchestration;
`arithmetic-quantum-mechanics` sharded-lab-book enforcement; `frontier`/`fr` controller; `vibefeld`/`af`
formaliser). Concretely:

- **Governance:** `CLAUDE.md` (== `AGENTS.md`), `PRD.md`, `README.md`, `CONVENTIONS.md` (rigour-rung table
  incl. the repo-specific `proved-mod-audit` rung + stochastic/signed notation), `FINDINGS.md` (founding
  faithfulness flags + inherited dead-route certificates), `RESEARCH_NOTES.md` (fr arms A–F), `INDEX.md`,
  this worklog, `docs/LEARNINGS.md`.
- **CI spine (Layer 3):** ported the gate scripts (`check-defs.py`, `argument.py` linker with a
  `proved-mod-audit` status, `check-refs.py`, `check-provenance.py`, `check-runs.py`, `fetch-refs.py`,
  `af-orchestrate.py`, `seed-af-workspaces.py`, tests) and added the AQM `check-report-shards.sh`
  (re-prefixed `AISM-`, adapted to the `report/main.tex` + `report/sections/` layout). `af` paths
  parameterised via `AF=${AF:-…/vibefeld/af}`. `scripts/check-all.sh` is **GREEN** on the scaffold and the
  LaTeX report builds.
- **Ingest / defs / refs:** ingested the curated classical-portfolio core into `docs/ingest/` (honestly
  re-tagged); seeded the Definitions DB with the core stochastic/signed vocabulary; set up the `refs/`
  manifest (Baake–Sumner, Högnäs–Mukherjea) + staged the contractive-projection/error-bound background.
- **Knowledge DAG:** seeded `argument/` from the ingested reduction chain
  (`op-classical ⇐ op-exposed-hull ⇐ HLC ⇐ Kernel/(EX)`), each node honestly tagged.
- **Controller:** `fr` campaign initialised (goal = `op-classical`; FRONTIER = the Kernel/(EX) conjecture;
  arms A–F).

**Nothing is rigorous in-repo yet** — the DAG is seeded from the classical-portfolio with honest status; the
first `af` elevation target is `lem-classical-equiv`. See `HANDOFF.md` and `bd ready`.

## 2026-07-02 (session 2) — sync-beads live, chain wired, FIRST RIGOROUS RESULT banked

- Implemented `argument.py --sync-beads` (pure planner + serialized bd executor; idempotent;
  reviewer-hardened: `--limit 0`, `--type blocks`, injectable-runner tests 80/80) — `bd ready` now == the
  proof frontier. Commits `17c9293`, fix `a2d78ce` context in `e68d1b6` chain. Independent opus review:
  REQUEST-CHANGES (1 MAJOR latent truncation-duplication, 1 MINOR dep-type, 2 NIT) → all fixed → APPROVE.
- Wired the missing final edge of the reduction chain: `op-classical` deps =
  `thm-classical-factorization; prop-approx-simplex` (ONE composed route, AND not OR — ingest-cited).
  Commit `c2d828f`. North star now correctly BLOCKED over 8 ancestors down to `conj-kernel`.
- **Banked `lem-classical-equiv`** (commit `e68d1b6`): af orchestration run 1 (8 rounds) built a 28-node
  tree, converged to 16 validated, exit classification = 1 MISSING fact (negative-mass formula) + sibling
  dep hygiene; orchestrator provisioned `def-negative-mass` + `def-almost-idempotent` onto the shard
  (`a2d78ce`); resumed `--phase verify` → root `validated`, taint 29/29 clean, in 7 more rounds. Oracle
  `af-lem-classical-equiv` registered; `fr verify` PASS; `fr log R banked` (new support arm R), tier T0.
  Brittleness WARN (29 nodes) accepted, factoring decision filed `aism-6ec`.
- Roles set by user: orchestrator = knowledge/strategy overview + direction evaluation, NEVER proof
  verification; no Fable subagents without permission (codex/opus/sonnet).
- Strategy review filed 2 constant-hygiene issues: `aism-8bi` (C₀ 1 vs ≥5/4 tension), `aism-z48`
  (H/δ = 2.000000000013 fuzz in an "exact" record). Standing fr decision: EXPLORE arm B next.

## 2026-07-02 (session 2, continued) — three waves harvested; frontier re-scoped to σ̃→1

- Arm B wave 1 (opus): OBSTRUCTION — obs-deep-leakage (heuristic shard) closes local-at-v routes;
  arm re-aimed at anti-splitting. Wave 2 (opus): OBSTRUCTION — obs-fwr-gap (heuristic shard) closes the
  web-rigidity family; s5 arithmetic independently recomputed over ℚ. lem-canonical-separator +
  lem-wiggle-rigidity imported as proved-mod-audit inputs. Commits fb305e7, 99e098c.
- Arm F wave 1 (opus): STALL-MAP over ~48k exact idempotents — dangerous regime never entered; collapse
  bound H(1−σ̃) ≤ ν(2+4δ) 0/500 (obs-height-collapse, the CANDIDATE FINISHER: + σ̃ ≤ 1−cτ ⇒ kernel
  closes); CERTIFIED finite-δ linear-law exceedance H/δ = 100/49 (hull-dip; kernel-safe; FINDINGS
  corrected). L3 bundle runs/2026-07-02-web-regime-hunt/ (first bundle through check-runs); headline
  certificate independently recomputed by the orchestrator. Commit 41218bf.
- obs-height-collapse seeded (861a737) and its codex orchestration launched in background.
- Tooling feedback for the fr/af maintainer agents: docs/tooling-feedback/{FR,AF}-FEEDBACK.md (5ddf3ca).
- fr decisions this stretch: B died→died (frontier reduced twice), F progress (T1), standing decision
  EXPLORE R (elevation in flight). Registry at 23 nodes; only lem-classical-equiv rigorous.
