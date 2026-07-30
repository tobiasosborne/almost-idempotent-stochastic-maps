---
id: lem-maincb-corner-equivalence
kind: lemma
contract: There is a universal e_sim > 0 such that, for every finite family of one-dimensional t-projections P_1,...,P_m in an extended t-C*-algebra with t <= e_sim, the relation j ~ k iff dim S_{P_j,P_k} = 1 is an equivalence relation.
defs: def-maincb-partition-state; def-one-dimensional-delta-projection; def-compressed-corner; def-extended-epsilon-cstar-algebra; def-delta-projection
deps: lem-extcb-one-dimensional-product; lem-extcb-one-dimensional-corner-dimension
status: proved
af: validated
workspace: proofs/lem-maincb-corner-equivalence
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M10 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1162-1187
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 8-node tree, root
`validated`, taint clean 8/8
(`proofs/lem-maincb-corner-equivalence/export.md`; oracle pass; tier
routine; parallel-af worktree run af-m10). One challenge repaired: the
root's threshold inference was false at the allowed boundary t = e_sim
— repaired by fixing a universal NON-STRICT threshold node (1.1).
Route: reflexivity + symmetry via the involution; transitivity via a
nonzero compressed product + the one-dimensional corner-dimension
bound. MAIN campaign row M10.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.3 row M10. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1162-1187
