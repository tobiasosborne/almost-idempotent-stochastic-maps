---
id: lem-stage1-rectified-nontrivial-projection
kind: lemma
contract: There are universal C_proj<infinity and e_proj>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_proj and 1<dim_C calX<infinity contains a nontrivial C_proj*epsilon_X-projection P_0 for the original product and original unit I_X.
defs: def-extended-epsilon-cstar-algebra; def-epsilon-cstar-algebra; def-delta-projection
deps: lem-stage1-rectified-cstar-control; lem-stage1-fixed-unitary-projection-bridge
status: proved
af: validated
workspace: proofs/lem-stage1-rectified-nontrivial-projection
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 7-node tree, root
`validated`, taint clean 7/7
(`proofs/lem-stage1-rectified-nontrivial-projection/export.md`; oracle
pass; tier routine, 7 nodes <= cap 10, budget 6/3/10). Zero challenges
— first-pass validation (one transient blocked verdict on 1.6 resolved
once its dependencies validated). Route: rectify via
lem-stage1-rectified-cstar-control, apply the C0 bridge
lem-stage1-fixed-unitary-projection-bridge once, transfer the
projection defect and both nonvanishing bounds back to the original
product and original unit I_X.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 3 / 10. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-rectified-nontrivial-projection); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:917-945`; exact-unit provider `argument/lemmas/lem-stage1-rectified-cstar-control.md:4`
