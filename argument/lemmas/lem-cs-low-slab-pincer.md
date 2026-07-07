---
id: lem-cs-low-slab-pincer
kind: lemma
contract: CS low-slab pincer: for an exact signed idempotent P, a row index v with nu_v = sum_j max(-P_vj, 0), an affine h with h(p_v) = 0 and 0 <= h(p_j) <= 1 for every row j, and every s > 0, one has sum over {j : h(p_j) >= s} of max(P_vj, 0) <= nu_v / s.
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved
af: seeded
provenance: W32 wave (docs/waves/2026-07-07-W32-cs-pincer.md): fresh-codex prover (worker Z) + SEPARATE fresh-codex hostile verifier (VZ, VALID with MINIMAL hypotheses — no hiddenness, no vertex, no top, no nonempty W, no delta > 0 anywhere; exact fixture on the W29 frontier instance realizes EQUALITY at s = t* — the bound is sharp); first-principles (row reproduction + row sums + sign split + Markov), no imports
owner: A
workspace: proofs/lem-cs-low-slab-pincer
---

**Role (the first true coefficient-coupling inequality).** Any admissible-at-v affine
functional caps v's OWN positive coefficient mass wherever the functional is high:
0 = h(p_v) = Σ_j P_vj h(p_j) (affinity + row reproduction + row sums), the sign split gives
Σ P_vj⁺ h_j = Σ P_vj⁻ h_j ≤ ν_v, and Markov localizes. Applied to a hidden vertex's optimal
exposer h* at s = κ (ν_v ≤ δ = τ², so ν_v/κ ≤ 4τ): a σ_a cap counterexample must pack
> 1 − θ − 4τ of the top's positive mass into G_a ∩ {h* < κ} — the SAME slab where
[[lem-hiddenness-depth-markov]] pins > 94% of the witness mass. The remaining frontier is
exactly [[conj-low-slab-cap]]: cap the low-slab coefficient mass.

**Pincer corollary (body, VZ-checked).** For any subset A of row indices: if
Σ_{j∈A} P_vj⁺ > 1 − θ then Σ_{j ∈ A, h(p_j) < s} P_vj⁺ > 1 − θ − ν_v/s (subtraction; strict
from the strict antecedent).

**Honest limit (VZ-confirmed, load-bearing).** The channel bounds mass ONLY where h is high;
mass at h = 0 (including all self/top-cluster mass, h(p_v) = 0) is invisible to the identity.
CS alone can NEVER cap the low slab — do not cite this as a σ_a cap (FINDINGS 2026-07-07).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; PRIME af-elevation candidate
(deps: none, four-line proof, single-minimal contract).
