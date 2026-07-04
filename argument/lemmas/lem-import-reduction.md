---
id: lem-import-reduction
kind: lemma
contract: Import reduction: let P be a rank-3 exact signed idempotent (square real matrix with P^2 = P and all row sums equal to 1), let U = (u_0,u_1,u_2) be an actual-row chart whose rows p_{u_0}, p_{u_1}, p_{u_2} form a basis of the row space, define coordinates a_q(i) by p_i = sum_q a_q(i)p_{u_q} and beta_r(i) = P_{u_r i}; fix a pivot index s, a non-chart row j with c = a_s(j) > 0, a transverse index r != s, and let t be the remaining index, writing d_r = a_r(j) and d_t = a_t(j); define R_{r,j}(i) = (1/c - 1)*max(-a_s(i),0) + max(a_s(i)*d_t/c, 0) - a_s(i)*d_r/c, I_{r,j}(U) = sum_i max(beta_r(i),0)*max(R_{r,j}(i),0), A_{r,s} = sum_i max(beta_r(i),0)*max(a_s(i),0), and B_{r,s} = sum_i max(beta_r(i),0)*max(-a_s(i),0); then I_{r,j}(U) <= ((max(1-c,0) + max(-d_t,0) + max(d_r,0))/c)*B_{r,s} + ((max(d_t,0) + max(-d_r,0))/c)*A_{r,s}.
defs: def-signed-idempotent
deps: 
status: proved-mod-audit
af: none
provenance: docs/waves/2026-07-04-G11-capped-charge.md §Task 1 eq. (4) (per-row split of R_{r,j}(i)_+ into a_s(i)^- and a_s(i)^+ multiples: (1/c-1)a_s^- has positive part ((1-c)^+/c)a_s^-; (a_s d_t/c)^+ = (a_s^+ d_t^+ + a_s^- d_t^-)/c; -a_s d_r/c <= (d_r^-/c)a_s^+ + (d_r^+/c)a_s^-; multiply by beta_r^+ and sum); exhibits verified by the orchestrator 2026-07-04
owner: A
workspace: proofs/lem-import-reduction
---

**G11's universal reduction (4)** of the collateral import to the two cross-pivot masses. The
statement is purely about the sum `I_{r,j}(U)` as defined — it does not consume the
[[lem-collateral-import]] inequality; the two COMPOSE: (CI) bounds `Phi_r(V_j)` by
`Phi_r(U) + I_{r,j}(U)`, and this lemma bounds `I_{r,j}(U)` by coefficient combinations of
`B_{r,s}` and `A_{r,s}`. With [[lem-cross-pivot-cancellation]],
`A_{r,s} = B_{r,s} + C_{r,s} - D_{r,s}`, so the dominant term reduces to `B_{r,s} + C_{r,s}` —
the exact (PRT) cross-pivot residual named by wave G11 for [[conj-sc]].

**Exhibits (T0, orchestrator-recomputed 2026-07-04).** The capped term toys of G11: the pure
`(iii)` instance (`delta = 1/4`, `c = 6/5`, `d_t = 0`, `d_r = -1/5`, single import row,
`I_{1,j} = 1/20`) and the mixed toy (`delta = 427/2000`, `I_{1,j} = 1/75`), plus the G10
`delta = 49/60` witness where the bound's dominant term is sharp. Note the coefficient
`(1-c)^+ = 0` whenever `c >= 1` (the first term vanishes for volume-expanding moves).

**What this does NOT say.** No claim that `B_{r,s}` or `A_{r,s}` is controlled by the pivot-s
unified budget — that is exactly the OPEN cross-pivot charge question ((PRT) residual, wave 12).
The `c > 0` restriction matches [[lem-collateral-import]]; `c < 0` is not covered.
