---
id: lem-maincb-stage3-call-envelope
kind: lemma
contract: There are universal K_3 >= max{1,L,c_0^cb*L} and e_call_3 > 0, with K_3*e_call_3 <= e_cross, such that, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended c_0^cb*epsilon-inclusion with one-dimensional atomic images, a supplied MAIN partition state for this same A,w has disjoint nonempty unions U,V sharing no class and R = U union V, 0 <= epsilon <= e_call_3, and two separately supplied current reset states for the U,V of that same partition state, v_U:B_U->A_U, v_V:B_V->A_V, are extended isomorphisms satisfying d_U <= c_0^cb*epsilon_U and d_V <= c_0^cb*epsilon_V, then lem-maincb-direct-corner-envelope gives epsilon_U, epsilon_V, epsilon_R <= L*epsilon, so t_3 = K_3*epsilon dominates every lem-maincb-cross-class-merging-datum geometric defect and epsilon_U, epsilon_V, d_U, d_V, epsilon_R, and lem-maincb-cross-class-merging-datum furnishes the explicit Stage-3 four-corner raw-call datum with rho <= C_cross*t_3.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-four-corner-merging-datum; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-direct-corner-envelope; lem-maincb-cross-class-merging-datum
status: stated
af: seeded
workspace: proofs/lem-maincb-stage3-call-envelope
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-S3 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1428,1443
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-6 row M19-S3 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M19-S3. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 3 / 9. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-S3. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1428,1443
