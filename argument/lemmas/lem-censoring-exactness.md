---
id: lem-censoring-exactness
kind: lemma
contract: Censoring exactness: for an exact signed idempotent P in block form [[A, B], [C, D]] (deleted | kept) with a = ||A||_{inf->inf} < 1, the censored matrix S = D + C*(I - A)^{-1}*B satisfies S^2 = S and S*1 = 1 exactly; and with delta = delta(P) and delta_A the negative mass of A, delta(S) <= delta*(1 + 2*(1 + delta) + (2 + 3*delta)*a/(1 - a)) + (1 + delta)^2*delta_A/(1 - a)^2, where the resolvent-squared term is necessary for signed A.
defs: def-signed-idempotent; def-negative-mass
deps: lem-negpart-subadditive
status: proved
af: none
provenance: W48 wave (docs/waves/2026-07-07-W48-mechanism-bricks.md; ideation candidate 2, re-derived independently): fresh-codex prover (worker BC — the four block identities BC = A(I-A), BD = (I-A)B, DC = C(I-A), D^2 = D - CB give the cancellation; the one-resolvent constant of the ideation sketch is FALSE for signed A, corrected LOUDLY) + SEPARATE fresh-codex joint hostile verifier (VBW, VALID — cancellation and both delta(S) terms confirmed; exact signed-A fixture with (I-A)^{-1} negative mass 1 vs delta_A/(1-a) = 1/9 shows one-resolvent control fails; a < 1 essential)
owner: A
---

**Role (the exact dynamic operation).** Meyer stochastic complementation survives signedness
with EXACT idempotence — states can be deleted exactly, at a priced delta cost. The
middleman-elimination supply line for (F2) (censor the transient middle; the actors resolve
onto cluster/visible/deep-far) and the algebraic form of the leak/closure dichotomy. Import
vocabulary: Meyer, SIAM Review 31(2):240-272 (1989) — `stated`, not byte-matched (L1).
