---
id: lem-parametric-halo-collapse
kind: lemma
contract: Parametric halo collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4, nonempty visible set W(P), hidden top vertex v of height H, and any halo width a > 0, writing sigma_a for the positive coefficient mass v places on rows at ell-1 distance > a*tau from conv W (tau = sqrt(delta)), sigma for the invisible mass, and nu_v for the row negative mass, one has H*(1 - sigma_a) <= (sigma - sigma_a)*a*tau + nu_v*(2 + 4*delta).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-invisible-mass; def-height
deps: lem-mass-split; lem-residual-lower; lem-residual-upper
status: proved
af: seeded
provenance: W23 wave (docs/waves/2026-07-06-W23-a-gap.md): fresh-codex derivation (worker H) + SEPARATE fresh-codex adversarial verifier (worker L, VALID — expanded the residual-split proof independently, checked the a = 1/4 calibration against the af-validated conj-halo-collapse contract, exact tests on the banked rank-5 and a constructed 4x4); generalizes conj-halo-collapse (af: validated) from a = 1/4 to arbitrary width
owner: A
workspace: proofs/lem-parametric-halo-collapse
---

**Role (the a-gap closer, sketch M1 step 2').** Generalizes the af-validated [[conj-halo-collapse]]
(the a = 1/4 case, recovered verbatim) to arbitrary halo width. This closes the g-bootstrap's
halo-width mismatch: the MIN-A contradiction surface can be posed at the SAME width a ≥ 4 where
[[lem-visible-g-small]] lives.

**Proof (worker H, T1; expanded and verified by worker L; ANSWER files verbatim in the session
scratchpad, quoted in the wave doc).** For σ_a < 1 split the row reproduction of the hidden top v as
`p_v = Σ_{j∈G_a} a_j⁺ p_j + (1 − σ_a)·q`. Since v is a top, d_j ≤ H for every row;
[[lem-residual-lower]] gives H ≤ dist₁(q, C_W); applying [[lem-residual-upper]] to q — near positive
rows priced by their actual distance ≤ a·τ (the halo comparison is strict), d_j = 0 rows free,
negative rows priced by the row diameter 2+4δ (`def-signed-idempotent`), bookkeeping via
[[lem-mass-split]] — yields `H·(1 − σ_a) ≤ (σ − σ_a)·a·τ + ν_v·(2+4δ)`. If σ_a ≥ 1 the left side is
≤ 0 and the right side is nonnegative — no division anywhere.

**Consequences (body notes, NOT part of the contract).**
- *Forced-mass curve:* with σ − σ_a ≤ 1 + ν_v (mass-split), ν_v ≤ δ ≤ 1/4, τ ≤ 1/2:
  `H·(1 − σ_a) ≤ (5a/4 + 3/2)·τ`; hence if σ_a ≤ 1/2 then `H ≤ T(a)·τ` with **T(a) = 5a/2 + 3**.
  T(1/4) = 29/8 (exactly the W18 constant); T(4) = 13.
- *MIN-A at width a:* if `H > T(a)·τ`, every hidden top has σ_a > 1/2, hence (sandwich
  g ≥ σ_a − ν_v) `g^{(a)}_v > 1/2 − δ`. At a = 4 this pairs with [[lem-visible-g-small]]
  (visible rows ≤ 4τ): a genuine numerical gap iff `4τ < 1/2 − δ`, i.e. δ < (17 − 12√2)/2 ≈ 0.0147.
- Scope: hidden TOP vertices only (all height-attaining hidden vertices) — exactly what MIN-A
  consumes; says nothing about non-top hidden vertices.

**Rigour tier.** In-repo paper proof with independent fresh-codex review (L5 satisfied; Review: line
in the banking commit). NOT af-validated, NOT L0-rigorous; strong af-elevation candidate (deps all
af-validated).
