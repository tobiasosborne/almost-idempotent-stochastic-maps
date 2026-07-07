---
id: lem-hiddenness-depth-markov
kind: lemma
contract: Hiddenness depth-Markov: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), hidden top vertex v of height H, and any hiddenness dual witness (lambda, alpha, beta) of v with sum_i beta_i < kappa = tau/4 (tau = sqrt(delta)), one has for every c > 0: lambda{f in F_v : dist_1(p_f, conv{p_w : w in W}) > H - c*tau} > 1 - (1/2 + delta)/c.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-hiddenness-dual-witness
status: proved
af: validated
provenance: W29 wave (docs/waves/2026-07-06-W29-witness-coupling.md): fresh-codex prover (worker W) + SEPARATE fresh-codex hostile verifier (VW, VALID-WITH-CORRECTIONS — the corrections WEAKEN the hypotheses: the c-parametric bound needs no tallness and no delta cutoff, only a witness with sum beta < kappa; quantifier check confirms it holds for EVERY witness tuple, no optimality/CS used; exact W19 7x7 fixture at two c values)
owner: A
workspace: proofs/lem-hiddenness-depth-markov
---

**Role (the quantitative form of "hidden tops have deep, far company").** Strengthens
[[lem-top-slab-companion]] from existence to measure: pairing the witness of
[[lem-hiddenness-dual-witness]] with the affine deficit psi = H − phi (phi the ell1/ell-infty
support functional at v; 0 ≤ psi ≤ D = 2+4δ; pairing legal since psi is affine, psi(p_v) = 0)
gives Σ_f λ_f ψ_f < κD = (1/2+δ)τ; Markov on the probability λ plus ψ_f ≥ H − d_f yields the
contract. This is W29's verified half; the missing half of [[conj-min-a-w4]] is the
COEFFICIENT-COUPLING lemma (no comparison between λ_f and P_vf⁺ exists yet — the named gap).

**Corollary (body, VW-checked exactly, strict even at the endpoint).** If additionally
H > 13τ and δ ≤ δ₁ = (17−12√2)/2: taking c = H/τ − 4 (> 9; threshold H − cτ = 4τ exactly)
gives λ(F_v ∩ G_4) > 1 − (1/2+δ)/9 ≥ 2√2/3 ≈ 0.943, using 1/2 + δ₁ = 9 − 6√2 = 3(3−2√2).
More than 94% of every witness's mass sits on rows simultaneously ρ-far from v AND in G_4.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate (single
dep, reviewed→queued).
