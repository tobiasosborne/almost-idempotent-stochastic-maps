# Wave W36 — the absorption transition dissected: the rho-halo exemption (2026-07-07, session 11)

**Node:** cluster-to-exposedness (conj-low-slab-cap's true content, W35), bd `aism-2fi` (P0).
**Design:** measurement-informed prove wave — worker AE analyzes the EXACT 1-parameter family
from the W35 bundle — + SEPARATE fresh hostile verifier VAE (independent recomputation incl.
re-solving the exposedness LP from scratch). Prompts + raw answers in the session-11
scratchpad (`W36/`). Paper wave: BOTH workers computed the family exactly and independently;
the endpoint matrices are rerunnable from `runs/2026-07-07-w35-absorption-threshold/`.

## Verdicts (verbatim first lines)

- Worker AE: `MECHANISM-PARTIAL (crossing quantity: clone-invariant rho-excess
  `Δρ(5,4)=||p5-p4||_1^2-16δ(P)`; general lemma: gap = no universal bridge yet from
  row-coefficient mass to positive affine-circuit halo mass.)`
- Verifier VAE: `VALID-WITH-CORRECTIONS (full rho-far sets are `{0,1,2,3,4}` before absorption
  and `{0,1,2,3}` after; `{1,2,4}` / `{1,2}` are only the far positive circuit supports. The
  family analysis and anatomy otherwise check out.)`

## Results (all exact, twice-independently computed)

1. **The family is a nilpotent idempotent perturbation:** P(s) = A + sB with A² = A,
   AB + BA = B, B² = 0 (so P(s)² = P(s) for ALL s); δ(s) = (3983/96000)s, argmax row fixed.
2. **The transition is a FAR-SET JUMP, not a t*-crossing:** t*₅ = 17/417 while row 4 is ρ-far,
   jumping to 51/569 (> κ) when row 4 enters the ρ-ball at the exact threshold
   s_abs = (1298070320000 − 32000000√1643434590)/579288089 ≈ 1.4031368 (smaller root; the
   `>= rho` convention keeps row 4 far AT equality). The branch-vs-κ equality points lie
   OUTSIDE the interval.
3. **The exposer anatomy (the mechanism, named): THE RHO-HALO EXEMPTION.** With the affine
   circuit p₅ = −3/80 p₀ + 23/400 p₁ + 5/12 p₂ − 1/200 p₃ + 341/600 p₄ as the ONLY
   affine-realizability constraint (rank 5, nullity 1 — VAE), the margin is a ratio:
   t* = (negative-anchor circuit mass)/(FAR positive circuit mass). Row 4's heavy positive
   coefficient (341/600) stops consuming margin the moment p₄ is ρ-near — absorption spends
   the halo exemption, NOT coefficient capacity.
4. **The missing bridge, sharpest form (4th independent confirmation):** shipped ROW mass
   (P_vj⁺) and affine-CIRCUIT mass (the witness/dependency coefficients) are different
   objects; no shard relates them. The witness of lem-hiddenness-dual-witness IS a circuit
   through p_v — the bridge question is now: does large low-slab row mass force large ρ-halo
   positive CIRCUIT mass (or small far positive circuit mass)? W37 attacks it, incl. the
   untried hybrid: substitute row reproduction INTO the witness balance once, producing a
   second circuit with coefficient products λ_f·P_fk — a genuine row/circuit hybrid.

## Banking (orchestrator)

No new registry shards (the family facts are instance-[T0], banked here + FINDINGS; the
abstracted schema is conditional-near-definitional — not codified, on VAE's caveat). FINDINGS
entry: the rho-halo exemption + the bridge in final form. Honest tiers: exact instance
analysis verified by independent recomputation; promotes nothing; the cap remains OPEN.
