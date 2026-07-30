---
id: lem-maincb-nested-corner-dimension-transport
kind: lemma
contract: There is a universal e_ncd > 0 such that, whenever R,P,Q are t-projections in a finite-dimensional extended t-C*-algebra, R is nonvanishing, all four left/right subordination errors of P,Q to R are at most t <= e_ncd, A_R = S^A_R, P^R = Co^A_R(P), and Q^R = Co^A_R(Q), one has dim S^A_{P,Q} = dim S^{A_R}_{P^R,Q^R}.
defs: def-operator-space; def-compressed-corner; def-delta-projection
deps: lem-maincb-nested-corner-comparison
status: stated
af: seeded
workspace: proofs/lem-maincb-nested-corner-dimension-transport
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.2 row M08 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1054-1082
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.2 row M08 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M08. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
3 / 2 / 7. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.2 row M08. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1054-1082; comparison locus proofs/lem-extcb1-close-corner-dimension/export.md:123-161
