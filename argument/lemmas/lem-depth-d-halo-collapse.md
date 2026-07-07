---
id: lem-depth-d-halo-collapse
kind: lemma
contract: Depth-d halo collapse: for an exact signed idempotent P with 0 < delta(P) <= 1/4 and nonempty visible set W(P), any row index v with d = dist_1(p_v, conv{p_w : w in W}), and any halo width a > 0, writing d_j = dist_1(p_j, conv W), sigma_a(v) = sum over {j : d_j > a*tau} of max(P_vj, 0) (tau = sqrt(delta)), sigma(v) = sum over {j : d_j > 0} of max(P_vj, 0), nu_v the row negative mass, and C_a(v) = sum over {j : d_j > a*tau, d_j > d} of max(P_vj, 0)*(d_j - d), one has d*(1 - sigma_a(v)) <= (sigma(v) - sigma_a(v))*a*tau + nu_v*(2 + 4*delta) + C_a(v).
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-invisible-mass; def-height
deps: lem-mass-split; lem-residual-upper
status: proved
af: seeded
provenance: W34 wave (docs/waves/2026-07-07-W34-gmax-self-consistency.md): fresh-codex prover (worker AB, the requested sub-target) + SEPARATE fresh-codex hostile verifier (VAB, VALID-WITH-CORRECTIONS — legitimized the convex split exactly: the residual q = (non-halo positive terms − negative terms)/(1 − sigma_a) has affine mass 1 − sigma_a, so p_v is a GENUINE convex combination of the G_a rows and q; calibration anchor: at a hidden top d = H and C_a = 0 recover the af-validated lem-parametric-halo-collapse contract VERBATIM; exact fixtures incl. a genuine non-top row on the banked W19 rank-3)
owner: A
workspace: proofs/lem-depth-d-halo-collapse
---

**Role (the collapse engine at EVERY depth).** Generalizes the af-validated
[[lem-parametric-halo-collapse]] from hidden tops to arbitrary row indices: the price of the
generalization is the explicit deeper-row correction C_a(v) (mass sent to rows strictly deeper
than v, weighted by the depth excess) — it vanishes exactly at tops. Gives every hidden vertex
a sigma_a dichotomy at its own depth; consumed by the g-max/absorption program (aism-2fi).

**Proof shape (worker AB, T1; VAB).** sigma_a ≥ 1 branch trivial (LHS ≤ 0, RHS ≥ 0). Else
split p_v = Σ_{G_a} P_vj⁺ p_j + (1−σ_a)q with q the signed residual ([[lem-mass-split]] makes
the coefficients total 1); convexity of dist₁(·, C_W) + the deeper-row rearrangement give
(1−σ_a)d ≤ C_a + (1−σ_a)dist(q, C_W); [[lem-residual-upper]] prices q (non-halo positive rows
at aτ, negative rows at the row diameter 2+4δ).

**Honest limits (the W34 diagnosis, kept loud).** One-directional like all collapse machinery:
high-g deep rows make this EASIER, not contradictory — the cap needs the opposite-direction
absorption input (FINDINGS 2026-07-07 W34).

**Rigour tier.** In-repo paper proof with independent fresh-codex hostile review (L5; Review:
line in the banking commit). NOT af-validated, NOT L0-rigorous; af-elevation candidate (deps
both af-validated).
