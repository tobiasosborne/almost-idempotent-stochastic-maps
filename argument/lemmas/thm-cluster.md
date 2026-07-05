---
id: thm-cluster
kind: theorem
contract: There are universal delta_0,C>0 such that a signed affine retraction P with neg mass <= delta <= delta_0 having representatives r^1..r^m pairwise 2rho-separated, each (rho,kappa)-exposed (disjoint clusters U_a), with every off-cluster row within gamma of conv{r^a}, admits a stochastic idempotent E with ||P-E||_{inf->inf} <= C(rho+gamma+delta/kappa+delta); so rho,gamma=O(sqrt delta), kappa>=c sqrt(delta) give O(sqrt delta), C independent of m, n, and the number of transient rows.
defs: def-exposed; def-stochastic
deps: lem-exposed-circuit
status: proved-mod-audit
af: seeded
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/thm-cluster
---

Well-separated exposed clusters reconstruct a stochastic idempotent, constant free of m,n,#transient. Feeds [[thm-classical-factorization]].
