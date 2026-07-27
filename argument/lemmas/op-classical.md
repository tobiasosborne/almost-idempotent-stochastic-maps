---
id: op-classical
kind: open-problem
contract: (OPEN) Classical projection stability: there are universal eta_0,C>0 (n-free) such that every row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta_0 admits a stochastic idempotent E with ||Q-E||_{inf->inf} <= C sqrt(eta) (the commutative case of op-npps).
defs: def-stochastic; def-almost-idempotent; def-near-positive-projection
deps: thm-classical-factorization; prop-approx-simplex
status: open
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/op-classical
---

The **north star** (`PRD.md`). Reduces via [[op-exposed-hull]] (global form of [[thm-classical-factorization]]) and via [[prop-approx-simplex]]; sharpness by [[ex-hume]]. OPEN in-repo.

**Contract split (USER-RATIFIED 2026-07-27, decision D1 option A of
`docs/plans/2026-07-27-W78-ratification-package.md`):** the contract line is
the upper stability bound ONLY. The sharpness of the exponent 1/2 (no
`C·eta^beta` with `beta > 1/2` can hold universally) is a SEPARATE statement
carried by [[ex-hume]] and is NOT part of this contract; a route that proves
the upper bound discharges this open problem. Rationale: the Route-F
assembly (`AUDIT-F0-ASSEMBLY.md` §§0.2, 4) proves only the upper bound, and
a compound contract would force `ex-hume` into every route's dependency
closure. The future Route-F wiring (applied only at the LAST step of the
ratified campaign, package §5 step 6) is
`routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]`.

The two `deps` encode a single **composed** route, not alternatives (AND is the honest encoding): the
exposed-hull/cluster geometry side produces `γ = O(√δ)` approximate simplex coordinates, and
[[prop-approx-simplex]] converts exactly those into the stochastic idempotent `E` within `C(√δ+γ)` —
"reduces `op-classical` to producing `γ=O(√δ)` coords" (`docs/ingest/README.md`, re-tag table row
`prop-approx-simplex`; proved-mod-audit).
