---
id: lem-hiddenness-alpha-slab-leakage
kind: lemma
contract: Hiddenness alpha-slab leakage: for an exact signed idempotent P with delta(P) > 0, nonempty visible set W(P), hidden top vertex v of height H, and any hiddenness dual witness (lambda, alpha, beta) of v with sum_i beta_i < kappa = tau/4 (tau = sqrt(delta)), one has for every c > 0: sum over {i : dist_1(p_i, conv{p_w : w in W}) <= H - c*tau} of alpha_i < (1/2 + delta)/c.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W29 wave (docs/waves/2026-07-06-W29-witness-coupling.md): fresh-codex prover (worker W) + SEPARATE fresh-codex hostile verifier (VW, VALID-WITH-CORRECTIONS — same weakened hypotheses as lem-hiddenness-depth-markov; sign-legality of dropping the lambda term checked; exact fixture)
owner: A
workspace: proofs/lem-hiddenness-alpha-slab-leakage
---

**Role (control of the witness's positive slack, where it is controllable).** The alpha family
of [[lem-hiddenness-dual-witness]] is unbounded in total (A = Σα has no a-priori bound), but
its mass on the DEEP-DEFICIT slab is small: dropping the (nonnegative) λ-term in the same
pairing that proves [[lem-hiddenness-depth-markov]] gives Σ_i α_i ψ_i < (1/2+δ)τ, and Markov
localizes α off the top slab. HONEST LIMIT (VW-confirmed): this is ABSOLUTE α-mass; nothing
bounds α on the top slab (ψ ≈ 0) — e.g. α-mass at v itself is invisible to the balance. Any
coupling argument must live with top-slab α or eliminate it structurally.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
