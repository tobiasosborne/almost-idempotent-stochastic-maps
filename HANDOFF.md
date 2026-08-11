<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`). Outsider-facing entry
   is now `README.md` (rewritten, reviewed 2026-08-11).
2. The proof sketch is `docs/plans/CURRENT.md` → **v53** (current).
3. **BOTH HALVES OF `op-classical` ARE AT THE AF-VALIDATED RUNG.**
   T0 = **200**, registry = **374**. Honest boundary: af-validated rung
   only — **NO Lean/mathlib proof**; `ex-hume` `disproved`; signed-δ
   sharpness has NO carrier.
4. **THE GLASS-BOX LAB CAMPAIGN (aism-xvcq) IS EXECUTED THROUGH PHASE 4
   (MVP).** Plan: `docs/plans/2026-08-11-communication-artifacts-plan.md`
   (carries a dated correction block — read it). The 7-page site is
   BUILT, REVIEWED, and **HOSTED**:
   https://tobiasosborne.github.io/almost-idempotent-stochastic-maps/
   (gh-pages = `git subtree split` mirror of `site/`; re-mirror procedure
   in `site/README.md` §Deployment; NO Actions — Rule 12). First Pages
   build was still propagating (404) at session close — VERIFY it serves,
   then click through all 7 pages once.

## SESSION-48 RECORD (2026-08-11, both parts)

Part 1: plan ratified (4 decisions), Phase 0 hygiene complete (7 commits,
2 reviews). Part 2: Phases 1–4 executed (see docs/worklog.md 2026-08-11
part-2 entry for the full record). Headlines:

- **site/** — 7 self-contained pages (Theorem w/ live 4×4 witness ·
  Defense w/ runtime counts · Atlas 374-node w/ Route-F-closure default
  lens · Replay w/ T0-dip chart + log explorer · Ledger · Lexicon ·
  Evidence w/ permanent L3 banner) + `site/data/*.json` (the canonical
  machine layer, gate: `check-site` in check-all) + `llms.txt`.
- **README** rewritten (reviewed SHIP, 0 overclaims); GLOSSARY,
  proofs/README (walked audit recipe), docs/README landed.
- **4 independent Opus reviews** this session; the phase-4 comprehensive
  review found 2 shipped-state BLOCKERs, both addressed:
  (1) fresh-clone check-refs failure → prose honest everywhere; the gate
  change itself is **USER DECISION bead `aism-qen0`**;
  (2) site/data generated from uncommitted frontier log → **BINDING
  PATTERN: stage `.frontier/log.jsonl` in the SAME commit as every
  `gen-site-data.py --generate`** (durable fix: bead `aism-a8tc`).
- Data layer corrected the plan's own §2 figures (retractions **7**,
  bundles **38**, externals 30 quotes/1,080 imports/23 no-quote) —
  downstream surfaces read `site/data/defense.json`, never prose.

## NEXT SESSION (ranked)

1. **Verify Pages serves** (was propagating at close) + click-through;
   if `site/` changed since, re-mirror per `site/README.md` §Deployment.
2. **USER DECISIONS pending:** `aism-qen0` (check-refs absent-vs-mismatch
   gate semantics); the **fr repo URL** (README/GLOSSARY/defense say
   "link forthcoming"); `aism-aywn` (paper polish feedback).
3. Deferred slate items (documented in `site/README.md` deviations):
   per-result drill-down pages + stable anchors (D/J), hover-cards (H),
   atlas hash deep-links, δ–H scatter, KaTeX. Plus beads `aism-a8tc`
   (frontier binding), `aism-i15b` (data-layer unit test), `aism-yfgy`
   (SCHEMA-sync gate), `aism-wazy` (M26 registry bug, pre-existing).
4. arXiv submission of `paper/main.tex` (user-ratified venue; when user
   is ready) — README/site then gain the arXiv link.
5. Lean/mathlib — top rung, ONLY on user elevation.

## Worked-pattern reminders (BINDING, carried forward)

- **Claude subagents = OPUS ONLY (user, 2026-08-11).** codex =
  `gpt-5.6-sol`, capped `xhigh`; fresh prover ≠ fresh verifier ≠
  designer ≠ auditor; Claude orchestrates only, judges nothing.
- **Stage `.frontier/log.jsonl` with every site-data regenerate** (the
  BLOCKER-2 lesson); regenerate immediately before each commit.
- Status-bearing public text gets a fresh independent reviewer BEFORE
  commit; batch reviews are acceptable only with the review landing in
  the same session (this session's phase-4 pass is the worked example).
- Site rules: numbers render from `site/data/*.json` at runtime; every
  page footer carries not-peer-reviewed/not-published/not-Lean; no
  repo-relative links in site pages (absolute GitHub URLs).

## Open beads

`aism-xvcq` (epic, in_progress — phases 0–4 MVP done; remaining scope =
deferred items above); `aism-qen0` (USER DECISION); `aism-a8tc`,
`aism-i15b`, `aism-yfgy` (infra); `aism-aywn` (paper, awaiting user);
`aism-wazy` (M26 bug); `aism-xjnc`, `aism-2kyc`, `aism-l1a`,
`aism-brez`, `aism-6ec` (small, pre-existing). 46 pre-discharge beads
remain DEFERRED with dated notes.

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified at every commit;
NOTE for fresh clones: green through every gate except byte-match until
`refs/` payloads are supplied — README explains, `fetch-refs.py --status`
lists the 12/23 auto-fetchable). In flight at close: NOTHING.

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim about signed-parameter (δ) sharpness: NO rigorous carrier.
- Any reopening of the legacy signed chain — user portfolio decision.
