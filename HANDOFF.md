<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v43** (current).
3. **Rigorous (af-validated, T0): 165.** Registry: 347. `op-classical` OPEN.
4. **SESSION-40 RECORD (2026-08-02, the re-validation-clearing + consumer-chain session):**
   - **NINE T0 events (T0 156 → 165):** M19-S3 re-banked (fresh v2 tree
     19/19 — re-seed architecture v2: S2-pattern constant-choice first
     child, nonnegative-c0 enlargement, K_3^0 absorption, no
     pending-sibling citations; cures the F5 gap); M18 + M20 re-flipped
     mechanically (certificates intact, oracles re-verified); M25
     re-banked (20/20 under typed-reset-alone + same-map law + explicit
     induction + the F1 typing cure); then the consumer chain M21 (6/6),
     M23 (11/11), M22 (9/9), M26 (11/11), M27 (7/7) — **all FIRST-PASS**
     under the binding elevation guidance. Bead `aism-mc54` CLOSED.
   - **M26 contract MIS-LANDING caught pre-launch and fixed** (P1
     `aism-wazy`, commit c8eb827b): 894c983f had pasted the typed-reset
     contract (design block 3) into the M26 shard; the user-ratified
     block 1 was landed byte-verbatim and the workspace re-seeded.
     Lesson: linker contract-match is shard<->workspace ONLY — verify
     root==RATIFIED-DESIGN-TEXT before every launch (now in the worked
     pattern); a duplicate-contract tripwire would catch this class.
   - **M24 CONTRACT-LEVEL GAP escalated** (P0 `aism-twpa`, commit
     2d9feb7a): `lem-maincb-stage1-maximality` requires
     `dim S_{P_j} = 1` but verifiers established no allowed input gives
     `dim >= 1` (only `P_j != 0` and `dim <= 1`; the nonzero-projection
     => nonzero-corner-space inference is unregistered). Prover root
     weakening correctly rejected as scope drift; workspace restored to
     the clean ratified seed (linker green); aborted tree preserved in
     the session scratchpad + classification on the bead/fr W124.
   - Every bank: rsync-back → export → (register-)oracle → `fr verify`
     PASS → mechanical flip → regenerate (argument + report-dag +
     report-stats) → check-all OK → fr log → commit → push.
5. **NEXT SESSION STARTS HERE — the M24 decision, then M28:**
   1. **USER DECISION (aism-twpa, P0):** resolve the M24
      `dim S_{P_j} = 1` gap via a design round + hostile audit +
      ratification. Options (unjudged): (a) a compressed-corner
      nontriviality provider row (candidate pointer, applicability
      unassessed: `lem-stage1-rectified-nontrivial-projection`); (b)
      amend M24 to the provable `dim <= 1` form IF the consumer survey
      (M28 + Stage-1 chain) allows; (c) strengthen a dep to export
      nontriviality. Do NOT re-launch M24 until ratified.
   2. **M28** (`lem-maincb-structural-assembly`) — the MAIN capstone —
      is blocked SOLELY on M24 (M27 banked this session; all other deps
      green; oracle already registered).
   3. Then the escalated `lem-thmainext-conditional` rewire (design
      sect-10 step 15), the decoupled campaigns (14-row ledger,
      k-ledger, f0-assembly), root rewire LAST.
   4. `aism-9kmt` report sync (P2, large — unanchored banks now
      ~120–174).
6. **Worked patterns (BINDING; follow verbatim):**
   - **Pre-launch check (NEW, the aism-wazy lesson):** verify the
     workspace root string == the ratified design contract text (not
     just == the shard — the shard itself can be mis-landed).
   - Provision: `python3 scripts/provision-af-row.py <rid>` + base
     `def-epsilon-cstar-algebra` + vocabulary defs + (where the row
     touches δ-homomorphism arithmetic) the byte-verbatim
     `GT-kitaev-def-delta-homomorphism` external (tex:443-456; reuse the
     registration in `proofs/lem-maincb-extended-inclusion-monotone/externals/`).
   - **Elevation guidance (in each shard body; demonstrated 6-for-6
     first-pass):** constant-choice FIRST child (nonnegative universal
     constants by enlargement under the monotonicity import; absorb every
     scalar prerequisite into the chosen universal; never assume an
     unregistered inequality like c0>=1); typed-reset provider ALONE with
     ONE fixed witness threaded through (same-map law); NO
     pending-sibling citations; typing-cited bijective=>isomorphism;
     explicit induction dependencies.
   - Launch: worktree per run (`git worktree add --detach
     .claude/worktrees/af-<row> HEAD`), orchestrator from INSIDE the
     worktree, ONE backgrounded call, tier routine, workers 4, node-cap =
     the row's (amended) hard cap.
   - Balloon/stuck: transparent repair growth ⇒ scoped cap amendment
     (flag it; ceiling 26); tangled tree ⇒ clean RE-SEED with sharpened
     body guidance; contract-level finding ⇒ STOP, escalate (exercised
     for M24; if the aborted tree's root was amended by the prover,
     git-checkout + git-clean the workspace back to the seed or the
     linker's contract-match fails).
   - Bank: serial in main (rsync back → export → oracle → verify → flip
     → regenerate → check-all → fr log → commit → push). Oracle
     registration: append to `config.oracles` in
     `.frontier/portfolio.json` (af-validated.py pattern).
7. **Open beads:** `aism-twpa` (P0, the M24 USER DECISION — blocks M28);
   `aism-wazy` (P1, the duplicate-contract tripwire lesson; the landing
   fix itself is DONE). Carried P1/P2 items unchanged (aism-9kmt report
   sync; typeset flags; polar-retraction REFACTOR warning; dormant
   signed-trunk defs; lit-DB items).
8. **Orchestration laws (BINDING):** parallel worktree orchestrations ≤5
   concurrent, serial banking; no design/audit codex while ANY af run is
   live; fr/bd writes FIRST, commit, launch LAST; codex = `gpt-5.6-sol`,
   xhigh cap (designs/audits xhigh or high; elevations tier routine). A
   verifier finding needing a CONTRACT/DEF change returns to design/user.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
   All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. **aism-twpa (P0):** design round + audit + user ratification for the
   M24 nontriviality gap; then re-seed/elevate M24.
2. **M28** — the MAIN structural-assembly capstone (blocked only on M24).
3. `lem-thmainext-conditional` rewire; then the decoupled campaigns.
4. `aism-9kmt` report sync (P2, large — banks ~120–174 unanchored).
5. Consider the `aism-wazy` tripwire: a linker check that no two registry
   rows share a byte-identical contract.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 165.
- Any claim about how the M24 gap should be resolved — that is the user's
  call after a design round (options on `aism-twpa`, deliberately
  unjudged).
- The report anchoring of banks ~120–174 (carried as `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
