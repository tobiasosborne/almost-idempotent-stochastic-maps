---
id: lem-hybrid-dual-certificate
kind: lemma
contract: Hybrid dual certificate: for an exact signed idempotent P, a hidden geometrically distinct row vertex v with hiddenness dual witness (lambda, alpha, beta) of objective B = sum_i beta_i, the hybrid weights mu_k = sum over f in F_v of lambda_f * P_fk satisfy sum_k mu_k = 1 and sum_k max(-mu_k, 0) <= delta(P); and if L_mu = sum over {k in F_v} of max(mu_k, 0) > 0, then t*(v) <= (B + sum_k max(-mu_k, 0)) / L_mu.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W37 wave (docs/waves/2026-07-07-W37-bridge.md): fresh-codex prover (worker AF, the single-substitution hybrid circuit) + SEPARATE fresh-codex hostile verifier (VAF, VALID — the substituted balance re-derived (d_f = sum_k P_fk d_k), the positive/negative resplit into a new feasible dual point checked, the tautology analysis confirmed: L_mu <= 1 + delta so the bound is weak — t*(v)*(L_mu - 1) <= delta at best)
owner: A
workspace: proofs/lem-hybrid-dual-certificate
---

**Role (the λ·P hybrid circuit, priced honestly).** One structural substitution of row
reproduction into the witness balance yields an almost-convex weight system μ = λP (total 1,
negative part ≤ δ — a λ-average of row negative masses) and a NEW feasible dual point whose
objective is (B + ν(μ))/L_μ. The wave's finding: the hybrid does NOT amplify — its bound is
near-tautological (L_μ ≤ 1 + δ). Banked to close the direction (do not re-run λP-substitution
waves without a genuinely new normalization idea); the μ-system's bookkeeping (total/negative
part) is reusable.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
