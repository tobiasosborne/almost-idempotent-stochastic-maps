---
id: lem-hcb3-offdiagonal-inverse
kind: lemma
contract: Off-diagonal Ha inverse propagation: there are universal C_rect < infinity and e_rect > 0 such that, for every H-CB datum with e <= e_rect, if Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} has level-one lower modulus at least 1/4, then every amplification of Ha^Q_{P,R} is bijective with inverse norm at most 1+C_rect*e.
defs: def-ha-map; def-hcb-datum
deps: lem-hcb2-amplified-adjointness; lem-hcb2-product-defect; lem-hcb3-diagonal-lower-modulus; lem-compcb-corner-algebra; lem-hcb3-uniform-square-lower; lem-hcb3-diagonal-inverse
status: proved
af: validated
provenance: PROOF-W74F-E-HCB.md §7.4; VERDICT-W74F-E-HCB.md HCB-3 conditional correction; DESIGN-FUDW-DECOMP-v3.md §2.1; VERDICT-FUDW-DECOMP-V3.md §D
owner: A
workspace: proofs/lem-hcb3-offdiagonal-inverse
---

**Status.** `proved`; `af: validated` — root-validated, taint-clean
adversarial tree (16/16; mechanical ledger reflection; export at
`proofs/lem-hcb3-offdiagonal-inverse/export.md`). Both level-one hypotheses
remain load-bearing in the contract.

**Provenance.** `PROOF-W74F-E-HCB.md` §7.4 and the conditional correction
in `VERDICT-W74F-E-HCB.md`; admitted by
`VERDICT-FUDW-DECOMP-V3.md` §D.
