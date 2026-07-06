# Wave W31 — the anchorless-witness attack on W-nonemptiness: rank-3 tangent structure banked (2026-07-07, session 11)

**Node:** sketch v7 ledger item 6 (W-nonemptiness, rank ≥ 3 production theorem), bd `aism-jwg`
continuation. **Design:** single fresh-codex prover (worker Y, the W30-convergent anchorless
mechanism) + SEPARATE fresh hostile verifier VY. Prompts + raw answers in the session-11
scratchpad (`W31/`). Paper wave (VY's exact fixture checks scratch-only, W22 pattern).

## Verdicts (verbatim first lines)

- Worker Y: `PARTIAL (proved: rank-3 maximum-volume slab reduction for hidden max-chart
  vertices; gap: anchorless-witness gives only an O(sqrt(delta)) slab error, while the
  max-volume area contradiction needs O(delta))`
- Verifier VY: `VALID (hypotheses as listed)`

## Results

1. **`lem-rank3-maxchart-hidden-tangent` (codified, proved/af:none).** All-hidden rank-3
   configurations force, at every max-area chart vertex, a ρ-far tangent companion in the
   2κ-slab with a negative transverse dip > 5τ/12. VY re-derived the load-bearing maximality
   step (|a_s| ≤ 1 at all ROWS via affinity + vertex extremality) and the exact constant
   τ(3−2δ)/(4(1+2δ)); two exact fixtures.
2. **The obstruction, priced exactly (worker Y):** the max-volume contradiction from two
   tangent companions gains area Θ(τ²) but hiddenness only bounds slab defects at Θ(τ) —
   the route needs slab defects O(τ²) or a coefficient-coupling input. NOT codified as a
   registry shard (meta-observation about a proof route); recorded in FINDINGS.
3. **Strategic convergence (the wave's real payload):** this is the SAME missing shape as the
   conj-min-a-w4 coupling gap (W29/W32): couple witness/slab geometry to row coefficients, or
   upgrade linear-scale defects to quadratic. ONE mechanism now sits under BOTH open ledger
   items.

## Banking (orchestrator)

Registry: the shard above (VY as reviewer). No run bundle (paper wave). FINDINGS + sketch in
lockstep at the next redraw. Honest tiers: reviewed paper proof (L5); NOT af-validated, NOT
L0-rigorous; W-nonemptiness at rank ≥ 3 remains OPEN.
