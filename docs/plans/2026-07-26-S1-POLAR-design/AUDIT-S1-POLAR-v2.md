# AUDIT — fresh hostile re-audit of `DESIGN-S1-POLAR-v2.md`

Date: 2026-07-27  
Role: fresh independent hostile auditor; not an author of either design or the
first audit  
Status: **AUDIT ONLY; NON-RIGOROUS; no status promotion**

## 0. Final disposition

**REDESIGN.**

The load-bearing mathematical repair is sound: the rectified multiplication is
bilinear, the involution is real-linear, the graph equation is a polynomial map
of finite-dimensional real vector spaces, Lee C.40 applies pointwise, and the
unchanged polar map becomes smooth before Lee C.34 is applied chartwise. Thus
there is **NO ROUTE-ALARM** and no dimension-dependent analytic constant was
found (`DESIGN-S1-POLAR-v2.md:50-70,106,189-206`;
`approximate_algebras.tex:420-429,692-807,809-855`;
`lee-smooth-manifolds-2ed.txt:31134-31137,31286-31298,31330-31344`).

The proposed nine-row DAG is nevertheless not landable. I found four defects.

1. **The ledger still does not thread compatible witnesses at contract level.**
   The row says that a tuple is “simultaneously selectable,” but its formal
   conclusion only gives scalar fields, formulas, and inequalities. It does not
   say that the fields are the witnesses for any of rows 1--8. The proposed
   definition is deliberately data-only and also contains no such validity
   assertion. Therefore a consumer sees
   \(\exists W\,\mathrm{Arithmetic}(W)\) and separate existential analytic
   theorems, not one \(W\) satisfying both. Proof-body provenance cannot enrich
   a registry contract (`DESIGN-S1-POLAR-v2.md:87-93,107,141-154,208-217,
   226,242,249,268`; first audit `AUDIT-S1-POLAR.md:31-40,260-271,293-294`).
2. **Rows 2 and 8 remain compound.** Row 2 joins graph
   existence/quantitative estimates/normal-derivative invertibility with a
   global Maurer--Cartan tangent trivialization. Row 8 joins smooth graph
   regularity, a smooth embedded atlas, a smooth polar inverse, a smooth scalar
   action, and smooth multiplication and inversion. A projected node count and
   a promise to split only after measurement do not satisfy the binding
   “no compound contracts” rule (`DESIGN-S1-POLAR-v2.md:100,106,118,124,250`;
   `BRIEF-S1-POLAR.md:46-50,72-74`;
   `DESIGN-FUDW-DECOMP-v4.1.md:586,607`; first audit
   `AUDIT-S1-POLAR.md:174-182,295-298`).
3. **The quotient-isolation proof has an omitted phase-lift obligation.**
   Isolation of the actual fixed points \(J,-J\) does not by itself state that
   \([J]\) is isolated for the quotient map. If \([U]\) is fixed, one must use
   \(\sigma(cU)=\bar c\,\sigma(U)\), choose a square root of the quotient phase,
   and prove that a class sufficiently close to \([J]\) yields an actual fixed
   lift in the \(J\)- or \(-J\)-isolation ball. The dependencies can support
   this derivation, but neither §5 nor the §6 obligation ledger states it
   (`DESIGN-S1-POLAR-v2.md:102,134,137-138,166-187,251,267`;
   `approximate_algebras.tex:943-951`).
4. **One provenance claim is false as written.** The three approximate-group
   defects are literal at TeX 872--874, but the two closeness estimates
   \(\|\mu(U,V)-U\boldsymbol\cdot V\|\) and
   \(\|\sigma(U)-U^\dagger\|\) are derived from the polar estimate at TeX
   845--868; they are not literal in TeX 857--893. The contract is still
   derivable, but its provenance and §9 disposition must say so
   (`DESIGN-S1-POLAR-v2.md:103,121,236`;
   `approximate_algebras.tex:845-868,870-878`).

Required redesign:

- split row 2 into graph control and Maurer--Cartan/tangent control;
- split row 8 at least into smooth-atlas, smooth-polar-inverse, and
  smooth-action/operations producers;
- split witness unification from pure scalar arithmetic, or make the arithmetic
  row universal over an already selected analytic tuple and have every consumer
  select and identify that tuple explicitly;
- add the quotient fixed-class phase-lift step to the index-data row and the
  fixed-class obligation ledger;
- correct the group-law provenance and state explicitly whether row 1
  reconstructs TeX 672--687 or uses only the weaker landed rectification
  contract.

## 1. Local-source and hash audit

The four payload hashes in v2 §1 match the local manifest:
`refs/manifest/checksums.sha256:4,13,19,23`. The Kitaev source also matches the
locked definition prefix (`definitions/def-epsilon-cstar-algebra.md:9-10`).

| locus checked | hostile result | verdict |
|---|---|---|
| TeX 407--440 | The definition includes bilinear multiplication, product norm, associator, conjugate-linear isometric involution, exact involution/product compatibility, the lower \(C^*\)-bound, exact two-sided unit equations, \(\|J\|=1\), and \(J^\dagger=J\). Row 1 must establish all of these for the rectified product. | **VALID** (`approximate_algebras.tex:407-440`) |
| TeX 458 | Each big-\(O\) instance is a concrete function independent of additional data. This permits named universal witnesses after fixed finite maxima/minima; it does not print numerical coefficients. | **VALID** (`approximate_algebras.tex:458`) |
| TeX 560 | Multiple-variable derivatives use an arbitrary direct-sum norm between max and sum. A two-summand vector comparison costs at most \(2\); comparing induced operator norms on both source and target can cost a second fixed factor. | **VALID-WITH-THE-v2-CLARIFICATION** (`approximate_algebras.tex:554-560`; `DESIGN-S1-POLAR-v2.md:194`) |
| TeX 655--687 | The multiplier estimates and Neumann interfaces are dimension-free. Proposition `prop_unit` supplies an \(O(\varepsilon)\)-Banach product with algebraic exact unit and exact involution compatibility, but does not print every new \(C^*\)-axiom or \(\|J\|=1\). The v2 scalar rescaling is algebraically correct, but every axiom still has to be expanded. | **VALID-WITH-DERIVATION** (`approximate_algebras.tex:655-687`; `DESIGN-S1-POLAR-v2.md:99,117`) |
| TeX 692--725 | The definition of \(\mathcal U\), \(\overline{\mathcal U}_\delta\), and \(\mathcal U_\delta\) includes the right-inverse condition. `lem_U_delta` proves \(L_X\) invertible only after using that condition and explicit smallness. | **VALID** (`approximate_algebras.tex:692-725`) |
| TeX 728--807 | The graph equation, uniqueness, \(C^1\) estimates, and Maurer--Cartan formula are present. The text proves only \(C^1\). It does not itself justify keeping graph control and global tangent trivialization in one atomic row. | **VALID-WITH-CORRECTIONS** (`approximate_algebras.tex:728-807`) |
| TeX 809--855 | The polar proposition and inner/outer losses are present. The inverse is directly secured on the shrunken inner domain, while line 845 writes the larger source symbol; v2 correctly uses the smaller domain. The line-849 \(v/u\) typo remains harmless. | **VALID-WITH-DERIVATION** (`approximate_algebras.tex:809-855`) |
| TeX 857--893 | The global domains and the three group defects are present. The two closeness bounds in row 5 require TeX 845--868 and the polar row; they are not two additional literal inequalities in this locus. The repeated denominator at 883--888 remains a genuine printed erratum and is not consumed. | **VALID-WITH-CORRECTED-PROVENANCE** (`approximate_algebras.tex:845-893`) |
| TeX 895--912 | The source asserts projected straight paths but omits the right-inverse and polar-domain argument. The exact quadratic identity and Neumann comparison in v2 are the needed derivation. The printed H-space type typo is still present at line 895. | **VALID-WITH-DERIVATION** (`approximate_algebras.tex:895-912`) |
| TeX 943--955 | The source asserts actual isolation, quotient topology, orientation, finite-CW type, and left inversion. It does not prove smoothness or the quotient fixed-class phase-lift. It is not sufficient provenance by itself. | **REFUTED AS SUFFICIENT PROVENANCE** (`approximate_algebras.tex:943-955`) |
| Lee C.34 | A smooth map between open subsets of equal-dimensional Euclidean spaces with invertible derivative at a point is locally a diffeomorphism. Corollary C.36 explicitly gives the injective-everywhere version used after chart reduction. | **VALID** (`lee-smooth-manifolds-2ed.txt:31134-31137,31286-31298`) |
| Lee C.40 | A smooth \(\Phi(x,y)\) with nonsingular \(y\)-derivative has a local smooth solution graph. It is local, so global smoothness of \(g_V\) must be obtained by equality with the already unique graph on overlaps. | **VALID** (`lee-smooth-manifolds-2ed.txt:31330-31344,31374-31385`) |
| Munkres Cor. 4.9 / Thm 5.11 | The compatible \(C^\infty\)-structure statements exist for the boundaryless and boundary cases. They do not make the selected maps equivariant or preserve fixed points. | **VALID AS FALLBACK ONLY** (`munkres-elementary-differential-topology.txt:2055-2056,2533-2558`) |
| Munkres Thm 4.2 | The \(C^r\)-to-\(C^p\) approximation and \(C^r\) differentiable homotopy are present. The relative form is Exercise 4.2(a), not a theorem. | **VALID-WITH-SCOPE CALLOUT** (`munkres-elementary-differential-topology.txt:1833-1840,1888-1901`) |
| Munkres Thm 3.10 | Fine-\(C^1\) neighborhoods preserve immersions and embeddings; the diffeomorphism conclusion has the displayed boundary-preservation hypothesis. | **VALID** (`munkres-elementary-differential-topology.txt:1509-1514,1596-1637`) |

The landed dependencies provide exactly the following interfaces:

- quantitative injectivity, two-sided Lipschitz control, and image containment,
  but no smooth IFT
  (`argument/lemmas/lem-stage1-quantitative-inverse-function.md:4`);
- an exact unit and a close product on the same involutive normed space, but no
  advertised full rectified \(C^*\)-axiom package
  (`argument/lemmas/lem-stage1-exact-unit-rectification.md:4`);
- a quotient theorem only for a smooth, free, proper action on a smooth
  manifold (`argument/lemmas/lem-topology-quotient-manifold.md:4`).

Accordingly, row 1 must reconstruct the stronger rectified package inside its
own proof. It may not silently import the stronger internal construction from
the landed rectification proof export through a weaker registry contract.

### 1.1 Deliverable-scope check

V2 did not silently narrow the original design brief. It still proposes a
formula-level polar retraction, approximate group laws, first-derivative
control, explicit local guards, dimension-freeness, an unblocking map, and
datum-only definitions (`BRIEF-S1-POLAR.md:30-64`;
`DESIGN-S1-POLAR-v2.md:95-111,127-217`). It also expands the consumer audit from
the three originally blocked interfaces to the complete
`lem-stage1-extra-fixed-class` chain (`DESIGN-FUDW-DECOMP-v4.1.md:200-208`;
`DESIGN-S1-POLAR-v2.md:170-187`). The failure below is therefore not
deliverable narrowing; it is atomicity and contract-level witness linkage.

## 2. Hard attack on the direct-smoothness repair

### 2.1 Graph equation

For fixed \(V\), the map
\[
f_V(A)=\frac12\left(
 ((J+A^\dagger)\boldsymbol\cdot V^\dagger)
 \boldsymbol\cdot(V\boldsymbol\cdot(J+A))-J\right)
\]
is a degree-two polynomial between finite-dimensional **real** vector spaces:
the rectified product is bilinear and the conjugate-linear involution is
real-linear. Exact involution/product compatibility also makes its value
Hermitian. Nonassociativity does not alter polynomiality because the
parenthesization is fixed (`DESIGN-S1-POLAR-v2.md:50-60,99-100`;
`approximate_algebras.tex:420-429,742-756`).

At every point
\((A^\parallel,g_V(A^\parallel))\), row 2 states
\[
\left\|D_{A^\perp}f_V-I_{\mathcal H}\right\|<1,
\]
so the partial derivative is invertible by Neumann. Lee C.40 therefore gives a
local smooth solution graph. The already-stated uniqueness identifies each
local solution with the same \(g_V\), so the local smooth graphs glue. This
part of the repair is **VALID** (`DESIGN-S1-POLAR-v2.md:100,106,124`;
`lee-smooth-manifolds-2ed.txt:31330-31344`).

### 2.2 Polar inverse

Once the graph atlas is smooth, the polar map is the restriction of a bilinear
ambient map and is smooth. Row 3 states that it is a bijective \(C^1\)
diffeomorphism onto an open set; hence its derivative is invertible at every
point. Applying Lee C.34 in local charts and using global injectivity makes the
set-theoretically same inverse smooth. Lee C.36 states exactly the
injective-local-diffeomorphism gluing principle in Euclidean coordinates
(`DESIGN-S1-POLAR-v2.md:101,106`; `approximate_algebras.tex:809-843`;
`lee-smooth-manifolds-2ed.txt:31134-31137,31286-31298`).

Thus bijectivity and derivative invertibility are supplied before the smooth
inverse theorem is consumed. No guessed radius is introduced. This part is
**VALID**.

### 2.3 Maps, action, and first derivatives

- The scalar action is the restriction/corestriction of the smooth ambient map
  \((c,U)\mapsto cU\), and it preserves \(\mathcal U\) by bilinearity and the
  right-inverse condition.
- \(U\boldsymbol\cdot V\) and \(U^\dagger\) are in the polar domain by row 5,
  so composition with the smooth \(u_\delta\) makes the same \(\mu,\sigma\)
  smooth as maps **into the embedded manifold** \(\mathcal U\).
- The graph functions, polar inverse, points, and coordinate maps are unchanged;
  the smooth atlas is the same atlas upgraded from \(C^1\). Hence their existing
  first derivatives are unchanged.

These conclusions are mathematically valid
(`DESIGN-S1-POLAR-v2.md:61-70,103,106`; `approximate_algebras.tex:857-868`).
The defect is architectural: they are several consumer interfaces combined
with graph and polar smoothness in one row. Therefore the direct route is
**VALID**, while proposed row 8 is **REFUTED AS AN ATOMIC CONTRACT**.

## 3. Constant-ledger recomputation

Put
\[
d=\delta_*,\qquad e=\varepsilon_r,\qquad q=C_{\rm grp}e.
\]
The minima in row 9 give
\[
\begin{gathered}
d\le\tfrac14,\quad e\le\tfrac14,\quad
C_{\rm ch}d,C_{\rm ch}e\le\kappa_{\rm ch}/4,\quad
C_{\rm pol}d,C_{\rm pol}e\le\kappa_{\rm pol}/4,\\
C_{\rm der}e\le\kappa_{\rm der}/8,\quad
q\le1,\quad q\le d/(12C_{\rm path}),\\
r_{\rm iso}\le d/4,\quad
C_{\rm der}r_{\rm iso}\le\kappa_{\rm der}/8 .
\end{gathered}
\]
These are literal consequences of `DESIGN-S1-POLAR-v2.md:107`.

Therefore:

1. \(C_{\rm ch}(e+d)\le\kappa_{\rm ch}/2\le\kappa_{\rm ch}\) and
   \(C_{\rm pol}(e+d)\le\kappa_{\rm pol}/2\le\kappa_{\rm pol}\).
2. Since \(\kappa_{\rm pol}\le1/2\),
   \[
   r_-=d(1-C_{\rm pol}(e+d))\ge 3d/4.
   \]
3. \(q\le d/(12C_{\rm path})\le d/12<3d/4\le r_-\).
4. \(C_{\rm path}q\le d/12\le1/48<1/4\).
5. Since \(e\le1/4\) and \(q\le1\),
   \[
   \eta=C_{\rm path}q(1+e+q)
   \le3C_{\rm path}q\le d/4<r_-.
   \]
6. \(C_{\rm der}(e+r_{\rm iso})\le\kappa_{\rm der}/4<1\), and in
   particular it is at most \(\kappa_{\rm der}\).
7. For the chart-retention guard,
   \[
   \begin{aligned}
   &(1+e)(1+C_{\rm ch}(e+d))r_{\rm iso}+q\\
   &\qquad\le
   \frac54\frac54\frac d4+\frac d{12}
   =\frac{91}{192}d<2d.
   \end{aligned}
   \]
8. \(0<r_{\rm iso}\le d\), \(q\le1\), and all remaining row-6/row-7
   numerical premises follow.

The displayed arithmetic, including all eight guards, is **VALID** and
dimension-free. The flaw is solely logical: row 9 does not state that this
tuple witnesses the analytic producer contracts. The exact correction is to
separate:

- a closed witness-unification result that explicitly identifies the common
  monotone maxima/minima with the witnesses of the analytic rows; and
- a universal scalar lemma saying that **every already selected** tuple with
  \(C_\bullet\ge1\), \(0<\kappa_\bullet\le1/2\), and
  \(0<e_{\rm rect}\le1/C_{\rm rect}\) satisfies the displayed implications.

Alternatively, each consumer must select the analytic witnesses and repeat the
universal scalar lemma locally. A data-only definition cannot establish the
identification (`DESIGN-S1-POLAR-v2.md:87-93,107,125,208-217`).

## 4. Verdict per proposed analytic row

| proposed row | verdict | hostile finding / exact correction |
|---|---|---|
| `lem-stage1-rectified-cstar-control` | **VALID-WITH-CORRECTIONS** | The scalar normalization is correct and can preserve every axiom by fixed-term estimates. The proof must reconstruct TeX 672--687 (including exact dagger compatibility) inside this row, or add an adequate producer; the landed contract exports only exact unit plus product/unit closeness. Do not consume hidden proof-export content. (`DESIGN-S1-POLAR-v2.md:99,117`; TeX 407--440,672--687; `argument/lemmas/lem-stage1-exact-unit-rectification.md:4`.) |
| `lem-stage1-unitary-chart-control` | **REFUTED AS AN ATOMIC ROW** | Its graph/estimate/normal-derivative interface and its global tangent/Maurer--Cartan interface are distinct. Split them regardless of the projected count. The mathematical conclusions remain plausible. (`DESIGN-S1-POLAR-v2.md:100,118`; TeX 758--807; `DESIGN-FUDW-DECOMP-v4.1.md:586`.) |
| `lem-stage1-polar-retraction` | **VALID** | The two radii are literal, the regularity is explicitly \(C^1\), and only the supported shrunken inner domain is used. (`DESIGN-S1-POLAR-v2.md:101,119`; TeX 809--855.) |
| `lem-stage1-polar-coherence-naturality` | **VALID** | Complete polar data are universally quantified. Uniqueness and bilinearity give coherence and scalar naturality without a free witness. (`DESIGN-S1-POLAR-v2.md:102,120`; TeX 809--845.) |
| `lem-stage1-approximate-group-laws` | **VALID-WITH-CORRECTED-PROVENANCE** | The contract is closed and the group-domain guard is explicit. Cite TeX 845--868/polar retraction for the two closeness estimates and TeX 872--874 for the three literal group defects. (`DESIGN-S1-POLAR-v2.md:103,121,236`.) |
| `lem-stage1-polar-path-admissibility` | **VALID** | The exact quadratic identity uses only bilinearity; \(L_{Z_t}=L_{U_0}+tL_{U_1-U_0}\), the explicit Neumann guard, and row-4 naturality close right-invertibility, the polar domain, joint continuity, and equivariance. (`DESIGN-S1-POLAR-v2.md:104,122`; TeX 655--661,699--725,895--912.) |
| `lem-stage1-inversion-derivative-control` | **VALID** | The group dependency is present, \(F_s\) is typed, and the displayed guard retains the target in the same chart. The ledger arithmetic verifies its premises once witnesses are genuinely threaded. (`DESIGN-S1-POLAR-v2.md:105,123`; TeX 728--762,857--892.) |
| `lem-stage1-smooth-unitary-polar-package` | **REFUTED AS AN ATOMIC ROW; DIRECT ROUTE VALID** | Lee C.40/C.34 support the unchanged-map upgrade, but smooth atlas, smooth polar inverse, smooth scalar action, and smooth \(\mu,\sigma\) must be factored into separate consumer interfaces. (`DESIGN-S1-POLAR-v2.md:106,124`; Lee txt 31134--31298,31330--31385.) |
| `lem-stage1-polar-constant-ledger` | **REFUTED AS A COMPOSITIONAL CONTRACT; ARITHMETIC VALID** | “Simultaneously selectable” is not a stated relation between this tuple and rows 1--8. Split witness unification from a universal scalar ledger, or make consumers select and identify the tuple. (`DESIGN-S1-POLAR-v2.md:107,125`; `AUDIT-S1-POLAR.md:260-271`.) |

The dependency directions are otherwise acyclic:
rectification/chart \(\to\) polar \(\to\) coherence \(\to\) group/path/derivative
\(\to\) smooth upgrades \(\to\) scalar ledger. Row 8 does not need row 9, so no
cycle was found (`DESIGN-S1-POLAR-v2.md:99-111`). The projected node counts are
only projections; the mandatory splits above must be made before measurement,
not conditional on a future \(>12\) result.

## 5. Verdict per downstream repair

| downstream repair | verdict | hostile finding / exact correction |
|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | **VALID-WITH-CORRECTIONS** | The quantitative IFT applies to \(F_s-\mathrm{id}\), whose derivative is close to \(-2I\), and chart retention makes equality of coordinates legitimate. Replace dependencies by the factored smooth rows and a genuinely compatible range producer. (`DESIGN-S1-POLAR-v2.md:134,174`; `AUDIT-S1-POLAR.md:304-312`.) |
| `lem-stage1-quotient-manifold-package` | **VALID-WITH-CORRECTIONS** | The finite-dimensional closedness argument is sound; the two Maurer--Cartan identities give a quotient tangent trivialization. It must depend on the factored smooth-atlas/action and Maurer--Cartan rows, not the compound row 8 or an unthreaded ledger. (`DESIGN-S1-POLAR-v2.md:135,156-164`; `argument/lemmas/lem-topology-quotient-manifold.md:4`.) |
| `lem-stage1-quotient-finite-cw` | **VALID** | Its hypothesis now exactly supplies a compact smooth boundaryless manifold to the landed triangulation contract. Compactness turns the locally finite triangulation into a finite complex in the landed row's proof plan. Status remains non-rigorous because the dependency is only `stated/seeded`. (`DESIGN-S1-POLAR-v2.md:136,176`; `argument/lemmas/lem-topology-finite-triangulation.md:4,7-9,20-29`; Munkres txt 4356--4365.) |
| `lem-stage1-quotient-left-inversion` | **VALID-WITH-CORRECTIONS** | Scalar naturality gives \(\mu(cU,dV)=cd\,\mu(U,V)\) and \(\sigma(cU)=\bar c\,\sigma(U)\); joint projected paths give the left-inversion homotopy. Use factored smooth-operation dependencies and the corrected witness interface. (`DESIGN-S1-POLAR-v2.md:137,177`; TeX 895--912.) |
| `lem-stage1-quotient-inversion-index-data` | **VALID-WITH-CORRECTIONS** | Derivative descent, vertical invariance, quotient-norm control, and determinant sign are sound. Add the omitted phase-lift: a nearby quotient fixed class must be converted, using a square root of its phase and scalar naturality, to an actual fixed lift in a \(J\)- or \(-J\)-isolation ball. (`DESIGN-S1-POLAR-v2.md:138,166-168,174,180`; TeX 943--951; `argument/lemmas/lem-topology-local-index-sign.md:4`.) |
| `lem-finite-polyhedron-maximal-simplex-placement` | **VALID** | In a finite simplicial complex, a simplex containing a given point extends in the finite face poset to an inclusion-maximal simplex. This discharges the exact narrowed Lefschetz-Hopf hypothesis. (`DESIGN-S1-POLAR-v2.md:139,179`; `argument/lemmas/lem-topology-lefschetz-hopf.md:4,25-33`.) |

All six ids are absent from `argument/lemmas/`; the repairs therefore change no
af-VALIDATED contract. They consume validated topology contracts without
modifying them. No re-validation obligation is triggered by the six proposed
interfaces themselves.

## 6. `lem-stage1-extra-fixed-class` obligation ledger

| obligation | re-audit |
|---|---|
| Actual inversion isolation near \(J,-J\) | **VALID-WITH-CORRECTIONS:** analytic isolation is supplied, but quotient isolation additionally needs the phase-lift described in §5. |
| Connected compact orientable positive-dimensional smooth quotient | **VALID-WITH-CORRECTIONS:** supplied after the smooth and Maurer--Cartan rows are factored and the common range is genuinely threaded. |
| Finite polyhedron / finite CW | **VALID:** corrected smooth hypothesis matches the landed triangulation contract (`lem-topology-finite-triangulation.md:4,22-29`). |
| Continuous H-space and left inversion; smooth \(\breve\sigma\) | **VALID-WITH-CORRECTIONS:** the direct smoothness route and joint paths supply this after factoring. |
| Left-inversion trace | **VALID:** no new polar shortfall was found once finite-CW H-space data exist (`DESIGN-S1-POLAR-v2.md:178,182`). |
| Lefschetz-Hopf maximal-simplex placement | **VALID:** the new finite-poset row supplies the exact landed hypothesis (`lem-topology-lefschetz-hopf.md:4,25-33`). |
| Local index \(+1\) | **VALID-WITH-CORRECTIONS:** smoothness, quotient derivative, and determinant sign are supplied, subject to the phase-lift proving that \([J]\) is isolated. |
| Nonzero top cohomology and \(\Lambda(\breve\sigma)\ge2\) | **VALID:** connectedness gives \(H^0\ne0\), positive-dimensional orientable closedness gives top cohomology nonzero, and the trace formula makes \(\Lambda\) the total Betti number (`argument/lemmas/lem-topology-orientable-top-cohomology.md:4,19-29`; `DESIGN-S1-POLAR-v2.md:181-182`). |

The corrected dependency list proposed at v2 lines 184--187 must therefore add
not only the quotient-index and maximal-simplex rows, but also record the
phase-lift inside the quotient-index proof. With that correction, no further
fixed-class consumer shortfall was found.

## 7. Definition hygiene

### `def-approximate-unitary-space`

**VALID.**

The proposed content is notation/data only. The right-inverse clauses belong to
the definitions of the approximate-unitary sets; conditioning \(\phi_V\) on
invertibility of \(L_V\) avoids asserting a chart; and \(u,h,\mu,\sigma\) remain
partial notation whose domains come from results. No estimate, existence,
regularity, compactness, orientation, or isolation statement is smuggled into
the definition (`DESIGN-S1-POLAR-v2.md:212,215-217`;
`approximate_algebras.tex:692-750,845-859`; first audit
`AUDIT-S1-POLAR.md:384-411`).

### `def-stage1-polar-witness-data`

**VALID AS DATA; REFUTED AS THE CLAIMED THREADING REPAIR.**

Fourteen scalar fields with no positivity, equation, inequality, admissibility,
or success predicate satisfy R35
(`DESIGN-S1-POLAR-v2.md:87-93,213`;
`DESIGN-FUDW-DECOMP-v4.1.md:607`). But precisely because the definition is
theorem-free, possession of this datum says nothing about whether its fields
witness any analytic row. The result DAG, not the definition, must export that
relation.

No constant in the arithmetic requires a numerical value: positivity,
\(C_\bullet\ge1\), and the displayed finite minima suffice. TeX 458 legitimately
supports named universal source witnesses; the path coefficient is instead
obtained by the explicit fixed-term Neumann derivation. No guessed radius was
found.

## 8. Dimension-freeness audit

| step | hostile conclusion |
|---|---|
| Rectification | Fixed-term product comparisons, scalar normalization, and operator-norm Neumann estimates introduce no basis sum (`approximate_algebras.tex:655-687`). |
| Charts and polar map | The only direct sum is the two-factor \(i\mathcal H\oplus\mathcal H\); max/sum and induced-operator conversions cost fixed factors (`approximate_algebras.tex:560,742-807,809-843`). |
| Group/path/derivative | A fixed number of associators, one quadratic path identity, and multiplier operator norms are used (`approximate_algebras.tex:655-661,857-893`). |
| Smooth upgrade | Lee C.34/C.40 are qualitative. Choosing Euclidean coordinates on a finite-dimensional real space changes no quantitative conclusion because no smoothness radius or norm modulus is exported (`lee-smooth-manifolds-2ed.txt:31134-31137,31330-31344`). |
| Compactness/closedness | Finite dimension is used only for bounded-closed compactness and injective \(\Rightarrow\) surjective. No compactness modulus becomes a coefficient (`DESIGN-S1-POLAR-v2.md:156-164,199-200`). |
| Quotient/orientation/index | The acting group and vertical line are fixed-dimensional; quotienting cannot enlarge the induced operator error; determinant dimension changes neither the norm guard nor the sign of \(2I\) (`DESIGN-S1-POLAR-v2.md:166-168,198-201`). |
| Amplification/block/stage | No entrywise sum, block count, number of stages, or amplification level occurs. The estimates apply verbatim whenever the amplified algebra satisfies the same axioms (`DESIGN-S1-POLAR-v2.md:202`). |

**DIMENSION-FREENESS VERDICT: VALID. NO ROUTE-LEVEL ALARM.**

## 9. Verdict on every v2 §9 disposition claim

### 9.1 Blockers, loci, and per-row claims

| v2 §9 claim | verdict |
|---|---|
| C1-versus-smooth blocker cleared | **VALID-WITH-CORRECTIONS:** direct route works, but row 8 must be factored (`DESIGN-S1-POLAR-v2.md:225`). |
| Free witnesses and naked formulas cleared | **REFUTED:** formulas are inlined, but row 9 does not identify its tuple with producer witnesses (`DESIGN-S1-POLAR-v2.md:226`). |
| Missing group-to-derivative edge cleared | **VALID** (`DESIGN-S1-POLAR-v2.md:105,227`). |
| TeX 458 used without numerical constants | **VALID** (`DESIGN-S1-POLAR-v2.md:228`; TeX 458). |
| TeX 560 fixed-factor clarification | **VALID** (`DESIGN-S1-POLAR-v2.md:229`; TeX 560). |
| Straight-path inverse guard | **VALID** (`DESIGN-S1-POLAR-v2.md:104,230`). |
| Full rectification and \(\|J\|=1\) | **VALID-WITH-CORRECTIONS:** reconstruction must not import stronger content from the weak landed contract (`DESIGN-S1-POLAR-v2.md:231`; TeX 407--440,672--687). |
| TeX 692--725 right-inverse/multiplier use | **VALID-WITH-CORRECTIONS:** the row conclusion includes it; the proof must actually perform the Neumann/right-inverse step (`DESIGN-S1-POLAR-v2.md:232`). |
| TeX 728--807 smooth repair | **VALID-WITH-CORRECTIONS:** Lee C.40 works, but rows 2 and 8 require factoring (`DESIGN-S1-POLAR-v2.md:233`). |
| TeX 809--843 inline radii | **VALID** (`DESIGN-S1-POLAR-v2.md:234`). |
| TeX 845--855 mismatch/typo | **VALID** (`DESIGN-S1-POLAR-v2.md:235`). |
| TeX 857--880 domains and defects | **VALID-WITH-CORRECTED-PROVENANCE:** only three defects are literal; two closeness bounds use TeX 845--868 (`DESIGN-S1-POLAR-v2.md:236`). |
| TeX 881--893 repeated denominator | **VALID:** the bad second-variable formula is not consumed (`DESIGN-S1-POLAR-v2.md:237`). |
| TeX 895--912 path omission/H-space typo | **VALID** (`DESIGN-S1-POLAR-v2.md:238`). |
| TeX 943--955 consumer closure | **VALID-WITH-CORRECTIONS:** added producers are enough only after factoring, witness repair, and the quotient phase-lift (`DESIGN-S1-POLAR-v2.md:239`). |
| Coherence row free polar witnesses | **VALID** (`DESIGN-S1-POLAR-v2.md:240`). |
| Derivative target chart retention | **VALID** (`DESIGN-S1-POLAR-v2.md:241`). |
| Ledger logical closure | **REFUTED:** conditional arithmetic is preserved, but compatibility is not in the contract (`DESIGN-S1-POLAR-v2.md:242`). |

### 9.2 Dependency, consumer, definition, and dimension claims

| v2 §9 claim | verdict |
|---|---|
| Explicit smooth producer | **VALID-WITH-CORRECTIONS:** mathematical producer exists; factor it (`DESIGN-S1-POLAR-v2.md:248`). |
| Witness threading | **REFUTED:** data plus an arithmetic existential does not export common analytic witnesses (`DESIGN-S1-POLAR-v2.md:249`). |
| Chart row cap/compoundness | **REFUTED:** a projected \(10/3\) count does not satisfy the no-compound rule (`DESIGN-S1-POLAR-v2.md:250`). |
| Derivative descent/same-chart/determinant | **VALID-WITH-CORRECTIONS:** add quotient fixed-class phase-lift (`DESIGN-S1-POLAR-v2.md:251`). |
| Quotient regularity/closedness/orientation | **VALID-WITH-CORRECTIONS:** use factored smooth and Maurer--Cartan rows (`DESIGN-S1-POLAR-v2.md:252`). |
| Left inversion joint paths/smooth map | **VALID-WITH-CORRECTIONS:** direct route works after factoring and witness repair (`DESIGN-S1-POLAR-v2.md:253`). |
| Smooth manifold/triangulation/local index | **VALID-WITH-CORRECTIONS:** phase-lift remains unstated (`DESIGN-S1-POLAR-v2.md:254`). |
| Lefschetz maximal simplex | **VALID** (`DESIGN-S1-POLAR-v2.md:255`). |
| Qualified \(\phi_V\) | **VALID** (`DESIGN-S1-POLAR-v2.md:256`). |
| Controlled rectification gap | **VALID-WITH-CORRECTIONS:** explicitly reconstruct stronger content instead of importing it from the landed contract (`DESIGN-S1-POLAR-v2.md:257`). |
| Straight-path gap | **VALID** (`DESIGN-S1-POLAR-v2.md:258`). |
| Source-radius mismatch | **VALID** (`DESIGN-S1-POLAR-v2.md:259`). |
| Derivative typing | **VALID** (`DESIGN-S1-POLAR-v2.md:260`). |
| No numerical polar constants | **VALID** (`DESIGN-S1-POLAR-v2.md:261`). |
| Additional smoothness/free-witness/missing-dep bundle | **REFUTED AS A BUNDLE:** smoothness and the missing edge are repaired; witness closure is not (`DESIGN-S1-POLAR-v2.md:262`). |
| Direct-sum/operator-norm correction | **VALID** (`DESIGN-S1-POLAR-v2.md:263`). |
| Qualitative smooth upgrade | **VALID** (`DESIGN-S1-POLAR-v2.md:264`). |
| Expand every rectified axiom | **VALID-WITH-CORRECTIONS:** contract says this; dependency use must remain honest (`DESIGN-S1-POLAR-v2.md:265`). |
| Qualify \(\phi_V\) | **VALID** (`DESIGN-S1-POLAR-v2.md:266`). |
| Complete fixed-class plan | **VALID-WITH-CORRECTIONS:** add the quotient phase-lift (`DESIGN-S1-POLAR-v2.md:267`). |
| Preserve finite-minimum arithmetic | **VALID FOR ARITHMETIC ONLY:** it does not cure tuple compatibility (`DESIGN-S1-POLAR-v2.md:268`). |

## 10. Final landing decision

**DO NOT LAND OR SEED THE v2 TABLE. REDESIGN, THEN RE-AUDIT.**

The mathematical route is still closable and no local-source acquisition is
needed for the direct smoothness repair. The redesign is architectural and
contract-logical, not a route obstruction:

1. factor the graph/Maurer--Cartan and the three smoothness interfaces;
2. export an actual common-witness relation, separately from universal scalar
   arithmetic;
3. add the quotient fixed-class phase-lift;
4. correct group-law and rectification provenance.

Nothing in this audit is rigorous, no status is promoted, and no af-VALIDATED
contract is changed.
