<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The governing plan is the RATIFIED W78 package as executed through the
   endorsed W97 rebuild and the S1-POLAR-v6 serial order — **which is now
   COMPLETE through the downstream quotient block**. The proof sketch is
   `docs/plans/CURRENT.md` → **v39** (fresh, reconciled with this
   session's banks).
3. **Rigorous (af-validated, T0): 117.** Registry: 298. `op-classical`
   OPEN.
4. **SESSION-36 HEADLINE (2026-07-29): FOUR elevations banked
   (120th→123rd, T0 113→117); the designed Stage-1 elevation surface is
   EXHAUSTED; every remaining front needs a design cycle or a user
   decision.**
   - `lem-stage1-quotient-left-inversion` (120th; 10 nodes; one
     challenge repaired in-ledger with two verified bridging substeps).
   - `lem-stage1-quotient-inversion-index-data` (121st; 12 nodes; two
     derivative-branch challenges repaired incl. explicit local slice
     charts; the audit-mandated square-root phase-lift validated).
   - `lem-topology-finite-triangulation` (122nd; first-pass ZERO
     challenges on the SECOND clean re-seed; bead `aism-j5t9` CLOSED).
   - `lem-stage1-quotient-finite-cw` (123rd; first-pass ZERO
     challenges; the quotient is a finite polyhedron / finite CW).
   - The Stage-1 topological substrate for Lefschetz–Hopf (connected
     finite-CW H-space with left inversion; isolated index-+1 fixed
     point) is now fully T0.
5. **PROCESS FINDING (FINDINGS.md 2026-07-29, read before ANY external
   registration): the scan-OCR locus trap.** `splitlines()` counts
   form-feed page separators as line breaks; sed/grep -n do not; a
   wrong-passage quote still PASSES `check-refs` (it checks
   quote-exists-somewhere, not quote-at-locus). One STUCK run validated
   5 nodes against corrupted externals (discarded; verification
   near-miss recorded — a verifier does not audit external content
   against refs/). Registration rule now: extract in `\n`-only space,
   verify quote-at-claimed-locus programmatically, eyeball the page
   image.
6. **NEXT SESSION — all fronts are decision-gated (beads filed):**
   1. **`aism-tpai` (P1): G-S1 design cycle** — the three Stage-1 split
      producers are ABSENT from the registry (the one remaining
      critical-path design gap; blocks M19-S1..M28). Fresh codex design
      + hostile audit in a zero-live-run window; landing the three
      contracts needs USER ratification (W78/W97 precedent).
   2. **`aism-dm8n` (P1): MAIN P0 definition gate (USER)** — 4
      datum-only defs (hard stop before M01); then land M01/M02 (+ the
      other pre-gate rows) and REWIRE M03's deps per
      `DESIGN-MAIN-STRUCTURE-v5` (do NOT elevate M03 against its
      current registry deps).
   3. **`aism-9kmt` (P2): report paper-track sync** for banks 120–123
      (session-35 worktree-subagent pattern) + carried shard-51
      `\ref` upgrades + retired-parent wording refresh.
   4. **`aism-65j4` (P2): commission the trace-row designs** (§9 steps
      28–29 + corrected `lem-stage1-extra-fixed-class`).
   5. Decoupled: the 14-row ledger campaign, then k-ledger (D4
      releases), f0-assembly, root rewire LAST (v39 open surface).
7. **Banking sequence (verified ~33×):** af export (md+tex) → per-id
   oracle appended to `.frontier/portfolio.json` (absolute paths) →
   `fr verify proofs/<rid>/export.md --oracle af-<rid>` → mechanical
   shard flip → regenerate (`argument.py --generate`,
   `gen-report-dag.py`, `gen-report-stats.py --extract`) → check-all →
   `fr log FH banked --artifact <export> --tier T0` → commit → push.
8. **Orchestration laws (BINDING):** af runs strictly sequential; no
   design/audit codex job while an af run is live; non-`.frontier/` repo
   writes abort live runs as PROVER-OVERREACH (subagents during a live
   run → ISOLATED WORKTREES); fr/bd writes FIRST, commit, launch LAST;
   commits only in zero-live-run windows. Codex = `gpt-5.6-sol`, xhigh
   cap (prover xhigh ONLY after a STUCK). A hard-cap hit is a factoring
   stop. Seeding pattern per shard: seed-af-workspaces.py (round-trip)
   + def-add per def (full shard file) + add-external per T0 dep
   (registry contract verbatim, literal `proofs/<dep>` path) + BINDING
   build-granularity note (one node per design-skeleton step) — 3 of 4
   runs this session landed first-pass or with ≤2 repaired challenges
   under it.
9. Gate: `sh scripts/check-all.sh` → `[check-all] OK` (verified at
   close). All work committed AND pushed. NOTHING is in flight.

## Next steps (ranked)

1. Item 6.1/6.2: the two P1 decision beads (G-S1 design; MAIN P0 defs)
   — both need the user; the G-S1 design JOB itself can be dispatched
   in a zero-live-run window once the user green-lights the cycle.
2. Item 6.3: report sync for the four new banks (P2, mechanical
   pattern, safe to do next session without decisions).
3. Literature follow-up carried from session 35: Gonzalez–Hartfiel 1991
   (LAA 145, on the stochastic idempotent matrix space) not in the lit
   DB; decide whether to queue in RESEARCH_NOTES.md (needs
   institutional access). Flor 1969 acquired + hash-verified, never
   promoted (uncited).
4. Carried housekeeping: polar-retraction 29-node REFACTOR warning
   (cosmetic); `def-stage1-polar-witness-data` `\rm` typeset flag;
   report/*.aux policy; repo-root-relative oracle paths (`aism-2kyc`);
   12 dormant signed-trunk draft defs; `aism-ur9` (dormant); two stale
   pre-session-33 agent worktrees under `.claude/worktrees/` (verify
   merged/stale before removing).

## What is intentionally NOT here

- Any claim `op-classical` is proved — OPEN. T0 = 117 covers the
  Route-F row chain and the ENTIRE Stage-1 polar block through
  quotient-finite-cw; everything beyond (G-S1 producers, MAIN rows,
  trace rows, ledger campaigns) remains non-rigorous/absent until
  designed, landed, and validated.
- Any claim the G-S1/MAIN/trace designs WILL land or validate — each is
  tested only by its own audit and elevation.
- The two retired parents re-elevating — retired in place per the
  endorsed design.
- Route X / XE decider work (fallback only). Signed trunk PAUSED.
