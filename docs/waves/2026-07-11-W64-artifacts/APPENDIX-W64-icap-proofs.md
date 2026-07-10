# Appendix: proposed routine proofs and exact I-cell calibrations

> **Status.** This appendix is a strategy artifact.  Every newly named result
> remains proposed / `conjecture`, even where a proof is written out.  The exact
> matrices are L3 constructive evidence, not registry promotions.

In §§A.1--A.6, use the notation of `ICAP-ATTACK.md` and
`context/DECOMPOSITION-W63-I.md`: \(\delta=\tau^2\),
\(D_0=2+4\delta\), \(b=c_m/128\), and
\[
 \delta\le\delta_{\rm rt}
 =\min\{2^{-16},(c_m/4)^2,(c_mb/120)^2\}.
\]
The exact L3 calibrations in §§A.7--A.8 deliberately have
\(\delta=1/16>\delta_{\rm rt}\) and are outside this routine ceiling.

## A.1 The single-root receiver cap

Let \(\mathscr C^*=(\phi,h,f^*,\eta^*)\) be the exhibited target I-certificate
and let \(\eta_I^*\) be its diagonal type-I marginal.  If
\((x,u)\) is diagonal and \(u\) is a row vertex, then \(p_x=p_u\), and every
legal vertex kernel is Dirac at that row point.  Since \(\eta^*\) is a
restriction of
\(\Gamma_{f^*}(x,u)=P_{f^*x}^+\xi_x(u)\), this gives, fiberwise,
\[
 0\le\eta_I^*(u)\le P_{f^*}^+(u).
\]
Also \(\eta_I^*(1)=M_I(\mathscr C^*)\ge1/16\).

Apply `lem-l5-positive-flow-foldback` at row \(f^*\), with source submeasure
\(\eta_I^*\), to an arbitrary \(0\le g\le1\):
\[
 \sum_u\eta_I^*(u)P_u^+(g)
 \le P_{f^*}^+(g)+2\delta(1+\delta).                    \tag{A.1}
\]
Taking the supremum proves B0.  On a finite receiver set, for signed measure
\(\Delta=\Pi_{f^*}-P_{f^*}^+\),
\[
 \sup_{0\le g\le1}\Delta(g)=\sum_R(\Delta_R)_+,
\]
attained by \(g=1_{\{\Delta_R>0\}}\).  Therefore
the fiberwise measure defined by
\[
 \Pi_{f^*}^{\circ}(\{R\})
 :=\min\{\Pi_{f^*}(\{R\}),P_{f^*}^+(\{R\})\},\qquad
 \Pi_{f^*}^{\circ}(E):=\sum_{R\in E}\Pi_{f^*}^{\circ}(\{R\})
\]
loses exactly this positive-variation mass.

## A.2 Score-bulk production and the X/I/D census

Put \(z=H-\phi\).  The standard check in
`lem-sl1a-score-selector` shows that \(z/D_0\) is an admissible exposer at
\(v\): it is affine, is zero at \(p_v\), and has row values in \([0,1]\).
L0 gives, strictly,
\[
 \int \frac{z}{D_0}\,d\lambda_A<\frac{2\tau}{7},
 \qquad
 \int h\,d\lambda_A<\frac{2\tau}{7}.
\]
Thus, for \(s=2z/D_0+h\),
\[
 \int s\,d\lambda_A<\frac{6\tau}{7}.                  \tag{A.2}
\]
Let \(F=\{s\le12\tau/13\}\).  Since \(s>12\tau/13\) on its complement,
\[
 \lambda_A(F^c)<\frac{6/7}{12/13}=\frac{13}{14},
 \qquad \lambda_A(F)>\frac1{14}.                       \tag{A.3}
\]
The score equality is on the good side.

Moreover \(\tau\le2^{-8}\) and \(D_0\ge2\), so
\(\theta<\tau/D_0<1/8\).  With
\(a_A=S(1-\theta)\lambda_A\),
\[
 a_A(F)>c_m\frac78\frac1{14}=\frac{c_m}{16}.           \tag{A.4}
\]

Fix any legal vertex kernel \(\xi\).  For every \(f\in F\), the support of
\(\lambda_A\) supplies the far/co-top hypotheses and its score supplies the
corner-score hypothesis.  `lem-sl1a-corner-ledger` applies to the same
\((\phi,h,\xi)\) and gives \(\Gamma_f(\mathcal C)>1/2\).  The literal radial
partition chooses a block of mass at least \(1/4\).  The proved arithmetic
then places \(f\) in exactly one of X/I/D, with the boundaries used in the
main file.

Since \(F_X,F_I,F_D\) partition a set of mass greater than \(3/42\), either
\(\lambda_A(F_I)\ge1/42\), or, after its strict failure,
\(\lambda_A(F_X)\ge1/42\), or both fail and
\[
 \lambda_A(F_D)>\frac3{42}-\frac1{42}-\frac1{42}=\frac1{42}.
                                                                    \tag{A.5}
\]
This proves the priority census.

## A.3 The common cell statistic and its constants

Define
\[
 g_J(x)=\sum_u\xi_x(u)1_{\mathcal C}(x,u)1_J(x,u).
\]
The function lies in \([0,1]\) and is independent of the root \(f\).  If
\(f\in F_J\), its selected radial block satisfies \(B(f)\subset\mathcal C\),
so
\[
 P_f^+(g_J)=\Gamma_f(\mathcal C\cap J)\ge\Gamma_f(B(f)\cap J).        \tag{A.6}
\]
This is \(>1/8\) in X, \(\ge1/16\) in I, and \(>1/16\) in D.

Let \(\alpha_J=a_A|_{F_J}\).  In the routed cell,
\[
 \alpha_J(1)>c_m\frac78\frac1{42}=\frac{c_m}{48}.       \tag{A.7}
\]
R2 at \(v\), with the one common test \(g_J\), gives
\[
 \sum_f\alpha_J(f)P_f^+(g_J)
 \le P_v^+(g_J)+e_\delta,
 \qquad e_\delta=2\delta(1+\delta).                    \tag{A.8}
\]
The left side exceeds \(c_m/384\) in X and \(c_m/768\) in I/D.

The smallest routine ceiling gives
\[
 \delta\le(c_mb/120)^2
 =\frac{c_m^4}{15360^2}.
\]
Since \(\delta\le2^{-16}<1\),
\[
 e_\delta<4\delta
 \le\frac{c_m^4}{58{,}982{,}400}
 <\frac{c_m}{1536}.                                    \tag{A.9}
\]
Subtracting (A.9) from the raw floors proves
\[
 P_v^+(g_X)>c_m/512,\qquad
 P_v^+(g_I),P_v^+(g_D)>c_m/1536.                       \tag{A.10}
\]

For I or D, a contributing pair has \(p_x=p_u\) with \(u\) a vertex; hence
\(\xi_x\) is Dirac and \(g_J\) is the intrinsic indicator \(1_{U_J}\).
For X, the retained object is a barycentric coupling; no transition
interpretation is available.

## A.4 The exact T spend and diagonal internal closure

Let \(\sigma_g=P_v^+\{d_Q>\tau/4\}\).  Since
\(P_v^+(1)=1+\nu_v\),
\[
 P_v^+\{d_Q\le\tau/4\}
 =1+\nu_v-\sigma_g
 <\delta+\frac{4\tau}{63}\left(D_0+\frac\tau4\right).  \tag{A.11}
\]
At \(\tau\le1/256\), division by \(\tau\) bounds the right side by
\[
 \frac8{63}+\frac{64}{63}\tau+\frac{16}{63}\tau^2
 <\frac2{15}.                                          \tag{A.12}
\]
This proves T+.

If \(g_J(x)>0\), the corner condition has \(z(p_x)<4\tau\).  A top support
functional satisfies \(\phi(p_x)\le d_x\), so
\[
 d_x>H-4\tau>12\tau>\tau/4.                            \tag{A.13}
\]
Thus every cell statistic is supported in the outer halo.

Now assume the bulk is I.  Let
\(\alpha_I=a_A|_{F_I}\), and for each \(f\in F_I\) let
\(\eta_f^I=\Gamma_f|_{B(f)\cap I}\).  From (A.7),
\(a_I:=\alpha_I(1)>c_m/48\), while
\(\eta_f^I\le P_f^+\) and \(\eta_f^I(1)\ge1/16\).  Hence
\[
 \beta_I(1):=\sum_f\alpha_I(f)\eta_f^I(1)
 >\frac{c_m}{768}.                                     \tag{A.14}
\]

For the same arbitrary receiver test \(0\le g\le1\), first apply R2 at each
root \(f\):
\[
 \sum_u\eta_f^I(u)P_u^+(g)\le P_f^+(g)+e_\delta.
\]
Weight and sum by \(\alpha_I(f)\), then apply R2 at \(v\) to
\(\alpha_I\le P_v^+\):
\[
 \Pi_I(g):=\sum_{f,u}\alpha_I(f)\eta_f^I(u)P_u^+(g)
 \le P_v^+(g)+(1+a_I)e_\delta.                         \tag{A.15}
\]
Because \(a_I\le P_v^+(1)\le1+\delta\), the overflow is at most
\((2+\delta)e_\delta\).  This is a two-fold coefficient calculation with the
same \(g\), not a new corner construction.

At \(\delta\le2^{-16}\), direct arithmetic gives
\[
 (2+\delta)e_\delta
 =2(2+\delta)\tau^2(1+\delta)<\frac\tau{60}.            \tag{A.16}
\]
Apply (A.15) to the shallow-halo indicator and use (A.12):
\[
 \Pi_I(\mathcal L_v)<\frac{2\tau}{15}+\frac\tau{60}
 =\frac{3\tau}{20}.                                   \tag{A.17}
\]

Let \(E=(1+a_I)e_\delta\) and define
\[
 \widehat\Pi_I(\{R\}):=\min\{\Pi_I(\{R\}),P_v^+(\{R\})\},\qquad
 \widehat\Pi_I(A):=\sum_{R\in A}\widehat\Pi_I(\{R\}).
\]
The total receiverwise
truncation loss is at most \(E\), so (A.14), (A.16), and (A.17) imply
\[
 \begin{aligned}
 \widehat\Pi_I(\mathcal H_v^{\rm out})
 &\ge \Pi_I(1)-\Pi_I(\mathcal L_v)-E\\
 &>\frac{c_m}{768}-\frac\tau6.
 \end{aligned}                                         \tag{A.18}
\]
Finally
\(\tau\le c_m^2/15360\le c_m/15360\), and therefore
\[
 \frac{c_m}{768}-\frac\tau6
 \ge c_m\left(\frac1{768}-\frac1{92160}\right)
 =\frac{119c_m}{92160}>\frac{c_m}{1024}.               \tag{A.19}
\]
The same proof applies to the bulk-D diagonal measure.

## A.5 Alpha-free cancellation

Let \(u\) be type I.  `lem-optimal-face-conic-reduction` gives probabilities
\(\lambda_u\) on \(T(u)\) and \(\gamma_u\) on \(O(u)\) such that
\[
 \bar p_{T,u}-p_u
 =t^*(u)(\bar p_{O,u}-p_u).                             \tag{A.20}
\]
Every corner carrier is hidden and has a nonempty far set, hence
\(0<t^*(u)<\tau/4\).  Since the row diameter is at most \(D_0\),
\[
 \|\bar p_{T,u}-p_u\|_1
 \le t^*(u)D_0
 <(1/2+\delta)\tau.                                    \tag{A.21}
\]
This proves the convex cancellation-radius bound.  Since every
\(t\in T(u)\) has \(\|p_t-p_u\|_1\ge4\tau\),
\[
 \begin{aligned}
 \int\|p_t-\bar p_{T,u}\|_1\,d\lambda_u(t)
 &\ge4\tau-\|\bar p_{T,u}-p_u\|_1\\
 &>(7/2-\delta)\tau.
 \end{aligned}                                         \tag{A.22}
\]
A geometrically singleton \(T(u)\)-hull has zero left side, so type I requires
at least two distinct far-tight row points.

## A.6 Why the W63 diagonal plateau is exactly D

The six-shape report computes
\[
 T(u)=\{f_{\rm transient}\},\qquad O(u)=\{o\}.
\]
Thus, at the row-point level,
\(K_T(u)=\{p_f-p_u\}\) with norm at least \(4\tau\), whereas
every point of \(K_O(u)\) has norm less than
\((1/2+\delta)\tau\) by (A.21).  Hence
\[
 d_1(K_T(u),K_O(u))>(7/2-\delta)\tau.                  \tag{A.25}
\]
The frozen fixture gives the sharper exact value
\[
 \frac{g_u}{\tau}=\frac{4194305}{1048576}
 =4+\frac1{1048576}.
\]
Its \(M_I=0\) is therefore a geometric zero, not a construction that almost
reaches \(1/16\).  The entire diagonal mass routes to D because the fixture has
only one far-tight ray.

## A.7 An exact short type-I module

With row labels \((u,o,a,b)\), define
\[
 P_I=
 \begin{pmatrix}
 1/16&-5/5456&160/341&160/341\\
 0&1&0&0\\
 1023/8192&1/8192&15/16&-1/16\\
 0&0&0&1
 \end{pmatrix}.                                        \tag{A.26}
\]
It has the factorized projection form
\[
 P_I=I-Ac^T,\qquad
 A=(-320/341,0,1/8,0)^T,\qquad
 c=(-1023/1024,-1/1024,1/2,1/2)^T.
\]
Here \(c^T\mathbf1=0\) and \(c^TA=1\), so
\(P_I\mathbf1=\mathbf1\) and \(P_I^2=P_I\).  Its row negativities are
\[
 (5/5456,0,1/16,0),
\]
so \(\delta=1/16\), \(\tau=1/4\), \(\rho=1\), and \(\kappa=1/16\).

The exact affine relation
\[
 \frac{p_a+p_b}{2}
 =\frac{1023}{1024}p_u+\frac1{1024}p_o                \tag{A.27}
\]
forces, for every admissible exposer at \(u\),
\((h(a)+h(b))/2=h(o)/1024\).  The optimum is attained at row values
\[
 h=(0,1,1/1024,1/1024),
\]
so
\[
 t^*(u)=1/1024<\kappa,\qquad
 T(u)=\{a,b\},\qquad O(u)=\{o\}.                       \tag{A.28}
\]
Subtracting \(p_u\) in (A.27) gives the exact intersection
\[
 \frac{(p_a-p_u)+(p_b-p_u)}2
 =\frac1{1024}(p_o-p_u),                               \tag{A.29}
\]
so \(u\) is type I.

The visible set is \(\{o,a,b\}\).  A primal/dual height certificate for the
hidden vertex \(u\) is
\[
 c_*=(2896/5797)p_a+(2901/5797)p_b,
\]
\[
 y=(1,-1,1,4351/4352),\qquad \|y\|_\infty=1,
\]
and both give
\[
 H_u=\|p_u-c_*\|_1
 =y\cdot p_u-4351/4352
 =\frac{2901}{1484032}.                                \tag{A.30}
\]
Thus \(H_u-16\tau=-5933227/1484032<0\): this module is extremely short.

Using \(v=u\), the support functional from (A.30), the exposer in (A.28),
selected row \(f=a\), and the Dirac kernel, the near radial block contains
\((u,u)\) with mass
\[
 \eta(u,u)=P_{a,u}^+=\frac{1023}{8192}>\frac1{16}.      \tag{A.31}
\]
The exact score is
\[
 \frac{2z(p_a)}{D_0}+h(p_a)
 =\frac{48335}{17808384}<\frac3{13}.
\]
Hence the local analogues of the cell quantities satisfy
\(M_X^{\rm loc}=0\) and \(M_I^{\rm loc}=1023/8192\).  This is **not** a
selected-corner configuration because
tallness fails.  Moreover it is not an SC-style public certificate: this near
block has mass below \(1/4\), and no I-base/L0 provenance exists.

The row-\(a\) reproduction identity makes the price visible:
\[
 p_a=\frac{1023}{8192}p_u+\frac1{8192}p_o
      +\frac{15}{16}p_a-\frac1{16}p_b.                 \tag{A.32}
\]
The constant I coefficient on \(u\) is paid by negative mass on the opposite
far-tight ray \(b\).

## A.8 An exact short numerical I-guard calibration with block mass

The preceding module can be direct-summed with a short hidden-top block.  Let
\[
 P_S=
 \begin{pmatrix}
 0&1/2&9/16&-1/16\\
 0&1&0&0\\
 0&0&1&0\\
 0&0&0&1
 \end{pmatrix},\qquad
 P=\operatorname{diag}(P_S,P_I),                       \tag{A.33}
\]
with labels \((v,q,s,n\mid u,o,a,b)\).  Direct multiplication gives
\(P^2=P\), every row sum is one, and \(\delta(P)=1/16\).

At \(v\), all of \(q,s,n\) are \(\rho\)-far and the row identity forces
\[
 \frac12h(q)+\frac9{16}h(s)=\frac1{16}h(n).
\]
Thus \(t^*(v)=1/17<1/16\), attained by
\((h(v),h(q),h(s),h(n))=(0,1/17,1/17,1)\), extended with value \(1\) on
every \(I\)-block row.  Blockwise harmonic exposers, extended with constant
value \(1\) on the other block, show that \(q,s,n,o,a,b\) are visible; the
relation (A.27) keeps \(u\) hidden.  Thus the global visible set is
\(\{q,s,n,o,a,b\}\), and \(v\) is the hidden global top with
\[
 H=\frac18,\qquad
 \phi=(1/8,0,0,-2\mid0,0,0,0)                         \tag{A.34}
\]
on the eight row points.  A closest visible point is
\((8/17)p_q+(9/17)p_s\), and the linear part
\(y=(0,1,1,-1\mid1,1,1,1)\) has \(\ell^\infty\)-norm one: explicitly
\(\phi(x)=y\cdot x-1\).  Hence (A.34) is an exact primal/dual height
certificate.  The other hidden vertex has the old competitor of height
\(2901/1484032<1/8\), so \(v\) is the global top.

Choose the zero admissible exposer, selected row \(f=a\), the Dirac kernel,
and the far radial block.  Then
\[
 \|p_a-p_v\|_1=9/4>1,\qquad
 d_a=0>H-4\tau=-7/8,\qquad
 \frac{2z(p_a)}{D_0}=\frac19<\frac3{13}.               \tag{A.35}
\]
The positive row-\(a\) carriers all lie in the numerical corner/radial block,
giving
\[
 \eta(u,u)=1023/8192,\qquad
 \eta(o,o)=1/8192,\qquad
 \eta(a,a)=15/16,\qquad
 \eta(1)=17/16.                                        \tag{A.36}
\]
The carrier \(u\) is type I by (A.29), so
\[
 M_X^{\rm loc}=0,\qquad M_I^{\rm loc}\ge1023/8192>1/16. \tag{A.37}
\]

These local quantities meet the numerical \(1/4,1/8,1/16\) I guards after
tallness is deleted.  This is still **not** a genuine selected-corner
configuration or SC
output, because
\[
 H-16\tau=1/8-4=-31/8.
\]
It has no I-base, ultra, thin-rim, or \(\lambda_A\) provenance; visible
carriers in (A.36) also show why one must not invoke the tall corner partition
outside its hypotheses.

The cheat is structural: the matrix is block diagonal.  Row \(v\) has zero
positive ownership of the I module, \(f=a\) is visible, and the top has no
outer-halo saturation linking it to the module.  A genuine refuter must couple
the two-ray identity (A.29) into the **same** tall, top-owned, ultra-low-width
web while keeping every row negativity at most \(\tau^2\).  This is exactly
what IC and T+ isolate.
