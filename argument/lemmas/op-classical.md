---
id: op-classical
kind: open-problem
contract: (OPEN) Classical projection stability: there are universal eta_0,C>0 (n-free) such that every row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta_0 admits a stochastic idempotent E with ||Q-E||_{inf->inf} <= C sqrt(eta) (the commutative case of op-npps; sharp exponent 1/2).
defs: def-stochastic; def-almost-idempotent; def-near-positive-projection
deps: thm-classical-factorization; prop-approx-simplex
status: open
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/op-classical
---

The **north star** (`PRD.md`). Reduces via [[op-exposed-hull]] (global form of [[thm-classical-factorization]]) and via [[prop-approx-simplex]]; sharpness by [[ex-hume]]. OPEN in-repo.

The two `deps` encode a single **composed** route, not alternatives (AND is the honest encoding): the
exposed-hull/cluster geometry side produces `γ = O(√δ)` approximate simplex coordinates, and
[[prop-approx-simplex]] converts exactly those into the stochastic idempotent `E` within `C(√δ+γ)` —
"reduces `op-classical` to producing `γ=O(√δ)` coords" (`docs/ingest/README.md`, re-tag table row
`prop-approx-simplex`; proved-mod-audit).
