---
id: lem-maincb-stage1-strict-refinement
kind: lemma
contract: If A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= epsilon_MAIN and an extended c_0^cb*epsilon-inclusion w:C^m->A has some P_j = w(e_j) with dim S_{P_j} > 1, then there is an extended c_0^cb*epsilon-inclusion C^{m+1}->A.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call
deps: lem-maincb-stage1-call-envelope; lem-maincb-stage1-raw-refinement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-stage1-strict-refinement
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M23 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1419-1426
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-7 row M23 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M23. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M23. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1419-1426
