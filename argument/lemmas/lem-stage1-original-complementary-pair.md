---
id: lem-stage1-original-complementary-pair
kind: lemma
contract: There are universal C_np<infinity and e_np>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_np and 1<dim_C calX<infinity contains nonvanishing C_np*epsilon_X-projections P' and P'' for the original product such that P'+P''=I_X and ||P'P''||,||P''P'||<=C_np*epsilon_X.
defs: def-extended-epsilon-cstar-algebra; def-delta-projection
deps: lem-stage1-rectified-nontrivial-projection
status: proved
af: validated
workspace: proofs/lem-stage1-original-complementary-pair
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 9-node tree, root
`validated`, taint clean 9/9
(`proofs/lem-stage1-original-complementary-pair/export.md`; oracle
pass; tier routine, 9 nodes <= cap 10, budget 6/2/10 + ratified
open-challenge resume at max-rounds 6). ONE major challenge raised and
repaired: node 1.3 had unjustifiably equated the original unit with an
exact two-sided unit; the prover factored 1.3 into 1.3.1/1.3.2 and
enlarged C_np to absorb the general-unit O(epsilon_X) complement
error — fresh verifiers then accepted all 9 nodes. Route (per the
prover build summary): take the C1 nontrivial projection P_0 and its
complement, prove both cross-products equal P_0-P_0^2 up to the
controlled unit error, and transfer nonvanishing + defect bounds to
the original product.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
6 / 2 / 10. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-original-complementary-pair); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:917-929,1419-1424`
