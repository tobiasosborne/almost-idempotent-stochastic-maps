# DESIGN — F2 typing correction and elevation provisioning

Date: 2026-07-27  
Role: fresh independent design mathematician  
Status: **DESIGN ONLY / NON-RIGOROUS / NO REGISTRY MUTATION / ESCALATE FOR
FRESH HOSTILE CHECK BEFORE VERBATIM LANDING**

## 0. Disposition

**SURGICAL TYPING CORRECTION DESIGNED; ESTIMATES AND HYPOTHESES UNCHANGED.**

The failed F2 elevation exposed a genuine type error.  In this repository
\(\ell_\infty^m=\mathbb R^m\), whereas diagonal extraction from the complex
matrix algebra \(M_n\) has codomain \(\mathbb C^n\).  The repair is to use
exactly the already af-validated F0 seam
\[
D:M_n\longrightarrow\mathbb C^n,\qquad
J:\mathbb C^n\longrightarrow M_n,\qquad
\Phi=JQ_{\mathbb C}D,
\]
where \(Q_{\mathbb C}\) is the canonical complex-linear extension of the
real row-stochastic map \(Q\).  After \(\mathcal B\) is proved commutative,
the complex coordinate isomorphism
\(\iota_{\mathbb C}:\mathbb C^k\to\mathcal B\) identifies
\(\mathbb R^k\) with \(\mathcal B_{\mathrm{sa}}\).  The stochastic maps are
the restrictions and corestrictions of the complex composites to those
real self-adjoint parts.

This adds no mathematical hypothesis.  It changes no quantifier, constant,
threshold, norm estimate, or output required by F3 or PRH.

## 1. Corrected one-line F2 contract

### 1.1 Verbatim candidate

The proposed corrected registry contract is the following single,
registry-ready flattened line:

```text
Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> C^n diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), J: C^n -> M_n diagonal inclusion, Q_C: C^n -> C^n the canonical complex-linear extension of Q, and Phi = J Q_C D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta, and ||Upsilon(Delta x Delta y) - xy|| <= K*eta*||x||*||y|| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota_C: C^k = l_inf^k(C) -> B such that D Delta iota_C maps R^k into R^n, iota_C^{-1} Upsilon J maps R^n into R^k, and the resulting restrictions and corestrictions A := (D Delta iota_C)|_{R^k}: l_inf^k -> l_inf^n and M := (iota_C^{-1} Upsilon J)|_{R^n}: l_inf^n -> l_inf^k are positive unital maps satisfying ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k.
```

Here and only at the output,
\(\ell_\infty^m=\mathbb R^m=(\mathbb C^m)_{\mathrm{sa}}\), in accordance
with `def-stochastic`.  The phrases “maps \(\mathbb R^k\) into
\(\mathbb R^n\)” and “maps \(\mathbb R^n\) into \(\mathbb R^k\)” make the
corestrictions in the displayed definitions literal rather than implicit.

### 1.2 Why this is the minimal interface

A positive complex-linear map between \(C^*\)-algebras preserves
self-adjoint elements: write a self-adjoint input as the difference of its
positive and negative parts.  Consequently:

- \(\iota_{\mathbb C}(\mathbb R^k)=\mathcal B_{\mathrm{sa}}\);
- \(\Delta\) sends this set into \((M_n)_{\mathrm{sa}}\), whose diagonal is
  real, so \(D\Delta\iota_{\mathbb C}(\mathbb R^k)\subseteq\mathbb R^n\);
- \(J(\mathbb R^n)\subseteq(M_n)_{\mathrm{sa}}\), \(\Upsilon\) preserves
  self-adjointness, and
  \(\iota_{\mathbb C}^{-1}(\mathcal B_{\mathrm{sa}})=\mathbb R^k\).

The restrictions are positive and unital because their complex parents are
positive and unital and the real positive cones are exactly the positive
cones in the self-adjoint coordinate parts.  No real map is called UCP or
assigned a cb norm.

This formulation keeps `PROOF-F2F3-BRIDGE.md` §1 valid with only systematic
typing substitutions:

\[
(\ell_\infty^m,D,J,Q,\iota)
\quad\rightsquigarrow\quad
(\mathbb C^m,D,J,Q_{\mathbb C},\iota_{\mathbb C})
\]
inside the \(C^*\)/UCP/cb argument, followed by restriction to
\(\mathbb R^m\) in §§1.4–1.5.  In particular,
\[
DJ=I_{\mathbb C^n},\qquad
D\Phi=Q_{\mathbb C}D,
\]
and the latter identity restricts on self-adjoint inputs to the old real
identity used in the \(QA-A\) calculation.  The proofs of
\[
AM-Q=D(\Delta\Upsilon-\Phi)J,\qquad
QA-A=D(\Phi\Delta-\Delta)\iota_{\mathbb C}
\]
are now identities on real inputs obtained by restricting correctly typed
complex identities.  Restriction cannot increase the cb/complex operator
norm, so the constants remain exactly \(K\eta\) and \(2K\eta\).  The
lower-modulus proof is applied only to \(x\in\mathbb R^k\), exactly as the
consumer requires.

### 1.3 Definition imports

The future `defs:` line **should gain `def-ucp-map`**.  The contract names
UCP maps, and that canonical locked definition now exists.  If the
projection-basis provisioning route in §2.2 is used and recorded in the
lemma body, `def-projection-basis` should also be listed so that the proof
uses no naked project term.  The prospective line is therefore

```text
defs: def-stochastic; def-ucp-map; def-projection-basis
```

This is definition/proof provisioning, not an additional theorem
hypothesis.

## 2. Elevation provisioning plan

### 2.1 What the aborted run established

The retained run stopped at 11 validated nodes out of 30.  Its open
challenge classification was:

1. a genuine root typing defect (`ch-2163ee19860aa3d7`);
2. missing in-scope facts: UCP complete contractivity and the relevant
   finite-dimensional \(C^*\)-algebra structure statements;
3. cross-sibling dependencies in the commutator and \(QA-A\) branches; and
4. an \(\varepsilon=K\eta\) abbreviation used outside the node where it was
   introduced.

The in-run amendment to node 1.1 did not repair the literal root contract;
the workspace must therefore be re-seeded from the corrected contract, not
resumed.

### 2.2 Finite-dimensional \(C^*\)-algebra structure

**Recommendation: provision the exact projection-basis sentence as a
byte-matched af external, then prove the coordinate isomorphism in-tree.**
The permitted local source is exactly
`refs/kitaev-2405.02434/approximate_algebras.tex:1361-1363`, already
transcribed in the locked cited `def-projection-basis`.  The external must
contain the byte-verbatim source sentence, not a strengthened paraphrase
such as a general classification theorem.

Once commutativity has been proved, take a projection basis
\(\{\Pi_1,\ldots,\Pi_k\}\) and define
\[
\iota_{\mathbb C}(\lambda_1,\ldots,\lambda_k)
   =\sum_{j=1}^k\lambda_j\Pi_j.
\]
The projection relations give multiplicativity, preservation of the
involution and unit, while the word “basis” gives bijectivity.  Hence this
is a unital \(*\)-isomorphism
\(\mathbb C^k\to\mathcal B\), and
\(\iota_{\mathbb C}(\mathbb R^k)=\mathcal B_{\mathrm{sa}}\).
Budget: **2–3 nodes** after the external (construction, isomorphism/real
part, parent).

The earlier proof also invoked the broader statement that every
finite-dimensional complex \(C^*\)-algebra is a direct sum of full matrix
algebras.  That broader theorem is **NOT IN LOCAL REFS** and must not be
registered as a cited external.  For the pre-commutativity contradiction,
retain an in-tree elementary derivation: choose minimal projections, show
the corners are zero or one-dimensional, build matrix units by equivalence
classes, and in a block of size at least two use the explicit two Pauli
contractions to obtain commutator norm \(2\).  The failed ledger already
exhibited this route; it needs **5 nodes** and no guessed source claim.

### 2.3 UCP complete contractivity

This fact is **DERIVABLE LOCALLY IN-TREE** from the definition of UCP and
finite-dimensional \(C^*\)-algebra order:

1. For each \(r\), \(T_r=\mathrm{id}_{M_r}\otimes T\) is unital and
   completely positive, hence 2-positive.  Applying
   \(\mathrm{id}_{M_2}\otimes T_r\) to the standard positive \(2\times2\)
   block gives the Schwarz inequality
   \(T_r(z)^*T_r(z)\le T_r(z^*z)\).
2. Since \(0\le z^*z\le\|z\|^2 1\), positivity and unitality give
   \(0\le T_r(z^*z)\le\|z\|^2 1\), and therefore
   \(\|T_r(z)\|\le\|z\|\).
3. Taking the supremum over \(r\) gives \(\|T\|_{\rm cb}\le1\);
   \(T(1)=1\) gives equality.

Use one shared validated node for this theorem and declare it as a
dependency wherever contractivity of \(\Delta\) or \(\Upsilon\) is used.
Do not cite it as a published theorem: no such byte-matched theorem was
identified in the permitted local refs.  Budget: **2–3 nodes**.

### 2.4 Dependency and scoping discipline

The clean re-seed should obey the following proof-DAG rules.

- Write \(K\eta\) in every node.  Do not introduce a global shorthand
  \(\varepsilon:=K\eta\); this removes the scope defect
  `ch-9bab33afd488f39c` by construction.
- Make the approximate-invariance node depend explicitly on the shared
  UCP-complete-contractivity node.
- Make the \(10K\eta\) commutator node depend explicitly on approximate
  invariance and on the typed diagonal-range node.  It must not mention
  unvalidated siblings.
- Make the \(QA-A\) node depend explicitly on approximate invariance (or
  rederive the two-line telescope locally); do not rely on a pending sibling.
- Let the lower-modulus combination node prove only the lower-modulus
  inference.  The root assembly, not that child, depends on the
  commutativity, \(A/M\), factor-error, \(QA-A\), and lower-modulus branches.
- Put the real-preservation/corestriction check immediately after
  \(\iota_{\mathbb C}\) is constructed and make every real-output node
  depend on it.

### 2.5 Node budget and factoring tripwire

An honest clean-tree estimate is **24–25 nodes**:

| block | nodes |
|---|---:|
| root and final assembly | 2 |
| typed complex setup and real-interface checks | 3 |
| UCP complete contractivity and approximate invariance | 4 |
| \(8K\eta/10K\eta\) commutator bounds | 2 |
| in-tree noncommutative norm-\(2\) witness | 5 |
| commutativity and projection-basis coordinate isomorphism | 3 |
| positive-unital \(A,M\), factor error, and \(QA-A\) | 3 |
| lower modulus | 3 |
| **total** | **25** |

This is at the requested envelope, so the first recommendation is the
byte-matched external plus a carefully dependency-declared re-seed, with a
hard stop at 25 live nodes.  Do not raise the cap if the prover expands.
If the projected or live tree exceeds 25, factor these atomic registry
sub-lemmas instead:

1. **`lem-fd-cstar-norm-two-commutator`:** every finite-dimensional
   noncommutative unital complex \(C^*\)-algebra contains self-adjoint
   contractions \(u,v\) with \(\|[u,v]\|=2\).
2. **`lem-fd-commutative-cstar-coordinates`:** every nonzero
   finite-dimensional commutative unital complex \(C^*\)-algebra admits
   \(k\ge1\) and a unital \(*\)-isomorphism
   \(\iota_{\mathbb C}:\mathbb C^k\to\mathcal B\) taking
   \(\mathbb R^k\) onto \(\mathcal B_{\mathrm{sa}}\).
3. **`lem-ucp-complete-contractivity`:** every UCP map between
   finite-dimensional unital complex \(C^*\)-algebras has cb norm \(1\).

The first and third would be af-proved from elementary in-tree arguments;
the second may consume only the exact projection-basis external.  None may
be presented as a locally cited theorem unless a separate byte-verbatim
source anchor is actually provisioned.

## 3. Consumer re-check

### 3.1 F3

`lem-routef-f3-retract-defect` asks literally for real positive unital maps
\(A:\ell_\infty^k\to\ell_\infty^n\) and
\(M:\ell_\infty^n\to\ell_\infty^k\), the same real row-stochastic \(Q\), and
the three estimates
\[
\|Q-AM\|\le K\eta,\qquad
\|QA-A\|\le2K\eta,\qquad
\|Ax\|_\infty\ge(1-3K\eta)\|x\|_\infty
\]
for every real \(x\in\ell_\infty^k\).  The corrected F2 conclusion returns
exactly those maps and estimates, with the same orientations and quantifier
on \(x\).  Its retained threshold gives
\(3K\eta\le1/8<1\), so F3's denominator guard is also unchanged and
supplied verbatim.

### 3.2 PRH

`lem-routef-prh-finish` consumes the real positive unital \(A,M\), the same
row-stochastic \(Q\), \(K\ge1\), the unchanged threshold
\(0\le\eta\le\min\{(24K)^{-1},1\}\), the F2 factor estimate
\(\|Q-AM\|\le K\eta\), and the F3 retract estimate
\(\|MA-I\|\le3K\eta/(1-3K\eta)\).  The complexification is entirely upstream
of these outputs and adds no PRH premise.  Thus the corrected F2 conclusion
plus F3 still satisfies PRH's literal hypothesis list with no constant or
estimate conversion.

### 3.3 Future strengthened \(k\)-ledger parent

`DESIGN-F0-ASSEMBLY.md` §1.3 predates the af-validated F0 typing repair and
writes \(\Phi=JQD\) schematically.  Its future verbatim landing must use the
now-authoritative typed seam
\[
D:M_n\to\mathbb C^n,\quad
J:\mathbb C^n\to M_n,\quad
Q_{\mathbb C}:\mathbb C^n\to\mathbb C^n,\quad
\Phi=JQ_{\mathbb C}D.
\]
That is exactly the \(\Phi\) in the corrected F2 contract.  Therefore the
F0 UCP lift, F0 defect identity, the three ledger factorization estimates,
and F2 all refer to one and the same complex map \(\Phi:M_n\to M_n\).
Only F2's conclusion then restricts to the real stochastic spaces.  The
parent still composes without a new hypothesis, constant, threshold, or
norm conversion.

## 4. Landing guard

This document authorizes no mutation.  Before any landing, a fresh hostile
checker must verify the one-line contract verbatim, especially the two
real-preservation clauses and the consumer comparison.  After endorsement,
the old F2 workspace must be discarded and re-seeded from the corrected
root with the provisioned exact external(s); the retained ill-typed tree
must not be resumed or mechanically reflected.
