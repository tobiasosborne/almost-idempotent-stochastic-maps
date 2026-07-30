<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v40** (current; the
   S1-ENDGAME fold-in is DONE). The S1-ENDGAME campaign is **COMPLETE**
   (bead `aism-8dsp` CLOSED): all 13 rows banked, **G-S1 gate
   DISCHARGED**.
3. **Rigorous (af-validated, T0): 130.** Registry: 311. `op-classical`
   OPEN.
4. **SESSION-38 RECORD (2026-07-30, the queue-completion session):**
   - **C1 `lem-stage1-rectified-nontrivial-projection` (134th, T0→128):**
     7 nodes, first-pass, ZERO challenges (budget 6/3/10).
   - **C2 `lem-stage1-original-complementary-pair` (135th, T0→129):**
     9 nodes, cap 10; one major challenge (node 1.3 equated the original
     unit with an exact two-sided unit beyond
     def-extended-epsilon-cstar-algebra) repaired by factoring +
     enlarging C_np to absorb the general-unit O(epsilon_X) complement
     error; resumed --phase all per the open-challenge rule.
   - **C3 `lem-stage1-fresh-two-point-inclusion` (136th, T0→130):**
     12 nodes, cap 14; TWO challenges (the GT external's independent
     delta-smallness hypothesis not established → leaf 1.7.1 pins
     e_up <= delta_max/(4*max{C_np,1}); 1.8's coefficient rested on
     then-pending 1.7 → leaf 1.8.1 explicit universal K, hard dep)
     repaired in-run; resumed --phase all. The ONE Kitaev external
     `GT-kitaev-prop-delta-hominc` (approximate_algebras.tex:1194-1196)
     registered under the locus-trap rule, programmatic quote-at-locus
     assertion PASS (unique at 1194-1196).
   - **G-S1 GATE DISCHARGED** — all three Stage-1 split producers
     (C1/C2/C3) T0. Sketch **v40** written + CURRENT pointer re-run;
     `aism-8dsp` closed with rationale.
   - **`aism-e1qs` (audit-allegation bug) CLOSED as already-resolved:**
     the allegation was adjudicated (ADJUDICATION-T0-ALLEGATION.md, T1/T2
     DEFECTIVE), both results retracted 2026-07-28 (LEARNINGS.md), and
     re-validated 2026-07-29 in W98 rows 4/8 on the typed
     explicit-binder spine; the bead had simply been left open.
   - Every bank followed the verified sequence (export md+tex →
     register-oracle → `fr verify` PASS → mechanical flip → regenerate →
     check-all OK → fr log banked → commit → push), now ~46×.
5. **NEXT SESSION STARTS HERE — the critical path is ONE USER DECISION:**
   1. **`aism-dm8n` (P1, USER): the MAIN P0 definition gate.**
      `DESIGN-MAIN-STRUCTURE-v5.md` (audited REPAIR-CONFIRMED,
      W78-ratified) has a HARD STOP before M01: four datum-only def
      shards need user sign-off (Rule 7). Then: land M01/M02 (+ M04–M18
      rows) → rewire M03 deps to M02 (do NOT elevate M03 against its
      current registry deps) → elevate serially. With G-S1 discharged,
      M19-S1..M28 are gated ONLY on this pre-gate.
   2. **`aism-9kmt` (P2) report paper-track sync** — scope broadened to
      banks 120–136 (17 T0 results); session-35 worktree-subagent
      pattern; delete the 13 S1-ENDGAME lines from `report/UNWIRED.md`
      on anchoring. Actionable WITHOUT user decisions.
   3. Parallel-af proposal (user "still thinking"): worktree-per-run on
      DAG antichains; unblocker `aism-2kyc`. Not yet filed as a bead.
6. **Per-row worked pattern (verified 13×; follow verbatim):**
   provision (def-add --file per def; add-external per dep with
   "imports validated registry lemma proofs/<dep> — <contract>"; GT
   externals under the FINDINGS.md locus-trap rule with a programmatic
   quote-at-locus assertion) → commit provisioning → launch
   `python3 scripts/af-orchestrate.py <id> --workers 4 --max-rounds
   <rounds> --node-cap <cap> --tier routine` in background → on
   "converging but hit --max-rounds" with all challenges resolved,
   resume `--phase verify --max-rounds 6`; with OPEN challenges,
   resume `--phase all --max-rounds 6` → on root=validated, bank per
   item 4's sequence. A BALLOON abort is a factoring STOP → classify →
   user decision (precedent bc3ca739: scoped cap amendment for
   transparent repair growth).
7. **Carried housekeeping (unchanged):** polar-retraction 29-node
   REFACTOR warning (cosmetic); `def-stage1-polar-witness-data` `\rm`
   typeset flag; report/*.aux policy; 12 dormant signed-trunk draft
   defs; `aism-ur9` (dormant); two stale pre-session-33 agent worktrees
   under `.claude/worktrees/`; Gonzalez–Hartfiel 1991 not in lit DB;
   Flor 1969 acquired, never promoted.
8. **Orchestration laws (BINDING, unchanged):** af runs strictly
   sequential; no design/audit codex while an af run is live; fr/bd
   writes FIRST, commit, launch LAST; commits only in zero-live-run
   windows. Codex = `gpt-5.6-sol`, xhigh cap (elevations run tier
   routine). A hard-cap hit is a factoring stop. A verifier finding
   needing a CONTRACT change returns to design/user.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. `aism-dm8n`: USER ratifies the MAIN P0 defs → land M01/M02 rows →
   rewire M03 → elevate the MAIN pre-gate serially (M01–M18), then
   M19-S1..M28.
2. `aism-9kmt` report sync (17 results) — parallel, no user decision
   needed.
3. Parallel-af decision (user pending) + `aism-2kyc` unblocker.
4. Housekeeping (item 7) opportunistically in zero-live-run windows.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 130. The S1-ENDGAME
  completion discharges G-S1, a Stage-1 gate — NOT the theorem: the
  MAIN pre-gate (P0 + M01–M18) and M19-S1..M28 remain, plus the
  decoupled campaigns (14-row ledger, k-ledger, f0-assembly, root
  rewire LAST).
- Any new registry content beyond the 13 ratified rows — zero new defs,
  zero new contracts this session.
- The report paper-track anchoring of banks 120–136 (deliberately
  carried as `aism-9kmt`; the 13 ids remain whitelisted in
  `report/UNWIRED.md` until anchored).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
