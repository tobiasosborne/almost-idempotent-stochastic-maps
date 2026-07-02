---
id: lem-leakage
kind: lemma
contract: Affine-face leakage: for row-stochastic Q with ||Q^2-Q|| <= eta and affine h:Delta_n->[0,1], m=max_j h(q_j), d_i=m-h(q_i), one has q_i({j:h(q_j)<=m-gamma}) <= (d_i+eta)/gamma; so a maximiser row leaks at most sqrt(eta) of its mass below level m-sqrt(eta) and no O(eta) closure is possible.
defs: def-stochastic; def-exposed
deps: 
status: proved-mod-audit
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/lem-leakage
---

The sqrt(eta) affine-face leakage scale. Feeds [[lem-exposed-circuit]].
