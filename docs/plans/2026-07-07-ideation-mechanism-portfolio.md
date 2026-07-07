# W44 ideation deliverable — five new mechanism candidates for (T1)/(T2), ranked

*(Proof-ideation wave W44. Status discipline: everything here is IDEATION — promotes nothing; the
two exact-algebra checks reported inside candidates 1 and 2 (PΓ = 0; S² = S, S1 = 1) were derived
and sanity-checked by the ideation agent during composition and MUST be independently re-established
by fresh codex provers before any banking. No repo files were touched.)*

**Target restated.** (T1): at a tall heavy near-cluster top v, every mass-carrying cluster vertex
u ∈ C admits an optimal hiddenness datum with R = 0, i.e.
conv{p_f − p_u : f ∈ T(u)} ∩ t\*(u)·conv{p_i − p_u : i ∈ O(u)} ≠ ∅. (T2): heavy cluster + cheap
bounded-alpha witnesses everywhere on C ⇒ v ships ≥ c mass outside C or some u ∈ C is
(ρ,κ)-exposed.

**A unifying observation used below.** (T1) is equivalent to
`0 ∈ conv{ (p_f − p_u) − t*(p_i − p_u) : f ∈ T, i ∈ O }`. Row reproduction already gives
`0 = Σ_j P_uj (p_j − p_u)` — zero in the *signed, all-rows* hull with coefficients = u's own row.
The entire terminal node is the upgrade from "zero in the signed hull via row coefficients" to
"zero in the convex hull via (T,O)-structured coefficients" — i.e. (T1) and (T2) are one statement:
convert row coefficients into circuit coefficients. Every candidate below is a force that acts on
row coefficients and circuits *simultaneously*.

---

## Candidate 1 (STRONG) — The signed carré du champ: exact variance annihilation `PΓ(g) = 0`

**Mechanism.** For any P-harmonic g (by the af-validated harmonic-affine bridge, g is exactly
affine-in-position — this includes every admissible exposer value vector, every s = P·1_S, and
ψ = H − φ), define the signed row-variance field
`Γ(g)_i := Σ_j P_ij (g_j − g_i)² = (P g²)_i − g_i²` (the identity uses only Pg = g, P1 = 1). Then
**PΓ(g) = 0 exactly** (PΓ = P(Pg²) − Pg² = 0 by P² = P), and `Γ(g)_i ≥ −ν_i·osc(g)²`. This is the
exact algebraic engine behind the δ=0 Baake–Sumner equal-input rigidity (for stochastic P, Γ ≥ 0
and PΓ = 0 forces variance zero on supports = g constant on every row's support = the
recurrent-class structure theorem in one line), now available *quantitatively at δ > 0*:
near-nonnegative field, annihilated by every row, so
`Σ_j P_vj⁺ (Γ_j + δ·osc²) ≤ 3δ·osc(g)²` — wherever any row puts positive mass, every harmonic
observable has row-variance O(δ·osc²). The scale is the rare correct one: a **τ² budget on squared
oscillation = τ-scale oscillation control per mass-step**, natively at the √δ scale the whole
program fights for; every linear channel loses a factor D = 2+4δ against τ, the quadratic channel
does not. Classical import: Bakry–Émery Γ-calculus / Dirichlet-form rigidity, specialized to the
degenerate exact-idempotent case where the "semigroup" is one projection. The cluster-uniform
kicker: for ν = μP with μ any probability on C (an *exact* fixed vector, `νP = ν`, mass 1,
negative part ≤ δ, concentrated on C by heaviness), one has **νΓ(g) = μPΓ(g) = 0 for every
harmonic g simultaneously** — a single ν provides a uniform quadratic budget for the exposers of
*all* cluster vertices at once: `Σ_i ν_i⁺ Γ_i(h*_u) ≤ 2δ·(1+δ)` for every u ∈ C with the same ν.
That is precisely the shape of control the W42 cluster-uniformity correction demanded and no
banked linear lemma provides (the CS pincer is per-row-at-its-own-zero; this is cross-row,
two-sided, and composes along the mass web without re-centering losses since each row is centered
at its own value). There is also a free tower: `P(g^k) − g^k` is annihilated for every k — a full
exact moment calculus.

**Where tall/heavy enters.** Heaviness: ν = μP is a near-probability concentrated on C — without
it the uniform budget doesn't localize on the cluster. Tallness: pair the budget with ψ = H − φ
and with the optimal exposers h\*_u; depth-Markov puts >94% of witness mass deep-and-far, and the
Γ-budget forbids ν-mass rows from straddling h\*-levels or depth-levels separated by ≫ τ — the
tall regime is exactly where the relevant level separations (0 vs t\* vs 1 in exposer value; top
slab vs aτ in depth against H > 13τ) exceed the τ-spread the budget permits.

**Why it dodges the walls.** Clone-invariant (purely geometric: Γ_i depends on the row measure
and g-values; ν is a hull point). Dimension-free (no counting anywhere; Markov localization only).
No alpha appears (no witness aggregation — the object is the exposer field itself, not the dual).
It does not fight the value-normalization stop head-on: it never tries to turn "h\* small" into
"h\* zero"; it constrains where *mass* can sit relative to h\*-levels, feeding the (T2)
mass-dichotomy instead of (T1) face-selection. **Mandatory dead-route differentiation:** the
recorded kills are the *canonical-g energy method* and *Jensen/convexity* — global convexity
inequalities on one canonical g. This is neither: it is an exact linear identity on the quadratic
field, holds for *every* harmonic g, and is consumed by Markov localization + ν-weighting; no
Jensen step, no energy minimization, no canonical selector. The wave brief must still require the
prover to read the ingest §10 certificate first and state the differentiation explicitly.

**First checkable step (shard-ready contract).** `Signed variance annihilation: for an exact
signed idempotent P and any vector g with Pg = g, the vector Gamma_i = sum_j P_ij*(g_j - g_i)^2
satisfies Gamma = P(g^2) - g^2, P*Gamma = 0, and Gamma_i >= -nu_i*osc(g)^2; consequently for every
row index v, sum_j max(P_vj,0)*(Gamma_j + delta*osc(g)^2) <= 3*delta*osc(g)^2, and for every
probability vector mu and nu = mu*P, sum_i nu_i*Gamma_i = 0.` One wave, near-certain; deps:
lem-harmonic-affine-bridge only; pure algebra, PRIME af-elevation shape. **Failure would teach:**
an error here means the harmonic machinery itself is being misused — maximally cheap to learn, and
the failure mode (if any) would be in the osc lower bound, which would sharpen the negative-part
bookkeeping for all future quadratic arguments.

**Feasibility.** Step 1: strong (the ideation agent verified the algebra during composition; the
codex prover re-derives independently). Program: medium-strong. Most likely failure point: the
quadratic budget, like the linear pencil, may constrain both sides "the same way" and fail to
*separate* witness measure from row measure — i.e. it maps the geography but the T/O selection
still doesn't fall out; even then it strictly extends the toolkit route (a) consumes.

---

## Candidate 2 (STRONG first step, MEDIUM program) — Exact censoring calculus: the Schur/stochastic complement of a signed idempotent is a signed idempotent

**Mechanism.** Block P = [[A, B],[C', D]] over a state split (deleted | kept), with I − A
invertible. The censored (watched-on-kept-states) matrix `S = D + C'(I−A)^{-1}B` satisfies
**S² = S exactly and S1 = 1 exactly** — the ideation-level check: from the four idempotence block
identities, BC' = A(I−A), BD = (I−A)B, DC' = C'(I−A), one gets
S² = D² + 2C'B + C'(I−A)^{-1}AB = D + C'(I−A)^{-1}B = S, and B1 = (I−A)1 gives S1 = 1. So Meyer's
stochastic-complement theory survives *signedness with exact idempotence*: censoring is an exact,
dimension-free, clone-safe (block) operation producing a new exact signed idempotent on fewer
states with explicit `δ(S) ≤ δ·(1 + (1+δ)²/(1−‖A‖_{∞→∞}))`-type control. Nothing in the registry
has any operation of this kind — the entire toolkit is static. Classical import: censored Markov
chains / stochastic complementation (Meyer), balayage. The intended use is a
*middleman-elimination* design for (T2): censor away the transient intermediate states (neither
cluster, nor visible-recurrent, nor deep-far), so that in S the actors are only {cluster, visible
hull, deep-far witnesses} and v's shipped mass resolves *directly* onto them — the (T2) trichotomy
becomes coefficient-visible in S's rows, where the row-far dual certificate and pincer can finally
bite on resolved coefficients. Separately, the *inapplicability* of censoring is itself the lever:
if the cluster block A_C has I − A_C nearly singular (the no-shipping branch), the cluster carries
a near-eigenvector at eigenvalue ≈ 1, and one P-application regularizes it exactly (`g := Pφ̃` is
exactly harmonic with ‖g − φ̃‖_∞ ≤ ‖Pφ̃ − φ̃‖_∞, by P² = P) — producing an exact affine observable
≈ 1 on the cluster, ≈ 0 elsewhere: an exposer template. **The leak/closure dichotomy of censoring
is (T2)'s dichotomy in algebraic form.**

**Where tall/heavy enters.** Heaviness + the ship-nothing branch = near-closure of the cluster
block = the singular side of the dichotomy (this is where the exposer template appears); the
shipping branch is where censoring applies with 1/c-controlled constants. Tallness: it keeps the
kept-block geometry honest — residual cancellation (banked) makes shallow-outside mass O(ν) in
tall regimes, so the censored middle is genuinely transient-shallow and δ(S) stays O(δ/c); and the
deep-far witness rows survive censoring as kept states.

**Why it dodges the walls.** Clone-invariance: block operations respect clone classes (delete/keep
whole classes). Dimension-free: the δ(S) bound is a norm bound, no counting. No alpha, no LP
faces, no value normalization anywhere — it changes the *object*, not the certificate. It cannot
re-walk the raw-index path products: (I−A)^{-1} = ΣA^k is a resolvent, and only its norm and the
resolved (geometric) rows are consumed, never per-path products.

**First checkable step (shard-ready contract).** `Censoring exactness: for an exact signed
idempotent P written in block form [[A,B],[C,D]] with ||A||_{inf->inf} < 1, the censored matrix
S = D + C*(I-A)^{-1}*B satisfies S^2 = S and S*1 = 1, and delta(S) <= delta(P)*(1 +
(1+delta(P))*(1+2*delta(P))/(1 - ||A||_{inf->inf})).` (Prover to tighten/fix the constant; the two
identities are the load-bearing content.) One wave, near-certain, deps: def-signed-idempotent
only; pure algebra, PRIME af-elevation candidate. **Failure would teach:** if S² = S fails, exact
idempotence does not survive censoring and the whole "dynamic operations" family (censoring,
deflation, lumping) is dead at once — a one-wave kill of three ideas.

**Feasibility.** Step 1: strong. Program: medium — the honest catch is that the second step must
pick the censored set so that (i) I − A is invertible with universal margin and (ii) the
height/visibility geometry of S provably relates to P's (censoring moves positions of kept rows;
the visible set of S vs W(P) is real work and the likely failure point).

---

## Candidate 3 (MEDIUM-STRONG) — Merge-and-return: the cluster observable s = P·1_C and the forced return-flow identity

**Mechanism.** The vector `s = P·1_C` (signed mass a row ships into the cluster) is exactly
P-harmonic (`Ps = P²1_C = s`), hence by the af-validated bridge exactly affine-in-position with
`s_i = p_i·s` and `‖s‖_∞ ≤ 1+δ`. Two consequences, both unexploited in the registry. (i)
**Cluster mass uniformity**: `|s_u − s_v| ≤ ‖p_u − p_v‖₁·(1+δ) ≤ 4τ(1+δ)` for u ∈ C — heaviness
of v propagates to *every* cluster row automatically, converting (T2)'s v-only hypothesis into a
cluster-uniform one for free (a direct hit on the W42 cluster-uniformity wall, on the mass side).
(ii) **The return-flow identity**: evaluating harmonicity of s at v and bookkeeping (the
ideation-level check: `Σ_{k∉C} P_vk s_k = s_v − Σ_{k∈C} P_vk s_k ≥ s_v(1−s_v) − 4τ(1+δ) − 2δ`
using uniformity and the sign split) forces
`Σ_{k∉C} P_vk⁺·max(s_k,0) ≥ s_v(1−s_v) − 5τ`: **the mass v ships out of the cluster must land on
states that ship fraction ≈ (1−θ) of their own mass straight back into C** — the merged 2-state
idempotent's trace identity (a nontrivial 2×2 idempotent has trace 1, so self-coefficients 1−θ
and 1−φ force φ = 1−θ) made exact with O(τ+δ) slack. This is the first banked-toolkit-shaped fact
whose conclusion is a *lower bound on specific return coefficient masses* — i.e. it points in the
row-to-circuit direction (T2) needs, where every dual certificate so far points the wrong way (the
dual-direction wall). Classical import: lumpability/aggregation of Markov chains, renormalization.
Third piece, same observable: the s-max-vertex dichotomy — h = (max s − s)/(range) is an
admissible exposer at the s-maximizing vertex (template: lem-conditional-g-near-exposer with 1_C
in place of 1_{G_a}, whose global-max hypothesis mechanics transfer), so **either the s-max vertex
is (ρ,κ)-exposed or some ρ-far row f has s_f ≥ max s − κ(1+2δ)** — a far near-total feeder exists.

**Where tall/heavy enters.** Heaviness is the input `s_v ≥ 1−θ` (and via uniformity, everywhere
on C). Tallness enters through the banked residual-cancellation lemma: shallow-outside mass is
O(ν·(H+D)/(H−aτ)) = O(ν) in tall regimes, so the return partners forced by (ii) are
ρ-far-or-deep — the returning environment *is* the witness territory, coupling row coefficients to
the far web.

**Why it dodges the walls.** s is geometric (s_i = p_i·s) and C is a union of clone classes ⇒
clone-invariant; no counting; no alpha (no dual witnesses consumed); no value-normalization fight
(the dichotomy needs only the κ-margin of an explicitly constructed exposer, not face membership).
The known danger is different: the constant-θ vs τ mismatch — a far feeder with s_f ≈ 1−θ−κ has
θ·D ≫ τ of positional freedom, so the s-exposer alone cannot pin feeders to a shell. That is
exactly where Candidate 1's quadratic channel or the banked pincer must take over; stated honestly
as the seam.

**First checkable step (shard-ready contract).** `Cluster return identity: for an exact signed
idempotent P, a subset C of row indices, and s = P*1_C, the vector s is P-harmonic with
s_i = p_i . s and -delta <= s_i <= 1 + delta; and for any row v with C contained in the ell-1 ball
of radius 4*tau around p_v, sum over {k not in C} of max(P_vk, 0)*max(s_k, 0) >=
s_v*(1 - s_v) - 4*tau*(1 + delta) - 2*delta.` One wave; deps: lem-harmonic-affine-bridge.
**Failure would teach:** if the return inequality fails, the slack bookkeeping (negative parts
crossing the cluster boundary) is subtler than the merged picture suggests — which would itself be
a certificate narrowing how lumped arguments may be run.

**Feasibility.** Step 1: strong (elementary bookkeeping over the bridge). Program: medium — most
likely failure point is the seam above: converting "far feeders returning (1−θ) of their mass"
into exposure or shipping requires a second channel; alone it stalls at the same constant-θ scale
gap that killed the shell-collapse reading.

---

## Candidate 4 (SPECULATIVE, cheap probe) — Wedderburn deflation: P′ = P − 1ν^T and the exposedness LP as the deflated harmonic box program

**Mechanism.** For any probability μ on C, ν = μP is an exact fixed vector (νP = μP² = ν), and
`P′ = P − 1ν^T` is an *exact idempotent* with row sums 0 and rank r−1 (Wedderburn/spectral
splitting: Pν-outer-products commute suitably, (P−1ν^T)² = P − 1ν^T). Deflating at ν = p_v: every
admissible exposer value vector h at v satisfies `P′h = h` exactly (since
⟨p_v, h⟩ = h(p_v) = 0), so **the exposedness LP at v is precisely the fixed-vector box program of
the deflated idempotent whose v-row is identically zero and whose cluster rows have ℓ1-norm ≤ 4τ
both as positions (p_u − p_v) and as coefficient vectors (P_u· − P_v·)**. Add the exact global
identity trace(P) = rank(P) (clone-invariant: cloning splits diagonal entries but preserves their
sum; rank is clone-invariant). Classical import: idempotent algebra, Wedderburn rank-one
reduction, Peirce decomposition. The hope: the deflated picture makes "tiny rows with tiny
coefficient vectors inside an exact idempotent" the object of study — a regime where norm
inequalities on idempotents (e.g. bounds relating a row's norm to its coefficient row through
P′² = P′) may force structure invisible in the affine picture.

**Where tall/heavy enters.** Heaviness makes the deflated cluster doubly tiny (positions and
coefficients); tallness keeps deflated far-deep rows at norm ≥ ρ − o(τ) — the deflated matrix has
an exact norm hierarchy (0 at v, O(τ) on C, ≥ 4τ far) that the idempotent algebra must reconcile.

**Why it dodges the walls.** Pure algebra: clone-invariant, dimension-free, alpha-free, no LP
faces. Honest structural risk instead: the deflated object leaves the row-sum-1 category
(sums 0), so the τ/ρ/κ scale conventions don't transport — any consequence must be translated
back explicitly; and rank descent cannot be iterated at fixed constants (rank is unbounded), so
this is a reformulation lever, not an induction.

**First checkable step (shard-ready contract).** `Deflation exactness: for an exact signed
idempotent P and any vector nu with nu = mu*P for a probability vector mu, the matrix
P' = P - 1*nu^T satisfies (P')^2 = P', P'*1 = 0, rank(P') = rank(P) - 1, and trace(P) = rank(P);
moreover for nu = p_v every admissible exposer value vector h at v satisfies P'*h = h.` One wave,
near-certain; deps: def-signed-idempotent, lem-hiddenness-dual-witness (for the exposer clause),
bridge. **Failure would teach:** essentially nothing can fail except the rank clause — whose
failure mode (ν outside the row space's "generic" position) would itself be a useful degeneracy
certificate.

**Feasibility.** Step 1: strong. Program: speculative — no contradiction endpoint is currently
visible; its value is reformulation power and the chance that the norm hierarchy inside an exact
row-sum-0 idempotent has a classical inequality (operator-theoretic) nobody has tried here.

---

## Candidate 5 (SPECULATIVE, terrain-mapping) — The δ=0 tangent cone: first-order deformation rigidity at the Baake–Sumner structure

**Mechanism.** Any fixed-rank counterexample sequence to (T1)/(T2) with tallness ratio H/τ → ∞
has H bounded (≤ 2+4δ), hence τ → 0, δ → 0: it converges (rows live in an (r−1)-dimensional
affine space — rank caps the ambient dimension, so compactness is available at fixed rank without
violating dimension-freeness) to a *stochastic* idempotent E plus a first-order signed
deformation. The tangent space of {P² = P} at E is exactly the off-diagonal Peirce blocks:
{X : EX + XE = X} = {X : EXE = (I−E)X(I−E) = 0}, with X1 = 0 for the row-sum constraint. The
terminal node's tall-heavy regime becomes a concrete finite question about E (whose structure is
the fully-understood equal-input/recurrent-class picture) and X: **can a first-order deformation
create a hidden vertex at height ≫ √(rate of created negativity) carrying a heavy near-cluster?**
— a polyhedral/linear-algebra rigidity question at the δ=0 stratum, where ex-hume's sharp 3×3
family must appear as the extremal saturating case. Classical import: deformation theory /
tangent cones of determinantal-type varieties, Peirce decomposition of idempotents.

**Where tall/heavy enters.** Tallness *is* the blow-up parameter (it forces the δ→0 limit);
heaviness passes to the limit as a recurrent-class candidate that is nevertheless hidden at first
order — the rigidity to be proved is that this is impossible.

**Why it dodges the walls.** It is not finite-corner-as-asymptotic in the dead sense provided it
is scoped honestly: the deliverable is per-rank constants B(r) (a generalization of in-flight
route (d) by different machinery — deformation theory instead of exact computation), never a
claim of uniformity; its real product is seeing the *mechanism* in the tractable tangent picture.
Clone-invariance and alpha are non-issues (geometric limit objects).

**First checkable step (shard-ready contract).** `Idempotent tangent space: for a stochastic
idempotent E, the tangent space at E of the variety of exact signed idempotents equals
{X : EX + XE = X, X*1 = 0} = {X : EXE = 0, (I-E)X(I-E) = 0, X*1 = 0}, and along any curve
P_t = E + tX + O(t^2) of exact signed idempotents the negative mass satisfies
delta(P_t) = t*max_i sum_j max(-X_ij,0) + O(t^2) on rows where E has no support overlap with X's
negative part.` (Prover to make the last clause precise; the Peirce part is standard.) **Failure
would teach:** if the tangent characterization misbehaves for *signed* row-sum-1 idempotents, the
variety has stratification pathologies at δ=0 — critical to know before anyone trusts a limit
argument.

**Feasibility.** Step 1: strong (standard). Program: speculative-to-medium; likely failure point
is rank semicontinuity in the limit (rank can drop, changing which E is approached) and the fact
that per-rank rigidity, even if proved, leaves uniformity untouched.

---

# Recommendation (one wave)

Wave **Candidate 1's first lemma** (the signed variance annihilation package) next: it is
near-certain bankable in one wave, it is the only candidate whose very first brick already
delivers *cluster-uniform* control (one ν budgets every cluster vertex's exposer simultaneously —
the exact wall W42 named), and it opens the quadratic channel, which is the only channel operating
natively at the τ² = δ scale rather than losing the factor D against τ. Candidates 2 and 4 are
pure-algebra one-wave lemmas with no geometric risk and could run as a parallel mutually-blind
pair if capacity allows, but if only one wave is funded, Γ dominates on downstream fan-out. The
wave brief must require the prover to read the ingest §10 canonical-g-energy/Jensen death
certificates first and state explicitly why an exact annihilation identity consumed by Markov
localization is neither.

**On (T1) vs (T2) softness.** (T2) is the softer target: its hypotheses are existential (some
cheap bounded-alpha witness per vertex) and its conclusion is a mass/exposure dichotomy — the
native output type of the banked toolkit (pincer, top-concentration, residual cancellation,
top-slab reduction) and of all five mechanisms above, whereas (T1)'s always-tight T/O sets are
exactly the degeneracy-fragile objects the W42 hard stop protects. The W41 exact certificate
record also favors (T2): all four families exhibit the mechanism as absorption/mass dichotomies
with exact residuals that codex fixtures can recompute, while testing always-tightness on a whole
optimal face is the fragile part of every fixture. Aim the new mechanisms at (T2) and let the
in-flight route (b) (strict complementarity / parametric face selection) remain the sole
(T1)-native attack.
