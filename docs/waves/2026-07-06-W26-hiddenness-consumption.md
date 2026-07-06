# Wave W26 — conj-min-a-w4 via HIDDENNESS consumption: the dual witness lands (2026-07-06, session 11)

**Node:** sketch v6 M1 step 4 (`conj-min-a-w4` + the named HIDDENNESS input), bd `aism-n7i` (P0).
**Design:** verbatim relaunch of the interrupted 2026-07-06 wave (briefs byte-frozen in
`runs/2026-07-06-w26-hiddenness/prompts/`, SHA256 match verified at relaunch): mutually-blind pair —
worker P (prove: LP-dual witness of t*(v) < κ + two-observable machinery) ∥ worker Q (adversary:
re-run the W25 insufficiency game with TRUE hiddenness hard-asserted via exact t* LPs) — then a
SEPARATE fresh hostile verifier VP on P's claimed partial. Prompts + raw answers in the session-11
scratchpad (`W26/PROMPT-{P,Q,VP}.md`, `W26/ANSWER-{P,Q,VP}.md`); answer copies banked in the run
bundle (`answers/`). Worker runtimes were short (~6–25 min); rigour rests on the hostile-verifier
pass + exact fixtures, not on effort proxies.

## Verdicts (verbatim first lines)

- Worker P: `PARTIAL (proved: hiddenness LP-dual witness and top-slab far-row consequence; gap: no
  inequality couples that witness to row-v positive mass `sigma_4`)`
- Worker Q: `FORCED-STRUCTURE (statement: `t*(v)<kappa` forces a convex combination of `rho`-far
  rows within `kappa*(2+4*delta)` of `p_v`; W25’s self-loop model lacks this and becomes visible)`
- Verifier VP: `VALID-WITH-CORRECTIONS (both claims survive; Claim 1’s strict `psi` inequality
  needs `E>0`, otherwise only `<=`)`

## Results

1. **`lem-hiddenness-dual-witness` (codified, proved/af:none).** For a hidden row vertex v the
   exposedness LP's dual yields a witness: λ ∈ Δ(F_v), α, β ≥ 0 with B = Σβ = t*(v) < κ and
   Σ_f λ_f(p_f − p_v) + Σ_i α_i(p_i − p_v) = Σ_i β_i(p_i − p_v). Pairing consequence (body): for
   affine ψ with ψ(p_v) = 0, 0 ≤ ψ ≤ E on rows, E > 0: some ρ-far row has ψ(p_f) < κE.
   VP re-derived the dual from scratch (feasibility, boundedness via the t* = +∞ empty-far-set
   convention — hidden ⇒ F_v ≠ ∅ — attainment, strong duality, strictness) and verified on the
   exact W19 7×7 duplicate-split fixture (t*(v) = 1/21 < 1/16, witness recomputed exactly).
2. **`lem-top-slab-companion` (codified, proved/af:none).** Tall width-4 configs: every hidden top
   has a ρ-far row f with d_f > H − (1/2+δ)τ; under H > 13τ, δ ≤ (17−12√2)/2 exactly
   13 − (1/2+δ) ≥ 4 + 6√2 > 4, so f ∈ G_4. The hidden top has deep, far COMPANY — the first
   banked fact that consumes hiddenness (the W25-mandated input).
3. **The W25 certificate dies under canonical geometry (worker Q, T1).** Recomputing the W25 3×3
   with exact canonical W: its labeled-hidden top has t* = 100/101 (VISIBLE), W = {v,s}, H = 0 —
   the insufficiency certificate cannot survive the hiddenness constraint, exactly as W25
   predicted. No second F0–F10 certificate found under the witness constraint (bounded Λ-C search,
   n ≤ 10, 1000 samples, 0 tall webs — [T3], no emptiness claim).
4. **Discrepancy kept honest:** Q's stronger α-free "gauge" form (far barycenter within κ(2+4δ) of
   p_v) matches its exact fixtures (rank-5: ‖q_far − p_v‖₁ = αD with α = t* = 1/41) but was NOT
   the form VP validated (VP's dual retains the α family). Q's general gauge claim stays
   worker-T1; any use must first reconcile the two dual forms.

## The remaining gap (the frontier, sharpened)

The witness is geometric; nothing yet couples it to the row's own coefficients P_vj⁺ (σ₄). Q's
interface for the next round: consume the witness at ALL deep carrier vertices (disintegration
hands mass to hidden vertices; every one of them is surrounded by its own far barycenter), not
just the top. That is wave W29's design.

## Banking (orchestrator)

Registry: `lem-hiddenness-dual-witness`, `lem-top-slab-companion` (both proved/af:none, VP as
reviewer). Bundle: `runs/2026-07-06-w26-hiddenness/` rewritten as a real bundle (worker Q's exact
script + report; orchestrator recompute rerun exit 0, tail matches report). FINDINGS + sketch in
lockstep. Honest tiers: reviewed paper proofs (L5); NOT af-validated, NOT L0-rigorous.
