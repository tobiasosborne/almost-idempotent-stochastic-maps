---
id: lem-genuine-disintegration
kind: lemma
contract: Genuine-mass disintegration: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), height H, halo width a > 0 with G_a = {j : dist_1(p_j, conv W) > a*tau} nonempty (tau = sqrt(delta)), fix for every row a vertex representation p_j = sum_v lambda_jv p_v over geometrically distinct row vertices; then every row index i satisfies g_i <= M_i^a + sum_{j in G_a} P_ij^+ * (H - d_j)/(H - a*tau), where g = P*1_{G_a}, d_j = dist_1(p_j, conv W), P_ij^+ = max(P_ij, 0), and M_i^a = sum_{j in G_a} P_ij^+ * sum_{v : d_v > a*tau} lambda_jv is positive mass supported entirely on HIDDEN row vertices at depth in (a*tau, H].
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: lem-residual-upper
status: proved
af: validated
provenance: W24 wave (docs/waves/2026-07-06-W24-step3-disintegration.md): fresh-codex prover (worker J, S3.1-S3.4) + SEPARATE fresh-codex adversarial verifier (worker K, VALID — checked classification, extreme-point identification, residual-upper hypotheses, ledger algebra, strictness, denominators; exact tests on the banked rank-3 and rank-5 instances); g-bootstrap step 3 of sketch M1
owner: A
workspace: proofs/lem-genuine-disintegration
---

**Role (g-bootstrap step 3, sketch M1).** Tells step 4 WHAT carries the harmonic web: any row with
`g_i ≥ 1/2` certifies positive disintegrated mass `M_i^a ≥ 1/2 − (slack)` sitting on hidden row
vertices strictly deeper than the halo. Bundle of the wave's S3.1–S3.4:

- **S3.1 (depth band):** j ∈ G_a ⇒ a·τ < d_j ≤ H; G_a ≠ ∅ ⇒ H > a·τ (all later denominators
  positive); d_j ≤ 2+4δ always (row diameter).
- **S3.2 (classification):** visible indices and indices coincident with a visible row point have
  d_j = 0 ∉ G_a; every j ∈ G_a is a hidden row vertex or a non-vertex row. Vertices with d_v > 0
  are never visible.
- **S3.3 (vertex disintegration):** rows = convex combinations of merged-duplicate row vertices
  (extreme points); by [[lem-residual-upper]] (no negative terms, m = 1) d_j ≤ Σ_v λ_jv d_v; hence
  for any θ ∈ [a·τ, d_j): `μ_j(θ) := Σ_{v: d_v > θ} λ_jv ≥ (d_j − θ)/(H − θ)`. A vertex j ∈ G_a
  takes the identity disintegration on its geometric representative (verifier K's presentation
  note folded in: λ is defined on a fixed representative set of distinct vertices).
- **S3.4 (ledger):** with L_i^a = Σ_{j∈G_a} P_ij⁺·Σ_{v: d_v ≤ a·τ} λ_jv one has
  M_i^a + L_i^a = Σ_{j∈G_a} P_ij⁺ and M_i^a ≥ g_i − L_i^a; θ = a·τ in S3.3 bounds
  L_i^a ≤ Σ_{j∈G_a} P_ij⁺·(H − d_j)/(H − a·τ) — the contract inequality.

**What this does NOT give (honest limits, worker J):** no bound on the NUMBER of hidden vertices;
no web/self-sustaining structure for {g ≥ 1/2} (that is step 4's open residual); no uniform
smallness of the slack — rows barely past the halo threshold may lose most of their disintegrated
weight to shallow vertices.

**Rigour tier.** In-repo paper proof with independent fresh-codex review (L5 satisfied; Review: line
in the banking commit). NOT af-validated, NOT L0-rigorous.
