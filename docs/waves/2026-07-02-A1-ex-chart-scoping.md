<!--
ROLE: verbatim harvest artifact for fr arm A, wave 1 (2026-07-02): (EX) chart-bound scoping.
STATUS: L0 exploration report only. Nothing below is rigorous or promoted. Tiers are inline:
  T0 = exact / recomputed / verbatim-from-source with file:line locus;
  T1 = solid heuristic;
  T2 = plausible heuristic;
  T3 = speculation.
Worker: codex. Arm A wave 1. Answers bd aism-vip.
Scope discipline: repo files only; no prior conversation trusted. Created only this file.
-->

# Arm A · Wave 1 · (EX) Chart Scoping Harvest

## Q1. Problem Statement

The ambient object is an exact signed row-stochastic idempotent `P`: `P 1 = 1`, `P^2 = P`, row negative mass
`nu_i(P)=sum_j(-P_ij)_+`, and `delta(P)=max_i nu_i(P)`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:50-64`]

An actual-row basis is an ordered `k=rank(P)` tuple `U=(u_1,...,u_k)` whose rows `r_s=p_{u_s}` form a linear
basis of the row space; its volume is the square root Gram determinant, and `Vol_max(P)` is the maximum over
actual-row bases. [T0: `docs/ingest/report/kernel-conjecture-v2.tex:81-96`]

The theta quasi-max-volume class is
`M_theta(P)={U actual-row basis: Vol(U) >= theta Vol_max(P)}`; the interface fixes `theta=1/2`, which gives the
Cramer box `|a_s(j)| <= 2` for coordinates `p_j=sum_s a_s(j) r_s`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:98-113`]

For a fixed chart, the coordinates obey `sum_s a_s(j)=1` and the harmonic identities
`sum_j P_{u_s j} a_t(j)=delta_st`; the pivot weights are `beta_s(j)=P_{u_s j}`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:115-129`]

For pivot `s`, the source defines `lambda_s(j)=1-a_s(j)`, `mu_s(j)=sum_{t!=s}(-a_t(j))_+`,
`sigma_s(j)=sum_{t!=s}(a_t(j))_+`, and `E_s(j)=(mu_s(j)-lambda_s(j))_+`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:130-143`]

The pivot score is `Phi_s(U)=sum_j (beta_s(j))_+ E_s(j)`, and `Phi(U)=max_s Phi_s(U)`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:146-151`]

The boxed `(EX)` statement is exactly existential: for every exact signed row-stochastic idempotent with
`delta(P)<=1/4`, there is some `U in M_{1/2}(P)` with `max_s Phi_s(U) <= C0 delta(P)`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:219-231`]

The registry contract adds `rank>=3`, `Vol(U0)>=(1/2)Vol_max(P)`, equivalence to `conj-kernel`, and the
composition through `lem-factorization` to `C_sf=2 C0+6`. [T0: `argument/lemmas/conj-ex.md:1-14`]

The downstream composition does not require a constructive selector: it assumes `(EX)`, chooses a `Phi`-argmin
`U*` over `M_{1/2}(P)`, applies minimality, and then applies the chartwise factorization. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:328-346`; `docs/ingest/experiments/out/w41_ex/proof.md:124-152`]

The hostile factorization audit explicitly checks the same quantifier step and says there is no quantifier
slip: `(F)` is universal in `s`, `(EX)` is existential in `U0`, and the argmin bridges them. [T0:
`docs/ingest/experiments/out/w42_factor_audit/audit.md:144-168`]

Therefore a pure variational argument over the finite chart class is admissible for this interface; no
downstream line asks for peeled, max-volume, canonical, or algorithmic tie-breaking. [T1 from the previous two
paragraphs]

The inherited equivalence to the Kernel Conjecture is a registry claim, not proved here: `conj-kernel` states
the hidden-row/invisible-mass form and says the equivalent working form is `conj-ex`. [T0:
`argument/lemmas/conj-kernel.md:1-14`]

## Q2. Selector Landscape Autopsy

Exact-max-volume selection is dead as a robust class: the B6 family has `delta(P)=1/2`, a unique exact
max-volume identity chart with `Phi/delta=m-3 eps`, and favorable charts at volume ratio `1-eps` with
`Phi/delta=1`. [T0: `docs/ingest/report/kernel-conjecture-v2.tex:169-205`]

That B6 death is outside the `(EX)` cap `delta<=1/4`, but it proves that any fixed `theta>1/2` can exclude the
good charts, which is why the interface pays for `theta=1/2`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:207-216`]

Arbitrary max-volume tie selection is dead for sharp `C0=1`: the transverse pair at `a=1/4` has a bad
max-volume tie with `Phi/delta=5/4`, while the `Phi`-argmin/best max-volume tie has ratio `1`. [T0:
`docs/ingest/experiments/out/w41_ex/proof.md:38-41`; `docs/ingest/experiments/out/w41_ex/proof.md:195-201`]

The peeled/most-convex and min-total-negative-coefficient selectors fail by the same transverse-pair mechanism:
over the 278 rank-3 records they have worst ratio `5/4` with 4 records above `1`. [T0:
`docs/ingest/experiments/out/w41_ex/proof.md:185-194`]

Pointwise bounds on `E_s(j)` are dead: the staircase examples have a single row with `E=6 delta` and a
perturbed example with `E=10 delta`, while selected sums remain controlled. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:309-316`]

Sigma-only control without selection is dead: the perturbed staircase identity chart lies in the theta-half
class and has `S^+_0 ~ m delta` even though selected charts collapse the envelope. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:317-319`]

Single-swap monotonicity is dead as a selector/contraction principle: in the staircase witnesses, the best legal
one-row swap from the selected chart still has `Phi/delta=1`, so there is no contraction. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:320-326`]

The Jensen/convexity route is dead: the source says Jensen has the wrong direction and a `k=7` instance refutes
the proposed upper bound. [T0: `docs/ingest/report/kernel-conjecture-v2.tex:487-490`]

The canonical-`g` energy method is dead for the prior kernel route: its own positive quadratic energy bound is
too small to force Branch A. [T0: `docs/ingest/report/sections/10-refutations-dead-routes.tex:117-121`;
`docs/ingest/report/STATUS-LEDGER.md:149-153`]

The literal psi-gap is refuted by an exact rational `6x6` idempotent with `delta=1/16` and an explicit
inequality violating the bare lemma. [T0: `docs/ingest/report/sections/10-refutations-dead-routes.tex:28-53`]

`C0<1` is refuted in the rank-3 suite: the transverse-pair and rank-three no-center families attain
`min_U max_s Phi_s(U)/delta=1`. [T0: `docs/ingest/report/kernel-conjecture-v2.tex:235-245`;
`docs/ingest/experiments/out/w41_ex/proof.md:247-255`]

The counterexamples exploit non-global selection rules: fixed max-volume choices, tie choices, pointwise row
criteria, and local single swaps can all choose or stare at a bad chart even when the global `Phi`-argmin chooses
the good one. [T1 synthesis of the selector failures above]

There is no rank-3 certified instance in the 278-record `delta<=1/4` suite where the full theta-half
`Phi`-argmin exceeds `1`: the table gives worst `1` and count `>1` equal to `0`. [T0:
`docs/ingest/experiments/out/w41_ex/proof.md:173-194`]

I recomputed the rank-3 JSON summary: `444` total records, `278` inside `delta<=1/4`, `2947` theta-half charts
inside the cap, and worst `phi_argmin` ratio `1`; the worst max-volume tie, peeled, and min-neg selectors have
ratio `5/4`. [T0 recomputation from `docs/ingest/experiments/out/w41_ex/rank3_results.json`; corroborated by
`docs/ingest/experiments/out/w41_ex/rank3_results.txt:1-17`]

Other exact data in `docs/ingest/experiments/out/` add an important warning: the rank-2 suite has `Phi=0` at
every theta-half `Phi`-argmin, but higher-rank no-center path stress records report `Phi/delta=3/2` at `k=6`
and `5/3` at `k=8` with `delta=1/100`. [T0:
`docs/ingest/experiments/out/w40_ndg/proof.md:22-38`;
`docs/ingest/experiments/out/w40_ndg/part_a_results.txt:7-8`]

The `w40` script says it used exact determinant structure for those no-center theta-half bases rather than
brute-force enumeration, so those high-rank values should be treated as exact stress data but should be audited
before being promoted to a global `(EX)` lower-bound statement. [T0/T1:
`docs/ingest/experiments/out/w40_ndg/proof.md:120-123`;
`docs/ingest/experiments/out/w40_ndg/verify_part_a.py:271-282`]

Kernel-v2 already flags no-center saturation above the aesthetic `1` at the repaired/older display level, with
selected ratios `59999/40000` at `k=6` and `149999/90000` at `k=8`, so the safe target is a universal `C0`, not
`C0=1`. [T0/T1: `docs/ingest/report/kernel-conjecture-v2.tex:434-440`]

I found no exact data in `docs/ingest/experiments/out/` suggesting an unbounded `Phi`-argmin ratio; the existing
higher-rank no-center evidence points to constants above `1`, not to blow-up. [T1 from `w40`, `w41`, `w42`]

## Q3. Walls-Check On The (EX) Route

The B4 one-sided ledger wall is a coefficient-mass sign wall: the old cap needed a lower bound on a mass pot,
while the harmonic identity produced only upper bounds. [T0:
`docs/waves/2026-07-02-B4-walls-check.md:36-73`]

The B4 class-count wall is a quotient-packing wall: a per-cluster `O(tau)` bound becomes a total cap only if
the number of geometrically distinct genuine-outside quotient classes is dimension-free. [T0:
`docs/waves/2026-07-02-B4-walls-check.md:77-126`]

In chart language, `(EX)` does not literally ask for visible-set mass or a lower bound on `conv W` mass; it asks
for a chart where positive pivot-row weights see small coordinate excess. [T0/T1 from Q1 definitions]

Thus `(EX)` structurally dodges the old one-sided ledger if the proof works by choosing coordinates and using
the pivot-row negative budget, as the factorization does through `Dneg <= 3 delta`. [T1:
`docs/ingest/report/kernel-conjecture-v2.tex:272-293`]

The one-sided wall reappears if a proposed proof tries to prove that positive `beta_s` mass must land on
low-excess rows by a lower-bound mass ledger; that would be the same forbidden sign direction in chart
coordinates. [T1]

The class-count wall does not literally reappear as a count of outside `C_W` classes, because `Phi_s` is a
weighted sum over chart-coordinate rows and total positive pivot mass is `1+nu_{u_s}`. [T1]

A class-count analogue does reappear if a proof bounds each transverse bad wedge or near-degenerate block
separately and then sums over dimension-many blocks; the high-rank no-center path is the warning sign that
repeated transverse/shear classes can accumulate constant-sized `Phi/delta` beyond `1`. [T1/T2:
`docs/ingest/report/kernel-conjecture-v2.tex:448-454`; `docs/ingest/experiments/out/w40_ndg/part_a_results.txt:7-8`]

Bounding `max_s Phi_s` should not require a dimension-free count if the proof is genuinely aggregate, for
example by a dual certificate that charges the entire `sum_j beta_s^+ E_s(j)` to negative mass and harmonic
identities at once. [T1]

Bounding `max_s Phi_s` probably does require a new idea if the proof is per-class, per-wedge, or per-swap and
then needs the number of bad classes to be `O(1)`. [T1]

Verdict on the walls: `(EX)` is not obviously the same wall in new clothes, but its natural near-degenerate
horn can import a chart-level class-count wall unless the argument is global/weighted from the start. [T1]

## Q4. Attack Routes

### Route 1: Variational / Exchange At The `Phi`-Argmin

Study a `Phi`-argmin over the finite class `M_{1/2}(P)` and derive inequalities against every volume-permitted
multi-row swap. [T1]

The source already gives the exact multi-row swap formula: for swap block `C=A[J,I]`, the volume factor is
`|det C|`, and new coordinates are `x'_I=x_I C^{-1}`, `x'_K=x_K-x_I C^{-1}D`. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:500-518`; `docs/ingest/experiments/out/w40_ndg/proof.md:195-239`]

Single-swap monotonicity is dead as a selector, but local optimality at the global argmin is not dead: it is a
comparison inequality, not a promise that one swap strictly improves the chart. [T1:
`docs/ingest/report/kernel-conjecture-v2.tex:320-326`]

Closest death certificate: single-swap contraction fails, so the route must use multi-row swaps or non-strict
stationarity, not a one-row descent algorithm. [T0/T1]

First lemma to try: if a block carrying `epsilon` of the pivot excess has `|det C|>=1/2`, then the swapped chart
is legal and argmin stationarity bounds that block's contribution by `O(delta)` plus excess moved to other
pivots. [T2]

DRAFT af contracts: "Volume-permitted exchange inequality: for a theta-half `Phi`-argmin `U` and a nonsingular
block swap `V in M_{1/2}(P)`, the explicit Schur coordinate transform implies `Phi(U)<=Phi(V)` with all
coordinates as in the block formula." [T2]

DRAFT af contracts: "Near-degenerate block charge: for a theta-half `Phi`-argmin, the total `beta_s^+ E_s`
carried by rows whose relevant exchange blocks have determinant below `1/2` is at most `C delta(P)`." [T2]

### Route 2: Fixed-Chart LP / Dual Certificate

For a fixed chart, `Phi_s` is a positive weighted sum of known coordinate excesses against the pivot row
`beta_s`; the row-negativity bound and harmonic identities are linear constraints in the beta row. [T1:
`docs/ingest/report/kernel-conjecture-v2.tex:121-129`; `docs/ingest/report/kernel-conjecture-v2.tex:146-151`]

This suggests a fixed-chart LP dual: prove a certificate that upper-bounds `sum beta_s^+ E_s` by `C delta`
using `sum beta_s lambda_s=0`, `sum beta_s=1`, and `sum beta_s^-<=delta`. [T1]

Closest death certificate: coefficient-only LP support-cleanup is dead because it misses full row negativity
geometry, so this route must keep the structural `P=LB`, `BL=I` constraints and not optimize coefficients in
isolation. [T0/T1: `docs/ingest/report/kernel-conjecture-v2.tex:457-463`;
`docs/ingest/report/sections/10-refutations-dead-routes.tex:136-143`]

First lemma to try: for each sharp rank-3 and no-center chart, produce an exact dual certificate proving its
observed `Phi/delta` bound from the beta-row constraints. [T1]

DRAFT af contract: "Fixed-chart beta-dual certificate: given chart coordinates `a_s(j)` and nonnegative dual
variables satisfying explicit linear inequalities, every pivot row with negative mass at most `delta` has
`Phi_s(U)<=C delta`." [T1]

DRAFT af contract: "Certificate existence for rank-3 max-volume best tie: every rank-3 exact signed
idempotent with `delta<=1/4` admits a max-volume triangle whose fixed-chart beta-dual certificate has `C=1`."
[T2]

### Route 3: Rank-Two Perturbation / Deflation

Rank two is qualitatively solved because a max-diameter basis puts every coordinate in `[0,1]`, forcing
`Phi=0`; the source says this has no direct higher-rank analogue. [T0:
`docs/ingest/experiments/out/w40_ndg/proof.md:241-349`; `docs/ingest/report/kernel-conjecture-v2.tex:528-538`]

The plausible higher-rank use is deflation: if a rank-`k` chart has one near-degenerate transverse direction,
collapse or quotient that direction, apply a lower-rank bound, and charge the discarded part to `delta`. [T2]

Closest death certificate: rank induction via stochastic complement is a dead route for the older HLC route,
so a deflation proof must be chart-specific and must not claim the old route is revived. [T0/T1:
`docs/ingest/report/sections/10-refutations-dead-routes.tex:152-172`]

First lemma to try: if all high-`E` rows lie within `epsilon` of a rank-`k-1` coordinate slab, then `(EX)_k`
follows from `(EX)_{k-1}` with an additive `O(epsilon)+O(delta)` term. [T2]

DRAFT af contract: "Coordinate-slab deflation: under an explicit coordinate-slab hypothesis in a theta-half
chart, a lower-rank `(EX)` bound implies a rank-`k` bound with a stated additive error." [T2]

### Route 4: Direct Idempotence In Chart Coordinates

Idempotence gives the harmonic coordinate equations `sum_j beta_s(j)a_t(j)=delta_st`, hence
`sum_j beta_s(j)lambda_s(j)=0`; this is exactly the deficit identity used by factorization. [T0:
`docs/ingest/report/kernel-conjecture-v2.tex:121-125`; `docs/ingest/report/kernel-conjecture-v2.tex:260-270`]

The direct target is sharper than factorization: prove at an argmin that the positive-beta high-excess rows
cannot be too large because the same beta row must satisfy all harmonic equations, not only the one scalar
deficit equation. [T1]

Closest death certificate: raw factorization gauge arguments are dead, so every coordinate statement must be
tied to an actual-row chart and invariant under chart changes, not to an arbitrary realization gauge. [T0/T1:
`docs/ingest/report/sections/10-refutations-dead-routes.tex:129-134`]

First lemma to try: for a `Phi`-argmin, the vector equations
`sum_j beta_s(j)a_t(j)=delta_st` force the beta-positive measure on the cone `{E_s large}` to have negative-mass
payment at least comparable to its `Phi_s` contribution. [T2]

DRAFT af contract: "Multi-coordinate deficit charge: in a theta-half `Phi`-argmin, the full harmonic coordinate
system bounds `sum_j beta_s^+ E_s(j)` by `C` times the negative mass of the pivot row." [T2]

### Route 5: Clone-Quotient / Measure Compression

Raw index path products are refuted by cloning, so any proof should be invariant under merging identical
coordinate rows with their beta weights. [T0: `FINDINGS.md:35-38`]

A clone-quotient formulation would replace index sums by a finite signed measure on coordinate vectors in the
box `[-2,2]^k`, with moment constraints from idempotence and objective `int E_s d beta_s^+`. [T1]

This route is attractive because it attacks class-count by aggregation rather than bounding the number of
classes. [T1]

First lemma to try: merging rows with identical chart coordinates and identical relevant beta columns preserves
`delta`, `Phi_s`, harmonic identities, and theta-half legality. [T2]

DRAFT af contract: "Chart clone-quotient invariance: aggregating identical coordinate atoms preserves the
fixed-chart `Phi_s`, row negative mass, and harmonic coordinate identities." [T2]

## Q5. Refutation Side

A counterexample to a candidate `C0` is a sequence of exact signed idempotents with `delta<=1/4` such that every
theta-half actual-row chart has `max_s Phi_s(U) > C0 delta(P)`. [T0/T1 from the `(EX)` contract]

A counterexample to all universal constants would need the normalized minimum
`min_{U in M_{1/2}} max_s Phi_s(U)/delta(P)` to grow without bound along rank or dimension. [T1]

Pure cloning cannot produce such a counterexample because clone-sensitive index counts are banned and cloned
rows should aggregate to one quotient class. [T0/T1: `FINDINGS.md:35-38`;
`docs/waves/2026-07-02-B4-walls-check.md:117-124`]

Promising refutation family 1: extend the high-rank no-center path / repeated-shear records beyond `k=8` with
full exact theta-half enumeration or certified determinant pruning. [T1]

This family is promising because existing exact records already give `Phi/delta=3/2` at `k=6` and `5/3` at
`k=8`, while the kernel document says scans climb toward a higher envelope. [T0/T1:
`docs/ingest/experiments/out/w40_ndg/part_a_results.txt:7-8`;
`docs/ingest/report/kernel-conjecture-v2.tex:434-440`]

Kill criterion for that refutation family: if certified ratios plateau near `2`, it argues for proving `(EX)`
with `C0>=2`; if certified ratios keep increasing with `k`, it becomes the primary counterexample program.
[T1]

Promising refutation family 2: build many geometrically distinct transverse-pair blocks around a pivot so that
no theta-half chart can include all favorable rows and the positive beta mass is spread across many bad wedges.
[T2]

This family directly tests the chart analogue of the B4 class-count wall: per-block payments may be small, but
dimension-many distinct blocks may make the aggregate large. [T1/T2:
`docs/waves/2026-07-02-B4-walls-check.md:99-126`]

Promising refutation family 3: tune many swap blocks just below the determinant threshold `|det C|=1/2`, so
volume-permitted exchange is unavailable while each block carries some excess. [T2]

A certified numerical hunt should use exact rational `L,B` with `BL=I`, `P=LB`, exact checks of `P^2=P` and row
sums, exact `delta`, exact chart-volume certificates, exact `Phi`, and an independent verifier. [T0/T1 from
`w41` harness description: `docs/ingest/experiments/out/w41_ex/proof.md:168-183`]

For ranks where full basis enumeration is infeasible, the hunt should produce a certificate that no omitted
basis is in `M_{1/2}` or that every omitted theta-half basis has worse `Phi`; otherwise it is only a heuristic
lower bound. [T1]

## Q6. Verdict And Plan

Honest verdict: `(EX)` is a promising primary because the statement is purely existential, the composition is
clean, and the known cheap selectors fail for reasons the global `Phi`-argmin can avoid. [T1] The aesthetic
constant `1` should not be treated as the real target, because higher-rank exact stress data already sits above
`1` if read as the same `Phi` minimization. [T0/T1] The route does not obviously repackage the old one-sided
ledger wall, but any proof that sums per transverse class or per near-degenerate block will hit a chart-level
version of the class-count wall. [T1]

Next wave 1: audit and extend the high-rank no-center/repeated-shear family. [T1] Concrete question: is the
`w40` high-rank `Phi/delta>1` datum fully `(EX)`-comparable, and do exact ratios plateau or grow with `k`?
[T1] Expected artifact: exact rational run bundle plus independent verifier. [T1] Kill criterion: certified
plateau below a modest constant, or certified growth past a preset bound such as `5`. [T1]

Next wave 2: derive the variational exchange inequalities at a `Phi`-argmin. [T1] Concrete question: can the
multi-row Schur swap formula give an aggregate stationarity inequality that survives the staircase and
no-center witnesses? [T1] Expected artifact: one or two single-statement draft lemmas plus exact checks on
mandatory families. [T1] Kill criterion: the inequality reduces to dead single-swap contraction or needs an
`O(1)` class count. [T1]

Next wave 3: build fixed-chart LP dual certificates for the sharp examples. [T1] Concrete question: can
rank-3 transverse/no-center and high-rank no-center charts be certified by the same beta-row dual template?
[T1] Expected artifact: exact dual certificates and a proposed certificate schema. [T1] Kill criterion: the
schema ignores `P=LB, BL=I` and collapses to the coefficient-only LP dead route. [T1]

Candidate DRAFT registry sub-lemma: "DRAFT: Finite chart argmin interface: for every fixed exact signed
idempotent `P`, the finite set `M_{1/2}(P)` has a `Phi`-argmin, and `(EX)` is equivalent to the bound on that
argmin." [T0/T1]

Candidate DRAFT registry sub-lemma: "DRAFT: Volume-permitted exchange stationarity: a theta-half `Phi`-argmin
cannot be improved by any block swap whose determinant keeps the chart in `M_{1/2}`; the coordinate transform is
the Schur formula." [T1]

Candidate DRAFT registry sub-lemma: "DRAFT: Near-degenerate excess charge: at a theta-half `Phi`-argmin, the
total excess on rows whose relevant exchange blocks are below the determinant threshold is `O(delta)`." [T2]

Candidate DRAFT registry sub-lemma: "DRAFT: Fixed-chart beta-dual certificate: an explicit feasible dual
certificate for a chart implies `Phi_s(U)<=C delta(P)` for every pivot row." [T1]

Candidate DRAFT registry sub-lemma: "DRAFT: Chart clone-quotient invariance: merging identical coordinate atoms
preserves the fixed-chart objective and constraints relevant to `(EX)`." [T2]
