---
id: lem-maincb-maximal-reset-selection
kind: lemma
contract: If A is a finite-dimensional extended epsilon-C*-algebra with 0 <= epsilon <= epsilon_MAIN, then the nonempty set of m admitting an extended c_0^cb*epsilon-inclusion C^m->A has a maximum, because the lower norm is positive and hence m <= dim_C A.
defs: def-maincb-reset-state; def-projection-basis
deps: lem-maincb-structural-domain-ledger; lem-maincb-initial-reset-inclusion
status: stated
af: none
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M22 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1417
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-7 row M22 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M22. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M22. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1417; elementary finite-dimensional selection
