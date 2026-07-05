---
id: conj-nsc
kind: lemma
contract: Negative self-support charge NSC(K0): there is a universal constant K0 (independent of the matrix size) such that for every rank-3 exact signed idempotent P (square real matrix with P^2 = P and all row sums equal to 1) with 0 < delta(P) <= 1/4 where delta(P) = max_i sum_l max(-P_il,0), every actual-row chart U = (u_0,u_1,u_2) whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, whose Gram volume satisfies Vol(U)/Vol_max(P) >= 1/2 with Vol_max(P) the maximum Gram volume over actual-row charts, and which minimizes Phi(U) = max_r Phi_r(U) among actual-row charts W with Vol(W)/Vol_max(P) >= 1/2, where coordinates a_q(i) are defined by p_i = sum_q a_q(i)p_{u_q}, beta_r(i) = P_{u_r i}, E_r(i) = max(sum_{q != r} max(-a_q(i),0) - (1 - a_r(i)), 0), and Phi_r(U) = sum_i max(beta_r(i),0)E_r(i), every maximal pivot s with Phi_s(U) = Phi(U), and every transverse index r != s, one has B_{r,s} <= K0 * SUM_carriers, where B_{r,s} = sum_i max(beta_r(i),0)*max(-a_s(i),0) and SUM_carriers = the sum over rows i with beta_r(i) > 0 and a_s(i) < 0 of beta_r(i)*nu_i(P) with nu_i(P) = sum_l max(-P_il,0).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: disproved
af: seeded
provenance: docs/waves/2026-07-04-G13-b-lemma-conditional.md §4 (NSC(K0) isolated as the single residual subclaim of the B-lemma; conditional proof B_{r,s} <= (5K0/4)*delta(P) under the cap); independent codex review APPROVE docs/waves/2026-07-04-G13-review.md §4 (single inequality, no hidden compound assertion; reduction correct); B-lemma target docs/waves/2026-07-04-G12-b-question.md §T1 Output And Gap
owner: A
workspace: proofs/conj-nsc
---

**DISPROVED 2026-07-05 (broad form; zero-denominator mode).** Exact rank-3 counterexample,
orchestrator-independently recomputed: `runs/2026-07-05-nsc-zero-denominator-refuter/` — a capped
(`δ ≈ 0.004975`) UNIQUE θ-half Φ-argmin with `Φ = (0,0,0)`, `B_{1,0} = 1/4020000000 > 0`, and the
only carrier row **entrywise nonnegative** (`ν = 0`), so the RHS vanishes. The refuting `B` is
`≪ δ` and the argmin carries no clean high-self non-fan Γ-branch (`Φ ≡ 0`), so the
branch-restricted B-lemma target `B ≤ K·δ` is NOT refuted — what dies is the broad charging shape
(B against carrier-ν). The hypothesis-scope note below fired exactly as recorded: the successor
shape (branch-restricted NSC vs direct δ-financed B-lemma vs capped (G)-emptiness) is escalated
to the user. Wave artifact: `docs/waves/2026-07-05-DC2-nsc-ratio-search.md`.

**The innermost open mechanism of the (PRT) collateral horn** (top-down sketch K<1>5, as it stood 2026-07-04). If NSC(K0)
holds, the B-lemma follows with `K = 5K0/4`: `sum_i beta_r(i)^+ = 1 + sum_i beta_r(i)^- <= 1 +
delta(P)` (row sum 1) and `nu_i(P) <= delta(P)` give `B_{r,s} <= K0(1+delta)delta <= (5K0/4)delta`
under `delta <= 1/4` (G13 §4, review-approved).

**Hypothesis-scope note (orchestrator, 2026-07-05 — read before attacking).** The G12/G13 record
states the B-lemma target "at a capped theta-half Phi-argmin, for a clean high-self non-fan Gamma
branch". This shard deliberately codifies the BROAD form — every capped theta-half Phi-argmin, no
branch clause — because (i) it is a stronger statement that still discharges the B-lemma wherever
the (PRT) skeleton invokes it; (ii) ALL empirical support (K0 ratios below, the 0.77764 stress
maximizer, the G12 realized argmin) lives at capped argmins with NO realized clean high-self
non-fan Gamma branch (G11: 0 realized in 352 capped candidates), so the branch-restricted form has
no known nonvacuous instance to test against; (iii) "high-self" has no pinned threshold in the
registry (G8 uses `kappa_j = 1 - P_jj^+` "tiny", G12 classifies empirically at `1/2`). If the
broad form is REFUTED, the recorded fallback is the branch-restricted variant (a new shard;
contract change = escalation), and capped (G)-emptiness remains the alternative route to (PRT).

**Data (L3, never proof).** Empirical `B_{r,s}/SUM_carriers` on all certified instances:
`200000000/175088281 (~1.14)`, `50000/17919 (~2.79)`, `9/4 (2.25)` — any universal `K0` must be
`>= 2.79`; `K0 ~ 3` would suffice on current data. `sup B/delta = 0.77764` family-limit (algebraic
law, cloning-invariant): `runs/2026-07-04-b-amplifier-hunt/`. Stress instance for wave 14 = the
0.77764 record maximizer.

**Mechanism constraints (why chart moves cannot prove this).** In every certified stress instance
the ENTIRE B-mass sits on volume-INADMISSIBLE carriers (`|a_s(i)|*m_U < 1/2`) — Phi-minimality
comparisons via [[lem-pivot-removing-move]] / [[lem-collateral-import]] / [[lem-negative-pivot-import]]
are blind to them (G13 §3a). The G6 warning applies: the pointwise shortcut
`nu_i >= const * a_s(i)^-` is FALSE away from the argmin mechanism — NSC must genuinely use
argmin/self-support/idempotence structure (`P^2 = P` row reproduction at the carriers), not
per-row sign accounting.

**Role.** Feeds the B-lemma step of the (PRT) skeleton inside [[conj-sc]]; composes with the
validated [[lem-cross-pivot-cancellation]] split `A = B + C - D` and the `C <= 2*delta` theta-half
Cramer box (mod-audit) toward the collateral conclusion of GAP B / (EX) = [[conj-ex]].
