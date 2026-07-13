# D-cap attack: the actorization/tail completion split

> **Status discipline.** Everything new in this file is proposed / `conjecture`,
> including the routine transfers whose derivations are given below. Nothing is
> promoted. All measures are on full row-point fibers in the exact signed
> picture.

## 0. Verdict first

I achieve objective **(a)**. D-cap admits a near-mechanical front end and a
five-way decomposition of its *already exhibited* D-certificate into proper
constant-mass subclasses:

\[
 \mathsf N,\qquad \mathsf G_{<4},\qquad \mathsf C_0,\qquad
 \mathsf A_{\rm esc},\qquad \mathsf T_{\rm esc}.
\]

Each realized class carries at least \(1/80\) of the original diagonal-D
coefficient measure (strictly more in the last priority cell). They mean,
respectively: near disjoint hulls; a natural gap with zero-face gauge below
four; a large-gauge zero-face barycenter collapsed below the starvation
window; failure to realize the synthetic actor displacement by any actual row;
and an actual starvation scaffold whose scalar tail exceeds the \(O(\delta)\)
cap. This is not one residual with five names: the five predicates partition
the D-mass, have fixed boundary ownership, and impose mutually exclusive extra
geometry on a constant fraction of the exhibited certificate.

Independently, the kernel-arbitrary part of the W64 score-bulk argument
transfers to D-cap by redoing its proof without invoking an I-cap shard. It
supplies one of the six top-owned overlays
\(X_{\rm gap},X_{\rm near},I_{\rm far},I_{\rm near},D_{\rm gap},D_{\rm near}\),
including the exact W64 D targets
\[
 P_v^+\{u\in U_D:g_u\ge\tau\}\ge c_m/3072
 \quad\hbox{or}\quad
 P_v^+\{u\in U_D:g_u<\tau\}>c_m/3072.
\]
The overlay is not identified with the original D-root measure.

The old rank/slab problem is sharpened as follows. The af-validated
`lem-hx-robust-scalar-starvation` is already rank-free and slab-free once one
has an actual row actor, \(A\ge4\), a \([\tau/2,2\tau]\) synthetic endpoint,
an \(O(\delta)\) residual, and an \(O(\delta)\) aggregate scalar tail. Therefore
the higher-rank “slab escape” is exactly isolated here into
\(\mathsf A_{\rm esc}\) (actorization failure) and
\(\mathsf T_{\rm esc}\) (scalar-tail escape), with the low-gauge, collapsed,
and near-gap cases retained rather than silently funneled into them.

**Hard core, in one sentence:** after robust starvation removes rank and slab, D-cap must force a synthetic zero-face displacement to become one actual \(\tau\)-scale row actor with an \(O(\delta)\) scalar tail, and the only remaining escapes are actorization, tail, low gauge, collapsed scale, or near intersection.

No creative leaf is proved below. The proposed common quantitative target for
each leaf is
\[
 Z_v(q_A)\ge {c_m\tau\over64}
       -{c_m\over16}P_v^+(\mathcal L_v),
 \qquad \mathcal L_v:=\{Q:d_Q\le\tau/4\}.              \tag{0.1}
\]
The exact T-spend then gives
\(Z_v(q_A)>7c_m\tau/960\).

## 1. The tree / the argument

### 1.1 Pinned objects and quantifier order

Adopt `context/DECOMPOSITION-W63-I.md` §§0--1.1 verbatim. Thus
\[
 b={c_m\over128},\qquad k_b={c_m^2\over8192},\qquad
 D_0=2+4\delta,
\]
\[
 \delta_{\rm rt}=\min\left\{2^{-16},(c_m/4)^2,
                         (c_mb/120)^2\right\},
 \qquad e_\delta:=2\delta(1+\delta).
\]
The pinned target is: there are universal
\(\gamma_{\rm dis}>0\) and
\(\delta_{\rm dis}\in(0,\delta_{\rm rt}]\) such that every I-base datum with
\[
 0<\delta\le\delta_{\rm dis},\qquad
 \|r_\omega-p_v\|_1<b\tau,\qquad
 \Omega(\omega)<b\tau,\qquad
 \theta<\tau/D_0,
\]
and an exhibited selected-corner certificate satisfying
\[
 M_X\le1/8,\qquad M_I<1/16,\qquad M_D>1/16
\]
obeys \(Z_v(q_A)\ge\gamma_{\rm dis}\tau\).

Fix an arbitrary datum in the pinned D-cap antecedent and its exhibited
certificate
\[
 \mathscr C^*=(\phi,h,f^*,\eta^*)\in\mathscr P(\mathfrak d),
 \quad M_X(\mathscr C^*)\le{1\over8},\quad
 M_I(\mathscr C^*)<{1\over16},\quad
 M_D(\mathscr C^*)>{1\over16}.                         \tag{1.1}
\]
It is never replaced. Put \(z=H-\phi\), and retain L0's probability
\(\lambda_A\) and its actual ownership relation
\[
 a_A:=S(1-\theta)\lambda_A\le P_v^+.                  \tag{1.2}
\]
Neither \(\lambda_A\) nor \(a_A\) is a hiddenness witness.

The construction has two independent arbitrary choices, both made before
classification:

1. Fix one legal row-point vertex kernel \(\xi\), arbitrary, for the score-bulk
   overlay.
2. For every carrier in the original D part of \(\eta^*\), fix one arbitrary
   reduced optimal display. No display is minimized or selected for a later
   property.

The tree is

```text
fixed D-certificate C*
  -> original D-root closure and zero-face geography (R0)
  -> score-good bulk (B1)
       -> arbitrary-kernel X/I/D census (B2)
       -> common top ownership (B3)
       -> exact T + same-center E packet (B4)
       -> one of six top-owned overlays (B5)
  -> original D-mass completion split (R1)
       -> N | G_<4 | C0 | A_esc | T_esc
       -> one of five proper creative leaves
```

The overlay and the original D-root split coexist but are never asserted to
overlap carrierwise.

### 1.2 R0 — original D-root closure and its exact structural cost

**(a) Pinned contract — `conj-w65-dcap-root-closure`.** Define
\[
 \eta_D^*(u):=\eta^*\{(x,u):p_x=p_u, u\hbox{ is type D}\},
 \qquad m_D^*:=\eta_D^*(1).
\]
Then
\[
 m_D^*>{1\over16},\qquad \eta_D^*\le P_{f^*}^+,       \tag{R0.1}
\]
and, with
\[
 \Pi_D^*(R):=\sum_u\eta_D^*(u)P_u^+(R),
\]
\[
 \sup_{0\le g\le1}\{\Pi_D^*(g)-P_{f^*}^+(g)\}
 \le e_\delta.                                         \tag{R0.2}
\]
The canonical receiverwise overlap
\(\widehat\Pi_D^*(\{R\})=\min\{\Pi_D^*(\{R\}),P_{f^*}^+(\{R\})\}\)
has mass \(>1/16-e_\delta\).

For every \(u\in\operatorname{supp}\eta_D^*\), fix an arbitrary reduced
optimal display and write it as
\[
 k_{T,u}+\sum_z a_{u,z}(p_z-p_u)=k_{O,u},
 \quad k_{T,u}\in K_T(u),\quad k_{O,u}\in K_O(u).      \tag{R0.3}
\]
Put
\[
 A_u:=\sum_z a_{u,z},\qquad
 q_u:=A_u^{-1}\sum_z a_{u,z}p_z,qquad
 \ell_u:=\|q_u-p_u\|_1,qquad
 g_u:=d_1(K_T(u),K_O(u)).                              \tag{R0.4}
\]
Then
\[
 A_u>0,\qquad 0<\ell_u<4\tau,\qquad
 g_u\le\|k_{T,u}-k_{O,u}\|_1=A_u\ell_u.              \tag{R0.5}
\]
Every zero-face row charged in (R0.3) has depth \(>H-8\tau\). In particular,
\[
 g_u\ge\tau\quad\Longrightarrow\quad A_u>{1\over4}. \tag{R0.6}
\]

**(b) Mechanism.** Diagonal Diracness makes \(\eta_D^*\) a full-fiber
submeasure of \(P_{f^*}^+\); one `lem-l5-positive-flow-foldback` call proves
(R0.2). `lem-positive-exposedness-margin`,
`lem-always-tight-dual-support`, and
`lem-optimal-face-conic-reduction` give (R0.3). Disjointness rules out
\(A_u=0\). `lem-zero-face-localization` gives
\(\|p_z-p_u\|_1<4\tau\), hence \(\ell_u<4\tau\), while (R0.3) gives
the equality in (R0.5). Since the depth function is 1-Lipschitz and
\(d_u>H-4\tau\), every charged \(z\) has depth \(>H-8\tau\). V separately
supplies more than \(13/16\) of the top's reduced-witness mass in \(G_v\).

**(c) Honest price.** Routine. It closes receivers only at the selected root
\(f^*\), not at \(v\), and it does not align \(\eta_D^*\), the conic
coefficients, V's witness, or \(P_v^+\). Positive evidence is the exact
constant-gauge implication (R0.6); adverse evidence is the W63 plateau, where
the D ledger is large but the entire completion is short.

**(d) Interface check.** The strict \(M_I<1/16\) boundary is retained. The
certificate and display field are fixed before every split. Conic coefficients
are geography, not transitions; no reciprocal of \(t^*(u)\) occurs.

**(e) Fallback.** Retain \(\Pi_D^*\), \(P_{f^*}^+\), their canonical overlap,
and the full joint distribution of \((g_u,A_u,\ell_u)\). Do not select a
receiver atom or average the reduced displays.

### 1.3 B1 — score-bulk transfer on the D-cap class

**(a) Pinned contract — `conj-w65-dcap-score-bulk-transfer`.** Put
\[
 s(x):={2z(p_x)\over D_0}+h(p_x),\qquad
 F:=\{x\in\operatorname{supp}\lambda_A:s(x)\le12\tau/13\}.
\]
Then
\[
 \lambda_A(F)>{1\over14},\qquad a_A(F)>{c_m\over16}.  \tag{B1}
\]

**(b) Mechanism.** The score argument uses only L0 and the fact that \(z/D_0\)
is an admissible exposer. Its mean is \(<6\tau/7\), so Markov at
\(12\tau/13\) gives the first inequality; (1.2), \(S\ge c_m\), and
\(\theta<\tau/D_0\) give the second. This is a fresh derivation on D-cap.
`lem-icap-score-bulk-production` itself is **not** invoked, because its own
hypothesis block assumes \(M_I\ge1/16\).

**(c) Honest price.** Near-mechanical. Its only likely failure is confusing
normalized web mass with top-owned mass. It says nothing about which cell has
bulk.

**(d) Interface check.** Score equality belongs to \(F\). The original
\((\phi,h)\) is retained; there is no cover, Jensen step, or new certificate.

**(e) Fallback.** For every \(L>6/7\), keep
\(\lambda_A\{s\le L\tau\}>1-6/(7L)\).

### 1.4 B2 — arbitrary-kernel bulk census

For every \(f\in F\), use the fixed \((\phi,h,\xi)\), the common corner
\(\mathcal C\), and the W56 radial block \(B(f)\), with radial equality assigned
to \(B_F\). Classify \(f\) as X, I, or D using
\[
 X:M_X>1/8;\qquad
 I:M_X\le1/8, M_I\ge1/16;\qquad
 D:M_X\le1/8, M_I<1/16.                              \tag{1.3}
\]

**(a) Pinned contract — `conj-w65-dcap-kernel-bulk-census`.** Exactly one
priority alternative holds:
\[
\begin{array}{ll}
 \mathrm{BI}:&\lambda_A(F_I)\ge1/42,\\
 \mathrm{BX}:&\lambda_A(F_I)<1/42,\quad\lambda_A(F_X)\ge1/42,\\
 \mathrm{BD}:&\lambda_A(F_I)<1/42,\quad\lambda_A(F_X)<1/42,
                       \quad\lambda_A(F_D)>1/42.
\end{array}                                             \tag{B2}
\]

**(b) Mechanism.** `lem-sl1a-corner-ledger` and
`lem-radial-horn-partition` classify every score-good root for every fixed legal
kernel. Then \(\lambda_A(F)>3/42\) gives the priority census. Again this is the
kernel-arbitrary proof behind `lem-icap-kernel-bulk-census`, redone because the
registered W64 contract is I-cap-only.

**(c) Honest price.** Routine-hard only in quantifier order. The census may
classify \(f^*\) differently and need not put bulk in D. That is information,
not a defect: it records the possible global completion surrounding a local D
root.

**(d) Interface check.** The kernel is arbitrary before inspection.
\(M_X=1/8\) stays diagonal, \(M_I=1/16\) belongs to I, and priority equality
belongs first to BI and then BX.

**(e) Fallback.** Retain all three cell weights instead of declaring a priority
cell.

### 1.5 B3 — one common receiver statistic and top ownership

Define, as in W64 but on the present class,
\[
 g_J(x):=\sum_u\xi_x(u)1_{\mathcal C}(x,u)1_J(x,u),
 \qquad J\in\{X,I,D\}.                                 \tag{1.4}
\]
For \(J=I,D\), diagonal Diracness makes \(g_J=1_{U_J}\).

**(a) Pinned contract — `conj-w65-dcap-common-ownership`.** In the routed
bulk cell,
\[
\begin{array}{c|c|c}
J&P_f^+(g_J),\ f\in F_J&P_v^+(g_J)\\ \hline
X&>1/8&>c_m/512\\
I&\ge1/16&>c_m/1536\\
D&>1/16&>c_m/1536.
\end{array}                                             \tag{B3}
\]

**(b) Mechanism.** Each selected block lies inside the common corner, so one
root-independent statistic dominates its cell mass. Restrict \(a_A\) to the
routed root set and apply `lem-l5-positive-flow-foldback` once to that same
statistic. The \(e_\delta\) arithmetic is the W64 arithmetic and is valid under
\(\delta_{\rm rt}\).

**(c) Honest price.** This supplies constant top ownership but not on the
original \(\eta_D^*\)-carriers. X retains barycentric provenance rather than
transition mass.

**(d) Interface check.** Exactly one common \(0\le g_J\le1\) is folded in the
realized case; no actor-dependent engine demands are summed.

**(e) Fallback.** Retain the sharper pre-error floors \(c_m/384\) in X and
\(c_m/768\) in I/D.

### 1.6 B4 — exact tallness spend and E at the same receiver center

Put
\[
 \mathcal L_v:=\{Q:d_Q\le\tau/4\},\qquad
 \mathcal H_v^{\rm out}:=\{Q:d_Q>\tau/4\},
\]
and use the single public receiver center \(p_{f^*}\):
\[
 \mathcal E_*:=\{R:\|p_R-p_{f^*}\|_1>1/2\}.           \tag{1.5}
\]

**(a) Pinned contract — `conj-w65-dcap-tall-same-center-packet`.** One has
\[
 P_v^+(\mathcal L_v)<\ell_T
 :=\delta+{4\tau\over63}\left(D_0+{\tau\over4}\right)
 <{2\tau\over15},                                      \tag{B4.1}
\]
every receiver on which the routed \(g_J\) is positive lies in
\(\mathcal H_v^{\rm out}\), and
\[
 P_v^+(\mathcal E_*)\ge{\tau S\over8}
                      \ge{c_m\tau\over8}.              \tag{B4.2}
\]
The exact undivided fallback is
\[
 (H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4).           \tag{B4.3}
\]

**(b) Mechanism.** `lem-ihorn-tall-halo-saturation` gives (B4.1), including
the exact strict constant. Corner deficit \(z<4\tau\) places routed receivers
in the outer halo. `lem-ihorn-universal-exterior-package` is invoked once, at
the same public center \(p_{f^*}\) used by R0's receiver closure, to get
(B4.2). This is the explicit T and E spend; no centerwise family is summed.

**(c) Honest price.** The crude subtraction
\(P_v^+(\mathcal E_*\cap\mathcal H_v^{\rm out})
\ge\tau S/8-\ell_T\) need not be positive for all \(c_m\). Thus T and E must
enter a common-test argument, not a decorative set difference. This is exactly
what the leaf target (0.1) records.

**(d) Interface check.** Equality \(d_Q=\tau/4\) is shallow; the half-ball
exterior is strict. Only one receiver center is used.

**(e) Fallback.** Keep (B4.3) and the unweakened exterior floor
\(\tau S/8\), rather than the simplified constants.

### 1.7 B5 — closed diagonal overlay and exact six-way label

In BI or BD, put \(\alpha_J=a_A|_{F_J}\), let \(\eta_f^J\) be the selected
diagonal cell measure at \(f\), and define
\[
 \beta_J(u)=\sum_f\alpha_J(f)\eta_f^J(u),\qquad
 \Pi_J(R)=\sum_u\beta_J(u)P_u^+(R).
\]

**(a) Pinned contract — `conj-w65-dcap-closed-overlay`.** For \(J=I,D\),
\[
 \beta_J(1)>c_m/768,\qquad
 \sup_{0\le g\le1}\{\Pi_J(g)-P_v^+(g)\}
       \le(2+\delta)e_\delta,                           \tag{B5.1}
\]
and the canonical overlap satisfies
\[
 \widehat\Pi_J(\mathcal H_v^{\rm out})>c_m/1024.       \tag{B5.2}
\]
The routed package receives exactly one guarded label:
\[
\begin{array}{ll}
X_{\rm gap}:&\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}\ge c_m/1024,\\
X_{\rm near}:&\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}<c_m/1024,
\quad\Xi_X\{\|p_x-p_u\|_1<b\tau\}>c_m/1024;\\[2mm]
I_{\rm far}:&P_v^+\{u\in U_I:\|p_u-p_v\|_1\ge4\tau\}\ge c_m/3072,\\
I_{\rm near}:&P_v^+\{u\in U_I:\|p_u-p_v\|_1\ge4\tau\}<c_m/3072,
\quad P_v^+\{u\in U_I:\|p_u-p_v\|_1<4\tau\}>c_m/3072;\\[2mm]
D_{\rm gap}:&P_v^+\{u\in U_D:g_u\ge\tau\}\ge c_m/3072,\\
D_{\rm near}:&P_v^+\{u\in U_D:g_u\ge\tau\}<c_m/3072,
\quad P_v^+\{u\in U_D:g_u<\tau\}>c_m/3072.
\end{array}                                             \tag{B5.3}
\]

**(b) Mechanism.** Two R2 foldbacks with the same arbitrary \(g\), first at
the roots and then at \(v\), give (B5.1). B4 removes shallow payment and gives
(B5.2). Literal two-piece mass partitions give (B5.3). These are the proofs
behind `lem-icap-closed-diagonal-flow` and
`lem-icap-priority-residual-split`, re-run on the present census; the I-cap-only
registered contracts are not silently enlarged.

**(c) Honest price.** Routine. The overlay is genuinely useful global
completion data, but identifying its D actors with the original
\(\eta_D^*\)-actors would be false. A BX or BI overlay is allowed around the
local D root.

**(d) Interface check.** The two R2 calls share one test and errors scale by
source mass, not root count. Equality belongs to X-gap, I-far, and D-gap. The
near alternatives carry the explicit failure guards mandated by W64 review.

**(e) Fallback.** Keep each full distance distribution and canonical overlap;
select no carrier atom.

### 1.8 R1 — five-way D completion split

For a carrier with \(g_u\ge\tau\), \(A_u\ge4\), and
\(\ell_u\ge\tau/2\), define a normalized endpoint and gauge by
\[
 (\widetilde q_u,\widetilde A_u)=
 \begin{cases}
   (q_u,A_u),&\ell_u\le2\tau,\\
   \left(p_u+{2\tau\over\ell_u}(q_u-p_u),
          {A_u\ell_u\over2\tau}\right),&\ell_u>2\tau.
 \end{cases}                                            \tag{1.6}
\]
Then \(\widetilde q_u\in K(P)\),
\(\tau/2\le\|\widetilde q_u-p_u\|_1\le2\tau\),
\(\widetilde A_u\ge4\), and
\[
 \widetilde A_u(\widetilde q_u-p_u)
       =A_u(q_u-p_u)=k_{O,u}-k_{T,u}.                   \tag{1.7}
\]
Let
\[
 \chi_u(x):={\operatorname{sgn}(\widetilde q_u-p_u)\cdot(x-p_u)
                  \over\|\widetilde q_u-p_u\|_1},
\]
and, with the signed fiber aggregate
\(c_{u,Q}=\sum_{j\in Q}P_{uj}\), put
\[
 \operatorname{Tail}_1(u):=
 \sum_{Q:|\chi_u(p_Q)|>1}\max(c_{u,Q},0).              \tag{1.8}
\]

Partition the support of \(\eta_D^*\) into
\[
\begin{array}{ll}
\mathsf N:&g_u<\tau;\\
\mathsf G_{<4}:&g_u\ge\tau,\ A_u<4;\\
\mathsf C_0:&g_u\ge\tau,\ A_u\ge4,\ \ell_u<\tau/2;\\
\mathsf A_{\rm esc}:&g_u\ge\tau,\ A_u\ge4,\ \ell_u\ge\tau/2,
\quad\forall f\ \|p_f-p_u+\widetilde A_u
                 (\widetilde q_u-p_u)\|_1>3\delta;\\
\mathsf T_{\rm esc}:&g_u\ge\tau,\ A_u\ge4,\ \ell_u\ge\tau/2,
\quad\exists f\ \|p_f-p_u+\widetilde A_u
                 (\widetilde q_u-p_u)\|_1\le3\delta.
\end{array}                                             \tag{1.9}
\]

**(a) Pinned contract — `conj-w65-dcap-five-way-completion-split`.** Exactly
one priority alternative is declared: the first cell in the displayed order
whose \(\eta_D^*\)-mass is at least \(1/80\); if the first four all have mass
less than \(1/80\), then
\[
 \eta_D^*(\mathsf T_{\rm esc})>{1\over80}.             \tag{R1.1}
\]
Moreover every carrier in \(\mathsf T_{\rm esc}\) satisfies
\[
 \operatorname{Tail}_1(u)>\delta.                      \tag{R1.2}
\]

**(b) Mechanism.** The five predicates partition the D support. If the first
four have mass \(<1/80\), then \(m_D^*>1/16=5/80\) forces (R1.1). For a
\(\mathsf T_{\rm esc}\) carrier, use the exhibited \(f\),
\((\widetilde A_u,\widetilde q_u)\), and \(\chi_u\) in
`lem-hx-robust-scalar-starvation` with
\[
 (K_R,L,K_C)=(3,1,1).
\]
Its explicit ceiling is \(2^{-16}\), already contained in
\(\delta_{\rm rt}\). A tail at most \(\delta\) would satisfy every hypothesis
of that proved obstruction, so (R1.2) follows. This is the exact point where
rank and slab disappear.

**(c) Honest price.** Routine once R0 is available. The split does not show
that actorization or a small tail occurs; it records their precise failure.
The W63 natural plateau supplies D mass and a natural gap but is rank three and
short. The W55 direct completion has order-one row negativity. Both support
the obstruction, but neither decides any of the five tall subclasses.

**(d) Interface check.** \(g_u=\tau\) belongs to the gap side, \(A_u=4\) to
the high-gauge side, \(\ell_u=\tau/2\) to the starvation window, and residual
equality \(3\delta\) to \(\mathsf T_{\rm esc}\). The sign functional is a
fixed clone-invariant normer, not a favorable scalar selector. The existential
row in the last cell is public data, not an inferred transition.

**(e) Fallback.** Retain the full joint distribution of
\((g_u,A_u,\ell_u,\operatorname{Tail}_1(u))\) and the complete set of actor
residuals. Do not dyadically recurse or select a best carrier.

### 1.9 The five creative leaves

Each leaf below receives the full pinned D-cap datum, R0, the realized B5
overlay, B4's T/E packet, the arbitrary display field, and its exact R1 mass
guard. Every new statement remains a conjecture.

#### N — `conj-w65-dcap-near-hulls-exclusion`

**(a) Pinned contract.** Every target datum with the priority package
\(\eta_D^*(\mathsf N)\ge1/80\) satisfies (0.1).

**(b) Mechanism.** Retain closest pairs
\((k_{T,u},k_{O,u})\) at distance \(<\tau\) as geography and use R0's
coefficient flow, the top-owned B5 overlay, and one common receiver statistic
centered at \(p_{f^*}\). The required endpoint is (0.1): the positive
\(c_m\tau/64\) term must be financed using E at \(\mathcal E_*\), while the
only permitted shallow loss is exactly
\((c_m/16)P_v^+(\mathcal L_v)\).

**(c) Honest price.** Creative-hard. Near disjoint hulls need not intersect,
and FINDINGS forbids transferring exposedness across \(4\tau\)-near rows.
Positive evidence is that a constant fraction of one actual D root now carries
the closest-pair package; adverse evidence is the possibility of many
high-dimensional almost-tangent disjoint hulls.

**(d) Interface check.** No near pair is promoted to an intersection, no
conic coefficient recurs, and no witness is averaged.

**(e) Fallback.** Make at most one fixed split at \(g_u=\tau/2\), equality on
the outer side, while retaining both pieces and all of R0/B4/B5.

#### G<4 — `conj-w65-dcap-low-gauge-gap-exclusion`

**(a) Pinned contract.** Every target datum with the guarded priority package
\(\eta_D^*(\mathsf G_{<4})\ge1/80\) satisfies (0.1).

**(b) Mechanism.** Here
\[
 A_u\ell_u\ge g_u\ge\tau,\qquad A_u<4
 \quad\Longrightarrow\quad \ell_u>\tau/4.             \tag{G.1}
\]
Thus \((p_u,q_u)\) is a genuine natural-scale synthetic pair. Apply the
transverse-moment / signed-variation / financing bank carrierwise only after
constructing one common nonnegative receiver test and one R2 foldback. Use E
at \(p_{f^*}\) to produce the main term in (0.1), then charge shallow receivers
by B4.

**(c) Honest price.** Creative-hard but better conditioned than N. The likely
death is angular incoherence of the normers \(\chi_u\): summing their individual
engine floors is illegal. The explicit norm gap (G.1) is positive evidence and
prevents freight censoring from being vacuous.

**(d) Interface check.** Synthetic endpoints are row-polytope points, not row
transitions. There is no summed pairwise demand before a common-test foldback.

**(e) Fallback.** Split once by a fixed clone-invariant common-direction
moment; retain the complementary mass without censoring it.

#### C0 — `conj-w65-dcap-collapsed-zero-cloud-exclusion`

**(a) Pinned contract.** Every target datum with the guarded priority package
\(\eta_D^*(\mathsf C_0)\ge1/80\) satisfies (0.1).

**(b) Mechanism.** The package has
\[
 A_u\ge4,\qquad \ell_u<\tau/2,\qquad A_u\ell_u\ge\tau. \tag{C0.1}
\]
Thus the zero-face barycenter collapses below the robust-starvation window only
by carrying large leverage. The target is a scale-recovery lemma: either a
positive fraction of the conic measure lies at radius at least \(\tau/2\),
reducing to the starvation window, or its cancellation produces a single
common receiver demand that, together with E and B4, proves (0.1).

**(c) Honest price.** Creative-hard. Convex cancellation can make a barycenter
small while every zero-face atom is spread, and coefficient size alone is not
transition mass. Positive evidence is the invariant product floor (C0.1);
adverse evidence is the realized unconditional alpha blow-up outside the tall
class.

**(d) Interface check.** No \(1/t^*\), alpha bound, finite directional cover,
or zero-face recurrence is asserted.

**(e) Fallback.** Publish the radial distribution of the zero-face conic
measure and split it once at radius \(\tau/2\); do not choose one atom or run a
second corner web.

#### A-esc — `conj-w65-dcap-actorization-escape-exclusion`

**(a) Pinned contract.** Every target datum with the guarded priority package
\(\eta_D^*(\mathsf A_{\rm esc})\ge1/80\) satisfies (0.1).

**(b) Mechanism.** This is the named **escaping-support actorization
completion problem**. For constant D mass, the synthetic displacement
\(k_{T,u}-k_{O,u}\) remains farther than \(3\delta\) from every actual row
displacement \(p_f-p_u\), even after the exact normalization (1.6). A proof
must use exact idempotence and the top-owned B5 overlay to show that such a
constant field of missing actors either creates a common exterior receiver at
the single center \(p_{f^*}\), or pays the B4 shallow budget, yielding (0.1).

**(c) Honest price.** This is the sharp higher-rank escape candidate. Its
refuter is a growing-rank exact factorization in which every conic actor is a
genuine convex combination at distance \(>3\delta\) from all row points while
the D ledger, tallness, ultra bounds, and row negativity remain valid. The
rank-three bounded-slab theorem and every exact plateau failure are positive
evidence against such a completion; no theorem currently forbids it.

**(d) Interface check.** The leaf states the absence of every actual actor; it
does not select a favorable minimizer, vertexize a barycenter, or interpret a
conic actor as a transition.

**(e) Fallback.** Retain the full actor-residual distribution. A weakened
theorem may assume the strictly weaker-than-starvation-completion hypothesis
that at least \(1/160\) of \(\eta_D^*\) has an actor residual at most
\(3\delta\); this removes A-esc but imposes neither rank three nor a bounded
slab.

#### T-esc — `conj-w65-dcap-scalar-tail-escape-exclusion`

**(a) Pinned contract.** Every target datum with the final priority package
\(\eta_D^*(\mathsf T_{\rm esc})>1/80\), including (R1.2), satisfies (0.1).

**(b) Mechanism.** This is the named **scalar-tail escaping-support completion
problem**. Every carrier has an actual \(3\delta\)-residual actor scaffold,
but robust starvation forces
\(\operatorname{Tail}_1(u)>\delta\). Aggregate only through one common
nonnegative test and R2; the goal is to prove that a constant family of such
tails cannot all avoid the same-center exterior mass (B4.2) while paying only
the exact shallow budget (B4.1). A legal close is precisely (0.1).

**(c) Honest price.** Creative-hard. A tail just above \(\delta\) on each
carrier is the same order as the R2 error and may rotate with \(u\), so neither
class counting nor a sum of scalar demands works. Positive evidence is that
all other robust-starvation inputs are now public and rank-free; the likely
death is a high-dimensional rotating-tail crown.

**(d) Interface check.** The tail uses positive parts of signed *fiber
aggregates*, exactly as in `lem-hx-robust-scalar-starvation`; it is not
\(P_u^+\), and it is never read probabilistically. One R2 common test is
mandatory.

**(e) Fallback.** Retain the entire tail-value distribution. A quantitative
weakened D-cap may assume
\(\operatorname{Tail}_1(u)\le K_C\delta\) on positive D mass for any fixed
universal \(K_C\); robust starvation then applies with its explicit
\(\delta_R(3,1,K_C)\). This is strictly weaker than the rank-three/bounded-slab
hypotheses of `lem-starvation-completion-obstruction`.

## 2. Assembly

Assume the routine nodes R0, B1--B5, and R1, and assume the five creative leaf
contracts. Let their ceilings be
\(\delta_N,\delta_G,\delta_{C0},\delta_A,\delta_T\), each in
\((0,\delta_{\rm rt}]\), and put
\[
 \delta_{\rm dis}:=\min\{\delta_{\rm rt},\delta_N,\delta_G,
                         \delta_{C0},\delta_A,\delta_T\},
 \qquad
 \gamma_{\rm dis}:={7c_m\over960}.                    \tag{2.1}
\]
All constants are fixed before the matrix, datum, certificate, kernel, or
reduced-display field.

Take an arbitrary pinned D-cap datum with
\(0<\delta\le\delta_{\rm dis}\), and fix its exhibited \(\mathscr C^*\).
R0 gives \(m_D^*>1/16\) and the display field. Independently fix an arbitrary
legal kernel; B1--B5 produce one of the six top-owned overlays and the exact
T/E packet. No favorable overlay is selected.

R1 gives exactly one of the five priority packages. The corresponding creative
leaf yields
\[
 Z_v(q_A)\ge {c_m\tau\over64}
 -{c_m\over16}P_v^+(\mathcal L_v).
\]
B4 now spends tallness, rather than merely citing it:
\[
 Z_v(q_A)>{c_m\tau\over64}
            -{c_m\over16}{2\tau\over15}
          ={7c_m\over960}\tau
          =\gamma_{\rm dis}\tau.                      \tag{2.2}
\]
This is the pinned D-cap conclusion. The E floor at the same center
\(p_{f^*}\) is an explicit premise of every leaf mechanism producing the first
term of (0.1); no proof that obtains that term without the B4 same-center packet
discharges the proposed leaf.

For the emptiness reading, `lem-ihorn-priced-ray-package` gives
\[
 Z_v(q_A)\le{\delta D_0\over S}\le{3\tau^2\over c_m}.
\]
Define separately
\[
 \delta_{\rm dis}^{\rm empty}:=
 \min\left\{\delta_{\rm dis},
        \left({7c_m^2\over5760}\right)^2\right\}.       \tag{2.3}
\]
Then the upper bound is at most \(\gamma_{\rm dis}\tau/2\), contradicting
(2.2). Thus the D-cap hypothesis class is empty below (2.3), conditional only
on the five creative leaf contracts.

Quantifier order is
\[
 c_m\ \longrightarrow\ (\delta_{\rm dis},\gamma_{\rm dis})
 \longrightarrow\ \mathfrak d\longrightarrow\mathscr C^*
 \longrightarrow\hbox{arbitrary kernel and arbitrary display field}
 \longrightarrow\hbox{forced labels}.
\]

## 3. Kill-list check

The table below is an interface audit, not a proof of a creative node. The
codes cover every wall in the brief and the absolute deaths in FINDINGS.

- **K1 — signed / clone / frame / paths.** Exact signed rows, full fibers, and
  row points only; no stochastic reading, raw-index path, clone count,
  coordinate-frame constant, or dimension loss.
- **K2 — dual direction / averaging.** No Jensen, W37 reversal, witness or
  \(y_c\) averaging, top-deficit lower reversal, or pointwise-to-barycenter
  promotion.
- **K3 — hiddenness / conic discipline.** No \(1/t^*\), no reduced-witness
  identification with \(P_v^+\), \(\eta\), or \(\lambda_A\), no
  \(\lambda P=p_v\), and no conic coefficient read as a transition or
  recurrence.
- **K4 — engine / R2.** Every aggregation requires one common nonnegative test
  and one R2 foldback; no summed actor-dependent demand, vanished endpoint, or
  implicit \(A=0\).
- **K5 — selectors / LP cleanup.** No favorable certificate, kernel, tie,
  minimizer, coefficient-only cleanup, max-volume rule, single-swap selector,
  finite cover, or failed-census emptiness inference.
- **K6 — tallness / centers.** B4 uses the exact T budget and E once at the
  same public center \(p_{f^*}\); no all-center floors are summed.
- **K7 — exact boundaries.** \(M_I<1/16\) stays in D-cap;
  \(M_I=1/16\) is I; \(M_X=1/8\) is diagonal; all radial, gap, gauge, window,
  residual, mass, and priority equalities are assigned.
- **K8 — freight / recursion.** No freight censoring without a norm gap, no
  second-generation web, transient deletion, max-principle far-side return,
  or lexicographic minimality.
- **K9 — FINDINGS absolute deaths.** The construction avoids legal-leak/orphan
  exclusions, broad NSC charging, unnormalized class sums, quadratic residual
  cleanup, generic spectral imports, exposer transfer across near rows,
  unconditional alpha bounds, W54 witness averaging, W55 conic recurrence,
  and all five W56 extraction deaths.
- **K10 — hypothesis honesty.** W64 I-cap shards are not consumed on D-cap.
  B1--B5 restate and derive only their kernel-arbitrary mechanisms from L0,
  the W56 corner bank, R2, T, and E.

| Node | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | K9 | K10 |
|---|---|---|---|---|---|---|---|---|---|---|
| R0 | PASS | PASS | PASS: conic geography only | PASS: one R2 | PASS: arbitrary displays | PASS via B4/leaf | PASS | PASS | PASS | PASS |
| B1 | PASS | PASS: affine mean only | PASS | PASS | PASS: fixed score | PASS via B4 | PASS: score equality in F | PASS | PASS | PASS: rederived |
| B2 | PASS | PASS | PASS | PASS | PASS: arbitrary kernel | PASS via B4 | PASS: exact cell priority | PASS | PASS | PASS: rederived |
| B3 | PASS | PASS | PASS: X is provenance | PASS: one common statistic | PASS | PASS via B4 | PASS | PASS | PASS | PASS: rederived |
| B4 | PASS | PASS | PASS | PASS | PASS | PASS: exact T and one-center E | PASS | PASS | PASS | PASS |
| B5 | PASS | PASS | PASS: flows separate from witnesses | PASS: same test in both folds | PASS | PASS: outer overlap | PASS: guarded near cells | PASS | PASS | PASS: rederived |
| R1 | PASS | PASS | PASS: no recurrence | PASS: robust call is pointwise | PASS: fixed normer, existential actor | PASS via leaf target | PASS | PASS | PASS: alpha blow-up retained as C0 | PASS |
| N | PASS | PASS: no exposer transfer | PASS | PASS: common test required | PASS | PASS: (0.1) | PASS | PASS | PASS | PASS |
| G<4 | PASS | PASS | PASS | PASS: no pairwise sum | PASS | PASS: (0.1) | PASS | PASS: explicit norm gap | PASS | PASS |
| C0 | PASS | PASS | PASS: alpha is not flow | PASS | PASS: no atom selection | PASS: (0.1) | PASS | PASS: no second web | PASS | PASS |
| A-esc | PASS | PASS | PASS: synthetic actor not vertexized | PASS | PASS: no favorable row | PASS: (0.1) | PASS | PASS | PASS: high-rank escape retained | PASS |
| T-esc | PASS | PASS | PASS | PASS: common tail test required | PASS | PASS: (0.1) | PASS | PASS | PASS: rotating tails retained | PASS |

There are no interface FAILs. The five creative rows remain mathematical gaps,
which is why every new node has conjectural status.

## 4. Dispatch order

### 4.1 Routine hostile batch

Verify in this order:

1. **R0:** diagonal full-fiber domination, the single R2 error \(e_\delta\),
   \(A_u>0\), \(\ell_u<4\tau\), and \(g_u\le A_u\ell_u\).
2. **B1:** the strict \(6\tau/7\) score mean, \(1/14\) Markov mass, and
   scaled ownership \(a_A(F)>c_m/16\).
3. **B2:** arbitrary-kernel quantifier order and exact \(1/42\) priority
   arithmetic.
4. **B3:** root-independent \(g_J\), one R2 foldback, and the three top-owned
   floors.
5. **B4:** the exact strict T constant, corner support in the outer halo, and E
   only at \(p_{f^*}\).
6. **B5:** two R2 folds with the same \(g\), the \(c_m/1024\) outer overlap,
   and all six verifier-corrected priority guards.
7. **R1:** normalization (1.6), all boundary assignments, \(5/80=1/16\), and
   the exact robust-starvation call at \((3,1,1)\).

The highest-value hostile check is that no line uses a W64 shard outside its
I-cap hypothesis block: B1--B5 must stand on the rederivations written here.

### 4.2 L3 decider shapes with exact targets

A genuine refuter sequence must consist of exact rational factorizations
\[
 P_k=L_kB_k,\qquad B_kL_k=I,
\]
with \(\tau_k\to0\), \(\delta_k=\tau_k^2\), every row negativity at most
\(\delta_k\), the full I-base/all-center hypotheses, \(H_k>16\tau_k\), the
ultra bounds, \(\theta_k<\tau_k/D_{0,k}\), and an exhibited fixed
D-certificate satisfying (1.1). It must verify the *true* ray value and
\[
 {Z_{v_k}(q_{A,k})\over\tau_k}\longrightarrow0.        \tag{4.1}
\]

Every run must print
\[
 m_D^*>1/16,\qquad
 \sup_{0\le g\le1}(\Pi_D^*(g)-P_{f^*}^+(g))\le e_\delta,
\]
\[
 P_v^+(\mathcal L_v)<\ell_T<2\tau/15,qquad
 P_v^+(\mathcal E_*)\ge\tau S/8,                      \tag{4.2}
\]
and exactly one B5 overlay, including (B5.1)--(B5.2) in BI/BD. The six exact
overlay targets are those in (B5.3); in particular D-gap and D-near must print
the \(c_m/3072\) inequalities and the near guard.

Fix the arbitrary reduced display field before measuring the five R1 cells.
The branch targets are:

1. **N:**
   \(\eta_D^*\{g_u<\tau\}\ge1/80\).
2. **G<4:** the N mass is \(<1/80\), and
   \(\eta_D^*\{g_u\ge\tau,A_u<4\}\ge1/80\).
3. **C0:** the first two masses are \(<1/80\), and
   \(\eta_D^*\{g_u\ge\tau,A_u\ge4,\ell_u<\tau/2\}\ge1/80\).
4. **A-esc:** the first three masses are \(<1/80\), and at least \(1/80\)
   lies on carriers with \(g_u\ge\tau,A_u\ge4,\ell_u\ge\tau/2\) and
   \[
    \forall f:\quad
    \|p_f-p_u+\widetilde A_u(\widetilde q_u-p_u)\|_1>3\delta.
   \]
5. **T-esc:** the first four masses are \(<1/80\), and strictly more than
   \(1/80\) lies on carriers with an \(f\) satisfying the complementary
   residual inequality and
   \(\operatorname{Tail}_1(u)>\delta\).

Every run must also print the proposed leaf deficit
\[
 \mathcal D_{\rm leaf}:=
 Z_v(q_A)-{c_m\tau\over64}
          +{c_m\over16}P_v^+(\mathcal L_v).            \tag{4.3}
\]
A proof attempt targets \(\mathcal D_{\rm leaf}\ge0\); a genuine refuter must
make it negative while satisfying its exact priority package.

The decisive A-esc refuter is a growing-rank exact completion in which
\(k_T-k_O\) stays \(>3\delta\) from every row displacement on constant D mass.
The decisive T-esc refuter has actual residual-\(3\delta\) actors but rotating
scalar tails \(>\delta\), with no common receiver test producing (4.3). Both
must remain tall; clone splitting, transient extensions, or the short W63
plateau do not qualify. The W63 diagonal plateau and W55 \(A_0=5\) completion
should be retained as unit tests: the former must route to D and fail tallness,
and the latter must reproduce its order-one finance-row negativity rather than
being mislabeled a refuter.

### 4.3 Creative order

1. Attack **A-esc** first. It is the cleanest formulation of a high-rank
   support escaping every actual actor slab.
2. Attack **T-esc** next. All robust-starvation inputs except the tail cap are
   already present, so this directly tests the rotating-tail threat.
3. Attack **G<4** with a common-test transverse-moment argument; it has the
   explicit norm gap \(\ell_u>\tau/4\).
4. Attack **C0** as a scale-recovery problem for a large-gauge collapsed
   zero-face cloud.
5. Attack **N** last. Near disjoint hulls lack both a starvation-scale gap and
   a legal exposedness-transfer theorem.

Every attempted proof must identify the exact line producing the
\(c_m\tau/64\) term from E at \(p_{f^*}\), and the exact subtraction of
\((c_m/16)P_v^+(\mathcal L_v)\) before B4 is applied. A ledger-only close does
not discharge any leaf.
