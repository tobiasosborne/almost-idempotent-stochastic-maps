---
id: lem-maincb-stage1-call-envelope
kind: lemma
contract: After the Stage-1 producer gate, there are universal K_1 >= 1 and e_call_1 > 0, with K_1*e_call_1 <= e_1 and all Stage-1-producer/old-side prerequisite thresholds absorbed into e_call_1, such that, if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= e_call_1, w:C^m->A is a supplied extended c_0^cb*epsilon-inclusion (including its unit clause), and some P_j = w(e_j) has dim S_{P_j} > 1, then the three Stage-1 producers and the literal old-side compression furnish an explicit Stage-1 raw-call datum satisfying lem-maincb-stage1-raw-refinement with base scale t_1 = K_1*epsilon.
defs: def-maincb-reset-state; def-maincb-raw-call; def-maincb-partition-state
deps: lem-maincb-direct-corner-envelope; lem-compcb-single-compression-transfer; lem-stage1-rectified-nontrivial-projection; lem-stage1-original-complementary-pair; lem-stage1-fresh-two-point-inclusion
status: stated
af: seeded
workspace: proofs/lem-maincb-stage1-call-envelope
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-S1 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:917-969,1419-1426
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-6 row M19-S1 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M19-S1. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 3 / 11. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-6 row M19-S1. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:917-969,1419-1426
