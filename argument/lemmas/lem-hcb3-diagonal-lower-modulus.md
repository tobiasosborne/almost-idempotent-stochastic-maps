---
id: lem-hcb3-diagonal-lower-modulus
kind: lemma
contract: Diagonal Ha lower-modulus propagation: there are universal C_diag < infinity and e_diag > 0 such that, for every H-CB datum with e <= e_diag, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then ||(Ha^Q_{P,P})_n(Z)|| >= (1-C_diag*e)||Z|| for every n >= 1 and Z in M_n tensor S_P.
defs: def-ha-map; def-hcb-datum
deps: lem-hcb2-amplified-adjointness; lem-hcb2-product-defect; lem-compcb-corner-algebra; lem-hcb3-uniform-square-lower
status: proved
af: validated
provenance: PROOF-W74F-E-HCB.md §7.3; VERDICT-W74F-E-HCB.md HCB-3 conditional correction; DESIGN-FUDW-DECOMP-v3.md §2.1; VERDICT-FUDW-DECOMP-V3.md §D; report lem:hcb3-diagonal-lower-modulus
owner: A
workspace: proofs/lem-hcb3-diagonal-lower-modulus
---

**Status.** `proved`; `af: validated` — root-validated, taint-clean
adversarial tree (29/29; mechanical ledger reflection; export at
`proofs/lem-hcb3-diagonal-lower-modulus/export.md`). The level-one
lower-modulus hypothesis remains load-bearing in the contract.

**Provenance.** `PROOF-W74F-E-HCB.md` §7.3 and the conditional correction
in `VERDICT-W74F-E-HCB.md`; admitted by
`VERDICT-FUDW-DECOMP-V3.md` §D.
