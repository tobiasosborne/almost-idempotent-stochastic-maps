---
id: lem-maincb-cross-union-zero-corners
kind: lemma
contract: There is a universal e_zero > 0 such that, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state has w:C^m->A a non-unital extended t-inclusion with one-dimensional images P_j, U,V are disjoint nonempty unions sharing no equivalence class, R = U union V, and t <= e_zero, then dim S^A_{P_U,P_V} = dim S^A_{P_V,P_U} = 0 and dim S^{A_R}_{P_U^R,P_V^R} = dim S^{A_R}_{P_V^R,P_U^R} = 0.
defs: def-maincb-partition-state; def-compressed-corner
deps: lem-maincb-nested-corner-dimension-transport; lem-maincb-corner-equivalence; lem-extcb-corner-dimension-additivity
status: stated
af: none
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M11 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1363-1369,1428,1443
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.3 row M11 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M11. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M11. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1363-1369,1428,1443
