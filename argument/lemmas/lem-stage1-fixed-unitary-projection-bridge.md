---
id: lem-stage1-fixed-unitary-projection-bridge
kind: lemma
contract: Fixed-unitary projection bridge: there are universal C_bridge<infinity and e_bridge^r>0 such that every finite-dimensional exact-unit epsilon_r-C*-algebra with 0<=epsilon_r<=e_bridge^r and 1<dim_C calX<infinity contains a nontrivial C_bridge*epsilon_r-projection P for the product bold-dot and unit J.
defs: def-epsilon-cstar-algebra; def-stage1-polar-witness-data; def-approximate-unitary-space; def-delta-projection
deps: lem-stage1-extra-fixed-class
status: proved
af: validated
workspace: proofs/lem-stage1-fixed-unitary-projection-bridge
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 10-node tree, root
`validated`, taint clean 10/10
(`proofs/lem-stage1-fixed-unitary-projection-bridge/export.md`; oracle
pass; tier routine, 10 nodes <= cap 12, budget 8/3/12). Two challenges
(an unbound Q in two leaf scopes) raised and repaired. Architecture (b)
validated: B1 applied exactly once internally, the nontrivial
C_bridge*epsilon_r-projection P=(2I+U+U^dagger)/4 (tex:939) exported.
Contract VERBATIM from DESIGN-S1-ENDGAME-v5 sect-2 (audit v5 LAND;
ratified 2026-07-30). Position 10/13.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-fixed-unitary-projection-bridge); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:917-943`, formula and estimate at `:939`
