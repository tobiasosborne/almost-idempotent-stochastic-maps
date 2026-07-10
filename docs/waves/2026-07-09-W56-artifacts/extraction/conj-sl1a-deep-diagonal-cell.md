---
id: conj-sl1a-deep-diagonal-cell
kind: lemma
contract: There exists a universal delta_D in (0,2^(-16)] such that no finite exact signed idempotent P with 0 < delta(P) <= delta_D, nonempty visible set, and hidden top vertex v of height H > 16sqrt(delta(P)) admits a top support functional phi, an admissible exposer h at v, a rho-far co-top row point f with 2(H-phi(p_f))/(2+4delta(P))+h(p_f) <= 12sqrt(delta(P))/13, a legal vertex kernel xi, and either owned radial cell B of the resulting doubly-low coupled corner for which Gamma_f(B) >= 1/4 and the diagonal Gamma_f-mass on carriers whose always-tight far hull is disjoint from their scaled always-tight upper hull is greater than 1/16.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
owner: W56-extraction
---

# Deep disjoint-diagonal cell exclusion

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
 K_T(u):=\operatorname{conv}\{p_r-p_u:r\in T(u)\},\qquad
 K_O(u):=t^*(u)\operatorname{conv}\{p_i-p_u:i\in O(u)\}.
\]
Call \(u\) type D when \(K_T(u)\cap K_O(u)=\varnothing\).

## Statement

There exists a universal \(\delta_D\in(0,2^{-16}]\) such that no finite exact signed idempotent \(P\) with \(0<\delta(P)\le\delta_D\), nonempty visible set, and hidden top vertex \(v\) of height \(H>16\tau\) admits a top support functional \(\phi\), an admissible exposer \(h\) at \(v\), a row point \(f\) satisfying \(\|p_f-p_v\|_1\ge4\tau\), \(d_f>H-4\tau\), and \(2z(p_f)/D+h(p_f)\le12\tau/13\), a legal vertex kernel \(\xi\), and a choice \(B\in\{B_F,B_N\}\) for which
\[
 \Gamma_f(B)\ge\frac14
 \quad\text{and}\quad
 \Gamma_f\{(x,u)\in B:p_x=p_u\ \text{and}\ K_T(u)\cap K_O(u)=\varnothing\}>\frac1{16}.
\]

## Notes

This one statement codifies the disjoint-diagonal residual and does not claim the invalid max-principle far-side return channel.  Minimality, the web measure and barycenter, and optimality of the top exposer have been stripped.  No horn label or per-horn mechanism remains; the contract treats either owned radial cell uniformly.  The radial cell itself is retained only because its \(1/4\) lower mass is the input to the exact \(1/8\) diagonal and \(1/16\) carrier-type bookkeeping.

All coefficient masses are full-fiber row-point sums, so the contract is clone-invariant.  The companion proved-candidate capacity draft claims that a zero-face blocker cannot ship \(1/16\) of its positive mass to the \(\kappa\)-high slab at \(\delta\le2^{-16}\), but this conjecture neither consumes that author-claim nor presents it as a proof of the cell exclusion.  A refutation of this existential ceiling must be an exact family with \(\delta_k\to0\) and type-D diagonal mass \(>1/16\); a single completed instance at a fixed scale can always lie above a smaller proposed ceiling.
