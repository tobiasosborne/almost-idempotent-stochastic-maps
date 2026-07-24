---
id: conj-hcb
kind: lemma
contract: H-CB: there are universal C_H < infinity and e_H > 0 such that, whenever e=delta+epsilon <= e_H, Q is a level-one one-dimensional delta-projection in an extended epsilon-C*-algebra A, and P,R,S are delta-projections, the maps 1_{M_n} tensor Ha^Q_{P,R}, under the COL-HILB identification with operators on C^n tensor S_{R,Q} and C^n tensor S_{P,Q}, satisfy for every n the adjoint equality, product defect at most C_H*e*||Z||||W||, and the uniform unit, norm, inverse, homomorphism, and canonical-identity closeness estimates required by lem_extension, with constants independent of n, dim A, block count, and block dimensions.
defs: def-extended-epsilon-cstar-algebra; def-ha-map
deps:
status: conjecture
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md §3 H-CB; hostile batch verdict VERDICT-W74F-BATCH.md §C (VALID decomposition, H-CB remains a GAP); report conj:hcb
owner: A
workspace: proofs/conj-hcb
---

**Open gap.** This is the H-CB node isolated by W74F-C.  It is a
`conjecture` with empty `deps`, not an imported theorem.

The level-one adjoint and product estimates do not automatically
amplify by treating \(I_n\otimes Q\) as one-dimensional: it is not.
The contract therefore requires whole-column operator estimates under
the corrected COL-HILB identification.  A proof or counterexample is
the first-priority Route-F decider.
