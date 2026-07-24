VERDICT: INVALID

# Fresh hostile architecture re-review — aism-fudw decomposition v2

The arithmetic headline is accurate: the table has 84 result rows, split
65 `proved-mod-audit` / 12 `stated` / 7 `cited candidate`, and it reserves
two additional uncontracted GAP ids.  The v2 document also correctly keeps
GAP-EA and the F2/F3 bridge loud and does not create a literal dependency
cycle.

It is nevertheless unsafe to transcribe or seed.  The five-row COMP-CB repair
does not carry the compression structure used to make the MAIN-CB corner
algebras; most H-CB children still lack a closed, non-circular hypothesis
datum; the new MAIN-CB rows replace one large implicit assembly by five
compound and partly undefined assemblies; and the ledger still has no
degree-two producer or correct local validity domains.  These are architecture
defects, not requests to raise an af node cap.

## 1. Coverage — INVALID

### 1.1 The claimed COMP-CB closure omits load-bearing clauses — BLOCKER

**Exact v2 loci:** disposition row 1.1 at line 17; COMP-CB rows 72--76;
closure claim at lines 421--423.

The source COMP-CB contract does not stop at amplification, one product
estimate, and compressed units.  It also exports exact idempotence and
involution, amplified almost-containment, and the fact that a nonvanishing
diagonal corner is itself an extended approximate \(C^*\)-algebra
(`DECOMP-W74F-C-THMAINEXT.md:154-168`;
`approximate_algebras.tex:1054-1082`).  Those facts type the corner algebras
used in Stage 1 and Stage 2.  A definition of \(Co_{P,Q}\) and \(S_{P,Q}\)
cannot carry these theorem-level estimates.

The five v2 rows therefore close the inputs explicitly noticed by the v1
review, but not COMP-CB itself.  Add the three rows in Registry impact A,
and make `lem-compcb-single-compression-transfer` import the
almost-containment and corner-algebra rows.  Until then, H-CB may use the
subset it actually imports, but MAIN-CB is not closed.

### 1.2 The MAIN-CB subtree still omits the relation and disjoint-merge mechanisms — BLOCKER

**Exact v2 loci:** rows 157--161 and parent wiring 234--242.

The source construction requires:

1. a maximum-dimensional commutative inclusion and a strict
   dimension-increasing refinement if one basis corner is not
   one-dimensional (`approximate_algebras.tex:1417-1426`);
2. transitivity of the relation
   \(j\sim k\iff S_{P_j,P_k}\ne0\), which uses the one-dimensional
   corner-product estimate (`tex:1428`, with `lem_PQR`);
3. cross-corner vanishing for distinct classes and a binary direct-sum
   merge satisfying the four-corner datum (`tex:1443`).

Row 157 instead speaks of iterating “nonzero orthogonal corner classes”;
row 158 has no `lem-extcb-one-dimensional-product` dependency; and row 160
asserts that the block maps “can be joined” without a row producing the
cross-class four-corner merging datum.  The union of rows 157--161 therefore
does not reconstruct the three printed stages.

**Correction:** withdraw rows 157--161 from the seedable proposal and replace
them by at least the refinement, maximality, corner-relation, cross-class
datum, one-class extension, one binary block merge, finite recombination, and
final assembly obligations listed in Registry impact C.  There is no safe
five-row ready-to-paste replacement in the present artifacts.

### 1.3 The stochastic-retract coverage gap is handled honestly — PASS AS BLOCKED

**Exact v2 loci:** lines 194--198 and 248--267.

The two uncontracted F2/F3 reservations do not reconstruct
`lem-routef-k-ledger`, but v2 says exactly that and forbids rewiring or
seeding.  This is a genuine open architecture input, not an additional
overclaim.  It remains a blocker to the ledger parent.

## 2. Faithfulness — INVALID

### 2.1 The Stage-1 maximality contract changes the source argument and uses a false literal — BLOCKER

**Exact v2 locus:** row 157.

The source chooses a commutative inclusion of maximum dimension and derives a
contradiction by constructing a larger one.  It does not prove the stated
iteration over “nonzero orthogonal corner classes.”  The images of an exact
projection basis under an approximate inclusion have small cross-products;
they are not literally orthogonal.

**Ready-to-paste correction:** replace row 157 by two `stated` rows:

> `lem-maincb-stage1-strict-refinement`: If a reset extended inclusion
> \(v_{\rm comm}:\mathbb C^m\to\mathcal A\) has a projection-basis image
> \(P_m\) with \(\dim S_{P_m}>1\), then the reviewed fresh-side, old-side,
> binary-merge, and improvement interfaces produce a reset extended
> inclusion \(\mathbb C^{m+1}\to\mathcal A\).

> `lem-maincb-stage1-maximality`: Every maximum-dimensional reset extended
> commutative inclusion into \(\mathcal A\) has
> \(\dim S_{P_j}=1\) for every projection-basis image \(P_j\).

The second depends on the first.  The first must import the binary merge and
error-improvement rows and remains `REFACTOR BEFORE SEEDING` until its MAIN
datum is defined.

### 2.2 Three EXT-CB children drop the smallness domains of their dependencies — MAJOR

**Exact v2 loci:** rows 107, 109, and 110.

`lem-extcb2-exact-representation` exists only for \(e\le e_{\rm rep}\), and
the four inverse maps exist only for \(e\le e_{\rm inv}\).  Rows 107, 109,
and 110 state their conclusions with no common smallness premise.  A
dependency edge does not silently add a hypothesis to a child contract.

**Ready-to-paste correction:** use the three thresholded replacement rows in
Registry impact B.  The eventual \(e_{\rm ext}\) may be their common minimum,
but every child must first be true on its own stated domain.

### 2.3 The ledger replaces several genuine guards by \(\eta\le\eta_A\) — BLOCKER

**Exact v2 loci:** rows 173--184, especially the normalization rows 178 and
181; threshold row 187.

The source requires, among other conditions,
\(\eta\le\varepsilon_E^{\rm corr}/C_A\),
\((C_T+C_{\Delta'})\eta\le1/2\), and
\((C_T+C_{\Upsilon'})\eta\le1/2\)
(`LEDGER-W74F-G-K.md:154-181,193-259`).  Its \(\eta_A\) is a source
linearization radius; v2 never states that it is below the MAIN-CB or
inverse-square-root radii.  Thus lines 173--184 are stronger than the
verified ledger.

There is no one-word correction: each family needs a named positive local
radius, those radii need small threshold-aggregation rows, and row 187 must
take their finite minimum.  Mark rows 173--184
`REFACTOR BEFORE SEEDING (GAP-LEDGER-DOMAINS)` until that sub-DAG exists.
Do not redefine \(\eta_A\) in terms of downstream constants; that would hide
a semantic cycle.

### 2.4 Amplified compression is stated outside its functional-calculus range — MAJOR

**Exact v2 locus:** row 72.

The compression is obtained by Banach functional calculus for a sufficiently
accurate approximate idempotent.  “For every pair of
\(\delta\)-projections” omits that domain.

**Exact correction text:** begin the contract:

> Amplified compression identity: there is a universal
> \(e_{\rm cmp}>0\) such that, whenever
> \(e=\delta+\varepsilon\le e_{\rm cmp}\), ...

and retain the two displayed amplification identities after that premise.

## 3. Contract hygiene — INVALID

### 3.1 Most H-CB children still rely on an unnamed ambient packet — BLOCKER

**Exact v2 loci:** rows 78--90, notably “every admissible
\(P,Q,R,n,Z,X\)” at line 80 and “under the hypotheses of” another result
at line 86.  Definition list 283--301 has no H-CB datum.

The contracts do not uniformly say that the ambient algebra is extended,
that \(Q\) is level-one one-dimensional, that the other projections are
\(\delta\)-projections, or that \(e=\delta+\varepsilon\).  They cannot use
`conj-hcb` as shorthand because the parent imports them.

**Correction:** add `def-hcb-datum` from Registry impact D and prefix every
H-CB child with “for every H-CB datum” plus its own explicit smallness
premise.  Replace “admissible” and sibling-hypothesis prose by the literal
datum and inequalities.  This is the same acyclic repair principle v2
correctly used for EXT-CB.

### 3.2 The five new MAIN-CB contracts are compound and meta-mathematical — BLOCKER

**Exact v2 loci:** rows 157--161; risks R16--R17 at lines 403--404.

The rows respectively package termination plus maximality plus invariant
preservation; equivalence plus block-size identification; a finite walk plus
map construction plus reset preservation; a finite merge sequence plus two
invariants; and the final existential theorem plus an all-level invariant.
Phrases such as “under the validated interfaces” and “from
`lem-maincb-equivalence-class-partition`” are not closed mathematical
hypotheses.  R16 and R17 concede missing obligations but defer the mandatory
factoring to a future prover.  The binding design rule requires factoring
now.

**Correction:** Registry impact C gives the minimum required obligation list.
No current row 157--161 is seedable.

### 3.3 The polar-chart row is an error-category packet, not one contract — MAJOR

**Exact v2 loci:** row 137; disposition line 40; risk R11 at line 398.

“Has the \(C^1\) approximate-unitary space and polar retraction ... with
polar, group-law, and first-derivative errors” combines construction,
regularity, a fixed-domain assertion, and three unnamed families of
inequalities.  `def-approximate-unitary-space` intentionally supplies only
notation, so “errors” has no contract-level meaning.

**Correction:** mark row 137
`REFACTOR BEFORE SEEDING (GAP-S1-POLAR-CONTRACT)` and extract separate
closed formula-level rows for (i) the polar retraction/domain, (ii) the
group-law comparison actually consumed downstream, and (iii) the derivative
estimate.  The permitted prose packet does not contain enough formula-level
text for a safe ready-to-paste three-row transcription.

## 4. DAG soundness — INVALID

### 4.1 The corner-equivalence row omits the edge that proves transitivity — BLOCKER

**Exact v2 locus:** row 158.

One-dimensionality only gives dimensions \(0\) or \(1\).  If
\(S_{P_j,P_k}\) and \(S_{P_k,P_\ell}\) are nonzero, transitivity uses the
nonzero compressed product supplied by
`lem-extcb-one-dimensional-product`.  That row is not a dependency.

**Exact dependency correction:**

```yaml
deps: lem-extcb-one-dimensional-product; lem-extcb-one-dimensional-corner-dimension; lem-extcb-corner-dimension-additivity; lem-compcb-amplified-compression-identities
```

This fixes the missing edge only; row 158 still requires the hygiene split
above.

### 4.2 The reset rows consume an unproduced \(C_{\rm split}\) — BLOCKER

**Exact v2 loci:** fresh inclusion row 149; raw/reset rows 153--156; risk R20
is unrelated and does not repair this.

Row 149 produces \(C_{\rm pair},e_{\rm pair}\), while row 153 defines
\(C_{\rm main}=\max\{C_{\rm co},C_{\rm split}\}\).  No proposal row defines
\(C_{\rm split}\).  The source defines it as a finite maximum and defines
\(e_{\rm split}\) as a finite minimum
(`PROOF-W74F-H-STAGE1.md:343-364`).

**Correction:** add `lem-stage1-common-split-ledger` from Registry impact A
and import it in `lem-maincb-split-corner-defect`, all three raw-reset rows,
and `lem-maincb-uniform-reset-chain`.

### 4.3 Stage 3 has no producer for the cross-class merge datum — BLOCKER

**Exact v2 loci:** rows 158--160.

Dimension additivity is used to show
\(S_{P_C,P_D}=0\) for distinct classes.  That is what permits the
direct-sum merge at the printed Stage 3.  Neither row 158 nor row 160 exports
this statement, and the generic four-corner theorem at line 103 applies only
after its datum has been produced.

**Correction:** add a `stated`
`lem-maincb-cross-class-merging-datum` followed by a `stated`
`lem-maincb-binary-block-merge`; make finite recombination depend on the
latter.  Exact target statements appear in Registry impact C.

### 4.4 Cycle check — PASS

The COMP-CB additions create no back-edge into H-CB, the EXT-CB parent is no
longer a semantic hypothesis of its children, and deletion of
`lem-stage1-two-side-packet` removes the v1 Stage-1/MAIN cycle.

## 5. Envelope realism — INVALID

### 5.1 The MAIN-CB projections are not credible — BLOCKER

**Exact v2 loci:** projected sizes 7/3, 4/2, 6/3, 5/3, and 5/2 on rows
157--161; parent claim 237--242; risks R16--R17.

The projections count the named imports but not the missing strict-progress
measure, relation proof, class-corner dimension calculation, cross-class
datum construction, finite inductions, and invariant preservation.  Those
are precisely the proof nodes.  The current numbers therefore measure a
table layout, not an af plan.

**Correction:** replace every projected-af cell on rows 157--161 by
`REFACTOR BEFORE SEEDING (GAP-MAIN-STRUCTURE)` until the Registry impact C
obligations are separate rows and then remeasure.

### 5.2 The 7/3 polar projection is unsupported — MAJOR

**Exact v2 loci:** row 137 and R11.

The cited source span contains inverse/implicit-function work, Neumann
control, manifold construction, polar regularity, group operations, and
derivatives.  A vague contract cannot justify a 7/3 projection.  Apply the
three-way contract split from finding 3.3 before estimating a tree.

### 5.3 What passed

The exact-target approximation is correctly marked `REFACTOR BEFORE
SEEDING (GAP-EA)`.  The H-CB and EXT-CB parent counts of 10/2 and 9/2 are
credible only after their imported children have closed contracts and have
actually validated.  The ledger parent correctly has no fictitious count.

## 6. Definition and external-input provisioning — INVALID

### 6.1 H-CB and MAIN-CB data vocabulary is missing — BLOCKER

**Exact v2 loci:** definition table 283--301; “admissible” in rows 80 and
153--155; “reset maximal commutative inclusion”, “corner classes”,
“single-level-one-map invariant”, and “Stage-2 block maps” in rows 150 and
157--161.

These are project-specific data/state notions, not common textbook terms.
They are neither existing definitions nor proposed definitions.

**Correction:** add the three `original / draft` datum-only proposals in
Registry impact D.  They must package inputs and notation only; termination,
existence, error bounds, and invariant preservation remain result contracts.

### 6.2 \(C_2\) has no result producer and \(\operatorname{def}_3\) is undefined — MAJOR

**Exact v2 loci:** rows 179, 183, 185--187; disposition line 36; risks
R19--R20.

The new degree-three row fixes the absence of \(C_3\) but introduces
\(\operatorname{def}_3\) without a definition.  Meanwhile \(C_2\) remains
only a promise that a future shard body will point to an inequality.  Bodies
do not export facts through the registry DAG.

**Correction:** add the expanded degree-two row and replace the degree-three
contract by the expanded formula in Registry impact B.  Then add
`lem-routef-degree-two-estimate` to the deps of rows 179, 183, 186, and 187.
No new `def_2`/`def_3` definition is needed.

### 6.3 External topology register — PASS, CONDITIONALLY

The seven external theorem inputs are listed and remain `cited candidate`.
In particular, the Hopf-structure row is correctly blocked on the exact
associativity/coassociativity hypothesis match, and the top-cohomology row
now includes “without boundary.”

## 7. Status law — VALID

The recomputed status counts are 65 `proved-mod-audit`, 12 `stated`, and
7 `cited candidate`.  No result is proposed above `proved-mod-audit`.
The five newly phrased MAIN-CB rows are `stated`; the exact-target,
four-corner merge, source-premise, IFT, and improvement rows are also
`stated`; and the topology leaves are not prematurely `cited`.

The defects above concern the truth domain, atomicity, and dependency
interfaces of rows, not an illicit promotion.  Any replacement MAIN-CB glue
must remain `stated`.

## 8. Gap honesty — INVALID

### 8.1 The named large gaps are honest — PASS

GAP-EA is loud, the F2/F3 ids are explicitly not result rows, and
`lem-routef-k-ledger` is correctly `DO NOT REWIRE OR SEED`.

### 8.2 Two smaller gaps are disguised as future shard-body work — MAJOR

**Exact v2 loci:** R11 at line 398, R16--R17 at 403--404, and R20 at
407; closure statement 421--434.

R20 explicitly leaves the \(C_2\) producer inside a future body; R11 defers
factoring a non-mathematical polar error packet; R16--R17 defer strict
progress and equivalence/block-size separation to future provers.  These are
architecture obligations under the binding design brief, not implementation
details.

**Correction:** promote them to the named pre-seeding gaps
`GAP-S1-POLAR-CONTRACT`, `GAP-MAIN-STRUCTURE`, and
`GAP-LEDGER-DOMAINS`; add the degree-two row now.  Amend the closure statement
to include those three names and the incomplete COMP-CB structure.

## 9. Disposition completeness — INVALID

The five repair-work-order blockers re-attacked directly are:

1. **COMP-CB — FAIL.** The five verdict-specified rows were copied, but
   source clauses needed by MAIN-CB were omitted (finding 1.1).
2. **EXT-CB semantic cycle — PASS WITH LOCAL CORRECTIONS.** The parent cycle
   is gone via `def-extcb-datum`; three children still need explicit
   smallness domains (finding 2.2).
3. **Stage-1 packet — FAIL.** The circular two-side wrapper is gone and
   isolation/trace are better factored, but the polar contract remains a
   compound unnamed error packet (finding 3.3).
4. **MAIN-CB assembly — FAIL.** The old root-sized omission has been renamed
   as five rows, but the strict refinement, relation transitivity, and
   disjoint-block merge are still absent (findings 1.2 and 4.3).
5. **Ledger finish — CORRECTLY UNRESOLVED.** PRH's positive-unital
   hypotheses are restored, and the F2/F3 bridge is honestly left
   uncontracted.  The parent remains blocked, as required.

The v1 corrections adding “without boundary,” positive quotient dimension,
the four named Stage-1 smallness clauses, the four requested small-\(\eta\)
clauses, the EXT datum, and the composite-definition retags are present.
That does not cure the new validity-domain regression in rows 173--184.

## 10. Repair-introduced regressions — INVALID

### 10.1 No new literal cycle and no status inflation — PASS

The COMP subtree is downward-only, the EXT cycle is removed, and all five
new MAIN structural rows are honestly `stated`.

### 10.2 New compound MAIN contracts — BLOCKER

**Exact v2 loci:** rows 157--161.

This is the principal repair regression.  The five rows expose names but not
atomic proof obligations.  Apply findings 3.2, 4.1, and 4.3.

### 10.3 New guard and constant regressions — BLOCKER

**Exact v2 loci:** rows 153--156 and 173--187.

The repair newly consumes an unproduced \(C_{\rm split}\), replaces several
local domains by \(\eta_A\), leaves \(C_2\) body-only, and introduces naked
\(\operatorname{def}_3\).  Apply findings 2.3, 4.2, and 6.2.

### 10.4 Wrong campaign issue in the phase map — MINOR

**Exact v2 locus:** line 370.

Campaign Phase 5 is `aism-y81y`, not `aism-fudw`
(`2026-07-24-af-elevation-campaign.md:37`).

**Exact correction text:**

> `### Phase 5 — stochastic-retract interface (`aism-y81y`)`

# Registry impact

Only the mechanically supportable corrections are given as complete rows
below.  The MAIN and ledger-domain gaps are withdrawal/refactoring
instructions, not authorization to invent replacement mathematics.

## A. New mechanically supportable result rows

| proposed id | kind / status | exact `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-compcb-amplified-compression-identities` | lemma / `proved-mod-audit` | Amplified compression identities: there is a universal \(e_{\rm cmp}>0\) such that, whenever \(e=\delta+\varepsilon\le e_{\rm cmp}\), every pair of \(\delta\)-projections \(P,Q\), every \(n\ge1\), and every \(X\in M_n\otimes\mathcal A\) satisfy \(Co_{P_n,Q_n}^2=Co_{P_n,Q_n}\) and \(Co_{P_n,Q_n}(X)^\dagger=Co_{Q_n,P_n}(X^\dagger)\), where \(P_n=I_n\otimes P\) and \(Q_n=I_n\otimes Q\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression` | `DECOMP-W74F-C-THMAINEXT.md:152-183`; pinned TeX 1054-1064, 1542-1544 | 4 / 2 |
| `lem-compcb-amplified-almost-containment` | lemma / `proved-mod-audit` | Amplified almost-containment: there are universal \(C_{\rm ac}<\infty\) and \(e_{\rm ac}>0\) such that, whenever \(e=\delta+\varepsilon\le e_{\rm ac}\), \(P_1,P,Q_1,Q\) are \(\delta\)-projections with \(\lVert P_1P-P_1\rVert,\lVert Q_1Q-Q_1\rVert\le\delta\), every \(n\ge1\), and \(X\in M_n\otimes S_{P_1,Q_1}\), one has \(\lVert Co_{P_n,Q_n}(X)-X\rVert\le C_{\rm ac}e\lVert X\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression`; `lem-compcb-amplified-compression-identities` | `DECOMP-W74F-C-THMAINEXT.md:154-181`; pinned TeX 1068-1075 | 5 / 3 |
| `lem-compcb-corner-algebra` | lemma / `proved-mod-audit` | Uniform compressed-corner algebra: there are universal \(C_{\rm ca}<\infty\) and \(e_{\rm ca}>0\) such that, whenever \(e=\delta+\varepsilon\le e_{\rm ca}\) and \(P\) is a nonvanishing \(\delta\)-projection, \(S_P\) with the compressed product, inherited involution, and compressed unit \(u_P=Co_P(P)\) is an extended \(C_{\rm ca}e\)-\(C^*\)-algebra. | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression-identities`; `lem-compcb-rectangular-product`; `lem-compcb-compressed-unit-action`; `lem-compcb-compressed-unit-norm` | `DECOMP-W74F-C-THMAINEXT.md:152-183`; pinned TeX 1077-1082 | 8 / 3 |
| `lem-stage1-common-split-ledger` | lemma / `proved-mod-audit` | Stage-1 common split constants: with the universal constants produced by the nontrivial-pair, fresh-pair, and old-side estimates, \(C_{\rm split}:=\max\{1,C_{\rm np},4C_{\rm np},C_{\rm pair},C_{\rm old}\}\) and \(e_{\rm split}:=\min\{e_{\rm np},e_{\rm pair},e_{\rm old},(2C_{\rm split})^{-1}\}\) are finite, positive, universal, and independent of dimension, amplification, block data, and stage index. | — | `lem-stage1-original-complementary-pair`; `lem-stage1-fresh-two-point-inclusion`; `lem-stage1-old-side-compression` | `PROOF-W74F-H-STAGE1.md:343-380`; Stage-1 verdict 157-177 | 4 / 2 |
| `lem-routef-degree-two-estimate` | lemma / `proved-mod-audit` | Route F degree-two estimate: there is a universal \(\eta_2>0\) such that, for \(0\le\eta\le\eta_2\), every amplification \(n\) and all \(X,Y\in M_n\otimes\mathcal B\) satisfy \(\lVert\Phi_n(\Delta_n(X)\Delta_n(Y))-\Delta_n(XY)\rVert\le C_2\eta\lVert X\rVert\lVert Y\rVert\), where \(C_2=C_{\Delta'}+4C_\Delta\) is finite and universal. | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-ai-defect-linearization`; `lem-routef-delta-prime-closeness`; `lem-routef-delta-normalization-closeness` | `LEDGER-W74F-G-K.md:193-226`; pinned TeX 2803-2812; G-verdict 119-128 | 6 / 3 |

## B. Exact replacement rows

| proposed id | exact replacement `contract:` value | exact replacement `deps:` | other exact change |
|---|---|---|---|
| `lem-compcb-amplified-compression` | Amplified compression identity: there is a universal \(e_{\rm cmp}>0\) such that, whenever \(e=\delta+\varepsilon\le e_{\rm cmp}\), every pair of \(\delta\)-projections \(P,Q\) in an extended \(\varepsilon\)-\(C^*\)-algebra and every \(n\ge1\) satisfy \(1_{M_n}\otimes Co_{P,Q}=Co_{I_n\otimes P,I_n\otimes Q}\) and \(M_n\otimes S_{P,Q}=S_{I_n\otimes P,I_n\otimes Q}\). | unchanged | — |
| `lem-compcb-single-compression-transfer` | unchanged | `lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities; lem-compcb-amplified-almost-containment; lem-compcb-corner-algebra; lem-compcb-rectangular-product` | remeasure; do not retain 6/3 without an af plan |
| `lem-extcb2-spatial-corner-system` | EXT-CB spatial corner system: there is a universal \(e_{\rm sp}>0\) such that every EXT-CB datum with \(e\le e_{\rm sp}\), together with an exact representation \(\mu_{11}\) satisfying the conclusion of `lem-extcb2-exact-representation`, admits one level-one unitary \(U_1:\mathbb C^r\to S_{P,Q}\); with the normalized \(U_2:\mathbb C\to S_{Q,Q}\), these unitaries define one exact spatial four-corner system \(\mu_{jk}\) whose amplifications use \(I_m\otimes U_j\). | `lem-extcb1-cross-corner-dimension; lem-extcb2-exact-representation` | retain P:`def-extcb-datum`; P:`def-spatial-four-corner-system` |
| `lem-extcb4-transported-corners` | EXT-CB transported corner comparison: there is a universal \(e_{\rm tr}>0\) such that, for every EXT-CB datum with \(e\le e_{\rm tr}\), the fixed spatial system and Ha inverses supplied by its dependencies define \(\gamma_{11}=v\) and \(\gamma_{jk}=(Ha^Q_{P_j,P_k})^{-1}\mu_{jk}\) for \((j,k)\ne(1,1)\), with \(\lVert(Ha^Q_{P,P})_m\gamma_{11,m}-\mu_{11,m}\rVert\le\kappa e\) and \((Ha^Q_{P_j,P_k})_m\gamma_{jk,m}=\mu_{jk,m}\) in the other three corners for every \(m\). | `lem-extcb2-spatial-corner-system; lem-extcb3-four-ha-inverses` | remove P:`def-four-corner-merging-datum` from this row |
| `lem-extcb4-complete-merging-datum` | EXT-CB complete merging datum: there is a universal \(e_{\rm dat}>0\) such that, for every EXT-CB datum with \(e\le e_{\rm dat}\), the four fixed transported corner maps satisfy `def-four-corner-merging-datum` at every amplification with common defect \(5(C_H+\kappa)e\). | `conj-hcb; lem-extcb3-four-ha-inverses; lem-extcb4-transported-corners` | — |
| `lem-maincb-equivalence-class-partition` | **WITHDRAW; replace by separate corner-relation, class-dimension, and cross-class-vanishing rows.** | add `lem-extcb-one-dimensional-product` and `lem-compcb-amplified-compression-identities` to the eventual relation row | projected af: `REFACTOR BEFORE SEEDING (GAP-MAIN-STRUCTURE)` |
| `lem-routef-degree-three-estimate` | Route F degree-three estimate: there is a universal \(\eta_3>0\) such that, for \(0\le\eta\le\eta_3\), every amplification \(n\) and all \(X,Y,Z\in M_n\otimes\mathcal B\) satisfy \(\lVert\Phi_n(\Delta_n(X)\Delta_n(Y)\Delta_n(Z))-\Delta_n(XYZ)\rVert\le C_3\eta\lVert X\rVert\lVert Y\rVert\lVert Z\rVert\), where \(C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'}\) is finite and universal. | unchanged | removes naked \(\operatorname{def}_3\) |
| `lem-routef-delta-phi-product` | unchanged apart from its future corrected local radius | add `lem-routef-degree-two-estimate` | — |
| `lem-routef-multiplicative-telescope` | unchanged apart from its future corrected local radius | add `lem-routef-degree-two-estimate` | — |
| `lem-routef-k-finiteness` | unchanged | add `lem-routef-degree-two-estimate` | — |
| `lem-routef-threshold-minimum` | **WITHDRAW pending a factored local-domain sub-DAG.** | eventual deps must include aggregated raw-factor, Delta, Upsilon, degree-two/three, MAIN, and PRH guard rows | projected af: `REFACTOR BEFORE SEEDING (GAP-LEDGER-DOMAINS)` |

## C. Required MAIN-CB replacement obligations

These are the exact mathematical interfaces the next factoring pass must
produce.  Their final ids may vary, but none may be recombined into the
current five packets.

| required id | status | exact target contract |
|---|---|---|
| `lem-maincb-stage1-strict-refinement` | `stated` | If a reset extended inclusion \(v_{\rm comm}:\mathbb C^m\to\mathcal A\) has a projection-basis image \(P_m\) with \(\dim S_{P_m}>1\), then the fresh-side, old-side, binary-merge, and improvement interfaces produce a reset extended inclusion \(\mathbb C^{m+1}\to\mathcal A\). |
| `lem-maincb-stage1-maximality` | `stated` | Every maximum-dimensional reset extended commutative inclusion into \(\mathcal A\) has \(\dim S_{P_j}=1\) for every projection-basis image \(P_j\). |
| `lem-maincb-corner-equivalence` | `stated` | For the one-dimensional projection-basis images \(P_1,\ldots,P_m\), the relation \(j\sim k\) if and only if \(S_{P_j,P_k}\ne0\) is an equivalence relation. |
| `lem-maincb-cross-class-merging-datum` | `stated` | For distinct equivalence classes \(C,D\), dimension additivity gives \(S_{P_C,P_D}=S_{P_D,P_C}=0\), and two reset block maps on \(S_{P_C}\) and \(S_{P_D}\), together with the zero off-diagonal maps, satisfy the four-corner merging datum at one common universal raw defect. |
| `lem-maincb-one-class-extension` | `stated` | For an equivalence class \(C=\{1,\ldots,s\}\), the finite compression/EXT-CB/reset induction produces one reset bijective level-one map \(M_s\to S_{P_C}\) carried by one level-one map at every amplification. |
| `lem-maincb-binary-block-merge` | `stated` | Two reset block maps for distinct classes, with the cross-class merging datum, produce after one four-corner merge and one improvement a reset bijective level-one map on their direct sum, preserving the single-level-one-map invariant. |
| `lem-maincb-stage3-finite-recombination` | `stated` | Repeated application of `lem-maincb-binary-block-merge` to the finite class set produces one reset bijective level-one map from the direct sum of all class matrix algebras. |
| `lem-maincb-structural-assembly` | `stated` | The maximum-dimensional Stage-1 selection, corner-equivalence partition, one-class maps, and finite recombination produce a finite-dimensional \(C^*\)-algebra \(\mathcal B\) and one bijective level-one map \(v:\mathcal B\to\mathcal A\) whose all-level maps are its amplifications. |

Every row above remains `REFACTOR BEFORE SEEDING` until the datum definitions
below exist and a fresh hostile review accepts its deps and projection.

## D. Definition proposal impact

| proposed def id | exact action |
|---|---|
| `def-hcb-datum` | **ADD, `original / draft` pending sign-off.** Datum only: an extended \(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\); a level-one one-dimensional \(\delta\)-projection \(Q\); \(\delta\)-projections \(P,R,S\); the corresponding compressed corners, amplified column spaces, and their defined sesquilinear forms; and \(e=\delta+\varepsilon\). It contains no column-norm comparison, Ha estimate, or inverse conclusion. |
| `def-maincb-reset-state` | **ADD, `original / draft` pending sign-off.** Datum only: a current compressed ambient algebra \(\mathcal A_Y\) with defect \(\varepsilon_Y\), an exact finite-dimensional source \(C^*\)-algebra, and one level-one map whose amplifications form the current reset extended inclusion. It contains no existence, termination, or preservation theorem. |
| `def-maincb-raw-call` | **ADD, `original / draft` pending sign-off.** Notation only for the input/output data of one Stage-1 split/merge, one Stage-2 compression/extension, or one Stage-3 binary merge. “Admissible” must be expanded into the literal defect and smallness inequalities; it is not part of the definition. |
