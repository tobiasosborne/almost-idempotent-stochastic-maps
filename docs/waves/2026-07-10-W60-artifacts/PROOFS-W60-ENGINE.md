| target | proved as stated? | ceiling/constants | fixture status |
|---|---|---|---|
| E1 | yes | unit moment; normalized Lipschitz constant \(1/\lVert q_1-q_0\rVert_1\) | normalized class constructed |
| E2 | yes | two sign-unions; global variation at most \(\lVert a-b\rVert_1\) | zero fibers included explicitly |
| E3 | yes | \((1-A\ell_\chi)/\Lambda-\nu(a)-\nu(b)\) | recentred sign functional completed |
| E4 | yes | explicit \(\delta_R=\min\{2^{-16},(4H^2)^{-1}\}\), with \(H\) below | T0 is in \((3,1,0)\); \(\delta_R=2^{-16}\) there |
| E5 | yes | \(\lVert p_r-p_s\rVert_1/[2(2+4\delta)]-2\delta\) | two-block stochastic family checked; factor-two slack at an endpoint |

# W60 engine proofs

Throughout, \(I\) is a finite index set, \(P=(P_{ij})_{i,j\in I}\) is a real
matrix satisfying

\[
P^2=P,\qquad P\mathbf 1=\mathbf 1,
\]

and \(p_i\) denotes its \(i\)-th row.  Its negative mass is

\[
\delta=\delta(P):=\max_i\sum_j(-P_{ij})_+,
\qquad \tau:=\sqrt\delta,
\]

and \(K(P)=\operatorname{conv}\{p_i:i\in I\}\).  The full row-point fibers are
the equivalence classes \(Q\) for the relation \(i\sim j\) if and only if
\(p_i=p_j\); \(p_Q\) is their common row point.  For a row vector \(r\) and a
set \(S\) of fibers, we use

\[
r(S):=\sum_{Q\in S}\sum_{j\in Q}r_j,
\quad
r^+(S):=\sum_{Q\in S}\sum_{j\in Q}(r_j)_+,
\quad
\nu(r):=\sum_j(-r_j)_+.
\]

All sums below are finite.  In particular, regrouping a coordinate sum by
full fibers requires no convergence argument.

## E1. Moment identity

### STATEMENT

**E1 (moment identity; merged N1/X0 at row-hull generality).**
For every finite exact signed idempotent \(P\), every \(q_0,q_1\in K(P)\) with
\(q_0\ne q_1\), and every affine function \(\chi\) on \(\mathbb R^I\) with
\(\chi(q_0)=0\) and \(\chi(q_1)=1\), the full row-point fibers satisfy
\(\sum_Qd_Q\chi(p_Q)=1\), where
\(d_Q:=\sum_{j\in Q}(q_{1j}-q_{0j})\).

Prove also, as a separate labelled construction, non-emptiness of the
normalized class: there exists such a \(\chi\) with
\[
|\chi(a)-\chi(b)|
\le \frac{\lVert a-b\rVert_1}{\lVert q_1-q_0\rVert_1}
\quad\text{for all }a,b
\]
(Hahn--Banach / dual-norm attainment on \(\ell^1\)).

### PROOF

**Mini-proof E1.1 (the synthetic-row properties used here).**  Let
\(q=\sum_i\lambda_i p_i\in K(P)\), where \(\lambda_i\ge0\) and
\(\sum_i\lambda_i=1\).  The \(i\)-th row of \(P^2=P\) says \(p_iP=p_i\).
Consequently

\[
qP=\sum_i\lambda_i p_iP=\sum_i\lambda_i p_i=q.       \tag{E1.1}
\]

Also \(p_i\mathbf1=1\), so

\[
q\mathbf1=\sum_i\lambda_i p_i\mathbf1=1.             \tag{E1.2}
\]

Finally, coordinatewise convexity of (x\mapsto(-x)_+) gives

\[
\nu(q)
=\sum_j\left(-\sum_i\lambda_iP_{ij}\right)_+
\le\sum_i\lambda_i\sum_j(-P_{ij})_+
\le\delta.                                             \tag{E1.3}
\]

Thus a synthetic row is left-fixed, has total mass one, and has negative
mass at most \(\delta\).  Only (E1.1)--(E1.2) are needed for the moment
identity; (E1.3) records the full synthetic-row assertion demanded by later
uses.

Put \(D=q_1-q_0\).  By (E1.1)--(E1.2),

\[
DP=D,\qquad D\mathbf1=0.                               \tag{E1.4}
\]

Write the affine function as \(\chi(x)=L(x)+\beta\), with \(L\) linear.  Since
\(DP=\sum_jD_jp_j\), (E1.4) yields

\[
\begin{aligned}
\sum_{j\in I}D_j\chi(p_j)
&=L\!\left(\sum_jD_jp_j\right)+\beta\sum_jD_j \\
&=L(DP)=L(D)\\
&=\chi(q_1)-\chi(q_0)=1.                              \tag{E1.5}
\end{aligned}
\]

The value \(\chi(p_j)\) is constant for \(j\) in a full row-point fiber.
Grouping (E1.5) by those fibers gives

\[
\sum_Q\left(\sum_{j\in Q}D_j\right)\chi(p_Q)
=\sum_Qd_Q\chi(p_Q)=1,                                \tag{E1.6}
\]

which is the claimed moment identity.  Notice that (E1.5) is an exact
idempotence calculation, not an index-level path interpretation.

**Construction E1.2 (non-emptiness of the normalized class).**  Let
\(s=\lVert D\rVert_1>0\), and define

\[
g_j:=
\begin{cases}
 1,&D_j>0,\\
-1,&D_j<0,\\
 0,&D_j=0.
\end{cases}
\]

Then \(\lVert g\rVert_\infty\le1\) and
\(g\cdot D=\sum_j|D_j|=s\).  Define the ambient affine functional

\[
\chi(x):=\frac{g\cdot(x-q_0)}s.                        \tag{E1.7}
\]

It satisfies \(\chi(q_0)=0\), \(\chi(q_1)=1\), and, by
\(\ell^1/\ell^\infty\) duality,

\[
|\chi(a)-\chi(b)|
=\frac{|g\cdot(a-b)|}{s}
\le\frac{\lVert a-b\rVert_1}{s}.                     \tag{E1.8}
\]

This is the finite-dimensional Hahn--Banach norm-attainment construction,
written explicitly.

### SCOPE

E1 supplies an exact scalar reproduction moment and a norming affine
functional for any two distinct synthetic rows.  It does not select the two
rows, control the fiber coefficients \(d_Q\) locally, or turn any coefficient
into a transition/path mass.  It gives neither a tail estimate nor actor,
slab, rank, or selected-corner data.

## E2. Two-sign-union variation ledger

### STATEMENT

**E2 (two-sign-union variation ledger).**
For every finite exact signed idempotent \(P\), every ordered pair \((a,b)\) of
synthetic rows (elements of \(K(P)\)), and every set \(S\) of full row-point
fibers:
\[
\sum_{Q\in S}|d_Q|
\le a^+(S)+b^+(S)+\nu(a)+\nu(b).                       \tag{E2.1}
\]
Pay each row budget once per sign-union, never per fiber.  Handle \(d_Q=0\)
fibers explicitly.  Also record the global bound
\[
\sum_Q|d_Q|\le\lVert a-b\rVert_1.                      \tag{E2.2}
\]

Here, as fixed in the brief,
\[
d_Q:=\sum_{j\in Q}(a_j-b_j).
\]

### PROOF

**Mini-proof E2.1 (synthetic rows and their subset budgets).**  If
\(r=\sum_i\lambda_i p_i\in K(P)\), the calculation in (E1.1)--(E1.3), repeated
here, gives

\[
rP=r,\qquad r\mathbf1=1,\qquad \nu(r)\le\delta.        \tag{E2.3}
\]

For any coordinate subset \(U\subseteq I\), split
\(r_j=(r_j)_+-(-r_j)_+\). Since \(r\mathbf1=1\), its total positive mass is
\(1+\nu(r)\), and hence

\[
-\nu(r)\le r(U)\le r^+(U)\le1+\nu(r).                \tag{E2.4}
\]

The proof below needs only the first inequality and the elementary bound
\(r(U)\le r^+(U)\); the fact that \(a,b\) are synthetic ensures in particular
that their displayed negative masses are finite and at most \(\delta\).

Partition \(S\) after fiber aggregation into

\[
S_+:=\{Q\in S:d_Q>0\},\quad
S_-:=\{Q\in S:d_Q<0\},\quad
S_0:=\{Q\in S:d_Q=0\}.                                \tag{E2.5}
\]

Let \(U_+=\bigcup_{Q\in S_+}Q\) and
\(U_-=\bigcup_{Q\in S_-}Q\).  These are two genuine coordinate subsets.
Applying each row budget once to the entire appropriate sign-union gives

\[
\begin{aligned}
\sum_{Q\in S_+}|d_Q|
&=a(U_+)-b(U_+)\\
&\le a^+(S_+)+\nu(b),                                  \tag{E2.6}\\
\sum_{Q\in S_-}|d_Q|
&=b(U_-)-a(U_-)\\
&\le b^+(S_-)+\nu(a).                                  \tag{E2.7}
\end{aligned}
\]

Every fiber in \(S_0\) contributes exactly zero, regardless of cancellation
inside that fiber.  Adding (E2.6)--(E2.7), and enlarging the two positive-mass
terms from their sign-unions to all of \(S\), proves (E2.1).  In particular,
neither negative budget is paid once per fiber.

For the global estimate, the triangle inequality inside each full fiber gives

\[
\sum_Q|d_Q|
=\sum_Q\left|\sum_{j\in Q}(a_j-b_j)\right|
\le\sum_Q\sum_{j\in Q}|a_j-b_j|
=\lVert a-b\rVert_1,                                  \tag{E2.8}
\]

which is (E2.2).

### SCOPE

E2 converts aggregate \(d\)-variation on a chosen set of full fibers into two
positive-mass terms plus two row negativity budgets.  It does not bound the
number of fibers, prevent cancellation within a fiber, or give a useful bound
when the two rows themselves place large positive mass on \(S\).  It contains
no per-fiber financing conclusion and no selection of \(a,b\) or \(S\).

## E3. Financing floor

### STATEMENT

**E3 (financing floor; N3 verbatim).**
For every finite exact signed idempotent \(P\), every ordered pair \((a,b)\) of
synthetic rows with \(\ell:=\lVert a-b\rVert_1>0\), every affine \(\chi\)
satisfying \(\chi(a)-\chi(b)=1\)
[VERIFIER CORRECTION applied per VERDICT-W60-ENGINE.md §E3: the former
endpoint-pin parenthetical was needlessly stronger than the condition the
proof uses; \(\chi(b)=0,\chi(a)=1\) is a permissible special normalization,
not a hypothesis needed by the lemma], all reals
\(A,\Lambda>0\), and every set \(N\) of full row-point fibers such that
\(|\chi(p_Q)|\le A\) for all \(Q\in N\) and
\(|\chi(p_Q)|\le\Lambda\) for all \(Q\notin N\), the complement \(F\) of
\(N\) satisfies
\[
a^+(F)+b^+(F)
\ge \frac{1-A\ell_\chi}{\Lambda}-\nu(a)-\nu(b),
\qquad
\ell_\chi:=\sum_Q|d_Q|\le\ell.                         \tag{E3.1}
\]
Derive this from E1 + E2 by splitting the identity over \(N\cup F\).  Include,
as a labelled corollary in the body (not a separate target), the
recentred-sign-functional instantiation: for rows \(r,s\) and any center
\(c\in K(P)\), the fibers within \(\ell^1\)-distance \(A\ell\) of \(c\)
qualify as \(N\) with \(\Lambda=(2+4\delta)/\ell\); prove the row-diameter
bound used.

### PROOF

The pinned normalization in the statement implies
\(\chi(a)-\chi(b)=1\).  More generally, the proof of E1 shows that this
difference-one condition alone gives the moment identity: adding a constant to
\(\chi\) contributes that constant times
\(\sum_Qd_Q=(a-b)\mathbf1=0\).  The absolute-value hypotheses above, however,
always refer to the particular representative of \(\chi\) that is displayed.
This distinction will matter in the recentred corollary below.

**Mini-proof E3.1 (synthetic-row facts used by E1 and E2).**  Write
\(a=\sum_i\alpha_i p_i\) and \(b=\sum_i\beta_i p_i\) as convex combinations.
Row idempotence and coordinatewise convexity of the negative part give

\[
aP=a,\quad bP=b,\quad a\mathbf1=b\mathbf1=1,
\quad \nu(a),\nu(b)\le\delta.                          \tag{E3.2}
\]

Thus E1 applies to \((b,a)\), and the subset ledgers used in E2 apply to both
rows.  This is the only synthetic-row input to the main financing estimate.

By E1 and the chosen orientation,

\[
1=\sum_Qd_Q\chi(p_Q).                                  \tag{E3.3}
\]

Split this identity over \(N\cup F\), take absolute values, use the two lever
bounds, then use E2 only on \(F\):

\[
\begin{aligned}
1
&\le A\sum_{Q\in N}|d_Q|+\Lambda\sum_{Q\in F}|d_Q|\\
&\le A\ell_\chi
 +\Lambda\bigl(a^+(F)+b^+(F)+\nu(a)+\nu(b)\bigr).
                                                               \tag{E3.4}
\end{aligned}
\]

Rearranging (E3.4) proves the floor in (E3.1).  Finally, grouping cannot
increase total variation, so E2.8 with \(a,b\) gives

\[
\ell_\chi=\sum_Q|d_Q|\le\lVert a-b\rVert_1=\ell.       \tag{E3.5}
\]

This proves E3.

**Mini-proof E3.2 (row-hull diameter used in the corollary).**  For any row
\(p_i\), total mass one implies

\[
\lVert p_i\rVert_1
=\sum_j(P_{ij})_++\sum_j(-P_{ij})_+
=1+2\nu(p_i)\le1+2\delta.                              \tag{E3.6}
\]

Hence \(\lVert p_i-p_k\rVert_1\le2+4\delta\) for all rows.  If
\(c=\sum_k\lambda_kp_k\in K(P)\), convexity then gives, for every fiber \(Q\),

\[
\lVert p_Q-c\rVert_1
\le\sum_k\lambda_k\lVert p_Q-p_k\rVert_1
\le2+4\delta.                                          \tag{E3.7}
\]

This proves the row-to-row and row-to-synthetic-center diameter bounds rather
than importing them from the definitions.

**Corollary E3.3 (recentred sign-functional instantiation).**  Let \(r,s\) be
row indices, put

\[
D:=p_r-p_s,\qquad \ell:=\lVert D\rVert_1>0,
\qquad \sigma_j:=\operatorname{sgn}(D_j),
\]

and fix any \(c\in K(P)\).  Define

\[
\psi_c(x):=\frac1\ell\sum_j\sigma_j(x_j-c_j).          \tag{E3.8}
\]

Then

\[
\psi_c(p_r)-\psi_c(p_s)
=\frac1\ell\sum_j\sigma_jD_j=1,                       \tag{E3.9}
\]

so the constant-shift-invariant moment identity (E3.3) applies, even though
the convenient centering \(\psi_c(c)=0\) need not pin either endpoint to zero.
Also

\[
|\psi_c(p_Q)|
\le\frac{\lVert p_Q-c\rVert_1}{\ell}.                 \tag{E3.10}
\]

Consequently every fiber satisfying
\(\lVert p_Q-c\rVert_1\le A\ell\) qualifies for \(N\) with the low-lever
bound \(A\).  By (E3.7), every remaining fiber, indeed every fiber at all,
has

\[
|\psi_c(p_Q)|\le\Lambda,
\qquad
\Lambda:=\frac{2+4\delta}{\ell}.                       \tag{E3.11}
\]

Thus the already-proved estimate (E3.4), whose proof requires only the
difference-one moment identity, applies directly to \(\psi_c\).  If one wants
literal endpoint pins, subtract \(\psi_c(p_s)\), while correspondingly
rechecking the absolute lever bounds for that shifted representative.

### SCOPE

E3 is a conditional demand estimate: it says how much positive coefficient
mass \(a,b\) must place in \(F\) once a normalized moment and low/high lever
bounds are supplied.  The right-hand side may be nonpositive.  The statement
does not construct a useful set \(N\), force confinement, select an actor pair,
or cap the supply on \(F\).  The recentred corollary supplies a canonical
functional and metric ball, but no assertion that exterior positive mass is
small.

## E4. Robust scalar starvation

### STATEMENT

**E4 (robust scalar starvation; X1 verbatim -- THE T0 GENERALIZATION).**
For every finite \(K_R,L,K_C\ge0\) there exists a universal
\(\delta_R(K_R,L,K_C)\in(0,2^{-16}]\) such that no finite exact signed
idempotent \(P\) with \(0<\delta(P)\le\delta_R\) admits full row-point fibers
represented by \(v,f\), a pair \((A,q)\) with \(A\ge4\), \(q\in K(P)\),
\[
\tau/2\le\lVert q-p_v\rVert_1\le2\tau,\qquad
\lVert p_f-p_v+A(q-p_v)\rVert_1\le K_R\delta,
\]
and an affine \(\chi\) with \(\chi(p_v)=0\), \(\chi(q)=1\),
\[
|\chi(x)-\chi(y)|
\le\frac{\lVert x-y\rVert_1}{\lVert q-p_v\rVert_1}
\quad\text{on }K(P),
\]
such that
\[
\operatorname{Tail}_L(v,\chi)
:=\sum_{Q:\,|\chi(p_Q)|>L}(c_Q)_+\le K_C\delta,
\qquad c_Q:=\sum_{j\in Q}P_{vj}.                       \tag{E4.2}
\]
Follow the X1 mechanism sketch: E1 unit moment for \(D=q-p_v\); sign-split the
tail; row budgets of the synthetic row \(q\) and of row \(f\) (via
\(p_f=p_v-A D+r\), \(\lVert r\rVert_1\le K_R\delta\)); core costs at most
\(L\lVert D\rVert_1\); derive an explicit universal ceiling
\(\delta_R(K_R,L,K_C)\) in closed form.

**MANDATORY FIXTURE.** Verify that the T0 configuration
(context/PAPER-PROOF-w59.md display, \(q=p_z\)) lies in the regime
\((K_R,L,K_C)=(3,1,0)\) and that the ceiling at \((3,1,0)\) is at least some
explicit positive number; compare with the T0 close.

### PROOF

Fix \(K_R,L,K_C\ge0\), and define the closed-form constants

\[
B:=K_C+1+\frac{K_C+K_R+1}{4},
\qquad
H:=2L+6B,                                               \tag{E4.3}
\]

\[
\boxed{
\delta_R(K_R,L,K_C)
:=\min\left\{2^{-16},\frac1{4H^2}\right\}.}           \tag{E4.4}
\]

Since \(B\ge5/4\), one has \(H>0\), so (E4.4) lies in
\((0,2^{-16}]\).

Assume for contradiction that data in the statement exist with
\(0<\delta\le\delta_R\).  Put

\[
D:=q-p_v,\qquad s:=\lVert D\rVert_1,
\qquad d_Q:=\sum_{j\in Q}D_j.                          \tag{E4.5}
\]

**Mini-proof E4.1 (the synthetic-row properties used in the moment and the
negative sign-union).**  If \(q=\sum_i\lambda_ip_i\), then row idempotence,
row sums, and convexity of the negative part give

\[
qP=q,\qquad q\mathbf1=1,
\qquad \nu(q)\le\sum_i\lambda_i\nu(p_i)\le\delta.      \tag{E4.6}
\]

Since also \(p_vP=p_v\) and \(p_v\mathbf1=1\), it follows that

\[
DP=D,\qquad D\mathbf1=0.                               \tag{E4.7}
\]

Writing \(\chi=\mathcal L+\beta\) and repeating the E1 calculation gives

\[
\sum_Qd_Q\chi(p_Q)
=\mathcal L(DP)=\mathcal L(D)
=\chi(q)-\chi(p_v)=1.                                  \tag{E4.8}
\]

Thus synthetic fixedness is used exactly to obtain the unit moment.  The
bound \(\nu(q)\le\delta\) will be used once on a union of negative-\(d\)
tail fibers.

**Mini-proof E4.2 (row subset budgets and the global lever).**  If a signed
row vector \(u\) has total mass one, then for every coordinate subset \(U\),

\[
-\nu(u)\le u(U)\le1+\nu(u),
\qquad \lVert u\rVert_1=1+2\nu(u).                     \tag{E4.9}
\]

For actual rows of \(P\), \(\nu(u)\le\delta\), and therefore

\[
\lVert p_i-p_k\rVert_1\le2+4\delta.                   \tag{E4.10}
\]

Both \(p_Q,p_v\in K(P)\); hence the Lipschitz condition and
\(\chi(p_v)=0\) imply

\[
|\chi(p_Q)|
\le\frac{\lVert p_Q-p_v\rVert_1}{s}
\le\frac{2+4\delta}{s}.                               \tag{E4.11}
\]

This is the only row-diameter use.

Let

\[
T:=\{Q:|\chi(p_Q)|>L\},\qquad C:=\{Q:|\chi(p_Q)|\le L\}.
\]

After full-fiber aggregation, split the tail into

\[
T_-:=\{Q\in T:d_Q<0\},\quad
T_+:=\{Q\in T:d_Q>0\},\quad
T_0:=\{Q\in T:d_Q=0\}.                                \tag{E4.12}
\]

The fibers in \(T_0\) contribute neither variation nor moment.  Write
\(U_\pm=\bigcup_{Q\in T_\pm}Q\).

On the negative sign-union, \(d_Q=q(Q)-c_Q<0\).  The tail cap and the single
synthetic-row lower subset budget give

\[
\begin{aligned}
\sum_{Q\in T_-}|d_Q|
&=c(U_-)-q(U_-)\\
&\le\sum_{Q\in T_-}(c_Q)_++\nu(q)\\
&\le(K_C+1)\delta.                                     \tag{E4.13}
\end{aligned}
\]

No coordinatewise positivity of \(c_Q\) was assumed: the positive part is
taken after the mandated full-fiber aggregation.

Define the residual row vector

\[
R:=p_f-p_v+AD,
\qquad \lVert R\rVert_1\le K_R\delta.                  \tag{E4.14}
\]

Let \(D_+:=\sum_{Q\in T_+}d_Q\).  Aggregating (E4.14) on the one union
(U_+) gives

\[
p_f(U_+)=c(U_+)-AD_++R(U_+).
\]

Consequently, using the row-(f) lower subset budget once,

\[
\begin{aligned}
AD_+
&=c(U_+)+R(U_+)-p_f(U_+)\\
&\le\sum_{Q\in T_+}(c_Q)_+
   +\lVert R\rVert_1+\nu(p_f)\\
&\le(K_C+K_R+1)\delta.                                 \tag{E4.15}
\end{aligned}
\]

Since \(A\ge4\), (E4.13)--(E4.15) yield the entire two-sign-union tail
budget

\[
\sum_{Q\in T}|d_Q|
\le\delta\left(K_C+1+\frac{K_C+K_R+1}{4}\right)
=B\delta.                                               \tag{E4.16}
\]

The two row budgets in (E4.13) and (E4.15) were each paid once, not once per
tail fiber.

On the core, grouping can only reduce variation, so

\[
\sum_{Q\in C}|d_Q|\le\sum_Q|d_Q|\le\lVert D\rVert_1=s.
                                                               \tag{E4.17}
\]

Split the unit moment (E4.8), and apply (E4.11), (E4.16), and (E4.17):

\[
\begin{aligned}
1
&\le Ls+\frac{2+4\delta}{s}B\delta\\
&\le2L\tau+2(2+4\delta)B\tau\\
&=\tau\bigl[2L+2(2+4\delta)B\bigr].                  \tag{E4.18}
\end{aligned}
\]

Here the second line uses exactly the actor window
\(s\le2\tau\), \(s\ge\tau/2\), and \(\delta=\tau^2\).

Because \(\delta\le2^{-16}\), one has \(2+4\delta<3\).  By (E4.4),
\(\tau\le1/(2H)\).  Therefore (E4.18) implies

\[
1<\tau(2L+6B)=\tau H\le\frac12,                        \tag{E4.19}
\]

a contradiction.  This proves E4 with the explicit ceiling (E4.4).

### FIXTURE: the T0 configuration

In the display of `context/PAPER-PROOF-w59.md`, set

\[
q=p_z,\quad D=p_z-p_v,\quad \delta=t=\tau^2,
\quad E=p_o-p_v.
\]

There \(A\in[4,6]\), \(\lVert D\rVert_1=\tau\), and
\(p_f-p_v=-AD+\delta E\).  Mini-proof E4.2 gives

\[
\lVert E\rVert_1\le2+4\delta<3,
\]

and hence

\[
\lVert p_f-p_v+AD\rVert_1
=\delta\lVert E\rVert_1<3\delta.                      \tag{E4.20}
\]

Thus the residual condition holds with \(K_R=3\), and the scale window holds
because \(\lVert q-p_v\rVert_1=\tau\).

The normalized class is nonempty by Construction E1.2.  For any member of
that class, the T0 relation

\[
p_w-p_v=a(p_f-p_v),\qquad a=\frac\tau{1+\tau},
\]

and the norming Lipschitz bound give

\[
\begin{aligned}
|\chi(p_w)|
&\le\frac{\lVert p_w-p_v\rVert_1}{\tau}\\
&\le a\bigl(A+\tau\lVert E\rVert_1\bigr)\\
&<\frac\tau{1+\tau}(6+3\tau)<1                       \tag{E4.21}
\end{aligned}
\]

for \(0<\tau\le1/256\).  The only fibers with positive aggregate top
coefficient are \(v,w\): T0 has \(c_v=1-\tau>0\),
\(c_w=\tau+\delta>0\), \(c_f=-\delta\), and every other \(c_Q=0\).
Equation (E4.21), together with \(\chi(p_v)=0\), therefore proves

\[
\operatorname{Tail}_1(v,\chi)=0.                       \tag{E4.22}
\]

So a hypothetical T0 configuration lies in the E4 regime
\((K_R,L,K_C)=(3,1,0)\).

For these constants,

\[
B=0+1+\frac{0+3+1}{4}=2,qquad H=2+12=14,
\]

and

\[
\delta_R(3,1,0)
=\min\{2^{-16},1/784\}=2^{-16}>0.                     \tag{E4.23}
\]

At the endpoint \(\tau=1/256\), the direct E4 necessary inequality is

\[
1\le\tau(10+16\delta)<\frac{11}{256}<1,               \tag{E4.24}
\]

whereas the original T0 paper close was
\(45/1024=11.25/256<1\).  Thus E4 covers the full T0 ceiling and its scalar
close has slightly more numerical room; it does not use T0's rank-three slab
geometry.

### SCOPE

E4 is an exclusion theorem only after all of the actor scaffold, scale window,
small residual, norming functional, and positive aggregate top-tail cap have
been supplied.  It does not produce the actor pair \((A,q)\), prove the tail
cap, align carriers, or say anything about selected-corner, exposedness,
hiddenness, freight, or kernel data.  It does not license index-level path
products, and the proof never uses them.

## E5. Forced exterior coupling

### STATEMENT

**E5 (forced exterior coupling; N7 verbatim).**
For every finite exact signed idempotent \(P\), every pair of row indices
\((r,s)\), and every \(c\in K(P)\), the full row-point fibers \(Q\) with
\(\lVert p_Q-c\rVert_1>1/2\) carry
\[
P_r^++P_s^+
\ge\frac{\lVert p_r-p_s\rVert_1}{2(2+4\delta(P))}
-2\delta(P).                                           \tag{E5.1}
\]
Instantiate E3.

**FIXTURE.** Check the \(\delta=0\) case by hand on a two-block stochastic
idempotent (two disjoint-support recurrent blocks, rows = mixtures) and report
the constant's tightness or slack.

Here and in the proof, “carry \(P_r^++P_s^+\)” means the sum of the two rows'
coordinatewise positive mass over precisely those fibers.

### PROOF

**Mini-proof E5.1 (row and synthetic-center facts used here).**  Actual rows
satisfy

\[
p_iP=p_i,qquad p_i\mathbf1=1,qquad \nu(p_i)\le\delta.
                                                               \tag{E5.2}
\]

If \(c=\sum_k\lambda_kp_k\in K(P)\), then, separately,

\[
cP=c,qquad c\mathbf1=1,qquad \nu(c)\le\delta,         \tag{E5.3}
\]

by convexity exactly as in (E1.1)--(E1.3).  The proof below uses the fact
\(c\in K(P)\) through the following diameter estimate.  Since
\(\lVert p_i\rVert_1=1+2\nu(p_i)\le1+2\delta\),

\[
\lVert p_Q-c\rVert_1
\le\sum_k\lambda_k\lVert p_Q-p_k\rVert_1
\le2+4\delta.                                          \tag{E5.4}
\]

Thus both the synthetic-center status and the row-diameter property have been
proved at the point of use.

Put \(D=p_r-p_s\) and \(\ell=\lVert D\rVert_1\).  If \(\ell=0\), the
right side of (E5.1) equals \(-2\delta\), whereas the left side is nonnegative,
so the assertion is immediate.  Assume \(\ell>0\), define
\(\sigma_j=\operatorname{sgn}(D_j)\), and use the recentred functional

\[
\psi_c(x):=\frac1\ell\sum_j\sigma_j(x_j-c_j).          \tag{E5.5}
\]

As proved directly in (E3.9)--(E3.10),

\[
\psi_c(p_r)-\psi_c(p_s)=1,qquad
|\psi_c(p_Q)|\le\frac{\lVert p_Q-c\rVert_1}{\ell}.    \tag{E5.6}
\]

Let

\[
N:=\{Q:\lVert p_Q-c\rVert_1\le1/2\},
\qquad F:=\{Q:\lVert p_Q-c\rVert_1>1/2\}.             \tag{E5.7}
\]

In E3 take

\[
A_0:=\frac1{2\ell},qquad
\Lambda:=\frac{2+4\delta}{\ell}.                      \tag{E5.8}
\]

Equations (E5.4)--(E5.6) verify the low and global lever hypotheses.  If
\(d_Q=\sum_{j\in Q}D_j\) and
\(\ell_\psi=\sum_Q|d_Q|\), E3 and
\(\ell_\psi\le\ell\) give

\[
\begin{aligned}
P_r^+(F)+P_s^+(F)
&\ge\frac{1-A_0\ell_\psi}{\Lambda}-\nu(p_r)-\nu(p_s)\\
&\ge\frac{1-1/2}{(2+4\delta)/\ell}-2\delta\\
&=\frac{\ell}{2(2+4\delta)}-2\delta.                 \tag{E5.9}
\end{aligned}
\]

This is (E5.1).

### FIXTURE: \(\delta=0\) on a two-block stochastic idempotent

Let \(I=B_1\sqcup B_2\sqcup T\), where (B_1,B_2) are nonempty.  Let
\(\mu_1,\mu_2\) be probability rows supported on (B_1,B_2), respectively.
Choose numbers \(\theta_i\in[0,1]\), with \(\theta_i=1\) on \(B_1\) and
\(\theta_i=0\) on \(B_2\), and define every row by

\[
p_i=\theta_i\mu_1+(1-\theta_i)\mu_2.                  \tag{E5.10}
\]

The coordinates in \(T\) receive zero mass.  The matrix is stochastic, so
\(\delta=0\), and

\[
\begin{aligned}
p_iP
&=\sum_{j\in B_1}\theta_i\mu_{1j}p_j
 +\sum_{j\in B_2}(1-\theta_i)\mu_{2j}p_j\\
&=\theta_i\mu_1+(1-\theta_i)\mu_2=p_i.                \tag{E5.11}
\end{aligned}
\]

Thus (P^2=P).  This is the two disjoint recurrent-block idempotent, with
optional transient rows that are mixtures of the two recurrent rows.

For two rows (r,s), disjointness of the supports gives

\[
\ell=\lVert p_r-p_s\rVert_1
=2|\theta_r-\theta_s|.                                 \tag{E5.12}
\]

Every \(c\in K(P)\) has the form
\(c=\gamma\mu_1+(1-\gamma)\mu_2\), \(0\le\gamma\le1\).  A row point with
mixture parameter \(\theta\) has distance

\[
\lVert p_\theta-c\rVert_1=2|\theta-\gamma|.           \tag{E5.13}
\]

Rows \(p_r,p_s\) put no coordinate mass on \(T\), so only the two recurrent
fibers can contribute to the exterior positive mass.  Their distances from
\(c\) are \(2(1-\gamma)\) and \(2\gamma\).  Therefore the exterior joint mass
\(M(\gamma)\) is

\[
M(\gamma)=
\begin{cases}
\theta_r+\theta_s,&0\le\gamma\le1/4,\\
2,&1/4<\gamma<3/4,\\
2-\theta_r-\theta_s,&3/4\le\gamma\le1.
\end{cases}                                            \tag{E5.14}
\]

The endpoint ownership in (E5.14) follows from the strict exterior condition
\(>1/2\).  In the first case,
\(M\ge|\theta_r-\theta_s|=\ell/2\); in the last case the same follows from
\((1-\theta_r)+(1-\theta_s)\ge|\theta_r-\theta_s|\); in the middle case
\(M=2\ge\ell\).  In particular this direct computation implies the E5
\(\delta=0\) lower bound \(M\ge\ell/4\).

The constant is not tight on this family.  Taking \(r\) in \(B_1\), \(s\) in
\(B_2\), and \(c=\mu_2\) gives \(\ell=2\) and \(M=1\), while E5 guarantees only
\(\ell/4=1/2\).  Thus the displayed E5 constant has exactly a factor-two slack
in this endpoint example; the stronger family-specific inequality
\(M\ge\ell/2\) is attained there.

### SCOPE

E5 forces joint positive exterior coupling for a pair of already chosen rows
and an already chosen center.  It does not say which of the two rows pays,
identify one exterior fiber, control the number of fibers, or furnish an actor
pair, tail cap, selected-corner datum, or freight carrier.  Its lower bound is
nonpositive — hence trivially true and uninformative — if and only if
\(\ell\le4\delta(2+4\delta)=8\delta+16\delta^2\); in particular E5 is vacuous
throughout the regime \(\ell\le8\delta\)
[VERIFIER CORRECTION applied per VERDICT-W60-ENGINE.md §E5: exact triviality
threshold recorded in place of the former vague vacuity sentence].  The
two-block fixture's better constant is special to that disjoint stochastic
geometry.
