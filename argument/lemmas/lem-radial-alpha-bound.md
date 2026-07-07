---
id: lem-radial-alpha-bound
kind: lemma
contract: Conditional radial alpha bound: for an exact signed idempotent P with delta(P) > 0 and a hidden row vertex v, if v admits an optimal hiddenness datum (h*, lambda, beta) with tangential residual R = 0, then the minimal witness alpha satisfies A_min(v) = 0; and if it admits one with R != 0 and radial reach r = sup{r' >= 0 : r'*(R/||R||_1) in conv{p_i - p_v : h*(p_i) = 0}} >= mu > 0, then A_min(v) <= (1 + tau/4)*(2 + 4*delta)/mu (tau = sqrt(delta)).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-zero-face-alpha-gauge
status: proved
af: none
provenance: W41 wave (docs/waves/2026-07-07-W41-tall-blowup-decider.md): fresh-codex prover (worker AN) + SEPARATE fresh-codex hostile verifier (VAN, VALID-WITH-CORRECTIONS — the gauge is priced by radial reach in the CONVEX HULL of zero-face displacements, not the cone (the free conic mass creates the hull normalization); R = 0 case explicit; ||R||_1 <= (1 + t*)(2 + 4*delta) re-derived)
owner: A
workspace: proofs/lem-radial-alpha-bound
---

**Role (tall-mode alpha control, priced by ONE geometric quantity).** Composes with
[[lem-zero-face-alpha-gauge]]: the witness free ray is bounded exactly by the zero face's
radial thickness in the residual direction. One-way only (VAN's correction): thickness ⇒ the
alpha bound; an absolute A_min bound does not force thickness without a lower bound on ||R||.
The blow-up ([[obs-realized-alpha-blowup]]) is exactly r → 0. VAN confirmed the three
no-control facts honestly: slab leakage, depth-Markov, and the pincer all miss r_Z — the
missing assertion is [[conj-tall-zero-face-radial-thickness]].

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
