---
id: lem-maincb-one-class-extension
kind: lemma
contract: If A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= epsilon_MAIN, a supplied MAIN partition state comes from an extended c_0^cb*epsilon-inclusion w:C^m->A, all atomic images P_j are one-dimensional, and C = {j_1,...,j_s} is one equivalence class, then there is a current reset state v_C:M_s->A_C that is an extended isomorphism and satisfies the local invariant d_C <= c_0^cb*epsilon_C; moreover epsilon_C <= K_call*epsilon, so the bound d_C <= c_0^cb*K_call*epsilon follows.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call
deps: lem-maincb-direct-corner-envelope; lem-maincb-corner-equivalence; lem-maincb-initial-raw-inclusion; lem-maincb-stage2-raw-extension; lem-maincb-stage2-call-envelope; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
status: stated
af: seeded
workspace: proofs/lem-maincb-one-class-extension
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M25 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1430-1441
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-7 row M25 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M25. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
7 / 3 / 11. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M25. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1430-1441
