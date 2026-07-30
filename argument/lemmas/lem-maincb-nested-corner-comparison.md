---
id: lem-maincb-nested-corner-comparison
kind: lemma
contract: There are universal C_nest < infinity and e_nest > 0 such that, whenever R,P,Q are t-projections in a finite-dimensional extended t-C*-algebra, R is nonvanishing, P,Q are subordinate to R with all four left/right subordination errors at most t <= e_nest, A_R = S^A_R, P^R = Co^A_R(P), and Q^R = Co^A_R(Q), then P^R,Q^R are C_nest*t-projections in A_R and, at every amplification, ||F^R_{P,Q}(Co^A_R X) - X|| <= C_nest*t*||X|| for X in S^A_{P,Q}, while ||Co^A_{P,Q} Y - Y|| <= C_nest*t*||Y|| for Y in S^{A_R}_{P^R,Q^R}.
defs: def-operator-space; def-compressed-corner; def-delta-projection
deps: lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities; lem-compcb-amplified-almost-containment; lem-compcb-corner-algebra; lem-compcb-rectangular-product
status: stated
af: none
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.2 row M07 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1054-1082,1435-1441
owner: A
---

**Status.** `stated` — contract transcribed from the audited
`DESIGN-MAIN-STRUCTURE-v5.md` sect-4.2 row M07 (REPAIR-CONFIRMED audit chain
v2..v5; W78-ratified package; full MAIN row package user-ratified
2026-07-30 in-session). MAIN campaign row M07. NOT proved in-repo;
af elevation pending.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
11 / 3 / 15. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.2 row M07. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1054-1082,1435-1441
