---
id: lem-prh-sharpness-family-arithmetic
kind: lemma
contract: Witness arithmetic for PRH sharpness: for every real lambda with 0 < lambda < 1/2, let A_lambda in R^(4x2) have rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), and let M_lambda in R^(2x4) have rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda); A_lambda and M_lambda have nonnegative entries and probability-vector rows and hence represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2); for every pair of integers r,s >= 1 and every B in R^(r x s), the induced l-infinity operator norm is ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|; M_lambda A_lambda has rows (1-lambda^2,lambda^2), (lambda^2,1-lambda^2), so epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and epsilon_lambda tends to 0 as lambda tends to 0; and P_lambda:=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.
defs: def-positive-approximate-retract
deps:
status: proved
af: validated
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md sect-7; docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS-V2.md sects-2.1,4.1 (W139 package); docs/plans/2026-08-08-EXHUME-SHARPNESS/BRIEF-PRHSHARP-FACTOR.md Situation (BALLOON run 1 at 27 live nodes and clean-reseed BALLOON run 2 at 28 live nodes, 2026-08-08); docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-PRHSHARP-ABORTED.md (run-2 tree, 2026-08-08); af elevation run 2 VALIDATED 2026-08-09 (fresh xhigh prover per FINDINGS 2026-08-08 remedy (a), separate fresh xhigh verifiers, 24/24 nodes validated, taint clean, cap 26 respected, 5+3 rounds; two in-run challenges repaired in-tree: non-strict norm chain incl. R=0, per-row product derivation; export proofs/lem-prh-sharpness-family-arithmetic/export.md; fr verify pass via oracle af-lem-prh-sharpness-family-arithmetic)
owner: A
workspace: proofs/lem-prh-sharpness-family-arithmetic
---

**Status.** `proved` / `af: validated` (2026-08-09, run 2). Mechanical reflection
of the codex ledger: root validated with 24/24 nodes clean under hard cap 26 by a
fresh xhigh prover and separate fresh xhigh verifiers (FINDINGS 2026-08-08 remedy
(a)); externally banked via `fr verify` on the export path.

**Factoring role.** This row contains the whole witness branch: the rows of
`A_lambda` and `M_lambda`, their probability-row interpretation, the induced
`l-infinity` max-row norm identity, both finite matrix products, the exact
retract defect, and the two relevant `P_lambda=A_lambda M_lambda` rows at
exact `l1` distance `2*lambda`.  It imports no theorem.

**Strict/weak boundary.** The max-row formula implies only
`||row_i(B)||_1 <= ||B||_{infinity->infinity}` for each row; equality is
asserted only after taking the maximum.  The downstream main proof must retain
this weak `<=` before combining it with its separate assumption `d<lambda`.

**Designed af budget.** Seven nodes; honest live expectation 11--21 nodes
under the observed 1.5--3x expansion; at most 5 rounds; hard cap 26.  The 3x
endpoint is 21, strictly below 26.  A cap hit is a new stop-and-classify event,
not permission to enlarge the cap.
