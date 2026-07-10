# Exact infeasibility certificate

Status: **AUTHOR-CLAIM**.  The displayed rational identity is independently
checkable; its proposed dimension-free extension is only a candidate lemma.

## Certificate identity

Let (0<s\le1/256), (t=s^2), (a=s/(1+s)), and (4\le A\le6), all
rational.  Use the canonical (L) and pinned top row from `FORMULATION.md`.
Write the two unknown rows of (B) as (D,E), and abbreviate

\[
 X=D_w,\quad Y=D_f,\quad U=E_w,\quad V=E_f,
\]

\[
 C=1+a(A-t),\qquad d=A+1-t.
\]

The six equations (BL=I_3) solve exactly to

\[
\begin{aligned}
D_v&=-1-CX-dY,&D_z&=1+AaX+AY,&D_o&=-t(aX+Y),\\
E_v&=-1-CU-dV,&E_z&=AaU+AV,&E_o&=1-t(aU+V).
\end{aligned}                                             \tag{C1}
\]

Take the following five entries of the completed matrix:

\[
 e_0=P_{fv},\quad e_1=P_{fz},\quad e_2=P_{zf},\quad
 e_3=P_{ov},\quad e_4=P_{ow}.                              \tag{C2}
\]

Substitution of (C1) into (P=LB) gives

\[
\begin{aligned}
e_0={}&1-s+A-t+ACX+AdY-tCU-tdV,\\
e_1={}&-A-A^2aX-A^2Y+AtaU+AtV,\\
e_2={}&Y-t,\\
e_3={}&-s-CU-dV,\\
e_4={}&s+t+U.
\end{aligned}                                             \tag{C3}
\]

Put

\[
 G=1+(A+1)s-s^3
\]

and

\[
\begin{array}{ll}
N_0=As(s+1)(A+1-t),
&N_1=(s+1)(A+1-t)G,\\
N_2=A^2(s+1)(A+1-t),
&N_3=At(s+1),\\
N_4=AtG.&
\end{array}                                               \tag{C4}
\]

Every (N_i) is strictly positive.  Direct expansion, with every coefficient
of (X,Y,U,V) cancelling, yields the exact identity

\[
 \sum_{i=0}^4N_i e_i=-M,                                  \tag{C5}
\]

where

\[
 M=A(s+1)(A+1-t)\bigl(1+(A+1)t-t^2\bigr).                 \tag{C6}
\]

The raw files additionally contain six unrestricted equality multipliers
(\mu_k) such that, before eliminating any variable,

\[
 \sum_iN_i e_i+M=\sum_k\mu_k\bigl((BL-I_3)_k\bigr).       \tag{C7}
\]

Thus (C7) is a literal Farkas combination, not reliance on a solved-form
calculation.

If every row has negative mass at most (t), then each selected entry obeys
(e_i\ge-t).  With (D_*=\sum_iN_i), (C5) gives

\[
 -M=\sum_iN_i e_i\ge-tD_*,
 \qquad\text{hence}\qquad \frac{M}{D_*}\le t.            \tag{C8}
\]

At the raw point (A=5,s=1/256), the exact values are

\[
 \frac{M}{D_*}
 =\frac{434073047116546305}{2260705411136539904},          \tag{C9}
\]

and

\[
 M-tD_*
 =\frac{555569345906618009855}{18446744073709551616}>0.   \tag{C10}
\]

This proves infeasibility of the necessary entry-bound relaxation and therefore
of every full negativity sign cell.

## Stability

For every rational (A\in[4,6]) and (0<s\le1/256), all five factors in
(C4) are positive.  The following deliberately crude rational bounds suffice:

\[
 N_0<1,\quad N_1<8,\quad N_2<253,\quad N_3<1,\quad N_4<1,
\]

so (D_*<264).  Also (M>A^2\ge16).  Consequently

\[
 \frac{M}{D_*}>\frac{16}{264}=\frac2{33}
 >\frac1{65536}\ge s^2=t.                                 \tag{C11}
\]

The multiplier identity never uses the norm equation for (Z), the distance
sign pattern, or (g).  It therefore survives independently imposing any
(g\in[4s,6s]).  On the consistent singleton display, (g=A\|Z\|_1=As).

## Clone and nonvertex stability

Clone columns with the same factor row may be aggregated.  A full-fiber
coefficient has lower bound (-t), because the sum of all negative entries in
that fiber is at most the whole-row negative mass.

More generally, if an added zero-top row has

\[
 \ell_x=\sum_u\theta_u\ell_u,qquad \theta_u\ge0,quad
 \sum_u\theta_u=1,
\]

then deleting (x) and replacing (b_u) by
(b_u+\theta_u b_x) preserves (BL=I) and the pinned top row.  The elementary
inequality

\[
 (-(r+\theta q))_+\le(-r)_++\theta(-q)_+                 \tag{C12}
\]

shows that total row negativity cannot increase after distributing the deleted
coefficient. This proves the six-point formal far-freight refinement reduces to
the same five-point certificate; it does not assert that the refinement realizes
the global H-X geometry.

## Nearby equality relaxation and the blocking constraints

The raw files include

\[
 B=\begin{pmatrix}c\\ e_z-c\\ e_o-c\end{pmatrix}.         \tag{C13}
\]

It satisfies (BL=I_3), hence (P=LB) has exact row sums and (P^2=P), and
it satisfies both affine gadget identities and all top-row coefficient pins.
The independent checker recomputes those facts.  It is not a completion:

\[
 \delta(P)=\frac{21475229695}{4294967296}>t,qquad
 \|Z\|_1=\frac{65537}{32768}>s.                            \tag{C14}
\]

Thus the exact left-inverse equations themselves are consistent. The Farkas
identity isolates the all-row negativity threshold as an independent blocker.
The actor-only metric norm is universally blocked as well, not merely failed by
this sample: the $D$-moment equation and $\max_j|x_j|=A$ give

\[
1=\left|\sum_jx_jD_j\right|\le A\|D\|_1=As<1.             \tag{C15}
\]

Separately, the exact exposedness calculation (20)--(21) in `FORMULATION.md`
shows that adding no new vertex blocks the genuine tall/co-top geometry. An
extra in-plane vertex is precisely the first modification that can change all
three mechanisms.

## Candidate registry contract

**Minimal actor-hull starvation completion obstruction:** There is a universal rational $s_0>0$ such that, for every $0<s\le s_0$, no rank-three exact signed idempotent with row negativity at most $s^2$, after clone aggregation and deletion of zero-top nonvertex rows in the local actor hull, can have five factor-row fibers $v,w,f,z,o$ satisfying $F+A Z=s^2O$, $p_w-p_v=sF/(1+s)$, $A\in[4,6]$, and the pinned top-row fiber masses $(1-s,s+s^2,-s^2,0,0)$.

## EXTRA-VERTEX certificate

Status: **AUTHOR-CLAIM**. This is exact-rational L3 evidence, not a proof
shard. The raw records are in raw/xv/ and are checked independently by
check_xv.py.

### Parametric seven-entry identity

After the exact reduction (XV7)--(XV11), put

\[
 H_q=X+Y-1,\qquad B_q=A+(1-t)X-AY,\qquad K_q=AY+tX,
\]

\[
 d=A+1-t,\qquad C=1+a(A-t).                              \tag{XV-C1}
\]

On the surviving strip

\[
 0\le Y\le1,\qquad \frac1s-A\le X\le\frac2s+4s,          \tag{XV-C2}
\]

all three of \(H_q,B_q,K_q\) are strictly positive. Select the entries

\[
 e=(P_{fq},P_{ov},P_{ow},P_{oz},P_{qv},P_{qw},P_{qf})
                                                               \tag{XV-C3}
\]

and give them the respective multipliers

\[
\begin{aligned}
N={}&(B_qXH_q,\ AH_qK_q,\ A(1-a)H_qK_q,\ dH_qK_q,\\
    &\hspace{28mm}AB_q,\ AB_qC,\ AB_qd).
\end{aligned}                                             \tag{XV-C4}
\]

Every \(N_i\) is positive. In the order
\((D0,Dx,Dy,E0,Ex,Ey)\), give the six \(BL=I_3\) residuals
the unrestricted multipliers

\[
\begin{aligned}
\mu={}&(AB_qX,-AB_qX,-AB_qX,\\
 &AH_qK_q+AB_qY,\ (1-t)H_qK_q-AB_qY,\ -AH_qK_q-AB_qY).
\end{aligned}                                             \tag{XV-C5}
\]

Direct coefficient cancellation gives the literal Farkas identity

\[
 \sum_{i=0}^6N_i e_i+AB_qH_q
 =\sum_{k=0}^5\mu_k(BL-I_3)_k.                           \tag{XV-C6}
\]

Consequently \(BL=I_3\) implies

\[
 \sum_iN_i e_i=-AB_qH_q.                                 \tag{XV-C7}
\]

The necessary entry bounds \(e_i\ge-t\) would force
\(AB_qH_q\le tD_*\), where \(D_*=\sum_iN_i\). But exactly

\[
 \frac{tD_*}{AB_qH_q}
 =t\left[
 \frac XA+\frac{K_q}{B_q}\left(2-a+\frac dA\right)
 +\frac{1+C+d}{H_q}\right].                              \tag{XV-C8}
\]

For every rational \(A\in[4,6]\), \(0<s\le1/256\), and every point in
(XV-C2),

\[
 H_q\ge249,\qquad B_q>249,\qquad K_q<7,\qquad C<2,\qquad d<7.
                                                               \tag{XV-C9}
\]

The three terms in (XV-C8), including the outer factor \(t\), are bounded
strictly by

\[
 \frac1{500},\qquad\frac1{1000},\qquad\frac1{1000},
\]

respectively. Hence

\[
 \frac{tD_*}{AB_qH_q}<\frac1{250},\qquad
 AB_qH_q-tD_*>\frac{249}{250}AB_qH_q>0.                  \tag{XV-C10}
\]

At the raw representative

\[
 A=5,\quad s=\frac1{256},\quad X=256,\quad Y=\frac12,
\]

the exact checked values are

\[
 H_q=\frac{511}{2},\quad B_q=\frac{66175}{256},\quad
 K_q=\frac{641}{256},\quad AB_qH_q=\frac{169077125}{512},
\]

\[
 D_*=\frac{145981017713367445}{8623489024},
\]

\[
 AB_qH_q-tD_*
 =\frac{186482464633099560555}{565148976676864}>0,
\]

\[
 \frac{AB_qH_q}{D_*}
 =\frac{81363545292800}{4170886220381927}.               \tag{XV-C11}
\]

The independent checker reconstructs (XV-C6) from raw affine forms, checks
the exact interval bounds in (XV-C9)--(XV-C10), and checks the full identity
at 81 rational parameter probes: three values each of \(A,s,Y\), and three
strip-owned choices of \(X\). No floating-point number is accepted from the
raw JSON.

### Near/far refinements and what the certificate consumes

The literal and near cases use (XV-C6) directly. For the seven-row far case,
first apply the metric reduction to the uncompressed matrix. Then distribute
the midpoint column by

\[
 b'_v=b_v+\tfrac12b_m,\qquad b'_f=b_f+\tfrac12b_m.        \tag{XV-C12}
\]

This preserves \(BL=I_3\), the top pins, \(q\), and does not increase any
row's negative mass by (C12). The resulting six-row problem is therefore
killed by (XV-C6). Loss of equality in the metric norm after compression is
irrelevant because the metric has already been used only for the reduction,
and (XV-C6) itself does not use it.

The parent five-entry multipliers do **not** extend unchanged: the new
\(D_q,E_q\) coefficients leave a nonzero residual, and the required
actor-cone correction has the wrong sign in the surviving xv_zo cell.
The operative Farkas identity is the genuinely new seven-entry pattern
(XV-C4)--(XV-C6). That seven-entry identity is certified for one exterior
fiber and is not claimed to superpose for two.

There is, however, a second exact multiplier pattern which is column-local.
For every zero-top exterior support fiber \(q_k=(1,X_k,Y_k)\) in the
canonical slab, the entry and row-budget consequences give

\[
 |D_{q_k}|\le t,\qquad |X_kD_{q_k}|\le s(2+4s^2).         \tag{XV-C13}
\]

Summing the \(D\)-moment proves (XV13). Thus this *column-local moment
pattern*, not the parent pattern and not the seven-entry pattern, replicates
to any fixed number of exterior support fibers. It certifies \(K\le124\) at
the parent ceiling, and every fixed \(K\) below the ceiling (XV14). It does
not justify a vertex-count-only statement when arbitrarily many exterior
nonvertex fibers are present.

### Updated candidate registry contract

The preceding minimal actor-hull contract remains valid and metric-free.
The certified extension has the following narrower metric-dependent form:

**Bounded-slab-support starvation completion obstruction:** For every fixed
integer \(K\ge1\), let
\[
s_0(K)=\min\{1/256,1/(12(K+1))\}.
\]
For every rational \(A\in[4,6]\) and \(0<s\le s_0(K)\), no rank-three exact
signed idempotent with every row negativity at most \(s^2\) and
\(\|p_z-p_v\|_1=s\) can have actor fibers \(v,w,f,z,o\) satisfying
\[
F+AZ=s^2O,\qquad p_w-p_v=\frac{s}{1+s}F,
\]
top-row fiber masses \(1-s,s+s^2,-s^2\) on \(v,w,f\), respectively, and
zero on \(z,o\) and all remaining fibers, at most \(K\) zero-top support
fibers outside the original actor hull each having canonical exposer
coordinate \(Y\in[0,1]\), and every other added zero-top support fiber inside
that hull. Adding any exact requirement \(g\in[4s,6s]\), including the
singleton locus \(g=As\), cannot restore feasibility.

This contract counts exterior support fibers, not merely geometric vertices.
It says nothing about higher rank, an unbounded number of exterior fibers,
or extra rows outside the canonical exposer slab.
