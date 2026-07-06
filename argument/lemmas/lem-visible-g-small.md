---
id: lem-visible-g-small
kind: lemma
contract: Visible rows are g-small: for an exact signed idempotent P with 0 < delta(P) <= 1/4, tau = sqrt(delta), visible set W nonempty, C_W = conv{p_w : w in W}, halo width a >= 4, G_a = {j : dist_1(p_j, C_W) > a*tau}, and g = P*1_{G_a}, every w in W satisfies -nu_w <= g_w <= 4*tau, where nu_w is the row-w negative mass.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: none
provenance: W21 wave (docs/waves/2026-07-06-W21-lemma-a-decider.md): fresh-codex prover (worker C), SEPARATE fresh-codex adversarial verifier (worker E, verdict VALID on all 7 checklist items), mutually-blind refuter converged NOT-REFUTED (bundle runs/2026-07-06-w21-lemma-a-decider/); g-bootstrap step 2 of sketch v3 M1
owner: A
workspace: proofs/lem-visible-g-small
---

**Role (g-bootstrap step 2, sketch v3 §Route A M1).** The load-bearing lemma of the g-bootstrap:
the harmonic observable `g = P·1_{G_a}` (exactly P-harmonic by idempotence, `Pg = P²1_G = P1_G = g`)
is O(τ)-small on the visible set. Consumed by the (still OPEN) step-4 once-applied maximum-principle
argument against band-supported webs.

**Proof (worker C, T1; independently verified by worker E; ANSWER files verbatim in the session
scratchpad, quoted in the wave doc).** Fix `w ∈ W`; write `a_j = P_wj`, `a_j± = max(±a_j, 0)`,
`ν_w = Σ_j a_j⁻ ≤ δ`.

1. *Degenerate branch.* If no row is ρ-far from `p_w` (t*(w) = +∞ convention), then by step 2 below
   `G_a = ∅`, hence `g_w = 0` and the claim is immediate.
2. *Halo-to-far-set inclusion (the only use of a ≥ 4).* `w ∈ W` gives `p_w ∈ C_W`, so
   `dist₁(p_j, C_W) ≤ ‖p_j − p_w‖₁` for every j. If `j ∈ G_a` then
   `‖p_j − p_w‖₁ ≥ dist₁(p_j, C_W) > a·τ ≥ 4τ = ρ` (strict halo comparison), hence
   `G_a ⊆ {j : ‖p_j − p_w‖₁ ≥ ρ}`.
3. *Exposer extraction.* Visibility gives `t*(w) ≥ κ = τ/4`; since t* is a supremum, for every
   `ε ∈ (0, κ)` there is an admissible exposer `h_ε` (affine, `h_ε(p_w) = 0`, `0 ≤ h_ε ≤ 1` on all
   rows) with `h_ε(p_j) ≥ κ − ε` on every ρ-far row.
4. *Pairing.* Row reproduction `p_w = Σ_j P_wj p_j` (row w of P² = P) plus row sum 1 make the affine
   `h_ε` distribute: `0 = h_ε(p_w) = Σ_j a_j h_ε(p_j)`. Sign-split and `0 ≤ h_ε ≤ 1` give
   `Σ_j a_j⁺ h_ε(p_j) = Σ_j a_j⁻ h_ε(p_j) ≤ ν_w ≤ δ`; positive near-mass contributes nonnegatively
   and is kept on the left.
5. *Conclusion.* By the inclusion, `(κ − ε)·Σ_{j∈G_a} a_j⁺ ≤ Σ_j a_j⁺ h_ε(p_j) ≤ δ`; letting ε → 0,
   `Σ_{j∈G_a} a_j⁺ ≤ δ/κ = 4τ`. Since `g_w = Σ_{j∈G_a} a_j ≤ Σ_{j∈G_a} a_j⁺` and
   `g_w ≥ −Σ_{j∈G_a} a_j⁻ ≥ −ν_w`: **−ν_w ≤ g_w ≤ 4τ**.

Duplicate/coincident rows are harmless (h is a function of the row point; the identity sums over
indices). W ≠ ∅ is needed only for w and C_W to exist.

**What this does NOT give.** No upper control on rows outside W (band rows, hidden rows, hidden
tops); lower control only `−ν_w`. The constant is 4 = δ/(κτ); the mechanism genuinely needs `a ≥ 4`
(for `a < 4` the inclusion in step 2 fails; the refuter's small-halo frontier certificate realizes
`g_w = √(147/569)·τ ≈ 0.51τ` at `a = 1/4` — no contradiction, just the open `(29τ/8, 4τ]` gap-band
question of the constants fight, see the wave doc).

**Rigour tier.** In-repo paper proof with independent fresh-codex review (L5 satisfied; verdict in
the banking commit's `Review:` line). NOT af-validated and NOT L0-rigorous; af elevation is the
filed follow-up (single-minimal contract, af-ready).
