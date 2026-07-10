<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (currently v25) + the rolling
   `docs/plans/CHANGELOG.md` (two-tier policy: small deltas live there — read the
   THREE 2026-07-10 W61 entries: engine pair validated; both deciders decided;
   engine bank complete at the oracle rung).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) decompose by MECHANISM SEPARATION (the W56 wall is certified dead);
   (iii) creativity mandate for proof-strategy subagents, FINDINGS dead routes
   absolute; (iv) mostly serial; Fable = author-only for the hardest creative steps;
   verification fresh-codex-only, BATCHED by default for routine harvests
   (CLAUDE.md §6); (v) no progress theatre.
4. `fr board` + `bd ready`. Beads sync across devices: `scripts/beads-sync.sh import`
   after pull / `export` before push (committed JSONL, .beads/issues.jsonl).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-10, session 16 — W61 banked)

**Rigorous (af-validated, T0): 34. Registry: 158.** Session 16 (W61) af-validated
the ENTIRE W60 engine bank (serial orchestration train, fresh codex verifier per
node, taint clean everywhere): `lem-hx-transverse-moment-identity` (14/14),
`lem-hx-robust-scalar-starvation` (12/12, the T0-generalization proper),
`lem-hx-signed-variation-ledger` (11/11), `lem-hx-financing-floor` (12/12 on a
CORRECTED contract), `lem-hx-forced-exterior-coupling` (12/12). **One retraction
(docs/LEARNINGS.md):** the floor's W60 contract quantified 'all reals A' — false at
A < 0 with N empty (af challenge ch-9388e571, concrete counterexample); restated to
the A > 0 form the W60 proof establishes; consumers unaffected (A·l = 1/2 / A ≥ 4).
The af oracle caught what BOTH the W60 prover and the batched hostile verifier
missed.

**BOTH aism-ur9 route-fork L3 deciders are DECIDED and banked** (exact-rational,
orchestrator-reproduced; synthesis in
`docs/waves/2026-07-10-W61-deciders-and-elevation.md`):
- **Decider A (X2 graft refuter): X2 NOT refuted.** The exact six-row factorized
  graft family achieves Gamma_f -> 1, M_X -> 3/4, T_B -> 0 and every checked
  selected-corner clause EXCEPT tallness (H = O(tau^3) << 16*tau, asymptotic).
  Route A's X2 prove-or-refute lane is genuinely open; tallness is the
  load-bearing hypothesis. Bundle: `runs/2026-07-10-w61-x2-graft-refuter/`.
- **Decider B (leak-financing refuter): FINANCING INSTANCE FOUND (local N5(ii)
  geometry).** The unconfined freight row pays the full engine demand with every
  banked ledger slack. The ledger-only close of N5(ii) is dead as budgeted:
  restating N5 with a freight-row/Gamma_f coupling budget is a Route-B
  PREREQUISITE. Bundle: `runs/2026-07-10-w61-leak-financing-refuter/`.
- **Convergent signal: TALLNESS (H > 16*tau) is the binding wall in both
  searches** — the resource the adversary cannot manufacture and the current
  ledgers do not consume.

**LIVE USER DECISION (aism-ur9), now fully informed:** Route A (codex named-H-X via
X2/X3F/X3N/X4; X2 lane open, tallness flagged) vs Route B (Fable
gamma-renegotiation via N4 + N5/N6; N5 restatement now a prerequisite, price +1
routine-hard). The engine bank is rigorous and consumable by BOTH routes and L6.5.

**THE OPEN SURFACE (six leaves, unchanged):** H-X (route fork above), H-D, H-I,
SL1b, L6.5 residuals, L5 dual-face mass minimax (aism-vuc, double-valued — also the
unregistered premise of the huddle assembly bridge aism-pus).

**Process lessons (binding, in the W61 wave doc):** af orchestrations are STRICTLY
SERIAL (the overreach guard is REPO-WIDE and flags any new dirt vs run start —
sibling workspaces, wave-doc drafts, even fr log writes); while a run is live the
tree stays completely clean and any necessary repo write (fr log) is committed
within seconds; wrapper logs go to the scratchpad.

## Next steps (ranked) — W62+

0. **The route fork (aism-ur9, USER DECISION — now decider-informed).** On decision:
   Route A -> first creative wave per DECOMPOSITION-W60-CODEX.md §4 (X2 as
   prove-or-refute decider with the graft family as stress fixture; X3N/X3F
   parallel). Route B -> N5 restatement (freight-row/Gamma_f budget) + gamma-dial
   memo FIRST, then N6-before-N5 creative order per DECOMPOSITION-W60-FABLE.md §4.
   Either way the tallness signal suggests the winning mechanism must CONSUME
   H > 16*tau quantitatively.
1. **L5 minimax (aism-vuc)**: double-valued (leaf + assembly-bridge premise).
2. **Paper-track reproduction of the five validated engine lemmas (aism-mg7)** —
   T0 results belong on the paper-track; currently UNWIRED-whitelisted.
3. **E1-E5 codification + small-gauge bridge** (batched); **assembly-bridge repair**
   (aism-pus).
4. **SL1b** (easiest), **H-D/H-I** (creative mechanism waves; Fable candidates).
5. Parked: af-elevation queue (aism-88r), aism-l1a (P2 polish), aism-cei (P1
   af->Lean trunk scoping), refs ingest (aism-5de), aism-nlg / aism-z98 (user
   decisions).

## Standing rules (delta from session 15)

Everything in CLAUDE.md §6 incl. batched verification default. codex = gpt-5.6-sol
(ultra creative / xhigh verify / high routine); wrap long dispatches in
`scripts/codex-dispatch.sh` (point --log OUTSIDE the repo during orchestrations).
Worker workspaces: `scripts/build-workspace.sh`. NEW (W61): orchestration guard
discipline above; validated-deps flip order (dep before consumer); af export via
stdout redirect (`af export -d <ws> > <ws>/export.md`). Methodology decisions of
record: `docs/plans/2026-07-10-methodology-assessment.md`.

## What is intentionally NOT here

- Any claim more than THIRTY-FOUR results are af-validated.
- Any claim any leaf, the huddle charge, the Kernel Conjecture, or op-classical is
  proved. The deciders are L3 EVIDENCE: decider A does not prove X2; decider B does
  not refute N5/N6 as mathematical conjectures (tallness + Gamma_f clauses fail in
  its instance; N6 untouched).
- Any claim the route fork is decided — it remains with the user (aism-ur9).
- `lem-huddle-charge-assembly` remains INVALID-as-stated / DO-NOT-CONSUME
  (aism-pus).
