# PROOF — Route F F2/F3 stochastic-retract bridge

**Prover disposition:** **F2 CLOSED; F3 CLOSED.**  The permitted material
supports the advertised retract constant
\(3K\eta/(1-3K\eta)\) exactly.  These are fresh-prover paper proofs, not
independently reviewed or L0-rigorous results.

## 0. The two contracts

**F2 contract.** Let \(K\ge1\) be a dimension-independent constant, let \(n\ge1\), let \(Q:\ell_\infty^n\to\ell_\infty^n\) be row-stochastic, let \(D:M_n\to\ell_\infty^n\) be diagonal extraction and \(J:\ell_\infty^n\to M_n\) diagonal inclusion, put \(\Phi=JQD\), let \(\mathcal B\) be a finite-dimensional unital \(C^*\)-algebra, and let \(\Delta:\mathcal B\to M_n\) and \(\Upsilon:M_n\to\mathcal B\) be UCP maps; if \(0\le\eta\le\min\{(24K)^{-1},1\}\), \(\|\Delta\Upsilon-\Phi\|_{\rm cb}\le K\eta\), \(\|\Upsilon\Delta-I_{\mathcal B}\|_{\rm cb}\le K\eta\), and \(\|\Upsilon(\Delta x\,\Delta y)-xy\|\le K\eta\|x\|\|y\|\) for all \(x,y\in\mathcal B\), then \(\mathcal B\) is commutative and there are \(k\ge1\) and a unital \(*\)-isomorphism \(\iota:\ell_\infty^k\to\mathcal B\) such that \(A:=D\Delta\iota:\ell_\infty^k\to\ell_\infty^n\) and \(M:=\iota^{-1}\Upsilon J:\ell_\infty^n\to\ell_\infty^k\) are positive unital maps satisfying \(\|Q-AM\|_{\infty\to\infty}\le K\eta\), \(\|QA-A\|_{\infty\to\infty}\le2K\eta\), and \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\) for every \(x\in\ell_\infty^k\).

**F3 contract.** Let \(K\ge1\) be a dimension-independent constant, let \(n,k\ge1\), let \(A:\ell_\infty^k\to\ell_\infty^n\) and \(M:\ell_\infty^n\to\ell_\infty^k\) be positive unital maps, let \(Q:\ell_\infty^n\to\ell_\infty^n\) be row-stochastic, and let \(\eta\ge0\) satisfy \(3K\eta<1\); if \(\|Q-AM\|_{\infty\to\infty}\le K\eta\), \(\|QA-A\|_{\infty\to\infty}\le2K\eta\), and \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\) for every \(x\in\ell_\infty^k\), then \(\|MA-I_k\|_{\infty\to\infty}\le3K\eta/(1-3K\eta)\).

## 1. F2 setup and proof

### 1.1 Source loci and scope

The extraction uses only:

- `AUDIT-W73B-ROUTE-F.md` Q4 for \(D,J,\Phi=JQD\), and Q5(a)--(e)
  for the \(2,8,10,3\) estimates and the definitions of \(A,M\);
- `LEDGER-W74F-G-K.md` (3.2)--(3.3) for one common, finite,
  dimension-free \(K\), and (4.2) for the compatible threshold
  \(\eta\le(24K)^{-1}\);
- the standard finite-dimensional \(C^*\)-algebra decomposition, with the
  only quantitative noncommutative-block calculation reproduced below.

The three displayed factorization estimates are hypotheses of the contract.
Thus this bridge neither assumes that a quarantined ledger row has already
proved them nor imports any proof claim from the Kitaev source.

### 1.2 Approximate invariance of \(\Delta\)

The row-stochastic \(Q\) is positive unital on the commutative algebra
\(\ell_\infty^n\), hence completely positive; \(D\) and \(J\) are UCP.
Therefore \(\Phi=JQD\) is UCP.
UCP maps are completely contractive, so
\(\|\Delta\|_{\rm cb}=\|\Upsilon\|_{\rm cb}=1\).  Hence
\[
\begin{aligned}
\|\Phi\Delta-\Delta\|_{\rm cb}
&\le
  \|(\Phi-\Delta\Upsilon)\Delta\|_{\rm cb}
  +\|\Delta(\Upsilon\Delta-I_{\mathcal B})\|_{\rm cb}\\
&\le 2K\eta.
\end{aligned}
\tag{1.1}
\]
This is exactly the fixed-length telescope in W73b Q5(a).

### 1.3 Quantitative commutativity forcing

Take contractions \(x,y\in\mathcal B\), and set
\[
a=\Delta x,\qquad b=\Delta y,\qquad
a_0=\Phi\Delta x,\qquad b_0=\Phi\Delta y.
\]
All four are contractions.  The range of \(\Phi=JQD\) consists of diagonal
matrices, so \([a_0,b_0]=0\).  By (1.1),
\[
\|a-a_0\|,\ \|b-b_0\|\le2K\eta.
\]
Consequently
\[
\begin{aligned}
\|[\Delta x,\Delta y]\|
&\le
  \|[a-a_0,b]\|+\|[a_0,b-b_0]\|\\
&\le
  2\|a-a_0\|\|b\|+2\|a_0\|\|b-b_0\|\\
&\le8K\eta.
\end{aligned}
\tag{1.2}
\]
Applying the assumed multiplicativity estimate in the two orders and using
\(\|\Upsilon\|=1\) gives
\[
\begin{aligned}
\|[x,y]\|
&\le
 \|xy-\Upsilon(\Delta x\,\Delta y)\|
 +\|\Upsilon([\Delta x,\Delta y])\|\\
&\qquad
 +\|\Upsilon(\Delta y\,\Delta x)-yx\|\\
&\le K\eta+8K\eta+K\eta
=10K\eta.
\end{aligned}
\tag{1.3}
\]

For completeness, if a finite-dimensional \(C^*\)-algebra is
noncommutative, one of its simple summands is \(M_d\) with \(d\ge2\).
In a \(2\times2\) corner of that summand, the contractions
\[
u=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
v=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]
have \(\|[u,v]\|=2\); extending them by zero preserves this norm.  But the
contract threshold gives
\[
10K\eta\le\frac{10}{24}=\frac5{12}<2,
\]
contradicting (1.3).  Therefore \(\mathcal B\) is commutative.

There are consequently \(k\ge1\) and a unital \(*\)-isomorphism
\(\iota:\ell_\infty^k\to\mathcal B\).

### 1.4 Positive-unital compression and the factor error

Define
\[
A:=D\Delta\iota,
\qquad
M:=\iota^{-1}\Upsilon J.
\tag{1.4}
\]
The maps \(D,J,\Delta,\Upsilon,\iota,\iota^{-1}\) are positive and unital
(indeed completely positive where applicable), so \(A\) and \(M\) are
positive unital maps of the required orientations.

Since \(DJ=I_{\ell_\infty^n}\) and \(\Phi=JQD\),
\[
\begin{aligned}
AM-Q
&=D\Delta\iota\iota^{-1}\Upsilon J-Q\\
&=D(\Delta\Upsilon-\Phi)J.
\end{aligned}
\]
Both \(D\) and \(J\) are contractions, whence
\[
\|AM-Q\|_{\infty\to\infty}\le K\eta.
\tag{1.5}
\]

Similarly, \(D\Phi=Q D\), so (1.1) yields
\[
QA-A=D(\Phi\Delta-\Delta)\iota
\quad\Longrightarrow\quad
\|QA-A\|_{\infty\to\infty}\le2K\eta.
\tag{1.6}
\]

### 1.5 Lower modulus of \(A\)

For \(x\in\ell_\infty^k\), the approximate-left-inverse estimate and the
contractivity of \(\Upsilon\) give
\[
\begin{aligned}
\|x\|_\infty
=\|\iota x\|
&\le\|\Upsilon\Delta\iota x\|+K\eta\|x\|_\infty\\
&\le\|\Delta\iota x\|+K\eta\|x\|_\infty.
\end{aligned}
\]
Thus
\[
\|\Delta\iota x\|\ge(1-K\eta)\|x\|_\infty.
\tag{1.7}
\]
On the other hand, (1.1), the identity
\(\Phi\Delta\iota=JQA\), the isometry of \(J\), and the contractivity of the
row-stochastic map \(Q\) imply
\[
\begin{aligned}
\|\Delta\iota x\|
&\le\|\Phi\Delta\iota x\|+2K\eta\|x\|_\infty\\
&=\|JQAx\|+2K\eta\|x\|_\infty\\
&\le\|Ax\|_\infty+2K\eta\|x\|_\infty.
\end{aligned}
\tag{1.8}
\]
Combining (1.7) and (1.8) proves
\[
\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty,
\tag{1.9}
\]
and completes F2.

## 2. F3 setup and proof

### 2.1 Source loci and scope

This is the argument in `AUDIT-W73B-ROUTE-F.md` Q5(e), with all of its inputs
promoted into the closed F3 hypothesis block.  Its threshold is precisely
\(3K\eta<1\); no UCP, cb-norm, source-theorem, or quarantined-ledger claim is
used inside this step.

### 2.2 Retract-defect estimate

A positive unital map between unital \(C^*\)-algebras has norm one, so
\(\|A\|_{\infty\to\infty}=1\).  For every \(x\in\ell_\infty^k\),
\[
\begin{aligned}
A(MA-I_k)x
&=AMAx-Ax\\
&=(AM-Q)Ax+(QA-A)x.
\end{aligned}
\]
Since \(\|AM-Q\|=\|Q-AM\|\), the F3 hypotheses therefore give
\[
\|A(MA-I_k)x\|_\infty
\le K\eta\|Ax\|_\infty+2K\eta\|x\|_\infty
\le3K\eta\|x\|_\infty.
\tag{2.1}
\]
Apply the assumed lower modulus of \(A\) to
\((MA-I_k)x\):
\[
(1-3K\eta)\|(MA-I_k)x\|_\infty
\le\|A(MA-I_k)x\|_\infty.
\tag{2.2}
\]
Because \(3K\eta<1\), division of (2.1)--(2.2) proves
\[
\boxed{
\|MA-I_k\|_{\infty\to\infty}
\le\frac{3K\eta}{1-3K\eta}.
}
\tag{2.3}
\]
This is the advertised bound, with no constant change.

## 3. Composition check against `lem-routef-prh-finish`

Assume the F2 hypothesis block.  F2 produces:

1. \(k\ge1\) and positive unital maps
   \(A:\ell_\infty^k\to\ell_\infty^n\) and
   \(M:\ell_\infty^n\to\ell_\infty^k\);
2. \(\|Q-AM\|_{\infty\to\infty}\le K\eta\);
3. \(\|QA-A\|_{\infty\to\infty}\le2K\eta\);
4. \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\) for all \(x\).

Moreover,
\[
3K\eta\le\frac18<1,
\]
so these outputs meet every F3 hypothesis.  F3 adds
\[
\|MA-I_k\|_{\infty\to\infty}
\le\frac{3K\eta}{1-3K\eta}.
\]
Together with the F2 inputs that \(Q\) is row-stochastic, \(K\ge1\), and
\(0\le\eta\le\min\{(24K)^{-1},1\}\), this is literally the complete
hypothesis list of `lem-routef-prh-finish`.  That consumer therefore returns
a stochastic idempotent \(E\) with
\[
\|Q-E\|_{\infty\to\infty}
\le(K+4\sqrt{2K})\sqrt\eta.
\]

## 4. Constant and threshold ledger

| item | bound | required threshold | dimension dependence |
|---|---:|---:|---|
| Approximate invariance | \(\|\Phi\Delta-\Delta\|_{\rm cb}\le2K\eta\) | none beyond the three factor estimates | none |
| Image commutator | \(\|[\Delta x,\Delta y]\|\le8K\eta\) for contractions | none | none |
| Algebra commutator | \(\|[x,y]\|\le10K\eta\) for contractions | \(10K\eta<2\) forces commutativity | none |
| Factor compression | \(\|Q-AM\|\le K\eta\) | none | none |
| Compressed invariance | \(\|QA-A\|\le2K\eta\) | none | none |
| Lower modulus | \(\|Ax\|\ge(1-3K\eta)\|x\|\) | positive once \(3K\eta<1\) | none |
| Retract defect | \(\|MA-I_k\|\le3K\eta/(1-3K\eta)\) | \(3K\eta<1\) | none |
| Route F common threshold | \(0\le\eta\le\min\{(24K)^{-1},1\}\) | implies \(10K\eta\le5/12<2\) and \(3K\eta\le1/8\) | none |

For comparison with `LEDGER-W74F-G-K.md` §5, the common threshold also gives
\[
\frac{3K\eta}{1-3K\eta}
\le\frac{24}{7}K\eta
<4K\eta
<\frac12.
\]
Thus the af-validated PRH consumer applies with exactly the ledger's relative
constant, and no unnamed big-\(O\) coefficient occurs in either bridge.

## 5. Hypothesis hygiene

- Every F2 input is quantified in its contract: the dimensions, \(Q,D,J,\Phi\),
  \(\mathcal B,\Delta,\Upsilon,K,\eta\), and all three estimates.
- Every F3 input is quantified in its contract: the dimensions, \(A,M,Q,K,\eta\),
  the denominator guard, the two operator estimates, and the lower modulus.
- F2 uses only the level-one multiplicativity estimate.  The stronger
  all-amplification estimate in ledger (3.2) is not smuggled into the proof.
- Positivity and unitality of both compressed maps are conclusions of F2, not
  inferred from norm bounds.
- The identity used in the lower-modulus proof is
  \(\Phi\Delta=JQD\Delta=JQA\), never the false identity
  \(\Phi\Delta=JA\).
- \(K\) is a named relative constant.  Its upstream existence and threshold
  domain are not reproved here; the contracts state exactly what the bridges
  consume.
- No Kitaev proof claim, quarantined result row, GAP id, numerical experiment,
  or dimension-dependent coordinate sum is an input.

## 6. LOUD defect register

1. **NO F2 MATHEMATICAL GAP FOUND.**  Conditional on the three explicitly
   stated factorization estimates, the positive-unital compression and all
   intermediate bounds are proved above.
2. **NO F3 MATHEMATICAL GAP FOUND.**  The permitted material supports
   \(3K\eta/(1-3K\eta)\) exactly; the constant was not forced or weakened.
3. **UPSTREAM SCOPE DEFECT REMAINS OUTSIDE THESE CONTRACTS.**
   `GAP-LEDGER-DOMAINS` still governs whether the three F2 factorization
   estimates have been produced on one closed common domain.  This proof does
   not close, consume, or disguise that separate gap.
4. **RIGOUR CEILING.**  This fresh-prover artifact is a
   `proved-mod-audit` candidate only.  It requires an independent hostile
   reviewer before registry codification and does not promote Route F or
   `op-classical` to L0.
