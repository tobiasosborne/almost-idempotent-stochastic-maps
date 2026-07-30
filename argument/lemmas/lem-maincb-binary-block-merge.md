---
id: lem-maincb-binary-block-merge
kind: lemma
contract: If A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= epsilon_MAIN, a supplied MAIN partition state comes from an extended c_0^cb*epsilon-inclusion w:C^m->A with one-dimensional atomic images, has disjoint nonempty unions U,V sharing no class, and two separately supplied current reset states v_U:B_U->A_U, v_V:B_V->A_V are extended isomorphisms satisfying d_U <= c_0^cb*epsilon_U and d_V <= c_0^cb*epsilon_V, then there is a current reset state v_{U union V}:B_U oplus B_V->A_{U union V} satisfying d_{U union V} <= c_0^cb*epsilon_{U union V}.
defs: def-maincb-partition-state; def-maincb-reset-state; def-maincb-raw-call; def-four-corner-merging-datum
deps: lem-maincb-stage3-raw-merge; lem-maincb-stage3-call-envelope; lem-maincb-reset-invariant-preservation; lem-maincb-structural-domain-ledger
status: stated
af: none
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M26 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1352-1359,1443
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-7 row M26 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M26. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
5 / 2 / 9. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-7 row M26. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1352-1359,1443
