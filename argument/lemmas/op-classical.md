---
id: op-classical
kind: theorem
contract: Classical projection stability: there are universal eta_0,C>0 (n-free) such that every row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta_0 admits a stochastic idempotent E with ||Q-E||_{inf->inf} <= C sqrt(eta) (the commutative case of op-npps).
defs: def-stochastic; def-almost-idempotent; def-near-positive-projection
deps:
routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]
status: proved
af: validated
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex); ROOT REWIRE 2026-08-08 (user-ratified): OR-routes block per DESIGN-F0-ASSEMBLY.md sect-3 / AUDIT-F0-ASSEMBLY.md sect-3 (Route F via the T0 lem-routef-f0-assembly; the legacy signed-geometry route retained as an independent alternative); the "(OPEN)" contract marker removed as part of the ratified discharge package (D1 sharpness split executed W80; sharpness now carried at T0 by cor-classical-sharpness; the former ex-hume contract was retracted as disproved on 2026-08-08)
owner: A
workspace: proofs/op-classical
---

**DISCHARGED AT T0 (2026-08-08).** Root af tree: 5/5 nodes validated/clean
(fresh codex prover, separate fresh hostile verifiers per node); external
oracle `af-op-classical` + `fr verify` PASS; mechanical flip. The theorem
is af-validated end-to-end through Route F; explicit witnesses
eta_0 = eta_K and C = K+4*sqrt(2K) from the strengthened
[[lem-routef-k-ledger]]. NOTE the honest boundary: this discharges the UPPER-BOUND contract (the D1 split, W80); sharpness of the exponent 1/2 is the separate af-validated corollary [[cor-classical-sharpness]], and af-validation is this repo's L0 rung (b), not a Lean/mathlib proof.

The **north star** (`PRD.md`). Two independent routes: Route F via
[[lem-routef-f0-assembly]] (the T0 Kitaev-factorization assembly; eta_0 = eta_K,
C = K+4*sqrt(2K)), and the legacy signed-geometry route via
[[thm-classical-factorization]] + [[prop-approx-simplex]]. Sharpness of the exponent 1/2 is carried separately at T0 by [[cor-classical-sharpness]].

**Contract split (USER-RATIFIED 2026-07-27, decision D1 option A of `docs/plans/2026-07-27-W78-ratification-package.md`):** the contract line is the upper stability bound ONLY. The sharpness of the exponent 1/2 (no `C·eta^beta` with `beta > 1/2` can hold universally) is a SEPARATE statement now carried at T0 by [[cor-classical-sharpness]] and is NOT part of this contract; a route that proves the upper bound discharges this theorem.
Rationale: the Route-F
assembly (`AUDIT-F0-ASSEMBLY.md` §§0.2, 4) proves only the upper bound, and
a compound contract would force `ex-hume` into every route's dependency
closure. Historical note: at the W80 split this separate statement was assigned to [[ex-hume]]; that pointer is superseded because the old ex-hume contract is now disproved.
The future Route-F wiring (applied only at the LAST step of the
ratified campaign, package §5 step 6) is
`routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]`.

The two `deps` encode a single **composed** route, not alternatives (AND is the honest encoding): the
exposed-hull/cluster geometry side produces `γ = O(√δ)` approximate simplex coordinates, and
[[prop-approx-simplex]] converts exactly those into the stochastic idempotent `E` within `C(√δ+γ)` —
"reduces `op-classical` to producing `γ=O(√δ)` coords" (`docs/ingest/README.md`, re-tag table row
`prop-approx-simplex`; proved-mod-audit).
