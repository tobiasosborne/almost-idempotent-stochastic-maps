# DESIGN — recorded-field identification repair

**Date:** 2026-08-01  
**Status:** DESIGN ONLY; non-rigorous; no registry mutation or status promotion  
**Issue:** `aism-4kof`  
**Decision:** use explicit recorded-field hypotheses at supplied-reset interfaces and explicit certificate selection at reset-producing interfaces; do not amend either locked state definition.

This design uses the literal current shards, not the earlier design paraphrases. In particular, it was checked against the complete evidence ledger at `proofs/lem-maincb-stage2-call-envelope/ledger/`, the locked definitions `def-maincb-reset-state`, `def-maincb-partition-state`, and `def-maincb-witness-ledger`, every M-row named in the brief, the five newly frozen T0 interfaces named in §6 below, and the pinned source `refs/kitaev-2405.02434/approximate_algebras.tex` (SHA256 `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`). The source supports the three-stage induction at lines 1414--1444 and the actual corner construction at lines 1428--1443. It does not define the project-original recorded fields; their binding is therefore an explicit contract-interface matter, not a cited theorem.

For explanatory prose only, write

\[
 \operatorname{ENV}(R):\quad \varepsilon_R\le W.L\varepsilon,
 \qquad
 \operatorname{RI}(R):\quad d_R\le W.c0_{cb}\varepsilon_R,
 \qquad
 \operatorname{UI}(R):\quad
 \lVert v_R(I_{B_R})-u_{A_R}\rVert\le W.c0_{cb}\varepsilon_R.
\]

`ENV` is not a proposed definition. It abbreviates one explicit contract clause. `RI` and `UI` likewise remain result clauses.

## 1. Deliverable 1 — repair-shape decision

### 1.1 The logical distinction exposed by the countermodel

There are two different situations.

1. **Supplied reset state.** Its `epsilon_U` is already a field of a datum. M04 proves that the same corner admits a small defect certificate; it does not alter that field and does not relate the recorded `d_U` or unit estimate to a fresh certificate. The exact `M_2` model at ledger nodes `1.1.2` and `1.1.5.1` proves that no such relation follows.
2. **Constructed reset state or raw-call target.** The result is existentially constructing the record. It may choose the M04-certified parameter as the new recorded field, and then pass that exact field through M19-R. This is a legal supply-time binding, not an identification of two pre-existing data.

The repair must therefore assume `ENV` when a state is supplied and export `ENV` when a state is constructed. For a fresh Stage-2 or Stage-3 target `R`, the raw-call target record is explicitly selected from the M04 certificate. It is not described as a field of the incoming `U`- or `V`-state.

### 1.2 Options and decision

| Shape | Benefit | Fatal cost / remaining obligation | Decision |
|---|---|---|---|
| (a) Explicit identification/bound hypotheses | Leaves all definitions and T0 contracts byte-stable; matches the distinction between supplied and constructed records; makes the induction invariant visible to verifiers. | `ENV` must be forwarded through M25--M27. | **Adopt.** |
| (b) State only actual M04 corner defects | Avoids talking about a supplied record. | M12 and frozen M13 consume the supplied reset's recorded `epsilon_U`; `RI/UI` relative to an arbitrary old record do not control `d_U` or the unit error relative to a fresh M04 certificate. It therefore does not close the consumers. | Reject. |
| (c) Amend `def-maincb-reset-state` or `def-maincb-partition-state` | Could make the binding structural. | Both definitions are locked and imported by banked T0 rows. It would turn a data carrier into an analytic assertion and force a revalidation cascade. | Reject and escalate if ever reconsidered. |

**Recommended repair shape:** option (a), specifically the inequality `recorded epsilon_R <= W.L*epsilon`. Equality to a distinguished “inherited defect” is unnecessary and would falsely suggest that an approximate-algebra defect parameter is canonical. At producing rows, choose a certificate satisfying the inequality; at consuming rows, require the inequality.

This satisfies the two typed-witness laws: each record used by a root has an explicit target and provider, and provider witnesses are fixed before receiving fields are enlarged or shrunk. No new numerical constant is introduced; every scalar guard in the repaired lines is inherited from the current contracts and the frozen witness arithmetic.

## 2. Deliverable 2 — complete per-row survey and cascade

The verdict column judges the literal current contract, not merely the intended proof.

| Row | Verdict | Recorded-field check | Action |
|---|---|---|---|
| M19-S2 `lem-maincb-stage2-call-envelope` | **DEFECTIVE AS WORDED** | The supplied `epsilon_U` is free, while `epsilon_R` is not a field of that supplied state. M04 only gives fresh certificates. Ledger nodes `1.1.2` and `1.1.5.1` validate the countermodel. | Add `ENV(U)` as a hypothesis; explicitly select the raw target record for `A_R` from M04; remove the claim that M04 bounds a pre-existing `epsilon_U`. |
| M19-S3 `lem-maincb-stage3-call-envelope` | **DEFECTIVE AS WORDED** | Identical defect for both supplied fields `epsilon_U,epsilon_V`; the target `epsilon_R` is fresh. | Add `ENV(U),ENV(V)` as hypotheses and explicitly select the raw target record for `A_R`. |
| M20 `lem-maincb-structural-domain-ledger` | **DEFECTIVE AS WORDED (typed interface)** | “Every atomic corner defect” has no displayed `A,w`, no selected certificate, and no reset record in scope. It repeats the same certificate/record ambiguity even though its scalar inequality is correct. | Make M20 purely scalar: retain `W.L*epsilon <= W.K_call*epsilon`; let M04-using rows select the actual certificate. |
| M12 `lem-maincb-cross-class-merging-datum` | **SOUND** | `epsilon_U,epsilon_V <= t` are literal hypotheses, not conclusions. Its two unit inequalities are also hypotheses. | Byte-unchanged. Repaired M19-S3 discharges every one of them. |
| M18 `lem-maincb-reset-constant-ledger` | **SOUND** | It binds provider witnesses and states conclusions only under each producer's respective hypotheses. It does not infer a supplied reset record from M04. | Byte-unchanged; its reference to the repaired S2/S3 hypotheses remains conditional. |
| M21 `lem-maincb-initial-reset-inclusion` | **SOUND** | The displayed `epsilon` is the ambient parameter of `A`, not a free reset-record field. | Byte-unchanged. |
| M22 `lem-maincb-maximal-reset-selection` | **SOUND** | It selects global maps at the displayed ambient parameter; no local recorded field appears. | Byte-unchanged. |
| M23 `lem-maincb-stage1-strict-refinement` | **SOUND** | Input and output defects are stated directly at the displayed global parameter. | Byte-unchanged. |
| M24 `lem-maincb-stage1-maximality` | **SOUND** | It quantifies over the same direct global-map class as M22/M23. | Byte-unchanged. |
| M25 `lem-maincb-one-class-extension` | **SOUND AS WORDED, BUT DOWNSTREAM-INSUFFICIENT AFTER THE S2/S3 REPAIR** | Its output state is existentially constructed, so its record can legally be selected at construction time; the old `epsilon_C <= W.K_call*epsilon` conclusion is true. But `W.K_call` is not dominated by `W.K2` or `W.K3`, so that conclusion cannot discharge `ENV(C)`. | Strengthen the same existential output to `epsilon_C <= W.L*epsilon <= W.K_call*epsilon`. No old conclusion is lost. |
| M26 `lem-maincb-binary-block-merge` | **DEFECTIVE AS WORDED** | Its supplied states have only `RI/UI`; arbitrary large records make those estimates too weak for M19-S3/M12. Its output also fails to export the bound needed by the next binary merge. | Add `ENV(U),ENV(V)` to the hypotheses and `ENV(U union V)` to the conclusion. |
| M27 `lem-maincb-stage3-finite-recombination` | **DEFECTIVE AS WORDED** | Its initial family does not satisfy the repaired M26 domain, and its conclusion does not export the final recorded-field bound used in M28's defect/unit comparison. | Add `ENV(C_a)` for every initial class and preserve `ENV` at the final union. |
| M28 `lem-maincb-structural-assembly` | **SOUND ONCE ITS PRODUCERS ARE REPAIRED** | It does not quantify a free local record. Repaired M25 and M27 provide `epsilon_J <= W.L*epsilon`; frozen witness arithmetic has `W.K_call >= W.L+1`. | Byte-unchanged. |

**Contract count:** six existing contracts change: M19-S2, M19-S3, M20, M25, M26, and M27. Five are defective/under-typed as worded; M25 is a sound producer whose export must be strengthened to keep the repaired consumers derivable. No definition and no new result row is required.

### 2.1 Clause-by-clause consumer check

**M19-S2 to frozen M13.** The displayed global `A,w` give the ambient and inclusion hypotheses. The same-state clause gives the Stage-2 geometry. `ENV(U)` plus `W.K2 >= W.L` gives `epsilon_U <= t_2`; `RI(U)` plus `W.K2 >= W.c0_cb*W.L` gives `d_U <= t_2`. The incoming unit clause is carried but not used by M13. M04 permits the target raw-call field to be selected with `epsilon_R <= W.L*epsilon <= t_2`. Thus every literal M13 antecedent is supplied without rebinding the old record.

**M19-S3 to M12.** `ENV(U),ENV(V)` and the two coefficient guards give `epsilon_U,epsilon_V,d_U,d_V <= t_3`. `UI(U),UI(V)` and `W.K3 >= W.c0_cb*W.L` give exactly the two M12 unit hypotheses. M04 supplies the target raw-call record for `A_R`. No clause is inferred from record naming alone.

**M25 to M27 to M28.** M25 selects the M04 certificate as the record at the scalar base and after every Stage-2 extension. M26 performs the same selection after every binary merge. M27 iterates the triple `ENV+RI+UI`, so its output supplies `epsilon_J <= W.L*epsilon`. M28 then gets both the final defect and unit bounds at most `W.c0_cb*W.L*epsilon`, and its existing full-corner telescope is paid by `W.K_call >= W.L+1`.

**M20's comparison role.** M20 needs to compare scales, not manufacture analytic certificates. The repaired pure scalar clause combines with M04 exactly where the compressed scalar call, Stage-2 call, Stage-3 call, or final telescope is constructed.

## 3. Deliverable 3 — verbatim repaired contracts

Each registry candidate below is one physical ASCII line. The unchanged portions are retained so that each line is self-contained. No proof-specific numerical value is chosen here; the numeric guard literals already belong to the ratified frozen scalar ledger.

### M19-S2 — `lem-maincb-stage2-call-envelope`

```text
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_s2^0,e_s2^0 witnesses of lem-maincb-stage2-extcb-datum, there is a universal K_2^0 >= 1 with every Stage-2 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K2 >= max{K_2^0,1,W.L,W.c0_cb*W.L}, and W.e_s2 <= e_s2^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has nonempty U contained in one equivalence class, j notin U in that same class, and R=U union {j}, 0 <= epsilon <= W.e_s2/W.K2, and a supplied current reset isomorphism v_U:M_{|U|}->A_U has recorded ambient field epsilon_U <= W.L*epsilon and satisfies d_U <= W.c0_cb*epsilon_U and ||v_U(I_{M_{|U|}})-u_{A_U}|| <= W.c0_cb*epsilon_U, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-2 raw-call target ambient record epsilon_R := W.L*epsilon, and t_2=W.K2*epsilon dominates epsilon_U,d_U,epsilon_R, the reset unit error, and every other datum error, so lem-maincb-stage2-extcb-datum furnishes the explicit Stage-2 EXT raw-call datum with total defect at most C_s2^0*t_2.
```

### M19-S3 — `lem-maincb-stage3-call-envelope`

```text
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, there is a universal K_3^0 >= 1 with every Stage-3 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K3 >= max{K_3^0,1,W.L,W.c0_cb*W.L}, and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has disjoint nonempty unions U,V sharing no class and R=U union V, 0 <= epsilon <= W.e_cross/W.K3, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-3 raw-call target ambient record epsilon_R := W.L*epsilon, and t_3=W.K3*epsilon dominates epsilon_U,epsilon_V,d_U,d_V,epsilon_R, both displayed unit norms, and every other datum error, so lem-maincb-cross-class-merging-datum furnishes the explicit Stage-3 four-corner raw-call datum with rho <= C_cross^0*t_3.
```

### M20 — `lem-maincb-structural-domain-ledger`

```text
contract: After first fixing a particular universal e_sim>0 witness furnished by lem-maincb-corner-equivalence and a particular universal e_full>0 witness furnished by lem-maincb-full-corner-identification, fix one def-maincb-witness-ledger datum W whose existence is furnished by lem-maincb-reset-constant-ledger instantiated with those same e_sim,e_full witnesses; then 0 <= epsilon <= W.epsilon_MAIN implies epsilon <= W.e_env, epsilon <= W.e1/W.K1, epsilon <= W.e_s2/W.K2, and epsilon <= W.e_cross/W.K3, while the global scalar scale epsilon, atomic scalar scale W.K_call*epsilon, and Stage-1, Stage-2, and Stage-3 scales W.K1*epsilon,W.K2*epsilon,W.K3*epsilon are all at most W.K_call*epsilon <= W.r_reset,e_sim,e_full; moreover W.L*epsilon <= W.K_call*epsilon and W.c0_cb*W.K_call*epsilon <= 1/2.
```

### M25 — `lem-maincb-one-class-extension`

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, all atomic images are one-dimensional, and C is one equivalence class, then there is a current reset isomorphism v_C:M_{|C|}->A_C whose recorded ambient field epsilon_C is selected so that A_C is an extended epsilon_C-C*-algebra and epsilon_C <= W.L*epsilon <= W.K_call*epsilon, and which satisfies d_C <= W.c0_cb*epsilon_C and ||v_C(I_{M_{|C|}})-u_{A_C}|| <= W.c0_cb*epsilon_C.
```

### M26 — `lem-maincb-binary-block-merge`

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} whose recorded ambient field epsilon_{U union V} is selected so that A_{U union V} is an extended epsilon_{U union V}-C*-algebra and epsilon_{U union V} <= W.L*epsilon, and which satisfies d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.
```

### M27 — `lem-maincb-stage3-finite-recombination`

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon and has classes C_1,...,C_q, and each initial current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} has recorded ambient field epsilon_{C_a} <= W.L*epsilon and satisfies d_{C_a} <= W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I_{B_{C_a}})-u_{A_{C_a}}|| <= W.c0_cb*epsilon_{C_a}, then there is a current reset isomorphism v:oplus_a B_{C_a}->A_{union_a C_a} whose recorded ambient field epsilon_{union_a C_a} satisfies epsilon_{union_a C_a} <= W.L*epsilon, d_{union_a C_a} <= W.c0_cb*epsilon_{union_a C_a}, and ||v(I_{oplus_a B_{C_a}})-u_{A_{union_a C_a}}|| <= W.c0_cb*epsilon_{union_a C_a}.
```

### 3.1 Why no smaller contract package closes

- S2/S3 cannot merely rename the M04 certificate: `d_U` and `UI(U)` remain tied to the old supplied record.
- M20 cannot keep the anaphoric atomic claim under the typed-witness law; the pure scalar comparison is all its consumers require.
- M25 must export `W.L`, not merely `W.K_call`, because the frozen arithmetic guarantees `W.K2,W.K3 >= W.c0_cb*W.L` but does not guarantee domination of `W.c0_cb*W.K_call` by either stage multiplier.
- M26 must both consume and produce `ENV`; otherwise either its first merge or its next recursive use is underived.
- M27 must carry the same predicate in its initial-family and final-state clauses; otherwise M28 cannot use the final `RI/UI` at a global scale.
- No amendment to M12, M16, M18, M19-R, or M28 is needed once these six interfaces are repaired.

## 4. Deliverable 4 — budgets and re-seed guidance

Every changed root is re-seeded. No old ledger is patched or transplanted. The existing evidence remains archived as the refutation record.

| Row | Target / rounds / hard cap | Re-seed instruction |
|---|---:|---|
| M19-S2 | 7 / 3 / 11 | Fresh root. Recreate the provider-smallness node, geometry node, and M13 application. Add one explicit record/certificate node and one corrected monotonicity node including the extended-inclusion unit clause. |
| M19-S3 | 8 / 3 / 12 | Fresh root. Use two supplied `ENV` hypotheses, one M04 target-certificate selection, and a literal four-inequality forwarding node to M12 (`epsilon`, `d`, and both unit errors). |
| M20 | 6 / 2 / 10 | Fresh scalar-only tree. Delete every reference to an atom or record; verify only the inequalities among fields of the same M18-supplied `W`. |
| M25 | 10 / 3 / 14 | Fresh root. Carry `ENV+RI+UI` as the Stage-2 induction predicate. The extra node binds the M04 certificate to the scalar base and every new target record. |
| M26 | 9 / 3 / 13 | Fresh root. One node forwards input `ENV+RI+UI` through S3/M12; one node records the M04-certified target before applying M17 and frozen M19-R. |
| M27 | 7 / 2 / 11 | Fresh finite-induction tree. The induction predicate is exactly `ENV+RI+UI`; the one-class case retains the supplied bound and every binary step imports repaired M26. |

All caps remain below the repository soft cap. A cap hit is a factoring stop, not authority to weaken the record binding.

### 4.1 M19-S2 parked ledger disposition

The old ledger has five validated nodes. Their design treatment is:

| Old node | Treatment in the re-seed |
|---|---|
| `1.1.1` | **Survives verbatim in substance:** provider finiteness and the `epsilon,t_2` margin calculation are unaffected. Recreate in the fresh tree. |
| `1.1.4` | **Survives verbatim in substance:** the equivalence-class geometry still supplies every M13 corner-dimension hypothesis. Recreate. |
| `1.2` | **Survives after antecedent rebinding:** the frozen M13 application is correct once the new root supplies all literal antecedents. Recreate only after the new certificate and scalar nodes validate. |
| amended `1.1.2` | **Archive-by-design:** its validated content is the distinction between fresh M04 certificates and the supplied record, including the countermodel. It is negative evidence, not a positive child of the repaired root. |
| `1.1.5.1` | **Archive-by-design:** retain the exact `M_2` countermodel as the red test; it must fail the repaired root because `epsilon_U <= W.L*epsilon` is now a hypothesis. |

The challenged conditional node `1.1.3.1` is not reused: its circular extra antecedents become genuine root hypotheses and the scalar implication is re-derived. Node `1.1.3.2` is also re-derived with the correct fact from `def-extended-delta-inclusion`: the unit clause is present and is monotone together with the multiplicative and norm clauses. The amended old `1.1.5` remains archived because it correctly records that the former root was false.

The mandatory red test for the new root is to remove `epsilon_U <= W.L*epsilon`; the exact `epsilon=0`, recorded-`epsilon_U>0` model must again satisfy all remaining hypotheses and refute the conclusion.

## 5. Deliverable 5 — dimension-freeness and induction arithmetic

No frozen scalar witness changes. For the `W` supplied by M18 and the validated witness-arithmetic row:

1. `W.K2,W.K3 >= W.L` and `W.K2,W.K3 >= W.c0_cb*W.L`. Hence `ENV(R)`, `RI(R)`, and `UI(R)` are all at most the relevant Stage-2 or Stage-3 base scale.
2. `W.K_call >= W.L+1`, and `epsilon <= W.epsilon_MAIN` implies `W.K_call*epsilon <= W.r_reset,e_sim,e_full`. M20 need only export those scalar comparisons.
3. M04 is uniform over every nonempty subset `R`; selecting its certificate for a new record introduces no dependence on `|R|`, `dim A`, class size, or merge depth.
4. Frozen M19-R replaces each raw output by a map satisfying `RI+UI` with the same coefficient `W.c0_cb`. The repaired caller supplies the target ambient field. M19-R is not asked to prove `ENV` and is not amended.
5. M25 selects the M04 record after every extension, and M26 does so after every merge. Thus M27 iterates a fixed three-clause invariant. It never adds record values or raw errors across classes.
6. At the final union, repaired M27 gives
   \[
   d_J,\ \lVert v_J(I)-u_{A_J}\rVert
   \le W.c0_{cb}\varepsilon_J
   \le W.c0_{cb}W.L\varepsilon.
   \]
   The frozen full-corner comparison costs the remaining global-unit displacement, and `W.K_call >= W.L+1` closes the existing M28 conclusion.

Every coefficient remains a finite expression of universal provider witnesses already fixed by M18. There is no amplification count, dimension, class count, induction length, or merge-tree factor. The repair therefore preserves dimension-freeness and the RI/UI arithmetic exactly.

## 6. Deliverable 6 — risk register, frozen rows, and escalation

### 6.1 Per-repaired-row first hostile attack

| Row | First attack a hostile verifier should make | Required decisive answer |
|---|---|---|
| M19-S2 | “`epsilon_U` is still being concluded or rebound.” | Point to the literal root hypothesis `epsilon_U <= W.L*epsilon`; separately point to the fresh raw target assignment `epsilon_R := W.L*epsilon`. |
| M19-S3 | “One of the two supplied records or unit errors is not below `t_3`.” | Display both `ENV` hypotheses and both uses of `W.K3 >= W.c0_cb*W.L`; no symmetry-by-notation shortcut. |
| M20 | “The contract still quantifies an atomic defect without an atom.” | It must contain only scalar inequalities on one explicitly fixed `W`; M04 appears only in consumers. |
| M25 | “The existential reset map is constructed, but its recorded ambient field is not the same target field passed to M19-R.” | At the scalar base and every extension, select the M04 certificate before forming the raw call, then apply M19-R to that same target record. |
| M26 | “The merge output has `RI/UI` but no reusable small record.” | The raw Stage-3 target record is the M04 certificate; M19-R leaves the source and target unchanged, so the output record satisfies `ENV`. |
| M27 | “A class-count or merge-depth factor accumulates, or the one-class case loses `ENV`.” | State the three-clause induction predicate; the one-class case is the supplied state, and every binary step returns the identical predicate via M26. |

### 6.2 Top three ways this design could be wrong

1. **Fresh-certificate/old-record confusion survives in a proof.** The contract repair is correct only if a supplied record is never silently overwritten. A new record may be selected only for a newly constructed raw target or existential output state.
2. **The M25/M26 proof fails to bind one literal target field through M19-R.** If the M04 certificate, raw-call `epsilon_R`, and output reset `epsilon_R` are three merely same-named quantities rather than one typed field, the repair recreates the 2026-07-28 definite-description failure.
3. **A downstream proof uses `W.K_call` where only `W.K2` or `W.K3` is available.** The closed induction must carry the sharper `W.L*epsilon` record bound. Reverting to M25's old coarse bound breaks S2/S3 even though all constants remain universal.

### 6.3 Frozen T0 check

The following current T0 contracts were checked and require no change:

- MAIN M01--M11 and M13--M16, in particular M04's “admits an extended `L*epsilon` bound,” frozen M13's literal supplied-`epsilon_U` antecedent, and frozen M16's raw Stage-2 target interface;
- `lem-maincb-isomorphism-unit-control` — unaffected because the issue is record identity, not the unit clause;
- `lem-maincb-witness-arithmetic` — already supplies every inequality used above, including the `L`, `K2`, `K3`, and `K_call` comparisons;
- `lem-maincb-compressed-corner-unit-comparison` — unaffected and still supplies M12's diagonal-unit bridge;
- M19-R `lem-maincb-reset-invariant-preservation` — already takes an explicit target ambient field `epsilon_R <= t` and returns `RI/UI` for that same target; the caller, not M19-R, supplies `ENV`.

M17 is not frozen T0, but its current target-ambient hypothesis is already sufficient and its contract need not change. The repaired M19-S3 supplies exactly the field it consumes.

**No-T0-invalidation verdict:** PASS at design level. No banked contract, validated external, locked definition, witness-arithmetic field, or provider ordering changes.

### 6.4 Exact-source and escalation ledger

- The only external ground truth used is the pinned TeX source: actual corners are uniformly controlled at 1428--1435; Stage-2 reset occurs at 1435--1441; Stage-3 reset occurs at 1443; the whole induction is 1414--1444. The paper contains no recorded-field semantics, and this design does not attribute any to it.
- **User-ratification item:** the six contract amendments in §3, including the stronger-but-true M25 export.
- **No definition escalation:** `def-maincb-reset-state` and `def-maincb-partition-state` remain byte-unchanged. Any future proposal to encode certificate identity in either definition must stop for a separate T0-cascade decision.
- **No missing-reference escalation:** the repair needs no new analytic fact beyond M04, the already banked unit/witness bridges, M16, and M19-R.
- **Conditional stop:** if a fresh verifier cannot keep the M04 certificate, raw-call target field, and M19-R output record as one typed field in M25 or M26, factor a new record-selection result row; do not amend a frozen provider or appeal to sameness of notation.

**Final design disposition:** six-contract identification/forwarding repair; ready for an independent hostile design audit, then explicit user ratification. No registry mutation is authorized by this document.
