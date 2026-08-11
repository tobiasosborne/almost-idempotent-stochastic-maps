<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`). The outsider entry
   point is `README.md` (rewritten + independently reviewed 2026-08-11).
2. The proof sketch is `docs/plans/CURRENT.md` → **v53** (current).
3. **BOTH HALVES OF `op-classical` ARE AT THE AF-VALIDATED RUNG.**
   T0 = **200**, registry = **374**. Honest boundary: af-validated rung
   only — **NO Lean/mathlib proof**; `ex-hume` `disproved`; signed-δ
   sharpness has NO carrier.
4. **THE GLASS-BOX LAB IS LIVE:**
   **https://tobiasosborne.github.io/almost-idempotent-stochastic-maps/**
   — 7 pages (Theorem · Defense · Atlas · Replay · Ledger · Lexicon ·
   Evidence), served from `gh-pages` = a `git subtree split` mirror of
   `site/` (procedure: `site/README.md` §Deployment; NO Actions,
   Rule 12). Verified end-to-end with real pointer events against the
   live URL (atlas click-selection incl.).

## SESSION-48 ACHIEVEMENTS (2026-08-11, complete record)

**The shareability campaign (`aism-xvcq`) went from ratified plan to a
live, reviewed, hosted communication layer in one session.** Narrative
detail: `docs/worklog.md`, three 2026-08-11 entries. In order:

1. **Plan ratified + landed** —
   `docs/plans/2026-08-11-communication-artifacts-plan.md` ("The
   Glass-Box Lab"), headline = the QUANTIFIED Swiss-Cheese Defense
   (user mandate: more than a Lean formalisation — six independent
   error-catching layers, each with holes, whose composition catches
   what each misses). All four framing decisions answered: public repo
   + GitHub Pages + arXiv eventually; honesty story FRONT PAGE; af/fr
   are public repos (af = github.com/tobiasosborne/vibefeld; **fr URL
   still needed from user**); site in-repo. Rendered proposal artifact:
   https://claude.ai/code/artifact/6d0be821-6f3d-4780-b65d-d546b30989b2
2. **Phase 0 — hygiene** (7 commits, 2 independent Opus reviews, both
   SHIP): report layer trued (PROVENANCE 112→200; shard 41 → 167
   reproduced w/ the 33-id set difference re-derived; "This is OPEN"
   overview contradiction fixed; `gen-report-dag.py` now DERIVES root
   status + gap links from the registry); portability (no wrong-user
   paths); munkres refs WARN retired; `test_gen_report_stats` wired
   red→green; 157 proofs stubs + 128MB worktrees + 11 staging dupes
   cleaned; 46 pre-discharge beads deferred, `aism-kmi` closed.
3. **Phase 1 — data layer**: `scripts/gen-site-data.py` +
   `site_sources.py` (stdlib, imports argument.py's parser) →
   `site/data/*.json` (dag w/ the op-classical closure route-1
   156-all-validated / legacy-44 `all_available=false`; defense = live
   Swiss-Cheese counts; retractions; runs; definitions; frontier w/ the
   T0 timeline 29→200 and its 7 real de-banking dips; stats);
   `check-site` gate wired into check-all (red→green proven);
   `llms.txt`. The layer immediately CORRECTED 4 figures in the plan's
   own §2 (retractions **7** not 8; bundles **38**; externals = 30
   byte-matched quotes + 1,080 dep imports + 23 no-quote; "1,016" was
   `def_added` events) — dated correction block in the plan.
4. **Phase 2 — front door + core**: README rewritten (independent
   review: SHIP, 0 overclaims, 36/36 links; all 8 tightenings applied);
   `site/index.html` (live 4×4 sharpness witness, constants story,
   proved/not-proved panels), `site/defense.html` (every number
   runtime-rendered from defense.json), `site/atlas.html` (374 nodes /
   856 edges, lenses, contract side panel). Navigation docs:
   `proofs/README.md` (5-step audit recipe WALKED against real
   artifacts incl. challenge pair ch-a5432952230b16be), `docs/README.md`,
   `GLOSSARY.md` (19 entries).
5. **Phase 3 — story layers**: `replay.html` (T0 dip chart + the
   1,304-entry log explorer), `ledger.html` (7 retraction cards +
   Rule-13 dead-route cards), `lexicon.html` (47 defs + glossary
   index), `evidence.html` (38 bundles, permanent L3 banner); nav wired
   across all 7 pages; 47 test assertions.
6. **Phase 4 — adversarial review + fixes**: the comprehensive review
   re-walked the audit recipe event-id-by-event-id (clean) and found 2
   shipped-state BLOCKERs, both addressed: (i) fresh-clone check-refs
   failure (11/23 refs payloads unfetchable) → prose now honest on all
   four surfaces; the gate-semantics change is **USER DECISION bead
   `aism-qen0`**; (ii) site/data generated from the uncommitted frontier
   log → **BINDING PATTERN: stage `.frontier/log.jsonl` in the same
   commit as every `gen-site-data.py --generate`** (durable fix: bead
   `aism-a8tc`). Plus 5 MAJORs (retracted-figure relabel; achieved-curve
   provenance; 6.657 rounding; glossary kernel wording; link
   unification) and the minor sweep. Headless-Chromium verified.
7. **Hosting flip**: GitHub Pages enabled via `gh api` (legacy build,
   no Actions); `gh-pages` = subtree mirror of `site/`.
8. **Atlas selection bug (user-reported) fixed + VERIFIED LIVE**:
   `setPointerCapture` on pointerdown was retargeting clicks to the
   svg — capture now deferred past the 3px drag threshold; red→green
   proven with real Playwright pointer events, then the same suite run
   green against the LIVE URL. Lesson recorded: UI tests must dispatch
   real pointer events, not call handlers programmatically.

**Session totals**: ~20 commits, every one gate-green; 5 independent
Opus reviews (counters, residual-status, README, phase-4 comprehensive,
+ the phase-4 fix disposition); 11 implementer/reviewer subagents; 3
new beads (`aism-qen0` USER-DECISION, `aism-a8tc`, `aism-i15b`); the
proposal artifact kept in sync.

## NEXT SESSION (ranked)

1. **USER DECISIONS pending:** the **fr repo URL** (README, GLOSSARY,
   defense.html say "link forthcoming"); `aism-qen0` (check-refs
   absent-vs-mismatch gate semantics); `aism-aywn` (paper polish
   feedback); arXiv timing (venue already ratified).
2. Deferred slate items (documented in `site/README.md` deviations):
   per-result drill-down pages + stable anchors (slates D/J),
   hover-cards (H), atlas hash deep-linking, δ–H scatter, KaTeX.
3. Infra beads: `aism-a8tc` (frontier-log binding), `aism-i15b`
   (data-layer unit test), `aism-yfgy` (SCHEMA-sync gate),
   `aism-wazy` (M26 registry bug, pre-existing).
4. Lean/mathlib — top rung, ONLY on user elevation.

## Worked-pattern reminders (BINDING, carried forward)

- **Claude subagents = OPUS ONLY (user, 2026-08-11).** codex =
  `gpt-5.6-sol`, capped `xhigh`; fresh prover ≠ fresh verifier ≠
  designer ≠ auditor; Claude orchestrates only, judges nothing.
- **Stage `.frontier/log.jsonl` with every site-data regenerate**, in
  the same commit (the BLOCKER-2 lesson).
- **Re-mirror gh-pages after any `site/` change on master**
  (`site/README.md` §Deployment — three commands, deliberate local
  step).
- Status-bearing public text gets a fresh independent reviewer BEFORE
  commit; UI behavior gets REAL-event tests (the atlas lesson).
- Site rules: numbers render from `site/data/*.json` at runtime; every
  page footer carries not-peer-reviewed/not-published/not-Lean; links
  in site pages are absolute GitHub URLs.

## Open beads

`aism-xvcq` (epic, in_progress — phases 0–4 MVP done + hosted;
remaining scope = deferred items above); `aism-qen0` (USER DECISION);
`aism-a8tc`, `aism-i15b`, `aism-yfgy` (infra); `aism-aywn` (paper,
awaiting user); `aism-wazy` (M26 bug); `aism-xjnc`, `aism-2kyc`,
`aism-l1a`, `aism-brez`, `aism-6ec` (small, pre-existing). 46
pre-discharge beads remain DEFERRED with dated notes.

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified at every commit).
Fresh-clone note: green through every gate except byte-match until
`refs/` payloads are supplied (README explains; `fetch-refs.py --status`
lists the 12/23 auto-fetchable). In flight at close: NOTHING.

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim about signed-parameter (δ) sharpness: NO rigorous carrier.
- Any reopening of the legacy signed chain — user portfolio decision.
