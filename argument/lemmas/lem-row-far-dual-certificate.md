---
id: lem-row-far-dual-certificate
kind: lemma
contract: Row-far dual certificate: for an exact signed idempotent P and a geometrically distinct row vertex v with delta(P) > 0 (tau = sqrt(delta), rho = 4*tau), writing L_F(v) = sum over {f : ||p_f - p_v||_1 >= rho} of max(P_vf, 0) and nu_v the row negative mass, if L_F(v) > 0 then t*(v) <= nu_v / L_F(v), where t*(v) is the exposedness margin of def-exposed.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: 
status: proved
af: none
provenance: W37 wave (docs/waves/2026-07-07-W37-bridge.md): fresh-codex prover (worker AF) + SEPARATE fresh-codex hostile verifier (VAF, VALID — re-derived the dual feasible set and the weak-duality direction from scratch: any feasible normalized circuit upper-bounds t* via pairing with an arbitrary admissible h, no attainment needed; exact fixture: SHARP on the W29 frontier, nu_3/L_F = 1/81 = t*(3) exactly; visible-row check with explicit gap)
owner: A
workspace: proofs/lem-row-far-dual-certificate
---

**Role (the row's own reproduction is a dual certificate).** Normalizing v's row reproduction
by its ρ-far positive mass gives a feasible point of the exposedness LP's dual (λ = P⁺/L_F on
F_v, α = P⁺/L_F off F_v, β = P⁻/L_F), so t*(v) ≤ ν_v/L_F(v) — the first exact inequality
relating a row's OWN coefficient mass to its exposedness margin. Visible corollary (body):
a visible vertex (t* ≥ κ, δ > 0) has L_F ≤ ν_v/κ ≤ 4τ — visible vertices ship at most 4τ
positive mass to their ρ-far set.

**Honest limit (THE dual-direction gap — FINDINGS 2026-07-07 W37, VAF-confirmed).** This is
an UPPER bound on t*: for hidden v it points the wrong way (large far mass makes hiddenness
easier); and ρ-NEAR mass contributes zero to L_F. Do not cite this as a low-slab cap; the
surviving counterexample mode is exactly the ρ-near deep cluster (W38).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate
(deps: none, four lines).
