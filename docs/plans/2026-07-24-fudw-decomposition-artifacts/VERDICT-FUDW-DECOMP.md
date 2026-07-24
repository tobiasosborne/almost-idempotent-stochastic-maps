VERDICT: INVALID

# Hostile architecture review — aism-fudw decomposition

The proposed factorization is not safe to transcribe or seed.  Several local
contracts are faithful, and the status ceiling is mostly honest, but the design
does not yet form a closed af dependency graph.  In particular, it omits the
sanctioned COMP-CB input used throughout H-CB, hides two semantic cycles behind
contract shorthand, and assigns one af root each to the still-unfactored
MAIN-CB structural assembly and Route-F stochastic-retract assembly.

## 1. Coverage — INVALID

### 1.1 Missing COMP-CB subtree — BLOCKER

**Exact design locus:** rows 47--60, especially
`lem-hcb-column-hilbert-squared` (line 47),
`lem-hcb0-compressed-associator` (line 48),
`lem-hcb3-diagonal-unit` (line 53), and
`lem-hcb4-canonical-gram` (line 58); assembly claim at lines 154--157.

The verified H-CB artifact does not prove these results from definitions alone.
It explicitly imports the sanctioned COMP-CB estimates at
`PROOF-W74F-E-HCB.md:75-109`; HCB-0 uses them five times, the unit estimate uses
the compressed-unit action, and the Gram estimate uses the compressed-product
and compressed-unit norm estimates.  Corrected COL-HILB in
`DECOMP-W74F-C-THMAINEXT.md:609-655` also imports COMP-CB.  No proposed result
shard carries any of those contracts, and the affected rows have empty or
insufficient dependency lists.  The claimed transitive closure at lines
154--157 therefore starts from unregistered premises.

**Exact correction:** add the five COMP-CB rows in Registry impact §A and apply
the dependency replacements there for
`lem-hcb-column-hilbert-squared`, `lem-hcb0-compressed-associator`,
`lem-hcb3-diagonal-unit`, `lem-hcb4-canonical-gram`, and
`lem-stage1-old-side-compression`.  Do not duplicate a fresh proof of COMP-CB
inside every H-CB workspace.

### 1.2 MAIN-CB structural assembly is absent — BLOCKER

**Exact design locus:** `lem-maincb-uniform-reset-chain` (line 115);
`lem-thmainext-conditional` wiring and projection (lines 173--184).

Line 115 carries only the numerical reset invariant.  It does not carry the
qualitative three-stage construction in
`DECOMP-W74F-C-THMAINEXT.md:546-589`: level-one termination, the maximal
commutative selection, the Stage-2 extension walk, the Stage-3 binary
recombination, preservation of bijectivity, or the single-level-one-map
invariant.  Those clauses are necessary to obtain the parent's existential
isomorphism.  Calling the parent “root plus seven imports, 8 nodes / depth 2”
silently assigns the entire construction to one af node.

**Exact correction:** add the deliberately `stated`
`lem-maincb-structural-assembly` row in Registry impact §A, add it to the
replacement `lem-thmainext-conditional` dependency list, and give it its own
prover/verifier pass.  A more detailed architect may split that row further; it
must not be silently proved inside the parent root.

### 1.3 The Route-F finish lacks the stochastic-retract interface — BLOCKER

**Exact design locus:** `lem-routef-prh-finish` (line 138);
`lem-routef-k-ledger` wiring and projection (lines 186--201).

The three UCP estimates do not, by themselves, match `lem-prh`.  PRH requires
positive unital maps \(A,M\).  Row 138 omits those hypotheses and merely assumes
the two norm bounds.  Nor does any preceding proposed row state the
stochastic-compression implication that produces those \(A,M\) and the bound
\(3K\eta/(1-3K\eta)\).  `LEDGER-W74F-G-K.md:457-475` calls that implication
“already hostile-checked” but does not factor its statement.  Thus the union of
the proposed contracts does not reconstruct the final clause of
`lem-routef-k-ledger`.

**Exact correction:** use the replacement `lem-routef-prh-finish` contract in
Registry impact §B.  In addition, the stochastic-retract bridge must be
extracted as its own row from
the W73 F2/F3 material before this parent is seeded.  The four artifacts
permitted by this review do not contain a sufficiently explicit closed
hypothesis block from which I can write a safe ready-to-paste bridge contract;
this is a named **GAP**, not permission to invent one.  Replace the 7/2 parent
projection by `REFACTOR / BLOCKED ON F2-F3 BRIDGE`.

## 2. Faithfulness — INVALID

### 2.1 False top-cohomology hypothesis — MAJOR

**Exact design locus:** `lem-topology-orientable-top-cohomology` (line 95).

The title says “closed”, but the contract assumes only “connected compact
orientable \(d\)-manifold”.  If manifolds with boundary are allowed, the
statement is false (for example, a compact interval has zero top cohomology).

**Exact correction text:** use the replacement
`lem-topology-orientable-top-cohomology` contract in Registry impact §B, which
says “compact orientable \(d\)-manifold **without boundary**”.

### 2.2 Positive-dimensional quotient lacks its hypothesis — MAJOR

**Exact design locus:** `lem-stage1-quotient-manifold-package` (line 105).

The verified Stage-1 packet assumes \(\dim\mathcal X>1\) at
`PROOF-W74F-H-STAGE1.md:17-29`.  Without that condition the quotient need not be
positive-dimensional.  The proposed contract drops the hypothesis.

**Exact correction:** the replacement
`lem-stage1-quotient-manifold-package` contract adds
\(1<\dim\mathcal X<\infty\) and separates the finite-CW conclusion into the new
`lem-stage1-quotient-finite-cw` row.

### 2.3 Four Stage-1 contracts drop their smallness/admissibility clauses — MAJOR

**Exact design locus:** `lem-stage1-original-complementary-pair` (line 110),
`lem-stage1-old-side-compression` (line 112),
`lem-maincb-error-improvement` (line 114), and
`lem-maincb-uniform-reset-chain` (line 115).

Lines 110 and 112 introduce positive thresholds but never assume the relevant
defect is below them.  Line 114 replaces the source's explicit
\(\delta\le\delta_{\max}^{\rm cb}\) premise by the undefined word
“admissible”.  Line 115 states the reset bounds without the common input-radius
guard.  Each contract is stronger than the verified artifact.

**Exact correction:** use the replacement contracts in Registry impact §B for
`lem-stage1-original-complementary-pair`,
`lem-stage1-old-side-compression`, `lem-maincb-error-improvement`, and
`lem-maincb-uniform-reset-chain`.

### 2.4 Several ledger inequalities lose their common small-\(\eta\) range — MAJOR

**Exact design locus:** `lem-routef-delta-phi-product` (line 130) and the three
telescope rows (lines 133--135).

The G-ledger first chooses \(\eta_A\) as a positive common linearization radius
for the finite source chain (`LEDGER-W74F-G-K.md:61-75`).  The proposed rows
state their inequalities without any range hypothesis.  That is a semantic
strengthening.

**Exact correction:** name \(\eta_A\) in
`lem-routef-ai-defect-linearization` and add \(0\le\eta\le\eta_A\) to the four
replacement ledger contracts in Registry impact §B.

### 2.5 PRH hypotheses are incomplete — BLOCKER

**Exact design locus:** `lem-routef-prh-finish` (line 138).

The conclusion is not implied by the four displayed numerical hypotheses
unless \(A\) and \(M\) are positive unital maps.  That requirement is literal
in the af-validated `lem-prh` contract.

**Exact correction:** use the replacement `lem-routef-prh-finish` contract in
Registry impact §B.

## 3. Contract hygiene — INVALID

### 3.1 The Stage-1 two-side packet is compound and circular — BLOCKER

**Exact design locus:** `lem-stage1-two-side-packet` (line 113), its use in
`lem-maincb-uniform-reset-chain` (line 115), and its seeding order
(lines 317--324).

The row bundles three independent claims: the old-side bound, the fresh-side
bound, and “MAIN-CB supplies” the comparison
\(\varepsilon_S\le C_{\rm co}(1+c_0^{\rm cb})\varepsilon_0\).  The first two
already have their own rows.  The third belongs to MAIN-CB, while MAIN-CB is
declared to depend on this packet.  This is exactly the kind of compound glue
contract that the campaign says drives af to STUCK.

**Exact correction:** delete this row; add only the atomic
`lem-maincb-split-corner-defect` comparison from Registry impact §A, and use the
replacement dependency lists for `lem-maincb-uniform-reset-chain` and
`lem-thmainext-conditional`.  No wrapper packet is needed.

### 3.2 EXT-CB children use parent-contract shorthand — MAJOR

**Exact design locus:** lines 77--80, each saying “under the hypotheses of
`conj-extcb`”.

A child contract may not use its parent theorem as the name of a hypothesis
block.  It is neither a definition nor an af external available at that phase.
The wording also makes the child contract non-self-contained.

**Exact correction:** provision `def-extcb-datum` in Definition impact §C and
use the closed replacement contracts for the four affected EXT-CB children in
Registry impact §B.

### 3.3 Two proposed “packets” enumerate independent goals — MAJOR

**Exact design locus:** `lem-extcb4-complete-merging-datum` (line 82) and
`lem-stage1-quotient-manifold-package` (line 105); attempted justification at
risk R13 (line 371).

The merging row repeats four independent conditions even though a proposed
datum definition exists.  The quotient row combines manifold classification,
connectedness, compactness, positive dimension, orientability, and finite CW
type.  Calling these “classification statements” does not reduce the number of
af goals.

**Exact correction:** the replacement
`lem-extcb4-complete-merging-datum` references the datum instead of
enumerating it.  The replacement `lem-stage1-quotient-manifold-package` plus
the new `lem-stage1-quotient-finite-cw` row split the quotient classification
from the finite-CW consequence.

### 3.4 Threshold contract is an unclosed symbol dump — MAJOR

**Exact design locus:** `lem-routef-threshold-minimum` (line 137).

The contract uses \(C_3\), \(C_E\), \(C_T\), \(\eta_A\), and several radii
without a contract that fixes all of them.  \(C_3\) occurs nowhere else in the
proposal table.  Positivity of a displayed minimum is not the useful
interface: downstream needs the implication that all local guards hold.

**Exact correction:** the replacement `lem-routef-threshold-minimum` contract
in Registry impact §B gives the common-guard interface.  The explicit minimum
remains in the shard body and
provenance; before seeding, its symbols must be supplied by atomic upstream
constant/estimate rows.  If the af prover cannot keep that proof within the
envelope, factor the \(C_2,C_3\) packet rather than re-expanding the root.

## 4. DAG soundness — INVALID

### 4.1 Hidden EXT-CB parent/child cycle — BLOCKER

**Exact design locus:** child rows 77--80 and parent dependency list
165--166.

Mechanically the proposed `deps:` fields are acyclic, but semantically each
child imports “the hypotheses of `conj-extcb`”, while `conj-extcb` imports the
children.  The linker cannot detect this prose cycle.

**Exact correction:** use `def-extcb-datum` and the four replacement EXT-CB
child contracts in Registry impact §§B and D.  No child may mention
`conj-extcb`.

### 4.2 Hidden Stage-1/MAIN-CB cycle — BLOCKER

**Exact design locus:** line 113 (“MAIN-CB supplies ...”), line 115
(`lem-maincb-uniform-reset-chain` depends on that row).

**Exact correction:** delete line-113's row and use the atomic
`lem-maincb-split-corner-defect` plus the replacement
`lem-maincb-uniform-reset-chain` dependencies.

### 4.3 Dangling mathematical imports despite resolved ids — BLOCKER

**Exact design locus:** lines 47--60.

The H-CB rows consume COMP-CB without declaring it.  This is a mathematical
dangling import even though every written id would resolve.

**Exact correction:** use the new COMP-CB rows and the affected replacement
dependency lists in Registry impact §§A--B.

After these repairs I found no further phase-order cycle in the written
dependency lists.  In particular, H-CB precedes EXT-CB, EXT-CB precedes
Stage 1/MAIN-CB, and the corrected ledger order is forward.

## 5. Envelope realism — INVALID

### 5.1 Parent projections count imports, not proof structure — BLOCKER

**Exact design locus:** parent projections 154--157, 168--171, 182--184,
195--201.

The 10/2 H-CB and 9/2 EXT-CB assembly estimates are plausible only after the
missing inputs are externalized.  The 8/2 MAIN-CB and 7/2 Route-F ledger
estimates are not credible: they allocate one root node to the entire
three-stage structural construction and one root node to the complete
factorization-to-stochastic-retract bridge.

**Exact correction text:** replace the MAIN-CB projection by
`REFACTOR: structural assembly not yet af-sized; seed only after lem-maincb-structural-assembly is validated`,
and replace the Route-F parent projection by
`REFACTOR / BLOCKED ON F2-F3 STOCHASTIC-RETRACT BRIDGE`.

### 5.2 Three near-envelope leaves are materially optimistic — MAJOR

**Exact design locus:** `lem-extcb-exact-target-approximation` (line 74,
9/3), `lem-stage1-uniform-inversion-isolation` (line 104, 9/3), and
`lem-stage1-left-inversion-trace` (line 107, 9/3); risk R12 (line 370).

The first hides the Newton/diagonal argument; the second spans the quantitative
inverse-function, polar-chart, derivative, and isolation machinery; the third
spans the Künneth, Hopf-structure, augmentation-filtration, and trace argument.
The source sections are far longer than nine atomic steps.  Marking an estimate
“9/3” does not make it credible.

**Exact correction text:** set each projected-af cell to
`REFACTOR BEFORE SEEDING (no credible <=12/3 projection yet)`.  For the
isolation row, first separate the polar-chart/derivative result from local
fixed-point isolation.  No safe exact polar-chart contract can be transcribed
from this design alone; a fresh factoring pass over the verified Stage-1
artifact is required.

## 6. Definition provisioning — INVALID

### 6.1 Substantive Stage-1 results are hidden inside a definition — BLOCKER

**Exact design locus:** proposed `def-approximate-unitary-space` (line 232),
Stage-1 rows 103--104, and external-input claim at line 252.

The existence and differentiability of the polar retraction and the uniform
chart/derivative estimates are results (`prop_polar` and the quantitative
inverse-function machinery), not vocabulary.  Row 104 depends only on a
definition and exact-unit rectification, so it has no result import carrying
those facts.  Line 252 says the Banach inverse-function estimate is represented
by “internal Stage-1 proposal nodes”, but no such proposal node exists.

**Exact correction:** the `def-approximate-unitary-space` entry in Definition
impact §C restricts the definition to notation and changes it to a
project-adopted draft.  Before seeding row 104, add separately reviewed
result shards for quantitative inverse-function control and polar-chart
control.  Their exact contracts require a new faithful factoring pass; inventing
them here would violate the brief's gap-honesty requirement.

### 6.2 Two proposed cited definitions are project-created composites — MAJOR

**Exact design locus:** `def-four-corner-merging-datum` (line 228) and
`def-canonical-corner-system` (line 231).

The source states four hypotheses of `lem_merging`; it does not define a term
“amplified four-corner merging datum”.  Likewise line 1404 defines the spatial
\(\mu_{jk}\) construction but does not define the HCB artifact's canonical
\(J\)-identifications, and the proposed shard conflates those two concepts.
Neither composite can be locked as `cited`.

**Exact correction:** the Definition impact table changes the merging datum to
`original / draft` and splits the canonical \(J\)-identifications from the
spatial four-corner system; all three project names are `original / draft`
pending sign-off.

### 6.3 Ledger vocabulary has no producer — MAJOR

**Exact design locus:** threshold row 137.

\(C_3\) is not produced by any proposed result or definition, and the row also
uses several symbols only informally introduced elsewhere.  This fails the
no-naked-symbol rule even before af seeding.

**Exact correction:** the replacement
`lem-routef-ai-defect-linearization` explicitly names \(C_A,\eta_A\), and the
replacement `lem-routef-threshold-minimum` uses the upstream guard interface.
The shard body must keep the verified explicit formula and point each symbol to
its producing dependency.  If \(C_3\) remains in the root contract, a separate
degree-three estimate row is mandatory.

### 6.4 What passed

The proposed cited definitions for the base \(\varepsilon\)-\(C^*\)-algebra,
\(\delta\)-projection, one-dimensional projection/equivalence, compressed
corner/product, operator space, projection basis, H-space/left inversion, and
Lefschetz/index data have genuine definition loci in the pinned source.  The
proposed extended-inclusion harmonization is correctly kept
`consensus / draft`.  The seven topology theorem rows are honestly only
`cited candidate` and are correctly blocked on acquisition and byte matching;
the Hopf-structure row must remain blocked until its non-coassociative
hypothesis match is settled.

## 7. Status law — INVALID

### 7.1 Glue promoted to `proved-mod-audit` — BLOCKER

**Exact design locus:** `lem-stage1-two-side-packet` (line 113).

This is new assembly glue, not a faithful atomic transcription of a verified
section, yet it is labelled `proved-mod-audit`.  It also contains the circular
MAIN-CB conclusion identified above.

**Exact correction:** delete it.  The verified atomic old-side, fresh-side, and
split-corner-defect statements may remain `proved-mod-audit`; any newly phrased
structural glue such as `lem-maincb-structural-assembly` starts `stated`.

### 7.2 What passed

No proposed result is labelled above `proved-mod-audit`; the five EXT-CB source
premises and IMPROVE-CB are honestly `stated`; and the topology leaves are not
to become `cited` before local source acquisition and byte matching.  Those
status choices are correct.

## 8. Gap honesty — INVALID

### 8.1 “No new glue” and “fully assigned” are false — BLOCKER

**Exact design locus:** closure claims 36--39 and 382--388; risk R13
(line 371).

The design invents the circular two-side glue, omits the COMP-CB contracts,
hides polar/IFT results in a definition, leaves the MAIN-CB structural
construction inside one root, and does not factor the stochastic-retract
bridge needed by the ledger parent.  Therefore the claims “No new mathematical
glue statement is introduced”, “fully assigned”, and “There is no invented
proof” are not supported.

**Exact correction text for the design's future closure paragraph:**

> This proposal is not yet seedable.  The verified H-CB sections require an
> explicit COMP-CB subtree; the Stage-1 analytic packet still requires a
> separate polar-chart/inverse-function factoring pass; MAIN-CB requires a
> structural-assembly shard; and the Route-F ledger parent is blocked on an
> explicit stochastic-retract bridge from the F2/F3 material.  These are named
> architecture gaps.  No parent is to be seeded until they have closed
> contracts, honest statuses, and a fresh hostile architecture review.

# Registry impact

The following are the only safe mechanical row changes supported by the
permitted verified packets.  They are not authorization to transcribe the rest
of the design: the polar-chart and F2/F3 bridge gaps above still block seeding.

## A. New result rows

| proposed id | kind / status | exact `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-compcb-amplified-compression` | lemma / `proved-mod-audit` | Amplified compression identity: for every pair of \(\delta\)-projections \(P,Q\) in an extended \(\varepsilon\)-\(C^*\)-algebra and every \(n\ge1\), \(1_{M_n}\otimes Co_{P,Q}=Co_{I_n\otimes P,I_n\otimes Q}\) and \(M_n\otimes S_{P,Q}=S_{I_n\otimes P,I_n\otimes Q}\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | — | `DECOMP-W74F-C-THMAINEXT.md` COMP-CB, lines 152--183 | 4 / 2 |
| `lem-compcb-rectangular-product` | lemma / `proved-mod-audit` | Uniform rectangular compressed-product estimate: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{co}}\), every compatible amplified rectangular pair satisfies \(\lVert A\mathbin{\cdot}B-AB\rVert\le C_{\mathrm{co}}e\lVert A\rVert\lVert B\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression` | `DECOMP-W74F-C-THMAINEXT.md` COMP-CB; `PROOF-W74F-E-HCB.md` (1.1) | 4 / 2 |
| `lem-compcb-compressed-unit-action` | lemma / `proved-mod-audit` | Uniform compressed-unit action: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{co}}\), every compatible amplified rectangular corner satisfies \(\lVert u_T\mathbin{\cdot}A-A\rVert\le C_{\mathrm{co}}e\lVert A\rVert\) and \(\lVert A\mathbin{\cdot}u_R-A\rVert\le C_{\mathrm{co}}e\lVert A\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression`; `lem-compcb-rectangular-product` | `PROOF-W74F-E-HCB.md` (1.1); `VERDICT-W74F-E-HCB.md` HCB-3 correction | 4 / 2 |
| `lem-compcb-compressed-unit-norm` | lemma / `proved-mod-audit` | Compressed-unit norm estimate: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{co}}\), every \(\delta\)-projection \(T\) satisfies \(\lVert u_T\rVert\le1+C_{\mathrm{co}}e\), and every nonvanishing \(T\) satisfies \(\lvert\lVert u_T\rVert-1\rvert\le C_{\mathrm{co}}e\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression` | `VERDICT-W74F-E-HCB.md:72-83` | 3 / 2 |
| `lem-compcb-single-compression-transfer` | lemma / `proved-mod-audit` | Single-compression transfer: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that restricting an extended \(\alpha\)-inclusion to one ideal and following it by one compatible amplified compression produces an extended \(C_{\mathrm{co}}(\alpha+\varepsilon)\)-inclusion whenever \(\alpha+\varepsilon\le e_{\mathrm{co}}\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression`; `lem-compcb-rectangular-product` | `DECOMP-W74F-C-THMAINEXT.md` COMP-CB; `PROOF-W74F-H-STAGE1.md` SPLIT-C; H-verdict SPLIT-C | 6 / 3 |
| `lem-maincb-split-corner-defect` | lemma / `proved-mod-audit` | MAIN-CB split-corner defect: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{split}}>0\) such that, if \(\varepsilon_0\le e_{\mathrm{split}}\) is the Stage-1 ambient-algebra defect and \(\varepsilon_S\) is the fresh split-corner defect, then \(\varepsilon_S\le C_{\mathrm{co}}(1+c_0^{\mathrm{cb}})\varepsilon_0\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-single-compression-transfer`; `lem-maincb-error-improvement` | `VERDICT-W74F-H-STAGE1.md:187-216` | 4 / 2 |
| `lem-stage1-quotient-finite-cw` | lemma / `proved-mod-audit` | Stage-1 quotient finite-CW consequence: if \(1<\dim\mathcal X<\infty\) and the Stage-1 quotient \(\breve{\mathcal U}\) is a compact \(C^1\) manifold, then \(\breve{\mathcal U}\) has finite CW type. | P:`def-approximate-unitary-space` | `lem-stage1-quotient-manifold-package`; `lem-topology-finite-triangulation` | `PROOF-W74F-H-STAGE1.md` SPLIT-A; H-verdict topological inputs | 3 / 2 |
| `lem-maincb-structural-assembly` | lemma / `stated` | MAIN-CB structural assembly: assuming the Stage-1 split, Stage-2 extension, Stage-3 binary-merge, and immediate-reset interfaces named in its dependencies, the finite three-stage construction terminates and yields a bijective level-one map \(v:\mathcal B\to\mathcal A\) from a finite-dimensional \(C^*\)-algebra \(\mathcal B\), and every all-level map used by the construction is the amplification of its single level-one map. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner` | `conj-extcb`; `lem-extcb-four-corner-merge`; `lem-stage1-fresh-two-point-inclusion`; `lem-stage1-old-side-compression`; `lem-maincb-split-corner-defect`; `lem-maincb-error-improvement`; `lem-maincb-uniform-reset-chain` | proposed glue extracted from `DECOMP-W74F-C-THMAINEXT.md` MAIN-CB; requires its own prover/verifier pass | REFACTOR before seeding |

## B. Replacement result rows

| proposed id | exact replacement `contract:` value | exact replacement `deps:` | other exact change |
|---|---|---|---|
| `lem-hcb-column-hilbert-squared` | unchanged | `lem-compcb-rectangular-product; lem-compcb-compressed-unit-norm` | — |
| `lem-hcb0-compressed-associator` | unchanged | `lem-compcb-rectangular-product` | — |
| `lem-hcb3-diagonal-unit` | unchanged | `lem-hcb1-column-action; lem-compcb-compressed-unit-action` | — |
| `lem-hcb4-canonical-gram` | unchanged | `lem-compcb-rectangular-product; lem-compcb-compressed-unit-norm` | — |
| `lem-stage1-old-side-compression` | Old-side Stage-1 compression: there are universal \(C_{\mathrm{old}}<\infty\) and \(e_{\mathrm{old}}>0\) such that, whenever \(0\le\varepsilon_0\le e_{\mathrm{old}}\), restricting a reset maximal commutative inclusion and applying the single compatible compression into \(S_{P_{[1,m-1]}}\) produces an extended \(C_{\mathrm{old}}\varepsilon_0\)-inclusion; when \(m=1\) this side is absent. | `lem-compcb-single-compression-transfer; lem-maincb-error-improvement` | — |
| `lem-extcb1-cross-corner-dimension` | EXT-CB cross-corner dimension: there is a universal \(e_{\mathrm{sel}}>0\) such that every EXT-CB datum with \(e=\delta+\varepsilon\le e_{\mathrm{sel}}\) satisfies \((\dim S_{P,Q},\dim S_{Q,Q})=(r,1)\). | unchanged | add P:`def-extcb-datum` to `defs:` |
| `lem-extcb2-exact-representation` | EXT-CB exact representation: there are universal \(\kappa<\infty\) and \(e_{\mathrm{rep}}>0\) such that every EXT-CB datum with \(e\le e_{\mathrm{rep}}\) admits one exact unital \(*\)-homomorphism \(\mu_{11}:M_r\to B(S_{P,Q})\) satisfying \(\lVert(\mu_{11})_m-(Ha^Q_{P,P})_m v_m\rVert\le\kappa e\) for every \(m\ge1\). | unchanged | add P:`def-extcb-datum` to `defs:` |
| `lem-extcb2-spatial-corner-system` | EXT-CB spatial corner system: for the datum and exact representation supplied by `lem-extcb2-exact-representation`, \(\mu_{11}\) is implemented by one level-one unitary \(U_1:\mathbb C^r\to S_{P,Q}\), and together with the normalized \(U_2:\mathbb C\to S_{Q,Q}\) it defines one exact spatial four-corner system \(\mu_{jk}\) whose amplifications use \(I_m\otimes U_j\). | unchanged | replace P:`def-canonical-corner-system` by P:`def-spatial-four-corner-system` |
| `lem-extcb3-four-ha-inverses` | EXT-CB four Ha inverses: there are universal \(C_{\mathrm{inv}}<\infty\) and \(e_{\mathrm{inv}}>0\) such that every EXT-CB datum with \(e\le e_{\mathrm{inv}}\) has each \(Ha^Q_{P_j,P_k}\) bijective at level one and, for every amplification, \((1-C_{\mathrm{inv}}e)\lVert Z\rVert\le\lVert(Ha^Q_{P_j,P_k})_m(Z)\rVert\le(1+C_{\mathrm{inv}}e)\lVert Z\rVert\) and \(\lVert((Ha^Q_{P_j,P_k})_m)^{-1}\rVert\le1+C_{\mathrm{inv}}e\). | unchanged | add P:`def-extcb-datum` to `defs:` |
| `lem-topology-orientable-top-cohomology` | Top cohomology of a closed orientable manifold: if \(M\) is a connected compact orientable \(d\)-manifold without boundary, then \(H^d(M;\mathbb R)\ne0\). | unchanged | candidate source still must byte-match this exact hypothesis |
| `lem-stage1-quotient-manifold-package` | Stage-1 quotient manifold: if \(1<\dim\mathcal X<\infty\) and the Stage-1 analytic construction is in its universal validity range, then \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact positive-dimensional orientable \(C^1\) manifold without boundary. | `lem-topology-quotient-manifold` | remove `lem-topology-finite-triangulation`; projected af becomes `REFACTOR BEFORE SEEDING` until polar-chart input is factored |
| `lem-stage1-extra-fixed-class` | unchanged | replace `lem-stage1-quotient-manifold-package` by `lem-stage1-quotient-manifold-package; lem-stage1-quotient-finite-cw` | — |
| `lem-stage1-original-complementary-pair` | Original-product complementary pair: there are universal \(C_{\mathrm{np}}<\infty\) and \(e_{\mathrm{np}}>0\) such that, whenever \(0\le\varepsilon_X\le e_{\mathrm{np}}\), the elements \(P'=P_0\) and \(P''=I_X-P'\) are nonvanishing Hermitian \(C_{\mathrm{np}}\varepsilon_X\)-projections, satisfy \(P'+P''=I_X\), and have both cross-products bounded by \(C_{\mathrm{np}}\varepsilon_X\). | unchanged | shard body must include the verifier's \(e_{\mathrm{nv}}\) term |
| `lem-stage1-two-side-packet` | **DELETE ROW** | — | its only nonduplicate clause moves to `lem-maincb-split-corner-defect` |
| `lem-maincb-error-improvement` | Complete error improvement: there are universal \(\delta_{\max}^{\mathrm{cb}}>0\) and \(c_0^{\mathrm{cb}}<\infty\) such that every extended \(\delta\)-inclusion into an extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\delta\le\delta_{\max}^{\mathrm{cb}}\) can be replaced by one extended \(c_0^{\mathrm{cb}}\varepsilon\)-inclusion, preserving bijectivity. | unchanged | — |
| `lem-maincb-uniform-reset-chain` | MAIN-CB uniform reset invariant: with \(C_{\mathrm{main}}=\max\{C_{\mathrm{co}},C_{\mathrm{split}}\}\), \(L=C_{\mathrm{main}}(1+c_0^{\mathrm{cb}})\), and \(C_{\mathrm{pre}}=2L^2\max\{1,C_{\mathrm{ext}},C_{\mathrm{merge}}\}\), there is a universal \(\varepsilon_E^{\mathrm{corr}}>0\) such that for \(0\le\varepsilon\le\varepsilon_E^{\mathrm{corr}}\) every Stage-1, Stage-2, and Stage-3 raw call satisfies \(\delta_{\mathrm{raw}}\le L^2\varepsilon\) and \(e_{\mathrm{raw}}\le C_{\mathrm{pre}}\varepsilon\), and every extension or merge is followed immediately by an error reset. | `conj-extcb; lem-extcb-four-corner-merge; lem-stage1-fresh-two-point-inclusion; lem-stage1-old-side-compression; lem-maincb-split-corner-defect; lem-maincb-error-improvement; lem-compcb-single-compression-transfer` | projected af: `REFACTOR BEFORE SEEDING` |
| `lem-thmainext-conditional` | unchanged | `conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-uniform-reset-chain; lem-maincb-structural-assembly; lem-extcb-four-corner-merge` | remove `lem-stage1-two-side-packet`; projected parent: `REFACTOR` |
| `lem-routef-ai-defect-linearization` | Approximate-algebra defect linearization: there are universal \(C_A<\infty\) and \(\eta_A>0\) such that, for \(0\le\eta\le\eta_A\), the image of \(\widetilde\Phi\) is an extended \(\varepsilon_{\mathrm{AI}}(\eta)\)-\(C^*\)-algebra with \(\varepsilon_{\mathrm{AI}}(\eta)\le C_A\eta\), where \(C_A=20+\frac{211}{8}C_\theta\). | unchanged | — |
| `lem-routef-delta-phi-product` | Normalized Delta product estimate: for \(0\le\eta\le\eta_A\) and every amplification \(n\), \(\lVert\widetilde\Phi_n(\Delta_n(X)\Delta_n(Y))-\widetilde\Delta_n(XY)\rVert\le(C_2+C_\theta+C_\Delta)\eta\lVert X\rVert\lVert Y\rVert\). | unchanged | \(C_2\) must be linked in the body to its producing repaired Delta estimate |
| `lem-routef-delta-upsilon-telescope` | Delta-Upsilon telescope: for \(0\le\eta\le\eta_A\), \(\lVert\Delta\Upsilon-\Phi\rVert_{\mathrm{cb}}\le(C_\theta+C_\Delta+2C_\Upsilon)\eta\). | unchanged | — |
| `lem-routef-multiplicative-telescope` | Multiplicative telescope: for \(0\le\eta\le\eta_A\) and every amplification \(n\), \(\lVert\Upsilon_n(\Delta_n(X)\Delta_n(Y))-XY\rVert\le[C_\Upsilon+2(C_2+C_\theta+C_\Delta)]\eta\lVert X\rVert\lVert Y\rVert\). | unchanged | — |
| `lem-routef-upsilon-delta-telescope` | Upsilon-Delta telescope: for \(0\le\eta\le\eta_A\), \(\lVert\Upsilon\Delta-I_{\mathcal B}\rVert_{\mathrm{cb}}\le(C_\Upsilon+2C_\Delta)\eta\). | unchanged | — |
| `lem-extcb4-complete-merging-datum` | EXT-CB complete merging datum: the four fixed transported corner maps of `lem-extcb4-transported-corners` satisfy `def-four-corner-merging-datum` at every amplification with common defect \(5(C_H+\kappa)e\). | unchanged | keep P:`def-four-corner-merging-datum` |
| `lem-routef-threshold-minimum` | Route F common threshold: there is a universal \(\eta_K>0\), equal to the finite minimum of the functional-calculus, MAIN-CB, H-CB, EXT-CB, selection, split, CP-normalization, degree-two/three, and PRH guards produced by its dependencies, such that \(0\le\eta\le\eta_K\) implies every local smallness hypothesis in the Route F factorization. | `lem-routef-main-radius-ledger; lem-routef-ai-defect-linearization; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-k-finiteness` | shard body retains the explicit corrected minimum, including \(e_{\mathrm{split}}/(C_{\mathrm{pre}}C_A)\) |
| `lem-routef-prh-finish` | Route F PRH finish: let \(A:\ell_\infty^k\to\ell_\infty^n\) and \(M:\ell_\infty^n\to\ell_\infty^k\) be positive unital maps and let \(Q\) be row-stochastic; if \(K\ge1\), \(0\le\eta\le\min\{(24K)^{-1},1\}\), \(\lVert Q-AM\rVert_{\infty\to\infty}\le K\eta\), and \(\lVert MA-I\rVert_{\infty\to\infty}\le3K\eta/(1-3K\eta)\), then there is a stochastic idempotent \(E\) with \(\lVert Q-E\rVert_{\infty\to\infty}\le(K+4\sqrt{2K})\sqrt\eta\). | `lem-prh; lem-routef-threshold-minimum` | this does not repair the missing upstream stochastic-retract bridge |
| `lem-routef-k-ledger` | unchanged | **DO NOT REWIRE OR SEED** until the F2/F3 stochastic-retract bridge has a closed reviewed row; after that, add it to the direct dependency list in addition to the three telescopes, \(K\), threshold, and finish rows | projected parent: `REFACTOR / BLOCKED` |

## C. Definition proposal impact

| proposed def id | exact correction |
|---|---|
| `def-extcb-datum` | **ADD, `original / draft` pending sign-off.** Canonical datum: an extended \(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\); \(\delta\)-projections \(P,Q\) with \(\lVert P+Q-I\rVert\le\delta\); an extended \(\delta\)-isomorphism \(v:M_r\to S_P\); \(\dim S_Q=1\); and \(S_{P,Q}\ne0\), with \(e=\delta+\varepsilon\). |
| `def-four-corner-merging-datum` | Change `cited / lock after byte-match` to `original / draft pending sign-off`; retain the source hypotheses as provenance. |
| `def-canonical-corner-system` | **DELETE composite proposal.** Replace it by `def-canonical-corner-identifications` (`original / draft`, the HCB \(J_{P,Q,n},J_{Q,P,n}\) maps) and `def-spatial-four-corner-system` (`original / draft`, the \(\mu_{jk}(A)=U_jAU_k^\dagger\) system). |
| `def-approximate-unitary-space` | Change to `consensus / draft pending sign-off` and restrict the statement to the notation \(\mathcal U,\mathcal U_e,u,\sigma\); do not include existence, differentiability, chart bounds, or isolation as definitional facts. |
