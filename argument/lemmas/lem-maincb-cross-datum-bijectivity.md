---
id: lem-maincb-cross-datum-bijectivity
kind: lemma
contract: After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding lem-maincb-direct-corner-envelope witnesses, and fixing the C_corner_unit,e_corner_unit witnesses of lem-maincb-compressed-corner-unit-comparison, there are universal C_cross^0 >= 1 and 0 < e_cross^0 <= e_corner_unit which are valid witnesses of lem-maincb-cross-class-merging-datum such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0 and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state comes from a non-unital extended t-inclusion w:C^m->A with one-dimensional images P_j, has disjoint nonempty unions U,V sharing no class and R=U union V, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V satisfy epsilon_U,epsilon_V,d_U,d_V <= t <= W.e_cross, d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= t, and ||v_V(I_{B_V})-u_{A_V}|| <= t, then, writing B_R:=B_U oplus B_V, q_U:=(I_{B_U},0), q_V:=(0,I_{B_V}), P_X^R:=Co^A_{P_R}(P_X) for X in {U,V}, gamma_UU:q_U B_R q_U->S^{A_R}_{P_U^R} defined by gamma_UU((b_U,0)):=Co^{A_R}_{P_U^R}(Co^A_{P_R}(v_U(b_U))), gamma_VV:q_V B_R q_V->S^{A_R}_{P_V^R} defined by gamma_VV((0,b_V)):=Co^{A_R}_{P_V^R}(Co^A_{P_R}(v_V(b_V))), gamma_UV:q_U B_R q_V={0}->S^{A_R}_{P_U^R,P_V^R}={0} the unique map, and gamma_VU:q_V B_R q_U={0}->S^{A_R}_{P_V^R,P_U^R}={0} the unique map, the explicit Stage-3 amplified four-corner datum in A_R furnished by lem-maincb-cross-class-merging-datum has these four fixed level-one maps and gamma_UU,gamma_UV,gamma_VU,gamma_VV are bijective.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-witness-ledger; def-four-corner-merging-datum; def-compressed-corner; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-one-dimensional-delta-projection
deps: lem-maincb-error-improvement; lem-maincb-direct-corner-envelope; lem-maincb-compressed-corner-unit-comparison; lem-maincb-cross-class-merging-datum; lem-maincb-outer-compression-transfer; lem-maincb-cross-union-zero-corners
status: proved
af: validated
workspace: proofs/lem-maincb-cross-datum-bijectivity
provenance: DESIGN-M17-TYPING-v3.md item 1 (v2 sect-2 proof route with audit F2 corner typing + F3 complete imports, landed verbatim); AUDIT-M17-TYPING-v2.md VALID-WITH-CORRECTIONS; user-ratified 2026-08-01 (tobiasosborne, in-session sign-off, third ratification); source approximate_algebras.tex:1325-1345,1363-1369
owner: A
---

**Status.** `proved` — af-VALIDATED in-repo (root validated 12/12 nodes clean, run 1 + verify resumes, tier routine, 2026-08-01; oracle PASS). Contract transcribed verbatim from the ratified
`DESIGN-M17-TYPING-v3.md` item 1 (the bijectivity bridge for the M12
four-corner datum; hostile-audit chain AUDIT-M17-TYPING-v2.md). NOT
proved in-repo; af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. Proof route: the diagonal maps are explicit compression
composites of the supplied extended reset ISOMORPHISMS (bijective by
def-extended-delta-inclusion; level-one bijectivity through the exported
compression clauses); the cross maps are the unique maps between zero
corners (lem-maincb-cross-union-zero-corners). A hard-cap hit is a
factoring stop, not a rounds bump.

**Provenance loci.** approximate_algebras.tex:1325-1345,1363-1369
