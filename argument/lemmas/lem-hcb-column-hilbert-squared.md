---
id: lem-hcb-column-hilbert-squared
kind: lemma
contract: Corrected amplified column-Hilbert estimate: there are universal C_col < infinity and e_col > 0 such that every H-CB datum with e <= e_col, every n >= 1, and every X in M_{n,1} tensor S_{P,Q} satisfy abs(<X,X>_n-||X||_{n,1}^2) <= C_col*e*||X||_{n,1}^2.
defs: def-hcb-datum; def-column-hilbert-corner
deps: lem-compcb-rectangular-product; lem-compcb-compressed-unit-norm
status: proved-mod-audit
af: none
provenance: PROOF-W74F-E-HCB.md §§1.2,5; VERDICT-W74F-E-HCB.md HCB-1b; DESIGN-FUDW-DECOMP-v3.md §2.1; VERDICT-FUDW-DECOMP-V3.md §D
owner: A
workspace: proofs/lem-hcb-column-hilbert-squared
---

**Status.** Hostile-verdict-compatible transcription at
`proved-mod-audit`; it records the corrected squared estimate and is not
L0-rigorous.

**Provenance.** `PROOF-W74F-E-HCB.md` §§1.2,5 and
`VERDICT-W74F-E-HCB.md` HCB-1b; safe-subset row in
`VERDICT-FUDW-DECOMP-V3.md` §D.
