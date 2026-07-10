# W63 decomposition of the I horn — the tall isotropic return web

This is a strategy artifact only. Every new node below has proposed status
`conjecture`, including the routine nodes proved in Appendix A. Nothing is
promoted here. All statements remain in the exact signed picture and use full
row-point fibers.

## 0. Binding-gap verdict

The hard core of I is a **tall completion obstruction**, but the useful front
end is a whole-measure transport dual at the natural scale \(\tau\). It is not
an atom-to-barycenter visibility argument.

Indeed, the already proved mass dualization and top-deficit price give, for
every datum in I,
\[
  0\le Z_v(q_A)\le \frac{\nu_vD_0}{S}
  \le \frac{\delta D_0}{S}\le \frac{3\tau^2}{c_m}.       \tag{0.1}
\]
Consequently any asserted lower bound \(Z_v(q_A)\ge\gamma\tau\), after a
further universal shrink of \(\delta\), proves that the corresponding
hypothesis class is empty. I is therefore asymptotically an emptiness theorem:
an internally reproducing, top-owned, far co-top web cannot coexist with
exact idempotence and tall hidden-top geometry. This also explains why Jensen,
pointwise visibility, or an average of support functionals cannot prove I: the
owned barycenter is *forced* to be top-dually blind at order \(\delta\).

The W62 §I(b) proposal—integrate the unit transverse moments of all pairs
\((p_v,p_Q)\)—is a necessary idea but not yet a theorem. The norming scalar,
its sign unions, and its high-lever receiver set depend on \(Q\). R2 folds back
one common nonnegative receiver statistic; it does not fold a diagonal family
of actor-dependent tests. Calling the integral a “whole-measure ledger” would
hide exactly the missing transport dual.

The decomposition below repairs that problem before creative work:

1. At scale \(b\tau\), with \(b=c_m/128\), drift or scalar width supplies one
   explicit separated synthetic pair and one fixed top-owned high-lever payer.
2. If both statistics are smaller than \(b\tau\), the selected barycenter lies
   within \(\tau/32\) of \(p_v\) and is universally shadowed by every admissible
   exposer. Splitting the selected measure at the exact depth boundary
   \(H-4\tau\) gives either one SL1b shallow-rim package or one
   *scaled-top-owned* SL1a web.
3. The SL1a web is not left as a hard leaf. The hostile-verified W56 corner
   ledger routes it into the off-diagonal, intersecting-diagonal, or
   disjoint-diagonal coefficient cell. The expected high-dimensional sign-cube
   plateau is isolated in the intersecting cell; an ultra, shallow-rim-free
   completion of the W55 starvation scaffold with a disjoint extracted package
   is isolated in the disjoint cell.

Thus the second-moment/width-amplification idea is used only where it really
delivers a single weighted chord. Pure second moments are not the hard core:
the signed carré-du-champ and generic variance routes have a certified
class-count wall, and an ultra-isotropic sign cube can evade every single
scalar. The rank-three bounded-slab theorem
`lem-starvation-completion-obstruction` is strong positive evidence for the
disjoint cell, but its rank and slab hypotheses are exactly what the new cell
must remove.

Tallness is load-bearing. Besides making every \(H-4\tau\) web genuinely deep,
the only permitted height budgets imply
\[
  1-\sigma_g<\frac{4\tau}{63}\left(D_0+\frac\tau4\right),                 \tag{0.2}
\]
so almost all positive mass lies beyond the \(\tau/4\) visible-hull halo.
Every creative leaf below must use this saturation or one of the two exact
height inequalities that yields it. A proof that ignores tallness has not
explained any of the three independent refuter failures.

## 1. The tree

### 1.1 Shared notation and exact boundaries

Adopt all notation of `context/DECOMPOSITION-W62-L5.md`. An **I-base datum**
below means an L5 datum with \(0<\delta\le1/4\), \(S\ge c_m\), the pinned
definition of \(\omega\), and all of I's structural hypotheses, but with **no
reference to the as-yet-unassembled ceiling \(\delta_I\)**. Thus it includes
\[
 \forall c\in K_v^{\mathrm{loc}}:\quad
 P_v^+(E_c\cap\mathrm{Sh}_v)<\frac{\tau S}{16},\qquad
 P_v^+(E_c\cap G_v)\ge\frac{\tau S}{16},                 \tag{1.1}
\]
and the two strict parent inequalities
\(\|r_\omega-p_v\|_1<1/8\), \(\Omega(\omega)<1/16\).
Sibling C owns equality at both \(1/8\) and \(1/16\). An **ultra I-base
datum** additionally satisfies
\(\|r_\omega-p_v\|_1<b\tau\) and \(\Omega(\omega)<b\tau\).

Put
\[
 M:=M_\omega,\qquad \mu_A(Q):=m_Q/S,\qquad
 b:=\frac{c_m}{128},\qquad
 k_b:=\frac{c_mb}{64}=\frac{c_m^2}{8192}.                \tag{1.2}
\]
Then \(c_m\le S\le M\le1+\delta\). Let \(\mathcal H_v\) be the compact
polytope of admissible **row-value profiles** at \(v\), equivalently affine
exposers modulo agreement on \(K(P)\). This is sufficient because every
barycenter used below lies in \(K(P)\). Define the selected depth rim
\[
 \mathcal R_{48}:=
 \{Q\in\operatorname{supp}\mu_A:H-8\tau<d_Q\le H-4\tau\},
 \qquad \theta:=\mu_A(\mathcal R_{48}).                   \tag{1.3}
\]
The rim owns equality at \(d_Q=H-4\tau\). Its complement in the selected
support has strict depth \(d_Q>H-4\tau\).

For the underlying selected-corner construction use the registry notation
\((\phi,h,f,\xi,B,\Gamma_f)\) and \(M_X(B),M_I(B),M_D(B)\) from
`def-selected-corner`. In particular, \(X\) means \(p_x\ne p_u\), \(I\)
means diagonal with intersecting always-tight hulls, and \(D\) means diagonal
with disjoint always-tight hulls. SC later erases \(\xi\) and exposes only the
restricted pair measure. The web measure constructed below is denoted
\(\lambda_A\); it is a normalized restriction of \(\mu_A\). Only the scaled
measure \(S(1-\theta)\lambda_A\) is a submeasure of \(P_v^+\). It is never
identified with the unrelated hiddenness-witness measure customarily denoted
\(\lambda\).

The routine ceiling used in the displayed arithmetic is
\[
 \delta_{\rm rt}:=\min\left\{
  2^{-16},\left(\frac{c_m}{4}\right)^2,
  \left(\frac{c_mb}{120}\right)^2
 \right\}.                                               \tag{1.4}
\]
This ceiling is intentionally conservative; retaining the exact inequalities
in the routine nodes permits later improvement.

```mermaid
flowchart TD
    I0[I-base datum]
    P[P priced O(delta) ray]
    T[T tall halo saturation]
    V[V dual-required co-top geography]
    E[E universal exterior payer]
    DQ{drift at least b tau?}
    D[D natural-scale drift]
    WQ{width at least b tau?}
    W[W natural-scale width]
    U[U ultra-isotropic compression]
    RQ{rim mass theta at least tau/D0?}
    SH[Sh shallow rim]
    LA[scaled-top-owned SL1a web]
    SC[selected-corner package]
    XQ{M_X greater than 1/8?}
    X[X off-diagonal]
    IQ{M_I at least 1/16?}
    IC[Icap intersection diagonal]
    DC[Dcap disjoint diagonal]
    Z[Z_v(q_A) at least gamma_I tau]

    I0 --> P
    I0 --> T
    I0 --> V
    I0 --> E
    I0 --> DQ
    DQ -->|yes; equality here| D
    DQ -->|no| WQ
    WQ -->|yes; equality here| W
    WQ -->|no| U
    U --> RQ
    RQ -->|yes; equality here| SH
    RQ -->|no| LA
    LA --> SC
    SC --> XQ
    XQ -->|yes| X
    XQ -->|no; equality diagonal| IQ
    IQ -->|yes; equality here| IC
    IQ -->|no| DC
    D --> Z
    W --> Z
    SH --> Z
    X --> Z
    IC --> Z
    DC --> Z
```

### 1.2 Routine extraction nodes

All nodes in this subsection remain tagged **proposed / `conjecture`** despite
the proofs in Appendix A.

These nodes make no exclusion claim. A routine node that does not itself use
tallness can afford not to spend it because it only extracts an exact package;
T and the two pinned height budgets remain in force for every creative consumer.

#### P — `conj-w63-I-priced-ray-package`

**(a) Pinned contract.** For every I-base datum, every attained R1 minimizer
\((\Lambda,c)\) (with \(c\) absent when \(\Lambda=0\)) satisfies
\[
 0\le
 \|p_v-q_A+\Lambda(p_v-c)\|_1-\Lambda H
 =Z_v(q_A)
 \le\frac{\nu_vD_0}{S}\le\frac{\delta D_0}{S}.          \tag{P}
\]

**(b) Mechanism.** R0 turns the selected mass objective into \(SZ_v(q_A)\);
`lem-top-deficit-price` bounds that objective above by \(\nu_vD_0\); R1 supplies
the attained ray. This is the constant-complexity certificate all creative
leaves receive.

**(c) Honest price.** Routine. The only plausible failure is a quantifier or
normalization error. Its strategic sting is that a creative \(\Omega(\tau)\)
lower bound must actually exclude the completion.

**(d) Interface check.** The certificate is arbitrary among minimizers. No tie
property, favorable center, or selected coordinate is used. The top-deficit
price is used only in its proved upper direction.

**(e) Fallback.** Keep R1's finite visible multipliers rather than the aggregated
pair \((\Lambda,c)\); the value and upper price are unchanged.

#### T — `conj-w63-I-tall-halo-saturation`

**(a) Pinned contract.** Let \(\sigma_v\) be invisible positive mass and
\(\sigma_g=P_v^+\{Q:d_Q>\tau/4\}\). Every I-base datum satisfies
\[
  1-\sigma_g<\frac{4\tau}{63}\left(D_0+\frac\tau4\right).                \tag{T}
\]

**(b) Mechanism.** Combine exactly
\(H(1-\sigma_g)\le(\sigma_v-\sigma_g)\tau/4+\nu_vD_0\),
\(\sigma_v\le1+\nu_v\), \(\nu_v\le\tau^2\), and \(H>16\tau\).

**(c) Honest price.** Routine. This is the quantitative point at which all
short corank-one and cubic-height fixtures leave the class.

**(d) Interface check.** It uses one of the two permitted tallness budgets and
no surrogate height estimate. If \(1-\sigma_g\le0\), the conclusion is automatic;
otherwise the displayed division is by \(H-\tau/4>0\).

**(e) Fallback.** Retain the sharper un-divided form
\((H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4)\).

#### V — `conj-w63-I-dual-cotop-geography`

**(a) Pinned contract.** For every I-base datum and every reduced optimal
hiddenness-witness display at \(v\), its probability component \(\lambda^v\)
satisfies
\[
 \lambda^v_{\mathcal Q}(G_v):=
 \sum_{f:\,Q(f)\in G_v}\lambda^v_f>\frac{13}{16}.       \tag{V}
\]

**(b) Mechanism.** The selected mass makes the \(4\tau\)-far set nonempty;
`lem-positive-exposedness-margin` gives \(t^*(v)>0\). Apply
`lem-always-tight-dual-support`, `lem-optimal-face-conic-reduction`, and
`lem-cotop-witness-pinning` at the original top \(v\).

**(c) Honest price.** Routine. The useful output is one dual-required far
co-top geography package; it contains no coefficient information.

**(d) Interface check.** The displayed quantity is the pushforward to full
row-point fibers. \(\lambda^v\) is never identified with \(\omega\),
\(\mu_A\), or \(\lambda_A\), and no claim about \(\lambda^vP\) is made. No
reciprocal of \(t^*(v)\) appears.

**(e) Fallback.** Retain the exact pinning moment
\(\int z_y\,d\lambda^v+\sum_z a_zz_y(z)<(1/2+\delta)\tau\)
for every \(y\in Y_v\), without converting it to the \(13/16\) geography.

#### E — `conj-w63-I-universal-exterior-package`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), every I-base
datum satisfies
\[
 \forall c\in K(P),\qquad P_v^+(E_c)\ge\frac18\tau S.   \tag{E}
\]

**(b) Mechanism.** This is `lem-l5-universal-exterior-payer` (R3) applied to
the selected submeasure \(m\). The ceiling (1.4) is below
\(\min\{1/16,(c_m/8)^2\}\).

**(c) Honest price.** Routine and already proved. E has the larger floor on
the larger total exterior set, while (1.1) localizes a smaller floor to \(G_v\);
the two statements are not ordered. Both remain separate per-center facts.

**(d) Interface check.** No common exterior fiber, disjoint family of payer
sets, or centerwise sum is inferred. Creative leaves may rerun E at one actual
center or use one common bounded receiver statistic only.

**(e) Fallback.** Retain R3's exact precursor
\[
 (1+S)P_v^+(E_c)\ge
 S\left(\frac{\tau}{1+2\delta}-2\delta\right)-2\delta(1+\delta).
\]

#### ED — `conj-w63-I-drift-payer-extraction`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), if an I-base datum
satisfies \(L:=\|r_\omega-p_v\|_1\ge b\tau\), then the pair
\((a,d):=(r_\omega,p_v)\) constructs the norming functional
\[
 \chi(x):=\frac{\operatorname{sgn}(a-d)\cdot(x-d)}L,
 \quad \chi(d)=0,\quad\chi(a)=1,
 \quad \operatorname{Lip}_{\ell^1}(\chi)=\frac1L.
\]
For full row-point fibers \(R\), put
\[
 d_R:=\sum_{j\in R}(a_j-d_j),\quad
 \ell_\chi:=\sum_R|d_R|>0,\quad
 A_{\rm lev}:=(2\ell_\chi)^{-1}>0,
 \quad F_\chi:=\{R:|\chi(p_R)|>A_{\rm lev}\}.
\]
Then \(|\chi(p_R)|\le D_0/L\) on every fiber and
\[
 P_v^+(F_\chi)\ge k_b\tau.                              \tag{ED}
\]

**(b) Mechanism.** Use `lem-hx-transverse-moment-identity` to make
\(\ell_\chi>0\), set \(A_{\rm lev}=(2\ell_\chi)^{-1}>0\), use global lever
\(\Lambda=D_0/L\), apply the corrected financing floor to the distinct
synthetic pair, dominate \(r_\omega^+\) by the actual \(\omega\)-actor flow,
and invoke R2 once on the same fixed set.

**(c) Honest price.** Routine-hard constants. The likely failure is only a
factor in the foldback arithmetic. The exact precursor is recorded in
Appendix A.

**(d) Interface check.** This is not the forbidden vanishing-endpoint call:
\(L\ge b\tau>0\). The financing parameter \(A_{\rm lev}\) is explicitly positive. One
fixed receiver set is folded once; no pairwise floors are summed.

**(e) Fallback.** Retain
\((1+M)P_v^+(F_\chi)\ge M(L/(2D_0)-2\delta)-2\delta(1+\delta)\)
instead of the clean \(k_b\tau\) floor.

#### EW — `conj-w63-I-width-payer-extraction`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), if
\(\Omega(\omega)\ge b\tau\), an attaining affine scalar, its exact sign split,
and the conditional barycenters \(a:=q_+\), \(d:=q_-\) construct a distinct
synthetic pair. Put \(L:=\|a-d\|_1>0\) and define
\[
 \chi(x):=\frac{\operatorname{sgn}(a-d)\cdot(x-d)}L,
 \quad \chi(d)=0,\quad\chi(a)=1,
 \quad \operatorname{Lip}_{\ell^1}(\chi)=\frac1L,
\]
\[
 d_R:=\sum_{j\in R}(a_j-d_j),\quad
 \ell_\chi:=\sum_R|d_R|>0,\quad
 A_{\rm lev}:=(2\ell_\chi)^{-1}>0,
 \quad F_\chi:=\{R:|\chi(p_R)|>A_{\rm lev}\}.
\]
Then \(|\chi(p_R)|\le D_0/L\) on every fiber and
\[
 s_+s_-\|q_+-q_-\|_1\ge\frac12\Omega(\omega),
 \qquad P_v^+(F_\chi)\ge k_b\tau.                       \tag{EW}
\]

**(b) Mechanism.** Exact affine centering gives the weighted chord identity.
Recenter the norming functional so that \(\chi(q_-)=0\), \(\chi(q_+)=1\).
Apply the corrected financing floor to \((q_+,q_-)\), multiply by
\(Ms_+s_-\), dominate the two conditional positive parts by the actual
\(\omega\)-actor flow, and use R2 once.

**(c) Honest price.** Routine-hard. Small conditional masses are harmless only
because the separation is retained in the product \(s_+s_-\|q_+-q_-\|_1\).

**(d) Interface check.** The scalar optimizer is chosen only for its attained
value. This is an exact sign-split identity, not Jensen and not an atom selector.
The endpoints are distinct because \(\Omega>0\), and \(A_{\rm lev}>0\) is explicit.

**(e) Fallback.** Keep the weighted chord as the entire output package and split
later by \(s_+s_-\); do not infer a mass floor for either endpoint.

#### U — `conj-w63-I-ultra-compression`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), every I-base datum with
\[
 \|r_\omega-p_v\|_1<b\tau,\qquad \Omega(\omega)<b\tau
\]
has
\[
 q_A\in\mathcal U_v(S):=
 \left\{q:\|q-p_v\|_1<\frac\tau{32},\quad
       \sup_{h\in\mathcal H_v}h(q)\le\frac\delta S\right\}.             \tag{U}
\]

**(b) Mechanism.** The width definition and \(m\le\omega\) give
\(\|q_A-r_\omega\|_1\le(M/S)\Omega\). For an admissible exposer, affine row
reproduction gives \(\sum P_{vj}^+h(p_j)=\sum P_{vj}^-h(p_j)\le\nu_v\).

**(c) Honest price.** Routine. This does not promote far-atom separation to
barycenter separation; it proves the opposite, a small upper radius.

**(d) Interface check.** The supremum is over admissible exposers, not top
support functionals, and no exposers are averaged. All inequalities are on the
selected full-fiber measure.

**(e) Fallback.** Retain the exact bounds
\(\|q_A-r_\omega\|_1\le M\Omega/S\) and
\(h(q_A)\le\nu_v/S\).

#### S0 — `conj-w63-I-rim-to-SL1b-package`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), if U holds and
\(\theta\ge\tau/D_0\), then
\(\mu_{\rm sh}:=\mu_A|_{\mathcal R_{48}}\) is a subprobability measure with
\[
 \mu_{\rm sh}(1)\ge\frac\tau{D_0},\quad
 \operatorname{supp}\mu_{\rm sh}\subseteq
 \{Q:\|p_Q-p_v\|_1\ge4\tau, d_Q\le H-4\tau\},
\quad
 \int h(p_Q)\,d\mu_{\rm sh}(Q)\le\frac\tau4
 \ \forall h\in\mathcal H_v.                           \tag{S0}
\]

**(b) Mechanism.** Restrict the selected measure. Exactly
\(S\mu_{\rm sh}=m|_{\mathcal R_{48}}\le P_v^+\). U's universal shadow bound
gives the last inequality because \(\delta/S\le\tau/4\). This is exactly the
registered SL1b package, with its true scaled ownership retained.

**(c) Honest price.** Routine. Equality \(d_Q=H-4\tau\) and
\(\theta=\tau/D_0\) are both intentionally retained here.

**(d) Interface check.** The submeasure is not normalized and no row is
selected. Universal quantification in \(h\) precedes every later use.

**(e) Fallback.** Keep the stronger values \(\theta\) and \(\delta/S\) instead
of replacing them by \(\tau/D_0\) and \(\tau/4\).

#### L0 — `conj-w63-I-cotop-SL1a-package`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), if U holds and
\(\theta<\tau/D_0\), then
\[
 \lambda_A:=\frac{\mu_A|_{\{d_Q>H-4\tau\}}}{1-\theta}                   \tag{1.5}
\]
is a probability measure satisfying
\[
 \operatorname{supp}\lambda_A\subseteq
 \{Q:\|p_Q-p_v\|_1\ge4\tau, d_Q>H-4\tau\},
\quad
 \|r_{\lambda_A}-p_v\|_1<\frac{33}{28}\tau,
\quad
 \int h(p_Q)\,d\lambda_A(Q)<\frac{2}{7}\tau
 \ \forall h\in\mathcal H_v.                           \tag{L0}
\]

**(b) Mechanism.** Delete rim mass \(\theta\), paying at most \(\theta D_0<\tau\)
in barycenter displacement, and renormalize. U pays the original radius and
exposer moment. The displayed constants are stronger than SL1a's
\(11\tau/5\) and \(4\tau/13\).

**(c) Honest price.** Routine. This is the decisive compression: a completely
arbitrary selected set \(A\) becomes one scaled-top-owned SL1a probability web.

**(d) Interface check.** The exact relation is
\(S(1-\theta)\lambda_A=m|_{\{d>H-4\tau\}}\le P_v^+\); the normalized
\(\lambda_A\) itself need not be a submeasure of \(P_v^+\). It is not a
hiddenness witness and not \(\lambda P\).

**(e) Fallback.** Retain the exact conditional bounds
\((\|q_A-p_v\|_1+\theta D_0)/(1-\theta)\) and
\(\delta/(S(1-\theta))\).

#### SC — `conj-w63-I-selected-corner-extraction`

**(a) Pinned contract.** Under \(\delta\le\delta_{\rm rt}\), let
\(\mathfrak d\) be ultra with \(\theta<\tau/D_0\). Let
\(\mathscr P(\mathfrak d)\) be the family of public selected-corner
certificates produced from L0's \(\lambda_A\) by the legal choices in the W56
extraction. Each certificate is
\(\mathscr C=(\phi,h,f,\eta)\), where an auxiliary legal kernel first produces
\((B,\Gamma_f)\) and then \(\eta:=\Gamma_f|_B\); the kernel is erased. Define
\(M_X(\mathscr C),M_I(\mathscr C),M_D(\mathscr C)\) by restricting \(\eta\)
to the three registry type predicates. Then
\(\mathscr P(\mathfrak d)\ne\varnothing\), and every
\(\mathscr C\in\mathscr P(\mathfrak d)\) has \(\eta(1)\ge1/4\) and exactly one of
\[
\begin{array}{ll}
 \mathrm X:&M_X(\mathscr C)>1/8,\\
 \mathrm I:&M_X(\mathscr C)\le1/8\ \text{and}\ M_I(\mathscr C)\ge1/16,\\
 \mathrm D:&M_X(\mathscr C)\le1/8,\ M_I(\mathscr C)<1/16,
              \ \text{and}\ M_D(\mathscr C)>1/16.
\end{array}                                               \tag{SC}
\]

**(b) Mechanism.** Use `lem-sl1a-score-selector`, choose an arbitrary legal
vertex kernel, apply `lem-sl1a-corner-ledger`, then
`lem-radial-horn-partition`. The last three-way arithmetic is the proved body
of `lem-sl1a-three-cell-reduction`.

**(c) Honest price.** Routine-hard but already hostile-verified in W56. The
kernel is construction-only. The public certificate retains one coupled
measure and its clone-invariant type masses rather than claiming a
dimension-free encoding of \(\xi\).

**(d) Interface check.** The kernel may be arbitrary; no favorable
disintegration is required. Radial equality belongs to \(B_F\), \(M_X=1/8\)
belongs to the diagonal cells, and \(M_I=1/16\) belongs to I.

**(e) Fallback.** State the three registered `conj-sl1a-*-cell` contracts as
broader sufficient assumptions. The I-restricted leaves below deliberately
retain more ownership and all-center information.

This is the objective function's constant-complexity-package alternative: the
public interface contains two affine profiles, one selected row, one coupled
nonnegative measure, and three derived scalars, independent of dimension; the
kernel is not retained. A base datum may admit certificates in different cells.
The creative contracts below are stated on the original I-base datum with an
exhibited certificate as an additional quantitative hypothesis. Assembly never
chooses a favorable certificate—it fixes any one and follows its forced cell.

### 1.3 Creative leaves

Every leaf below is a new proposed `conjecture`. Each contract repeats the
whole structural I antecedent through the phrase “I-base datum”; no cell is
silently enlarged to a broader W56 class. D, W, and Sh are proper scalar/rim
subclasses. X, I\(_\cap\), and D\(_\cap\) are proper subclasses of the original
I-base class obtained by adding the ultra, rim-free, and exhibited-certificate
inequalities; their public certificate also has the constant interface above.

#### D — `conj-w63-I-natural-drift-exclusion`

**(a) Pinned contract.** There are universal \(\gamma_D>0\) and
\(\delta_D\in(0,1/4]\) such that every I-base datum with
\[
 0<\delta\le\delta_D,\qquad b\tau\le\|r_\omega-p_v\|_1<1/8
\]
satisfies \(Z_v(q_A)\ge\gamma_D\tau\).

**(b) Mechanism sketch.** Fix the arbitrary priced ray P. ED supplies one
separated pair and one fixed payer \(F_\chi\) of mass \(k_b\tau\). Use R2 only
on that receiver set, the signed-variation ledger only on its two sign unions,
and E at one actual local center. Then use T plus the two exact height inequalities to force the payer into a left-side
height deficit. The target inequality is not obtained from the financing floor
alone; tallness must rule out a nearly closed freight completion.

**(c) Honest price.** Creative-hard. Likeliest death: \(F_\chi\) is a co-top
freight set whose deficit is small for the actual ray. Evidence for the node is
that the W61 financer realizes precisely this local payment but only at
\(H=O(\tau^3)\). Evidence against a cheap close is that no banked lemma aligns
an arbitrary R1 ray with \(F_\chi\).

**(d) Interface check.** D owns equality at \(b\tau\); U/W own strict lower
drift. The R1 minimizer is arbitrary. Financing is on a quantitatively distinct
pair, never on a collapsed \((p_v,r_\omega)\).

**(e) Fallback.** Split clone-invariantly into
\(b\tau\le L<\tau/2\), \(\tau/2\le L\le2\tau\), and \(L>2\tau\).
The middle window can target `lem-hx-robust-scalar-starvation`; the other two
retain, respectively, a microdrift payer and a macroscopic pair.

#### W — `conj-w63-I-natural-width-exclusion`

**(a) Pinned contract.** There are universal \(\gamma_W>0\) and
\(\delta_W\in(0,1/4]\) such that every I-base datum with
\[
 0<\delta\le\delta_W,\qquad
 \|r_\omega-p_v\|_1<b\tau,\qquad
 b\tau\le\Omega(\omega)<1/16
\]
satisfies \(Z_v(q_A)\ge\gamma_W\tau\).

**(b) Mechanism sketch.** EW supplies one weighted chord and one fixed payer.
Fold the actual \(\omega\)-actor flow once by R2. Couple the payer to the
arbitrary ray P through a common bounded receiver statistic, compare it with E
at the same center, then use T and the
exact height budgets. This is the legitimate part of the proposed
second-moment/width-amplification route.

**(c) Honest price.** Creative-hard. A two-prong crown can make its conditional
rows finance one another while the selected barycenter stays ray-blind. The
positive evidence is that the weighted demand is \(\Omega(\tau)\) on the correct
top-owned carrier; the negative evidence is the W55 same-carrier wall.

**(d) Interface check.** W owns equality at \(\Omega=b\tau\); the parent C node
owns equality at \(1/16\). No atom mass floor, coordinate frame, or averaged
support functional occurs.

**(e) Fallback.** Split at a fixed lower bound for \(s_+s_-\). The balanced
branch has an explicitly separated pair; the unbalanced branch outputs one
small conditional mass and the same weighted chord, not a selected atom.

#### Sh — `conj-w63-I-shallow-rim-exclusion`

**(a) Pinned contract.** There are universal \(\gamma_{\rm Sh}>0\) and
\(\delta_{\rm Sh}\in(0,1/4]\) such that every I-base datum with
\[
 0<\delta\le\delta_{\rm Sh},\qquad
 \|r_\omega-p_v\|_1<b\tau,\quad \Omega(\omega)<b\tau,
 \quad\theta\ge\tau/D_0
\]
satisfies \(Z_v(q_A)\ge\gamma_{\rm Sh}\tau\).

**(b) Mechanism sketch.** S0 gives a scaled-top-owned SL1b package. Its rows are far
from \(p_v\) and shallow relative to the top, while the submeasure is shadowed
on average under *every* admissible exposer. Combine its transverse moment with
R2, P, and T. The
shallow depth supplies a fixed \(4\tau\) top-deficit lower bound; E prevents
discarding the complementary exterior payer, while tallness
must exclude the W54 counterweight's global completion.

**(c) Honest price.** Creative-hard but the cheapest of the ultra leaves. The
likeliest death is the exact constants fight: mass \(O(\tau)\) at deficit
\(O(\tau)\) costs only \(O(\delta)\), compatible with the top-deficit budget.
The known shallow counterweight is local evidence against a scalar-only proof;
no tall completion is known.

**(d) Interface check.** Sh owns both \(\theta=\tau/D_0\) and the row-depth
boundary \(d=H-4\tau\). The measure is never normalized or reduced to a point,
so no Jensen step is available.

**(e) Fallback.** Split the rim at \(d=H-6\tau\), assigning equality explicitly.
The shallower half has more top deficit; the deeper half has a narrower
completion band. The broader registered fallback is
`conj-shallow-counterweight-exclusion`.

#### X — `conj-w63-I-off-diagonal-corner-exclusion`

**(a) Pinned contract.** There are universal \(\gamma_X>0\) and
\(\delta_X\in(0,\delta_{\rm rt}]\) such that every I-base datum
\(\mathfrak d\) with
\[
 0<\delta\le\delta_X,\quad
 \|r_\omega-p_v\|_1<b\tau,\quad \Omega(\omega)<b\tau,
 \quad\theta<\tau/D_0,
\]
for which there exists an exhibited \(\mathscr C\in\mathscr P(\mathfrak d)\)
with \(M_X(\mathscr C)>1/8\),
satisfies \(Z_v(q_A)\ge\gamma_X\tau\).

**(b) Mechanism sketch.** Work with the already fixed package \(\mathscr C\). Its
off-diagonal mass is coupled coefficient--kernel mass: literal positive
coefficient flow from the selected co-top corner row \(f\) to \(x\), paired
with a geometrically distinct barycentric vertex \(u\). It is not transition
mass from \(f\) to \(u\).
Integrate transverse moments only after constructing one common receiver test;
use the signed ledger and R2 once, then feed the resulting freight cost into P
and T. E and the all-center \(G_v\)-floor remain available and must prevent a single
unconfined freight row from paying every test.

**(c) Honest price.** Creative-hard. Likeliest death: \(p_x\ne p_u\) but
\(\|p_x-p_u\|_1=o(\tau)\), so off-diagonal mass has no norm gap. The W61 thin
graft realizes that escape locally and fails only at tallness. Positive evidence
is the constant coefficient mass \(>1/8\), absent from the original I wording.

**(d) Interface check.** Strict \(M_X>1/8\) belongs here; equality belongs to
the diagonal cells. The package was arbitrary before its cell was known; no
optimization or favorable tie is used. No freight censoring is invoked.

**(e) Fallback.** Split \(M_X\) by the clone-invariant pair distance
\(\|p_x-p_u\|_1\ge b\tau\) versus \(<b\tau\). The first has an engine gap; the
second is a named near-freight/cluster-absorption package, not a censored block.

#### I\(_\cap\) — `conj-w63-I-intersection-diagonal-corner-exclusion`

**(a) Pinned contract.** There are universal \(\gamma_\cap>0\) and
\(\delta_\cap\in(0,\delta_{\rm rt}]\) such that every I-base datum
\(\mathfrak d\) with
\[
 0<\delta\le\delta_\cap,\quad
 \|r_\omega-p_v\|_1<b\tau,\quad \Omega(\omega)<b\tau,
 \quad\theta<\tau/D_0,
\]
for which there exists an exhibited \(\mathscr C\in\mathscr P(\mathfrak d)\)
with \(M_X(\mathscr C)\le1/8\) and \(M_I(\mathscr C)\ge1/16\),
satisfies \(Z_v(q_A)\ge\gamma_\cap\tau\).

**(b) Mechanism sketch.** Work with the already fixed package \(\mathscr C\).
At each diagonal type-I carrier,
`lem-optimal-face-conic-reduction` gives an alpha-free display. Keep those
displays as geography; do not average their hiddenness witnesses. The creative
task is a whole-measure transport dual on the *coefficient* measure
\(\eta|_I\): produce one common bounded receiver statistic whose
\(\Omega(\tau)\) demand contradicts R2, P, and T. V supplies a second,
dual-required co-top geography package, but it is not identified with the
coefficient measure. The original scaled-top-owned \(\lambda_A\), the
top-owned \(\omega\), E, and the all-center floor remain in the contract and are
not discarded after corner extraction.

**(c) Honest price.** Highest risk and highest information. This is where an
exact high-dimensional sign-cube plateau is expected to land: many alpha-free
carriers, a common mean near \(p_v\), and no scalar direction with large width.
The bank supplies constant diagonal mass and exact alpha-free geometry, but no
coefficient-to-witness overlap.

**(d) Interface check.** I\(_\cap\) owns equality at \(M_I=1/16\) and at
\(M_X=1/8\). The package was arbitrary before classification. Alpha-free
existence is used existentially at each carrier; no
claim is made that every reduced display is alpha-free. No \(1/t^*\) occurs.

**(e) Fallback.** On the diagonal type-I cell put
\(\eta_I(\{u\})=\eta\{(x,u):p_x=p_u,\ u\text{ type I}\}\).
Because vertex kernels are Dirac on vertex row points, \(\eta_I\le P_f^+\) is
a full-fiber submeasure. Split by the single clone-invariant statistic
\[
 \mathfrak F_I:=\sup_{0\le g\le1}
 \left\{\sum_u\eta_I(\{u\})P_u^+(g)-P_f^+(g)\right\}.
\]
R2 caps it by \(2\delta(1+\delta)\). A proposed common-test lower mechanism
must beat that cap; the strict reverse is the isolated internally closed
sign-cube completion package. This is not a second-generation web recursion.

#### D\(_\cap\) — `conj-w63-I-disjoint-diagonal-corner-exclusion`

**(a) Pinned contract.** There are universal \(\gamma_{\rm dis}>0\) and
\(\delta_{\rm dis}\in(0,\delta_{\rm rt}]\) such that every I-base datum
\(\mathfrak d\) with
\[
 0<\delta\le\delta_{\rm dis},\quad
 \|r_\omega-p_v\|_1<b\tau,\quad \Omega(\omega)<b\tau,
 \quad\theta<\tau/D_0,
\]
for which there exists an exhibited \(\mathscr C\in\mathscr P(\mathfrak d)\)
with \(M_X(\mathscr C)\le1/8\), \(M_I(\mathscr C)<1/16\), and
\(M_D(\mathscr C)>1/16\),
satisfies \(Z_v(q_A)\ge\gamma_{\rm dis}\tau\).

**(b) Mechanism sketch.** Work with the already fixed package \(\mathscr C\).
Disjoint always-tight hulls supply a strict separator
and a zero-face conic term through `lem-always-tight-dual-support` and
`lem-optimal-face-conic-reduction`. Here
`lem-positive-exposedness-margin` gives \(t^*(u)>0\), and
`lem-zero-face-localization` places the zero-face rows \(4\tau\)-near the
carrier \(u\). Because the corner ledger gives \(d_u>H-4\tau\), the
1-Lipschitz depth function places them in the \(H-8\tau\) co-top band. This is
geography only; V independently supplies the original top's far co-top
witness geography. Use the t*-free separator/corner machinery and the validated
transverse-moment/robust-starvation bank to obstruct completion. A legal use of
`lem-hx-robust-scalar-starvation` must first construct its actual row fiber,
\(A\ge4\), \(O(\delta)\) residual, and fiber-aggregate tail cap.
The final incompatibility must also use T's exact saturation and E at the same
receiver center; conic geography alone is not a tallness argument.

**(c) Honest price.** Creative-hard. The W55 \(A_0=5\) plateau is adverse local
evidence; its direct completion has order-one row negativity, and the broader
rank-three class with the theorem's pinned actor/slab hypotheses is already
impossible. The likely death is a
higher-rank support escaping that slab while recycling the same conic geography.

**(d) Interface check.** Strict \(M_I<1/16\) belongs here, and the package was
arbitrary before classification. Conic coefficients
are never interpreted as transitions, the reduced witness is never identified
with \(P_v^+\), and no constant divides by \(t^*\).

**(e) Fallback.** Let \(g_u=d_1(K_T(u),K_O(u))\). Split the D-mass at
\(g_u=\tau\), equality assigned to the large-gap cell. Large gap forces a
constant zero-face conic package; small gap outputs one near-intersection pair.
Neither branch asserts conic recurrence.

## 2. Assembly implication

Assume P, T, V, E, ED, EW, U, S0, L0, and SC, and assume the six creative leaves
D, W, Sh, X, I\(_\cap\), and D\(_\cap\) with the quantifiers above. Let their
constants be
\[
 (\gamma_D,\delta_D),\ (\gamma_W,\delta_W),\
 (\gamma_{\rm Sh},\delta_{\rm Sh}),\ (\gamma_X,\delta_X),\
 (\gamma_\cap,\delta_\cap),\
 (\gamma_{\rm dis},\delta_{\rm dis}).
\]
Set
\[
 \boxed{\gamma_I:=\min\{\gamma_D,\gamma_W,\gamma_{\rm Sh},
          \gamma_X,\gamma_\cap,\gamma_{\rm dis}\}>0}                  \tag{2.1}
\]
and
\[
 \boxed{\delta_I:=\min\left\{
  \delta_{\rm rt},\delta_D,\delta_W,\delta_{\rm Sh},\delta_X,
  \delta_\cap,\delta_{\rm dis},
  \left(\frac{\gamma_Ic_m}{6}\right)^2
 \right\}>0.}                                                         \tag{2.2}
\]
All constants are fixed before the matrix. Since \(c_m\) is the already fixed
universal branch threshold, (2.1)–(2.2) are universal.

Now quantify explicitly. Take an arbitrary exact signed idempotent \(P\), an
arbitrary hidden top \(v\), and an arbitrary target set \(A\) forming an
I-base datum with \(0<\delta\le\delta_I\). Thus the universal statements (1.1) for
**all** local centers, the strict parent drift/width inequalities, and
\(S\ge c_m\) are fixed before any support functional or corner package is
chosen.

There are exhaustive cases.

1. If \(\|r_\omega-p_v\|_1\ge b\tau\), parent strictness makes this exactly
   D's interval, including its lower equality. D gives
   \(Z_v(q_A)\ge\gamma_D\tau\ge\gamma_I\tau\).
2. Otherwise drift is strict below \(b\tau\). If
   \(\Omega(\omega)\ge b\tau\), W owns the width equality and gives the same
   conclusion with \(\gamma_W\).
3. Otherwise both statistics are strict below \(b\tau\), so U applies. Form
   \(\theta\) only now.
   - If \(\theta\ge\tau/D_0\), S0 gives the rim package and Sh owns equality,
     hence \(Z_v(q_A)\ge\gamma_{\rm Sh}\tau\).
   - If \(\theta<\tau/D_0\), L0 constructs \(\lambda_A\). SC makes
     \(\mathscr P(\mathfrak d)\) nonempty; fix any
     \(\mathscr C\in\mathscr P(\mathfrak d)\) before inspecting its cell. If
     \(M_X(\mathscr C)>1/8\), X applies. Otherwise
     \(M_X(\mathscr C)\le1/8\). If \(M_I(\mathscr C)\ge1/16\),
     I\(_\cap\) applies, including equality. In the remaining case
     \(M_I(\mathscr C)<1/16\), the partition and
     \(\eta(1)\ge1/4\) give
     \[
       M_D(\mathscr C)=\eta(1)-M_X(\mathscr C)-M_I(\mathscr C)>1/16,
     \]
     so D\(_\cap\) applies.

Thus every I-base datum at this ceiling satisfies
\[
 Z_v(q_A)\ge\gamma_I\tau.                              \tag{2.3}
\]
This is the pinned conclusion of I. Moreover P and the last ceiling in (2.2)
give
\[
 Z_v(q_A)\le\frac{3\tau^2}{c_m}\le\frac12\gamma_I\tau,
\]
so the six leaves actually make the I antecedent empty below this ceiling.
This is not used to change the target; it records the true completion content.

Finally, \(Y_v\) is compact. Only after all data, all-center hypotheses, and
the case are fixed, choose one maximizer
\(y\in Y_v\) with \(y\cdot(p_v-q_A)=Z_v(q_A)\). No \(y_c\) is ever selected,
and no family of witnesses is averaged.

## 3. Kill-list and adverse-calibration checks

### 3.1 Exact fixture routing, node by node

Abbreviate the exact fixtures by **Sp** (heavy simplex spike), **Fan** (growing
simplex fan), **W61** (thin graft and dyadic financer), and **W55**
(\(A_0=5\) plateau). “Parent” means that the fixture is excluded before the
node is invoked, not that the node proves its exclusion.

| Node | Sp | Fan | W61 | W55 |
|---|---|---|---|---|
| P | Its exact \(Z=2\delta\) passes the price, but \(H=2\delta\) fails I. | Same: true ray value \(2\delta\), but parent tallness/width fail. | The priced ray is compatible with the local seeds; parent tallness fails. | Canonical completion is outside small \(\delta\); only the theorem's pinned rank-three/slab class is already impossible. |
| T | Excluded: \(H=2\tau^2<16\tau\); its nominal “deep” rows have \(d=0\) only because \(H-8\tau<0\). | Same exact tallness failure. | Both families have \(H=O(\tau^3)\), the gate T is designed to spend. | Direct completion fails all-row negativity before T; an unrestricted completion could enter any of D/W/Sh/X/I/D. |
| V | Its hiddenness witness exists, but its \(G_v\) geography is only nominal because the fixture is short; parent tallness fails. | Same, and parent width fails independently. | The seed witnesses are exact geography only; parent tallness fails. | A genuine completion must pass V, but V is never treated as top-coefficient overlap. |
| E | The simplex family satisfies a strong exterior floor, showing E alone does not buy tallness. | Likewise passes the all-center floor strongly; parent height/width fail. | The local financer can pay E but fails height. | A genuine completion must pass E; the direct matrix already fails negativity. |
| ED | Drift is \(2\delta<b\tau\) eventually, and parent width/tallness fail. | Same. | A local payer exists, but no tall I-base datum exists. | Its natural scalar scaffold motivates ED's robust-starvation fallback. |
| EW | Exact \(\Omega\to3/4>1/16\), so parent I excludes it. | Exact \(\Omega=(3+4\delta)/(4(1+\delta)^2)\to3/4\), independent of fan size. | No tall I-base datum; the financer warns that payer extraction alone is insufficient. | The two-prong/scaffold geometry is routed here only if it first meets I's width gate. |
| U | Not reached: exact width exceeds \(1/16\), and tallness fails. | Not reached for the same two independent gates. | Not reached because tallness fails. | A genuine low-width completion would enter U; the tested direct one fails negativity. |
| S0 | Not reached. Counterfactually the simplex actors have \(d=0\), impossible in a tall rim. | Not reached; same observation. | Not reached; cubic height. | Only a W55 completion satisfying the theorem's pinned rank-three/slab hypotheses is already blocked; a generic shallow escape is not. |
| L0 | Not reached; the short fixture's co-top label is vacuous. | Not reached; parent width and height fail. | Not reached; parent height fails. | Only a completion with both ultra diagnostics and \(\theta<\tau/D_0\) produces L0's scaled-top-owned SL1a web. |
| SC | Not reached. | Not reached. | Not reached. | Only an ultra completion with \(\theta<\tau/D_0\) reaches SC; then an arbitrary fixed package is routed X/I/D. |
| D | Counterfactual drift is below this branch; actual fixture fails parent height/width. | Same. | Handles the natural-scale version of the W61 financer; the tested one is excluded by height. | Handles only a completed natural-drift variant. |
| W | Parent \(\Omega<1/16\) excludes it. | Parent \(\Omega<1/16\) independently excludes every tested \(m\). | Handles a scale-matched two-prong financer; tested seeds fail height. | Handles a low-width-but-\(\tau\)-anisotropic completion, not the pinned rank-three failure. |
| Sh | Tallness excludes the simplex shapes before their \(d=0\) rows can masquerade as rim rows. | Same. | The local shallow financer is assigned here only after a tall completion. | A shallow completion outside the theorem's pinned class is Sh's adverse target; no generic block is claimed. |
| X | No fixture reaches SC. | No fixture reaches SC. | This is the intended home of an off-diagonal freight completion; current graft/financer fail tallness. | A slab-escape completion with genuine off-diagonal freight routes here. |
| I\(_\cap\) | No fixture reaches SC. | A genuinely low-width high-dimensional fan is routed here when its diagonal carriers are alpha-free; the tested fan fails width and height. | No tested seed enters. | Not the canonical disjoint plateau; it owns the sign-cube/dual-simplex threat. |
| D\(_\cap\) | No fixture reaches SC. | No tested fan enters. | A disjoint freight completion would enter only after tallness. | Conditional home only if a completion is ultra, has \(\theta<\tau/D_0\), and its fixed SC package is disjoint; the direct matrix fails negativity and the pinned rank-three/slab class is impossible. |

All displayed blockers are exact: for Sp/Fan, \(H=Z=2\delta\), drift
\(=2\delta\), and \(\Omega\to3/4\); the W61 heights are cubic; the direct W55
finance row has negative mass about \(5\), not \(\tau^2\). Clone splitting
changes none of these full-fiber quantities.

### 3.2 Wall codes

The following codes cover every hard wall in the brief and the complete
DEAD-ROUTE/WALL index of context/FINDINGS.md.

- **K1 — signed/clone/frame:** full-fiber quantities only; no stochastic
  interpretation, raw-index path floor, coordinate frame, class count, or
  dimension-dependent constant.
- **K2 — dual direction:** top-deficit price is upper-only; no Jensen, no
  pointwise-to-barycenter promotion, no witness or \(y_c\) averaging, and no
  reversal of the W37 circuit inequality.
- **K3 — hiddenness geography:** no \(1/t^*\); reduced witnesses and conic
  coefficients are geography only; no identification with \(P_v^+\) or
  \(\lambda P=p_v\).
- **K4 — engine allocation:** financing uses distinct endpoints and explicit
  \(A_{\rm lev}>0\); no call on collapsed \((p_v,r_\omega)\); no sum of pairwise demands
  without one R2 foldback on a common nonnegative test.
- **K5 — selection/LP:** arbitrary R1 minimizer and arbitrary legal kernel;
  no favorable tie, exact-max-volume selector, coefficient-only cleanup,
  finite cover, generic spectral import, or Gamma-only/class-count argument.
- **K6 — tallness/centers:** only the two pinned height budgets are used; R3
  and (1.1) remain per-center and are never summed over centers.
- **K7 — W55/W56:** no conic recurrence or thin/thick transition fiction; no
  lexicographic minimality, freight censoring without a norm gap,
  second-generation recursion, transient-row deletion, or max-principle
  far-side return.
- **K8 — boundaries/quantifiers:** all strict/equality ownership is explicit;
  the all-center antecedent precedes every package and the single final \(y\).

The promised complete crosswalk is:

| Brief/FINDINGS wall or death certificate | Audit code |
|---|---|
| Signed picture, full fibers, clone invariance, frame-free constants; raw-index path products and cloning | K1 |
| No \(1/t^*\); reduced witness is geography; \(\lambda P\ne p_v\); no coefficient overlap | K3 |
| Vanished-endpoint financing; corrected \(A_{\rm lev}>0\); W37 dual-direction wall | K2, K4 |
| Witness/\(y_c\) averaging, Jensen, W53 affine-pairing blind spot, W54 simplex/cylinder averaging | K2 |
| R1 argmin/tie misuse, legal-leak absorption, orphan exclusion/financing, and external-source-only payment | K4, K5 |
| Exact-max-volume, pointwise, \(\sigma\)-only, and single-swap selectors | K5 |
| Pairwise engine sums without R2; R3 per-center quantifier | K4, K6 |
| Rule-13 raw paths, universal-\(C\), canonical-\(g\), literal-\(\psi\), and finite-corner routes | K1, K2, K5 |
| Fixed-chart beta-LP, naive chart averaging, unnormalized chart sums, and dimension-free class-count routes | K1, K5 |
| Coefficient-only LP cleanup, broad NSC charging, \(\Gamma\)-emptiness, and arm-A additive-master bookkeeping | K5 |
| E2 quadratic residuals, W20 failed-census emptiness, generic spectral/error-bound imports | K5 |
| No-free-frontier/W18/W19 class packing and poke-charge wall; W30 anchor-production gap | K1, K5 |
| W37/W38 circuit reversal, W40 LP-only alpha bounds, W49/W50 tightness/spectral wall | K2, K3, K5 |
| W49F empty certified tall class: absence of fixtures is evidence only | K6 |
| W53 upper-only deficit price and rho-near blind spot | K2, K6 |
| W54 witness averaging and \(t^*\)-free discipline | K2, K3 |
| W55 \(\lambda P\), conic recurrence, thin/thick, and same-carrier completion wall | K3, K7 |
| W56 one-hard-leaf, lexicographic minimality, freight censoring, second-generation recursion, and max-principle far-side return | K7 |
| Strict/equality ownership and all-centers-before-one-\(y\) quantifiers | K8 |

This is the exhaustive Rule-13/FINDINGS crosswalk; the per-node table below
audits every row through its assigned code. Every node receives a verdict for
every code; the combined “K2 and K3”
column means an independent PASS for each code. “PASS” is an interface verdict,
not a proof of a creative node.

| Node | K1 | K2 and K3 | K4 | K5 | K6 | K7 | K8 |
|---|---|---|---|---|---|---|---|
| P | **PASS:** hull/fiber scalars. | **PASS:** upper price only; no witness use. | **PASS:** no engine call. | **PASS:** every attained ray works. | **PASS:** no center sum. | **PASS:** no recurrence/preprocessing. | **PASS:** ray chosen after the datum. |
| T | **PASS:** positive full-fiber mass. | **PASS:** no dual selector. | **PASS:** no engine. | **PASS:** scalar algebra only. | **PASS:** exact halo budget and strict \(H>16\tau\). | **PASS:** none invoked. | **PASS:** strict height owns strict output. |
| V | **PASS:** row-point witness geography. | **PASS:** pinning is upper/geographic only. | **PASS:** no engine call. | **PASS:** every reduced display is allowed. | **PASS:** no center sum. | **PASS:** no conic recurrence. | **PASS:** witness chosen after the datum. |
| E | **PASS:** full-fiber exterior mass. | **PASS:** no dual promotion. | **PASS:** R3 already contains one legal R2 foldback. | **PASS:** no center selector. | **PASS:** per-center only, never summed. | **PASS:** no recurrence/path. | **PASS:** universal center precedes later packages. |
| ED | **PASS:** synthetic hull pair, full-fiber \(F\). | **PASS:** no top-witness averaging. | **PASS:** \(L\ge b\tau\), \(A_{\rm lev}>0\), one R2. | **PASS:** normer only, no favorable ray. | **PASS:** creative consumer must spend T. | **PASS:** no censoring or paths. | **PASS:** drift equality owned by D. |
| EW | **PASS:** affine scalar and fiber flow. | **PASS:** exact sign identity, not Jensen. | **PASS:** distinct pair, \(A_{\rm lev}>0\), one R2. | **PASS:** attained width value only. | **PASS:** no center aggregation. | **PASS:** no class/Gamma recursion. | **PASS:** width equality explicit. |
| U | **PASS:** selected quotient measure. | **PASS:** upper radius and affine equality only. | **PASS:** no financing call. | **PASS:** no atom selector. | **PASS:** retains all I centers/tallness. | **PASS:** no preprocessing. | **PASS:** both lower inequalities strict. |
| S0 | **PASS:** \(S\mu_{\rm sh}\le P_v^+\) exactly. | **PASS:** universal shadow, no averaged witness. | **PASS:** no pairwise sum. | **PASS:** no selected row. | **PASS:** height enters via the exact rim. | **PASS:** no shallow recursion. | **PASS:** both equalities assigned to rim. |
| L0 | **PASS:** only \(S(1-\theta)\lambda_A\le P_v^+\). | **PASS:** no separation promotion. | **PASS:** no engine yet. | **PASS:** no witness/coefficients identified. | **PASS:** strict \(H-4\tau\) support. | **PASS:** no cover or recurrence. | **PASS:** strict rim complement. |
| SC | **PASS:** kernel on row points, fiber coefficients. | **PASS:** one score selector, no witness average. | **PASS:** no summed engine demand. | **PASS:** arbitrary legal kernel. | **PASS:** top remains tall/co-top. | **PASS:** W56 dead mechanisms removed. | **PASS:** radial/X/I boundaries exact. |
| D | **PASS:** one fixed fiber set. | **PASS:** arbitrary ray; no W37 reversal. | **PASS:** ED distinct pair and one foldback. | **PASS:** no favorable minimizer. | **PASS:** T is mandatory; centers unsummed. | **PASS:** no freight censor. | **PASS:** lower drift equality here. |
| W | **PASS:** weighted chord is clone-safe. | **PASS:** no Jensen or \(y\)-averaging. | **PASS:** EW pays once. | **PASS:** no atom/tie selector. | **PASS:** exact tallness required. | **PASS:** no Gamma/class recursion. | **PASS:** lower width equality here. |
| Sh | **PASS:** full-fiber subprobability. | **PASS:** upper shadow plus depth, no promotion. | **PASS:** any future integration must use R2. | **PASS:** no row selector/cover. | **PASS:** completion must spend T. | **PASS:** no second web. | **PASS:** rim/depth equality here. |
| X | **PASS:** coupled fiber-kernel mass. | **PASS:** no witness averaging or reverse dual. | **PASS:** common receiver test required. | **PASS:** arbitrary kernel; no censoring. | **PASS:** all-center floor retained. | **PASS:** near freight is a fallback cell, not deletion. | **PASS:** strict \(M_X>1/8\). |
| I\(_\cap\) | **PASS:** diagonal carrier measure. | **PASS:** displays stay separate; no witness average. | **PASS:** target is one common \(g\), then R2. | **PASS:** no class count/finite cover. | **PASS:** T and centers retained. | **PASS:** no recursive web. | **PASS:** both mass equalities owned here. |
| D\(_\cap\) | **PASS:** gap/conic geography is clone-safe. | **PASS:** no \(\lambda P\), no W37 reverse. | **PASS:** robust starvation only after all legal inputs. | **PASS:** no favorable display or LP cleanup. | **PASS:** tall completion is the target. | **PASS:** conic recurrence explicitly forbidden. | **PASS:** strict \(M_I<1/16\). |

## 4. Recommended dispatch order

1. **Routine hostile batch first.** Verify P, T, V, E, ED, EW, U, S0, and L0 from
   Appendix A, in that order. Then re-run SC against the already extracted W56
   shards, checking the exact \(1/4,1/8,1/16\) boundaries and an arbitrary
   legal kernel. The most valuable algebra checks are ED/EW's one-R2 foldback
   and U's partial-fiber inequality. Clone-split every test.

2. **Cheap exact L3 deciders before creative proofs.** A genuine refuter family
   must have \(P^2=P\), row sums one, \(\delta_k\to0\), nonempty \(W\), a hidden
   top with \(H>16\tau\), the full I all-center inequalities, and
   \(Z_v(q_A)/\tau\to0\).

   - **Natural-drift completion (D):** require
     \(b\tau\le\|r_\omega-p_v\|_1<1/8\), \(\Omega<1/16\), and test whether the
     ED payer can remain co-top for the actual R1 ray.
   - **Natural-width bouquet (W):** require drift \(<b\tau\) and
     \(b\tau\le\Omega<1/16\); record the exact weighted chord and whether one
     common receiver pays it. The old fan is not a candidate because its width
     tends to \(3/4\).
   - **Tall shallow counterweight (Sh):** force
     \(\theta\ge\tau/D_0\) and sweep \(H/\tau\downarrow16\), preserving
     universal exposer shadow and all-row negativity.
   - **Off-diagonal freight family (X):** target
     \(M_X>1/8\) and separately measure the mass at
     \(\|p_x-p_u\|\ge b\tau\). This is the exact tall completion of the W61
     graft/financer to try.
   - **Ultra sign cube (I\(_\cap\)):** require both statistics \(<b\tau\),
     \(\theta<\tau/D_0\), and an extracted corner with
     \(M_X\le1/8,M_I\ge1/16\). This is the decisive high-dimensional plateau
     search; compute the true R1 value, not pointwise deficits.
   - **High-rank slab escape (D\(_\cap\)):** start from W55
     \(A_0=5,g=5\tau\), but require all row negativities \(\le\tau^2\),
     \(H>16\tau\), and support outside the proved rank-three slab. Record the
     distribution of \(g_u/\tau\).

3. **Creative dispatch last, highest information first.** Attack
   I\(_\cap\) first: either a refuter realizes the predicted sign cube or a
   common-test transport theorem closes the principal threat. Next attack
   D\(_\cap\), because the bounded-slab theorem and robust-starvation bank give
   the strongest positive mechanism. Then X, Sh, W, and D. For every proof
   attempt require an explicit line showing where (T), or one of its two exact
   parent height inequalities, is consumed. A ledger-only proof is rejected
   before review.

## Appendix A. Routine proofs (nodes remain proposed)

### A.1 P, T, V, and E

For fixed \(y\in Y_v\), R0's affine identity gives
\[
 S\,y\cdot(p_v-q_A)=\sum_Qm_Qz_y(Q)
 \le\sum_QP_v^+(\{Q\})z_y(Q)\le\nu_vD_0.
\]
Take the supremum over the same compact \(Y_v\), then invoke R1. This proves P.

For T, \(\sigma_v-\sigma_g=(\sigma_v-1)+(1-\sigma_g)\le
\nu_v+(1-\sigma_g)\). Insert this in the exact halo inequality:
\[
 (H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4).
\]
If \(1-\sigma_g\le0\), T is immediate. Otherwise \(H>16\tau\) and
\(\nu_v\le\tau^2\) give (T).

For V, \(S>0\) supplies a nonempty far set at \(v\), so
`lem-positive-exposedness-margin` gives \(t^*(v)>0\). Reduced optimal displays
exist by the banked optimal-face reduction. The \(c=4\), \(\delta\le1/4\)
case of `lem-cotop-witness-pinning` gives
\(\lambda^v_{\mathcal Q}(G_v)>1-(1/2+\delta)/4\ge13/16\), with strictness inherited from
the pinning lemma. This proves V.

Finally, \(m\le P_v^+\) has mass \(S\ge c_m\) and is supported on
\(4\tau\)-far fibers. Since \(\delta_{\rm rt}\le
\min\{1/16,(c_m/8)^2\}\), `lem-l5-universal-exterior-payer` applies verbatim
and proves E.

### A.2 ED

Let \(a=r_\omega\), \(d=p_v\), and \(L=\|a-d\|_1\ge b\tau\). A norming sign
vector \(s=\operatorname{sgn}(a-d)\) gives
\(\chi(x)=s\cdot(x-d)/L\), so \(\chi(d)=0\), \(\chi(a)=1\), and \(\chi\)
has Lipschitz constant \(1/L\). Put
\[
 \ell_\chi=\sum_R\left|\sum_{j\in R}(a_j-d_j)\right|,\quad
 A_{\rm lev}=(2\ell_\chi)^{-1}>0,\quad \Lambda=D_0/L,
\]
and \(F_\chi=\{R:|\chi(p_R)|>A_{\rm lev}\}\). The transverse moment makes
\(\ell_\chi>0\), and the global row diameter gives \(|\chi(p_R)|\le\Lambda\).
The financing floor yields
\[
 a^+(F_\chi)+P_v^+(F_\chi)\ge L/(2D_0)-2\delta.          \tag{A.1}
\]
Convexity of positive parts and R2 give
\[
 M a^+(F_\chi)\le\sum_Q\omega_QP_Q^+(F_\chi)
 \le P_v^+(F_\chi)+2\delta(1+\delta).                  \tag{A.2}
\]
Writing \(V=P_v^+(F_\chi)\), multiply (A.1) by \(M\) and use (A.2):
\[
 (1+M)V\ge M(L/(2D_0)-2\delta)-2\delta(1+\delta).      \tag{A.3}
\]
Since \(M\ge c_m\), \(M\le1+\delta\), \(D_0\le3\), and
\(\tau\le c_mb/120\), the right side is at least
\(c_mb\tau/8\), while \(1+M\le9/4\). Thus
\(V\ge c_mb\tau/18>k_b\tau\), proving ED.

### A.3 EW

Choose an attaining affine 1-Lipschitz scalar \(\ell\), subtract
\(\ell(r_\omega)\), and put
\(Q_+=\{Q:\ell(p_Q)-\ell(r_\omega)\ge0\}\) and
\(Q_-=\{Q:\ell(p_Q)-\ell(r_\omega)<0\}\), assigning all zero values to
\(Q_+\). Let their masses and barycenters be \(s_+,q_+\) and \(s_-,q_-\).
Then \(s_+,s_->0\), \(s_++s_-=1\). Exact centering gives
\[
 s_+s_-\bigl(\ell(q_+)-\ell(q_-)\bigr)=\frac12\Omega(\omega),
\]
so the first inequality in EW follows by Lipschitzness. Apply the same
financing construction as in A.2 to \((q_+,q_-)\), whose distance is \(L>0\),
with its norming functional recentered to be zero at \(q_-\).
After multiplying by \(Ms_+s_-\), positive-part subadditivity gives
\[
 Ms_+s_-\{q_+^+(F_\chi)+q_-^+(F_\chi)\}
 \le\sum_Q\omega_QP_Q^+(F_\chi).
\]
R2 therefore implies
\[
 P_v^+(F_\chi)\ge
 \frac{M\Omega(\omega)}{4D_0}
 -2M\delta s_+s_- -2\delta(1+\delta).                  \tag{A.4}
\]
Using \(M\ge c_m\), \(D_0\le3\), \(s_+s_-\le1/4\), and the ceiling in
(1.4), the right side exceeds \(c_mb\tau/64=k_b\tau\). This proves EW.

### A.4 U

For every \(u\) with \(\|u\|_\infty\le1\),
\[
 \left|u\cdot(q_A-r_\omega)\right|
 \le\frac1S\sum_Qm_Q|u\cdot(p_Q-r_\omega)|
 \le\frac{M}{S}\Omega(\omega).
\]
Take the supremum in \(u\) and add the drift. Since
\(b=c_m/128\), \(S\ge c_m\), and \(M\le5/4\),
\[
 \|q_A-p_v\|_1
 <b\tau\left(1+\frac{5}{4c_m}\right)
 \le\frac9{512}\tau<\frac\tau{32}.                   \tag{A.5}
\]
For \(h\in\mathcal H_v\), affine reproduction and \(h(p_v)=0\) give
\[
 \sum_jP_{vj}^+h(p_j)=\sum_jP_{vj}^-h(p_j)\le\nu_v.
\]
Restrict the left side to \(m\), divide by \(S\), and use affinity at the
barycenter. This proves U. No atom separation is inferred.

### A.5 S0 and L0

If \(\theta\ge\tau/D_0\), the support and mass clauses of S0 are definitions.
For every exposer,
\[
 \int h\,d\mu_{\rm sh}\le h(q_A)\le\delta/S
 \le\tau^2/c_m\le\tau/4,
\]
using \(\tau\le c_m/4\). This proves S0.

If \(\theta<\tau/D_0\), L0's support and normalization are immediate. Let
\(r_{\rm rim}\) denote the unnormalized rim moment. Then
\[
 \|r_{\lambda_A}-p_v\|_1
 \le\frac{\|q_A-p_v\|_1+\theta D_0}{1-\theta}
 <\frac{\tau/32+\tau}{1-\tau/D_0}
 \le\frac{33}{28}\tau,                                \tag{A.6}
\]
because \(\tau\le1/4\) and \(D_0\ge2\). Likewise
\[
 \int h\,d\lambda_A
 \le\frac{\delta}{S(1-\theta)}
 <\frac{\tau^2}{c_m(1-\tau/D_0)}
 \le\frac27\tau.                                      \tag{A.7}
\]
This proves L0 and, in particular, the weaker registered SL1a constants.

### A.6 SC

L0 implies the hypotheses of `lem-sl1a-score-selector`. Choose any top support
functional and any relative-interior optimal exposer; the score selector gives
one support row \(f\). For any legal row-point vertex kernel,
`lem-sl1a-corner-ledger` gives \(\Gamma_f(C_f)>1/2\), and
`lem-radial-horn-partition` gives a block \(B\in\{B_F,B_N\}\) with
\(\Gamma_f(B)\ge1/4\). Push this construction to the public certificate
\(\eta=\Gamma_f|_B\) and erase the kernel. The three masses partition \(\eta\).
If \(M_X>1/8\), X holds. Otherwise \(M_X\le1/8\); if
\(M_I\ge1/16\), I holds, while if
\(M_I<1/16\),
\[
 M_D=\eta(1)-M_X-M_I>1/4-1/8-1/16=1/16.
\]
This proves SC with all equality boundaries as stated.
