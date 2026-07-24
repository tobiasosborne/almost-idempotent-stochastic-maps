VERDICT: INVALID

# Hostile verification of `DESIGN-FUDW-DECOMP-v3.md`

The verdict is against the architecture v3 actually claims, not against its
open end-to-end mathematics.  GAP-EA, GAP-MAIN-STRUCTURE, and the uncontracted
F2/F3 reservations are honestly declared and are not reasons for this verdict.
The invalidity comes from four defects inside the claimed 92-row architecture:

1. the MAIN reset constants are consumed before any upstream result produces
   the closed constant package;
2. exact-unit rectification omits its stated inverse-function dependency;
3. the polar provenance reservation is still counted and typed as a
   `proved-mod-audit` result contract; and
4. fourteen ledger-domain factoring targets whose displayed domains are known
   to be stronger than the verified source are likewise counted and typed as
   `proved-mod-audit` result contracts.

The last two defects are not cured by writing `WITHDRAW` or `REFACTOR` in the
non-schema `projected af` column.  A mechanically transcribed registry shard
would still receive the displayed false/non-closed contract and
`proved-mod-audit` status.

## 1. Coverage — INVALID

### 1.1 The reset chain has no upstream producer for its complete constant package — BLOCKER

**Exact v3 loci:** rows
`lem-maincb-stage1-raw-reset-bound` through
`lem-maincb-uniform-reset-chain`, lines 189--192; the later
`lem-routef-main-radius-ledger`, line 213.

The verified Stage-1 packet fixes
\(C_{\rm main},L,C_{\rm pre},\varepsilon_E^{\rm corr}\) before walking any of
the three stages (`PROOF-W74F-H-STAGE1.md:389-423`; hostile verdict
`VERDICT-W74F-H-STAGE1.md:181-250`).  V3 instead:

- defines only \(C_{\rm main},L,C_{\rm pre}\) inside the Stage-1 raw-bound
  contract while already using the unproduced
  \(\varepsilon_E^{\rm corr}\);
- makes the Stage-2, Stage-3, and uniform contracts refer to “the constants
  above,” which is not a self-contained registry contract; and
- places the only displayed producer of \(\varepsilon_E^{\rm corr}\) after
  those rows, with dependency direction
  `raw bounds -> uniform reset -> routef main-radius ledger`.

Thus the later row cannot supply the hypotheses of its own ancestors.  This is
a semantic back-edge even though the literal id graph is acyclic.

**Ready-to-paste correction:** replace the later
`lem-routef-main-radius-ledger` by the upstream
`lem-maincb-reset-constant-ledger` row in Registry impact A, place it before
the three raw-bound rows, and apply all four dependency/contract replacements
in Registry impact B.

### 1.2 The substantive parent coverage otherwise survives the v2 repair — PASS

The three new COMP producers carry exact compression identities,
almost-containment, and compressed-corner algebra inheritance.  The
theorem-free H datum closes the H children without importing `conj-hcb`.
The eight `stated` MAIN obligations separately expose strict refinement,
maximality, the corner relation, cross-class data, one-class extension, binary
merge, finite recombination, and final assembly.  The degree-two row and the
expanded degree-three formula carry the two formerly implicit producers.
F2/F3 remain correctly absent from result coverage.

## 2. Faithfulness — INVALID

### 2.1 Fourteen ledger rows retain domains stronger than the verified ledger — BLOCKER

**Exact v3 loci:** lines 216--221, 223--228, and 230--231:

`lem-routef-raw-factor-norms`,
`lem-routef-raw-factor-units`,
`lem-routef-raw-factor-identities`,
`lem-routef-raw-product-estimate`,
`lem-routef-delta-prime-closeness`,
`lem-routef-delta-normalization-closeness`,
`lem-routef-delta-phi-product`,
`lem-routef-upsilon-prime-closeness`,
`lem-routef-upsilon-normalization-closeness`,
`lem-routef-delta-upsilon-telescope`,
`lem-routef-multiplicative-telescope`,
`lem-routef-upsilon-delta-telescope`,
`lem-routef-k-finiteness`, and
`lem-routef-threshold-minimum`.

The source requires separate MAIN, CP-normalization, degree, and finite-minimum
guards, including
\(\eta\le\varepsilon_E^{\rm corr}/C_A\),
\((C_T+C_{\Delta'})\eta\le1/2\), and
\((C_T+C_{\Upsilon'})\eta\le1/2\)
(`LEDGER-W74F-G-K.md:154-181,193-259`).  As the v2 hostile verdict already
records at lines 118--137, \(\eta_A\) is only the source-linearization radius.
The displayed v3 contracts have not acquired the missing implications merely
because their final column names GAP-LEDGER-DOMAINS.

**Ready-to-paste correction:** apply Registry impact C.  Remove these fourteen
entries from the contracted-result inventory and retain their ids only as
uncontracted GAP-LEDGER-DOMAINS reservations.  Closed replacement contracts
may reuse the ids only after each states its dependency-produced local radius.
Do not redefine \(\eta_A\) using downstream constants.

### 2.2 The repaired COMP, H, EXT, MAIN-target, and degree contracts are faithful — PASS

The three new COMP contracts match the clauses isolated by the v2 verdict.
The H datum contains data and notation only.  The three corrected EXT children
state explicit smallness radii.  The eight MAIN rows remain `stated` targets
rather than transcribed proofs.  The degree-two contract has its own
\(\eta_2\), and the degree-three contract gives
\[
C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'},
\]
matching the reviewed expansion rather than the former naked
\(\operatorname{def}_3\).

## 3. Contract hygiene — INVALID

### 3.1 The polar provenance reservation is still a non-closed result row — MAJOR

**Exact v3 loci:** lines 164--172, especially
`lem-stage1-polar-chart-control` at line 172; the 92-row/status count at
lines 82--92.

V3 correctly says the permitted source prose does not yet yield a closed
formula-level polar contract.  Nevertheless the proposal table calls that
same reservation a `lemma / proved-mod-audit`, supplies the compound phrase
“polar, group-law, and first-derivative errors,” and counts it among the 92
contracted results.  “WITHDRAW” in the projected-size cell does not turn a
compound contract into a non-result reservation.

**Ready-to-paste correction:** delete the row from the contracted table and
insert this reservation beside F2/F3:

| reserved id | disposition | why no contract is supplied |
|---|---|---|
| `gap-stage1-polar-chart-contract` | **GAP / DO NOT SHARD OR SEED** | The permitted Stage-1 prose has not yet been factored into closed formula-level contracts for the polar retraction, group-law error, and first-derivative error. |

Keep `lem-stage1-inversion-derivative-control`,
`lem-stage1-quotient-manifold-package`, and
`lem-stage1-quotient-left-inversion` design-blocked until reviewed replacement
ids exist; do not transcribe them with a dangling
`lem-stage1-polar-chart-control` dependency.

### 3.2 “The constants above” is not a contract interface — BLOCKER

**Exact v3 loci:** lines 190--192.

Contracts are mechanically independent registry values; table order supplies
neither quantifiers nor imported constants.  The exact replacements in
Registry impact B name the upstream producer and remove this contextual prose.

## 4. DAG soundness — INVALID

### 4.1 Exact-unit rectification drops a dependency used by its source proof — MAJOR

**Exact v3 loci:** `lem-stage1-quantitative-inverse-function`, line 170, and
`lem-stage1-exact-unit-rectification`, line 171 (`deps: —`).

`PROOF-W74F-H-STAGE1.md:112-121` says explicitly that `prop_unit` uses the
quantitative inverse-function lemma, and the hostile Stage-1 verdict confirms
that inverse-function input at lines 55--61.  V3 names the producer but leaves
the consumer disconnected.

**Exact correction text:**

> `deps: lem-stage1-quantitative-inverse-function`

for `lem-stage1-exact-unit-rectification`.

### 4.2 The reset-constant ordering is a semantic back-edge — BLOCKER

**Exact v3 loci:** lines 189--192 and 213.

Apply finding 1.1.  The constant ledger must precede and be imported by all
three raw rows and the uniform row.  It must not depend on the uniform row or
on `lem-thmainext-conditional`.

### 4.3 The PRH finish has an unnecessary gap dependency — MINOR

**Exact v3 locus:** `lem-routef-prh-finish`, line 232.

Its displayed contract already includes the complete numerical hypotheses
needed to invoke the af-validated `lem-prh`.  It neither uses nor concludes the
global threshold.  Keeping `lem-routef-threshold-minimum` as a dependency
quietly makes an otherwise closed leaf load-bearing on GAP-LEDGER-DOMAINS.

**Exact correction text:**

> `deps: lem-prh`

The contract, defs, provenance, and projected size are otherwise unchanged.

No literal id cycle was found in the remaining proposal.  The H and EXT
parent/child directions are repaired, and the eight MAIN structural edges are
downward-only.

## 5. Envelope realism — VALID

The v3 projections are appropriately conservative:

- the expanded single-compression transfer is explicitly marked for
  remeasurement;
- the polar target, all eight MAIN structural targets, and the unsafe ledger
  targets receive no asserted af size;
- the H and EXT parent workspaces count only their validated direct imports;
  and
- the exact degree rows acknowledge their domain dependencies.

Adding the reset-constant producer leaves each corrected raw row within the
stated direct-import envelope.  No node-cap increase is proposed.  This pass
does not certify that any projected proof will actually stay within its
estimate; the design correctly requires factoring on ballooning.

## 6. Definition provisioning — VALID

The 20-definition proposal is internally complete for the contracts that may
eventually be transcribed:

- `def-hcb-datum` is a closed, theorem-free datum and does not import the H
  conclusion;
- `def-maincb-reset-state` and `def-maincb-raw-call` contain no success or
  termination theorem;
- the EXT datum and spatial/merging data are separated;
- the polar definition is notation-only; and
- the Stage-1 external-input register keeps all seven topology facts
  conditional on local acquisition and byte matching.

`def-epsilon-cstar-algebra` and the existing
`def-extended-epsilon-cstar-algebra` are distinct proposed terms, not a
duplicate-definition collision.  The reset constants in finding 1.1 are
theorem outputs and therefore need a result producer, not another definition.
All proposed `original`/`consensus` definitions remain draft pending sign-off,
and no `cited candidate` may become `cited` before the stated provenance gate.

## 7. Status law — INVALID

### 7.1 The genuine result targets stay below L0 — PASS

The eight MAIN glue rows and all unverified source premises are `stated`;
topology rows are only `cited candidate`; verified artifact transcriptions are
at most `proved-mod-audit`; nothing is called `proved`.

### 7.2 Fifteen non-result reservations inflate the contracted status inventory — BLOCKER

**Exact v3 loci:** the `proved-mod-audit` polar row at line 172 and the fourteen
`proved-mod-audit` ledger rows listed in finding 2.1; count declaration
lines 82--92.

The design itself says these entries are withdrawn and lack closed contracts.
They therefore cannot simultaneously be contracted `proved-mod-audit` result
rows.  After applying Registry impact C, and replacing rather than adding the
misplaced line-213 constant ledger, the honest inventory is:

> **77 contracted result rows: 55 `proved-mod-audit`, 15 `stated`, and 7
> `cited candidate`; plus 17 uncontracted GAP reservations (polar,
> fourteen ledger-domain targets, F2, and F3).**

This count is a design inventory only, not registry authorization.

## 8. Gap honesty — INVALID

### 8.1 GAP-EA, GAP-MAIN-STRUCTURE, and F2/F3 are honestly quarantined — PASS

GAP-EA's exact-target row and inherited improvement row are `stated`, not
claimed source proofs.  All eight MAIN structural contracts are exact `stated`
proof targets with no optimistic numerical projection.  F2/F3 have no result
contracts, no dependencies, and no parent rewiring.

### 8.2 The polar and ledger gaps are loud but not structurally quarantined — BLOCKER

**Exact v3 loci:** lines 164--172 and 204--232; the phase statements at
lines 453--470.

The prose is honest, but the mechanically relevant table is not: the gap
targets remain `proved-mod-audit` contracts, and faithful downstream rows
still name them as dependencies.  Quarantine must be represented in the
proposal's result inventory, not only in commentary or a projected-af cell.

**Ready-to-paste correction:** apply Registry impact C, keep every dependent
Stage-1 or ledger row design-blocked, and do not transcribe it until its
dependency names resolve to reviewed closed contracts.  The corrected
`lem-routef-prh-finish` is the sole exception because its contract is
independent of the threshold.

## 9. Disposition completeness against v1 and v2 — INVALID

The v1 corrections remain present: the quotient has positive dimension and no
boundary, the Stage-1 smallness clauses are exposed, EXT uses a closed datum,
and the composite definition was not restored.

Most v2 corrections are also complete: all three missing COMP producers are
present; the H datum is closed; the three EXT domains are explicit; the common
split, degree-two, and expanded degree-three producers are present; the eight
MAIN targets replace the former five compound packets; Phase 5 names
`aism-y81y`; and no F2/F3 mathematics is invented.

Two dispositions are only textual:

- v2 finding 3.3 required the non-closed polar packet to be withdrawn, but v3
  retains it in the contracted/status count; and
- v2 finding 2.3 required the globally stated ledger domains not to be used as
  verified contracts before a local-domain sub-DAG exists, but v3 retains
  those contracts and their `proved-mod-audit` labels.

In addition, the v3 reset refactoring exposes the previously unnoticed
producer-order defect in finding 1.1.  Therefore the claim that every v2
finding has been mechanically dispositioned is false as a standalone
architecture claim.

## 10. Repair-introduced regressions — INVALID

### 10.1 No parent-contract, route, or literal-cycle regression — PASS

Parent contracts remain unchanged, `routes:` is absent, the deleted
two-side packet is not resurrected, Phase 5 uses the campaign issue, and no
literal cycle was found.

### 10.2 The repaired inventory conflates provenance targets with result rows — BLOCKER

**Exact v3 loci:** lines 82--92, 164--172, and 204--232.

V3 newly describes the polar and ledger entries as “withdrawn,” yet continues
to count and status them exactly like result rows.  The correction is the
inventory split in Registry impact C.

### 10.3 The reset repair introduces an upstream/downstream mismatch — BLOCKER

**Exact v3 loci:** lines 189--192 and 213.

The new common-split producer is sound, but the full reset-radius producer is
placed downstream of the consumers and imports their assembly.  Apply Registry
impact A/B.  This correction does not invent mathematics: it transcribes the
already hostile-verified constant ledger at
`PROOF-W74F-H-STAGE1.md:389-423`.

# Registry impact

These are the only mechanically supportable changes.  GAP reservations below
are withdrawal instructions, not replacement mathematics.

## A. New upstream MAIN constant row

Delete the later `lem-routef-main-radius-ledger` proposal and put this row
immediately before the three raw-reset rows:

| proposed id | kind / status | exact `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-maincb-reset-constant-ledger` | lemma / `proved-mod-audit` | MAIN-CB reset constants: with \(C_{\rm main}:=\max\{C_{\rm co},C_{\rm split}\}\), \(L:=C_{\rm main}(1+c_0^{\rm cb})\), \(C_{\rm pre}:=2L^2\max\{1,C_{\rm ext},C_{\rm merge}\}\), and \(\varepsilon_E^{\rm corr}:=\min\{\delta_{\max}^{\rm cb},e_H,e_{\rm ext},e_{\rm sel},e_{\rm split}\}/C_{\rm pre}\), all four quantities are finite, positive, universal, and independent of dimension, amplification, block data, and stage index. | — | `lem-compcb-single-compression-transfer`; `lem-stage1-common-split-ledger`; `lem-maincb-error-improvement`; `conj-hcb`; `conj-extcb`; `lem-extcb1-cross-corner-dimension`; `lem-extcb-four-corner-merge` | `PROOF-W74F-H-STAGE1.md:389-423`; `VERDICT-W74F-H-STAGE1.md:181-250` | 8 / 3 |

The row is itself blocked until its listed H/EXT/EA inputs close; that is an
honest dependency, not a reason to globalize a radius.

## B. Exact replacement rows

| proposed id | exact replacement `contract:` value | exact replacement `deps:` | other exact change |
|---|---|---|---|
| `lem-stage1-exact-unit-rectification` | unchanged | `lem-stage1-quantitative-inverse-function` | — |
| `lem-maincb-stage1-raw-reset-bound` | MAIN-CB Stage-1 raw bound: for the universal constants supplied by `lem-maincb-reset-constant-ledger`, every Stage-1 raw-call datum in a reset state with \(0\le\varepsilon_0\le\varepsilon_E^{\rm corr}\), old-side defect at most \(C_{\rm co}(1+c_0^{\rm cb})\varepsilon_0\), and split-corner defect \(\varepsilon_S\le C_{\rm co}(1+c_0^{\rm cb})\varepsilon_0\) has \(\delta_{\rm raw}\le L^2\varepsilon_0\) and \(e_{\rm raw}\le C_{\rm pre}\varepsilon_0\). | `lem-maincb-reset-constant-ledger`; `lem-stage1-fresh-two-point-inclusion`; `lem-stage1-old-side-compression`; `lem-maincb-split-corner-defect`; `lem-maincb-error-improvement` | defs/provenance unchanged |
| `lem-maincb-stage2-raw-reset-bound` | MAIN-CB Stage-2 raw bound: for the universal constants supplied by `lem-maincb-reset-constant-ledger`, every Stage-2 raw-call datum with \(0\le\varepsilon\le\varepsilon_E^{\rm corr}\), current-corner defect \(\varepsilon_Y\le L\varepsilon\), a reset map of defect at most \(c_0^{\rm cb}\varepsilon_Y\), and one compatible compression has \(\delta_{\rm raw}\le L^2\varepsilon\) and \(e_{\rm raw}\le C_{\rm pre}\varepsilon\). | `lem-maincb-reset-constant-ledger`; `lem-compcb-single-compression-transfer`; `conj-extcb`; `lem-maincb-error-improvement` | defs/provenance unchanged |
| `lem-maincb-stage3-raw-reset-bound` | MAIN-CB Stage-3 raw bound: for the universal constants supplied by `lem-maincb-reset-constant-ledger`, every Stage-3 raw-call datum with \(0\le\varepsilon\le\varepsilon_E^{\rm corr}\), current sum-corner defect \(\varepsilon_Y\le L\varepsilon\), and two reset block maps satisfying a cross-class four-corner datum has \(\delta_{\rm raw}\le L^2\varepsilon\) and \(e_{\rm raw}\le C_{\rm pre}\varepsilon\). | `lem-maincb-reset-constant-ledger`; `lem-extcb-four-corner-merge`; `lem-maincb-error-improvement` | defs/provenance unchanged |
| `lem-maincb-uniform-reset-chain` | MAIN-CB uniform reset invariant: for the universal constants supplied by `lem-maincb-reset-constant-ledger` and \(0\le\varepsilon\le\varepsilon_E^{\rm corr}\), every Stage-1, Stage-2, and Stage-3 raw-call datum satisfying the literal local hypotheses of the three raw-bound rows has \(\delta_{\rm raw}\le L^2\varepsilon\) and \(e_{\rm raw}\le C_{\rm pre}\varepsilon\), and every extension or merge is followed immediately by an error reset. | `lem-maincb-reset-constant-ledger`; `lem-maincb-stage1-raw-reset-bound`; `lem-maincb-stage2-raw-reset-bound`; `lem-maincb-stage3-raw-reset-bound` | defs/provenance unchanged |
| `lem-routef-prh-finish` | unchanged | `lem-prh` | — |

Every eventual threshold-aggregation replacement must depend on
`lem-maincb-reset-constant-ledger`, not on the deleted
`lem-routef-main-radius-ledger`.

## C. Exact withdrawal actions

Move these ids out of all contracted-result/status counts:

| gap family | ids | exact disposition |
|---|---|---|
| `GAP-S1-POLAR-CONTRACT` | `lem-stage1-polar-chart-control` | **NO RESULT ROW.** Replace by the uncontracted `gap-stage1-polar-chart-contract` reservation in finding 3.1. Supply no `contract:`, `status:`, or `deps:` until reviewed formula-level replacements exist. |
| `GAP-LEDGER-DOMAINS` | `lem-routef-raw-factor-norms`; `lem-routef-raw-factor-units`; `lem-routef-raw-factor-identities`; `lem-routef-raw-product-estimate`; `lem-routef-delta-prime-closeness`; `lem-routef-delta-normalization-closeness`; `lem-routef-delta-phi-product`; `lem-routef-upsilon-prime-closeness`; `lem-routef-upsilon-normalization-closeness`; `lem-routef-delta-upsilon-telescope`; `lem-routef-multiplicative-telescope`; `lem-routef-upsilon-delta-telescope`; `lem-routef-k-finiteness`; `lem-routef-threshold-minimum` | **NO RESULT ROWS.** Retain the ids only as `GAP / DO NOT SHARD OR SEED` reservations. Supply no `contract:`, `status:`, or `deps:` until closed local-radius producers and the finite-minimum DAG exist. |

The exact degree-two and degree-three contracts may remain in the design, but
they must not be transcribed with dangling dependencies.  Reconnect and seed
them only after the local-domain replacement rows exist.

## D. Safe-to-transcribe and seed-first subset

Subject to creation and sign-off of every proposed definition actually named
by a row, the following subset is architecturally safe:

1. **COMP first:** `lem-compcb-amplified-compression`,
   `lem-compcb-amplified-compression-identities`,
   `lem-compcb-amplified-almost-containment`,
   `lem-compcb-rectangular-product`,
   `lem-compcb-compressed-unit-action`,
   `lem-compcb-compressed-unit-norm`, and
   `lem-compcb-corner-algebra`.
   `lem-compcb-single-compression-transfer` is safe to transcribe but must be
   remeasured before seeding.
2. **H after COMP and `def-hcb-datum`:** all fourteen H rows at v3
   lines 112--125, then the existing `conj-hcb` parent after every child
   validates.
3. **Independent EXT front end:** the `stated`
   `lem-extcb-one-dimensional-product`,
   `lem-extcb-one-dimensional-corner-dimension`,
   `lem-extcb-corner-dimension-additivity`, and
   `lem-extcb-four-corner-merge`, followed by
   `lem-extcb1-close-corner-dimension` and
   `lem-extcb1-cross-corner-dimension`.  No EXT row downstream of
   `lem-extcb-exact-target-approximation` may seed before GAP-EA closes.
4. **Independent Stage-1 front end:** the `stated`
   `lem-stage1-quantitative-inverse-function`, then the corrected
   `lem-stage1-exact-unit-rectification`.  No polar-dependent row is in the
   safe subset.
5. **Independent ledger/finish leaves:**
   `lem-routef-functional-calculus-closeness`,
   `lem-routef-ai-defect-linearization`, and the corrected
   `lem-routef-prh-finish`.

The seven topology rows are not safe to transcribe as `cited` until their local
sources are acquired and byte-matched.  The MAIN reset/structural rows, both
degree rows, all telescopes, the threshold, and every parent downstream of a
named GAP remain design-only until their stated blockers close.
