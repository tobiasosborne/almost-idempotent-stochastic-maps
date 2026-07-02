---
id: thm-well-exposed
kind: theorem
contract: There are universal delta_0,c,C>0 such that if a signed affine retraction P with neg mass <= delta <= delta_0 has every row-polytope vertex pairwise separated and (rho,kappa)-exposed with rho <= C sqrt(delta), kappa >= c sqrt(delta), then the vertices are affinely independent (K is a simplex) and thm-simplex gives a stochastic idempotent within C sqrt(delta).
defs: def-exposed; def-stochastic
deps: thm-simplex; lem-exposed-circuit
status: proved-mod-audit
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/thm-well-exposed
---

Well-separated exposed vertices => simplex => O(sqrt delta) via [[thm-simplex]].
