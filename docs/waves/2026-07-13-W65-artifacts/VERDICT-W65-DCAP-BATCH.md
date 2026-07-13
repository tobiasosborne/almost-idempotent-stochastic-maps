# W65 D-cap routine batch — hostile verdict

conj-w65-dcap-root-closure: VALID

conj-w65-dcap-score-bulk-transfer: VALID

conj-w65-dcap-kernel-bulk-census: VALID

conj-w65-dcap-common-ownership: VALID

conj-w65-dcap-tall-same-center-packet: VALID

conj-w65-dcap-closed-overlay: VALID-WITH-CORRECTION

conj-w65-dcap-five-way-completion-split: VALID

## R0 — `conj-w65-dcap-root-closure`

The diagonal restriction is a legal full-fiber submeasure.  The public certificate has
\(\eta^*=\Gamma_{f^*}|_B\); if \(p_x=p_u\) and \(u\) is a row vertex, the legal vertex kernel at the
row point \(p_x=p_u\) is Dirac.  Thus restriction to the D cell gives
\(0\le\eta_D^*(u)\le P_{f^*}^+(\{u\})\), even though the construction kernel has been erased.  Also
\[
 m_D^*=\eta^*(1)-M_X-M_I
 \ge\frac14-M_X-M_I
 >\frac14-\frac18-\frac1{16}=\frac1{16}.
\]

The one call to `lem-l5-positive-flow-foldback` uses one arbitrary common fiber test
\(0\le g\le1\), source \(\eta_D^*\le P_{f^*}^+\), and exactly the error
\(e_\delta=2\delta(1+\delta)\).  Consequently the positive coordinate overflow is at most
\(e_\delta\), and
\(\widehat\Pi_D^*(1)\ge\Pi_D^*(1)-e_\delta\ge m_D^*-e_\delta>1/16-e_\delta\).

All four structural shards are legal on each D carrier.  The corner ledger makes \(u\) a hidden
geometrically distinct vertex with \(d_u>H-4\tau\).  Since the visible set is nonempty, a visible
row lies at distance at least \(d_u>12\tau>4\tau\), so the far set required by
`lem-positive-exposedness-margin` is genuinely nonempty and \(t^*(u)>0\).  This discharges the
hypotheses of `lem-always-tight-dual-support`, `lem-optimal-face-conic-reduction`, and
`lem-zero-face-localization`; none assumes the I-cap inequality.  Disjointness forces \(A_u>0\),
and then
\[
 k_{O,u}-k_{T,u}=A_u(q_u-p_u),\qquad
 0<\ell_u<4\tau,\qquad g_u\le A_u\ell_u.
\]
Thus \(g_u\ge\tau\) implies \(\tau<4\tau A_u\), hence \(A_u>1/4\).  Localization plus the
1-Lipschitz depth function gives the claimed strict depth \(d_z>H-8\tau\).

## B1 — `conj-w65-dcap-score-bulk-transfer`

`lem-ihorn-cotop-sl1a-package` is an I-base shard, not an I-cap shard: its actual hypothesis block
contains no condition \(M_I\ge1/16\), and every listed base, ultra, rim, and ceiling hypothesis is in
the pinned D-cap antecedent.  Both \(z/D_0\) and \(h\) are admissible exposers, so
\[
 \int s\,d\lambda_A
 <2\frac{2\tau}{7}+\frac{2\tau}{7}=\frac{6\tau}{7}.
\]
Because equality at \(12\tau/13\) belongs to \(F\), Markov gives
\[
 \lambda_A(F)>1-\frac{6/7}{12/13}=1-\frac{13}{14}=\frac1{14}.
\]
Moreover \(\tau\le1/256\) and \(D_0\ge2\) give
\(\theta<1/512<1/8\), whence
\[
 a_A(F)=S(1-\theta)\lambda_A(F)
 >c_m\frac78\frac1{14}=\frac{c_m}{16}.
\]
No certificate, exposer, or score is reselected.

## B2 — `conj-w65-dcap-kernel-bulk-census`

The actual contracts of `lem-sl1a-corner-ledger` and `lem-radial-horn-partition` match the D-cap
inputs and contain no I-cap coefficient hypothesis.  The kernel is fixed before any root or cell is
inspected.  The ledger gives \(\Gamma_f(\mathcal C)>1/2\) for every \(f\in F\); the radial shard,
with distance equality assigned to the far block, gives \(\Gamma_f(B(f))\ge1/4\).  The X/I/D
predicates then partition the block, with \(M_X=1/8\) diagonal and \(M_I=1/16\) in I.  In the last
case
\[
 M_D>\frac14-\frac18-\frac1{16}=\frac1{16}.
\]
Finally \(\lambda_A(F)>1/14=3/42\).  Failure of BI and BX therefore gives
\[
 \lambda_A(F_D)>\frac3{42}-\frac1{42}-\frac1{42}=\frac1{42}.
\]
The sequential strict failure guards make the three declared alternatives exhaustive and disjoint.

## B3 — `conj-w65-dcap-common-ownership`

The selected block is contained in the fixed common corner, so the single root-independent
\(g_J\) dominates the routed cell mass.  For I and D, diagonal Diracness makes it the indicator of
the corresponding fixed corner vertex set \(U_J\).  The source
\(\alpha_J=a_A|_{F_J}\) is a nonnegative full-fiber submeasure of \(P_v^+\), and only this one
statistic is passed to `lem-l5-positive-flow-foldback`.  Its mass satisfies
\[
 \alpha_J(1)>c_m\frac78\frac1{42}=\frac{c_m}{48}.
\]
Thus the pre-error floors are \(c_m/384\) in X and \(c_m/768\) in I/D.  The ceiling arithmetic is
\[
 \delta\le\left(\frac{c_mb}{120}\right)^2
 =\frac{c_m^4}{235929600},\qquad
 e_\delta<4\delta\le\frac{c_m^4}{58982400}<\frac{c_m}{1536}.
\]
Subtracting this one source-independent error gives exactly
\[
 \frac{c_m}{384}-\frac{c_m}{1536}=\frac{c_m}{512},\qquad
 \frac{c_m}{768}-\frac{c_m}{1536}=\frac{c_m}{1536},
\]
with the claimed strict inequalities.

## B4 — `conj-w65-dcap-tall-same-center-packet`

The actual hypothesis blocks of `lem-ihorn-tall-halo-saturation` and
`lem-ihorn-universal-exterior-package` use the I-base data only; neither assumes
\(M_I\ge1/16\).  Their all-center, ultra, tallness, and ceiling hypotheses are all present.  Since
the shallow boundary belongs to \(\mathcal L_v\), the tall-halo conclusion gives
\[
 P_v^+(\mathcal L_v)<\ell_T
 =\delta+\frac{4\tau}{63}\left(D_0+\frac\tau4\right).
\]
At \(\tau\le1/256\),
\[
 \frac{\ell_T}{\tau}
 \le\frac8{63}+\frac{4100}{1032192}
 <\frac8{63}+\frac2{315}=\frac2{15};
\]
the comparison is exact because \(4100\cdot315=1291500<2064384\).

If \(g_J(x)>0\), the common corner gives \(z(p_x)<4\tau\), hence
\(d_x\ge H-z(p_x)>H-4\tau>\tau/4\).  The routed receiver support is therefore in the strict outer
halo.  The exterior shard is used once, at the already public center \(p_{f^*}\in K(P)\), and gives
\(P_v^+(\mathcal E_*)\ge\tau S/8\ge c_m\tau/8\).  No family of centers is summed.

## B5 — `conj-w65-dcap-closed-overlay`

### Exact defect and exact correction

The literal original is not well formed.  Its exact failing lines are
\[
\begin{aligned}
X_{\rm gap}:&\quad\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}\ge c_m/1024,\\
X_{\rm near}:&\quad\Xi_X\{\|p_x-p_u\|_1\ge b\tau\}<c_m/1024,
\quad\Xi_X\{\|p_x-p_u\|_1<b\tau\}>c_m/1024.
\end{aligned}
\]
Here \(\Xi_X\) has no definition in the literal pinned D-cap contract.

The exact corrected statement is the original B5 statement with the following definition inserted
immediately before its label display:
\[
 \boxed{\Xi_X(x,u):=P_v^+(\{x\})\,\xi_x(u)
       1_{\mathcal C}(x,u)1_X(x,u).}                 \tag{B5.C}
\]
Thus the corrected contract is:
\[
 \beta_J(1)>c_m/768,\qquad
 \sup_{0\le g\le1}\{\Pi_J(g)-P_v^+(g)\}
       \le(2+\delta)e_\delta\quad(J=I,D),
\]
\[
 \widehat\Pi_J(\mathcal H_v^{\rm out})>c_m/1024,
\]
and the routed package receives exactly one guarded label
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
\end{array}
\]

This is the unique legal reading in the pinned construction.  The fixed kernel and the already
defined statistic
\(g_X(x)=\sum_u\xi_x(u)1_{\mathcal C}(x,u)1_X(x,u)\) determine its top-owned pairwise lift
coefficient by coefficient, and (B5.C) is exactly that lift; in particular
\(\Xi_X(1)=P_v^+(g_X)\).  It also matches the explicit W64 registry source.  A measure chosen only
to have the same total would not be a legal reading because it would discard the fixed pairwise
kernel provenance.

The corrected proof is valid.  The first R2 layer uses the same arbitrary \(g\) at every root and
contributes \(\alpha_J(1)e_\delta\); the second layer at \(v\) uses that same \(g\) and contributes
one \(e_\delta\).  Since \(\alpha_J(1)\le1+\delta\), the total is
\((2+\delta)e_\delta\), not a root count or a sum of pairwise demands.  Also
\[
 \beta_J(1)>\frac{c_m}{48}\frac1{16}=\frac{c_m}{768}.
\]
Writing \(E=(2+\delta)e_\delta\), the exact bound
\[
 \frac E\tau=2\tau(1+\delta)(2+\delta)
 <\frac{8385}{524288}<\frac1{60}
\]
gives \(\Pi_J(\mathcal L_v)<3\tau/20\).  Hence
\[
 \widehat\Pi_J(\mathcal H_v^{\rm out})
 >\frac{c_m}{768}-\frac\tau{60}-\frac{3\tau}{20}
 =\frac{c_m}{768}-\frac\tau6.
\]
Because \(\tau\le c_mb/120=c_m^2/15360\le c_m/15360\), the last expression is at least
\(119c_m/92160>c_m/1024\).  The X and I/D total floors are respectively \(>c_m/512\) and
\(>c_m/1536\), so their literal two-piece partitions produce the displayed \(c_m/1024\) and
\(c_m/3072\) guarded splits with equality on gap/far.

There is one additional typographical omission in the proof, not in the contract.  The exact line
\[
 \tau\le{c_mb\over120}={c_m^2\over15360}le{c_m\over15360}
\]
must read
\[
 \tau\le{c_mb\over120}={c_m^2\over15360}\le{c_m\over15360}.
\]
The required inequality follows from \(0<c_m<1\) and is the inequality actually used on the next
line.

## R1 — `conj-w65-dcap-five-way-completion-split`

The five predicates are a genuine disjoint partition with every boundary owned as stated.  Since
\(m_D^*>1/16=5/80\), if the first four cells each have mass below \(1/80\), then
\[
 \eta_D^*(\mathsf T_{\rm esc})
 >\frac5{80}-\frac4{80}=\frac1{80}.
\]

The normalization is exact.  When \(\ell_u>2\tau\), with
\(r=2\tau/\ell_u\in(0,1)\),
\[
 \widetilde q_u=(1-r)p_u+rq_u\in K(P),\quad
 \|\widetilde q_u-p_u\|_1=2\tau,\quad
 \widetilde A_u=\frac{A_u\ell_u}{2\tau}>A_u\ge4,
\]
and in both branches
\[
 \widetilde A_u(\widetilde q_u-p_u)=A_u(q_u-p_u)=k_{O,u}-k_{T,u}.
\]

The actual contract of `lem-hx-robust-scalar-starvation` matches the call exactly and has no
rank, slab, I-cap, or selected-corner hypothesis.  Its row fiber is the full fiber represented by
\(u\); its actual row is the exhibited \(f\); its endpoint lies in
\([\tau/2,2\tau]\); \(\widetilde A_u\ge4\); and its residual is at most \(3\delta\).  The affine
sign normer has \(\chi_u(p_u)=0\), \(\chi_u(\widetilde q_u)=1\), and Lipschitz constant
\(1/\|\widetilde q_u-p_u\|_1\).  Its tail is exactly the shard's positive part of the signed
full-fiber aggregate \(c_{u,Q}=\sum_{j\in Q}P_{uj}\), taken after aggregation.

For \((K_R,L,K_C)=(3,1,1)\),
\[
 B=\frac{13}{4},\qquad H_R=2+6B=\frac{43}{2},\qquad
 (4H_R^2)^{-1}=\frac1{1849},
\]
so \(\delta_R(3,1,1)=\min\{2^{-16},1/1849\}=2^{-16}\).  Therefore a tail
\(\operatorname{Tail}_1(u)\le\delta\) would satisfy every hypothesis of the proved impossibility
shard.  Its negation is exactly \(\operatorname{Tail}_1(u)>\delta\).

## CROSS-CUTTING

- **Hypothesis honesty.**  Every directly consumed registry shard was reopened.  None of the eleven
  consumed shards assumes \(M_I\ge1/16\).  In particular, no `lem-icap-*` shard is consumed; the
  words “I-base” in L0, T, and E name the common structural base and do not import the I-cap
  coefficient inequality.
- **R2 discipline.**  R0 and B3 each use one common nonnegative test.  B5 uses one arbitrary common
  test through both nested folds; its first-layer error is weighted by source mass and its second
  layer contributes once.  No node sums carrier-dependent tests or multiplies an error by a root or
  class count.
- **Quantifiers and boundaries.**  The certificate, the independent census kernel, and the entire
  reduced-display field are fixed before their respective classifications.  Equality is assigned at
  the score threshold, radial distance and mass thresholds, \(M_X=1/8\), \(M_I=1/16\), priority
  thresholds, shallow depth, gap, gauge, starvation window, and residual boundary.  No favorable
  certificate, kernel, display, row, or scalar direction is selected.
- **Notation.**  There is no harmful drift between the overlay and original D-root populations:
  \(U_J\) is the fixed diagonal support of \(g_J\), while
  \(g_u=d_1(K_T(u),K_O(u))\) is the intrinsic actor-hull gap and is meaningful on every D vertex.
  The overlay is never identified with \(\eta_D^*\).  The only ill-formed public symbol is the
  original B5 \(\Xi_X\), repaired above.
- **Walls.**  The proofs use no signed-to-stochastic reading, raw-index path, dual reversal, witness
  averaging, conic recurrence, coefficient cleanup, alpha bound, finite cover, second web, freight
  censoring, selector, or centerwise sum.  Thus none crosses FINDINGS' absolute dead routes or
  K1--K10.
- **Clone invariance.**  All masses are on full row-point fibers; kernels are clone-constant and
  Dirac at vertex row points; actor-hull distances and all thresholds use row-point \(\ell^1\)
  geometry.  Under a compatible clone lift, the sign normer and its scalar values are preserved, and
  the starvation tail uses signed fiber aggregates.  Every public quantity and threshold is
  clone-invariant.
- **Remaining arithmetic.**  The assembly normalization is correct:
  \[
   \frac{c_m\tau}{64}-\frac{c_m}{16}\frac{2\tau}{15}
   =\left(\frac{15}{960}-\frac8{960}\right)c_m\tau
   =\frac{7c_m}{960}\tau.
  \]
  The separate emptiness ceiling also has the right scale: \(3\tau^2/c_m\le
  (7c_m/1920)\tau\) follows from \(\tau\le7c_m^2/5760\).
