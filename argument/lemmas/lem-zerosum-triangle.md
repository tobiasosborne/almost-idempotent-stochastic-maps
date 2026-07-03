---
id: lem-zerosum-triangle
kind: lemma
contract: Zero-sum triangle bound: let w and v be vectors in R^d with v having coordinate sum zero (sum_l v(l) = 0); write n(x) = sum_l max(-x(l), 0); then n(w - v) <= n(w) + n(v).
defs: 
deps: 
status: proved-mod-audit
af: none
provenance: docs/waves/2026-07-03-A10-weighted-payment.md (arm A wave 10, codex; the zero-sum triangle step of the fan payment proof — pointwise max(-(w(l)-v(l)), 0) <= max(-w(l), 0) + max(v(l), 0), summed, plus sum_l max(v(l), 0) = sum_l max(-v(l), 0) = n(v) by the zero coordinate sum); factored out of proofs/lem-fan-payment after the run-1/run-2 balloon aborts (aism-ugk)
owner: A
workspace: proofs/lem-zerosum-triangle
---

First factored dependency of [[lem-fan-payment]] (the A10 all-mass fan payment). Contains the
run-1 MISSING-fact challenge (`ch-810708fc6185feba`): the identity `sum_l max(v(l),0) = n(v)`
holds exactly because `v` has zero coordinate sum — for general `v` only the pointwise inequality
survives. Elementary two-step proof recorded in the provenance field; `proved-mod-audit` until
af-validated.
