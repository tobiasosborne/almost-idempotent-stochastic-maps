# AUDIT — hostile audit of DESIGN-LEDGER-SETTING-RESCOPE

Date: 2026-08-05
Role: fresh hostile auditor
Status: **NON-RIGOROUS AUDIT / DESIGN ONLY / NOTHING PROMOTED**

## 0. Verdict

**DESIGN-REJECTED.**

The byte-only part succeeds: after removing the proposed prefix, all sixteen
contract suffixes equal the landed `contract:` values byte-for-byte.  The
scalar-domain comparison also succeeds:
\(\rho_T\le\rho_{\rm id}^{\rm corr}\), and every later analytic radius and
\(\eta_K\) is at most \(\rho_T\).

The repair nevertheless fails its load-bearing deletion test.  The proposed
Layer-0 definition says that the AI row supplies an extended approximate
algebra and its estimate, and that MAIN therefore furnishes
\((\mathcal B,v)\).  Those are theorem conclusions.  Once they are fields of
an imported definition, a row can “unpack” them after deleting the result
dependencies.  Worse, universal quantification over such data is compatible
with an empty data class: no proposed result proves that every F0 input
produces a datum.  The future strengthened K-ledger therefore cannot
instantiate the re-scoped family from its proposed dependencies.

This is the same laundering shape that the repository's established typed
witness definitions explicitly prohibit.  Compare
`def-maincb-witness-ledger` and `def-stage1-polar-witness-data`: data and
typing live in the definition; existence, inequalities, and analytic witness
relations live in result rows.

All sixteen rows remain `stated`; the two live workspaces remain `seeded`.

## 1. Numbered findings

| no. | severity | locus | finding | required correction |
|---:|---|---|---|---|
| 1 | **BLOCKER** | §1.1 items 1 and 4 | The definition fixes existential theorem witnesses, asserts the AI structure and estimate, and says MAIN furnishes an extended isomorphism.  Deleting AI/MAIN from a consumer still leaves those conclusions available by “unpacking S”. | Replace the shard by a data-and-typing-only input/notation package.  Remove every “furnished/supplies/therefore” clause, every output-existence assertion, and every analytic estimate from Layer 0. |
| 2 | **BLOCKER** | §§1.2, 5.2 | No result proves formation/nonemptiness of `def-routef-raw-factor-setting` for every finite-dimensional UCP/cb input.  Thus `For every ... datum S` silently weakens the original all-input setting and may be vacuous.  The proposed strengthened K-ledger has no dependency capable of producing `S`. | Add a registry formation lemma.  Its quantifier order must choose one global AI/MAIN witness package first and then, for every admissible `(H,Phi,eta)`, furnish `(B,v)` and a setting datum.  Make the strengthened K-ledger depend on that lemma.  Contracts using “furnished by” must import the corresponding producer directly. |
| 3 | **HIGH** | §1.1 item 1; §§2.1, 2.5 | It is unclear whether `eta_A,C_E,epsilon_E` are global choices or fields reselected with each `S`.  If they vary with `S`, the derived `K` varies with the input datum, so row 13's “universal K” is not established. | State the quantifier order in the formation result as `there exists one universal W, such that for every raw input ...`; every row and every successive packet must be over that same `W`. |
| 4 | **HIGH** | §2.1 and prefixes for rows 6--14 | “Furnished for S by ...” and “successive packet” are defined only in design prose, not in a canonical definition or result contract.  Several prefixes name result ids absent from the row's direct `deps:` line. | Either introduce a theorem-free typed serial-packet datum plus explicit producer relations, or add every named provider as a direct dependency.  With the present wording the missing direct edges are: row 7 `+row 5`; row 8 `+row 5`; row 9 `+rows 5,6`; row 10 `+rows 5,8`; row 11 `+rows 5,6,8`; row 12 `+rows 5,8`; row 13 `+rows 5,6,8,9`; row 14 `+rows 5,6,8,9`. |
| 5 | **BLOCKER** | §2.5 row 14 | “The scalar hypotheses of F2/F3/PRH” is not an exported interface of any of those contracts.  F2, F3, and PRH have map/data hypotheses; for an arbitrary raw datum there is no `Q,D,J,Q_C,A,M` and hence no literal sense in which “the PRH finish is admissible.”  Reading only a hidden scalar projection weakens the landed suffix by fiat. | Factor a genuine scalar-threshold lemma that explicitly proves the required inequalities (F2 threshold, `3*K*eta<1`, and the rational retract bound), and leave actual F2/F3/PRH admissibility to the strengthened K-ledger where the F0 and map data are bound.  This requires revising row 14's contract, not merely prefixing its old suffix. |
| 6 | **MEDIUM** | §1.1 item 6; rows 1, D2, 7, D3, 11 | Item 6 types displayed `X,Y,Z` but does not say they are universally quantified.  “Every amplification” binds the level, not the vectors. | State explicitly that every displayed matrix variable is universally quantified over the stated matrix-level domain, or bind those variables in each prefix. |
| 7 | **MEDIUM** | §§3, 4 | Dropping `def-almost-idempotent` is correct, but the continuation plan registers only the new setting definition.  That definition itself invokes `def-ucp-map`; neither live workspace currently has that definition registered. | After the definition is redesigned, provision each referenced canonical definition exactly once in both workspaces, including `def-ucp-map`; keep the already registered extended-algebra/inclusion definitions without duplication. |
| 8 | **LOW** | §1.2; landed row-3 body | The new shard correctly distinguishes the old two-term `rho_id` from the three-term `rho_id^corr`, but the landed row-3 body says later uses of `rho_id` denote the corrected value. | During an authorized landing, reconcile that stale body sentence with the v2 audit: only row 3 uses `rho_id^corr`; later effective domains are unchanged because they also descend from `rho_T`. |

## 2. Mandatory attacks

### Attack 1 — deletion test on the definition

**VERDICT: FAILED / KILL.**  Items 1 and 4 contain theorem content.  In
particular, “furnished together ... by” AI, the displayed
`epsilon_AI <= C_A*eta <= epsilon_E`, and “therefore MAIN furnishes”
`(B,v)` are not data declarations.  The final disclaimer does not undo the
logical import: the proposed continuation explicitly plans to replace proof
steps by “unpack S”.  This is a Layer-0 laundering vector.

The corrected architecture needs two objects:

1. a theorem-free raw-input/notation datum; and
2. a result row proving formation of one coherent factor datum from the AI
   and MAIN contracts, with the global-before-input quantifier order.

### Attack 2 — byte-suffix check, all sixteen rows

**VERDICT: CLEARED.**  An ordered extraction of the sixteen proposed
`contract:` lines, stripping through the final binder colon, had an empty
`diff -u` against the landed contracts in this order:

`raw-factor-norms`, `raw-factor-units`, `raw-factor-identities`,
`raw-product-estimate`, `delta-prime-closeness`,
`delta-normalization-closeness`, `degree-two-estimate`,
`delta-phi-product`, `degree-three-estimate`,
`upsilon-prime-closeness`, `upsilon-normalization-closeness`,
`delta-upsilon-telescope`, `multiplicative-telescope`,
`upsilon-delta-telescope`, `k-finiteness`, `threshold-minimum`.

There is zero suffix drift: constants, spaces, apostrophes, brackets,
`rho_id^corr`, `I_B`, and `infinity` spelling all match.

### Attack 3 — binding adequacy, row by row

**VERDICT: NOT-CLEARED.**  The radius arithmetic is sound, but binding is
not.

| row | binding verdict |
|---|---|
| 1 | `S` would type the raw maps, but obtains them by the finding-1 theorem import; `X` is not explicitly universal. |
| 2 | Unit types are supplied, conditional on the invalid factor datum. |
| 3 | `rho_AI := eta_A`, all map names, and the corrected radius are supplied; `B,v` and their existence are laundered through `S`. |
| 4 | Amplification and `X,Y` are explicit in the suffix; the raw factor still comes from the invalid datum. |
| 5 | The diagonal and CP vocabulary are present; the required factor/involution package is still inherited through the invalid datum. |
| 6 | `Delta'` is related only by the noncanonical “furnished” phrase; the pointwise `X` convention is implicit. |
| D2 | The pair is named and the radius is below `rho_T`, but “successive” is not a registered relation and `X,Y` are not explicitly universal. |
| 7 | Same pair issue; row 5 is named but absent from direct deps; `X,Y` remain implicit. |
| D3 | Pair and radius order are otherwise adequate; `X,Y,Z` remain implicit. |
| 8 | The same `Delta` is intended, but row 5 is a named non-direct import; the Choi construction is meaningful only after the serial relation is formalized. |
| 9 | The matching `Upsilon'` is intended; rows 5 and 6 are named non-direct imports; pointwise `X` is implicit. |
| 10 | The packet intends the same maps, but rows 5 and 8 are named non-direct imports. |
| 11 | The packet intends the same maps, but rows 5, 6, and 8 are named non-direct imports; `X,Y` are implicit. |
| 12 | Rows 5 and 8 are named non-direct imports. |
| 13 | Rows 5, 6, 8, and 9 are named non-direct imports; universality of `K` also fails unless the witness constants are globally fixed. |
| 14 | The same four direct imports are missing, and the alleged scalar F2/F3/PRH interface does not exist. |

The domain subcheck itself is **CLEARED**:
`rho_T <= rho_id^corr`; rows 2, 4, and 5 are on `rho_T`; every later
normalization/degree/telescope radius contains or descends from `rho_T`; and
`eta_K <= rho_fac <= rho_2 <= rho_T`.  No row's stated radius exceeds the
proposed datum domain.

### Attack 4 — hidden narrowing / hidden strengthening

**VERDICT: FAILED BOTH WAYS.**  Narrowing occurs because the old ambient
all-input statement becomes universal only over possibly nonexistent data.
Strengthening occurs because the definition grants AI structure, a defect
estimate, and a MAIN isomorphism as primitive fields.  The fact that all
analytic row radii lie below the datum radius does not cure either defect.

### Attack 5 — `defs:` lines

**VERDICT: PARTLY CLEARED, OVERALL NOT-CLEARED.**  Removing
`def-almost-idempotent` from all sixteen rows is right: it is the real
row-stochastic/infinity-norm picture.  The retained direct definitions for
the diagonal, CP/UCP, stochastic, and PRH vocabulary are reasonable.

The replacement definition is not acceptable until findings 1--3 are
repaired.  In addition, textual provider imports belong in `deps:`, not
`defs:`; finding 4 lists the missing edges.  The live af workspaces also need
the transitive canonical vocabulary noted in finding 7.

### Attack 6 — af continuation plan

**VERDICT: MECHANICS CLEARED; PROPOSED CONTINUATION NOT-CLEARED.**  With af
0.1.6, empirical tests on temporary copies confirmed:

- amending pending root `1` changed the root JSON but left validated child
  `1.1` byte-identical and validated; and
- amending pending interior node `1.1` left validated descendant `1.1.2`
  byte-identical and validated.

The binary rejects amendment of validated nodes, exactly as the design says.
Thus mechanical preservation is real, not assumed.  It does not validate a
new ancestor, and the design correctly requires fresh bottom-up review.

The 20-node/six-round row-1 allowance and 5-or-6-node/two-round row-3
allowance are plausible for the current trees.  They are not executable as
specified because several proposed amendments discharge obligations by
unpacking the invalid definition.  After a data-only definition and a
formation result are designed, the amendment list and budget must be
recomputed.  No currently validated child is itself invalidated merely by
adding the missing root context; the unsupported step is formation of that
context.

### Attack 7 — blast radius

**VERDICT: NOT-CLEARED; GUARD CLEARED.**  The existing registry has no
consumer outside the sixteen-row family, as the design says.  The future
strengthened `lem-routef-k-ledger`, however, cannot construct `S`: none of
rows 10--14 asserts existence of a raw setting, and the proposed parent deps
do not include a formation result.  Hence the rescope is not yet
consumption-compatible with the F0 assembly design.

The **DO-NOT-REWIRE guard is untouched and must remain untouched**.  The F0
assembly itself still consumes only the future strengthened K-ledger; its
contract need not change during this redesign.

### Attack 8 — disposition of the design's ten risks

| risk | disposition | reason |
|---:|---|---|
| 1 | **NOT-CLEARED** | Definition-as-theorem laundering and empty-datum vacuity are real (findings 1--2). |
| 2 | **NOT-CLEARED** | Scalar radius ordering is correct, but datum formation is absent; the claimed no-narrowing conclusion therefore fails. |
| 3 | **NOT-CLEARED** | Same-output intent is present, but “furnished/successive” is plan-only vocabulary and direct imports are missing. |
| 4 | **NOT-CLEARED** | Row 14 has no legitimate scalar projection of the F2/F3/PRH contracts. |
| 5 | **NOT-CLEARED** | The global-versus-per-`S` scope of AI/MAIN witnesses is not formalized. |
| 6 | **NOT-CLEARED** | Existing definitions are linked, but theorem conclusions are duplicated into Layer 0. |
| 7 | **CLEARED** | All sixteen suffixes are byte-identical to the landed contracts. |
| 8 | **NOT-CLEARED** | Matrix levels are typed, but displayed vectors are not explicitly universally bound. |
| 9 | **CLEARED** | af preserves child states mechanically and the design does demand new ancestor review. |
| 10 | **NOT-CLEARED** | The guard is respected now, but the advertised future blast omits a formation row, dependency corrections, and vocabulary provisioning. |

### Attack 9 — under-specification hunt

**VERDICT: FAILED.**  Four residual under-specifications remain:

1. no nonvacuous formation theorem for `S`;
2. no global-before-input quantifier order for `eta_A,C_E,epsilon_E`;
3. no canonical meaning or direct import discipline for “furnished” and
   “successive”; and
4. no scalar-only F2/F3/PRH interface for row 14.

The design does intend one fixed `v` inside each `S`, and universal
quantification over compatible later outputs avoids assuming uniqueness.
That part is conceptually sound.  It becomes useful only after formation and
serial-output relations are theorem-level objects rather than prose.

### Attack 10 — linker and gate mechanics

**VERDICT: STRUCTURAL MECHANICS CLEARED; LANDING PACKAGE NOT-CLEARED.**

- The linker compares normalized whitespace only.  Amending each live root
  to the exact proposed one-line registry text would pass contract-match.
- The proposed definition frontmatter is structurally accepted by
  `check-defs`: id/path, `kind: original`, `source: internal`, `sha256: -`,
  and nonempty `consensus:` are schema-correct, and its term/aliases do not
  collide with the current definitions.  Its proposed `status: draft`
  produces the expected warning; an authorized post-ratification landing
  must record the actual sign-off and lock it.
- These gates do not test whether a definition contains a theorem.  Their
  structural acceptance cannot clear finding 1.
- Because findings 2, 4, 5, and 7 require a new result row and dependency or
  contract changes, the advertised prefix/defs/root-only landing is not a
  complete linker-ready package.

## 3. Exact redesign gate

Do not land any part of this design independently.  A replacement design
must, in one auditable package:

1. provide a theorem-free raw-input/notation definition;
2. provide an explicit formation result with one global witness package and
   all required AI/MAIN dependencies;
3. make the same-datum/same-`v`/same-successive-output relation canonical and
   repair every direct dependency edge;
4. replace row 14 by an explicit scalar arithmetic interface, leaving actual
   F2/F3/PRH application to the strengthened K-ledger;
5. bind all amplification variables and matrix-level vectors universally;
6. revise the two af amendment plans and budgets against those corrected
   contracts; and
7. retain the DO-NOT-REWIRE guard and every `stated` status until the normal
   independent elevation protocol completes.

Nothing in this audit promotes a definition, row, af node, parent, or root.
