# AUDIT — fresh hostile re-audit of `DESIGN-S1-POLAR-v4.md`

Date: 2026-07-27  
Role: fresh independent hostile auditor; not an author of any S1-POLAR design
or prior audit  
Status: **AUDIT ONLY; NON-RIGOROUS; no status promotion**

## 0. Final disposition

**REDESIGN.**

V4 removes the forbidden contract-text phrases, preserves the scalar arithmetic,
adds the six prescribed `defs` lists, and carries the protected v3 material
forward exactly. It nevertheless fails the binding clause-by-clause test.

The highest-value defect is a silent domain weakening in three analytic
clauses. Producers 6, 7, and 8 quantify over **every exact-unit**
\(\varepsilon_r\)-\(C^*\)-algebra; v4's corresponding `(A_6)`, `(A_7)`, and
`(A_8)` quantify only over **finite-dimensional** such algebras
(`DESIGN-S1-POLAR-v4.md:107-109,114`). The group and derivative clauses also
turn affirmative producer conclusions into `if`-conditionals. Those are not
faithful substitutions of \(W\)'s constants.

The Maurer--Cartan and derivative clauses additionally do not bind their graph
and polar maps cleanly. `(A_3)` asserts a grammatically unquantified “the
family” and adds the graph producer's equation and estimates to the
Maurer--Cartan conclusion. `(A_8)` places the polar inverse and the entire graph
package in an antecedent. Bound variables in `(A_2)` and `(A_4)` do not acquire
scope over later conjuncts merely because the conjuncts are adjacent. The
datum-only \(W\) cannot carry those maps
(`DESIGN-S1-POLAR-v4.md:114,236`; `DESIGN-FUDW-DECOMP-v4.1.md:607`).

There is no source failure, dimension-dependent constant, or route-level
mathematical obstruction. This is a contract/binder/factoring failure, so the
disposition is **REDESIGN**, not `ROUTE-ALARM`.

For this audit, \(A_1,\ldots,A_7\) denote the seven producer clauses in the
binding audit's order, corresponding respectively to v4 labels `(A_1)`,
`(A_2)`, `(A_3)`, `(A_4)`, `(A_6)`, `(A_7)`, `(A_8)`.

## 1. Clause-by-clause audit of row 13

### 1.1 \(A_1\): rectified \(C^*\)-control — VALID

The producer requires:

- the same finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra domain and
  \(0\le\varepsilon_X\le e_{\rm rect}\) guard;
- existence on the same involutive normed space of
  \(\boldsymbol\cdot\) and \(J=J^\dagger\);
- every exact-unit \(\varepsilon_r\)-\(C^*\)-axiom, including
  \(\|J\|=1\);
- \(\varepsilon_r=C_{\rm rect}\varepsilon_X\);
- the unit and product closeness estimates.

V4 `(A_1)` contains all of these, with the implicit \(x,y\) quantification made
explicit and no additional mathematical hypothesis
(`DESIGN-S1-POLAR-v4.md:102,114`). **VALID.**

### 1.2 \(A_2\): unitary graph control — VALID

The domains, guard, quantifier order, unique graph value, displayed formula for
\(f_V\), unitary-chart point, chart-covering statement, and all three estimates
are present:

1. the \(g_V+\frac12(V^\dagger\boldsymbol\cdot V-J)\) estimate;
2. the \(Dg_V\) estimate;
3. the normal derivative estimate, including the strict \(<1\).

This matches the graph producer
(`DESIGN-S1-POLAR-v4.md:103,114`; TeX `approximate_algebras.tex:728-793`).
Under the producer's conventional pointwise-unique-function reading, no
conjunct is dropped or added. **VALID.**

### 1.3 \(A_3\): Maurer--Cartan control — REFUTED

The actual Maurer--Cartan producer concludes only:

- the tangent-image formula;
- the global \(C^1\) trivialization and distortion bound
  \(1+C_{\rm ch}\varepsilon_r\);
- \(\omega_{cU}(cZ)=\omega_U(Z)\);
- \(\omega_U(iU)=iJ\).

V4 preserves all four conclusions, but its preamble is not a faithful
object-level binder. It says “and the family of unique graph maps” without an
existential, universal, `let`, or implication binder, then asserts the graph
equation, chart membership, and all three graph estimates as part of the same
clause (`DESIGN-S1-POLAR-v4.md:104,114`). Those assertions are not conclusions
of the row-3 producer. As written they are added conjuncts; at the same time,
the phrase “the family” does not formally introduce a family whose scope
contains the Maurer--Cartan conclusions.

Exact correction: quantify a family \(g=(g_U)_U\) object-level and put the
minimal unique-graph characterization needed to identify the row-2 maps in an
antecedent. Keep only the tangent-image, trivialization/distortion, and two
equivariance identities in the consequent. Do not re-assert the row-2 norm and
normal-derivative conclusions as row-3 conclusions. **REFUTED.**

### 1.4 \(A_4\): polar retraction — VALID

V4 retains the producer's finite-dimensional domain and polar guard, the
\(C^1\) diffeomorphism, the inverse \((u_\delta,h_\delta)\), all three inverse
identities, openness of \(S_\delta\), and both sides of the exact two-radius
sandwich (`DESIGN-S1-POLAR-v4.md:105,114`; TeX
`approximate_algebras.tex:809-855`). Writing
\(S_\delta:=\Pi_\delta(\mathcal U\times B_\delta^\mathcal H(J))\) is merely the
image already specified by “onto \(S_\delta\).” **VALID.**

### 1.5 \(A_5\) (v4 `(A_6)`): approximate group laws — REFUTED

All seven required estimates/identities are present:

1. the two-sided unit identity;
2. \(\sigma(J)=J\);
3. product closeness;
4. adjoint closeness;
5. associativity defect;
6. left-inverse defect;
7. right-inverse defect.

Two logical changes remain:

- the producer says “for every exact-unit
  \(\varepsilon_r\)-\(C^*\)-algebra,” while `(A_6)` inserts
  “finite-dimensional”;
- the producer affirmatively says that the polar inverse defines the global
  \(C^1\) maps, while `(A_6)` says **if** an inverse exists, **then** the maps
  and conclusions follow.

The first weakens the domain; the second adds an antecedent and hence weakens
the conclusion. Adjacency to `(A_4)` does not make this an exact restatement,
and `(A_4)` itself has only the finite-dimensional domain
(`DESIGN-S1-POLAR-v4.md:105,107,114`). Exact correction: use the producer's
full domain and affirmative inverse/map conclusion verbatim with \(W\)'s
constants. **REFUTED.**

### 1.6 \(A_6\) (v4 `(A_7)`): path admissibility — REFUTED

The path clause correctly retains \(q\in[0,1]\), all three path guards,
invertibility of every \(L_{Z_t}\), approximate-unitary membership, joint
continuity, endpoint joining, and scalar equivariance
(`DESIGN-S1-POLAR-v4.md:108,114`).

It nevertheless changes the producer's domain from every exact-unit algebra to
every **finite-dimensional** exact-unit algebra
(`DESIGN-S1-POLAR-v4.md:108,114`). That is a silent weakening. Exact
correction: delete “finite-dimensional” and retain the rest of the producer
quantifiers and conclusion. **REFUTED.**

### 1.7 \(A_7\) (v4 `(A_8)`): inversion derivative — REFUTED

The five quantitative guards, same-chart retention, and
\[
\|D(F_s-\mathrm{id})(A)+2I_{i\mathcal H}\|
 \le C_{\rm der}(\varepsilon_r+r)
\]
are all present (`DESIGN-S1-POLAR-v4.md:109,114`).

The restatement still changes the theorem in three ways:

1. it restricts “every exact-unit algebra” to “every finite-dimensional
   exact-unit algebra”;
2. it changes the producer's affirmative globally defined
   \(\sigma(U)=u_\delta(U^\dagger)\) conclusion into an `if`-conditional on
   \(u_\delta\) being an inverse;
3. it places the graph equation, chart membership, and all three graph
   estimates in that antecedent, although those are imported row-2 facts, not
   row-8 hypotheses or conclusions.

This both weakens the producer by added antecedents and fails to bind the maps
affirmatively. Exact correction: restore the producer's full domain; introduce
the uniquely determined \(u_\delta\), \(g_{sJ}\), \(\chi_s\), and \(\sigma\)
object-level (or quantify them under an explicit dependency antecedent already
guaranteed by the other conjuncts); and leave only chart retention and the
derivative estimate as the row-8 conclusion. **REFUTED.**

### 1.8 \(R\): scalar arithmetic — VALID

`(R)` states all four finite-minimum equations exactly:

1. \(\delta_*\);
2. \(\varepsilon_*^r\);
3. \(e_{\rm S1}\);
4. \(r_{\rm iso}\).

For the same tuple and every \(0\le\varepsilon_X\le e_{\rm S1}\), it defines
\(\varepsilon_r,q,r_-,\eta\) and states all ten inequalities from row 12: both
chart/polar guards, \(q<r_-\), the short-path guard, \(\eta<r_-\), the
derivative guard, chart retention, the lower bound on \(r_-\), the upper bound
on \(\eta\), and the final derivative contraction
(`DESIGN-S1-POLAR-v4.md:113-114`). No scalar conjunct is dropped or added.
**VALID.**

## 2. Meta-language and self-containment

### 2.1 Meta-language sweep — VALID

Inside the mathematical statement of row 13 there is no “the contract of,”
“the conclusion of,” “replacing constants,” “as in row,” other row id, or
unspecified imported conclusion. The four minima and all scalar consequences
are explicit. References to `def-stage1-polar-witness-data` and
`def-epsilon-cstar-algebra` are definition imports, not contract
meta-language (`DESIGN-S1-POLAR-v4.md:114`;
`argument/README.md:9-16,42-46`). **VALID.**

### 2.2 Binder/self-containment sweep — REFUTED

The absence of forbidden prose does not make the statement closed. \(W\) has
fourteen scalar fields and deliberately contains no maps
(`DESIGN-S1-POLAR-v4.md:236`; `DESIGN-FUDW-DECOMP-v4.1.md:375-381,607`).
Nevertheless:

- `(A_3)` refers to “the family” \(g_U\) without a binder;
- `(A_6)` and `(A_8)` bind the polar inverse only as an `if` antecedent;
- `(A_7)` uses \(u_\delta\) by definite reference to an inverse local to a
  different universally quantified conjunct;
- `(A_8)` uses a nested “and if \(\chi_s(A)=\cdots\), then” rather than a
  scoped definition of \(\chi_s\).

Variables quantified inside `(A_2)` or `(A_4)` do not scope over `(A_3)`,
`(A_6)`, `(A_7)`, or `(A_8)`. Each dependent clause must use an explicit
object-level map binder/definition or an explicit implication whose antecedent
identifies the unique imported maps. **REFUTED.**

## 3. Budget honesty — REFUTED

V4 projects row 13 at \(11/3\) and describes those eleven nodes as root, tuple
selection, seven monotonicity transports, arithmetic application, and final
assembly (`DESIGN-S1-POLAR-v4.md:18,114,136`). This is an optimistic list, not
an honest hostile projection:

- the FUDW convention counts a parent together with its direct imported
  results (`DESIGN-FUDW-DECOMP-v4.1.md:286-305`);
- row 13 already has eight direct producer/arithmetic imports
  (`DESIGN-S1-POLAR-v4.md:114`);
- each of seven clauses still needs both a producer instantiation and a
  monotonicity transport unless those are demonstrably closed in one atomic
  node;
- the rewritten \(A_3\) and \(A_7\) map binders add real logical work, not
  typography.

My conservative projection is **18 nodes / depth 4**: root, tuple
selection/range, seven producer instantiations, seven transports, arithmetic,
and conjunction assembly. The most optimistic fusion gives \(11/3\), but it
has no slack and has not been measured against a faithful root. The mechanical
policy is \(>12\) nodes or depth \(>3\) implies refactor
(`argument/README.md:80-81`), and R14 says the polar target remains uncontracted
until reviewed formula-level replacements exist
(`DESIGN-FUDW-DECOMP-v4.1.md:586`).

Exact correction: after repairing the clauses, re-project under one declared
counting convention. If the producer applications and monotonicity arguments
do not each close in one atomic node, factor parameterized transport helpers
that receive the same \(W\); do not split into unrelated existential tuples
and do not raise the cap. **REFUTED.**

## 4. Six downstream `defs` additions — VALID

The lists match binding audit §0.2 exactly:

| downstream row | v4 `defs` verdict |
|---|---|
| `lem-stage1-uniform-inversion-isolation` | `def-epsilon-cstar-algebra`; `def-approximate-unitary-space` — **VALID** |
| `lem-stage1-quotient-manifold-package` | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` — **VALID** |
| `lem-stage1-quotient-finite-cw` | `def-approximate-unitary-space`; `def-epsilon-cstar-algebra` — **VALID** |
| `lem-stage1-quotient-left-inversion` | `def-approximate-unitary-space`; `def-h-space-left-inversion`; `def-epsilon-cstar-algebra` — **VALID** |
| `lem-stage1-quotient-inversion-index-data` | `def-approximate-unitary-space`; `def-lefschetz-fixed-point-data`; `def-epsilon-cstar-algebra` — **VALID** |
| `lem-finite-polyhedron-maximal-simplex-placement` | `none` — **VALID** |

Loci: `AUDIT-S1-POLAR-v3.md:66-85`;
`DESIGN-S1-POLAR-v4.md:144-151`. The six contracts, dependency lists, and
projected budgets are otherwise byte-identical after normalizing away the new
`defs` column (v3 `:165-170`; v4 `:146-151`). **VALID.**

## 5. Carry-forward and source integrity — VALID

The protected carry-forward surfaces are exact:

| surface | compared loci | result |
|---|---|---|
| rows 1--12 | v3 `:121-132`; v4 `:102-113` | byte-identical |
| six downstream contracts/deps/budgets | v3 `:165-170`; v4 `:146-151` | byte-identical after deleting only the new `defs` field |
| obligation ledger and ten-id list | v3 `:193-223`; v4 `:174-204` | byte-identical |
| dimension-freeness audit | v3 `:224-249`; v4 `:205-230` | byte-identical |
| definition provisioning | v3 `:250-260`; v4 `:231-241` | byte-identical |
| genuine serial order | v3 `:261-298`; v4 `:242-279` | byte-identical |
| local-source/hash section | v3 `:39-72`; v4 `:21-54` | byte-identical |

The normalized downstream comparison has the same SHA256 on both sides:
`93d0858b55c118cd3be0e12f876a373aebf0259f9300ae419e870b8427ebbf0d`.
No silent mathematical carry-forward change was found. Editorial changes in
§§0, 2, 4, 10, and 11 describe the declared row-13/metadata repair and version
transition; they do not alter the protected contracts or ledgers. **VALID.**

The three source hashes printed in v4 are exact:

- Kitaev:
  `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`;
- Lee:
  `324b7d8b1f70d40eb7608919e3c9cef93628215fa9e9f0816cb4c9549f058b3c`;
- Munkres:
  `9fcbbac92a09926498c1caba8fafa61b1a3568033485b3977edc523cc0459e5d`.

Spot checks confirm that the pinned interfaces were not perturbed: Kitaev's
axioms and data-independent \(O(\cdot)\) discipline
(`approximate_algebras.tex:407-440,458`), graph/Maurer--Cartan/polar/group/path
and quotient loci (`:692-912,943-955`), Lee C.34/C.36/C.40
(`lee-smooth-manifolds-2ed.txt:31134-31137,31286-31298,31330-31344,31374-31385`),
and the unused Munkres fallback loci
(`munkres-elementary-differential-topology.txt:1509-1514,1596-1637,1833-1840,1888-1901,2055-2056,2533-2558`)
match v4 §1 (`DESIGN-S1-POLAR-v4.md:21-53`). There is no
**NOT IN LOCAL REFS** escalation.

## 6. Required correction before another audit

1. Restore the literal producer domains in the group, path, and derivative
   clauses; do not insert `finite-dimensional`.
2. Replace the unbound/conditional map prose in \(A_3,A_5,A_6,A_7\) by
   explicit object-level binders/definitions or by antecedents that encode
   exactly the imported dependency data already guaranteed by the other
   conjuncts; add no new guard or conclusion.
3. Preserve every already correct estimate and identity in \(A_1,A_2,A_4,R\)
   and every listed conclusion in the other clauses.
4. Re-project the corrected root honestly and factor parameterized
   monotonicity helpers if it exceeds \(12/3\).
5. Preserve the now-correct downstream `defs`, all byte-stable carry-forward
   material, and the design-only/non-rigorous status ceiling.

**DO NOT LAND OR SEED v4. REDESIGN ROW 13, THEN RUN A FRESH HOSTILE AUDIT.**
