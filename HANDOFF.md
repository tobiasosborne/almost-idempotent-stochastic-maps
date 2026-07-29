<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v39**. The Stage-1
   polar substrate is COMPLETE (every designed-and-landed Stage-1
   elevation target af-validated). The live campaign is the **S1-ENDGAME
   design cycle** (bead `aism-tpai`, claimed): the chain from the T0
   substrate to the three G-S1 producers.
3. **Rigorous (af-validated, T0): 117.** Registry: 298. `op-classical`
   OPEN.
4. **SESSION-36 RECORD (2026-07-29), two phases:**
   - **Phase 1 — four elevations banked (120th→123rd, T0 113→117):**
     `lem-stage1-quotient-left-inversion` (10 nodes, 1 challenge
     repaired), `lem-stage1-quotient-inversion-index-data` (12 nodes, 2
     challenges repaired, square-root phase-lift validated),
     `lem-topology-finite-triangulation` (first-pass 0-challenge on the
     second clean re-seed; `aism-j5t9` CLOSED),
     `lem-stage1-quotient-finite-cw` (first-pass 0-challenge). The
     Lefschetz–Hopf substrate (connected finite-CW H-space with left
     inversion; isolated index-+1 fixed point) is fully T0.
   - **Phase 2 — the S1-ENDGAME design cycle (user green-lit), 1.5
     rounds run:** BRIEF → DESIGN v1 → hostile AUDIT v1 = **REDESIGN**
     (findings: A1 bialgebra antecedent invalid for a non-associative
     H-space; B1/C1 untyped same-`breve-sigma`/same-inversion witnesses
     — the 13e defect family; C1 budget implausible; G-S1 alone does
     not unblock M19) → BRIEF v2 → **DESIGN v2 LANDED, UNAUDITED**
     (`docs/plans/2026-07-29-S1-ENDGAME-design/DESIGN-S1-ENDGAME-v2.md`,
     428 lines: weak-coproduct conditions replace the bialgebra
     antecedent — cites Hatcher, ground-truth availability UNVERIFIED;
     two typed synchronization helper rows; a fixed-unitary projection
     bridge row; 3 new helper rows total, zero new defs, budgets ≤15).
     The graceful stop landed here — **audit v2 was deliberately NOT
     dispatched.**
5. **PROCESS FINDING (FINDINGS.md 2026-07-29):** the scan-OCR locus trap
   — `splitlines()` counts form feeds as lines; `check-refs` passes any
   verbatim quote regardless of claimed locus; a verifier does NOT audit
   external content against refs/. Registration rule: `\n`-only
   extraction + programmatic quote-at-locus check + page-image eyeball.
6. **NEXT SESSION STARTS HERE:**
   1. **Dispatch the fresh hostile AUDIT v2** over
      `DESIGN-S1-ENDGAME-v2.md` (fresh codex xhigh, verdict to
      `AUDIT-S1-ENDGAME-v2.md`; reuse the v1 audit prompt shape — see
      the audit-v1 commit `bf7dc57a` / the eight attack fronts; ADD:
      verify the Hatcher weak-coproduct claim against LOCAL ground
      truth — if Hatcher is not in `refs/`, that is an L1 stop the
      designer must re-route or we acquire the source).
   2. On LAND / LAND-WITH-CORRECTIONS: assemble the **user ratification
      package** (7+3 = ten row contracts, zero new defs, one new
      external `prop_delta_hominc` tex:1194-1196) — NOTHING lands
      without user sign-off. On REDESIGN: BRIEF v3 with the findings,
      one more round.
   3. After ratification: land shards → seed per the verified pattern
      (HANDOFF §8 of session 36 phase 1, incl. the locus-trap rule) →
      elevate serially per the design's order → G-S1 gate discharged →
      then the MAIN campaign still needs `aism-dm8n` (P0 defs, USER) +
      M01–M18.
   4. Parallel P2 items: `aism-9kmt` (report sync for banks 120–123),
      `aism-65j4` (now largely subsumed by the S1-ENDGAME design —
      close or re-scope it when the design lands).
7. **Banking sequence (verified ~33×):** af export (md+tex) → per-id
   oracle appended to `.frontier/portfolio.json` → `fr verify` →
   mechanical shard flip → regenerate (argument.py --generate,
   gen-report-dag.py, gen-report-stats.py --extract) → check-all →
   `fr log FH banked --artifact <export> --tier T0` → commit → push.
8. **Orchestration laws (BINDING):** af runs strictly sequential; no
   design/audit codex job while an af run is live; fr/bd writes FIRST,
   commit, launch LAST; commits only in zero-live-run windows. Codex =
   `gpt-5.6-sol`, xhigh cap. A hard-cap hit is a factoring stop; a
   verifier finding needing a CONTRACT change returns to design/user.
   Design-cycle pattern (validated this session): BRIEF → fresh-codex
   design → SEPARATE fresh-codex hostile audit → repair rounds → user
   ratification → land → elevate.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. **NOTHING is in flight.**

## Next steps (ranked)

1. Item 6.1: dispatch hostile audit v2 (the one queued action).
2. Items 6.2–6.3: the ratification → land → elevate pipeline.
3. `aism-dm8n` (MAIN P0 defs, USER decision) — independent of the
   S1-ENDGAME outcome; can be ratified any time.
4. `aism-9kmt` report sync (P2, mechanical).
5. Literature follow-up carried: Gonzalez–Hartfiel 1991 (LAA 145) not
   in the lit DB; Flor 1969 acquired + hash-verified, never promoted.
6. Carried housekeeping: polar-retraction 29-node REFACTOR warning
   (cosmetic); `def-stage1-polar-witness-data` `\rm` typeset flag;
   report/*.aux policy; repo-root-relative oracle paths (`aism-2kyc`);
   12 dormant signed-trunk draft defs; `aism-ur9` (dormant); two stale
   pre-session-33 agent worktrees under `.claude/worktrees/`.

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 117.
- Any claim DESIGN-S1-ENDGAME-v2 is sound — it is UNAUDITED; audit v1
  of its predecessor returned REDESIGN, and v2's Hatcher ground-truth
  claim is unverified (L1 flag for the auditor).
- Any registry/def change from the design cycle — NOTHING landed; the
  registry is byte-identical to the post-bank state (T0 117).
- The two retired parents re-elevating; Route X / XE decider work
  (fallback only); signed trunk PAUSED.
