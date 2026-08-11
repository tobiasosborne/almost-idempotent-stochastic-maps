<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v53** (current).
3. **BOTH HALVES OF `op-classical` ARE AT THE AF-VALIDATED RUNG.**
   T0 = **200**, registry = **374**. Upper bound: `op-classical`
   (discharged 2026-08-08, Route F). Sharpness: `cor-classical-sharpness`
   (banked 2026-08-09). Honest boundary: af-validated rung only — **NO
   Lean/mathlib proof exists**; `ex-hume` remains `disproved`;
   signed-parameter (δ) sharpness has NO carrier.
4. **THE LIVE CAMPAIGN is `aism-xvcq` (shareability), governed by the
   RATIFIED plan `docs/plans/2026-08-11-communication-artifacts-plan.md`
   ("The Glass-Box Lab").** The math campaign is parked (paper polish
   `aism-aywn` + Lean remain user-elevation-only). Headline deliverable:
   the QUANTIFIED Swiss-Cheese Defense (6 error-catching layers; counts
   in the plan §2). Rendered proposal:
   https://claude.ai/code/artifact/6d0be821-6f3d-4780-b65d-d546b30989b2

## SESSION-48 RECORD (2026-08-11)

Plan ratified (all 4 framing decisions answered by user: public repo +
GitHub Pages + arXiv eventually; honesty story FRONT PAGE; af/fr are
PUBLIC repos — af = github.com/tobiasosborne/vibefeld, fr URL to get
from user; site lives in-repo). **PHASE 0 (hygiene) COMPLETE** — 7
commits, every one gate-green, both status-bearing packages carried
independent fresh-Opus reviews (verdicts SHIP 7/7). Orchestration: 5
parallel implementer subagents + 2 reviewers; **user directive
(2026-08-11, binding): all Claude subagents = OPUS, never Fable.**
Details in `docs/worklog.md` (2026-08-11 entry). Highlights:

- Report layer TRUE again: PROVENANCE header 112→**200**; shard 41 →
  **167 reproduced** (169 ledger rows = 167 T0 + 2 retracted-anchored-
  as-conjecture; the 33-id not-reproduced set difference re-derived
  byte-identical); 00_overview's "This is OPEN" contradiction replaced
  by the discharge + honest boundary; `gen-report-dag.py` now DERIVES
  the root-status sentence and GAP links from the registry (atlas
  645→643 edges, gap links 2→0, both former gaps verified wired);
  PROVENANCE's 2026-07-25 block retitled HISTORICAL. Report rebuilt
  (302 pp, clean); `paper/main.pdf` verified current.
- Portability: AF fallback chain env→which→~/go/bin→../vibefeld (no
  wrong-user literals); REPO derived from `__file__`; munkres
  acknowledged-absent entry retired (1,133 externals, 0 failed);
  `test_gen_report_stats.py` wired into check-all (red→green proven).
- Evidence manifests: INDEX.md Script→output table completed (19 rows
  — NOTE: the Run-bundles table was already complete; the survey's
  "19 bundles missing" referred to this second table). SCHEMA
  contracts added (nsc_pair_table, floor_table + 5 registry rows).
- Local cleanup: 157 empty proofs/ stubs deleted (211 tracked
  workspaces remain, 0 orphans), 128MB stale worktrees freed, 11
  byte-identical refs-staging dupes deleted (munkres OCR kept).
- Beads: 46 pre-discharge beads DEFERRED with dated supersession notes
  (ready queue 45→7); `aism-kmi` (the op-classical carrier) CLOSED
  (forced past 2 deferred-superseded blockers); new bead `aism-yfgy`
  (check-runs should gate SCHEMA/manifest sync — name-substring match
  is blind to Script→output staleness).

## NEXT SESSION (ranked) — the plan's phase ladder

1. **Phase 1 — site data layer** (plan §Phases): `argument.py
   --emit-json` (or a new `gen-site-data.py`); parsers for
   LEARNINGS/FINDINGS/.frontier-log/runs/ledger-challenge-counts →
   `site/data/*.json`; `llms.txt`; `check-site.py --check` wired into
   check-all. All stdlib. The Defense counts (challenges/validations/
   retraction attributions) are part of this layer — they feed the
   headline page.
2. **Phase 2 — front door + core**: README rewrite (reviewer≠author on
   status claims) · site shell + design system (iron-gall palette +
   validated status badges, spec in the plan) · Theorem page with the
   live 4×4 sharpness witness · **Defense headline page** · Proof
   Atlas MVP. Ask user for the fr repo URL.
3. Phase 3 story layers, Phase 4 evidence+polish (plan §Phases).
4. Paper polish (`aism-aywn`) — still awaiting user feedback.
5. Lean/mathlib — top rung, ONLY on user elevation.

Minor known items: gen-report-stats snapshot is ~17 fr-log records
behind (advisory, not an error; refresh = deliberate `--extract` run);
`check-report-shards.sh` needs bash not sh on some boxes (`set -o
pipefail`); SHARD_CATALOG has a catalog-only AISM-00-ROADMAP block
(pre-existing).

## Worked-pattern reminders (BINDING, carried forward)

- **Subagents: Claude-side = OPUS ONLY (user, 2026-08-11).** codex =
  `gpt-5.6-sol`, effort capped `xhigh` (`ultra` forbidden); fresh
  prover ≠ fresh verifier ≠ designer ≠ auditor; Claude orchestrates
  only and judges nothing. (Also in agent memory: subagents-use-opus.)
- Status-bearing doc changes get a fresh independent reviewer before
  commit (Rule 3/L5) — the two session-48 SHIP verdicts are the
  worked pattern (recompute counts column-wise; verify section refs
  against real labels; sha256 generator idempotence).
- Report authoring at scale: the W140 pipeline
  (`docs/plans/2026-08-09-W140-REPORT-SYNC/README.md`).
- Elevation cadence / remedy ladder / BALLOON discipline: session-46
  HANDOFF (git 52af30fe) + worklog 2026-08-09.

## Open beads

**`aism-xvcq`** (P1 epic, in_progress — the live thread; plan ratified,
Phase 0 done, Phase 1 next); `aism-aywn` (paper, awaiting user);
`aism-wazy` (M26 contract mis-landing — real registry bug, live);
`aism-yfgy` (SCHEMA-sync gate gap, new); `aism-xjnc` (CHANGELOG),
`aism-2kyc`, `aism-l1a`, `aism-brez` (small infra); `aism-6ec`
(af-tree brittleness factoring, doubtful value while math is parked).
46 pre-discharge beads sit in DEFERRED with dated notes — reopen only
if the legacy signed route is user-revived.

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified after every one
of the 7 commits this session). In flight at close: NOTHING (no af
runs, no codex, no worktrees, no background agents).

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim about signed-parameter (δ) sharpness: NO rigorous carrier.
- Any reopening of the legacy signed chain — user portfolio decision
  (sketch v53 §4 records the bridge idea and its risks).
