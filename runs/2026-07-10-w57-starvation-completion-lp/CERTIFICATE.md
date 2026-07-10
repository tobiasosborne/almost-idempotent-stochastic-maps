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
