---
id: lem-l5-mass-barycenter-dualization
kind: lemma
contract: For every exact signed idempotent P with delta(P) > 0, nonempty visible set W, and hidden top vertex v of height H > 16*sqrt(delta(P)), and every index set A with ||p_j - p_v||_1 >= 4*sqrt(delta(P)) and dist_1(p_j, C_W) > H - 8*sqrt(delta(P)) for every j in A and S := sum_{j in A} max(P_vj, 0) > 0, the full-fiber submeasure m_Q := sum_{j in A cap Q} max(P_vj, 0) and its barycenter q := (1/S)*sum_Q m_Q*p_Q satisfy sup_{y in Y_v} sum_{j in A} max(P_vj, 0)*y.(p_v - p_j) = S*Z_v(q), where Y_v is the top dual face of lem-top-support-dual-face and Z_v(q) = sup_{y in Y_v} y.(p_v - q).
defs: def-signed-idempotent; def-visible-set; def-height
deps: lem-top-support-dual-face; lem-affine-barycenter-identity; lem-delta-zero-endpoint
status: proved
af: none
provenance: W62 wave (docs/waves/2026-07-10-W62-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W62-L5-BATCH.md §R0; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W62-L5-BATCH.md line 'R0: VALID' (incl. clone audit with a partially selected fiber). Reviewer != author.
owner: B
---

**Role (W62 L5 batch, 1/4 — the mass-to-one-point conversion).** Reduces the
L5-GAP-1 mass minimax to the visibility of ONE owned synthetic barycenter: the
mass-weighted far-deep deficit objective equals \(S\cdot Z_v(q_A)\), so L5 asks for
one top-dual direction separating one row-hull point. This replaces the W54
finite-cover framing (retired as the main target in
`DECOMPOSITION-W62-L5.md` §0).

**Mechanism (one line).** Exact finite affine integration of
\(z_y(j)=y\cdot(p_v-p_j)\) against the fiber submeasure
([[lem-affine-barycenter-identity]]), then a supremum over the same compact face
\(Y_v\) ([[lem-top-support-dual-face]]).

**Honest scope (verifier-mandated).** \(A\) need not be fiber-saturated: a
partially selected clone fiber is legal, and \(m_Q\) is defined before fiber
aggregation. Clone invariance is with respect to the weighted lift
\(P'_{ab}=P_{\pi(a)\pi(b)}w_b\) with positive fiber weights summing to one. The
barycenter may re-enter the summit cylinder even when every atom is pointwise
visible (the W54 simplex obstruction) — this lemma converts the objective, it does
not lower-bound it. Failure at level \(\gamma\tau\) places \(q\) in the co-top
cylinder: \(Z_v(q)<\gamma\tau\Rightarrow \mathrm{dist}_1(q,C_W)>H-\gamma\tau\).
Signed picture; clone-invariant.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W62). NOT af-validated.
af-elevation-shaped (single minimal contract). Consumers: the W62 assembly
(R0+R1+R2+R3+S+C+I => L5-GAP-1); the S/C/I creative horns.
