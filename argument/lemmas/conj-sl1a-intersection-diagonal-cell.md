---
id: conj-sl1a-intersection-diagonal-cell
kind: lemma
contract: There exists a universal delta_I in (0,2^(-16)] such that no finite exact signed idempotent P with 0 < delta(P) <= delta_I, nonempty visible set W, and hidden top vertex v of height H > 16sqrt(delta(P)) admits an affine phi with phi(p_v) = H, phi <= 0 on C_W = conv{p_w:w in W}, and |phi(a)-phi(b)| <= ||a-b||_1, an admissible exposer h at v, a row point f with ||p_f-p_v||_1 >= 4sqrt(delta(P)), dist_1(p_f,C_W) > H-4sqrt(delta(P)), and 2(H-phi(p_f))/(2+4delta(P))+h(p_f) <= 12sqrt(delta(P))/13, and a probability kernel xi_x(u) from row points to geometrically distinct row vertices, constant on clone fibers, with p_x = sum_u xi_x(u)p_u and Dirac at vertex points, such that, on defining P_fx^+ = sum_{j:p_j=p_x} max(P_fj,0), Gamma_f(x,u) = P_fx^+ xi_x(u), C_f = {(x,u):H-phi(p_x) < 4sqrt(delta(P)), h(p_x) < 4sqrt(delta(P)), H-phi(p_u) < 4sqrt(delta(P)), h(p_u) < 4sqrt(delta(P))}, B_F = C_f intersect {(x,u):||p_u-p_v||_1 >= 4sqrt(delta(P))}, B_N = C_f intersect {(x,u):||p_u-p_v||_1 < 4sqrt(delta(P))}, the exposedness-LP optimal face F^*(u) = {(g,t^*(u)):g is affine, g(p_u) = 0, 0 <= g(p_i) <= 1 for every row i, and g(p_r) >= t^*(u) whenever ||p_r-p_u||_1 >= 4sqrt(delta(P))}, T(u) = {r:||p_r-p_u||_1 >= 4sqrt(delta(P)) and g(p_r) = t^*(u) for every (g,t^*(u)) in F^*(u)}, O(u) = {i:g(p_i) = 1 for every (g,t^*(u)) in F^*(u)}, K_T(u) = conv{p_r-p_u:r in T(u)}, and K_O(u) = t^*(u)conv{p_i-p_u:i in O(u)}, some B in {B_F,B_N} satisfies Gamma_f(B) >= 1/4, Gamma_f{(x,u) in B:p_x != p_u} <= 1/8, and Gamma_f{(x,u) in B:p_x = p_u and K_T(u) intersect K_O(u) != empty} >= 1/16.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
af: none
provenance: W56 wave (docs/waves/2026-07-09-W56-artifacts/): extracted from the twice-hostile-verified routine material of DECOMPOSITION-v2 (verdict-round1.md, verdict-round2.md); per-shard fresh hostile codex verdict in verdict-extraction.md (4 VALID + 6 VALID-WITH-CORRECTIONS, corrections applied and re-listed in the wave doc); reviewer != author throughout.
owner: B
---

# Intersection-diagonal cell exclusion

## Local notation

For an exact signed idempotent \(P\), put
\[
 \delta:=\delta(P),\quad \tau:=\sqrt\delta,\quad D:=2+4\delta,
 \quad C_W:=\operatorname{conv}\{p_w:w\in W\},\quad d_x:=\operatorname{dist}_1(p_x,C_W).
\]
A top support functional at a hidden top \(v\) is an affine function \(\phi\) satisfying \(\phi(p_v)=H\), \(\phi\le0\) on \(C_W\), and \(|\phi(a)-\phi(b)|\le\|a-b\|_1\).  For such a \(\phi\), write \(z:=H-\phi\).  A legal vertex kernel \(\xi_x(u)\) is a probability kernel from row points to geometrically distinct row vertices, constant on clone fibers, satisfying \(p_x=\sum_u\xi_x(u)p_u\) and equal to the Dirac mass at each vertex point.  With
\[
 P_{fx}^+:=\sum_{j:p_j=p_x}\max(P_{fj},0),\qquad
 \Gamma_f(x,u):=P_{fx}^+\xi_x(u),
\]
set
\[
 C_f:=\{(x,u):z(p_x)<4\tau,\ h(p_x)<4\tau,\ z(p_u)<4\tau,\ h(p_u)<4\tau\},
\]
\[
 B_F:=C_f\cap\{\|p_u-p_v\|_1\ge4\tau\},
 \qquad
 B_N:=C_f\cap\{\|p_u-p_v\|_1<4\tau\}.
\]
For a hidden vertex \(u\), let \(\mathcal F^*(u)\) be the optimal face of the exposedness LP,
\[
 \mathcal F^*(u):=\{(g,t^*(u)):g\text{ is affine},\ g(p_u)=0,\ 0\le g(p_i)\le1\ \text{for every row }i,\ g(p_r)\ge t^*(u)\ \text{whenever }\|p_r-p_u\|_1\ge4\tau\},
\]
and define
\[
 T(u):=\{r:\|p_r-p_u\|_1\ge4\tau\ \text{and}\ g(p_r)=t^*(u)\ \text{for every }(g,t^*(u))\in\mathcal F^*(u)\},
\]
\[
 O(u):=\{i:g(p_i)=1\ \text{for every }(g,t^*(u))\in\mathcal F^*(u)\}.
\]
Define
\[
 K_T(u):=\operatorname{conv}\{p_r-p_u:r\in T(u)\},qquad
 K_O(u):=t^*(u)\operatorname{conv}\{p_i-p_u:i\in O(u)\}.
\]
Call \(u\) type I when \(K_T(u)\cap K_O(u)\ne\varnothing\).
For \(B\subseteq C_f\), put
\[
 M_X(B):=\Gamma_f\{(x,u)\in B:p_x\ne p_u\}.
\]

## Statement

There exists a universal \(\delta_I\in(0,2^{-16}]\) such that no finite exact signed idempotent \(P\) with \(0<\delta(P)\le\delta_I\), nonempty visible set, and hidden top vertex \(v\) of height \(H>16\tau\) admits a top support functional \(\phi\), an admissible exposer \(h\) at \(v\), a row point \(f\) satisfying \(\|p_f-p_v\|_1\ge4\tau\), \(d_f>H-4\tau\), and \(2z(p_f)/D+h(p_f)\le12\tau/13\), a legal vertex kernel \(\xi\), and a choice \(B\in\{B_F,B_N\}\) for which
\[
 \Gamma_f(B)\ge\frac14,
 \qquad M_X(B)\le\frac18,
 \quad\text{and}\quad
 \Gamma_f\{(x,u)\in B:p_x=p_u\ \text{and}\ K_T(u)\cap K_O(u)\ne\varnothing\}\ge\frac1{16}.
\]

## Notes

This is a single cell-exclusion conjecture; it does not assert a second-generation recursion or a termination functional.  Lexicographic minimality, the original web and barycenter, and relative-interior optimality of the top exposer are absent because none is needed to define or route this coefficient-mass cell.  The horn label is removed; only the owned radial cell remains, because the reduction needs its \(1/4\) mass before the diagonal and type splits.

The type is attached to the carrier \(u\), while the diagonal condition \(p_x=p_u\) keeps the coefficient and kernel coordinates correctly coupled.  All masses are row-point masses, hence clone-invariant.  Refuting the positive-ceiling statement requires a family of exact instances with \(\delta_k\to0\) and type-I diagonal mass at least \(1/16\); one fixed-\(\delta\) example is insufficient.
