---
id: op-exposed-hull
kind: open-problem
contract: (OPEN) Global exposed-hull lemma: there are universal c,C>0 such that for every near-positive signed affine retraction with neg mass <= delta, taking rho=C sqrt(delta) and W_{rho,kappa}={vertices v: e_v(rho)>=kappa} with kappa=c sqrt(delta), every row is within C sqrt(delta) of conv W_{rho,kappa}; by thm-classical-factorization (global form) this implies op-classical.
defs: def-exposed; def-stochastic
deps: conj-kernel
status: open
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/op-exposed-hull
---

The intermediate open lemma; blocked on [[conj-kernel]] (the classical-portfolio's reduction op-exposed-hull <= HLC <= Kernel). Feeds [[thm-classical-factorization]] (global form) -> [[op-classical]].
