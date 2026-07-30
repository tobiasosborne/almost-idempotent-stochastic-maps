VERDICT: REDESIGN — B0b lacks its manifold antecedent, and B1/C0/C1 still do not expose one fully typed same-package witness (including a bound `r_bidx`).

# Hostile audit of `DESIGN-S1-ENDGAME-v2.md`

Date: 2026-07-30  
Role: fresh hostile design auditor  
Target: `DESIGN-S1-ENDGAME-v2.md` against both binding briefs and audit v1

The Hatcher repair is mathematically viable, C3's missing universality locus is
repaired, and the G-S1-only hand-off is now honest. The design nevertheless
cannot land. B0b asserts manifold properties without importing the root that
supplies them; B1 uses an unbound `r_bidx` and relies on a B0a estimate that
B0b does not re-export; and C1 purports to apply C0 to a selected B1 package
although C0's contract is not parameterized by such a package. These are
missing antecedent / typed-witness failures, not mechanical prose defects.

## 1. FIRST JOB — L1 ground truth

### 1.1 File and manifest

`refs/hatcher-algebraic-topology/AT.txt` exists. Its SHA256 is
`9f69088c02fbe1354fdc342c495ac04a59c9a8d16e4517ce2d6b7d989cf1cf06`,
which matches `refs/manifest/checksums.sha256:13`.

The following is the actual `awk` extraction, with lines counted by `\n` only.

`refs/hatcher-algebraic-topology/AT.txt:17654-17677`:

```text
17654:We can summarize this situation by saying that H ∗ (X; R) is a Hopf algebra, that
17655:L
17656:n
17657:over a commutative base ring R , satisfying the
17658:is, a graded algebra A =
17659:n≥0 A
17660:
17661:following two conditions:
17662:
17663:(1) There is an identity element 1 ∈ A0 such that the map R →A0 , r ֏ r · 1 , is an
17664:isomorphism. In this case one says A is connected.
17665:(2) There is a diagonal or coproduct ∆ : A→A ⊗ A , a homomorphism of graded alP
17666:′
17667:′′
17668:gebras satisfying ∆(α) = α ⊗ 1 + 1 ⊗ α + i α′i ⊗ α′′
17669:i where |αi | > 0 and |αi | > 0 ,
17670:for all α with |α| > 0 .
17671:
17672:Here and in what follows we take ⊗ to mean ⊗R . The multiplication in A ⊗ A is given
17673:
17674:by the standard formula (α ⊗ β)(γ ⊗ δ) = (−1)|β||γ| (αγ ⊗ βδ) . For a general Hopf
17675:algebra the multiplication is not assumed to be either associative or commutative (in
17676:the graded sense), though in the example of H ∗ (X; R) for X an H–space the algebra
17677:structure is of course associative and commutative.
```

`refs/hatcher-algebraic-topology/AT.txt:17798-17800`:

```text
17798:Theorem 3C.4. If A is a commutative, associative Hopf algebra over a field F of
17799:characteristic 0 , and An is finite-dimensional over F for each n , then A is isomorphic as an algebra to the tensor product of an exterior algebra on odd-dimensional
17800:generators and a polynomial algebra on even-dimensional generators.
```

### 1.2 Locus disposition

**Correctable source-description defect.** The first passage's clause (1) is
the identity-component condition `A_0 = R*1`; it does not literally state
`Delta(1)=1 tensor 1`. A1 may still prove `Delta(1)=1 tensor 1` directly
because `mu^*` and the cross-product isomorphism are unital ring maps
(`DESIGN-S1-ENDGAME-v2.md:53,141-144`), but the workspace external must not
quote clause (1) as if it said that.

**Correctable source-description defect, not a fatal A1 gap.** Theorem 3C.4
does not itself conclude “an exterior algebra.” It concludes exterior on odd
generators tensor polynomial on even generators. The design does contain the
needed extra argument: total finite dimensionality excludes every nontrivial
polynomial factor (`DESIGN-S1-ENDGAME-v2.md:145-147`). Total finite
dimensionality also has to exclude infinitely many odd generators; that small
obligation should be made explicit in node 7 rather than left to assembly.
`GT-hatcher-hopf-structure-3C4` must be registered with the printed
exterior-tensor-polynomial statement, not an exterior-only strengthening.

The surrounding topological construction assumes path-connectedness and
finitely generated free cohomology in each degree
(`AT.txt:17620-17623`). A1's antecedents suffice: a connected CW complex is
path-connected, and finite total-dimensional real cohomology makes every
graded piece a finitely generated free real vector space. Independently, the
actual Kunneth root permits any CW complexes with those module hypotheses
(`argument/lemmas/lem-topology-kunneth-cross-product.md:4,19-29`). No finite-CW
hypothesis is missing from A1.

## 2. Mandatory-repair dispositions

| repair | disposition | audit |
|---|---|---|
| R-A1 | **REPAIRED, with source-text and budget corrections required** | A1 removes the inapplicable standard-bialgebra dependency (`DESIGN-S1-ENDGAME-v2.md:13-17,53,59-75`), derives the weak coproduct from the actual Kunneth conclusion, and separately removes the polynomial factor (`ibid.:140-147`). The two externals must retain the exact printed statements above. The claimed 8/12 budget is not credible; see finding F8. |
| R-B1 | **NOT-REPAIRED** | B0a visibly binds one row-13 inverse/map package (`ibid.:86,170-177`), but B0b lacks a direct provider for its manifold conclusions, does not re-export B0a's near-adjoint estimate, and pre-uses `[U_0]`; B1 then uses free `r_bidx` (`ibid.:87-88`). |
| R-C1 | **NOT-REPAIRED** | Factoring C0 is mathematically sensible, and its fixed-term estimate is honest, but C1's “apply C0 to that exact package” step is not licensed by C0's algebra-only root contract (`ibid.:100-101,206-223`). |
| R-C3 | **REPAIRED** | C3 now cites line 458 in both its row and provenance ledger (`ibid.:103,333-339`); the local text says exactly that every big-O instance is a concrete function independent of additional data (`approximate_algebras.tex:458`). |
| R-M04 | **REPAIRED** | The hand-off now says only G-S1 is discharged and retains P0 plus M01-M18, including M04, as separate predecessors (`DESIGN-S1-ENDGAME-v2.md:125-130,307-320,424-428`). |
| R-form | **NOT-REPAIRED** | “Bialgebra” is gone and all ten rows are one physical ASCII line, but new untyped/non-explicit descriptions occur in B0b/B1/C0, most plainly the free `r_bidx` (`ibid.:87-88,100`). |

## 3. Full attack fronts

### F1 — fatal — B0b has no root-contract provider for its manifold antecedent

B0b concludes that the same `breve-calU` is a connected compact orientable
smooth manifold without boundary of dimension `N-1`, then uses those facts for
finite triangulation and local index (`DESIGN-S1-ENDGAME-v2.md:87,182-185`).
Its deps are B0a, the polar ledger, quotient-finite-CW, QIFT, and the local-index
row (`ibid.:87`).

None supplies the asserted manifold package:

- B0a's root concludes only a connected H-space, smooth left inversion,
  covariance, and near-adjoint estimate (`ibid.:86`).
- `lem-stage1-quotient-finite-cw` is conditional: it requires
  `breve-calU` already to be a compact smooth boundaryless manifold
  (`argument/lemmas/lem-stage1-quotient-finite-cw.md:4`).
- Its own triangulation dependency has the matching conditional conclusion
  “every compact smooth manifold without boundary is homeomorphic to a finite
  simplicial complex”
  (`argument/lemmas/lem-topology-finite-triangulation.md:4`); it does not
  manufacture B0b's missing manifold hypothesis.
- `lem-topology-local-index-sign` likewise requires a smooth self-map of a
  compact orientable manifold (`argument/lemmas/lem-topology-local-index-sign.md:4,20-22`).
- The only existing root with the missing connected/compact/orientable/smooth/
  boundaryless/dimension conclusion is
  `lem-stage1-quotient-manifold-package`
  (`argument/lemmas/lem-stage1-quotient-manifold-package.md:4`), and it is not
  a B0b dependency.

B0a's internal dependency on that row is not a transitive import: a consumer
may use B0a's root contract, not B0a's explanatory body or dependency closure.
Therefore B0b cannot discharge either the finite-CW antecedent or the
compact/orientable antecedent of the index row. Adding a direct dependency or
changing B0a to export the manifold conjunct changes the mathematical
interface and forces REDESIGN.

### F2 — fatal — the B0a estimate disappears at the B0b-to-B1 boundary

B0a explicitly concludes, for its displayed `sigma`,
`||sigma(U)-U^dagger|| <= C_grp*epsilon_r`
(`DESIGN-S1-ENDGAME-v2.md:86`). B1 needs exactly this fact after obtaining an
actual fixed lift in order to prove
`||U-U^dagger|| <= C_fix*epsilon_r`
(`ibid.:88,201`).

B0b names the B0a witnesses but does not repeat the near-adjoint estimate in
its root conclusion (`ibid.:87`). B1 does not directly depend on B0a
(`ibid.:88`). None of B1's original ten roots exports the estimate for this
displayed map: the actual quotient-left-inversion and quotient-index roots
hide their selected maps
(`argument/lemmas/lem-stage1-quotient-left-inversion.md:4`;
`argument/lemmas/lem-stage1-quotient-inversion-index-data.md:4`), and the
uniform-isolation root gives only isolation for an anaphoric smooth `sigma`
(`argument/lemmas/lem-stage1-uniform-inversion-isolation.md:4`).

The phrase “witnesses supplied by B0a” is not an object-level expansion of
B0a's conclusions. Compare the validated ledger's explicit policy that all
analytic predicates are expanded in the root itself
(`argument/lemmas/lem-stage1-polar-constant-ledger.md:21-31`). B0b must
contractually re-export every B0a field/property B1 consumes, or B1 must
receive a genuinely parameterized package with those clauses.

### F3 — fatal — `r_bidx` is a free witness in B1

B0b existentially introduces `r_bidx` (`DESIGN-S1-ENDGAME-v2.md:87`). B1's
“writing” tuple omits it, but B1 concludes
`||U-J|| >= r_bidx` and `||U+J|| >= r_bidx`
(`ibid.:88`). Thus `r_bidx` is neither:

1. one of B1's own existential universal witnesses;
2. a quantified input; nor
3. a field explicitly destructured from B0b.

This is a literal naked symbol and an untyped witness. The proof skeleton's
reference to “B0b's two isolation clauses” does not bind it
(`ibid.:202`). This alone forces REDESIGN under the typed-witness law.

### F4 — fatal — B0b pre-uses a representative, and the provider relation is not explicit logic

B0b says “every `breve-sigma`-fixed class `[U_0]` has representatives `U_0`
and phases ...” (`DESIGN-S1-ENDGAME-v2.md:87`). `U_0` is used to name the
quantified class before the contract says it exists. The correct binder shape
is “for every fixed class `breve-U`, there exist a representative `U_0` and
phases `c,a` ... with `[U_0]=breve-U`.”

More generally, B0b, B1, and C0 use “the exact displayed witnesses supplied
by [earlier lemma]” (`ibid.:87-88,100`) even though those earlier rows provide
existential, non-unique packages. This is not the row-13 pattern: row 13 first
binds one universal `W`, and (A_5) then binds the genuinely unique inverse of
one displayed `Pi_delta`
(`argument/lemmas/lem-stage1-polar-constant-ledger.md:4`). A repaired chain
must use explicit existential/conditional quantifiers and spell the receiving
package's required conjuncts in the root contract.

### F5 — fatal — C1 cannot pass its selected B1 package into C0

C1's skeleton first applies B1 and retains its package, then says “Apply C0 to
that exact package” (`DESIGN-S1-ENDGAME-v2.md:219-220`). But C0's root
contract quantifies only an exact-unit algebra; it does not accept a B1
package as an input (`ibid.:100`). An independent application of C0 is free
to obtain a different existential B1 package.

There are two honest designs:

1. make C0 explicitly conditional on a fully displayed B1 package and have C1
   pass that package; or
2. let C0 apply B1 exactly once internally, export only the resulting
   projection, and have C1 apply C0 without independently selecting B1.

The current hybrid asserts an application rule its root does not have. The
projection formula itself is not the problem: Kitaev's exact text gives
`P=(2I+U+U^\dag)/4` and the `O(delta+epsilon)` conclusion at
`approximate_algebras.tex:939`, and C0 allocates separate fixed-term and two
nonvanishing-branch nodes (`DESIGN-S1-ENDGAME-v2.md:208-213`).

### F6 — correctable — A1's source language must not strengthen either Hatcher external

The design repeatedly describes the loci as direct “weak conditions” and
“Hopf structure” support (`DESIGN-S1-ENDGAME-v2.md:53,65-71,326-331`).
The registered externals must say exactly:

- connectedness plus the positive-positive coproduct-tail formula, not
  “Delta(1)=...” as Hatcher's first printed clause; and
- exterior tensor polynomial, not exterior-only.

A1's own contract may contain the separately derived `Delta(1)` clause and
the finite-dimensional exterior corollary. This is a registration/prose
correction because nodes 3 and 7 already supply the missing derivations; it
does not by itself change A1's mathematical content.

### F7 — correctable — Block A has two smaller contract/skeleton quantifier omissions

In A1, `sum_j a'_j tensor a''_j` does not explicitly say that a finite family
of positive-degree tails exists (`DESIGN-S1-ENDGAME-v2.md:53`). The finite
homogeneous decomposition makes the intended statement true, but the binding
contract rule asks for explicit quantifiers. Also the ASCII `R` used for
coefficients in A1-A3 should be stated once as the real field (or written
`reals`) rather than left to typography (`ibid.:53-55`).

These are mechanical contract clarifications if made without changing the
real-coefficient content.

### F8 — fatal under the factoring rule — A1 and B0b budgets are not plausible

The advertised targets/hard caps are A1 `8/12` and B0b `9/14`
(`DESIGN-S1-ENDGAME-v2.md:53,87,378-394`).

- The already validated Hopf-structure row took 13 nodes even though it
  started from the stronger standard-bialgebra antecedent
  (`argument/lemmas/lem-topology-hopf-structure.md:14-17`). A1 additionally
  constructs `Delta`, proves multiplicativity, proves two edge identities and
  the positive-positive tail, applies 3C.4, excludes polynomial generators,
  and proves finiteness of the odd generator set. Eight routine-tier nodes
  with hard cap 12 is not credible.
- The validated quotient-index row took 12 nodes
  (`argument/lemmas/lem-stage1-quotient-inversion-index-data.md:14-25`), while
  the validated actual-isolation row took 7
  (`argument/lemmas/lem-stage1-uniform-inversion-isolation.md:44-51`).
  B0b reconstructs both same-map branches, adds manifold/finite-polyhedron
  attachment, and performs the global phase lift in 9 target nodes. Reusing
  B0a avoids some setup, but it does not collapse these verifier-visible
  obligations to nine.

B0a's 8/12, B1's 10/15, C0's 8/12, C1's 7/12, C2's 6/10, and C3's 9/14 are
plausible only after the interface defects are repaired. A2/A3 are also
plausible. A1 and B0b should be factored or given an honestly justified
routine-tier plan; merely raising a hard cap while retaining concealed
multi-obligation nodes would violate the original `~12` factoring rule.

### F9 — note — Kitaev source-fidelity pass

The local Kitaev file exists and its SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`
matches `refs/manifest/checksums.sha256:4`. Every v2-cited Kitaev range was
checked in `\n`-counted source space:

- `:895-912` contains the H-space/unit, inversion, and left-inversion
  definitions. Line 912 says exactly that associativity is unnecessary and
  only the first inversion homotopy is used.
- `:917-945`, including v2's narrower `:929-943`, contains the
  delta-projection alternatives, nontriviality, Lemma
  `lem_nontriv_projection`, and the projection bridge. The explicit bridge
  formula is at line 939, not inside the brief's shorthand `:929-935`.
- `:939-955`, `:945-969`, and `:947-968` contain the quotient phase lift,
  quotient-property list, and Lefschetz contradiction.
- `:971-1050`, including `:975-1016`, `:1016-1049`, and `:1023-1050`,
  contains `prop_H-group`, the Kunneth/coprod construction, the explicit
  warning at line 1007 that the coproduct need not be coassociative, the
  exterior-algebra reduction, and the associated-graded trace proof.
- `:1192-1222` contains the smallness convention, full
  `prop_delta_hominc`, and proof. The exact proposition text at
  `:1194-1196` gives `||v||<=1+O(delta+epsilon)` and the lower upgrade when
  a supplied modulus is `>2*delta`.
- `:1419-1424` contains `P''=tilde-P_m-P'`, exact complementarity, and the
  two basis images.

The decisive universality sentence is byte-verbatim at line 458:

> Here and in general, each instance of big-\(O\) or similar notation stands
> for a concrete function, not depending on any additional data.

Thus R-C3's source repair is genuine. Source fidelity does not cure the
typed-provider failures.

### F10 — note — M19-S1 consumer shape matches, conditionally

The current MAIN design is
`docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`.
Its exact M19-S1 contract is at line 381 and M15 at line 343.
Clause-by-clause:

1. Future M04 supplies the selected `S_{P_j}` as an extended
   `L*epsilon`-C*-algebra with its compressed unit
   (`DESIGN-MAIN-STRUCTURE-v5.md:287,381`). G-S1 correctly does not claim to
   supply this.
2. `dim S_{P_j}>1` instantiates the strict dimension hypothesis of C1-C3
   (`DESIGN-S1-ENDGAME-v2.md:101-103,307-310`).
3. C3 returns the same pair and its one level-one `C^2` map, exact unit
   clause, basis images, and canonical amplification family
   (`ibid.:103,310-311`).
4. C2/C3's internal `P',P''` remain distinct from the outer old/fresh targets
   (`ibid.:312`).
5. `lem-compcb-single-compression-transfer` supplies the old side when
   `m>1`; its actual root is an extended-inclusion transfer
   (`argument/lemmas/lem-compcb-single-compression-transfer.md:4`).
6. A finite universal maximum/minimum can price `L*C_proj`, `L*C_np`,
   `L*C_pair`, old-side constants, and thresholds (`DESIGN-S1-ENDGAME-v2.md:314-316`).

Therefore the producer *shapes* match M19-S1/M15 once their own contracts are
sound and validated. The design correctly states that G-S1 alone does not
make MAIN eligible (`ibid.:125-130,318-320`).

### F11 — fatal antecedent despite otherwise clean dependency/status graph

Every existing direct dependency named in the ten row tables exists and has
`status: proved` / `af: validated`; every proposed dependency is earlier in
the stated serial order. No retired parent, parked row, or
`stated/seeded` row is imported. A1 does not import
`lem-topology-hopf-structure` (`DESIGN-S1-ENDGAME-v2.md:53,59-75`).

The per-row root-contract consumption check is:

- **A1:** the Kunneth root's CW plus finitely-generated-free antecedents follow
  from A1's CW and finite-dimensional-real-cohomology hypotheses. **A2/A3**
  consume only the exact earlier proposed conclusions.
- **B0a:** row 13 supplies the displayed graph data, unique polar inverse,
  operations, paths, derivative range, and arithmetic in (A_2),(A_4)-(A_7),(R)
  (`argument/lemmas/lem-stage1-polar-constant-ledger.md:4`). The smooth-atlas,
  smooth-polar-inverse, and explicit-smooth-operations roots are conditional
  on exactly those displayed objects
  (`argument/lemmas/lem-stage1-smooth-unitary-atlas.md:4`;
  `argument/lemmas/lem-stage1-smooth-polar-inverse.md:4`;
  `argument/lemmas/lem-stage1-explicit-smooth-unitary-operations.md:4`). The quotient-manifold
  theorem's smooth/free/proper antecedents can be proved for that same scalar
  action before applying its root
  (`argument/lemmas/lem-topology-quotient-manifold.md:4`). No strengthening was found in B0a.
- **B0b:** QIFT's derivative-closeness hypotheses match the planned received
  A7 charts (`argument/lemmas/lem-stage1-quantitative-inverse-function.md:4`), but the
  finite-CW and local-index roots are unavailable until F1's missing manifold
  antecedent is supplied.
- **B1:** assuming a corrected complete B0b package, the trace, Lefschetz,
  maximal-simplex, and top-cohomology roots have the needed exact shapes
  (`argument/lemmas/lem-topology-lefschetz-hopf.md:4`;
  `argument/lemmas/lem-finite-polyhedron-maximal-simplex-placement.md:4`;
  `argument/lemmas/lem-topology-orientable-top-cohomology.md:4`). The singleton-only-fixed-set
  contradiction supplies finiteness and pointwise maximal-simplex placement.
  The original quotient/isolation roots remain valid obligation checks but do
  not identify the displayed package; F2 remains.
- **C0-C3:** after a typed B1/C0 repair, C0 consumes B1's fixed lift and
  distances; C1 consumes row-13 (A_1)'s same-space product/unit
  rectification (an extended algebra is in particular a level-one
  epsilon-C*-algebra); C2 consumes only C1; and C3 consumes only the pair
  returned together by C2. No conclusion strengthening was found in C2/C3.

The proposed graph is acyclic:

`A1 -> A2 -> A3`, `B0a -> B0b -> B1 -> C0 -> C1 -> C2 -> C3`,
with `A3 -> B1`.

The serial list at `DESIGN-S1-ENDGAME-v2.md:105-123` is therefore a
topological order. Status and acyclicity do not repair F1: B0b's *listed*
deps simply omit a required root conclusion.

### F12 — note — no independent dimension leak found

No coefficient in the intended mathematics must depend on `N`, cohomology
dimension, the number of exterior generators, triangulation size,
amplification level, or block count:

- A1-A3 are qualitative finite-dimensional algebra.
- B0b uses determinant sign through an invertible homotopy, not a determinant
  magnitude.
- B1 needs only two nonzero cohomological degrees.
- C0-C2 are fixed-term expansions.
- C3's four basis products are tensor-level terms, and line 458 makes the
  proposition's big-O functions data-independent.

The dimension audit at `DESIGN-S1-ENDGAME-v2.md:268-285` is sound, conditional
on supplying the missing interfaces.

### F13 — note — zero new definition shards remains achievable

All ten listed definition ids exist and are locked
(`definitions/INDEX.md`; detailed uses at
`DESIGN-S1-ENDGAME-v2.md:246-266`). The weak coproduct, augmentation
filtration, and displayed maps are theorem-local data, so they need not become
new canonical terms.

However, “the package supplied by lemma X” cannot function as an undefined
package predicate. The repair should spell its fields and clauses directly
with explicit quantifiers; it need not add a new definition shard. Thus the
zero-new-def objective is still achievable, but the present contracts do not
achieve typed self-containment.

### F14 — contract-form summary

All ten contract cells are one physical line and contain ASCII only
(`DESIGN-S1-ENDGAME-v2.md:53-55,86-88,100-103`). No contract assigns a
numerical value to a universal constant, and the ambiguous word “bialgebra”
is gone.

Contract form nevertheless fails for the semantic reasons in F2-F5:
non-unique existential packages are referred to by definite description,
`[U_0]` precedes its representative binder, `r_bidx` is free, and C0 has no
package parameter despite C1 treating it as if it did.

## 4. Required redesign surface

1. Give B0b a direct root-contract provider for the compact orientable smooth
   quotient (most directly `lem-stage1-quotient-manifold-package`), or enlarge
   B0a's contract to export those exact conjuncts. Then re-check the
   finite-CW and local-index antecedents.
2. Replace every “the exact witnesses supplied by ...” anaphor with explicit
   quantification over one displayed package and the exact conjuncts that
   package satisfies. B0b must re-export B0a's near-adjoint estimate if B1 is
   to consume it through B0b.
3. In B0b quantify a fixed class `breve-U` first and then existentially bind
   `U_0,c,a`. In B1 explicitly bind the same `r_bidx` supplied by B0b.
4. Choose one C0/C1 architecture: either C0 is a parameterized bridge on a
   displayed B1 package, or C0 selects B1 once internally and C1 consumes only
   C0's projection. Do not select B1 independently on both sides.
5. Register the two Hatcher externals with the exact extracted statements;
   keep `Delta(1)` and the finite-total-dimensional exterior-only corollary as
   explicit A1 derivations. Add the finite-odd-generator argument.
6. Re-factor or honestly redesign the A1 and B0b proof granularity. Their
   present 8/12 and 9/14 budgets conceal more work than comparable validated
   trees.
7. Preserve the successful repairs: line-458 provenance, the conditional
   M19-S1 clause match, zero new definitions if possible, T0-only imports,
   dimension-free constants, and the G-S1-only hand-off.
