---
id: lem-maincb-full-corner-identification
kind: lemma
contract: There is a universal e_full > 0 such that, if R is a t-projection in an extended t-C*-algebra and ||R-I|| <= t <= e_full, then Co_R = I and S_R = A, at every amplification.
defs: def-operator-space; def-compressed-corner; def-delta-projection; def-extended-epsilon-cstar-algebra
deps: lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities
status: proved
af: validated
workspace: proofs/lem-maincb-full-corner-identification
provenance: DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M06 (landed verbatim, LaTeX flattened to registry ASCII); AUDIT-MAIN-STRUCTURE-v5.md REPAIR-CONFIRMED (W78-ratified package); user-ratified 2026-07-30; source approximate_algebras.tex:1064-1066,1542-1544
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 8 live nodes (10 total,
2 archived), root `validated`, taint clean
(`proofs/lem-maincb-full-corner-identification/export.md`; oracle pass;
tier routine; parallel-af worktree run af-m06). One cross-sibling
dependency challenge repaired in-run (the idempotent-rigidity node made
self-contained). Route: level-one closeness -> amplified idempotence ->
idempotent rigidity Co_R = I, S_R = A -> propagation to every
amplification via lem-compcb-amplified-compression. MAIN campaign row
M06.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
4 / 2 / 8. Per-row skeleton and audit delta:
DESIGN-MAIN-STRUCTURE-v5.md sect-4.1 row M06. A hard-cap hit is a factoring stop,
not a rounds bump. Constants live in the proof body, never the contract.

**Provenance loci.** approximate_algebras.tex:1064-1066,1542-1544
