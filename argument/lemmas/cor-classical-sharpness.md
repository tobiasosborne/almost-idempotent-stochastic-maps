---
id: cor-classical-sharpness
kind: corollary
contract: Classical square-root sharpness: for every 0 < lambda < 1/2, choose positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2) supplied by lem-prh-sharpness, and put eta_lambda=2*lambda^2 and Q_lambda=A_lambda M_lambda; then Q_lambda is row-stochastic, ||Q_lambda^2-Q_lambda||_{infinity->infinity} <= eta_lambda, and every stochastic idempotent F on l-infinity(4) satisfies ||Q_lambda-F||_{infinity->infinity} >= lambda=sqrt(eta_lambda/2). Consequently, for every C>0, eta_0>0, and beta>1/2 there exist 0<eta<min{eta_0,1/4} and a row-stochastic Q on l-infinity(4) with ||Q^2-Q||_{infinity->infinity} <= eta such that every stochastic idempotent E satisfies ||Q-E||_{infinity->infinity} > C*eta^beta; equivalently, no uniform exponent beta>1/2 can replace 1/2 in op-classical.
defs: def-positive-approximate-retract; def-stochastic; def-almost-idempotent
deps: lem-prh-sharpness
status: stated
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §7 (explicit 4x4 family and lower bound); docs/plans/2026-07-23-W74F-artifacts/VERDICT-W74F-BATCH.md §A (family rechecked); DESIGN-EXHUME-SHARPNESS.md §§4-6 (direct stochastic defect and quantified corollary, pending fresh hostile audit and user ratification)
owner: A
workspace: proofs/cor-classical-sharpness
---

**Status.** `stated` design consequence only.  This row promotes nothing
until `lem-prh-sharpness` is T0 and this row has its own fresh prover and
separate fresh verifier tree.

**Direct stochastic bridge.** Positive unital maps between finite
`l-infinity` spaces have probability-vector rows and norm one.  Therefore
`Q_lambda=A_lambda M_lambda` is row-stochastic and
\[
Q_\lambda^2-Q_\lambda
=A_\lambda(M_\lambda A_\lambda-I_2)M_\lambda,
\qquad
\lVert Q_\lambda^2-Q_\lambda\rVert_{\infty\to\infty}
\le 2\lambda^2=\eta_\lambda.
\]
The lower bound for every stochastic idempotent is exactly the imported
`lem-prh-sharpness` conclusion for `A_lambda M_lambda`.

**Explicit quantifier discharge.** Given `C>0`, `eta_0>0`, and
`beta>1/2`, choose
\[
0<\lambda<\min\left\{
  \frac1{2\sqrt2},
  \sqrt{\frac{\eta_0}{2}},
  (C2^\beta)^{-1/(2\beta-1)}
\right\}
\]
and set `eta=eta_lambda=2*lambda^2`.  Then
`0<eta<min{eta_0,1/4}` and
\[
C\eta^\beta=C2^\beta\lambda^{2\beta}<\lambda
\le\lVert Q_\lambda-E\rVert_{\infty\to\infty}
\]
for every stochastic idempotent `E`.  This is the exact negative statement
needed at the `op-classical` interface.
