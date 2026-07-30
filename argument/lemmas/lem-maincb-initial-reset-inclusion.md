---
id: lem-maincb-initial-reset-inclusion
kind: lemma
contract: For every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= epsilon_MAIN, there is an extended c_0^cb*epsilon-inclusion C->A.
defs: def-maincb-reset-state; def-maincb-raw-call; def-operator-space; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-initial-raw-inclusion; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-initial-reset-inclusion
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M21 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:430-455,1317-1319,1417
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-7 row M21 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M21. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
3 / 2 / 7. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M21. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:430-455,1317-1319,1417
