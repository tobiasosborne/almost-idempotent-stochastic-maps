# DESIGN v2 — bijectivity bridge plus typed M17 package

## 0. Verdict

**DESIGN-CLOSABLE, subject to the mandated fresh hostile audit and user
ratification.** Exactly one new row and one amended contract suffice. The new
row chooses a possibly smaller pair of valid M12 witnesses and binds the four
literal corner maps by formula. This simultaneously pays the outer-compression
and zero-corner thresholds and prevents an opaque same-datum inference. M12 and
M19-S3 remain byte-frozen T0 rows; no definition changes.

The contracts below are proposed design text, not proved or ratified claims.

## 1. Deliverable 1 — new bijectivity bridge row

Proposed id: `lem-maincb-cross-datum-bijectivity`.

One physical-line ASCII contract:

```text
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit which are valid witnesses of lem-maincb-cross-class-merging-datum such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then, writing B_R:=B_U oplus B_V, q_U:=(I_{B_U},0), q_V:=(0,I_{B_V}), P_X^R:=Co^A_{P_R}(P_X) for X in {U,V}, gamma_UU:=Co^{A_R}_{P_U^R} o Co^A_{P_R} o v_U, gamma_VV:=Co^{A_R}_{P_V^R} o Co^A_{P_R} o v_V, gamma_UV:q_U B_R q_V={0}->S^{A_R}_{P_U^R,P_V^R}={0} the unique map, and gamma_VU:q_V B_R q_U={0}->S^{A_R}_{P_V^R,P_U^R}={0} the unique map, the explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum has these four fixed level-one maps and gamma_UU,gamma_UV,gamma_VU,gamma_VV are bijective.
```

Proposed registry imports:

```text
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-witness-ledger; def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-one-dimensional-delta-projection; def-compressed-corner
deps: lem-maincb-cross-class-merging-datum; lem-maincb-outer-compression-transfer; lem-maincb-cross-union-zero-corners
```

### Proof route and exact exported loci

1. Fix the providers in the displayed order. Take any valid M12 pair
   `(C_cross^0,e_old)` and replace only its receiving margin by
   `e_cross^0=min{e_old,e_out,e_zero}`. Threshold shrinking preserves M12's
   universal conclusion, so the pair remains a valid M12 witness pair. This is
   typed-witness law (ii), not an unstated comparison between independently
   chosen witnesses. The M12 root exports the datum under exactly the copied
   hypotheses at
   `proofs/lem-maincb-cross-class-merging-datum/export.md:3-13`.
2. For `X=U,V`, the reset datum types `B_X` as a finite-dimensional C*-algebra
   and `v_X` as a fixed-amplification extended `d_X`-isomorphism
   (`definitions/def-maincb-reset-state.md:13-20`). Since `d_X<=t`, tolerance
   monotonicity makes it an extended `t`-isomorphism. The coordinate-projection
   identities and the extended `t`-inclusion `w` give the `t`-projection,
   subordination, and nonvanishing hypotheses for `(R,P)=(P_R,P_X)`; the lower
   norm estimate on the nonempty coordinate projection gives
   `||P_R||>=1-t`. Thus the T0 root
   `proofs/lem-maincb-outer-compression-transfer/export.md:3-13` applies to the
   displayed literal map and exports
   `gamma_XX=Co^{A_R}_{P_X^R} o Co^A_{P_R} o v_X` as an extended
   `C_out*t`-isomorphism. By
   `definitions/def-extended-delta-inclusion.md:13-17`, each diagonal map is
   bijective at level one.
3. The copied M12 hypotheses and `t<=e_cross^0<=e_zero` activate the T0 root
   `proofs/lem-maincb-cross-union-zero-corners/export.md:3-13`, which exports
   both target cross-corners as zero. The source cross-corners of
   `B_U oplus B_V` are also zero. The unique linear map `{0}->{0}` in either
   orientation is bijective, so `gamma_UV` and `gamma_VU` are bijective.
4. M12's root identifies its output as the datum formed by the
   nested-corner, outer-compression, and zero-cross-corner constructions. The
   bridge contract displays those constructions and their sources and targets
   explicitly. Hence the two diagonal maps just certified and the two unique
   zero maps are the maps of that same datum. M12's internal nodes 1.4, 1.6,
   and 1.8 (`export.md:63-73,87-97,111-121`) are useful audit concordance only;
   the bridge proof must re-derive the result from the three imported T0 roots
   above and must not import those internal nodes as theorem clauses.

The pinned source records the four-corner maps and the separate bijectivity
premise/conclusion at
`refs/kitaev-2405.02434/approximate_algebras.tex:1325-1349`, its direct-sum
specialization at `:1352-1359`, and the corner-dimension decomposition behind
the zero corners at `:1363-1369`. The source definition of isomorphism as a
bijective inclusion is at `:443-455`, with the extended form at `:1477-1484`;
the compression geometry used by the T0 outer-transfer row is at `:1068-1082`.

**Budget:** fresh routine-tier seed; target **7 live nodes / 3 rounds / hard
cap 11**. Suggested nodes are root, ordered witness selection and threshold
shrink, common geometric prerequisites, the two diagonal maps together, the
two zero maps together, same-datum identification, and final quantifier
assembly. A cap hit means STOP/factor; it is not a reason to enlarge M12 or a
definition.

## 2. Deliverable 2 — amended typed M17

One physical-line ASCII contract:

```text
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum furnished by lem-maincb-cross-datum-bijectivity, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are the maps certified bijective by lem-maincb-cross-datum-bijectivity, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
```

Proposed imports:

```text
defs: def-maincb-raw-call; def-maincb-witness-ledger; def-four-corner-merging-datum; def-operator-space; def-extended-delta-inclusion; def-extended-epsilon-cstar-algebra
deps: lem-maincb-cross-class-merging-datum; lem-maincb-cross-datum-bijectivity; lem-extcb-four-corner-merge; lem-maincb-isomorphism-unit-control
```

The conclusion is unchanged. Compared with v1 section 1, the datum is now
restricted to the literal M12 construction, the bridge-selected M12 witnesses
are fixed before all receiving witnesses, and the bijectivity clause points to
the bridge's fully displayed maps. This is a provider binding, not sameness by
notation.

The positive proof must preserve challenge `ch-40fe16a76915988d`'s sign-safe
argument. Put `s=delta+epsilon_{A_R}>=0`. From unit control and norm
nonnegativity,
`||v(I)-u|| <= C_iso_unit*s <= abs(C_iso_unit)*s`; only then multiply
`s <= (abs(C_merge)*(C_cross^0+1)+1)*t` by the nonnegative absolute value.
Choose `e_3` internally small enough for the corresponding absolute-value
range conditions, in addition to the displayed conditions, and choose `D_3`
using absolute values. No contract assumes `C_iso_unit>=0`.

## 3. Deliverable 3 — M26 dischargeability re-check

The discharge is for the one literal datum throughout. The new bridge must be
elevated before M17; M26 itself remains a later seeded row.

| M17 input | Exporting clause on the M26 path | Verdict |
|---|---|---|
| Common `C_cross^0,e_cross^0` | The bridge contract furnishes a pair which is explicitly a valid M12 pair. M19-S3 is instantiated only after fixing that same pair, exactly as its root begins (`proofs/lem-maincb-stage3-call-envelope/export.md:3-13`). | Discharged after bridge validation. |
| Ledger range `W.e_cross<=min{e_cross^0,e_3}` | M26 fixes the ledger `W` supplied on the M18/M20 path. The planned M18 contract records this exact inequality; its scalar construction is backed by T0 `lem-maincb-witness-arithmetic` (`proofs/lem-maincb-witness-arithmetic/export.md:3-13,63-73`). This is unchanged by the typing repair. | Dischargeable on the already designed ledger path; no new premise. |
| Merge and unit smallness conditions on `e_3` | M17 chooses `e_3` after `C_cross^0,C_merge,C_iso_unit` are fixed and may shrink it using absolute values. These are provider-witness choices, not facts M26 must manufacture. | Discharged inside M17. |
| Literal M12 datum | M19-S3's T0 root says `t_3=W.K3*epsilon` dominates every M12 input and therefore M12 furnishes the explicit Stage-3 four-corner raw-call datum with `rho<=C_cross^0*t_3` (`stage3-call-envelope/export.md:3-13`). Its packaging clause names `B_R=B_U oplus B_V`, the diagonal outer-compression maps, the two zero maps, and the one fixed amplification family (`:159-169`; explicit formula audit at `:171-181`). | Discharged; same datum, not a second existential choice. |
| `B_U,B_V` finite-dimensional C*-algebras and source `B_U oplus B_V` | Each supplied reset state contains the named finite-dimensional C*-algebra (`definitions/def-maincb-reset-state.md:13-20`); M19-S3's packaging clause takes their named direct sum (`stage3-call-envelope/export.md:159-169`). | Discharged. |
| `A_R` finite-dimensional extended `epsilon_{A_R}`-C*-algebra | M19-S3's T0 root certifies the Stage-3 target ambient record; node 1.2.2 spells out `epsilon_{A_R}=epsilon_R=W.L*epsilon` and the extended structure (`stage3-call-envelope/export.md:87-97`). `A_R` is a compressed-corner image in finite-dimensional `A`, hence finite-dimensional. | Discharged. |
| Four maps are the bridge-certified maps | M12's T0 root identifies the datum as its nested-corner, outer-compression, and zero-cross-corner construction (`cross-class-merging-datum/export.md:3-13`). The bridge contract displays those four maps and certifies them bijective. M19-S3 packages precisely those maps (`stage3-call-envelope/export.md:159-169`). | Discharged after bridge validation. |
| `0<=rho<=C_cross^0*t_3` | M19-S3 exports the common defect bound at its root (`:3-13`); the explicit M12 construction uses the nonnegative common defect parameter. With `epsilon>=0` and `W.K3>=1`, `t_3>=0` (`:135-145`). | Discharged. |
| `0<=epsilon_{A_R}<=t_3<=W.e_cross` | M19-S3 sets `epsilon_{A_R}=W.L*epsilon` (`:87-97`) and exports `W.L*epsilon<=t_3<=W.e_cross` (`:135-145`), with `epsilon>=0`. | Discharged. |
| Unit-control domain and final map type | The typed M17 hypotheses allow `lem-extcb-four-corner-merge` to produce an extended isomorphism; `lem-maincb-isomorphism-unit-control` then applies because the source and target types are explicit. The absolute-value calculation in section 2 supplies its range and output bound. | Discharged inside M17. |

Thus the literal chain is

```text
M26 -> M19-S3 -> (M12 datum + bijectivity bridge on that datum) -> typed M17.
```

**Discharge-chain verdict: PASS at the contract/interface level, conditional
only on validating the new bridge and re-validating M17.** There is no M12 or
M19-S3 amendment and no hidden appeal to an M12 proof subnode. The planned
M18/M20 scalar ledger remains a later non-T0 elevation, but the v2 package adds
no new obligation to it: its existing selection of M12 witnesses may choose
the pair furnished by the bridge.

## 4. Deliverable 4 — budgets and re-seed guidance

- **Bridge:** fresh seed, **7 nodes / 3 rounds / cap 11**, routine tier. Fix
  provider witnesses first, shrink only the receiving margin, and display all
  four map types in the root. Do not import M12 nodes 1.4/1.6 as externals.
- **M17:** clean re-seed after ratification, **6 live nodes / 2 rounds / cap
  9**. Use: root; absolute-value witness choice; total-defect smallness; typed
  four-corner merge using the bridge; unit-control range; sign-safe unit/final
  assembly. Re-derive the useful arithmetic of old validated nodes 1.1, 1.2,
  and 1.4; do not patch the old 11-node obstruction tree.
- **Red test:** retain the exact validated countermodel from old node 1.3.1:
  `B=C oplus C`, `A_R=M_2(C) oplus M_2(C)`, scalar diagonal embeddings, and
  zero cross maps. It satisfies an arbitrary defect-zero four-corner datum but
  has non-surjective diagonal maps. Before accepting the new seed, perturb the
  root by deleting the M12-plus-bridge restriction and confirm that this model
  makes the statement RED; then restore the typed root. The countermodel is a
  regression oracle, not a positive-tree node.

## 5. Deliverable 5 — risk register and STOP conditions

### First hostile attacks

- **Bridge row:** attack witness identity first. Verify that the shrunken
  `e_cross^0` is still a witness for the same M12 theorem instance and that the
  displayed `gamma` maps, including their exact domains and targets, are the
  literal maps of M12's datum. Then attack the outer-transfer prerequisites;
  no internal M12 node may be smuggled in.
- **M17 row:** attack the exact source/target typing and the equality between
  M19-S3's packaged map family and the bridge-certified family. Next attack
  every multiplication by `C_merge` or `C_iso_unit`; the proof must use
  absolute values unless nonnegativity has actually been exported.

### Top two ways this design could be wrong

1. **Same-datum failure.** If M12's root phrase “the ... constructions form
   the explicit ... datum” is held not to identify the displayed
   outer-compression and unique zero maps, the bridge cannot attach its result
   to M19-S3 without amending a frozen T0 interface. Repeated symbols or
   internal node 1.8 would not repair that failure.
2. **Witness-selection mismatch.** If M19-S3 or the M18 ledger is forced to
   use an independently fixed arbitrary M12 pair rather than the smaller pair
   furnished by the bridge, `t<=e_out,e_zero` is unavailable. The lawful order
   is bridge-selected M12 pair first, then M17/M19-S3/M18 receiving witnesses.

**Current STOP escalation: none.** Every fact needed by the bridge is present
in an exported T0 root or the pinned source, and the exact one-new-row/
one-amended-contract package is viable. STOP during hostile audit or elevation
if either risk above materializes: the next repair would require a frozen T0
amendment or another row, both outside the authorized scope.
