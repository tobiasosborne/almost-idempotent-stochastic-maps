VERDICT: REDESIGN — B0a still uses an untyped ledger-witness anaphor; B0i leaves its quotient space unbound; B0s lacks a dimension-free ambient-ball antecedent.

# Hostile audit of `DESIGN-S1-ENDGAME-v3.md`

Date: 2026-07-30  
Role: fresh hostile design auditor  
Target: `DESIGN-S1-ENDGAME-v3.md` against the original brief, audit v2, and
the v3 repair brief

The factoring and most of the literal repair work are materially better.
B0b now imports the manifold package directly, the near-adjoint estimate is
present in every root on the B0a-to-B1 path, `r_bidx` is bound, architecture
(b) is implemented for C0/C1, and the Hatcher and Kitaev loci are accurate.
The design still cannot land. B0a retains the prohibited non-unique
“tuple supplied by lemma” choice, so B0i cannot legally reuse the same
row-13 witness when it invokes (A_7). B0i also fails to bind
`breve-calU`. Independently, B0s upgrades coordinate-chart injectivity to a
universal *ambient*-ball isolation statement without any root-contract clause
putting a universal ambient ball inside the displayed chart image. That
missing quantitative bridge is exactly where data or dimension dependence can
enter, and C0 later depends on the resulting radius.

## 1. Per-repair dispositions

| repair | disposition | audit |
|---|---|---|
| **R-F1** | **REPAIRED** | Final B0b directly lists `lem-stage1-quotient-manifold-package` and `lem-stage1-quotient-finite-cw` (`DESIGN-S1-ENDGAME-v3.md:61`). The former root gives the canonical quotient connected/compact/orientable/smooth/boundaryless/dimension package (`argument/lemmas/lem-stage1-quotient-manifold-package.md:4`), which supplies the compact/smooth/boundaryless antecedent of the latter root (`argument/lemmas/lem-stage1-quotient-finite-cw.md:4`). B0i separately imports the manifold package before the local-index root (`DESIGN-S1-ENDGAME-v3.md:59`); compactness, orientability, smoothness, isolation, and positive determinant match `argument/lemmas/lem-topology-local-index-sign.md:4`. The finite-triangulation root itself says only the conditional compact-smooth-boundaryless conclusion (`argument/lemmas/lem-topology-finite-triangulation.md:4`), and v3 does not improperly read more from it. |
| **R-F2** | **REPAIRED, at the stated root interfaces** | The literal estimate is in B0a (`DESIGN-S1-ENDGAME-v3.md:58`), B0i (`:59`), B0s (`:60`), final B0b (`:61`), and B1 (`:62`). The displayed map formulas and scalar covariance travel with it at every hop. F1 below still prevents the *proof* of the B0a-to-B0i same-witness hop, but no root-conclusion hop silently drops the estimate. |
| **R-F3** | **REPAIRED** | B0s, B0b, and B1 each existentially introduce the universal `r_bidx>0` they use (`DESIGN-S1-ENDGAME-v3.md:60-62`). The other conclusion constants are leading existential witnesses or named fields of the displayed `W`. The legality of B0a's way of choosing that `W` fails R-F4, not the narrow radius-name scan. |
| **R-F4** | **NOT-REPAIRED** | The class-before-representative order is repaired in B0b (`DESIGN-S1-ENDGAME-v3.md:61,258-260`) and B1 binds `breve-U` before `U_0,c,a,U` (`:62`). But B0a still says “writing `W=...` for one tuple supplied by `lem-stage1-polar-constant-ledger`” (`:58`). This is the same prohibited definite selection of a non-unique existential provider in different words. B0i then tries to use (A_7) for “the package's `W`” (`:214-220`). Also, B0i's existential list omits `breve-calU` while its conclusion uses it (`:59`). See F1-F2. |
| **R-F5** | **REPAIRED** | Architecture (b) is implemented. C0 depends only on B1 and eliminates one B1 package internally (`DESIGN-S1-ENDGAME-v3.md:90,289-304`). C1 depends on C0, not B1, and applies C0 once to one rectification (`:91,306-318`). The cited bridge range contains the formula at `approximate_algebras.tex:939` (`DESIGN-S1-ENDGAME-v3.md:90,458-460`). |
| **R-F6** | **REPAIRED** | The weak-Hopf external is restricted to connectedness and the positive-positive tail and explicitly imports no `Delta(1)` clause (`DESIGN-S1-ENDGAME-v3.md:432-438`). The 3C.4 external retains the exterior-tensor-polynomial conclusion (`:439-443`). A0 separately proves `Delta(1)` (`:139-141`), and A1 separately excludes polynomial generators and proves finiteness of the odd family (`:162-167`). |
| **R-F7** | **REPAIRED** | A0 declares real coefficients and explicitly binds a finite set `J_a` and its positive-degree tail factors (`DESIGN-S1-ENDGAME-v3.md:43`). A1 re-exports the same finite-family clause and uses `reals` throughout (`:44`). |
| **R-F8** | **REPAIRED as a factoring/budget surface, conditional on redesigning F1-F3** | The requested target/cap pairs are present exactly at `DESIGN-S1-ENDGAME-v3.md:495-509`, with targets at most ten and caps at most fifteen. A0+A1 is budgeted above the 13-node Hopf benchmark, and B0i+B0s+B0b above the 12-node quotient-index plus 7-node isolation benchmarks (`:511-516`). The advertised B0i/B0s feasibility is not presently realizable because of F1 and F3; their numerical envelopes have room for a repaired interface, but the current skeleton is not a proof plan. |

## 2. Blocking findings

### F1 — fatal — B0a still selects an untyped ledger witness, so B0i has no legal same-`W` (A_7) antecedent

B0a's root does not explicitly quantify a ledger witness and spell the
properties by which it is known to be that witness. Instead it says:
“writing `W=...` for one tuple supplied by
`lem-stage1-polar-constant-ledger`” (`DESIGN-S1-ENDGAME-v3.md:58`).
That is precisely a non-unique existential package selected by definite
description.

This is not rescued by `def-stage1-polar-witness-data`. That definition
contains only the fourteen scalar fields and explicitly contains no
positivity, existence, estimate, map, or admissibility assertion
(`definitions/def-stage1-polar-witness-data.md:13-28`). The analytic fact that
one `W` satisfies (A_1)-(A_7),(R) exists only in the ledger root
(`argument/lemmas/lem-stage1-polar-constant-ledger.md:4`).

The defect becomes load-bearing in B0i. Its skeleton applies B0a once and then
“instantiate[s] row-13 (A_7) for the package's `W`”
(`DESIGN-S1-ENDGAME-v3.md:214-220`). A fresh application of the existential
ledger root may choose a different `W`; B0a is not parameterized by a
previously fixed ledger witness, and its root does not export an object-level
predicate tying its `W` to (A_7). B0i's direct ledger dependency therefore
does not synchronize the witnesses.

The alternatives change the design interface: parameterize B0a/B0i on one
explicitly bound witness with every consumed ledger clause spelled out, or
reconstruct B0a's maps from B0i's own single ledger selection. The latter also
invalidates B0i's eight-node skeleton because it repeats B0a's reconstruction.
This is a typed-witness and antecedent failure, not a prose correction.

### F2 — fatal — B0i has an unbound quotient-space witness

B0i existentially binds `W`, six maps, and the sign-indexed chart maps, but it
does not bind “a space `breve-calU`” (`DESIGN-S1-ENDGAME-v3.md:59`). It then
uses `breve-calU` in

- `breve-calU=calU_e/U(1)`;
- the H-space and manifold conclusions;
- the domain/codomain of `breve-sigma`; and
- the local-index conclusion.

Unlike A0/A1's explicit “set `A=...`” binder (`DESIGN-S1-ENDGAME-v3.md:43-44`)
and unlike B0s/B0b/B1's explicit “and a space `breve-calU`” existential
(`:60-62`), B0i has neither an existential binder nor a `set`/`writing`
clause. A bare equation in the body of a `such that` clause does not quantify
its left-hand symbol.

The same B contracts introduce `breve-e` only through the bare expression
`breve-e=[J]` (`DESIGN-S1-ENDGAME-v3.md:59-62`), although no listed definition
reserves that notation. At minimum B0i's missing space binder is an
unambiguous free-symbol failure; the repaired contracts should explicitly set
`breve-e:=[J]` as well. Under the brief's rule, an untyped witness forces
REDESIGN even if the intended referent is evident.

### F3 — fatal — B0s has no dimension-free route from coordinate isolation to an ambient isolation ball

B0i exports:

- a chart `chi_s:B_{r_iso}^{icalH}(0)->calU`;
- an inverse only on `chi_s(B_{r_iso}^{icalH}(0))`;
- invariance of that chart image under `sigma`; and
- a derivative estimate for the coordinate map `F_s`

(`DESIGN-S1-ENDGAME-v3.md:59`).

It does **not** export any quantitative inclusion of the form

`calU intersect B_rho(sJ) subseteq chi_s(B_{r_iso}^{icalH}(0))`

for a universal `rho>0`, nor a dimension-free lower Lipschitz estimate for
`chi_s`. The QIFT root gives injectivity and image control *inside its Banach
coordinate ball* (`argument/lemmas/lem-stage1-quantitative-inverse-function.md:4`);
it does not say which ambient points of `calU` lie in that chart image.

Nevertheless B0s says there is one universal `r_bidx>0` for which `J` and
`-J` are the only actual fixed points in their ambient balls
(`DESIGN-S1-ENDGAME-v3.md:60`). Its skeleton simply says “translate chart
injectivity back to `calU`” and then choose a universal radius below the chart
radii (`:237-246`). A chart image is an open neighborhood, so this gives an
algebra-dependent positive ambient radius, not a uniform one. The coordinate
domain radius `r_iso` is not an ambient inradius.

The already validated `lem-stage1-uniform-inversion-isolation` root has exactly
the desired universal ambient-ball conclusion
(`argument/lemmas/lem-stage1-uniform-inversion-isolation.md:4`), but B0s does
not import it (`DESIGN-S1-ENDGAME-v3.md:60`), and its root's anaphoric
`sigma` would in any event require a same-map synchronization argument.

This missing bridge is dimension/data sensitive and propagates:
B1's distance bounds use `r_bidx` (`DESIGN-S1-ENDGAME-v3.md:62,285-287`), and
C0 uses them to exclude the two vanishing alternatives (`:299-304`). The
claimed dimension-freeness at `DESIGN-S1-ENDGAME-v3.md:377,380` is therefore
unproved.

## 3. Remaining contract-antecedent audit

### F4 — correctable — A2's prose names a dependency it does not import

A2's table has only A1 as a dependency
(`DESIGN-S1-ENDGAME-v3.md:45`). That is sufficient because A1's root
re-exports A0's finite-tail formula (`:44`). But the A2 skeleton says “Insert
A0's ... formula” (`:179`), and the budget table says A2 “now imports A0 and
A1 separately” (`:499`). It does not. Both phrases must say that A2 consumes
the finite-tail clause from A1's root; otherwise they violate the root-only
import rule. This is a dependency-description correction, not a mathematical
gap.

### F5 — correctable — A1 must make the grade-preserving consequence explicit

The exact printed 3C.4 conclusion says “isomorphic as an algebra”
(`refs/hatcher-algebraic-topology/AT.txt:17798-17800`), and v3 correctly
registers only that wording (`DESIGN-S1-ENDGAME-v3.md:439-443`). A1's contract,
however, concludes “isomorphic as a graded algebra”
(`DESIGN-S1-ENDGAME-v3.md:44`), which A2 uses to obtain homogeneous exterior
monomial bases (`:173-186`).

The homogeneous odd-generator construction can supply the grading
compatibility, and Kitaev's local guide states the graded formulation at
`approximate_algebras.tex:1016`; therefore this is not an independent
mathematical obstruction. But the A1 skeleton must explicitly derive that the
algebra isomorphism sending the exterior generators to the homogeneous
odd-degree generators preserves degree. It may not silently strengthen the
registered Hatcher external.

### F6 — note — all other direct root-contract consumptions checked cleanly

- **A0.** The Kunneth root requires CW spaces and finitely-generated-free
  cohomology in each degree (`argument/lemmas/lem-topology-kunneth-cross-product.md:4`).
  A0's connected CW and finite total real cohomology hypotheses imply those
  conditions. A0 itself derives the edge terms and `Delta(1)`.
- **A1-A3.** Each proposed dependency is earlier. A1 re-exports every
  coproduct clause A2 uses; A2 supplies exactly the associated-graded action
  A3 traces (`DESIGN-S1-ENDGAME-v3.md:44-46`).
- **B0a.** The smooth-atlas and smooth-polar-inverse roots are conditional on
  the displayed graph/polar data
  (`argument/lemmas/lem-stage1-smooth-unitary-atlas.md:4`;
  `argument/lemmas/lem-stage1-smooth-polar-inverse.md:4`), and the explicit
  operations root requires those same displayed maps
  (`argument/lemmas/lem-stage1-explicit-smooth-unitary-operations.md:4`).
  The ledger root contains the required (A_2),(A_4)-(A_6),(R) clauses. F1 is
  the failure to bind them to one legal `W`, not a conclusion-strength mismatch.
- **B0i.** Once the same-`W` problem is repaired, the manifold root and
  local-index root have the exact needed antecedents. QIFT supplies
  coordinate injectivity, but not F3's missing ambient inradius.
- **B0b.** Its direct manifold-to-finite-CW application is exact
  (`DESIGN-S1-ENDGAME-v3.md:64-79`). Its final root re-exports every B1 field.
- **B1.** The trace root receives connected finite-CW type, the H-space, and
  the displayed left inversion. The Lefschetz-Hopf root requires a finite
  polyhedron, finite fixed set, and pointwise maximal-simplex placement
  (`argument/lemmas/lem-topology-lefschetz-hopf.md:4`); under the singleton
  contradiction these are supplied by B0b and
  `lem-finite-polyhedron-maximal-simplex-placement`
  (`argument/lemmas/lem-finite-polyhedron-maximal-simplex-placement.md:4`).
  The top-cohomology root's connected/compact/orientable/boundaryless
  hypotheses are present
  (`argument/lemmas/lem-topology-orientable-top-cohomology.md:4`).
- **C0-C3.** C0 consumes B1 once. C1 uses ledger clause (A_1) on the
  level-one algebra of its extended input and applies C0 once. C2 consumes
  C1's one nontrivial projection. C3 consumes C2's jointly returned pair;
  no possibly-different pair is selected.

## 4. Source-fidelity audit

### F7 — note — Hatcher externals and A0 construction loci are faithful

The required `awk` extraction, counting lines by `\n`, confirms:

- `AT.txt:17620-17652` constructs `Delta` from `mu^*` and the inverse cross
  product, identifies its two edge components, and assumes path-connectedness
  plus finitely-generated-free cohomology.
- `AT.txt:17654-17677` states connectedness and the positive-positive
  coproduct-tail condition. It does not state `Delta(1)=1 tensor 1`.
- `AT.txt:17798-17800` concludes exterior tensor polynomial over a
  characteristic-zero field, “as an algebra.” It does not conclude
  exterior-only.

Thus v3's external descriptions at
`DESIGN-S1-ENDGAME-v3.md:429-448` are source-faithful. A0's new construction
locus and A1's polynomial/finiteness obligations are correctly separated.

### F8 — note — every cited Kitaev range was re-extracted; no wrong locus found

The newline-counted local TeX confirms:

- `:895-912` is the H-space/left-inversion definition and warning that only
  the first inversion homotopy is used.
- `:917-945` contains the projection alternatives, nontrivial-projection
  lemma, exact-unit reduction, and bridge. The formula
  `P=(2I+U+U^dagger)/4` and the `O(delta+epsilon)` conclusion are exactly at
  `:939`.
- `:945-969` contains the quotient phase lift, the five quotient properties,
  and the Lefschetz contradiction.
- `:971-1050` contains the trace proposition, coproduct/augmentation
  construction, exterior reduction, associated-graded argument, and trace.
- `:1192-1222` contains the smallness convention, Proposition
  `prop_delta_hominc`, and its proof; the statement is exactly at
  `:1194-1196`.
- `:1419-1424` contains the complementary pair and the two basis images.
- `:458` says the big-O functions do not depend on additional data.

The new v3 loci for A0, B0i, and B0s are genuine. B0s's source line `:943`
does assert constant-size isolation qualitatively, but it does not fill F3's
required root-contract derivation. The changed bridge ranges now all contain
`:939`.

## 5. M19-S1/M15 interface and completeness

### F9 — note — the three producer shapes match M19-S1/M15, conditional on F1-F3

M15 requires complementary outer target projections, an old inclusion when
`m>1`, a fresh `C^2` inclusion, fixed amplifications, and all defects below one
base scale
(`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md:343`).
M19-S1 supplies the selected extended corner and depends on the three exact
G-S1 ids plus old-side compression (`ibid.:381`).

Clause-by-clause:

1. Future M04 supplies the selected `S_{P_j}` as a finite-dimensional
   extended `L*epsilon`-C*-algebra with compressed unit
   (`DESIGN-MAIN-STRUCTURE-v5.md:287,381`).
2. `dim S_{P_j}>1` is exactly C1-C3's strict dimension hypothesis
   (`DESIGN-S1-ENDGAME-v3.md:91-93`).
3. C1 returns a nontrivial projection in that original corner algebra; C2
   returns one jointly selected complementary pair.
4. C3 applies C2 once and returns that same pair, the exact unit clause, one
   level-one map, exact basis images, and the canonical amplification family
   (`DESIGN-S1-ENDGAME-v3.md:93,329-344`).
5. The internal `P',P''` are not the outer M15 targets; the outer fresh target
   remains `P_j` and the C3 codomain is its corner
   (`DESIGN-S1-ENDGAME-v3.md:411-415`).
6. `lem-compcb-single-compression-transfer` supplies the old side when
   `m>1`; a finite universal maximum/minimum absorbs `L` and all producer
   constants/thresholds (`:415-418`).

The hand-off is honest: v3 says only G-S1 is removed and MAIN remains gated on
P0 and M01-M18 (`DESIGN-S1-ENDGAME-v3.md:118-122,563-566`). It does not claim
M19-S1 or any later MAIN row has become eligible.

### F10 — note — factoring preserves the requested conclusion surface syntactically

A1 re-exports all of A0 and adds the finite odd exterior conclusion
(`DESIGN-S1-ENDGAME-v3.md:43-44`). Final B0b re-exports the displayed maps,
H-space/left inversion, manifold/CW facts, local index, actual isolation, and
global phase lift (`:61,248-263`). B1 and C0-C3 retain the original extra-class
and three G-S1 outputs (`:62,90-93`). No old conclusion was visibly orphaned
by the split.

This is only syntactic coverage. F1 prevents the same-`W` proof of B0i, and F3
prevents the universal actual-isolation conclusion. Consequently the 13 rows
do not yet *jointly discharge* G-S1.

## 6. Dependency/status, contract form, definitions, and budgets

### F11 — note — status graph and serial order are otherwise clean

Every existing direct dependency named by the 13 row tables exists with
frontmatter `status: proved` and `af: validated`. This includes the four roots
called out in R-F1, all ten fixed B1 dependencies, the Kunneth leaf, row 13,
the smooth-operation helpers, QIFT, and every topology leaf. No retired,
parked, stated, seeded, or non-T0 row is imported.

The proposed graph

`A0 -> A1 -> A2 -> A3`,
`B0a -> B0i -> B0s -> B0b -> B1 -> C0 -> C1 -> C2 -> C3`,
with `A3 -> B1`,

is acyclic, and the serial order at `DESIGN-S1-ENDGAME-v3.md:95-116` is a
topological order. F1 is an object-identity failure inside that graph, not a
cycle or status failure.

### F12 — note — contract/definition surface is mostly compliant

All 13 contract values occupy one physical source line, use ASCII, and assign
no numerical value to a universal constant
(`DESIGN-S1-ENDGAME-v3.md:41-46,56-62,88-93`). No undefined package predicate
has been added. Every listed definition exists and is locked
(`definitions/INDEX.md`; design audit at
`DESIGN-S1-ENDGAME-v3.md:346-366`), so zero new definition shards remains
achievable.

The exceptions are semantic, not formatting: B0a's prohibited provider
anaphor (F1) and B0i's free quotient-space symbol (F2). The local coproduct,
filtration, chart, and displayed-map data do not themselves require new
definition shards.

### F13 — note — budget arithmetic is plausible only after the blocking interfaces are redesigned

The factored targets/caps are:

| row | target / cap |
|---|---:|
| A0 / A1 / A2 / A3 | 10/15, 7/11, 9/14, 4/8 |
| B0a / B0i / B0s / B0b / B1 | 8/12, 8/13, 7/12, 5/9, 10/15 |
| C0 / C1 / C2 / C3 | 8/12, 6/10, 6/10, 9/14 |

These respect cap 26 and the approximately-12 factoring rule
(`DESIGN-S1-ENDGAME-v3.md:493-516`). B0i's cap 13 is consistent with the
validated 12-node quotient-index benchmark, and B0s's target 7 matches the
validated isolation benchmark. But a repair that makes B0i reconstruct B0a,
or that adds a substantial quantitative ambient-chart theorem, must be
re-budgeted rather than hidden inside nodes 1, 3, or 6.

## 7. Required redesign surface

1. Eliminate B0a's “one tuple supplied by” construction. Choose one honest
   same-witness architecture: either parameterize the receiving rows on one
   explicitly quantified ledger witness and spell every consumed conjunct in
   roots, or reconstruct the maps from one ledger selection in the row that
   uses (A_7). Do not use an undefined `LedgerPackage(W)` predicate and do not
   apply the existential ledger twice.
2. Explicitly bind `breve-calU` in B0i and explicitly set/bind
   `breve-e=[J]` everywhere it is used. Re-scan all 13 contracts for free
   symbols after the rewrite.
3. Supply a dimension-free quantitative bridge from the B0i sign charts to
   ambient neighborhoods—most directly, a root clause with a universal
   ambient inradius or a uniform inverse-chart estimate. Merely calling
   `chi_s` a chart is insufficient. Preserve the identity of the displayed
   `sigma`.
4. Re-budget B0i/B0s after those repairs. If same-witness reconstruction or
   the ambient-inradius proof exceeds the present granularity, factor again.
5. Correct the A2 dependency prose to consume A1's re-export, and make A1's
   grade-preservation derivation explicit without strengthening the Hatcher
   external.
6. Preserve the successful surfaces: direct manifold imports, literal
   estimate re-export, bound `r_bidx`, C0/C1 architecture (b), exact Hatcher
   externals, line-939/line-458 provenance, zero new definitions if possible,
   T0-only acyclicity, the producer/M19 clause match, and the G-S1-only
   hand-off.
