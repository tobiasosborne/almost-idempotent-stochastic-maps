# Wave W29 — the coupling attack on conj-min-a-w4: depth-Markov banked, the pincer certified (2026-07-06/07, session 11)

**Node:** sketch v7 ledger item 5 (conj-min-a-w4 = the witness-to-sigma_4 coupling), bd `aism-hhf`
(P0, under the aism-n7i umbrella). **Design:** mutually-blind pair — worker W (prove: consume the
reviewed W26 bricks) ∥ worker X (refute: witness-constrained tall-web hunt) — + SEPARATE fresh
hostile verifier VW on W's claims. Prompts + raw answers in the session-11 scratchpad (`W29/`);
X's self-contained exact verifier recovered into the run bundle.

## Verdicts (verbatim first lines)

- Worker W: `PARTIAL (proved: depth-Markov top-slab refinement of the hiddenness witness; gap: no
  inequality couples the dual witness weights to the row coefficients defining `sigma_4`)`
- Verifier VW: `VALID-WITH-CORRECTIONS (both claims valid; the c-parametric DM/AL bounds use
  weaker hypotheses than listed; tallness and the δ cutoff are only needed for the `G_4` constant
  corollary)`
- Worker X: `NOT-REFUTED (frontier: H/tau <= sqrt(5/99) in delta-window true-hidden
  constructions; binding constraint: true hiddenness keeps G_4 empty, while tall/high-sigma
  attempts are absorbed into W)`

## Results

1. **`lem-hiddenness-depth-markov` (codified, proved/af:none, VW's WEAKENED hypotheses).** For
   any hidden top and ANY dual witness with Σβ < κ, for every c > 0:
   λ{f ∈ F_v : d_f > H − cτ} > 1 − (1/2+δ)/c. Corollary (tall + δ ≤ δ₁, exact, strict at the
   endpoint via 1/2 + δ₁ = 3(3−2√2)): λ(F_v ∩ G_4) > 2√2/3 ≈ 0.943 — over 94% of every
   witness's mass is simultaneously ρ-far and deep. No optimality/CS used (VW quantifier check).
2. **`lem-hiddenness-alpha-slab-leakage` (codified, proved/af:none).** The witness's positive
   slack has absolute mass < (1/2+δ)/c on the deep slab {d_i ≤ H − cτ}; NOTHING bounds α on the
   top slab (honest limit kept loud).
3. **The pincer, certified (worker X, exact + T3).** Best certified TRUE-hidden frontier:
   δ = 99/8000, H²/δ = 5/99 (H/τ ≈ 0.225 ≪ 13), G_4 = ∅, σ_4 ≡ 0, with exact hiddenness
   witnesses at both hidden tops (t* = 1/81). Diagnosis: true hiddenness folds back BEFORE
   depth 4τ (max d_j = H < 4τ in every certified construction); tall attempts die by
   exposedness absorption (the would-be top turns canonically visible). Bounded search — NO
   emptiness claim; but the refuter interface is now fully exact-certified end to end.
4. **The named bridge (unchanged, sharper):** a coefficient-coupling lemma relating witness
   mass to P_vj⁺. NEW unexplored tool noted for W32: worker W confirmed the witness lemmas use
   NO complementary slackness — the OPTIMAL exposer h* (value t* on λ-support, 1 on β-support,
   0 on α-support) paired with row reproduction at v (0 = Σ_j P_vj h*(p_j), sign-split ⇒
   positive mass on {h* ≥ s} ≤ ν_v/s) is an untouched coupling channel.

## Banking (orchestrator)

Registry: the two shards above (VW as reviewer). Bundle `runs/2026-07-06-w29-witness-coupling/`
(X's verifier script, orchestrator rerun PASS). FINDINGS + sketch-v7 unscoped list updated.
Honest tiers: reviewed paper proofs (L5); NOT af-validated, NOT L0-rigorous; conj-min-a-w4
remains OPEN.
