---
id: lem-intersection-witness-confinement
kind: lemma
contract: Intersection-branch witness confinement: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set, hidden top vertex v with t*(v) in (0, kappa), and an alpha-free reduced optimal display sum over T of lambda_f*(p_f - p_v) = t*(v)*sum over O of gamma_i*(p_i - p_v) (lambda, gamma probability vectors on T(v), O(v), per lem-optimal-face-conic-reduction): (B1) (lambda, 0, t*gamma) is a hiddenness dual witness of v with sum beta = t*(v) < kappa; (B2) the witness barycenter b = sum lambda_f p_f satisfies ||b - p_v||_1 = t*(v)*||q - p_v||_1 <= t*(v)*(2+4*delta) < (1/2+delta)*tau; (B3) for every admissible exposer h at v, sum_f lambda_f*h(p_f) <= t*(v); (B4) for every top support functional phi at v and every finite convex average, sum_f lambda_f*(H - phi(p_f)) <= t*(v)*(2+4*delta) < (1/2+delta)*tau; hence for lambda the mass at deficit >= tau is < 1/2 + delta.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-optimal-face-conic-reduction; lem-hiddenness-dual-witness; lem-top-deficit-price; lem-top-support-dual-face
status: proved
af: none
provenance: W54 wave (docs/waves/2026-07-09-W54-huddle-charge-decomposition.md): Fable author L2 (Theorem B) + fresh hostile codex verifier V-L2 (VALID-WITH-CORRECTIONS; the overstated "never a majority" consequence weakened to the Markov form < 1/2 + delta as prescribed). Full proof text: docs/waves/2026-07-09-W54-artifacts/l2-attack.md
owner: A
---

**Role (the intersection branch's rigid anatomy — and the averaging dead-end).** In the
alpha-free branch the ENTIRE dual witness is confined: barycenter within (1/2+delta)*tau
of the top, defeated on average by EVERY admissible exposer, and (B4, the identity-level
cap) invisible on average to EVERY top support functional — the witness-averaging route
to Branch II is impossible BY IDENTITY (FINDINGS 2026-07-09 W54; the special alpha-free
case of [[lem-cotop-witness-pinning]]'s pairing). What survives as attack surface is the
SPLIT of the confined witness into its co-top part ([[conj-straddling-web-exclusion]])
and its shallow universally-shadowed part ([[conj-shallow-counterweight-exclusion]]).

**Rigour tier.** L5 (reviewer != author: fresh hostile codex V-L2; corrections applied).
NOT af-validated.
