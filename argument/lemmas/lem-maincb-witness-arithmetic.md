---
id: lem-maincb-witness-arithmetic
kind: lemma
contract: After first fixing positive finite universal provider witnesses D_0,D_1,D_2,D_3,e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb,e_it,K_disp,K_floor,epsilon_unit,delta_unit,a_unit,L,c0_cb,K_1,K_2,K_3,e_env,e_s2,e_cross,e_sim,e_full with K_2,K_3 >= max{1,L,c0_cb*L}, set D_* = max{1,D_0,D_1,D_2,D_3}; then there is a def-maincb-witness-ledger datum W whose fields satisfy W.r_reset = min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}, W.K_call = max{1,L+1,c0_cb,K_1,K_2,K_3}, W.epsilon_MAIN = min{e_env,e_1/K_1,e_s2/K_2,e_cross/K_3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,c0_cb*W.K_call}]^{-1}}, and the remaining fields equal the correspondingly named receiving witnesses; in particular every field is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index.
defs: def-maincb-witness-ledger
deps:
status: stated
af: seeded
workspace: proofs/lem-maincb-witness-arithmetic
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 (new row, landed verbatim); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source finite max/min arithmetic; W93 pattern `DESIGN-S1-POLAR-v6.md` §§2-3,8
owner: A
---
**Status.** `stated` — contract transcribed verbatim from the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 (aism-jl4g repair package, hostile-audit
chain AUDIT-MAINCB-REPAIR.md; user-ratified 2026-08-01 in-session). NOT
proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** finite max/min arithmetic; W93 pattern `DESIGN-S1-POLAR-v6.md` §§2-3,8
