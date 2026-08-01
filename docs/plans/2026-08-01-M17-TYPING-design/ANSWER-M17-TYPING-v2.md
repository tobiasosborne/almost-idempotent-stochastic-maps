Created and pushed [DESIGN-M17-TYPING-v2.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-01-M17-TYPING-design/DESIGN-M17-TYPING-v2.md).

Bridge-row contract:

```text
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit which are valid witnesses of lem-maincb-cross-class-merging-datum such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then, writing B_R:=B_U oplus B_V, q_U:=(I_{B_U},0), q_V:=(0,I_{B_V}), P_X^R:=Co^A_{P_R}(P_X) for X in {U,V}, gamma_UU:=Co^{A_R}_{P_U^R} o Co^A_{P_R} o v_U, gamma_VV:=Co^{A_R}_{P_V^R} o Co^A_{P_R} o v_V, gamma_UV:q_U B_R q_V={0}->S^{A_R}_{P_U^R,P_V^R}={0} the unique map, and gamma_VU:q_V B_R q_U={0}->S^{A_R}_{P_V^R,P_U^R}={0} the unique map, the explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum has these four fixed level-one maps and gamma_UU,gamma_UV,gamma_VU,gamma_VV are bijective.
```

Typed M17 contract:

```text
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum furnished by lem-maincb-cross-datum-bijectivity, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are the maps certified bijective by lem-maincb-cross-datum-bijectivity, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
```

Discharge-chain verdict: **PASS at the contract/interface level**, conditional on validating the bridge and re-validating M17:

```text
M26 -> M19-S3 -> (M12 datum + bijectivity bridge on that same datum) -> typed M17
```

STOP escalation: **none currently**. Hostile audit and user ratification remain required. STOP if the audit rejects either the same-datum identification or the shared shrunken-witness selection, since either failure would require a frozen T0 amendment or another row.

`sh scripts/check-all.sh` passed. Commit `f8920d0a` was pushed to `origin/master`.