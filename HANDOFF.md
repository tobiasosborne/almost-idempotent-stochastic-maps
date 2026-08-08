<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v51** (current).
3. **`op-classical` is `proved` / `af: validated`** (discharged 2026-08-08,
   session 45). T0 = **196**. Registry = **374**. Honest boundary:
   af-validated rung only (NO Lean proof); upper bound only — **sharpness
   is an ACTIVE campaign (W139), not yet T0**, and signed-parameter (δ)
   sharpness is established at NO rigorous rung (ex-hume is retracted).

## SESSION-45 RECORD (2026-08-08, W138 + W139 — the long day)

1. **W138: `op-classical` DISCHARGED AT T0** (T0 190 → 196). Strengthened
   K-ledger package: design → hostile REJECT → v2 (3 helpers) → hostile
   LAND (zero corrections) → user-ratified → landed → five-stage
   elevation queue banked same-day (helpers 191-193; strengthened parent
   194 FIRST PASS 7/7; F0-assembly 195) → user-ratified root rewire
   (audited OR-routes; kind → theorem) → root af tree 5/5 clean → 196.
   Full report truthfulness sweep; PRD/sketch v50. Artifacts:
   `docs/plans/2026-08-08-KLEDGER-STRENGTHENED/`.
2. **USER P0 paper delivered** (bead `aism-aywn`): `paper/main.tex`, 4pp
   (fresh draft → separate faithfulness audit → 4 corrections applied →
   post-discharge footnote). Awaiting user polish feedback.
3. **W139 (bead `aism-4fl4`): the sharpness campaign — IN PROGRESS.**
   - `ex-hume` RETRACTED (`disproved`): its inherited contract is FALSE
     as stated (I_3 counterexample: ||P_s−I_3|| = 2(1−s+s²) ≠ claimed
     2s(1−s+s²)). Three hostile audit rounds; user-ratified; first
     `docs/LEARNINGS.md` entry; 51-locus citation sweep landed (incl.
     `thm-rank-one` contract fix + the locked
     `def-near-positive-projection` scoping fix).
   - Active route (stochastic η only): `cor-classical-sharpness`
     (`stated`; dep `lem-prh-sharpness`) — the direct 4×4 witness with
     the explicit quantified no-β>1/2 negative.
   - `lem-prh-sharpness` FACTORED after two balloon aborts (user-ratified,
     AUDIT-PRHSHARP-FACTOR.md LAND-W-E-C): +
     `lem-prh-sharpness-family-arithmetic`,
     `lem-prh-sharpness-row-coincidence` (both `stated`); main row deps
     extended, contract byte-frozen.
   - **Elevation state at close: NOTHING in flight; no sharpness row T0.**
     family-arithmetic run 1 ALSO ballooned (27>26, 20 validated — the
     THIRD balloon in this family; trees + classification:
     `docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-*.md`, FINDINGS
     2026-08-08 "family-specific pathology").

## NEXT SESSION — the W139 finish (ranked, with the binding know-how)

1. **Elevate `lem-prh-sharpness-family-arithmetic`** (workspace committed
   at `af: seeded`, provisioned per DESIGN-PRHSHARP-FACTOR.md §5.1).
   Apply FINDINGS remedy (a) FIRST: fresh prover at **xhigh** (override
   `--prover-effort xhigh`), cap 26, ~5 rounds. The two run-1 challenges
   to pre-empt: cross-sibling dependency declarations, and the
   identification "the displayed candidate vectors ARE the rows of
   A_lambda, M_lambda" (make it definitional in node 1). If xhigh also
   balloons: remedy (b) skeleton-tightening design addendum (fresh audit,
   user ratification); only then (c) further factoring. NEVER bump caps.
2. **Elevate `lem-prh-sharpness-row-coincidence`** (cap 22; seed per
   §5.2 only after stage 1 banks).
3. **Elevate the slimmed main `lem-prh-sharpness`** (cap 18). BINDING:
   its current `proofs/lem-prh-sharpness` workspace was seeded BEFORE the
   deps ratification — **delete and cleanly re-seed** per
   DESIGN-PRHSHARP-FACTOR.md §5.3 (2 defs + the two sub-lemma externals
   byte-verbatim at literal proofs/<id> paths, only after both are T0).
4. **Elevate `cor-classical-sharpness`** (cap 20; external = the T0 main
   row contract, byte-verbatim; seeding in DESIGN-EXHUME-SHARPNESS-V2.md
   §5.2).
5. **Stage D closure** (DESIGN-EXHUME-SHARPNESS-V2.md §Stage D, BINDING):
   the deferred active-carrier halves of the 50-locus sweep (loci that
   say "carried at T0 by cor-classical-sharpness" may only land once it
   IS T0), the fully-typeset sharpness subsection in
   `report/sections/02_prh.tex`, PROVENANCE rows + UNWIRED delisting,
   `op-classical` pointer-block update (body/provenance only — contract/
   deps/routes UNTOUCHABLE), paper §5 switch to the 4×4 witness + footnote
   update, sketch v52 + CURRENT, PRD/README/HANDOFF, full gates, push.
6. Then: report sync `aism-9kmt`; paper polish (`aism-aywn`); Lean only on
   user elevation.

## Worked-pattern reminders (BINDING)

- Elevation cadence per row: seed+provision (commit) → fresh worktree →
  ONE backgrounded `af-orchestrate.py` (workers 4, tier routine unless
  FINDINGS says otherwise) → on validation: rsync back, remove worktree,
  export md+tex, oracle insert (before the `af-lem-thmainext-conditional`
  anchor in `.frontier/portfolio.json` config.oracles), `fr verify` on
  the EXPORT PATH (`proofs/<id>/export.md` — the bank gate matches the
  verified claim string exactly), mechanical flip, regenerate
  (argument.py --generate; gen-report-dag.py; gen-report-defs.py
  --dag-anchors; gen-report-stats.py --extract), `check-all`, `fr log
  banked`, commit.
- Never resume an af run across a registry ratification; balloon vs
  build-shape vs missing-fact taxonomy in FINDINGS 2026-08-08 (two
  entries).
- codex = `gpt-5.6-sol`, effort capped at `xhigh` (`ultra` forbidden).
- Design/audit rounds: fresh worker per role; Claude orchestrates only;
  every package lands only on explicit user ratification.

## Open beads

`aism-4fl4` (W139 sharpness — IN PROGRESS, the top priority),
`aism-aywn` (paper, delivered, awaiting feedback), `aism-9kmt` (report
sync — biggest debt after sharpness), `aism-wazy`, `aism-xjnc`, carried
P1s unchanged. Closed this session: `aism-e30g` (W138), `aism-xuvw`
(Route-F T0 epic) + 3 children.

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified at close). All work
committed AND pushed. **NOTHING in flight** (no af runs, no codex, no
elevation worktrees).

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim that sharpness is rigorous: `cor-classical-sharpness` is
  `stated`; `ex-hume` is `disproved`; signed-δ sharpness has NO carrier.
- Any `op-npps` (general positive-maps) claim — out of scope.
