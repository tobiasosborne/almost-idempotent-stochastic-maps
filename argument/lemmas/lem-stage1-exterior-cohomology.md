---
id: lem-stage1-exterior-cohomology
kind: lemma
contract: Exterior cohomology of a finite H-space over the real field: if M is a connected CW complex with dim_reals H^*(M;reals) < infinity and (M,mu,e) is an H-space, set A=H^*(M;reals), A^+=direct_sum_{k>0} A^k, and Delta=(cross product)^(-1) o mu^*; then A is a finite-dimensional graded-commutative associative unital algebra with A^0=reals*1, Delta:A->A tensor_reals A is a degree-preserving unital algebra homomorphism with Delta(1)=1 tensor 1, for every homogeneous a in A^+ there exist a finite set J_a and homogeneous a'_j,a''_j in A^+ for j in J_a such that Delta(a)=a tensor 1+1 tensor a+sum_{j in J_a} a'_j tensor a''_j, and A is isomorphic as a graded algebra to an exterior algebra on a finite family of odd-positive-degree homogeneous generators.
defs: def-h-space-left-inversion
deps: lem-stage1-hspace-coproduct-tail
status: proved
af: validated
workspace: proofs/lem-stage1-exterior-cohomology
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 8-node tree, root
`validated`, taint clean 8/8, ZERO challenges
(`proofs/lem-stage1-exterior-cohomology/export.md`; oracle
`af-lem-stage1-exterior-cohomology` pass; run tier routine, 8 nodes ==
design target 8 <= cap 12, budget 8/3/12). Workspace: 1 def + T0 dep A0
+ the two Hatcher GT externals (quote-at-locus 2/2). Contract
transcribed VERBATIM from the audited `DESIGN-S1-ENDGAME-v5.md` sect-2
(audit v5 LAND; user ratified 2026-07-30). Elevation position 2/13.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
8 / 3 / 12. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-exterior-cohomology); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** exact printed conditions `refs/hatcher-algebraic-topology/AT.txt:17654-17677`; exact Theorem 3C.4 `:17798-17800`; grading guide `refs/kitaev-2405.02434/approximate_algebras.tex:1016`; finite-total-dimensional guide `:1009-1022`
