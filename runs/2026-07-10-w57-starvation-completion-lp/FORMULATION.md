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

The first genuinely different case is **not decided here**: rank three with an
additional vertex outside the actor hull. Such a column cannot be distributed
with nonnegative barycentric weights, changes the $BL=I$ moments, and may destroy
the fixed exposures (20). It is the first support pattern capable of the actual
tall/hidden geometry. General higher-rank or redundant transverse-support
patterns are likewise outside the proved family, although a minimal transverse
rank lift with only one support row per new direction may retain the local
cancellation. Therefore this is an exact actor-hull infeasibility result, not a
dimension-free completion theorem and not a proof of H-X or L6.5.

## 6. Stability family

The certificate in `CERTIFICATE.md` is contradictory for every rational
$A\in[4,6]$ and $0<s\le1/256$. It does not consume (7), (8), or any distance
constraint. Consequently adding a requirement $g\in[4s,6s]$ cannot restore
feasibility. The nonvacuous singleton tableau lies on the consistent locus
$g=A\|Z\|_1=As$; no independent two-parameter singleton family is claimed.
