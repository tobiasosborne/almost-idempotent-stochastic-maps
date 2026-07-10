# W62 prover — L5 routine batch R0–R3

All matrices below are finite exact signed idempotents: \(P^2=P\) and
\(P\mathbf 1=\mathbf 1\). For a scalar \(x\), write
\(x^+=\max\{x,0\}\) and \(x^-=\max\{-x,0\}\), so \(x=x^+-x^-\).
Full equal-row fibers are denoted by \(Q,R\). All input and output measures
are full-fiber aggregates.

## §R0 — conj-w62-mass-barycenter-dualization

### CONTRACT

> For every L5 datum \((P,v,A)\) with \(S>0\), the quotient barycenter \(q\)
> above satisfies
> \[
>   \sup_{y\in Y_v}\sum_{j\in A}(P_{vj})_+z_y(j)=S Z_v(q).
> \]

Here
\[
 m_Q=\sum_{j\in A\cap Q}(P_{vj})^+,\qquad
 S=\sum_Qm_Q,\qquad \mu_Q=m_Q/S,\qquad
 q=\sum_Q\mu_Qp_Q,
\]
and \(z_y(j)=y\cdot(p_v-p_j)\),
\(Z_v(q)=\sup_{y\in Y_v}y\cdot(p_v-q)\).

### PROOF

By lem-top-support-dual-face, \(Y_v\) is nonempty and is the same top dual
face in both suprema. Since \(p_j=p_Q\) for \(j\in Q\), for each fixed
\(y\in Y_v\),
\[
\begin{aligned}
 \sum_{j\in A}(P_{vj})^+z_y(j)
 &=\sum_Q\sum_{j\in A\cap Q}(P_{vj})^+
          y\cdot(p_v-p_Q)\\
 &=\sum_Qm_Q\,y\cdot(p_v-p_Q)\\
 &=S\sum_Q\mu_Q\,y\cdot(p_v-p_Q).
\end{aligned}
\]
Apply lem-affine-barycenter-identity to the probability measure \(\mu\) and
the affine function \(a_y(x)=y\cdot(p_v-x)\). Its barycenter is \(q\), so
\[
 \sum_Q\mu_Q\,y\cdot(p_v-p_Q)=y\cdot(p_v-q).
\]
Consequently, pointwise on the single common set \(Y_v\),
\[
 \sum_{j\in A}(P_{vj})^+z_y(j)=S\,y\cdot(p_v-q).
\]
Because \(S>0\), taking the supremum over \(Y_v\) gives
\[
 \sup_{y\in Y_v}\sum_{j\in A}(P_{vj})^+z_y(j)
 =S\sup_{y\in Y_v}y\cdot(p_v-q)=S Z_v(q).
\]
No sign is discarded and no pointwise optimizing direction is selected.

The L5 definition assumes \(\delta>0\). There is no omitted tall endpoint:
lem-delta-zero-endpoint gives \(H=0\) at \(\delta=0\), which is incompatible
with \(H>16\sqrt\delta=0\).

### FIXTURES

**Partially selected clone fiber.** Let a fiber \(Q\), with row point \(p_Q\),
carry positive \(v\)-row mass \(\alpha\). Split that atom compatibly into two
clone indices of mass \(\alpha/2\) each and put exactly one in \(A\). Thus
\(m_Q=\alpha/2\). If the other selected fibers have total mass \(T\),
row-point moment \(b\), and fixed-\(y\) deficit sum \(L_y\), then both before
the split (viewing the intended half atom as a quotient submeasure) and after
the split,
\[
 S=T+\alpha/2,\qquad
 q=\frac{b+(\alpha/2)p_Q}{T+\alpha/2},
\]
and
\[
 \sum_{j\in A}(P_{vj})^+z_y(j)
 =L_y+(\alpha/2)y\cdot(p_v-p_Q).
\]
Thus \(S\), \(q\), the fixed-\(y\) objective, its supremum, and \(S Z_v(q)\)
are unchanged. Splitting the selected half again into two selected clones of
mass \(\alpha/4\) gives the same literal set-based check. Only \(m_Q\), not
the clone count, enters.

### CONTRACT DELTA

None.

### TOOLS

- lem-top-support-dual-face: nonemptiness and the common face \(Y_v\).
- lem-affine-barycenter-identity: exact affine integration at \(q\).
- lem-delta-zero-endpoint: endpoint check only.

## §R1 — conj-w62-top-face-primal-ray-formula

### CONTRACT

> For every exact signed idempotent \(P\) with \(\delta(P)>0\), nonempty
> visible set, and hidden top vertex \(v\) of height \(H\), and every
> \(q\in K(P)\),
> \[
>  Z_v(q)=\min_{\Lambda\ge0,\ c\in C_W}
>  \left\{\|p_v-q+\Lambda(p_v-c)\|_1-\Lambda H\right\},
> \]
> where \(c\) is omitted when \(\Lambda=0\).

### PROOF

Put \(d=p_v-q\). By lem-top-support-dual-face,
\[
 Y_v=\{y:\|y\|_\infty\le1,\ y\cdot p_v-h_{C_W}(y)=H\}.
\]
Equivalently,
\[
 Y_v=\{y:\|y\|_\infty\le1,\ 
             y\cdot(p_v-p_w)\ge H\text{ for every visible row point }p_w\}.
 \tag{R1.1}
\]
The forward implication follows from the definition of \(h_{C_W}\).
Conversely, the inequalities give
\(y\cdot p_v-h_{C_W}(y)\ge H\). For every
\(\|y\|_\infty\le1\), however,
\[
 y\cdot p_v-h_{C_W}(y)
 =\min_{c\in C_W}y\cdot(p_v-c)
 \le\min_{c\in C_W}\|p_v-c\|_1=H.
\]
Thus equality holds, proving (R1.1).

Using the finite set of distinct visible row points, \(Z_v(q)\) is the
finite linear program
\[
 \max\{d\cdot y:-1\le y_i\le1,\ 
       (p_v-p_w)\cdot y\ge H\text{ for every }w\}.       \tag{R1.2}
\]
It is feasible by lem-top-support-dual-face and bounded by the
\(\ell^\infty\) box.

Give the visible constraint indexed by \(w\) a multiplier
\(\lambda_w\ge0\). For feasible \(y\),
\[
 d\cdot y\le d\cdot y+
 \sum_w\lambda_w\bigl((p_v-p_w)\cdot y-H\bigr).
\]
The supremum of the right side over \(\|y\|_\infty\le1\) is, by
\(\ell^1\)-\(\ell^\infty\) duality,
\[
 \left\|d+\sum_w\lambda_w(p_v-p_w)\right\|_1
 -H\sum_w\lambda_w.                                    \tag{R1.3}
\]
Finite LP strong duality gives equality between (R1.2) and the minimum of
(R1.3) over \(\lambda_w\ge0\). It also gives an attained dual optimum:
the primal is feasible with finite optimum, and the dual is feasible at
\(\lambda=0\).

Set \(\Lambda=\sum_w\lambda_w\). If \(\Lambda>0\), put
\[
 c=\Lambda^{-1}\sum_w\lambda_wp_w\in C_W.
\]
Then
\[
 \sum_w\lambda_w(p_v-p_w)=\Lambda(p_v-c),
\]
so (R1.3) becomes
\[
 \|p_v-q+\Lambda(p_v-c)\|_1-\Lambda H.                 \tag{R1.4}
\]
Conversely, every \(\Lambda>0\) and \(c\in C_W\) have a finite convex
representation by visible row points, which recovers nonnegative
multipliers of total mass \(\Lambda\). Hence the aggregation loses no value.

If \(\Lambda=0\), nonnegativity forces all \(\lambda_w=0\), and (R1.3) is
\(\|p_v-q\|_1\); \(c\) is neither defined nor needed. An attained optimal
multiplier family maps either to this zero-multiplier point or to an attained
pair \((\Lambda,c)\) with \(\Lambda>0\). This proves the formula and
attainment, including the \(\Lambda=0\) edge.

### FIXTURES

**One dimension: \(C_W=\{0\}\), \(p_v=1\).** Here \(H=1\),
\(Y_v=\{1\}\), and for \(0\le q\le1\),
\[
 Z_v(q)=1-q.
\]
The ray formula gives
\[
 \min_{\Lambda\ge0}\{|1-q+\Lambda|-\Lambda\}=1-q,
\]
since \(1-q+\Lambda\ge0\). The value is attained at \(\Lambda=0\)
(indeed at every \(\Lambda\ge0\)), and the center is correctly absent at
\(\Lambda=0\).

**Two-point visible hull.** In the two-dimensional LP model take
\[
 C_W=\operatorname{conv}\{(0,0),(1,0)\},\qquad
 p_v=(0,1),\qquad H=1,\qquad q=(-1/2,0),
\]
with \(q\) included in the ambient row hull. Then
\[
 Y_v=\{(t,1):-1\le t\le0\},\qquad
 Z_v(q)=\max_{-1\le t\le0}(t/2+1)=1.
\]
Writing \(c=(s,0)\), \(0\le s\le1\), the ray side is
\[
\begin{aligned}
 \|(1/2,1)+\Lambda(-s,1)\|_1-\Lambda
 &=|1/2-\Lambda s|+|1+\Lambda|-\Lambda\\
 &=|1/2-\Lambda s|+1\ge1.
\end{aligned}
\]
Equality is attained at \(s=1,\Lambda=1/2\). At \(\Lambda=0\) the value is
\(3/2\), so this checks a genuinely nonzero multiplier and the sign
\(+\Lambda(p_v-c)\).

### CONTRACT DELTA

None.

### TOOLS

- lem-top-support-dual-face: exact description and nonemptiness of \(Y_v\).
- Finite LP strong duality and elementary \(\ell^1\)-\(\ell^\infty\) duality.

## §R2 — conj-w62-positive-flow-foldback

### CONTRACT

> For every finite exact signed idempotent \(P\), row \(v\), nonnegative
> full-fiber submeasure \(m_Q\le\sum_{j\in Q}(P_{vj})_+\), and function
> \(g:\mathcal Q(P)\to[0,M]\),
> \[
>  \sum_Qm_Q\sum_R\sum_{k\in R}(P_{Qk})_+g_R
>  \le
>  \sum_R\sum_{k\in R}(P_{vk})_+g_R+2\delta(1+\delta)M.
> \]

Here \(\delta=\delta(P)\), and \(P_{Qk}\) is the common value \(P_{ik}\)
for \(i\in Q\).

### PROOF

Write
\[
 a_i=P_{vi},\qquad a_i=a_i^+-a_i^-.
\]
Disintegrate the quotient submeasure canonically. For a fiber \(Q\), put
\(A_Q=\sum_{i\in Q}a_i^+\), and for \(i\in Q\) define
\[
 b_i=
 \begin{cases}
 (m_Q/A_Q)a_i^+,&A_Q>0,\\
 0,&A_Q=0.
 \end{cases}
\]
Then \(0\le b_i\le a_i^+\), \(\sum_{i\in Q}b_i=m_Q\), and this proportional
construction is invariant under a compatible clone split. Put
\(r_i=a_i^+-b_i\ge0\). Thus
\[
 a_i=b_i+r_i-a_i^-.                                    \tag{R2.1}
\]

Lift \(g\) to indices by \(\widetilde g_k=g_R\) for \(k\in R\). Then
\(0\le\widetilde g_k\le M\). Equal source rows within each fiber give
\[
 T:=\sum_Qm_Q\sum_R\sum_{k\in R}(P_{Qk})^+g_R
   =\sum_i b_i\sum_kP_{ik}^+\widetilde g_k.             \tag{R2.2}
\]
This is an aggregate identity, not a pathwise lower bound.

Exact idempotence gives, for every receiver \(k\),
\[
 a_k=P_{vk}=\sum_iP_{vi}P_{ik}=\sum_i a_iP_{ik}.        \tag{R2.3}
\]
Insert (R2.1) and \(P_{ik}=P_{ik}^+-P_{ik}^-\) into (R2.3), and solve for
the selected positive-source/positive-receiver term:
\[
\begin{aligned}
 \sum_i b_iP_{ik}^+
 ={}&a_k-\sum_i r_iP_{ik}^+-\sum_i a_i^-P_{ik}^-\\
   &+\sum_i b_iP_{ik}^-+\sum_i r_iP_{ik}^-
      +\sum_i a_i^-P_{ik}^+.                           \tag{R2.4}
\end{aligned}
\]
The two explicitly negative terms name the favorable sign contributions:
positive remainder through positive coefficients, and negative source
through negative coefficients. Since \(\widetilde g_k\ge0\), discard them
in an upper bound. Also
\(a_k\widetilde g_k\le a_k^+\widetilde g_k\). Multiply (R2.4) by
\(\widetilde g_k\), sum over \(k\), and use \(b_i+r_i=a_i^+\):
\[
\begin{aligned}
 T\le{}&\sum_k a_k^+\widetilde g_k\\
 &+\underbrace{\sum_i a_i^+\sum_kP_{ik}^-\widetilde g_k}_{
       \text{positive-source/negative-receiver leak}}\\
 &+\underbrace{\sum_i a_i^-\sum_kP_{ik}^+\widetilde g_k}_{
       \text{negative-source/positive-receiver leak}}. \tag{R2.5}
\end{aligned}
\]

Every row has negative mass at most \(\delta\). By lem-mass-split, every
row has positive mass at most \(1+\delta\), and for row \(v\),
\[
 \sum_i a_i^+\le1+\delta,\qquad \sum_i a_i^-\le\delta.
\]
The two named leaks in (R2.5) therefore satisfy, separately,
\[
 \sum_i a_i^+\sum_kP_{ik}^-\widetilde g_k
 \le M(1+\delta)\delta,                                \tag{R2.6}
\]
and
\[
 \sum_i a_i^-\sum_kP_{ik}^+\widetilde g_k
 \le M\delta(1+\delta).                                \tag{R2.7}
\]
Substitute (R2.6)–(R2.7) into (R2.5) and regroup receivers by full fibers.
This gives exactly
\[
 \sum_Qm_Q\sum_R\sum_{k\in R}(P_{Qk})^+g_R
 \le\sum_R\sum_{k\in R}(P_{vk})^+g_R
       +2\delta(1+\delta)M.
\]
Raw indices occur only inside the exact matrix identity; all input and
output quantities are clone-invariant full-fiber aggregates.

### FIXTURES

**Indicator.** For a full-fiber set \(F\), take \(g=1_F\), \(M=1\). Then
\[
 \sum_Qm_QP_Q^+(F)
 \le P_v^+(F)+2\delta(1+\delta).                        \tag{R2.8}
\]
The boundary convention defining \(F\) is irrelevant to R2, provided \(F\)
is a union of full fibers.

**Top deficit.** In the top-face setting, take
\(g_R=z_y(R)=y\cdot(p_v-p_R)\) for fixed \(y\in Y_v\).
Lemma lem-top-deficit-price gives \(z_y(R)\ge0\), and the row-diameter bound
with \(\|y\|_\infty\le1\) gives
\[
 0\le z_y(R)\le\|p_v-p_R\|_1\le D_0:=2+4\delta.
\]
R2 therefore yields
\[
 \sum_Qm_Q\sum_RP_Q^+(\{R\})z_y(R)
 \le\sum_RP_v^+(\{R\})z_y(R)
      +2\delta(1+\delta)D_0.
\]
The first term on the right is at most \(\delta D_0\) by
lem-top-deficit-price.

**Endpoint \(\delta=0\).** All coefficients are then nonnegative, so both
leaks (R2.6)–(R2.7) vanish. For arbitrary \(m\), R2 is the exact subflow
domination
\[
 \sum_Qm_Q\sum_RP_Q(R)g_R\le\sum_RP_v(R)g_R.
\]
For the full measure \(m_Q=P_v(Q)\), \(r=0\), and \(P_vP=P_v\) turns this
into equality:
\[
 \sum_QP_v(Q)\sum_RP_Q(R)g_R=\sum_RP_v(R)g_R.
\]
Thus the endpoint reduces to exact stochastic one-step flow conservation.

### CONTRACT DELTA

None.

### TOOLS

- lem-mass-split: positive mass equals one plus negative mass.
- lem-top-deficit-price: only in the \(g=z_y\) fixture.

## §R3 — conj-w62-universal-exterior-payer

### CONTRACT

> There is \(\delta_E>0\) such that for every finite exact signed idempotent
> \(P\) with \(0<\delta(P)=\delta\le\delta_E\), every row \(v\) of \(P\),
> and every nonnegative full-fiber submeasure \(m\le P_v^+\) of mass
> \(S\ge c_m\) supported on
> \(\{Q:\|p_Q-p_v\|_1\ge4\tau\}\), one has
> \[
>   \forall c\in K(P),\qquad P_v^+(E_c)\ge\frac18\,\tau S.
> \]

Here \(c_m\in(0,1)\) is fixed first, \(\tau=\sqrt\delta\), and
\[
 E_c=\{R:\|p_R-c\|_1>1/2\}.
\]
We prove the contract with the explicit ceiling
\[
 \boxed{\displaystyle
 \delta_E=\min\left\{\frac1{16},\left(\frac{c_m}{8}\right)^2\right\}.}
 \tag{R3.1}
\]

### PROOF

Fix the data and then fix an arbitrary \(c\in K(P)\). Put
\[
 V=P_v^+(E_c),\qquad T=\sum_Qm_QP_Q^+(E_c).             \tag{R3.2}
\]
The set \(E_c\) is a full-fiber set because it is defined by row points.

For every charged fiber \(Q\), lem-hx-forced-exterior-coupling descends
directly to the quotient. Applying it to any \(s\in Q\) gives the same row
point \(p_s=p_Q\) and the same positive fiber totals \(P_s^+=P_Q^+\). No
representative is retained, and
\[
 V+P_Q^+(E_c)
 \ge\frac{\|p_v-p_Q\|_1}{2(2+4\delta)}-2\delta.         \tag{R3.3}
\]
On the support of \(m\), \(\|p_v-p_Q\|_1\ge4\tau\). Thus, including equality
at the far-set boundary,
\[
 V+P_Q^+(E_c)
 \ge\frac{4\tau}{4+8\delta}-2\delta
 =\frac{\tau}{1+2\delta}-2\delta.                      \tag{R3.4}
\]
Multiply by \(m_Q\ge0\) and sum over \(Q\):
\[
 SV+T\ge
 S\left(\frac{\tau}{1+2\delta}-2\delta\right).          \tag{R3.5}
\]

Apply R2, proved above, to this same submeasure and the actual indicator
\(g=1_{E_c}\):
\[
 T\le V+2\delta(1+\delta).                             \tag{R3.6}
\]
Combining (R3.5) and (R3.6) first gives the requested exact intermediate
inequality
\[
 \boxed{(1+S)V\ge
 S\left(\frac{\tau}{1+2\delta}-2\delta\right)
 -2\delta(1+\delta).}                                  \tag{R3.7}
\]

It remains to derive the clean constant. Since \(m\le P_v^+\),
lem-mass-split gives
\[
 c_m\le S\le1+\delta.                                  \tag{R3.8}
\]
For (R3.7) to imply \(V\ge\tau S/8\), it suffices, after dividing by
\(S\tau>0\), that
\[
 \frac1{1+2\delta}-2\tau
 -\frac{2\tau(1+\delta)}S
 \ge\frac{1+S}{8}.                                     \tag{R3.9}
\]
Under (R3.1), \(\delta\le1/16\) and \(\tau\le c_m/8\). Using (R3.8),
\[
 \frac1{1+2\delta}\ge\frac89,\qquad
 2\tau\le\frac14,\qquad
 \frac{2\tau(1+\delta)}S
 \le\frac{2(c_m/8)(17/16)}{c_m}=\frac{17}{64},          \tag{R3.10}
\]
whereas
\[
 \frac{1+S}{8}\le\frac{2+\delta}{8}\le\frac{33}{128}.   \tag{R3.11}
\]
The left side of (R3.9) is at least
\[
 \frac89-\frac14-\frac{17}{64}
 =\frac{215}{576}>\frac{33}{128};                      \tag{R3.12}
\]
indeed \(215\cdot128=27520>19008=33\cdot576\).
Hence (R3.9) holds. Multiplying it by \(S\tau\) and using (R3.7),
\[
 (1+S)V\ge\frac18S\tau(1+S),
\]
so \(V\ge\tau S/8\).

The center \(c\) was arbitrary, and the ceiling and estimates are independent
of it. The conclusion therefore holds for every \(c\in K(P)\). The suggested
ceiling \(\min\{1/16,(c_m/32)^2\}\) is valid, but (R3.1) is a strictly larger
sufficient ceiling obtained from the displayed estimates.

### FIXTURES

**Far-set boundary and T0 vacuity threshold.** At
\(\|p_Q-p_v\|_1=4\tau\), T0 gives exactly the right side of (R3.4). Its
contract says this floor is nonpositive precisely when
\[
 \|p_Q-p_v\|_1\le8\delta+16\delta^2.
\]
For \(\delta\le1/16\), hence \(\tau\le1/4\),
\[
\begin{aligned}
 4\tau-(8\delta+16\delta^2)
 &=4\tau(1-2\tau-4\tau^3)\\
 &\ge4\tau\left(1-\frac12-\frac1{16}\right)
 =\frac74\tau>0.
\end{aligned}
\]
Thus T0 is informative even at separation exactly \(4\tau\). At
\(\delta=1/16\), its floor is
\[
 \frac{\tau}{1+2\delta}-2\delta
 =\frac{1/4}{9/8}-\frac18=\frac7{72}>0.
\]
The set \(E_c\) remains strict: fibers at distance exactly \(1/2\) are not
counted.

**W61 dyadic leak-financer calibration.** The W61 sketch records a financer
that pays a *local* exterior demand. Equations (R3.3)–(R3.7) show exactly
what R3 blocks: for one fixed center \(c\), actor rows charged by \(m\)
cannot all reuse their own positive exterior leaks without the aggregate
being folded back to row \(v\). The resulting \(v\)-row floor is uniform
because the argument can be rerun for each \(c\).

This does **not** sum floors over different centers and therefore does not,
by itself, exclude the dyadic leak-financer shape. A common \(v\)-row leak
may pay the inequalities for many centers, and a spread-out web may pay each
center with different mass. The for-all-centers conclusion forces the
financer to pass every local half-ball test, but it does not turn those
local demands into disjoint demands. R3 defeats repeated pairwise charging
at a fixed center; exclusion of a globally recycling financer remains a
downstream geometric task.

### CONTRACT DELTA

None. The pinned existential ceiling is proved with the explicit, stronger
choice (R3.1); this changes no hypothesis or conclusion.

### TOOLS

- lem-hx-forced-exterior-coupling: the strict-half-ball two-row floor and
  its exact vacuity threshold.
- §R2 above: foldback of the charged actor flow for \(g=1_{E_c}\).
- lem-mass-split: \(S\le P_v^+(\mathcal Q(P))\le1+\delta\).
