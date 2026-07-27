# BRIEF — factor `lem-stage1-approximate-group-laws` into registry sub-lemmas (balloon repair, small, surgical)

You are a fresh, independent design mathematician. Design ONLY; no registry
mutation; everything you produce is escalated for verbatim landing after a
fresh hostile check.

## The problem

The af elevation of `argument/lemmas/lem-stage1-approximate-group-laws.md`
(contract = the audited `DESIGN-S1-POLAR-v6.md` §3 row 6, landed verbatim;
design budget 10/3) ABORTED [BALLOON] at 60 live nodes > cap 52. Read the
retained ledger at `proofs/lem-stage1-approximate-group-laws/ledger/` —
especially the challenge texts named in the abort classification
(ch-48d353ace6a9dc20, ch-bcb1423b02741b55, ch-dae10d5f420f8290,
ch-fe5a3e5c6156f90e, ch-6afca6cb47447c4e, ch-fd51d1ba33561893) and the run
log tail. Diagnosis: (i) three logically separable blocks (polar-domain
MEMBERSHIP of U bold-dot V and U^dagger with right-invertibility; the two
CLOSENESS estimates; the three associator/inverse DEFECT telescopes) were
forced into one tree with heavy cross-sibling dependencies; (ii) several
strict inequalities are false at the allowed endpoint epsilon_r = 0 (the
same endpoint family already repaired at T0 in F2/F3); (iii) the prover's
aggregation found C_grp = 600 workable — constants live in proof bodies,
never in contracts (over-banking guard).

The T0 inputs available as deps: `lem-stage1-polar-retraction` (the C^1
polar diffeomorphism + sandwich), `lem-stage1-polar-coherence-naturality`,
`lem-stage1-unitary-graph-control`, `lem-stage1-rectified-cstar-control`,
`lem-stage1-quantitative-inverse-function` (all af-validated; read their
contract lines). The row-6 contract text itself MUST NOT change — it is the
hostile-endorsed audited text; you are factoring its PROOF, not amending
its statement.

## Your deliverables — write `docs/plans/2026-07-27-S1-GROUP-FACTORING-design/DESIGN-S1-GROUP-FACTORING.md`

1. **Two or three atomic sub-lemma contracts** (one-line each,
   registry-ready flattened ASCII in the house style of the landed Stage-1
   rows), factoring the row-6 proof along its natural seams. Candidate
   split (YOU decide and justify; fewer, cleaner rows preferred):
   (a) `lem-stage1-group-domain-membership` — under the row-6 guards,
   U bold-dot V and U^dagger lie in S_delta (with the right-inverse
   condition), so u_delta applies;
   (b) `lem-stage1-group-closeness` — the two closeness estimates
   ||mu(U,V) - U bold-dot V|| and ||sigma(U) - U^dagger|| <= C*epsilon_r;
   (c) optionally a defect-telescope row, OR leave the three defect bounds
   plus basepoint identities in the parent. Requirements: every estimate
   must hold at the endpoint epsilon_r = 0 (use <= throughout; no strict
   inequality whose two sides vanish); constants stay in proof bodies;
   quantifier structure and guards inherited verbatim from the row-6
   contract; each sub-lemma's deps drawn only from the T0 rows above;
   the parent row-6 deps line becomes the sub-lemmas (+ retained T0 rows
   as needed). State the exact prospective `defs:`/`deps:` lines per shard.
2. **Node budgets** per sub-lemma and for the re-seeded parent (target:
   each tree <= 15 nodes; parent <= 12). Dependency/scoping discipline in
   the style of DESIGN-F2-TYPING §2.4: no cross-sibling imports, every
   inequality endpoint-safe, each node names its dependencies explicitly.
3. **Consumer re-check** (one paragraph): rows 8 (inversion-derivative
   control), 11 (smooth operations), 13e (group transport), and the
   downstream quotient rows consume row 6's CONTRACT, which is unchanged —
   confirm nothing else needs touching.

## Hard constraints

Contract of row 6 unchanged; no new hypotheses; no guessed constants in
contracts; NOT-IN-LOCAL-REFS discipline; sub-lemma provenance = derivation
from the named T0 rows + TeX 845-878 loci already recorded on the row-6
shard; write ONLY inside `docs/plans/2026-07-27-S1-GROUP-FACTORING-design/`.
