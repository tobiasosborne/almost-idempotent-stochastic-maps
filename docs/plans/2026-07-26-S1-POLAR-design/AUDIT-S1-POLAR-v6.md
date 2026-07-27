# AUDIT — fresh hostile re-audit of `DESIGN-S1-POLAR-v6.md`

Date: 2026-07-27  
Role: fresh independent hostile auditor; not an author of any S1-POLAR design
or prior audit  
Status: **AUDIT ONLY; NON-RIGOROUS; no status promotion**

## 0. Final disposition

**LAND**, after the exact non-contract diff-accounting correction in §4 below.
The mathematical v6 repair is landable only through the existing
definition/ratification gate and explicit user ratification. Nothing in this
audit is a proof or a status promotion.

All nine prescribed finite-dimensional insertions are present and coherent.
The polar inverse and graph maps now have matching finite-dimensional
producers under the same guards at every use site. The exhaustive reverse-edge
sweep finds no consumer of rows 6--8 or helpers 13e--13g on a wider domain.
The five analytic downstream rows are explicitly finite-dimensional, and the
sixth is algebra-independent.

The sole finding is documentary: besides the declared surfaces, the diff also
contains three mechanical v5-to-v6 label substitutions. No contract contains
an undeclared word change. The exact correction is to add those three
substitutions to §0's diff accounting; no mathematical contract needs repair.

## 1. Nine insertion sites

| insertion site | verdict | hostile check |
|---|---|---|
| Base row 6 `lem-stage1-approximate-group-laws` | **VALID** | The contract now says “for every finite-dimensional exact-unit” and otherwise matches v5 byte-for-byte (`DESIGN-S1-POLAR-v6.md:153`; v5 `:128`). Its polar guard is exactly \(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\), matching row 4 (`v6:151`). |
| Base row 7 `lem-stage1-polar-path-admissibility` | **VALID** | The finite-dimensional insertion is present and is the only contract change (`v6:154`; v5 `:129`). The same polar guard and the strict path-tolerance inclusion put every \(Z_t\) in row 4's polar domain (`v6:151,154`). |
| Base row 8 `lem-stage1-inversion-derivative-control` | **VALID** | The finite-dimensional insertion is present and is the only contract change (`v6:155`; v5 `:130`). Its graph and polar guards exactly match rows 2 and 4, and its group-domain guard matches row 6 (`v6:149,151,153,155`). |
| Helper 13e `lem-stage1-approximate-group-laws-transport` | **VALID** | The helper now quantifies over every finite-dimensional exact-unit algebra (`v6:164`; v5 `:139`). Its base producer is the identically restricted row 6, and the displayed polar guard is unchanged. |
| Helper 13f `lem-stage1-polar-path-transport` | **VALID** | The helper now has the same finite-dimensional domain as row 7 and retains the same polar/path guards (`v6:165`; v5 `:140`; base at `v6:154`). |
| Helper 13g `lem-stage1-inversion-derivative-transport` | **VALID** | The helper now has the same finite-dimensional domain as row 8 and retains all graph, polar, group, and derivative guards (`v6:166`; v5 `:141`; base at `v6:155`). |
| Row-13 clause \((A_5)\) | **VALID** | Its independent quantifier is now finite-dimensional, matching \((A_4)\), helper 13e, and base row 6 (`v6:164,167`). |
| Row-13 clause \((A_6)\) | **VALID** | Its independent quantifier is now finite-dimensional, matching \((A_4)\), helper 13f, and base row 7 (`v6:165,167`). |
| Row-13 clause \((A_7)\) | **VALID** | Its independent quantifier is now finite-dimensional, matching \((A_2)\), \((A_4)\), helper 13g, and base row 8 (`v6:149,151,155-166,167`). |

The row-13 line contains six occurrences of “finite-dimensional exact-unit”:
the pre-existing \((A_2)\)--\((A_4)\) occurrences and the three new
\((A_5)\)--\((A_7)\) occurrences. Removing only the last three makes the line
byte-identical to v5 (`v5:142`; `v6:167`).

## 2. Definite-description trace — VALID

### 2.1 Polar inverse

Row 4 affirmatively produces the \(C^1\) polar diffeomorphism and its unique
inverse \((u_\delta,h_\delta)\) for every finite-dimensional exact-unit algebra
and every \(\delta>0\) satisfying
\(C_{\rm pol}(\varepsilon_r+\delta)\le\kappa_{\rm pol}\)
(`DESIGN-S1-POLAR-v6.md:151`).

- Row 6, helper 13e, and \((A_5)\) use that inverse only on the same
  finite-dimensional domain and under that identical polar guard; their extra
  inequality is precisely the inner-domain guard needed for products and
  adjoints (`v6:153,164,167`).
- Row 7, helper 13f, and \((A_6)\) use its first component only on the same
  finite-dimensional domain and under the identical polar guard. Their strict
  path tolerance is below row 4's inner radius (`v6:151,154,165,167`).
- Row 8, helper 13g, and \((A_7)\) use its first component only on the same
  finite-dimensional domain, with \(\delta>0\) and the identical polar guard.
  The row-6 group guard supplies the all-\(\mathcal U\) adjoint domain
  (`v6:153,155,166-167`).

Thus every occurrence of \(u_\delta\) or \((u_\delta,h_\delta)\) in the nine
contracts traces to row 4 on a matching domain. No definite description
outlives its producer.

### 2.2 Graph maps and chart coverage

Row 2 produces the unique \(C^1\) maps \(g_V\) and states that their graph
charts cover \(\mathcal U\), for finite-dimensional exact-unit algebras under
\(C_{\rm ch}(\varepsilon_r+\delta)\le\kappa_{\rm ch}\)
(`DESIGN-S1-POLAR-v6.md:149`). For \(s\in\{\pm1\}\), exact unitality makes
\(sJ\in\mathcal U\subseteq\overline{\mathcal U}_\delta\), so row 2 applies
with \(V=sJ\). Row 8, helper 13g, and \((A_7)\) use exactly the same
finite-dimensional domain, the same \(\delta\), the same graph guard, and the
same \(B_{2\delta}\) graph domain (`v6:155,166-167`). Their “same
\(sJ\)-graph chart” language therefore has the required chart producer.

The source-level graph and polar objects are likewise introduced in the one
exact-unit-algebra discussion at TeX `approximate_algebras.tex:692,728-793,
809-855`; this source reading does not enlarge any contract domain.

## 3. Reverse-defect sweep — VALID

The exact-dependency columns give the following exhaustive incoming edges.

| narrowed target | every direct consumer | domain check |
|---|---|---|
| Row 6 | Row 8 (`v6:155`); smooth operations row 11 (`:158`); helper 13e (`:164`); quotient-left-inversion (`:209`) | Row 8, helper 13e, and the downstream row are explicitly finite-dimensional. Row 11 is under rows 9 and 10 as well as row 6; rows 9 and 10 are each explicitly finite-dimensional (`:156-158`), so the intersection of its imported interfaces is not wider than row 6. |
| Row 7 | Helper 13f (`v6:165`); quotient-left-inversion (`:209`) | Both contracts are explicitly finite-dimensional. |
| Row 8 | Helper 13g (`v6:166`); uniform inversion isolation (`:206`); quotient inversion/index data (`:210`) | All three contracts are explicitly finite-dimensional. |
| Helper 13e | Common ledger row 13 (`v6:167`) | Its receiving clause \((A_5)\) is explicitly finite-dimensional. |
| Helper 13f | Common ledger row 13 (`v6:167`) | Its receiving clause \((A_6)\) is explicitly finite-dimensional. |
| Helper 13g | Common ledger row 13 (`v6:167`) | Its receiving clause \((A_7)\) is explicitly finite-dimensional. |

Row 5 is conditional on already supplied polar data and consumes none of the
narrowed rows. Rows 9 and 10 consume graph/polar producers directly and are
already finite-dimensional. Helpers 13a--13d consume none of rows 6--8 or
13e--13g (`v6:152,156-157,160-163`). There is therefore no reverse copy of the
v5 defect.

### 3.1 Six downstream rows

| downstream row | verdict and locus |
|---|---|
| `lem-stage1-uniform-inversion-isolation` | **VALID** — explicitly finite-dimensional (`v6:206`). |
| `lem-stage1-quotient-manifold-package` | **VALID** — explicitly finite-dimensional (`v6:207`). |
| `lem-stage1-quotient-finite-cw` | **VALID** — explicitly finite-dimensional (`v6:208`). |
| `lem-stage1-quotient-left-inversion` | **VALID** — explicitly finite-dimensional and the only downstream row directly importing both rows 6 and 7 (`v6:209`). |
| `lem-stage1-quotient-inversion-index-data` | **VALID** — explicitly finite-dimensional and directly imports row 8 (`v6:210`). |
| `lem-finite-polyhedron-maximal-simplex-placement` | **VALID** — algebra-independent, with no dependencies (`v6:211`). |

### 3.2 Obligation ledger

Each ledger line is also closed on the repaired domain:

- actual isolation and quotient isolation use the finite-dimensional rows at
  `v6:206,210` (`v6:238-239`);
- quotient manifold, finite-CW, H-space/left-inversion, and left-inversion
  trace use the finite-dimensional downstream interfaces or their topological
  consequences (`v6:240-243`);
- maximal-simplex placement is algebra-independent (`v6:244`);
- local index and top cohomology use the finite-dimensional quotient packages
  or their topological consequences (`v6:245-246`).

No obligation-ledger line invokes rows 6--8 on an arbitrary exact-unit
algebra.

## 4. Diff integrity — VALID-WITH-CORRECTIONS (exact)

The contract diff is clean:

- v5 rows 6--8 at `:128-130` versus v6 at `:153-155` differ only by the three
  finite-dimensional insertions;
- v5 helpers 13e--13g at `:139-141` versus v6 at `:164-166` differ only by the
  three insertions;
- v5 row 13 at `:142` versus v6 at `:167` differs only by the three insertions
  in \((A_5)\)--\((A_7)\);
- §§1--2 are byte-identical (`v5:26-114`; `v6:51-139`);
- the feasibility/budget section is byte-identical (`v5:148-172`;
  `v6:173-197`), while §0 and the disposition table reclassify the now-closed
  13e--13g projections;
- §§5--9, including all six downstream contracts and the obligation ledger,
  are byte-identical (`v5:173-321`; `v6:198-346`);
- §0 and the downstream-sweep paragraph are the declared new accounting
  (`v6:7-49`), and the v5-audit disposition table is the declared replacement
  (`v6:347-412`).

There are nevertheless three additional non-contract substitutions not named
in §0's “exact delta” table:

1. “fifth” to “sixth” in the document title (`v5:1`; `v6:1`);
2. “v5 disposition” to “v6 disposition” in §11 (`v5:404`; `v6:416`);
3. “this v5 design” to “this v6 design” in the next-action sentence
   (`v5:412`; `v6:424`).

These are correct mechanical version labels, not mathematical changes, but
the brief requires every extra diff to be a finding. **Exact correction:** add
these three label substitutions to §0's declared diff accounting. Do not
change any contract.

## 5. Provenance — VALID

The Kitaev payload recomputes to
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`,
matching the v6 ledger (`DESIGN-S1-POLAR-v6.md:53-56`).

TeX line 692 fixes one generic exact-unit \(\varepsilon\)-\(C^*\)-algebra for
the entire approximate-unitary discussion. The polar proposition and inverse
are then presented at `approximate_algebras.tex:809-855`; the group maps and
their domains at `:857-878`; the inversion derivative at `:880-892`; and the
projected-path/H-space discussion at `:895-912`. Restricting rows 6--8 from
all exact-unit algebras to finite-dimensional exact-unit algebras claims
strictly less. Their unchanged provenance cells at
`DESIGN-S1-POLAR-v6.md:153-155` therefore remain sane.

This validates only the provenance interface for the proposed weakening. The
rows remain `stated` candidates and nothing here is rigorous.
