<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The governing plan is the RATIFIED
   **`docs/plans/2026-07-27-W78-ratification-package.md`** (D1–D4). The live
   campaign bead is **`aism-kqeb` (W80)**. The proof sketch is
   `docs/plans/CURRENT.md` → **v36** (2026-07-28; folds the sessions 31–33
   T0 gains — Rule-9 debt is CLEAR).
3. **Rigorous (af-validated, T0): 107.** Registry: 295. Definitions: 45.
   `op-classical` OPEN.
4. **Session-33 arc (T0 106 → 107):**
   - **Transport 13g `lem-stage1-inversion-derivative-transport`
     af-VALIDATED (107th)** — but it took TWO runs. Run 1 (tier routine)
     ABORTED [STUCK] at 15/16 validated: the workspace had been seeded
     with ONLY the parent control external, whose contract binds
     u_delta/g_{sJ} as bare anaphors, so three root premises were
     underivable from the exact allowed inputs (E1 u_delta =
     Pi_delta-inverse first component; E2 g_{sJ}'s f_{sJ}/C^1
     characterization; E3 sigma globally C^1). Unlike 13e, all three are
     carried VERBATIM by existing T0 results, so the fix was a
     13e-precedent DEPS-ONLY widening (contract byte-unchanged):
     + polar-retraction (E1), unitary-graph-control (E2),
     smooth-unitary-operations (E3) + its three antecedents
     (approximate-group-laws, smooth-unitary-atlas, smooth-polar-inverse);
     workspace wiped + re-seeded (round-trip OK), all 7 deps registered as
     byte-matched af externals. Run 2 validated 13/13 clean in 6 rounds.
     **LESSON (transport seeding): a transport workspace must import the
     providers of every definite description its root binds explicitly,
     not only its direct parent.**
   - **W96: THE REPORT IS FULLY CAUGHT UP.** Two worktree agents wrote
     shards 49 (AISM-49: smooth-polar-inverse 99th,
     smooth-unitary-operations 100th, polar-scalar-arithmetic 101st) and
     50/51 (AISM-50/51: the six transports 102nd–107th, incl. the 13g
     STUCK/widening record); merged in the main checkout with genuine
     full gates (3-way merge of the five shared files; one stale
     cross-remark in 51 re-pointed at 49's labels). UNWIRED −9;
     PROVENANCE +18 source +9 claim rows. ALL 107 T0 results are now
     anchored on the paper track or deliberately whitelisted; zero
     unanchored ids.
   - **Sketch v36** written and pointed
     (`docs/plans/2026-07-28-top-down-proof-sketch-v36.md`).
   - Housekeeping: NODE_SOFT_CAP brittleness-prose drift fixed
     (CLAUDE.md/AGENTS.md L4 + §6, argument/README.md gate 5 now name
     `scripts/af_constants.py NODE_SOFT_CAP = 26`).
5. **13e `lem-stage1-approximate-group-laws-transport` is PAUSED — USER
   DECISION `aism-b5hz` — and it now BLOCKS THE CRITICAL PATH.** Three
   STUCK runs (last with prover xhigh) converged on a genuine
   ratified-contract interface defect: the group-laws family binds
   u_delta by the ELLIPTICAL description "the inverse u_delta of the
   polar map", while the ratified 13e transport contract binds
   (u_delta, h_delta) EXPLICITLY as the unique inverse of Pi_delta. The
   identification u_grp = u_pol needs a typed polar datum the parent
   contract never exposes — formally underivable from ANY validated
   externals (three independent verifier cohorts; 13g's success shows the
   widening fix does NOT apply here — no T0 result supplies the missing
   datum). Workspace intact, 28/37 validated. Options in the bead:
   (A) mini design/audit cycle restating 13e's binder anaphorically
   (deviates from ratified text — needs ratification; check what row 13
   needs first); (B) explicit-binder amendment of the group-laws family +
   re-elevation (3 af-validated contracts touched); (C) fresh codex
   design round. Do NOT re-run 13e unchanged (it will STUCK again).
6. **NEXT SESSION: resolve `aism-b5hz` first.** Row 13
   (`lem-stage1-polar-constant-ledger`, the 8-way conjunction) consumes
   ALL SEVEN transports and is blocked until 13e closes; behind it queue
   maximal-simplex + the 5 downstream rows, then polar §9 steps 28–29
   (blocked on their own audited designs), package §5 step 3 (G-S1 split
   producers), MAIN (`DESIGN-MAIN-STRUCTURE-v5.md` §10), the 14-row
   ledger, the strengthened k-ledger, f0-assembly, root rewire LAST.
   There is NO other unblocked critical-path elevation work.
7. **Banking sequence (verified ~18× total):** af export (md+tex) →
   append per-id oracle to `.frontier/portfolio.json` (`af-<rid>` /
   `scripts/oracles/af-validated.py <rid>` / ledger+shard inputs,
   absolute paths; NOTE the oracle reads the claim on STDIN — a bare
   invocation without stdin hangs) → `fr verify proofs/<rid>/export.md
   --oracle af-<rid>` → flip shard mechanically (status: proved /
   af: validated + body Status update) → regenerate
   (`argument.py --generate`, `gen-report-dag.py`,
   `gen-report-stats.py --extract`) → check-all → `fr log FH banked
   --artifact <export> --tier T0 --decide EXPLOIT FH` (the bank gate
   accepts `banked` ONLY for oracle-verified artifacts; documentation
   waves log `progress`) → commit → seed the next row in the same commit
   window.
8. **Orchestration laws (BINDING):** af runs strictly sequential; no
   design/audit codex job while an af run is live; any non-`.frontier/`
   repo write aborts a live run as PROVER-OVERREACH (`.frontier/` is
   exempt — fr logging mid-run is safe); fr/bd writes FIRST, commit, af
   launch as the turn's LAST action; commits only in zero-live-run
   windows; `git push` allowed while a run is live.
9. Standing mandates: codex = `gpt-5.6-sol`, xhigh cap (escalate prover
   to xhigh ONLY after a STUCK; factor per a fresh design cycle ONLY
   after a BALLOON); batched verification default; NOTHING lands without
   ratification (D1–D4 envelope) — deps-only widenings with the contract
   byte-unchanged are the recorded harmless exception (13e/13g
   precedent); Route X/XE fallback only; signed trunk PAUSED.
10. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
    close). All work committed AND pushed.

## Next steps (ranked)

1. **`aism-b5hz`: USER DECISION on the 13e interface defect** — the only
   non-resource blocker on the Route-F critical path (see item 5).
2. After 13e: seed + elevate **row 13 `lem-stage1-polar-constant-ledger`**
   (consumes all seven transports), then maximal-simplex + the 5
   downstream rows.
3. Polar §9 steps 28–29 (three separately-designed trace rows + corrected
   `lem-stage1-extra-fixed-class`) — blocked on their own audited
   campaign designs.
4. Package §5 step 3 (G-S1 split producers) once rows 1–13 are T0.
5. Carried housekeeping: `aism-j5t9` (Munkres C^r-triangulation def
   external); polar-retraction 29-node REFACTOR warning (cosmetic);
   `def-stage1-polar-witness-data` body uses `\rm` (gen-report-defs
   warning-level flag each run); report/*.aux tracking policy;
   repo-root-relative oracle paths (would also let the worktree test-skip
   retire); 12 dormant signed-trunk draft defs; `aism-ur9` (dormant);
   two stale pre-session-33 agent worktrees under `.claude/worktrees/`
   (agent-a745…, agent-ad79… — verify merged/stale before removing).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 107 covers the Route-F
  row chain, polar analytic rows 1–12, and transports 13a–d, f, g.
  Transport 13e (paused), row 13, maximal-simplex, the 5 downstream rows,
  G-S1, MAIN, the 14-row ledger, the strengthened k-ledger, f0-assembly,
  and the root rewire all remain non-rigorous.
- Any promise 13e resolves without a ratified contract change — three
  independent verifier cohorts established the underivability; the 13g
  deps-widening fix does NOT transfer (no T0 provider exists for the
  group-laws binder).
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
