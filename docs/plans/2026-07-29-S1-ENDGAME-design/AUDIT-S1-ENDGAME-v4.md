VERDICT: REDESIGN — R-G1 still applies and reselects the polar ledger in C1 after B1, and B0i/B0b lack the antecedent needed to consume the quotient-manifold root over the full parameterized epsilon_*^r range.

# Hostile audit of `DESIGN-S1-ENDGAME-v4.md`

Date: 2026-07-30  
Role: fresh hostile design auditor  
Target: `DESIGN-S1-ENDGAME-v4.md` against the original brief, audit v3, and
the v4 repair brief

The ambient-ball repair is mathematically credible: the exact-unit law and
(A_2) graph uniqueness do give the radius-`r_iso` ambient inclusion in the
ambient operator norm, and QIFT then gives same-map isolation. The design
nevertheless cannot land. Its headline claim that B1 is the unique ledger
instantiator is contradicted by C1's direct ledger dependency and skeleton.
Independently, the parameterized B0i root claims the compact orientable
quotient package for every `epsilon_r<=epsilon_*^r`, but the root it invokes
only supplies that package below a separate existential `e_quot^r`; v4
neither relates the two thresholds nor imports/spells the Maurer--Cartan
antecedent needed to reconstruct orientation. B0b repeats the bad direct
manifold-root application. Both defects touch mathematical contracts or
missing antecedents and therefore force REDESIGN.

## 1. Priority attack 1 — parameterization and the single ledger witness

### F1 — fatal — the ledger is applied twice, and C1 reselects a witness

V4 expressly says that B1 is the unique ledger instantiator
(`DESIGN-S1-ENDGAME-v4.md:14`) and that “no later row or node invokes it
again” (`:101-104`). B1 indeed applies
`lem-stage1-polar-constant-ledger` at its first node and passes that witness
to conditional B0b (`:275-282`).

But C1's row has a second direct dependency on
`lem-stage1-polar-constant-ledger` (`DESIGN-S1-ENDGAME-v4.md:132`), and C1's
first skeleton node says “Fix one row-13 tuple and its single (A_1)
rectification” (`:308-315`). C0 has deliberately forgotten B1's package
(`:297-306`), so C1 cannot be receiving the B1 witness; it necessarily
eliminates the existential ledger again and selects another `W`.

This fails the v4 brief's test literally: the ledger root is not applied
exactly once across all thirteen rows, and a downstream C row reselects
rather than receiving the typed witness. It also falsifies v4's dependency
summary, which displays only one ledger edge entering B1
(`DESIGN-S1-ENDGAME-v4.md:447-458`).

The mathematics of C1 may be repairable by importing an already-T0
rectification theorem such as
`lem-stage1-rectified-cstar-control` (whose actual root directly supplies
the exact-unit rectification) instead of applying the global ledger, or by
carrying the same ledger witness through C0. Either repair changes a direct
dependency/witness interface and the current proof architecture; it is not
a mechanical wording edit.

### F2 — fatal — the parameterized manifold conclusion has no root-valid range

B0i quantifies every exact-unit algebra with
`0<=epsilon_r<=epsilon_*^r` and concludes that `breve-calU` is a connected,
compact, orientable smooth manifold without boundary of the stated
dimension; its dependencies include
`lem-stage1-quotient-manifold-package`
(`DESIGN-S1-ENDGAME-v4.md:94`). Its skeleton says to apply that root
directly (`:233-249`).

The actual root does **not** conclude this at `epsilon_*^r`. It says only
that there exists a separate universal `e_quot^r>0` and gives the manifold
package when `epsilon_r<=e_quot^r`
(`argument/lemmas/lem-stage1-quotient-manifold-package.md:4`). Neither the
ledger root nor B0i's antecedent states
`epsilon_*^r<=e_quot^r`. The parameterized root cannot “derive one receiving
threshold” and then prove a conclusion for every input all the way up to
the already-fixed `epsilon_*^r`.

Nor does B0i reconstruct the missing package from its displayed
antecedents. In particular, v4 omits ledger clause (A_3), imports neither
`lem-stage1-maurer-cartan-trivialization` nor its parameterized transport,
and has no root clause giving the global tangent trivialization used for
orientation. The actual Maurer--Cartan root contains precisely that global
bundle trivialization
(`argument/lemmas/lem-stage1-maurer-cartan-trivialization.md:4`).
Root-only consumption forbids recovering it from a dependency body or from
the dependency closure of the non-parameterized manifold package.

B0b repeats the problem: it is still universal up to
`epsilon_*^r`, directly lists the same manifold root, and its skeleton again
says “Apply the manifold root directly”
(`DESIGN-S1-ENDGAME-v4.md:96,265-273`). B0b can apply the conditional
finite-CW root once compact/smooth/boundaryless data are valid
(`argument/lemmas/lem-stage1-quotient-finite-cw.md:4`), but that does not
repair the absent manifold antecedent.

This is a parameterization regression: the former existential receiving
threshold was removed, while an unrelated T0 threshold was treated as if it
were one of the fields of `W`. The repair must either:

1. parameterize the B rows at an explicitly bound common receiving radius
   below `epsilon_*^r` and every non-parameterized provider threshold; or
2. add and spell the actual parameterized manifold/orientation antecedents,
   including the (A_3) same-graph Maurer--Cartan data, and rederive the
   package.

Either option changes contract meaning and requires rebudgeting.

### F3 — correctable — B1's claimed direct use of (R) is not literal

B1's first node says it “record[s] the exact
(A_2),(A_4)--(A_7),(R) conjuncts appearing in the B1 root” from the ledger
(`DESIGN-S1-ENDGAME-v4.md:275-282`). The ledger's actual (R) clause is
quantified over `epsilon_X<=e_S1` after setting
`epsilon_r=C_rect*epsilon_X`
(`argument/lemmas/lem-stage1-polar-constant-ledger.md:4`). The
parameterized B contracts instead assume an arbitrary exact-unit algebra
with `epsilon_r<=epsilon_*^r` and assert the specialized guards directly
(`DESIGN-S1-ENDGAME-v4.md:93-97`).

Those guards are elementary consequences of the displayed minimum formula
for `epsilon_*^r`, so this is not a third mathematical obstruction. But the
ledger root does not hand them over in the claimed quantifier form. B1 needs
an explicit scalar-arithmetic derivation rather than saying the root's (R)
clause is verbatim identical. That obligation must remain visible when F1
and F2 are redesigned.

### Same-witness result inside B0a--B1

Apart from F2, the parameterized B chain itself is synchronized correctly.
B0a--B0b quantify `W` before the algebra and repeat the formulas for the
same graph functions, polar inverse, `mu`, and `sigma`
(`DESIGN-S1-ENDGAME-v4.md:93-96`). B1 binds one ledger witness and calls
B0b on that witness (`:277-282`). B0b binds a fixed class before
`U_0,c,a`, and B1 binds `breve-U` before `U_0,c,a,U` (`:96-97`). No
definite-description reselection occurs on that B-only path.

The specialized clauses omit some ledger conclusions that are not consumed
(for example the quantitative `g_V` displacement bound and the polar-set
outer inclusions); that omission is not itself a weakening used later.
The smooth-atlas, smooth-polar-inverse, and explicit-operation roots receive
the graph uniqueness, normal invertibility, displayed diffeomorphism,
domain-defined operations, and same formulas they actually require
(`argument/lemmas/lem-stage1-smooth-unitary-atlas.md:4`;
`argument/lemmas/lem-stage1-smooth-polar-inverse.md:4`;
`argument/lemmas/lem-stage1-explicit-smooth-unitary-operations.md:4`).

## 2. Priority attack 2 — the ambient-ball bridge

### Result — the bridge and `r_bidx=r_iso` survive hostile checking

B0i exports

`calU intersect B_{r_iso}(sJ) subseteq chi_s(B_{r_iso}^{icalH}(0))`

and

`||A-B||<=||chi_s(A)-chi_s(B)||`

for its same displayed charts and `sigma`
(`DESIGN-S1-ENDGAME-v4.md:94`). The derivation is summarized at
`:105-120` and budgeted at B0i nodes 4--5 (`:239-243`).

The QIFT root itself supplies Banach-space injectivity, two-sided
Lipschitz control, and an image ball in the norm in which its Banach spaces
are posed (`argument/lemmas/lem-stage1-quantitative-inverse-function.md:4`).
Applied to `Theta_s(B)=sJ+sB` on the underlying ambient Banach space with
`V=sI`, its derivative error is zero, so there is no norm conversion or
dimension-dependent constant.

More importantly, the graph capture can be checked directly. If
`U in calU` and `||U-sJ||<r_iso`, put `B=s(U-sJ)`. Exact unitality gives
`U=sJ bold-dot (J+B)`. The anti-Hermitian and Hermitian projections
`A=(B-B^dagger)/2` and `K=(B+B^dagger)/2` each have norm at most `||B||`
because `dagger` is isometric. Since `U^dagger bold-dot U=J`,
the displayed (A_2) equation gives `f_{sJ}(A+K)=0`; (A_2) uniqueness forces
`K=g_{sJ}(A)`. Thus `U=chi_s(A)` with `||A||<r_iso`. Taking the
anti-Hermitian part of a chart difference similarly gives the claimed
lower-Lipschitz constant `1`. All norms here are the ambient operator/Banach
norm or its restricted subspace norm.

B0s then applies QIFT to `G_s=F_s-id`. From
`||DG_s+2I||<1`, choosing `V=-2I` gives
`||V^(-1)DG_s-I||<1/2`, hence injectivity on the coordinate ball.
Covariance from the same B0a package gives `sigma(sJ)=sJ`, so `G_s(0)=0`.
The ambient inclusion first captures any ambient fixed point in that same
chart, and injectivity forces its coordinate to be zero
(`DESIGN-S1-ENDGAME-v4.md:252-263`).

Consequently `r_bidx=r_iso` is legitimate, not merely
`r_iso/C`: `r_iso` is a positive universal field of the bound witness, and
the strict-ball convention avoids a boundary claim. The equality assigns
one bound witness to another, not a numerical value to a universal
constant. The same formula-defined `sigma` is retained, and B1's distance
bounds and C0's two vanishing-alternative exclusions remain dimension-free
(`DESIGN-S1-ENDGAME-v4.md:291-305`).

R-G3 is therefore repaired. F2 independently prevents B0i's full
manifold/index package from landing, but it does not invalidate this
ambient-norm calculation.

## 3. Per-repair dispositions

| repair | disposition | audit |
|---|---|---|
| **R-G1** | **NOT-REPAIRED** | B1 does instantiate the B chain once, but C1 directly imports and re-eliminates the ledger (`DESIGN-S1-ENDGAME-v4.md:132,277-282,308-315`). In addition, B0i/B0b cannot apply the separate-threshold manifold root over their full parameterized range (`:94,96,233-249,265-273`; `argument/lemmas/lem-stage1-quotient-manifold-package.md:4`). |
| **R-G2** | **REPAIRED** | B0i now existentially binds `a space breve-calU`; every B contract binds the quotient space before its equation and says `set breve-e:=[J]` at first use (`DESIGN-S1-ENDGAME-v4.md:93-97`). The independent free-symbol scan below found no remaining blocking free conclusion witness. |
| **R-G3** | **REPAIRED** | The radius-`r_iso` ambient inclusion and constant-one lower-Lipschitz estimate follow from exact unitality, the norm-one Hermitian splitting, and (A_2) uniqueness; QIFT then gives same-map coordinate isolation (`DESIGN-S1-ENDGAME-v4.md:94,105-120,233-263`). No ambient/coordinate norm mismatch was found. |
| **R-G4** | **NOT-REPAIRED** | The printed pairs are exactly the requested `10/15, 8/12, 9/14, 4/8, 8/12, 10/15, 7/12, 5/9, 11/15, 8/12, 6/10, 6/10, 9/14`, totaling 98 targets (`DESIGN-S1-ENDGAME-v4.md:460-483`). But B0i node 2 conceals the absent common-threshold/orientation obligation, and the proposed repairs to F2 require either a new antecedent/provider or a reconstruction. The present ten-node B0i budget therefore does not price the actual proof. |
| **R-G5** | **REPAIRED** | A1 has explicit grading nodes 6--7 and keeps 3C.4 at “as an algebra”; A2 node 4 consumes the finite tail from A1's root only (`DESIGN-S1-ENDGAME-v4.md:179-206,464-467`). |

## 4. Full attack fronts

### Front 1 — contract antecedents and root-only imports

**F4 — fatal (same defect as F2).** The B0i/B0b manifold applications lack
the threshold relation and parameterized orientation provider described in
F2. This is the only new root-antecedent fatal found.

All other direct uses checked as follows:

- A0 satisfies the Kunneth root: finite total real cohomology gives
  finite-dimensional, hence finitely generated free, real cohomology in
  each degree
  (`argument/lemmas/lem-topology-kunneth-cross-product.md:4`).
- A1 consumes A0's root and the exact weak-Hopf/3C.4 externals. A2 consumes
  only A1; A3 consumes only A2.
- B0a's same graph and polar objects match the three smooth roots quoted
  above. Its quotient H-space and left-inversion homotopies use the
  displayed operation estimates and projected paths, not a second ledger
  selection.
- B0s receives the same charts and `sigma` from B0i and applies QIFT in the
  norm required by its root.
- Once manifold data are valid, the finite-CW root's exact conditional
  antecedent is compact, smooth, and boundaryless
  (`argument/lemmas/lem-stage1-quotient-finite-cw.md:4`).
- B1's Lefschetz-Hopf application has a finite singleton fixed set under
  the contradiction and maximal-simplex placement; the trace and top
  cohomology roots receive their literal hypotheses
  (`argument/lemmas/lem-topology-lefschetz-hopf.md:4`;
  `argument/lemmas/lem-topology-orientable-top-cohomology.md:4`;
  `argument/lemmas/lem-finite-polyhedron-maximal-simplex-placement.md:4`).
- C0 consumes B1 once. C2 consumes C1's one projection, and C3 consumes
  C2's jointly returned pair.

**F5 — note — the fixed B1 list contains intentionally unused/anaphoric
roots.** V4 keeps the ten fixed dependencies and adds the ledger and B0b
(`DESIGN-S1-ENDGAME-v4.md:97`). Its skeleton actually obtains same-map
isolation, manifold/CW data, H-space data, index, and phase lifting from
B0b, and explicitly says the fixed uniform-isolation root is not used
(`:121-123`). This avoids an identity error, but future landing must not
pretend that an anaphoric T0 root proves a property of the displayed map.
The fixed ten may remain as mandated bookkeeping; the proof must consume
only conclusions whose objects are synchronized.

### Front 2 — typed witnesses and free symbols

**F6 — fatal (same defect as F1).** C1's fresh row-13 tuple is the only
downstream reselection. C0 exports no `W`, so it cannot be interpreted as
the B1 witness.

The independent scan of all thirteen contracts otherwise passes:

- A0/A1 bind `M,mu,e,A,A^+,Delta` and the finite tail; A2 binds the
  filtration data and quantifies the indices in its concluding range; A3
  quantifies `k`.
- Each conditional B row quantifies `W` before its fields, the algebra
  before `calU,J`, and binds every formula-defined map before re-export.
- B0a--B0b bind a space `breve-calU` before the quotient equation and set
  `breve-e` before its first H-space/index occurrence
  (`DESIGN-S1-ENDGAME-v4.md:93-96`).
- B0b binds `breve-V` before `U_0,c,a`; B1 binds `breve-U` before
  `U_0,c,a,U` (`:96-97`).
- C0--C3 existentially introduce every output constant, projection, pair,
  and map. No bare equation is used as the sole binder of a conclusion
  witness.

R-G2 therefore holds.

### Front 3 — source fidelity

**F7 — note — all v4 source loci checked byte-faithful under `\n` counting.**

- `AT.txt:17620-17652` constructs the coproduct and its two edge terms.
- `AT.txt:17654-17677` states connectedness and the positive-positive
  coproduct tail; it does not supply `Delta(1)`.
- `AT.txt:17798-17800` states exterior tensor polynomial **as an algebra**.
- `approximate_algebras.tex:895-912` contains the H-space/left-inversion
  definitions.
- `:917-945` contains the nontrivial-projection statement, exact-unit
  reduction, bridge formula at `:939`, and constant-size qualitative
  isolation at `:943`.
- `:945-969` contains the quotient phase lift, the five quotient
  properties, and the Lefschetz contradiction.
- `:971-1050` contains the trace proposition and proof; `:1016` is the
  graded exterior guide, not a strengthening of Hatcher's external.
- `:1192-1222` contains the smallness convention and
  `prop_delta_hominc`, whose exact statement is `:1194-1196`.
- `:1419-1424` contains the corner complementary pair and the two basis
  images.
- `:458` says big-O instances do not depend on additional data.

The only v3-to-v4 locus changes are the narrowed/clarified A1 guide
(`:1016`, `:1009-1022`) and wording that points directly to the existing
bridge/external lines; they are correct. No new source or external was
added.

### Front 4 — M19-S1 and M15

**F8 — note — the producer interface still matches, conditional on
redesigning F1/F2.**

M15 requires complementary target projections, an old inclusion when
`m>1`, a fresh `C^2` inclusion, fixed amplification families, and a common
defect scale
(`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:343`).
M19-S1 assumes the selected extended corner and depends on the three exact
producer ids plus old-side compression (`ibid.:381`).

C1 accepts the selected finite-dimensional extended corner and returns a
nontrivial original-corner projection. C2 returns that projection and its
same selected complement with exact sum equal to the corner unit. C3
consumes the same pair and returns one extended `C^2` inclusion, exact unit
and basis images, and the canonical amplification family
(`DESIGN-S1-ENDGAME-v4.md:131-134,317-337,394-404`). The internal pair is
not confused with M15's outer target projections. A finite universal
maximum/minimum absorbs the M04 corner scale and all producer/old-side
coefficients.

The hand-off correctly claims only G-S1: MAIN still requires P0 and
M01--M18 (`DESIGN-S1-ENDGAME-v4.md:154-158,504-521`).

### Front 5 — contract form

**F9 — note — physical form passes.** All thirteen contract values are one
physical ASCII line (`DESIGN-S1-ENDGAME-v4.md:80-83,93-97,131-134`).
Every conclusion coefficient/radius is an input field or an explicitly
introduced existential. `r_bidx=r_iso` equates two bound witnesses; it does
not assign a numerical constant. The fixed rational entries in the
ledger-derived minimum formulas define fields relative to the existential
coefficient/margin witnesses and do not state an absolute numerical value
for `r_iso`.

### Front 6 — dependency status, acyclicity, and serial order

**F10 — note — status and order pass apart from the false single-ledger
claim.** Every existing dependency named in the tables has
`status: proved` and `af: validated`; no retired/stated parent is imported.
All proposed dependencies point earlier in the displayed serial order
(`DESIGN-S1-ENDGAME-v4.md:136-158`). The proposed graph is acyclic.

The graph description at `:449-453` is incomplete because it omits C1's
second existing ledger edge. Adding that edge does not create a cycle, but
it is the fatal witness-reselection defect F1.

### Front 7 — dimension-freeness

**F11 — note/fatal split.** The ambient bridge, isolation radius, B1
distance bounds, C0 projection bridge, and C1--C3 fixed-term estimates are
dimension-free for the reasons in section 2 and
`DESIGN-S1-ENDGAME-v4.md:360-375`.

F2 prevents the parameterized quotient manifold/index statement from being
proved over the claimed range. This is not evidence that the topology is
dimension-dependent; it is a missing root antecedent. V4 may not label the
whole B0i package dimension-free until the common threshold and
orientation provider are explicitly supplied.

### Front 8 — definition layer

**F12 — note — zero new definitions is sound.** Every listed definition
exists and is locked (`definitions/INDEX.md`). The long hypotheses are
result-local conjuncts rather than an undefined `LedgerPackage(W)`
predicate. Cohomology, graded/exterior algebra, associated graded, trace,
and `C^2` are textbook notions. No new definition shard is required by the
successful ambient bridge.

### Front 9 — completeness

**F13 — fatal by propagation.** Syntactically the thirteen rows retain the
trace chain, extra fixed class, fixed-unitary projection bridge, rectified
projection, complementary pair, and fresh two-point inclusion. Nothing is
orphaned at the level of displayed conclusions.

Semantically, F1 means the advertised single-witness architecture is not
the architecture of the C chain, and F2 means B0i/B0b do not have a legal
manifold/index proof at their stated parameterized range. B1 therefore
cannot instantiate a valid complete quotient package, so C0--C3 do not yet
jointly discharge the three G-S1 producers.

## 5. Required redesign surface

1. Remove C1's second application of
   `lem-stage1-polar-constant-ledger`. Either give C1 a direct T0
   exact-unit rectification provider whose contract needs no `W`, or carry
   B1's same typed witness through C0 into C1. Update the contract/deps,
   skeleton, graph prose, and budget consistently.
2. Repair the parameterized quotient-manifold interface. A B row quantified
   up to `epsilon_*^r` cannot directly consume a theorem quantified only up
   to an unrelated existential `e_quot^r`. Add a common receiving threshold
   to the parameterized architecture, or spell/import enough same-graph
   (A_3) Maurer--Cartan data to reconstruct compactness, orientation,
   smoothness, boundarylessness, and dimension without the
   non-parameterized root.
3. Rebudget B0i/B0b after item 2. The present ten-node B0i skeleton hides
   the range/orientation obligation.
4. Correct B1's scalar-arithmetic prose: the ledger's (R) quantifier is over
   rectified `epsilon_X`; derive the guards for arbitrary exact-unit
   `epsilon_r<=epsilon_*^r` from the displayed minima instead of calling
   them literal root conjuncts.
5. Preserve the successful repairs: explicit quotient/basepoint binders,
   the same-map radius-`r_iso` ambient bridge, A1's explicit grading step,
   A2's A1-root-only tail use, exact source loci, zero new definitions,
   T0-only acyclicity, the M19/M15 producer shapes, and the G-S1-only
   hand-off.
