---
id: lem-maincb-cross-class-merging-datum
kind: lemma
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then lem-maincb-compressed-corner-unit-comparison and the nested-corner, outer-compression, and zero-cross-corner constructions form the explicit Stage-3 amplified four-corner datum in A_R with common defect rho <= C_cross^0*t.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-maincb-witness-ledger; def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-one-dimensional-delta-projection; def-compressed-corner
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-nested-corner-comparison; lem-maincb-outer-compression-transfer; lem-maincb-compressed-corner-unit-comparison; lem-maincb-cross-union-zero-corners; lem-compcb-corner-algebra; lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities
status: proved
af: validated
workspace: proofs/lem-maincb-cross-class-merging-datum
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M12 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:1054-1082,1325-1345,1358,1363-1369,1443
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated 11/11 nodes clean, re-seed run + verify resume, tier routine, 2026-08-01; oracle af-lem-maincb-cross-class-merging-datum PASS; runs 1-3 parked 9/10 pre-repair on the missing unit clause — the ratified unit-hypothesis thread + corner-unit bridge closed it). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M12 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M12. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
11 / 3 / 15. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1054-1082,1325-1345,1358,1363-1369,1443
