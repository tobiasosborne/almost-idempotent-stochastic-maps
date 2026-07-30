---
id: lem-maincb-direct-corner-envelope
kind: lemma
contract: There are universal L >= 1 and e_env > 0 such that, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= e_env, and w:C^m->A is an extended c_0^cb*epsilon-inclusion, then every nonempty U has P_U a c_0^cb*epsilon-projection, every A_U = S^A_{P_U} is an extended L*epsilon-C*-algebra, and for U subseteq R all subordination and complementarity errors among P_U, P_{R minus U}, P_R are at most L*epsilon.
defs: def-maincb-partition-state; def-compressed-corner; def-delta-projection; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-error-improvement; lem-compcb-corner-algebra
status: proved
af: validated
workspace: proofs/lem-maincb-direct-corner-envelope
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M04 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1068-1084,1367-1368,1428-1435
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 7-node tree, root
`validated`, taint clean 7/7
(`proofs/lem-maincb-direct-corner-envelope/export.md`; oracle pass;
tier routine; parallel-af worktree run af-m04). One challenge (a
hidden partition-state assumption) repaired by a bridge defining
P_U = w(e_U), A_U = S^A_{P_U} directly from the displayed (A,w). MAIN
campaign row M04.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M04. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1068-1084,1367-1368,1428-1435
