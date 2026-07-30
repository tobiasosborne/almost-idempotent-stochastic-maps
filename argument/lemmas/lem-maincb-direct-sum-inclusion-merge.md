---
id: lem-maincb-direct-sum-inclusion-merge
kind: lemma
contract: There are universal C_dir < infinity and e_dir > 0 such that, if B_1,B_2 are finite-dimensional C*-algebras, P_1,P_2 are target t-projections, ||P_1+P_2-I|| <= t, and v_i:B_i->S_{P_i} are extended t-inclusions with target ambient defect at most t <= e_dir, then (x_1,x_2) |-> v_1(x_1)+v_2(x_2) is an extended C_dir*t-inclusion; bijectivity is asserted only if both v_i are bijective and both target cross-corners vanish.
defs: def-operator-space; def-extended-delta-inclusion; def-compressed-corner
deps: lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities; lem-compcb-corner-algebra; lem-compcb-rectangular-product
status: stated
af: seeded
workspace: proofs/lem-maincb-direct-sum-inclusion-merge
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M05 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1325-1359,1542-1544,1557
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.1 row M05 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M05. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M05. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1325-1359,1542-1544,1557
