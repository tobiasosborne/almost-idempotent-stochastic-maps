# Wave W33 — the harmonic-affine bridge: the g-machinery IS the exposer machinery (2026-07-07, session 11)

**Node:** sketch v7/aism-2fi attack surface (i) — fuse the two-observable machinery with the
exposer family. **Design:** single fresh-codex prover (worker AA) + SEPARATE fresh hostile
verifier VAA. Prompts + raw answers in the session-11 scratchpad (`W33/`). Paper wave.

## Verdicts (verbatim first lines)

- Worker AA: `PROVED (bridge; cap partial)`
- Verifier VAA: `VALID-WITH-CORRECTIONS (all three survive; keep Claim N’s `g_v > min_i g_i`
  hypothesis explicit, and Claim T’s `lambda` must come from a full hiddenness-dual witness
  tuple)`

## Results

1. **`lem-harmonic-affine-bridge` (codified, proved/af:none).** {g : Pg = g} = the
   affine-in-position functionals, forward direction ONE LINE (g_i = Σ_j P_ij g_j = p_i·g,
   u = g works; constants absorbable since row sums are 1). Clone-robust automatically. Exact
   fixture: entrywise verification on the banked W19 rank-5.
2. **`lem-conditional-g-near-exposer` (codified, proved/af:none).** At a g-maximizing HIDDEN
   vertex the normalized g-deficit is an admissible exposer; hiddenness forces ρ-far high-g
   company within (τ/4)(1+2δ) of the max. The max hypothesis is ESSENTIAL (VAA fixture: the
   W19 g-max is a visible row; the construction breaks at the hidden non-max top). In the tall
   width-4 window the g-max vertex IS hidden (Lemma A cap 4τ vs forced g > 1/2 − δ) — the
   hypothesis is then automatic.
3. **`lem-two-observable-pencil-bound` (codified, proved/af:none).** Every admissible affine F
   obeys BOTH coupling channels at once (witness side < κE; coefficient side ≤ ν_v E; the
   latter checked with exact EQUALITY on the W29 frontier). Honest limit: the two bounds
   point the same way — the pencil alone yields no infeasibility; the low slab stays open.
4. **The W34 channel (opened by the bridge + AA's clone-robust variant):** at the g-max hidden
   vertex r, harmonicity gives the SELF-consistency ledger Σ_j P_rj (g_r − g_j) = 0, whose
   sign-split + Markov concentrates r's positive mass on near-max-g rows up to O(δ) — and
   claim N's exposer is built from the SAME g that defines the web. Hiddenness now constrains
   the exact functional carrying the anti-splitting obstruction.

## Banking (orchestrator)

Registry: the three shards above (VAA as reviewer). FINDINGS pointer in the session's unified-
mechanism entry; sketch v8 at the next redraw. Honest tiers: reviewed paper proofs (L5); NOT
af-validated, NOT L0-rigorous; conj-low-slab-cap remains OPEN.
