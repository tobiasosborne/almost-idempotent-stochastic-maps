# Appendix: routine proofs for the D-cap batch

Everything in this appendix remains proposed / `conjecture`.  Nothing is
promoted.  We use the exact signed picture, aggregate on full row-point fibers,
and adopt the notation and boundary conventions of
`context/DECOMPOSITION-W63-I.md` §§0--1.1 and `DCAP-ATTACK.md` §1.1.  Thus

\[
 \tau=\sqrt\delta,
 \quad b={c_m\over128},
 \quad D_0=2+4\delta,
 \quad e_\delta=2\delta(1+\delta),
\]
\[
 \delta_{\rm rt}=\min\left\{2^{-16},(c_m/4)^2,
                    (c_mb/120)^2\right\},
 \qquad a_A=S(1-\theta)\lambda_A\le P_v^+.
\]
In particular
\[
 \tau\le {1\over256},\qquad \nu_x\le\delta
 \quad\hbox{for every row }x,qquad
 P_x^+(1)=1+\nu_x\le1+\delta.                         \tag{A.0}
\]
The fixed datum is the pinned D-cap datum and the fixed certificate is always
\(\mathscr C^*=(\phi,h,f^*,\eta^*)\); neither is replaced.  No
`lem-icap-*` shard is consumed anywhere below.

## R0 — `conj-w65-dcap-root-closure`

### Pinned contract (verbatim)

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

### Exact registry shards consumed and hypothesis audit

- `argument/lem-l5-positive-flow-foldback.md`.  Its hypotheses are checked as
  follows: \(P\) is the fixed finite exact signed idempotent; the row is
  \(f^*\); the diagonal measure \(\eta_D^*\) is nonnegative and is a
  full-fiber submeasure of \(P_{f^*}^+\), as proved below; the test is an
  arbitrary common \(g\colon\{\text{fibers}\}\to[0,1]\), so its parameter is
  \(M=1\).
- `argument/lem-positive-exposedness-margin.md`.  A carrier \(u\) is a hidden
  geometrically distinct row vertex because it is a diagonal I/D corner
  vertex.  Here \(\delta>0\), hence \(\rho=4\tau>0\); its type-D actor hulls
  are defined only with the nonempty far-tight family, so the far set is
  nonempty.  Thus \(t^*(u)>0\).
- `argument/lem-always-tight-dual-support.md`.  The same \(P,u\) satisfy:
  exact signed idempotence, \(\delta>0\), nonempty visible set, and hidden
  geometrically distinct vertex.  We use reduced witnesses, exactly as the
  shard requires after redundant centered-zero constraints are deleted.
- `argument/lem-optimal-face-conic-reduction.md`.  The preceding margin gives
  \(t^*(u)>0\); \(u\) is hidden and geometrically distinct; the display is
  reduced.  Hence its far and upper-box terms are points of \(K_T(u)\) and
  \(K_O(u)\), and its remaining coefficients are nonnegative and supported on
  the always-tight zero face.
- `argument/lem-zero-face-localization.md`.  For each charged \(z\), \(P\) is
  exact and \(u\) is a hidden geometrically distinct row vertex; the charged
  row is in the zero face of an optimal exposer.  Therefore
  \(\|p_z-p_u\|_1<4\tau\).  We use only this first, center-free conclusion.

These are the only registry shards consumed in R0.

### Proof

The selected block has mass at least \(1/4\), and its X, I, D cells partition
it.  For the fixed D certificate,
\(M_X\le1/8\), \(M_I<1/16\), so
\[
 m_D^*\ge {1\over4}-M_X-M_I
 >{1\over4}-{1\over8}-{1\over16}={1\over16}.          \tag{R0.7}
\]
On the diagonal cell \(p_x=p_u\), and \(u\) is a row vertex.  A legal vertex
kernel is Dirac at a vertex, including its whole clone fiber.  Consequently
the \(u\)-mass of this restriction is part of the full positive coefficient
fiber of row \(f^*\):
\[
 0\le \eta_D^*(u)\le P_{f^*}^+(\{u\}).                \tag{R0.8}
\]
This proves (R0.1).

Apply `lem-l5-positive-flow-foldback` once to
\(m=\eta_D^*\), at row \(f^*\), with an arbitrary \(0\le g\le1\).  It gives
\[
 \sum_u\eta_D^*(u)P_u^+(g)
 \le P_{f^*}^+(g)+2\delta(1+\delta),                  \tag{R0.9}
\]
which is (R0.2), uniformly in \(g\).

For completeness, on the finite receiver-fiber set put
\(d_R=\Pi_D^*(\{R\})-P_{f^*}^+(\{R\})\).  The supremum in
(R0.2) equals \(\sum_R(d_R)_+\), by choosing the indicator of
\(\{R:d_R>0\}\).  Since \(P_u^+(1)=1+\nu_u\ge1\),
\[
 \begin{aligned}
 \widehat\Pi_D^*(1)
 &=\Pi_D^*(1)-\sum_R(d_R)_+\\
 &\ge\sum_u\eta_D^*(u)-e_\delta
 =m_D^*-e_\delta>{1\over16}-e_\delta .               \tag{R0.10}
 \end{aligned}
\]

Now fix, without optimizing it, an arbitrary reduced optimal display at a
carrier \(u\).  The optimal-face reduction is precisely
\[
 k_{T,u}+\sum_z a_{u,z}(p_z-p_u)=k_{O,u},
 \qquad a_{u,z}\ge0,                                  \tag{R0.11}
\]
with the two displayed endpoints in the two actor hulls.  If
\(A_u=\sum_z a_{u,z}=0\), then (R0.11) says
\(k_{T,u}=k_{O,u}\), contradicting the defining type-D disjointness.
Thus \(A_u>0\) and \(q_u\) is defined.  Equation (R0.11) becomes
\[
 k_{O,u}-k_{T,u}=A_u(q_u-p_u).                         \tag{R0.12}
\]
If \(q_u=p_u\), the right side vanishes and again the two hulls intersect.
Hence \(\ell_u>0\).  Every charged row satisfies
\(\|p_z-p_u\|_1<4\tau\), so convexity and strictness give
\[
 \ell_u=\left\|{1\over A_u}\sum_z a_{u,z}(p_z-p_u)\right\|_1
 \le {1\over A_u}\sum_z a_{u,z}\|p_z-p_u\|_1
 <4\tau.                                               \tag{R0.13}
\]
Because \(k_{T,u}\in K_T(u)\), \(k_{O,u}\in K_O(u)\), (R0.12) gives
\[
 g_u\le\|k_{T,u}-k_{O,u}\|_1=A_u\ell_u,              \tag{R0.14}
\]
proving (R0.5).

The corner condition gives \(d_u>H-4\tau\).  Distance to the visible hull is
1-Lipschitz, hence every charged \(z\) satisfies
\[
 d_z\ge d_u-\|p_z-p_u\|_1>H-4\tau-4\tau=H-8\tau.     \tag{R0.15}
\]
Finally, if \(g_u\ge\tau\), then
\(\tau\le g_u\le A_u\ell_u<4\tau A_u\).  Since
\(\tau>0\), this yields \(A_u>1/4\), proving (R0.6).

## B1 — `conj-w65-dcap-score-bulk-transfer`

### Pinned contract (verbatim)

**(a) Pinned contract — `conj-w65-dcap-score-bulk-transfer`.** Put
\[
 s(x):={2z(p_x)\over D_0}+h(p_x),\qquad
 F:=\{x\in\operatorname{supp}\lambda_A:s(x)\le12\tau/13\}.
\]
Then
\[
 \lambda_A(F)>{1\over14},\qquad a_A(F)>{c_m\over16}.  \tag{B1}
\]

### Exact registry shards consumed and hypothesis audit

- `argument/lem-ihorn-cotop-sl1a-package.md` (L0).  Line by line: the pinned
  D-cap datum has \(c_m\in(0,1)\), the displayed \(b,\delta_{\rm rt},D_0\),
  a finite exact signed idempotent with \(0<\delta\le\delta_{\rm rt}\le1/4\),
  nonempty visible set, and a hidden top \(v\) with \(H>16\tau\).  Its
  selected set \(A\) is \(4\tau\)-far and deeper than \(H-8\tau\); its
  full-fiber measure \(m\le P_v^+\) has mass \(S\ge c_m\).  Its \(\omega\),
  all-center shallow/exterior inequalities, strict parent drift and width
  bounds, ultra bounds \(\|r_\omega-p_v\|_1<b\tau\) and
  \(\Omega(\omega)<b\tau\), rim definition, and
  \(\theta<\tau/D_0\) are all part of the adopted I-base and pinned D-cap
  antecedent.  L0 therefore supplies a probability \(\lambda_A\), the strict
  all-exposer bound
  \(\int a\,d\lambda_A<2\tau/7\), and
  \(a_A=S(1-\theta)\lambda_A\le P_v^+\).

No score-bulk or I-cap shard is used.

### Proof

The top support functional has \(z=H-\phi\ge0\) on row points,
\(z(p_v)=0\), and is 1-Lipschitz.  The row-polytope diameter is at most
\(D_0\), so \(0\le z\le D_0\) there.  Thus \(z/D_0\) is an admissible
exposer at \(v\).  Applying L0 to \(z/D_0\) and to \(h\) gives
\[
 \int s\,d\lambda_A
 =2\int {z\over D_0}\,d\lambda_A+\int h\,d\lambda_A
 <2{2\tau\over7}+{2\tau\over7}={6\tau\over7}.        \tag{B1.1}
\]
The score is nonnegative.  On \(F^c\) it is strictly larger than
\(12\tau/13\), hence
\[
 {12\tau\over13}\lambda_A(F^c)
 <\int s\,d\lambda_A<{6\tau\over7}.
\]
Since
\[
 {6/7\over12/13}={6\cdot13\over7\cdot12}={13\over14},
\]
we obtain \(\lambda_A(F^c)<13/14\), or
\(\lambda_A(F)>1/14\).

Also \(\tau\le1/256\) and \(D_0\ge2\), so
\[
 \theta<{\tau\over D_0}\le{1\over512}<{1\over8},
 \qquad 1-\theta>{7\over8}.                            \tag{B1.2}
\]
Using \(S\ge c_m\) and the exact definition of \(a_A\),
\[
 a_A(F)=S(1-\theta)\lambda_A(F)
 >c_m{7\over8}{1\over14}={c_m\over16}.               \tag{B1.3}
\]

## B2 — `conj-w65-dcap-kernel-bulk-census`

### Pinned contract (verbatim)

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

### Exact registry shards consumed and hypothesis audit

- `argument/lem-sl1a-corner-ledger.md`.  For every \(f\in F\), the fixed
  \(P\) is exact with \(0<\delta\le2^{-16}\); \(W\ne\varnothing\); \(v\)
  is hidden top with \(H>16\tau\); the fixed \(\phi\) is a top support
  functional and \(h\) is admissible.  L0 places every \(f\) in the
  \(4\tau\)-far, strict \((H-4\tau)\)-deep support, and the definition of
  \(F\) gives its score inequality with equality included.  The kernel
  \(\xi\) was fixed before inspection, is a probability kernel on distinct
  row vertices, is clone-constant, barycentrically represents every row
  point, and is Dirac at vertices.  Thus the shard applies for this arbitrary
  kernel and gives \(\Gamma_f(\mathcal C)>1/2\).
- `argument/lem-radial-horn-partition.md`.  For each such \(f\),
  \(\Gamma_f\) is a finite nonnegative pair measure, \(v\) is a row point,
  \(\tau>0\), and \(\Gamma_f(\mathcal C)>1/2\).  Therefore the far block has
  mass at least \(1/4\), or, with that failure guard, the strict near block
  has mass greater than \(1/4\).  Distance equality belongs to the far block.

No kernel-arbitrary W64 or I-cap shard is consumed.

### Proof

Fix the legal kernel before examining any \(f\).  The preceding audit proves,
uniformly for every \(f\in F\), that the W56 radial rule selects a block
\(B(f)\subset\mathcal C\) with
\[
 \Gamma_f(B(f))\ge{1\over4}.                           \tag{B2.1}
\]
The X, I, and D predicates are disjoint and exhaustive on this block.  If
\(M_X>1/8\), the root is X.  Otherwise \(M_X\le1/8\).  In the latter case,
if \(M_I\ge1/16\) the root is I; if \(M_I<1/16\), then
\[
 M_D=\Gamma_f(B(f))-M_X-M_I
 >{1\over4}-{1\over8}-{1\over16}={1\over16},          \tag{B2.2}
\]
so the root is D.  This proves the genuine partition
\(F=F_I\sqcup F_X\sqcup F_D\) for the already fixed kernel, with all stated
boundaries.

By B1,
\[
 \lambda_A(F)>{1\over14}={3\over42}.                  \tag{B2.3}
\]
If \(\lambda_A(F_I)\ge1/42\), BI holds.  Otherwise its strict failure guard
holds.  Under that guard, if \(\lambda_A(F_X)\ge1/42\), BX holds.  If this
also fails, additivity of the partition gives
\[
 \lambda_A(F_D)
 =\lambda_A(F)-\lambda_A(F_I)-\lambda_A(F_X)
 >{3\over42}-{1\over42}-{1\over42}={1\over42}.        \tag{B2.4}
\]
This is BD.  The sequential failure guards make the three alternatives
pairwise disjoint, so exactly one holds.

## B3 — `conj-w65-dcap-common-ownership`

### Pinned contract (verbatim)

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

### Exact registry shards consumed and hypothesis audit

- `argument/lem-l5-positive-flow-foldback.md`.  The fixed \(P\) is finite,
  exact, and signed idempotent; the row is \(v\); the source measure is
  \(\alpha_J:=a_A|_{F_J}\), which is a nonnegative full-fiber submeasure of
  \(P_v^+\) because \(a_A\le P_v^+\); and the single statistic \(g_J\) is
  clone-invariant and lies in \([0,1]\), so \(M=1\).  Only the statistic of
  the actually routed cell is folded back.

The corner ledger and radial partition were re-proved into the inputs below
in B2; no W64 or I-cap ownership shard is consumed.

### Proof

For every \(f\in F_J\), its selected block lies in \(\mathcal C\), so
\[
 \begin{aligned}
 P_f^+(g_J)
 &=\sum_xP_{fx}^+\sum_u\xi_x(u)
       1_{\mathcal C}(x,u)1_J(x,u)\\
 &=\Gamma_f(\mathcal C\cap J)
 \ge\Gamma_f(B(f)\cap J).                             \tag{B3.1}
 \end{aligned}
\]
The last member is \(>1/8\) in X, \(\ge1/16\) in I, and \(>1/16\) in D,
by the cell definitions.  This proves the middle column.

For I and D, a contributing pair has \(p_x=p_u\) with \(u\) a row vertex.
The only vertex-kernel representation of that vertex is Dirac at \(u\).
Thus \(g_J\) is the indicator of the intrinsic row-vertex set \(U_J\), and
the kernel disappears on the diagonal.  This also proves clone invariance.

Every routed root set has \(\lambda_A\)-mass at least \(1/42\), strictly so
in BD.  By (B1.2),
\[
 \alpha_J(1)=S(1-\theta)\lambda_A(F_J)
 >c_m{7\over8}{1\over42}={c_m\over48}.                \tag{B3.2}
\]
Apply the foldback shard once to this same \(g_J\):
\[
 \int_{F_J}P_f^+(g_J)\,d\alpha_J(f)
 \le P_v^+(g_J)+e_\delta.                             \tag{B3.3}
\]
The left side is therefore strictly greater than \(c_m/384\) in X and
strictly greater than \(c_m/768\) in I and D.

It remains to display the error arithmetic.  Since
\(b=c_m/128\),
\[
 \delta\le(c_mb/120)^2={c_m^4\over235929600},
\]
and \(\delta<1\), so
\[
 e_\delta=2\delta(1+\delta)<4\delta
 \le {c_m^4\over58982400}<{c_m\over1536}.             \tag{B3.4}
\]
Consequently
\[
 {c_m\over384}-{c_m\over1536}={c_m\over512},
 \qquad
 {c_m\over768}-{c_m\over1536}={c_m\over1536}.        \tag{B3.5}
\]
Combining (B3.3)--(B3.5) proves the last column, with strict inequalities.
There was one common test and one foldback, never a sum of carrier-dependent
demands.

## B4 — `conj-w65-dcap-tall-same-center-packet`

### Pinned contract (verbatim)

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

### Exact registry shards consumed and hypothesis audit

- `argument/lem-ihorn-tall-halo-saturation.md`.  Its I-base hypothesis block
  is a class name, not the I-cap coefficient inequality.  Line by line, the
  pinned D-cap datum supplies \(c_m\in(0,1)\), finite exact signed
  idempotence, \(0<\delta\le\delta_{\rm rt}\le1/4\), nonempty \(W\), hidden
  top \(v\), \(H>16\tau\), the \(4\tau\)-far and \((H-8\tau)\)-deep selected
  set, its full-fiber submeasure of mass \(S\ge c_m\), the prescribed
  \(\omega\), both all-center G/shallow inequalities, and the two strict
  parent drift/width inequalities.  Thus both the divided saturation bound
  and its undivided precursor apply on D-cap.
- `argument/lem-ihorn-universal-exterior-package.md`.  The same audited
  I-base block holds; in addition \(b\) and \(\delta_{\rm rt}\) are exactly
  the shard's constants and \(\delta\le\delta_{\rm rt}\).  Its center may be
  any \(c\in K(P)\); the public center \(p_{f^*}\) is a row point and hence is
  in \(K(P)\).

No I-cap tallness shard is consumed.

### Proof

The tall-halo shard directly retains the exact fallback
\[
 (H-\tau/4)(1-\sigma_g)\le\nu_v(D_0+\tau/4),
\]
which is (B4.3), and gives
\[
 1-\sigma_g<{4\tau\over63}(D_0+\tau/4).               \tag{B4.4}
\]
Here \(\sigma_g\) is the positive mass on fibers of depth strictly greater
than \(\tau/4\).  Since total positive mass is \(1+\nu_v\), the boundary
\(d_Q=\tau/4\) belongs to \(\mathcal L_v\), and
\[
 \begin{aligned}
 P_v^+(\mathcal L_v)
 &=(1+\nu_v)-\sigma_g\\
 &=(1-\sigma_g)+\nu_v\\
 &<\delta+{4\tau\over63}(D_0+\tau/4)=\ell_T.          \tag{B4.5}
 \end{aligned}
\]

For the numerical simplification, \(\tau\le1/256\),
\(\delta\le1/65536\), and therefore
\[
 {\ell_T\over\tau}
 \le {1\over256}+{4\over63}
       \left(2+{1\over16384}+{1\over1024}\right)
 ={8\over63}+{4100\over1032192}.                      \tag{B4.6}
\]
Moreover
\[
 {2\over15}-{8\over63}={2\over315},
 \qquad
 4100\cdot315=1291500<2064384=2\cdot1032192.          \tag{B4.7}
\]
Thus \(4100/1032192<2/315\), proving
\(\ell_T<2\tau/15\).

If \(g_J(x)>0\), some \(u\) has
\(\xi_x(u)1_{\mathcal C}(x,u)1_J(x,u)>0\), so
\(z(p_x)<4\tau\).  For every \(c\) in the visible hull,
\(\phi(p_x)\le\phi(c)+\|p_x-c\|_1\le\|p_x-c\|_1\);
taking the infimum gives \(\phi(p_x)\le d_x\), hence
\[
 d_x\ge\phi(p_x)=H-z(p_x)>H-4\tau>12\tau>{\tau\over4}. \tag{B4.8}
\]
So the support of every routed common receiver statistic lies in
\(\mathcal H_v^{\rm out}\).

Finally apply the universal exterior package once, at the single center
\(c=p_{f^*}\).  With the strict exterior convention in its contract,
\[
 P_v^+(\mathcal E_*)\ge{\tau S\over8}
 \ge{c_m\tau\over8},                                  \tag{B4.9}
\]
which is (B4.2).  No family of centers is summed.

## B5 — `conj-w65-dcap-closed-overlay`

### Pinned contract (verbatim)

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

### Exact registry shards consumed and hypothesis audit

- `argument/lem-l5-positive-flow-foldback.md`, first at each routed root
  \(f\): \(P\) is finite exact signed idempotent; \(m=\eta_f^J\) is the
  nonnegative diagonal-cell restriction and is a full-fiber submeasure of
  \(P_f^+\); and the same arbitrary clone-invariant \(g\in[0,1]\) is used at
  every root.
- The same shard, then at \(v\):
  \(m=\alpha_J=a_A|_{F_J}\) is a nonnegative full-fiber submeasure of
  \(P_v^+\), and the test is still that same \(g\).  The first-layer errors
  are integrated against total source mass; they are not multiplied by the
  number of roots.

The B4 proof above supplies the tallness estimate used below from the audited
T shard.  No `lem-icap-closed-diagonal-flow` or
`lem-icap-priority-residual-split` shard is consumed.

### DEFECT B5.U — undefined \(\Xi_X\) in the pinned contract

The exact failing lines are the two X lines of (B5.3), beginning
\[
 X_{\rm gap}:\quad\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}\ge c_m/1024.
\]
Neither `DCAP-ATTACK.md` §1.1 nor §§1.2--1.7 defines \(\Xi_X\), and the brief
adopts notation only from `context/DECOMPOSITION-W63-I.md` §§0--1.1 and
`DCAP-ATTACK.md` §1.1.  Therefore (B5.3), and hence the literal B5 contract,
is not a well-formed standalone statement.  This is a definitional defect,
not a failure of the intended mass estimate.

The unique correction consistent with the already defined \(g_X\) and with
full-fiber ownership is to insert before (B5.3)
\[
 \boxed{\ \Xi_X(x,u):=P_v^+(\{x\})\,\xi_x(u)
       1_{\mathcal C}(x,u)1_X(x,u).\ }                 \tag{B5.C}
\]
Then \(\Xi_X(1)=P_v^+(g_X)\), and the X split is meaningful.  The proof below
proves all of (B5.1)--(B5.2) as written and proves (B5.3) under precisely this
displayed correction.  No stronger interpretation is assumed.

### Proof of (B5.1)--(B5.2) and of corrected (B5.3)

In BI or BD, (B3.2) gives
\(\alpha_J(1)>c_m/48\).  For every routed root,
\(\eta_f^I(1)\ge1/16\) and \(\eta_f^D(1)>1/16\).  Therefore
\[
 \beta_J(1)=\int_{F_J}\eta_f^J(1)\,d\alpha_J(f)
 >{c_m\over48}{1\over16}={c_m\over768}.               \tag{B5.4}
\]

Fix one arbitrary \(0\le g\le1\).  The first-layer foldback gives, for every
\(f\),
\[
 \sum_u\eta_f^J(u)P_u^+(g)\le P_f^+(g)+e_\delta.      \tag{B5.5}
\]
Integrate (B5.5) against \(\alpha_J\), then use the second-layer foldback at
\(v\):
\[
 \begin{aligned}
 \Pi_J(g)
 &\le\int_{F_J}P_f^+(g)\,d\alpha_J(f)
       +\alpha_J(1)e_\delta\\
 &\le P_v^+(g)+e_\delta+\alpha_J(1)e_\delta.          \tag{B5.6}
 \end{aligned}
\]
Because \(\alpha_J\le P_v^+\), (A.0) gives
\(\alpha_J(1)\le1+\nu_v\le1+\delta\).  Hence
\[
 \Pi_J(g)-P_v^+(g)\le(2+\delta)e_\delta.              \tag{B5.7}
\]
This holds for every common \(g\), proving the overflow part of (B5.1).

Let \(E=(2+\delta)e_\delta\).  At \(\delta\le2^{-16}\),
\(1+\delta<65/64\), \(2+\delta<129/64\), and
\(\tau\le1/256\).  Consequently
\[
 {E\over\tau}=2\tau(1+\delta)(2+\delta)
 <{2\over256}{65\over64}{129\over64}
 ={8385\over524288}<{1\over60},                       \tag{B5.8}
\]
where \(8385\cdot60=503100<524288\).  Thus \(E<\tau/60\).
Taking \(g=1_{\mathcal L_v}\) in (B5.7) and using B4 yields
\[
 \Pi_J(\mathcal L_v)
 \le P_v^+(\mathcal L_v)+E
 <{2\tau\over15}+{\tau\over60}={3\tau\over20}.      \tag{B5.9}
\]

On the finite receiver fibers, the overflow supremum is the sum of positive
coordinate differences.  Since \(\Pi_J(1)\ge\beta_J(1)\), the total canonical
overlap is at least \(\beta_J(1)-E\).  Its shallow portion is at most
\(\Pi_J(\mathcal L_v)\).  Hence
\[
 \begin{aligned}
 \widehat\Pi_J(\mathcal H_v^{\rm out})
 &\ge\widehat\Pi_J(1)-\widehat\Pi_J(\mathcal L_v)\\
 &> {c_m\over768}-{\tau\over60}-{3\tau\over20}
 ={c_m\over768}-{\tau\over6}.                        \tag{B5.10}
 \end{aligned}
\]
The third routine ceiling gives
\[
 \tau\le{c_mb\over120}={c_m^2\over15360}le{c_m\over15360}.
\]
Therefore
\[
 {c_m\over768}-{\tau\over6}
 \ge c_m\left({1\over768}-{1\over92160}\right)
 ={119c_m\over92160}>{90c_m\over92160}={c_m\over1024}. \tag{B5.11}
\]
This proves (B5.2).

It remains to prove the corrected labels.  In BX, (B5.C) and B3 give
\[
 \Xi_X(1)=P_v^+(g_X)>{c_m\over512}.                   \tag{B5.12}
\]
The predicates \(\|p_x-p_u\|_1\ge b\tau\) and
\(<b\tau\) partition its support, with equality in the first.  If the first
mass is at least \(c_m/1024\), X-gap holds.  Otherwise the explicit failure
guard holds and the complementary mass is
\[
 >{c_m\over512}-{c_m\over1024}={c_m\over1024},        \tag{B5.13}
\]
so X-near holds.

In BI and BD, diagonal Diracness gives
\(P_v^+(U_J)=P_v^+(g_J)>c_m/1536\).  The far/near radial predicates on
\(U_I\), and the gap/near-gap predicates on \(U_D\), are literal two-piece
partitions, with equality in I-far and D-gap.  In either case, if the first
piece is at least \(c_m/3072\), the first label holds.  If it is smaller, its
explicit failure guard holds and the complementary mass is
\[
 >{c_m\over1536}-{c_m\over3072}={c_m\over3072}.       \tag{B5.14}
\]
Thus exactly one guarded label is obtained in the routed branch.  This proof
does not identify the bulk overlay with the original \(\eta_D^*\) field.

## R1 — `conj-w65-dcap-five-way-completion-split`

### Pinned contract (verbatim)

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

### Exact registry shards consumed and hypothesis audit

- `argument/lem-hx-robust-scalar-starvation.md`.  We instantiate its
  universally quantified constants first as
  \((K_R,L,K_C)=(3,1,1)\).  For a carrier in
  \(\mathsf T_{\rm esc}\), the row fiber called \(v\) in the shard is the
  full fiber represented by \(u\), and the shard's \(f\) is the exhibited
  actual row in the definition of that cell.  The normalized values satisfy
  \(\widetilde A_u\ge4\),
  \(\tau/2\le\|\widetilde q_u-p_u\|_1\le2\tau\), and
  \(\widetilde q_u\in K(P)\).  The actor residual is at most
  \(3\delta=K_R\delta\).  The displayed \(\chi_u\) is affine,
  \(\chi_u(p_u)=0\), \(\chi_u(\widetilde q_u)=1\), and has Lipschitz
  constant \(1/\|\widetilde q_u-p_u\|_1\).  The tail uses the shard's exact
  signed full-fiber aggregates \(c_{u,Q}=\sum_{j\in Q}P_{uj}\), with the
  positive part taken after fiber aggregation.  Finally
  \(0<\delta\le\delta_{\rm rt}\le2^{-16}\), which is within the explicit
  ceiling computed below.

R0 supplies the carrier quantities; no rank-three, slab, I-cap, or reciprocal
\(1/t^*\) result is consumed.

### Proof

First verify the normalization used by the cells.  If \(\ell_u\le2\tau\),
the definition leaves \((q_u,A_u)\) unchanged.  If \(\ell_u>2\tau\), put
\(r=2\tau/\ell_u\in(0,1)\).  Then
\[
 \widetilde q_u=(1-r)p_u+r q_u\in K(P),
 \qquad \|\widetilde q_u-p_u\|_1=r\ell_u=2\tau,        \tag{R1.3}
\]
and
\[
 \widetilde A_u={A_u\ell_u\over2\tau}>A_u\ge4.       \tag{R1.4}
\]
In both cases
\[
 {\tau\over2}\le\|\widetilde q_u-p_u\|_1\le2\tau,
 \quad \widetilde A_u\ge4,
 \quad
 \widetilde A_u(\widetilde q_u-p_u)
 =A_u(q_u-p_u)=k_{O,u}-k_{T,u}.                        \tag{R1.5}
\]

The five predicates in (1.9) are exhaustive and disjoint.  First split at
\(g_u<\tau\) versus \(g_u\ge\tau\); then at \(A_u<4\) versus
\(A_u\ge4\); then at \(\ell_u<\tau/2\) versus
\(\ell_u\ge\tau/2\); finally, on the remaining set, the statement that all
row fibers have residual \(>3\delta\) is the logical complement of the
existence of one with residual \(\le3\delta\).  This also verifies all
equality ownership in the displayed cell definitions.

Since R0 gives
\[
 \eta_D^*(1)=m_D^*>{1\over16}={5\over80},             \tag{R1.6}
\]
at least one of five cells has mass at least \(1/80\).  Declaring the first
such cell makes the priority alternatives unique.  If the first four masses
are all less than \(1/80\), then
\[
 \eta_D^*(\mathsf T_{\rm esc})
 =m_D^*-\sum_{C\in\{\mathsf N,\mathsf G_{<4},
               \mathsf C_0,\mathsf A_{\rm esc}\}}\eta_D^*(C)
 >{5\over80}-{4\over80}={1\over80},                   \tag{R1.7}
\]
which is (R1.1).

Now fix \(u\in\mathsf T_{\rm esc}\) and choose one public row \(f\) whose
residual is at most \(3\delta\).  With
\(D_u=\widetilde q_u-p_u\ne0\), the sign functional is
\[
 \chi_u(x)={\operatorname{sgn}(D_u)\cdot(x-p_u)\over\|D_u\|_1}.
\]
Because the dual norm of \(\operatorname{sgn}(D_u)\) is one,
\[
 |\chi_u(x)-\chi_u(y)|
 \le {\|x-y\|_1\over\|D_u\|_1},\quad
 \chi_u(p_u)=0,quad
 \chi_u(\widetilde q_u)
 ={\operatorname{sgn}(D_u)\cdot D_u\over\|D_u\|_1}=1. \tag{R1.8}
\]

For \((K_R,L,K_C)=(3,1,1)\), the explicit starvation-shard constants are
\[
 B=K_C+1+{K_C+K_R+1\over4}
 =1+1+{1+3+1\over4}={13\over4},
\]
\[
 H_R=2L+6B=2+6{13\over4}={43\over2},
 \qquad (4H_R^2)^{-1}={1\over1849}.                   \tag{R1.9}
\]
Since \(1849<65536\),
\[
 \delta_R(3,1,1)
 =\min\{2^{-16},1/1849\}=2^{-16}.                    \tag{R1.10}
\]
All audited hypotheses of `lem-hx-robust-scalar-starvation` therefore hold
except possibly its forbidden tail cap.  If
\(\operatorname{Tail}_1(u)\le\delta\), that cap would hold with
\(K_C=1\), and the proved shard would say that this finite exact signed
idempotent cannot exist.  Hence necessarily
\[
 \operatorname{Tail}_1(u)>\delta,                     \tag{R1.11}
\]
which proves (R1.2).  The argument uses the fixed clone-invariant sign normer,
not a favorable scalar selector, and reads no conic coefficient as a
transition.
