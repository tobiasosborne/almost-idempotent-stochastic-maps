---
id: conj-sl1a-off-diagonal-cell
kind: lemma
contract: There exists a universal delta_X in (0,2^(-16)] such that no finite exact signed idempotent P with 0 < delta(P) <= delta_X, nonempty visible set, and hidden top vertex v of height H > 16sqrt(delta(P)) admits a top support functional phi, an admissible exposer h at v, a rho-far co-top row point f with 2(H-phi(p_f))/(2+4delta(P))+h(p_f) <= 12sqrt(delta(P))/13, a legal vertex kernel xi, and either owned radial cell B of the resulting doubly-low coupled corner for which Gamma_f(B) >= 1/4 and Gamma_f{(x,u) in B:p_x != p_u} > 1/8.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: 
status: conjecture
owner: W56-extraction
---

# Off-diagonal freight cell exclusion

## Local notation

For an exact signed idempotent \(P\), put
\[
 \delta:=\delta(P),\quad \tau:=\sqrt\delta,\quad D:=2+4\delta,
 \quad C_W:=\operatorname{conv}\{p_w:w\in W\},\quad d_x:=\operatorname{dist}_1(p_x,C_W).
\]
For a top support functional \(\phi\) at a hidden top \(v\), write \(z:=H-\phi\).  A legal vertex kernel \(\xi_x(u)\) is a probability kernel from row points to geometrically distinct row vertices, constant on clone fibers, satisfying \(p_x=\sum_u\xi_x(u)p_u\) and equal to the Dirac mass at each vertex point.  With full-fiber coefficient mass \(P_{fx}^+:=\sum_{j:p_j=p_x}\max(P_{fj},0)\), set
\[
 \Gamma_f(x,u):=P_{fx}^+\xi_x(u),
\]
\[
 C_f:=\{(x,u):z(p_x)<4\tau,\ h(p_x)<4\tau,\ z(p_u)<4\tau,\ h(p_u)<4\tau\},
\]
and give the radial boundary to the far cell:
\[
 B_F:=C_f\cap\{\|p_u-p_v\|_1\ge4\tau\},
 \qquad
 B_N:=C_f\cap\{\|p_u-p_v\|_1<4\tau\}.
\]

## Statement

There exists a universal \(\delta_X\in(0,2^{-16}]\) such that no finite exact signed idempotent \(P\) with \(0<\delta(P)\le\delta_X\), nonempty visible set, and hidden top vertex \(v\) of height \(H>16\tau\) admits a top support functional \(\phi\), an admissible exposer \(h\) at \(v\), a row point \(f\) satisfying \(\|p_f-p_v\|_1\ge4\tau\), \(d_f>H-4\tau\), and \(2z(p_f)/D+h(p_f)\le12\tau/13\), a legal vertex kernel \(\xi\), and a choice \(B\in\{B_F,B_N\}\) for which
\[
 \Gamma_f(B)\ge\frac14
 \quad\text{and}\quad
 \Gamma_f\{(x,u)\in B:p_x\ne p_u\}>\frac18.
\]

## Notes

This is one exclusion contract, not a claimed proof mechanism.  The lexicographic minimality condition, the web measure and its barycenter, and optimality or relative-interiority of \(h\) have been removed because they are not used after the selected-corner datum exists.  No horn label is retained: the same contract quantifies over either owned radial cell.  Radial membership itself remains because it is what preserves the exact \(1/4\) horn mass and \(1/8\) off-diagonal threshold in the reduction.

The contract is clone-invariant because \(P_{fx}^+\) is a full-fiber sum and \(\xi\) is a kernel on row points.  A refutation requires exact instances with all displayed hypotheses along a family \(\delta_k\to0\) and off-diagonal mass \(>1/8\); a single instance at fixed positive \(\delta\) does not refute the existential ceiling.
