# W62 L5 routine batch — hostile verification verdict

R0: VALID
R1: VALID
R2: VALID
R3: VALID

## R0 — mass barycenter dualization

For fixed (y\in Y_v), direct recomputation gives
\[
\begin{aligned}
 \sum_{j\in A}(P_{vj})_+z_y(j)
 &=\sum_Q\left(\sum_{j\in A\cap Q}(P_{vj})_+\right)
       y\cdot(p_v-p_Q)\\
 &=\sum_Qm_Qy\cdot(p_v-p_Q)\\
 &=S\,y\cdot\left(p_v-\sum_Q\mu_Qp_Q\right)
 =S\,y\cdot(p_v-q).
\end{aligned}
\]
This is a pointwise identity on one common set (Y_v), so (S>0) permits
taking the same supremum on both sides. There is no interchange of a supremum
and a sum. The quantifier order is correct: (A), hence (m,S,\mu,q), is fixed
before (y) is optimized. Zero weights cause no problem, while (S=0) is
properly excluded because (\mu) and (q) would then be undefined.

The cited contracts are used as stated. `lem-top-support-dual-face` supplies a
nonempty (Y_v) under the L5 hypotheses, and
`lem-affine-barycenter-identity` applies to the finite probability measure
(\mu). The separate (\delta=0) observation is correct but not needed: an L5
datum already has (\delta>0), and the cited endpoint lemma would give (H=0),
contrary to (H>0).

The partial-clone attack passes. Under an equal split of an incoming atom of
mass (\alpha), selecting only one clone contributes
(m_Q=\alpha/2) and exactly
((\alpha/2)y\cdot(p_v-p_Q)) to the left side. It contributes the same weight
to (S) and to the moment defining (q), so the displayed pointwise identity
still holds. No requirement that (A) be a union of full fibers was smuggled
in.

No small exact counterexample can evade the displayed identity: once the
objects are defined, it is finite linear algebra independent of rank. Exact
rational rank-one through rank-three projection fixtures, including partial
selection after a weighted clone split, reproduce the equality term by term.

## R1 — top-face primal ray formula

Put (d=p_v-q). Since (H=d_1(p_v,C_W)), for every
(\|y\|_\infty\le1),
\[
 y\cdot p_v-h_{C_W}(y)
 =\min_{c\in C_W}y\cdot(p_v-c)\le H.
\]
Consequently the registry description of (Y_v) is exactly equivalent to
\[
 \|y\|_\infty\le1,\qquad
 (p_v-p_w)\cdot y\ge H\quad\text{for every visible row point }p_w.
\]
Equality in the support expression follows from the reverse inequality. This
checks both directions of (R1.1), including all boundary equalities.

For multipliers (\lambda_w\ge0), the correct upper Lagrangian for the
maximization problem is
\[
 d\cdot y+\sum_w\lambda_w((p_v-p_w)\cdot y-H).
\]
Maximizing it over the box gives, with the verified plus sign,
\[
 \left\|d+\sum_w\lambda_w(p_v-p_w)\right\|_1
       -H\sum_w\lambda_w.
\]
The primal is a feasible bounded finite LP. Its ordinary finite dual is
feasible, so strong duality and dual attainment apply. If
(\Lambda=\sum_w\lambda_w>0), the substitution
(c=\Lambda^{-1}\sum_w\lambda_wp_w\in C_W) is reversible because every point
of the finite visible hull has a finite convex representation. If
(\Lambda=0), nonnegativity forces every multiplier to vanish and the value is
(\|p_v-q\|_1); no (c) is needed. Thus the stated minimum, understood as the
disjoint domain
\[
 \{\Lambda=0\}\ \cup\ ((0,\infty)\times C_W),
\]
is attained. No positivity of (H), beyond what “hidden top vertex” normally
provides, is secretly used.

Weighted cloning embeds every old row by the (\ell^1)-isometry
(Jx=(w_bx_{\pi(b)})_b), where the weights over each clone fiber sum to one.
It preserves (K(P)), (C_W), all relevant distances, and the ray objective.
Dual box functionals restrict by weighted averaging and lift by taking equal
values on clones, so the primal support value is also unchanged. The formula
therefore survives the clone audit.

The one-dimensional and two-dimensional rational tests in the proof recompute
correctly, including a genuinely nonzero optimal multiplier in the latter.
No exact signed-idempotent counterexample of rank at most three was found. More
decisively, any such counterexample would contradict the finite LP duality
calculation above once the cited exact description of (Y_v) is imposed.

## R2 — positive-flow foldback

Let (a_i=P_{vi}=b_i+r_i-a_i^-), where (0\le b_i\le a_i^+),
(r_i=a_i^+-b_i), and (\sum_{i\in Q}b_i=m_Q). For each receiver (k),
(P_v=P_vP) gives
\[
\begin{aligned}
 a_k={}&\sum_i b_iP_{ik}^+ +\sum_i r_iP_{ik}^+
        -\sum_i a_i^-P_{ik}^+\\
      &-\sum_i b_iP_{ik}^- -\sum_i r_iP_{ik}^-
        +\sum_i a_i^-P_{ik}^-.
\end{aligned}
\]
Solving for the first term yields exactly R2.4:
\[
\begin{aligned}
 \sum_i b_iP_{ik}^+={}&a_k-\sum_i r_iP_{ik}^+
 -\sum_i a_i^-P_{ik}^-\\
 &+\sum_i b_iP_{ik}^-+\sum_i r_iP_{ik}^-
 +\sum_i a_i^-P_{ik}^+.
\end{aligned}
\]
Thus both discarded terms really are nonpositive after multiplication by
(g_k\ge0). Combining (b_i+r_i=a_i^+) leaves two, and only two, adverse
budgets:
\[
 \sum_i a_i^+\sum_kP_{ik}^-g_k
 \quad\text{and}\quad
 \sum_i a_i^-\sum_kP_{ik}^+g_k.
\]
The first is at most (M(1+\delta)\delta), and the second is separately at
most (M\delta(1+\delta)), using `lem-mass-split` exactly as stated. This
recomputes the claimed error (2\delta(1+\delta)M); no aggregate of unknown
sign was discarded.

All requested edge cases pass. If (m=0), the left side is zero. If
(\delta=0), every coefficient is nonnegative, both leaks vanish, and the
subflow is dominated by (P_vP=P_v), with equality for the full measure. If
(M=0), then (g=0). Constant (g), arbitrary fiber indicators, and fibers
with (A_Q=0) are covered by the same calculation. Since the finite domain is
nonempty, the existence of a map into ([0,M]) already entails (M\ge0).

Under a weighted clone split, incoming coefficients are divided among the
clones according to their weights, source rows are duplicated, and their
full-fiber totals are unchanged.
The proportional disintegration gives (b'_a=w_ab_{\pi(a)}). Hence R2.2, both
leak sums, the right-side fiber aggregate, and (\delta) are all literally
preserved. The occurrence of (\sum_iP_{vi}P_{ik}) is one fully summed matrix
identity, not a raw-index path-product lower bound.

As an additional exact counterexample hunt, 6,940 box-extreme cases were
checked over rational row-sum-one idempotent projections of rank at most three
and size at most six. For each matrix, all rows and all full-fiber indicator
functions were tested; the extremal submeasure takes every allowed (m_Q)
because its left coefficient is nonnegative. No negative slack occurred. This
finite search is only corroboration; the termwise calculation above is the
proof.

## R3 — universal exterior payer

The actual registry contract for `lem-hx-forced-exterior-coupling` concerns a
pair of row indices (r,s), not arbitrary row-polytope points, and states
\[
 P_r^+(E_c)+P_s^+(E_c)
 \ge \frac{\|p_r-p_s\|_1}{2(2+4\delta)}-2\delta
\]
for the strict set (E_c=\{Q:\|p_Q-c\|_1>1/2\}). R3 uses precisely this
version: for each charged full fiber (Q), it chooses an actual representative
(s\in Q). Equal source rows make (P_s^+(E_c)=P_Q^+(E_c)), so no synthetic
row-point invocation occurs.

Writing (V=P_v^+(E_c)) and
(T=\sum_Qm_QP_Q^+(E_c)), the separation hypothesis, including equality at
(4\tau), gives
\[
 V+P_Q^+(E_c)\ge
 \frac{4\tau}{2(2+4\delta)}-2\delta
 =\frac{\tau}{1+2\delta}-2\delta.
\]
Multiplication by (m_Q\ge0), summation, and R2 with the actual indicator of
the same strict full-fiber set give
\[
 SV+T\ge S\left(\frac{\tau}{1+2\delta}-2\delta\right),
 \qquad
 T\le V+2\delta(1+\delta),
\]
hence exactly
\[
 (1+S)V\ge
 S\left(\frac{\tau}{1+2\delta}-2\delta\right)
 -2\delta(1+\delta).
\]

The ceiling arithmetic also checks exactly. To obtain (V\ge\tau S/8), it
suffices after division by (S\tau>0) that
\[
 \frac1{1+2\delta}-2\tau-
 \frac{2\tau(1+\delta)}S\ge\frac{1+S}{8}.
\]
For
\[
 \delta\le\delta_E=
 \min\left\{\frac1{16},\left(\frac{c_m}{8}\right)^2\right\},
 \qquad c_m\le S\le1+\delta,
\]
the left side is at least
\[
 \frac89-\frac14-\frac{17}{64}=\frac{215}{576},
\]
whereas the right side is at most (33/128), and
(215/576>33/128). Thus the claimed explicit ceiling is valid, including its
equality boundary. The order (c_m) first, then (\delta_E), is essential.

The underlying financing-floor correction is respected. R3 invokes the banked
forced-coupling lemma rather than `lem-hx-financing-floor` directly; in the
derivation of that banked instance the pair separation
(\ell\ge4\tau>0) makes both
(A=1/(2\ell)>0) and (\Lambda=(2+4\delta)/\ell>0). Thus the corrected
(A>0) contract is not crossed. The coupling floor is nonpositive exactly
when
(\ell\le8\delta+16\delta^2). At (\ell=4\tau) and
(\delta\le1/16),
\[
 4\tau-(8\delta+16\delta^2)
 =4\tau(1-2\tau-4\tau^3)>0,
\]
so the use is informative even on the separation boundary. Fibers at distance
exactly (1/2) from (c) remain excluded throughout. Since the proof is rerun
after an arbitrary (c\in K(P)) is fixed and no estimate depends on (c), the
final universal quantifier is valid; no floors for different centers are
summed.

An exact rank-two boundary fixture stresses both conventions. Take
(\tau=1/64), (\delta=1/4096), (c_m=1/8), and
\[
 P=\begin{pmatrix}
 1&0&0&0\\
 0&1&0&0\\
 31/32&1/32&0&0\\
 1+\delta&-\delta&0&0
 \end{pmatrix}.
\]
Then (P^2=P), (P\mathbf1=\mathbf1), (\operatorname{rank}P=2),
(\delta(P)=\delta=(c_m/8)^2). For (v=3) (the third displayed row), select
only the first row-point fiber with mass (S=31/32). Its distance from (p_v)
is exactly (4\tau). At the row-hull center with line coordinate (1/4), that
fiber lies at distance exactly (1/2) and is therefore excluded from (E_c),
but the other endpoint contributes (V=1/32). No center can exclude both
endpoints, so (V\ge1/32>31/16384=\tau S/8). No violation was found in this or
the other exact rational rank-at-most-three fixtures.

The weighted clone isometry preserves strict distances, (E_c), (S,V,T),
and every full-fiber positive mass. Therefore the entire R3 display is clone
invariant.

## NOTES

The weakest accepted step is R3's allocation from the two-payer coupling
package to the single (v)-row payer, namely the combination of the summed
pairwise floor with R2. R2.4 is sign-dense, but its six terms check directly;
the R3 allocation is more fragile because changing the strict exterior set,
the row-index scope of the engine lemma, or either leak constant would break
the conclusion.

No batch statement is judged true but under-proved. There is, however, a
codification hygiene gap outside the mathematical contracts: “compatible
clone split” should be defined explicitly by the weighted lift
(P'_{ab}=P_{\pi(a),\pi(b)}w_b), with positive fiber weights summing to one,
before clone invariance is added as registry metadata.

The codifier must also retain these honest-scope caveats:

- R0 permits a partially selected clone fiber and defines its weight before
  fiber aggregation; it does not require (A) to be fiber-saturated.
- R1's (\Lambda=0) point has no (c), and no favorable minimizer or tie rule
  is supplied.
- R2 is an aggregate full-fiber inequality with the positive part taken before
  receiver-fiber aggregation. It is not a pointwise path-product estimate and
  gives no probabilistic interpretation to signed coefficients.
- R3's ceiling depends on the previously fixed (c_m). Its conclusion is
  pointwise-uniform in the sense “for every center separately”; it neither
  identifies one common exterior fiber nor licenses summing demands over
  centers. The far boundary is (\ge4\tau), while the exterior boundary is
  strictly (>1/2).

No raw-index floor, class count, selector, Jensen step, or probabilistic reading
of a signed row is used in any of the four accepted proofs.
