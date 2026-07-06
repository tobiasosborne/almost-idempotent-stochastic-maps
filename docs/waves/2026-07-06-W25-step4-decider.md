# Wave W25 — step-4 decider: prove vs insufficiency, blind-convergent; step 4 reduced to conj-min-a-w4 + a named missing input (2026-07-06)

**Node:** sketch v5 M1 step 4 — THE remaining open step of the g-bootstrap; bd `aism-7pe` (P0).
**Design:** mutually-blind adversarial pair with asymmetric mandates — worker M (PROVE the
once-applied maximum principle on the width-4 surface; imports restricted to the three reviewed
lemmas + af-validated shards + first principles; obs-deep-leakage FORBIDDEN) vs worker N (OBSTRUCT:
prove the fact-set insufficient by a certified model, the E2 pattern) — plus a SEPARATE fresh
hostile verifier (worker O) on M's claimed derivation. Prompts + raw answers in the session
scratchpad (`W25/PROMPT-{M,N,O}.md`, `W25/ANSWER-{M,N,O}.md`); N's certificate in
`runs/2026-07-06-w25-step4-decider/` (L3 bundle, orchestrator recompute 17/17 from printed values).

## Verdicts (verbatim first lines)

- Worker M (prover): `PARTIAL (proved: the once-applied height maximum principle gives only a
  near-top hidden-web lower bound; gap: a width-4 anti-splitting cap on that web)`
- Worker N (obstructor): `INSUFFICIENT (certified model: facts F0-F8 all satisfied with web +
  H > 13*tau; violated true-fact: canonical exposedness/visible-set geometry, since the "hidden"
  top is actually exposed)`
- Worker O (verifier of M): `VALID (no error found; checks: support functional, diameter bound,
  harmonic/sign split, three displayed consequences, final lower bound, rank-5 exact test)`

## What the wave established

1. **The verified positive yield (codified `lem-top-concentration`, proved/af:none):** with an
   affine ℓ1/ℓ∞ support functional paired once against row reproduction, the hidden top's positive
   mass concentrates on the deep set — `Σ_{j∉G_a} P_vj⁺ ≤ ν_v(2+4δ)/(H − aτ)` — and the
   disintegration slack obeys the same bound; hence in tall width-4 configs
   `M_v⁴ > 1/2 − δ − τ(2+4δ)/9`. **The once-applied principle yields a LOWER bound on the deep
   hidden web — the recorded wall in its precise form: the local maximum principle pushes mass
   INTO the near-top hidden band, not out of it.**
2. **The insufficiency certificate (worker N; L3 bundle):** a 3×3 exact idempotent
   (`δ = 1/100`, labels W = {w}, hidden top = v, labeled H = 20τ) satisfies EVERY imported scalar
   fact with a sustained web — while the labeled-hidden top is ACTUALLY (ρ,κ)-exposed
   (explicit exposer, margin 100/101 ≥ κ). **No proof of step 4 can close from the current
   fact-list; the mandatory missing input is HIDDENNESS — t*(v) < κ, the failure of every
   admissible exposer, which no banked lemma consumes.**
3. **Blind convergence (the third occurrence of the E2 pattern):** M's minimal missing statement
   (the upper cap `M_v⁴ + R_v ≤ 1/2 − δ`) and N's violated-fact diagnosis (hiddenness) are the
   SAME gap seen from opposite sides — the quantitative content of non-exposedness at the deep
   vertices.
4. **Codified frontier:** `conj-min-a-w4` — in tall width-4 configs, SOME hidden top has
   `σ₄ ≤ 1/2`. With the reviewed parametric collapse this closes `H ≤ 13τ` (δ ≤ δ₁), i.e. the
   height side of Kernel at B = 13. Registry: 55 results, linker green.

## Orchestrator recomputation (banked)

N's certificate recomputed ENTIRELY from printed values (`scripts/orchestrator_recompute.py`,
17/17: algebra, distances, harmonicity, the three labeled fact conclusions, the exposer margin,
the exact squared-form δ-window check); worker checker rerun exit 0. M's arithmetic hand-checked
(sign-split ≤ δD; H − 4τ > 9τ; d_j ≥ φ_j) and independently verified by O, incl. an exact
LP-constructed support functional on the banked rank-5 instance.

## Wave outcome (orchestrator, [T2] strategic)

The decision tree took its expected branch: PARTIAL + INSUFFICIENT with a named missing fact.
Step 4 is no longer an unscoped mechanism hunt — it is ONE conjecture (`conj-min-a-w4`) plus ONE
named input to consume (hiddenness), with the verified concentration lemma as the first brick of
any future proof. Next wave: `aism-n7i` (P0) — turn the exposer-failure witnesses of t*(v) < κ
into the width-4 cap, with the two-observable machinery in scope and `lem-canonical-separator`
re-establishment as a sub-target. Honest tiers: concentration = reviewed; insufficiency = exact
certificate relative to the enumerated fact-list; conj-min-a-w4 = conjecture; nothing af-validated,
nothing L0-rigorous.
