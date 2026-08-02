# DESIGN-M24-NONTRIVIALITY

Status: **DESIGN ONLY — non-rigorous, not user-ratified, and not an elevation verdict.**

Date: 2026-08-02
Role: fresh independent design mathematician
Scope: repair the missing lower bound in M24 without changing any T0 result, locked definition, or downstream contract

## Executive recommendation

Choose **option (a)**: add one ledger-bound provider, `lem-maincb-corner-nontriviality`, and amend only M24's dependency list and proof architecture. Keep the M24 contract byte-for-byte unchanged.

The provider should prove, for the exact M18 witness ledger and exact Stage-1 map, that each atomic image is a nonvanishing approximate projection and that the unit of the M04 singleton corner algebra is nonzero. Hence `dim S_{P_j} >= 1`. The already validated strict-refinement argument supplies `dim S_{P_j} <= 1`, so equality follows. This route uses the existing M04/M18/M20 threshold chain; it needs no new definition, no new universal constant, no T0 amendment, and no appeal to the paper's unsupported sentence “It is clear that ...”.

Option (b) is rejected: the weakened conclusion `dim S_{P_j} <= 1` does not satisfy the literal one-dimensional-image premises of M10, M25, M19-S3, M26, and M27, and it does not make the relation in `def-maincb-partition-state` reflexive. Option (c) has no distinct viable form: M22, M23, and M18 are frozen T0 rows, and any additive premise strong enough to repair M24 is precisely a new provider of type (a).

---

## Deliverable 1 — consumer survey and option judgment

### 1.1 Exact downstream use of M24

The dependency path from M24 to M28 is not merely an upper-dimension path:

| Step | Frozen consumer/interface | Exact need | What fails with only `dim S_{P_j} <= 1` |
|---|---|---|---|
| 1 | M22, `lem-maincb-maximal-reset-selection` | Select one maximal admissible `w:C^m->A` for the fixed ledger `W`. | Nothing yet; this fixes the witness to which every later step must refer. |
| 2 | M24, `lem-maincb-stage1-maximality` | Conclude `dim S_{P_j}=1` for every `P_j=w(e_j)`. | The zero-dimensional case remains possible. |
| 3 | M10, `lem-maincb-corner-equivalence` | Its contract begins with “for every finite family of one-dimensional t-projections”. | A family with `dim S_{P_j}=0` is outside the premise. |
| 4 | `def-maincb-partition-state` | Define `j ~ k` by `dim S_{P_j,P_k}=1`, and use its class family when this is an equivalence relation. | Reflexivity is `dim S_{P_j,P_j}=dim S_{P_j}=1`; an atomic zero corner prevents an equivalence relation and therefore prevents a class family. |
| 5 | M25, `lem-maincb-one-class-extension` | The contract says “all atomic images are one-dimensional”. | `dim <= 1` is not that premise. |
| 6 | M27, `lem-maincb-stage3-finite-recombination` | The contract says “with one-dimensional atomic images and has classes C_1,...,C_q”. | Both the one-dimensional-image premise and the class-family premise can fail. |
| 7 | M27 -> M26 -> M19-S3 | M26 says “with one-dimensional atomic images”; M19-S3 has the same literal requirement. | The binary recombination engine cannot be called. |
| 8 | M28, `lem-maincb-structural-assembly` | Uses M24, M10, M25, and M27 to assemble `B=oplus_C M_{|C|}` and the final reset isomorphism. | The direct-sum indexing classes and their matrix-block models have not been established. |

M28 therefore uses the equality in M24 in two logically separate ways: it supplies the one-dimensional hypotheses of the Stage-2/Stage-3 providers, and it supplies reflexivity for the class relation. Neither use is discharged by an upper bound alone.

### 1.2 Judgment on the three options

| Option | Judgment | Reason |
|---|---|---|
| (a) Add a nontriviality provider | **SELECT** | It repairs exactly the missing implication `S_{P_j} != 0`, preserves the M24 and M28 interfaces, and can be typed through the already validated W-ledger chain. |
| (b) Weaken M24 to `dim S_{P_j} <= 1` | **REJECT** | It breaks the literal contracts identified above and makes the partition relation potentially non-reflexive. Repairing every consumer would be a broad, unjustified redesign, not a local M24 repair. |
| (c) Strengthen existing M24 dependencies | **REJECT AS A DISTINCT OPTION** | M22, M23, and M18 are frozen T0 results and none exports compressed-corner nontriviality. Adding a new strong premise without changing them is exactly option (a); amending them would invalidate T0 artifacts. |

### 1.3 Defect-record closure

| Verifier challenge | Design response |
|---|---|
| `ch-94ae993f6abc0f5b` | Accept the challenge exactly: neither `P_j!=0` nor a nonexistent supplied partition state proves `S_{P_j}!=0`. The new provider instead proves `P_j` is nonvanishing and independently proves that the algebra unit furnished by M04 is a nonzero member of the exact singleton corner. |
| `ch-7411a0325c917f52` | Add the missing T0-shaped import before rebuilding M24. The new lower-bound child and the existing M23 upper-bound child give the two integer inequalities needed by the unchanged root. |
| `ch-37eff8dcb9a3b5d1` | Preserve the rejection of scope drift. The M24 root is not weakened. |

### 1.4 Why the nearby banked tools do not themselves close the gap

- `lem-compcb-corner-algebra`, `lem-compcb-compressed-unit-norm`, and `lem-compcb-compressed-unit-action` exhibit the right generic mechanism: the compressed corner has unit `Co_P(P)` and that unit is close to norm one. Their generic smallness parameter is not explicitly a field of the MAIN ledger, however. The validated M04 row is the already typed, ledger-compatible wrapper for this use.
- `lem-maincb-compressed-corner-unit-comparison` compares the compressed unit to the projection, but its separate coefficient threshold is likewise not explicitly synchronized in `W`; it is unnecessary once M04 is used.
- `lem-extcb-one-dimensional-corner-dimension` and `lem-extcb-corner-dimension-additivity` provide upper-dimension and additivity facts. They do not exclude the zero corner.
- `lem-stage1-rectified-nontrivial-projection` assumes `1 < dim X` to manufacture a nontrivial projection in `X`. Using it to prove merely `dim X >= 1` would be circular and would conflate the Stage-1 splitting tool with the missing base nonvanishing fact.

---

## Deliverable 2 — proposed registry contracts and wiring

### 2.1 New provider row

Proposed id: `lem-maincb-corner-nontriviality`

The contract below is one physical ASCII line and introduces no explicit numerical universal constant:

```text
Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, w:C^m->A is an extended W.c0_cb*epsilon-inclusion, and e_j is any projection-basis element of C^m, then P_j=w(e_j) is a W.c0_cb*epsilon-projection satisfying | ||P_j||-1 | <= W.c0_cb*epsilon and hence is nonvanishing, while S_{P_j} contains a nonzero element and therefore dim S_{P_j} >= 1.
```

Proposed registry metadata:

| Field | Design |
|---|---|
| id | `lem-maincb-corner-nontriviality` |
| contract | The exact one-line contract above |
| defs | `def-maincb-witness-ledger; def-projection-basis; def-epsilon-cstar-algebra; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-compressed-corner` |
| deps | `lem-maincb-reset-constant-ledger; lem-maincb-structural-domain-ledger; lem-maincb-direct-corner-envelope; lem-maincb-witness-arithmetic` |
| initial status / af | `stated / seeded` |
| source | `refs/kitaev-2405.02434/approximate_algebras.tex:407-456,917-929,1054-1065,1067-1084,1367-1368,1417-1428` plus finite-dimensional linear algebra |
| budget | target `6` nodes / `3` rounds / hard cap `10` |
| flag | **NEW additive provider** |

The neighboring sentence at line `1066` is motivation only. It is deliberately excluded from the provider's exact external ranges and must not be registered or used as a proved external claim: the paper says nontriviality is “clear” without supplying the missing implication. The proposed proof instead derives a nonzero algebra unit from the formal unit-norm axiom and the validated ledger inequalities.

### 2.2 Amended M24 row

The M24 contract must remain byte-for-byte equal to the current registry contract:

```text
Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and w:C^m->A has maximum source dimension among all extended W.c0_cb*epsilon-inclusions satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then every projection-basis image P_j=w(e_j) satisfies dim S_{P_j}=1.
```

Proposed metadata after the provider is T0:

| Field | Design |
|---|---|
| id | `lem-maincb-stage1-maximality` |
| contract | **UNCHANGED**, exact line above |
| defs | **UNCHANGED**: `def-maincb-partition-state; def-maincb-witness-ledger; def-projection-basis; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion` |
| deps | `lem-maincb-maximal-reset-selection; lem-maincb-stage1-strict-refinement; lem-maincb-reset-constant-ledger; lem-maincb-corner-nontriviality` |
| status / af before re-elevation | `stated / seeded` |
| source | Existing M24 provenance remains; append the ratified repair-design locus and the new provider dependency |
| budget | target `5` nodes / `2` rounds / hard cap `9` |
| flag | **AMENDED: deps, proof tree, and budget only; contract unchanged** |

For landing review, the complete package is consolidated below. Each contract cell is a one-physical-line ASCII contract.

| ID | One-line contract verbatim | Defs | Deps | Exact provenance | Budget (target nodes/rounds/hard cap) | Flag |
|---|---|---|---|---|---|---|
| `lem-maincb-corner-nontriviality` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, w:C^m->A is an extended W.c0_cb*epsilon-inclusion, and e_j is any projection-basis element of C^m, then P_j=w(e_j) is a W.c0_cb*epsilon-projection satisfying | ||P_j||-1 | <= W.c0_cb*epsilon and hence is nonvanishing, while S_{P_j} contains a nonzero element and therefore dim S_{P_j} >= 1.` | `def-maincb-witness-ledger`; `def-projection-basis`; `def-epsilon-cstar-algebra`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion`; `def-delta-projection`; `def-compressed-corner` | `lem-maincb-reset-constant-ledger`; `lem-maincb-structural-domain-ledger`; `lem-maincb-direct-corner-envelope`; `lem-maincb-witness-arithmetic` | `refs/kitaev-2405.02434/approximate_algebras.tex:407-456,917-929,1054-1065,1067-1084,1367-1368,1417-1428`; finite-dimensional linear algebra | `6/3/10` | **NEW** additive provider |
| `lem-maincb-stage1-maximality` | `Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= W.epsilon_MAIN and w:C^m->A has maximum source dimension among all extended W.c0_cb*epsilon-inclusions satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, then every projection-basis image P_j=w(e_j) satisfies dim S_{P_j}=1.` | `def-maincb-partition-state`; `def-maincb-witness-ledger`; `def-projection-basis`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-maincb-maximal-reset-selection`; `lem-maincb-stage1-strict-refinement`; `lem-maincb-reset-constant-ledger`; `lem-maincb-corner-nontriviality` | Existing M24 provenance at `refs/kitaev-2405.02434/approximate_algebras.tex:1417-1426`; append this ratified repair-design locus | `5/2/9` | **AMENDED deps/proof/budget only; contract byte-UNCHANGED** |

### 2.3 M28 row

No M28 contract, definition, dependency, provenance, or budget amendment is proposed. Its present dependency on M24 is the correct abstraction boundary. Keep the existing M28 elevation budget at target `9` nodes / `3` rounds / hard cap `13`.

---

## Deliverable 3 — definition decision

### 3.1 Reused definitions

| Definition | Role in the repair |
|---|---|
| `def-maincb-witness-ledger` | Types the single fixed `W`, its MAIN threshold, the corner-envelope fields, and reset scale. |
| `def-projection-basis` | Types `e_j` as a nonzero norm-one projection in `C^m`; no anonymous coordinate idempotent is introduced. |
| `def-epsilon-cstar-algebra` | Supplies the approximate-unit norm axiom used to show the corner unit is nonzero. |
| `def-extended-epsilon-cstar-algebra` | Types the ambient algebra and the extended structure on `S_{P_j}` supplied by M04. |
| `def-extended-delta-inclusion` | Supplies linear, star, multiplicative, norm, and unit control for `w`. |
| `def-delta-projection` | Types the conclusion that `P_j` is a nonvanishing approximate projection. |
| `def-compressed-corner` | Fixes the exact compressed space `S_{P_j}`; the new contract does not require a definite-description name for its unit. |
| `def-one-dimensional-delta-projection` | Not needed by the new provider itself, but remains the existing semantic interface reached after M24 combines `dim >= 1` and `dim <= 1`. |
| `def-near-positive-projection` | Assessed and unchanged; it is not needed for this atomic nonvanishing/unit argument. |
| `def-maincb-partition-state` | Remains unchanged; it explains why equality, rather than only an upper bound, is required downstream. |

### 3.2 New-definition judgment

**Zero new definitions.** “Nonvanishing” is already part of `def-delta-projection`, the compressed unit and space are already canonical in `def-compressed-corner`, and the witness synchronization is already expressed by `def-maincb-witness-ledger`. A new “nonzero corner” or “atomic support” definition would duplicate existing vocabulary and invite drift.

No locked definition is to be amended.

---

## Deliverable 4 — proof architecture and node budgets

### 4.1 New provider: `lem-maincb-corner-nontriviality`

Recommended AF tree: target `6` nodes, `3` prover/verifier rounds, hard cap `10` nodes.

1. **Root.** Fix exactly the `W` supplied by M18, an admissible `A,w`, and a projection-basis element `e_j`; set `d=W.c0_cb*epsilon` and `P_j=w(e_j)`.
   1. **Same-instance ledger alignment.** Use M18 to retain the particular M04 witnesses `L^0,e_env^0` chosen before `W`, with `W.L>=L^0` and `W.e_env<=e_env^0`. Use M20 to obtain `epsilon<=W.e_env` and `W.L*epsilon<=W.K_call*epsilon<=W.r_reset`. No witness may be reselected.
   2. **Atomic image is nonvanishing.** From the projection-basis clauses, `e_j=e_j^*=e_j^2` and `||e_j||=1`. Apply the star, product, and two-sided norm clauses of the extended `d`-inclusion to get the `d`-projection inequalities and `| ||P_j||-1 |<=d`. This is the second, quantitative alternative in the existing nonvanishing definition; it is stronger than the scratchpad's bare `P_j!=0` statement.
   3. **Corner-envelope threshold.** M20 gives `epsilon<=W.e_env<=e_env^0`; hence M04 applies to the singleton `U={j}` and makes the exact vector space `S_{P_j}` an extended `L^0*epsilon`-C*-algebra. Denote the unit furnished by this algebra structure locally by `I_{S_{P_j}}`; the registry contract does not bind it by definite description.
   4. **The corner-algebra unit is nonzero.** From the chosen ledger and witness arithmetic,
      `L^0*epsilon <= W.L*epsilon <= W.K_call*epsilon <= W.r_reset`.
      The witness-arithmetic contract fixes `K_disp` positive and has `D_*>=1`; therefore the recorded term `[2*(1+K_disp)*D_*]^{-1}` in `W.r_reset` gives `L^0*epsilon<=1/2`. The base approximate-unit axiom then gives `| ||I_{S_{P_j}}||-1 |<=L^0*epsilon<=1/2`, so `||I_{S_{P_j}}||>=1/2` and `I_{S_{P_j}}!=0`.
   5. **Dimension conclusion.** By its type, this nonzero unit belongs to `S_{P_j}`. Since the corner space is finite-dimensional, `dim S_{P_j}>=1`. Combine with step 2 for the full root contract.

The numerical `1/2` occurs only inside the proof arithmetic; it is not a registry-contract constant. If the verifier prefers not to expose this derived value, the same node may state only that the recorded reset term makes `L^0*epsilon<1`, which is all nonzeroness needs.

Per-node imports and analytic loci:

| Node | Exact imports | Analytic source locus |
|---|---|---|
| Root | All seven row defs; M18 for the definite description of `W` | None; binder/typing node |
| 1.1 same-instance ledger | M18; M20; `lem-maincb-witness-arithmetic`; `def-maincb-witness-ledger` | None; finite max/min arithmetic exported by the T0 rows |
| 1.2 nonvanishing image | `def-projection-basis`; `def-extended-delta-inclusion`; `def-delta-projection` | `refs/kitaev-2405.02434/approximate_algebras.tex:443-456,917-929` |
| 1.3 singleton corner | M04; M18; M20; `def-compressed-corner`; `def-extended-epsilon-cstar-algebra` | `refs/kitaev-2405.02434/approximate_algebras.tex:1054-1065,1067-1084,1367-1368,1428-1435` |
| 1.4 nonzero unit | M04; M18; M20; `lem-maincb-witness-arithmetic`; `def-epsilon-cstar-algebra`; `def-extended-epsilon-cstar-algebra` | `refs/kitaev-2405.02434/approximate_algebras.tex:407-440,1477-1479` |
| 1.5 dimension | `def-compressed-corner`; the output of node 1.4 | Finite-dimensional linear algebra; no paper theorem imported |

### 4.2 Rebuilt M24 tree

Recommended AF tree: target `5` nodes, `2` prover/verifier rounds, hard cap `9` nodes.

1. **Root.** Fix the one M18 ledger `W`, the maximal `w`, and arbitrary `j`.
   1. **Admissible-family/maximality setup.** Recreate the formerly validated scratchpad node 1.1 verbatim in substance: define the admissible source dimensions using the exact extended-inclusion and near-unit clauses in the root, record that `w` is admissible, and record its maximality. This node must use the same `W` and same `w` as the root.
   2. **Lower bound.** Invoke `lem-maincb-corner-nontriviality` on that exact `W,w,e_j` to obtain `dim S_{P_j}>=1`.
   3. **Upper bound.** Recreate the formerly validated amended scratchpad node 1.3 verbatim in substance: if `dim S_{P_j}>1`, M23 supplies an admissible extended `W.c0_cb*epsilon`-inclusion `w_+:C^{m+1}->A` with the same near-unit threshold, contradicting maximality of `m`. Hence `dim S_{P_j}<=1`.
   4. **Equality.** Combine the two integer inequalities.

The formerly validated scratchpad node 1.2 (`P_j!=0`) is a true but insufficient statement. It should not be extended into the invalid inference `P_j!=0 => S_{P_j}!=0`, and it need not be transplanted into the fresh tree because the new provider subsumes it quantitatively.

Per-node imports and analytic loci:

| Node | Exact imports | Analytic source locus |
|---|---|---|
| Root | M18; all unchanged M24 defs | `refs/kitaev-2405.02434/approximate_algebras.tex:1417-1426` for theorem context only |
| 1.1 admissibility | M22; M18; `def-extended-delta-inclusion`; `def-projection-basis` | `refs/kitaev-2405.02434/approximate_algebras.tex:1417-1419` |
| 1.2 lower bound | `lem-maincb-corner-nontriviality` on the same `W,w,e_j` | None directly; consume the validated provider export |
| 1.3 upper bound | M23; node 1.1's fixed admissibility predicate | Consume M23's T0 export, whose analytic provenance is `refs/kitaev-2405.02434/approximate_algebras.tex:917-969,1194-1222,1419-1426` |
| 1.4 equality | Nodes 1.2 and 1.3 | Integer dimension arithmetic; no external |

### 4.3 Why the provider is atomic

The new row owns exactly one reusable bridge:

```text
ledger-sized atomic image -> M04 singleton algebra with nonzero unit -> nonzero compressed corner
```

It does not choose a maximal inclusion, split a corner, define a class relation, reset a map, or assemble blocks. Those remain in M22–M28. The proposed ten-node cap is below the repository soft cap and leaves room for a verifier-requested typing child without permitting the proof to balloon.

---

## Deliverable 5 — dimension-free ledger and threshold audit

### 5.1 Exact witness chain

The repair introduces no free threshold. It uses this already frozen chain:

1. M18 first fixes the M04 witnesses `L^0,e_env^0` for the selected `c0`, then furnishes one `W` with `W.c0_cb=c0`, `W.L>=L^0`, and `W.e_env<=e_env^0`.
2. M20 gives, for `epsilon<=W.epsilon_MAIN`,
   `epsilon<=W.e_env`,
   `W.L*epsilon<=W.K_call*epsilon`, and
   `W.K_call*epsilon<=W.r_reset`.
3. Therefore `epsilon<=e_env^0`, so the exact M04 witness instance applies, and `L^0*epsilon<=W.r_reset`.
4. `lem-maincb-witness-arithmetic` records
   `W.r_reset <= [2*(1+K_disp)*D_*]^{-1}` with `D_*>=1`.
   Its contract fixes `K_disp` as positive and finite. Thus the right side is at most `1/2`, and in particular below `1`.
5. The unit norm defect in the singleton corner is consequently below `1`, proving the unit of its M04 algebra structure is nonzero.

Every quantity is a universal witness already selected in M18 or a field of the one `W`. There is no dependence on `dim A`, `m`, the index `j`, amplification, block size, class count, or stage count.

### 5.2 No hidden `c0>=1` assumption

The proof must not infer smallness from `W.c0_cb*epsilon` by silently assuming `W.c0_cb>=1`. It does not need that inference. The projection's nonvanishing estimate comes directly from the inclusion norm clause at defect `d=W.c0_cb*epsilon`; the compressed-unit nonzeroness comes from `L^0*epsilon<=W.r_reset<1`. These are separate estimates.

### 5.3 No reset and no second witness

The provider and M24 use the original Stage-1 `w`; neither performs a reset. Hence no reset-output provider belongs in either dependency list. If an AF prover nevertheless introduces a reset, that is a design violation. In later consumers where a reset is genuinely needed, the established rule remains: use `lem-maincb-reset-output-typing` alone and keep one same-map witness; never combine it with a second reset provider.

---

## Deliverable 6 — exact source and external-provisioning plan

The local source is `refs/kitaev-2405.02434/approximate_algebras.tex`, whose checked payload hash matches the manifest. Provision only the precise clauses needed by the new provider:

| Local locus | Role | Use discipline |
|---|---|---|
| lines 407–440 | Approximate C*-algebra and unit norm clauses | Use the unit defect estimate after M04 has typed the singleton corner. |
| lines 443–456 | Approximate morphism/inclusion clauses | Use star, multiplication, two-sided norm, and unit control for `w`. |
| lines 917–929 | Approximate projection and nonvanishing alternatives | Match `P_j` to the existing nonvanishing definition through the norm-one preimage. |
| lines 1054–1065 and 1067–1082 | Compressed-space and corner-theorem context | Identify the exact vector space `S_{P_j}` and support the already banked M04 corner structure, deliberately excluding the unsupported sentence at line 1066. |
| lines 1068–1084, 1367–1368, 1428–1435 | M04's already banked direct-corner application | Consume through `lem-maincb-direct-corner-envelope`; do not restate M04. |
| lines 1417–1428 | Stage-1 maximality context | Motivation and M24 provenance only. |

The sentence at line 1066 asserting the corner/nonvanishing equivalence is **not** an external theorem and must not be provisioned as one. The AF provider must prove the needed nonzero-corner direction from the preceding formal clauses and the W-ledger inequalities.

External provisioning for the new workspace should be minimal and byte-matched:

- the seven reused definition shards listed in Deliverable 2;
- the exact validated exports of M04, M18, M20, and `lem-maincb-witness-arithmetic`;
- only the quoted source clauses above that are not already encapsulated by those exports;
- the elementary finite-dimensional fact that a vector space containing a nonzero vector has dimension at least one, treated at the repo's accepted common-knowledge level rather than invented as a project definition.

The M24 workspace should provision the new provider export plus its existing M22/M23/M18 imports. It should not independently provision line 1066 or re-prove the provider internally.

---

## Deliverable 7 — T0 non-invalidation and re-seed/elevation sequence

### 7.1 Non-invalidation table

| Frozen artifact | Proposed treatment | Why no invalidation occurs |
|---|---|---|
| M04 direct corner envelope | Consume exact export | Contract, tree, externals, and verdict unchanged. |
| M18 reset constant ledger | Consume exact export | Same frozen witness order and same `W`; no field or contract amendment. |
| M20 structural domain ledger | Consume exact export | Its inequalities are used verbatim; no strengthening. |
| Witness arithmetic | Consume exact export | Its recorded reset term is used verbatim; no amendment. |
| M22 maximal reset selection | Consume in M24 | Same maximal `w`; no contract or proof change. |
| M23 strict refinement | Consume in M24 | Same contradiction producing source dimension `m+1`; no change. |
| M10 corner equivalence | Downstream consumer only | Its one-dimensional premise is preserved rather than weakened. |
| M25, M19-S3, M26, M27 | Downstream consumers only | Their restored one-dimensional-image clauses stay byte-identical. |
| `lem-compcb-corner-algebra` | Indirectly consume through M04 | Its generic contract/export and registered externals stay untouched. |
| `lem-compcb-compressed-unit-norm` and `lem-compcb-compressed-unit-action` | Architecture cross-check only | Neither is directly imported, amended, or re-provisioned into a validated workspace. |
| `lem-maincb-compressed-corner-unit-comparison` | Architecture cross-check only | Its separate threshold is not spliced into `W`; contract/export stay untouched. |
| `lem-extcb-one-dimensional-corner-dimension` and `lem-extcb-corner-dimension-additivity` | Consumer/tool survey only | They are neither strengthened nor used to infer a lower bound. |
| `lem-stage1-rectified-nontrivial-projection` | Explicitly rejected for this role | Its `dim>1` premise is not changed or used circularly. |
| Every locked definition listed in Deliverable 3 | Reuse or survey only | Zero definition edits and zero duplicate terms. |
| Existing byte-matched externals in validated workspaces | Read-only | No ledger, external payload, export, or verdict is edited; the new provider gets a new workspace. |
| M24 | Fresh re-seed after deps-only amendment | It is currently `stated/seeded`, not T0; its root contract remains byte-identical. |
| M28 | No row amendment | It remains parked until M24 is T0. |

No existing validated AF ledger, external file, export, or oracle verdict should be edited. The new provider receives a new workspace. M24 receives a clean re-seed rather than surgery on the challenged scratchpad ledger.

The status scan of the `lem-maincb-*` registry shards confirms the brief's boundary: the banked MAIN rows M01–M23 and M25–M27 are `status: proved`, `af: validated`; M24 and M28 alone are `status: stated`, `af: seeded`. The design changes no row on the banked side of that boundary.

### 7.2 Serial landing and elevation order

1. Subject this design to the required hostile independent design audit and user ratification. Apply corrections to the design before any registry work.
2. Land only the new provider shard with `status: stated`, `af: seeded`, the exact contract/defs/deps above, and source provenance. Seed its workspace from the registry contract.
3. Elevate `lem-maincb-corner-nontriviality` first. Require a fresh prover and a separate fresh hostile verifier; register and pass its external oracle before any status flip.
4. Only after the provider is T0, amend M24's deps by adding that provider. Keep the M24 contract byte-identical, discard/re-seed the challenged workspace cleanly, and provision only the ratified definitions and validated exports.
5. Elevate M24 with a fresh prover and separate verifier. Preserve the old scratchpad solely as forensic evidence; do not transplant its root or challenged inference. The admissibility and upper-bound subarguments may be recreated because their earlier verdicts show a viable shape, not because scratchpad status is inherited.
6. Before launching M28, run a preflight: M24 is T0; every M28 dependency is T0; the M28 workspace root byte-matches the unchanged registry contract; the registered oracle is present; and no dependency or contract drift has occurred. Then use the existing M28 target `9` nodes / `3` rounds / hard cap `13`.

At each landing, regenerate only the artifacts required by the repository workflow. This design document itself does not authorize any such landing.

---

## Deliverable 8 — adversarial elevation guidance and risk register

### 8.1 Prover/verifier guidance for the new provider

The prover's first child must freeze the exact same-instance constant chain. It should name the M04 witnesses selected before M18's `W`, record `W.L>=L^0` and `W.e_env<=e_env^0`, and never make an existential reselection after `W` is fixed.

The verifier should attack these points first:

1. Does the extended-inclusion definition genuinely give both the approximate-projection estimates and `| ||w(e_j)||-1 |<=d` for the exact typed projection-basis element?
2. Does M04 apply to the singleton `{j}` without already assuming `S_{P_j}!=0` or one-dimensionality?
3. Does the M04 conclusion really type the exact `S_{P_j}` as an extended `L^0*epsilon`-C*-algebra, so its furnished unit is an element of that same vector space? No identification with `Co_{P_j}(P_j)` is needed by the proposed contract.
4. Is the derivation `L^0*epsilon<1` available from the frozen contracts alone, with no hidden sign assumption on `K_disp`, no hidden `c0>=1`, and no second witness selection?
5. Is the final dimension conclusion about the same `S_{P_j}` and same `P_j=w(e_j)` as in the root?

### 8.2 Prover/verifier guidance for M24

- Make the first child the provider-first binder/admissibility child: fix the particular M18-supplied `W` before defining the admissible family, and introduce no fresh constant witness afterward.
- Use one shared `W`, one shared admissible-family definition, one shared maximal `w`, and one arbitrary but fixed `j`.
- Cite `def-extended-delta-inclusion` at the exact point where map typing or inclusion properties are used. Do not cite a generic morphism statement and silently upgrade it to an extended inclusion.
- Obtain the lower bound only by calling the new provider. Do not cite paper line 1066, do not infer it from `P_j!=0`, and do not manufacture a partition state.
- Obtain the upper bound only from the M23 refinement for the same `W,w,j`, then feed the resulting `w_+` into the admissibility predicate fixed in the first child.
- Use no pending-sibling citation: validate the lower-bound and upper-bound children independently before the equality/root assembly node cites either one.
- The typed-reset-provider-alone rule is vacuous here because no reset is part of M24. Do not import a reset provider; in particular, do not combine `lem-maincb-reset-output-typing` with M19-R. Also do not introduce a second maximal map, a fresh ledger, or a fresh M04 witness.
- Treat the scratchpad's old node 1.2 as insufficient evidence, even though its bare nonzero conclusion was validated.

### 8.3 Risk register

| Risk | Earliest hostile test | Required response |
|---|---|---|
| M04's singleton conclusion is being used circularly and secretly assumes a nonzero corner | Inspect the exact M04 export and its AF externals before accepting the provider's corner node | If circularity exists, stop; do not patch it inside M24. Redesign a lower generic provider and audit its T0 impact. |
| M04's algebra structure is not typed on the exact same singleton vector space `S_{P_j}` | Track the local singleton abbreviation through M04's root and require the unit to have type `S_{P_j}` | Reject any proof using a unit from a merely isomorphic or separately selected corner. |
| The cited big-`O` second alternative does not formalize the explicit lower-norm estimate as the predicate “nonvanishing” | Challenge the provider after granting the displayed norm inequality but withholding the vocabulary conclusion | Prefer a pre-existing typed bridge if one exists; otherwise stop for a separately audited bridge design rather than silently interpreting big-`O`. |
| The frozen W contracts do not export enough sign/order information to prove the unit defect is below one | Force the prover to derive every inequality from M18/M20/witness-arithmetic and point to the witness-arithmetic contract's “positive finite” binder; permit no prose appeal to post hoc enlargement | If that exported binder is insufficient under AF's exact typing, amend this design before landing; do not amend M18 casually. |
| The provider proves `P_j!=0` but not that `S_{P_j}` contains a nonzero element | Ask the verifier to erase the projection-nonzero sentence and see whether the corner-algebra unit proof still stands | Reject the proof unless the approximate-unit norm axiom independently establishes a nonzero element of the exact corner. |
| Provider and M23 act on different ledgers or different maps | Track `W,w,e_j,P_j` literally through every root and child statement | Reject any existential reselection; re-seed with a shared-instance root. |
| Weakening M24 is reintroduced as a shortcut | Check M10/M25/M19-S3/M26/M27 contracts and partition-state reflexivity before verdict | Reject the shortcut; equality is an interface requirement. |
| The provider workspace balloons by re-proving generic corner algebra | Enforce the `10`-node cap and inspect whether M04 is being consumed as a module | Factor only a genuinely missing typed bridge; otherwise restart with the M04 export. |
| M28 is launched against a stale M24 root or dependency graph | Byte-compare M28/M24 registry roots and run the linker/oracle preflight immediately before launch | Re-seed rather than editing a live AF ledger. |

### 8.4 Three most plausible ways this design could still be wrong

1. The exact validated M04 export may not expose the algebra structure on the same singleton `S_{P_j}` with sufficient typing precision to introduce its unit as an element of that vector space.
2. The exact formal meaning of the cited big-`O` “second alternative” may not permit AF to turn the explicit bound `| ||P_j||-1 |<=W.c0_cb*epsilon` into the word “nonvanishing” without an additional already-typed bridge, even though the quantitative estimate itself is stronger on paper.
3. A same-instance mismatch may remain between M18's selected M04 witnesses and the M04 instance consumed by the provider, despite the intended `W.L>=L^0`, `W.e_env<=e_env^0` wiring.

These are the first targets for the hostile design audit. None licenses weakening M24 or modifying a T0 row without a separately ratified redesign.

---

## Final design verdict

The minimal safe repair is one new additive provider plus a deps-only M24 re-seed. It preserves the exact theorem interface required by every downstream structural consumer, makes the missing lower bound explicit and reusable, and keeps all constants inside the already validated universal ledger. The repair should not be landed until a hostile auditor confirms the same-instance M04/W typing and the exported strict unit-norm bound.
