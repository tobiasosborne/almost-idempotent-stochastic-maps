STATUS: UNVERIFIED PROVER OUTPUT

# W74F-F — EXT-CB conditional on H-CB

Date: 2026-07-24  
Role: fresh prover; this document is not a verifier verdict  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`  
Checked SHA256:
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

## 0. Claimed outcome

EXT-CB follows from the corrected conditional form of H-CB, APPROX-CB,
MERGE-CB, and the named level-one selection lemmas.

The construction uses exactly one level-one unitary
\[
 U_1:\mathbb C^r\longrightarrow\mathcal S_{P,Q}
\]
and four level-one corner maps. Their amplifications, rather than newly chosen
objects at each level, satisfy all the merging estimates.

One possible relative constant is
\[
\boxed{
 C_{\rm ext}
 =C_{\rm merge}\!
   \left[1+5C_H+20C_{\rm app}(C_H+1)\right].
}
\tag{0.1}
\]
An explicit universal threshold is given in (1.8) below. The constants in
(0.1) are the named constants of the three premises under the normalizations
in Section 1. They are independent of \(r\), the amplification level, the
dimension of \(\mathcal A\), and all block data.

The proof slightly improves the source construction. It keeps the \(11\)
corner exactly equal to the given \(v\), but defines each of the other three
corners by transporting one exact spatial matrix-corner system through the
corresponding *level-one* Ha inverse. Consequently, the complete comparison
error is zero in those three corners; only the \(11\) corner carries the
APPROX-CB error.

No obstruction to EXT-CB was found under the stated premises.

## 1. Premise ledger and normalization

Put
\[
 e=\delta+\varepsilon,\qquad
 P_1=P,\quad P_2=Q,\qquad
 H_j=\mathcal S_{P_j,Q},
\]
and
\[
 h_{jk}=\operatorname{Ha}^{Q}_{P_j,P_k}:
 \mathcal S_{P_j,P_k}\longrightarrow\mathcal B(H_k,H_j).
\tag{1.1}
\]
The amplification level is denoted by \(m\), reserving \(r\) for the size of
the input matrix algebra.

All premise constants may be enlarged, so assume
\[
 C_H,C_{\rm app},C_{\rm merge}\ge1.
\]

### 1.1 Exact H-CB clauses consumed

This proof uses H-CB only through the following clauses. They state explicitly
the corrected interface after
`PROOF-W74F-E-HCB.md` Sections 7.3--7.4 and 9 and the hostile verifier's
contract-impact correction.

For \(e\le e_H\), uniformly in \(m\):

1. **Exact adjointness**
   \[
   h_{kj,m}(Z^\dagger)=h_{jk,m}(Z)^\dagger.
   \tag{H1}
   \]

2. **Product defect**
   \[
   \|h_{jl,m}(Z\mathbin{\cdot}W)
       -h_{jk,m}(Z)h_{kl,m}(W)\|
   \le C_He\|Z\|\|W\|.
   \tag{H2}
   \]

3. **Diagonal homomorphism, unit, and upper norm.** If
   \(u_j=\widetilde P_j=\operatorname{Co}_{P_j}(P_j)\), then
   \[
   \|h_{jj,m}(I_m\otimes u_j)-I\|\le C_He,\qquad
   \|h_{jj,m}(Z)\|\le(1+C_He)\|Z\|.
   \tag{H3}
   \]
   I enlarge \(C_H\), if necessary, to include the mechanically available
   canonical-unit estimate
   \[
   \|u_j-P_j\|\le C_He.
   \tag{H3u}
   \]
   This is part of the “unit estimates required by `lem_extension`” in the
   H-CB interface; it is not an inverse assertion. Only an upper bound on
   \(\|u_P\|\) is used for arbitrary \(P\); a lower unit-norm estimate is used
   only for the nonvanishing one-dimensional \(Q\).

4. **Special corners.** The maps \(h_{P,Q}\) and \(h_{Q,P}\), including
   \(h_{Q,Q}\), are completely \(C_He\)-close to their canonical column/row
   identifications. The Neumann condition against those identifications
   implies level-one bijectivity and the corresponding complete norm and
   inverse bounds after shrinking the threshold.
   \(\tag{H4}\)

5. **Conditional diagonal inverse.** If the level-one lower modulus of
   \(h_{R,R}\) is at least \(1/4\), then
   \[
   \|h_{R,R,m}(Z)\|\ge(1-C_He)\|Z\|.
   \]
   If \(h_{R,R}\) is also bijective at level one, then every \(h_{R,R,m}\)
   is bijective and
   \[
   \|h_{R,R,m}^{-1}\|\le1+C_He.
   \tag{H5}
   \]

6. **Conditional off-diagonal inverse.** If \(h_{P,R}\) is bijective at
   level one and the diagonal anchor \(h_{R,R}\) satisfies the preceding
   lower-modulus hypothesis, then every \(h_{P,R,m}\) is bijective and
   \[
   \begin{aligned}
   (1-C_He)\|Z\|
   &\le\|h_{P,R,m}(Z)\|
   \le(1+C_He)\|Z\|,\\
   \|h_{P,R,m}^{-1}\|&\le1+C_He.
   \end{aligned}
   \tag{H6}
   \]

No unconditional inverse estimate for a general \(h_{P,P}\) is used.
In particular, this proof does not invoke the false inverse statement killed
by the exact \(\mathbb C\oplus\mathbb C\) example in the H-CB report.

### 1.2 APPROX-CB clause consumed

There is a universal admissible defect \(a_{\rm app}>0\) such that if
\[
 T:M_r\longrightarrow\mathcal B(H_1)
\]
is an extended \(\alpha\)-homomorphism between exact finite-dimensional
\(C^*\)-algebras and \(\alpha\le a_{\rm app}\), then APPROX-CB produces
one exact unital \(*\)-homomorphism
\[
 \mu_{11}:M_r\longrightarrow\mathcal B(H_1)
\]
such that
\[
 \|\mu_{11,m}-T_m\|\le C_{\rm app}\alpha
 \quad\text{for every }m.
\tag{APP}
\]
The exactness follows by applying `lem_approx_ext` (`tex:1508-1535`) with
exact target \(\mathcal B(H_1)\), hence target error \(0\). The same norm-one
diagonal is used at every amplification; this is the premise feature that
prevents \(r\)-dependence.

### 1.3 MERGE-CB clause consumed

There is a universal admissible defect \(a_{\rm merge}>0\) such that if the
same four level-one maps
\[
 \gamma_{jk}:\mathcal B(K_k,K_j)\longrightarrow
 \mathcal S_{P_j,P_k}
\]
satisfy, at every amplification, `merging0`--`merging3` with common defect
\(\rho\), then the single combined map has extended-inclusion defect at most
\[
 C_{\rm merge}(\rho+\varepsilon).
\tag{MERGE}
\]
If all four level-one \(\gamma_{jk}\) are bijective, the combined map is
bijective exactly. This is the amplified `lem_merging` mechanism
(`tex:1325-1350`), whose factorization through the four-corner
`lem_alpha` map preserves bijectivity.

### 1.4 Level-one selection clauses consumed

The only uses of `lem_PQR`, `lem_1d_proj`, and `lem_add_dim` are the
level-one dimension argument in Section 2. They are never applied to
\(I_m\otimes Q\). Let \(e_{\rm sel}>0\) be a common universal threshold for
those level-one statements.

### 1.5 Constants and threshold

Define
\[
 A_0:=4(C_H+1),\qquad
 \kappa:=C_{\rm app}A_0=4C_{\rm app}(C_H+1),
\qquad
 D_0:=5(C_H+\kappa).
\tag{1.7}
\]
Set
\[
\boxed{
 e_{\rm ext}:=\min\left\{
 e_H,\ e_{\rm sel},\
 \frac{a_{\rm app}}{A_0},\
 \frac{a_{\rm merge}}{D_0+1},\
 \frac1{4(C_H+1)},\
 \frac1{4(\kappa+1)}
 \right\}.
}
\tag{1.8}
\]
Every entry in this minimum is a positive universal number. In particular,
for \(e\le e_{\rm ext}\),
\[
 C_He\le\tfrac14,\qquad
 \kappa e\le\tfrac14.
\tag{1.9}
\]

## 2. EXTCB-1 — the level-one dimension calculation

Write \(E_{ab}\) for the standard matrix units in \(M_r\) and
\[
 R_a:=v(E_{aa})\qquad(1\le a\le r).
\]
The named level-one argument at `tex:1382-1384` gives:

- each \(R_a\) is a one-dimensional approximate projection in
  \(\mathcal S_P\);
- the \(R_a\) are pairwise equivalent;
- because \(Q\) is one-dimensional, `lem_1d_proj` gives
  \(\dim\mathcal S_{R_a,Q}\le1\);
- equivalence and `lem_PQR` make all these dimensions equal;
- `lem_add_dim` gives
  \[
  \dim H_1=\dim\mathcal S_{P,Q}
     =\sum_{a=1}^r\dim\mathcal S_{R_a,Q}.
  \]

The hypothesis \(\mathcal S_{P,Q}\ne0\) excludes the all-zero alternative.
Therefore
\[
\boxed{\dim H_1=r.}
\tag{2.1}
\]
Also,
\[
\boxed{\dim H_2=\dim\mathcal S_{Q,Q}=\dim\mathcal S_Q=1.}
\tag{2.2}
\]
This is the only dimension count in the proof.

## 3. EXTCB-2 — one exact representation and one unitary

Let
\[
 T:=h_{11}v:M_r\longrightarrow\mathcal B(H_1).
\tag{3.1}
\]
At amplification \(m\), H-CB and the extended \(\delta\)-isomorphism
properties of \(v\) give
\[
\begin{aligned}
\|T_m(XY)-T_m(X)T_m(Y)\|
&\le(1+C_He)\delta\|X\|\|Y\|\\
&\quad+C_He(1+\delta)^2\|X\|\|Y\|\\
&\le A_0e\|X\|\|Y\|.
\end{aligned}
\tag{3.2}
\]
Similarly,
\[
\|T_m(I)-I\|
\le(1+C_He)\delta+C_He
\le A_0e.
\tag{3.3}
\]
The involution is preserved exactly. Hence \(T\) is one extended
\(A_0e\)-homomorphism.

Because \(A_0e\le a_{\rm app}\), APPROX-CB with exact target
\(\mathcal B(H_1)\) yields one exact unital \(*\)-homomorphism
\[
 \mu_{11}:M_r\longrightarrow\mathcal B(H_1)
\]
with
\[
\boxed{
 \|\mu_{11,m}-h_{11,m}v_m\|
 \le\kappa e
 \quad(m\ge1).
}
\tag{3.4}
\]

The map \(\mu_{11}\) is nonzero because it is unital. Since \(M_r\) is
simple, its kernel is zero. By (2.1), both its domain and codomain have
dimension \(r^2\), so it is onto. Thus \(\mu_{11}\) is an exact
\(*\)-isomorphism
\[
 M_r\cong\mathcal B(H_1).
\]
Every exact \(*\)-isomorphism between these full finite-dimensional matrix
algebras is spatial. Therefore there is one unitary
\[
\boxed{
 U_1:\mathbb C^r\longrightarrow H_1,\qquad
 \mu_{11}(A)=U_1AU_1^\dagger.
}
\tag{3.5}
\]

This is exactly where finite dimension and exactness are used. If
\(\mu_{11}\) were merely approximate, or if the equal finite dimensions were
not known, the conclusion (3.5) would not follow from this argument.

Normalize the nonzero vector \(u_Q=\widetilde Q\in H_2\) in the H-CB Hilbert
norm and let
\[
 U_2:\mathbb C\longrightarrow H_2
\]
be the resulting unitary. For \(K_1=\mathbb C^r\), \(K_2=\mathbb C\), define
one exact four-corner system
\[
 \mu_{jk}:\mathcal B(K_k,K_j)\longrightarrow\mathcal B(H_k,H_j),
 \qquad
 \mu_{jk}(A)=U_jAU_k^\dagger.
\tag{3.6}
\]
It satisfies, exactly and completely isometrically,
\[
\begin{aligned}
\mu_{kj}(X^\dagger)&=\mu_{jk}(X)^\dagger,\\
\mu_{jl}(XY)&=\mu_{jk}(X)\mu_{kl}(Y),\\
\mu_{jj}(I_{K_j})&=I_{H_j}.
\end{aligned}
\tag{3.7}
\]
At level \(m\), these are the amplifications using
\(I_m\otimes U_1\) and \(I_m\otimes U_2\). No unitary is chosen at level
\(m\).

## 4. EXTCB-3 — conditional H-CB produces the four complete inverses

First consider \(h_{11}\). Equation (3.4) and
\(\kappa e<1\) imply that \(T=h_{11}v\) is bijective by Neumann inversion
against the isomorphism \(\mu_{11}\). Since \(v\) is bijective, \(h_{11}\)
is bijective.

For \(Z=v(A)\), (3.4) also gives the quantitative lower bound
\[
\frac{\|h_{11}(Z)\|}{\|Z\|}
\ge\frac{1-\kappa e}{1+\delta}
\ge\frac14.
\tag{4.1}
\]
Thus \(h_{11}\) meets both hypotheses of the corrected conditional diagonal
clause (H5), rather than merely being bijective.

For \(h_{12},h_{21},h_{22}\), clause (H4) gives a Neumann perturbation of
the appropriate canonical identity map at level one. The threshold (1.8)
makes the Neumann norm \(<1\), so all three are level-one bijections.
Moreover, \(h_{22}\) has level-one lower modulus at least \(1/4\).

Apply (H5) to \(h_{11}\) and \(h_{22}\), then (H6) to the two
off-diagonal maps, using \(h_{22}\) as the anchor for \(h_{12}\) and
\(h_{11}\) as the anchor for \(h_{21}\). We obtain, for every \(j,k,m\),
\[
\boxed{
\begin{aligned}
(1-C_He)\|Z\|
&\le\|h_{jk,m}(Z)\|
\le(1+C_He)\|Z\|,\\
\|h_{jk,m}^{-1}\|&\le1+C_He.
\end{aligned}}
\tag{4.2}
\]
Because \(h_{jk}\) is a level-one bijection,
\[
 h_{jk,m}^{-1}=1_{M_m}\otimes h_{jk}^{-1}.
\tag{4.3}
\]
Thus (4.2) does not choose an inverse separately at each amplification.

## 5. EXTCB-4 — one set of corner maps and all four cb estimates

Define the four level-one maps
\[
\boxed{
\begin{aligned}
\gamma_{11}&:=v,\\
\gamma_{12}&:=h_{12}^{-1}\mu_{12},\\
\gamma_{21}&:=h_{21}^{-1}\mu_{21},\\
\gamma_{22}&:=h_{22}^{-1}\mu_{22}.
\end{aligned}}
\tag{5.1}
\]
The first identity ensures that the eventual \(v_+\) genuinely extends
\(v\) on the upper-left corner.

For all \(j,k,m\), put
\[
 d_{jk,m}:=h_{jk,m}\gamma_{jk,m}-\mu_{jk,m}.
\]
Equations (3.4), (4.3), and (5.1) give the complete four-corner comparison
\[
\boxed{
\begin{aligned}
\|d_{11,m}\|&\le\kappa e,\\
d_{12,m}&=d_{21,m}=d_{22,m}=0.
\end{aligned}}
\tag{5.2}
\]
In particular, complete closeness is proved for all four corners, not only
for \(h_{11}\). Equivalently,
\[
\|\gamma_{11,m}-h_{11,m}^{-1}\mu_{11,m}\|
\le(1+C_He)\kappa e,
\tag{5.3}
\]
and the analogous difference is exactly zero in the other three corners.

### 5.1 Exact adjoint condition

The map \(v\) preserves the involution exactly. For the other corners,
(H1), (3.7), and inversion give
\[
\boxed{
\gamma_{kj,m}(X^\dagger)=\gamma_{jk,m}(X)^\dagger.
}
\tag{5.4}
\]

### 5.2 Complete product condition

By (4.2), (5.2), and (1.9),
\[
\|\gamma_{jk,m}(X)\|
\le(1+C_He)(1+\kappa e)\|X\|
<2\|X\|.
\tag{5.5}
\]
Let
\[
 D=\gamma_{jl,m}(XY)
   -\gamma_{jk,m}(X)\mathbin{\cdot}\gamma_{kl,m}(Y).
\]
Apply \(h_{jl,m}\). The first term differs from \(\mu_{jl,m}(XY)\) by at
most \(\kappa e\|X\|\|Y\|\). By (H2), the image of the second term differs
from
\[
 h_{jk,m}\gamma_{jk,m}(X)\,
 h_{kl,m}\gamma_{kl,m}(Y)
\]
by at most \(4C_He\|X\|\|Y\|\). Expanding the latter two factors using
(5.2), and using the exact multiplication in (3.7), costs at most
\[
 \left(2\kappa+\kappa^2e\right)e\|X\|\|Y\|.
\]
Since \(\kappa e\le1/4\),
\[
\|h_{jl,m}(D)\|
\le4(C_H+\kappa)e\|X\|\|Y\|.
\]
Using \(\|h_{jl,m}^{-1}\|\le5/4\) gives
\[
\boxed{
\|D\|\le5(C_H+\kappa)e\|X\|\|Y\|.
}
\tag{5.6}
\]

### 5.3 Complete unit condition

For \(j=1,2\), equations (H3), (H3u), (3.7), and (5.2) imply
\[
\begin{aligned}
\|\gamma_{jj,m}(I_m\otimes I_{K_j})-I_m\otimes P_j\|
&\le(1+C_He)(\kappa+C_H)e+C_He\\
&\le3(C_H+\kappa)e.
\end{aligned}
\tag{5.7}
\]

### 5.4 Complete norm condition

The upper half of (4.2) and the lower estimate on
\(\|h_{jk,m}\gamma_{jk,m}(X)\|\) give
\[
\|\gamma_{jk,m}(X)\|
\ge\frac{1-\kappa e}{1+C_He}\|X\|
\ge\left(1-(C_H+\kappa)e\right)\|X\|.
\tag{5.8}
\]
The inverse bound in (4.2) and the upper estimate on the same image give
\[
\|\gamma_{jk,m}(X)\|
\le(1+C_He)(1+\kappa e)\|X\|
\le\left(1+2(C_H+\kappa)e\right)\|X\|.
\tag{5.9}
\]

Equations (5.4), (5.6), (5.7), and (5.8)--(5.9) are precisely the
complete versions of `merging0`--`merging3`, with common defect
\[
\boxed{\rho=D_0e=5(C_H+\kappa)e.}
\tag{5.10}
\]

Finally, all four level-one corner maps are bijective:
\(\gamma_{11}=v\) by hypothesis, while the other three are compositions of
the bijections \(h_{jk}^{-1}\) and \(\mu_{jk}\).

## 6. EXTCB-5 — merge and exact bijectivity

Define one level-one map
\[
\boxed{
v_+\!\begin{pmatrix}
A_{11}&A_{12}\\
A_{21}&A_{22}
\end{pmatrix}
=\sum_{j,k=1}^2\gamma_{jk}(A_{jk})
:\ M_{r+1}\longrightarrow\mathcal A.
}
\tag{6.1}
\]
Its \(m\)-th amplification is automatically
\[
 1_{M_m}\otimes v_+,
\]
built from \(I_m\otimes U_1\), \(I_m\otimes U_2\), and the amplifications
of the same four maps (5.1).

By (1.8), \(\rho\) and \(\varepsilon\) lie in the admissible MERGE-CB
range. Equations (5.4)--(5.10) and (MERGE) yield
\[
\begin{aligned}
\operatorname{defect}(v_+)
&\le C_{\rm merge}(\rho+\varepsilon)\\
&\le C_{\rm merge}(D_0+1)e
=C_{\rm ext}e,
\end{aligned}
\tag{6.2}
\]
where
\[
\boxed{
C_{\rm ext}
=C_{\rm merge}\!
 \left[1+5C_H+20C_{\rm app}(C_H+1)\right].
}
\tag{6.3}
\]
Thus every amplification is a \(C_{\rm ext}e\)-inclusion.

Bijectivity is not obtained by a perturbative “almost onto” argument. Each
\(\gamma_{jk}\) is exactly bijective, so the exact factorization in
`lem_merging`,
\[
\text{canonical corner decomposition}
\longrightarrow\bigoplus_{j,k}\mathcal S_{P_j,P_k}
\longrightarrow\mathcal A,
\]
is a composition of linear bijections. Hence \(v_+\) is exactly bijective.
Its algebraic amplification \(1_{M_m}\otimes v_+\) is then exactly
bijective with inverse \(1_{M_m}\otimes v_+^{-1}\). Consequently \(v_+\)
is one extended \(C_{\rm ext}e\)-isomorphism.

Also, by (5.1),
\[
v_+\!\begin{pmatrix}A&0\\0&0\end{pmatrix}=v(A),
\]
so this construction has the literal extension property, although the
registered EXT-CB contract only asks for existence of the one map.

## 7. Constant ledger

| Constant | Definition / producing inequality | Dependence |
|---|---|---|
| \(C_H,e_H\) | Corrected conditional H-CB, (H1)--(H6) | universal only |
| \(C_{\rm app},a_{\rm app}\) | APPROX-CB exact-target correction, (APP) | universal only; norm-one diagonal |
| \(C_{\rm merge},a_{\rm merge}\) | MERGE-CB, (MERGE) | universal only; fixed four corners |
| \(e_{\rm sel}\) | Level-one selection lemmas | universal only |
| \(A_0\) | \(4(C_H+1)\), composition defect (3.2)--(3.3) | no \(r,m,\dim\mathcal A\) |
| \(\kappa\) | \(4C_{\rm app}(C_H+1)\), complete APPROX error (3.4) | no \(r,m,\dim\mathcal A\) |
| \(D_0\) | \(5(C_H+\kappa)\), four merging conditions (5.10) | no \(r,m,\dim\mathcal A\) |
| \(e_{\rm ext}\) | finite positive minimum (1.8) | universal only |
| \(C_{\rm ext}\) | \(C_{\rm merge}(D_0+1)\), (6.2)--(6.3) | universal only |

There is no hidden dependence on \(r\):

1. the level-one dimension calculation is exact and contributes no norm
   constant;
2. APPROX-CB uses a diagonal of projective norm one in \(M_r\), so its
   correction bound is \(C_{\rm app}\), not \(rC_{\rm app}\);
3. \(U_1\), \(U_2\), and every \(I_m\otimes U_j\) have norm one;
4. H-CB tests whole columns and has constants independent of \(m\);
5. MERGE-CB sees one fixed \(2\times2\) corner decomposition, never \(r\)
   separately indexed corners.

## 8. Hypothesis hygiene

### Finite-dimensional extended \(\varepsilon\)-\(C^*\)-algebra

The extended structure supplies all H-CB and MERGE-CB estimates at the same
amplification level. Finite dimension is used in the level-one dimension
count and in turning the exact injective \(\mu_{11}:M_r\to\mathcal B(H_1)\)
between equal-dimensional full matrix algebras into a spatial isomorphism.

### \(P,Q\) are \(\delta\)-projections and
\(\|P+Q-I\|\le\delta\)

The projection hypotheses define the four compressed corners and their
units. Approximate complementarity is consumed by MERGE-CB, whose
four-corner recombination maps onto \(\mathcal A\).

### \(v:M_r\to\mathcal S_P\) is an extended \(\delta\)-isomorphism

Its complete homomorphism and norm bounds are used in (3.2)--(3.3); its
level-one bijectivity gives \(\dim\mathcal S_P=r^2\), the matrix-unit
selection in Section 2, the quantitative lower bound (4.1), exact
bijectivity of \(\gamma_{11}\), and the literal extension property.

### \(\dim\mathcal S_Q=1\)

This is used:

1. by the level-one selection lemmas in Section 2;
2. to give \(H_2=\mathcal S_{Q,Q}\) dimension one;
3. to define the Hilbert spaces and Ha maps in H-CB;
4. to choose the single normalized unitary \(U_2:\mathbb C\to H_2\).

It is never applied to \(I_m\otimes Q\) as a one-dimensional projection.

### \(\mathcal S_{P,Q}\ne0\)

This is used exactly once: it rules out
\(\dim\mathcal S_{R_a,Q}=0\) for every \(a\), forcing
\(\dim\mathcal S_{P,Q}=r\). Without it, the spatial \(r\times r\)
representation in Section 3 need not exist.

### \(e\le e_{\rm ext}\)

This ensures the H-CB validity range, the level-one selection range, the
APPROX-CB and MERGE-CB input ranges, the Neumann inequalities, the
\(1/4\) lower-modulus trigger, and all denominator estimates.

## 9. Hostile checkpoints

1. **No per-\(m\) unitary:** \(U_1\) is chosen once in (3.5);
   every level uses \(I_m\otimes U_1\).
2. **All four corners:** (5.2) gives the complete comparison in every
   corner; three errors are exactly zero.
3. **No \(r\)-dependence:** the five mechanisms excluding it are listed
   after the constant ledger.
4. **Exact bijectivity:** Section 6 uses exact corner and `lem_alpha`
   bijections, not a limiting or approximate-surjectivity argument.
5. **Finite dimension / exactness:** their precise use in obtaining
   conjugation by \(U_1\) is isolated after (3.5).
6. **The two nontrivial hypotheses:** \(\dim\mathcal S_Q=1\) supplies the
   one-dimensional Hilbert corner; \(\mathcal S_{P,Q}\ne0\) selects the
   \(r\)-dimensional rather than zero branch.

## 10. DEFECT REGISTER — LOUD

1. **THIS IS CONDITIONAL ON H-CB.** The proof consumes the corrected
   conditional inverse clauses (H5)--(H6), not the overbroad registered
   inverse wording. The parallel hostile H-CB verdict is
   `VALID-WITH-CORRECTIONS`; the registry contract still requires that
   wording correction. This report does not promote H-CB or EXT-CB.

2. **THE MECHANICAL CONSTANTS ARE RELATIVE, NOT DECIMAL.** The source uses
   unnamed universal big-\(O\) constants. Equations (1.7)--(1.8) and
   (6.3) are explicit in \(C_H,C_{\rm app},C_{\rm merge}\) and the positive
   universal premise thresholds, but an absolute decimal value cannot be
   extracted from the supplied TeX.

3. **APPROX-CB EXACTNESS IS ESSENTIAL.** The output \(\mu_{11}\) is exact
   only because its target is the exact \(C^*\)-algebra
   \(\mathcal B(H_1)\). Applying APPROX-CB with the original approximate
   algebra \(\mathcal A\) as target would not justify (3.5).

4. **THE SOURCE'S THREE NATURAL CORNER FORMULAS ARE REPLACED.** Instead of
   separately proving that the formulas at `tex:1407-1409` are completely
   close at all levels, (5.1) transports the exact spatial corners through
   the already established level-one Ha inverses. This is a deliberate
   proof change. It preserves \(\gamma_{11}=v\), uses no per-level object,
   and makes the three disputed complete-closeness estimates exact.

5. **NO INTERNAL EXT-CB GAP REMAINS GIVEN THE PINNED PREMISES, BUT THIS IS
   NOT SELF-CERTIFICATION.** A separate fresh hostile verifier must still
   attack the dimension argument, the exact-target APPROX step, the
   conditional inverse triggers, the four-corner transport, and the
   MERGE-CB constant normalization.

