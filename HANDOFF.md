<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v44** (current).
3. **Rigorous (af-validated, T0): 168.** Registry: 349. `op-classical` OPEN.
4. **SESSION-41 RECORD (2026-08-02, the MAIN-completion session; user
   pre-ratified the process in-session: "i ratify the decisions"):**
   - **THE MAIN CAMPAIGN IS COMPLETE: every row M01–M28 af-validated T0**
     (T0 165 → 168). The capstone M28 `lem-maincb-structural-assembly`
     delivers, at T0, the universal witnesses
     `C_struct = W.c0_cb*W.K_call`, `e_struct = W.epsilon_MAIN` (extended
     `C_struct*eps`-isomorphism from `⊕_C M_{|C|}` with unit control).
   - **The M24 gap (aism-twpa P0) repaired END-TO-END in one session, zero
     self-judged steps:** design round (fresh codex, option (a):
     NEW provider `lem-maincb-corner-nontriviality`, M24 contract
     byte-UNCHANGED, deps-only; (b) REJECTED — frozen consumers
     M10/M25/M19-S3/M26/M27 need literal one-dimensionality + partition
     reflexivity; (c) collapses into (a)) → SEPARATE fresh hostile audit
     DESIGN-CONFIRMED (3 editorial fixes → DESIGN-M24-NONTRIVIALITY-v2.md)
     → provider banked FIRST-PASS 7/7 (T0 166; one challenge cured by the
     byte-verbatim GT-kitaev-def-delta-homomorphism external) → M24
     re-seeded clean and banked FIRST-PASS 5/5, ZERO challenges (T0 167).
     Bead CLOSED.
   - **M28 banked on run 2 (T0 168):** run 1 ABORTED [BALLOON] 20 > cap 13
     (root NEVER challenged — 4/6 challenges were missing workspace
     vocabulary, 2 were glue-node structure); response per the balloon law:
     vocabulary provisioned (def-delta-projection, def-projection-basis,
     def-one-dimensional-delta-projection, def-compressed-corner + the GT
     δ-homomorphism external), shard-body guidance sharpened, SCOPED CAP
     AMENDMENT 13→20 (flagged); run 2 validated 20/20 (cross-unit
     monotonicity challenges cured by an amplification-wise direct check;
     finished in a resumed `--phase verify` pass).
   - **The `lem-thmainext-conditional` rewire LANDED** (design v5 sect-10
     step 15; precondition M28+M19-R T0 met): fresh-designer re-validation
     against the repaired contracts kept the seven-dep line VERBATIM
     (rationale corrected: reset ledger reaches thmainext through M28, NOT
     M19-R; W-ledger coherent — C_E := W.c0_cb*W.K_call,
     epsilon_E := W.epsilon_MAIN, contract byte-unchanged); separate
     hostile audit DESIGN-CONFIRMED; deps-only landing, status stays
     `proved-mod-audit`, af stays `none` (NOT a rigour promotion).
   - **Sketch v44** folded in (CURRENT.md regenerated); FRONTIER updated
     (the stale pre-session-40 M17 line replaced).
   - Every bank: rsync-back → export → oracle → `fr verify` PASS (export.md
     bank-gate path) → mechanical flip → regenerate → check-all OK →
     fr log → commit → push. Waves W125–W132 on arm FH.
5. **NEXT SESSION STARTS HERE — the decoupled campaigns (sketch v44 open
   surface):**
   1. The **14-row ledger campaign** (local radii), the **k-ledger**, and
      the **F0-assembly design** — the remaining Route-F chain above the
      MAIN subtree. Re-orient from `fr board` + the W97 elevation-queue
      trail; these are design/elevation campaigns of the same shape as
      MAIN.
   2. The **thmainext elevation** (af workspace exists, af: none; its deps
      are now correctly wired; the W-ledger coherence statement in
      DESIGN-THMAINEXT-REWIRE.md sect-3 gives the witness choices) and the
      **root rewire LAST** — unchanged order from v41–v44.
   3. `aism-9kmt` report sync (P2, LARGE — unanchored banks now ~120–177).
6. **Worked patterns (BINDING; follow verbatim):**
   - **Pre-launch checks:** workspace root string == the RATIFIED design
     contract text (not merely == the shard); def_added names UNIQUE in
     the ledger (af def-add does NOT reject duplicates — it assigns fresh
     ids and pollutes the seed; wipe + re-seed if polluted).
   - **Provision the PROOF's vocabulary, not the contract's** (the M28
     lesson, demonstrated twice): at seeding time add the per-node import
     lists from the design skeleton — base def-epsilon-cstar-algebra,
     projection/corner vocabulary, and the byte-verbatim
     GT-kitaev-def-delta-homomorphism external wherever δ-homomorphism
     arithmetic appears (reuse the registration in
     proofs/lem-maincb-extended-inclusion-monotone/externals/).
   - Elevation guidance that produced 8 first-pass banks: constant-choice /
     binder FIRST child; one fixed W threaded (same-map law); NO
     pending-sibling citations; explicit typing citations at point of use;
     NO reset provider unless the row genuinely resets.
   - Launch: worktree per run (`git worktree add --detach
     .claude/worktrees/af-<row> HEAD`), orchestrator from INSIDE the
     worktree, ONE backgrounded call, tier routine, workers 4, node-cap =
     the row's (amended) hard cap.
   - Balloon/stuck: read the orchestrator's classification; missing
     vocabulary ⇒ provision + clean re-seed; transparent repair growth ⇒
     scoped cap amendment (flag it; ceiling 26); "converging, hit
     max-rounds" ⇒ resume `--phase verify` on the SAME tree (no rebuild —
     worked for M28); contract-level finding ⇒ STOP, escalate.
   - Bank: serial in main (rsync back → export → oracle → `fr verify`
     export.md → flip → regenerate → check-all → fr log → commit → push).
     `fr log banked` REQUIRES the oracle-verified artifact; design/audit
     harvests log as `progress` (class design, tier T2).
7. **Open beads:** `aism-wazy` (P1, duplicate-contract tripwire
   suggestion; the mis-landing fix itself is long done); `aism-9kmt` (P2
   report sync). Carried P1 items unchanged (typeset flags,
   polar-retraction REFACTOR warning, dormant signed-trunk defs, lit-DB).
8. **Orchestration laws (BINDING):** parallel worktree orchestrations ≤5
   concurrent, serial banking; no design/audit codex while ANY af run is
   live; fr/bd writes FIRST, commit, launch LAST; codex = `gpt-5.6-sol`,
   xhigh cap (designs/audits xhigh or high; elevations tier routine). A
   verifier finding needing a CONTRACT/DEF change returns to design/user.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at close).
   All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. The decoupled campaigns: 14-row ledger local radii, k-ledger,
   F0-assembly design (re-orient from `fr board` + the W97 trail).
2. The thmainext af elevation (deps now wired; W-ledger witness choices in
   DESIGN-THMAINEXT-REWIRE.md sect-3), then the root rewire LAST.
3. `aism-9kmt` report sync (P2, large — banks ~120–177 unanchored).
4. The `aism-wazy` tripwire: a linker check that no two registry rows
   share a byte-identical contract.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 168. The MAIN subtree
  being complete is a STRUCTURAL milestone inside Route F, not the
  theorem: `lem-thmainext-conditional` remains `proved-mod-audit`, and
  the chain above it (ledger campaigns, F0 assembly, root) is not T0.
- Any rigour claim for the thmainext rewire — it was a WIRING alignment
  of the ratified plan (deps-only; audited), not a promotion.
- The report anchoring of banks ~120–177 (carried as `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
