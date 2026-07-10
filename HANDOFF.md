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
   FOUR 2026-07-10 W61/W62 entries: engine pair validated; both route-fork
   deciders decided; engine bank complete at the oracle rung; the L5 minimax
   decomposed with its routine batch proved).
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

## Current state (2026-07-10, session 16 — W61 + W62 banked)

**Rigorous (af-validated, T0): 34. Registry: 162.** Session 16 (W61) af-validated
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

**W62 (same session): the L5 minimax DECOMPOSED, routine batch PROVED.** Strategist
tree banked (`docs/waves/2026-07-10-W62-artifacts/DECOMPOSITION-W62-L5.md`):
binding gap re-verdicted as an engine-payer mass-transport dual on the owned
barycenter q_A (the W54 finite-cover framing retired). Routine batch R0-R3 proved
at L5 (4/4 VALID, fresh batched hostile verifier, zero corrections; registry
158 -> 162): `lem-l5-mass-barycenter-dualization`, `lem-l5-top-face-ray-formula`,
`lem-l5-positive-flow-foldback`, `lem-l5-universal-exterior-payer` (row v pays
tau*S/8 outside EVERY half-ball, ceiling min{1/16,(c_m/8)^2} — first consumer of
the W61 T0 engine outside H-X). **L5-GAP-1 residual == the S/C/I creative fork**
(shallow payer / drift-width chord / isotropic web; disjoint-exhaustive on the
proved interface). I-horn refuter batch: ALL BLOCKED
(`runs/2026-07-10-w62-i-horn-refuter/`) — **tallness binds for the 3rd consecutive
independent refuter search**; width gate independently repels the fan. Non-proof
green light for the I-first creative wave (aism-5wow).

**THE OPEN SURFACE (six leaves):** H-X (route fork above), H-D, H-I, SL1b, L6.5
residuals, L5 minimax — the last now reduced to the S/C/I horns (aism-vuc; still
double-valued: also the unregistered premise of the huddle assembly bridge
aism-pus, whose premise wording should now be the L5-GAP-1 statement that
lem-l5-mass-barycenter-dualization converts).

**Process lessons (binding, in the W61 wave doc):** af orchestrations are STRICTLY
SERIAL (the overreach guard is REPO-WIDE and flags any new dirt vs run start —
sibling workspaces, wave-doc drafts, even fr log writes); while a run is live the
tree stays completely clean and any necessary repo write (fr log) is committed
within seconds; wrapper logs go to the scratchpad.

## Next steps (ranked) — W62+

0. **The route fork (aism-ur9, USER DECISION — now decider-informed)** and/or
   **the I-horn creative wave (aism-5wow)** — both fully teed up; the L5 line
   does not need the fork decision. On decision:
   Route A -> first creative wave per DECOMPOSITION-W60-CODEX.md §4 (X2 as
   prove-or-refute decider with the graft family as stress fixture; X3N/X3F
   parallel). Route B -> N5 restatement (freight-row/Gamma_f budget) + gamma-dial
   memo FIRST, then N6-before-N5 creative order per DECOMPOSITION-W60-FABLE.md §4.
   Either way the tallness signal suggests the winning mechanism must CONSUME
   H > 16*tau quantitatively.
1. **L5 S/C pre-creative L3 shapes** (shallow-counterweight completion; two-prong
   bouquet — DECOMPOSITION-W62-L5.md §4.2), then C and S creative waves.
2. **assembly-bridge repair (aism-pus)** — register the L5 premise as the
   L5-GAP-1 statement on the now-proved W62 interface; codify l2-attack §2.6-2.7.
3. **E1-E5 codification + small-gauge bridge** (batched). (Paper-track engine
   reproduction DONE — shards 21/22, aism-mg7 closed.)
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

- Any claim more than THIRTY-FOUR results are af-validated (the four W62 lem-l5-*
  shards are L5-tier, NOT af-validated).
- Any claim any leaf, the huddle charge, the Kernel Conjecture, or op-classical is
  proved. The deciders are L3 EVIDENCE: decider A does not prove X2; decider B does
  not refute N5/N6 as mathematical conjectures (tallness + Gamma_f clauses fail in
  its instance; N6 untouched).
- Any claim the route fork is decided — it remains with the user (aism-ur9).
- Any claim L5-GAP-1 is proved: only its routine reduction interface is; S/C/I are
  open conjectures, and the refuter searches are L3 evidence, not emptiness.
- `lem-huddle-charge-assembly` remains INVALID-as-stated / DO-NOT-CONSUME
  (aism-pus).
