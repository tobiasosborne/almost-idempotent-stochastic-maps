---
id: lem-maincb-stage2-call-envelope
kind: lemma
contract: There are universal K_2 >= max{1,L,c_0^cb*L} and e_call_2 > 0, with K_2*e_call_2 <= e_s2, such that, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended c_0^cb*epsilon-inclusion with one-dimensional atomic images, a supplied MAIN partition state for this same A,w has nonempty U contained in one equivalence class, j notin U belonging to that same class, and R = U union {j}, 0 <= epsilon <= e_call_2, and a supplied current reset state for the U of that same partition state, v_U:M_{|U|}->A_U, is an extended isomorphism satisfying d_U <= c_0^cb*epsilon_U, then lem-maincb-direct-corner-envelope gives epsilon_U, epsilon_R <= L*epsilon, so t_2 = K_2*epsilon dominates every lem-maincb-stage2-extcb-datum geometric defect and epsilon_U, d_U, epsilon_R, and lem-maincb-stage2-extcb-datum furnishes the explicit Stage-2 EXT raw-call datum with post-helper total defect at most C_s2*t_2.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-extcb-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-direct-corner-envelope; lem-maincb-stage2-extcb-datum
status: stated
af: seeded
workspace: proofs/lem-maincb-stage2-call-envelope
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-S2 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1428-1441
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-6 row M19-S2 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M19-S2. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 3 / 9. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-S2. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1428-1441
