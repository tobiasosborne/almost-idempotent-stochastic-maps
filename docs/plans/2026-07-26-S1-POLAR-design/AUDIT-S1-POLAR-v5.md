# AUDIT — fresh hostile re-audit of `DESIGN-S1-POLAR-v5.md`

Date: 2026-07-27  
Role: fresh independent hostile auditor; not an author of any S1-POLAR design
or prior audit  
Status: **AUDIT ONLY; NON-RIGOROUS; no status promotion**

## 0. Final disposition

**REDESIGN.**

The critical domain check fails. Row 13's \((A_4)\) produces the polar
diffeomorphism and inverse only for **finite-dimensional** exact-unit
algebras. Its \((A_5),(A_6),(A_7)\) then independently quantify over **every**
exact-unit algebra and refer to “the unique inverse” of that polar map. No
earlier conjunct of row 13 asserts that this inverse exists on the wider
domain. In \((A_7)\), the unique graph map is likewise available from
\((A_2)\) only in finite dimension
(`DESIGN-S1-POLAR-v5.md:142`; base rows at `:124,126,128-130`).

Thus the answer to the brief's critical question is: **the polar inverse comes
from nowhere inside row 13 on the non-finite-dimensional part of the
quantified domain**. A definite description is not an existence theorem, and
variables introduced under \((A_4)\)'s finite-dimensional universal
quantifier do not scope into the independent universal quantifiers of
\((A_5)-(A_7)\). The datum \(W\) cannot repair this: it contains scalars and
typing only, while \(u,h,\mu,\sigma\) are reserved only as partial notation on
domains supplied by result rows (`DESIGN-S1-POLAR-v5.md:270-271`;
`DESIGN-FUDW-DECOMP-v4.1.md:607`).

The defect is not confined to the common ledger. Base producers 6, 7, and 8
already quantify over every exact-unit algebra while importing polar and graph
producers stated only in finite dimension. Helpers 13e--13g inherit, rather
than close, that mismatch (`DESIGN-S1-POLAR-v5.md:124,126,128-130,139-141`).

This is a contract/domain and dependency-closure defect, not evidence of a
route-level mathematical obstruction. The pinned source itself presents the
approximate-unitary discussion for an exact-unit algebra and states the polar
proposition and inverse at TeX 692 and 809--845, so an all-domain producer may
be designable; alternatively every affected consumer in this design is
finite-dimensional. Either repair requires a new audited contract
architecture. Therefore the disposition is **REDESIGN**, not `ROUTE-ALARM`.

## 1. Verdicts on transport helpers 13a--13g

| helper | verdict | hostile check |
|---|---|---|
| 13a `lem-stage1-rectified-cstar-transport` | **VALID** | The domain and rectification conclusion match row 1. The stronger receiving conditions \(C_{\rm rect}\ge C_{\rm rect}^0\) and \(e_{\rm rect}\le e_{\rm rect}^0\) put every input in the base range. Increasing \(\varepsilon_r=C_{\rm rect}\varepsilon_X\) weakens each approximate axiom and both closeness bounds; \(e_{\rm rect}\le1/C_{\rm rect}\) retains the required small range. (`DESIGN-S1-POLAR-v5.md:123,135`; TeX `approximate_algebras.tex:407-440`.) |
| 13b `lem-stage1-unitary-graph-transport` | **VALID** | The domain, graph equation, chart point/cover, uniqueness, and all three estimates match row 2. The receiving guard implies the base guard. Enlarging \(C_{\rm ch}\) weakens the three bounds. In particular the strict conclusion is preserved because \(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\le\tfrac12<1\), not merely because the coefficient grew. (`DESIGN-S1-POLAR-v5.md:124,136`; TeX `:728-793`.) |
| 13c `lem-stage1-maurer-cartan-transport` | **VALID** | It has row 3's finite-dimensional domain and guard, and the family \(g=(g_U)\) is object-level bound by the minimal unique-zero characterization prescribed in audit v4. Only tangent image, trivialization, distortion, and the two equivariance identities occur in the conclusion. Increasing \(C_{\rm ch}\) only enlarges \(1+C_{\rm ch}\varepsilon_r\), while the guard is strengthened. (`DESIGN-S1-POLAR-v5.md:125,137`; `AUDIT-S1-POLAR-v4.md:75-98`.) |
| 13d `lem-stage1-polar-retraction-transport` | **VALID** | The exact image, inverse, and identities are unchanged. With \(D=\varepsilon_r\delta+\delta^2\ge0\), increasing \(C_{\rm pol}\) shrinks the inner tolerance \(\delta-C_{\rm pol}D\) and enlarges the outer tolerance \(\delta+C_{\rm pol}D\); hence both sandwich inclusions weaken in the correct direction. The receiving guard also implies the base guard and keeps the inner radius positive. (`DESIGN-S1-POLAR-v5.md:126,138`; TeX `:809-855`.) |
| 13e `lem-stage1-approximate-group-laws-transport` | **REFUTED** | Its coefficient/margin monotonicity is directionally correct, and all seven identities/estimates are retained. But it quantifies over every exact-unit algebra and then writes \((u_\delta,h_\delta)\) for a unique polar inverse whose existence is supplied nowhere on that domain. Its only direct producer has the same defect, and the actual polar producer is finite-dimensional. (`DESIGN-S1-POLAR-v5.md:126,128,139`.) |
| 13f `lem-stage1-polar-path-transport` | **REFUTED** | Increasing \(C_{\rm path},C_{\rm pol}\) strengthens the guards and enlarges the asserted approximate-unitary tolerance, so the scalar monotonicity is correct. The path nevertheless uses \(u_\delta(Z_t)\) for every exact-unit algebra without an all-domain polar bijectivity result. (`DESIGN-S1-POLAR-v5.md:126,129,140`.) |
| 13g `lem-stage1-inversion-derivative-transport` | **REFUTED** | The five guards are monotone in the claimed direction and the larger \(C_{\rm der}\) weakens the derivative estimate. But both named objects can fail to be defined on the stated domain: \(u_\delta\) comes only from the finite-dimensional polar row, and \(g_{sJ}\) comes only from the finite-dimensional graph row. Its direct producer repeats both unsupported definite descriptions. (`DESIGN-S1-POLAR-v5.md:124,126,130,141`.) |

For 13a--13d, the claimed root/producer-instantiation/monotonicity/assembly
\(4/2\) trees are credible. For 13e--13g, pure monotonicity would also be
atomic **after** a domain-coherent base producer exists, but the current
\(4/2\) projections omit the existence of the maps used in their own
statements (`DESIGN-S1-POLAR-v5.md:104-113,164-170`;
`argument/README.md:43-46,80-81`).

## 2. Row 13, clause by clause

### 2.1 \((A_1)\) — VALID

This is exactly helper 13a's receiving-\(W\) conclusion: the same
finite-dimensional input, range, exact-unit output, normalization, and two
closeness estimates. No map from another clause is referenced
(`DESIGN-S1-POLAR-v5.md:135,142`).

### 2.2 \((A_2)\) — VALID

This is exactly helper 13b's receiving-\(W\) conclusion, including the
finite-dimensional domain, unique graph value, chart point and cover, all
three bounds, and the strict \(<1\) normal-derivative conclusion
(`DESIGN-S1-POLAR-v5.md:136,142`).

### 2.3 \((A_3)\) — VALID

The clause correctly retains the finite-dimensional domain of rows 2 and 3.
It universally binds the \(C^1\) family and identifies it only by the unique
zero equation before stating the tangent/Maurer--Cartan conclusions. That
matches helper 13c and implements the binding correction prescribed by audit
v4 (`DESIGN-S1-POLAR-v5.md:125,137,142`;
`AUDIT-S1-POLAR-v4.md:94-98,221-224`).

### 2.4 \((A_4)\) — VALID

This is exactly helper 13d's finite-dimensional polar conclusion, including
bijectivity, openness, the inverse and its three identities, and both
sandwich radii (`DESIGN-S1-POLAR-v5.md:138,142`). It is also the precise locus
at which row 13's polar existence stops: the quantifier says
finite-dimensional.

### 2.5 \((A_5)\) — REFUTED

The clause does instantiate helper 13e formula-for-formula, but the helper's
formula is not closed on its stated domain. \((A_5)\) starts a new
“for every exact-unit algebra” quantifier and then says “writing
\((u_\delta,h_\delta)\) for the unique inverse.” \((A_4)\) gives such an
inverse only when that algebra is finite-dimensional. There is no bijectivity
hypothesis or affirmative all-domain bijectivity conclusion before the
definition of \(\mu,\sigma\) (`DESIGN-S1-POLAR-v5.md:142`). The seven group
identities and estimates are otherwise faithfully retained.

### 2.6 \((A_6)\) — REFUTED

The path guards and conclusions match helper 13f, but the path
\(H(t,U_0,U_1)=u_\delta(Z_t)\) is defined for every exact-unit algebra by
reference to the same unproduced all-domain inverse. Neither adjacency to
\((A_4)\) nor reuse of the same scalar tuple changes the domain of \((A_4)\)
(`DESIGN-S1-POLAR-v5.md:140,142`).

### 2.7 \((A_7)\) — REFUTED

The clause matches helper 13g and fixes v4's conditional syntax, but an
affirmative definite description is still not an existence proof. On the
non-finite-dimensional part of its domain:

1. no earlier clause makes \(\Pi_\delta\) bijective, so \(u_\delta\) and
   \(\sigma\) are not defined; and
2. no earlier clause supplies the unique \(C^1\) graph \(g_{sJ}\), because
   \((A_2)\) is finite-dimensional.

Consequently \(\chi_s\), \(F_s\), same-chart retention, and the derivative
bound are not well-typed there (`DESIGN-S1-POLAR-v5.md:124,126,141-142`).

### 2.8 \((R)\) — VALID

The four finite-minimum definitions and all ten scalar consequences are
byte-stable from v4 and match row 12 for the same \(W\). The binding v4 audit
already independently validated this arithmetic, and v5 changes none of it
(`DESIGN-S1-POLAR-v4.md:113-114`;
`DESIGN-S1-POLAR-v5.md:134,142`;
`AUDIT-S1-POLAR-v4.md:178-193`).

## 3. Producer-side coherence — REFUTED

The domain mismatch predates the v5 helpers:

- Row 6 quantifies over every exact-unit algebra and uses “the inverse
  \(u_\delta\)” while its polar dependency, row 4, is finite-dimensional.
- Row 7 likewise defines its projected path through \(u_\delta\) on every
  exact-unit algebra while importing only row 4 and the conditional
  coherence row 5.
- Row 8 quantifies over every exact-unit algebra but uses both \(u_\delta\)
  and \(g_{sJ}\); rows 4 and 2 supply those objects only in finite dimension.
  Importing row 6 does not close the gap because row 6 is itself defective.

Loci: `DESIGN-S1-POLAR-v5.md:124,126-130`. Row 5 is not the missing producer:
its universal statement is explicitly conditional on already given polar
data, so it proves coherence/naturality, not existence
(`DESIGN-S1-POLAR-v5.md:127`).

The local TeX does discuss a generic exact-unit algebra at line 692, gives the
polar proposition at 809--843, names its inverse at 845, and then defines the
group operations at 857--878. That is possible provenance for a future
all-domain row, not an import in the present contracts. Registry dependencies
are unconditional proof imports, and a contract must itself be the canonical
closed statement (`argument/README.md:9-16,43-46`).

## 4. Budget — VALID-WITH-CORRECTIONS

Under v5's declared atomic-import convention, the **ledger's own** \(11/3\)
count is credible once its imported helpers are valid:

- root;
- one finite max/min tuple-selection and range node;
- seven helper applications;
- one scalar-arithmetic application;
- one final conjunction assembly.

That is eleven nodes, and the helper layer gives depth three
(`DESIGN-S1-POLAR-v5.md:104-113,142,171`). The eight direct dependencies are
therefore not hidden by the count.

However, the helper budget is not uniformly honest as written. My projection
is:

- 13a--13d: **\(4/2\)**, as claimed;
- 13e--13f: no closed projection until an all-domain polar producer is added
  or their domains are restricted; merely inserting the missing polar
  existence into each current tree adds at least one substantive node;
- 13g: no closed projection until both all-domain polar and graph existence
  are added or its domain is restricted; inserting both locally adds at least
  two substantive nodes.

Thus row 13 may retain the conditional **\(11/3\)** projection after a
producer/domain repair, but v5 cannot use that number to certify the current
architecture. Remeasure the corrected producer/helper rows; do not raise the
\(12/3\) cap (`argument/README.md:80-81`;
`DESIGN-FUDW-DECOMP-v4.1.md:586`).

## 5. Carry-forward integrity, sources, dimension-freeness, and serial order

### 5.1 Carry-forward — VALID

Normalized comparison with v4 found no silent change outside the six declared
repair surfaces:

| protected surface | v4 locus | v5 locus | result |
|---|---:|---:|---|
| rows 1--12 | `:102-113` | `:123-134` | byte-identical |
| six downstream rows | `:146-151` | `:181-186` | byte-identical |
| obligation ledger and ten-id list | `:174-204` | `:209-239` | byte-identical |
| dimension-freeness audit | `:205-230` | `:240-265` | byte-identical |
| definition provisioning | `:231-241` | `:266-276` | byte-identical |
| local-source/hash section | `:21-54` | `:26-59` | byte-identical |

The remaining diffs are the declared clause repairs, helper architecture and
budgets, helper insertion in the serial order, exhaustive v4-audit
disposition, and version wording (`DESIGN-S1-POLAR-v5.md:7-24,60-171,277-414`).
**VALID.**

### 5.2 Source and dimension-freeness — VALID

The three printed hashes recompute exactly:

- Kitaev:
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`;
- Lee:
  `324b7d8b1f70d40eb7608919e3c9cef93628215fa9e9f0816cb4c9549f058b3c`;
- Munkres:
  `9fcbbac92a09926498c1caba8fafa61b1a3568033485b3977edc523cc0459e5d`.

The pinned Kitaev polar/group loci and Lee inverse/implicit-function loci are
stable (`DESIGN-S1-POLAR-v5.md:26-58`; TeX `:692-912`; Lee
`:31134-31137,31286-31298,31330-31344,31374-31385`). There is no **NOT IN
LOCAL REFS** escalation.

The helpers use only finite maxima/minima over seven fixed packages and
monotone changes of universal coefficients. No dimension-dependent constant
is introduced. The all-domain map-existence gap is a quantifier/producer
failure, not a hidden dimension-dependent coefficient
(`DESIGN-S1-POLAR-v5.md:240-261`). **VALID at design level, subject to the
domain redesign.**

### 5.3 Serial order — VALID

The proposed order places rows 1--12 first, then all seven helpers, then row
13, then the downstream consumers. Every helper follows its base producer and
all eight ledger imports precede the ledger. No downstream dependency dangles
and no row consumes a later row (`DESIGN-S1-POLAR-v5.md:282-320`).

This is a valid topological order, not authorization to land the three
refuted producers, helpers, or clauses. If the redesign adds all-domain graph
or polar producer ids, they must be inserted before rows 6--8 and helpers
13e--13g.

## 6. Exact corrections required

Choose and audit one coherent domain architecture:

1. **Finite-dimensional repair (smallest for the stated downstream
   consumers):** restrict base producers 6--8, helpers 13e--13g, and row-13
   clauses \((A_5)-(A_7)\) to finite-dimensional exact-unit algebras. Then
   rows 2 and 4 supply the graph and polar maps on exactly the consumed
   domain.
2. **All-domain repair:** add or widen explicit graph and polar producers
   whose contracts affirm bijectivity/existence and uniqueness for every
   exact-unit algebra under exactly the guards used by rows 6--8. Make rows
   6--8 depend on those producers, then make each helper and each row-13
   clause introduce the maps only after that matching-domain existence
   assertion. A phrase of the form “writing \(u_\delta\) for the unique
   inverse” is insufficient unless the same clause first asserts
   bijectivity or imports an exactly matching producer.

In either repair, preserve the already valid monotonicity directions in
13a--13d, the scalar arithmetic, the byte-stable downstream material, and the
datum-only definitions. Re-project the changed producer/helper trees and keep
the \(12/3\) cap.

**DO NOT LAND OR SEED v5. REDESIGN THE POLAR/GRAPH DOMAIN CLOSURE, THEN RUN A
FRESH HOSTILE AUDIT.**
