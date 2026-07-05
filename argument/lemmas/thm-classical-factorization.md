---
id: thm-classical-factorization
kind: theorem
contract: There are universal eta_0,C>0 such that if Q is row-stochastic with eta=||Q^2-Q||_{inf->inf}<=eta_0 and the rows of P=theta(2Q-1) satisfy the thm-cluster geometry (rho,gamma=O(sqrt eta), kappa>=c sqrt eta), then there exist a finite-dim commutative special JB-algebra J and unital positive maps Delta:J->ell^inf_n, Upsilon:ell^inf_n->J with Upsilon Delta=id_J, ||Delta Upsilon-Q||_{inf->inf}<=C sqrt(eta), and Upsilon(Delta x . Delta y)=x*y.
defs: def-stochastic
deps: thm-cluster; op-exposed-hull
status: proved-mod-audit
af: seeded
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/thm-classical-factorization
---

The (conditional) factorization; its global form + [[op-exposed-hull]] gives [[op-classical]]. NOTE: the JB-algebra target vocabulary (commutative special JB-algebra, unital positive maps Delta,Upsilon) is the bridge to the general Jordan case and is DEFERRED here (out of scope per `PRD.md`; lives in ../almost-idempotent-positive-maps).
