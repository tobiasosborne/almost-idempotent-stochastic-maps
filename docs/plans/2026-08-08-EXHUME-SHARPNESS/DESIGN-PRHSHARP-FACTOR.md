Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE — pending fresh hostile audit and user ratification.

# DESIGN — factor `lem-prh-sharpness` after two BALLOON aborts

Date: 2026-08-08
Role: fresh factoring designer
Disposition: NATURAL TWO-ROW SPLIT FITS THE BUDGETS; NO DEVIATION PROPOSED

The two new rows are exactly the independent branch boundaries requested in
`BRIEF-PRHSHARP-FACTOR.md`: one exports the explicit witness and all of its finite
arithmetic, and one exports the general row-coincidence theorem for stochastic
idempotents.  The byte-frozen main row retains only witness instantiation, the
distance contradiction, scale assembly, and a dedicated quantified reading of its
final intrinsic-sharpness clause.  Nothing here is rigorous or authorized for
landing until a fresh hostile audit and explicit user ratification.

## 1. New registry shard 1 — explicit family and arithmetic

The following is complete land-ready shard text.  It may be landed verbatim only
after the guard at the head of this file is released.

```markdown
---
id: lem-prh-sharpness-family-arithmetic
kind: lemma
contract: Witness arithmetic for PRH sharpness: for every real lambda with 0 < lambda < 1/2, let A_lambda in R^(4x2) have rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), and let M_lambda in R^(2x4) have rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda); A_lambda and M_lambda have nonnegative entries and probability-vector rows and hence represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2); for every pair of integers r,s >= 1 and every B in R^(r x s), the induced l-infinity operator norm is ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|; M_lambda A_lambda has rows (1-lambda^2,lambda^2), (lambda^2,1-lambda^2), so epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and epsilon_lambda tends to 0 as lambda tends to 0; and P_lambda:=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.
defs: def-positive-approximate-retract
deps:
status: stated
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md sect-7; docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS-V2.md sects-2.1,4.1 (W139 package); docs/plans/2026-08-08-EXHUME-SHARPNESS/BRIEF-PRHSHARP-FACTOR.md Situation (BALLOON run 1 at 27 live nodes and clean-reseed BALLOON run 2 at 28 live nodes, 2026-08-08); docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-PRHSHARP-ABORTED.md (run-2 tree, 2026-08-08)
owner: A
workspace: proofs/lem-prh-sharpness-family-arithmetic
---

**Status.** `stated` design transcription only.  This shard promotes nothing
and may not be seeded before fresh hostile audit and user ratification.

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
```

## 2. New registry shard 2 — row coincidence

The following is complete land-ready shard text.  It is independent of shard 1
and may be landed verbatim only after the guard at the head of this file is
released.

```markdown
---
id: lem-prh-sharpness-row-coincidence
kind: lemma
contract: Row coincidence for stochastic idempotents: for every integer n >= 1, every n-by-n row-stochastic idempotent matrix F=(f_ab) over R, and all i,j in {1,...,n}, if f_ii>0 and f_ij>0 then row_i(F)=row_j(F).
defs: def-stochastic
deps:
status: stated
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md sect-7 (especially sect-7.1); docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS-V2.md sects-2.1,4.1 (W139 package); docs/plans/2026-08-08-EXHUME-SHARPNESS/BRIEF-PRHSHARP-FACTOR.md Situation (BALLOON run 1 at 27 live nodes and clean-reseed BALLOON run 2 at 28 live nodes, 2026-08-08); docs/plans/2026-08-08-EXHUME-SHARPNESS/TREE-PRHSHARP-ABORTED.md (run-2 tree, 2026-08-08)
owner: A
workspace: proofs/lem-prh-sharpness-row-coincidence
---

**Status.** `stated` design transcription only.  This shard promotes nothing
and may not be seeded before fresh hostile audit and user ratification.

**Factoring role.** This row contains the entire general-idempotent branch.
For the stationary probability `pi=row_i(F)`, its positive support is closed.
A finite source-component argument rules out edges between distinct support
components, and the edges from `i` to every support vertex force strong
connectivity.  The minimum-ratio argument then proves uniqueness of the
stationary probability on that support and hence equality of rows `i` and `j`.
No finite Markov-chain classification theorem is imported.

**Designed af budget.** Six nodes; honest live expectation 9--18 nodes under
the observed 1.5--3x expansion; at most 5 rounds; hard cap 22.  The 3x endpoint
is 18, strictly below 22.  A cap hit is a new stop-and-classify event, not
permission to enlarge the cap.
```

## 3. Byte-frozen main row — dependency delta only

The contract below is copied byte-for-byte from the current registry shard and
must not change during landing:

```text
contract: PRH square-root sharpness: for every 0 < lambda < 1/2 there are positive unital maps A:l-infinity(2)->l-infinity(4) and M:l-infinity(4)->l-infinity(2) with epsilon_lambda=||MA-I_2||_{infinity->infinity}=2*lambda^2 tending to 0 such that every stochastic idempotent F on l-infinity(4) satisfies ||AM-F||_{infinity->infinity} >= lambda=sqrt(epsilon_lambda/2); hence the sqrt(epsilon) order in PRH is intrinsically sharp.
```

The only proposed registry edit is to replace the empty `deps:` line by:

```text
deps: lem-prh-sharpness-family-arithmetic; lem-prh-sharpness-row-coincidence
```

No `defs:` change is needed.  The main row remains
`proved-mod-audit` / `af: seeded`; its existing provenance, owner, workspace,
body, and byte-frozen contract remain untouched.  After ratification and after
both new dependencies are T0, neither aborted main tree may be resumed or
patched: cleanly re-seed the frozen root with the revised imports.

## 4. Complete af tree skeletons

Each root below is byte-identical to its proposed registry contract.  Child
wording is the land-ready design boundary; a fresh prover may refine a child
without weakening the root or importing undeclared theorems.

### 4.1 `lem-prh-sharpness-family-arithmetic` — 7 designed nodes

- **Node 1 — Root.** Witness arithmetic for PRH sharpness: for every real lambda with 0 < lambda < 1/2, let A_lambda in R^(4x2) have rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), and let M_lambda in R^(2x4) have rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda); A_lambda and M_lambda have nonnegative entries and probability-vector rows and hence represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2); for every pair of integers r,s >= 1 and every B in R^(r x s), the induced l-infinity operator norm is ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|; M_lambda A_lambda has rows (1-lambda^2,lambda^2), (lambda^2,1-lambda^2), so epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and epsilon_lambda tends to 0 as lambda tends to 0; and P_lambda:=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.
- **Node 1.1 — Probability rows and map types.** Fix arbitrary real
  `lambda` with `0<lambda<1/2`.  Then `lambda>0` and `1-lambda>0`;
  every displayed entry of `A_lambda` and `M_lambda` is nonnegative,
  their respective four and two row sums are one, and
  `def-positive-approximate-retract` identifies them with positive unital
  maps of the asserted finite `l-infinity` types.
- **Node 1.2 — Max-row norm identity.** For integers `r,s>=1` and
  `B in R^(r x s)`, the induced norm from `l-infinity(s)` to
  `l-infinity(r)` equals the maximum row `l1` norm.
  - **Node 1.2.1 — Upper inequality.** For every `x in R^s` and each row
    `i`, the triangle inequality gives
    `|(Bx)_i| <= (sum_j |B_ij|)*||x||_infinity`; taking maxima and the
    operator-norm supremum proves `||B|| <= max_i sum_j |B_ij|`.
  - **Node 1.2.2 — Lower inequality.** Choose a maximizing row `i_0` and
    `x_j=1` when `B_(i_0,j)>=0`, `x_j=-1` otherwise.  Then
    `||x||_infinity=1` and `(Bx)_(i_0)=sum_j |B_(i_0,j)|`, proving the
    reverse inequality.
- **Node 1.3 — The `M_lambda A_lambda` product and defect.** Direct
  multiplication gives rows
  `(1-lambda^2,lambda^2)` and
  `(lambda^2,1-lambda^2)`.  Subtracting `I_2` gives rows
  `(-lambda^2,lambda^2)` and `(lambda^2,-lambda^2)`; node 1.2 therefore
  gives the exact norm `2*lambda^2`.  This positive expression tends to
  zero as `lambda` tends to zero.
- **Node 1.4 — The `A_lambda M_lambda` product and separation.** Direct
  multiplication gives the four rows stated at the root; they are
  probability vectors, so `P_lambda` is row-stochastic.  Subtracting row
  3 from row 1 gives
  `(lambda*(1-lambda),-lambda*(1-lambda),lambda^2,-lambda^2)`, whose
  `l1` norm is `2*lambda*(1-lambda)+2*lambda^2=2*lambda`.

Designed count: 7.  Honest live expectation: 11--21.  Maximum rounds: 5.
Hard cap: 26.

### 4.2 `lem-prh-sharpness-row-coincidence` — 6 designed nodes

- **Node 1 — Root.** Row coincidence for stochastic idempotents: for every integer n >= 1, every n-by-n row-stochastic idempotent matrix F=(f_ab) over R, and all i,j in {1,...,n}, if f_ii>0 and f_ij>0 then row_i(F)=row_j(F).
- **Node 1.1 — Stationarity and closed support.** Put
  `pi=row_i(F)` and `S={r:pi_r>0}`.  The `i`-th row of `F^2=F` gives
  `pi F=pi`.  For `t` outside `S`, the equality
  `0=pi_t=sum_r pi_r f_rt` and nonnegativity imply `f_rt=0` for every
  `r in S`; hence `S` is closed under every positive transition.
- **Node 1.2 — Source-component exclusion.** In the finite directed
  support graph on `S`, suppose the condensation graph has an edge.  It
  then has a source strongly connected component `C` with an outgoing
  edge.  There is no transition into `C` from `S\C`, while stationarity
  gives
  `pi(C)=sum_{r in C} pi_r F(r,C)=pi(C)-sum_{r in C} pi_r F(r,S\C)`.
  The last sum is strictly positive because `pi_r>0` on `S` and `C` has
  an outgoing edge, a contradiction.  Thus there are no edges between
  distinct components.
- **Node 1.3 — Strong connectivity of the support.** For every `r in S`,
  `f_ir=pi_r>0`, so the support graph has an edge `i->r`.  Node 1.2 rules
  out an edge between distinct components, hence every `r in S` lies in
  the component of `i` and the graph on `S` is strongly connected.
- **Node 1.4 — Stationary rows on the support.** For every `r in S`,
  closedness makes `row_r(F)` a probability supported on `S`, and the
  `r`-th row of `F^2=F` makes it stationary.  Every nonzero stationary
  nonnegative vector on this strongly connected finite graph has full
  support, since its support is a nonempty closed subset.
- **Node 1.5 — Minimum-ratio uniqueness and assembly.** For stationary
  probabilities `p,q` on `S`, node 1.4 makes all coordinates positive.
  Put `c=min_{r in S} q_r/p_r>0`.  Then `q-cp` is nonnegative,
  stationary, and has a zero coordinate.  If nonzero, normalization would
  produce a stationary probability with proper support, contradicting
  node 1.4.  Hence `q=cp`, and total mass gives `c=1`.  Thus all rows
  indexed by `S` equal `pi`; since `f_ij>0` puts `j in S`, rows `i` and
  `j` coincide.

Designed count: 6.  Honest live expectation: 9--18.  Maximum rounds: 5.
Hard cap: 22.

### 4.3 Slimmed `lem-prh-sharpness` — 5 designed nodes

- **Node 1 — Root.** PRH square-root sharpness: for every 0 < lambda < 1/2 there are positive unital maps A:l-infinity(2)->l-infinity(4) and M:l-infinity(4)->l-infinity(2) with epsilon_lambda=||MA-I_2||_{infinity->infinity}=2*lambda^2 tending to 0 such that every stochastic idempotent F on l-infinity(4) satisfies ||AM-F||_{infinity->infinity} >= lambda=sqrt(epsilon_lambda/2); hence the sqrt(epsilon) order in PRH is intrinsically sharp.
- **Node 1.1 — Instantiate the imported witness.** Fix arbitrary
  `0<lambda<1/2` and take the explicit `A=A_lambda`, `M=M_lambda`,
  `P=AM`, and `epsilon_lambda` from
  `lem-prh-sharpness-family-arithmetic`.  The imported contract supplies
  the positive-unital types, exact retract defect, max-row norm identity,
  all four rows of `P`, and exact row-1/row-3 separation `2*lambda`.
- **Node 1.2 — Coincidence and distance telescope.** Let `F=(f_ab)` be
  any stochastic idempotent on `l-infinity(4)` and set
  `d=||P-F||_{infinity->infinity}`.  If `d<lambda`, the imported max-row
  identity gives the correctly weak consequences
  `||row_1(P)-row_1(F)||_1 <= d` and
  `||row_3(P)-row_3(F)||_1 <= d`.  Coordinate domination and the explicit
  first row of `P` then give
  `f_11 >= 1-lambda-d > 1-2*lambda > 0` and
  `f_13 >= lambda-d > 0`.  Applying
  `lem-prh-sharpness-row-coincidence` with `i=1,j=3` makes rows 1 and 3
  of `F` coincide, so the triangle inequality and the two weak row bounds
  give `2*lambda <= d+d < 2*lambda`, a contradiction.  Therefore
  `||AM-F||_{infinity->infinity}>=lambda` for every such `F`.
- **Node 1.3 — Scale assembly.** The imported identity
  `epsilon_lambda=2*lambda^2` and `lambda>0` give
  `lambda=sqrt(epsilon_lambda/2)`, while the same family contract gives
  `epsilon_lambda->0` as `lambda->0`.  Nodes 1.1--1.2 therefore supply
  every clause of the frozen root before its final semicolon.
- **Node 1.4 — Dedicated quantified final-clause discharge.** Give
  “the `sqrt(epsilon)` order in PRH is intrinsically sharp” the following
  precise reading: for every `C>0`, `epsilon_0>0`, and `beta>1/2`, there
  exists `0<lambda<1/2` with `epsilon_lambda<epsilon_0` such that every
  stochastic idempotent `F` satisfies
  `||A_lambda M_lambda-F||_{infinity->infinity}>C*epsilon_lambda^beta`.
  Indeed choose
  `0<lambda<min{1/2,sqrt(epsilon_0/2),(C*2^beta)^(-1/(2*beta-1))}`.
  Since `2*beta-1>0`, this gives
  `C*epsilon_lambda^beta=C*2^beta*lambda^(2*beta)<lambda`; node 1.2 gives
  the weak lower bound `||A_lambda M_lambda-F||>=lambda`, hence the
  required strict failure for every `F`.  Thus no uniform power
  `C*epsilon^beta` with `beta>1/2` can replace square-root order along
  this family, exactly supporting the frozen root's final clause.

Designed count: 5.  Honest live expectation: 8--15.  Maximum rounds: 4.
Hard cap: 18.

Rounding each per-target 1.5x lower endpoint upward gives 11+9+8=28 live
nodes (the unrounded total is 27); the summed 28--54 live-expectation range
covers the observed 28--31-node monolith with margin rather than using the
rejected eight-node projection.  Factoring
adds interfaces but removes cross-branch patch thrash; the per-target 3x
endpoints are respectively 21, 18, and 15, each strictly below its cap and
every cap is at most 26.

## 5. Exact seeding packages

No command in this section is authorized by this design.  Run these packages
only after a fresh hostile `LAND` verdict and explicit user ratification.
Before every `def-add` and `add-external`, check the fresh workspace for a
duplicate name.

### 5.1 `lem-prh-sharpness-family-arithmetic`

Initialize node 1 from the section 1 contract and register exactly one
definition:

```text
python3 scripts/seed-af-workspaces.py lem-prh-sharpness-family-arithmetic
af def-add def-positive-approximate-retract --file definitions/def-positive-approximate-retract.md -d proofs/lem-prh-sharpness-family-arithmetic
```

There are no theorem externals.  The norm identity and every matrix
calculation are proved in-tree.

### 5.2 `lem-prh-sharpness-row-coincidence`

Initialize node 1 from the section 2 contract and register exactly one
definition:

```text
python3 scripts/seed-af-workspaces.py lem-prh-sharpness-row-coincidence
af def-add def-stochastic --file definitions/def-stochastic.md -d proofs/lem-prh-sharpness-row-coincidence
```

There are no theorem externals.  Support closure, the finite
source-component step, and stationary-probability uniqueness are all proved
in-tree.

### 5.3 Slimmed `lem-prh-sharpness`

Only after both new rows are af-validated, externally verified, banked T0,
and present on the revised main `deps:` line, cleanly re-seed the main root
from the byte-frozen contract.  Register exactly its two existing definitions:

```text
python3 scripts/seed-af-workspaces.py lem-prh-sharpness
af def-add def-positive-approximate-retract --file definitions/def-positive-approximate-retract.md -d proofs/lem-prh-sharpness
af def-add def-stochastic --file definitions/def-stochastic.md -d proofs/lem-prh-sharpness
```

Register exactly the following two externals, once each.  Each source has the
literal validated-workspace path followed by the byte-verbatim proposed
registry contract.

**E1 — `lem-prh-sharpness-family-arithmetic`**

```text
imports validated registry lemma proofs/lem-prh-sharpness-family-arithmetic — Witness arithmetic for PRH sharpness: for every real lambda with 0 < lambda < 1/2, let A_lambda in R^(4x2) have rows (1,0), (0,1), (1-lambda,lambda), (lambda,1-lambda), and let M_lambda in R^(2x4) have rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda); A_lambda and M_lambda have nonnegative entries and probability-vector rows and hence represent positive unital maps A_lambda:l-infinity(2)->l-infinity(4) and M_lambda:l-infinity(4)->l-infinity(2); for every pair of integers r,s >= 1 and every B in R^(r x s), the induced l-infinity operator norm is ||B||_{infinity->infinity}=max_{1<=i<=r} sum_{j=1}^s |B_ij|; M_lambda A_lambda has rows (1-lambda^2,lambda^2), (lambda^2,1-lambda^2), so epsilon_lambda:=||M_lambda A_lambda-I_2||_{infinity->infinity}=2*lambda^2 and epsilon_lambda tends to 0 as lambda tends to 0; and P_lambda:=A_lambda M_lambda is row-stochastic with rows (1-lambda,0,lambda,0), (0,1-lambda,0,lambda), ((1-lambda)^2,lambda*(1-lambda),lambda*(1-lambda),lambda^2), (lambda*(1-lambda),(1-lambda)^2,lambda^2,lambda*(1-lambda)), and ||row_1(P_lambda)-row_3(P_lambda)||_1=2*lambda.
```

Invocation shape:

```text
af add-external --name "lem-prh-sharpness-family-arithmetic" --source <the exact E1 source string above> -d proofs/lem-prh-sharpness
```

**E2 — `lem-prh-sharpness-row-coincidence`**

```text
imports validated registry lemma proofs/lem-prh-sharpness-row-coincidence — Row coincidence for stochastic idempotents: for every integer n >= 1, every n-by-n row-stochastic idempotent matrix F=(f_ab) over R, and all i,j in {1,...,n}, if f_ii>0 and f_ij>0 then row_i(F)=row_j(F).
```

Invocation shape:

```text
af add-external --name "lem-prh-sharpness-row-coincidence" --source <the exact E2 source string above> -d proofs/lem-prh-sharpness
```

There are no other theorem externals.  In particular W74F, W139, the two
aborted trees, `cor-classical-sharpness`, and `op-classical` are proof guides,
provenance, or consumers, never axioms of these targets.

## 6. Elevation order and budgets

1. After hostile audit and user ratification, land
   `lem-prh-sharpness-family-arithmetic` as `stated` / `af: none`, seed it,
   and elevate it with 7 designed nodes, an 11--21 live expectation, at most
   5 rounds, and hard cap 26.
2. Independently land `lem-prh-sharpness-row-coincidence` as
   `stated` / `af: none`, seed it, and elevate it with 6 designed nodes, a
   9--18 live expectation, at most 5 rounds, and hard cap 22.  It imports
   neither the family row nor any theorem external.
3. Only after both rows have clean validated roots, exports, oracle passes,
   registry banks, and passing gates, replace the main row's empty `deps:`
   line by the section 3 line, discard the aborted tree state, and cleanly re-seed
   the byte-frozen main contract.  Elevate it with 5 designed nodes, an 8--15
   live expectation, at most 4 rounds, and hard cap 18.  Keep its landing
   status `proved-mod-audit` / `af: seeded` until the new root is actually
   validated and externally banked.
4. Only after the main row is T0 may its existing consumer
   `cor-classical-sharpness` proceed; that consumer's contract and deps do not
   change in this factoring.

Every target uses a fresh prover and separate fresh hostile verifier(s),
bottom-up.  A cap hit is classified as `MISSING fact`, `DAG dep`, or
`genuine gap`; no cap is raised and no aborted tree is resumed across the
dependency edit.

## 7. Ranked hostile-audit attack list

1. **Frozen-contract and dependency fidelity.** Byte-compare the section 3
   contract with `argument/lemmas/lem-prh-sharpness.md`; reject any change at
   all.  Check that only the two new ids are added to its formerly empty
   `deps:` line and that `cor-classical-sharpness` remains unchanged.
2. **Strict-versus-weak bookkeeping.** Attack node 4.3.2 line by line.  The
   max-row norm supplies row errors `<=d`, never `<d`; strict positivity and
   the final contradiction must come only from the separate hypothesis
   `d<lambda` and `lambda<1/2`.
3. **Row-coincidence source-component step.** Verify that a finite
   condensation graph with an edge really yields a source component with an
   outgoing edge, that stationarity forbids it, and that no transition or
   positive-mass case is silently dropped.
4. **Stationary-probability uniqueness.** Check full support before forming
   `min q_r/p_r`, nonnegativity and stationarity of `q-cp`, and the proper
   closed-support contradiction.  Reject any silent appeal to a Markov-chain
   classification theorem.
5. **Witness arithmetic and dimensions.** Recompute both `M_lambda A_lambda`
   and all four rows of `A_lambda M_lambda`, the signs in the row-1/row-3
   difference, probability-row claims, and the exact max-row norm
   `2*lambda^2`.
6. **Quantified final clause.** Check that node 4.3.4 binds `C`, `epsilon_0`,
   and `beta`, uses `beta>1/2`, obtains a strict power-law failure for every
   stochastic idempotent at arbitrarily small defect, and therefore supports
   precisely—not more than—the frozen phrase “intrinsically sharp.”
7. **External exactness and acyclicity.** Byte-compare E1 and E2 with the two
   shard contracts, verify the literal `proofs/<id>` paths, confirm both new
   rows have empty deps, and reject any undeclared W74F/W139 theorem import.
8. **Budget realism.** Use the two aborts' 28--31-node evidence, not the old
   eight-node projection.  Treat splits beyond 21/18/15 expected live nodes
   as early brittleness warnings and enforce hard caps 26/22/18 without
   exception.
9. **Status and sequencing.** New rows land only as `stated` / `af: none`;
   the main remains `proved-mod-audit` / `af: seeded` at the deps edit; no
   main re-seed occurs until both new rows are T0, and no promotion is inferred
   from this design itself.
