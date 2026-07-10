---
id: conj-b-restricted
kind: lemma
contract: Branch-restricted B-lemma: there is a universal constant K (n-free) such that for every rank-3 exact signed idempotent P with 0 < delta(P) <= 1/4, every theta-half Phi-argmin actual-row chart U = (u_0,u_1,u_2) (notation of def-pivot), every maximal pivot s admitting a non-chart row j whose pivot-removing chart V_j is theta-half admissible with Psi_j < Phi_s(U) <= Gamma_j (def-pivot), and every transverse index r != s: B_{r,s} = sum_i max(P_{u_r i},0)*max(-a_s(i),0) <= K*delta(P).
defs: def-signed-idempotent; def-negative-mass; def-pivot
deps: 
status: conjecture
af: none
provenance: docs/waves/2026-07-04-G12-b-question.md §T1 Output And Gap (the original branch-sensitive target); docs/waves/2026-07-05-W15-gamma-emptiness.md (the T1 residual making this the sole missing ingredient, and the first certified instance of the hypothesis class); user-adopted fallback decision 2026-07-05 (successor to the disproved conj-gamma-emptiness and broad conj-nsc)
owner: A
workspace: proofs/conj-b-restricted
---

**Contract rewritten 2026-07-10 (notation -> defs; aism-0mm); the pre-rewrite contract is preserved
verbatim below.** The rank-3 chart machinery (actual-row chart, theta-half, Vol_max, Phi_r/E_r,
maximal pivot, pivot-removing chart V_j, theta-half admissible, Psi_j, Gamma_j, the new coordinates
a_s^j/a_q^j) was moved into [[def-pivot]]; only the cell-specific quantity B_{r,s} stays inline. The
MATHEMATICAL CONTENT is identical.

> PRE-REWRITE CONTRACT (verbatim): Branch-restricted B-lemma: there is a universal constant K
> (independent of the matrix size) such that for every rank-3 exact signed idempotent P (square real
> matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i
> sum_l max(-P_il,0), every actual-row chart U = (u_0,u_1,u_2) whose rows p_{u_0}, p_{u_1}, p_{u_2}
> form a basis of the row space, which is theta-half (Vol(U)/Vol_max(P) >= 1/2, with Vol_max(P) the
> maximum Gram volume over actual-row charts) and minimizes Phi(U) = max_r Phi_r(U) among theta-half
> actual-row charts, where coordinates a_q(i) are defined by p_i = sum_q a_q(i)p_{u_q}, E_r(i) =
> max(sum_{q != r} max(-a_q(i),0) - (1 - a_r(i)), 0), and Phi_r(U) = sum_i max(P_{u_r i},0)E_r(i),
> every maximal pivot s with Phi_s(U) = Phi(U) for which there exists a non-chart row j whose
> pivot-removing chart V_j = U - u_s + j is theta-half admissible (|a_s(j)|*Vol(U)/Vol_max(P) >= 1/2)
> and which, with new coordinates a_s^j(i) = a_s(i)/a_s(j) and a_q^j(i) = a_q(i) - a_s(i)a_q(j)/a_s(j)
> for q != s, Psi_j = sum_i max(P_{ji},0)*max(sum_{q != s} max(-a_q^j(i),0) - (1 - a_s^j(i)), 0), and
> Gamma_j = max over r != s of sum_i max(P_{u_r i},0)*max(sum_{q != r} max(-a_q^j(i),0) - (1 -
> a_r^j(i)), 0), satisfies Psi_j < Phi_s(U) <= Gamma_j, and every transverse index r != s, one has
> B_{r,s} = sum_i max(P_{u_r i},0)*max(-a_s(i),0) <= K*delta(P).

**The single open link of the (PRT) collateral horn** (sketch-v2 node K3) after two refutations
narrowed its shape. If this holds with constant `K`, the wave-15 residual closes the collateral
conclusion EXPLICITLY: `M − Φ_r(U) ≤ 17·B_{r,s} + 20·δ ≤ (17K + 20)·δ` under the θ-half Cramer
box (c>0 constant 16, c<0 constant 20) — nothing else is missing on that branch.

**The hypothesis class is certified NONEMPTY** (unlike every earlier "clean-branch" statement):
the wave-15 refuter `runs/2026-07-05-gamma-emptiness-refuter/` is its first certified member,
with `B_{1,2}/δ = 0.7708` — so `K ≥ 0.7708` is forced, and the wave-13 amplifier family law
(`sup B/δ = 0.77764`, cloning-invariant) suggests `K ≥ 0.77764`. All certified data to date is
consistent with `K ~ 1`.

**Charging constraints inherited from the death certificates (both orchestrator-verified):**
(i) broad [[conj-nsc]] is DEAD — do NOT charge `B` to carrier row-negativity: a carrier can be
entrywise nonnegative at a certified argmin (`runs/2026-07-05-nsc-zero-denominator-refuter/`);
(ii) [[conj-gamma-emptiness]] is DEAD — the branch cannot be argued away; (iii) the G6 warning
stands (pointwise `ν_i ≥ const·a_s(i)⁻` is false); (iv) in the wave-13 stress instances all
B-mass sits on volume-inadmissible carriers (chart-move blind spot), so the proof must price
B-mass by argmin structure that survives inadmissibility — candidate leads: the G8 (FE)
stationarity recipe applied to `B_{r,s}` (recon lane 1, candidate 2), or a Γ-block-specific
obstruction using the certified instance's anatomy.

**Stress seed for any wave:** the wave-15 instance (6 rows, insert-y skeleton + one row) — the
first place prove-side and refute-side can both grip a realized clean Γ-block.
