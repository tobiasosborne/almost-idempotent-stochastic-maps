# DESIGN v3 — the bijectivity bridge + typed M17 package (FINAL, audit corrections applied)

**Date:** 2026-08-01
**Status:** v2 (`DESIGN-M17-TYPING-v2.md`) with the hostile audit's three
exact corrections F1–F3 (`AUDIT-M17-TYPING-v2.md` §1) applied VERBATIM;
nothing else differs from v2. The audit's per-row verdicts were
VALID-WITH-CORRECTIONS for both rows; its DESIGN-REFUTED disposition
targeted only the v2 "exact package" claim, cured here by including the
M26 deps amendment the discharge chain requires. Awaiting USER
ratification. No definition change; no frozen T0 amendment.

## The package (three items)

### 1. NEW row `lem-maincb-cross-datum-bijectivity` (F2 + F3 applied)

```text
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit which are valid witnesses of lem-maincb-cross-class-merging-datum such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then, writing B_R:=B_U oplus B_V, q_U:=(I_{B_U},0), q_V:=(0,I_{B_V}), P_X^R:=Co^A_{P_R}(P_X) for X in {U,V}, gamma_UU:q_U B_R q_U->S^{A_R}_{P_U^R} defined by gamma_UU((b_U,0)):=Co^{A_R}_{P_U^R}(Co^A_{P_R}(v_U(b_U))), gamma_VV:q_V B_R q_V->S^{A_R}_{P_V^R} defined by gamma_VV((0,b_V)):=Co^{A_R}_{P_V^R}(Co^A_{P_R}(v_V(b_V))), gamma_UV:q_U B_R q_V={0}->S^{A_R}_{P_U^R,P_V^R}={0} the unique map, and gamma_VU:q_V B_R q_U={0}->S^{A_R}_{P_V^R,P_U^R}={0} the unique map, the explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum has these four fixed level-one maps and gamma_UU,gamma_UV,gamma_VU,gamma_VV are bijective.
```

```text
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-witness-ledger; def-four-corner-merging-datum; def-compressed-corner; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-one-dimensional-delta-projection
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-compressed-corner-unit-comparison; lem-maincb-cross-class-merging-datum; lem-maincb-outer-compression-transfer; lem-maincb-cross-union-zero-corners
```

All six deps are `af: validated` (audit F3: "no new result is needed").
Provenance: `approximate_algebras.tex:1325-1345,1363-1369`; proof route and
budget per `DESIGN-M17-TYPING-v2.md` §§2–4 (budget 8 / 3 / 12).

### 2. AMENDED M17 `lem-maincb-stage3-raw-merge` (F1 applied — plain bijectivity property, no certificate anaphor)

```text
contract: After first fixing the universal C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum furnished by lem-maincb-cross-datum-bijectivity, C_merge,a_merge witnesses of lem-extcb-four-corner-merge, and C_iso_unit,e_iso_unit witnesses of lem-maincb-isomorphism-unit-control, there are universal D_3 < infinity and e_3 > 0 such that for every def-maincb-witness-ledger datum W with W.e_cross <= min{e_cross^0,e_3}, (C_cross^0+1)*e_3 <= a_merge, and (C_merge*(C_cross^0+1)+1)*e_3 <= e_iso_unit, every explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum with source B_U oplus B_V, with B_U and B_V finite-dimensional C*-algebras, with A_R a finite-dimensional extended epsilon_{A_R}-C*-algebra, whose four fixed level-one corner maps are bijective, and with 0 <= rho <= C_cross^0*t and 0 <= epsilon_{A_R} <= t <= W.e_cross yields an extended D_3*t-isomorphism v:B_U oplus B_V->A_R satisfying ||v(I_{B_U oplus B_V})-u_{A_R}|| <= D_3*t.
```

Deps gain `lem-maincb-cross-datum-bijectivity` (witness provider); the
sign-safe C_iso_unit chain per v2 §3. Budget 6 / 2 / 9 (v1 §4 re-seed
guidance; countermodel retained as red test).

### 3. M26 `lem-maincb-binary-block-merge` deps metadata amendment (F1)

Contract UNCHANGED (the ratified ENV form). Its `deps:` line becomes:

```text
deps: lem-maincb-stage3-raw-merge; lem-maincb-stage3-call-envelope; lem-maincb-cross-datum-bijectivity; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
```

so M26 can apply the bridge to its displayed Stage-3 inputs and pass the
plain bijectivity premise to M17 (audit §4 discharge-chain re-derivation).

## Ratification items

(i) the new bridge row; (ii) the amended M17 contract; (iii) the M26 deps
amendment. Zero definition changes; zero frozen-T0 changes.
