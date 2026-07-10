---
id: conj-sl1a-intersection-diagonal-cell
kind: lemma
contract: There exists a universal delta_I in (0,2^(-16)] such that no finite exact signed idempotent P with 0 < delta(P) <= delta_I, nonempty visible set, and hidden top vertex v of height H > 16sqrt(delta(P)) admits a top support functional phi, an admissible exposer h at v, a rho-far co-top row point f with 2(H-phi(p_f))/(2+4delta(P))+h(p_f) <= 12sqrt(delta(P))/13, a legal vertex kernel xi, and either owned radial cell B of the resulting doubly-low coupled corner for which Gamma_f(B) >= 1/4 and the diagonal Gamma_f-mass on carriers whose always-tight far hull intersects their scaled always-tight upper hull is at least 1/16.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
owner: W56-extraction
---

# Intersection-diagonal cell exclusion

## Local notation

For an exact signed idempotent \(P\), put
\[
 \delta:=\delta(P),\quad \tau:=\sqrt\delta,\quad D:=2+4\delta,
 \quad C_W:=\operatorname{conv}\{p_w:w\in W\},\quad d_x:=\operatorname{dist}_1(p_x,C_W).
\]
For a top support functional \(\phi\) at a hidden top \(v\), write \(z:=H-\phi\).  A legal vertex kernel \(\xi_x(u)\) is a probability kernel from row points to geometrically distinct row vertices, constant on clone fibers, satisfying \(p_x=\sum_u\xi_x(u)p_u\) and equal to the Dirac mass at each vertex point.  With
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
For a hidden vertex \(u\), let \(T(u)\) and \(O(u)\) be respectively the \(4\tau\)-far and upper-box constraint families tight on the whole optimal face of the exposedness LP at \(u\), and define
\[
 K_T(u):=\operatorname{conv}\{p_r-p_u:r\in T(u)\},qquad
 K_O(u):=t^*(u)\operatorname{conv}\{p_i-p_u:i\in O(u)\}.
\]
Call \(u\) type I when \(K_T(u)\cap K_O(u)\ne\varnothing\).

## Statement

There exists a universal \(\delta_I\in(0,2^{-16}]\) such that no finite exact signed idempotent \(P\) with \(0<\delta(P)\le\delta_I\), nonempty visible set, and hidden top vertex \(v\) of height \(H>16\tau\) admits a top support functional \(\phi\), an admissible exposer \(h\) at \(v\), a row point \(f\) satisfying \(\|p_f-p_v\|_1\ge4\tau\), \(d_f>H-4\tau\), and \(2z(p_f)/D+h(p_f)\le12\tau/13\), a legal vertex kernel \(\xi\), and a choice \(B\in\{B_F,B_N\}\) for which
\[
 \Gamma_f(B)\ge\frac14
 \quad\text{and}\quad
 \Gamma_f\{(x,u)\in B:p_x=p_u\ \text{and}\ K_T(u)\cap K_O(u)\ne\varnothing\}\ge\frac1{16}.
\]

## Notes

This is a single cell-exclusion conjecture; it does not assert a second-generation recursion or a termination functional.  Lexicographic minimality, the original web and barycenter, and relative-interior optimality of the top exposer are absent because none is needed to define or route this coefficient-mass cell.  The horn label is removed; only the owned radial cell remains, because the reduction needs its \(1/4\) mass before the diagonal and type splits.

The type is attached to the carrier \(u\), while the diagonal condition \(p_x=p_u\) keeps the coefficient and kernel coordinates correctly coupled.  All masses are row-point masses, hence clone-invariant.  Refuting the positive-ceiling statement requires a family of exact instances with \(\delta_k\to0\) and type-I diagonal mass at least \(1/16\); one fixed-\(\delta\) example is insufficient.
