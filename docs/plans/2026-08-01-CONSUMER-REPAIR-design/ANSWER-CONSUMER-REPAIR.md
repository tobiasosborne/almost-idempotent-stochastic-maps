Created [DESIGN-CONSUMER-REPAIR.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-01-CONSUMER-REPAIR-design/DESIGN-CONSUMER-REPAIR.md).

### Repaired contracts

M26:

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has disjoint nonempty unions U,V sharing no class, and current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then there is a current reset isomorphism v_{U union V}:B_U oplus B_V->A_{U union V} whose recorded ambient field epsilon_{U union V} is selected so that A_{U union V} is an extended epsilon_{U union V}-C*-algebra and epsilon_{U union V} <= W.L*epsilon, and which satisfies d_{U union V} <= W.c0_cb*epsilon_{U union V} and ||v_{U union V}(I_{B_U oplus B_V})-u_{A_{U union V}}|| <= W.c0_cb*epsilon_{U union V}.
```

M27:

```text
contract: Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, a supplied MAIN partition state comes from an extended W.c0_cb*epsilon-inclusion w:C^m->A satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images and has classes C_1,...,C_q, and each initial current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} has recorded ambient field epsilon_{C_a} <= W.L*epsilon and satisfies d_{C_a} <= W.c0_cb*epsilon_{C_a} and ||v_{C_a}(I_{B_{C_a}})-u_{A_{C_a}}|| <= W.c0_cb*epsilon_{C_a}, then there is a current reset isomorphism v:oplus_a B_{C_a}->A_{union_a C_a} whose recorded ambient field epsilon_{union_a C_a} satisfies epsilon_{union_a C_a} <= W.L*epsilon, d_{union_a C_a} <= W.c0_cb*epsilon_{union_a C_a}, and ||v(I_{oplus_a B_{C_a}})-u_{A_{union_a C_a}}|| <= W.c0_cb*epsilon_{union_a C_a}.
```

M19-R:

```text
contract: After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R that satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, is an extended W.c0_cb*epsilon_R-inclusion, is an extended W.c0_cb*epsilon_R-isomorphism when u_R is bijective, and leaves the source, target corner, and amplification form unchanged.
```

### Verdicts

- **F-B recommendation:** strengthen and re-validate M19-R. A bridge would have to reconstruct essentially the same same-witness theorem while leaving the canonical provider under-typed.
- **M25 cascade:** **YES—substantive re-validation is required.** Its export does not derive the typing in-line; it infers “bijective hence extended isomorphism” without first proving extended inclusion.
- **Additional cascade:** M18 also byte-imports the old M19-R contract and needs external refresh plus fresh affected-premise verification.
- **Survey:** M21, M22, M23, M24, and M28 contracts all stand unchanged. M21 additionally needs direct access to the witness-arithmetic formula establishing `W.r_reset <= e_0`; this is dependency/proof hygiene, not a contract change.

### Escalation

User ratification is needed to permit temporary demotion/re-validation of M25 and the M18 external refresh alongside M19-R. This exceeds a literal “M19-R-only” re-validation exception. No definition or reference escalation was found.

No `fr`, `bd`, commit, or push was run.