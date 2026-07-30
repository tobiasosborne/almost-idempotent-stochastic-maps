<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v41** (current).
3. **Rigorous (af-validated, T0): 144.** Registry: 341. `op-classical`
   OPEN.
4. **SESSION-38 RECORD (2026-07-30, the MAIN-campaign session):**
   - **S1-ENDGAME COMPLETED** (rows C1–C3 banked, 134th–136th; G-S1
     DISCHARGED; sketch v40; `aism-8dsp` closed).
   - **The full MAIN package landed** (30 rows M01–M28 verbatim from
     the audited DESIGN-MAIN-STRUCTURE-v5, user-ratified in-session;
     registry 311→341; M03 deps rewired; the P0 def gate turned out to
     be ALREADY discharged 2026-07-27 — `aism-dm8n` was stale).
   - **PARALLEL-AF ROLLED OUT (user-ratified):** detached-worktree
     orchestrations (≤5 concurrent), ALL banking serial in the main
     checkout (fr's absolute-path oracle contract respected; the
     `aism-2kyc` migration is unnecessary — see the bead note).
     Reusable tooling: `scripts/provision-af-row.py` (provisions a
     workspace from its shard; REFUSES non-validated dep externals).
   - **EIGHTEEN MAIN rows banked (137th–151st; T0 130→144):** M14,
     M01, M06, M10, M02(×2: weaker then STRENGTHENED), M07 (telescope
     gap-stop CLEARED), M05, M08, M15, M11, M09, M03 (IMPROVE-CB
     rigorous, run 4), M04, M13(×2: VACUOUS flagged, then NON-VACUOUS
     under the amended def).
   - **THREE contract-level interface defects caught** (sketch v41 map
     change 3): M02 under-export (RESOLVED, user-ratified
     strengthening); partition-state 'union of classes' semantics
     (RESOLVED, user-ratified amendment to 'nonempty subset of J';
     M13's vacuous validation honestly flagged then superseded);
     **OPEN: `aism-jl4g` (P0)** — the unit-clause thread + the W93
     anaphoric-constant pattern (below).
   - Every bank: export → register-oracle → `fr verify` PASS →
     mechanical flip → regenerate → check-all OK → fr log → commit →
     push (now ~65× lifetime).
5. **NEXT SESSION STARTS HERE — `aism-jl4g` (P0), the ONLY gate:**
   1. Dispatch a fresh-codex DESIGN job + hostile audit (zero live
      runs now; W78/W97 protocol) for the TWO-defect repair package:
      (a) **unit-clause thread**: def-four-corner-merging-datum
      requires a diagonal-unit estimate; def-extended-delta-inclusion
      has NO unit clause, so extended isomorphisms cannot supply it —
      thread ||v_W(I_{B_W}) - u_{A_W}|| <= t from the reset states
      through M12 / M19-S3 / M26 / M25 / M19-R (source near-unitality:
      prop_delta_hominc third clause, tex:1194-1196 — already a
      registered GT external in C3's workspace).
      (b) **maincb witness ledger**: M19-S1/M20–M28 use c_0^cb, L,
      e_env, e_1, e_s2, e_cross, K_1..3, K_call, epsilon_MAIN,
      r_reset as unquantified anaphors — af verifiers refuse anaphoric
      constants (the W93 lesson). Repair pattern PROVEN in-repo:
      def-stage1-polar-witness-data + rebound contracts (see the
      Stage-1 B-chain shards). Produce a def-maincb-witness-ledger +
      contract rebindings for the affected rows.
   2. User ratifies the package (defs + contract amendments).
   3. Then: complete M12 (parked 9/10, ONLY the unit clause open) and
      M19-S1 (parked 15/17, ONLY ledger nodes open) — both parked
      trees preserved in main `proofs/`; re-seed under the repaired
      contracts per the session-38 lesson (patched trees thrash,
      fresh builds close). Then M16, M17, M19-S2/S3/R, M20–M28.
   4. On M28 + M19-R: the escalated `lem-thmainext-conditional` rewire
      (design sect-10 step 15). Then the decoupled campaigns (14-row
      ledger, k-ledger, f0-assembly, root rewire LAST).
6. **Worked patterns (BINDING; follow verbatim):**
   - Provision: `python3 scripts/provision-af-row.py <rid>` + base
     `def-epsilon-cstar-algebra` (the M01/M14 lesson) + any
     vocabulary defs the contract uses (L2: no naked symbols — check
     delta-projection/compressed-corner especially).
   - Launch: worktree per run (`git worktree add --detach
     .claude/worktrees/af-<row> HEAD`), orchestrator from INSIDE the
     worktree, ONE backgrounded call (no inner `&` — the session-38
     orphan incident), tier routine, workers 4.
   - Balloon/stuck: transparent repair growth ⇒ scoped cap amendment
     (flag it; ceiling = repo cap 26); tangled/stale-premise tree ⇒
     clean RE-SEED (never patch a tree that architected around a
     missing provider); contract-level finding ⇒ STOP, escalate.
   - Bank: serial in main (rsync back → export → oracle → verify →
     flip → regenerate → check-all → fr log → commit → push).
7. **Parallel P2 / carried items:** `aism-9kmt` report sync (now banks
   120–151, ~31 results); v41 sketch is current; housekeeping items
   unchanged from session 37 (polar-retraction REFACTOR warning, \rm
   typeset flags — now also def-maincb-reset-state —, report/*.aux
   policy, dormant signed-trunk defs, `aism-ur9`, Gonzalez–Hartfiel /
   Flor lit-DB items).
8. **Orchestration laws (BINDING, session-38 amendments):** parallel
   worktree orchestrations ARE ratified (≤5 concurrent, serial
   banking); no design/audit codex while ANY af run is live; fr/bd
   writes FIRST, commit, launch LAST; codex = `gpt-5.6-sol`, xhigh
   cap, elevations tier routine. A verifier finding needing a
   CONTRACT/DEF change returns to design/user — session 38 exercised
   this three times; it works.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. `aism-jl4g` (P0): the two-defect design round → user ratification →
   M12/M19-S1 completions → M16–M28.
2. `lem-thmainext-conditional` rewire after M28+M19-R (escalated).
3. `aism-9kmt` report sync (P2, large).
4. Decoupled campaigns (14-row ledger, k-ledger, f0-assembly, root
   rewire LAST) toward `op-classical`.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 144. The MAIN
  campaign is 18/31 rows; the remainder is gated on ONE design round
  (`aism-jl4g`), not on elevation capacity.
- Any claim the vacuous M13 validation counts as mathematical
  content — it was flagged at bank time and SUPERSEDED by the
  non-vacuous run-4 validation under the user-ratified def amendment.
- The report anchoring of banks 120–151 (carried as `aism-9kmt`).
- Route X / XE decider work (fallback only); signed trunk PAUSED.
