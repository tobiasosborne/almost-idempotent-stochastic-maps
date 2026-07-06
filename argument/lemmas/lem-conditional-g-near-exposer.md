---
id: lem-conditional-g-near-exposer
kind: lemma
contract: Conditional g-near-exposer: for an exact signed idempotent P with delta(P) > 0, halo width a > 0 with G_a = {j : dist_1(p_j, conv{p_w : w in W}) > a*tau} (tau = sqrt(delta), W = W(P) nonempty), and a hidden row vertex v that globally maximizes g = P*1_{G_a} over row indices with g_v > min_i g_i, the function h = (g_v - g)/(g_v - min_i g_i) is an admissible exposer for v, and some row f with ||p_f - p_v||_1 >= 4*tau satisfies g_f > g_v - (tau/4)*(g_v - min_i g_i) >= g_v - (tau/4)*(1 + 2*delta).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass
deps: lem-harmonic-affine-bridge
status: proved
af: none
provenance: W33 wave (docs/waves/2026-07-07-W33-harmonic-affine-bridge.md): fresh-codex prover (worker AA) + SEPARATE fresh-codex hostile verifier (VAA, VALID-WITH-CORRECTIONS — the global-max and g_v > min g hypotheses made explicit AND shown ESSENTIAL by exact fixture: on the banked W19 rank-5 the g-max row is visible row 4 and forcing the construction at hidden row 5 breaks the [0,1] box); g-range -nu_i <= g_i <= 1 + nu_i re-derived
owner: A
workspace: proofs/lem-conditional-g-near-exposer
---

**Role (hiddenness constrains g AT the g-max).** By [[lem-harmonic-affine-bridge]] the
normalized g-deficit is affine, hence an admissible exposer at a g-maximizing hidden vertex;
hiddenness (def-exposed, t* < κ) then forces ρ-far HIGH-g company: some far row within
(τ/4)(1+2δ) of the maximum. In the tall width-4 window (H > 13τ, δ ≤ δ₁) the g-max row vertex
IS hidden (visible rows are capped at 4τ by [[lem-visible-g-small]] while hidden tops carry
g > 1/2 − δ; g is affine so its row-max is attained at a vertex) — the hypothesis is then
automatic. W34 consumes this together with the g-max self-consistency Markov.

**Honest limits (VAA).** The global-max hypothesis is ESSENTIAL (fixture-refuted otherwise);
the companion f is far from v but nothing yet places f in G_a or bounds P_vf.

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous.
