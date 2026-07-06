---
id: lem-rho-near-residual-cancellation
kind: lemma
contract: Residual cancellation at a hidden top: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), hidden top vertex v of height H > a*tau (tau = sqrt(delta), any halo width a > 0), and ANY subset C of row indices with S = sum over C of max(P_vj, 0) < 1, writing A = sum over {j not in C : dist_1(p_j, conv W) <= a*tau} of max(P_vj, 0), one has A*(H - a*tau) <= nu_v*(H + 2 + 4*delta).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-invisible-mass; def-height
deps: lem-mass-split; lem-residual-lower; lem-residual-upper
status: proved
af: none
provenance: W38 wave (docs/waves/2026-07-07-W38-self-cluster.md): fresh-codex prover (worker AG) + SEPARATE fresh-codex hostile verifier (VAG, VALID-WITH-CORRECTIONS — the deep-outside term B is priced at H BEFORE cancelling, making the cancellation exact; the rho-near condition on C is UNUSED by the identity, so C is arbitrary; exact fixtures at a = 1/8 on the W29 frontier and the a = 4 hypothesis-failure case flagged)
owner: A
workspace: proofs/lem-rho-near-residual-cancellation
---

**Role (the route-death certificate for the renormalized self-cluster split, in lemma form).**
Splitting a hidden top's row around ANY subset C and pricing the residual (lower + upper
residual lemmas, both af-validated) makes the deep-outside term CANCEL EXACTLY — what remains
bounds only the SHALLOW-outside mass A by O(ν_v). Consequences kept loud: in the pure-cluster
case (deep-outside = 0) it gives 1 − S ≤ ν_v(2+4δ+aτ)/(H−aτ) = O(τ) in tall regimes — i.e.
S = 1 − O(τ) clusters are CONSISTENT with all residual identities; the renormalized budget
ν/(1−S) exactly pays the height. Do NOT re-run the naive self-cluster split (FINDINGS
2026-07-07 W37+W38); the surviving question is [[conj-near-cluster-absorption]].

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
