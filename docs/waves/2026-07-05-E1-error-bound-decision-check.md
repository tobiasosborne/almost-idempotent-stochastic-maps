<!--
WAVE: E1 (arm E wave 1, decision-check: complementarity/error-bound reformulation + Luo-Pang
  applicability + uniformity pilot) — 2026-07-05, session 9, bd aism-78w. FIRST-EVER arm-E pull.
WORKERS: two fresh codex exec, prompts in the session scratchpad
  (PROMPT-e1a-error-bound-audit.md, PROMPT-e1b-uniformity-pilot.md). Worker A answer VERBATIM
  below; worker B full report banked VERBATIM at
  runs/2026-07-05-e1-uniformity-pilot/data/pilot-full-report.md (summary + pointer below).
  Workers ran no fr/bd/git and edited no tracked file.
ORCHESTRATOR: mechanical bank; did NOT judge the mathematics (L5). Pilot script rerun from the
  banked bundle (exit 0; one mechanical re-home patch of output/rerun paths, W17b precedent);
  orchestrator INDEPENDENTLY recomputed 3 pilot headline points from the printed matrices alone
  (scripts/orchestrator_recompute.py — all match); worker A's staged quotes spot-checked against
  refs-staging/luo-pang-error-bounds-analytic-1994.txt line loci mechanically (grep), not
  mathematically.
HEADLINE: (A) The staged Luo-Pang 1994 primary does NOT support the lit-review §1.3 attribution
  as directly applicable: the 1/2-exponent results (Thm 4.1/Cor 4.1) require Assumption 4.1 —
  every quadratic NONNEGATIVE on the polyhedron — and the idempotence entries (E^2-E)_ij are
  sign-indefinite on the stochastic polytope (T1 witness at n=2); general analytic Thms 2.1/2.2
  give fixed-n bounds with UNSPECIFIED exponent and instance/compact constants; the staged
  Example 4.2 shows a quadratic system with exponent <= 1/4, so even fixed-n sqrt is NOT free.
  Norm conversion costs n^{3/4} (Frobenius) / n (entrywise-l1) on top. Citation drift caught:
  the monotone-LCP error bound is Mangasarian-Shiau, Math. Programming 36 (1986) 81-89, NOT
  "SIAM JCO 25, 1987" (that is their separate Lipschitz paper). VERDICT: GO-CONDITIONAL as a
  bespoke, clone-invariant, structure-aware metric-subregularity programme; NO-GO as black-box.
  Two named intermediates: (E-int-1) fixed-n feasible-slice local sqrt bound with C_n in stratum
  data, then measure n-dependence; (E-int-2) a nonnegative-quadratic residual R_n with zero set
  S_n and R_n(Q) <= K*eta, K n-free — would make Cor 4.1 applicable by construction.
  (B) Pilot: NO visible blowup — largest certified r ~ 1.375 at the stochasticized ex-hume
  anchor (TRUE n=3 minimum); clone/block-sum invariance exact; coupled n=4..12 bounded.
  BONUS (A, T1): the (EB) formulation itself is clone-lift and block-sum invariant in the
  theorem direction — a smell test all future arm-E proofs must pass.
TIER: worker-tagged (T0 staged loci / exact pilot arithmetic; T1 short proofs; T2 gaps;
  LIT-stated items queued for acquisition). Nothing rigorous; no registry status changed.
-->

# E1 — arm E decision-check: error-bound/complementarity route (Luo–Pang audit + pilot)

## Worker A — applicability audit (verbatim ANSWER-A.md)

# E1 worker A decision-check: complementarity/error-bound route

[T0] **Executive verdict 1/3.** The staged Luo--Pang text supports a general analytic fixed-`n` error bound with an unspecified exponent, and a `1/2` theorem only for quadratic systems satisfying extra nonnegativity/copositivity hypotheses; it does **not** by itself verify the lit-review attribution that `E^2=E, E>=0, E1=1` has a directly applicable Luo--Pang/Mangasarian--Shiau `1/2` error bound.

[T1] **Executive verdict 2/3.** The sharpest dimension obstruction is not the elementary norm conversion, although that already costs `n^{3/4}` for a Euclidean `1/2` bound; the sharp obstruction is that all available black-box constants/exponents are instance- and dimension-dependent, while general polynomial Lojasiewicz exponents degrade with `N=n^2` variables.

[T2] **Executive verdict 3/3.** Verdict: **GO-CONDITIONAL** only as a bespoke, structure-aware metric-subregularity programme; **NO-GO** as a black-box "apply Luo--Pang and done" route.

## A. Reformulation

[T0] The target is exactly `op-classical`: `argument/lemmas/op-classical.md:4` states universal `eta_0,C>0`, independent of `n`, for row-stochastic `Q` with `||Q^2-Q||_{inf->inf} <= eta <= eta_0`, giving a stochastic idempotent `E` with `||Q-E||_{inf->inf} <= C sqrt(eta)`.

[T0] The repo convention fixes row-stochastic and stochastic idempotent as `Q>=0`, `Q1=1`, and `E^2=E`: `CONVENTIONS.md:37-42` and `definitions/def-stochastic.md:13-16`; the map norm is the max row `l1` norm of the matrix residual: `definitions/def-almost-idempotent.md:43-48`.

[T1] Let `x=vec(E) in R^N`, `N=n^2`, and write
`P_n={E in R^{n x n}: E_ij >= 0 for all i,j, sum_j E_ij=1 for all i}`.
Then the stochastic idempotents are
`S_n={E in P_n: G(E)=E^2-E=0}`.

[T1] As a polynomial feasibility system, this is:
`g_ij(E)=(E^2-E)_ij=sum_k E_ik E_kj - E_ij = 0` for `1<=i,j<=n`,
`h_i(E)=sum_j E_ij-1=0` for `1<=i<=n`, and
`b_ij(E)=-E_ij <= 0` for `1<=i,j<=n`.
The `g_ij` are quadratic, the `h_i` and `b_ij` are linear.

[T1] For the programme's query points, `Q in P_n` exactly; hence `b_ij(Q)<=0` and `h_i(Q)=0` exactly, and the only nonzero residual block is `G(Q)=Q^2-Q`.
Thus the desired feasible-point error bound is
`dist_{inf->inf}(Q,S_n) <= C sqrt(||G(Q)||_{inf->inf})`, `Q in P_n`.

[T1] This feasible-point restriction is materially stronger information than a general infeasible test point: all row-sum and bound residuals vanish before any theorem is applied, so a residual of the form `||[b(E)]_+||+||h(E)||+||G(E)||` reduces at `Q` to the quadratic block alone.

[T2] The feasible-point restriction does **not** remove the boundary degeneracy: nearest points of `S_n` may lie on faces of `P_n`, and the active zero entries of a stochastic idempotent are exactly where positivity correction can lose a square root.

### Complementarity forms

[T1] A minimal mixed-complementarity encoding of the bounds is:
`0 <= e_ij ⟂ y_ij=0 >= 0` for all entries, together with the free equations `G(E)=0` and `h(E)=0`.
This is equivalent to the polynomial feasibility system because the complementarity pairs impose only `e_ij>=0`.

[T1] In that mixed form, a pair is strictly complementary when `e_ij>0` and `y_ij=0`; it is degenerate exactly at active zero entries `e_ij=0`, because then both members of the complementarity pair vanish.

[T2] This mixed form is mathematically valid but analytically weak: the complementarity residual contains no information about `E^2-E`, so it does not place the idempotence equation inside Luo--Pang's `1/2` complementarity applications.

[T1] A second, artificial, "functional complementarity" form for each quadratic equality is `0 <= g_ij(E) ⟂ -g_ij(E) >= 0`, together with `h(E)=0` and `E>=0`.
It is equivalent to `g_ij(E)=0` because the two inequalities require `g_ij(E)>=0` and `g_ij(E)<=0`.

[T1] In this second form, every quadratic equality pair is degenerate at every solution: `g_ij(E)=0=-g_ij(E)`.

[T2] This second form is not a useful import of linear/nonlinear complementarity theory; it repackages an equality as two opposite inequalities and leaves the proof in the general analytic-system regime.

[T1] The raw quadratic entries `g_ij` are sign-indefinite on `P_n`, so Luo--Pang's Section 4 nonnegative-quadratic hypothesis is not automatically met.
For `n=2`, if `E=[[a,1-a],[b,1-b]]`, then `g_11(E)=(1-a)(b-a)`, which is positive for `(a,b)=(0,1)` and negative for `(a,b)=(0.8,0)`.

[T0] The repo records the programme's geometric square-root scale as `tau=sqrt(delta)` and the exposedness window as `H=O(sqrt(delta))`: `CONVENTIONS.md:51-60`; it also records the honest headline that the realizable-family relation is linear `delta=H/2`, with the quadratic-looking envelope coming from the window: `PRD.md:48-50`.

[T2] The real connection between complementarity degeneracy and the exposedness window is qualitative, not yet a theorem: zero positivity constraints are where a signed idempotent can exit the stochastic cone, but Luo--Pang's staged complementarity statements do not identify this with the programme's frame-free `H=O(sqrt(delta))` mechanism.

## B. Luo--Pang audit from the staged text

### Staged theorem statements and nearby load-bearing text

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:17-22`] "Using a 1958 result of Lojasiewicz, we establish an error bound for analytic systems consisting of equalities and inequalities defined by real analytic functions. In particular, we show that over any bounded region, the distance from any vector x in the region to the solution set of an analytic system is bounded by a residual function, ralsed to a certain power, evaluated at x. For quadratic systems satisfying certain nonnegativity assumptions, we show that this exponent is equal to ½."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:109-120`] "Second, for the special case where the defining functions of the system (1.1) are quadratic and satisfy some nonnegativity conditions (but are not necessarily convex), we show that 3, = ½is a valid exponent. The latter result is interesting because not only does it provide an explanation to an error bound of Mangasarian and Shiau [ 26] for the monotone linear complementarity problem, it also allows for a generalization to the horizontal linear complementarity problem which has in recent years received an increasing amount of attention in the literature [ 36, 30, 35 ]. Finally, we give other applications of the error bound results. In particular, by specializing (1.2) to the Karush-Kuhn-Tucker conditions of a nonlinear program, we obtain an error bound similar to that in [25] but under absolutely no assumption except for the analyticity of the functions involved. In particular, we do not require any convexity assumptions. We also derive new error bounds for an affine variational inequality, a nonlinear complementarity problem, and the 0--1 integer feasibility problem."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:156-172`] "Theorem 2.1. Let X C_~~ be an open set and f :X--* ~ be an analytic function. Let S denote the solution set o f f ( x ) = O. Suppose S S ~. Then f o r each compact subset X c X , there exist constant .c> 0 and 7 > 0 such that
`dist(s, S) ~<~-If(x) I ~, Vx~X.`

Theorem 2.2. Let S denote the set o f x in ~n satisfying
`fl (x) <~0 . . . . . fr(x) ~<O,       gl (x) = 0 . . . . . gs(x) = O,`
where each fi and g1 are analytic functions defined on some open set X C ~n. Suppose S ~ O. Then f o r each compact subset X c X, there exist constants .r> 0 and 7 > 0 such that
`dist(x, S) ~<~-(II[f(x) ] + U+ IIg(x)II) ~, Vx~~,`
where f ( x ) = (fl (x) . . . . . fr(X) )T and g ( x ) = (gl (x) ..... ge(x) )T."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:218-222`] "The exponent y and the multiplicative constant ~-given in Theorems 2.1 and 2.2 depend only on the functionsfand g, as well as on the size of the compact set where the error bound holds. However, neither theorem gives any clue for computing the exponent y or the multiplicative constant ~-. In Section 4, we will determine these constants explicitly for certain quadratic systems."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:260-261`] "Theorem 3.1. Let M: ~n ~ ~m be an analytic multifunction. Then, for any compact set S in W ~, the multifunction Ms is locally upper Hölderian everywhere in ~~."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:327-345`] "Consider the quadratic functions
`B(x)=½xTQix+g~x+ci,                      i=1 ..... r`
where each Qi ~ E n × n is a symmetric matrix, each qi is an n-vector, and each c/is a constant.
Let A be an m X n matrix and a be an m-vector. We denote by S the solution set of the following quadratic system:
`Ax<~a,         f(x) =0,          i = 1. . . . . r.`

Assumption 4.1. For i = 1. . . . r, fi(x) >~0 for all x ~ P : = {xlAx<a}.

Assumption 4.2. There exists a vector x* ~ S such that for all i = 1. . . . . r, Q/is copositive on the set P - x * ; that is, ( x - x * ) T Q i ( x - x *) >~0 for all x ~ P and for all i."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:347-350`] "Notice that we could have included linear equations in the set P. However, we shall leave these out throughout this section in order to simplify the notation somewhat. If they are included, the only change needed in the error bound results below is to add an extra term in the residual functions to denote their violation."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:442-455`] "Theorem 4.1. Suppose that Assumptions 4.1 and 4.2 hoM. Then, there exist positive constants Kl, Kz, K3 and K4 such that
`dist(x, S) ~< K1(11lAx- a] + II 1/z + II[ A x - a] + II2)`
`+K2           I[Q~xll1/2 ( [ l [ A x - a ] ÷ l [ + l l [ A x - a ] + [ [ 1/2)`
`       i=1`
`      (~                       )~~`
`+ «3           IIQixll 1/2 + 1         V'lf/(x) I`
`       ~i= 1`
`+«4~          [f~(x)l,       Vx~R".`
`       i=1`"

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:782-793`] "Corollary 4.1. Let P = {x]Ax~<a} be a polyhedral set. Suppose that fl . . . . . fr are some quadratic functions satisfying Assumptions 4.1 and 4.2. Then, for any p> 0, there exists some constant ~> 0 such that
`dist(x, S) ~< ~ l / 2 ( x ) ,   Vx with [Ixll ~<p,`
where
`r(x)   =    II [Ax-a] + II + ~ If,(x) I`
`                                     i=1`
is the residual function."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:820-828`] "Corollary 4,2. Suppose, in addition to Assumption 4.1, that the matrices Qx. . . . . Qr are symmetric positive semi-definite and that
`S.'= {xlAx<~a, f i ( x ) = 0 , i = 1. . . . . r}`
is nonempty. Then there exists a constant T> 0 such that
`dist (x, S)~<T (11 [ A x - a ] + [11/2+11[ A x - a ] + [[2+ ~     (Il/(X)[ 1/2.~_Il/(X)])),`
`                        \                                         i=1                          /`
`Vx ~ Nn.`"

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:881-891`] "Theorem 5.1. Let S denote the set of triples (x, A,/z) satisfying the conditions (5.1) where the functions F, g and h are analytic. Suppose S ~ O. Then for any compact set C c__~\" × ~'~ × ~t, there exist positive constants \"rand y such that
`dist((x, A,/~), S) ~<zr(x, A,/~)r,             V(x, A,/z) ~ C,`
where
`r(x, A,/~) = IIL(x, A, tz)II + II Ig(x) ] + II + I1[ -,~] + II + IIh(x)II + I A~'g(x) I`
is the residual function for the system (5.1)."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:980-986`] "Theorem 5.2. Suppose that the AVI (X, q, M) has a solution x* such that
`( x - x * ) X M ( x - x *) >~Ofor all x belonging to the set 9-(X, q, M).`
Then for any compact set f~c ~\", there exists a positive constant \"csuch that
`dist(x, S) ~ 777(X)1/2, V x E X ~ O,`
where S is the solution set of the AVI (X, q, M) and
`~(x) = Il [ A x - a ] + II + Ilßx-bll + I to(x) --xT(q +Mx) l`
is the residual function of the AVI."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1023-1030`] "T h e o r e m 5.3. For any compact set X c ~n, there exist positive constants \"rand y such that
`dist(x, S) ~ ~ ( x ) ~,   Vx~~',`
where
`r(x) = [[[ --f(x) ] + Il + I1[ - x ] + Il + Ix~f(x) [`
is the residual function for the NCP (5.8)."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1053-1061`] "T h e o r e m 5.4. Let (A, B) be a pair of square matrices satisfying the condition (5.10). If the problem (5.9) has a solution, then for any compact set C c ~ 2~, there exists a positive constant ~'> 0 such that
`dist((x, y), S) ~<7-r(x, y)l/2,    V(X,y) ~ C,`
where S is the solution set of (5.9) and
`r(x, y) = IIq +Ax+By[[ + Il[ - (x, y) ] + Il + [xTYl`
is the residual function for (5.9)."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1114-1122`] "Theorem 5.5. Suppose the LCP ( q, M) has a solution x ' f o r which (i) Ms« is nonsingular, and (ii) A~tis copositive on R~+ . Then f o r every compact set C c ~n there exists a constant • > 0 such that
`dist(x, S) <~rr(x) 1/z      Vx~C,`
where S is the solution set of the LCP ( q, M) and
`r(x) = Il[ - x ] + 11+ I1[ - q - M x ] + II + IxT(q +Mx] I`
is the residual function for this problem."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1138-1146`] "Theorem 5.6. For any compact set X c ~~, there exist positive constants • and y such that
`dist(x, S) ~<~r(x) r,     Vx~X,`
where
`r(x) = II [f(x) ] + II + [Ig(x) II + ~    Ixi( 1 - Xi) I`
is the residual function."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1157-1163`] "In the general case, we have not been able to obtain explicit formulas for the multiplier or the exponent in the error bound result. We feel that such formulas would be useful for computational and other purposes; however, these might be difficult to obtain in general, but the task might be possible for special classes of problems. In particular, it would be interesting to investigate the extent to which the error bound results in Section 4 will hold under certain relaxed assumptions."

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1172-1179`] "In a subsequent work, we have shown that Theorem 4.1 and Corollary 4.1 remain valid without Assumption 4.2. From these generalized results, it follows that Theorem 5.2 is valid without the copositivity assumption on the matrix M, that Theorem 5.4 holds for any horizontal LCP (5.9) without the monotonicity assumption (5.10), and that Theorem 5.5 holds without the assumptions (i) and (ii). The proof of the generalized Theorem 4.1 and Corollary 4.1 is based on [ 19, Lemma 3.1 ] which yields a structural characterization for the solution set S of the system (4.1) under Assumption 4.1 alone. The detailed proof will be included in a monograph by the authors dealing with the class of mathematical programs with equilibrium constraints."

### Audit rows

| Staged result | Hypotheses / residual / norm | Exponent | Constant depends on | Conversion to `||.||_{inf->inf}` | Verdict for (EB) |
|---|---|---:|---|---|---|
| [STAGED-quote] Theorems 2.1--2.2, lines 156-172 | [T1] General analytic inequalities/equalities on a compact subset; residual is Euclidean `||[f]_+||_2+||g||_2`; distance is Euclidean in `R^N`. | [T0] Unspecified `gamma>0`. | [T0] Functions and compact-set size, lines 218-220. | [T1] For feasible stochastic `Q`, residual is `||G(Q)||_F <= sqrt(n) eta`; target distance `d_inf <= sqrt(n) d_F`, so a `gamma` bound becomes `d_inf <= c(n) n^{(1+gamma)/2} eta^gamma`. | GIVES-UNSPECIFIED-EXPONENT. |
| [STAGED-quote] Theorem 3.1, lines 260-261 | [T1] Analytic multifunction, compact value restriction; not a direct residual bound for one fixed feasibility set. | [T0] Locally Hölder, exponent not displayed in statement. | [T2] Local analytic stratification constants. | [T2] Same Euclidean-to-row-norm conversion would apply after a parameterization, but no direct `eta` residual is stated. | INAPPLICABLE as a direct (EB) theorem. |
| [STAGED-quote] Theorem 4.1 + Corollary 4.1, lines 327-345, 442-455, 770-793 | [T0] Quadratic equations over a polyhedron, but Assumption 4.1 requires every quadratic `f_i` to be nonnegative on the polyhedron; Assumption 4.2 requires copositivity, unless relying on the unstaged subsequent work. | [T0] `1/2` on bounded regions via Corollary 4.1. | [T2] Instance constants: the proof uses Hoffman constants and minima over finite polyhedral pieces; no `n`-uniform statement is made. | [T1] If it applied with residual `sum_ij |g_ij(Q)|`, then `sum_ij |G_ij(Q)| <= n eta`; Euclidean distance to row norm costs `sqrt(n)`, so `d_inf <= sqrt(n) kappa sqrt(n eta)=kappa n sqrt(eta)`. | INAPPLICABLE directly, because `g_ij=(E^2-E)_ij` is sign-indefinite on `P_n`. |
| [STAGED-quote] Corollary 4.2, lines 820-828 | [T0] Adds positive-semidefinite quadratic matrices to Assumption 4.1. | [T0] Square-root terms appear globally. | [T2] Instance constants; no uniformity in `n`. | [T1] Same or worse than the Corollary 4.1 conversion, depending on residual chosen. | INAPPLICABLE: idempotence entries are neither nonnegative quadratics nor PSD quadratics on `P_n`. |
| [STAGED-quote] Theorem 5.1, lines 881-891 | [T0] Analytic KKT systems; residual includes stationarity, inequality, multiplier nonnegativity, equality, and complementarity terms. | [T0] Unspecified `gamma`. | [T2] Instance/compact constants. | [T1] If vectorized with Euclidean residual, a `gamma` bound costs `n^{(1+gamma)/2}` before any multiplier dimensions. | GIVES-UNSPECIFIED-EXPONENT, not (EB). |
| [STAGED-quote] Theorem 5.2, lines 980-986 | [T0] Affine variational inequality with a copositivity condition on the AVI feasible-complementarity set. | [T0] `1/2`. | [T2] Instance and compact-set constants. | [T2] Not naturally in the row-sum matrix norm; Euclidean conversion would still introduce dimension. | INAPPLICABLE unless the idempotent-map problem is first reduced to such an AVI with verified copositivity. |
| [STAGED-quote] Theorem 5.3, lines 1023-1030 | [T0] Analytic nonlinear complementarity problem `x>=0`, `f(x)>=0`, `x^T f(x)=0`, compact test set. | [T0] Unspecified `gamma`. | [T2] Instance/compact constants. | [T1] Same `n^{(1+gamma)/2}` Euclidean conversion if applied to `N=n^2` variables. | GIVES-UNSPECIFIED-EXPONENT at best; artificial complementarity encodings of `g=0` do not improve this. |
| [STAGED-quote] Theorem 5.4, lines 1053-1061 | [T0] Horizontal LCP under monotonicity condition (5.10), compact test set. | [T0] `1/2`. | [T2] Instance/compact constants. | [T2] Euclidean-to-row conversion remains; no native `inf->inf` statement. | INAPPLICABLE: `E^2=E` is not a horizontal LCP without a new, nontrivial reformulation. |
| [STAGED-quote] Theorem 5.5, lines 1114-1122 | [T0] LCP under nonsingularity and copositivity of a principal-pivot transform. | [T0] `1/2`. | [T2] Instance/compact constants. | [T2] Euclidean conversion remains; no `n`-uniformity. | INAPPLICABLE to the raw idempotent equations. |
| [STAGED-quote] Theorem 5.6, lines 1138-1146 | [T0] 0-1 feasibility encoded analytically. | [T0] Unspecified `gamma`. | [T2] Instance/compact constants. | [T2] Not relevant to stochastic idempotents. | INAPPLICABLE. |

[T0] Loud conclusion: the staged paper contains statements saying `1/2` for **quadratic systems satisfying nonnegativity assumptions** and for **specific complementarity/AVI/LCP classes**, but I found no staged theorem pinning exponent `1/2` for the raw stochastic-idempotent system `E^2-E=0`, `E>=0`, `E1=1`.

[T0] The staged notes added claim a later monograph removes Assumption 4.2, not Assumption 4.1, and the proof is not in the staged text: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1172-1179`.

[T2] Therefore, the lit-review sentence "Mangasarian--Shiau 1987 + Luo--Pang 1994 gives exponent exactly 1/2 at degenerate solutions" is not verified by this staged primary for the programme's system; it remains a refs-acquisition and reformulation obligation.

## C. Dimension audit

### C.1 Ranked dimension entry points

[T2] **Rank 1: uniform metric subregularity constants across all stochastic-idempotent strata.** Fixed `n` has finitely many semialgebraic strata, but the number and conditioning of support/partition/absorption patterns grow with `n`; this is the main open content if one wants a dimension-free `C`.

[LIT-stated] General effective Lojasiewicz bounds for polynomial maps in `N` variables and degree `d` have exponents controlled by quantities of the form `1/(d(3d-3)^{N-1})` or comparable `d^{-O(N)}` bounds; sources to acquire include J. Kollar, "An effective Lojasiewicz inequality for real polynomials", Periodica Mathematica Hungarica 38 (1999), and D'Acunto--Kurdyka, "Explicit bounds for the Lojasiewicz exponent in the gradient inequality for polynomials", Annales Polonici Mathematici 87 (2005).

[T1] With `N=n^2`, any such general exponent is useless for (EB): an error bound `dist <= c eta^gamma` with `gamma<1/2` is weaker than `sqrt(eta)` as `eta downarrow 0`, because `eta^gamma >= eta^{1/2}` for `0<eta<=1`.

[T1] **Rank 2: norm conversions.** For any `A in R^{n x n}`, with Frobenius norm `||A||_F` and row norm `||A||_{inf->inf}=max_i sum_j |A_ij|`,
`||A||_{inf->inf} <= sqrt(n)||A||_F` and `||A||_F <= sqrt(n)||A||_{inf->inf}`.
Proof: each row has `||r||_1 <= sqrt(n)||r||_2`, and `||A||_F^2=sum_i ||r_i||_2^2 <= sum_i ||r_i||_1^2 <= n ||A||_{inf->inf}^2`.

[T1] If a Euclidean theorem gives `dist_F(Q,S_n) <= kappa ||G(Q)||_F^{1/2}`, then for `eta=||G(Q)||_{inf->inf}`,
`dist_{inf->inf}(Q,S_n) <= sqrt(n) kappa (sqrt(n) eta)^{1/2}=kappa n^{3/4} sqrt(eta)`.

[T1] If a theorem instead uses the entrywise `l1` residual `sum_ij |G_ij(Q)|`, then `sum_ij |G_ij(Q)| <= n eta`, so Euclidean distance conversion gives `dist_{inf->inf} <= sqrt(n) kappa sqrt(n eta)=kappa n sqrt(eta)`.

[T2] These norm factors alone do not disprove the route, but they show that a Euclidean black-box theorem cannot be the final dimension-free proof unless its constant carries compensating powers of `n`, which the staged text does not provide.

[T1] **Rank 3: fixed-`n` compactness.** The stochastic polytope `P_n` is compact because it is a closed bounded product of simplices; `S_n` is closed in `P_n`, hence compact and nonempty because the identity matrix belongs to it.

[T1] Theorem 2.2 gives a fixed-`n` Hölder error bound with some exponent: apply it to the analytic system `b_ij(E)<=0`, `h_i(E)=0`, `g_ij(E)=0` on a compact neighborhood of `P_n`; for feasible `Q in P_n`, this yields `dist_F(Q,S_n) <= c_n ||Q^2-Q||_F^{gamma_n}` for some `c_n,gamma_n>0`.

[T2] Fixed-`n` compactness does **not** by itself give fixed-`n` `sqrt` (EB), because arbitrary quadratic systems can have worse exponents; Luo--Pang's own Example 4.2 records a quadratic system where the error-bound exponent is at most `1/4`: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:403-409`.

[T1] Conditional compactness upgrade: if one proves a local feasible-slice `sqrt` bound around every `E in S_n`, then compactness gives fixed-`n` (EB).
Indeed, finitely many local neighborhoods cover `S_n`; away from their union, continuity and compactness give a positive residual floor `m_n>0`; since any two row-stochastic matrices have row-norm distance at most `2`, the away-region bound is `dist_{inf->inf}(Q,S_n)<=2 <= (2/sqrt(m_n)) sqrt(eta)` whenever `eta>=m_n`.

[T2] Thus the open content is not merely compactness; it is local `sqrt` geometry with constants whose finite-cover maximum remains bounded as `n` grows.

[T0] **Rank 4: combinatorial union of strata.** The repo records Baake--Sumner and Hognas--Mukherjea as the load-bearing references for idempotent Markov structure and the `delta=0` anchor: `PRD.md:64-66` and `RESEARCH_NOTES.md:51-55`.

[LIT-stated] The stochastic-idempotent set decomposes by recurrent/absorbing classes and transient rows as convex combinations of class stationary distributions; this is the standard idempotent Markov-chain partition structure attributed in the repo to Baake--Sumner and Hognas--Mukherjea, but the detailed statement still needs byte-verified local refs before use.

[T2] Error-bound constants can blow up near intersections of these strata: support entries approach zero, classes split/merge, and the active set of positivity constraints changes; this is exactly the regime a dimension-free proof must control rather than cover by finitely many fixed-`n` charts.

### C.2 Clone and block-direct-sum smell tests

[T1] Block-direct sums are benign for the target statement. If `Q=diag(Q_1,...,Q_m)`, then `Q^2-Q=diag(Q_1^2-Q_1,...,Q_m^2-Q_m)` and `||Q^2-Q||_{inf->inf}=max_alpha ||Q_alpha^2-Q_alpha||_{inf->inf}`.
If each block has a correction `E_alpha` with constant `C`, then `E=diag(E_alpha)` is stochastic idempotent and gives the same constant for the direct sum.

[T1] A weighted clone lift is also compatible with the formulation. Let `pi:{1,...,N}->{1,...,n}` be a surjection and weights `w_b>0` satisfy `sum_{b:pi(b)=j} w_b=1`. Define `L(Q)_{ab}=Q_{pi(a),pi(b)} w_b`. Then `L(Q)` is row-stochastic and `(L(Q)^2-L(Q))_{ab}=(Q^2-Q)_{pi(a),pi(b)}w_b`, so each cloned row has the same residual row `l1` norm as its parent.

[T1] If `E` is a stochastic idempotent for `Q`, then `L(E)` is a stochastic idempotent for `L(Q)`, and `||L(Q)-L(E)||_{inf->inf}=||Q-E||_{inf->inf}` by the same row-sum calculation.

[T2] Therefore the target formulation passes the clone smell test in the theorem direction, while Euclidean black-box bounds fail the smell test because their constants and norm conversions see the enlarged variable count `N^2`.

[T2] A proof that charges by raw index counts, numbers of active inequalities, or Euclidean dimension is suspect unless it is shown invariant under this clone lift.

## D. Verdict and retarget

[T2] **Verdict: GO-CONDITIONAL.** Resource arm E only if it is retargeted from "apply Luo--Pang" to "prove a structured, clone-invariant feasible-slice error bound for the stochastic-idempotent variety."

[T2] The single sharpest intermediate statement worth proving next is:
For each fixed `n`, prove a feasible-slice local `sqrt` bound
`dist_{inf->inf}(Q,S_n) <= C_n sqrt(||Q^2-Q||_{inf->inf})` for `Q in P_n` near `S_n`, with `C_n` expressed in stratum data; then measure which stratum parameters can or cannot be bounded independently of `n`.

[T2] A more Luo--Pang-specific intermediate is:
Find a residual `R_n(E)` made of nonnegative quadratic functions on `P_n`, with zero set exactly `S_n`, and with `R_n(Q) <= K ||Q^2-Q||_{inf->inf}` using `K` independent of `n`; without this, Corollary 4.1 cannot be applied to the raw idempotence residual.

[T2] Kill criterion 1: produce a fixed dimension `n` and a feasible family `Q_t in P_n` with `eta_t=||Q_t^2-Q_t||_{inf->inf}->0` but `dist(Q_t,S_n)/sqrt(eta_t)->infty`; that would kill (EB), not just arm E.

[T2] Kill criterion 2: prove that every local `sqrt` constant must depend on a support/angle parameter that is unbounded under the weighted clone lift while residual and natural lifted distance are preserved; that would kill dimension-free black-box error-bound proofs.

[T2] Kill criterion 3: show that any nonnegative-quadratic reformulation comparable to `||E^2-E||` already encodes the Kernel/(EX) geometry; that would not kill the theorem, but it would kill arm E as an independent shortcut.

[T1] If a dimension-free feasible-slice error bound is proved in exactly the target norm and residual, it **is** `op-classical`: no downstream interface remains, because `S_n` is precisely the set of row-stochastic idempotents and the residual is exactly `||Q^2-Q||_{inf->inf}`.

[T2] If the bound is instead proved for signed idempotents, Euclidean distance, entrywise residuals, or an artificial complementarity residual, the arm still owes the corresponding bridge back to row-stochastic `Q`, `||.||_{inf->inf}`, and `eta`; these bridges are exactly where dimension can re-enter.

### Refs-acquisition list

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1245-1246`] O.L. Mangasarian and T.-H. Shiau, "Error bounds for monotone linear complementarity problems," Mathematical Programming 36 (1986) 81-89. Acquire because Luo--Pang cites this as the monotone-LCP square-root antecedent; note this staged citation is **1986 Mathematical Programming**, not the lit-review's "SIAM JCO 25, 1987" wording.

[STAGED-quote: `refs-staging/luo-pang-error-bounds-analytic-1994.txt:1247-1248`] O.L. Mangasarian and T.-H. Shian/Shiau, "Lipschitz continuity of solutions of linear inequalities, programs and complementarity problems," SIAM Journal on Control and Optimization 25 (1987) 583-595. Acquire or disambiguate because the prompt asks for "Mangasarian--Shiau 1987" and the staged bibliography separates it from the monotone-LCP error-bound paper.

[LIT-stated] Facchinei and Pang, *Finite-Dimensional Variational Inequalities and Complementarity Problems*, Springer, 2003. Acquire the error-bound/complementarity chapters because the staged Luo--Pang notes added point to later MPEC/generalized results not proved in the staged paper.

[LIT-stated] J. Kollar, "An effective Lojasiewicz inequality for real polynomials", Periodica Mathematica Hungarica 38 (1999). Acquire for explicit dimension/degree exponent degradation.

[LIT-stated] D'Acunto and Kurdyka, "Explicit bounds for the Lojasiewicz exponent in the gradient inequality for polynomials", Annales Polonici Mathematici 87 (2005). Acquire for effective polynomial exponent bounds of `d(3d-3)^{N-1}` type.

[T0] Baake--Sumner and Hognas--Mukherjea are already in the repo acquisition queue for stochastic-idempotent structure: `RESEARCH_NOTES.md:51-55`; promote/byte-verify before using the detailed partition/absorption classification as more than [LIT-stated].

[T2] Optional but useful: acquire Luo--Pang's later MPEC monograph/source alluded to in the staged notes added, because it is the only staged hint that Assumption 4.2 can be removed while retaining the Section 4 square-root theorem.

---

## Worker B — uniformity pilot (summary; full report banked verbatim in the bundle)

Full report incl. every exact matrix and the 17-row assert list:
`runs/2026-07-05-e1-uniformity-pilot/data/pilot-full-report.md`. Rerun:
`python3 runs/2026-07-05-e1-uniformity-pilot/scripts/e1_worker_b_pilot.py` (exit 0).

- Largest certified ratio: `r^2 = 61937/32768` (`r ~ 1.375`) at the stochasticized `ex-hume`
  anchor `s = 1/16` (`eta = 241/32896`, `dist = 241/2048`) — TRUE n=3 minimum over ALL 3x3
  stochastic idempotents (worker enumeration of the four combinatorial types, derived from
  `E^2 = E` as T1, + exact rational vertex-enumeration LPs).
- Clone lift (weighted split) and block direct sum: exactly invariance-compatible for `eta`,
  distance, and candidate idempotents [worker T1 + exact examples] — any dimension blowup must
  be COUPLED.
- Coupled level-chain family, n = 4..12 (absorbing state + shared lower-level leak):
  `r^2` drifts `3/23 -> 11/69`, bounded; constructed-candidate upper bounds only (honest
  framing stamped in the report and bundle README).
- Wave-2 protocol + decision-grade criteria recorded (report §Task 5): kill = a coupled
  rank-growing family with certified LOWER bounds on `min_E ||Q-E||/sqrt(eta)` growing with n;
  support = tightly bracketed bounded ratios on quotient-web families.

## Orchestrator actions (mechanical)

1. Pilot script rerun from the banked bundle: exit 0; report byte-identical modulo the
   re-homed paths.
2. Independent recomputation of 3 headline points from the printed matrices alone
   (`runs/2026-07-05-e1-uniformity-pilot/scripts/orchestrator_recompute.py`): anchor s=1/16,
   coupled n=6, block sum — `(eta, dist, r^2)` all match; `E` candidates verified stochastic
   idempotent. The minimality claims remain worker-certified.
3. No registry/status change. Follow-ups filed in bd (arm-E retarget intermediates; refs
   acquisitions incl. the Mangasarian–Shiau 1986-vs-1987 disambiguation).
