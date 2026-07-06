# Wave W24 — g-bootstrap step 3 (disintegration) derived + hostile verification (2026-07-06)

**Node:** sketch v4 M1 step 3, bd `aism-o1x`. **Design:** fresh codex prover (worker J) + SEPARATE
fresh codex adversarial verifier (worker K, hostile brief with exact-test instructions). Prompts +
raw answers in the session scratchpad (`W24/PROMPT-{J,K}.md`, `W24/ANSWER-{J,K}.md`). No numeric
bundle (paper wave; the verifier's exact checks were scratch-only by design).

## Verdicts (verbatim first lines)

- Worker J (prover): `PROVED (S3.1-S3.4 all T1)`
- Worker K (verifier): `VALID (no error found; checks: specified def shards, lem-residual-upper,
  exact scratch checks on w19 rank-3 and rank-5 matrices at a=1/4)`

## The result (codified as `lem-genuine-disintegration`, status: proved, af: none)

S3.1 (depth band a·τ < d_j ≤ H; G_a ≠ ∅ ⇒ H > a·τ), S3.2 (every j ∈ G_a is a hidden row vertex or a
non-vertex row; coincidence-with-visible excluded), S3.3 (vertex disintegration with the averaging
bound μ_j(θ) ≥ (d_j − θ)/(H − θ)), S3.4 (the ledger): for every row i,

    g_i ≤ M_i^a + Σ_{j∈G_a} P_ij⁺·(H − d_j)/(H − a·τ),

where M_i^a is positive disintegrated mass supported ENTIRELY on hidden row vertices at depth in
(a·τ, H]. So a row with g_i ≥ 1/2 certifies ≥ 1/2 − slack of mass on strictly-deep hidden vertices.
Honest limits stated by the prover and kept in the shard: no count of hidden vertices, no
web-structure claim, no uniform slack bound (rows barely past the halo lose most weight to shallow
vertices) — all of that is exactly step 4's open residual.

Verifier K checked the classification against the def shards, the extreme-point identification, the
residual-upper hypotheses (m = 1, no negative terms), the ledger algebra, strict/non-strict
consistency, positive denominators, and ran exact checks on the banked rank-3 (G = {3,4}) and rank-5
(G = {5}) instances; one presentation caveat (identity disintegration on the geometric
representative) folded into the shard body.

## Wave outcome (orchestrator, [T2] strategic)

Step 3 of the g-bootstrap is done at reviewed tier. Combined with W23, the bootstrap's remaining
mathematical content is EXACTLY step 4 (the analytic anti-splitting residual), now posed with full
precision: for δ < (17−12√2)/2 and H > 13τ, the P-harmonic observable g^{(4)} has every hidden top
> 1/2 − δ and every visible row ≤ 4τ; by this wave's ledger the web's mass disintegrates onto deep
hidden vertices; the once-applied maximum principle must derive a contradiction. Whether
obs-deep-leakage (heuristic) is still a blocking dep of that final step is re-priced in sketch v5.
Honest tiers: reviewed paper proof (L5); NOT af-validated, NOT L0-rigorous.
