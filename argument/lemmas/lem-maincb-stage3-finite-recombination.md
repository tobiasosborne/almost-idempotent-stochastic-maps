---
id: lem-maincb-stage3-finite-recombination
kind: lemma
contract: If A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= epsilon_MAIN, a supplied MAIN partition state comes from an extended c_0^cb*epsilon-inclusion w:C^m->A with one-dimensional atomic images and has all equivalence classes C_1,...,C_q, and as initial data every C_a has a finite-dimensional C*-algebra B_{C_a} and current reset isomorphism v_{C_a}:B_{C_a}->A_{C_a} satisfying d_{C_a} <= c_0^cb*epsilon_{C_a}, then there is a current reset isomorphism oplus_{a=1}^q B_{C_a} -> A_{union_a C_a} satisfying the same local invariant at the full union.
defs: def-maincb-partition-state; def-maincb-reset-state; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-maincb-binary-block-merge
status: stated
af: seeded
workspace: proofs/lem-maincb-stage3-finite-recombination
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M27 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1443
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-7 row M27 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M27. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M27. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1443; AUDIT-MAIN-STRUCTURE-v3.md sect-6-8
