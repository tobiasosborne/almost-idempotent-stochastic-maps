Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE — pending fresh hostile audit and user ratification.

# DESIGN — sharpness at T0 through the direct stochastic PRH family

Date: 2026-08-08
Role: fresh design worker
Disposition: USE `lem-prh-sharpness` + ONE NEW COROLLARY; DO NOT PUT THE
3x3 DISTANCE-TO-SET COMPUTATION ON THE T0 CRITICAL PATH

## 1. Route decision

The least-churn, smallest-tree route is:

1. elevate the existing byte-frozen `lem-prh-sharpness` contract;
2. add and elevate one new row, `cor-classical-sharpness`, which sets
   \(Q_\lambda=A_\lambda M_\lambda\), uses

   \[
   Q_\lambda^2-Q_\lambda
   =A_\lambda(M_\lambda A_\lambda-I_2)M_\lambda,
   \]

   and discharges the negative exponent quantifiers explicitly; and
3. quarantine the current false `ex-hume` contract as `disproved` and discard
   its old seeded workspace. This is a retraction of the old wording, not a
   rescope to the corrected 3x3 theorem and not a T0 promotion.

This route is direct in the stochastic category. It needs neither
`lem-classical-equiv` nor `thm-rank-one`, creates no route into or out of the
validated `op-classical` root, and has one dependency edge:

```text
lem-prh-sharpness  --->  cor-classical-sharpness
     T0 first                  T0 second
```

The existing `lem-prh-sharpness` statement is literally covered by the W74F
paper proof and its separate hostile verdict. Its only substantial structural
ingredient is the finite stochastic-idempotent row-coincidence lemma, whose
proof is already self-contained in W74F. The corollary is then matrix norm
arithmetic plus one scalar choice. By contrast, a corrected `ex-hume` root
would have to prove the **lower** half of an exact distance-to-a-nonconvex-set
identity for every \(0<s<1\), as well as the signed-to-stochastic transfer.
That unnecessary higher-risk computation should not be placed on the last T0
critical path.

### Registry-surface accounting

| item | action at ratified landing | proof target in this package? |
|---|---|---|
| `lem-prh-sharpness` | contract and deps byte-frozen; remains `proved-mod-audit` / `af: none` until seeding | yes, first |
| `cor-classical-sharpness` | one new `stated` / `af: none` row | yes, second |
| `ex-hume` | retain the old false contract verbatim but retag it `disproved` / `af: none`; record the retraction and delete the stale workspace | no |
| `op-classical` | no contract or deps change; at most add one body pointer to the new corollary after it validates | no; already T0 |

Thus the mathematical T0 package is two targets and one new registry row.
No contract is rescoped. The 3x3 family may be rescued later under the same
`ex-hume` id only by a separate, user-ratified rescope with a fresh design,
fresh hostile audit, and clean re-seed.

## 2. Land-ready registry text

### 2.1 Existing first target: `lem-prh-sharpness` (byte-frozen)

This shard already has the only non-rigorous status justified by its source:
W74F section 7 proves the displayed statement and
`VERDICT-W74F-BATCH.md` section A says `VALID`, no correction.  The following
is the complete landing text; it is unchanged before seeding.

```markdown
---
id: lem-prh-sharpness
kind: lemma
contract: PRH square-root sharpness: for every 0 < lambda < 1/2 there are positive unital maps A:l-infinity(2)->l-infinity(4) and M:l-infinity(4)->l-infinity(2) with epsilon_lambda=||MA-I_2||_{infinity->infinity}=2*lambda^2 tending to 0 such that every stochastic idempotent F on l-infinity(4) satisfies ||AM-F||_{infinity->infinity} >= lambda=sqrt(epsilon_lambda/2); hence the sqrt(epsilon) order in PRH is intrinsically sharp.
defs: def-positive-approximate-retract; def-stochastic
deps:
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md §7; hostile batch verdict VERDICT-W74F-BATCH.md §A (VALID, no correction)
owner: A
workspace: proofs/lem-prh-sharpness
---

**Status.** Hostile-verified paper proof, hence `proved-mod-audit`; not
`af`-validated and not L0-rigorous.

**Transcribed family.** The encoder rows are
\[
(1,0),\quad(0,1),\quad(1-\lambda,\lambda),\quad
(\lambda,1-\lambda),
\]
and the decoder rows put masses \(1-\lambda,\lambda\) respectively on
the first and third states, and on the second and fourth states.  The
artifact computes
\[
\lVert MA-I_2\rVert_{\infty\to\infty}=2\lambda^2.
\]
Its row-coincidence argument for stochastic idempotents shows that an
idempotent within distance \(<\lambda\) would have two equal rows whose
corresponding \(AM\)-rows are \(2\lambda\) apart, a contradiction.

**Honest scope.** This is sharpness for PRH itself, not a transfer of the
independent sharpness statement for `op-classical`; the optimal universal
constant remains undetermined.
```

The later `proved` / `af: validated` flip is mechanical only after a clean
validated tree, export, external oracle, and `fr verify` pass.

### 2.2 New row: `cor-classical-sharpness`

This is the sole new mathematical shard.  Its final sentence is only a plain
mathematical negation of a uniform estimate; it does not quantify over proofs.

```markdown
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
```

### 2.3 Retraction-only text for the old `ex-hume` row

This is not a corrected 3x3 theorem.  The false contract is retained as the
object marked `disproved`, following the registry's existing refutation
practice.  That is more honest than silently replacing it with a stronger
new theorem whose difficult lower-bound direction has not been formalized.

```markdown
---
id: ex-hume
kind: obstruction
contract: The explicit 3x3 family P_s=I-u_s v_s^T (v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T) is a signed affine retraction with neg mass delta=s^2 whose distance to every stochastic idempotent is 2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta): no bound C delta^beta with beta>1/2 holds, so the exponent 1/2 in op-classical/op-npps is sharp.
defs: def-stochastic; def-signed-idempotent; def-negative-mass
deps:
status: disproved
af: none
provenance: RETRACTED 2026-08-08: the inherited contract from docs/ingest/classical-portfolio is false as quantified; docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md finding 3 gives the corrected distance-to-set candidate and removes the out-of-scope/eponymatic framing; superseded as the active sharpness carrier by cor-classical-sharpness, pending that row's independent af elevation
owner: A
workspace: proofs/ex-hume
---

**DISPROVED AS WRITTEN (2026-08-08).** A single scalar cannot be the
distance from `P_s` to every stochastic idempotent: different idempotents
have different distances (in particular, the identity is one stochastic
idempotent).  The contract also omitted the required parameter domain and
mixed the in-scope stochastic theorem with `op-npps`.

**Corrected candidate, not registered here.** The paper faithfulness audit
records the intended statement with `0<s<1`, distance to the **set** of
stochastic idempotents, row-normalized stochastic witnesses, and an explicit
for-every-idempotent lower bound.  This package neither proves nor promotes
that candidate.  Any later rescue under the stable id `ex-hume` must replace
this historical contract only after a separate design/audit/ratification
round and must initialize a fresh workspace.

**Active successor.** The in-scope T0 sharpness route is
[[cor-classical-sharpness]], via the direct stochastic 4x4 family of
[[lem-prh-sharpness]].
```

The `disproved` retag is outside Hard Constraint 3's rule for new/rescoped
claims: it is a downgrade of the unchanged false claim, not a new assertion.
It must be accompanied by a `docs/LEARNINGS.md` entry.  The old
`proofs/ex-hume/ledger/000001.json`, `000002.json`, and `meta.json` must be
deleted at ratified landing; no state from that workspace may be reused.

## 3. Verified constants and loci

| formula / constant | value used here | source locus | audit status / use |
|---|---:|---|---|
| PRH-family domain | \(0<\lambda<1/2\) | `PROOF-W74F-A-PRH.md:402-405` | literal; used by first target |
| encoder rows | \((1,0),(0,1),(1-\lambda,\lambda),(\lambda,1-\lambda)\) | `PROOF-W74F-A-PRH.md:408-417` | literal; all probability rows |
| decoder rows | \((1-\lambda)\delta_{x_1}+\lambda\delta_{y_1}\), \((1-\lambda)\delta_{x_2}+\lambda\delta_{y_2}\) | `PROOF-W74F-A-PRH.md:419-425` | literal; all probability rows |
| retract defect | \(\varepsilon_\lambda=\lVert M_\lambda A_\lambda-I_2\rVert=2\lambda^2\) | `PROOF-W74F-A-PRH.md:426-442` | literal; independently rechecked at `VERDICT-W74F-BATCH.md:78-94` |
| two selected \(AM\)-row distance | \(2\lambda\) | `PROOF-W74F-A-PRH.md:444-456` | literal |
| distance from every stochastic idempotent | \(\lVert A_\lambda M_\lambda-F\rVert\ge\lambda=\sqrt{\varepsilon_\lambda/2}\) | `PROOF-W74F-A-PRH.md:459-498` | literal; hostile recheck `VERDICT-W74F-BATCH.md:78-94` |
| stochastic witness | \(Q_\lambda=A_\lambda M_\lambda\) | product of the literal maps above | derived in the new corollary; positive unital composition |
| almost-idempotent defect | \(\lVert Q_\lambda^2-Q_\lambda\rVert\le2\lambda^2=\eta_\lambda\) | identity \(Q^2-Q=A(MA-I)M\), W74F value above | new elementary consequence; \(\lVert A\rVert=\lVert M\rVert=1\) |
| admissible-defect cutoff | \(\lambda<1/(2\sqrt2)\Rightarrow\eta_\lambda<1/4\) | scalar arithmetic | matches `def-almost-idempotent` |
| arbitrary theorem threshold | \(\lambda<\sqrt{\eta_0/2}\Rightarrow\eta_\lambda<\eta_0\) | scalar arithmetic | discharges `eta_0` explicitly |
| exponent contradiction | \(\lambda<(C2^\beta)^{-1/(2\beta-1)}\Rightarrow C\eta_\lambda^\beta<\lambda\) | scalar arithmetic, \(2\beta-1>0\) | discharges every \(C>0,\beta>1/2\) |
| corrected 3x3 distance candidate | \(\operatorname{dist}(P_s,\mathcal I_{\rm stoch})=2s-2s^2+2s^3\), \(0<s<1\) | `paper/main.tex:291-304`; `AUDIT-PAPER.md:26-45` | **not used by chosen route; not promoted** |
| corrected 3x3 stochasticization bounds | \(\lVert P_s-Q_s\rVert\le2s^2\), \(\lVert Q_s^2-Q_s\rVert\le6s^2+4s^4\) | `paper/main.tex:306-310`; `AUDIT-PAPER.md:38-40` | **not used by chosen route; fresh proof still required for any rescue** |
| corrected 3x3 lower transfer | \(\lVert Q_s-F\rVert\ge2s(1-s)^2\) for every \(F\) | `paper/main.tex:312-317`; `AUDIT-PAPER.md:41-44` | **not used by chosen route; depends on the exact distance lower direction** |

No constant from `lem-classical-equiv` is imported into either T0 target.
No exact equality is claimed for
\(\lVert Q_\lambda^2-Q_\lambda\rVert\); the upper bound is all the
`op-classical`-shaped counterexample needs.

## 4. Complete af skeletons and budgets

Every root below is byte-identical to its registry contract. Child wording
is a design and may be refined by the fresh prover without weakening the root
or importing undeclared facts.

### 4.1 `lem-prh-sharpness` — 8 designed nodes

- **1 ROOT.** The exact frozen `lem-prh-sharpness` contract in section 2.1.
- **1.1 EXPLICIT FAMILY AND RETRACT DEFECT.** For fixed
  \(0<\lambda<1/2\), define the four rows of \(A\) and two rows of \(M\)
  exactly as in W74F (7.2)-(7.3). They are probability vectors. Direct
  multiplication gives the two rows
  \((1-\lambda^2,\lambda^2)\) and
  \((\lambda^2,1-\lambda^2)\) of \(MA\), hence
  \(\lVert MA-I_2\rVert=2\lambda^2\), tending to zero with
  \(\lambda\downarrow0\).
- **1.2 ROW-COINCIDENCE LEMMA.** If \(F=(f_{ij})\) is a finite stochastic
  idempotent, \(f_{ii}>0\), and \(f_{ij}>0\), then
  \(F_{j\bullet}=F_{i\bullet}\).
  - **1.2.1 CLOSED SUPPORT AND NO INTER-COMPONENT EDGE.** Put
    \(\pi=F_{i\bullet}\) and \(S=\{r:\pi_r>0\}\). From
    \(\pi F=\pi\) and nonnegativity, \(S\) is closed. If the directed
    graph on \(S\) had an edge between distinct strongly connected
    components, a source component with an outgoing edge would contradict
    stationarity after summing \(\pi\) over that component.
  - **1.2.2 STRONG CONNECTIVITY, UNIQUENESS, AND ASSEMBLY.** Since
    \(i\to r\) for every \(r\in S\), node 1.2.1 makes the graph on \(S\)
    strongly connected. Every \(F_{r\bullet}\), \(r\in S\), is supported
    on \(S\) and stationary. For stationary probabilities \(p,q\) on this
    finite irreducible graph, \(c=\min_r q_r/p_r\) makes \(q-cp\)
    nonnegative, stationary, and zero in one coordinate; a nonzero such
    vector would normalize to a stationary probability with proper closed
    support. Thus \(p=q\), and all rows indexed by \(S\), including row
    \(j\), equal \(\pi\).
- **1.3 TWO-ROW SEPARATION.** With \(P=AM\), compute
  \(P_{x_1\bullet}=\mu_1\) and
  \(P_{y_1\bullet}=(1-\lambda)\mu_1+\lambda\mu_2\). The supports of
  \(\mu_1,\mu_2\) are disjoint, so their corresponding row distance is
  \(2\lambda\).
- **1.4 LOWER BOUND AGAINST EVERY IDEMPOTENT.** For a stochastic
  idempotent \(F\), put \(d=\lVert P-F\rVert\). If \(d<\lambda\), coordinate
  domination by row \(\ell^1\) distance gives
  \(f_{x_1x_1}>1-2\lambda>0\) and
  \(f_{x_1y_1}>0\). Node 1.2 makes the \(x_1,y_1\) rows of \(F\) equal,
  while node 1.3 and the triangle inequality give
  \(2\lambda\le2d<2\lambda\), a contradiction.
- **1.5 ROOT ASSEMBLY.** Nodes 1.1 and 1.4 supply the existential maps,
  exact retract defect, every-idempotent lower bound, and
  \(\lambda=\sqrt{\varepsilon_\lambda/2}\). Since
  \(\varepsilon_\lambda\downarrow0\), an \(o(\sqrt\varepsilon)\) uniform PRH
  conclusion is impossible.

Designed count: **8**. Honest live expectation under the repository's
1.5-3x expansion: **12-24**. Maximum rounds: **5**. Hard live-node cap:
**26** (`NODE_SOFT_CAP`). Use the routine `high/high` tier: the work is an
explicit finite proof, not a creative architecture search. A cap hit is a
stop-and-classify event; it is not permission to enlarge the cap.

### 4.2 `cor-classical-sharpness` — 6 designed nodes

- **1 ROOT.** The exact `cor-classical-sharpness` contract in section 2.2.
- **1.1 IMPORTED WITNESSES AND STOCHASTICITY.** Fix
  \(0<\lambda<1/2\), instantiate the validated
  `lem-prh-sharpness` external, and set
  \(\eta_\lambda=2\lambda^2\), \(Q_\lambda=A_\lambda M_\lambda\).
  Positive unital maps between finite `l-infinity` spaces have
  probability-vector rows and norm one; their composition is therefore
  row-stochastic.
- **1.2 DEFECT.** Associativity gives
  \(Q_\lambda^2-Q_\lambda
   =A_\lambda(M_\lambda A_\lambda-I_2)M_\lambda\).
  Submultiplicativity, the norm-one fact, and the imported equality give
  \(\lVert Q_\lambda^2-Q_\lambda\rVert\le2\lambda^2=\eta_\lambda\).
- **1.3 DISTANCE LOWER BOUND.** The imported external applies to the same
  witnesses and says that every stochastic idempotent \(F\) satisfies
  \(\lVert Q_\lambda-F\rVert\ge\lambda
   =\sqrt{\eta_\lambda/2}\).
- **1.4 SCALAR CHOICE.** Given \(C>0\), \(\eta_0>0\), and
  \(\beta>1/2\), the minimum of the three positive numbers displayed in
  section 2.2 is positive; choose \(\lambda\) strictly between zero and
  that minimum. Then
  \(0<\eta_\lambda<\min\{\eta_0,1/4\}\) and
  \(C\eta_\lambda^\beta<\lambda\).
- **1.5 NEGATIVE ASSEMBLY.** Apply nodes 1.1-1.4 with
  \(Q=Q_\lambda\) and \(\eta=\eta_\lambda\). Every stochastic idempotent
  lies farther than \(C\eta^\beta\), which negates the proposed uniform
  estimate with all quantifiers in the root's order.

Designed count: **6**. Honest live expectation: **9-18**. Maximum rounds:
**4**. Hard live-node cap: **20**. Use routine `high/high`. The tree must
not re-prove the W74F family or import `op-classical`.

## 5. Exact seeding packages and fact census

No command in this section is authorized by this design.  Execute it only
after a fresh hostile `LAND` verdict and explicit user ratification.
Before each `def-add`, check the new workspace for duplicate names; `af`
does not reject duplicate definition registrations.

### 5.1 `lem-prh-sharpness`

Initialize node 1 from the section 2.1 contract by the repository seeder:

```text
python3 scripts/seed-af-workspaces.py lem-prh-sharpness
```

Register each definition exactly once:

```text
af def-add def-positive-approximate-retract --file definitions/def-positive-approximate-retract.md -d proofs/lem-prh-sharpness
af def-add def-stochastic --file definitions/def-stochastic.md -d proofs/lem-prh-sharpness
```

There are **no theorem externals**.  W74F is a proof guide and provenance,
not an axiom.  The row-coincidence theorem is proved inside nodes 1.2-1.2.2.

### 5.2 `cor-classical-sharpness`

Do not create this workspace until `lem-prh-sharpness` has a clean validated
root, export, oracle pass, registry bank, and passing gate.  Then initialize
node 1 from the section 2.2 contract and register exactly:

```text
python3 scripts/seed-af-workspaces.py cor-classical-sharpness
af def-add def-positive-approximate-retract --file definitions/def-positive-approximate-retract.md -d proofs/cor-classical-sharpness
af def-add def-stochastic --file definitions/def-stochastic.md -d proofs/cor-classical-sharpness
af def-add def-almost-idempotent --file definitions/def-almost-idempotent.md -d proofs/cor-classical-sharpness
```

Register one external, exactly once.  Its source contains the literal
validated-workspace path and the byte-identical registry contract:

```text
name: lem-prh-sharpness
source: imports validated registry lemma proofs/lem-prh-sharpness — PRH square-root sharpness: for every 0 < lambda < 1/2 there are positive unital maps A:l-infinity(2)->l-infinity(4) and M:l-infinity(4)->l-infinity(2) with epsilon_lambda=||MA-I_2||_{infinity->infinity}=2*lambda^2 tending to 0 such that every stochastic idempotent F on l-infinity(4) satisfies ||AM-F||_{infinity->infinity} >= lambda=sqrt(epsilon_lambda/2); hence the sqrt(epsilon) order in PRH is intrinsically sharp.
```

Invocation shape:

```text
af add-external --name "lem-prh-sharpness" --source <the exact source string above> -d proofs/cor-classical-sharpness
```

No external for `lem-classical-equiv`, `lem-prh`, `op-classical`,
`thm-rank-one`, or `ex-hume` is permitted.

### 5.3 Complete textbook/definitional fact census

| # | fact used | classification | where discharged |
|---:|---|---|---|
| 1 | A positive unital map between finite `l-infinity` spaces is represented by a matrix with probability-vector rows, and conversely. | project definition | both workspaces: `def-positive-approximate-retract`, `def-stochastic` |
| 2 | The induced ∞→∞ matrix norm is the maximum row \(\ell^1\) norm. | BSc/MSc linear algebra, also stated in `def-almost-idempotent` | explicit in sharpness nodes 1.1/1.4 and corollary node 1.2 |
| 3 | Products of probability-row matrices again have probability rows. | finite matrix arithmetic | corollary node 1.1 |
| 4 | A positive unital map on finite `l-infinity` has operator norm exactly one. | elementary order/norm fact | proved in corollary node 1.1 from ∞→∞ row norm; not an external |
| 5 | Matrix multiplication is associative and \(AMAM-AM=A(MA-I)M\). | BSc linear algebra | corollary node 1.2 |
| 6 | The induced operator norm is submultiplicative. | BSc functional analysis | corollary node 1.2 |
| 7 | The displayed \(A,M,MA,AM\) rows follow by finite 2x4/4x2 multiplication. | explicit finite computation | sharpness nodes 1.1 and 1.3 |
| 8 | Disjointly supported probability vectors have \(\ell^1\) distance two. | elementary \(\ell^1\) arithmetic | sharpness node 1.3 |
| 9 | A coordinate difference is bounded by the containing row's \(\ell^1\) difference. | triangle inequality | sharpness node 1.4 |
| 10 | For a stochastic idempotent, every row is stationary: \(F_{r\bullet}F=F_{r\bullet}\). | definitional unfolding of \(F^2=F\) | sharpness node 1.2 |
| 11 | The support of a nonnegative stationary probability is closed under positive transitions. | elementary nonnegative-sum argument | sharpness node 1.2.1 |
| 12 | A finite acyclic condensation graph with an edge has a source component with an outgoing edge. | finite graph theory | proved/used explicitly in node 1.2.1 |
| 13 | A finite irreducible stochastic matrix has a unique stationary probability. | nontrivial textbook theorem, not silently imported | proved by the minimum-ratio argument in node 1.2.2 |
| 14 | The triangle inequality applied to two rows gives \(2\lambda\le2d\) when the corresponding \(F\)-rows coincide. | norm arithmetic | sharpness node 1.4 |
| 15 | \(2\lambda^2\downarrow0\) and \(\lambda=\sqrt{(2\lambda^2)/2}\) for \(\lambda>0\). | real arithmetic | sharpness node 1.5 |
| 16 | The minimum of finitely many positive reals is positive, and every positive real interval contains a smaller positive real. | ordered-field/Archimedean real arithmetic | corollary node 1.4 |
| 17 | If \(\beta>1/2\), then \(2\beta-1>0\), so positive powers preserve the strict cutoff used in section 2.2. | real exponent arithmetic | corollary node 1.4 |
| 18 | Existential witnesses exported by a validated dependency may be fixed and used consistently downstream. | first-order logic / af external discipline | corollary nodes 1.1-1.3; the single external is the provider |
| 19 | `eta<1/4` is the admissible almost-idempotent range. | project definition | `def-almost-idempotent`; corollary node 1.4 |
| 20 | Negating a proposed uniform estimate means: for each \(C,\eta_0,\beta\) there is one admissible \(Q,\eta\) for which every exact \(E\) violates it. | first-order quantifier logic | written literally in the corollary root and node 1.5 |

No finite Markov-chain classification theorem, signed/stochastic bridge, or
asymptotic big-O lemma is silently invoked.

## 6. Landing manifest

The design itself authorizes none of these mutations.  After hostile audit
and user ratification, land in the following atomic stages.

### Stage A — registry landing, no promotion

1. Add `argument/lemmas/cor-classical-sharpness.md` exactly as in section
   2.2 (`stated`, `af: none`).
2. Leave `argument/lemmas/lem-prh-sharpness.md` byte-identical at
   `proved-mod-audit`, `af: none`.
3. Replace `argument/lemmas/ex-hume.md` by the retraction-only text in
   section 2.3; remove the tracked stale `proofs/ex-hume/` workspace.  Do
   not archive or copy its ledger into a new proof workspace.
4. Append a dated `docs/LEARNINGS.md` entry quoting the old false wording,
   the “distance to every” quantifier failure, the omitted domain, the
   out-of-scope `op-npps` clause, the paper-audit correction locus, and
   `cor-classical-sharpness` as the active successor.
5. Update the `docs/ingest/README.md` re-tag row for `ex-hume`: the inherited
   contract is now explicitly retracted; the corrected 3x3 candidate remains
   non-rigorous and is not the chosen T0 route.
6. Add `cor-classical-sharpness` temporarily to `report/UNWIRED.md`.
   Keep `lem-prh-sharpness` and the now-disproved `ex-hume` entries until the
   report stage below.
7. Regenerate `argument/INDEX.md` and `argument/DAG.md`; expected registry
   count is **372** and T0 remains **196**.
8. Run `python3 scripts/argument.py --check` and
   `sh scripts/check-all.sh` before the atomic landing commit.  Record the
   independent design audit and user ratification in provenance/commit body.

### Stage B — elevate `lem-prh-sharpness`

1. Seed only after Stage A is committed and clean; apply section 5.1 exactly.
2. Run the routine `high/high` fresh-prover/separate-fresh-verifier protocol,
   at most 5 rounds, `--node-cap 26`.
3. On a clean validated root: export, run the external oracle and `fr verify`,
   mechanically flip to `proved` / `af: validated`, regenerate, gate, and
   commit.  Expected T0: **197**.

### Stage C — elevate `cor-classical-sharpness`

1. Only after Stage B is banked, seed with section 5.2 and its one
   byte-exact external.
2. Run routine `high/high`, at most 4 rounds, `--node-cap 20`.
3. On clean validation: export, oracle, `fr verify`, mechanical status flip,
   regenerate, gate, and commit.  Expected T0: **198**; registry: **372**.
4. The `op-classical` contract, deps, routes, status, and workspace remain
   untouched.  The only permitted edit to that T0 shard is one body sentence
   saying that the separate sharpness carrier is now
   `[[cor-classical-sharpness]]`; historical D1 prose may remain visibly
   historical but must not be presented as the current carrier.

### Stage D — Rule 9 documentation/report/paper closure

1. Append a compact, fully typeset sharpness subsection to
   `report/sections/02_prh.tex`, reproducing both validated rows: the 4x4
   family/row-coincidence lower bound and the direct
   \(Q^2-Q=A(MA-I)M\) corollary with the explicit \(C,\eta_0,\beta\)
   cutoff.  Update that shard's summary/keywords.
2. Add both registry/export source rows and both claim rows to
   `report/PROVENANCE.md`; remove `lem-prh-sharpness` and
   `cor-classical-sharpness` from `report/UNWIRED.md`.  Keep `ex-hume`
   whitelisted as `disproved`, unless the status ledger itself supplies its
   single honest anchor.  Regenerate `report/SHARD_CATALOG.md` by its
   documented mechanism; never hand-edit generated layers.
3. Replace every current report sentence matching “sharpness remains with
   `ex-hume`” by the T0 `cor-classical-sharpness` status.  At minimum the
   current hits are shards 00, 02, 20, 23-29, 34-38, 41-44, 46, 48-51b.
   This is a status-pointer sweep, not permission to rewrite their theorems.
4. Supersede `docs/plans/2026-08-08-top-down-proof-sketch-v50.md` with the
   next dated/versioned sketch and run
   `python3 scripts/gen-current-pointer.py`; record T0 198, registry 372,
   the direct stochastic carrier, and the retracted old `ex-hume` wording.
5. Update `PRD.md` headline/current-state text, `HANDOFF.md`, `README.md`,
   and any `FINDINGS.md` 2026-08-08 sharpness pointer.  Remove the uncitable
   eponym from active prose; use “the historical 3x3 family” if discussion
   of that deferred candidate is needed.
6. Keep `paper/main.tex` section 5 consistent with the banked contracts by
   replacing the 3x3 paragraph as the theorem's proof of sharpness with the
   direct 4x4 PRH family and quantified corollary.  Its status footnote must
   say that sharpness is af-validated, while still saying no Lean/mathlib
   proof exists.  The corrected 3x3 formulas may appear only as an explicitly
   non-T0 historical remark; omitting them is smaller and safer.
7. Refresh generated campaign statistics (`--extract` then `--check`) and
   any generated report DAG/definition layers whose inputs changed.  Run
   `cd report && make`, then the complete `sh scripts/check-all.sh` gate and
   rerun generators/checks for idempotence.
8. Log the wave in `fr`, update/close the sharpness bead, append
   `docs/worklog.md`, complete the repository session-close protocol, and
   push.  These are future landing duties; this design worker performs none
   of them.

## 7. Elevation order and stop rules

1. Fresh hostile audit of this file, explicitly attacking every item in
   section 8.
2. User ratification.
3. Stage A registry/retraction landing.
4. `lem-prh-sharpness` seed → prove → separate fresh verify → oracle →
   bank.
5. `cor-classical-sharpness` seed with the now-T0 external → prove →
   separate fresh verify → oracle → bank.
6. Rule 9 documentation/report/paper closure and final gates.

Stop rather than improvising if:

- the first tree exceeds 26 live nodes (classify missing fact vs bad shape);
- the corollary cannot consume exactly the witnesses exported by the
  byte-frozen first contract;
- any proposed fix requires changing the `lem-prh-sharpness` contract;
- anyone attempts to use, resume, or amend `proofs/ex-hume`; or
- anyone proposes to promote the corrected 3x3 distance formula without its
  own fresh lower-bound proof.

## 8. Ranked risks for the fresh hostile audit

1. **FATAL if wrong — quantifier dischargeability of the negative
   statement.** The verifier must negate the proposed uniform theorem
   literally and check the order `for every C, eta_0, beta` → `there exist
   eta,Q` → `for every E`. It must verify the strict scalar cutoff and
   that the chosen `eta` is an admissible upper bound for the actual defect.
2. **HIGH — witness identity across the dependency boundary.** The \(A,M\)
   used to define \(Q=AM\), to bound \(MA-I\), and to invoke the
   every-idempotent lower bound must be the same existential witnesses from
   `lem-prh-sharpness`; repeated notation alone is not binder unification.
3. **HIGH — row-coincidence proof.** Attack closure of the stationary
   support, the source-SCC argument, positivity of the minimum ratio, and the
   inference that every relevant row is stationary and supported on the
   same irreducible class. A hidden appeal to a full classification theorem
   is a seeding failure.
4. **HIGH — direct stochastic defect.** Check types and order in
   \(A(MA-I_2)M\), norm-one of both positive unital maps, and that the proof
   claims only `<= 2*lambda^2`, not an unearned equality.
5. **HIGH — supersession honesty.** The old `ex-hume` contract is false and
   may not remain `proved-mod-audit`, be described as the T0 carrier, or be
   silently replaced without a historical record. The `disproved` row,
   `docs/LEARNINGS.md`, ingest row, PRD/sketch/report/paper pointers, and
   provenance must tell the same story.
6. **HIGH — workspace re-seed discipline.** The current
   `proofs/ex-hume` root is byte-bound to the old contract and has only
   pending assumption nodes. It must be deleted at the retraction landing
   and never resumed. A later corrected `ex-hume` rescope must start from a
   genuinely fresh `af init`; this package does not perform that re-seed.
7. **HIGH but off the chosen path — distance-to-set lower-bound direction.**
   The corrected 3x3 equality requires both an upper witness and a lower
   bound against **all** stochastic idempotents. The paper audit corrects
   the quantifier but is not an af proof. No triangle inequality from one
   convenient idempotent proves the infimum's lower direction. This is the
   principal reason the 3x3 rescope is deferred.
8. **HIGH but off the chosen path — the \(Q_s\) defect constant.** Any future
   3x3 rescue must independently verify
   \(\lVert Q_s^2-Q_s\rVert\le6s^2+4s^4\) for the actual row-positive-part
   normalization, with \(0<s<1\), and then verify the subtraction leading to
   \(2s(1-s)^2\). Those constants are not imported into this package.
9. **MEDIUM — strict versus weak inequalities.** The lower family gives
   `>= lambda`; the scalar cutoff must give the strict
   `C*eta^beta < lambda`. Reversing either comparison would fail to refute
   the uniform bound.
10. **MEDIUM — report/status drift.** The repository currently has many
    stock sentences naming `ex-hume` as the remaining sharpness carrier.
    A partial sweep would leave a false headline even if both af trees pass.
11. **MEDIUM — tree expansion.** The row-coincidence proof is the only
    plausible balloon source. Its designed eight-node tree has 3x headroom
    to 24 under the cap 26. If fresh workers begin deriving general Markov
    chain classification, stop and return them to nodes 1.2.1-1.2.2.

## 9. Expected end state after ratified execution

- `op-classical`: unchanged `proved` / `af: validated` upper-bound root.
- `lem-prh-sharpness`: `proved` / `af: validated`.
- `cor-classical-sharpness`: `proved` / `af: validated`, the active
  op-classical-facing sharpness carrier.
- `ex-hume`: `disproved` / `af: none`, historical false wording retained
  honestly and stale workspace absent.
- Registry: 372 rows. T0: 198.
- Sharp exponent \(1/2\): T0 by a direct row-stochastic 4x4 family; no
  signed bridge, no dependence on the upper-bound proof, and no claim of a
  Lean/mathlib formalization.
