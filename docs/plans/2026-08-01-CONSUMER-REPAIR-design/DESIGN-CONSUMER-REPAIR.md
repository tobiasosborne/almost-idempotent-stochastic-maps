# DESIGN — consumer-chain repair

**Date:** 2026-08-01

**Status:** DESIGN ONLY; non-rigorous; no registry, definition, proof, report, or script mutation

**Scope:** M26/M27 one-dimensional-atomic-image hypothesis restoration and M19-R output typing

This design was checked against the literal current shards, the cited parked-ledger challenges, the complete M19-R and M25 exports, the registered dependency externals, the pre-ENV MAIN-v5 contracts, the RECFIELD repair, and the pinned Kitaev source. The source payload is `refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256 `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`, matching `refs/manifest/checksums.sha256`.

**Decision summary.** Restore the omitted hypothesis in M26 and M27 exactly. Strengthen and re-validate M19-R so its one literal output witness is explicitly typed as an extended `W.c0_cb*epsilon_R`-inclusion/isomorphism. Keep M21, M22, M23, M24, and M28 contracts unchanged. There is, however, a mandatory T0-cascade escalation: M25's banked proof did not in fact derive the missing typing in-line, and both M25 and M18 byte-snapshot the old M19-R contract.

## 1. Deliverable 1 — F-A contracts and interface check

Only the words `with one-dimensional atomic images` are added to each current ENV-form hypothesis. Every other byte of each contract value is retained.

This directly answers M26 challenges `ch-c393331c4b1ad7da` (M19-S3 antecedent) and `ch-bc46dcefe4c24c51` (cross-datum-bijectivity antecedent). Their later parked-tree workaround tried to infer atomic one-dimensionality from the conditional class-family semantics; the ratified F-A finding requires the hypothesis to be explicit instead.

### M26 — `lem-maincb-binary-block-merge`

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} whose recorded ambient field epsilon_{U union V} is selected so that A_{U union V} is an extended epsilon_{U union V}-C*-algebra and epsilon_{U union V} <= W.L*epsilon, and which satisfies d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.
```

### M27 — `lem-maincb-stage3-finite-recombination`

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has classes C_1,...,C_q, and each initial current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} has recorded ambient field epsilon_{C_a} <= W.L*epsilon and satisfies d_{C_a} <= W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I_{B_{C_a}})-u_{A_{C_a}}|| <= W.c0_cb*epsilon_{C_a}, then there is a current reset isomorphism v:oplus_a B_{C_a}->A_{union_a C_a} whose recorded ambient field epsilon_{union_a C_a} satisfies epsilon_{union_a C_a} <= W.L*epsilon, d_{union_a C_a} <= W.c0_cb*epsilon_{union_a C_a}, and ||v(I_{oplus_a B_{C_a}})-u_{A_{union_a C_a}}|| <= W.c0_cb*epsilon_{union_a C_a}.
```

### Interface verification

- **M26 to M27: exact match.** M27 fixes one global `A,w` with one-dimensional atomic images and starts from class states carrying `ENV+RI+UI`. At every binary step, disjoint unions of already merged classes satisfy M26's geometry, and M26 returns the identical `ENV+RI+UI` predicate on their union. No class-count or merge-depth coefficient is introduced.
- **M27 to M28: exact match.** M28's M22/M24 branch supplies a maximal `w` whose projection-basis images are one-dimensional; M25 supplies every initial class state; repaired M27 returns the full-union state. Its bounds are unchanged, so M28 still uses `epsilon_J <= W.L*epsilon`, `RI/UI`, and `W.K_call >= W.L+1` to obtain its displayed `W.c0_cb*W.K_call*epsilon` isomorphism and unit bound.
- The hypothesis is attached to the same displayed `w` that defines `P_j=w(e_j)` in the supplied partition state. This is typed-witness law (i), not an inference from repeated notation or from the conditional class-family field.

The atomic clause is faithful to the pre-ENV v5 forms and to the source's Stage-1/Stage-2 transition at TeX 1417--1428. The actual merge is TeX 1325--1359 and 1443.

## 2. Deliverable 2 — F-B decision, contract, and cascade

### 2.1 Repaired M19-R contract

The hypotheses and all scalar guards are byte-identical to the current contract. Only the output clause is strengthened.

```text
contract: After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R that satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, is an extended W.c0_cb*epsilon_R-inclusion, is an extended W.c0_cb*epsilon_R-isomorphism when u_R is bijective, and leaves the source, target corner, and amplification form unchanged.
```

This is provable by the existing tree's **same literal witness**. Export node 1.2 constructs one M02 iterate `v_R` as an extended `K_floor*epsilon_R`-inclusion; the root guard has `W.c0_cb >= K_floor`; `lem-maincb-extended-inclusion-monotone` upgrades that same map at every amplification; nodes 1.4--1.5 prove that same map bijective when `u_R` is bijective and forbid substitution of M03's separate existential output. Thus law (i) is respected. Provider witnesses `K_floor` and `C_unit` are fixed before the receiving coefficient `W.c0_cb` is enlarged, so law (ii) is respected. No new constant or dimension-dependent choice appears.

### 2.2 Option comparison and recommendation

| Option | Mathematical shape | Cost | Verdict |
|---|---|---|---|
| Strengthen M19-R | Repairs the canonical provider; all callers receive one typed witness directly; exactly follows the M02-STRENGTHENED precedent. | Fresh M19-R validation plus the banked-consumer refresh below. | **Recommend, subject to the explicit cascade ratification in §5.** |
| Add a same-witness bridge row | Leaves M19-R's old root unchanged. | The old existential contract does not identify its witness with the proof-internal M02 iterate, so a sound bridge must reconstruct essentially the strengthened M19-R theorem rather than merely cite it. It also leaves the canonical provider under-typed. | Fallback only if the user refuses the M18 external-refresh cascade. |

Strengthening remains preferable because M25 must be repaired in either option: the claimed cheaper “M25 already derived the typing” premise is false on the literal export.

### 2.3 M25-cascade verdict — **YES, substantive re-validation required**

`proofs/lem-maincb-one-class-extension/externals/25114e693d8262b4.json` stores the complete old M19-R contract. More importantly, M25 export nodes 1.1.2.2 and 1.1.3.2 infer “bijective and hence an extended isomorphism” after importing only M19-R's old numerical bounds and bijectivity conclusion. The export contains no `K_floor`, no application of `lem-maincb-extended-inclusion-monotone`, and no other derivation that the improved map is an extended inclusion. Therefore the current M25 certificate has the same typing gap as M21/M23/M26; it is not merely an external-snapshot bookkeeping issue.

Consequences:

1. M25's contract remains byte-unchanged and is mathematically supported once strengthened M19-R is imported.
2. M25 must be honestly demoted and freshly re-validated; re-registering the stronger external without fresh hostile verification is forbidden by the repository's exact-premise precedent.
3. The repaired M25 proof should replace both faulty “bijective hence isomorphism” steps by the strengthened M19-R isomorphism conclusion. Its ENV induction and every other validated node survive in substance.

There is one additional cascade not mentioned in the brief: `proofs/lem-maincb-reset-constant-ledger/externals/8ae71b835f9f4daf.json` also stores the complete old M19-R contract. M18 uses only its unchanged constants/eligibility interface, so no mathematical step or contract changes, but strict byte-external discipline requires external refresh and fresh verification of the affected premise set. M20 imports M18's unchanged contract, so it needs no mathematical re-validation once M18 is re-banked; the landing transaction must nevertheless avoid a committed interval in which a validated M20 rests on a demoted M18.

## 3. Deliverable 3 — consumer survey

| Row | Verdict after F-A/F-B | Reason / implementation guidance |
|---|---|---|
| M21 `lem-maincb-initial-reset-inclusion` | **Contract stands as-is.** | Strengthened M19-R closes typing challenges `ch-badf51f17e1eba66` and `ch-3252308f0b77411e` by supplying the required extended `W.c0_cb*epsilon`-inclusion and unit bound. Re-seed with `t:=epsilon` in the ancestor context. Add a direct dependency on `lem-maincb-witness-arithmetic` (or another exact exported provider of the same formula) to obtain `W.r_reset <= e_0`; the current M18/M20 contracts do not themselves export that inequality. This resolves hygiene challenges `ch-497c658458dedf3a` and `ch-2ba51f6789c8a046` without changing the root. |
| M22 `lem-maincb-maximal-reset-selection` | **Contract stands as-is.** | Once M21 is banked, nonemptiness and the dimension bound are unchanged. No repaired clause appears in its statement. |
| M23 `lem-maincb-stage1-strict-refinement` | **Contract stands as-is.** | The parked tree already constructs the eligible Stage-1 raw map. Strengthened M19-R directly types the improved `v_1` at tolerance `W.c0_cb*epsilon`, closing ch-0c8c4a8212a96fab and ch-03d8796a2b6adab2. |
| M24 `lem-maincb-stage1-maximality` | **Contract stands as-is.** | Its contradiction uses only M22 and repaired M23; it is also the exact producer of the one-dimensional atomic-image hypothesis consumed by M25/M27 in M28. |
| M28 `lem-maincb-structural-assembly` | **Contract stands as-is.** | M24 supplies one-dimensional atoms, unchanged M25 supplies class states, and repaired M27 supplies the full-union `ENV+RI+UI` state. Its final constants and dimension-free arithmetic are unchanged. |

The M21 producer issue is a dependency/proof hygiene repair, not a fourth contract amendment. If the same fixed `W` cannot be connected to the `lem-maincb-witness-arithmetic` formula by an explicit direct import, stop and factor a small same-ledger projection row; do not add `t <= e_0` to M21 or alter a frozen provider by anaphora.

## 4. Deliverable 4 — budgets and re-seed guidance

Every changed root is freshly seeded. A “survives” verdict below means recreate the mathematical content; it does not transplant an old validation onto a changed premise set.

| Row | Target / rounds / hard cap | Re-seed plan and surviving content |
|---|---:|---|
| M19-R re-validation | 9 / 3 / 13 | Fresh root. Recreate current nodes 1.1--1.5 in substance, import `lem-maincb-extended-inclusion-monotone`, and add one explicit same-witness typing node between current 1.2 and the final discharge. Keep the literal-M02-iterate discipline. |
| M26 | 9 / 3 / 13 | Fresh repaired root. Recreate scalar nodes 1.1.1.1--1.1.1.2, raw-merge node 1.1.4, and the valid part of 1.2.1. Archive 1.1.2.1 and 1.1.3.1: they try to recover the missing root hypothesis from conditional class semantics. Archive negative node 1.2.2 after using it as the red test. Apply strengthened M19-R for the final typed isomorphism. |
| M27 | 7 / 2 / 11 | Fresh finite-induction root; the old workspace has no proof child to preserve. Carry one-dimensional atomic images globally and `ENV+RI+UI` as the induction predicate; one-class is identity, every nontrivial step is repaired M26. |
| M21 | 5 / 2 / 9 | Fresh tree. Recreate validated nodes 1.1 and 1.2.1 with `t:=epsilon` ancestor-bound. Import the exact witness-arithmetic formula to prove `t<=W.r_reset<=e_0`, then invoke the global scalar producer and strengthened M19-R. Archive old 1.2.2/1.2.2.1 as the producer-hypothesis red test and old 1.3--1.4.1 as superseded negative evidence. |
| M23 | 8 / 3 / 12 | Re-seed or cleanly resume only the sound prefix. Nodes 1.1--1.5 survive in substance. Replace 1.6/1.6.1 by a direct application of strengthened M19-R; replace 1.7 by `w_+:=v_1` using the exported `W.c0_cb*epsilon` type and unit estimate. |

**Cascade-only refresh budgets.** M18: affected-premise review target 5 / 2 / existing hard cap 16, contract unchanged. M25: substantive repair/review target 7 / 2 / existing scoped hard cap 17, contract unchanged; reverify both scalar and Stage-2 reset applications plus their induction ancestors. A cap hit is a factoring stop.

No budget contains dimension, amplification, class count, or merge depth. M19-R changes only a tolerance label on one already constructed map; M26/M27 continue to reset after every merge rather than add errors.

## 5. Deliverable 5 — risk register and escalation

| Repaired row | First way it could be wrong | Second way it could be wrong |
|---|---|---|
| M19-R | The proof types M02's iterate but takes the unit estimate or bijectivity from a different M03 existential witness. The final node must name one literal map throughout. | `K_floor <= W.c0_cb` is used only numerically while amplified inclusion monotonicity is left implicit. Import and apply the validated monotonicity row to the same map. |
| M26 | “One-dimensional atomic images” is attached to an unrelated map rather than the displayed `w` defining the supplied partition. Keep the clause in the same `A,w` hypothesis. | M17 gives a bijective raw map, but the improved map is again called an isomorphism from bijectivity alone. Use strengthened M19-R's explicit isomorphism conclusion. |
| M27 | The finite induction forgets the global atomic hypothesis after replacing two class unions by their union. Keep `A,w` fixed; only the reset state changes. | The induction accumulates a class-count factor or loses `ENV` in the one-class case. Its invariant must remain exactly `ENV+RI+UI`, with no summed error. |

**Top two global failure modes:** (1) treating same notation as witness identity, especially across M02/M19-R/M25; (2) refreshing an external string mechanically while retaining an old T0 verdict under a changed exact premise set.

### Required escalation

1. **M25 T0 defect:** contrary to the brief's working premise, its validated export does not derive the output inclusion typing in-line. Its status cannot honestly remain rigorous once this finding is adopted. User authorization is required for the temporary demotion and re-validation transaction; no M25 contract change is proposed.
2. **M18 external cascade:** strengthening M19-R also stales M18's byte-snapshot. This exceeds a literal reading of “M19-R re-validation is the sanctioned exception.” Ratify the M18 external refresh/re-validation together with M19-R and M25, or choose the bridge fallback. Do not silently waive the exact-external rule.

There is no definition escalation, no missing-reference escalation, and no route-level alarm. Exact source support is: inclusion/isomorphism definitions at TeX 443--456 and 1477--1484; near-unit control at 1192--1222; error improvement at 1256--1319 and 1557; amplified improvement at 1508--1535; merge at 1325--1359; and the three-stage consumer chain at 1414--1444. The source does not provide the project-original recorded-field semantics, and this design attributes none to it.

**Final disposition:** recommend the three repaired contracts above, with M19-R/M18/M25 treated as one explicitly ratified re-validation cascade. M21, M22, M23, M24, and M28 contracts remain frozen; M21 receives only the direct provider dependency needed to close its parked producer-hypothesis gap.
