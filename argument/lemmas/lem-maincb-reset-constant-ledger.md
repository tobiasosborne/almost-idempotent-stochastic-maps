---
id: lem-maincb-reset-constant-ledger
kind: lemma
contract: After first fixing e_it,K_disp,K_floor from lem-maincb-improvement-iteration, epsilon_max^cb,delta_max^cb,c0^0 from lem-maincb-error-improvement, C_unit,epsilon_unit,delta_unit,a_unit from lem-maincb-reset-invariant-preservation, a valid enlarged c0 >= max{c0^0,K_floor,C_unit*(K_floor+1)}, L^0,e_env^0 from lem-maincb-direct-corner-envelope for this c0, e_full from lem-maincb-full-corner-identification, e_sim from lem-maincb-corner-equivalence, D_0,e_0 from lem-maincb-initial-raw-inclusion, D_1,e_1,K_1^0 from lem-maincb-stage1-call-envelope, C_s2^0,e_s2^0 from lem-maincb-stage2-extcb-datum, D_2,e_2 from lem-maincb-stage2-raw-extension, K_2^0 from lem-maincb-stage2-call-envelope, C_cross^0,e_cross^0 from lem-maincb-cross-class-merging-datum, D_3,e_3 from lem-maincb-stage3-raw-merge, and K_3^0 from lem-maincb-stage3-call-envelope, set D_* = max{1,D_0,D_1,D_2,D_3}; then there exists one def-maincb-witness-ledger datum W supplied by lem-maincb-witness-arithmetic with W.c0_cb=c0, W.L>=L^0, W.K1>=K_1^0, W.K2>=max{K_2^0,1,W.L,W.c0_cb*W.L}, W.K3>=max{K_3^0,1,W.L,W.c0_cb*W.L}, W.e_env<=e_env^0, W.e1<=e_1, W.e_s2<=min{e_s2^0,e_2}, and W.e_cross<=min{e_cross^0,e_3}, such that under the respective producer hypotheses at base scale 0 <= t <= W.r_reset and target ambient defect at most t, the literal maps u_0:C->A furnished by lem-maincb-initial-raw-inclusion and u_1:C^{m+1}->A furnished by lem-maincb-stage1-call-envelope with lem-maincb-stage1-raw-refinement are extended D_*t-inclusions, the literal maps u_2:M_{r+1}->A_R furnished by lem-maincb-stage2-call-envelope with lem-maincb-stage2-raw-extension and u_3:B_U oplus B_V->A_R furnished by lem-maincb-stage3-call-envelope with lem-maincb-stage3-raw-merge are extended D_*t-isomorphisms, and ||u_0(I_C)-I_A||,||u_1(I_{C^{m+1}})-I_A||,||u_2(I_{M_{r+1}})-u_{A_R}||,||u_3(I_{B_U oplus B_V})-u_{A_R}|| <= D_*t, so each satisfies the M02/M03 and near-unit thresholds and is eligible for lem-maincb-reset-invariant-preservation; all selected witnesses are universal and independent of dimension, amplification, block data, class count, and stage index.
defs: def-maincb-witness-ledger; def-maincb-raw-call; def-maincb-reset-state
deps: lem-maincb-witness-arithmetic; lem-maincb-improvement-iteration; lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-full-corner-identification; lem-maincb-corner-equivalence; lem-maincb-cross-class-merging-datum; lem-maincb-initial-raw-inclusion; lem-maincb-stage1-raw-refinement; lem-maincb-stage2-extcb-datum; lem-maincb-stage2-raw-extension; lem-maincb-stage3-raw-merge; lem-maincb-stage1-call-envelope; lem-maincb-stage2-call-envelope; lem-maincb-stage3-call-envelope; lem-maincb-reset-invariant-preservation; lem-maincb-extended-inclusion-monotone
status: proved
af: validated
workspace: proofs/lem-maincb-reset-constant-ledger
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M18 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source finite arithmetic; TeX loci inherited from providers; monotonicity dep factored in per DESIGN-M18-MONOTONE.md (audit F5; user-ratified 2026-08-01)
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated 15/15 nodes clean, run 2 re-seed with the monotonicity micro-row + instantiation-record discipline, tier routine, 2026-08-01; oracle PASS; run 1 ballooned 20 nodes re-deriving monotonicity — the L4 factoring fixed it). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M18 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M18. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
12 / 3 / 16. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** finite arithmetic; TeX loci inherited from providers
