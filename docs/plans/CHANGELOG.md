<!--
ROLE: the rolling changelog for the top-down proof-sketch series (docs/plans/*top-down-proof-sketch*.md).
TRIGGER: any change to the strategic map (CLAUDE.md Rule 9 stewardship mandate).
-->

# Sketch changelog

**Two-tier policy.** Sub-50-line single-wave map deltas are appended HERE (no new sketch file, no pin
bump); a new numbered sketch file is created ONLY at session close or when the Tier-1 leaf set changes.
Old numbered files remain immutable for line citations.

After adding a new numbered sketch file, re-run `python3 scripts/gen-current-pointer.py` to refresh
`docs/plans/CURRENT.md` (CLAUDE.md Rule 9).

## Retrofit entries (v20–v24, backfilled 2026-07-10)

### v20 — 2026-07-10, W56 SL1a-surface delta

Registry 140 → 150 (+7 proved L5 lemmas, +3 conjectures). The W56 decomposition wave
certified a wall (any terminal hard leaf retaining the full SL1a counterexample class
restates SL1a) and banked `lem-sl1a-three-cell-reduction`: SL1a is now EQUIVALENT to
three disjoint sigma-cells — `conj-sl1a-deep-diagonal-cell` (H-D),
`conj-sl1a-intersection-diagonal-cell` (H-I), `conj-sl1a-off-diagonal-cell` (H-X). Five
new dead-route certificates filed (one-hard-leaf-after-free-preprocessing, lex-(V,R)
stratification, freight censoring without a norm gap, second-gen L-C recursion,
max-principle far-side return).

### v21 — 2026-07-10, W57 completion-LP delta

No registry change (L3 evidence only). `runs/2026-07-10-w57-starvation-completion-lp`:
the W55 starvation gadget's minimal rank-3 completions are exact-INFEASIBLE (stable
Farkas certificates over A0 in [4,6], tau <= 1/256). Named a CANDIDATE mechanism —
"minimal actor-hull starvation completion obstruction" — needing a dimension-free paper
proof (bd aism-cq2) before it is anything; the first extra-vertex completion family left
undecided as the next refuter route.

### v22 — 2026-07-10, W58 extra-vertex delta

No registry change (L3 evidence only). `runs/2026-07-10-w58-starvation-completion-extra-vertex`:
the first-extra-vertex escape is also exact-INFEASIBLE, uniform over A0 in [4,6],
tau <= 1/256, Y in [0,1]. A column-local seven-entry multiplier pattern extends the
obstruction to every fixed K below a K-dependent ceiling — the candidate lemma is now
K-parametric. Residual: unbounded-K and rank > 3; the paper-proof wave becomes the main
line.

### v23 — 2026-07-10, W59 obstruction-lemma delta

Registry 150 → 151: `lem-starvation-completion-obstruction` PROVED (L5), STRONGER than
the W58 candidate — K-FREE (any finite exterior zero-top support fiber set in the
canonical slab), universal ceiling tau <= 1/256, first-principles proof independent of
the LP computation. Mechanism: exact idempotence demands one unit of transverse moment;
the actor hull and aggregated exterior budgets supply only O(tau). First proved
mechanism on the H-X / large-gauge front; the honest gap to generalize (slab
confinement, rank >= 3, the H-X tableau) is named as the new Tier-1 item 0.

### v24 — 2026-07-10, af-elevation delta

Rigorous (af-validated, T0) count: 28 → 29. `lem-starvation-completion-obstruction`
af-validated the root in 3 rounds (7 nodes, all validated, taint clean); `fr verify`
PASS (▣). Terminal artifact of the W55–W59 arc: threat named → exact kills → paper
proof → af oracle. Tier-1 order unchanged — the generalization wave toward the H-X
tableau is now anchored to a T0 lemma.

## 2026-07-10 — OR-routes land; op-classical's formal closure now contains the live surface (delta on v24)

The linker gained disjunctive `routes:` support (aism-3ne, user-decided option (a) of the
op-hlc OR-question). op-hlc now declares BOTH routes — [lem-kernel-implies-hlc; conj-kernel]
| [lem-min-a-implies-height] — without false conjunction. op-classical's directed ancestor
closure: 12 -> 41 prerequisites (+29 = the whole MIN-A/absorption/huddle component incl. the
three-cell SL1a surface); reachable open conjectures 1 -> 11 (7 irreducible leaves). Per-route
closures: Kernel = 3, MIN-A = 30. op-hlc correctly remains status: open (declared, not
discharged). No mathematical content changed — this is codification of the map the sketch
already asserted in prose.

## v25 — 2026-07-10, W60 engine-bank delta (new numbered file)

Registry 153 → 158 (+5 proved L5 lemmas, the W60 ENGINE BANK; batched hostile verdict
MIXED = 3 VALID + 2 VALID-WITH-CORRECTIONS, corrections applied as prescribed).
`lem-hx-transverse-moment-identity` / `lem-hx-signed-variation-ledger` /
`lem-hx-financing-floor` / `lem-hx-robust-scalar-starvation` /
`lem-hx-forced-exterior-coupling`. W59 §HONEST-LIMITS gaps 1 (rank) and 2 (slab)
RETIRED at the mechanism level; the tableau metric pin relaxed to the window
[tau/2, 2tau]; fiberwise zero-top relaxed to an O(delta) top-tail cap. The H-X hard
residual is now a two-route FORK (USER DECISION aism-ur9): Route A codex exact-H-X
(X2/X3F/X3N/X4) vs Route B Fable gamma-renegotiation (N4 + N5/N6, surface change +
gamma dial). Both independent strategist trees banked in
`docs/waves/2026-07-10-W60-artifacts/`. New Tier-1 item 0: the route decision + its
two cheap L3 deciders; engine-bank af-elevation queued (prime:
lem-hx-robust-scalar-starvation).

## 2026-07-10 — W61: engine pair af-validated (T0 29 -> 31); both route-fork deciders decided (delta on v25)

af-elevation (aism-zo1): `lem-hx-transverse-moment-identity` (14/14 nodes) and
`lem-hx-robust-scalar-starvation` (12/12 nodes) are af-VALIDATED, taint clean — the
T0 generalization proper of the starvation mechanism now sits at the oracle rung;
T0 count 29 -> 31. The two L3 route-fork deciders (aism-3nk/aism-kup) are decided
and banked (`runs/2026-07-10-w61-x2-graft-refuter/`,
`runs/2026-07-10-w61-leak-financing-refuter/`): (A) X2 NOT refuted — the graft
family gets every checked selected-corner clause except TALLNESS (H = O(tau^3));
(B) FINANCING INSTANCE FOUND in local N5(ii) geometry — the ledger-only close of
N5(ii) is dead as budgeted; N5 needs a freight-row/Gamma_f-coupling budget as a
PREREQUISITE. Convergent signal: tallness is the binding wall in both searches —
the resource the adversary cannot manufacture and the ledgers do not yet consume.
Route fork aism-ur9 remains a USER DECISION, now fully informed (synthesis in
`docs/waves/2026-07-10-W61-deciders-and-elevation.md`). Remaining engine-bank
elevations (ledger/floor/coupling) queued serially. No surface change; no new
mathematics beyond the oracle promotions and the two L3 records.

## 2026-07-10 — W61 completion: the ENTIRE W60 engine bank is af-validated (T0 29 -> 34; delta on v25)

The serial elevation train finished: `lem-hx-signed-variation-ledger` (11/11),
`lem-hx-financing-floor` (12/12 on a CORRECTED contract — the af oracle caught a
genuine quantifier defect the W60 L5 batched verdict missed: 'all reals A' is
false at A < 0 with N empty; restated to the A > 0 form the proof establishes;
retraction entry in docs/LEARNINGS.md), and `lem-hx-forced-exterior-coupling`
(12/12). All five W60 engine lemmas now sit at the oracle rung. The H-X hard
residual (route fork aism-ur9) now consumes a fully rigorous engine; paper-track
reproduction filed (aism-mg7).

## 2026-07-10 — W62: the L5 minimax DECOMPOSED and its routine batch PROVED (registry 158 -> 162; delta on v25)

The L5-GAP-1 surface (aism-vuc, the W54 Branch-I premise) is re-verdicted and
reduced. Strategist tree banked (DECOMPOSITION-W62-L5.md): the binding gap is an
engine-payer mass-transport dual on the owned barycenter q_A, NOT a finite cover of
Y_v (the W54 cover framing retired as main target). The routine batch R0-R3 is
PROVED (L5; codex prover + fresh batched hostile verifier, 4/4 VALID):
`lem-l5-mass-barycenter-dualization` (mass objective = S*Z_v(q_A)),
`lem-l5-top-face-ray-formula` (Z_v as a one-pair outward visible-ray LP dual,
attained), `lem-l5-positive-flow-foldback` (the P^2=P same-carrier allocation),
`lem-l5-universal-exterior-payer` (THE new step: the af-validated engine forces
row v itself to pay tau*S/8 outside EVERY half-ball; explicit ceiling
min{1/16,(c_m/8)^2} — first consumer of the W61 T0 engine outside H-X).
L5-GAP-1 now == S/C/I: three disjoint-exhaustive creative horns (shallow payer /
drift-width chord / isotropic web) with named refuter shapes; assembly with
threaded quantifiers banked. Next: the five L3 refuter deciders, then creative
I -> C -> S.
