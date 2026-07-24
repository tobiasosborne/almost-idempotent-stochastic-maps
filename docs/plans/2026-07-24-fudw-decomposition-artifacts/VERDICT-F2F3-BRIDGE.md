VERDICT: VALID-WITH-CORRECTIONS

# Fresh hostile verification of the Route F F2/F3 bridge

F2: VALID

F3: VALID

Both contracts are closed conditional statements, both proofs are correct, and
their composition supplies the literal hypothesis list of
`lem-routef-prh-finish`.  The overall correction grade is caused by one
endpoint error in the proof's comparison ledger and one stale scope sentence;
neither changes either contract or any constant.

## 1. Inequalities and norms

### Finding 1.1 — PASS

The approximate-invariance telescope is exact:
\[
\Phi\Delta-\Delta
=(\Phi-\Delta\Upsilon)\Delta
+ \Delta(\Upsilon\Delta-I_{\mathcal B}),
\]
and UCP complete contractivity gives
\(\|\Phi\Delta-\Delta\|_{\rm cb}\le2K\eta\).

For contractions \(x,y\), writing
\(a=\Delta x\), \(b=\Delta y\),
\(a_0=\Phi\Delta x\), and \(b_0=\Phi\Delta y\), the range of \(\Phi\)
is diagonal and hence
\[
\|[\Delta x,\Delta y]\|
\le2\|a-a_0\|\|b\|+2\|a_0\|\|b-b_0\|
\le8K\eta.
\]
The two level-one multiplicativity errors and contractivity of \(\Upsilon\)
then give \(\|[x,y]\|\le10K\eta\).  No amplified estimate is silently used.

Compression changes cb norm to the required
\(\ell^\infty\!\to\!\ell^\infty\) operator norm only by contractive
pre- and post-composition:
\[
AM-Q=D(\Delta\Upsilon-\Phi)J,\qquad
QA-A=D(\Phi\Delta-\Delta)\iota.
\]
Thus the constants \(K\eta\) and \(2K\eta\) are correct.  There is no hidden
\(n\)- or \(k\)-dependence.

The lower-modulus calculation is also exact:
\[
\|\Delta\iota x\|\ge(1-K\eta)\|x\|_\infty,\qquad
\|\Delta\iota x\|\le\|Ax\|_\infty+2K\eta\|x\|_\infty,
\]
where the second inequality correctly uses
\(\Phi\Delta\iota=JQA\), the isometry of \(J\), and contractivity of \(Q\).
Hence \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\).

For F3,
\[
A(MA-I_k)x=(AM-Q)Ax+(QA-A)x.
\]
Since a positive unital \(A\) has norm one, the right side has norm at most
\(3K\eta\|x\|_\infty\).  Applying the lower modulus of \(A\) to
\((MA-I_k)x\) and dividing by \(1-3K\eta>0\) proves exactly
\[
\|MA-I_k\|_{\infty\to\infty}
\le\frac{3K\eta}{1-3K\eta}.
\]

### Finding 1.2 — MINOR: the displayed strict chain fails at \(\eta=0\)

`PROOF-F2F3-BRIDGE.md:266-272` writes
\[
\frac{3K\eta}{1-3K\eta}
\le\frac{24}{7}K\eta<4K\eta<\frac12.
\]
The contracts allow \(\eta=0\), where both strict comparisons on the left
become \(0<0\), which is false.  PRH still applies at that endpoint, so this
is not a contract or constant defect.

**Ready-to-paste correction:**

> The common threshold gives
> \[
> \frac{3K\eta}{1-3K\eta}
> \le\frac{24}{7}K\eta
> \le4K\eta
> \le\frac16
> <\frac12.
> \]

This version is valid also at \(\eta=0\).

## 2. F2 commutativity and the isomorphism

### Finding 2.1 — PASS

The stated hypotheses force commutativity.  A noncommutative
finite-dimensional \(C^*\)-algebra has a matrix summand \(M_d\), \(d\ge2\).
Putting the two Pauli contractions in a \(2\times2\) corner and zero in all
other coordinates gives contractions with commutator norm exactly \(2\).
But
\[
10K\eta\le\frac5{12}<2
\]
under the F2 threshold, a contradiction.  Therefore
\(\mathcal B\) is finite-dimensional and commutative, so
\(\mathcal B\cong\ell_\infty^k\) by a unital *-isomorphism \(\iota\).

Both \(\iota\) and \(\iota^{-1}\) are positive unital.  Consequently
\[
A=D\Delta\iota,\qquad M=\iota^{-1}\Upsilon J
\]
have the claimed orientations and are positive unital.  No counterexample
algebra survives the quantitative commutator gap.

## 3. Literal composition into `lem-routef-prh-finish`

### Finding 3.1 — PASS

F2 returns:

1. \(k\ge1\) and positive unital
   \(A:\ell_\infty^k\to\ell_\infty^n\) and
   \(M:\ell_\infty^n\to\ell_\infty^k\);
2. \(\|Q-AM\|_{\infty\to\infty}\le K\eta\);
3. \(\|QA-A\|_{\infty\to\infty}\le2K\eta\);
4. \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\).

The retained F2 inputs give row-stochastic \(Q\), \(K\ge1\), and
\(0\le\eta\le\min\{(24K)^{-1},1\}\).  In particular
\(3K\eta\le1/8<1\), so all F3 hypotheses hold.  F3 returns
\[
\|MA-I_k\|_{\infty\to\infty}
\le\frac{3K\eta}{1-3K\eta}.
\]
These are literally all hypotheses of the registered
`lem-routef-prh-finish`; its quantifiers, threshold, denominator, and
constants match.  The consumer then gives the claimed
\((K+4\sqrt{2K})\sqrt\eta\) bound.

## 4. Permitted-material discipline

### Finding 4.1 — PASS

No theorem or proof claim from the Kitaev source is imported.  The three
factorization estimates are explicit hypotheses of F2 rather than conclusions
borrowed from the source or from a quarantined component row.  The proof uses
only those hypotheses, the canonical \(D,J,\Phi=JQD\) lift, elementary
UCP/positive-unital contractivity, and the standard finite-dimensional
\(C^*\)-algebra decomposition.  The quantitative noncommutative witness is
reproduced in the artifact.

The use of the W74F ledger is limited to compatibility with a common universal
\(K\) and the guard \((24K)^{-1}\); no invalid first-round ledger assertion is
used to prove either conditional bridge.

## 5. Threshold arithmetic

### Finding 5.1 — PASS, subject to Finding 1.2

The required implications are
\[
10K\eta\le\frac5{12}<2,\qquad
3K\eta\le\frac18<1,
\]
and
\[
\frac{3K\eta}{1-3K\eta}
\le4K\eta\le\frac16<\frac12.
\]
They are all dimension-free and sufficient.  No stronger smallness condition
is hidden in F2, F3, or their composition.

## 6. Hypothesis hygiene and scope

### Finding 6.1 — PASS

Every variable and estimate used in each proof occurs in its contract.  F2
uses only level-one multiplicativity even though the upstream ledger supplies
an amplified estimate.  F3 needs no UCP or cb-norm premise.  Every F3
hypothesis is an F2 conclusion or a retained F2 input, so the bridge has no
unsupplied internal hypothesis.

### Finding 6.2 — MINOR: the defect-register scope sentence is stale

`PROOF-F2F3-BRIDGE.md:302-305` says that `GAP-LEDGER-DOMAINS` still governs
whether the three estimates have been produced on one closed common domain.
The later hostile-verified W74F-H Stage-1 repair closed the relative
\(K/\eta_K\) ledger at `proved-mod-audit`, and the registered
`lem-routef-k-ledger` now states the common-domain three-estimate output.
The detailed component-domain sub-DAG remains an af-factoring/seeding concern,
not an unresolved mathematical premise of these bridge contracts.

**Ready-to-paste correction for defect-register item 3:**

> **UPSTREAM REGISTRY SCOPE REMAINS OUTSIDE THESE CONTRACTS.**
> The hostile-verified W74F-H repair closes the relative common-domain
> \(K/\eta_K\) ledger at `proved-mod-audit`, but its detailed component-domain
> factoring and all L0 elevation remain separate work.  These bridge proofs
> consume only their explicit hypotheses; they neither import quarantined
> component rows nor promote the upstream ledger.

## 7. Registry impact

Both gap reservations may be replaced by result rows at
`status: proved-mod-audit`, `af: none`.  Neither result is L0-rigorous.
Suggested ids are `lem-routef-f2-positive-unital-compression` and
`lem-routef-f3-retract-defect`.

### F2 exact contract text

> Route F F2 positive-unital compression: let \(K\ge1\) be a dimension-independent constant, let \(n\ge1\), let \(Q:\ell_\infty^n\to\ell_\infty^n\) be row-stochastic, let \(D:M_n\to\ell_\infty^n\) be diagonal extraction and \(J:\ell_\infty^n\to M_n\) diagonal inclusion, put \(\Phi=JQD\), let \(\mathcal B\) be a finite-dimensional unital \(C^*\)-algebra, and let \(\Delta:\mathcal B\to M_n\) and \(\Upsilon:M_n\to\mathcal B\) be UCP maps; if \(0\le\eta\le\min\{(24K)^{-1},1\}\), \(\|\Delta\Upsilon-\Phi\|_{\rm cb}\le K\eta\), \(\|\Upsilon\Delta-I_{\mathcal B}\|_{\rm cb}\le K\eta\), and \(\|\Upsilon(\Delta x\,\Delta y)-xy\|\le K\eta\|x\|\|y\|\) for all \(x,y\in\mathcal B\), then \(\mathcal B\) is commutative and there are \(k\ge1\) and a unital \(*\)-isomorphism \(\iota:\ell_\infty^k\to\mathcal B\) such that \(A:=D\Delta\iota:\ell_\infty^k\to\ell_\infty^n\) and \(M:=\iota^{-1}\Upsilon J:\ell_\infty^n\to\ell_\infty^k\) are positive unital maps satisfying \(\|Q-AM\|_{\infty\to\infty}\le K\eta\), \(\|QA-A\|_{\infty\to\infty}\le2K\eta\), and \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\) for every \(x\in\ell_\infty^k\).

### F3 exact contract text

> Route F F3 retract defect: let \(K\ge1\) be a dimension-independent constant, let \(n,k\ge1\), let \(A:\ell_\infty^k\to\ell_\infty^n\) and \(M:\ell_\infty^n\to\ell_\infty^k\) be positive unital maps, let \(Q:\ell_\infty^n\to\ell_\infty^n\) be row-stochastic, and let \(\eta\ge0\) satisfy \(3K\eta<1\); if \(\|Q-AM\|_{\infty\to\infty}\le K\eta\), \(\|QA-A\|_{\infty\to\infty}\le2K\eta\), and \(\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty\) for every \(x\in\ell_\infty^k\), then \(\|MA-I_k\|_{\infty\to\infty}\le3K\eta/(1-3K\eta)\).

The new bridge rows should be direct imports of any parent that claims the
full Route F stochastic-idempotent conclusion, together with the existing
`lem-routef-prh-finish`.  The bridge rows themselves must not import the
quarantined component-domain rows: their factorization estimates are explicit
contract hypotheses.
