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
