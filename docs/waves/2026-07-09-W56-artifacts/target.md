# W56 TARGET — decompose SL1a into a DAG of Tier-2 lemmas

## STATUS DISCIPLINE (read first, binding)

Everything you produce is AUTHOR-CLAIM strategy material, NOT rigorous, NOT a promotion
of any status. Quoted shard contracts (status: proved in argument/) are the ONLY facts
you may treat as established; cite each by id and quote the clause at the point of use.
Registry shards with status: conjecture are OPEN — never use one as a premise unless the
statement you are building is explicitly conditional and says so. Numerical/heuristic
claims are inadmissible as proof steps. Dimension-free and clone-invariant throughout:
every statement and constant must be independent of the matrix size n, and phrased on
row POINTS / geometrically distinct row vertices / coefficient-mass sums — never raw
index counts (see CONVENTIONS.md and the cloning-obstruction entries in
context/FINDINGS.md).

## THE PINNED TARGET (verbatim registry contract, argument/conj-straddling-web-exclusion.md)

> (CONJECTURE) Co-top straddling-web exclusion (SL1a): there exists universal
> delta_0 > 0 such that no exact signed idempotent P with 0 < delta(P) <= delta_0,
> nonempty visible set, and hidden top vertex v of height H > 16*tau admits a
> probability measure lambda on rows that are simultaneously rho-far from v
> (||p_f - p_v||_1 >= 4*tau) and co-top (dist_1(p_f, conv W) > H - 4*tau), with
> barycenter within 2.2*tau of p_v and with average value <= (16/13)*kappa under every
> admissible exposer at v.

Notation is the repo standard (context/l2-attack.md §0): delta = delta(P),
tau = sqrt(delta), rho = 4*tau, kappa = tau/4, D = 2 + 4*delta, W the visible set,
d_j = dist_1(p_j, conv{p_w : w in W}), H = max_j d_j.

## YOUR TASK

Author a DECOMPOSITION of SL1a into an acyclic DAG of smaller candidate lemmas
("leaves") plus a CHECKABLE ASSEMBLY proving: (all leaves) => SL1a. The objective
function (user directive of record): every leaf must be **Tier-2**, defined as:

- **Tier-2 leaf** = a single fully-quantified lemma statement (registry-contract style,
  one sentence, all constants explicit or existentially quantified with declared
  dependencies) whose proof is plausibly ROUTINE: either (a) a composition of named
  status:proved shards, (b) a self-contained finite-dimensional convexity / LP-duality /
  measure-bookkeeping argument of bounded scope, or (c) an exactly decidable structural
  dichotomy. Grade each leaf EASY or MEDIUM and justify the grade by exhibiting the
  mechanism (not just naming it).
- **NOT Tier-2**: any leaf whose statement implies SL1a (or L2-core, or the huddle
  charge) in one or two lines without introducing a genuinely smaller object — that is a
  RESTATEMENT, the known failure mode (cf. the GAP-A "(EX) restated" dead route in
  context/FINDINGS.md). Apply this test to every leaf and record the outcome.
- If, after genuine effort, ONE leaf must remain harder than MEDIUM, you may include at
  most one such leaf, flagged HARD, and it must come with (i) a strictly smaller
  configuration space than SL1a (state exactly what was removed), and (ii) its own
  further-decomposition path sketched to one more level.

## HARD CONSTRAINTS (banked walls — violating any of these invalidates the deliverable)

1. **Proposition D (context/l2-attack.md §2.4, PROVED).** No route through
   (lambda, Phi_v)-pairings alone: for the Branch-II display the lambda-average
   top-deficit is capped at t*D by an identity, and pointwise cylinder exclusion does
   NOT average up (D2). Your leaves must couple to at least one of: v's own
   coefficients a_j^+; row reproduction (exact idempotence) at rows OTHER than v — in
   particular at the web rows f themselves, which are deep (d_f > H - 4*tau) and carry
   their own hiddenness anatomy; or the always-tight / visible-set structure
   (lem-always-tight-dual-support, def-visible-set).
2. **W55 dead routes (context/2026-07-09-W55-cotop-web-coupling-strategy.md).** No
   identification or direct comparison of lambda*P with p_v. Dual conic/LP multipliers
   are NOT transition mass. No thin/thick split from a single separator moment.
   "Some web member is exposed" is ill-typed until nonvertex support, pairwise
   separation, and same-carrier vertexization are explicitly solved — if a leaf needs
   web members to be geometrically distinct row vertices, the vertexization step must
   itself be a leaf or a cited proved shard (lem-genuine-disintegration is the banked
   disintegration tool; check its exact contract).
3. **B6 scale gap (context/l2-attack.md).** Straddle antipodes are forced only at
   (7/2 - delta)*tau < rho: do NOT quantify leaves over "mutually rho-far" families —
   use barycenter-radius formulations.
4. Every constant explicit; constant bookkeeping must tie back to SL1a's verbatim
   constants (2.2*tau radius, (16/13)*kappa exposer bound, depth band H - 4*tau,
   H > 16*tau, rho = 4*tau). If a leaf strengthens or weakens a constant, the assembly
   must carry the conversion arithmetic.
5. All statements clone-invariant and dimension-free (constraint 0 of the repo).

## MANDATORY RED TESTS (run each leaf and the assembly against these; record outcomes)

- **Proposition E two-point counterweight (context/l2-attack.md §2.8):** the shallow
  counterweight escape is EXCLUDED from SL1a's hypothesis class by the co-top depth
  clause — but check no leaf of yours re-admits it (e.g. by weakening the depth band).
- **The W55 exact starvation gadget (A0 = 5, g = 5*tau, exact top-row reproduction,
  zero far positive inflow — context/W55 strategy §"Exact local refuter target"):** any
  leaf that a local gadget of this type already satisfies is NOT closable by scalar
  ledgers alone; say explicitly for each leaf whether the gadget (or its obvious
  co-top analogue) satisfies the leaf's hypotheses, and if so what global resource the
  leaf's mechanism invokes beyond the gadget's reach.
- **Clone splitting / transient-row extension:** verify each leaf's hypotheses and
  conclusion are stable under cloning rows and appending transient rows.
- **Non-vacuity / coverage:** check the decomposition against the known data anatomy
  (context/FINDINGS.md census facts, e.g. all banked instances have H^2/delta < 16;
  the W52 families in context/2026-07-09-w54-huddle-charge-decomposition-tree.md §5):
  each known family should land in an identifiable leaf/branch, none in uncovered space.

## RESOURCES (read in this order)

1. context/l2-attack.md — SL1a's birth: Theorems A/B/C, Propositions D/E, §2.6-2.7
   reductions, refuter obligations R1-R6, honest assessment. THE key prior art.
2. argument/conj-straddling-web-exclusion.md, argument/conj-shallow-counterweight-exclusion.md,
   argument/lem-l2-core-collapse.md, argument/lem-intersection-witness-confinement.md —
   the codified surface around the target.
3. context/2026-07-09-w54-huddle-charge-decomposition-tree.md — the decomposition
   TEMPLATE (structure, boundary-ownership discipline, G8 constant ordering, honest
   assessment format) AND the Branch-I side of the unification (L6 anatomy).
4. context/l6-attack.md + context/2026-07-09-W55-cotop-web-coupling-strategy.md — the
   Branch-I residual web SL1a unifies with; the E1-E5 front-end shapes (NOT L0 — treat
   as inspiration only, do not cite as premises); dead routes.
5. context/FINDINGS.md — dead-route certificates. Do not re-walk them.
6. argument/*.md — the full 140-shard registry. Any status:proved shard is quotable.
   definitions/*.md + CONVENTIONS.md — the vocabulary. No naked symbols.

## DELIVERABLE FORMAT (write INCREMENTALLY to DECOMPOSITION.md in this directory)

Follow the W54 tree template (context/2026-07-09-w54-huddle-charge-decomposition-tree.md):

1. **§1 THE PINNED TARGET** — SL1a verbatim + the standing proved reductions you will
   use everywhere (each with shard id + quoted clause).
2. **§2 THE DAG** — the decomposition: splits (each a literal Q / not-Q with declared
   boundary ownership) and/or a lemma pipeline; an ASCII tree/DAG summary; an
   exhaustiveness argument.
3. **§3 THE LEAVES** — one subsection per leaf: fully-quantified statement
   (registry-contract style), May-consume list (status:proved shards only), mechanism
   (concrete, not hand-wavy), grade (EASY/MEDIUM[/at most one HARD]), risk note
   (including what a refuter attacks and the exact-instance kill criterion), red-test
   outcomes, and the restatement-test verdict.
4. **§4 THE ASSEMBLY** — step-by-step derivation (all leaves) => SL1a with G8-style
   constant discipline (fix constants in dependency order, existential leaf constants
   read FIRST), every step citing a leaf or a proved shard.
5. **§5 COVERAGE CHECK** — against the known instance families (evidence of non-vacuity
   only; no numerical fact is a proof step).
6. **§6 HONEST ASSESSMENT** — hardest/most-likely-false leaf; what a refuter attacks
   first; which leaves are independently dispatchable to parallel provers NOW; pruned
   alternative decompositions (one line each, why dropped).

Write DECOMPOSITION.md incrementally as you work (do not hold it all for the end).
Your FINAL MESSAGE must be exactly: first line
`VERDICT: <DECOMPOSED-ALL-TIER2 | DECOMPOSED-WITH-ONE-HARD | BLOCKED — one-sentence qualifier>`,
then a one-paragraph summary of the DAG shape and leaf count.
