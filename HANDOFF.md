<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (currently v24) + the rolling
   `docs/plans/CHANGELOG.md` (two-tier policy: small deltas live there — read the
   2026-07-10 entries: OR-routes landed; closure 12 -> 41).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves (the proof does not work while leaves are open — "value per effort" applies
   only WITHIN the leaf set); (ii) decompose by MECHANISM SEPARATION (the W56 wall:
   one-hard-leaf-after-free-preprocessing is certified dead); (iii) creativity mandate:
   proof-strategy subagents think outside the box, FINDINGS dead routes absolute;
   (iv) mostly serial; Fable = author-only for the hardest creative steps; verification
   fresh-codex-only, BATCHED by default for routine harvests (CLAUDE.md §6);
   (v) no progress theatre.
4. `fr board` + `bd ready`. Beads sync across devices: `scripts/beads-sync.sh import`
   after pull / `export` before push (committed JSONL, .beads/issues.jsonl).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-10, session 14 close)

**Rigorous (af-validated, T0): 29. Registry: 155** (incl. the two Phase-2 bridges'
final states). **op-classical's machine-checked ancestor closure: 41 nodes** — the
OR-route linker feature (routes: field) landed and op-hlc declares BOTH routes
(Kernel | MIN-A), so the three-cell SL1a surface, SL1b, L6.5, and the huddle system
are now FORMALLY reachable from the goal (was: prose only, closure 12).

**THE OPEN SURFACE (unchanged mathematically — six leaves):**
- **H-X** (`conj-sl1a-off-diagonal-cell`): T0-anchored by
  `lem-starvation-completion-obstruction` (af-validated; the W55-W59 arc). Named gaps
  to the cell: slab confinement / rank / tableau constants — the W60 generalization
  wave is THE next mathematical wave (sketch v24 item 0).
- **H-D**, **H-I** (the other two cells): genuinely open, no mechanism seed.
- **SL1b**: easiest sibling, still untouched.
- **L6.5 residuals**: E1-E5 codification, small-gauge bridge, mixed co-top straddle.
- **L5 dual-face mass minimax** (aism-vuc): independent; NOTE it is also the
  unregistered premise blocking the huddle assembly bridge (aism-pus) — closing it
  pays twice.

**Session 14 delivered (all pushed through 0e734ae):** the W55-W59 gadget arc
(T0 28 -> 29); the W56 three-cell SL1a surface; the FULL remediation program
(5-audit synthesis, epic aism-9s3): gate integrity hardened (OVERCLAIM tests,
un-vacuumed check-refs, anchor whitelist, quota fast-fail, widened overreach guard,
NODE_SOFT_CAP), ops tooling (codex-dispatch/build-workspace/beads-sync), docs
(CURRENT.md pointer, CHANGELOG, FINDINGS index, W59 wave doc), the LAB-BOOK OVERHAUL
(paper-track; typeset math; 13 T0 shards; codex fidelity 13/13 FAITHFUL), Phase 2
registry codification (10 defs, DAG wiring, 6 contracts shortened, halo rename), the
P0 OR-route feature, and the bridge hostile pass (one proved conditional, one INVALID
recorded in-shard, DO-NOT-CONSUME).

## Next steps (ranked) — W60+

0. **W60: the H-X generalization wave** (sketch v24 item 0): formulate the
   moment-vs-budget ledger at the H-X tableau; decide which of (slab confinement /
   rank / tableau constants) is the binding gap. Strategy pass (creative, out-of-box
   prompt) then prover; batched verification.
1. **L5 minimax** (aism-vuc): now double-valued (leaf + the assembly-bridge premise).
2. **E1-E5 codification + the small-gauge bridge** (fresh standalone passes; batched).
3. **The assembly-bridge repair** (aism-pus): codify l2-attack §2.6-2.7 intersecting-
   hulls -> SL1a/SL1b as a registry lemma + register the L5 premise; re-verify.
4. **SL1b** (easiest), **H-D/H-I** (need creative mechanism waves; Fable candidates).
5. Parked: af-elevation queue (defs now exist for the contract shortening that gated
   lem-top-deficit-price — aism-88r), aism-l1a (P2 polish), aism-cei (P1 af->Lean
   trunk scoping), refs ingest (aism-5de). USER DECISIONS: aism-nlg (contract
   rewording, awaiting your call), aism-z98 (DAG-blocked, not actually a user decision).

## Standing rules (delta from session 13)

Everything in CLAUDE.md §6 incl. the NEW batched-verification default. codex =
gpt-5.6-sol (ultra creative / xhigh verify / high routine); quota outages: wrap long
dispatches in `scripts/codex-dispatch.sh` (probe + reset-parse + retry). Worker
workspaces: `scripts/build-workspace.sh <dir> [--waves ...] [--plans ...]`. Oracle
registration: `scripts/register-oracle.py <rid>`. New sketch file => re-run
`python3 scripts/gen-current-pointer.py` (gated). Session close: beads-sync export
before push. The methodology decisions of record:
`docs/plans/2026-07-10-methodology-assessment.md` (do not relitigate what
demonstrably works).

## What is intentionally NOT here

- Any claim more than TWENTY-NINE results are af-validated; L5 is not L0.
- Any claim any leaf, the huddle charge, the Kernel Conjecture, or op-classical is
  proved. `lem-huddle-charge-assembly` is INVALID-as-stated (in-shard verdict):
  DO NOT CONSUME until aism-pus lands.
- Any claim the three-cell surface is strict progress (SL1a == the conjunction);
  the OR-route closure growth is CODIFICATION of the known map, not new mathematics.
