<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v52** (current).
3. **`op-classical` is `proved` / `af: validated`**; T0 = **199**, registry
   = **374**. Honest boundary: af-validated rung only (NO Lean); upper
   bound only. **PRH square-root sharpness is T0**
   (`lem-prh-sharpness` + its two sub-lemmas, banked 2026-08-09), but the
   classical-picture carrier `cor-classical-sharpness` is still `stated` —
   its run 1 BALLOONED and the remedy needs USER RATIFICATION (below).
   Signed-parameter (δ) sharpness has NO rigorous carrier (`ex-hume`
   remains `disproved`).

## SESSION-46 RECORD (2026-08-09, W139 stages 1-4 + W140)

1. **W139 stages 1-3 BANKED** (T0 196 → 199): family-arithmetic 24/24
   (xhigh remedy (a), cap 26), row-coincidence 19/19 (cap 22), slimmed
   main FIRST-PASS 12/12 (cap 18, zero challenges — the twice-ballooned
   monolith closes at 12 nodes once factored). Each: fresh xhigh prover,
   separate fresh xhigh verifiers, export, oracle insert, external
   `fr verify` pass, mechanical flip, regenerate.
2. **W139 stage 4 BALLOON — USER DECISION REQUIRED.**
   `cor-classical-sharpness` (seeded per DESIGN-EXHUME-SHARPNESS-V2.md
   §5.2, workspace committed at `af: seeded`) run 1 aborted at BUILD with
   26 live > cap 20 (fourth family balloon: 27/28/27/26). Classification
   (TREE-CORSHARP-ABORTED.md, FINDINGS 2026-08-09): build-shape — the
   quantifier-discharge branch (~10 nodes: explicit
   b=(C·2^β)^(−1/(2β−1)) arithmetic, per-(C,η₀,β) counterexample
   packaging, a logical-equivalence wrapper) plus defect factorization.
   NOT a missing fact, NOT a gap tell. Options (standing preference
   order; caps NEVER bumped):
   - **(b)** skeleton-tightening design addendum: make η_λ/Q_λ
     definitional in node 1; state the negation clause directly as the
     per-(C,η₀,β) counterexample family (drop the equivalence wrapper).
     Fresh hostile audit + user ratification; cap 20 unchanged.
   - **(c)** factor the quantifier branch into a registry sub-lemma
     (e.g. `lem-classical-sharpness-exponent-negation`); ratification +
     provisioning + two elevations.
3. **W140 (user-directed): report sync LANDED — `aism-9kmt` CLOSED.** 92
   af-validated results anchored as shards 52-72 (authors → mechanical
   contract validation → wiring → hostile faithfulness audit, 26 findings
   fixed verbatim → re-audit 10/10 LAND). PROVENANCE +94/+184 rows;
   UNWIRED −92; PDF clean, 0 undefined refs. Protocol record:
   `docs/plans/2026-08-09-W140-REPORT-SYNC/` (incl. the honest record of
   the VACUOUS first audit pass, caught and re-run).
4. **W140 addendum (user-directed): stats layer rebuilt.**
   `scripts/gen-report-stats.py` is now a retraction-aware,
   artifact-counted post-discharge census; `--check` green; independent
   codex review of the diff ran before its commit.

## NEXT SESSION (ranked)

1. **USER: ratify the stage-4 remedy** ((b) addendum vs (c) factoring).
   Then bank `cor-classical-sharpness` (export → oracle → `fr verify` →
   flip → regenerate → gate → commit).
2. **Stage D closure** (DESIGN-EXHUME-SHARPNESS-V2.md §Stage D, BINDING;
   only after the corollary is T0): the deferred active-carrier citation
   halves, the typeset sharpness subsection in
   `report/sections/02_prh.tex`, `op-classical` pointer-block update
   (body/provenance ONLY — contract/deps/routes untouchable), paper §5
   switch to the 4×4 witness, sketch v53 + CURRENT, PRD/README/HANDOFF.
3. Paper polish (`aism-aywn`, awaiting user feedback).
4. Optional (user portfolio decision): the legacy signed chain
   (`conj-kernel`/`op-hlc`/`op-exposed-hull`) via the
   recurrent-to-exposed identification bridge over the T0 root +
   `lem-classical-equiv` (sketch v52 §4; (EX) is linear-in-δ and stays
   out of reach of this route).
5. Lean/mathlib only on user elevation.

## Worked-pattern reminders (BINDING)

- Elevation cadence per row: seed+provision (commit) → fresh worktree →
  ONE backgrounded `af-orchestrate.py` → on validation: rsync back, remove
  worktree, export md+tex, oracle insert (before the
  `af-lem-thmainext-conditional` anchor in `.frontier/portfolio.json`
  config.oracles), `fr verify` on the EXPORT PATH, mechanical flip,
  regenerate (argument.py --generate; gen-report-dag.py; gen-report-defs.py
  --dag-anchors; gen-report-stats.py --extract), `check-all`, `fr log
  banked`, commit.
- A converging run that hits max-rounds may be resumed with
  `--phase verify` per the orchestrator RECOMMEND (validated twice this
  session); a BALLOON is always stop-and-classify, never resume, never a
  cap bump.
- codex = `gpt-5.6-sol`, effort capped at `xhigh` (`ultra` forbidden);
  fresh prover ≠ fresh verifier ≠ fixer ≠ re-auditor; Claude orchestrates
  only and judges nothing.
- Report-shard authoring at scale (the W140 pipeline, reusable): authors →
  mechanical byte-verbatim contract validation → wiring → hostile
  faithfulness audit → verbatim fixes → fresh re-audit. Check audit
  outputs for per-item verdicts — an implausibly fast all-clear with
  missing per-item verdicts means a VACUOUS run (it happened; recorded).

## Open beads

`aism-4fl4` (W139 — stage 4 blocked on user remedy ratification),
`aism-aywn` (paper, awaiting feedback), `aism-wazy`, `aism-xjnc`, carried
P1s unchanged. Closed this session: `aism-9kmt` (W140 report sync).

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified). All work committed
AND pushed (verify with `git status`). In flight at close: NOTHING (no af
runs, no codex, no elevation worktrees; the cor-classical-sharpness
worktree removed after the abort was recorded).

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim that classical sharpness is rigorous: `cor-classical-sharpness`
  is `stated` (dep `lem-prh-sharpness` IS T0); signed-δ sharpness has NO
  carrier; `ex-hume` is `disproved`.
- Any decision on the stage-4 remedy or the legacy-chain reopening — both
  are the user's.
