Status: remedy (b) itself was user-ratified in-session 2026-08-09; the addendum TEXT is hostile-audited (AUDIT-CORSHARP-SKELETON.md, LAND-WITH-EXACT-CORRECTIONS, corrections folded) / NON-RIGOROUS / DO NOT PROMOTE FROM THIS FILE ALONE.

# ADDENDUM — tighten the `cor-classical-sharpness` af skeleton

Date: 2026-08-09
Role: fresh proof-strategy designer
Disposition: REMEDY (b); KEEP THE BYTE-FROZEN INTERFACE AND CAP 20

## 1. Diagnosis

Run 1 expanded to 26 live nodes before verification, over the hard cap 20; it
is the fourth balloon in this sharpness family.  The recorded tree localizes
the excess in two places: nodes 1.4--1.5 spent about ten nodes on scalar
choice, counterexample packaging, and a separate logical-equivalence wrapper,
while nodes 1.2.x split the elementary defect factorization into a second
branch.  See
`docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-CORSHARP-ABORTED.md`,
especially nodes 1.2.x and 1.4--1.5.

This is the family-specific expansion pattern recorded in `FINDINGS.md` on
2026-08-08 and 2026-08-09: designs of 7, 6, and 5 nodes expanded as far as the
24, 19, and 12 live-node landed trees, with observed expansion about
1.5--3x, while explicit identifications and wide quantifier branches caused
the aborts.  The repair therefore makes `eta_lambda` and `Q_lambda`
definitions at first use, treats the validated `lem-prh-sharpness` export as
the sole source of its family content, keeps the norm calculation in one
node, and makes the final clause itself the direct quantified counterexample
rather than proving a second equivalence statement.

## 2. The tightened skeleton

Node 1 remains the byte-frozen registry contract.  The following four child
statements are exact design text; a prover may refine their internal
justification, but may not weaken them, create the forbidden wrapper branch,
or change the root interface.

- **Node 1.1 — Definitional witness package. Exact statement:** For an
  arbitrary real `lambda` with `0<lambda<1/2`, choose the positive unital maps
  `A_lambda:l-infinity(2)->l-infinity(4)` and
  `M_lambda:l-infinity(4)->l-infinity(2)` supplied by the registered external
  `lem-prh-sharpness`, and define in this node
  \[
  \eta_\lambda:=2\lambda^2=\varepsilon_\lambda,
  \qquad
  Q_\lambda:=A_\lambda M_\lambda.
  \]
  These displayed equations are the definitions of `eta_lambda` and
  `Q_lambda`, so in every descendant `Q_lambda` is definitionally
  `A_lambda M_lambda`.  The imported external supplies exactly
  \[
  \varepsilon_\lambda
   =\lVert M_\lambda A_\lambda-I_2\rVert_{\infty\to\infty}
   =2\lambda^2
  \]
  and, for every stochastic idempotent `F` on `l-infinity(4)`,
  \[
  \lVert A_\lambda M_\lambda-F\rVert_{\infty\to\infty}
  \ge\lambda=\sqrt{\varepsilon_\lambda/2}.
  \]

- **Node 1.2 — One-node stochastic bridge and defect bound. Exact
  statement:** For the maps and definitions in node 1.1,
  `def-positive-approximate-retract` identifies `A_lambda` and `M_lambda`
  with probability-row matrices; hence their product `Q_lambda` is
  row-stochastic, and the induced `infinity->infinity` norms satisfy
  `||A_lambda||=||M_lambda||=1`.  In this same node, associativity gives the
  sole matrix computation required in this target,
  \[
  Q_\lambda^2-Q_\lambda
   =A_\lambda(M_\lambda A_\lambda-I_2)M_\lambda,
  \]
  and submultiplicativity gives only the weak bound
  \[
  \begin{aligned}
  \lVert Q_\lambda^2-Q_\lambda\rVert_{\infty\to\infty}
  &\le
  \lVert A_\lambda\rVert_{\infty\to\infty}
  \lVert M_\lambda A_\lambda-I_2\rVert_{\infty\to\infty}
  \lVert M_\lambda\rVert_{\infty\to\infty}\\
  &=2\lambda^2=\eta_\lambda.
  \end{aligned}
  \]
  No exact equality for the defect of `Q_lambda` is asserted.

- **Node 1.3 — Imported distance and scale. Exact statement:** Because node
  1.1 defines `Q_lambda:=A_lambda M_lambda`, the lower bound in the registered
  external `lem-prh-sharpness` reads directly
  \[
  \lVert Q_\lambda-F\rVert_{\infty\to\infty}\ge\lambda
  \]
  for every stochastic idempotent `F` on `l-infinity(4)`; and because
  `eta_lambda:=2*lambda^2` with `lambda>0`, one has
  `lambda=sqrt(eta_lambda/2)`.  Together with node 1.2, this proves every
  clause of the root's first sentence without re-deriving any entry of the
  imported family.

- **Node 1.4 — Direct quantified counterexample and explicit local expansion
  of the final clause. Exact statement:** Fix arbitrary `C>0`, `eta_0>0`, and
  `beta>1/2`, and choose
  \[
  0<\lambda<\min\left\{
    \frac{1}{2\sqrt2},
    \sqrt{\frac{\eta_0}{2}},
    (C\,2^\beta)^{-1/(2\beta-1)}
  \right\}.
  \]
  With the definitions `eta:=eta_lambda=2*lambda^2` and
  `Q:=Q_lambda=A_lambda M_lambda` from node 1.1, node 1.2 gives a
  row-stochastic `Q` with
  `||Q^2-Q||_{infinity->infinity}<=eta`, the strict choice of `lambda` gives
  `0<eta<min{eta_0,1/4}`, and for every stochastic idempotent `E`, node 1.3
  and the same strict choice give
  \[
  C\eta^\beta=C\,2^\beta\lambda^{2\beta}
  <\lambda
  \le\lVert Q_\lambda-E\rVert_{\infty\to\infty}.
  \]
  For each fixed `beta>1/2`, “`beta` can replace `1/2`” means that there exist
  `C>0,eta_0>0`, independent of the dimension, such that for every dimension,
  every admissible `eta<=eta_0`, and every row-stochastic `Q` of defect at
  most `eta`, some stochastic idempotent `E` satisfies
  `||Q-E||<=C*eta^beta`.  The already constructed dimension-four witness,
  for arbitrary proposed `C,eta_0`, is the literal logical negation of that
  formula.  This discharge stays inside node 1.4: do not cite or import
  `op-classical`, and do not create a separate wrapper branch.

**Budget arithmetic.** The final-clause discharge is a sixth designed
obligation even though it is kept physically inside node 1.4; it must not
become a separate af branch.  Thus the honest count is the root, nodes
1.1--1.4, and the final-clause discharge, hence **6 designed obligations
total**.  The family budget law gives `6 x 3 = 18 <= 20`, leaving two
live-node slots below the unchanged cap.

## 3. Exact registry-body replacement and provenance append

Every current frontmatter field remains byte-identical except `provenance:`.
Append exactly this clause to its current value:

```text
; docs/plans/2026-08-08-EXHUME-SHARPNESS/ADDENDUM-CORSHARP-SKELETON.md §§2-4 (remedy (b) itself was user-ratified in-session 2026-08-09; the addendum TEXT is hostile-audited (AUDIT-CORSHARP-SKELETON.md, LAND-WITH-EXACT-CORRECTIONS, corrections folded))
```

Thus the exact replacement `provenance:` line is:

```text
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §7 (explicit 4x4 family and lower bound); docs/plans/2026-07-23-W74F-artifacts/VERDICT-W74F-BATCH.md §A (family rechecked); DESIGN-EXHUME-SHARPNESS.md §§4-6 (direct stochastic defect and quantified corollary, pending fresh hostile audit and user ratification); docs/plans/2026-08-08-EXHUME-SHARPNESS/ADDENDUM-CORSHARP-SKELETON.md §§2-4 (remedy (b) itself was user-ratified in-session 2026-08-09; the addendum TEXT is hostile-audited (AUDIT-CORSHARP-SKELETON.md, LAND-WITH-EXACT-CORRECTIONS, corrections folded))
```

Replace everything after the closing frontmatter `---` line by exactly the
following body:

```markdown
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
```

## 4. Run parameters and abort rule

Run parameters are unchanged: hard live-node cap **20**, at most **4**
rounds, **4** workers, and `xhigh` prover / `xhigh` verifiers.  Use a fresh
prover and separate fresh hostile verifiers; do not resume the 26-node
aborted tree.

For any new cap hit, use the abort taxonomy at
`docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-PRHSHARP-FACTOR.md` §6:
classify it as `MISSING fact`, `DAG dep`, or `genuine gap`; never raise the
cap.  The run-1 evidence and its build-shape classification remain at
`docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-CORSHARP-ABORTED.md`.
