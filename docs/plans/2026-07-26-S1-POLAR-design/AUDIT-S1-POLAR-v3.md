# AUDIT — fresh hostile re-audit of `DESIGN-S1-POLAR-v3.md`

Date: 2026-07-27  
Role: fresh independent hostile auditor; not an author of any of the three
designs or either prior audit  
Status: **AUDIT ONLY; NON-RIGOROUS; no status promotion**

## 0. Final disposition

**REDESIGN.**

The analytic route still appears mathematically closable, and I found no
route-level obstruction or dimension-dependent coefficient. The mandated
factoring, direct smoothness upgrade, corrected provenance, and quotient
phase-lift are real repairs. But the third `DESIGNED-CLOSABLE` claim still is
not landable: its new load-bearing row 13 is not a mathematical registry
contract.

### 0.1 Fatal defect: row 13 quantifies over contract text

`lem-stage1-polar-constant-ledger` says that, “after replacing the leading
existential constants in the contracts of” seven named rows, “the entire
remaining universally quantified conclusion” of each contract is true
simultaneously. It then refers to “the finite-minimum values specified by” row
12 and “the full conclusion” of row 12
(`DESIGN-S1-POLAR-v3.md:88-105,133,155,309,343,419,442`).

That is meta-level text rewriting, not an object-level proposition about
algebras, maps, constants, and inequalities. The registry requires the
`contract:` line itself to be the mathematical statement and the single source
of truth for the af root conjecture and dependent imports
(`argument/README.md:9-16,24-28,42-46,73-76`). Neither the linker nor an af
proof root has an object representing “the contract of lemma X,” a substitution
operation on that string, or “the entire remaining conclusion.” A YAML
dependency edge imports a theorem; it does not turn the theorem's source text
into a quantified mathematical object. This is exactly the level distinction
that killed v2, now papered over with more explicit meta-language
(`AUDIT-S1-POLAR-v2.md:23-32,236-249,263,376,383,412-414`;
`BRIEF-S1-POLAR-REPAIR-v3.md:30-42,102-108`).

**Row 13 is REFUTED as a closed registry/af contract.** Consequently rows
12–13 do not yet export the genuine common-witness relation required by the
binding audit, and every downstream row depending on row 13 remains blocked at
contract level.

The exact object-level repair is one of the following:

1. Keep row 12 universal. Replace row 13 by a root of the form
   \(\exists W\,[A_1(W)\wedge\cdots\wedge A_7(W)\wedge R(W)]\), where
   \(A_1,\ldots,A_7\) are the seven **fully restated parameterized
   conclusions** of rows 1, 2, 3, 4, 6, 7, and 8, referring to the same graph
   maps, polar inverse, group maps, and scalar fields, and \(R(W)\) explicitly
   states the four finite-minimum equations and all scalar conclusions from
   row 12. No phrase may refer to contracts, textual replacement, or “the full
   conclusion” of another row.
2. Or use the binding option (b): delete row 13 and make every consumer choose
   the seven producer witnesses, take the finite maxima/minima object-level,
   and apply universal row 12 locally.

The first repair preserves the intended architecture. It must be re-projected
against the 12-node/depth-3 cap after its actual object-level root is written;
the present `10 / 3` projection is not a projection of a well-formed theorem
(`DESIGN-S1-POLAR-v3.md:133-137`; `argument/README.md:80-81`;
`DESIGN-FUDW-DECOMP-v4.1.md:586,607`).

### 0.2 Secondary transcription defect

The six downstream proposal rows have contracts and `deps`, but their table has
no `defs` field at all (`DESIGN-S1-POLAR-v3.md:157-170`). All six ids are absent
from the current registry, so there is no existing shard metadata to inherit.
Before transcription, add exact definition imports:

- isolation: `def-epsilon-cstar-algebra`;
  `def-approximate-unitary-space`;
- quotient manifold and finite-CW: `def-approximate-unitary-space` (and
  `def-epsilon-cstar-algebra` where the contract names the algebra);
- quotient left inversion: `def-approximate-unitary-space`;
  `def-h-space-left-inversion`; `def-epsilon-cstar-algebra`;
- quotient index: `def-approximate-unitary-space`;
  `def-lefschetz-fixed-point-data`; `def-epsilon-cstar-algebra`;
- maximal-simplex placement: none.

This is a registry-completeness correction, not a mathematical alarm
(`BRIEF-S1-POLAR.md:46-50`; `argument/README.md:24-29,45-46,73-75`;
`DESIGN-FUDW-DECOMP-v4.1.md:196-208,397-399`).

## 1. Local-source, retained-content, and interface audit

The three hashes printed by v3 are exact:

- Kitaev:
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`;
- Lee:
  `324b7d8b1f70d40eb7608919e3c9cef93628215fa9e9f0816cb4c9549f058b3c`;
- Munkres:
  `9fcbbac92a09926498c1caba8fafa61b1a3568033485b3977edc523cc0459e5d`.

These match the local payloads and v3
`DESIGN-S1-POLAR-v3.md:39-48`.

| checked locus | hostile result | verdict |
|---|---|---|
| Kitaev 407–440 | The source has bilinear product, product norm, associator, conjugate-linear isometric involution, exact dagger/product compatibility, lower \(C^*\)-bound, both exact unit laws, \(\|J\|=1\), and \(J^\dagger=J\). Row 1's reconstruction list now names all of them. | **VALID** (`approximate_algebras.tex:407-440`; `DESIGN-S1-POLAR-v3.md:121,143`) |
| Kitaev 458 | Each \(O(\cdot)\) is a concrete data-independent function. It supports named small-range coefficients, not invented numerical values. | **VALID** (`approximate_algebras.tex:458`; `DESIGN-S1-POLAR-v3.md:55,107-111`) |
| Kitaev 554–560 | Multiple-variable derivatives use a direct-sum norm between max and sum. Two-factor vector comparison costs at most \(2\); source and target operator-norm comparison may cost another fixed factor. | **VALID** (`approximate_algebras.tex:554-560`; `DESIGN-S1-POLAR-v3.md:56,232`) |
| Kitaev 655–687 | Multiplier/Neumann estimates are present. `prop_unit` prints exact unit, close product, and exact dagger compatibility, but not every rectified \(C^*\)-axiom or \(\|J\|=1\). V3 correctly requires reconstruction rather than consuming hidden content from the landed shard. | **VALID-WITH-CORRECTIONS**: retain the stated in-tree derivation (`approximate_algebras.tex:655-687`; `DESIGN-S1-POLAR-v3.md:121,143`; `argument/lemmas/lem-stage1-exact-unit-rectification.md:4-9`) |
| Kitaev 692–807 | The approximate-unitary sets include the right-inverse condition; graph existence, uniqueness, \(C^1\) estimates, tangent spaces, and the Maurer–Cartan formula are present. The source remains only \(C^1\). | **VALID** (`approximate_algebras.tex:692-725,728-807`; `DESIGN-S1-POLAR-v3.md:122-123,144-145`) |
| Kitaev 809–855 | The \(C^1\) polar map and inner/outer losses are present. The supported domain is the shrunken inner set; line 845's larger symbol and line 849's \(v/u\) typo are not consumed. | **VALID-WITH-CORRECTIONS**: retain the displayed derivation and smaller domain (`approximate_algebras.tex:809-855`; `DESIGN-S1-POLAR-v3.md:124,146`) |
| Kitaev 845–878 | Product/adjoint inputs are put in an \(O(\varepsilon_r)\) approximate-unitary set at 861–868; polar closeness at 845–855 yields the two map-closeness estimates. Only the three group defects are literal at 872–874, and the basepoints are at 876–878. | **VALID** (`approximate_algebras.tex:845-878`; `DESIGN-S1-POLAR-v3.md:126,148`) |
| Kitaev 881–893 | The first-variable inversion derivative is typed at 889–892. The repeated denominator at 883–888 remains a printed erratum and is not used. | **VALID** (`approximate_algebras.tex:881-893`; `DESIGN-S1-POLAR-v3.md:128,150`) |
| Kitaev 895–912 | The H-space prose asserts projection of straight paths but omits right-invertibility and polar-domain estimates. V3's exact quadratic identity and Neumann obligation are still needed. | **VALID-WITH-CORRECTIONS**: retain the stated derivation (`approximate_algebras.tex:895-912`; `DESIGN-S1-POLAR-v3.md:127,149`) |
| Kitaev 943–955 | Actual isolation, quotient fixed classes, topology, orientation, finite-CW type, and left inversion are prose assertions. Line 945 displays the phase square root, but does not itself prove nearby quotient isolation. | **REFUTED** as sufficient provenance (`approximate_algebras.tex:943-955`; `DESIGN-S1-POLAR-v3.md:61-62,169,172-179`) |
| Lee C.34/C.36 | C.34 is the smooth local inverse theorem; C.36 says an injective smooth map with everywhere nonzero Jacobian is a diffeomorphism onto its image, and proves the inverse is locally the smooth inverse. Row 10 supplies smoothness, derivative invertibility, and injectivity before use. | **VALID** (`lee-smooth-manifolds-2ed.txt:31134-31137,31286-31298`; `DESIGN-S1-POLAR-v3.md:130,152`) |
| Lee C.40 | It gives a local smooth solution graph when the normal derivative is nonsingular. Row-2 uniqueness identifies these local solutions on overlaps. | **VALID** (`lee-smooth-manifolds-2ed.txt:31330-31344,31374-31385`; `DESIGN-S1-POLAR-v3.md:122,129,151`) |
| Munkres 4.9/5.11 | Compatible smooth structures are present, but they do not preserve the selected maps or equivariance. V3 uses them only as fallback. | **VALID** as fallback only (`munkres-elementary-differential-topology.txt:2055-2056,2533-2558`; `DESIGN-S1-POLAR-v3.md:65,69-71`) |
| Munkres 4.2 | Smooth approximation and differentiable homotopy are present; the relative statement is an exercise. V3 does not consume it. | **VALID** with the stated scope callout (`munkres-elementary-differential-topology.txt:1833-1840,1888-1901`; `DESIGN-S1-POLAR-v3.md:66`) |
| Munkres 3.10 | Fine-\(C^1\) stability of immersion/embedding is present; diffeomorphism needs the boundary-preservation hypothesis. V3 does not consume it. | **VALID** (`munkres-elementary-differential-topology.txt:1509-1514,1596-1637`; `DESIGN-S1-POLAR-v3.md:67`) |

The landed interfaces are used honestly:

- the quantitative inverse row exports only injectivity, Lipschitz bounds, and
  image containment (`lem-stage1-quantitative-inverse-function.md:4-9`);
- the landed rectification row exports only exact unit and product/unit
  closeness (`lem-stage1-exact-unit-rectification.md:4-9`);
- the quotient theorem requires a smooth free proper action on a smooth
  manifold (`lem-topology-quotient-manifold.md:4-9`);
- the local-index row requires an isolated fixed point of a smooth self-map on
  a compact orientable manifold (`lem-topology-local-index-sign.md:4,14-22`);
- the finite-triangulation row still has `status: stated`, `af: seeded`, and
  assumes a compact smooth boundaryless manifold
  (`lem-topology-finite-triangulation.md:4,7-9,20-29`);
- the Lefschetz row has the exact maximal-simplex hypothesis
  (`lem-topology-lefschetz-hopf.md:4,25-33`);
- the top-cohomology row has the exact connected/compact/orientable/without-
  boundary hypotheses (`lem-topology-orientable-top-cohomology.md:4,19-29`).

### 1.1 Verbatim-retention check

The contract strings of v3 rows 1, 4, 5, 6, 7, and 8 match their v2
counterparts byte-for-byte after accounting for v3's added numeric table
column. Only the allowed provenance/dependency changes occur
(`DESIGN-S1-POLAR-v2.md:99,101-105`;
`DESIGN-S1-POLAR-v3.md:121,124-128`). The two definition-content cells also
match verbatim (`DESIGN-S1-POLAR-v2.md:212-213`;
`DESIGN-S1-POLAR-v3.md:254-255`). Row 12 changes v2's existential packaging
to universal quantification but retains every scalar formula and inequality
(`DESIGN-S1-POLAR-v2.md:107`; `DESIGN-S1-POLAR-v3.md:132`;
`BRIEF-S1-POLAR-REPAIR-v3.md:69-79`). No forbidden silent mathematical change
was found.

## 2. Witness-unification attack

### 2.1 Monotonicity of all seven producers

The finite-maxima/minima mathematics is sound. The failure is row 13's
meta-level statement, not monotonicity.

| producer | hostile monotonicity check | verdict |
|---|---|---|
| Row 1, rectification | Increasing \(C_{\rm rect}\) weakens all defect/closeness bounds and permits viewing a smaller-defect algebra as an \(\varepsilon_r=C_{\rm rect}\varepsilon_X\) algebra; shrinking \(e_{\rm rect}\) strengthens the premise. In the actual seven-row join \(C_{\rm rect}\) occurs only here. | **VALID** (`DESIGN-S1-POLAR-v3.md:121`) |
| Row 2, graph | Increasing \(C_{\rm ch}\) and decreasing \(\kappa_{\rm ch}\) strengthen \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\), weaken both norm bounds, and retain \(C_{\rm ch}(\varepsilon_r+\delta)<1\) because \(\kappa_{\rm ch}\le1/2\). The unique graph itself is independent of the chosen bound. | **VALID** (`DESIGN-S1-POLAR-v3.md:122`; TeX 758–793) |
| Row 3, Maurer–Cartan | The names \(C_{\rm ch},\kappa_{\rm ch}\) are locally bound, not automatically row-2's witnesses. This is not a new obstruction: choose row 3's pair after importing row 2, then take the common max/min; uniqueness identifies the graph maps. A larger \(C_{\rm ch}\) strengthens the guard and weakens \(1+C_{\rm ch}\varepsilon_r\). | **VALID** (`DESIGN-S1-POLAR-v3.md:123,145`; TeX 795–807) |
| Row 4, polar | A larger \(C_{\rm pol}\) strengthens the guard, shrinks the inner radius \(\delta-C_{\rm pol}(\varepsilon_r\delta+\delta^2)\), and enlarges the outer radius. Thus **both** sandwich inclusions become weaker, not conflicting. A smaller \(\kappa_{\rm pol}\) strengthens the premise. | **VALID** (`DESIGN-S1-POLAR-v3.md:124`; TeX 809–843) |
| Row 6, group | Larger \(C_{\rm grp}\) strengthens the domain guard and weakens every error bound. Larger \(C_{\rm pol}\)/smaller \(\kappa_{\rm pol}\) strengthen both polar and inner-radius guards. | **VALID** (`DESIGN-S1-POLAR-v3.md:126`; TeX 845–878) |
| Row 7, path | Larger \(C_{\rm path}\) strengthens both path guards and enlarges the approximate-unitary set in the conclusion; larger \(C_{\rm pol}\) shrinks the admissible inner domain. All directions are monotone. | **VALID** (`DESIGN-S1-POLAR-v3.md:127`; TeX 895–912) |
| Row 8, derivative | Increasing \(C_{\rm ch}\), \(C_{\rm pol}\), \(C_{\rm grp}\), and \(C_{\rm der}\) strengthens every displayed guard, including the chart-retention left side, while only \(C_{\rm der}\) appears in the concluding error bound and makes it weaker. Decreasing the three margins strengthens the premises. | **VALID** (`DESIGN-S1-POLAR-v3.md:128`) |

The common maps are also coherent: graph solutions are unique (TeX 758–793),
and \(S_\delta\) is the image of the literal polar map, whose inverse is unique
(`DESIGN-S1-POLAR-v3.md:122,124-125`). Thus an object-level row 13 can use one
tuple and the same maps. The current text simply does not state that
object-level conjunction.

### 2.2 Consumer linkage

Rows 12–13 **do not presently deliver** what the four quantitative consumers
need. Rows 16–20 of the landing order import an id whose alleged conclusion
cannot be an af root (`DESIGN-S1-POLAR-v3.md:165-169,281-287`). Once row 13 is
replaced by the explicit conjunction above, its same tuple supplies:

- row 8's chart/polar/group/derivative guards for isolation;
- rows 3, 9, and 11 at a common rectified range for the quotient;
- rows 5–7 and 11 at a common range for the H-space/left inversion;
- row 8, smooth \(\sigma\), and the actual-isolation radius for quotient index.

That is a valid repair plan, but it is not the contract currently written.

## 3. Independent recomputation of row 12

Let
\[
d=\delta_*,\qquad e=\varepsilon_r,\qquad q=C_{\rm grp}e .
\]
From v3's minima one gets
\[
\begin{gathered}
d,e\le\tfrac14,\quad
C_{\rm ch}d,C_{\rm ch}e\le\kappa_{\rm ch}/4,\quad
C_{\rm pol}d,C_{\rm pol}e\le\kappa_{\rm pol}/4,\\
C_{\rm der}e\le\kappa_{\rm der}/8,\quad
q\le1,\quad q\le d/(12C_{\rm path}),\\
0<r_{\rm iso}\le d/4,\quad
C_{\rm der}r_{\rm iso}\le\kappa_{\rm der}/8 .
\end{gathered}
\]
These follow directly from `DESIGN-S1-POLAR-v3.md:132`.

All eight guards recompute:

1. \(C_{\rm ch}(e+d)\le\kappa_{\rm ch}/2\le\kappa_{\rm ch}\), and the same
   calculation gives the polar guard.
2. \(r_-=d(1-C_{\rm pol}(e+d))\ge3d/4\).
3. \(q\le d/(12C_{\rm path})\le d/12<3d/4\le r_-\).
4. \(C_{\rm path}q\le d/12\le1/48<1/4\).
5. Since \(e\le1/4\) and \(q\le1\),
   \(\eta=C_{\rm path}q(1+e+q)\le3C_{\rm path}q\le d/4<r_-\).
6. \(C_{\rm der}(e+r_{\rm iso})\le\kappa_{\rm der}/4
   \le\kappa_{\rm der}\).
7. The retention left side is at most
   \[
   \frac54\frac54\frac d4+\frac d{12}
   =\frac{91}{192}d<2d .
   \]
8. \(0<r_{\rm iso}\le d\), \(q\le1\), and the rectified-input premise
   follows from \(e_{\rm S1}\le e_{\rm rect}\) and
   \(C_{\rm rect}e_{\rm S1}\le\varepsilon_*^r\).

The three advertised final bounds are therefore exactly
\[
r_-\ge3d/4,\qquad
\eta\le d/4,\qquad
C_{\rm der}(r_{\rm iso}+e)\le\kappa_{\rm der}/4<1 .
\]
**Row 12's scalar arithmetic is VALID**, with no transcription error
(`DESIGN-S1-POLAR-v3.md:132,154`; compare the independent v2 computation at
`AUDIT-S1-POLAR-v2.md:187-245`).

## 4. Verdict per analytic row

| # / proposed row | verdict | hostile finding |
|---|---|---|
| 1 `lem-stage1-rectified-cstar-control` | **VALID** | V3 now explicitly makes the stronger package an in-tree reconstruction and enumerates every axiom, including exact dagger compatibility and \(\|J\|=1\). It consumes only the landed contract's weak advertised interface. (`DESIGN-S1-POLAR-v3.md:121,143`; TeX 407–440,672–687; `lem-stage1-exact-unit-rectification.md:4`.) |
| 2 `lem-stage1-unitary-graph-control` | **VALID** | This is now one graph/estimate/normal-invertibility interface, exactly the mandatory first factor. The right-inverse and Neumann work remains an explicit derivation. (`DESIGN-S1-POLAR-v3.md:122,144`; TeX 692–793.) |
| 3 `lem-stage1-maurer-cartan-trivialization` | **VALID** | This is a distinct tangent/trivialization interface. The separately bound \(C_{\rm ch},\kappa_{\rm ch}\) can dominate row 2's pair, and unique graph maps prevent witness ambiguity. The two equivariance formulas follow from \(L_{cU}=cL_U\) and \(L_U(iJ)=iU\). (`DESIGN-S1-POLAR-v3.md:123,145`; TeX 795–807.) |
| 4 `lem-stage1-polar-retraction` | **VALID** | Contract retained verbatim; the inner and outer radii are correctly inlined and monotone. (`DESIGN-S1-POLAR-v2.md:101`; `DESIGN-S1-POLAR-v3.md:124`; TeX 809–855.) |
| 5 `lem-stage1-polar-coherence-naturality` | **VALID** | Contract retained verbatim. Injectivity at the larger of two scales gives coherence; bilinearity gives scalar naturality. (`DESIGN-S1-POLAR-v2.md:102`; `DESIGN-S1-POLAR-v3.md:125`; TeX 809–845.) |
| 6 `lem-stage1-approximate-group-laws` | **VALID** | Contract retained verbatim and provenance is now honest: closeness is derived at 845–868, defects are literal at 872–874, basepoints at 876–878. (`DESIGN-S1-POLAR-v3.md:126,148`; TeX 845–878.) |
| 7 `lem-stage1-polar-path-admissibility` | **VALID** | Contract retained verbatim. The exact quadratic identity, one Neumann comparison, one polar domain, and scalar naturality supply the omitted source steps. (`DESIGN-S1-POLAR-v3.md:127,149`; TeX 655–661,699–725,895–912.) |
| 8 `lem-stage1-inversion-derivative-control` | **VALID** | Contract retained verbatim; the group dependency supplies the adjoint domain, and the retention guard types the target chart. (`DESIGN-S1-POLAR-v3.md:128,150`; TeX 857–893.) |
| 9 `lem-stage1-smooth-unitary-atlas` | **VALID** | Atomic atlas upgrade. The fixed-parenthesization graph equation is a degree-two real polynomial; row 2 gives normal invertibility and uniqueness; Lee C.40 glues the unchanged graph locally. (`DESIGN-S1-POLAR-v3.md:129,151`; TeX 420–429,742–793; Lee txt:31330–31344,31374–31385.) |
| 10 `lem-stage1-smooth-polar-inverse` | **VALID** | Atomic inverse upgrade. Row 9 makes the ambient-bilinear polar map smooth; row 4 supplies the same bijective \(C^1\) local diffeomorphism; Lee C.34/C.36 makes its same inverse smooth. (`DESIGN-S1-POLAR-v3.md:130,152`; Lee txt:31134–31137,31286–31298.) |
| 11 `lem-stage1-smooth-unitary-operations` | **VALID** | Atomic consumer interface at the granularity demanded by the repair brief. Row 6 supplies product/adjoint domains, row 10 supplies smooth \(u_\delta\), and row 9 supplies the embedded target. The conclusion explicitly says smooth **into** \(\mathcal U\). (`DESIGN-S1-POLAR-v3.md:131,153`; TeX 857–868.) |
| 12 `lem-stage1-polar-scalar-arithmetic` | **VALID** | Universal, object-level, and independently recomputed in §3 above. (`DESIGN-S1-POLAR-v3.md:132,154`.) |
| 13 `lem-stage1-polar-constant-ledger` | **REFUTED** | It rewrites and quantifies over contract text instead of stating the seven analytic predicates and arithmetic conjunction object-level. Exact required repair is §0.1 above. (`DESIGN-S1-POLAR-v3.md:88-105,133,155`; `argument/README.md:14-16,42-46`.) |

Rows 2–3 and 9–11 are genuinely factored. No remaining compoundness defect was
found in those five interfaces (`BRIEF-S1-POLAR-REPAIR-v3.md:21-29`;
`DESIGN-FUDW-DECOMP-v4.1.md:586`).

## 5. Verdict per downstream repair

All statements below remain non-rigorous design candidates. The repeated
correction is mandatory: replace the invalid row-13 dependency by the repaired
object-level common-witness result and add the exact `defs` metadata listed in
§0.2.

| downstream repair | verdict | hostile finding / exact correction |
|---|---|---|
| `lem-stage1-uniform-inversion-isolation` | **VALID-WITH-CORRECTIONS** | The quantitative IFT applies to \(F_s-\mathrm{id}\), and chart retention legitimizes coordinate equality. Rewire row 13 to its object-level replacement and add the two definition imports. (`DESIGN-S1-POLAR-v3.md:165`; `lem-stage1-quantitative-inverse-function.md:4`.) |
| `lem-stage1-quotient-manifold-package` | **VALID-WITH-CORRECTIONS** | Rows 3, 9, and 11 supply orientation, smooth manifold, and smooth action; compactness/closedness uses the finite-dimensional Neumann argument. Rewire row 13 and state `defs`. (`DESIGN-S1-POLAR-v3.md:166,199`; `lem-topology-quotient-manifold.md:4`.) |
| `lem-stage1-quotient-finite-cw` | **VALID-WITH-CORRECTIONS** | Its hypothesis exactly matches the landed compact-smooth-boundaryless contract, and status cannot outrun the seeded dependency. Add carried definition metadata; it remains transitively blocked by the corrected quotient row. (`DESIGN-S1-POLAR-v3.md:167,200,295-297`; `lem-topology-finite-triangulation.md:4,7-9,20-29`.) |
| `lem-stage1-quotient-left-inversion` | **VALID-WITH-CORRECTIONS** | Rows 5–7 and 11 supply scalar descent, smooth inversion, and joint paths. Rewire row 13 and add `def-h-space-left-inversion` plus the algebra/unitary defs. (`DESIGN-S1-POLAR-v3.md:168,201`; TeX 895–912.) |
| `lem-stage1-quotient-inversion-index-data` | **VALID-WITH-CORRECTIONS** | The new phase-lift is correct and explicit; derivative descent and determinant sign are supported. Rewire row 13 and add the fixed-index/unitary/algebra defs. (`DESIGN-S1-POLAR-v3.md:169,172-179,198,204`; `lem-topology-local-index-sign.md:4,14-22`.) |
| `lem-finite-polyhedron-maximal-simplex-placement` | **VALID** | A simplex containing a point extends in the finite face poset to a maximal simplex. No definition or analytic dependency is needed. (`DESIGN-S1-POLAR-v3.md:170`; `lem-topology-lefschetz-hopf.md:4,25-33`.) |

### 5.1 Phase-lift check

If \([U]\) is quotient-fixed, choose \(U_0\) near \(J\) with
\(\sigma(U_0)=cU_0\). Row 11 exports
\(\sigma(aU_0)=\bar a\,\sigma(U_0)\). For \(a^2=c\),
\[
\sigma(aU_0)=\bar a c\,U_0=aU_0 .
\]
Continuity at \(J\) makes \(c\) close to \(1\); choosing the root \(a\) close to
\(1\) puts \(aU_0\) in the \(J\)-ball and \(-aU_0\) in the \(-J\)-ball. Actual
isolation then gives \(aU_0=J\) and \(-aU_0=-J\), hence \([U]=[J]\).
This is explicitly in the quotient-index contract and proof obligation and is
recorded separately in the fixed-class ledger
(`DESIGN-S1-POLAR-v3.md:131,169,172-179,198,204,220-222`;
TeX 943–951). **The phase-lift repair is VALID.**

## 6. Verdict per `lem-stage1-extra-fixed-class` obligation

| obligation-ledger line | verdict | hostile finding |
|---|---|---|
| Actual inversion isolation near \(J,-J\) | **VALID-WITH-CORRECTIONS** | Analytically supplied by the isolation row, but that row must import the repaired object-level common tuple. (`DESIGN-S1-POLAR-v3.md:197`.) |
| Quotient isolation of \([J]\) | **VALID-WITH-CORRECTIONS** | The square-root phase-lift is now explicit and correct; its quotient-index producer still needs the row-13 rewire. (`DESIGN-S1-POLAR-v3.md:198`; §5.1 above.) |
| Connected compact orientable positive-dimensional smooth quotient | **VALID-WITH-CORRECTIONS** | Rows 3, 9, and 11 and the landed smooth quotient theorem supply the advertised interfaces, conditional on repaired common witnesses. (`DESIGN-S1-POLAR-v3.md:199`; `lem-topology-quotient-manifold.md:4`.) |
| Finite polyhedron / finite CW | **VALID-WITH-CORRECTIONS** | Hypothesis match is exact; the explicit warning that triangulation is still `stated/seeded` is honest. (`DESIGN-S1-POLAR-v3.md:200,295-297`; `lem-topology-finite-triangulation.md:4,7-9`.) |
| Continuous H-space and left inversion; smooth \(\breve\sigma\) | **VALID-WITH-CORRECTIONS** | Rows 5–7 and 11 suffice after the common-witness repair. (`DESIGN-S1-POLAR-v3.md:201`.) |
| Left-inversion trace | **VALID** | No new polar obligation is hidden here once finite-CW H-space data and the separately designed trace row exist. (`DESIGN-S1-POLAR-v3.md:202`.) |
| Lefschetz-Hopf maximal-simplex placement | **VALID** | The finite-poset row matches the narrowed landed Lefschetz contract. (`DESIGN-S1-POLAR-v3.md:203`; `lem-topology-lefschetz-hopf.md:4,25-33`.) |
| Local index \(+1\) | **VALID-WITH-CORRECTIONS** | Smoothness, genuine quotient isolation, quotient derivative control, and positive determinant are present, conditional on the repaired common-witness import. (`DESIGN-S1-POLAR-v3.md:204`; `lem-topology-local-index-sign.md:4,14-22`.) |
| Nonzero top cohomology and \(\Lambda(\breve\sigma)\ge2\) | **VALID** | Positive quotient dimension separates \(H^0\) from top degree; the landed top-cohomology hypotheses and trace formula are exactly the stated inputs. (`DESIGN-S1-POLAR-v3.md:205`; `lem-topology-orientable-top-cohomology.md:4,19-29`.) |

The ten-id dependency list really does add quotient-index and maximal-simplex
rows (`DESIGN-S1-POLAR-v3.md:207-222`). It is a topological list after the
proposed rows exist. It does not cure the invalid common-witness root upstream.

## 7. Definitions, dimension-freeness, DAG, and landing order

### 7.1 Definitions

| proposed definition | verdict | hostile finding |
|---|---|---|
| `def-approximate-unitary-space` | **VALID** | The content is notation-only, conditions \(\phi_V\) on invertibility of \(L_V\), and asserts no chart, inverse, estimate, regularity, compactness, orientation, or isolation theorem. It matches v2 verbatim. (`DESIGN-S1-POLAR-v2.md:212`; `DESIGN-S1-POLAR-v3.md:254,257-259`; TeX 692–750,845–859.) |
| `def-stage1-polar-witness-data` | **VALID** | It is valid as data: fourteen scalar fields and no positivity, validity, existence, or theorem predicate comply with R35. It cannot repair witness threading; that must be a result-level object proposition. (`DESIGN-S1-POLAR-v3.md:255,257-259`; `DESIGN-FUDW-DECOMP-v4.1.md:607`.) |

### 7.2 Dimension-freeness

The factoring introduces no new quantitative modulus. Rectification, graph,
polar, group, path, and derivative estimates use a fixed number of
operator-norm operations; the only direct sum has two factors; Lee's smooth
upgrades are qualitative; compactness and injective-implies-surjective are
qualitative finite-dimensional steps; \(U(1)\), the vertical line, and the
phase square root are fixed-dimensional; and the max/min join has seven fixed
packages (`DESIGN-S1-POLAR-v3.md:224-248`; TeX 458,554–560,655–687;
Lee txt:31134–31137,31286–31298,31330–31344).

**DIMENSION-FREENESS VERDICT: VALID AT DESIGN LEVEL. NO ROUTE-ALARM.**

### 7.3 DAG and budgets

Ignoring the ill-formed content of row 13, the declared edges are acyclic:
\[
\text{rectification}\to\text{graph}\to
\{\text{MC},\text{polar}\}\to
\{\text{coherence},\text{group},\text{path},\text{derivative}\}
\]
with the three smooth rows downstream of their exact inputs, universal
arithmetic independent, and the witness join downstream of rows
1,2,3,4,6,7,8,12. Row 13 correctly does not depend on rows 9–11
(`DESIGN-S1-POLAR-v3.md:119-137`). The six downstream edges then follow the
expected order (`ibid.:163-170`).

All well-formed factored rows claim at most 12 nodes/depth 3. Those are honest
design projections, not measured trees. Row 13's `10 / 3` claim is
**REFUTED AS A CURRENT PROJECTION** because there is no object-level root to
project; remeasure after writing the replacement contract
(`DESIGN-S1-POLAR-v3.md:133`; `argument/README.md:80-81`).

The serial order at `DESIGN-S1-POLAR-v3.md:261-297` is a genuine topological
sort and begins with the required definition/ratification gate. It cannot be
executed past item 13 until row 13 is redesigned. The seeded triangulation
status warning at lines 295–297 is correct.

## 8. Verdict on every v3 §10 disposition claim

The tables below follow v3 §10 in order. “VALID-WITH-CORRECTIONS” means the
mathematics/disposition is right only after the exact row-13 rewire or metadata
correction stated above.

### 8.1 V3 §10.1

| v3 §10.1 claim | verdict | exact check |
|---|---|---|
| §0.1 ledger incompatibility cleared | **REFUTED** | Row 13 is meta-level, not an object conjunction (`DESIGN-S1-POLAR-v3.md:309`; §0.1 above). |
| §0.2 compound rows cleared | **VALID** | Rows 2–3 and 9–11 are actually split (`ibid.:310,122-123,129-131`). |
| §0.3 quotient phase-lift cleared | **VALID** | Explicit in contract and ledger (`ibid.:311,169,198`). |
| §0.4 group provenance cleared | **VALID** | Correct split at TeX 845–878 (`ibid.:312,126,148`). |
| Hashes / locked-definition prefix | **VALID** | Hashes match; definition locus is TeX 407–440 (`ibid.:313`; `def-epsilon-cstar-algebra.md:9-10`). |
| TeX 407–440 complete axiom list | **VALID** | Row 1/§4 enumerate it (`ibid.:314,121,143`; TeX 407–440). |
| TeX 458 named witnesses | **VALID-WITH-CORRECTIONS** | No value is guessed, but row 13 still must state the object relation (`ibid.:315`; TeX 458). |
| TeX 560 norm comparison | **VALID** | Fixed two-stage factors are stated (`ibid.:316,232`; TeX 554–560). |
| TeX 655–687 rectification | **VALID** | V3 explicitly reconstructs rather than over-imports (`ibid.:317,121,143`). |
| TeX 692–725 right-inverse/Neumann | **VALID** | Explicit obligations remain in rows 2, 6, 7 (`ibid.:318,144,148-149`). |
| TeX 728–807 \(C^1\)/compoundness | **VALID** | Rows 2–3 and 9 split quantitative, MC, and smooth interfaces (`ibid.:319`). |
| TeX 809–855 polar losses | **VALID** | Retained row 4 uses the smaller domain (`ibid.:320,124`; TeX 809–855). |
| TeX 857–893 provenance/erratum | **VALID** | Row 6 corrected; row 8 avoids bad display (`ibid.:321,126,128`). |
| TeX 895–912 path omissions/type typo | **VALID** | Row 7 plus locked H-space definition (`ibid.:322,127`). |
| TeX 943–955 insufficient provenance | **VALID-WITH-CORRECTIONS** | Smooth/phase producers are present, but their consumers still need the repaired common tuple (`ibid.:323,129-131,169`). |
| Lee C.34/C.36 | **VALID** | Row 10 hypotheses match (`ibid.:324,130`; Lee txt:31134–31137,31286–31298). |
| Lee C.40 local graph only | **VALID** | Row-2 uniqueness supplies overlap equality (`ibid.:325,122,129`; Lee txt:31330–31344). |
| Munkres 4.9/5.11 fallback only | **VALID** | Explicit non-use (`ibid.:326,65,69-71`). |
| Munkres 4.2 relative form exercise | **VALID** | Explicit non-use/scope (`ibid.:327,66`). |
| Munkres 3.10 boundary qualification | **VALID** | Exact qualification, non-use (`ibid.:328,67`). |
| Landed quantitative IFT not smooth | **VALID** | Rows 9–10 use Lee, not the landed quantitative row (`ibid.:329,129-130`; `lem-stage1-quantitative-inverse-function.md:4`). |
| Landed rectification contract weak | **VALID** | Row 1 reconstructs internally (`ibid.:330,121,143`; landed shard line 4). |
| Landed quotient requires smooth data | **VALID-WITH-CORRECTIONS** | Rows 9/11 supply smooth data; common-range rewire remains (`ibid.:331,129,131,166`). |
| Deliverable scope not narrowed | **VALID** | Thirteen rows, six downstream rows, definitions, dimensions, and order are all present (`ibid.:332`; `BRIEF-S1-POLAR-REAUDIT-v3.md:14-19`). |

### 8.2 V3 §10.2

| v3 §10.2 claim | verdict | exact check |
|---|---|---|
| Polynomial graph and uniqueness gluing | **VALID** | Rows 2/9; TeX 420–429,742–793; Lee C.40 (`DESIGN-S1-POLAR-v3.md:338`). |
| Smooth polar inverse | **VALID** | Row 10; Lee C.34/C.36 (`ibid.:339,130`). |
| Smooth scalar action, \(\mu,\sigma\) into manifold | **VALID** | Row 11 explicitly corestricts to \(\mathcal U\) (`ibid.:340,131`). |
| First derivatives unchanged | **VALID** | Same maps/graphs are upgraded, not replaced (`ibid.:341,129-131`). |
| Eight scalar guards | **VALID** | Independently recomputed in §3 (`ibid.:342,132`). |
| Arithmetic logically connected to analytic witnesses | **REFUTED** | Row 13's “simultaneous substitution” is contract-text meta-language (`ibid.:343,133`; §0.1). |

### 8.3 V3 §10.3

| v3 §10.3 claim | verdict | exact check |
|---|---|---|
| Rectified control corrected | **VALID** | Full reconstruction (`DESIGN-S1-POLAR-v3.md:349,121,143`). |
| Unitary chart factoring | **VALID** | Rows 2–3 (`ibid.:350,122-123`). |
| Polar retraction retained | **VALID** | Exact contract match (`ibid.:351,124`; v2:101). |
| Coherence retained | **VALID** | Exact contract match (`ibid.:352,125`; v2:102). |
| Group provenance corrected | **VALID** | TeX 845–878 split (`ibid.:353,126`). |
| Path retained | **VALID** | Exact contract match (`ibid.:354,127`; v2:104). |
| Derivative retained/factored dep | **VALID** | Exact contract; graph dep renamed to factored row (`ibid.:355,128`). |
| Smooth package factoring | **VALID** | Rows 9–11 (`ibid.:356,129-131`). |
| Constant ledger repaired | **REFUTED** | Scalar row valid; witness row meta-level (`ibid.:357,132-133`). |
| Dependency order acyclic | **VALID-WITH-CORRECTIONS** | Edge order is acyclic, but row 13 is not a theorem until replaced (`ibid.:358`; §7.3). |
| Every row within cap after factoring | **VALID-WITH-CORRECTIONS** | Rows 1–12 are projected within cap; repaired row 13 must be re-projected (`ibid.:359,133`; `argument/README.md:80-81`). |

### 8.4 V3 §10.4

| v3 §10.4 claim | verdict | exact check |
|---|---|---|
| Isolation factored/range-correct | **VALID-WITH-CORRECTIONS** | Factored rows are right; replace row-13 dep (`DESIGN-S1-POLAR-v3.md:365,165`). |
| Quotient factored/range-correct | **VALID-WITH-CORRECTIONS** | Rows 3/9/11 are right; replace row-13 dep (`ibid.:366,166`). |
| Finite-CW contract/status | **VALID** | Exact smooth hypothesis and status warning (`ibid.:367,167,295-297`). |
| Left inversion factored/range-correct | **VALID-WITH-CORRECTIONS** | Rows 5–7/11 are right; replace row-13 dep (`ibid.:368,168`). |
| Quotient index phase-lift | **VALID** | Explicit contract/proof obligation (`ibid.:369,169,172-179`). |
| Maximal-simplex placement | **VALID** | Exact landed hypothesis (`ibid.:370,170`; Lefschetz shard line 4). |
| Actual isolation obligation | **VALID-WITH-CORRECTIONS** | Upstream common-witness rewire (`ibid.:371,197`). |
| Quotient isolation phase-lift obligation | **VALID** | Separately recorded (`ibid.:372,198`). |
| Smooth quotient obligation | **VALID-WITH-CORRECTIONS** | Smooth producers exist; common range must be object-level (`ibid.:373,199`). |
| Finite-CW obligation | **VALID** | Exact landed hypothesis and honest status (`ibid.:374,200`). |
| H-space/left inversion/smooth inversion | **VALID-WITH-CORRECTIONS** | Factored producers correct; common-range rewire (`ibid.:375,201`). |
| Left-inversion trace | **VALID** | No new polar claim (`ibid.:376,202`). |
| Lefschetz maximal-simplex | **VALID** | Explicit producer (`ibid.:377,203`). |
| Local index \(+1\) | **VALID-WITH-CORRECTIONS** | Phase lift is fixed; common analytic tuple remains (`ibid.:378,204`). |
| Top cohomology/Lefschetz comparison | **VALID** | Exact landed hypotheses (`ibid.:379,205`). |
| Ten-id extra-fixed dependency list | **VALID** | Both additions are explicit (`ibid.:380,207-218`). |

### 8.5 V3 §10.5

| v3 §10.5 claim | verdict | exact check |
|---|---|---|
| Approximate-unitary definition | **VALID** | Unchanged theorem-free content (`DESIGN-S1-POLAR-v3.md:386,254`). |
| Witness data plus result-level relation | **REFUTED** | The datum is valid, but the claimed row-13 result-level relation is not object-level (`ibid.:387,255,133`). |
| No guessed numerical constant | **VALID** | Named witnesses/minima only (`ibid.:388`; TeX 458). |
| Rectification dimension-free | **VALID** | Fixed-term/operator-norm derivation (`ibid.:389,231`). |
| Charts/polar dimension-free | **VALID** | Fixed two-block norms (`ibid.:390,232-233`). |
| Group/path/derivative dimension-free | **VALID** | Fixed operations/operator norms (`ibid.:391,234-236`). |
| Smooth upgrade dimension-free | **VALID** | Qualitative Lee theorems (`ibid.:392,237-239`). |
| Compactness qualitative | **VALID** | No modulus exported (`ibid.:393,241`). |
| Quotient/orientation/index/phase dimension-free | **VALID** | Fixed \(U(1)\), vertical line, qualitative square root (`ibid.:394,242`). |
| Amplification/block/stage independence | **VALID** | No count or entrywise sum (`ibid.:395,243`). |
| No route-level alarm | **VALID** | Confirmed in §7.2 (`ibid.:396,245-248`). |

### 8.6 V3 §10.6

| v3 §10.6 claim | verdict | exact check |
|---|---|---|
| \(C^1\)-versus-smooth blocker | **VALID** | Rows 9–11 factor the direct repair (`DESIGN-S1-POLAR-v3.md:402,129-131`). |
| Free witnesses/naked formulas | **REFUTED** | Formulas are inline, but row 13 is meta-level (`ibid.:403,132-133`). |
| Group-to-derivative edge | **VALID** | Row 8 imports row 6 (`ibid.:404,128`). |
| TeX 458 use | **VALID** | Named constants only (`ibid.:405`; TeX 458). |
| TeX 560 clarification | **VALID** | Two-stage fixed factors (`ibid.:406,232`). |
| Straight-path inverse guard | **VALID** | Explicit row 7 (`ibid.:407,127`). |
| Full rectification/weak landed contract | **VALID** | In-tree reconstruction (`ibid.:408,121,143`). |
| TeX 692–725 Neumann/right inverse | **VALID** | Explicit proof obligations correctly retain the required derivation (`ibid.:409,144,148-149`). |
| TeX 728–807 smooth repair/factoring | **VALID** | Rows 2–3/9 (`ibid.:410,122-123,129`). |
| TeX 809–843 radii | **VALID** | Row 4 (`ibid.:411,124`). |
| TeX 845–855 mismatch/typo | **VALID** | Smaller domain/non-use (`ibid.:412,124,146`). |
| TeX 857–880 provenance | **VALID** | Corrected row 6 (`ibid.:413,126`; TeX 845–878). |
| TeX 881–893 non-use | **VALID** | Row 8 uses only typed inversion derivative (`ibid.:414,128`). |
| TeX 895–912 path/type repair | **VALID** | Row 7 plus locked definition (`ibid.:415,127`). |
| TeX 943–955 full closure | **VALID-WITH-CORRECTIONS** | Factoring/phase fixed; witness relation still not object-level (`ibid.:416,129-133,169`). |
| Coherence has no free polar witness | **VALID** | Complete polar data universally quantified (`ibid.:417,125`). |
| Derivative target-chart retention | **VALID** | Explicit guard/conclusion (`ibid.:418,128`). |
| Ledger logical closure | **REFUTED** | Row 13 still does not state a mathematical relation (`ibid.:419,133`). |
| Explicit smooth producer factoring | **VALID** | Rows 9–11 (`ibid.:420,129-131`). |
| Witness threading | **REFUTED** | §2 explanation does not cure row-13 meta-contract (`ibid.:421,73-111,133`). |
| Chart row factoring | **VALID** | Rows 2–3 (`ibid.:422,122-123`). |
| Derivative descent/same-chart/determinant/phase | **VALID** | Row 8 plus phase-lifted index row (`ibid.:423,128,169`). |
| Quotient regularity/closedness/orientation | **VALID-WITH-CORRECTIONS** | Factored deps correct; row-13 rewire remains (`ibid.:424,166`). |
| Left inversion operations/witnesses | **VALID-WITH-CORRECTIONS** | Operations fixed; witness root not (`ibid.:425,168`). |
| Smooth manifold/triangulation/local index/phase | **VALID-WITH-CORRECTIONS** | Smooth/phase interfaces exist; upstream tuple still blocked (`ibid.:426,166-169`). |
| Maximal-simplex placement | **VALID** | Row 170 (`ibid.:427,170`). |
| Qualified \(\phi_V\) | **VALID** | Definition text unchanged (`ibid.:428,254`). |
| Controlled rectification reconstruction | **VALID** | Row 1 (`ibid.:429,121,143`). |
| Straight-path gap | **VALID** | Row 7 (`ibid.:430,127,149`). |
| Source-radius mismatch | **VALID** | Row 4 (`ibid.:431,124`). |
| Derivative typing | **VALID** | Row 8 (`ibid.:432,128`). |
| No numerical polar constants | **VALID** | Named values only (`ibid.:433`; TeX 458). |
| Bundled smoothness/witness/edge repair | **REFUTED** | Smoothness and edge are fixed; witness relation is not (`ibid.:434,129-133`). |
| Direct-sum/operator norm | **VALID** | Fixed-factor accounting (`ibid.:435,232`; TeX 554–560). |
| Qualitative smooth upgrade | **VALID** | Rows 9–10 (`ibid.:436,129-130`). |
| Expand every rectified axiom | **VALID** | Row 1 feasibility list (`ibid.:437,143`). |
| Qualify \(\phi_V\) | **VALID** | Definition row (`ibid.:438,254`). |
| Complete fixed-class plan/phase | **VALID-WITH-CORRECTIONS** | Phase and ten deps are present; row-13 upstream remains (`ibid.:439,193-222`). |
| Separate scalar arithmetic from witness join | **REFUTED** | Row 12 succeeds, but the disposition claims a successful separation-and-join repair and row 13 fails (`ibid.:440,132-133`). |
| Factor graph/MC and smooth interfaces | **VALID** | Five rows 2–3,9–11 (`ibid.:441`). |
| Export actual common-witness relation | **REFUTED** | Text substitution is not an object relation (`ibid.:442,133`). |
| Add quotient phase-lift | **VALID** | Contract and ledger (`ibid.:443,169,198`). |
| Correct group and rectification provenance | **VALID** | Rows 1/6 and §4 (`ibid.:444,121,126,143,148`). |
| Do not land v2; redesign/re-audit | **VALID** | V3 stayed design-only and requested this audit (`ibid.:445,457-459`). |

## 9. Required redesign before landing

1. Replace row 13 with the explicit object-level common-witness conjunction in
   §0.1, or use consumer-local option (b). Do not mention contract text,
   textual substitution, “the full conclusion,” or another row's unspecified
   formula.
2. Re-project that actual root and factor it if it exceeds 12 nodes or depth 3.
3. Rewire the four row-13-dependent downstream interfaces to the repaired id.
4. Add explicit `defs` metadata to all six downstream proposals as specified in
   §0.2.
5. Re-audit only those repairs. Do not alter the verified scalar arithmetic,
   direct-smoothness route, retained contracts, two definition contents,
   corrected group provenance, or phase-lift.

There is no **NOT IN LOCAL REFS** escalation and no **ROUTE-ALARM**. The
correct decision is nevertheless:

**DO NOT LAND OR SEED THE v3 TABLE. REDESIGN ROW 13, COMPLETE DOWNSTREAM
METADATA, THEN RE-AUDIT.**
