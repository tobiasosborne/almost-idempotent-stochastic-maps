VERDICT: VALID-WITH-CORRECTIONS

# Fresh hostile verification of `DESIGN-FUDW-DECOMP-v4.md`

V4 correctly applies every A/B/C action ordered by the v3 verdict. Its printed
77-row inventory is internally exact, the fifteen v3 withdrawals are
structurally quarantined, and the advertised safe-to-transcribe partition is
sound. One later-state correction is required: the two F2/F3 reservations are
now contradicted by the supplied hostile-reviewed, registered
`proved-mod-audit` shards. They must be replaced in the design inventory by
those existing result rows. The corrected inventory is 79 contracted rows
(57/15/7) plus 15 reservations. This is a mechanical present-state correction,
not new mathematics and not a reason to lift any remaining GAP.

## 1. Coverage — VALID-WITH-CORRECTIONS

### 1.1 Registry impact A is applied exactly — PASS

At `DESIGN-FUDW-DECOMP-v4.md:213`,
`lem-maincb-reset-constant-ledger` is immediately before the three raw-reset
rows. The complete row is byte-identical to
`VERDICT-FUDW-DECOMP-V3.md:349`: contract, empty defs, seven dependencies,
provenance, and `8 / 3` projection all match.

Its four formulas agree with `PROOF-W74F-H-STAGE1.md:389-423`.
Factoring the common positive divisor \(C_{\rm pre}\) out of the minimum in
the proof gives exactly the contract's displayed
\(\min\{\delta_{\max}^{\rm cb},e_H,e_{\rm ext},e_{\rm sel},e_{\rm split}\}/
C_{\rm pre}\). The source's universality and independence conclusion is
retained.

`lem-routef-main-radius-ledger` occurs nowhere in the v4 design or its answer:
there is no surviving row, dependency, reference, or count.

### 1.2 The v3 coverage repair otherwise survives — PASS

The COMP, H, EXT, Stage-1, MAIN, degree, and PRH contracts not targeted by A/B/C
are preserved. The polar result is not claimed, the fourteen unsafe ledger
contracts are not claimed, and parents downstream of those absences remain
design-blocked.

### 1.3 The F2/F3 coverage reservation is stale — MAJOR

**Exact v4 loci:** disposition rows at lines 41, 53, 72, and 97; GAP rows
268-269; ledger wiring at lines 347-368; Phase 5 at lines 557-564; risks R29-R30
at lines 603-604; closure statement at lines 628-637; and
`ANSWER-REPAIR-V4.md:3,10-12`.

`VERDICT-F2F3-BRIDGE.md:5-13,118-141,205-224` validates both closed conditional
contracts and their literal composition into `lem-routef-prh-finish`. More
decisively, `lem-routef-f2-positive-unital-compression.md` and
`lem-routef-f3-retract-defect.md` are already registered at
`status: proved-mod-audit`. Their empty dependency lists deliberately avoid
every quarantined ledger-domain id.

V4 therefore must not continue to say that the contracts are unavailable or
reserve two GAP ids. This does not unblock `lem-routef-k-ledger`: the fourteen
component-domain reservations remain an architecture/seeding blocker.

**Ready-to-paste correction:** delete the two reservation rows at v4 lines
268-269, insert the two exact result rows in Registry impact A below, and apply
the count, wiring, phase, risk, and closure replacements in Registry impact B.

## 2. Faithfulness — VALID

### 2.1 Registry impact B is byte-faithful — PASS

The contract/dependency pairs at v4 lines 214-217 are byte-identical to
`VERDICT-FUDW-DECOMP-V3.md:359-362`:

- Stage 1 names the upstream constant ledger and retains the separate
  old-side and split-corner defects.
- Stage 2 names the current-corner defect and one compatible compression.
- Stage 3 names the current sum-corner defect and cross-class four-corner
  datum.
- The uniform row imports the constant ledger and all three literal raw rows.

For all four, defs and provenance are unchanged from v3 lines 189-192.
`lem-stage1-exact-unit-rectification` has exactly the required IFT dependency
at v4 line 196, and `lem-routef-prh-finish` has exactly `deps: lem-prh` at line
243. No mathematical content was strengthened or weakened by the repair.

### 2.2 Registry impact C is faithful — PASS

The polar provenance prose is not converted into a formula contract. The
fourteen ledger ids retain no unsound global \(\eta_A\) contract. The exact
degree-two and degree-three statements remain visible but explicitly
non-transcribable until reviewed local-domain ids exist. This is precisely the
v3 verdict's permitted design-only treatment.

### 2.3 The supplied F2/F3 replacements are faithful — PASS

The registered contracts are the verifier's §7 exact texts, flattened only
into registry ASCII. F2 derives commutativity and positive-unital \(A,M\) from
three explicit factorization hypotheses. F3 consumes exactly F2's estimates
and yields the advertised
\(3K\eta/(1-3K\eta)\) defect. Neither contract imports or presupposes a
quarantined component-domain result.

## 3. Contract hygiene — VALID

The new upstream constant row is one constant-ledger result; none of the four
reset contracts uses contextual phrases such as “the constants above.”
The polar id is represented only by the uncontracted
`gap-stage1-polar-chart-contract` reservation.

The F2 and F3 registered contracts are closed conditional statements. F2 has
one output package needed by the stochastic-retract composition; F3 is the
separate retract-defect implication. Their separation is the required
factoring, not a compound-contract regression.

## 4. DAG soundness — VALID

The exact-unit edge and the PRH edge are corrected. All three raw rows and the
uniform row point downstream from `lem-maincb-reset-constant-ledger`; the
constant producer has no dependency on a raw row,
`lem-maincb-uniform-reset-chain`, or `lem-thmainext-conditional`.

Each of the fourteen withdrawn ledger ids occurs exactly once, in the GAP
inventory at v4 lines 254-267. `lem-stage1-polar-chart-control` and
`lem-routef-main-radius-ledger` occur zero times. No contracted row has a
dependency on any of those sixteen withdrawn ids. The four affected surviving
Stage-1/degree rows use explicit `UNRESOLVED / DO NOT TRANSCRIBE` markers
instead of counterfeit dependency ids.

The only external dependency ids in the 77-row table are the existing
`conj-hcb`, `conj-extcb`, `lem-kitaev-almost-idemp-audit`, and `lem-prh`.
No literal or semantic cycle was found. Adding the two registered F2/F3 leaves
adds no cycle because both have empty `deps`.

## 5. Envelope realism — VALID

V4 retains the v3 verdict's conservative projections, including
`REMEASURE BEFORE SEEDING` for single-compression transfer and no numerical
projection for any quarantined polar, MAIN-structure, or ledger-domain work.
The new reset-constant row is exactly `8 / 3`.

The registered F2/F3 shards have `af: none`; the correction must preserve that
value. They are not thereby af-validated or automatically seedable. Phase 5
must remeasure and factor either proof before seeding if its plan would exceed
12 nodes or depth 3.

## 6. Definition and external-input provisioning — VALID

The design contains exactly 20 proposed definition rows. Their
cited/consensus/original gates and the seven-row Stage-1 external-input
register are unchanged. The H, EXT, reset-state, and raw-call data definitions
remain theorem-free.

The two registered bridge shards use the already existing `def-stochastic`
and require no new definition proposal. Their standard finite-dimensional
\(C^*\)-algebra and positive/UCP vocabulary was already accepted by the
bridge verifier.

## 7. Status law — VALID-WITH-CORRECTIONS

### 7.1 V4's printed inventory is internally exact — PASS

An independent enumeration of v4's proposal tables gives exactly:

- 77 contracted rows;
- 55 `proved-mod-audit`, 15 `stated`, and 7 `cited candidate`;
- section counts 22 COMP/H, 12 EXT, 7 topology, 31 Stage-1/MAIN, and
  5 ledger/finish; and
- 17 rows in the uncontracted GAP table.

The table contains no duplicate contracted id and no status above
`proved-mod-audit`.

### 7.2 Present-state counts must include the registered bridges — MAJOR

Once the two false reservations are removed and the two supplied registered
rows are recognized, the correct standalone inventory is:

> **79 contracted result rows: 57 `proved-mod-audit`, 15 `stated`, and
> 7 `cited candidate`; plus 15 uncontracted GAP reservations (one polar and
> fourteen ledger-domain targets).**

Definitions remain 20. This correction changes neither status of an existing
v4 row nor any L0/af claim.

**Ready-to-paste correction:** replace v4 lines 106-117 by Registry impact
B.1 below, and make the same numerical replacements in
`ANSWER-REPAIR-V4.md:2-4`.

## 8. Gap honesty — VALID-WITH-CORRECTIONS

### 8.1 The four surviving GAP families are honestly scoped — PASS

- **GAP-EA:** its exact-target and improvement rows are `stated`; every
  dependent reset/MAIN row is explicitly blocked.
- **GAP-S1-POLAR-CONTRACT:** the only inventory entry is the uncontracted polar
  reservation; polar-dependent result contracts are design-only.
- **GAP-MAIN-STRUCTURE:** all eight obligations are `stated`, carry no
  optimistic af number, and block their parent.
- **GAP-LEDGER-DOMAINS:** fourteen ids are reservation-only; both degree rows
  and all future telescopes/threshold wiring remain blocked.

No `proved-mod-audit` row quietly treats one of those gaps as a proved
dependency. Conditional contracts downstream of a named gap are visibly
non-transcribable.

### 8.2 F2/F3 are no longer GAPs — MAJOR

The claims at v4 lines 268-269, 350-351, 367-368, 603-604, and 636-637 are
factually obsolete against the supplied registry shards. Apply Registry impact
A/B. The corrected closure statement has four gap families, not five.

## 9. Disposition completeness against v1/v2/v3 — VALID-WITH-CORRECTIONS

The v4 tables enumerate every v1 finding, every v2 finding, and all 19 v3
findings. The substantive prior corrections remain present:

- COMP structure, closed H datum, EXT domains, Stage-1 hypotheses, and topology
  gates are not regressed;
- the eight MAIN obligations remain separate `stated` targets;
- the common-split, degree-two, and expanded degree-three producers remain;
- v3 A/B/C and §D are applied; and
- no parent contract or route is changed.

The rows saying F2/F3 are still blocked were accurate dispositions of the
earlier permitted artifact set, but they are stale as present-tense v4 state.
Replace their disposition text as specified in Registry impact B.2; no prior
verdict finding is otherwise missing.

## 10. Repair-introduced regressions — VALID-WITH-CORRECTIONS

No A/B/C repair introduced a parent-contract change, route change, cycle,
definition collision, status promotion, or hidden result row. The one defect
is later-state drift: v4 fossilizes the former F2/F3 gaps after independently
reviewed registry rows have closed them. Because the exact replacements
already exist and do not touch the remaining gap DAG, this is mechanically
repairable and does not warrant `INVALID`.

# Registry impact

These are the only result rows changed by this verdict. The rows already exist
in the registry; v4 must recognize them, not create duplicates or alter their
bytes.

## A. Replace the two F2/F3 reservations by registered result rows

Delete:

- `gap-routef-f2-positive-unital-compression-contract`
- `gap-routef-f3-retract-defect-contract`

Insert these exact inventory rows:

| id | kind / status | exact `contract:` value | defs | deps | provenance | af |
|---|---|---|---|---|---|---|
| `lem-routef-f2-positive-unital-compression` | lemma / `proved-mod-audit` | Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> l_inf^n diagonal extraction and J: l_inf^n -> M_n diagonal inclusion, Phi = J Q D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, \|\|Delta Upsilon - Phi\|\|_cb <= K*eta, \|\|Upsilon Delta - I_B\|\|_cb <= K*eta, and \|\|Upsilon(Delta x Delta y) - xy\|\| <= K*eta*\|\|x\|\|*\|\|y\|\| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota: l_inf^k -> B such that A := D Delta iota: l_inf^k -> l_inf^n and M := iota^{-1} Upsilon J: l_inf^n -> l_inf^k are positive unital maps satisfying \|\|Q - AM\|\|_{inf->inf} <= K*eta, \|\|QA - A\|\|_{inf->inf} <= 2K*eta, and \|\|Ax\|\|_inf >= (1-3K*eta)*\|\|x\|\|_inf for every x in l_inf^k. | `def-stochastic` | — | `PROOF-F2F3-BRIDGE.md` §1; `VERDICT-F2F3-BRIDGE.md` §7; registered shard is authoritative | `none` |
| `lem-routef-f3-retract-defect` | lemma / `proved-mod-audit` | Route F F3 retract defect: let K >= 1 be a dimension-independent constant, n,k >= 1, A: l_inf^k -> l_inf^n and M: l_inf^n -> l_inf^k positive unital maps, Q: l_inf^n -> l_inf^n row-stochastic, and eta >= 0 with 3K*eta < 1; if \|\|Q - AM\|\|_{inf->inf} <= K*eta, \|\|QA - A\|\|_{inf->inf} <= 2K*eta, and \|\|Ax\|\|_inf >= (1-3K*eta)*\|\|x\|\|_inf for every x in l_inf^k, then \|\|MA - I_k\|\|_{inf->inf} <= 3K*eta/(1-3K*eta). | `def-stochastic` | — | `PROOF-F2F3-BRIDGE.md` §2; `VERDICT-F2F3-BRIDGE.md` §7; registered shard is authoritative | `none` |

The backslashes before the doubled norm bars above are Markdown-table escapes.
For byte-mechanical use, the authoritative registered fields are:

```yaml
id: lem-routef-f2-positive-unital-compression
kind: lemma
contract: Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> l_inf^n diagonal extraction and J: l_inf^n -> M_n diagonal inclusion, Phi = J Q D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta, and ||Upsilon(Delta x Delta y) - xy|| <= K*eta*||x||*||y|| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota: l_inf^k -> B such that A := D Delta iota: l_inf^k -> l_inf^n and M := iota^{-1} Upsilon J: l_inf^n -> l_inf^k are positive unital maps satisfying ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k.
defs: def-stochastic
deps:
status: proved-mod-audit
af: none
```

```yaml
id: lem-routef-f3-retract-defect
kind: lemma
contract: Route F F3 retract defect: let K >= 1 be a dimension-independent constant, n,k >= 1, A: l_inf^k -> l_inf^n and M: l_inf^n -> l_inf^k positive unital maps, Q: l_inf^n -> l_inf^n row-stochastic, and eta >= 0 with 3K*eta < 1; if ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k, then ||MA - I_k||_{inf->inf} <= 3K*eta/(1-3K*eta).
defs: def-stochastic
deps:
status: proved-mod-audit
af: none
```

If inserted into v4's mathematical-display table, the exact LaTeX contract
texts are `VERDICT-F2F3-BRIDGE.md:214,218`; do not paraphrase them.

## B. Consequential ready-to-paste design corrections

### B.1 Counts

Replace v4 lines 106-117 by:

> This standalone inventory contains **79 contracted result rows**:
>
> - 22 COMP-CB / H-CB rows;
> - 12 EXT-CB rows;
> - 7 contingent topology leaves;
> - 31 Stage-1 / MAIN-CB rows;
> - 5 Route F ledger/finish rows; and
> - 2 existing registered F2/F3 bridge rows.
>
> It also contains **15 uncontracted GAP reservations**: one polar target and
> fourteen ledger-domain targets. Of the 79 contracted rows, **57** are
> `proved-mod-audit`, **15** are `stated`, and **7** are `cited candidate`.
> No row is proposed above `proved-mod-audit`.

Retitle v4 line 245:

> `### 2.6 Complete uncontracted GAP inventory — 15 reservations, not result rows`

At v4 lines 247-249, replace `77-row` by `79-row`, then delete lines 268-269.

### B.2 Dispositions

Use this replacement wherever v4's disposition tables presently say F2/F3
remain uncontracted:

> **CLOSED AFTER THE PRIOR VERDICTS:** the hostile-reviewed registered
> `proved-mod-audit` rows `lem-routef-f2-positive-unital-compression` and
> `lem-routef-f3-retract-defect` replace the former reservations. They have
> empty deps and do not import `GAP-LEDGER-DOMAINS`. The ledger parent remains
> design-blocked only on its component-domain factoring.

The historical v3 count disposition may still record that A/B/C produced
77/55/15/7; add “before the later registered F2/F3 reconciliation” so that it
is not presented as the current total.

### B.3 `lem-routef-k-ledger` wiring

Replace v4 lines 347-368 by:

> **DO NOT REWIRE OR SEED.** The existing contract stays unchanged. The
> registered `lem-routef-f2-positive-unital-compression` and
> `lem-routef-f3-retract-defect` rows close the stochastic-retract bridge and
> compose literally with `lem-routef-prh-finish`; they do not import any
> quarantined component-domain row. The parent nevertheless remains blocked
> because the fourteen `GAP-LEDGER-DOMAINS` reservations do not yet form a
> transcribable local-domain DAG. Accordingly there is still no complete
> proposed `deps:` replacement and no projected parent node count.
>
> After the fourteen local-domain replacements close, the complete parent
> wiring must include the three telescope results, \(K\)-finiteness, the
> rebuilt threshold, `lem-routef-f2-positive-unital-compression`,
> `lem-routef-f3-retract-defect`, and `lem-routef-prh-finish`. Until then:
>
> **REFACTOR / BLOCKED ON GAP-LEDGER-DOMAINS.**

### B.4 Phase 5

Replace v4 lines 559-564 by:

> 1. Reuse the already registered
>    `lem-routef-f2-positive-unital-compression` and
>    `lem-routef-f3-retract-defect`; do not recreate the former GAP ids.
> 2. Both rows remain `proved-mod-audit` with `af: none`. Remeasure each before
>    seeding and factor it if its plan exceeds the 12-node/depth-3 envelope.
> 3. Keep `lem-routef-k-ledger` blocked until `GAP-LEDGER-DOMAINS` closes; then
>    propose complete parent wiring containing both bridge rows and
>    `lem-routef-prh-finish`.
> 4. F0/root work remains separate and downstream; this design creates no F0
>    row and no root theorem claim.

### B.5 Risks and closure

Replace R29-R30 by:

| id | risk | required control |
|---|---|---|
| R29 | The registered F2 bridge could be duplicated or incorrectly coupled to quarantined ledger components. | Reuse `lem-routef-f2-positive-unital-compression` with its exact contract, empty deps, and `af: none`; its three factorization estimates remain explicit hypotheses. |
| R30 | The registered F3 bridge could be left stale as a GAP or its exact denominator weakened. | Reuse `lem-routef-f3-retract-defect` verbatim; retain \(3K\eta<1\) and \(3K\eta/(1-3K\eta)\). |

Replace “Five gap families remain” and item 5 at v4 lines 628-637 by:

> Four gap families remain:
>
> 1. **GAP-EA** blocks exact-target approximation and IMPROVE-CB.
> 2. **GAP-S1-POLAR-CONTRACT** is the uncontracted polar reservation and blocks
>    every polar-dependent Stage-1 row.
> 3. **GAP-MAIN-STRUCTURE** covers the eight unverified structural targets.
> 4. **GAP-LEDGER-DOMAINS** contains fourteen uncontracted target reservations
>    and blocks both degree contracts, every telescope, threshold aggregation,
>    and complete parent rewiring.
>
> The F2/F3 bridge is closed by two registered `proved-mod-audit` rows; this
> changes no remaining GAP and makes no L0 or af-validation claim.

## C. Safe-to-transcribe and seed-first subset

Subject to sign-off of every proposed definition named by a row, the v3 §D
partition remains correct:

1. **COMP first:** `lem-compcb-amplified-compression`,
   `lem-compcb-amplified-compression-identities`,
   `lem-compcb-amplified-almost-containment`,
   `lem-compcb-rectangular-product`,
   `lem-compcb-compressed-unit-action`,
   `lem-compcb-compressed-unit-norm`, and
   `lem-compcb-corner-algebra`.
   `lem-compcb-single-compression-transfer` is safe to transcribe but must be
   remeasured before seeding.
2. **H after COMP and `def-hcb-datum`:** all fourteen H rows from
   `lem-hcb-column-hilbert-squared` through
   `lem-hcb4-canonical-inverse`, then the existing `conj-hcb` parent after the
   children validate.
3. **Independent EXT front end:** the `stated`
   `lem-extcb-one-dimensional-product`,
   `lem-extcb-one-dimensional-corner-dimension`,
   `lem-extcb-corner-dimension-additivity`, and
   `lem-extcb-four-corner-merge`, followed by
   `lem-extcb1-close-corner-dimension` and
   `lem-extcb1-cross-corner-dimension`. Nothing downstream of
   `lem-extcb-exact-target-approximation` seeds before GAP-EA closes.
4. **Independent Stage-1 front end:**
   `lem-stage1-quantitative-inverse-function`, then
   `lem-stage1-exact-unit-rectification`. No polar-dependent row is safe.
5. **Independent ledger/finish leaves:**
   `lem-routef-functional-calculus-closeness`,
   `lem-routef-ai-defect-linearization`, and
   `lem-routef-prh-finish`.
6. **Existing registered bridge leaves:** do not transcribe duplicates.
   `lem-routef-f2-positive-unital-compression` and
   `lem-routef-f3-retract-defect` are architecturally independent of the
   component-domain GAP and may be scheduled for af work only after their
   `af: none` plans are remeasured.

The seven topology rows remain blocked on local acquisition, hashing, and byte
matching. The MAIN reset/structural rows, both degree rows, all telescopes, the
threshold, and every parent downstream of a surviving named GAP remain
design-only. The H/EXT elevation news promotes no v4 status.
