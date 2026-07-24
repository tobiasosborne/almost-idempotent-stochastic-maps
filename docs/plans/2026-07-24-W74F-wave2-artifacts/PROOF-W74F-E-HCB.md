STATUS: UNVERIFIED PROVER OUTPUT

# W74F-E — H-CB: complete Ha-module estimates

Date: 2026-07-24  
Role: fresh prover; this document is not a verifier verdict  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`  
Checked SHA256:
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

## 0. Claimed outcome

The uniform-in-\(n\) adjoint, product, unit, norm, and special-corner estimates
of H-CB follow from COMP-CB and corrected COL-HILB. The key is an exact
amplified variational identity derived by summing `Ha_def` algebraically,
followed by one estimate of a *whole rectangular compressed associator*. No
matrix entry is estimated separately.

There is one necessary qualification to the wording of item (3). A general
\(h_{P,P}\) need not be injective, even when \(\delta=\varepsilon=0\).
Consequently, an unconditional inverse estimate for \(h_{P,P}\) is false.
The estimate actually needed in `lem_extension` is conditional on the
level-one lower bound/bijectivity established there. Under the fixed lower
bound \(1/4\), the inverse estimates are uniform at every amplification.
Section 2 gives the exact counterexample, and Sections 7.3--7.4 give the
correct conditional inverse result.

Relative to the universal constants in the sanctioned COMP-CB and corrected
COL-HILB contracts, one possible common choice is
\[
  C_H=4000c,\qquad e_H=\frac1{10000c},\qquad
  c:=\max\{1,C_{\rm co},C_{\rm col},e_{\rm in}^{-1}\}.
\tag{0.1}
\]
Here \(C_{\rm co}\) is enlarged once to dominate all the COMP-CB product,
unit, and compressed-unit norm estimates listed in Section 1.2, and
\(C_{\rm col}\) is the constant in corrected COL-HILB. Both are universal
sanctioned inputs; \(e_{\rm in}>0\) is a common universal validity threshold
for those two estimates. Thus (0.1) is independent of \(n\),
\(\dim\mathcal A\), the number of blocks, and every block dimension. The TeX
and the sanctioned contracts use unnamed big-\(O\) constants, so an absolute
decimal value of \(C_H\) cannot be extracted from the supplied data.

## 1. Precise setup and norm conventions

### 1.1 Corners and norms

Put
\[
  e=\delta+\varepsilon,\qquad
  \mathcal A_n=M_n\otimes\mathcal A,\qquad
  u_T:=\widetilde T=\operatorname{Co}_T(T).
\]
For compatible amplified rectangular corners, \(A\cdot B\) denotes the
amplified compressed product. The symbol \(\|\cdot\|\) always denotes the
appropriate ambient operator-space norm \(\|\cdot\|_{p,q}\). In particular:

- \(Z,W\) in square \(n\)-amplified corners carry the level-\(n\) ambient
  norm;
- a column \(X\in M_{n,1}\otimes\mathcal S_{T,Q}\) carries the rectangular
  ambient norm \(\|X\|_{n,1}\);
- the column Hilbert norm is
  \[
    q_T(X):=\|X\|_{\rm Euc}
      =\left(\sum_i\langle X_i,X_i\rangle\right)^{1/2};
  \]
- the norm of \(h_n(Z)\) is the operator norm from the \(q_R\)-Hilbert
  column to the \(q_P\)-Hilbert column.

All rectangular products below may be embedded as single blocks in a square
matrix algebra \(M_N\otimes\mathcal A\). Ruan's corner axiom makes those
embeddings isometric. Thus the \(\varepsilon\)-\(C^*\) axioms apply with
their original constants and no factor depending on \(N\).

### 1.2 Normalized sanctioned estimates

After enlarging \(C_{\rm co}\) once, COMP-CB gives, at every compatible
rectangular amplification,
\[
\begin{aligned}
 \|A\cdot B-AB\|
   &\le C_{\rm co}e\|A\|\|B\|,\\
 \|u_T\cdot A-A\|+\|A\cdot u_R-A\|
   &\le 2C_{\rm co}e\|A\|,\\
 \bigl|\|u_T\|-1\bigr|&\le C_{\rm co}e.
\end{aligned}
\tag{1.1}
\]
The second line means that each of its two summands is bounded by
\(C_{\rm co}e\|A\|\). Corrected COL-HILB gives
\[
  \bigl|q_T(X)^2-\|X\|_{n,1}^2\bigr|
     \le C_{\rm col}e\|X\|_{n,1}^2.
\tag{1.2}
\]
Let \(e_{\rm in}>0\) be a common universal threshold on which these
sanctioned estimates hold. For the rest of the proof set
\[
  c=\max\{1,C_{\rm co},C_{\rm col},e_{\rm in}^{-1}\}
\]
and assume \(e\le e_H\). In particular, \(ce\le10^{-4}\). We will repeatedly
use the harmless consequences
\[
\begin{aligned}
 (1-ce)\|X\|^2&\le q_T(X)^2\le(1+ce)\|X\|^2,\\
 \sqrt{\frac{1+ce}{1-ce}}&\le2,\\
 \|A\cdot B\|&\le2\|A\|\|B\|.
\end{aligned}
\tag{1.3}
\]

## 2. Counterexample audit before assembly

### 2.1 The literal unconditional inverse clause is false

Let
\[
  \mathcal A=\mathbb C\oplus\mathbb C,\qquad
  P=(1,1),\qquad Q=(1,0)
\]
with its exact \(C^*\)-algebra structure and canonical matrix norms. Then
\(\delta=\varepsilon=0\), \(Q\) is one-dimensional,
\[
  \mathcal S_P=\mathbb C\oplus\mathbb C,\qquad
  \mathcal S_{P,Q}=\mathbb C\oplus0.
\]
Exact `Ha_def` is ordinary left multiplication, hence
\[
  h_{P,P}(a,b)(x,0)=(ax,0).
\]
Thus \(h_{P,P}(0,1)=0\). There can be no unconditional lower norm or inverse
estimate for \(h_{P,P}\), even at \(n=1\).

This does not refute the H-CB input actually used by `lem_extension`. At
`tex:1391`, the source first proves that its particular \(h_{11}\) is a
level-one isomorphism. What remains to be supplied is the passage from that
fixed level-one lower bound to all amplifications. Section 7.3 supplies it.

### 2.2 Search for an \(n\)-growth counterexample

The two plausible amplification mechanisms do not produce one:

1. An exotic column norm cannot separate from the scalar Hilbert norm by a
   growing factor, because corrected COL-HILB is the uniform squared estimate
   (1.2).
2. In the special \(P,Q\) corner, a square matrix \(Z\) cannot have large
   ambient norm but small column action: \(Z^\dagger\cdot Z\) is exactly a
   scalar Gram matrix tensored with \(u_Q\). Section 8.2 makes this
   quantitative using one \(C^*\)-axiom at level \(n\).

At \(e=0\), the variational identity in Section 5 reduces \(h_n(Z)X\) exactly
to \(Z\cdot X\), so there is no exact-algebra family with constants growing
in \(n\). The only counterexample found is the necessary kernel example
above.

## 3. HCB-0 — a uniform compressed-associator bound

For any compatible amplified rectangular corners,
\[
  \|(A\cdot B)\cdot C-A\cdot(B\cdot C)\|
   \le C_{\rm as}e\|A\|\|B\|\|C\|,
  \qquad C_{\rm as}:=9c.
\tag{3.1}
\]

Indeed, insert the five intermediate terms
\[
\begin{aligned}
(A\cdot B)\cdot C
&\longrightarrow (A\cdot B)C
\longrightarrow (AB)C\\
&\longrightarrow A(BC)
\longrightarrow A(B\cdot C)
\longrightarrow A\cdot(B\cdot C).
\end{aligned}
\]
The two outer compression errors are each at most
\(2ce\|A\|\|B\|\|C\|\), by (1.1) and the last inequality of (1.3).
The two inner replacement errors are each at most
\((1+\varepsilon)ce\|A\|\|B\|\|C\|\le2ce\|A\|\|B\|\|C\|\).
The middle ambient associator is at most
\(\varepsilon\|A\|\|B\|\|C\|\le e\|A\|\|B\|\|C\|\).
Their sum is at most \((8c+1)e\le9ce\), proving (3.1).

This is the only associator estimate used below.

## 4. HCB-1a — the exact amplified variational identity

Write \(h_{P,R}=\operatorname{Ha}^Q_{P,R}\) and
\(h_{P,R,n}=1_{M_n}\otimes h_{P,R}\). For
\[
 Z\in M_n\otimes\mathcal S_{P,R},\quad
 X\in M_{n,1}\otimes\mathcal S_{R,Q},\quad
 Y\in M_{n,1}\otimes\mathcal S_{P,Q},
\]
the level-one identity `Ha_def` (`tex:1147-1150`), summed algebraically over
the matrix indices, gives
\[
  (Y^\dagger\cdot Z)\cdot X+Y^\dagger\cdot(Z\cdot X)
   =2\langle Y,h_{P,R,n}(Z)X\rangle\,u_Q.
\tag{4.1}
\]
There is no estimate and no triangle inequality in this summation. It is
just matrix multiplication combined with bilinearity of the compressed
products.

Because \(Q\) is one-dimensional at level one,
\[
  Y^\dagger\cdot V=\langle Y,V\rangle u_Q
\tag{4.2}
\]
for all \(Q\)-columns \(Y,V\); this is the exact amplified column identity
at `tex:1547-1550`. Taking \(V=Z\cdot X\) in (4.2) and subtracting it twice
from (4.1) yields
\[
\boxed{
  2\langle Y,h_{P,R,n}(Z)X-Z\cdot X\rangle u_Q
   =(Y^\dagger\cdot Z)\cdot X-Y^\dagger\cdot(Z\cdot X).
}
\tag{4.3}
\]
The right side is one whole compressed associator.

## 5. HCB-1b — column action is uniformly close to multiplication

Put
\[
  D=h_{P,R,n}(Z)X-Z\cdot X
\]
and take \(Y=D\) in (4.3). Positivity of the column inner product and
(1.2) give
\[
  2q_P(D)^2\|u_Q\|
  \le C_{\rm as}e\|D\|\|Z\|\|X\|.
\tag{5.1}
\]
Using \(\|u_Q\|\ge1-ce\) and both sides of (1.3), then cancelling
\(\|D\|\) (the case \(D=0\) is immediate), gives
\[
\boxed{
 q_P\!\left(h_{P,R,n}(Z)X-Z\cdot X\right)
 \le C_{\rm act}e\|Z\|q_R(X),
 \qquad C_{\rm act}:=18c.
}
\tag{5.2}
\]
For completeness, the coefficient before \(C_{\rm as}\) produced by the
conversion is
\[
  \frac{\sqrt{1+ce}}{2(1-ce)^{5/2}}<2,
\]
so \(C_{\rm act}=2C_{\rm as}=18c\) is valid.

Also, (1.1)--(1.3) imply the whole-column multiplication estimate
\[
  q_P(Z\cdot X)\le4\|Z\|q_R(X).
\tag{5.3}
\]
Consequently,
\[
  \|h_{P,R,n}(Z)\|_{\rm op}
   \le(4+C_{\rm act}e)\|Z\|\le5\|Z\|.
\tag{5.4}
\]
Equations (5.2)--(5.4) contain no sum of norms of matrix entries.

## 6. HCB-2 — adjointness and the product defect

### 6.1 Exact amplified adjointness

The \((i,j)\) block of the Hilbert-space adjoint of
\(h_{P,R,n}(Z)\) is \(h_{P,R}(Z_{ji})^\dagger\). By the exact level-one
identity `Ha_dag` (`tex:1151-1153`), this equals
\(h_{R,P}(Z_{ji}^\dagger)\), the \((i,j)\) block of
\(h_{R,P,n}(Z^\dagger)\). Therefore
\[
\boxed{
 h_{P,R,n}(Z)^\dagger=h_{R,P,n}(Z^\dagger)
}
\tag{6.1}
\]
exactly, for every \(n\).

### 6.2 Uniform product estimate

Fix \(q_R(X)=1\). Insert compressed multiplication between the two terms:
\[
\begin{aligned}
&h_{P,R,n}(Z\cdot W)X-h_{P,S,n}(Z)h_{S,R,n}(W)X\\
={}&[h_{P,R,n}(Z\cdot W)X-(Z\cdot W)\cdot X]\\
&+[(Z\cdot W)\cdot X-Z\cdot(W\cdot X)]\\
&+[Z\cdot(W\cdot X)-Z\cdot(h_{S,R,n}(W)X)]\\
&+[Z\cdot(h_{S,R,n}(W)X)-h_{P,S,n}(Z)h_{S,R,n}(W)X].
\end{aligned}
\tag{6.2}
\]
By (5.2), (3.1), (5.3), and (5.4), the four lines on the right are bounded,
respectively, by
\[
  2C_{\rm act}e,\qquad
  2C_{\rm as}e,\qquad
  4C_{\rm act}e,\qquad
  5C_{\rm act}e
\]
times \(\|Z\|\|W\|\). Hence
\[
\boxed{
\begin{aligned}
&\|h_{P,R,n}(Z\cdot W)
 -h_{P,S,n}(Z)h_{S,R,n}(W)\|_{\rm op}\\
&\hspace{25mm}\le C_{\rm prod}e\|Z\|\|W\|,
\qquad C_{\rm prod}:=24C_{\rm as}=216c.
\end{aligned}}
\tag{6.3}
\]
This proves the amplified `Ha_prod` estimate without expanding a matrix
product into its \(n\) summands.

## 7. HCB-3 — diagonal maps, norms, and the necessary inverse hypothesis

### 7.1 Unit estimate

For \(X\in M_{n,1}\otimes\mathcal S_{P,Q}\), (5.2), (1.1), and
\(\|u_P\|\le1+ce\le2\) give
\[
\begin{aligned}
q_P(h_{P,P,n}(I_n\otimes u_P)X-X)
&\le 2C_{\rm act}e\,q_P(X)+2ce\,q_P(X).
\end{aligned}
\]
Thus
\[
\boxed{
 \|h_{P,P,n}(I_n\otimes u_P)-I\|_{\rm op}
 \le C_{\rm unit}e,\qquad C_{\rm unit}:=38c.
}
\tag{7.1}
\]
Together, (6.1), (6.3), and (7.1) say that \(h_{P,P}\) is an extended
\(C_{\rm prod}e\)-homomorphism.

### 7.2 Uniform upper norm

The compressed product and the ambient \(C^*\)-axiom give
\[
 (1-2ce)\|Z\|^2
 \le\|Z^\dagger\cdot Z\|
 \le(1+2ce)\|Z\|^2.
\tag{7.2}
\]
Let \(b_n=\|h_{P,P,n}\|\). Exact adjointness and (6.3) imply
\[
 b_n^2\le b_n(1+2ce)+C_{\rm prod}e.
\tag{7.3}
\]
The positive root of this quadratic is at most
\[
 1+(2c+C_{\rm prod})e.
\]
Therefore
\[
\boxed{
 \|h_{P,P,n}(Z)\|_{\rm op}
 \le(1+C_{\rm up}e)\|Z\|,
 \qquad C_{\rm up}:=218c.
}
\tag{7.4}
\]

### 7.3 Complete lower and inverse bound from a level-one lower bound

This paragraph states the hypothesis that the exact direct-sum counterexample
shows is necessary. Suppose
\[
 a_1:=\inf_{Z\ne0}
 \frac{\|h_{P,P}(Z)\|_{\rm op}}{\|Z\|}\ge\frac14.
\tag{7.5}
\]
For general \(n\), define \(a_n\) analogously. Ruan's two-by-two block
estimate gives
\[
 a_{2n}\ge\frac12a_n.
\tag{7.6}
\]
Indeed, writing a \(2n\)-matrix as four \(n\)-blocks gives
\(\|Z\|_{2n}\le2\max_{ij}\|Z_{ij}\|_n\), while compression onto a target
block gives
\(\|h_{2n}(Z)\|\ge\max_{ij}\|h_n(Z_{ij})\|\).

On the other hand, exact adjointness, (6.3), and the lower half of (7.2)
give
\[
 a_n^2\ge a_n(1-2ce)-C_{\rm prod}e.
\tag{7.7}
\]
The smaller root of the associated quadratic is at most
\(3C_{\rm prod}e<1/8\). Therefore (7.5) puts \(a_1\) above the smaller root,
and (7.7) puts it above the larger root:
\[
 a_1\ge1-C_{\rm diag}e,\qquad
 C_{\rm diag}:=2c+3C_{\rm prod}=650c.
\tag{7.8}
\]
Equations (7.6)--(7.7) now induct on powers of two: after (7.8), the next
pre-bootstrap value is at least
\((1-C_{\rm diag}e)/2>1/8\), hence is again on the upper-root branch.
Monotonicity under the standard matrix inclusions handles arbitrary \(n\).
Thus
\[
\boxed{
 \|h_{P,P,n}(Z)\|_{\rm op}
 \ge(1-C_{\rm diag}e)\|Z\|\quad(n\ge1).
}
\tag{7.9}
\]
If \(h_{P,P}\) is bijective at level one, all its amplifications are
bijective and
\[
\boxed{
 \|h_{P,P,n}^{-1}\|
 \le\frac1{1-C_{\rm diag}e}
 \le1+1300ce.
}
\tag{7.10}
\]

### 7.4 Off-diagonal inverse propagation used in `lem_extension`

The same argument supplies the four corner inverses needed after the source's
level-one dimension calculation. Suppose the diagonal anchor \(h_{R,R}\)
satisfies (7.5), and \(h_{P,R}\) is bijective at level one. From (6.1),
(6.3), (7.2), and (7.9),
\[
\begin{aligned}
\|h_{P,R,n}(Z)\|_{\rm op}^2
&\ge\|h_{R,R,n}(Z^\dagger\cdot Z)\|_{\rm op}
       -C_{\rm prod}e\|Z\|^2\\
&\ge(1-868ce)\|Z\|^2.
\end{aligned}
\tag{7.11}
\]
Hence
\[
 \|h_{P,R,n}(Z)\|_{\rm op}\ge(1-868ce)\|Z\|,
 \qquad
 \|h_{P,R,n}^{-1}\|\le1+1736ce.
\tag{7.12}
\]
The analogous upper estimate is
\(\|h_{P,R,n}(Z)\|\le(1+654ce)\|Z\|\).
Thus the source's *level-one* bijectivity of the four \(h_{jk}\), once
obtained, has dimension-free complete inverse bounds. No inverse is asserted
without that necessary level-one hypothesis.

## 8. HCB-4 — the two special maps

### 8.1 Canonical identity maps

The level-one space \(\mathcal S_{Q,Q}\) is
\(\mathbb C u_Q\). Let
\[
  \alpha=q_Q(u_Q),\qquad q_0=\alpha^{-1}u_Q.
\]
Then \(q_0\) is a unit Hilbert vector. From (1.1)--(1.2),
\[
  |\alpha-1|\le2ce,\qquad
  |\alpha^{-1}-1|\le3ce.
\tag{8.1}
\]

After identifying \(\mathcal S_{Q,Q}\) with \(\mathbb C\) by
\(q_0\leftrightarrow1\), define
\[
\begin{aligned}
J_{P,Q,n}:M_n\otimes\mathcal S_{P,Q}
 &\longrightarrow
 \mathcal B(\mathbb C^n,\mathbb C^n\otimes\mathcal S_{P,Q}),\\
[J_{P,Q,n}(Z)c]_i&=\sum_j Z_{ij}c_j.
\end{aligned}
\tag{8.2}
\]
Define the row identification by adjunction,
\[
 J_{Q,P,n}(Z)=J_{P,Q,n}(Z^\dagger)^\dagger.
\tag{8.3}
\]
These are the canonical identity identifications used below.

### 8.2 The Gram estimate: the canonical maps are complete near-isometries

For \(Z\in M_n\otimes\mathcal S_{P,Q}\), let
\[
  G=J_{P,Q,n}(Z)^\dagger J_{P,Q,n}(Z)\in M_n.
\]
The exact column inner-product identity gives
\[
  Z^\dagger\cdot Z=G\otimes u_Q.
\tag{8.4}
\]
Ruan's scalar tensor identity (`tex:1475`) gives
\[
 \|G\otimes u_Q\|_n=\|G\|\,\|u_Q\|.
\tag{8.5}
\]
Meanwhile COMP-CB and the \(\varepsilon\)-\(C^*\) axiom in
\(M_n\otimes\mathcal A\) give
\[
 \left|\|Z^\dagger\cdot Z\|-\|Z\|^2\right|
 \le2ce\|Z\|^2.
\tag{8.6}
\]
Combining (8.4)--(8.6) with
\(|\|u_Q\|-1|\le ce\) yields
\[
\boxed{
 (1-4ce)\|Z\|
 \le\|J_{P,Q,n}(Z)\|_{\rm op}
 \le(1+4ce)\|Z\|.
}
\tag{8.7}
\]
The same holds for \(J_{Q,P,n}\) by adjunction. This is the step that rules
out an operator-space norm hidden from column action.

### 8.3 Complete closeness of the Ha maps to the identities

Let \(V=(c_jq_0)_j\) with \(q_Q(V)=\|c\|_2\). Equation (5.2) gives
\[
 q_P(h_{P,Q,n}(Z)V-Z\cdot V)
 \le C_{\rm act}e\|Z\|\|c\|_2.
\tag{8.8}
\]
Since
\[
 Z\cdot V=\alpha^{-1}(Zc)\cdot u_Q,
\]
the right-unit estimate (1.1), (8.1), corrected COL-HILB, and Ruan's
inequality \(\|Zc\|_{n,1}\le\|Z\|\|c\|_2\) give
\[
 q_P(Z\cdot V-J_{P,Q,n}(Z)c)
 \le16ce\|Z\|\|c\|_2.
\tag{8.9}
\]
Therefore
\[
\boxed{
 \|h_{P,Q,n}(Z)-J_{P,Q,n}(Z)\|_{\rm op}
 \le C_{\rm sp}e\|Z\|,
 \qquad C_{\rm sp}:=40c.
}
\tag{8.10}
\]
Exact adjointness (6.1) and (8.3) give the same estimate for \(h_{Q,P,n}\).
Equivalently,
\[
\boxed{
\begin{aligned}
\|h_{Q,P,n}(Z)-J_{Q,P,n}(Z)\|_{\rm op}
 &\le40ce\|Z\|.
\end{aligned}}
\tag{8.11}
\]

Combining (8.7) with (8.10)--(8.11) gives the complete norm bounds
\[
 (1-44ce)\|Z\|\le\|h_{P,Q,n}(Z)\|
 \le(1+44ce)\|Z\|,
\tag{8.12}
\]
and likewise for \(h_{Q,P,n}\). The maps are therefore bijective and a
Neumann estimate gives
\[
\begin{aligned}
 \|h_{P,Q,n}^{-1}\|,\ \|h_{Q,P,n}^{-1}\|
   &\le1+88ce,\\
 \|h_{P,Q,n}^{-1}-J_{P,Q,n}^{-1}\|,\
 \|h_{Q,P,n}^{-1}-J_{Q,P,n}^{-1}\|
   &\le160ce.
\end{aligned}
\tag{8.13}
\]
All four estimates are uniform in \(n\).

## 9. Contract reconciliation

With \(C_H,e_H\) from (0.1), the following hold simultaneously for every
\(n\ge1\):

1. Exact amplified adjointness is (6.1).
2. The amplified product defect is (6.3), bounded by
   \(C_He\|Z\|\|W\|\).
3. The map \(h_{P,P}\) is an extended \(C_He\)-homomorphism by
   (6.1), (6.3), and (7.1), with complete upper norm (7.4). If its
   level-one lower bound is at least \(1/4\) and it is bijective—as is
   established separately for \(h_{11}\) in the source's extension
   argument—then (7.9)--(7.10) give the required complete inverse estimate.
   The four corner inverses then obey (7.12).
4. The maps \(h_{P,Q}\) and \(h_{Q,P}\) are completely
   \(C_He\)-close to their canonical identity identifications by
   (8.10)--(8.11), and their complete norm and inverse estimates are
   (8.12)--(8.13).

Thus the \(n\)-uniform analytic content of H-CB closes. The exact
\(\mathbb C\oplus\mathbb C\) example shows why item (3) must not be read as
asserting an inverse for an arbitrary \(h_{P,P}\) before the source's
level-one faithfulness argument.

## 10. Constant ledger

| Constant | Value used here | Producing inequality | Dependence |
|---|---:|---|---|
| \(C_{\rm co}\) | sanctioned | COMP-CB product, unit, and \(u_T\)-norm estimates (1.1) | universal only |
| \(C_{\rm col}\) | sanctioned | corrected COL-HILB (1.2) | universal only |
| \(e_{\rm in}\) | sanctioned common validity threshold | COMP-CB and COL-HILB input range | universal only |
| \(c\) | \(\max\{1,C_{\rm co},C_{\rm col},e_{\rm in}^{-1}\}\) | normalization | universal only |
| \(C_{\rm as}\) | \(9c\) | five-term compressed associator, (3.1) | universal only |
| \(C_{\rm act}\) | \(18c\) | variational identity plus COL-HILB, (5.2) | universal only |
| crude action bound | \(5\) | (5.3)--(5.4) | none |
| \(C_{\rm prod}\) | \(216c\) | four-term product comparison, (6.2)--(6.3) | universal only |
| \(C_{\rm unit}\) | \(38c\) | action plus compressed-unit defect, (7.1) | universal only |
| \(C_{\rm up}\) | \(218c\) | \(C^*\) square bootstrap, (7.3)--(7.4) | universal only |
| \(C_{\rm diag}\) | \(650c\) | lower-root bootstrap, (7.7)--(7.9) | universal only |
| diagonal inverse | \(1300c\) | Neumann/geometric bound, (7.10) | universal only |
| rectangular lower | \(868c\) | diagonal anchor plus product defect, (7.11) | universal only |
| rectangular inverse | \(1736c\) | (7.12) | universal only |
| canonical \(J\) distortion | \(4c\) | Gram identity, (8.4)--(8.7) | universal only |
| \(C_{\rm sp}\) | \(40c\) | action, unit, and normalization, (8.8)--(8.11) | universal only |
| special inverse difference | \(160c\) | Neumann resolvent identity, (8.13) | universal only |
| \(C_H\) | \(4000c\) | common domination | universal only |
| \(e_H\) | \(1/(10000c)\) | all denominators, roots, and Neumann bounds | universal only |

No ledger entry depends on \(n\), \(\dim\mathcal A\), a block count, or a
block dimension.

## 11. Hypothesis hygiene

### 11.1 Where one-dimensionality of \(Q\) is used

It is used exactly in the following places:

1. to define the level-one Hilbert inner products and the maps
   \(\operatorname{Ha}^Q_{P,R}\) (`tex:1123-1160`);
2. to obtain the exact column identity (4.2);
3. to identify \(\mathcal S_{Q,Q}=\mathbb C u_Q\);
4. to scalarize \(Z^\dagger\cdot Z\) as the Gram matrix
   \(G\otimes u_Q\) in (8.4).

It is never asserted that \(I_n\otimes Q\) is one-dimensional, and
`lem_PQ_Hilb` is never applied to \(I_n\otimes Q\).

### 11.2 Where the \(\varepsilon\)-\(C^*\) axioms are used

1. Ambient submultiplicativity and associativity are used in Section 3 after
   embedding each rectangular chain in one square
   \(M_N\otimes\mathcal A\).
2. The \(C^*\) lower and upper square estimates are used at level \(n\) in
   (7.2) and (8.6).
3. Ruan's matrix axioms are used for all rectangular embeddings, for
   (7.6), and for the exact scalar tensor norm (8.5).
4. Corrected COL-HILB, whose sanctioned proof uses the
   \(\varepsilon\)-\(C^*\) axiom in \(M_{n+1}\otimes\mathcal A\), is imported
   only through (1.2).

Every use is at one whole amplification level. No estimate sums the norms of
the \(n\) entries of a column.

## 12. DEFECT REGISTER — LOUD

1. **UNCONDITIONAL INVERSE FOR \(h_{P,P}\) IS FALSE.** Section 2.1 gives
   an exact \(\mathbb C\oplus\mathbb C\) counterexample. The corrected
   inverse statement is conditional on a fixed level-one lower bound and
   bijectivity. This is the form consumed by `lem_extension`.

2. **THE INPUT CONSTANTS AND THRESHOLDS ARE NOT NUMERICAL.** The supplied
   TeX and the sanctioned COMP-CB/COL-HILB contracts contain unnamed
   universal big-\(O\) constants and implicit universal smallness
   thresholds. Formula (0.1) is explicit in those sanctioned inputs, but no
   absolute decimal \(C_H\) can honestly be extracted without first
   numerically expanding them.

3. **COMP-CB NORMALIZATION.** I used its stated common constant after
   enlarging it to dominate the two compressed-unit estimates and
   \(|\|u_T\|-1|\) in (1.1). If a later registry contract exposes separate
   constants for those estimates, replace \(c\) by their maximum; no other
   line changes.

4. **NO CLAIM ABOUT EXT-CB.** This report supplies the complete Ha estimates
   and the conditional corner-inverse propagation only. It does not check
   the separate construction of the single level-one unitary \(U_1\), the
   approximation step, or the final merging argument.

5. **NO SELF-CERTIFICATION.** All conclusions above remain unverified prover
   output until attacked by a separate fresh verifier.
