---
id: lem-maincb-direct-corner-envelope
kind: lemma
contract: There are universal L >= 1 and e_env > 0 such that, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= e_env, and w:C^m->A is an extended c_0^cb*epsilon-inclusion, then every nonempty U has P_U a c_0^cb*epsilon-projection, every A_U = S^A_{P_U} is an extended L*epsilon-C*-algebra, and for U subseteq R all subordination and complementarity errors among P_U, P_{R minus U}, P_R are at most L*epsilon.
defs: def-maincb-partition-state; def-compressed-corner; def-delta-projection
deps: lem-maincb-error-improvement; lem-compcb-corner-algebra
status: stated
af: seeded
workspace: proofs/lem-maincb-direct-corner-envelope
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M04 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1068-1084,1367-1368,1428-1435
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.1 row M04 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M04. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M04. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1068-1084,1367-1368,1428-1435
