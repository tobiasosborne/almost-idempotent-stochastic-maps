<!--
ROLE: strategist-level proof sketches for the OPEN conjectures (user request, 2026-07-07,
  session-11 close). Grounded ONLY in banked L0/L5 results and exact certificates; every
  mechanism's crux and failure risk stated. A SKETCH — promotes nothing (L0). Companion to
  sketch v11 (the canonical map); wave briefs should be derived from these.
-->

# Proof sketches for the open conjectures (2026-07-07)

Toolkit tiers cited: [L0] = af-validated; [L5] = reviewed (hostile-verified paper proof);
[cert] = exact certificate in a banked bundle.

## 1. (T1) — cluster-uniform optimal-face residual cancellation
**Statement.** Tall heavy near-cluster regime (hidden top v, H > (K_a/θ)τ, ρ-near deep
cluster C with mass ≥ 1−θ): every mass-carrying cluster vertex u admits an optimal
hiddenness datum with R = 0 — equivalently [L5, VAQ-verified characterization]
conv{d_f : f ∈ T_u} ∩ t*(u)·conv{d_i : i ∈ O_u} ≠ ∅.

**Sketch (four steps + a dichotomy).**
(i) *O-location lemma* [new, T1-short]: an always-upper-tight row (h = 1 across the whole
optimal face) maximizes every optimal exposer, hence is an exposed point of the row polytope
in the exposer cone; combined with the pincer [L0] (v's and u's mass avoid high-h rows) it
carries no cluster mass — O sits on the anchor side, ρ-far, shallow-leaning. (Matches every
[cert]: O = visible anchors in all four W41 families.)
(ii) *T-spread* [banked]: depth-Markov [L0] + top-slab companion [L0] put T_u's reach in the
deep far top slab; the witness balance [L0] makes conv(T_u) fold back to within
t*·D + α-correction of the origin.
(iii) *The sign/rebalancing crux* [THE open step]: at a strictly complementary optimum
(Goldman–Tucker) span{d_i : i ∈ T∪O} is large; R ∈ span{T,O} would allow re-splitting the
balance over T∪O — the obstruction is SIGNS (the OBS4/HEIGHT+A [cert] counter-models are
exactly sign-infeasible flat configs). The tall input must convert depth into sign-feasibility.
(iv) *The spread dichotomy* [new, decidable]: the needed correction has scale ≤ κD ≈ (½+δ)τ,
while the cluster's spatial extent is up to 4τ — a factor ~8 of room. CASE A (spread
cluster): aggregate the fold-back points of the cluster vertices' witnesses (each within κD
of its u [L0 witness]; the u's spread over ≤ 4τ but ≥ some μ·τ by assumption) — the union of
T-hulls then contains a fat neighborhood of the fold-back region in the top-slab directions,
absorbing any κD-scale correction: intersection holds. CASE B (point cluster — all cluster
rows quotient to one point): the configuration collapses to a heavy self-loop at one quotient
vertex; lem-self-defect-shadow [L5] + sharp-vertex-visibility [L5] + the rank-2 corollary
[L5] take over (the two-point v–cluster structure is rank-2-flavored) — absorption holds
directly. The dichotomy threshold μ is the quantity to optimize.
**Price/risks.** (iii) is genuinely hard — it killed the thickness route (W42 value-
normalization hard stop). The dichotomy in (iv) is new and untested; the intermediate-spread
regime (cluster diameter between δ-scale and τ-scale) is where a counterexample would live.
**First decider:** rank 3, where the row hull has nullity ≤ small and the intersection is a
finite scalar check [per the W36/W41 pattern] — prove (T1) there outright or find the
intermediate-spread obstruction exactly.

## 2. (T2) — the row-to-circuit absorption bridge
**Statement.** If v carries ≥ 1−θ on C and every mass-carrying u ∈ C has a cheap witness
with α ≤ A₀, then v ships ≥ c mass outside C or some u ∈ C is (ρ,κ)-exposed.

**Sketch.** Aggregate the cluster witnesses with weights P_vu⁺ (legal once α is bounded —
the W39-AI center-coefficient obstruction is exactly removed by the hypothesis). The
aggregated balance reproduces the cluster barycenter; received-mass proximity [L5] puts that
barycenter within D(θ+2δ) of p_v. Subtract v's own row reproduction (cluster-heavy by
hypothesis): the difference is a circuit with far support confined to the top slab
[L5, bounded-α top-slab reduction] and total payment < κ + O(θD). Feed the difference
circuit to the characterization at the best u: it supplies the α-free rebalancing unless the
far supports are sign-infeasible — the SAME crux as (T1)(iii). Honest conclusion: (T1) and
(T2) converge on one sign/rebalancing lemma; prove it once, get both.

## 3. conj-near-cluster-absorption (given T1 or T2)
**Sketch.** With α-free (or A₀-bounded) witnesses cluster-uniformly: the aggregation is
coefficient-bounded; combine (a) the pincer [L0] at s = κ (row mass off the low slab ≤ 4τ),
(b) the capacity threshold [L5, lem-row-zero-capacity] (any candidate exposer vanishing on
the cluster pays κ·(far target mass) ≤ ν), and (c) LP duality (exposure of u ⇔ no cheap
witness): the bounded aggregated circuits either drive every candidate's payment ≥ κ
(exposure — absorption) or force v's mass outside C. Assembly is LP-exact; expected to be a
T1-moderate composition once the crux lemma exists. Then conj-low-slab-cap follows by
composition with the pincer [L0], the height clause H ≤ (K_a/θ)τ by the collapse [L0], and
conj-min-a-w4 as the (4, ½) specialization [L5 assembly already banked].

## 4. Kernel(i) — W-nonemptiness at rank ≥ 3
**Statement.** Universal δ₀: every exact signed idempotent with δ ≤ δ₀ has W(P) ≠ ∅.
(Banked strata [L5]: δ = 0; simplex polytopes; rank ≤ 2; plus the rank-3 tangent structure.)

**Sketch (corner concentration + quotient induction).**
(i) Assume W = ∅ (all vertices hidden). Take the max-area chart; for each chart vertex u_s
the barycentric exposer h_s = (1−a_s)/2 is admissible [L5, tangent lemma machinery]; the CS
pincer [L0] at h_s with s = κ gives: u_s's row places ≤ ν/κ ≤ 4τ mass outside its own
a_s ≥ 1−2κ corner — EVERY vertex is (1−4τ)-corner-concentrated.
(ii) *Near-decoupling lemma* [new, the main step]: corner concentration at every chart vertex
+ exact idempotence force P within O(τ) (row-wise ℓ¹) of a block structure over the corner
classes (each row ≈ its own corner's affine data); prove via the residual lemmas [L0] applied
per corner (the off-corner mass ≤ 4τ prices the cross-terms) — expected T1-moderate.
(iii) *Merge-and-induct*: if two corner classes are within ρ, merge them (quotient step;
clone-safe by construction) and recurse on strictly fewer geometric classes — termination is
structural (finitely many classes), dodging the class-count wall (no numeric class bound is
used). If NO two classes are within ρ, every class is ρ-isolated: sharp-vertex-visibility
[L5] exposes its vertex — contradiction with all-hidden.
**Price/risks.** (ii)'s O(τ) constant must not blow up under merging (each merge can perturb
δ — track the budget; this is where it can fail); the interplay of merging with the (ρ,κ)
scales needs the same care that killed naive cloning arguments. The W30-U anchor law
("hiddenness needs visible anchors" — 297 exact audits, no W = ∅ ever) is strong evidence;
the sketch converts it into induction rather than counting.

## 5. The small items
- **loose-δ robustness lemma** (op-exposed-hull's literal wording): re-run the W27 assembly
  at parameters (C√δ, c√δ) for d ≤ δ ≤ δ₀ directly: the larger ρ SHRINKS far sets (margins
  only need re-checking on subsets [L5 monotonicity]); the larger κ = c√δ threshold is met
  by re-deriving the visible vertices' margins from the sharp-vertex/simplex machinery [L5]
  at the coarser scale, possibly costing a constant in C. T1-short; low risk.
- **Trunk <2>7**: not a conjecture — an audit program: classify thm-classical-factorization's
  inherited proof (routine / needs-def / gap-risk), with the W27 findings (the <2>6 output is
  row-sum-one signed, NOT stochastic; pinned-δ form) as explicit interface questions;
  then re-derive the three DC4 gaps as W22/W27-pattern waves.

## Order of attack (strategist recommendation)
1. The (T1)(iii) sign/rebalancing lemma AT RANK 3 (finite check; both terminal routes hinge
   on it). 2. The spread dichotomy (iv) — its CASE B is nearly assembled from banked pieces.
3. Kernel(i)'s near-decoupling lemma (ii) — independent of 1–2, uses only L0 tools.
4. loose-δ (cheap win). 5. <2>7 audit in parallel as trunk debt.
