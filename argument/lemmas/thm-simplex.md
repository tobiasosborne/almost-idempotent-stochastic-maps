---
id: thm-simplex
kind: theorem
contract: There are universal delta_0,C>0 such that every signed affine retraction P with neg mass <= delta <= delta_0 whose row polytope K is (i) of affine dimension <=1 (point/segment) or (ii) a simplex with vertices among the rows admits a stochastic idempotent E with ||P-E||_{inf->inf} <= C sqrt(delta), constant C independent of the number of vertices m and of n.
defs: def-stochastic
deps: lem-classical-equiv
status: proved-mod-audit
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/thm-simplex
---

Vertex-count-free O(sqrt delta) stability for simplex row polytopes. Feeds [[thm-well-exposed]].
