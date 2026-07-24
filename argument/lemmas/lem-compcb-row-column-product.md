---
id: lem-compcb-row-column-product
kind: lemma
contract: Row-column compressed-product estimate: there are universal C_rc < infinity and e_rc > 0 such that, whenever e = delta+epsilon <= e_rc, P,Q are delta-projections in an extended epsilon-C*-algebra A, n >= 1, and X,Y are in M_{n,1} tensor S_{P,Q}, one has ||Co_Q(Y^dagger X) - Y^dagger X|| <= C_rc*e*||Y||*||X||, where Y^dagger X is the ambient product of the 1-by-n row Y^dagger with the n-by-1 column X.
defs: def-extended-epsilon-cstar-algebra; def-delta-projection; def-compressed-corner; def-column-hilbert-corner
deps: lem-compcb-rectangular-product; lem-compcb-amplified-compression
status: proved
af: validated
provenance: factored out of proofs/lem-hcb-column-hilbert-squared per the 3rd-stall tripwire (2026-07-25, challenge ch-80ba7318f6e1e540 node 1.3.2 — the validated rectangular-product contract quantifies over square M_m amplifications only; the row/column pair (Y^dagger, X) needs its own estimate); UNPROVED here pending its own af pass
owner: A
workspace: proofs/lem-compcb-row-column-product
---

**Status.** `stated` — the row/column instantiation gap named by the blocking
challenge in orchestration #12: [[lem-compcb-rectangular-product]]'s validated
compatibility clause requires both factors inside one square amplification
M_m tensor A, which the 1-by-n / n-by-1 pair does not satisfy. Factored per
the campaign's 3rd-stall tripwire rule; the af pass is the proof.

**Mechanism sketch (not a proof, from the challenge's own repair route).**
Embed the row and column as off-diagonal blocks of M_{n+1} tensor A with block
delta-projections; corner membership + identification of the compressed and
ambient products + norm preservation then let the validated square
rectangular-product estimate apply.
