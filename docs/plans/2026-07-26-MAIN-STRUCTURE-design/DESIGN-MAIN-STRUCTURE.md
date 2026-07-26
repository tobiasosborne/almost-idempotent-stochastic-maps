# DESIGN-MAIN-STRUCTURE — hostile audit and repaired proof plan

**Status:** design only; no result below is proved, reviewed, or promoted.

## 1. Headline verdict

I found a **genuine structural gap in the v4.1 contract factoring**, but no
genuine mathematical gap in Kitaev's source argument.

The eight MAIN ids are not registered in this checkout: none of
`argument/lemmas/lem-maincb-{stage1-strict-refinement,stage1-maximality,corner-equivalence,cross-class-merging-datum,one-class-extension,binary-block-merge,stage3-finite-recombination,structural-assembly}.md`
exists.  The reset-chain and fresh/old-side shards named by the brief are also
absent.  Thus the only authoritative landed MAIN contract is the narrowed
IMPROVE-CB contract at
`argument/lemmas/lem-maincb-error-improvement.md:1-9`; the other contracts
audited below are the **proposals** at
`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:221-228`,
not landed rows.

The decisive defects are:

1. Stage 1 uses the direct-sum **inclusion** merge in the source
   (`refs/kitaev-2405.02434/approximate_algebras.tex:1352-1359,1419-1426`).
   The proposed refinement
   instead imports `lem-extcb-four-corner-merge`, whose exact contract requires
   four **bijective** corner maps
   (`argument/lemmas/lem-extcb-four-corner-merge.md:4-6`).  For a direct-sum
   source the off-diagonal source corners are zero while the target
   off-diagonal corners need not be zero, so those maps cannot be bijective.
2. The proposed binary merge accepts two individual equivalence classes.
   After one merge its output is a union of classes, so it cannot be applied a
   second time.  Hence the proposed finite recombination does not follow for
   three or more classes.
3. Dimension additivity proves zero corners for the original sums \(P_U,P_V\),
   but the four-corner datum used at a merge lives in the compressed ambient
   corner \(S_{P_{U\cup V}}\).  No proposed dependency transports the zero
   dimension to the compressed target corners.
4. The reset threshold omits at least the now-landed
   \(\varepsilon_{\max}^{\rm cb}\), the four-corner total-defect threshold
   \(a_{\rm merge}\), and the thresholds needed for corner transitivity and
   compatible compression.  This is a local-domain defect, not a
   dimension-freeness counterexample.
5. The assembly has no producer for the initial/maximal commutative reset
   inclusion, and its proposed conclusion does not state the uniform
   \(O(\varepsilon)\) extended-isomorphism estimate consumed by
   `lem-thmainext-conditional`.

Accordingly, the current MAIN subtree is **DO NOT SEED**.  It becomes
plausibly seedable after the helper rows and corrected interfaces below are
user-ratified and independently reviewed.

## 2. Factoring required before the nine target rows

These are result rows, not definitions.  Each is supported by local source or
an elementary finite-dimensional derivation, but none is claimed proved.

| helper row | exact job | projected af |
|---|---|---|
| `lem-maincb-initial-reset-inclusion` | The scalar-unit map, followed by IMPROVE-CB if needed, gives a reset extended inclusion \(\mathbb C\to A\). | 4–5 / depth 2 |
| `lem-maincb-maximal-reset-selection` | Level-one lower norm makes every \(\mathbb C^m\to A\) injective, so \(m\le\dim_{\mathbb C}A\); the nonempty finite set of feasible source dimensions has a maximum. | 4–5 / depth 2 |
| `lem-maincb-direct-sum-inclusion-merge` | Extended version of `cor_merge_sum` for two diagonal extended inclusions; no off-diagonal bijectivity and no output-surjectivity claim.  Use the two-block proof at `refs/kitaev-2405.02434/approximate_algebras.tex:1325-1359` at every amplification, as licensed at `refs/kitaev-2405.02434/approximate_algebras.tex:1542-1557`. | 7–9 / depth 3 |
| `lem-maincb-close-corner-transport` | If the relevant finite-dimensional compression idempotents are universally \(<1\) apart, their ranges have the same dimension; apply to original and compatible-compressed corners. | 5–7 / depth 3 |
| `lem-maincb-stage2-extcb-datum` | From a current one-class map, compatible compression, atomic corner additivity, and close-corner transport, produce exactly the hypotheses of `conj-extcb`: compressed ambient extended algebra, extended isomorphism onto \(S_P\), \(\dim S_Q=1\), \(S_{P,Q}\ne0\), and \(\|P+Q-I\|\) control. | 9–11 / depth 3 |
| `lem-maincb-improvement-one-step` | Norm-one-diagonal correction with uniform amplified displacement and recurrence \(d^+\le K(d^2+\varepsilon)\). | 7–9 / depth 3 |
| `lem-maincb-improvement-iteration` | Stop the recurrence at a universal \(O(\varepsilon)\) floor, sum the displacement geometrically, and treat \(\varepsilon=0\). | 5–7 / depth 3 |

The general close-corner transport statement is **NOT IN LOCAL REFS as a
reusable contract**.  The validated
`lem-extcb1-close-corner-dimension` is restricted to an EXT-CB datum
(`argument/lemmas/lem-extcb1-close-corner-dimension.md:4-6`) and must not be
silently generalized.  The generic row therefore needs its own elementary
proof.

Missing definition shards:

- the already-proposed but absent `def-maincb-reset-state` and
  `def-maincb-raw-call`
  (`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:403-428`);
- the already-proposed but absent `def-operator-space`, needed by the amplified
  improvement proof
  (`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:391`);
- a datum-only `def-maincb-partition-state`: the finite atomic family
  \(P_1,\ldots,P_m\), its equivalence-class partition, the notation
  \(P_U=\sum_{j\in U}P_j\), \(A_U=S_{P_U}\), and a current union-block reset
  map.  It must contain no existence, zero-corner, preservation, or
  termination assertion.

## 3. Per-row plans and verdicts

### 3.1 `lem-maincb-stage1-strict-refinement`

**Mechanism.** Relabel the offending \(P_j\) as \(P_m\).  The Stage-1
nontrivial-projection packet supplies \(P',P''\) in \(S_{P_m}\); the
fresh-two-point row gives \(\mathbb C^2\to S_{P_m}\), and the old-side
compression row gives
\(\mathbb C^{m-1}\to S_{P_{[1,m-1]}}\).  Apply the new direct-sum inclusion
merge, not the four-corner isomorphism lemma, to obtain a raw
\(\mathbb C^{m+1}\)-inclusion, then IMPROVE-CB and the Stage-1 reset bound.
This is exactly the source move at
`refs/kitaev-2405.02434/approximate_algebras.tex:1417-1426`.

Exact hypotheses still to expose are: finite-dimensional \(A\);
\(\varepsilon\le\varepsilon_{\rm MAIN}\); the old and fresh defects required by
the Stage-1 raw-bound row; and the narrowed IMPROVE-CB hypotheses.  The
fresh/old-side and reset rows are absent in this checkout, so this plan is
conditional on their eventual reviewed contracts.

**Corrected interface.** For a finite-dimensional extended
\(\varepsilon\)-\(C^*\)-algebra in the corrected reset domain, if a reset
extended inclusion \(\mathbb C^m\to A\) has some projection-basis image
\(P_j\) with \(\dim S_{P_j}>1\), there is a reset extended inclusion
\(\mathbb C^{m+1}\to A\), with the same universal reset error.

**Budget:** 7–9 nodes / depth 3 after the direct-sum helper.

**Verdict:** **GAP — contract-factoring defect.**  The source step is
supported, but the proposed dependency on the bijective four-corner merge
cannot prove it.

### 3.2 `lem-maincb-stage1-maximality`

Let \(d=\dim_{\mathbb C}A\).  By the initial-inclusion and maximal-selection
helpers, maximal reset source dimension exists.  If a maximal
\(\mathbb C^m\to A\) had a
non-one-dimensional image, strict refinement would give
\(\mathbb C^{m+1}\to A\), contradicting maximality.  Relabeling handles an
arbitrary \(P_j\).

The proposed conditional statement is sound, but its use at assembly needs
the absent existence/boundedness producer.  Its interface must say that \(A\)
is finite-dimensional and that maximality is among reset inclusions in the
same local domain.

**Budget:** 3–4 nodes / depth 2.

**Verdict:** **SUPPORTED-WITH-DERIVATION** — derive nonemptiness and
\(m\le d\); no source gap.

### 3.3 `lem-maincb-corner-equivalence`

Reflexivity is \(\dim S_{P_j}=1\).  Symmetry follows because dagger is an
involutive bijection \(S_{P_j,P_k}\leftrightarrow S_{P_k,P_j}\), using the
compression identity.  For transitivity choose nonzero
\(X\in S_{P_j,P_k}\), \(Y\in S_{P_k,P_l}\).  The validated product estimate
(`argument/lemmas/lem-extcb-one-dimensional-product.md:4-6`) gives
\[
 \|X\mathbin\cdot Y\|\ge(1-C_{\rm PQR}e)\|X\|\|Y\|>0
\]
when \(e\le\min\{e_{\rm PQR},(2C_{\rm PQR})^{-1}\}\).  Thus
\(S_{P_j,P_l}\ne0\); the validated dimension bound
(`argument/lemmas/lem-extcb-one-dimensional-corner-dimension.md:4-6`) makes
its dimension exactly one.  This expands the compressed sentence at
`refs/kitaev-2405.02434/approximate_algebras.tex:1180-1187`.

**Contract correction.** Add an existential universal \(e_{\sim}>0\) and the
explicit hypothesis that the common atomic corner parameter
\(e=\delta_{\rm at}+\varepsilon\) is at most \(e_{\sim}\).  The proposed
unqualified contract at
`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:223`
is stronger than its inputs.  Corner-dimension additivity is not needed for
this row.

**Budget:** 7–8 nodes / depth 3.

**Verdict:** **GAP AS WRITTEN — contract-factoring defect;**
**SUPPORTED-WITH-DERIVATION** after the local-domain correction.

### 3.4 `lem-maincb-one-class-extension`

This is the first induction and must remain class-internal.  For
\(C=\{1,\ldots,s\}\), use \(r=1,\ldots,s\).

- Base: the one-dimensional corner \(S_{P_1}\) has its canonical scalar
  extended isomorphism.
- Step: compress the current \(M_{r-1}\)-map and the two target projections
  into \(A_r=S_{P_{[1,r]}}\).  Single-compression transfer supplies only an
  **inclusion**
  (`argument/lemmas/lem-compcb-single-compression-transfer.md:4-6`), so the
  new Stage-2-datum helper must separately prove level-one bijectivity and
  the nonzero cross corner.  Atomic equivalence plus dimension additivity
  (`argument/lemmas/lem-extcb-corner-dimension-additivity.md:4-6`) gives the
  dimensions before compression; close-corner transport carries them into
  \(A_r\).
- Now `conj-extcb` applies with all of its exact hypotheses and returns one
  map \(M_r\to A_r\), uniform in \(r\) and amplification
  (`argument/lemmas/conj-extcb.md:4-6,23-33`).  IMPROVE-CB immediately resets
  the error.

This is the derivation suppressed at
`refs/kitaev-2405.02434/approximate_algebras.tex:1430-1441`.

**Corrected interface.** Quantify a universal \(e_{\rm cls}\), the
partitioned reset state, and \(\varepsilon\le e_{\rm cls}\); conclude a reset
extended isomorphism \(v_C:M_{|C|}\to A_C\), not merely a “level-one map
carried at every amplification.”

**Budget:** Stage-2 datum helper 9–11 / depth 3; induction root 4–5 / depth 3.

**Verdict:** **GAP — contract-factoring defect.**  The proposed deps do not
produce the EXT-CB datum.  The source mathematics is supported after that
derivation is factored.

### 3.5 `lem-maincb-cross-class-merging-datum`

The row must be union-stable.  Let \(U,V\) be disjoint nonempty **unions of
equivalence classes**.  For \(j\in U,k\in V\), the indices are inequivalent;
the one-dimensional-corner bound therefore gives
\(\dim S_{P_j,P_k}=0\).  Dimension additivity then gives
\[
 \dim S_{P_U,P_V}=\sum_{j\in U,k\in V}\dim S_{P_j,P_k}=0,
\]
and similarly in the reverse direction.  This is the source mechanism at
`refs/kitaev-2405.02434/approximate_algebras.tex:1363-1369,1428,1443`.

That is not yet the required datum.  Compress into
\(A_{U\cup V}=S_{P_{U\cup V}}\), use generic close-corner transport to prove
the two target off-diagonal corners there are still zero, and only then use
the unique maps \(0\to0\).  They are bijective and all product/norm/dagger
conditions involving them are vacuous.  The two reset diagonal maps supply
the diagonal conditions; compatible compressed projections supply
\(\|P_U'+P_V'-I_{A_{U\cup V}}\|\le\rho\).

**Contract correction.** Replace “distinct equivalence classes \(C,D\)” by
“disjoint nonempty unions \(U,V\) of equivalence classes,” name the compressed
ambient \(A_{U\cup V}\), and state the dependency-produced common raw defect
\(\rho\) and local domain \(\rho+\varepsilon_{U\cup V}\le e_{\rm cross}\).

**Budget:** 9–11 nodes / depth 3 after close-corner transport.

**Verdict:** **GAP — contract-factoring defect.**  Atomic additivity supports
the source claim, but the proposed row neither handles unions nor transports
zero corners to the actual merge ambient.

### 3.6 `lem-maincb-binary-block-merge`

Take two reset maps on the disjoint class unions \(U,V\), apply the corrected
cross-block datum, then the validated four-corner merge.  Its exact smallness
hypothesis is the **total** defect
\(\rho+\varepsilon_{U\cup V}\le a_{\rm merge}\)
(`argument/lemmas/lem-extcb-four-corner-merge.md:4,18-25`).  Its output is an
extended \(C_{\rm merge}(\rho+\varepsilon_{U\cup V})\)-isomorphism.  Apply
IMPROVE-CB only after checking both its raw-defect bound
\(\le\delta_{\max}^{\rm cb}\) and its ambient bound
\(\varepsilon_{U\cup V}\le\varepsilon_{\max}^{\rm cb}\); this yields the reset
map on \(U\cup V\).

**Contract correction.** Inputs and output must be class unions, and the
corrected reset ledger must explicitly discharge \(a_{\rm merge}\),
\(\delta_{\max}^{\rm cb}\), and \(\varepsilon_{\max}^{\rm cb}\).

**Budget:** 5–6 nodes / depth 2.

**Verdict:** **GAP AS WRITTEN — contract-factoring defect;**
**SUPPORTED-WITH-DERIVATION** with the union-stable datum and corrected ledger.

### 3.7 `lem-maincb-stage3-finite-recombination`

This is the second induction.  Enumerate the finitely many equivalence classes
\(C_1,\ldots,C_q\).  Start with \(U_1=C_1\), and at step \(t\) merge the
current union \(U_t\) with \(C_{t+1}\), obtaining
\(U_{t+1}=U_t\cup C_{t+1}\).  The union-stable binary row applies at every
step.  Error is reset after each merge, so no factor \(q\) enters the bound.

The proposed binary contract only accepts two individual classes, so
“repeated application” at
`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:227`
is invalid after the first step.

**Budget:** 4–5 nodes / depth 2 after the corrected binary row.

**Verdict:** **GAP — contract-factoring defect.**  This is the clearest
structural failure; it is not a gap in the source sentence at
`refs/kitaev-2405.02434/approximate_algebras.tex:1443`.

### 3.8 `lem-maincb-structural-assembly`

Use the initial/maximal-selection helper, maximality, the corrected
equivalence partition, all one-class maps, and the independent finite
recombination.  Set
\[
 B=\bigoplus_{C}M_{|C|}.
\]
The Stage-3 output is one reset extended isomorphism \(v:B\to A\); finiteness
of the partition makes \(B\) finite-dimensional.

**Contract correction.** The conclusion must quantify universal
\(C_{\rm struct},e_{\rm struct}>0\) and state that for
\(\varepsilon\le e_{\rm struct}\), every finite-dimensional extended
\(\varepsilon\)-\(C^*\)-algebra \(A\) has one extended
\(C_{\rm struct}\varepsilon\)-isomorphism \(v:B\to A\).  “One bijective
level-one map whose all-level maps are its amplifications”
(`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:228`)
does not assert the uniform amplified error bound required by
`argument/lemmas/lem-thmainext-conditional.md:4`.

**Budget:** 6–7 nodes / depth 2 after the two branches close.

**Verdict:** **GAP — contract-factoring defect.**  Initial selection and the
quantitative extended conclusion are missing; no source-level counterexample
was found.

### 3.9 `lem-maincb-error-improvement`

The landed narrowed contract is faithful to the literal finite-dimensional
and small-\(\varepsilon\) hypotheses at
`refs/kitaev-2405.02434/approximate_algebras.tex:1317-1319`, with the extended
adaptation at
`refs/kitaev-2405.02434/approximate_algebras.tex:1508-1535,1557`.  The
exact-target correction contract, however, has target
\(B(H)\) (`argument/lemmas/lem-extcb-exact-target-correction.md:4`), while
IMPROVE-CB has an approximate target \(A\).  It does not imply this row.

Use the two factored helpers:

1. the norm-one diagonal
   (`refs/kitaev-2405.02434/approximate_algebras.tex:1239-1254`) and the
   approximate cocycle calculation
   (`refs/kitaev-2405.02434/approximate_algebras.tex:1256-1311`) give one
   amplified correction with \(d^+\le K(d^2+\varepsilon)\);
2. iterate until \(d_s\le K_0\varepsilon\), using the same level-one map at
   every amplification
   (`refs/kitaev-2405.02434/approximate_algebras.tex:1508-1535`);
3. obtain the two-sided \(1\pm c_0^{\rm cb}\varepsilon\) bounds from a fixed
   positive lower modulus and the extended inclusion argument
   (`refs/kitaev-2405.02434/approximate_algebras.tex:1483-1506`);
4. if the original \(v\) is bijective, choose
   \(\delta_{\max}^{\rm cb}\) so the final map is a \(<1\) perturbation of
   \(v\) after composing with \(v^{-1}\); the Neumann argument preserves
   bijectivity.

The note “now safe to seed” at
`argument/lemmas/lem-maincb-error-improvement.md:13-31` is premature under the
node cap: the exact-target import is only a proof-pattern precedent.

**Contract correction:** none; the landed narrowed contract is the right
target.  **Dependency correction:** replace the sole logical reliance on
exact-target correction by the one-step and iteration helpers above; the
exact-target row may be omitted as an unused import.

**Budget:** helpers 7–9 and 5–7 nodes respectively; root 5–6 / depth 3.

**Verdict:** **SUPPORTED-WITH-DERIVATION.**  The missing work is the
approximate-target Newton floor plus lower-norm/bijectivity control, not new
mathematics.

## 4. Named-hazard adjudication

### R19 — circularity

**Current factoring: not cleared.**  The source chooses a maximal feasible
\(m\) first; it does not need an arbitrary refinement run to discover that
maximum.  After adding finite-dimensionality and initial/maximal selection,
the refinement measure is
\[
 \mu=m\quad\text{strictly increasing},\qquad\text{equivalently}\qquad
 N=\dim_{\mathbb C}A-m\in\mathbb N
\]
with \(N\) decreasing by exactly one at every strict refinement.  An extended
inclusion is injective at level one in the reset domain, hence
\(m\le\dim_{\mathbb C}A\).  Therefore no refinement sequence can be infinite:
it has at most \(\dim_{\mathbb C}A-m_0\) steps.  Such an arbitrary sequence
may stop early because all corners are already one-dimensional; **strict
increase alone does not prove that its terminal point is maximal**.  The
maximality argument is instead: select a maximal feasible \(m\), then one
strict refinement contradicts that selection.  No conclusion of maximality is
used to prove refinement.  The source dimension increase is explicit at
`refs/kitaev-2405.02434/approximate_algebras.tex:1419-1426`.

### R21 — conflated inductions

**Conceptually cleared, contractually not yet cleared.**

- One-class induction: fixed class \(C\), measure \(|C|-r\), operation
  \(M_{r-1}\to M_r\) via EXT-CB.
- Cross-class induction: all one-class maps already constructed, measure
  \(q-t\), operation \(U_t\to U_t\cup C_{t+1}\) via zero-corner direct-sum
  merge.

They share the reset invariant but neither consumes the other's induction
hypothesis.  They join only in structural assembly, as intended by the v4.1
DAG at
`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:321-333`.
The proposed class-only binary contract must be repaired to unions before this
separation is executable.

### R22 — missing zero datum

**Current factoring fails; corrected mechanism clears it.**  The zero maps may
not be assumed.  First prove atomic cross dimensions zero from
inequivalence plus the \(\le1\) theorem; then apply dimension additivity; then
transport the zero dimension into the compressed merge ambient; only then are
the off-diagonal maps the bijections \(0\to0\).  The missing third step is the
precise defect in the proposed dependency list.

## 5. Dimension-freeness and reset ledger

No unavoidable dimension leak was found:

- the finite-dimensional diagonal has projective norm one, including for a
  direct sum
  (`refs/kitaev-2405.02434/approximate_algebras.tex:1245-1254`), so the improvement
  constants do not count matrix blocks;
- the source convention says every \(O(\cdot)\) instance is independent of
  additional data
  (`refs/kitaev-2405.02434/approximate_algebras.tex:458`), and the landed
  IMPROVE-CB contract explicitly quantifies universal
  \(\varepsilon_{\max}^{\rm cb},\delta_{\max}^{\rm cb},c_0^{\rm cb}\)
  (`argument/lemmas/lem-maincb-error-improvement.md:4`);
- `conj-extcb` explicitly makes \(C_{\rm ext}\) independent of \(r\),
  amplification, \(\dim A\), and block data
  (`argument/lemmas/conj-extcb.md:32-33`);
- single compression and four-corner merge quantify universal constants
  (`argument/lemmas/lem-compcb-single-compression-transfer.md:4`,
  `argument/lemmas/lem-extcb-four-corner-merge.md:4`);
- every induction step is binary and immediately reset, so neither class size,
  class count, nor stage index is summed into the error.

But the v4.1 ledger is **incomplete**.  Its displayed
\[
 \varepsilon_E^{\rm corr}
 =\min\{\delta_{\max}^{\rm cb},e_H,e_{\rm ext},e_{\rm sel},e_{\rm split}\}
   /C_{\rm pre}
\]
at
`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:216`
predates the landed narrowing and does not discharge all exact hypotheses.

Let the new helper rows produce universal positive thresholds
\(e_{\rm dir},e_{\sim},e_{\rm close},e_{\rm step},e_{\rm cross}\) and the
direct-sum constant \(C_{\rm dir}\).  A sound reset package must at least use
\[
\begin{aligned}
 C_{\rm pre}
   &=2L^2\max\{1,C_{\rm ext},C_{\rm merge},C_{\rm dir}\},\\
 \varepsilon_{\rm MAIN}
   &=C_{\rm pre}^{-1}\min\{
      \varepsilon_{\max}^{\rm cb},\delta_{\max}^{\rm cb},
      a_{\rm merge},e_H,e_{\rm ext},e_{\rm sel},e_{\rm split},
      e_{\rm dir},e_{\sim},e_{\rm close},e_{\rm step},e_{\rm cross}\}.
\end{aligned}
\]
Each new \(e_*\) must be a dependency-produced threshold that already
incorporates its COMP/corner-algebra subthresholds; none may be guessed.
Since \(L,C_{\rm pre}\) and every entry of the finite minimum are universal,
this repair remains independent of dimension, amplification, block data, and
stage index.

**LOUD finding:** until this corrected threshold producer exists, the raw
reset rows do not establish the exact smallness hypotheses of IMPROVE-CB or
the validated merge.  This is a contract/local-domain leak, not evidence of a
dimension-dependent constant.

R17 and R36 remain binding in the repair: the reset and raw-call definitions
contain data only, never estimates, and the complete corrected constant
package must be proved before any raw Stage-1/2/3 row consumes it.  No helper
may refer forward to a threshold produced by its own consumer.

## 6. Recommended landing order

1. Ratify/provision the three missing MAIN datum definitions and
   `def-operator-space`.
2. Prove IMPROVE-CB through its two factored helpers.
3. Land the corrected reset-constant package and the three raw/reset rows.
4. Prove the direct-sum inclusion merge, initial inclusion, maximal selection,
   and generic close-corner transport.
5. Close refinement then maximality, then corner equivalence.
6. Close the Stage-2 EXT-CB datum helper and one-class induction.
7. Close the union-stable cross-block datum, binary merge, and finite
   recombination.
8. Close structural assembly; only then rewire or seed
   `lem-thmainext-conditional`.

Nothing here authorizes a status promotion or an `af` seed.  Every contract
correction above is escalated for user ratification.
