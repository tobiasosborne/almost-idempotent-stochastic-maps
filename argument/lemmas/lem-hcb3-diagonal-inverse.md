---
id: lem-hcb3-diagonal-inverse
kind: lemma
contract: Diagonal Ha inverse propagation: there are universal C_inv < infinity and e_inv > 0 such that, for every H-CB datum with e <= e_inv, if Ha^Q_{P,P} has level-one lower modulus at least 1/4 and is bijective at level one, then every amplification is bijective and ||((Ha^Q_{P,P})_n)^(-1)|| <= 1+C_inv*e.
defs: def-ha-map; def-hcb-datum
deps: lem-hcb3-diagonal-lower-modulus; lem-hcb2-amplified-adjointness; lem-hcb2-product-defect; lem-compcb-corner-algebra; lem-hcb3-uniform-square-lower
status: proved
af: validated
provenance: PROOF-W74F-E-HCB.md §7.3 (7.10); VERDICT-W74F-E-HCB.md HCB-3 conditional correction; DESIGN-FUDW-DECOMP-v3.md §2.1; VERDICT-FUDW-DECOMP-V3.md §D
owner: A
workspace: proofs/lem-hcb3-diagonal-inverse
---

**Status.** `proved`; `af: validated` — root-validated, taint-clean
adversarial tree (5/5; mechanical ledger reflection; export at
`proofs/lem-hcb3-diagonal-inverse/export.md`). The level-one bijectivity and
lower-modulus hypotheses remain load-bearing in the contract.

**Provenance.** `PROOF-W74F-E-HCB.md` §7.3 and the conditional correction
in `VERDICT-W74F-E-HCB.md`; admitted by
`VERDICT-FUDW-DECOMP-V3.md` §D.
