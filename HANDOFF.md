<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v34**, 2026-07-26 — reconciled
   with sessions 27 AND 28; the v33 reconciliation debt is CLEARED). Stewardship mandate
   binding (Rule 9).
3. **Rigorous (af-validated, T0): 82.** Registry: 264. Session 28 (2026-07-26, this device)
   banked SIX elevations:
   `lem-topology-lefschetz-hopf` (77th, 2 nodes), `lem-topology-kunneth-cross-product`
   (78th, 7), `lem-topology-orientable-top-cohomology` (79th, 14),
   `lem-topology-quotient-manifold` (80th, 4), `lem-topology-hopf-structure` (81st, 13),
   and **`lem-extcb-exact-target-correction` (82nd, 6 nodes, first-pass, zero challenges) —
   GAP-EA, the first of the four v4.1 GAP families, is DISCHARGED at L0** (aism-fbh8 closed;
   design cycle: codex design job → `docs/plans/2026-07-26-GAP-EA-design/DESIGN-GAP-EA.md`
   option (a) → verbatim landing → 6-node elevation exactly on budget).
4. **USER DECISIONS PENDING (two new, filed as P1 beads):**
   (a) **IMPROVE-CB contract narrowing** (DESIGN-GAP-EA §2.3/§4.8): add the pinned source's
   finite-dim-source + ε ≤ ε_max^cb hypotheses before `lem-maincb-error-improvement` seeds;
   also its dep switches to the general correction row. Register MODIFICATION — outside the
   verbatim delegation. Do NOT seed IMPROVE-CB unnarrowed.
   (b) **`lem-topology-local-index-sign` scope gap** (21/23 validated, parked): the contract's
   unqualified C¹ self-map exceeds `def-lefschetz-fixed-point-data`'s compact-orientable
   scope. Narrow the contract (checking the `lem-stage1-extra-fixed-class` consumer) vs
   re-scope the def (L2 ripple).
5. **Two parked topology trees** (ledgers preserved, both ~90% validated):
   `finite-triangulation` (19/23; node-1.5 modus_ponens bookkeeping thrash — process repair
   bead filed) and `local-index-sign` (see 4b). The other five topology rows are T0.
6. **ORCHESTRATION LAWS (session 28, banked to bd memory — READ BEFORE RUNNING af):**
   (i) af orchestrations are strictly SEQUENTIAL per checkout (parallel runs mutually abort
   via the porcelain-snapshot overreach guard); (ii) pre-create any new repo dir a codex job
   will write mid-run; (iii) commits land ONLY in zero-live-run windows — the Stop-hook-forced
   fr logging appends to `.frontier/log.jsonl` and kills a live run whose baseline was
   committed-clean. All seven session-28 aborts were process-level; zero mathematical
   refutations (campaign total stays 2,386+ adversarial jobs, zero route-level refutations).
7. **fr circuit-breaker is ARMED: FH "stalled ×2"** (elevations bank T0 but don't move the
   OPEN line). The logged decision is **EXPLORE XE next cycle** (Route X deciders:
   aggregate-peak, QCMP ratio, quotient-refinement/cross-financing) before further FH
   exploitation. Do not relax the breaker (Rule 5 / §9).
8. Standing user mandates (2026-07-26, unchanged): codex = `gpt-5.6-sol`, effort capped
   `xhigh`; batched verification default; banking precedent (validated root replaces contract
   verbatim); ratification-queue delegation (verbatim provisioning only, modifications
   escalate); signed trunk PAUSED.
9. `fr board` + `bd ready`; beads sync via `bash scripts/beads-sync.sh export` at close.
10. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-26, session 28 close)

Session 28 = the af-elevation campaign orchestrated end-to-end under the user mandate "work
through the af elevations, look for blockers/strange behaviour": 7 workspaces seeded with 11
byte-matched refs externals (+1 more at GAP-EA seeding, check-refs all green), 6 elevations
banked (5 topology + GAP-EA correction), 2 precise diagnoses on the parked trees, 3
orchestration-infrastructure laws discovered and codified, the GAP-EA design→land→seed→elevate
cycle completed in-session, and the v34 sketch delta clearing the Rule-9 reconciliation debt
(sessions 27+28). All work oracle-verified (`fr verify` PASS ×6) and committed.

## Next steps (ranked)

1. **Honor the breaker: XE decider wave** (aism-ea2f) — aggregate-peak / QCMP ratio /
   quotient-refinement deciders; then return to FH exploitation.
2. **User decisions 4a/4b** unblock: IMPROVE-CB seeding (after narrowing) and the
   local-index-sign finish.
3. **Bridge row elevation** (`lem-extcb-exact-target-approximation`, 2–3 nodes, bead filed) —
   cheap, unblocked now.
4. **GAP-LEDGER-DOMAINS** (the largest remaining family): 14 per-row codex derivations of
   dependency-produced local radii per v4.1 §D ordering; `lem-routef-k-finiteness` last.
5. **GAP-S1-POLAR-CONTRACT + GAP-MAIN-STRUCTURE**: polar contracts, then the eight MAIN
   `stated` targets (gated on 4a).
6. **finite-triangulation repair** (bead filed): re-type node 1.5's inference or archive+
   restate; then a short finishing run.
7. Housekeeping (carried): `report/sections/*.aux` tracking policy; repo-root-relative oracle
   paths; the 12 dormant signed-trunk draft defs.

## What is intentionally NOT here

- Any claim `op-classical` is proved. It is OPEN. T0 = 82; the GAP families
  (LEDGER-DOMAINS, S1-POLAR, MAIN-STRUCTURE), the assemblies
  (`lem-thmainext-conditional`, `lem-routef-k-ledger`, F0/F2/F3), and phase 5 remain
  design-only or `proved-mod-audit`/`stated`. The LEARNINGS 2026-07-26 partial retraction
  stands: fresh proofs with derived local domains ARE needed on the demoted rows.
- Any promise the remaining GAP families will close — expected but not banked.
- Signed-trunk movement (RDSE/LDHR-48 stay PAUSED per standing directive viii).
