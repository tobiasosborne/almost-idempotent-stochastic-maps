Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE — pending fresh hostile re-audit and user ratification.

# DESIGN V2 — sharpness at T0 through the direct stochastic PRH family

Date: 2026-08-08
Role: fresh v2 design worker (neither v1 author nor hostile auditor)
Disposition: USE `lem-prh-sharpness` + ONE NEW COROLLARY; RETRACT THE
MALFORMED `ex-hume` CLAIM PRECISELY; DO NOT PUT THE 3x3 DISTANCE-TO-SET
COMPUTATION ON THE T0 CRITICAL PATH

## Repair of audit finding 1

The linker vocabulary is `disproved`, not `refuted`
(`argument/README.md`, shard schema).  At ratified landing `ex-hume` therefore
becomes `status: disproved`, `af: none`.

The malformed historical contract is not retained as the canonical statement.
It is replaced by a fully bound formulation of the false proposition: the
domain is `0<s<1`; the claimed equality is quantified over every 3x3 stochastic
idempotent; the asymptotic variable is `s->0`; `C` and `beta` are quantified;
and the out-of-scope `op-npps` clause is dropped.  The old contract is quoted
byte-verbatim in the shard body as historical evidence.  The body then refutes
the precise proposition with the stochastic idempotent `I_3` and the exact
calculation required in audit finding 3.  This contract replacement is a
landed-contract change and is explicitly gated on fresh hostile re-audit and
user ratification.

This is a retraction-only rescope.  It does not register, prove, seed, or
promote the corrected distance-to-set candidate.

## Repair of audit finding 2

The landing manifest in part (f) is closed over the audit's complete binding
enumeration.  It contains **50 citation-locus actions**: `AGENTS.md` and
`CLAUDE.md` separately; the existing and new `FINDINGS.md` loci separately;
both `RESEARCH_NOTES.md` and both `refs/manifest/SOURCES.md` loci; both
`thm-rank-one` loci; all five `op-classical` provenance/body loci; four ingest
loci; the 26 audit-cleared report shards; paper section 5; `INDEX.md`;
`lem-signed-carre-du-champ`; and `lem-routef-f0-assembly`.

The `thm-rank-one` contract loses its false “sharp family” clause.  That is a
second landed-contract change, so its exact replacement is separately flagged
for user ratification.  The validated `op-classical` contract, deps, routes,
status, af tree, and workspace remain untouched; only the exact provenance/body
pointers listed in part (f) change after the new carrier validates.  Its D1
record remains visibly historical.

The report sweep is carried forward over exactly sections 00, 02, 20, 23--29,
34--38, 41--44, 46, 48, 49, 49b, 50, 51, and 51b.  Historical plans, audits,
waves, `.frontier`, `.beads`, `docs/worklog.md`, and numerical run bundles remain
historical.  The current numerical `INDEX.md` anchor and the two registry
fixture/negative references receive explicit matrix-family-only annotations;
they are not treated as imports of the disproved contract.

## Repair of audit finding 3

For every fixed `0<s<1`, put

\[
a=1-s+s^2,
\qquad
v_s=(1,-1+s,-s),
\qquad
u_s=(a,-s,0)^{\mathsf T}.
\]

Then `v_s^T 1=0` and `v_s^T u_s=1`, so
`P_s=I_3-u_s v_s^T` satisfies `P_s 1=1` and `P_s^2=P_s`.  Its only
negative entry is `(P_s)_{23}=-s^2`, hence its maximal row negative mass
is exactly `delta_s=s^2`.  But `I_3` is a stochastic idempotent and

\[
\lVert P_s-I_3\rVert_{\infty\to\infty}
=\lVert u_sv_s^{\mathsf T}\rVert_{\infty\to\infty}
=2a,
\]

whereas the claimed common value is
`2s-2s^2+2s^3=2sa`.  Their difference is

\[
2a-2sa=2(1-s)a>0.
\]

Thus the literal per-idempotent equality in the repaired proposition is false.
This computation is included verbatim in substance in the proposed
`ex-hume` shard, the proposed `docs/LEARNINGS.md` entry, and the proposed dated
`FINDINGS.md` record.  No uncited attribution is used in active prose.

### Cleared-text byte-diff declaration

- **Changed because findings 1--3 force it:** the route/accounting prose for
  `ex-hume`; the complete retraction shard; the manifest; the supersession and
  documentation-drift risks; and the expected-end-state wording.
- **Changed and separately ratification-gated because finding 2 forces it:**
  the `thm-rank-one` contract and its body pointer.
- **Unchanged verbatim from v1:** the complete `lem-prh-sharpness` landing text;
  the complete `cor-classical-sharpness` landing text; the verified-constants
  table; both af skeletons and their 12--24/cap-26 and 9--18/cap-20 budgets;
  both seeding packages; the 20-item fact census; Stage B and Stage C items
  1--3; the paper section-5 action; the elevation order; the explicit
  stale-workspace deletion sentence after the `ex-hume` shard; and the
  no-resume stop rule.  Stage C item 4 changes only because finding 2 requires
  the complete pointer repair.
- **No cleared mathematical text changed:** the audit-cleared 4x4 arithmetic,
  stochastic defect computation, lower bound, scalar cutoff, corollary
  quantifiers, dependency edge, or seeding external.

## (a) Route decision and justification

The least-churn, smallest-tree route is:

1. elevate the existing byte-frozen `lem-prh-sharpness` contract;
2. add and elevate one new row, `cor-classical-sharpness`, which sets
   \(Q_\lambda=A_\lambda M_\lambda\), uses

   \[
   Q_\lambda^2-Q_\lambda
   =A_\lambda(M_\lambda A_\lambda-I_2)M_\lambda,
   \]

   and discharges the negative exponent quantifiers explicitly; and
3. quarantine the false `ex-hume` claim as `disproved`, replacing its malformed
   contract by the fully quantified false proposition in part (b), and discard
   its old seeded workspace.  This is a precise retraction, not a rescope to the
   corrected 3x3 theorem and not a T0 promotion.

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
| `ex-hume` | replace the malformed contract with the precise false proposition; retag `disproved` / `af: none`; record the exact counterexample; delete the stale workspace | no |
| `thm-rank-one` | remove the false “sharp family” clause from its nonvalidated contract and annotate its body; **landed-contract change requiring user ratification** | no |
| `op-classical` | contract/deps/routes/status/workspace untouched; after validation repair only the exact provenance/body pointers in part (f) | no; already T0 |

Thus the mathematical T0 package is two targets and one new registry row.
There are two non-T0 contract changes made solely for honest retraction and
consumer hygiene: `ex-hume` and `thm-rank-one`.  Both require user
ratification.  The 3x3 family may be rescued later under a separately designed
and ratified corrected contract with a fresh hostile audit and clean re-seed.

## (b) Complete land-ready registry text

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

### Retracted row: `ex-hume` (changed to repair findings 1 and 3)

This shard registers and disproves the precise historical proposition.  It
does not assert the corrected distance-to-set candidate.

```markdown
---
id: ex-hume
kind: obstruction
contract: Disproved historical 3x3-family proposition: for every real s with 0<s<1, set v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T, P_s=I_3-u_s v_s^T, and delta_s=s^2; then P_s is a signed affine retraction with maximal row negative mass delta_s and, for every 3x3 stochastic idempotent E, ||P_s-E||_{infinity->infinity}=2s-2s^2+2s^3; as s->0, this claimed common value is 2*sqrt(delta_s)+O(delta_s); moreover, for every C>0 and beta>1/2 there exists a real s with 0<s<1 such that every 3x3 stochastic idempotent E satisfies ||P_s-E||_{infinity->infinity}>C*delta_s^beta.
defs: def-stochastic; def-signed-idempotent; def-negative-mass
deps:
status: disproved
af: none
provenance: RETRACTED 2026-08-08: the inherited contract quoted below is false as quantified; exact counterexample P_s versus I_3 recorded in this body, docs/LEARNINGS.md, and FINDINGS.md; docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md finding 3 records a corrected distance-to-set candidate that remains non-rigorous; active sharpness successor cor-classical-sharpness is separate and subject to its own independent af elevation
owner: A
workspace: proofs/ex-hume
---

**DISPROVED HISTORICAL PROPOSITION (2026-08-08).** The former canonical
contract was, byte-verbatim:

> The explicit 3x3 family P_s=I-u_s v_s^T (v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T) is a signed affine retraction with neg mass delta=s^2 whose distance to every stochastic idempotent is 2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta): no bound C delta^beta with beta>1/2 holds, so the exponent 1/2 in op-classical/op-npps is sharp.

That wording omitted the parameter domain and mathematical quantifiers,
left the limiting variable in `O(delta)` unstated, mixed in the out-of-scope
`op-npps`, and asserted one common distance to every stochastic idempotent.
The contract above makes the false proposition precise before disproving it.

**Exact counterexample to the per-idempotent equality.** Fix `0<s<1` and
write `a=1-s+s^2`.  The displayed vectors satisfy
`v_s^T 1=0` and `v_s^T u_s=1`; hence `P_s 1=1` and `P_s^2=P_s`.
The only negative entry of `P_s` is `(P_s)_{23}=-s^2`, so its maximal
row negative mass is exactly `delta_s=s^2`.  But `I_3` is a stochastic
idempotent and
\[
\lVert P_s-I_3\rVert_{\infty\to\infty}
=\lVert u_sv_s^{\mathsf T}\rVert_{\infty\to\infty}
=2a,
\]
while the claimed common value is
`2s-2s^2+2s^3=2sa`.  Their difference is
`2(1-s)a>0`.  Therefore the canonical proposition is false.

**Corrected candidate, not registered here.** The paper faithfulness audit
records the intended statement with `0<s<1`, distance to the **set** of
stochastic idempotents, row-normalized stochastic witnesses, and an explicit
for-every-idempotent lower bound.  This package neither proves nor promotes
that candidate.  Any later rescue of the historical 3x3 family must use a
separate design/audit/ratification round and initialize a fresh workspace.

**Active successor.** The in-scope T0 sharpness route is
[[cor-classical-sharpness]], via the direct stochastic 4x4 family of
[[lem-prh-sharpness]].
```

The old `proofs/ex-hume/ledger/000001.json`, `000002.json`, and `meta.json`
must be deleted at ratified landing; no state from that workspace may be
reused.

### Corrected `thm-rank-one` consumer text (finding-2 contract change)

This nonvalidated shard's contract change is mandatory consumer hygiene and
requires explicit user ratification.  Replace only its contract and body with:

```markdown
contract: There are universal delta_0,C>0 such that every rank-one signed affine retraction P=I-u v^T (sum_j v_j=0, v^T u=1) with neg mass <= delta <= delta_0 is within ||P-E||_{inf->inf} <= C sqrt(delta) of a stochastic idempotent E.
```

```markdown
Rank-one retractions are O(sqrt delta)-stable.  The historical 3x3 matrix
family recorded in [[ex-hume]] is a rank-one instance; this is a
matrix-family reference only and imports no claim from the disproved
`ex-hume` contract.
```

Its `defs`, `deps`, `status`, `af`, provenance, owner, and workspace remain
unchanged.  In particular this edit does not promote `thm-rank-one`.

## (c) 3. Verified constants and loci

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

## (d) 4. Complete af skeletons and budgets

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

## (e) 5. Exact seeding packages and fact census

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

## (f) 6. Closed landing manifest

The design itself authorizes none of these mutations.  After hostile audit
and user ratification, land in the following atomic stages.

### Binding 50-locus citation census

The count treats each listed line group or required new record as one locus;
the 26 report shards are counted individually.

The audit enumeration is carried forward verbatim:

> - `AGENTS.md:105` + `CLAUDE.md:105` (edit BOTH, keep byte-identical),
>   `CONVENTIONS.md:57`, `FINDINGS.md:36-37` + the new dated record,
>   `RESEARCH_NOTES.md:97,145`, `refs/manifest/SOURCES.md:25,84`.
> - `thm-rank-one` (nonvalidated): its CONTRACT at line 4 and body line
>   14 call ex-hume a sharp family — design the exact corrected contract
>   text (this is a landed-contract change: flag for ratification).
> - `op-classical` (VALIDATED): contract/deps/routes UNTOUCHABLE; design
>   the exact body/provenance pointer repairs for lines 10, 20-22,
>   28-29, 33-35 (sharpness pointer must now go to the new corollary;
>   line 38 stays visibly historical).
> - `docs/ingest/README.md:114,119,297` +
>   `docs/ingest/OVERVIEW.md:98` (honest re-tag annotations; ingest text
>   itself stays quoted history).
> - The report sweep of v1 (sections list) carries forward; the paper §5
>   action per audit finding 7.
> - INDEX.md:27, lem-signed-carre-du-champ fixture, and the
>   lem-routef-f0-assembly negative statement: add the explicit
>   "historical matrix-family reference, not an import of the false
>   contract" clarifications the audit says keep them truthful.

| # | required locus | exact landing disposition |
|---:|---|---|
| 1 | `AGENTS.md:105` | Replace the current `ex-hume` carrier sentence with: `The \`√η\` exponent in \`op-classical\` is nonetheless **sharp**, with the af-validated carrier \`cor-classical-sharpness\`; the former \`ex-hume\` contract is disproved historical record.` |
| 2 | `CLAUDE.md:105` | Apply the byte-identical replacement from locus 1, then verify `cmp -s AGENTS.md CLAUDE.md`. |
| 3 | `CONVENTIONS.md:57` | Replace the carrier clause with: `**Sharp exponent:** distance-to-idempotent scales like \`√δ\` (equivalently \`√η\`); op-classical-facing sharpness is certified at T0 by \`cor-classical-sharpness\`, while \`ex-hume\` is a disproved historical contract.` |
| 4 | `FINDINGS.md:36-37` | Replace the active carrier with: `The \`√η\`/\`√δ\` distance exponent is nonetheless **sharp**; the op-classical-facing T0 carrier is \`cor-classical-sharpness\`. The former \`ex-hume\` contract is disproved and is not a sharpness certificate.` |
| 5 | new dated `FINDINGS.md` record | Append the exact “Dated FINDINGS record” block below, including the `I_3` counterexample computation and the active-successor boundary. |
| 6 | `RESEARCH_NOTES.md:97` | Replace `+ ex-hume sharpness` with `+ op-classical sharpness now carried at T0 by cor-classical-sharpness; the former ex-hume contract is disproved historical record`. |
| 7 | `RESEARCH_NOTES.md:145` | Replace the cross-check with: `**Sharpness cross-check (historical only):** SBD Remark 5.4's 3-state family versus the historical 3x3 matrix family recorded in the disproved \`ex-hume\` shard — compare mechanisms only; do not import the false contract.` |
| 8 | `refs/manifest/SOURCES.md:25` | In the Salzmann--Bergh--Datta role cell, replace the `ex-hume` cross-check with `the √η-sharpness external anchor supporting cor-classical-sharpness; any comparison with the historical 3x3 matrix family in ex-hume is matrix-family-only and imports no claim from that disproved contract`. |
| 9 | `refs/manifest/SOURCES.md:84` | Replace the current `ex-hume` anchor clause with: `(ii) the external √η-sharpness anchor supporting \`cor-classical-sharpness\`; the historical 3x3 matrix family recorded in \`ex-hume\` may be compared only as a matrix-family reference, not as an import of its disproved contract.` |
| 10 | `argument/lemmas/thm-rank-one.md:4` | Replace the contract byte-exactly by the corrected contract in part (b). **User ratification required.** |
| 11 | `argument/lemmas/thm-rank-one.md:14` | Replace the body byte-exactly by the corrected body in part (b), making the matrix-family-only boundary explicit. |
| 12 | `argument/lemmas/op-classical.md:10` | Keep the validated contract/deps/routes untouched.  In provenance replace `(D1 sharpness split executed W80; sharpness carried by ex-hume)` with `(D1 sharpness split executed W80; sharpness now carried at T0 by cor-classical-sharpness; the former ex-hume contract was retracted as disproved on 2026-08-08)`. |
| 13 | `argument/lemmas/op-classical.md:20-22` | Replace the sharpness sentence with: `NOTE the honest boundary: this discharges the UPPER-BOUND contract (the D1 split, W80); sharpness of the exponent 1/2 is the separate af-validated corollary [[cor-classical-sharpness]], and af-validation is this repo's L0 rung (b), not a Lean/mathlib proof.` |
| 14 | `argument/lemmas/op-classical.md:28-29` | Replace the pointer with: `Sharpness of the exponent 1/2 is carried separately at T0 by [[cor-classical-sharpness]].` |
| 15 | `argument/lemmas/op-classical.md:33-35` | Replace the current-carrier paragraph with: `**Contract split (USER-RATIFIED 2026-07-27, decision D1 option A of \`docs/plans/2026-07-27-W78-ratification-package.md\`):** the contract line is the upper stability bound ONLY. The sharpness of the exponent 1/2 (no \`C·eta^beta\` with \`beta > 1/2\` can hold universally) is a SEPARATE statement now carried at T0 by [[cor-classical-sharpness]] and is NOT part of this contract; a route that proves the upper bound discharges this theorem.` |
| 16 | `argument/lemmas/op-classical.md:38` | Preserve the D1 history visibly by adding immediately before the future-wiring sentence: `Historical note: at the W80 split this separate statement was assigned to [[ex-hume]]; that pointer is superseded because the old ex-hume contract is now disproved.` |
| 17 | `docs/ingest/README.md:114` | Replace the `thm-rank-one` row's tail by: `the historical 3x3 matrix family recorded in \`ex-hume\` is a rank-one instance, but this is a matrix-family reference only and imports no sharpness claim from that disproved contract.` Keep the inherited theorem `proved-mod-audit`. |
| 18 | `docs/ingest/README.md:119` | Retag the row as historical/retracted: quote the inherited “distance to every” wording as ingest history, state registry `disproved, af:none`, cite the exact `I_3` counterexample, and state that the corrected distance-to-set candidate remains non-rigorous and off the T0 route. |
| 19 | `docs/ingest/README.md:297` | Replace the parenthetical with: `(The \`√η\` exponent in \`op-classical\` is nonetheless sharp at T0 via \`cor-classical-sharpness\`; the former \`ex-hume\` contract is disproved historical record.)` |
| 20 | `docs/ingest/OVERVIEW.md:98` | Replace the certificate assertion with: `The inherited portfolio reports the naive O(delta) full-matrix strengthening as refuted by its historical 3x3 matrix family; the former registry contract \`ex-hume\` is now disproved and is not a certificate for that statement. The active op-classical sharpness carrier is the separate direct-stochastic \`cor-classical-sharpness\`.` |
| 21 | `report/sections/00_overview.tex` | Replace the bespoke “sharpness not claimed / ex-hume proved-mod-audit” boundary by the validated `cor-classical-sharpness` carrier; retain the no-Lean boundary. |
| 22 | `report/sections/02_prh.tex` | Add the fully typeset two-row sharpness subsection specified in Stage D and replace its stale `ex-hume` pointer by `cor-classical-sharpness`. |
| 23 | `report/sections/20_hcb3_diagonal_unit.tex` | Replace only the stale stock carrier sentence by the validated `cor-classical-sharpness` status. |
| 24 | `report/sections/23_hcb3_diagonal_lower_modulus.tex` | Same stock carrier replacement. |
| 25 | `report/sections/24_hcb3_diagonal_inverse.tex` | Same stock carrier replacement. |
| 26 | `report/sections/25_hcb3_offdiagonal_inverse.tex` | Same stock carrier replacement. |
| 27 | `report/sections/26_hcb4_canonical_gram.tex` | Same stock carrier replacement. |
| 28 | `report/sections/27_hcb4_canonical_closeness.tex` | Same stock carrier replacement. |
| 29 | `report/sections/28_hcb4_canonical_inverse.tex` | Same stock carrier replacement. |
| 30 | `report/sections/29_hcb.tex` | Same stock carrier replacement. |
| 31 | `report/sections/34_extcb_four_corner_merge.tex` | Same stock carrier replacement. |
| 32 | `report/sections/35_extcb.tex` | Same stock carrier replacement. |
| 33 | `report/sections/36_routef_prh_finish.tex` | Same stock carrier replacement. |
| 34 | `report/sections/37_stage1_quantitative_ift.tex` | Same stock carrier replacement. |
| 35 | `report/sections/38_stage1_exact_unit.tex` | Same stock carrier replacement. |
| 36 | `report/sections/41_status_outlook.tex` | Replace the bespoke “sharpness remains open / ex-hume proved-mod-audit” status by the validated `cor-classical-sharpness` carrier; retain the no-Lean boundary and the disproved historical record. |
| 37 | `report/sections/42_routef_f0_seam.tex` | Replace only the stale stock carrier sentence by the validated `cor-classical-sharpness` status. |
| 38 | `report/sections/43_routef_ai_ledger.tex` | Same stock carrier replacement. |
| 39 | `report/sections/44_routef_f2_f3.tex` | Same stock carrier replacement. |
| 40 | `report/sections/46_stage1_polar_retraction.tex` | Same stock carrier replacement. |
| 41 | `report/sections/48_stage1_smooth_polar.tex` | Same stock carrier replacement. |
| 42 | `report/sections/49_stage1_smooth_upgrades.tex` | Same stock carrier replacement. |
| 43 | `report/sections/49b_stage1_explicit_bridges.tex` | Same stock carrier replacement. |
| 44 | `report/sections/50_stage1_polar_transports.tex` | Same stock carrier replacement. |
| 45 | `report/sections/51_stage1_polar_transports_ii.tex` | Same stock carrier replacement. |
| 46 | `report/sections/51b_stage1_ledger_keystone.tex` | Same stock carrier replacement. |
| 47 | `paper/main.tex` section 5 | Apply the audit-cleared paper action in Stage D verbatim: replace the 3x3 proof of sharpness by the direct 4x4 PRH family and quantified corollary; update the footnote to af-validated sharpness but no Lean proof; omit the old formulas or keep them only as explicitly non-T0 historical candidate. |
| 48 | `INDEX.md:27` | In the E1 pilot row, annotate `the stochasticized historical 3x3 matrix-family anchor s=1/16 (matrix-family reference only, not an import of the disproved ex-hume contract)`; preserve every numerical status and scope qualifier. |
| 49 | `argument/lemmas/lem-signed-carre-du-champ.md:9` | In provenance replace `ex-hume` by `the historical 3x3 matrix family recorded in ex-hume (fixture reference only, not an import of its disproved contract)`; contract/deps/status remain untouched. |
| 50 | `argument/lemmas/lem-routef-f0-assembly.md:29-31` | Keep the negative statement and add: `The name ex-hume here is a historical matrix-family pointer only; this row has no dependency on it and imports no part of its disproved contract.` Contract/deps/status remain untouched. |

The report set in loci 21--46 is exactly the audit-cleared enumeration:
sections 00, 02, 20, 23--29, 34--38, 41--44, 46, 48, 49, 49b, 50, 51,
and 51b.  No historical wave, plan, audit, numerical run bundle, frontier log,
bead log, or worklog prose is silently rewritten.

### Exact retraction records required by loci 5 and the landing discipline

#### Dated `docs/LEARNINGS.md` entry

```markdown
## 2026-08-08 — `ex-hume`: “distance to every stochastic idempotent equals one common value” is false

- **Claimed:** `ex-hume` carried `proved-mod-audit` / `af: seeded` with the historical contract: “The explicit 3x3 family P_s=I-u_s v_s^T (v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T) is a signed affine retraction with neg mass delta=s^2 whose distance to every stochastic idempotent is 2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta): no bound C delta^beta with beta>1/2 holds, so the exponent 1/2 in op-classical/op-npps is sharp.”
- **Why wrong:** for `0<s<1`, put `a=1-s+s^2`.  Although `v_s^T 1=0`, `v_s^T u_s=1`, and the only negative entry of `P_s` is `(P_s)_{23}=-s^2`, the stochastic idempotent `I_3` satisfies `||P_s-I_3||_{infinity->infinity}=||u_s v_s^T||_{infinity->infinity}=2a`, while the claimed common value is `2sa`; the difference is `2(1-s)a>0`.  Thus the per-idempotent equality is false.  The old contract also omitted `0<s<1`, left its quantifiers and asymptotic variable unstated, and mixed in the out-of-scope `op-npps`.
- **Caught by:** the fresh hostile audit of `DESIGN-EXHUME-SHARPNESS.md`, finding 3, after the paper faithfulness audit had already corrected “distance to every” to a distance-to-set candidate.
- **Resolution:** replace the malformed contract by the fully quantified false proposition solely so it can be honestly marked `disproved`; set `af: none`; delete and never resume the stale old-contract workspace; record the corrected 3x3 distance-to-set formula only as a non-rigorous candidate; and use `cor-classical-sharpness`, via the direct stochastic 4x4 PRH family, as the separately elevated active carrier.  All active consumers are covered by the 50-locus manifest in `DESIGN-EXHUME-SHARPNESS-V2.md`.
```

#### Dated `FINDINGS.md` record

```markdown
## 2026-08-08 — `ex-hume` retraction: historical matrix family survives; the old sharpness contract does not

- **Retracted proposition.** The former `ex-hume` contract claimed, without binding all variables, that the explicit `P_s=I_3-u_sv_s^T` family had one common distance `2s-2s^2+2s^3` to every stochastic idempotent.  The canonical retraction now states that historical proposition with `0<s<1`, a per-idempotent universal quantifier, `s->0` as the asymptotic variable, quantified `C,beta`, and no `op-npps` clause, and marks it `disproved`.
- **Exact death certificate.** Put `a=1-s+s^2`.  Then `v_s^T 1=0`, `v_s^T u_s=1`, `P_s 1=1`, `P_s^2=P_s`, and the only negative entry is `(P_s)_{23}=-s^2`.  But `I_3` is a stochastic idempotent and `||P_s-I_3||_{infinity->infinity}=||u_sv_s^T||_{infinity->infinity}=2a`, whereas the claimed common value is `2sa`; the positive difference is `2(1-s)a`.  Therefore “distance to every ... equals” is false.
- **Boundary.** The corrected distance-to-the-set formula in `paper/main.tex` section 5 remains a non-rigorous historical candidate and is not seeded here.  References to the old 3x3 matrices in numerical fixtures or negative “not consumed” statements are matrix-family references only, never imports of the disproved contract.  The active op-classical-facing sharpness carrier is `cor-classical-sharpness`, built directly from the 4x4 `lem-prh-sharpness` witnesses.
```

### Exact `op-classical` pointer-only repair block

After `cor-classical-sharpness` validates, the following is the complete
authorized change surface in the T0 shard.  The contract, `defs`, `deps`,
`routes`, `status`, `af`, `owner`, workspace, and af ledger remain byte-identical.

```markdown
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex); ROOT REWIRE 2026-08-08 (user-ratified): OR-routes block per DESIGN-F0-ASSEMBLY.md sect-3 / AUDIT-F0-ASSEMBLY.md sect-3 (Route F via the T0 lem-routef-f0-assembly; the legacy signed-geometry route retained as an independent alternative); the "(OPEN)" contract marker removed as part of the ratified discharge package (D1 sharpness split executed W80; sharpness now carried at T0 by cor-classical-sharpness; the former ex-hume contract was retracted as disproved on 2026-08-08)
```

```markdown
**DISCHARGED AT T0 (2026-08-08).** Root af tree: 5/5 nodes validated/clean
(fresh codex prover, separate fresh hostile verifiers per node); external
oracle `af-op-classical` + `fr verify` PASS; mechanical flip. The theorem
is af-validated end-to-end through Route F; explicit witnesses
eta_0 = eta_K and C = K+4*sqrt(2K) from the strengthened
[[lem-routef-k-ledger]]. NOTE the honest boundary: this discharges the
UPPER-BOUND contract (the D1 split, W80); sharpness of the exponent 1/2
is the separate af-validated corollary [[cor-classical-sharpness]], and
af-validation is this repo's L0 rung (b), not a Lean/mathlib proof.

The **north star** (`PRD.md`). Two independent routes: Route F via
[[lem-routef-f0-assembly]] (the T0 Kitaev-factorization assembly; eta_0 = eta_K,
C = K+4*sqrt(2K)), and the legacy signed-geometry route via
[[thm-classical-factorization]] + [[prop-approx-simplex]]. Sharpness of the
exponent 1/2 is carried separately at T0 by [[cor-classical-sharpness]].

**Contract split (USER-RATIFIED 2026-07-27, decision D1 option A of
`docs/plans/2026-07-27-W78-ratification-package.md`):** the contract line is
the upper stability bound ONLY. The sharpness of the exponent 1/2 (no
`C·eta^beta` with `beta > 1/2` can hold universally) is a SEPARATE statement
now carried at T0 by [[cor-classical-sharpness]] and is NOT part of this
contract; a route that proves the upper bound discharges this theorem.
Rationale: the Route-F assembly (`AUDIT-F0-ASSEMBLY.md` §§0.2, 4) proves only
the upper bound, and a compound contract would force a sharpness carrier into
every route's dependency closure. Historical note: at the W80 split this
separate statement was assigned to [[ex-hume]]; that pointer is superseded
because the old `ex-hume` contract is now disproved. The future Route-F wiring
(applied only at the LAST step of the ratified campaign, package §5 step 6) is
`routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]`.
```

### Stage A — registry landing and retraction, no promotion

1. Add `argument/lemmas/cor-classical-sharpness.md` exactly as in part (b)
   (`stated`, `af: none`).
2. Leave `argument/lemmas/lem-prh-sharpness.md` byte-identical at
   `proved-mod-audit`, `af: none`.
3. Replace `argument/lemmas/ex-hume.md` by the precise retraction text in
   part (b), with `disproved` / `af: none`; remove the tracked stale
   `proofs/ex-hume/` workspace.  Do not archive or copy its ledger into a new
   proof workspace.
4. Apply the exact `thm-rank-one` contract/body corrections in part (b).
   This and the `ex-hume` contract replacement require explicit user
   ratification; neither is a promotion.
5. Append the exact dated `docs/LEARNINGS.md` and `FINDINGS.md` blocks above.
6. Apply citation-census loci 1--20 and 48--50 that describe the retraction.
   `AGENTS.md` and `CLAUDE.md` must remain byte-identical.  When a line refers
   to the eventual T0 successor, word it prospectively until Stage C banks or
   defer that active-carrier half to Stage D; never call the new row T0 early.
7. Add `cor-classical-sharpness` temporarily to `report/UNWIRED.md`.
   Keep `lem-prh-sharpness` and the now-disproved `ex-hume` entries until the
   report stage below.
8. Regenerate `argument/INDEX.md` and `argument/DAG.md`; expected registry
   count is **372** and T0 remains **196**.
9. Run `python3 scripts/argument.py --check` and
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
   untouched.  Apply only the complete provenance/body pointer block above;
   its D1 assignment to `ex-hume` remains visibly marked as historical.

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
3. Apply report census loci 21--46 exactly.  This is a status-pointer sweep,
   not permission to rewrite their theorems.
4. Supersede `docs/plans/2026-08-08-top-down-proof-sketch-v50.md` with the
   next dated/versioned sketch and run
   `python3 scripts/gen-current-pointer.py`; record T0 198, registry 372,
   the direct stochastic carrier, and the retracted old `ex-hume` wording.
5. Update `PRD.md` headline/current-state text, `HANDOFF.md`, and `README.md`
   to the same boundary: upper bound and sharpness T0, no Lean proof;
   `cor-classical-sharpness` active; `ex-hume` disproved historical record.
   Remove the uncitable eponym from active prose; use “the historical 3x3
   family” if discussion of that deferred candidate is needed.
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
8. Re-run `rg` over the active repository for `ex-hume`, `Hume`, and stale
   sharpness-status phrases.  Every survivor must be one of: the exact
   historical quote; an explicitly historical matrix-family reference; the
   `disproved` status record; or an explicit non-import/negative statement.
9. Log the wave in `fr`, update/close the sharpness bead, append
   `docs/worklog.md`, complete the repository session-close protocol, and
   push.  These are future landing duties; this design worker performs none
   of them.

### Mechanical closure outside the 50 citation loci

- Regenerate `argument/INDEX.md`, `argument/DAG.md`, the report DAG and
  definition layers if affected, campaign statistics, and
  `report/SHARD_CATALOG.md`; do not hand-edit generated files.
- Reconcile `report/PROVENANCE.md` and `report/UNWIRED.md` exactly as Stage D
  states.
- Update `PRD.md`, `HANDOFF.md`, `README.md`, and the superseding live proof
  sketch in lockstep with the banked statuses.
- The expected registry count is 372; T0 stays 196 at Stage A, becomes 197
  after Stage B, and becomes 198 after Stage C.

## (g) 7. Elevation order and stop rules

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

## (h) 8. Ranked risks for the fresh hostile re-audit

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
5. **HIGH — precise retraction and supersession honesty.** Attack every
   binder in the new `ex-hume` contract, the byte-verbatim old-contract
   quote, the `I_3` computation, and the `disproved` vocabulary.  The
   corrected distance-to-set candidate must remain off the T0 path.  The
   active-consumer sweep must cover all 50 counted loci, and the
   `thm-rank-one` contract change must be user-ratified.
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
10. **MEDIUM — closed-manifest status timing.** Stage A may record a
    prospective successor but must not call it T0 before Stage C.  After
    Stage C, every active current-status pointer must name
    `cor-classical-sharpness`; every surviving `ex-hume` reference must be
    explicitly historical, `disproved`, or a matrix-family-only/non-import
    reference.  `AGENTS.md` and `CLAUDE.md` must remain byte-identical.
11. **MEDIUM — tree expansion.** The row-coincidence proof is the only
    plausible balloon source. Its designed eight-node tree has 3x headroom
    to 24 under the cap 26. If fresh workers begin deriving general Markov
    chain classification, stop and return them to nodes 1.2.1-1.2.2.

## 9. Expected end state after ratified execution

- `op-classical`: unchanged `proved` / `af: validated` upper-bound root;
  pointer-only body/provenance repair complete.
- `lem-prh-sharpness`: `proved` / `af: validated`.
- `cor-classical-sharpness`: `proved` / `af: validated`, the active
  op-classical-facing sharpness carrier.
- `ex-hume`: precise historical proposition `disproved` / `af: none`, old
  wording quoted byte-verbatim, exact `I_3` counterexample recorded, stale
  workspace absent.
- `thm-rank-one`: still `proved-mod-audit` / `af: none`, with its
  user-ratified contract no longer calling the historical family sharp.
- Registry: 372 rows. T0: 198. Citation manifest: 50/50 loci reconciled.
- Sharp exponent \(1/2\): T0 by a direct row-stochastic 4x4 family; no
  signed bridge, no dependence on the upper-bound proof, and no claim of a
  Lean/mathlib formalization.
