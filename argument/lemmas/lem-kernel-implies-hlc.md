---
id: lem-kernel-implies-hlc
kind: lemma
contract: Kernel implies HLC: if there are universal delta_0>0 and B<inf (n-free) such that every exact signed idempotent P with delta(P) <= delta_0 has W(P) nonempty and every hidden row vertex v with invisible mass sigma~_v > tau = sqrt(delta) has dist_1(p_v, conv{p_w : w in W}) <= B*tau, then every exact signed idempotent P with delta(P) <= min{delta_0, 1/4} satisfies H(P) <= max{B,3}*sqrt(delta(P)).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-invisible-mass; def-height
deps: conj-kernel; lem-mass-split
status: proved
af: none
provenance: W22 wave (docs/waves/2026-07-06-W22-kernel-implies-hlc.md): fresh-codex prover (worker F, independent of the ingest text) + SEPARATE fresh-codex adversarial verifier (worker G, VALID on all 7 checklist items incl. a 17-fixture exact test); re-derivation of the trunk step <2>5 recorded at docs/ingest/report/kernel-conjecture.tex:176-221 (ingest treated as object of study, not imported)
owner: A
workspace: proofs/lem-kernel-implies-hlc
---

**Role (trunk step <2>5).** The conditional assembly that makes [[conj-kernel]] theorem-facing:
Kernel ⇒ the hull-linear cap [[op-hlc]]. With the mod-audit steps <2>6 (HLC ⇒ op-exposed-hull) and
<2>7 (clusters + rounding) it completes the chain to `op-classical`.

**Proof (worker F, T1; independently verified by worker G; ANSWER files verbatim in the session
scratchpad, quoted in the wave doc).** Sketch of the banked derivation:

1. *Height at a row vertex.* Every row lies in conv{row vertices} (extreme points of the row polytope
   are exactly the merged-duplicate row vertices of `def-exposed`); dist₁(·, C_W) is convex; hence
   H = max over row vertices.
2. *δ = 0 branch.* ρ = κ = 0; h ≡ 0 is an admissible exposer with t* = 0 ≥ κ, so every row vertex is
   visible and H = 0.
3. *H > 0 ⇒ the attaining vertex v is hidden* (visible ⇒ p_w ∈ C_W ⇒ dist 0).
4. *Small branch (σ̃_v ≤ τ), re-derived s8 cap.* Pick nearest points c_j ∈ C_W for each row,
   c₊ = (1/(1+ν_v))·Σ a_j⁺ c_j ∈ C_W (via [[lem-mass-split]]); the split identity
   p_v − c₊ = Σ a_j⁺(p_j − c_j) − Σ a_j⁻(p_j − c₊) with the row-diameter clause
   ‖p_i − p_j‖₁ ≤ 2+4δ of `def-signed-idempotent` gives H ≤ σ̃_v·H + ν_v·(2+4δ), i.e.
   H(1−σ̃_v) ≤ ν_v(2+4δ); with σ̃_v ≤ τ ≤ 1/2: H ≤ 2ν_v(2+4δ) ≤ 6δ ≤ 3τ (δ ≤ 1/4).
5. *Large branch (σ̃_v > τ).* The Kernel hypothesis applies to v verbatim: H ≤ B·τ.
6. *Assembly.* H ≤ max{B,3}·τ; δ ≤ δ₀ used only to invoke Kernel (incl. W ≠ ∅); δ ≤ 1/4 only in the
   small branch. Squaring gives the HLC form δ ≥ H²/max{B,3}².

**Rigour tier.** In-repo paper proof with independent fresh-codex review (L5 satisfied; Review: line
in the banking commit). NOT af-validated, NOT L0-rigorous. Its dep [[conj-kernel]] is a CONJECTURE —
this lemma is a conditional implication and can never make [[op-hlc]] unconditional by itself.
