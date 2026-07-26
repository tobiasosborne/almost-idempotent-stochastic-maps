# AUDIT-MAIN-STRUCTURE — fresh hostile audit

**Status:** hostile design audit only. Nothing here is a proof, a status
promotion, or authorization to seed.

## 1. Final disposition

**DESIGN-REFUTED.**

All five defect claims against the v4.1 MAIN factoring are **CONFIRMED**.
In particular, v4.1 must not be seeded as written.  However, the proposed
repair is not well-founded:

1. its new reset threshold imports `e_dir`, `e_sim`, `e_close`, and `e_cross`
   before the rows producing them are landed, and two of those imports create
   actual dependency cycles;
2. its “close-corner transport” assumes, rather than proves, the load-bearing
   comparison between an original corner and a corner formed inside a
   compressed ambient algebra;
3. the existing validated single-compression row is instantiated by
   compression with the image of an ideal unit, not by the outer compression
   used in Stage 2 and Stage 3; and
4. the claimed separation of the two inductions omits the conditional family
   of one-class maps required as the initial data of recombination.

These are repair-design failures, not a dimension-dependent counterexample
and not evidence that Kitaev's theorem is false.  Thus the disposition is not
`ROUTE-ALARM`; a different, acyclic repair is needed.

The pinned TeX was checked against the manifest before auditing:
`refs/kitaev-2405.02434/approximate_algebras.tex` has SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching `refs/manifest/checksums.sha256:4`.

## 2. Verdicts on the five defect claims

### Defect 1 — four-corner bijectivity: **CONFIRMED**

The v4.1 refinement row imports `lem-extcb-four-corner-merge`
(`DESIGN-FUDW-DECOMP-v4.1.md:221`), and the landed contract really does require
four bijective corner maps
(`argument/lemmas/lem-extcb-four-corner-merge.md:4-6`).

That is stronger than the Stage-1 source step.  Kitaev's general merging lemma
concludes an inclusion without bijectivity and adds surjectivity only when all
four corner maps are bijective
(`approximate_algebras.tex:1325-1349`).  Its direct-sum corollary concludes an
inclusion from the two diagonal inclusions alone; the extra zero-cross-corner
hypothesis is used only for the optional bijective conclusion
(`approximate_algebras.tex:1352-1359`).  Stage 1 invokes precisely that
corollary to obtain an inclusion
(`approximate_algebras.tex:1419-1426`).

For a direct-sum source the off-diagonal source corners are zero.  The target
off-diagonal corners are not forced to vanish: already in the exact algebra
\(M_3\), \(P_1=e_{11}\) and \(P_2=e_{22}+e_{33}\) have
\(P_1M_3P_2\ne0\).  Thus no reading of the landed four-bijective-map contract
can justify the general Stage-1 move.  The source's weaker direct-sum
inclusion mechanism is genuinely needed.

### Defect 2 — binary merge non-iterability: **CONFIRMED**

The proposed binary contract accepts maps for two *distinct equivalence
classes* (`DESIGN-FUDW-DECOMP-v4.1.md:226`).  Its output is a map on the direct
sum of those two classes, which is not itself an equivalence class.  Therefore
the “repeated application” asserted in the next row is ill-typed after the
first merge (`DESIGN-FUDW-DECOMP-v4.1.md:227`).

An implicit union-class reading rescues Kitaev's compressed prose, but it
cannot rescue the literal v4.1 contract.  The source only says that the class
maps are “successively” merged (`approximate_algebras.tex:1443`); making that
sentence executable requires a union-stable conditional merge theorem.

### Defect 3 — zero-corner transport: **CONFIRMED**

Dimension additivity gives the original-ambient identity
\[
 \dim S_{P_U,P_V}
   =\sum_{j\in U,k\in V}\dim S_{P_j,P_k},
\]
by `approximate_algebras.tex:1363-1369`.  This supports zero original corners
for unions of distinct classes, exactly as suggested by the setup at
`approximate_algebras.tex:1428` and Stage 3 at line 1443.

It does **not** identify that corner with the off-diagonal corner formed using
the compressed product of \(A_{U\cup V}=S_{P_{U\cup V}}\).  Intermediate
binary merges cannot instead be performed in the original \(A\), because
\(P_U+P_V\) is not close to \(I_A\) until \(U\cup V\) is the full class set,
whereas the merge hypotheses require approximate complementarity
(`approximate_algebras.tex:1325-1326`;
`definitions/def-four-corner-merging-datum.md:13-24`).

The v4.1 dependencies provide amplification identities but no comparison
between the original compression idempotent and the nested-compressed one
(`DESIGN-FUDW-DECOMP-v4.1.md:224`).  The landed close-dimension theorem is
restricted to an EXT-CB datum and compares \(S_{v(I_r),Q}\) with \(S_{P,Q}\)
in one ambient algebra
(`argument/lemmas/lem-extcb1-close-corner-dimension.md:4-6`); it is not the
missing nested-corner theorem.

### Defect 4 — threshold omissions: **CONFIRMED**

The v4.1 reset radius
`DESIGN-FUDW-DECOMP-v4.1.md:216` omits exact hypotheses now present in its
consumers:

- IMPROVE-CB requires both universal
  \(\varepsilon_{\max}^{\rm cb}\) and \(\delta_{\max}^{\rm cb}\)
  (`argument/lemmas/lem-maincb-error-improvement.md:4`);
- four-corner merge requires the *total* defect
  \(\rho+\varepsilon\le a_{\rm merge}\)
  (`argument/lemmas/lem-extcb-four-corner-merge.md:4,18-25`);
- corner transitivity needs the product threshold \(e_{\rm PQR}\)
  (`argument/lemmas/lem-extcb-one-dimensional-product.md:4`) together with
  the smallness domain of the one-dimensional corner bound
  (`argument/lemmas/lem-extcb-one-dimensional-corner-dimension.md:4`); and
- compatible compression has its own \(e_{\rm co}\)
  (`argument/lemmas/lem-compcb-single-compression-transfer.md:4`).

This is a local-domain defect.  No one of these thresholds is
dimension-dependent.

### Defect 5 — missing assembly producers and conclusion: **CONFIRMED**

The maximality row is conditional on a maximum-dimensional reset inclusion
(`DESIGN-FUDW-DECOMP-v4.1.md:222`), but neither it nor the assembly dependency
list produces a nonempty bounded family from which such an inclusion can be
selected (`DESIGN-FUDW-DECOMP-v4.1.md:228,308-334`).

The assembly conclusion also states only a bijective level-one map whose
higher maps are amplifications (`DESIGN-FUDW-DECOMP-v4.1.md:228`).  It does not
state that these maps form an extended \(C\varepsilon\)-isomorphism.  The
consumer requires exactly that quantitative, amplification-uniform conclusion
(`argument/lemmas/lem-thmainext-conditional.md:4,26-30`).  Neither the word
“reset” in an upstream datum nor a dependency edge can strengthen the
assembly contract.

## 3. Verdicts on the seven proposed helper rows

### `lem-maincb-initial-reset-inclusion`:
**VALID-WITH-CORRECTIONS**

The scalar map \(\lambda\mapsto\lambda I_A\) has a universal
\(O(\varepsilon)\) amplified defect: the approximate-unit axioms are at
`approximate_algebras.tex:430-439`, the inclusion clauses at lines 443-455,
and \(\|X\otimes I_A\|=\|X\|\|I_A\|\) at lines 1467-1475.  IMPROVE-CB may then
reset it because the source is the finite-dimensional algebra \(\mathbb C\)
(`argument/lemmas/lem-maincb-error-improvement.md:4`).

The helper contract must explicitly quantify its raw constant and threshold,
assume the finite-dimensional MAIN ambient and
\(\varepsilon\le\varepsilon_{\max}^{\rm cb}\), and discharge the raw
\(\delta_{\max}^{\rm cb}\) bound before invoking IMPROVE-CB.  “If needed” is
not a contract.

### `lem-maincb-maximal-reset-selection`: **VALID**

For reset defect \(<1\), the level-one lower norm makes
\(\mathbb C^m\to A\) injective, hence \(m\le\dim_{\mathbb C}A\).  The preceding
initial row makes the feasible set nonempty.  A nonempty bounded subset of
\(\mathbb N\) has a maximum.  The contract must retain the design's stated
restriction to one fixed finite-dimensional ambient and one fixed reset
domain (`DESIGN-MAIN-STRUCTURE.md:120-137`).

### `lem-maincb-direct-sum-inclusion-merge`:
**VALID-WITH-CORRECTIONS**

The level-one result is exactly `cor_merge_sum`
(`approximate_algebras.tex:1352-1359`), derived from the non-surjective part
of the four-corner lemma (`approximate_algebras.tex:1325-1350`).  The tensor
section identifies amplified corners and permits applying the original
lemmas in \(M_n\otimes A\) (`approximate_algebras.tex:1542-1544,1557`).
The wider citation `1542-1557` in the design unnecessarily includes the known
unsquared display at lines 1551-1555; that display is not support for this
helper.

The contract must introduce universal \(C_{\rm dir},e_{\rm dir}\), a common
defect controlling the two diagonal maps, the two target projections, and
their complementarity, and conclude only an extended
\(C_{\rm dir}(\rho+\varepsilon)\)-**inclusion**.  It may claim bijectivity only
under the additional zero-target-cross-corner and bijective-diagonal
hypotheses from line 1358.

### `lem-maincb-close-corner-transport`: **REFUTED**

The abstract statement it cites is true: close bounded idempotents on one
Banach space have isomorphic ranges.  Indeed, the already validated proof
constructs the intertwiner
\(W=FE+(I-F)(I-E)\) under
\(\|E-F\|(2\|E\|+1)<1\)
(`proofs/lem-extcb1-close-corner-dimension/export.md:123-161`).

But this assumes the load-bearing fact.  The original compression acts on
\(A\); the compression internal to \(A_R=S_R\) acts on \(A_R\) with its
compressed product.  The design neither lifts the latter to an idempotent on
a common space nor proves an operator-norm comparison.  The source's
almost-containment statement is only one-sided
(`approximate_algebras.tex:1068-1075`).  Exact correction requires a separate
nested-corner comparison producer (or an expanded helper proving that
comparison) before the close-idempotent range lemma can be applied.

### `lem-maincb-stage2-extcb-datum`: **REFUTED**

The intended dimension count is sound *after* a genuine nested-corner
transport: atomic equivalence and additivity can supply the square, scalar,
and cross dimensions, after which injectivity plus equal finite dimension
gives bijectivity.  This matches the source Extension proof
(`approximate_algebras.tex:1378-1412`) and the exact EXT-CB hypotheses
(`argument/lemmas/conj-extcb.md:4-6`).

The proposed inputs do not presently produce the required compressed map.
The design says that `lem-compcb-single-compression-transfer` supplies it
(`DESIGN-MAIN-STRUCTURE.md:175-183`), but the validated proof instantiates
that row with an ideal \(J\), \(P=v(q)\), and
\(T=\operatorname{Co}_{P}\circ v|_J\)
(`proofs/lem-compcb-single-compression-transfer/export.md:17-18,63-65`).
Stage 2 instead uses the *outer* map
\(\operatorname{Co}_{P_{[1,r]}}\circ v_{r-1}\)
(`approximate_algebras.tex:1435-1441`).  A new outer-compatible compression
transfer, based on amplified almost-containment, is needed.  It must then be
combined with the missing nested-corner comparison, a common defect, and
explicit proofs of complementarity, \(\dim S_Q=1\), bijectivity onto \(S_P\),
and \(S_{P,Q}\ne0\).  Therefore this helper is not merely underspecified; its
listed dependency mechanism is wrong.

### `lem-maincb-improvement-one-step`:
**VALID-WITH-CORRECTIONS**

The norm-one finite-dimensional diagonal is at
`approximate_algebras.tex:1239-1254`; the cocycle correction and
\(O(d^2+\varepsilon)\) estimate are at lines 1256-1311.  The amplified proof
uses the same level-one correction entrywise and keeps the constants uniform
(`approximate_algebras.tex:1508-1535`).  A formal contract must state
universal \(K,e_{\rm step}\), the displacement bound
\(\|v^+-v\|_{\rm cb}\le Kd\), dagger preservation, and that every
amplification is generated by the same level-one \(v^+\).

### `lem-maincb-improvement-iteration`:
**VALID-WITH-CORRECTIONS**

Newton iteration, finite stopping for \(\varepsilon>0\), and convergence for
\(\varepsilon=0\) are stated at `approximate_algebras.tex:1313`; the extended
adaptation is at lines 1508-1535.  The contract must include a universal
initial basin, the cumulative displacement bound \(O(d_0)\), and the final
\(O(\varepsilon)\) defect.  The root still has to obtain uniform amplified
lower bounds from `approximate_algebras.tex:1483-1506` and preserve
bijectivity by a quantified Neumann radius.  The exact-target theorem cannot
replace this work because its codomain is \(B(H)\)
(`argument/lemmas/lem-extcb-exact-target-correction.md:4`), whereas
IMPROVE-CB has approximate codomain \(A\).

## 4. Hazard adjudications

### R19 — strict measure: **VALID**

The design correctly distinguishes bounded refinement from maximal
selection.  Each refinement changes \(m\) to \(m+1\)
(`approximate_algebras.tex:1419-1426`), so
\(\dim_{\mathbb C}A-m\) strictly decreases.  This proves termination, not
that an arbitrary terminal point is globally maximal.  Selecting a maximum
from the nonempty bounded feasible set first, then contradicting it by one
refinement, is the noncircular argument
(`DESIGN-MAIN-STRUCTURE.md:348-367`).  This clears R19 once the initial and
selection helpers exist.

### R21 — separation of inductions: **VALID-WITH-CORRECTIONS**

The two induction hypotheses are different, as the design says
(`DESIGN-MAIN-STRUCTURE.md:369-384`), and the v4.1 DAG deliberately keeps two
branches (`DESIGN-FUDW-DECOMP-v4.1.md:321-333`).  But cross-class
recombination necessarily consumes the *outputs* of the one-class
construction: Kitaev begins Stage 3 with all \(v_C\) already constructed
(`approximate_algebras.tex:1443`).

To make “join only at assembly” literal, finite recombination must be a
conditional theorem whose hypotheses include one reset isomorphism for every
equivalence class.  Structural assembly then instantiates those hypotheses
using `lem-maincb-one-class-extension`.  The proposed recombination interface
at `DESIGN-MAIN-STRUCTURE.md:256-269` does not state that input family.
Without this correction, either the recombination row has a missing
dependency or the assembly has an unexpressed application step.

### R22 — zero datum: **REFUTED**

Atomic zero dimensions followed by additivity are correct, but the design's
claim that its corrected mechanism “clears” R22
(`DESIGN-MAIN-STRUCTURE.md:386-393`) is false.  It still lacks:

1. the nested-corner operator comparison needed to transport zero dimension;
   and
2. outer-compatible compression of each diagonal reset map into
   \(A_{U\cup V}\), followed by the dimension argument that upgrades those
   compressed inclusions to bijections onto the diagonal target corners.

Only after both steps exist do the off-diagonal maps become legitimate
bijections \(0\to0\) and the four maps satisfy the landed merge contract
(`argument/lemmas/lem-extcb-four-corner-merge.md:4-6`).

## 5. Dimension-freeness and threshold dependency

No dimension-dependent entry was found.  The source makes every \(O(\cdot)\)
constant independent of additional data (`approximate_algebras.tex:458`),
the finite-dimensional diagonal has norm one even for direct sums
(`approximate_algebras.tex:1245-1254`), EXT-CB records independence of rank,
amplification, ambient dimension, and block data
(`argument/lemmas/conj-extcb.md:32-33`), and the landed IMPROVE-CB constants
are universal (`argument/lemmas/lem-maincb-error-improvement.md:4`).
The use of \(\dim A\) in maximal selection bounds a finite process; it is not
a stability constant.

The proposed corrected minimum is nevertheless **logically circular**.
`DESIGN-MAIN-STRUCTURE.md:428-440` places
\(C_{\rm dir},e_{\rm dir},e_{\sim},e_{\rm close},e_{\rm cross}\) inside the
reset package, while the landing order places the reset package at step 3,
the direct-sum and close rows at step 4, corner equivalence at step 5, and the
cross datum at step 7 (`DESIGN-MAIN-STRUCTURE.md:458-469`).

This is more than an ordering typo:

- v4.1 corner equivalence depends on maximality, which depends on refinement,
  which consumes the uniform reset chain
  (`DESIGN-FUDW-DECOMP-v4.1.md:221-223`); importing its \(e_{\sim}\) into the
  reset ledger closes a cycle;
- the cross datum depends on the uniform reset chain
  (`DESIGN-FUDW-DECOMP-v4.1.md:224`); importing its \(e_{\rm cross}\) into that
  ledger closes another cycle.

This directly contradicts the design's own no-forward-threshold rule
(`DESIGN-MAIN-STRUCTURE.md:442-456`) and R36
(`DESIGN-FUDW-DECOMP-v4.1.md:608`).

The exact architectural correction is to keep the upstream raw-reset ledger
dependent only on already-produced IMPROVE/COMP/EXT/direct-merge constants,
and place \(e_{\sim}\), nested-corner, and cross-datum thresholds in a
separate downstream MAIN-domain minimum used by structural assembly.
Alternatively, their threshold producers must be made purely conditional,
have all backward reset dependencies removed, and be landed before the raw
ledger.  The present design does neither.

## 6. Landing-order verdict

The proposed order is **REFUTED**.  Steps 3–7 are not topologically sorted for
the corrected threshold formula, and Stage 2/3 additionally wait on two
unlisted results: outer-compatible compression transfer and nested-corner
comparison.  The order can become well-founded only after the threshold
ledger is split as above, the two missing compression results are factored,
and finite recombination is made explicitly conditional on the family of
one-class reset maps.

Therefore:

- v4.1 MAIN factoring remains **DO NOT SEED**;
- the five defect findings are bankable only as design-audit findings;
- the seven-row repair is **not** an elevation plan in its current form; and
- no claim here changes the open or non-rigorous status of the MAIN chain or
  `op-classical`.
