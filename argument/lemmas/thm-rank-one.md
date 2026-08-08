---
id: thm-rank-one
kind: theorem
contract: There are universal delta_0,C>0 such that every rank-one signed affine retraction P=I-u v^T (sum_j v_j=0, v^T u=1) with neg mass <= delta <= delta_0 is within ||P-E||_{inf->inf} <= C sqrt(delta) of a stochastic idempotent E.
defs: def-stochastic
deps: lem-classical-equiv
status: proved-mod-audit
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/thm-rank-one
---

Rank-one retractions are O(sqrt delta)-stable.  The historical 3x3 matrix
family recorded in [[ex-hume]] is a rank-one instance; this is a
matrix-family reference only and imports no claim from the disproved
`ex-hume` contract.
