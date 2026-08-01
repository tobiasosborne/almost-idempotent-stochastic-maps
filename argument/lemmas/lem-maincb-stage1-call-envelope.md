---
id: lem-maincb-stage1-call-envelope
kind: lemma
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, and fixing the D_1^0,e_1^0 witnesses of lem-maincb-stage1-raw-refinement, there are universal receiving witnesses K_1^0 >= 1, D_1 >= D_1^0, and e_1 > 0 with e_1 <= min{e_1^0,e_corner_unit} and every Stage-1 producer prerequisite absorbed, such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.K1 >= K_1^0, and W.e1 <= e_1, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.e1/W.K1, w:C^m->A is a supplied extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon, and some P_j=w(e_j) has dim S_{P_j}>1, then the three Stage-1 producers, lem-maincb-compressed-corner-unit-comparison, and literal old-side compression furnish the explicit Stage-1 raw call at t_1=W.K1*epsilon whose literal map u_1:C^{m+1}->A is an extended D_1*t_1-inclusion and satisfies ||u_1(I_{C^{m+1}})-I_A|| <= D_1*t_1, when m=1, u_1 is the supplied fresh C^2->A_fresh=S_{P_fresh} inclusion followed by the canonical amplified linear embedding A_fresh->A; lem-compcb-rectangular-product, lem-maincb-compressed-corner-unit-comparison, P_fresh=w(I_C), and the displayed incoming unit estimate furnish the asserted A-valued inclusion and unit bounds.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state; def-maincb-witness-ledger; def-compressed-corner; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-direct-corner-envelope; lem-compcb-single-compression-transfer; lem-maincb-compressed-corner-unit-comparison; lem-stage1-rectified-nontrivial-projection; lem-stage1-original-complementary-pair; lem-stage1-fresh-two-point-inclusion; lem-maincb-stage1-raw-refinement; lem-maincb-error-improvement; lem-compcb-rectangular-product
status: proved
af: validated
workspace: proofs/lem-maincb-stage1-call-envelope
provenance: DESIGN-MAINCB-REPAIR-v2.md sect-4 row M19-S1 (amended contract, landed verbatim; supersedes the 2026-07-30 DESIGN-MAIN-STRUCTURE-v5 form); AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED (F1-F3 applied verbatim in v2); user-ratified 2026-08-01 (tobiasosborne, in-session sign-off); source approximate_algebras.tex:917-969,1054-1082,1352-1359,1419-1426
owner: A
---
**Status.** `proved` — af-VALIDATED in-repo (root validated 11/11 nodes clean, re-seed run first-pass, tier routine, 2026-08-01; oracle af-lem-maincb-stage1-call-envelope PASS; the pre-repair runs 1-3 stalled x3 on the anaphoric c_0^cb — the W93-pattern ledger repair closed it). Contract AMENDED per the audited
`DESIGN-MAINCB-REPAIR-v2.md` sect-4 row M19-S1 (aism-jl4g two-defect repair:
unit-clause thread + witness-ledger rebinding; hostile-audit chain
AUDIT-MAINCB-REPAIR.md DESIGN-CONFIRMED; user-ratified 2026-08-01
in-session; supersedes the 2026-07-30 v5 contract). MAIN campaign row
M19-S1. NOT proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
11 / 3 / 14. Per-row skeleton and audit delta:
DESIGN-MAINCB-REPAIR-v2.md sect-4 (and sect-8 re-seed guidance where applicable).
A hard-cap hit is a factoring stop, not a rounds bump. Constants live in the
proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:917-969,1054-1082,1352-1359,1419-1426
