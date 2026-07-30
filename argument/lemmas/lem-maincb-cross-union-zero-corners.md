---
id: lem-maincb-cross-union-zero-corners
kind: lemma
contract: There is a universal e_zero > 0 such that, if A is a finite-dimensional extended epsilon_A-C*-algebra with epsilon_A <= t, a supplied MAIN partition state has w:C^m->A a non-unital extended t-inclusion with one-dimensional images P_j, U,V are disjoint nonempty unions sharing no equivalence class, R = U union V, and t <= e_zero, then dim S^A_{P_U,P_V} = dim S^A_{P_V,P_U} = 0 and dim S^{A_R}_{P_U^R,P_V^R} = dim S^{A_R}_{P_V^R,P_U^R} = 0.
defs: def-maincb-partition-state; def-compressed-corner; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion; def-delta-projection; def-one-dimensional-delta-projection
deps: lem-maincb-nested-corner-dimension-transport; lem-maincb-corner-equivalence; lem-extcb-corner-dimension-additivity; lem-extcb-one-dimensional-corner-dimension
status: proved
af: validated
workspace: proofs/lem-maincb-cross-union-zero-corners
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M11 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1363-1369,1428,1443
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 12-node tree, root
`validated`, taint clean 12/12
(`proofs/lem-maincb-cross-union-zero-corners/export.md`; oracle pass;
tier routine; parallel-af worktree run af-m11). Verifier-driven
completions along the way: the nonvanishing inference rebuilt on the
def-delta-projection second norm alternative, and the unrelated =>
dim 0 step rewired onto the T0 dichotomy provider
lem-extcb-one-dimensional-corner-dimension (defs/deps widened,
contract byte-unchanged). Original-ambient zero corners by additivity;
nested zero corners by M08 dimension transport in both orientations.
MAIN campaign row M11.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M11. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1363-1369,1428,1443
