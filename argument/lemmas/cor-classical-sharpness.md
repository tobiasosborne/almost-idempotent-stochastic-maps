---
id: cor-classical-sharpness
kind: corollary
contract: Classical square-root sharpness: for every 0 < lambda < 1/2, choose positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2) supplied by lem-prh-sharpness, and put eta_lambda=2*lambda^2 and Q_lambda=A_lambda M_lambda; then Q_lambda is row-stochastic, ||Q_lambda^2-Q_lambda||_{infinity->infinity} <= eta_lambda, and every stochastic idempotent F on l-infinity(4) satisfies ||Q_lambda-F||_{infinity->infinity} >= lambda=sqrt(eta_lambda/2). Consequently, for every C>0, eta_0>0, and beta>1/2 there exist 0<eta<min{eta_0,1/4} and a row-stochastic Q on l-infinity(4) with ||Q^2-Q||_{infinity->infinity} <= eta such that every stochastic idempotent E satisfies ||Q-E||_{infinity->infinity} > C*eta^beta; equivalently, no uniform exponent beta>1/2 can replace 1/2 in op-classical.
defs: def-positive-approximate-retract; def-stochastic; def-almost-idempotent
deps: lem-prh-sharpness
status: stated
af: seeded
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §7 (explicit 4x4 family and lower bound); docs/plans/2026-07-23-W74F-artifacts/VERDICT-W74F-BATCH.md §A (family rechecked); DESIGN-EXHUME-SHARPNESS.md §§4-6 (direct stochastic defect and quantified corollary, pending fresh hostile audit and user ratification); docs/plans/2026-08-08-EXHUME-SHARPNESS/ADDENDUM-CORSHARP-SKELETON.md §§2-4 (remedy (b) itself was user-ratified in-session 2026-08-09; the addendum TEXT is hostile-audited (AUDIT-CORSHARP-SKELETON.md, LAND-WITH-EXACT-CORRECTIONS, corrections folded))
owner: A
workspace: proofs/cor-classical-sharpness
---
**Status.** `stated` design consequence only.  `lem-prh-sharpness` is T0,
but this row is not: af run 1 aborted at build with 26 live nodes over the
hard cap 20; remedy (b) itself was user-ratified in-session 2026-08-09; the
addendum TEXT is hostile-audited (AUDIT-CORSHARP-SKELETON.md,
LAND-WITH-EXACT-CORRECTIONS, corrections folded).  It is prover guidance only
until a fresh prover and separate fresh verifiers validate a clean new tree.

**Definitional witness package.** For arbitrary `0<lambda<1/2`, take the
positive unital maps `A_lambda,M_lambda` from the validated
`lem-prh-sharpness` external and define
\[
\eta_\lambda:=2\lambda^2=\varepsilon_\lambda,
\qquad
Q_\lambda:=A_\lambda M_\lambda.
\]
These are definitions: in particular, the displayed `Q_lambda` is
definitionally `A_lambda M_lambda`.  Cite the external directly for
`||M_lambda A_lambda-I_2||=2*lambda^2` and for
`||A_lambda M_lambda-F||>=lambda=sqrt(epsilon_lambda/2)` for every
stochastic idempotent `F`; do not reproduce its finite family arithmetic.

**One-node stochastic bridge.** By `def-positive-approximate-retract`, the
two positive unital maps have probability-vector rows and
`||A_lambda||=||M_lambda||=1`; their product `Q_lambda` is row-stochastic.
The only matrix computation left in this target is
\[
Q_\lambda^2-Q_\lambda
=A_\lambda(M_\lambda A_\lambda-I_2)M_\lambda,
\]
so submultiplicativity gives the weak inequality
\[
\lVert Q_\lambda^2-Q_\lambda\rVert_{\infty\to\infty}
\le 1\cdot(2\lambda^2)\cdot1
=\eta_\lambda.
\]
The imported lower bound, read through the definition of `Q_lambda`, gives
`||Q_lambda-F||>=lambda=sqrt(eta_lambda/2)` for every stochastic idempotent
`F`.

**Direct final clause.** Given arbitrary `C>0`, `eta_0>0`, and
`beta>1/2`, choose
\[
0<\lambda<\min\left\{
  \frac1{2\sqrt2},
  \sqrt{\frac{\eta_0}{2}},
  (C\,2^\beta)^{-1/(2\beta-1)}
\right\},
\]
and use the definitions `eta=eta_lambda` and `Q=Q_lambda`.  Then
`0<eta<min{eta_0,1/4}`, `Q` is row-stochastic,
`||Q^2-Q||<=eta`, and every stochastic idempotent `E` satisfies
\[
C\eta^\beta=C\,2^\beta\lambda^{2\beta}
<\lambda\le\lVert Q_\lambda-E\rVert_{\infty\to\infty}.
\]
For each fixed `beta>1/2`, “`beta` can replace `1/2`” means that there exist
`C>0,eta_0>0`, independent of the dimension, such that for every dimension,
every admissible `eta<=eta_0`, and every row-stochastic `Q` of defect at most
`eta`, some stochastic idempotent `E` satisfies `||Q-E||<=C*eta^beta`.  The
already constructed dimension-four witness, for arbitrary proposed
`C,eta_0`, is the literal logical negation of that formula.  This discharge
stays inside the direct final-clause node: do not cite or import
`op-classical`, and do not create a separate wrapper branch.

**Prover contract — MUST-NOTs.**

- MUST NOT create a separate equivalence, logical-negation, or final-clause
  wrapper branch; the direct per-`(C,eta_0,beta)` statement above discharges
  that wording inside one designed node.
- MUST NOT split node 1.4's cutoff positivity and nonempty interval, `eta`
  endpoint checks, strict power inequality, reuse of nodes 1.2--1.3,
  counterexample packaging, or the explicit logical-negation sentence into
  child branches.  They must appear as one linear justification with no child
  branches.  If a verifier will not accept that linear node, the run must
  abort and move to remedy (c), rather than regrow the run-1 branch.
- MUST NOT re-derive any content exported by `lem-prh-sharpness`, including
  its witness construction, retract-defect equality, or distance lower
  bound; cite the registered external.
- MUST NOT perform per-entry arithmetic for `A_lambda`, `M_lambda`,
  `M_lambda A_lambda`, or `A_lambda M_lambda`; none is required by this
  corollary.
- MUST NOT split the identity and submultiplicative estimate into separate
  designed branches; keep the factorization, probability-row norm-one facts,
  and weak defect bound in the same node.
- MUST NOT turn a norm-derived weak inequality into a strict one.  All norm
  estimates remain weak; strictness enters only from the separately stated
  strict choice of `lambda` in the direct final-clause node.
- MUST NOT alter one byte of the root contract, `defs`, or `deps`, or import
  any theorem other than the already registered `lem-prh-sharpness`
  external.
