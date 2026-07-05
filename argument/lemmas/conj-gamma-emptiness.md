---
id: conj-gamma-emptiness
kind: lemma
contract: Capped Gamma-emptiness: for every rank-3 exact signed idempotent P (square real matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i sum_l max(-P_il,0), every actual-row chart U = (u_0,u_1,u_2) whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, which is theta-half (Vol(U)/Vol_max(P) >= 1/2, with Vol_max(P) the maximum Gram volume over actual-row charts) and minimizes Phi(U) = max_r Phi_r(U) among theta-half actual-row charts, where coordinates a_q(i) are defined by p_i = sum_q a_q(i)p_{u_q}, E_r(i) = max(sum_{q != r} max(-a_q(i),0) - (1 - a_r(i)), 0), and Phi_r(U) = sum_i max(P_{u_r i},0)E_r(i), every maximal pivot s with Phi_s(U) = Phi(U), and every non-chart row j whose pivot-removing chart V_j = U - u_s + j is theta-half admissible (|a_s(j)|*Vol(U)/Vol_max(P) >= 1/2), with new coordinates a_s^j(i) = a_s(i)/a_s(j) and a_q^j(i) = a_q(i) - a_s(i)a_q(j)/a_s(j) for q != s, Psi_j = sum_i max(P_{ji},0)*max(sum_{q != s} max(-a_q^j(i),0) - (1 - a_s^j(i)), 0), and Gamma_j = max over r != s of sum_i max(P_{u_r i},0)*max(sum_{q != r} max(-a_q^j(i),0) - (1 - a_r^j(i)), 0), it is NOT the case that Psi_j < Phi_s(U) <= Gamma_j.
defs: def-signed-idempotent; def-negative-mass
deps: 
status: conjecture
af: none
provenance: docs/waves/2026-07-04-G11-capped-charge.md (0 clean (G) branches in 352 capped candidates; "prove capped (G)-emptiness" named as the alternative route); docs/waves/2026-07-04-G10-collateral-branch.md (the delta=49/60 clean-Gamma witness — pattern is cap-blocked, not structurally impossible); successor decision docs/recon/2026-07-05-open-mechanism-recon.md §0 + runs/2026-07-05-nsc-zero-denominator-refuter/ (user decision 2026-07-05 after the broad-NSC refutation)
owner: A
workspace: proofs/conj-gamma-emptiness
---

**The adopted successor to the disproved broad [[conj-nsc]]** (user decision 2026-07-05: attack
capped (G)-emptiness first as a bounded proof attempt; the δ-financed branch-restricted B-lemma is
the recorded fallback target — the aism-z98 shape). If this holds, the Γ-branch of the validated
pivot-removing disjunction [[lem-pivot-removing-move]] (`Φ_s(U) ≤ max(Ψ_j, Γ_j)`) is VACUOUS under
the cap: every admissible pivot-removing move at a capped θ-half Φ-argmin is Ψ-blocked (or
volume-inadmissible), the (PRT) collateral horn's B-lemma regime is never entered, and sketch-v2
node K3's open charge reduces to the realized-and-charged (V)/(Ψ) branches (G9).

**Scope note (read before attacking).** Stated UNQUALIFIED — over every admissible pivot-removing
row `j`, with no "high-self"/"non-fan" clause: (i) those qualifiers have no pinned registry
threshold (the drift risk that bit broad NSC); (ii) the G10/G11 searches effectively tested the
unqualified form (0 realized in 352 capped candidates; G11 also reports 0 among the 93 high-self
β_s-positive admissible candidates); (iii) unqualified emptiness makes the Γ-branch vacuous
wherever it arises. Note `Ψ_j ≥ 0`, so any clean Γ-block forces `Φ_s(U) > 0` — no extra
positivity hypothesis is needed. If REFUTED by an instance outside the high-self non-fan class,
the narrowed (NF-restricted) variant is the recorded fallback; if refuted inside it, the
Γ-emptiness route is dead and the program moves to the δ-financed B-lemma.

**Refute-side design (the untried G11 direction).** Structured dilution of the G10 `δ = 49/60`
clean-Γ witness across `k ≥ 3` auxiliary near-silent rows, pushing `δ ≤ 1/4` while preserving
`Ψ_j < Φ_s(U) ≤ Γ_j` — adversarial, not uniform-random (three prior budgets survived random
probing and fell to targeted constructions: D3, G5, G6).

**Prove-side leads.** The cap enters through the θ-half Cramer box and the validated import
machinery: [[lem-collateral-import]] (c>0), [[lem-negative-pivot-import]] (c<0, reviewed),
[[lem-import-reduction]], [[lem-cross-pivot-cancellation]] — a clean Γ-block forces
`Φ_s(U) − Φ_r(U) ≤ I_{r,j}(U)`, and the import reduces to cross-pivot masses; the question is
whether `δ ≤ 1/4` starves that forcing below `Φ_s(U)`. WARNING (DC2): any charge of carrier mass
to carrier row-negativity alone is DEAD (`runs/2026-07-05-nsc-zero-denominator-refuter/` — a
carrier can be entrywise nonnegative at a certified argmin).
