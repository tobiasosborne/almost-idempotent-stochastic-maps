# Bounded-slab starvation completion obstruction

**Outcome.**  The candidate lemma is proved below in a stronger form: at the
universal ceiling \(0<\tau\le 1/256\), no bound at all is needed on the
number of exterior zero-top support fibers (the matrix is still finite).

## §STATEMENT

### Contract notation

Let \(I\) be a finite index set and let \(P=(P_{ij})_{i,j\in I}\) be a real
matrix with rows \(p_i\in\mathbb R^I\).  A *rank-three exact signed
idempotent* means

\[
 P^2=P,\qquad P\mathbf 1=\mathbf 1,\qquad \operatorname {rank}P=3.
\]

Its row-\(i\) negative mass is

\[
 \nu_i:=\sum_{j\in I}(-P_{ij})_+,
 \qquad r_+:=\max\{r,0\}.
\]

The **full row-point fibers** are the equivalence classes for
\(i\sim j\iff p_i=p_j\).  For a fiber \(Q\subseteq I\), write
\(p_Q\) for its common row point and, after fixing rows \(v,z,o\), put

\[
 c_Q:=\sum_{j\in Q}P_{vj},\qquad
 d_Q:=\sum_{j\in Q}(P_{zj}-P_{vj}),\qquad
 e_Q:=\sum_{j\in Q}(P_{oj}-P_{vj}).                 \tag{1}
\]

If \(u\) represents the fiber \([u]\), we abbreviate
\(c_u:=c_{[u]}\), \(d_u:=d_{[u]}\), and \(e_u:=e_{[u]}\).

The fiber is a *support fiber* if \((c_Q,d_Q,e_Q)\ne(0,0,0)\), and it is
*zero-top* if \(c_Q=0\).  These are full-fiber notions: clone indices are
coalesced before either condition is read; *nonactor* means a fiber other
than \([v],[w],[f],[z],[o]\).

**Lemma (one-sentence registry contract).**  For every finite \(I\), every real \(A\in[4,6]\), every real \(\tau\in(0,1/256]\), and \(t:=\tau^2\), \(a:=\tau/(1+\tau)\), there is no rank-three exact signed idempotent \(P\) with \(\nu_i\le t\) for every \(i\in I\) having five distinct full row-point fibers represented by \(v,w,f,z,o\) such that, with \(D:=p_z-p_v\) and \(E:=p_o-p_v\), the vectors \(D,E\) are linearly independent, \(\lVert D\rVert_1=\tau\), \(p_f-p_v=-AD+tE\), \(p_w-p_v=a(p_f-p_v)\), the top-row fiber masses are \(c_v=1-\tau\), \(c_w=\tau+t\), \(c_f=-t\), and \(c_Q=0\) for every other full row-point fiber \(Q\), for every full row-point fiber \(Q\) there are unique real \(x_Q,y_Q\) with \(p_Q=p_v+x_QD+y_QE\), and every nonactor support fiber \(Q\) satisfies either \(p_Q\in\mathcal H:=\operatorname {conv}\{p_v,p_w,p_f,p_z,p_o\}\) or \(0\le y_Q\le1\).

The affine coordinate \(h(p_v+xD+yE):=y\) is the canonical affine
\(y\)-coordinate (the exposer coordinate on support fibers), and an
*exterior support fiber* means a support fiber \(Q\) with
\(p_Q\notin\mathcal H\); no exposer admissibility is asserted for a
nonsupport fiber.  Thus the last clause says exactly that every exterior
support fiber is in the closed canonical slab.  The lemma allows
arbitrarily many such exterior fibers; since \(I\) is finite, their number
is finite.  Its conclusion therefore implies the stated
\(K\)-parametric candidate, because
\(\min\{1/256,1/(12(K+1))\}\le1/256\) for every \(K\ge1\).

## §PROOF

Assume, for contradiction, that the data in the lemma exist.  Throughout the
proof \(t=\tau^2\), and for a row \(i\) and a coordinate subset \(S\subseteq I\)
we abbreviate \(P_i(S):=\sum_{j\in S}P_{ij}\).

### Claim 1: signed-row subset ledger

For every row \(i\) and every \(S\subseteq I\),

\[
 -t\le P_i(S)\le1+t,
 \qquad
 \lVert p_i\rVert_1\le1+2t.                            \tag{2}
\]

Indeed, write \(P_{ij}=P_{ij}^+-P_{ij}^-\), where
\(P_{ij}^+=(P_{ij})_+\) and \(P_{ij}^-=(-P_{ij})_+\).
Because the row sum is one and \(\sum_jP_{ij}^-=\nu_i\),

\[
 \sum_jP_{ij}^+=1+\nu_i.
\]

Consequently

\[
 -\nu_i\le -\sum_{j\in S}P_{ij}^-
 \le P_i(S)
 \le\sum_{j\in S}P_{ij}^+
 \le1+\nu_i.
\]

Since \(\nu_i\le t\), this proves the subset bounds, and

\[
 \lVert p_i\rVert_1
 =\sum_jP_{ij}^++\sum_jP_{ij}^-
 =1+2\nu_i\le1+2t,
\]

which proves (2).

The canonical-coordinate clause adds no hypothesis beyond rank three and
the stated transversality.  Indeed, \(p_v\) has coordinate sum one whereas
\(D\) and \(E\) have coordinate sum zero, so the independence of \(D,E\)
implies that \(p_v,D,E\) are linearly independent.  They are therefore a
basis of the three-dimensional row space of \(P\).  Every row \(p_Q\) has
coordinate sum one, forcing its coefficient of \(p_v\) in this basis to be
one; hence the real numbers \(x_Q,y_Q\) exist and are unique.

### Claim 2: the unit transverse reproduction moment

The full-fiber coefficients in (1) satisfy

\[
 \boxed{\displaystyle \sum_Q x_Qd_Q=1},                \tag{3}
\]

where the sum is over all full row-point fibers.

To prove this directly from idempotence, subtract the \(v\)-row of
\(P^2=P\) from the \(z\)-row.  With \(D=p_z-p_v\), this gives

\[
 DP=D.                                                   \tag{4}
\]

Also \(\sum_jD_j=0\), because both \(p_z\) and \(p_v\) have row sum one.
Abbreviate \(x_j:=x_{[j]}\) and \(y_j:=y_{[j]}\) (the canonical coordinates of the
fiber \([j]\), constant on clone fibers per the conventions of the STATEMENT).
Using the canonical expansion \(p_j=p_v+x_jD+y_jE\) in (4),

\[
\begin{aligned}
 D
   =DP
   &=\sum_{j\in I}D_jp_j\\
   &=\left(\sum_jD_j\right)p_v
     +\left(\sum_jx_jD_j\right)D
     +\left(\sum_jy_jD_j\right)E\\
   &=\left(\sum_jx_jD_j\right)D
     +\left(\sum_jy_jD_j\right)E .                     \tag{5}
\end{aligned}
\]

The vectors \(D,E\) are linearly independent, so comparison of their
coefficients gives \(\sum_jx_jD_j=1\).  The coordinate \(x_j\) is constant
on a row-point fiber \(Q\), and
\(\sum_{j\in Q}D_j=d_Q\) by (1); grouping the finite sum by fibers proves
(3).  Notice that (3) is an idempotence identity, not an interpretation of
any auxiliary multiplier as transition mass.

The actor relations give their canonical coordinates explicitly:

\[
 (x_v,y_v)=(0,0),\quad (x_z,y_z)=(1,0),\quad
 (x_o,y_o)=(0,1),\quad (x_f,y_f)=(-A,t),\quad
 (x_w,y_w)=(-Aa,ta).                                    \tag{6}
\]

Because \(0<a<1\) and \(A\ge4\), every point of the actor hull
\(\mathcal H\) has

\[
 -A\le x\le1,\qquad |x|\le A.                          \tag{7}
\]

### Claim 3: the canonical slab bounds every exterior lever arm

Let \(Q\) be any exterior support fiber and write
\((X_Q,Y_Q):=(x_Q,y_Q)\).  Then

\[
 |X_Q|\tau\le2+4t.                                      \tag{8}
\]

Indeed, \(0\le Y_Q\le1\) by the slab hypothesis, and
\(p_o=p_v+E\), so

\[
 X_QD=p_Q-(1-Y_Q)p_v-Y_Qp_o.                            \tag{9}
\]

Taking \(\ell_1\)-norms, using Claim 1 on the three rows involved and
using \(\lVert D\rVert_1=\tau\), we obtain

\[
\begin{aligned}
 |X_Q|\tau
 &\le \lVert p_Q\rVert_1
       +(1-Y_Q)\lVert p_v\rVert_1+Y_Q\lVert p_o\rVert_1\\
 &\le (1+2t)+(1-Y_Q)(1+2t)+Y_Q(1+2t)\\
 &=2+4t,
\end{aligned}                                           \tag{10}
\]

as asserted.  This estimate is obtained in the original coordinates; no
fiber aggregation or column deletion has been used to replace the metric
equality.

### Claim 4: one global exterior coefficient budget

Let \(\mathscr E\) be the set of all exterior support fibers.  Although its
cardinality is unrestricted, its aggregate \(D\)-variation satisfies

\[
 \sum_{Q\in\mathscr E}|d_Q|
 \le t\left(1+\frac{2+t}{A}\right).                     \tag{11}
\]

For any fiber \(Q\), the definitions of \(c_Q,d_Q,e_Q\) and the actor
relations give

\[
 P_z(Q)=c_Q+d_Q,\qquad
 P_o(Q)=c_Q+e_Q,\qquad
 P_f(Q)=c_Q-Ad_Q+te_Q.                                  \tag{12}
\]

Every exterior fiber is a nonactor fiber and hence is zero-top, so \(c_Q=0\)
there.  Partition the exterior fibers according to the sign of their
*aggregate* coefficient:

\[
 \mathscr E_-:=\{Q\in\mathscr E:d_Q<0\},\qquad
 \mathscr E_+:=\{Q\in\mathscr E:d_Q\ge0\},
\]

and let \(S_-:=\bigcup_{Q\in\mathscr E_-}Q\) and
\(S_+:=\bigcup_{Q\in\mathscr E_+}Q\), which are genuine subsets of the
original coordinate set \(I\).  By (12) and the lower subset bound (2) for
row \(z\),

\[
 -\sum_{Q\in\mathscr E_-}|d_Q|
 =\sum_{Q\in\mathscr E_-}d_Q
 =P_z(S_-)\ge-t;
\]

hence

\[
 \sum_{Q\in\mathscr E_-}|d_Q|\le t.                    \tag{13}
\]

Put

\[
 D_+:=\sum_{Q\in\mathscr E_+}d_Q\ge0,
 \qquad E_+:=\sum_{Q\in\mathscr E_+}e_Q.
\]

Applying (12) to the union \(S_+\), and then applying the two sides of the
subset ledger (2) to rows \(f\) and \(o\), gives

\[
 -AD_++tE_+=P_f(S_+)\ge-t,
 \qquad E_+=P_o(S_+)\le1+t.                             \tag{14}
\]

It follows, without any sign assumption on \(E_+\), that

\[
 AD_+\le t(E_++1)\le t(2+t),
 \qquad
 \sum_{Q\in\mathscr E_+}|d_Q|=D_+
 \le\frac{t(2+t)}A.                                    \tag{15}
\]

Adding (13) and (15) proves (11).  The important point is that each row
budget is applied once to a union of full fibers, rather than once per
fiber.

Combining (8), (11), and \(t=\tau^2\) now bounds the *entire* exterior
contribution to the unit moment:

\[
\begin{aligned}
 \sum_{Q\in\mathscr E}|X_Qd_Q|
 &\le \frac{2+4t}{\tau}\sum_{Q\in\mathscr E}|d_Q|\\
 &\le \tau(2+4t)\left(1+\frac{2+t}{A}\right).           \tag{16}
\end{aligned}
\]

### Claim 5: the unit moment cannot be financed

Let \(\mathscr H\) be the set of support fibers contained in the actor hull.
All remaining nonsupport fibers have \(d_Q=0\), and the hypotheses partition
the support fibers into \(\mathscr H\) and \(\mathscr E\).  From (7),

\[
 \left|\sum_{Q\in\mathscr H}x_Qd_Q\right|
 \le A\sum_{Q\in\mathscr H}|d_Q|.                    \tag{17}
\]

Moreover, grouping coordinates can only decrease total variation:

\[
 \sum_{Q\in\mathscr H}|d_Q|
 \le\sum_Q\left|\sum_{j\in Q}D_j\right|
 \le\sum_{j\in I}|D_j|
 =\lVert D\rVert_1
 =\tau.                                                  \tag{18}
\]

Apply (16)--(18) to the unit moment (3).  The triangle inequality gives the
necessary inequality

\[
 1\le
 \tau\left[
 A+(2+4t)\left(1+\frac{2+t}{A}\right)
 \right].                                                \tag{19}
\]

The constants now close with ample room.  Since
\(0<\tau\le1/256\), we have \(t=\tau^2<1/4\) and \(t<1\), and hence

\[
 2+4t<3,
 \qquad
 \frac{2+t}{A}\le\frac{2+t}{4}<\frac34,
 \qquad A\le6.                                         \tag{20}
\]

Thus the right-hand side of (19) is strictly smaller than

\[
 \frac1{256}
 \left[6+3\left(1+\frac34\right)\right]
 =\frac{45}{1024}<1,                                    \tag{21}
\]

contradicting (19).  This proves the lemma.

### Dimension and clone audit

No estimate above contains \(|I|\) or the number of fibers.  Every sign
partition is made after passing to full equal-row fibers, but the sets
\(S_-\) and \(S_+\) to which Claim 1 is applied are unions of the original
coordinate indices.  Internal cancellation within a fiber therefore causes
no problem.  Under a clone split that replaces one coordinate by columns
whose entries sum to the original column and duplicates the corresponding
row point, the full-fiber quantities in (1), its canonical coordinates,
and the union identities (12)--(15) remain unchanged.  Independently, (18)
is written in the original coordinates and is valid for every
multiplicity.  The proof is therefore dimension-free and clone-invariant.

### Check of the decided W57/W58 families

The six W57/W58 support patterns have the following relevant defining
features; these are the only case facts consumed here:

- **literal_r3_actor5** and **hx_near_r3_actor5** have no added exterior
  fiber;
- **hx_far_r3_nonvertex6** adds only
  \(p_x=(p_v+p_f)/2\), which is in \(\mathcal H\);
- **xv_literal_r3_vertex6** and **xv_hx_near_r3_vertex6** add one zero-top
  exterior fiber \(q\) with \(0\le Y_q\le1\);
- **xv_hx_far_r3_vertex6_nonvertex7** adds that same kind of exterior fiber
  and the actor-hull midpoint \(p_m=(p_v+p_f)/2\).

At the raw decision locus all six use \(A=5\), \(\tau=1/256\), the actor
relations and full-fiber top pins in the contract, and
\(\lVert p_z-p_v\rVert_1=\tau\); their stated stability variants use
\(A\in[4,6]\) and \(0<\tau\le1/256\), which are covered as well.  Their
extra distance, freight, visible-set, exposer, and sign-cell constraints
only shrink the class just proved empty.  Hence the lemma excludes every
W57/W58-decided family, including the boundary cases \(Y_q=0\) and
\(Y_q=1\).

## §MECHANISM

The killing resource is the **single global transverse reproduction
moment** (3): idempotence forces one unit of \(D\)-moment, while the metric
pin lets every actor-hull fiber together contribute only \(A\tau\), and
the shared row-negativity budgets of rows \(z,f,o\), applied once to the
negative and positive exterior sign-unions, let *all* canonical-slab
exterior fibers together contribute only
\(\tau(2+4\tau^2)(1+(2+\tau^2)/A)\); to generalize this mechanism to
**conj-sl1a-off-diagonal-cell** or the L6.5 large-gauge wall one would have
to extract from the general configuration a transverse displacement \(D\),
a bounded slab making each carrier's \(D\)-lever at most \(O(1/\tau)\),
a constant number of genuine row-subset negativity ledgers that bound the
*aggregate* signed \(D\)-coefficient variation by \(O(\tau^2)\), and an
idempotence/left-inverse identity forcing an \(\Omega(1)\) transverse
moment; the coefficients here are only coefficients in exact identities
and inequalities, never transition masses or flows.

## §HONEST LIMITS

The proof gives more than the proposed fixed-\(K\) statement but only
within its stated rank-three slab geometry.

- **The \(K\)-ceiling is removed.**  Every finite number of exterior
  zero-top support fibers is covered at the universal ceiling
  \(\tau\le1/256\); the improvement comes exactly from applying the
  row budgets to the two sign-unions in Claim 4 instead of paying once per
  fiber.
- **The universal \(\tau\)-ceiling is retained and is not optimized.**
  The crude close (20)--(21) has much more room than needed, but no larger
  constant is claimed here.
- **Rank greater than three is not covered.**  An exterior row can then have
  further transverse components, so (9) acquires extra terms that may
  cancel \(X_QD\); neither the lever bound (8) nor this two-coordinate
  moment close follows.
- **Exterior support fibers outside the canonical slab are not covered.**
  The inequalities \(0\le Y_Q\le1\) are used in (10) to make the
  \(p_v,p_o\) combination convex; an uncontrolled \(Y_Q\) introduces an
  uncontrolled lever.
- **Fiberwise zero-top exterior support is essential to Claim 4.**  If an
  exterior support fiber has \(c_Q\ne0\), the three identities (12) acquire
  a top term and the sign-union budget (13)--(15) no longer follows.
- **No metric-free, tall-geometry, or general H-X/L6.5 theorem is claimed.**
  The exact pin \(\lVert p_z-p_v\rVert_1=\tau\) drives (8) and (18);
  the argument proves the completion obstruction for the stated tableau
  relaxation, not the upstream geometric reductions that would have to
  produce that tableau.
