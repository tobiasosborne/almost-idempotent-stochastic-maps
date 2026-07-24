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

## 2026-07-10 — W63 (session 17): S/C pre-creative deciders BOTH BLOCKED; the C width bouquet fails ONLY tallness (4th consecutive bind; delta on v25)

No registry change (L3 evidence only; `runs/2026-07-10-w63-sc-decider/`, aism-3yyz).
This completes the DECOMPOSITION-W62-L5.md §4.2 pre-creative decider program for
all three horns. (i) The S shallow-counterweight completion is blocked exactly at
hiddenness (the legal W61 factorized seed is cubic-height) and at the top-row
tau^2 negativity budget; formally dialing the face equation to H/tau in [16,20]
flips the proposed top VISIBLE (exact exposers exhibited) — tall + shallow-payer
configurations fight hiddenness itself. (ii) The C two-prong width bouquet is a
COMPLETE near-refuter: it satisfies C's entire center-uniform antecedent, enters
the width branch (Omega -> 3/4), realizes the weighted chord, PAYS the C(b) engine
demand through one reusable ballast fiber, and has Z_v(q_A)/tau -> 0 — failing
ONLY H > 16*tau. Map consequence: tallness now binds in FOUR consecutive
independent refuter searches, and for C specifically the missing step is isolated
to the chord-demand-to-ray-certificate coupling UNDER tallness; the S/C/I creative
waves inherit these fixtures (C: width bouquet; S: visibility-flip; I: W62
bundle). The I-horn creative decomposition wave (aism-5wow) is in flight.

## 2026-07-10 — W63 (session 17): the I horn DECOMPOSED (strategy artifact; verification in flight; delta on v25)

Fresh codex ultra strategist-prover returned
`docs/waves/2026-07-10-W63-artifacts/DECOMPOSITION-W63-I.md` (aism-5wow):
node I (`conj-w62-isotropic-cotop-web-exclusion`) decomposed into TEN routine
nodes (P priced-ray, T tall-halo-saturation, V dual-co-top-geography, E
universal-exterior, ED/EW drift/width payer extraction, U ultra-compression,
S0 rim-to-SL1b, L0 co-top-SL1a, SC selected-corner extraction; inline proofs in
Appendix A, ALL still proposed pending the batched hostile verifier now in
flight) + SIX creative leaves (D natural-drift, W natural-width, Sh shallow-rim,
X off-diagonal, I-cap intersection-diagonal, D-cap disjoint-diagonal) with an
explicit assembly (gamma_I/delta_I threaded) and a full K1-K8 kill-list
crosswalk incl. exact fixture routing for all four refuter families.
Binding-gap verdict: I is asymptotically an EMPTINESS theorem
(Z_v(q_A) <= 3*tau^2/c_m always, so any gamma*tau lower bound empties the
class below a ceiling) whose hard core is a TALL COMPLETION OBSTRUCTION.
Structural headline: the isotropic core is routed through the W56 SL1a corner
machinery into the SAME X/I/D cell trichotomy as the SL1a fronts — the L5
minimax residual and the H-X/H-I/H-D leaves now share cell geometry; the
sign-cube plateau threat is isolated in I-cap, the strongest positive mechanism
(bounded-slab + robust starvation) points at D-cap. NOT claimed: any creative
leaf, any status promotion; the routine batch is unverified until the verdict
lands.

## 2026-07-10 — W63 (session 17): I-horn routine batch VERIFIED 10/10 and codified (registry 162 -> 172; delta on v25)

The fresh batched hostile codex verifier (xhigh) returned
`docs/waves/2026-07-10-W63-artifacts/VERDICT-W63-I-BATCH.md`: ALL TEN routine
nodes VALID, assembly SOUND, zero corrections (it recomputed (A.3)-(A.7) incl.
the s_+s_- weights and 1-theta denominators, checked the corrected A > 0
financing-floor calls, clone-split ED/EW/U/S0/L0, and audited every
strict/equality boundary against the W62 node-I interface). Codified as
registry shards `lem-ihorn-*` (priced-ray-package, tall-halo-saturation,
dual-cotop-geography, universal-exterior-package, drift-payer-extraction,
width-payer-extraction, ultra-compression, rim-sl1b-package, cotop-sl1a-package,
selected-corner-extraction), all status proved (L5), UNWIRED-whitelisted.
Map consequence: node I of the L5-GAP-1 trichotomy is now REDUCED on a proved
interface to six creative leaves (D/W/Sh/X/I-cap/D-cap); the ultra-isotropic
core routes through lem-ihorn-cotop-sl1a-package (constants STRONGER than the
registered SL1a thresholds) and lem-ihorn-selected-corner-extraction into the
same X/I/D cell trichotomy as the SL1a fronts. Open surface strictly reduced:
the sign-cube threat is pinned in I-cap; D-cap has the strongest positive
mechanism (bounded-slab + robust starvation). Next per §4: the six W63 L3
decider shapes, then creative I-cap -> D-cap -> X -> Sh -> W -> D.

## 2026-07-11 — W63 (session 17): six-shape I-horn decider batch ALL BLOCKED; 5th consecutive tallness bind; pre-creative program COMPLETE (delta on v25)

No registry change (L3 evidence only; `runs/2026-07-11-w63-ihorn-six-shape-decider/`,
aism-t20p). All six W63 creative-leaf decider shapes BLOCKED with zero genuine
I-base data: D/W reach the drift equality and an exactly PAID weighted chord
(true ray value 2*tau^2) but remain the old wide fan (Omega -> 3/4) and short;
Sh binds at the tau^2 negativity budget; X yields the FIRST exact
definition-level M_X > 1/8 corner ledger (by-catch fixture — not an SC output,
no I-base/L0 input); the attempted I-cap diagonal plateau has M_I = 0 and routes
to the D cell, missing the I cell by exactly 1/16 (the predicted sign-cube cell
has never been entered); D-cap stays inside the proved rank-three obstruction
class and the canonical W55 completion fails negativity by order one. Map
consequence: the pre-creative decider program for ALL NINE creative surfaces of
the W62+W63 trees is complete; tallness and the negativity budget are the only
walls ever named; creative queue green-lit (aism-72zn, I-cap first, with the
X ledger and routes-to-D plateau as adverse fixtures).

## 2026-07-11 — W64 (session 17): I-cap DECOMPOSED (strategy artifact; hostile verify in flight; delta on v25)

Fresh codex ultra strategist-prover returned
`docs/waves/2026-07-11-W64-artifacts/ICAP-ATTACK-W64.md` (+ appendix proofs;
aism-72zn): node I-cap (`conj-w63-I-intersection-diagonal-corner-exclusion`, the
sign-cube cell) achieves objective (a) — decomposed into EIGHT routine nodes
(B0 single-root receiver cap; S score-bulk production, lambda_A{score-good}
> 1/14; C arbitrary-kernel X/I/D bulk census, one cell >= 1/42; G common
receiver statistic with constant top ownership P_v^+ > c_m/512 resp. c_m/1536;
T+ the explicit tallness spend P_v^+{d_Q <= tau/4} < 2*tau/15; IC the
internally closed diagonal-flow package with O(delta)-overflow two-fold flow;
A the structural cost of type I — a singleton far-tight family is impossible,
exactly why the W63 plateau had M_I = 0; R the exact six-way residual split) +
SIX strictly smaller creative leaves (X_gap/X_near/I_far/I_near/D_gap/D_near),
assembly with gamma_cap/delta_cap threading and a separate honest emptiness
ceiling. Hard core in one sentence: an exact high-rank sign cube must carry
constant top mass on alpha-free cancellation vertices while its two-fold
positive flow is covered inside the saturated halo and every common scalar
demand stays O(delta). NEW exact calibrations: a short 4x4 module with local
type-I ledger mass 1023/8192 > 1/16 and an 8x8 block extension meeting all
numerical I guards — both short and with ZERO top ownership: intersection alone
is NOT the obstruction; coupling a multi-ray I module into a tall ultra web is.
Batched hostile verifier (fresh codex xhigh) dispatched over the 8-node routine
batch. Nothing promoted.

## 2026-07-11 — W64 (session 17): I-cap routine batch verdict 7/8 VALID + 1 corrected; calibrations verified (delta on v25)

The fresh batched hostile codex verifier returned
`docs/waves/2026-07-11-W64-artifacts/VERDICT-W64-ICAP-BATCH.md`:
B0/S/C/G/T+/IC/A all VALID (every constants chain recomputed: 6tau/7, 1/14,
1/42 census, c_m/512 and c_m/1536 ownership floors, 2tau/15 T-spend, c_m/1024
outer-halo flow; clone audits with split and partially selected fibers; kernel
fixed before classification; R2 source dominations matched; dependency
contracts checked incl. the corrected A>0 financing floor). R is
VALID-WITH-CORRECTION: the six-way routing alternatives are exhaustive but NOT
pairwise disjoint (exact overlap distributions exhibited); minimal honest fix =
priority guards (take the first line if it holds, else the second; equality
owned by the first) — preserves all constants; the §2 assembly's 'exactly one'
inherits the same repair. All three calibration matrices (the 4x4 I module,
P_S, and the 8x8 block extension) recomputed and VERIFIED exactly, incl. the
zero-top-ownership claim. Codification of the eight shards (R in corrected
form) in flight.

## 2026-07-11 — W64 (session 17): I-cap routine batch codified, R in corrected form (registry 172 -> 180; delta on v25)

Eight shards installed: `lem-icap-{single-root-receiver-cap, score-bulk-production,
kernel-bulk-census, common-receiver-ownership, tallness-spend,
closed-diagonal-flow, type-i-structural-cost, priority-residual-split}` — all
status proved (L5; codex ultra prover + fresh batched hostile codex verifier;
R restated per the verifier-mandated priority-guard correction, recorded in its
provenance). Map consequence: I-cap is REDUCED on a proved interface to six
strictly smaller creative leaves (X_gap/X_near/I_far/I_near/D_gap/D_near) with
the closed sign-cube packet isolated; combined with W63, the L5-GAP-1 tree now
has TWO proved reduction layers below the W62 trichotomy. Session-17 registry
total: 162 -> 180 (+18 proved, all hostile-verified, two verifier-mandated
corrections caught). Creative queue (aism-72zn continues): D-cap next per the
W63 order, then X, Sh, W, D, and the W64 six leaves.

## 2026-07-13 — W65 (session 18): D-cap decomposed and its routine batch codified (registry 180 -> 187; delta on v25)

The D-cap leaf `conj-w63-I-disjoint-diagonal-corner-exclusion` (ranked first in
the W63/W64 creative order; strongest positive mechanism) is DECOMPOSED on the
proved interface (`docs/waves/2026-07-13-W65-artifacts/DCAP-ATTACK-W65.md`):
7 routine nodes + 5 proper creative leaves, full pipeline
strategist-prover(xhigh) -> routine prover(high) -> batched hostile
verifier(xhigh) with three independent codex contexts — FIRST wave under the
2026-07-13 effort cap (ultra retired); deliverable quality on par with the
ultra-era waves. Verdict 7/7: R0/B1/B2/B3/B4/R1 VALID, B5
VALID-WITH-CORRECTION (Xi_X undefined in the strategy doc's (B5.3);
routine prover self-flagged it, verifier confirmed the (B5.C) inline
definition as the unique legal reading). Seven shards installed:
`lem-dcap-{root-closure, score-bulk-transfer, kernel-bulk-census,
common-ownership, tall-same-center-packet, closed-overlay,
five-way-completion-split}` — all status proved (L5; B5 restated per the
correction, recorded in its provenance; hypothesis-honesty audited: zero
I-cap-scoped lem-icap-* consumption, B1-B5 rederived kernel-arbitrarily on
the D-cap class).

Map consequence — the KEY structural sharpening: `lem-hx-robust-scalar-starvation`
is already rank- and slab-free once actorized, so the feared "higher-rank slab
escape" of the D cell is NOT a diffuse threat but exactly TWO named completion
packages with refuter shapes: A-esc (actorization escape: the synthetic
zero-face displacement stays > 3*delta from every actual row displacement on
constant D mass) and T-esc (scalar-tail escape: actual actors exist but
Tail_1(u) > delta rotates with the carrier). D-cap == five proper creative
leaves N / G<4 / C0 / A-esc / T-esc on the proved five-way 1/80 priority
split, each targeting Z_v(q_A) >= c_m*tau/64 - (c_m/16)P_v^+(L_v), assembling
to gamma_dis = 7*c_m/960 with an explicit emptiness ceiling. Creative order
(W65 §4.3): A-esc, T-esc, G<4, C0, N — with pre-creative L3 decider shapes
pinned in DCAP-ATTACK-W65.md §4.2. Creative queue (aism-72zn continues).

## 2026-07-14 — W66 (session 19): D-cap five-leaf pre-creative decider batch — ALL BLOCKED, sixth tallness bind (delta on v25; no registry change)

The DCAP-ATTACK-W65.md §4.2 decider program is COMPLETE
(`runs/2026-07-14-w66-dcap-five-leaf-decider/`, bd aism-nrag; fresh codex
xhigh worker, exact Fractions, orchestrator-reproduced): all five W65 creative
leaves BLOCKED in the tested exact families (C0: PARTIAL definition-level
by-catch), ZERO genuine I-base data, ZERO genuine refuters, and tallness
(H > 16*tau) binds for the SIXTH consecutive independent exact batch. Both
mandatory unit tests pass (the W63 diagonal plateau routes to D with M_I = 0,
M_D = 1023/1024 and fails tallness; the W55 A0=5 completion reproduces its
exact order-one finance negativity and is rejected, never mislabeled a
refuter).

Map consequences (evidence-level, L3 — no sketch-node status changes):
(i) the factorized W63 plateau with its UNIQUE singleton reduced display is
the first exact LOCAL C0 cell entrant (eta_D*(C0) = 1-2*tau; g/tau ~ 4,
A ~ 2/tau, ell/tau = 2*tau) — an adverse fixture for the C0 leaf, but its
leaf-hypothesis antecedent fails (selection not far, omega mass 0, short,
D_leaf > 0); (ii) NO tested family even reaches the A-esc actorization window
(ell < tau/2 routes to C0 first) — an A-esc refuter must beat the
ell >= tau/2 gate on constant D mass while tall; (iii) the T-esc
residual/tail shape has only ever been exhibited together with order-one
finance-row negativity — the creative T-esc proof should target exactly this
incompatibility; (iv) the decisive wall is tallness TOGETHER WITH a legal far
selected mass and a nonempty ultra omega package. Non-proof green light for
the creative queue in the W65 §4.3 order (aism-72zn: A-esc, T-esc, G<4, C0,
N), now fully decider-informed.

## 2026-07-14 — W67 (session 19): A-esc decomposed and its routine batch codified (registry 187 -> 192; delta on v25)

The A-esc leaf `conj-w65-dcap-actorization-escape-exclusion` (first in the W65
§4.3 creative order) is DECOMPOSED on the proved interface
(`docs/waves/2026-07-14-W67-artifacts/AESC-ATTACK-W67.md`), full pipeline
strategist(xhigh) -> independent routine prover(high) -> batched hostile
verifier(xhigh), three codex contexts. Verdict 5/5: SF, SF-K, HS, TU VALID;
SEP VALID-WITH-CORRECTION (the strategist applied an affine functional to a
displacement; corrected to the linear part — 4th genuine defect caught
upstream of codification). Five shards installed: `lem-aesc-{synthetic-
finance-tail-amplification, synthetic-finance-fixed-k, guarded-hull-split,
common-tail-union, separation-geography}` — all proved (L5; SEP in corrected
form, correction named in provenance).

Map consequence — the KEY mechanism extension: the starvation engine now
prices SYNTHETIC finance rows. On the A-esc window, if the missing actor
x_u = p_u - A~_u(q~_u - p_u) is within 3*delta of the row HULL K(P) (not of
any actual row), then Tail_1(u) > tau/8 — a tau-scale cost, rank- and
slab-free, consuming only rP = r, mass 1, nu(r) <= delta and
lem-hx-transverse-moment-identity. With the guarded hull split (1/160) and
the one-foldback tail union (P_f*^+(U_tail) > tau/2560), A-esc == exactly TWO
strictly smaller creative residuals: HES (hull-exterior separator
synchronization; refuter = growing-rank rotating-separator crown) and DTR
(diffuse-tail ray conversion; refuter = growing-rank tall completion with
rotating incidence, distributing W55's order-one finance negativity). Both
target the stronger same-center inequality (EC) with the exact E line
(c_m*tau/64 at p_f*) and the shallow subtraction before B4. Fixed-K fallback:
assuming an actor residual <= K*delta on 1/160 mass REMOVES A-esc at explicit
ceiling delta <= (3K+19)^(-2) with Tail_1 >= tau/15 — no rank/slab
hypotheses. Creative order (W67 §4.3): DTR first (best-conditioned target so
far), its growing-rank decider in parallel, then HES (macroscopic h_u >=
tau/32 subcase first). Creative queue (aism-72zn continues).

## 2026-07-14 — W68 (session 19): the assembly bridge REPAIRED and the L5-GAP-1 parent registered (registry 192 -> 194 + 1 rewrite; delta on v25)

The 2026-07-10 INVALID verdict on `lem-huddle-charge-assembly` (aism-pus) is
DISCHARGED by executing its own repair recipe
(`docs/waves/2026-07-14-W68-artifacts/`): fresh codex xhigh prover -> fresh
xhigh hostile verifier, 3/3 VALID-WITH-CORRECTION (all corrections
registry-schema level; zero mathematical defects). Three registry changes:

1. **`conj-l5-gap-1` REGISTERED** (conjecture, no deps — the verifier ruled
   deps are proof imports, not attack-tree arrows): the dual-face mass
   minimax, verbatim-consistent with the W54 verdict item 2 and the W62
   pinned target. The entire W62-W67 reduction tree (lem-l5-*, lem-ihorn-*,
   lem-icap-*, lem-dcap-*, lem-aesc-*) now has its parent formally in the
   DAG (relation recorded in the shard body until a reduction lemma actually
   concludes it).
2. **`lem-intersection-branch-production` PROVED (L5)**: the previously
   missing Branch-II implication — the L2-core intersecting-hulls
   configuration produces either the SL1a-forbidden probability measure
   (barycenter 2.2*tau, exposer (16/13)*kappa) or the SL1b-forbidden
   sub-probability measure (mass >= tau/(2+4*delta)) — codified from
   l2-attack §§2.6-2.7 with a genuine dependency repair: the prose "B5"
   co-top clause is NOT in lem-intersection-witness-confinement's contract;
   the proved lem-top-witness-third-actor supplies it (13/16 at c = 4).
3. **`lem-huddle-charge-assembly` REWRITTEN: stated/DO-NOT-CONSUME ->
   proved (conditional)**: explicitly conditional two-branch contract on
   {SL1a, SL1b, cotop-web-coupling, conj-l5-gap-1} with
   delta_0 = min{delta_a, delta_b, delta_c, delta_5(c_*/2), 1/4,
   (c_5*c_*/6)^2}; intersection branch via the production lemma; disjoint
   branch via coupling + L5 at c_m = c_*/2 + lem-top-deficit-price;
   lem-l2-core-collapse dropped (production works at configuration level);
   AG-1/AG-2 discharged as real deps (lem-hiddenness-dual-witness +
   lem-positive-exposedness-margin), not "modulo" prose.

Map consequence: the known broken link between the L5 minimax campaign and
the SL1a/kernel trunk is CLOSED. The W62-W67 pillar now feeds a proved
conditional bridge; the four named conjectures (SL1a, SL1b, cotop-web-
coupling, L5-GAP-1) are the complete conditional surface of the tall
near-cluster charge. aism-pus CLOSED.

## 2026-07-14 — W69 (session 20): the DTR pair — POTI reduction banked raw + the growing-rank decider (delta on v26; no registry change)

Session 20 (wind-up session): the route fork aism-ur9 was decided ROUTE A
(codex named-H-X) by the strategist under explicit user delegation ("no
strong feeling"; rationale on the issue: no surface change + decider-informed;
Route B recorded as fallback). Then the DTR pair per AESC-ATTACK-W67 §4.3:

- **W69 decider (runs/2026-07-14-w69-dtr-growing-rank-decider/, L3,
  reproduced):** PARTIAL — the sharpest decider finding to date. Growing rank
  (certified 4..32, no clones/transients) DOES realize the local DTR geometry
  with exactly ZERO finance negativity (local D_EC = -7/64 < 0): the feared
  finance-distribution mechanism is real locally. But every GLOBAL gate fails
  by exact rank-uniform margins (R0 ownership excess exactly 1/8; H/tau = 0;
  shallow mass 1; empty ultra omega), D_leaf > 0 at every rank, and NO gate
  margin improves with rank. Zero entrants, zero refuters. Creative
  implication: DTR's proof must price global root-to-top synchronization,
  not local negativity.
- **W69 attack (DTR-ATTACK-W69.md, banked RAW — objective (c), UNVERIFIED):**
  DTR reduced to the named **pinned-deficit oriented-tail-incidence problem
  (POTI)** via the canonical root/top overlap rho = min{m_A, eta_D*|_B} (not
  the B5 overlay) and the oriented tail charge G_phi; the claimed-routine
  inequality S*Z_v(q_A) >= G_phi (POTI-R) converts oriented tail incidence
  into the top ray, splitting DTR into two proper residuals POTI-0 /
  POTI(+), plus a quantitative ACTOR-FREE weakened conversion with exact
  loss and separate D_POTI / D_EC / D_leaf decider targets. NOTHING in this
  doc is verified: the routine batch (incl. POTI-R) awaits the independent
  prover + batched hostile verifier (bd aism-cmk0) before any codification.

## 2026-07-16 — v27 / W70 (session 21): the DTR/POTI routine batch VERIFIED and codified (registry 194 -> 200)

The aism-cmk0 pipeline ran end-to-end on DTR-ATTACK-W69.md: fresh routine
prover (gpt-5.6-sol, high) -> fresh batched hostile verifier (gpt-5.6-sol,
xhigh) -> fresh transcription codifier (high) + orchestrator audit.
**VERDICT-W70-DTR-BATCH.md: 4/4 VALID, ZERO corrections — the cleanest
batch verdict of the campaign.** The verifier explicitly discharged the two
highest-risk checks: the pinned-deficit bounds 0 <= z <= D_0 hold at EVERY
row index (lem-top-deficit-price's literal scope — not an extension), and
lem-l5-mass-barycenter-dualization is literally about the un-normalized
m_A (no hidden renormalization).

Codified (six shards, W68 deps-semantics):
- lem-dtr-canonical-overlap (COV, proved L5)
- lem-dtr-oriented-tail-ray-conversion (POTI-R, proved L5): S*Z_v(q_A) >= G_phi
- lem-dtr-tail-coherent-conversion (TC, proved L5) — the first PROVED
  quantitatively weakened theorem on the A-esc front (actor-free, exact
  loss r_0*alpha*lambda/(16S))
- lem-dtr-poti-assembly (proved L5, conditional; conclusion not consumable
  unconditionally)
- conj-dtr-zero-oriented-surplus-exclusion (POTI-0, registered open)
- conj-dtr-positive-oriented-surplus-gap-exclusion (POTI+, registered open)

Map consequence: **DTR == POTI-0 + POTI+ through a proved conditional
chain**; the A-esc creative surface is now HES + POTI-0 + POTI+, each
strictly smaller than its predecessor; the diagnostics D_POTI/D_EC/D_leaf
are proved ordered. Sketch v27 created (Tier-1 leaf set changed + absorbs
the session-20 Route A decision); CURRENT.md regenerated.

## 2026-07-16 — W71 single-wave delta (session 21): the POTI-0 zero-overlap decider — BLOCKED with an exact ownership trade-off law (no sketch bump; L3 only)

runs/2026-07-16-w71-poti0-zero-overlap-decider/ (fresh codex xhigh,
orchestrator-reproduced exit 0): 0 entrants, 0 POTI-0 refuters, 0 POTI+
window entrants; SEVENTH consecutive tallness bind. Headline: in the exact
anchor/probe growing-rank family the trade-off law max_i nu(P_i) = beta*a
makes R0 root ownership (beta >= 1/8) and the negativity gate
(beta <= tau^2/a) exactly incompatible at every rank and tau — the
root-ownership repair cost tends to 1/8 and does NOT distribute with rank.
This inverts W69 one level up (local DTR geometry free; ROOT OWNERSHIP
order-one) and names the creative target for the POTI-0 attack: prove that
carrier ownership + the delta negativity budget force either positive
canonical overlap (rho(1) > 0) or an order-one cost — the root-to-top
synchronization price, now with an exact family witnessing the mechanism.
Support disjointness (rho(1) = G_phi = 0) was reached only OUTSIDE the
gate; orientation starvation never reached. The proved W70 orderings pass
exactly on every certified instance (D_EC = D_POTI/S throughout). Tier-1
leaf set unchanged (POTI-0/POTI+/HES); v27 stands.

## 2026-07-16 — W72 single-wave delta (session 21): POTI-0 attack banked RAW; routine batch proved standalone; verification INTERRUPTED (no sketch bump)

docs/waves/2026-07-16-W70-artifacts/POTI0-ATTACK-W72.md (fresh codex
strategist xhigh, objectives (a)+(c)): POTI-0 == [S0 exact cause split
rho(1)=0 vs orientation starvation] + [RX root-selection exchange ledger —
the exact zero-overlap price sigma_B >= w_*M_B - e_delta] + [O48 fixed-level
starvation ledger — every overlapped carrier forces > tau/16 tail mass into
the single public slab {z < 48*tau}, folded to the top row with one new
legal foldback] + TWO named disjoint proper-subclass creative residuals:
RDSE (root-dilution selected-support exchange, owns rho(1)=0; exact escape
= selected-root dilution w_*->0, unbounded below on the pinned interface)
and LDHR-48 (low-deficit huddle ray, owns starvation; exact escape =
r=O(tau) or a rotating near-top huddle). KEY negative: the W71 order-one
ownership law is FAMILY-SPECIFIC, not the general mechanism. The routine
batch (S0/RX/O48/ASM2) was proved standalone by an independent fresh prover
(APPENDIX-W72-poti0-proofs.md); the batched hostile verifier was
INTERRUPTED before producing a verdict — the batch is UNVERIFIED and
NOTHING is codified. The sketch is NOT bumped: POTI-0 == RDSE + LDHR-48
becomes a map change only when the verdict lands (first task next session,
brief committed: BRIEF-W72-POTI0-VERIFIER.md). Tier-1 leaf set formally
unchanged (POTI-0/POTI+/HES); v27 stands.

## 2026-07-23 — v28 (W73 + W73b + W74F wave 1): a SECOND, independent route enters the map

Three sessions' worth of state that v27 never absorbed, plus the wave that
follows from it.

**W73 (strategy reset).** A user-mandated fresh-perspective session (6 repo
summarizers + 3 literature researchers + 4 independent codex xhigh
strategists) produced two things v27 does not contain: (i) the confirmation
that op-classical is posed as OPEN in the 2024-25 literature, with Kitaev
(arXiv:2405.02434) identifying the same mechanism and proving an adjacent
dimension-free factorization theorem, and SBD (arXiv:2405.01532) proving the
sharp dimension-free sqrt(eps) repair for the classical FIXED-POINT sibling;
(ii) **Route F** — an architecture two strategists converged on
independently, which bypasses the entire signed-geometry trunk (no exposed
hulls, hidden vertices, charts, heights, no Kernel/(EX)). Both papers are now
ingested and pinned under refs/ (aism-5de).

**W73b (the decisive audit).** A fresh hostile codex auditor, source-first
against the byte-verified tex: Q1 VALID (the imported statement is exactly
what Route F needs, incl. tensor-extended multiplicativity and the map
orientations), Q2 VALID-WITH-CORRECTIONS (universality explicitly claimed
and enforced by design, constants never extracted), **Q3 INVALID** (the
printed proof of th_factorization uses a FALSE direct-sum diagonal formula at
tex:1254 / tex:2780-2783 — exact C+C counterexample — and rests on
th_main_ext, whose amplified proof is outline-level at tex:1542-1557), Q4
VALID (the cb-lift identity F0, both directions), Q5 VALID (all F2-F3
constants re-derived). Two findings matter more than the headline: the real
flaw is SMALLER than the sibling repo's C14 diagnosis (the auditor PROVED the
positivity argument entrywise given an exact central diagonal, and supplied an
elementary Haar / phase-balanced repair; lem_RC and the Upsilon' construction
survive fully), and the PRINCIPAL BLOCKER is th_main_ext, not the diagonal.
Residual risk register: (1) th_main_ext at amplified strength; (2) a universal
constant ledger; (3) the exact whole-algebra diagonal repair + use-site
recheck; (4) no unproved cone-projection shortcut; (5) full audit of
th_almost_idemp (tex:2239-2723); (6) PRH standalone; (7) provenance closure.

**W74F wave 1 (2026-07-23, user directive: concerted effort on Route F).**
Four fresh codex gpt-5.6-sol xhigh workers, one per disjoint register item,
briefs committed: W74F-A PRH proof (item 6, aism-6m8v) · W74F-B diagonal
repair + use-site ledger (items 3+4, aism-0m77) · W74F-C **decomposition** of
th_main_ext + universality ledger (items 1+2, aism-2r3m) · W74F-D per-block
audit of th_almost_idemp (item 5, aism-7gqw). Epic aism-enze. All are
prover/auditor output; a batched hostile verification pass gates codification.

**Map changes in v28:** Route F added as a second candidate route with
per-step statuses (F0/F2/F3/F5 audit-VALID *conditional on* F1; F1's printed
proof invalid; F4/PRH unverified); the residual register installed as the new
Tier-1 face; **PRH named as the load-bearing independent asset** — it
establishes op-classical <= "a positive approximate retract exists" whether or
not the Kitaev import ever closes; Route X (RTS / APAL / QCMP) registered as
the in-repo fallback shape with the carrier lemma as its engine; RDSE/LDHR-48
creative attacks PAUSED (user directive; the strategists' altitude diagnosis
is the stated reason and is itself unverified); the W72 verification debt
carried forward explicitly.

**Promotes nothing.** Registry unchanged at 200, T0 at 34. Route F is a
CONDITIONAL reduction whose sole large import has an INVALID-as-printed proof.

## 2026-07-23 — v28 wave-1 verdict (W74-F): the batched hostile verifier returns A/B/C/D all VALID

The four wave-1 prover/auditor artifacts (banked raw and unverified earlier this
session) cleared a single fresh codex xhigh hostile verifier
(VERDICT-W74F-BATCH.md), one pass over the batch, tex SHA re-checked, W73b audit
NOT treated as an oracle: **A VALID · B VALID · C VALID · D VALID, no correction
required to any target**. Verified transcribable statements banked for A (PRH:
||AM-E|| <= 2sqrt(2eps) with the sqrt intrinsic-sharpness family), B (finite
phase-balanced diagonal, projective norm exactly 1, block-count-free, exact
algebra B, entrywise CP-ization, no cone projection), C (th_main_ext ==
H-CB + EXT-CB, decomposition confirmed complete and correctly classified), D
(th_almost_idemp diagrammatic core dimension-free at 10eta). Cross-target: the
constant chain is consistent once eps_AI / K / eps_PRH are kept distinct, the
conditional finish is ||Q-E|| <= (K+4sqrt(2K))sqrt(eta), and there is NO
circularity (no target assumes th_factorization to prove an ingredient of it).

Net effect on Route F's residual register: item 6 (PRH) proved; items 3+4 (the
diagonal repair, no cone shortcut) discharged; item 5 (th_almost_idemp)
discharged mod local source edits; items 1+2 REDUCED from "prove the outline" to
two named amplified gaps **H-CB** (uniform column-Hilbert / operator-module
estimates for 1_{M_n}(x)Ha, where the risk is a hidden n-factor) and **EXT-CB**
(the amplified extension lemma on one level-one unitary), plus the final
unconditional K/eta_K ledger. Route F remains a CONDITIONAL reduction; the
principal next attack is H-CB (a refutation would challenge th_main_ext's claimed
uniformity).

Sketch v28 updated in place (Map change 3 gains the verdict block; Tier-1 order 0
now reads codify-survivors then prove-or-refute-H-CB). Promotes nothing: registry
200, T0 34 — a hostile-verified L5 result is not af-validated and not yet a
registry shard; codification is the next mechanical step.

## 2026-07-24 — v29 (W74F wave 2 + W72 discharge): both th_main_ext gaps close at L5

**Wave-1 codification (aism-zbcm).** Registry 200 → 208: lem-prh (+sharpness, constant
2*sqrt(2), sqrt(eps) intrinsically sharp), lem-kitaev-diagonal-repair (+ CP-ization
corollary), conj-hcb, conj-extcb, lem-thmainext-conditional, lem-kitaev-almost-idemp-audit.
Four draft definitions pending user ratification (3 cited byte-verbatim from the pinned
Kitaev tex, 1 original). The PRH reduction (op-classical <= positive-approximate-retract-
exists) is now a registry fact.

**Wave 2 (aism-wwur, aism-9lb7).** One fresh codex xhigh prover + one SEPARATE fresh
hostile codex xhigh verifier per gap:
- H-CB: VALID-WITH-CORRECTIONS. C_H = 4000c, e_H = 1/(10000c) relative to the sanctioned
  COMP-CB/COL-HILB constants; no n-growth family. The unconditional h_{P,P} inverse is
  FALSE (exact C+C counterexample); conj-hcb amended to the verifier's exact
  conditional-inverse clause (the form lem_extension consumes) and flipped
  proved-mod-audit. Not an escalation — refinement, not refutation.
- EXT-CB: VALID-WITH-CORRECTIONS. Transported-corner construction (gamma_jk =
  h_jk^{-1} mu_jk, gamma_11 = v) confirmed: one level-one unitary carries every
  amplification; C_ext = C_merge[1+5C_H+20C_app(C_H+1)]. One proof-level correction
  (close-idempotent normalization folded into e_sel); no contract amendment; conj-extcb
  flipped proved-mod-audit with dep conj-hcb.
Through lem-thmainext-conditional, th_main_ext now holds at the proved-mod-audit rung —
the W73b principal blocker is closed at L5. Route F residual surface: the unconditional
K/eta_K ledger (wave 3, aism-xpxk, prover in flight) + PRH af-elevation (aism-h9qc).

**W72 debt discharged (aism-x0up).** Re-dispatched batched hostile verifier from a
rebuilt build-workspace.sh snapshot: S0/RX/O48/ASM2 all VALID, cross-cutting clean.
Codified (registry 208 → 214): S0/RX/O48 + conditional assembly proved-mod-audit;
RDSE + LDHR-48 registered as conjectures (attacks remain PAUSED). POTI-0 == RDSE +
LDHR-48 is now a proved-mod-audit conditional reduction.

**Not claimed:** op-classical proved; any new af-validation (T0 = 34); numerical K;
ratified definitions. All new statuses are proved-mod-audit via single fresh hostile
passes (the batched-verification default), one rung below T0.
