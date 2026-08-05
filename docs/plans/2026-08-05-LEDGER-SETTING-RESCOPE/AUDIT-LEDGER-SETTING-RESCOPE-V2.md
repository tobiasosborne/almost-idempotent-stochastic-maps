# AUDIT — hostile re-audit of DESIGN-LEDGER-SETTING-RESCOPE-V2

Date: 2026-08-05
Role: fresh hostile auditor
Status: **NON-RIGOROUS AUDIT / DESIGN ONLY / NOTHING PROMOTED**

## 0. Verdict

**LAND-WITH-EXACT-CORRECTIONS.**

The v2 design clears all three v1 BLOCKERS.  Its definition is data-and-typing
only; its formation row has the required
`exists W_RF, for every input, exists S` order and is derivable from its three
declared providers; and row 14 has been reduced to the genuine scalar
interface proved in the ratified LEDGER-DOMAINS design.  I independently
recomputed the fifteen unchanged suffixes: all are byte-identical to the
landed contracts.  Injecting the proposed formation row and all proposed
`deps:` replacements into the live registry gives 365 nodes, no dangling
imports, and no cycle.  The future strengthened K-ledger block is also
acyclic.

The package is not clean LAND.  Four exact defects remain:

1. rows 6 and 9 still display a free `X` in their normalization formulas;
2. the raw-identities continuation cannot instantiate its validated
   existential node `1.1` at the particular formation-selected `S.B,S.v`;
3. the design requires the new formation row to be validated before the two
   live continuations, but does not specify the formation workspace's own
   provisioning/elevation phase; and
4. the enumerated landing surface omits required persistent and hard-gate
   edits, including the retained landing script and the new formation id's
   `report/UNWIRED.md` entry.

None is a new mathematical gap in the Route-F estimates.  Each has a local,
exact correction below.  No implementation is authorized by this audit.  All
sixteen rows remain `status: stated`; the two live roots remain pending in
their `af: seeded` workspaces; the DO-NOT-REWIRE guard remains in force.

## 1. Numbered findings

| no. | severity | locus | finding | exact correction |
|---:|---|---|---|---|
| 1 | **MEDIUM** | v2 lines 393--398 (row 6) and 439--444 (row 9) | The suffixes display `Delta(X)` and `Upsilon(X)`, but the prefixes do not bind `X`.  Calling the resulting maps UCP does not bind the variable occurring in their defining formulas. | In row 6, insert `and for every X in S.B` before “writing the fields”.  In row 9, insert `and for every X in B(H)` at the same point (`H` is already bound by the input tuple).  Leave both landed suffixes byte-unchanged. |
| 2 | **HIGH** | v2 lines 627--644; live raw-identities node `1.1` | Section 5.3 says the amended root will instantiate validated node `1.1` on the root's same `W_RF,S,B,v`.  Node `1.1` is existential: it concludes that MAIN supplies *some* `B,v`; it is not a lemma parameterized by a preselected `S.B,S.v`.  No uniqueness permits the advertised instantiation. | Amend root `1` to cite the formation external directly for the fixed `S`'s exact idempotence, extended structure, `B`, bijective `v`, and `u=v^(-1)`, then apply validated node `1.2`, which is universal in the bijection `v`.  Preserve node `1.1` mechanically but do not use it as the same-output bridge.  If the verifier requires an explicit bridge, add one pending fixed-`S` child within the already stated 6-node/2-round contingency. |
| 3 | **HIGH** | v2 lines 578--599, 652--661 | The two continuations correctly wait for a validated formation external, but the landing plan creates the formation row only as `stated/none`; it never enumerates seeding, provisioning, verifying, exporting, or banking that workspace.  As written, the prerequisite state for section 5 is never reached. | Add a phase before either live amendment: seed `proofs/lem-routef-raw-factor-setting-formation` at the exact contract; provision the four declared definitions exactly once and the three provider externals at literal `proofs/<id>` paths; run the proposed 10/3, cap-14 fresh-prover/fresh-verifier elevation; export, oracle-verify, and only then mechanically bank the formation row.  This is a future plan, not a promotion by this audit. |
| 4 | **HIGH** | v2 lines 652--665; live `scripts/land-ledger-domains-rows.py`; `report/UNWIRED.md` | The “authorized future landing surface” is not a complete reproducible/gate-clean package.  The retained generator still hard-codes all old contracts/defs/deps and the stale row-3 sentence; every shard's provenance still attributes the whole contract to the old design; a new unanchored formation row will hard-fail `check-provenance`; and the usual lockstep state documents are not enumerated. | Expand the landing manifest exactly as in §11 below: update the retained script; update all sixteen provenance/status notes honestly; add the formation id to `report/UNWIRED.md`; add the formation elevation phase; regenerate every definition/argument/report projection; and update `HANDOFF.md`, the live proof-strategy pointer/sketch, and `docs/worklog.md` in the authorized implementation session. |

No finding is a BLOCKER.  The verdict is therefore not DESIGN-REJECTED, but
the package must not land without all four corrections.

## 2. Attack 1 — finding-by-finding closure of the v1 audit

**VERDICT: SEVEN CLEARED; ONE NOT-CLEARED (MEDIUM).  NO BLOCKER SURVIVES.**

| v1 finding | disposition | exact v2 locus and audit reason |
|---:|---|---|
| 1 — definition launders AI/MAIN conclusions (**BLOCKER**) | **CLEARED** | §1.1, especially lines 74--220 and the explicit exclusions at 222--234.  The definition records scalar fields, typed objects, maps, and notation only.  It asserts no existence, defect hypothesis, idempotence, extended structure/isomorphism, inverse relation, universality, positivity, or estimate. |
| 2 — no nonvacuous formation result (**BLOCKER**) | **CLEARED** | §2.1 line 262 and lines 275--288.  One `W_RF` is chosen first; every admissible finite-dimensional UCP/cb input then receives `B,v,S`.  §6.2 lines 669--690 makes both formation and the four packet producers direct future K-ledger imports. |
| 3 — global witnesses could vary with `S` (**HIGH**) | **CLEARED** | §2.1 line 262 has `there exists one choice W_RF ... such that for every ...`; lines 275--278 explicitly restrict the input-specific existential to `B,v,S`.  Every family prefix begins by fixing that same formation-produced header. |
| 4 — “furnished/successive” was prose and required edges were absent (**HIGH**) | **CLEARED** | §3.3--§3.5 spells the chain `Delta' -> Delta -> Upsilon' -> Upsilon`; each named provider is direct.  The complete required-edge check appears in §7 below.  The undefined word “successive” is gone. |
| 5 — row 14 used a phantom F2/F3/PRH interface (**BLOCKER**) | **CLEARED** | §3.5 lines 495--518.  The row now exports only `eta_K` positivity and literal scalar inequalities; all F2/F3/PRH result ids and their vocabulary leave its `deps:`/`defs:`.  §6.2 binds the map data at the strengthened parent. |
| 6 — matrix variables not universally bound (**MEDIUM**) | **NOT-CLEARED** | The listed amplified rows are repaired at lines 344, 378, 404, 412, 422, and 463.  But the same acceptance principle catches two missed sites: free `X` in row 6 line 396 and row 9 line 442.  Apply finding 1's exact prefixes. |
| 7 — `def-ucp-map` absent from live workspaces (**MEDIUM**) | **CLEARED for the two live workspaces** | §5.1 lines 585--599 requires exactly one new setting definition and one `def-ucp-map`, retains the already registered extended definitions, and mandates uniqueness preflight.  The omitted *formation-workspace* plan is the separate new finding 3. |
| 8 — stale row-3 body aliases later `rho_id` to `rho_id^corr` (**LOW**) | **CLEARED** | §3.2 lines 368--373 gives the exact replacement sentence, and §6.1 line 659 includes that edit in the future surface.  The row-3 contract suffix itself remains byte-identical. |

The v1 redesign gate is correspondingly cleared on data-only separation,
formation/nonvacuity, global witness order, direct producer relations, row-14
scalar factoring, and guard/status preservation.  Its universal binder and
af-continuation requirements clear only after findings 1--3 above are folded
in.

## 3. Attack 2 — deletion test from scratch

**VERDICT: CLEARED.**

### 3.1 Definition alone

Deleting every analytic result leaves a possibly empty record schema.  A
consumer may unpack:

- four real scalar fields and derived scalar formulas;
- typed `H,Phi,eta,tilde-Phi,A,star,B,v,u`; and
- the notation `tilde-Delta=v` and `tilde-Upsilon=u tilde-Phi`.

It may not unpack a defect bound, existence of any header/datum, positivity or
universality of a scalar, exact idempotence, an extended-algebra conclusion,
an extended-isomorphism conclusion, bijectivity, `u=v^(-1)`, or any estimate.
The explicit disclaimer at v2 lines 222--234 matches the actual fields rather
than trying to retract theorem content already placed in them.

### 3.2 Producer-by-producer deletion from formation/a consumer

| deleted producer | what remains | conclusion that is lost |
|---|---|---|
| `lem-routef-ai-defect-linearization` | Kitaev still supplies exact idempotence and an asymptotic extended interface for sufficiently small `eta`; the definition still records formulas. | No fixed `(C_A,eta_A)` with the stated exact `C_A`, no `rho_AI=eta_A` witness, and no exported `epsilon_AI(eta)<=C_A*eta`.  Hence the MAIN threshold chain and the formation contract fail. |
| `lem-kitaev-almost-idemp-audit` | AI still exports the explicit extended structure and linear estimate and has Kitaev as a transitive proof dependency, but AI's *contract* does not export `tilde-Phi^2=tilde-Phi`.  The definition exports only the formula. | The formation row's exact-idempotence conclusion cannot be consumed at contract level.  The direct edge remains necessary. |
| `lem-thmainext-conditional` | The definition can record types `B,v,u` only inside an already given datum; Kitaev/AI produce `A` but no factor algebra or isomorphism. | No nonempty `S` with `B,v`, no extended `C_E*epsilon_AI`-isomorphism, no bijectivity, and no `u=v^(-1)`. |

Thus none of the three producer conclusions survives *via the definition*.
All existence and estimates are in the formation contract, and deleting the
corresponding result makes that contract unprovable rather than silently
true by unpacking.

## 4. Attack 3 — formation-lemma soundness

**VERDICT: MATHEMATICALLY CLEARED; OPERATIONAL PLAN NEEDS FINDING 3.**

The contract is derivable from its declared dependencies:

1. choose the universal `(C_A,eta_A)` from AI and `(C_E,epsilon_E)` from
   MAIN once, before input data, and assemble the scalar header;
2. `eta<=rho_id^corr` gives `eta<=1/8<1/4`, `eta<=eta_A`, and
   `C_A*eta<=epsilon_E` (the displayed formula makes `C_A>0`);
3. Kitaev gives `tilde-Phi^2=tilde-Phi` for the same `Phi,eta`;
4. AI gives the exact displayed `A,star,epsilon_AI`, the extended structure,
   and `epsilon_AI<=C_A*eta`; nonnegativity follows directly from the
   displayed maximum on this domain;
5. finite-dimensional `H` makes `B(H)` and its range `A` finite-dimensional;
6. MAIN applied to that same `A` gives one finite-dimensional `B` and one
   extended `C_E*epsilon_AI`-isomorphism `v:B->A`; and
7. package precisely these outputs with `u=v^(-1)` as `S`.

The quantifier order is genuinely

```text
exists W_RF, for every (H,Phi,eta), exists (B,v,S), ...
```

not a per-input reselection of the scalar witnesses.  Nonvacuity is delivered
for every nonzero finite-dimensional `H`, every UCP `Phi`, and every
`0<=eta<=rho_id^corr` satisfying the cb-defect antecedent.  The later packet
rows are nonvacuous on their smaller radii because
`eta_K<=rho_fac<=rho_2<=rho_T<=rho_id^corr` and rows 5, 6, 8, and 9 are
existential producers imported directly by the eventual parent.

The proposed 10-node/3-round target with cap 14 is plausible: it mirrors the
already validated analytic setup subtree in the raw-identities workspace and
keeps the three analytic providers external.  What is missing is not budget
but the explicit formation-workspace execution phase in finding 3.

## 5. Attack 4 — independent byte-suffix re-diff

**VERDICT: CLEARED, 15/15 BYTE-EQUAL.**

I independently extracted each v2 code-block contract, removed the new
prefix by locating the landed title/suffix boundary, and compared the
remaining bytes directly with the live shard's one-line `contract:`.  The
SHA256 prefixes below are over the extracted suffix and equal the hashes of
the landed text.

| row | result id | suffix SHA256[:16] | result |
|---:|---|---|---|
| 1 | `lem-routef-raw-factor-norms` | `880d2f981e98975d` | BYTE-EQUAL |
| 2 | `lem-routef-raw-factor-units` | `41b441234ed6df2c` | BYTE-EQUAL |
| 3 | `lem-routef-raw-factor-identities` | `ada66693219c992b` | BYTE-EQUAL |
| 4 | `lem-routef-raw-product-estimate` | `2f4d8c2c0f9fc278` | BYTE-EQUAL |
| 5 | `lem-routef-delta-prime-closeness` | `be0654b5690e4e7a` | BYTE-EQUAL |
| 6 | `lem-routef-delta-normalization-closeness` | `38c4d6c810ee3c30` | BYTE-EQUAL |
| D2 | `lem-routef-degree-two-estimate` | `c9af7e4c3203eec8` | BYTE-EQUAL |
| 7 | `lem-routef-delta-phi-product` | `1967e28e3eec1204` | BYTE-EQUAL |
| D3 | `lem-routef-degree-three-estimate` | `fee246d3fe2936bd` | BYTE-EQUAL |
| 8 | `lem-routef-upsilon-prime-closeness` | `f19e937db51bfdf8` | BYTE-EQUAL |
| 9 | `lem-routef-upsilon-normalization-closeness` | `70bc606cc2fbd653` | BYTE-EQUAL |
| 10 | `lem-routef-delta-upsilon-telescope` | `a4af5c461ccb7517` | BYTE-EQUAL |
| 11 | `lem-routef-multiplicative-telescope` | `29f16e63504d4a17` | BYTE-EQUAL |
| 12 | `lem-routef-upsilon-delta-telescope` | `371d8380b51f8c23` | BYTE-EQUAL |
| 13 | `lem-routef-k-finiteness` | `abb2c54dabd9c5aa` | BYTE-EQUAL |

Row 14 is deliberately excluded: v2 replaces, rather than prefixes, its
mathematical suffix.

## 6. Attack 5 — row 14 scalar-interface revision

**VERDICT: CLEARED.  NO OVERCLAIM OR UNDERCLAIM.**

The revised row exports exactly the scalar arithmetic of ratified
`DESIGN-LEDGER-DOMAINS-v2.md` §3.5:

| ratified scalar fact | v2 row-14 text |
|---|---|
| `eta_K=min{rho_fac,(24K)^(-1),1}>0` | literal |
| `eta<=rho_fac` and `eta<=min{(24K)^(-1),1}` | literal |
| `3Keta<=1/8<1` | literal |
| `3Keta/(1-3Keta)<=4Keta<=1/6<1/2` | literal |

It asserts no `Q,D,J,Q_C,A,M`, no commutativity, no F2/F3 conclusion, and no
PRH admissibility.  Accordingly the F2/F3/PRH result ids and the
stochastic/retract definitions correctly leave the row.

It remains sufficient for the strengthened K-ledger.  There the F0 rows bind
the same `Q,Phi,eta`; formation and rows 5/6/8/9 construct the same
`B,Delta,Upsilon` packet; rows 10--13 supply the three estimates and common
`K`; row 14 supplies F2's threshold and F3's denominator guard; F2 binds and
produces `A,M`; F3 gives the rational retract estimate; and PRH consumes the
same `Q,A,M,K,eta`.  No map interface belongs in row 14 itself.

## 7. Attack 6 — dependency-edge and cycle audit

**VERDICT: CLEARED.**

Every edge required by v1 finding 4 is present directly:

| consumer | required additions | v2 `deps:` locus | result |
|---|---|---|---|
| row 7 | row 5 | line 414 | PRESENT |
| row 8 | row 5 | line 434 | PRESENT |
| row 9 | rows 5, 6 | line 444 | PRESENT |
| row 10 | rows 5, 8 | line 454 | PRESENT |
| row 11 | rows 5, 6, 8 | line 465 | PRESENT |
| row 12 | rows 5, 8 | line 476 | PRESENT |
| row 13 | rows 5, 6, 8, 9 | line 488 | PRESENT |
| row 14 | rows 5, 6, 8, 9 | line 500 | PRESENT |

I parsed the live 364-node graph, injected the proposed formation node and all
sixteen replacement `deps:` lists, and reran a full DFS: 365 nodes, zero
missing imports, zero cycles.  Injecting the future strengthened K-ledger
dependency block also gives zero cycles.  All new family edges point left in

```text
formation, 1, 2, 3, 4, 5, 6, D2, 7, D3, 8, 9, 10, 11, 12, 13, 14.
```

“Supplied” is now a contract-level producer relation backed by a direct edge,
and every later row spells out which earlier output its map is formed from.
There is no free-standing prose notion of a “successive packet”.  This is the
direct-edge option allowed by v1 finding 4 and is canonical enough for the
linker and future af externals.

## 8. Attack 7 — binder audit

**VERDICT: NOT-CLEARED; EXACTLY TWO FREE VARIABLES.**

| row | displayed matrix/amplification variables | disposition |
|---|---|---|
| 1 | `n>=1`, `X in M_n(S.B)` | bound |
| 4 | `n>=1`, `X,Y in M_n(S.B)` | bound |
| D2 | `n>=1`, `X,Y in M_n(S.B)` | bound |
| 7 | `n>=1`, `X,Y in M_n(S.B)` | bound |
| D3 | `n>=1`, `X,Y,Z in M_n(S.B)` | bound |
| 11 | `n>=1`, `X,Y in M_n(S.B)` | bound |
| 6 | `X` in `Delta(X)=...` | **FREE**; bind `X in S.B` |
| 9 | `X` in `Upsilon(X)=...` | **FREE**; bind `X in B(H)` |

No other proposed contract displays an unbound `X,Y,Z` or an unbound
amplification index.  The definition's `q>=1` amplification convention is
explicitly universal and its bilinear-operation field types both arguments.

## 9. Attack 8 — vocabulary and provisioning

**VERDICT: L2 CLEARED; TWO LIVE WORKSPACES CLEARED; FORMATION WORKSPACE
PLAN NOT-CLEARED.**

The new definition's term and aliases do not collide with the current 46
definition shards.  Its frontmatter satisfies the `check-defs` schema; at
design time `draft` would produce only the intended warning, while an
authorized post-ratification landing must record the sign-off and lock it.
The body references rather than redefines:

- `def-ucp-map` (which already contains both CP and UCP vocabulary),
- `def-extended-epsilon-cstar-algebra`, and
- `def-extended-delta-inclusion`.

The two live workspaces currently contain one copy each of the two extended
definitions and no copy of either the proposed setting definition or
`def-ucp-map`.  Section 5.1's “add exactly once” plan is therefore correct;
retaining the historical `def-almost-idempotent` without citing it is
compatible with append-only af semantics.

The new formation workspace is missing from the plan.  At seeding it must
provision exactly once:

```text
def-routef-raw-factor-setting
def-ucp-map
def-extended-epsilon-cstar-algebra
def-extended-delta-inclusion
```

and exactly one external for each declared provider, with literal paths:

```text
proofs/lem-kitaev-almost-idemp-audit
proofs/lem-routef-ai-defect-linearization
proofs/lem-thmainext-conditional
```

Preflight must run the same uniqueness check before every `def-add` and
`add-external` operation.

## 10. Attack 9 — af continuation plans

**VERDICT: MECHANICS AND BUDGETS PLAUSIBLE; PLAN NEEDS FINDINGS 2--3.**

The live state matches the design:

- `lem-routef-raw-factor-norms`: 20 nodes, 13 validated, 7 pending;
- `lem-routef-raw-factor-identities`: 5 nodes, 4 validated, root pending; and
- af version `0.1.6` permits amendment only of pending nodes.

The prior empirical amendment test and the current ledger semantics support
the claim that amending a pending node preserves validated descendants.
That is mechanical preservation only.  Every amended node and ancestor still
requires fresh hostile review.

For raw norms, the seven named pending nodes are exactly the seven currently
pending nodes.  Moving formation/same-output obligations into those ancestors
is compatible with retaining the validated analytic and scalar children.
The 20-node target, cap 22, six-round allowance is plausible.

For raw identities, only root amendment is mechanically necessary, but the
advertised use of node `1.1` is invalid for the same-witness reason in finding
2.  Formation plus universal algebraic node `1.2` is sufficient; alternatively
one new fixed-`S` bridge fits the stated 6-node/2-round contingency.  The
5-node/one-round optimistic budget therefore remains plausible after the
wording correction.

Neither continuation may start until the formation row has itself completed
the fresh-prover/fresh-verifier phase described in finding 3.  Preserving old
badges cannot substitute for that external's validation.

## 11. Attack 10 — fresh under-specification and full landing mechanics

**VERDICT: MATHEMATICAL PACKAGE CLOSED AFTER FINDING 1; LANDING PACKAGE
INCOMPLETE UNTIL THE FOLLOWING EXACT MANIFEST IS ADOPTED.**

The hostile hunt found no additional missing analytic estimate, radius, map
seam, or dependency edge.  It did find that v2 §6.1 is not a complete
implementation manifest.  An authorized implementation must enumerate and
perform the following serial phases.

### 11.1 Registry/definition landing phase

1. Add the user-ratified, locked
   `definitions/def-routef-raw-factor-setting.md`.
2. Add the formation shard initially as `status: stated`, `af: none`, with
   provenance extended to cite this audit and the user ratification.
3. Apply the sixteen corrected `contract:`, `defs:`, and `deps:` lines,
   including the two `X` binders from finding 1 and the row-14 replacement.
4. Replace the row-3 stale body sentence exactly as v2 lines 370--373 direct.
5. Update all sixteen `provenance:` lines and status notes: the whole
   contracts are no longer verbatim from the old LEDGER-DOMAINS design; only
   fifteen suffixes are.  Record the v2 rescope design, this audit, and the
   ratification.  Reconcile the already-stale `af: none` body wording in the
   two `af: seeded` shards.
6. Update `scripts/land-ledger-domains-rows.py` with the same contracts,
   defs, deps, row-3 sentence, provenance, and body wording.  It is the
   retained reproducer and currently hard-codes the rejected pre-rescope
   package.
7. Add `lem-routef-raw-factor-setting-formation` to the fenced whitelist in
   `report/UNWIRED.md`.  Without this exact edit,
   `check-provenance.py --check` hard-fails the new unanchored row.

### 11.2 Formation elevation phase

1. Seed the exact formation root and provision the definitions/externals in
   §9 above exactly once.
2. Run the 10-node/3-round, cap-14 adversarial elevation with fresh prover and
   separate fresh verifier(s).
3. Export, register/verify the oracle, and mechanically change only the
   formation row to `status: proved`, `af: validated` if and only if the af
   ledger validates cleanly.
4. Regenerate and gate before either live tree consumes the external.

This future phase does not alter the requirement that all sixteen family
rows remain `stated` at the design landing.

### 11.3 Live continuation phase

1. Provision the two live workspaces exactly as v2 §5.1.
2. Amend raw norms as §5.2 specifies.
3. Amend raw identities using the corrected formation-plus-node-`1.2` plan
   from finding 2, not the invalid same-witness instantiation of node `1.1`.
4. Obtain fresh bottom-up hostile verdicts; no preserved child badge validates
   an amended ancestor.

### 11.4 Lockstep/gate phase

Regenerate at least:

```text
definitions/INDEX.md
argument/INDEX.md
argument/DAG.md
report/generated/defs/*
report/generated/dag/*
report/generated/stats/* (with the deliberate snapshot refresh)
```

Then reconcile `HANDOFF.md`, the current proof-strategy sketch/pointer, and
`docs/worklog.md` in the authorized implementation session, run the full
`sh scripts/check-all.sh` gate, and follow the repository's independent
review/commit/push protocol.  These are not optional follow-ups under Rule 9.

The live baseline checks used for this audit were green apart from existing
warnings: `check-defs` 0 errors, `argument.py --check` 0 errors, and
`check-provenance.py --check` 0 errors.  The hard UNWIRED failure described
above follows directly from `check_anchor`: every new unanchored registry id
must be report-anchored or fenced in `report/UNWIRED.md`.

## 12. Final disposition

**LAND-WITH-EXACT-CORRECTIONS** means:

- fold findings 1--4 into the design/authorized landing instructions;
- do not land the current v2 text as-is;
- do not amend either live af tree until the formation row is independently
  validated;
- do not release the strengthened-K-ledger DO-NOT-REWIRE guard in this
  package; and
- do not promote any of the sixteen rows as a consequence of this audit.

Nothing in this file proves or promotes a definition, lemma, af node, parent,
or root.
