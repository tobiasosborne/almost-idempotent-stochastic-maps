<!--
WAVE: E2 (arm E wave 2, E-int-2 prove-or-refute: the nonnegative-quadratic residual (R)) —
  2026-07-06, session 9, bd aism-5an (E-int-2 half).
WORKERS: two ADVERSARIAL, MUTUALLY BLIND fresh codex exec (constructor E2-C, obstructor E2-O;
  prompts in the session scratchpad: PROMPT-e2c-residual-constructor.md,
  PROMPT-e2o-residual-obstructor.md). Both answers VERBATIM below. Workers ran no fr/bd/git and
  edited no tracked file.
ORCHESTRATOR: mechanical bank; did NOT judge the mathematics (L5). Both worker scripts rerun
  (exit 0); orchestrator INDEPENDENTLY recomputed in exact rationals: the witness
  Q* = ((1/3,2/3),(2/3,1/3)) (residual + eta = 4/9), the P_2 residual formula, the idempotent
  classification samples, the clone-lift residual identity (2->4 lift), the eta formula
  2|a-b|max(1-a,b) and the cubic hatch F_2 <= eta + zero-set on an 8x8 rational grid, and the
  retraction idempotents behind the aff-hull lemma (n=4 samples).
HEADLINE: **E-int-2 REFUTED — KILL-1, twice independently.** Both workers, blind to each other,
  proved the SAME n=2 no-go lemma: every quadratic nonnegative on P_2 and vanishing on S_2 is
  IDENTICALLY ZERO on P_2 (r divisible by (a-b); two-sided nonnegativity across the interior
  rank-one continuum forces r = c(a-b)^2; the isolated idempotent I_2 = Q(1,0) forces c = 0).
  The obstructor propagated it: the weighted clone lift transports the blindness into EVERY
  P_n (n >= 2), so Z_n strictly contains S_n — no family satisfies (a)+(b) at any n; there is
  no K(n) to bound (the failure precedes the domination condition (c), which the obstructor's
  coherence audit shows was the easy direction all along). Structural cause: an interior
  rank-one idempotent CONTINUUM plus an extra boundary idempotent in the same two-state
  quotient — nonnegative quadratics can only touch the continuum to second order, and the
  boundary idempotent annihilates the one remaining coefficient.
  SURVIVORS (constructor): (i) the DEGREE-3 escape hatch — F_2(a,b) = (a-b)^2((1-a)+b) is
  nonnegative on P_2, has zero set EXACTLY S_2, and satisfies F_2 <= eta (higher-degree
  residuals are not blocked; Luo-Pang §4 is degree-2-specific, so this feeds a different
  error-bound engine or a stratified application); (ii) aff(S_n) = the FULL row-stochastic
  affine space (T1, via the deterministic retractions R_{i->j}) — no linear form vanishes on
  S_n, SOS-of-linear permanently dead; (iii) the stratified/disjunctive route (per-chart
  quadratic residuals patched across strata). Honesty: this kills ONLY the quadratic
  Assumption-4.1 construction route; it does NOT disprove fixed-n sqrt error bounds by other
  means. Arm E's remaining content: E-int-1 (stratum-data constants) + the degree->=3 /
  stratified residual question.
TIER: worker-tagged (T0 exact loci/arithmetic; T1 short proofs given in full — two independent
  derivations of the core lemma; T2 gaps). Nothing rigorous; no registry status changed by this
  wave (codification of the no-go + aff-hull lemmas filed as bd follow-up).
-->

# E2 — E-int-2 decider: the nonnegative-quadratic residual is IMPOSSIBLE (KILL-1)

Target refuted (E-int-2 / (R)): for each n, quadratics {f_alpha} with (a) f_alpha >= 0 on P_n;
(b) common zero set in P_n exactly S_n; (c) sum f_alpha <= K*eta, K n-free; (d) clone-lift
compatible.

---

## Worker O — obstructor (verbatim ANSWER-O.md)

# E2 worker O -- obstruction to the nonnegative-quadratic residual

[T1] **KILL-1 achieved.** No family satisfying (a)+(b) exists already at `n=2`; in fact every quadratic nonnegative on `P_2` and zero on `S_2` restricts to the zero function on all of `P_2`.
[T1] **Sharp obstruction.** The rank-one idempotent line in the relative interior forces a nonnegative quadratic to be a multiple of `(a-b)^2`, and the additional idempotent `I_2` forces that multiple to be `0`.
[T1] **What survives for the constructor.** Nothing of E-int-2 survives as stated: by weighted clone-lift, the same blindness occurs inside every `P_n`, so changing `K` or adding clone compatibility cannot repair (a)+(b).

## Line/Segment Analysis

[T0] I use the exact row-stochastic parametrization
`Q(a,b)=((a,1-a),(b,1-b))`, so `P_2` is the square `0 <= a,b <= 1`.

[T0] Exact multiplication gives
`Q(a,b)^2-Q(a,b)=(((1-a)(b-a),-(1-a)(b-a)),(b(a-b),-b(a-b)))`.

[T1] Hence `Q(a,b)` is idempotent iff `(1-a)(b-a)=0` and `b(a-b)=0`, equivalently
`S_2 = {a=b, 0<=a<=1} union {(1,0)}`.

[T1] Let `q` be any quadratic with `q >= 0` on `P_2` and `q=0` on `S_2`, and let `r(a,b)=q(Q(a,b))`.
Since `r(t,t)=0` for every `t in [0,1]`, the degree-two polynomial `r` is divisible by `a-b`, so
`r(a,b)=(a-b) l(a,b)` for an affine linear form `l`.

[T1] For any `t in (0,1)`, the points `(t+eps,t)` and `(t-eps,t)` lie in `P_2` for all sufficiently small rational `eps>0`; nonnegativity of `r` on both sides of the diagonal forces `l(t,t)=0`.
Since `l` is affine and vanishes on the whole open diagonal segment, `l=c(a-b)`.

[T1] Therefore `r(a,b)=c(a-b)^2`; nonnegativity gives `c>=0`, while vanishing at the additional idempotent `I_2=Q(1,0)` gives `0=r(1,0)=c`.
Thus `r` is identically zero on `P_2`.

[T1] Consequently the common zero set
`Z_2 = {Q in P_2 : q(Q)=0 for every q in C_2}` is exactly `P_2`, not `S_2`.

[T0] A concrete rational non-idempotent witness in `Z_2 \ S_2` is
`Q_* = ((1/3,2/3),(2/3,1/3))`.
For this witness,
`Q_*^2-Q_* = ((2/9,-2/9),(-2/9,2/9))` and `eta(Q_*)=4/9`.

[T1] This proves KILL-1 at fixed dimension `n=2`: any finite family satisfying (a) and vanishing on `S_2` has every member zero on all of `P_2`, so its common zero set contains the above `Q_*`.

## Clone-Lift Propagation

[T1] The fixed-dimension obstruction propagates to every `n >= 2`.
Choose a two-block partition of `{1,...,n}` with block map `pi` and positive rational weights `w_j` satisfying `sum_{j:pi(j)=s} w_j=1` for `s=1,2`.

[T1] For a parent `2 x 2` stochastic matrix `R`, define the weighted clone lift
`L(R)_{ij}=R_{pi(i),pi(j)} w_j`.
Then `L(R)` is row-stochastic and exact multiplication gives
`(L(R)^2-L(R))_{ij}=(R^2-R)_{pi(i),pi(j)} w_j`.

[T1] Therefore `R in S_2` implies `L(R) in S_n`, and a non-idempotent parent remains non-idempotent because all weights are positive.

[T1] If `q in C_n`, then `h(R)=q(L(R))` is a quadratic on `P_2`, is nonnegative on `P_2`, and vanishes on `S_2`.
By the `n=2` result, `h` is identically zero on `P_2`.

[T1] Thus every admissible quadratic in dimension `n` vanishes on every weighted clone-lift copy `L(P_2)`.
In particular `L(Q_*)` is a non-idempotent point of `P_n` at which every admissible quadratic vanishes.

[T1] Hence `Z_n` strictly contains `S_n` for every `n >= 2`; the obstruction is not dimension growth of `K`, but exact clone-invariant blindness.

[T0] The helper script `verify_obstruction.py` checks the displayed rational witness and the clone-lift arithmetic with exact `Fraction` arithmetic for `2 <= n <= 7`.

## Local Cone Analysis

[T1] Let `E_pi = 1 pi^T` with `pi_j>0` and `sum_j pi_j=1`; this is a rank-one stochastic idempotent in the relative interior of `P_n`.
The tangent space of the affine hull of `P_n` is `T={X : X1=0}`.

[T1] The idempotence linearization at `E_pi` is
`DG_{E_pi}(X)=X E_pi + E_pi X - X = 1 (pi^T X) - X`, because `X E_pi=0` for `X1=0`.

[T1] Its kernel on `T` is `K={1 v^T : v1=0}`, exactly the tangent space to the rank-one idempotent stratum `rho -> 1 rho^T`.

[T1] If `q in C_n`, then `q(E_pi)=0` and `q>=0` on a relative neighborhood in `P_n`; hence the first derivative of `q` along `T` vanishes and its Hessian on `T` is positive semidefinite.
Since `q` also vanishes on the rank-one stratum, the Hessian vanishes on `K`; positive semidefiniteness then makes `K` a null subspace of the local quadratic form.

[T1] In `n=2`, `T/K` is one-dimensional, so the local form is only a scalar multiple of the transverse square `(a-b)^2`.
The boundary idempotent `I_2` sets that scalar to zero, producing total blindness on `P_2`.

[T2] For `n>2`, this local argument alone does not classify all of `C_n`, but the clone-lift reduction shows that every two-state quotient direction has the same fatal one-dimensional transverse collapse.

## Coherence Audit Of (c)

[T0] The staged Luo-Pang assumptions at `refs-staging/luo-pang-error-bounds-analytic-1994.txt:327-345` require each quadratic equation function to be nonnegative on the polyhedron, and Corollary 4.1 at lines `782-793` uses residual `sum_i |f_i(x)|` plus polyhedral inequality violation.

[T1] On feasible `Q in P_n`, the polyhedral violation is zero and `f_alpha(Q)>=0`, so the residual is `R_n(Q)=sum_alpha f_alpha(Q)`.
If Corollary 4.1 applied and `R_n(Q) <= K eta(Q)`, it would give the desired transfer `dist(Q,S_n) <= tau sqrt(K eta(Q))`.

[T1] Thus the upper domination condition (c) is not the hard detection condition; making `R_n` smaller only strengthens the bound once the zero set is correct.
The real burden is (b), the exact zero set.

[T1] Since KILL-1 shows (b) is impossible already at `n=2`, KILL-2 and KILL-3 are moot for E-int-2 as stated.
There is no dimension-growing `K` to quantify because no admissible zero-set residual exists.

## Complete `n=2` Decision

[T1] `C_2`, modulo functions vanishing on the affine hull of `P_2`, is the zero cone.
Equivalently, every `q in C_2` vanishes at every point of `P_2`.

[T1] Therefore `Z_2=P_2`.
Since `S_2={Q(a,a):0<=a<=1} union {I_2}` is a proper subset of `P_2`, condition (b) is impossible for any finite or infinite family of such quadratics.

[T1] The exact structural obstruction is the coexistence of an interior rank-one idempotent continuum and an extra boundary idempotent in the same two-state quotient.
Nonnegative quadratics can touch the interior continuum only to second order, and the boundary idempotent annihilates the only remaining second-order coefficient.

---

## Worker C — constructor (verbatim ANSWER-C.md)

# E2 worker C answer: nonnegative-quadratic residual

[T1] Executive verdict: (R) NOT FOUND; in fact (R) is impossible already for
`n=2`, so no family satisfying the stated "for each n" target exists.
[T1] The obstruction is degree-exact: on `P_2`, any quadratic polynomial
nonnegative on the square and vanishing on all rank-one idempotents must be
`c(a-b)^2`, hence it cannot also vanish at the isolated idempotent `(a,b)=(1,0)`
unless `c=0`.
[T0] Exact rational witnesses and the weighted clone residual identity are
asserted in `waves-scratch/e2-nonneg-residual/exact_checks.py`; running
`python3 waves-scratch/e2-nonneg-residual/exact_checks.py` exits `0`.

## Sources and conventions read

[T0] `docs/waves/2026-07-05-E1-error-bound-decision-check.md:255-263` records
the weighted clone lift
`L(Q)_{ab}=Q_{pi(a),pi(b)} w_b` and the identity
`(L(Q)^2-L(Q))_{ab}=(Q^2-Q)_{pi(a),pi(b)}w_b`.

[T0] `refs-staging/luo-pang-error-bounds-analytic-1994.txt:327-345` states the
quadratic system and Assumptions 4.1/4.2; Assumption 4.1 is exactly the
requirement that each quadratic equation function be nonnegative on the
polyhedron.

[T0] `refs-staging/luo-pang-error-bounds-analytic-1994.txt:782-793` states
Corollary 4.1 with residual `r(x)=||[Ax-a]_+||+sum_i |f_i(x)|`.

[T0] `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1172-1179` says the
later work removes Assumption 4.2, not Assumption 4.1.

[T0] `CONVENTIONS.md:37-42` and `definitions/def-stochastic.md:13-16` fix the
row-stochastic convention and stochastic idempotents as `Q>=0`, `Q1=1`, and
`Q^2=Q`.

## n=2 warm-up: complete obstruction

### Exact parametrization

[T1] Every `Q in P_2` has the form
`Q(a,b)=[[a,1-a],[b,1-b]]` with `0<=a,b<=1`.

[T1] Direct multiplication gives
`Q(a,b)^2-Q(a,b) =
[[(1-a)(b-a),(1-a)(a-b)],[b(a-b),b(b-a)]]`.

[T1] Therefore `Q(a,b)^2=Q(a,b)` iff either `a=b`, or both `1-a=0` and `b=0`.

[T1] Hence
`S_2 = {Q(t,t): 0<=t<=1} union {Q(1,0)}`.

[T1] The row-sum residual is zero row-by-row:
for stochastic `Q`, `(Q^2-Q)1=Q(Q1)-Q1=Q1-Q1=0`.

[T1] In this parametrization
`eta(Q(a,b))=2|a-b| max(1-a,b)`.

[T0] The script checks the exact idempotents `Q(0,0)`, `Q(1/2,1/2)`,
`Q(1,1)`, and `Q(1,0)`, and checks the non-idempotent witness
`Q(0,1)` with `Q^2-Q=[[1,-1],[-1,1]]` and `eta=2`.

### No-go lemma for quadratic nonnegative residuals on P_2

[T1] Let `g(a,b)` be a real polynomial of degree at most `2`, nonnegative on
the square `[0,1]^2`, and zero on all of `S_2`.

[T1] Since `g(t,t)=0` for infinitely many `t in [0,1]`, the quadratic
polynomial `t -> g(t,t)` is identically zero.

[T1] Thus `g(a,b)` is divisible by `a-b`, so
`g(a,b)=(a-b)(u a+v b+w)` for some real `u,v,w`.

[T1] Fix `t in (0,1)` and perturb to `(t+eps,t)` and `(t-eps,t)` for small
nonzero rational `eps`; both points remain in the square, and nonnegativity on
both sides of the zero line forces `(u+v)t+w=0`.

[T1] Since this holds for all `t in (0,1)`, `w=0` and `u+v=0`, so
`g(a,b)=u(a-b)^2`.

[T1] Nonnegativity on the square forces `u>=0`.

[T1] The isolated idempotent `Q(1,0)` gives `0=g(1,0)=u`, hence `u=0` and
`g` is identically zero on `P_2`.

[T1] If a finite family `{f_alpha}` satisfying (a) and (b) existed for `n=2`,
then each restricted `g_alpha=f_alpha|_{P_2}` would be nonnegative and zero on
`S_2`, hence each `g_alpha` would be identically zero; the common zero set would
be all of `P_2`, contradicting (b).

[T1] Consequently there is no fixed-`n` construction for `n=2`, no `K(2)`, and
no dimension-free `K`.

### Degree-three escape hatch, not usable for E-int-2

[T1] The obstruction is specifically quadratic: the cubic
`F_2(a,b)=(a-b)^2((1-a)+b)` is nonnegative on `P_2`.

[T1] Its zero set on `P_2` is exactly `S_2`, because either `a=b` or
`(1-a)+b=0`, and the latter is exactly `(a,b)=(1,0)`.

[T1] It satisfies `F_2(Q)<=eta(Q)` on `P_2`, since
`(1-a)+b <= 2 max(1-a,b)` and `|a-b|<=1`.

[T2] This does not feed Luo-Pang Corollary 4.1 as staged, because E-int-2 asks
for quadratic functions satisfying Assumption 4.1.

## Candidate ledger

### 1. Raw residual entries and fixed row partial sums

[T1] Define `G(Q)=Q^2-Q`; the entry functions `G_ij` and fixed partial sums
`sum_{j in J} G_ij` are quadratic.

[T1] They fail (a): already in `n=2`, the nontrivial fixed partial sums are
singletons or their negatives because each residual row has zero sum.

[T0] At `Q(0,1)`, `G=[[1,-1],[-1,1]]`, so `G_11>0`, `G_12<0`, `G_21<0`,
and `G_22>0`.

[T0] At `Q(4/5,0)`, `G_11=-4/25` and `G_12=4/25`.

[T0] At `Q(0,2/5)`, `G_21=-4/25` and `G_22=4/25`.

[T1] Therefore every nonzero singleton partial sum has both signs on `P_2`;
the empty and full-row sums are identically zero and cannot cut out `S_2`.

[T2] These functions are clone-formula compatible at the residual level, but
the sign failure kills them before (b), (c), or (d) matter.

### 2. Positive/negative flux split of a residual entry

[T1] For each row `i` and column `k`,
`(Q^2-Q)_ik = p_ik(Q)-ell_ik(Q)` with
`p_ik=sum_{j != k} Q_ij Q_jk >=0` and
`ell_ik=Q_ik(1-Q_kk)>=0` on `P_n`.

[T1] The nonnegativity part (a) holds for the individual pieces `p_ik` and
`ell_ik`.

[T0] The exact idempotent `Q(1/2,1/2)` in `P_2` has
`p_11=Q_12 Q_21=1/4` and `ell_11=Q_11(1-Q_11)=1/4`.

[T1] Thus these nonnegative quadratic pieces do not vanish on `S_n`, so (b)
fails.

[T1] Since they are positive at a point with `eta=0`, any sum containing one of
these pieces also fails (c) for every finite `K`.

[T2] The signed difference `p_ik-ell_ik` recovers the residual entry but then
returns to the sign-indefiniteness of Candidate 1.

### 3. Diagonal, trace, and Frobenius-style quadratics

[T1] The trace candidates
`tr(Q-Q^2)`, `tr(Q^2-Q)`, and
`sum_ij Q_ij Q_ji - tr(Q)=tr(Q^2)-tr(Q)` are quadratic.

[T0] At the swap matrix `Q(0,1)`, `tr(Q-Q^2)=-2`,
`tr(Q^2-Q)=2`, `tr(Q)-||Q||_F^2=-2`, and
`sum_ij Q_ij Q_ji-tr(Q)=2`.

[T0] At the lazy matrix `Q(3/4,1/4)`,
`tr(Q-Q^2)=1/4`, `tr(Q^2-Q)=-1/4`,
`tr(Q)-||Q||_F^2=1/4`, and
`sum_ij Q_ij Q_ji-tr(Q)=-1/4`.

[T1] Hence each sign choice among these standard trace forms fails (a).

[T1] Adding a linear term that vanishes on all stochastic idempotents cannot
repair this route, because the affine hull of `S_n` is the whole row-stochastic
affine space; see Candidate 5.

[T2] Adding a linear term that does not vanish on `S_n` would need exact
cancellation on every idempotent stratum, and the `n=2` no-go lemma says no
quadratic correction of this type can satisfy (a) and (b) on `P_2`.

### 4. Fixed pairings with `Q(I-Q)` or `(I-Q)` columns

[T1] Let `A(Q)=Q(I-Q)=Q-Q^2`.

[T1] In `n=2`, with `d=a-b`,
`A_11=(1-a)d`, `A_12=-(1-a)d`, `A_21=-bd`, and `A_22=bd`.

[T1] For a fixed linear pairing
`L_c(Q)=sum_ij c_ij A_ij`, this becomes
`L_c(Q)=d((1-a)(c_11-c_12)+b(c_22-c_21))`.

[T1] If `L_c>=0` on all of `P_2`, then approaching the line `a=b=t` from the
two sides forces `(1-t)(c_11-c_12)+t(c_22-c_21)=0` for every `t in (0,1)`.

[T1] Therefore `c_11=c_12` and `c_22=c_21`, so `L_c` is identically zero on
`P_2`.

[T1] The same argument with signs reversed rules out nonzero fixed pairings
that are nonpositive on all of `P_2`.

[T2] Thus fixed sign-definite pairings with `Q(I-Q)` cannot produce the
nonnegative quadratic residual demanded by Assumption 4.1.

[T2] Pairings of the form `Q_ij(v_j-(Qv)_j)` either reduce to nonnegative flux
pieces that fail to vanish on rank-one idempotents, or to signed residual
pairings covered by the preceding sign obstruction.

### 5. Sum of squares of linear forms

[T1] The affine hull of `S_n` is the full row-stochastic affine space
`{Q: Q1=1}`.

[T1] Proof: the identity matrix `I` is in `S_n`.

[T1] For every `i != j`, let `R_{i->j}` be the deterministic retraction that
sends state `i` to state `j` and fixes every other state.

[T1] Each `R_{i->j}` is row-stochastic and idempotent, because `j` is fixed and
all other fixed states remain fixed after one step.

[T1] The difference `R_{i->j}-I` has only one nonzero row, namely
`e_j-e_i` in row `i`.

[T1] These differences form the standard basis of all row-sum-zero
perturbations, so `aff(S_n)={Q:Q1=1}`.

[T1] Therefore any linear form vanishing on all of `S_n` vanishes on the entire
row-stochastic affine space.

[T1] A sum of squares of such linear forms is identically zero on `P_n`, so the
SOS-of-linear route cannot cut out `S_n`.

### 6. Clone-lift check

[T1] The weighted clone lift from E1 preserves row-stochasticity:
`sum_b L(Q)_{ab}=sum_j Q_{pi(a),j} sum_{b:pi(b)=j} w_b=1`.

[T1] It also satisfies
`(L(Q)^2-L(Q))_{ab}=(Q^2-Q)_{pi(a),pi(b)}w_b`.

[T1] Consequently every cloned row has the same residual `l1` norm as its
parent row.

[T0] The script checks this with the exact sample
`Q=Q(2/3,1/5)`, `pi=(0,0,1)`, and weights `(1/3,2/3,1)`.

[T2] Candidate families based on raw residual entries inherit this residual
identity, but they fail nonnegativity; trace/Frobenius candidates either fail
nonnegativity or charge raw clone counts in non-invariant ways.

## Consequence for E-int-2

[T1] Since (R) requires the construction for each `n`, the `n=2` no-go lemma
disproves E-int-2 exactly as stated.

[T1] The failure occurs before the residual comparison (c): there is no
nonnegative quadratic family on `P_2` whose common zero set is `S_2`.

[T1] Therefore no exact growth `K(n)` exists for the stated quadratic target;
even a dimension-dependent `K(2)` has no object to bound.

[T2] This does not disprove a fixed-`n` square-root error bound by other means;
it only kills the Luo-Pang Assumption-4.1 construction route requiring
nonnegative quadratic equation functions.

## What a wave-3 construction should try

[T1] Do not continue searching for E-int-2 as stated; the `n=2` obstruction is
structural and exact.

[T2] A local-stratum version may still be viable: near the rank-one diagonal
in `P_2`, `(a-b)^2` is the natural nonnegative quadratic; near the isolated
identity, a different local chart is needed.

[T2] A higher-degree nonnegative residual is plausible: the exact `n=2` cubic
`(a-b)^2((1-a)+b)` has the right zero set and satisfies `F_2<=eta`.

[T2] A disjunctive or stratified Luo-Pang application may be the right
replacement: apply quadratic nonnegative residuals on individual polyhedral
pieces or charts, then patch constants outside Assumption 4.1.

[T2] Any proposed global residual must pass the weighted clone lift with the
same `K`; raw Euclidean/Frobenius aggregates remain suspect because they see
clone multiplicity rather than parent row residual mass.
