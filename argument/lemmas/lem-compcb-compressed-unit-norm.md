---
id: lem-compcb-compressed-unit-norm
kind: lemma
contract: Compressed-unit norm estimate: there are universal C_co < infinity and e_co > 0 such that, for e=delta+epsilon <= e_co, every delta-projection T satisfies ||u_T|| <= 1+C_co*e, and every nonvanishing T satisfies abs(||u_T||-1) <= C_co*e.
defs: def-extended-epsilon-cstar-algebra; def-delta-projection; def-compressed-corner
deps: lem-compcb-amplified-compression; lem-compcb-amplified-compression-identities
status: proved-mod-audit
af: seeded
provenance: DESIGN-FUDW-DECOMP-v3.md §2.1 (H-CB verdict:72-83); VERDICT-W74F-E-HCB.md HCB-3 correction; VERDICT-FUDW-DECOMP-V3.md §D
owner: A
workspace: proofs/lem-compcb-compressed-unit-norm
---

**Status.** Faithful corrected transcription at `proved-mod-audit`; the
two-sided estimate is restricted to nonvanishing \(T\), exactly as required
by the hostile verdict. It is not L0-rigorous.

**Provenance.** `DESIGN-FUDW-DECOMP-v3.md` §2.1 and
`VERDICT-W74F-E-HCB.md` HCB-3 correction; safe-subset authorization in
`VERDICT-FUDW-DECOMP-V3.md` §D.
