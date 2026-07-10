# Exact completion problem and decided family

Status: **AUTHOR-CLAIM**. This is a finite exact decision problem, not a
promotion of H-X, L6.5, or any other open statement. The scripts use only
`fractions.Fraction` arithmetic.

## 1. Rational parameters and canonical factor gauge

The raw decision point is

\[
s=\tau=\frac1{256},\qquad t=s^2=\frac1{65536},\qquad
a=\frac{s}{1+s}=\frac1{257},\qquad A=A_0=5.               \tag{1}
\]

For stability, $A$ ranges over the rational interval $[4,6]$ and
$0<s\le1/256$.

Write $P=LB$, with every row of $L\in\mathbb Q^{n\times r}$ starting with
$1$, and impose

\[
BL=I_r.                                                     \tag{2}
\]

Then $P^2=P$. Also $\mathbf1=Le_0$, so
$B\mathbf1=BL e_0=e_0$ and $P\mathbf1=\mathbf1$. The map
$u\mapsto uB$ is injective because $uBL=u$; affine relations and vertexhood
may therefore be checked in factor coordinates.

The first possible rank is $r=3$. In actor order $(v,w,f,z,o)$ use

\[
L=\begin{pmatrix}
1&0&0\\
1&-Aa&ta\\
1&-A&t\\
1&1&0\\
1&0&1
\end{pmatrix}.                                             \tag{3}
\]

This gauge is exhaustive for a transverse rank-three completion on exactly
these five row points: $Z=p_z-p_v$ and $O=p_o-p_v$ are independent because an
affine exposer vanishes on $Z$ but takes value $1$ on $O$, and they may be
chosen as the two factor axes. The W55 centered tableau then forces

\[
F+AZ=tO,\qquad p_w-p_v=aF,                                 \tag{4}
\]

where identifying the source symbols with
$F=p_f-p_v$, $Z=p_z-p_v$, $O=p_o-p_v$ is an explicit
inference from its centered display.

Since $\ell_v=e_0$, row $p_v$ is the first row of $B$. Pin it to

\[
c=(1-s,\ s+t,\ -t,\ 0,\ 0).                               \tag{5}
\]

Directly, $cL=e_0^T$. Thus the top row reproduces exactly, has negative mass
$t$, has positive support only on $v,w$, and has zero positive inflow to $f$.
Write the two unknown rows of $B$ as $D,E\in\mathbb Q^5$. For
$\ell_i=(1,x_i,y_i)$,

\[
P_{ij}=c_j+x_iD_j+y_iE_j.                                  \tag{6}
\]

The literal metric pin is

\[
\|Z\|_1=\|D\|_1=s.                                        \tag{7}
\]

On a fixed sign cell for $D$, this is one rational linear equality. If the
*full* always-tight families are the singleton families $T=\{f\}$ and
$O=\{o\}$, then

\[
g=\|F-tO\|_1=A\|Z\|_1=As=5\tau.                           \tag{8}
\]

Singleton support of one display is not enough: the completion cell must also
certify the whole optimal face, as specified below.

There is already an exact metric obstruction in the actor-only chart. The
$D$-moment row of (2) gives $\sum_jx_jD_j=1$, while
$\max_j|x_j|=A$. Hence

\[
1\le A\|D\|_1=As<1                                        \tag{9}
\]

for $A\le6$ and $s\le1/256$. The main certificate is stronger in a different
direction: it does not use (7) and proves that even dropping the metric pin
cannot rescue the all-row negativity threshold.

## 2. Exact negativity LP and support cells

For every row $i$, impose

\[
\nu_i=\sum_j(-P_{ij})_+\le t.                              \tag{10}
\]

On a prescribed negative-entry set $N_i$, (10) is exactly

\[
P_{ij}\le0\ (j\in N_i),\quad P_{ij}\ge0\ (j\notin N_i),
\qquad -\sum_{j\in N_i}P_{ij}\le t.                       \tag{11}
\]

The objective form replaces $t$ by a variable $d$ and minimizes $d$; the
completion threshold is $d\le t$, with equality already forced by row $v$.
The emitted Farkas certificate contradicts the weaker necessary inequalities

\[
P_{ij}\ge-t\quad\text{for every }i,j,                      \tag{12}
\]

so it simultaneously decides every entry-sign cell. No simplex enumeration is
needed.

## 3. Exact full-system geometry

This subsection states the constraints a genuine tall/co-top completion would
have to satisfy. The raw certificate kills a closed algebraic relaxation first;
the checker does not claim that its equality-only sample realizes this geometry.

### Hiddenness and the full optimal face

The canonical exposer is $h(1,x,y)=y$, with

\[
h_v=h_z=0,qquad h_f=t,qquad h_o=1,qquad h_w=at.          \tag{13}
\]

Fix $z,w$ in the $4s$-near distance cell and $f,o$ in the far cell. For any
admissible exposer $r$, affinity and (4) give

\[
r_f+A r_z=t r_o\le t,
\]

so $t^*(v)\le t$; (13) attains $t$, hence
$t^*(v)=t<s/4$. At optimum, $r_f\ge t$, $r_z\ge0$, and
$r_o\le1$, so equality forces $r_f=t,r_z=0,r_o=1$ on the
whole optimal face. With no additional tight actor this certifies
$T=\{f\}$, $Z=\{z\}$ after deleting the centered $v$ constraint, and
$O=\{o\}$, making (8) the full-hull gap.

### Metric, height, support functional, and co-top cells

For every actor pair and coordinate choose
$\sigma_{ik,j}\in\{-1,1\}$ and set

\[
R_{ik,j}=(\ell_i-\ell_k)\mathbin{\cdot}b_j,qquad
\sigma_{ik,j}R_{ik,j}\ge0,qquad
D_{ik}=\sum_j\sigma_{ik,j}R_{ik,j}.                        \tag{14}
\]

Thus $D_{ik}=\|p_i-p_k\|_1$ on that finite sign cell. For the minimal
visible-set candidate $W=\{o\}$, choose a sign vector
$\eta\in\{-1,1\}^5$ for $p_v-p_o$ and define

\[
\phi(p_i)=\sum_j\eta_j(P_{ij}-P_{oj}),qquad
H=\phi(p_v)=D_{vo},qquad q_i=H-\phi(p_i).                 \tag{15}
\]

This is an ambient $1$-Lipschitz functional because
$\|\eta\|_\infty=1$, and it vanishes at $o$. The exact top/co-top cell uses
the fixed rational slack $t$ for strict requirements:

\[
D_{io}\le H\quad(\text{all }i),\qquad H\ge16s+t,qquad
D_{fv}\ge4s,qquad D_{fo}\ge H-4s+t,                      \tag{16}
\]

\[
q_i\ge0\quad(\text{all }i),qquad
q_f+Aq_z=tq_o,qquad 0\le q_o\le2+4t.                     \tag{17}
\]

The affine identity in (17) is automatic from (4), but is listed as a raw
residual in a full geometry implementation. It yields the exact selected-row
score

\[
\frac{2q_f}{2+4t}+h_f\le3t<\frac{12s}{13}.                \tag{18}
\]

Affinity gives the corresponding $q,h<4s$ inequalities for $w,v,f$ and for
the midpoint freight point used below.

### Recomputing the visible set

Once the far set $F_u=\{i:D_{ui}\ge4s\}$ is fixed, an exposer at a factor
vertex $u$ with margin at least $m$ is the rational linear system

\[
r_i=\alpha+\beta x_i+\gamma y_i,quad r_u=0,quad
0\le r_i\le1,quad r_i\ge m\ (i\in F_u).                  \tag{19}
\]

A vertex is declared visible by a solution of (19) at $m=s/4$; it is declared
hidden by rational Farkas multipliers proving (19) infeasible at $m=s/4$.
Together with the vertex set read from the fixed factor polytope, these finite
primal/dual cells recompute $W$ exactly.

In fact, the five-point cell fails this recomputation independently of the
matrix certificate. Injectivity makes $v,z,f,o$ the vertices of the canonical
quadrilateral and $w$ a nonvertex. The vertices $z,f$ have admissible exposers

\[
g_z(x,y)=\frac{1-x}{A+1},qquad
g_f(x,y)=\frac{x+A}{A+1},                                  \tag{20}
\]

with far margins much larger than $s/4$, so both are visible. Moreover

\[
\frac{p_f+A p_z}{A+1}
=\left(1-\frac{t}{A+1}\right)p_v+\frac{t}{A+1}p_o,         \tag{21}
\]

which puts $p_v$ within
$t\|p_o-p_v\|_1/(A+1)\ll16s$ of the visible hull containing
$f,z,o$. Therefore the formal $W=\{o\}$ cell is empty. The freight systems
below are exact constrained H-X candidate relaxations, not realized H-X data.

## 4. Decided cases

Every case includes all unknown entry-sign and metric-sign cells.

### `literal_r3_actor5`

This is (2)--(21) on the five actor points, with $A=5$ and $g=5s$.
It is the literal W55 local tableau plus the full-system constraints. Clone
splitting is included by aggregating duplicate factor rows; a fiber aggregate
is still at least $-t$.

### `hx_near_r3_actor5`

The nonvertex $w=(1-a)v+af$ has the legal kernel

\[
\xi_w(v)=\frac1{1+s},\qquad \xi_w(f)=\frac{s}{1+s}.        \tag{22}
\]

Pin the *row-$f$* freight, not the unrelated source entry $P_{vw}$, by

\[
P_{fw}\ge\frac{1+s}{4}.                                   \tag{23}
\]

Then the nominal near atom has

\[
\Gamma_f(w,v)=\frac{P_{fw}}{1+s}\ge\frac14>\frac18.       \tag{24}
\]

Equations (16)--(19) are the H-X top/co-top/hiddenness constraints that would
make this a genuine $B_N$ datum. Equation (20) proves those constraints cannot
hold in the actor-only polytope; the Farkas certificate independently kills an
even weaker algebraic relaxation.

### `hx_far_r3_nonvertex6`

The point $w$ cannot fund the far atom: its far kernel weight is $a$, so under
the negativity budget

\[
\Gamma_f(w,f)\le a(1+t)<s<\frac18.                        \tag{25}
\]

The first zero-top nonvertex refinement adds

\[
\ell_x=\tfrac12\ell_v+\tfrac12\ell_f,qquad P_{vx}=0,
\qquad P_{fx}\ge\frac12,\qquad D_{xv}\le4s-t.            \tag{26}
\]

Its legal kernel has $\xi_x(v)=\xi_x(f)=1/2$, so the nominal far atom
$(x,f)$ has mass at least $1/4>1/8$. The full H-X $B_F$ constraints are again
(16)--(19); this six-point polytope still has the same visible vertices, so it
is a local freight relaxation rather than a realized co-top datum.

This refinement compresses exactly via

\[
b'_v=b_v+\tfrac12b_x,qquad b'_f=b_f+\tfrac12b_x,           \tag{27}
\]

with other columns unchanged. Then $B'L_5=I_3$, the top row is unchanged, and

\[
P'_{iv}=P_{iv}+\tfrac12P_{ix},\qquad
P'_{if}=P_{if}+\tfrac12P_{ix}.                             \tag{28}
\]

The inequality

\[
(-(u+\theta x))_+\le(-u)_++\theta(-x)_+\qquad(\theta\ge0) \tag{29}
\]

shows that total row negativity cannot increase. The same analytic argument
covers clones and any number of zero-top nonvertices having nonnegative actor
barycentric coordinates. The independent script mechanically checks the raw
midpoint instance (26)--(28); the general statement is the displayed exact
inequality.

## 5. Minimality and the exact boundary

Rank $2$ has affine row dimension at most one. Since $p_z\ne p_v$ and an
affine exposer vanishes at both, it would vanish on the entire affine row line,
contradicting $h_f=t>0$. Thus rank $3$ is first.

The five actor points are distinct: $z\ne v$ by (7), $f,z,o$ have forced
different exposer data, and $w=(1-a)v+af$ is a strict nonvertex. Thus five
row points are the smallest literal support, and (3) exhausts its transverse
rank-three gauges. The sixth zero-top nonvertex is the smallest local far-horn
refinement and compresses back to actor5.

The first genuinely different case was **not decided by the parent sections
1--6**: rank three with an additional vertex outside the actor hull. Such a
column cannot be distributed with nonnegative barycentric weights, changes the
$BL=I$ moments, and may destroy the fixed exposures (20). The appended
EXTRA-VERTEX section decides exactly that family. General higher-rank or
unbounded redundant transverse-support patterns remain outside the campaign.
Therefore the parent result is an exact actor-hull infeasibility result, not a
dimension-free completion theorem and not a proof of H-X or L6.5.

## 6. Stability family

The certificate in `CERTIFICATE.md` is contradictory for every rational
$A\in[4,6]$ and $0<s\le1/256$. It does not consume (7), (8), or any distance
constraint. Consequently adding a requirement $g\in[4s,6s]$ cannot restore
feasibility. The nonvacuous singleton tableau lies on the consistent locus
$g=A\|Z\|_1=As$; no independent two-parameter singleton family is claimed.

## EXTRA-VERTEX — 7. First exterior completion family

This section is the one-family extension of the completed actor-hull campaign.
Its status is again **AUTHOR-CLAIM** and exact-rational L3 evidence. It does
not promote H-X, L6.5, or conj-sl1a-off-diagonal-cell.

### 7.1 Definition and exterior case grammar

Keep (1)--(8), the actor order and gauge (3), and rank \(r=3\). Add one
zero-top row-point fiber \(q\), with

\[
 \ell_q=(1,X,Y),\qquad c_q=P_{vq}=0.                    \tag{XV1}
\]

Thus \(L\) has six rows and \(B=(c;D;E)\) has six columns. The top row is

\[
 c=(1-s,s+t,-t,0,0,0),                                  \tag{XV2}
\]

and \(BL=I_3\), \(P=LB\), \(\|D\|_1=s\), and all row-negativity
constraints are imposed on the enlarged matrices. Clones are full-fiber
aggregates as before. The word *vertex* in this section means that \(q\) is
outside the old actor hull, not merely that a sixth index has been appended.

In the \((x,y)\)-plane the old actor hull is exactly

\[
 Y\ge0,\qquad tX+AY\ge0,\qquad X+Y\le1,
 \qquad A+(1-t)X-AY\ge0.                                \tag{XV3}
\]

The actor constraints force the unique optimum-\(t\) exposer to be
\(h(x,y)=y\). Hence an extra-vertex completion of the same optimal-face
problem must have

\[
 0\le Y\le1.                                             \tag{XV4}
\]

Within this closed slab, the strict exterior is the following disjoint list;
equality belongs to the nonviolated side, so every boundary is owned:

| location cell | exact violated facets | old vertex change |
|---|---|---|
| xv_fv | \(tX+AY<0\), the other two upper facets nonnegative | none generically; \(v\) is cut if \(Y=0\), and \(f\) is cut if the \(of\) facet is equality |
| xv_of | \(A+(1-t)X-AY<0\), \(tX+AY\ge0\) | none generically; \(f\) is cut if the \(fv\) facet is equality |
| xv_f_corner | both preceding expressions are \(<0\) | \(f\) is cut off |
| xv_zo | \(X+Y>1\) | none for \(Y>0\); \(z\) is cut if \(Y=0\) |

The first three cells have \(X<0\); xv_zo has \(X>0\). There is no fifth
cell in (XV4). All distance-coordinate signs, the near/far status of \(q\),
and the visible-set/exposer primal-dual cells remain part of the finite LP
grammar. In particular, \(W\) is recomputed from the enlarged row polytope;
it is not silently fixed to \(\{o\}\).

The full optimal-face support patterns are also owned. If \(q\) is
\(4s\)-near, \(Y=0\) adds \(q\) to \(Z\), \(0<Y<1\) is nontight, and \(Y=1\)
adds it to \(O\). If \(q\) is \(4s\)-far, \(Y<t\) is incompatible with
\(t^*(v)=t\), \(Y=t\) adds it to \(T\), \(t<Y<1\) is nontight, and \(Y=1\)
adds it to \(O\). The singleton cell still has
\(T=\{f\},Z=\{z\},O=\{o\}\) and \(g=A\|D\|_1=As\). On a
boundary-support cell, \(g=5s\) is a separate full-hull equality to be
recomputed, not a consequence of one displayed exposer.

### 7.2 Honest smallest-first support list

The decided family consists of the following three support patterns. Each
contains every location and sign cell above; the common algebraic relaxation
below decides them before any geometry cell can rescue feasibility.

1. xv_literal_r3_vertex6: the five actors and the exterior vertex \(q\).
   This is the smallest genuine change to the actor hull.
2. xv_hx_near_r3_vertex6: the same support, with
   \(P_{fw}\ge(1+s)/4\). When both \(v,f\) remain vertices, the kernel is
   (22), so the \((w,v)\) atom has mass at least \(1/4\). Whenever \(f\) is
   cut but \(v\) remains a vertex, write

   \[
   f=\alpha q+\beta v+\gamma o,
   \quad \alpha=-\frac A X,
   \quad \beta=\frac{A+(1-t)X-AY}{X},
   \quad \gamma=\frac{tX+AY}{X}.                         \tag{XV5}
   \]

   These are nonnegative and sum to one (all three are positive in the
   strict xv_f_corner cell). Composing with
   \(w=(1-a)v+af\) leaves vertex-kernel mass at \(v\) at least
   \(1-a=1/(1+s)\), so the same \(1/4\) near lower bound survives exact
   revertexization. On a boundary that cuts \(v\), the kernel must likewise
   be revertexized and its radial owner recomputed; no automatic horn label
   is assigned. The common literal relaxation already kills that boundary.
3. xv_hx_far_r3_vertex6_nonvertex7: add the smallest zero-top freight row

   \[
   \ell_m=\tfrac12(\ell_v+\ell_f),\qquad P_{vm}=0,
   \qquad P_{fm}\ge\tfrac12.                             \tag{XV6}
   \]

   When \(v,f\) are vertices, \(\xi_m(v)=\xi_m(f)=1/2\), and the nominal far
   atom has mass at least \(1/4\). The row \(w\) cannot replace \(m\), since
   its far vertex share gives at most
   \(a(1+t)<s<1/8\); the new point \(q\) is a vertex and therefore has Dirac
   kernel, giving no off-diagonal atom by itself. In xv_f_corner, the
   midpoint kernel must be composed with (XV5), and its radial/corner owner
   must be recomputed. The same warning applies on any boundary cutting a
   kernel vertex. No unverified far label is assigned there.

The full H-X versions extend (14)--(19) to every displayed row, recompute the
geometric vertices and \(W\), and use the strict rational slack \(t\) for the
strict horn inequalities. The raw equality-only samples do not satisfy the
freight inequalities and are not presented as H-X data.

These are deliberately the smallest support patterns. A nonvertex whose
kernel uses \(q\) is another support fiber outside the *old* actor hull; it is
not silently compressed while retaining the metric equality. Bounded numbers
of such fibers are covered by §7.4, while an unbounded collection is outside
this one-family decision.

### 7.3 Exact reduction to the only possible exterior cell

Every row \(p_i\), viewed as a signed coefficient vector, has

\[
 \|p_i\|_1=1+2\nu_i\le1+2t.                              \tag{XV7}
\]

Since

\[
 p_q=(1-Y)p_v+Yp_o+XD,
\]

(XV4), convexity, and (XV7) give the exact necessary bound

\[
 |X|s\le2+4t.                                             \tag{XV8}
\]

The \(D\)-moment of \(BL=I\) gives

\[
 XD_q=1-\sum_{j\ne q}x_jD_j\ge1-As>0.                   \tag{XV9}
\]

Here (XV9) also covers the midpoint (XV6), because every non-\(q\) factor
coordinate has \(|x_j|\le A\). If \(X<0\), then \(D_q<0\). But
\(P_{zq}=D_q\ge-t\), so (XV8) implies

\[
 XD_q\le |X|t\le s(2+4t),
\]

contradicting (XV9). Uniformly over \(A\in[4,6]\) and
\(0<s\le1/256\), the exact worst-case margin is

\[
 1-As-s(2+4s^2)\ge
 \frac{4063231}{4194304}>0.                              \tag{XV10}
\]

Thus every putative completion lies in xv_zo, and

\[
 \frac1s-A\le X\le\frac2s+4s,\qquad 0\le Y\le1.          \tag{XV11}
\]

This reduction is essential: without the metric and full row-budget
constraints, arbitrary far-left entry-bound relaxations can be feasible.

### 7.4 What a second exterior vertex changes

A second exterior vertex adds a second moment column and new polygon/kernel
order types; the seven-entry identity in CERTIFICATE.md is not claimed to
superpose unchanged. A separate column-local estimate does replicate. For
each zero-top exterior support fiber \(q_k=(1,X_k,Y_k)\) with
\(0\le Y_k\le1\),

\[
 |D_{q_k}|\le t,\qquad |X_kD_{q_k}|\le s(2+4s^2).         \tag{XV12}
\]

Indeed the negative case uses \(P_{zq_k}\ge-t\); in the positive case,
\(P_{fq_k}=-AD_{q_k}+tE_{q_k}\ge-t\) and
\(E_{q_k}=P_{oq_k}\le1+t\) give
\(D_{q_k}\le t(2+t)/A<t\). Consequently, with at most \(K\) exterior
zero-top support fibers and all other added zero-top fibers in the original
actor hull,

\[
 1\le s\bigl(A+K(2+4s^2)\bigr).                          \tag{XV13}
\]

This is contradictory for \(K\le124\) at the parent ceiling; at \(K=124\)
the worst exact margin is \(8161/1048576\). For every fixed \(K\ge1\), the
safe rational ceiling

\[
 s_K=\min\left\{\frac1{256},\frac1{12(K+1)}\right\}       \tag{XV14}
\]

makes (XV13) contradictory. This counts exterior *support fibers*, not just
geometric vertices. It does not cover an unbounded collection of nonvertices
reaching outside the old actor hull, nor does it enumerate the two-vertex H-X
kernel order types.
