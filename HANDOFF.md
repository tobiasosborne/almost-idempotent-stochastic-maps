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
   (banked 2026-08-09) — no uniform exponent β>1/2 can replace 1/2, via
   the T0 `lem-prh-sharpness` 4×4 witness chain. Honest boundary:
   af-validated rung only — **NO Lean/mathlib proof exists**; `ex-hume`
   remains `disproved`; signed-parameter (δ) sharpness has NO carrier.

## SESSION-46 RECORD (2026-08-09, W139 stages 1-4 + W140 + Stage D)

1. **The sharpness campaign closed at T0** (196 → 200): the factored
   chain banked in one day — family-arithmetic 24/24 (xhigh remedy (a)),
   row-coincidence 19/19, slimmed main FIRST-PASS 12/12, and, after a
   26-node run-1 balloon, the corollary FIRST-PASS 5/5 under the audited
   remedy-(b) skeleton (user-ratified "b"; designer → hostile audit
   LAND-WITH-EXACT-CORRECTIONS, 4 findings folded verbatim;
   ADDENDUM/AUDIT-CORSHARP-SKELETON.md). Every bank: fresh xhigh prover,
   separate fresh xhigh verifiers, export, oracle insert, external
   `fr verify` pass, mechanical flip.
2. **W140 report sync landed** (`aism-9kmt` closed): 92 T0 results
   anchored as shards 52-72 (authors → mechanical byte-verbatim contract
   validation → wiring → hostile faithfulness audit, 26 findings fixed →
   re-audit 10/10 LAND; the VACUOUS first audit pass caught and re-run —
   protocol record in `docs/plans/2026-08-09-W140-REPORT-SYNC/`). Stats
   layer rebuilt as a retraction-aware census (independent review).
3. **Stage D landed**: the deferred 50-locus census halves applied
   exactly (op-classical pointer block 12-16; report sweep 21-46 incl.
   the typeset four-row sharpness subsection in 02_prh.tex; paper §5 on
   the 4×4 witness with the af-validated/no-Lean footnote; root-doc loci
   1-9, 48-50; CLAUDE==AGENTS byte-identical). PROVENANCE/UNWIRED/catalog
   wired; all layers regenerated; rg sweep clean (every remaining
   `ex-hume` mention is historical/matrix-family-only/dated-record).

## NEXT SESSION (ranked)

1. **Paper polish** (`aism-aywn`): `paper/main.tex` is content-consistent
   with both banked halves (§5 now the 4×4 witness); awaiting user
   feedback for the polish pass.
2. **Lean/mathlib**: top rung, ONLY on user elevation.
3. **Optional (user portfolio decision)**: the legacy signed chain
   (`conj-kernel`/`op-hlc`/`op-exposed-hull`) via a recurrent-to-exposed
   identification bridge over the T0 root + `lem-classical-equiv`
   (sketch v53 §4: real content, exposedness-window/cloning-obstruction
   terrain; (EX) is linear-in-δ and out of reach of that route).
4. Report meta-shards 39-41 refresh on the next natural pass.

## Worked-pattern reminders (BINDING)

- Elevation cadence per row: seed+provision (commit) → fresh worktree →
  ONE backgrounded `af-orchestrate.py` → on validation: rsync back, remove
  worktree, export md+tex, oracle insert (before the
  `af-lem-thmainext-conditional` anchor in `.frontier/portfolio.json`
  config.oracles), `fr verify` on the EXPORT PATH, mechanical flip,
  regenerate (argument.py --generate; gen-report-dag.py; gen-report-defs.py
  --dag-anchors; gen-report-stats.py --extract + render), `check-all`,
  `fr log banked`, commit.
- A converging run that hits max-rounds may be resumed with
  `--phase verify` per the orchestrator RECOMMEND (validated three times
  this session); a BALLOON is always stop-and-classify, never resume,
  never a cap bump. Remedy ladder: (a) xhigh fresh prover same cap →
  (b) audited skeleton-tightening addendum → (c) factoring. Both (b)
  successes this campaign came from making identifications DEFINITIONAL
  and forcing wide quantifier arithmetic into ONE linear node.
- codex = `gpt-5.6-sol`, effort capped at `xhigh` (`ultra` forbidden);
  fresh prover ≠ fresh verifier ≠ designer ≠ auditor ≠ fixer; Claude
  orchestrates only and judges nothing.
- Report authoring at scale: the W140 pipeline
  (`docs/plans/2026-08-09-W140-REPORT-SYNC/README.md`). Always check
  audit outputs for per-item verdicts — an implausibly fast all-clear
  with missing per-item verdicts is a VACUOUS run (it happened; recorded).

## Open beads

`aism-aywn` (paper, awaiting user feedback), `aism-wazy`, `aism-xjnc`,
carried P1s unchanged. Closed this session: `aism-9kmt` (W140),
`aism-4fl4` (the sharpness campaign).

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified at close). All work
committed AND pushed (verify `git status` = up to date with origin).
In flight at close: NOTHING (no af runs, no codex, no elevation
worktrees).

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim about signed-parameter (δ) sharpness: NO rigorous carrier.
- Any reopening of the legacy signed chain — that is a user portfolio
  decision (sketch v53 §4 records the bridge idea and its risks).
