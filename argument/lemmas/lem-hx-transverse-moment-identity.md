---
id: lem-hx-transverse-moment-identity
kind: lemma
contract: For every finite exact signed idempotent P, all points q0 != q1 of the row polytope K(P) = conv{p_i}, and every affine function chi on R^I with chi(q0) = 0 and chi(q1) = 1, the full row-point fibers satisfy sum_Q d_Q*chi(p_Q) = 1, where d_Q = sum_{j in Q}(q1_j - q0_j).
defs: def-signed-idempotent
deps: 
status: proved
af: seeded
workspace: proofs/lem-hx-transverse-moment-identity
provenance: W60 wave (docs/waves/2026-07-10-W60-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W60-ENGINE.md §E1; fresh hostile codex verifier (gpt-5.6-sol, xhigh), batched verdict VERDICT-W60-ENGINE.md line 'E1: VALID'. Reviewer != author.
owner: B
---

**Role (W60 engine bank, 1/5).** The basis-free, rank-free form of the transverse
moment identity — W59 Claim 2 (`lem-starvation-completion-obstruction`) freed from
its rank-3 coordinate basis and extended from rows to arbitrary row-polytope
(synthetic-row) endpoint pairs. Retires the rank>3 half of the W59 §HONEST LIMITS
moment-side gap: the unit moment needs no rank hypothesis at all.

**Statement.** For every finite exact signed idempotent \(P\) (\(P^2=P\),
\(P\mathbf1=\mathbf1\)), all \(q_0\ne q_1\in K(P):=\operatorname{conv}\{p_i\}\), and
every affine \(\chi\) on \(\mathbb R^I\) with \(\chi(q_0)=0\), \(\chi(q_1)=1\):
\[ \sum_Q d_Q\,\chi(p_Q)=1,\qquad d_Q:=\sum_{j\in Q}(q_{1j}-q_{0j}), \]
the sum over full row-point fibers \(Q\).

**Mechanism (one line).** \(D:=q_1-q_0\) satisfies \(DP=D\) and \(D\mathbf1=0\)
(hull points are fixed, mass-one); the affine constant dies against
\(D\mathbf1=0\) and the linear part reproduces \(L(D)=\chi(q_1)-\chi(q_0)=1\);
regroup by fibers.

**Also proved in the source (Construction E1.2, body-level, not part of this
contract):** the normalized class is nonempty — the sign functional
\(\chi(x)=\operatorname{sgn}(D)\cdot(x-q_0)/\lVert D\rVert_1\) has ℓ¹-Lipschitz
constant \(1/\lVert D\rVert_1\) (dual-norm attainment, finite-dimensional).

**Scope.** An identity, not an inequality: it supplies no bound by itself and no
selection of \((q_0,q_1,\chi)\). Clone-invariant (full-fiber sums of affine values
on row points). Signed picture.

**Rigour tier.** L5 (fresh hostile codex, batched W60 verdict). NOT af-validated.
af-elevation candidate (single minimal contract). Consumers:
[[lem-hx-financing-floor]], [[lem-hx-robust-scalar-starvation]].
