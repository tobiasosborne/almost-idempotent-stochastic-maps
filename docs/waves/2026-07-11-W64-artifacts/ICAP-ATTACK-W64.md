# I-cap attack: score-bulk transport and the closed sign-cube packet

> **Status discipline.** Everything new in this file is **proposed / `conjecture`**,
> including the routine nodes proved in the companion appendix.  Nothing is
> promoted.  All statements remain in the exact signed picture and on full
> row-point fibers.

## 0. Verdict first

I achieve objective **(a)**: I-cap decomposes, after near-mechanical work on the
proved interface, into six disjoint, strictly smaller constant-mass packages
\[
 X_{\rm gap},\ X_{\rm near},\ I_{\rm far},\ I_{\rm near},\
 D_{\rm gap},\ D_{\rm near}.
\]
I do **not** prove I-cap, obtain a weakened height theorem, or claim objective
(c) for the whole class; the named internally closed sign-cube package is the
bulk-I branch, while mixed X and D branches remain creative.

The new routine step is a **score-bulk census**.  For the exhibited target
certificate \(\mathscr C^*=(\phi,h,f^*,\eta^*)\), L0 makes the score
\(s=2(H-\phi)/D_0+h\) have \(\lambda_A\)-mean \(<6\tau/7\).  Hence
\(\lambda_A\{s\le12\tau/13\}>1/14\).  Fix one fresh arbitrary legal kernel
before inspecting cells and run the proved corner/radial arithmetic at every
score-good root.  One of X/I/D has bulk mass at least \(1/42\).  A single
root-independent receiver statistic and one R2 foldback then give constant
top-owned cell mass:
\[
 P_v^+(g_X)>c_m/512,\qquad
 P_v^+(g_I),P_v^+(g_D)>c_m/1536.                       \tag{V0}
\]
In I and D the statistic is an intrinsic vertex-set indicator; the kernel
disappears.

For a diagonal bulk, two further R2 foldbacks on the **same** receiver test
produce an \(O(\delta)\)-overflow two-fold flow.  Tallness is spent through
\[
 P_v^+\{d_Q\le\tau/4\}
 <\delta+\frac{4\tau}{63}\left(D_0+\frac\tau4\right)
 <\frac{2\tau}{15},                                    \tag{T-spend}
\]
leaving more than \(c_m/1024\) of receiverwise covered flow in the outer
halo.  The old one-root cap \(\mathfrak F_I=O(\delta)\) was automatic and
T-free; this constant top-owned completion is the genuine reduction.

**Hard core, in one sentence:** an exact high-rank sign cube must carry
constant top mass on alpha-free cancellation vertices while its two-fold
positive flow is covered inside the saturated halo and every common scalar
demand remains \(O(\delta)\).

The structural diagnosis is sharp.  Type I forces the far-tight hull to cancel
from radius \(4\tau\) down below \((1/2+\delta)\tau\), so a singleton
\(T(u)\) is impossible; this is exactly why the W63 plateau has \(M_I=0\).
Conversely, a new exact short \(4\times4\) module has local type-I ledger mass
\(1023/8192>1/16\), and an \(8\times8\) block-diagonal extension meets all
numerical I mass guards.  Both fail tallness and neither supplies the required
top ownership; in the \(8\times8\) example that ownership is exactly zero.  Thus exact
idempotence alone does not force D: coupling a multi-ray I module into the same
tall ultra web is the real cost.

## 1. The tree / the argument

### 1.1 Pinned notation and public objects

Adopt `context/DECOMPOSITION-W63-I.md` §§0--1.1 verbatim.  In particular,
\[
 b=\frac{c_m}{128},\qquad
 \delta_{\rm rt}=\min\left\{2^{-16},(c_m/4)^2,(c_mb/120)^2\right\},
 \qquad D_0=2+4\delta.
\]
Fix an arbitrary datum in the pinned I-cap antecedent and its already exhibited
certificate
\[
 \mathscr C^*=(\phi,h,f^*,\eta^*)\in\mathscr P(\mathfrak d),
 \qquad M_X(\mathscr C^*)\le\frac18,\qquad
 M_I(\mathscr C^*)\ge\frac1{16}.                       \tag{1.1}
\]
No replacement certificate is chosen.  Put \(z=H-\phi\).  L0 supplies
\(\lambda_A\) and the exact ownership relation
\[
 a_A:=S(1-\theta)\lambda_A\le P_v^+                  \tag{1.2}
\]
as full-fiber measures.  The hiddenness-witness measure is unrelated and never
appears below.

For the bulk construction, fix one fresh arbitrary legal row-point vertex
kernel \(\xi\), independently of the erased kernel behind \(\mathscr C^*\),
and fix it **before** any cell is inspected.  Every statement below holds for
every such choice.  The kernel is erased again after the common statistics are
formed, except for the public restricted barycentric coupling \(\Xi_X\) in the
X branch.

The tree is

```text
target I certificate C*
  -> bare one-root R2 cap (diagnostic only)
  -> score-good bulk F, lambda_A(F) > 1/14
  -> arbitrary-kernel X/I/D census
       I bulk (>=1/42) -> internally closed diagonal flow -> far / near
       else X bulk (>=1/42) -> coupled freight            -> gap / near
       else D bulk (>1/42) -> internally closed diagonal flow -> gap / near
```

### 1.2 Routine node B0 — the old single-root closure, honestly priced

**(a) Pinned contract — `conj-icap-single-root-receiver-cap`.**  On the
diagonal type-I part of \(\mathscr C^*\), define
\[
 \eta_I^*(u):=\eta^*\{(x,u):p_x=p_u,\ u\text{ is type I}\},
 \qquad m_I^*:=\eta_I^*(1).
\]
Then
\[
 m_I^*\ge\frac1{16},\qquad \eta_I^*\le P_{f^*}^+,
\]
and, with \(\Pi_{f^*}(R)=\sum_u\eta_I^*(u)P_u^+(R)\),
\[
 \mathfrak F_{f^*}:=\sup_{0\le g\le1}
 \{\Pi_{f^*}(g)-P_{f^*}^+(g)\}
 \le e_\delta:=2\delta(1+\delta).                     \tag{B0}
\]
The supremum is attained by the single receiver test
\(1_{\{\Pi_{f^*}>P_{f^*}^+\}}\).

**(b) Mechanism.**  Diracness of every legal kernel at a vertex makes the
diagonal measure a full-fiber submeasure of \(P_{f^*}^+\).  Apply
`lem-l5-positive-flow-foldback` once at row \(f^*\).

**(c) Honest price.**  Routine, but strategically insufficient.  The cap is
automatic for every exact I-certificate, gives no top-owned lower mass at
\(f^*\), and does not spend T.  Treating B0 alone as the “completion package”
would merely rename the old hard leaf.

**(d) Interface check.**  One common \(g\), full fibers, no witness display,
no atom selection, and no second corner extraction.

**(e) Fallback.**  The receiver overlap
\[
 \Pi_{f^*}^{\circ}(\{R\})
 :=\min\{\Pi_{f^*}(\{R\}),P_{f^*}^+(\{R\})\},\qquad
 \Pi_{f^*}^{\circ}(E):=\sum_{R\in E}\Pi_{f^*}^{\circ}(\{R\})
\]
has mass at least \(m_I^*-e_\delta\).  This is useful for exact refuter
measurements, but it is not the main reduction.

### 1.3 Routine node S — score-bulk production

**(a) Pinned contract — `conj-icap-score-bulk`.**  Define
\[
 s(x):=\frac{2z(p_x)}{D_0}+h(p_x),\qquad
 F:=\left\{x\in\operatorname{supp}\lambda_A:
 s(x)\le\frac{12\tau}{13}\right\}.                    \tag{1.3}
\]
Then
\[
 \lambda_A(F)>\frac1{14},qquad
 a_A(F)>\frac{c_m}{16}.                                \tag{S}
\]

**(b) Mechanism.**  The score selector's proved check says \(z/D_0\) is an
admissible exposer at \(v\).  L0 therefore gives
\[
 \int s\,d\lambda_A<2\frac{2\tau}{7}+\frac{2\tau}{7}
 =\frac{6\tau}{7}.
\]
Markov at \(12\tau/13\) gives \(\lambda_A(F)>1/14\).
Also \(\theta<\tau/D_0<1/8\), so (1.2) and \(S\ge c_m\) give the displayed
owned-mass floor.

**(c) Honest price.**  Routine.  Its only plausible failure is confusing the
normalized \(\lambda_A\) with the owned measure \(a_A\); (1.2) prevents that.

**(d) Interface check.**  Equality in the score belongs to \(F\).  This is one
fixed affine score, not a finite cover, averaged support functional, or Jensen
argument.  The given \((\phi,h)\) is retained.

**(e) Fallback.**  Keep the exact estimate
\(\lambda_A\{s\le L\tau\}>1-6/(7L)\) for any \(L>6/7\).

### 1.4 Routine node C — arbitrary-kernel bulk census

For every \(f\in F\), use the same \((\phi,h,\xi)\).  The corner ledger gives
the common set
\[
 \mathcal C:=\{(x,u):z(p_x)<4\tau,\ h(p_x)<4\tau,\
                         z(p_u)<4\tau,\ h(p_u)<4\tau\}
\]
with \(\Gamma_f(\mathcal C)>1/2\).  Define \(B(f)=B_F\) if
\(\Gamma_f(B_F)\ge1/4\), and otherwise \(B(f)=B_N\).  Classify \(f\) by
\[
\begin{array}{ll}
 X:&M_X(B(f))>1/8,\\
 I:&M_X(B(f))\le1/8,\ M_I(B(f))\ge1/16,\\
 D:&M_X(B(f))\le1/8,\ M_I(B(f))<1/16,
\end{array}                                             \tag{1.4}
\]
where the D line automatically has \(M_D(B(f))>1/16\).  Write the resulting
partition as \(F_X\sqcup F_I\sqcup F_D=F\).

**(a) Pinned contract — `conj-icap-bulk-census`.**  Exactly one priority
alternative is declared:
\[
\begin{array}{ll}
 \mathrm{BI}:&\lambda_A(F_I)\ge1/42;\\
 \mathrm{BX}:&\lambda_A(F_I)<1/42,\ \lambda_A(F_X)\ge1/42;\\
 \mathrm{BD}:&\lambda_A(F_I)<1/42,\ \lambda_A(F_X)<1/42,
                \ \lambda_A(F_D)>1/42.
\end{array}                                             \tag{C}
\]

**(b) Mechanism.**  This is \(1/14=3/42\) plus the proved corner and radial
partitions.  No cell conjecture is used.

**(c) Honest price.**  Routine-hard only because quantifier order matters.
The census may classify the original root differently under the fresh kernel;
that is harmless.  The original public I-certificate remains fixed, while the
bulk census is an independent package.

**(d) Interface check.**  The kernel is arbitrary before classification.
Radial distance and radial mass equality belong to \(B_F\); \(M_X=1/8\)
continues diagonally; \(M_I=1/16\) belongs to I.  Priority equality belongs to
BI first and BX second.

**(e) Fallback.**  Retain all three weights rather than priority-routing.  That
only strengthens later mixed-cell information.

### 1.5 Routine node G — one common receiver statistic and top ownership

For \(J=X,I,D\), set
\[
 g_J(x):=\sum_u\xi_x(u)
 1_{\mathcal C}(x,u)1_{\mathrm{type}\ J}(x,u),
 \qquad 0\le g_J\le1.                                  \tag{1.5}
\]
Here “type X” means \(p_x\ne p_u\), and I/D have the diagonal predicates in
`def-selected-corner`.

**(a) Pinned contract — `conj-icap-common-cell-foldback`.**  In the routed
bulk cell,
\[
 \begin{array}{c|c|c}
 J& P_f^+(g_J)\text{ for every }f\in F_J
   &P_v^+(g_J)\\ \hline
 X&>1/8&>c_m/512\\
 I&\ge1/16&>c_m/1536\\
 D&>1/16&>c_m/1536.
 \end{array}                                            \tag{G}
\]
For I and D, \(g_J=1_{U_J}\) is the indicator of
\[
 U_J:=\{u:u\text{ is a row vertex},\ z(p_u)<4\tau,\ h(p_u)<4\tau,
                   \ u\text{ has type }J\}.             \tag{1.6}
\]

**(b) Mechanism.**  The selected radial block varies with \(f\), but
\(B(f)\subset\mathcal C\), so \(P_f^+(g_J)=\Gamma_f(\mathcal C\cap J)\)
dominates its cell mass.  Restrict (1.2) to \(F_J\) and apply R2 once to this
single \(g_J\).  The source mass is greater than \(c_m/48\).  Since
\[
 e_\delta=2\delta(1+\delta)<4\delta
 \le\frac{c_m^4}{58{,}982{,}400}<\frac{c_m}{1536},       \tag{1.7}
\]
the conservative floors in (G) follow.  On a diagonal vertex the legal kernel
is Dirac, so it disappears from I and D.

**(c) Honest price.**  This is the decisive gain over B0: constant top-owned
cell mass.  It still gives no circuit/coefficient identification.  In X the
coupling coordinate \(u\) is barycentric provenance, not a transition from
\(v\).

**(d) Interface check.**  Exactly one common nonnegative statistic is folded
in the realized case.  There is no sum of actor-dependent engine tests and no
kernel optimization.

**(e) Fallback.**  Keep the sharper pre-error floors
\(c_m/384\) in X and \(c_m/768\) in I/D.

### 1.6 Routine node T+ — tall completion, not a decorative hypothesis

Let
\[
 \mathcal L_v:=\{Q:d_Q\le\tau/4\},\qquad
 \mathcal H_v^{\rm out}:=\{Q:d_Q>\tau/4\}.
\]

**(a) Pinned contract — `conj-icap-tall-cell-packet`.**  Every routed package
satisfies
\[
 P_v^+(\mathcal L_v)
 <\ell_T:=\delta+\frac{4\tau}{63}\left(D_0+\frac\tau4\right)
 <\frac{2\tau}{15},                                    \tag{T+}
\]
and every receiver on which \(g_J>0\) lies in
\(\mathcal H_v^{\rm out}\).

**(b) Mechanism.**  T gives \(1-\sigma_g<(4\tau/63)(D_0+\tau/4)\), while
\(P_v^+(1)=1+\nu_v\) and \(\nu_v\le\delta\).  Also
\(z(p_x)<4\tau\) implies
\(d_x>H-4\tau>12\tau>\tau/4\).  This is the exact line at which tallness is
consumed.

For a secondary branch of absolute mass \(m_R\), (T+) says that the only
available shallow leakage is an \(O(\tau)\) fraction:
\[
 \frac{P_v^+(\mathcal L_v)}{m_R}<\frac{2\tau}{15m_R}.    \tag{1.8}
\]
Thus a creative proof may not pay a constant cell package from shallow rows.

**(c) Honest price.**  T does not itself align \(P_v^+\), the corner
coefficients, and an alpha-free witness.  That missing alignment is precisely
the completion problem.

**(d) Interface check.**  This uses only the permitted halo height budget.
Equality \(d_Q=\tau/4\) belongs to the shallow set.

**(e) Fallback.**  Retain the sharper undivided parent inequality
\((H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4)\).

### 1.7 Routine node IC — the internally closed diagonal-flow package

This node applies in BI; the identical flow construction applies in BD with
type D in place of type I.

Put
\[
 \alpha_I:=a_A|_{F_I},\qquad a_I:=\alpha_I(1)>\frac{c_m}{48}.
\]
For each \(f\in F_I\), let \(\eta_f^I\) be the type-I restriction of
\(\Gamma_f|_{B(f)}\).  Then
\(\eta_f^I\le P_f^+\) and \(\eta_f^I(1)\ge1/16\).  Define
\[
 \mathcal E_I(f,u):=\alpha_I(f)\eta_f^I(u),\qquad
 \beta_I(u):=\sum_{f\in F_I}\alpha_I(f)\eta_f^I(u),
 \qquad
 \Pi_I(R):=\sum_u\beta_I(u)P_u^+(R).                   \tag{1.9}
\]
Thus the public coefficient layer is one coupled measure \(\mathcal E_I\),
not a dimension-dependent list of roots.

**(a) Pinned contract — `conj-icap-internally-closed-sign-cube-packet`.**
The package satisfies
\[
 \beta_I(1)>\frac{c_m}{768},                            \tag{1.10}
\]
\[
 \overline{\mathfrak F}_I:=
 \sup_{0\le g\le1}\{\Pi_I(g)-P_v^+(g)\}
 \le (1+a_I)e_\delta\le(2+\delta)e_\delta,             \tag{1.11}
\]
and the receiverwise covered measure
\[
 \widehat\Pi_I(\{R\}):=\min\{\Pi_I(\{R\}),P_v^+(\{R\})\},\qquad
 \widehat\Pi_I(E):=\sum_{R\in E}\widehat\Pi_I(\{R\})
\]
obeys
\[
 \widehat\Pi_I(\mathcal H_v^{\rm out})>\frac{c_m}{1024}.
 \tag{1.12}
\]

**(b) Mechanism.**  Apply R2 at each root \(f\) to \(\eta_f^I\), weight by
\(\alpha_I(f)\), and then apply R2 at \(v\) to
\(\alpha_I\le P_v^+\), always using the same arbitrary \(g\).  This proves
(1.11), with the supremum attained by the one overflow indicator.  It is a
fixed two-fold positive-flow calculation, not a recursive corner/web
construction.

Now actually spend T: (1.11) and (T+) give
\[
 \Pi_I(\mathcal L_v)<\frac{3\tau}{20},
 \qquad (2+\delta)e_\delta<\frac\tau{60}.
\]
Consequently
\[
 \widehat\Pi_I(\mathcal H_v^{\rm out})
 >\frac{c_m}{768}-\frac\tau6
 >\frac{c_m}{1024},                                    \tag{1.13}
\]
where \(\tau\le c_m^2/15360\le c_m/15360\) comes from
\(\delta_{\rm rt}\).

**(c) Honest price.**  This is the named internally closed sign-cube
completion package.  It is strictly smaller than I-cap because it requires a
positive-measure *field* of I roots, a constant type-I coefficient layer, an
\(O(\delta)\) common-test overflow, and constant covered outer-halo return.
Its likely death is a high-dimensional stationary Rademacher crown.

**(d) Interface check.**  The two R2 uses share one \(g\); errors are weighted
by total source mass, not by the number of roots.  No hiddenness witnesses are
averaged.  No carrier is used as a new top and no score/corner extraction is
run at a receiver, so this is not the killed second-generation L-C recursion.

**(e) Fallback.**  Retain \(\Pi_I\), \(P_v^+\), and their canonical overlap
rather than selecting a receiver atom.  B0 remains a one-root check on the
original certificate.

If a pair-distance diagnostic is needed, retain the joint coefficient flow
\[
 \mathcal J_I(u,R):=\beta_I(u)P_u^+(\{R\}).
\]
For \(\Pi_I(\{R\})>0\), put
\(c_R=\min\{1,P_v^+(\{R\})/\Pi_I(\{R\})\}\), and put \(c_R=0\) otherwise.
Then \(\widehat{\mathcal J}_I(u,R):=c_R\mathcal J_I(u,R)\) has receiver
marginal \(\widehat\Pi_I\).  This is the only lifted overlap used below.

In BD, define \(\alpha_D,\eta_f^D,\beta_D,\Pi_D,\widehat\Pi_D\) by the same
formulas with I replaced by D.  Since every D root has
\(\eta_f^D(1)>1/16\), equations (1.10)--(1.13) hold with the same conservative
constants (and strictness only improves).

### 1.8 Routine node A — what type I structurally costs

For a type-I carrier \(u\), put
\[
 \rho_T(u):=\operatorname{dist}_1(0,K_T(u)).
\]

**(a) Pinned contract — `conj-icap-alpha-free-cancellation-cost`.**  Every
type-I carrier in B0 or IC has
\[
 \rho_T(u)\le t^*(u)D_0
 <\left(\frac12+\delta\right)\tau.                      \tag{A1}
\]
If \(\lambda_u\) is the far-tight probability in an alpha-free display and
\(\bar p_{T,u}=\int p_t\,d\lambda_u(t)\), then
\[
 \int\|p_t-\bar p_{T,u}\|_1\,d\lambda_u(t)
 >\left(\frac72-\delta\right)\tau.                     \tag{A2}
\]
In particular the \(T(u)\)-hull cannot be geometrically singleton.

**(b) Mechanism.**  `lem-optimal-face-conic-reduction` gives, existentially,
\[
 \bar p_{T,u}-p_u=t^*(u)(\bar p_{O,u}-p_u).
\]
Since \(t^*(u)<\tau/4\) and every row-point distance is at most \(D_0\),
(A1) follows.  Every \(t\in T(u)\) is at least \(4\tau\) from \(u\), so the
triangle inequality gives (A2).

**(c) Honest price.**  Routine geometry, not an exclusion.  It identifies the
cost: convex cancellation by a factor exceeding seven, carried by genuinely
different far-tight directions.

**(d) Interface check.**  Alpha-free displays are used one carrier at a time
as geography.  They are never averaged against \(\beta_I\), identified with
coefficients, or divided by \(t^*(u)\).

**(e) Fallback.**  Use only (A1), the clone-safe convex-hull distance.  Any
singleton or halfspace certificate with \(\rho_T(u)\ge(1/2+\delta)\tau\)
forces type D immediately.

### 1.9 Routine node R — exact six-way residual split

**(a) Pinned contract — conj-icap-six-cell-return-split.**  The routed bulk
package lies in exactly one of the following six cells.

**X.**  In BX define the public barycentric coupling
\[
 \Xi_X(x,u):=P_v^+(x)\xi_x(u)1_{\mathcal C}(x,u)1_X(x,u),
 \qquad \Xi_X(1)=P_v^+(g_X)>\frac{c_m}{512}.             \tag{1.14}
\]
Route to
\[
\begin{array}{ll}
 X_{\rm gap}:&\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}\ge c_m/1024,\\
 X_{\rm near}:&\Xi_X\{\|p_x-p_u\|_1<b\tau\}>c_m/1024.
\end{array}                                             \tag{1.15}
\]

**I.**  In BI put \(n_I=P_v^+|_{U_I}\), so
\(n_I(1)>c_m/1536\).  Route to
\[
\begin{array}{ll}
 I_{\rm far}:&n_I\{\|p_u-p_v\|_1\ge4\tau\}\ge c_m/3072,\\
 I_{\rm near}:&n_I\{\|p_u-p_v\|_1<4\tau\}>c_m/3072.
\end{array}                                             \tag{1.16}
\]

**D.**  In BD put \(n_D=P_v^+|_{U_D}\), so
\(n_D(1)>c_m/1536\), and let
\(g_u=d_1(K_T(u),K_O(u))>0\).  Route to
\[
\begin{array}{ll}
 D_{\rm gap}:&n_D\{g_u\ge\tau\}\ge c_m/3072,\\
 D_{\rm near}:&n_D\{g_u<\tau\}>c_m/3072.
\end{array}                                             \tag{1.17}
\]

All three splits assign equality to the first line.  They are literal
two-piece mass partitions, so the second line is strict.  Each output is a
proper subclass with a constant public mass package; none is I-cap with a new
name.

**(b) Mechanism.**  In each bulk cell, split the constant mass from G into two
measurable pieces and compare each with half of its conservative floor.

**(c) Honest price.**  Routine.  The split supplies geometry but proves no
exclusion; in particular, “near” is never silently discarded.

**(d) Interface check.**  All distances are on row points or compact
always-tight hulls.  Equality belongs to X-gap, I-far, and D-gap.

**(e) Fallback.**  Retain the full distance distribution instead of its
two-bin summary.  No atom or favorable carrier is selected.

### 1.10 The six creative leaves

Every leaf below is proposed.  Its phrase “target I datum” repeats the complete
pinned I-cap antecedent, including the exhibited \(\mathscr C^*\), and also
receives the arbitrary-kernel census package, (T+), and the relevant exact
branch inequality above.

#### X-gap — `conj-icap-bulk-X-gap-exclusion`

**(a) Pinned contract.**  There are universal \(\gamma_{Xg}>0\) and
\(\delta_{Xg}\in(0,\delta_{\rm rt}]\) such that every target I datum with an
\(X_{\rm gap}\) package and \(0<\delta\le\delta_{Xg}\) satisfies
\(Z_v(q_A)\ge\gamma_{Xg}\tau\).

**(b) Mechanism.**  The package has constant coupled mass and an explicit
\(b\tau\) norm gap.  This is the legal input scale for the
`lem-hx-transverse-moment-identity` / signed-variation / financing bank, but
the pair-dependent normers must first be replaced by one common receiver
statistic and folded through R2.  The mandatory T-priced intermediate target
is: for universal \(\Gamma_{Xg},C_{Xg}>0\) with
\(\Gamma_{Xg}>2C_{Xg}/15\),
\[
 Z_v(q_A)\ge
 \Gamma_{Xg}\tau-C_{Xg}P_v^+(\mathcal L_v).            \tag{Xg-T}
\]
Substitution of (T+) then gives the pinned contract with
\(\gamma_{Xg}=\Gamma_{Xg}-2C_{Xg}/15>0\).  A proof that produces only an
unpriced outer-halo ledger has not consumed tallness.

**(c) Honest price.**  Creative-hard.  The likely death is angular
incoherence: a high-dimensional family of separated pairs may have no common
normer.  Positive evidence is that the coefficient-kernel mass and norm gap
now coexist on the same coupled measure.  The W63 X fixture is only short.

**(d) Interface check.**  \(\Xi_X\) is not transition mass \(v\to u\).
No pairwise engine floors are summed before a common-test foldback.

**(e) Fallback.**  Split by a clone-invariant common-direction moment.  Do not
censor the complement or select one freight atom.

#### X-near — `conj-icap-bulk-X-near-exclusion`

**(a) Pinned contract.**  There are universal \(\gamma_{Xn}>0\) and
\(\delta_{Xn}\in(0,\delta_{\rm rt}]\) such that every target I datum with an
\(X_{\rm near}\) package and \(0<\delta\le\delta_{Xn}\) satisfies
\(Z_v(q_A)\ge\gamma_{Xn}\tau\).

**(b) Mechanism.**  This is cluster absorption for off-diagonal barycentric
freight: constant mass has \(p_x\ne p_u\) but displacement below \(b\tau\).
Use T+ and the top-owned common \(g_X\); no financing call is legal until a
new norm gap is produced.  As in (Xg-T), the required intermediate form is
\[
 Z_v(q_A)\ge
 \Gamma_{Xn}\tau-C_{Xn}P_v^+(\mathcal L_v),\qquad
 \Gamma_{Xn}>2C_{Xn}/15,                               \tag{Xn-T}
\]
so T+ is used by subtraction, not merely cited.

**(c) Honest price.**  Creative-hard and probably harder than X-gap.  The
known obstruction is exactly that proximity does not transfer exposedness.

**(d) Interface check.**  Near freight is retained, not deleted by
`lem-censoring-exactness`.

**(e) Fallback.**  Make one fixed split at a smaller multiple of \(\tau\), if
needed.  Do not iterate the split, use a finite cover, or invoke a class count.

#### I-far — `conj-icap-bulk-I-far-sign-cube-exclusion`

**(a) Pinned contract.**  There are universal \(\gamma_{If}>0\) and
\(\delta_{If}\in(0,\delta_{\rm rt}]\) such that every target I datum with an
\(I_{\rm far}\) package and \(0<\delta\le\delta_{If}\) satisfies
\(Z_v(q_A)\ge\gamma_{If}\tau\).

**(b) Mechanism.**  This leaf receives all of IC and A: constant top mass on
far co-top alpha-free vertices, a constant internally covered two-fold flow in
the outer halo, and carrierwise multi-ray cancellation.  The desired close is
one common transport test whose \(\Omega(\tau)\) demand contradicts (1.11),
P, and T+.  V remains independent geography and is never identified with the
coefficient field.

**(c) Honest price.**  Highest-information residual.  A balanced
high-dimensional sign cube is a plausible exact refuter: it makes each carrier
alpha-free while killing every fixed scalar width.  No exact tall completion
is known.

**(d) Interface check.**  Alpha-free witnesses stay separate.  The common
flow is coefficients only.  There is no \(1/t^*\), witness averaging, or
second corner recursion.  The radial top-owned measure \(n_I\) and the
coefficient-flow actor marginal \(\beta_I\) coexist in the packet but are not
identified or asserted to overlap.

**(e) Fallback.**  Split the covered flow by
\(\|p_R-p_u\|_1\ge b\tau\) versus \(<b\tau\) on the explicitly retained joint
measure \(\widehat{\mathcal J}_I\).  The latter is the sharpest form of the
internally closed sign-cube completion package.  No identification with the
separate radial carrier measure \(n_I\) is made.

#### I-near — `conj-icap-bulk-I-near-huddle-exclusion`

**(a) Pinned contract.**  There are universal \(\gamma_{In}>0\) and
\(\delta_{In}\in(0,\delta_{\rm rt}]\) such that every target I datum with an
\(I_{\rm near}\) package and \(0<\delta\le\delta_{In}\) satisfies
\(Z_v(q_A)\ge\gamma_{In}\tau\).

**(b) Mechanism.**  Row \(v\) owns constant mass on alpha-free vertices within
\(4\tau\) of \(p_v\), yet every such vertex has depth \(>H-4\tau\).  Combine
this near-deep huddle with IC's covered outer-halo flow and T+.  A proof needs
a genuine cluster-to-exposedness or cluster-to-common-test statement.

**(c) Honest price.**  Creative-hard.  The existing near-cluster absorption
surface concerns a nearly full huddle; the present floor is only
\(c_m/3072\).  Exposer transfer across \(4\tau\)-near rows is a recorded dead
route.

**(d) Interface check.**  Nearness is not treated as equality or recurrence.
No max-principle far-side return is asserted.

**(e) Fallback.**  Split at \(2\tau\), assigning equality to the outer cell,
while retaining the full IC package in both pieces.

#### D-gap — `conj-icap-bulk-D-gap-exclusion`

**(a) Pinned contract.**  There are universal \(\gamma_{Dg}>0\) and
\(\delta_{Dg}\in(0,\delta_{\rm rt}]\) such that every target I datum with a
\(D_{\rm gap}\) package and \(0<\delta\le\delta_{Dg}\) satisfies
\(Z_v(q_A)\ge\gamma_{Dg}\tau\).

**(b) Mechanism.**  Constant top-owned D mass has separator gap at least
\(\tau\).  This is the best route to the validated robust-starvation bank, but
one must first construct that lemma's actual row fiber, \(A\ge4\),
\(O(\delta)\) residual, and common tail cap.  The diagonal-flow analogue of IC
and T+ remove shallow payment.

**(c) Honest price.**  Creative-hard, but supported by
`lem-starvation-completion-obstruction`.  Its likely death is a high-rank
support escaping the proved slab while preserving the separator.

**(d) Interface check.**  Conic multipliers are geography, not transition
weights.  No recurrence is inferred, and \(n_D\) is not identified with the
actor marginal \(\beta_D\).

**(e) Fallback.**  Split by the actual robust-starvation scaffold window;
retain every failed-input branch explicitly.

#### D-near — `conj-icap-bulk-D-near-intersection-exclusion`

**(a) Pinned contract.**  There are universal \(\gamma_{Dn}>0\) and
\(\delta_{Dn}\in(0,\delta_{\rm rt}]\) such that every target I datum with a
\(D_{\rm near}\) package and \(0<\delta\le\delta_{Dn}\) satisfies
\(Z_v(q_A)\ge\gamma_{Dn}\tau\).

**(b) Mechanism.**  The always-tight hulls are disjoint but within \(\tau\).
Use their closest pair as geography and the top-owned diagonal-flow package as
coefficients.  Any stability theorem must be t*-free and must consume T+.

**(c) Honest price.**  Creative-hard.  The separator is too weak for the
current starvation theorem, while unconditional LP alpha control is false.

**(d) Interface check.**  A near intersection is not promoted to an actual
intersection, and no conic coefficient is iterated.

**(e) Fallback.**  Retain the closest-pair distance distribution as a public
measure; do not choose a favorable carrier.

## 2. Assembly

Assume the routine nodes above and the six creative leaf contracts.  Put
\[
 \gamma_\cap:=\min\{\gamma_{Xg},\gamma_{Xn},\gamma_{If},
                    \gamma_{In},\gamma_{Dg},\gamma_{Dn}\}>0,          \tag{2.1}
\]
\[
 \delta_\cap:=\min\{\delta_{\rm rt},\delta_{Xg},\delta_{Xn},
                     \delta_{If},\delta_{In},\delta_{Dg},\delta_{Dn}\}>0.
                                                                    \tag{2.2}
\]
All constants are fixed before the matrix, datum, certificate, or fresh
arbitrary kernel.

Take an arbitrary target I datum with \(0<\delta\le\delta_\cap\) and fix its
exhibited \(\mathscr C^*\).  S constructs \(F\).  Fix any legal census kernel
before inspecting cells.  C gives exactly one of BI, BX, BD.

- In BX, (1.15) gives exactly one of \(X_{\rm gap}\), \(X_{\rm near}\).
- In BI, IC and A apply, and (1.16) gives exactly one of
  \(I_{\rm far}\), \(I_{\rm near}\).
- In BD, the diagonal-flow analogue of IC applies, and (1.17) gives exactly
  one of \(D_{\rm gap}\), \(D_{\rm near}\).

The realized creative leaf yields
\[
 Z_v(q_A)\ge\gamma_\cap\tau,
\]
which is the pinned I-cap conclusion.  No favorable certificate, kernel,
radial block, or minimizer has been selected.

For the emptiness reading, P gives
\[
 Z_v(q_A)\le\frac{\delta D_0}{S}\le\frac{3\tau^2}{c_m}.
\]
For the emptiness statement define, separately,
\[
 \delta_\cap^{\rm empty}:=
 \min\left\{\delta_\cap,
       \left(\frac{\gamma_\cap c_m}{6}\right)^2\right\}.              \tag{2.3}
\]
At this ceiling the upper bound is at most \(\gamma_\cap\tau/2\), so the
target hypothesis class is
empty.  Equation (2.3) records the price; it is not used to pretend that any
creative leaf has been proved.

## 3. Kill-list check

The following codes cover the brief and the complete dead-route/wall index of
`context/FINDINGS.md`.

- **K1 — signed/clone/frame.** Full fibers and row points only; no stochastic
  reading, raw-index paths, coordinate frame, class count, or dimension loss.
- **K2 — dual direction.** No Jensen, W37 reversal, witness/\(y_c\) averaging,
  top-deficit lower bound, or pointwise-to-barycenter promotion.
- **K3 — hiddenness geography.** No \(1/t^*\), no reduced-witness identification
  with coefficients or \(P_v^+\), and no \(\lambda P=p_v\).
- **K4 — engine/R2.** Every aggregation uses one common nonnegative test; no
  summed actor-dependent demands, vanished endpoint, or implicit \(A=0\).
- **K5 — selection/LP.** No favorable kernel/tie/minimizer, coefficient-only
  cleanup, max-volume/pointwise/single-swap selector, finite cover, broad NSC
  charge, failed-census emptiness, quadratic residual, or generic spectral
  import.
- **K6 — tallness/centers.** T is spent through (T+) and (1.13); only the two
  pinned height budgets are used; all-center floors are never summed over
  centers.
- **K7 — W55/W56.** No conic recurrence, thin/thick fiction, lexicographic
  minimality, freight censoring without a norm gap, second L-C web, transient
  deletion, or max-principle far-side return.
- **K8 — boundaries/quantifiers.** All equalities are owned; datum and original
  certificate precede an arbitrary census kernel, which precedes classification.

This crosswalk includes the absolute deaths in FINDINGS: raw paths and old
selectors (§2026-07-02); legal-leak/orphan and coefficient-only payment
(§2026-07-03); unnormalized chart/class sums and broad NSC; quadratic residuals;
the dual-direction and alpha-blow-up walls; generic spectral imports; W54
witness averaging; W55 \(\lambda P\)/conic recurrence; and all five W56
extraction deaths.

“PASS” below is an interface verdict, not a proof of a creative node.

| Node | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 |
|---|---|---|---|---|---|---|---|---|
| B0 | PASS | PASS | PASS | PASS: one common test | PASS | PASS via consumers | PASS: no recursion | PASS |
| S | PASS | PASS: affine mean only | PASS | PASS | PASS: one fixed score | PASS via T+ | PASS | PASS: score equality in F |
| C | PASS | PASS | PASS | PASS | PASS: arbitrary kernel | PASS via T+ | PASS: no preprocessing minimality | PASS: exact cell priority |
| G | PASS | PASS | PASS: X coupling not transition | PASS: one R2 | PASS | PASS via T+ | PASS | PASS |
| T+ | PASS | PASS | PASS | PASS | PASS | PASS: exact T budget | PASS | PASS: halo equality shallow |
| IC/A | PASS | PASS | PASS: displays separate | PASS: same g in both folds | PASS | PASS: (1.13) spends T | PASS: no second corner web | PASS |
| X-gap | PASS | PASS | PASS | PASS: common test still required | PASS | PASS: target (Xg-T) | PASS: explicit norm gap | PASS |
| X-near | PASS | PASS | PASS | PASS | PASS | PASS: target (Xn-T) | PASS: no censoring | PASS |
| I-far | PASS | PASS | PASS | PASS | PASS | PASS: covered halo flow | PASS: no witness recursion | PASS |
| I-near | PASS | PASS: no exposer transfer | PASS | PASS | PASS | PASS | PASS: no max-principle return | PASS |
| D-gap | PASS | PASS | PASS: conic terms geographic | PASS: robust engine gated | PASS | PASS | PASS: no recurrence | PASS |
| D-near | PASS | PASS | PASS | PASS | PASS: no LP alpha claim | PASS | PASS | PASS |

There are no interface FAILs.  The six creative nodes remain mathematical
gaps, which is why their status is `conjecture`.

## 4. Dispatch order

### 4.1 Routine hostile batch

Verify, in order, B0, S, C, G, T+, IC, A, and R.  The highest-value checks are:

1. \(\lambda_A(F)>1/14\) from the strict \(6\tau/7\) score mean;
2. the fact that \(g_J\) is independent of the root and its radial block;
3. the exact R2 scaling by the *unnormalized* source measure;
4. two R2 folds in IC using the same \(g\), with error \((1+a_I)e_\delta\),
   not a class-count multiple;
5. the T-spent bound (1.13); and
6. clone-splitting invariance of every public measure and threshold.

The companion appendix gives standalone proofs.

### 4.2 L3 deciders with exact target inequalities

A refuter to any leaf must be a sequence of exact rational factorizations
\(P_k=L_kB_k\), \(B_kL_k=I\), with \(\tau_k\to0\), all row negativities at
most \(\tau_k^2\), the full I-base/all-center package,
\(H_k>16\tau_k\), ultra diagnostics, \(\theta_k<\tau_k/D_{0,k}\), an
exhibited target I-certificate, and
\[
 \frac{Z_{v_k}(q_{A,k})}{\tau_k}\longrightarrow0.       \tag{4.1}
\]
It must then hit one exact branch target:

- **X-gap:** \(\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}\ge c_m/1024\).
- **X-near:** the strict complementary mass is \(>c_m/1024\).
- **I-far:** \(P_v^+(U_I\cap\{\|p_u-p_v\|_1\ge4\tau\})\ge c_m/3072\),
  together with (1.10)--(1.12).
- **I-near:** the strict near mass is \(>c_m/3072\), again with
  (1.10)--(1.12).
- **D-gap:** \(P_v^+\{u\in U_D:g_u\ge\tau\}\ge c_m/3072\).
- **D-near:** the strict small-gap mass is \(>c_m/3072\).

Every run must also print
\[
 P_v^+(\mathcal L_v)<\ell_T,\qquad
 \overline{\mathfrak F}_J\le(2+\delta)e_\delta
\]
for \(J=I,D\) where applicable.  The X branches must print the proposed
T-priced **deficit**
\[
 \mathcal D_{X\bullet}:=
 Z_v(q_A)-\Gamma_{X\bullet}\tau
 +C_{X\bullet}P_v^+(\mathcal L_v)
\]
for pre-registered constants satisfying
\(\Gamma_{X\bullet}>2C_{X\bullet}/15\).  Proof attempts target
\(\mathcal D_{X\bullet}\ge0\); a genuine refuter should make it negative.
A small
\(\mathfrak F_I\) is required by exactness and is
not evidence against the package.

The decisive I refuter shape is a **balanced Rademacher crown**.  At the local
geometry level use disjoint mass-zero directions
\[
 d_j:=\frac{e_{2j-1}-e_{2j}}2,\qquad \|d_j\|_1=1,
\]
and set
\[
 p_{r_\varepsilon}=p_v+\frac{4\tau}{d}
       \sum_{j=1}^d\varepsilon_jd_j,\qquad
 \varepsilon\in\{\pm1\}^d.
\]
Its mean is \(p_v\), while every affine \(\ell^1\)-Lipschitz scalar has mean
absolute deviation at most \(4\tau/\sqrt d\); taking
\(d>(4/b)^2\) reaches the ultra-width scale.  A genuine exact refuter must add
constant top ownership, type-I diagonal mass at every bulk root, symmetric
T/O clouds with intersecting hulls, a stationary receiver flow satisfying
(1.11), a tall visible hull, the all-center exterior floors, and
\(\nu_i\le\tau^2\).  Clones do not count toward \(d\); the directions must be
geometrically distinct.

Before that high-rank search, use both exact short calibrations in the appendix as
unit tests.  The \(4\times4\) module tests the optimal-face intersection; its
\(8\times8\) direct-sum extension crosses every numerical I mass guard.  They
are not refuters: both fail tallness by an order-one margin, and the latter
achieves its mass only by severing the I module from top ownership.

### 4.3 Creative order

1. Attack **I-far** first with the Rademacher-crown completion.  It most
   directly decides the internally closed sign-cube threat.
2. Attack **I-near** next as a deep alpha-free huddle; require an explicit
   replacement for the dead exposer-transfer argument.
3. Attack **D-gap**, where the proved starvation package gives the best
   positive mechanism, then **D-near**.
4. Attack **X-gap**, whose missing theorem is a common-test transport dual,
   then **X-near**.

Every attempted proof must identify the line using (T+) or the undivided
parent height budget.  A ledger-only proof is rejected before review.
