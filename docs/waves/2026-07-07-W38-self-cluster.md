# Wave W38 — the self-cluster mode: the residual route dies exactly; the frontier conjecture registered (2026-07-07, session 11)

**Node:** the last surviving counterexample mode (W37's diagnosis), bd `aism-2fi` (P0).
**Design:** single fresh-codex prover (worker AG) + SEPARATE fresh hostile verifier VAG.
Prompts + raw answers in the session-11 scratchpad (`W38/`). Paper wave.

## Verdicts (verbatim first lines)

- Worker AG: `GAP (missing: cluster-to-exposedness / row-to-circuit bridge; current residual
  identities do not imply any universal `theta_0` cap on `S_near`)`
- Verifier VAG: `VALID-WITH-CORRECTIONS (RC and SD are valid; AN is valid. Corrections: `B`
  must be priced at `H` before it cancels; SD has sharper numerator `nu_out`; the W29 `a=4`
  fixture is outside RC's `H>aτ` hypothesis.)`

## Results

1. **`lem-rho-near-residual-cancellation` (codified, proved/af:none, VAG-corrected).** For ANY
   row subset C at a hidden top (the near condition is UNUSED — VAG's finding), the residual
   split cancels the deep-outside term exactly and bounds only shallow-outside mass:
   A(H − aτ) ≤ ν(H + D). Pure-cluster consequence: 1 − S ≤ ν(D + aτ)/(H − aτ) = O(τ) — heavy
   clusters are CONSISTENT with all residual identities; the route dies exactly.
2. **`lem-self-defect-shadow` (codified, proved/af:none, VAG-SHARPENED to ν_out).** Heavy
   self-loops shadow the vertex at distance D·ν_out/(1 − P_vv) — the amplified budget permits
   hiding at O(τ) distance; no standalone cap.
3. **The def-exposed normalization catch:** admissible exposers are VALUE-normalized (no
   Lipschitz bound) — ρ-near rows need a conditioning lemma before any exposer transfer
   (lever (a) of sketch v9).
4. **`conj-near-cluster-absorption` REGISTERED** — the five-route convergence point, with the
   certified evidence and the five priced levers in its shard body. Together with the far-mass
   machinery it implies conj-low-slab-cap and the full chain.

## Banking (orchestrator)

Registry: the two lemmas + the conjecture (VAG as reviewer for the lemmas). Sketch v9 already
carries the convergence (committed 9b7215f); FINDINGS updated at the W37 bank. Honest tiers:
reviewed (L5); NOT L0; the conjecture promotes nothing.
