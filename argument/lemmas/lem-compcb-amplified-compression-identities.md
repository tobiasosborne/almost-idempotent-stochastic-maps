---
id: lem-compcb-amplified-compression-identities
kind: lemma
contract: Amplified compression identities: there is a universal e_cmp > 0 such that, whenever A is an extended epsilon-C*-algebra, e=delta+epsilon <= e_cmp, P,Q are delta-projections in A, n >= 1, and X is in M_n tensor A, one has Co_{P_n,Q_n}^2=Co_{P_n,Q_n} and Co_{P_n,Q_n}(X)^dagger=Co_{Q_n,P_n}(X^dagger), where P_n=I_n tensor P and Q_n=I_n tensor Q.
defs: def-extended-epsilon-cstar-algebra; def-delta-projection; def-compressed-corner
deps: lem-compcb-amplified-compression
status: proved-mod-audit
af: seeded
provenance: DESIGN-FUDW-DECOMP-v3.md §2.1 (DECOMP:152-183; TeX 1054-1064,1542-1544); VERDICT-FUDW-DECOMP-V3.md §§2.2,D
owner: A
workspace: proofs/lem-compcb-amplified-compression-identities
---

**Status.** Faithful safe-subset transcription at `proved-mod-audit`; it is
not `cited`, not `af`-validated, and not L0-rigorous.

**Provenance.** `DESIGN-FUDW-DECOMP-v3.md` §2.1 at the recorded source loci;
safe-subset authorization and faithfulness finding in
`VERDICT-FUDW-DECOMP-V3.md` §§2.2,D.

**Contract amendment (2026-07-24, orchestration #3).** The codified contract
left the ambient `A` unbound (challenge `ch-95a269be39e1e821`: never assumed
`A` an extended epsilon-C*-algebra with `P,Q` in `A`). Amended to the af
prover's corrected root text, demanded by the fresh in-tree verifier —
a mechanical verdict-driven contract amendment (session-23 standing
precedent), recorded here and in the commit. No strengthening: the added
clauses are the intended (and used) hypotheses of the source proof
(PROOF-W74F-E-HCB.md ambient conventions §1).
