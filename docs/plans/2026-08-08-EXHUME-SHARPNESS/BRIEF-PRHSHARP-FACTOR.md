# BRIEF — design the factoring of `lem-prh-sharpness` (two BALLOON aborts)

You are a fresh design worker. You built neither aborted tree and must not
trust them; re-derive the factoring from the sources.

## Situation

Two independent af elevation runs of `lem-prh-sharpness` (byte-frozen
contract, `argument/lemmas/lem-prh-sharpness.md:4`) aborted on the
brittleness cap 26: run 1 at 27 live (patch-node thrash on the
strict-vs-weak inequality bookkeeping + a challenge demanding separate
support for the final "hence ... intrinsically sharp" clause), run 2 — a
CLEAN fresh-prover re-seed — at 28 live with 18 validated and challenges
that are dependency-declaration bookkeeping plus the same final-clause
support gap (`TREE-PRHSHARP-ABORTED.md`, same directory, is run 2's tree).
Diagnosis: the honest one-tree size is ~28-31 >> the design's 8-node
projection; the row must be factored (ROW8-FACTOR precedent).

## Task

Design a factoring into AT MOST two new sub-lemma registry rows plus the
slimmed main row. The natural branch boundaries visible in both runs:

1. **The explicit family and its arithmetic** (rows of A_lambda, M_lambda;
   the 2x4/4x2 products; ||MA - I_2|| = 2*lambda^2 exactly; the
   probability-row facts) — everything about the WITNESS.
2. **The row-coincidence lemma for stochastic idempotents** (stationary
   rows; support closed under positive transitions; the finite
   source-component argument; unique stationary probability by the
   minimum-ratio argument; the conclusion that an idempotent close to AM
   has two coinciding relevant rows) — everything about a general
   stochastic idempotent F near AM.
3. The slimmed main row telescopes 1+2 into ||AM - F|| >= lambda and
   discharges the final clause ("hence the sqrt(epsilon) order in PRH is
   intrinsically sharp") EXPLICITLY — both aborted runs show this clause
   needs its own supported step: give it a precise quantified reading
   (for every C>0, beta>1/2 the bound C*epsilon^beta fails along the
   family as lambda->0 — mirror the quantifier-discharge pattern of the
   landed cor-classical-sharpness contract) and a dedicated node.

You may deviate from this split ONLY with explicit justification.

## Hard constraints (violation = REJECTED)

1. **The main row's `contract:` line stays BYTE-IDENTICAL** (it is the
   thrice-audited W139 package's byte-frozen first target and
   cor-classical-sharpness's sole dep). Only its `deps:` (+ `defs:` if
   strictly needed) may change, ADDING the new sub-lemma ids.
2. Sub-lemma contracts fully self-contained and quantified: every symbol
   bound in-contract or resolving to a declared def; explicit domains
   (0 < lambda < 1/2); the l_inf operator norm convention stated where
   used; NO strict inequality claimed where only weak follows (the run-1
   killer — state the max-row-norm consequences with the correct <=).
3. Deps: sub-lemmas may dep on each other acyclically; nothing else
   (both are elementary/finite; `def-stochastic`,
   `def-positive-approximate-retract` available; no theorem externals —
   in-tree proofs per the audited census).
4. Statuses at landing: `stated`/`af: none` for the new rows; the main
   row stays `proved-mod-audit`/`af: seeded` with contract untouched.
5. **Budgets:** per target designed nodes, honest 1.5-3x expectation,
   max rounds, hard cap; every 3x endpoint STRICTLY under its cap and
   every cap <= 26. The evidence: the monolith honestly needs ~28-31
   nodes total, so budget the pieces against that reality, not the old
   8-node projection.
6. Provenance lines cite PROOF-W74F-A-PRH.md sect-7, the W139 package
   (DESIGN-EXHUME-SHARPNESS-V2.md sect-2.1/4.1), and the two balloon
   aborts (2026-08-08, this file's directory).
7. Registry ids: kebab-case consistent with the family
   (e.g. `lem-prh-sharpness-family-arithmetic`,
   `lem-prh-sharpness-row-coincidence` — yours to finalize).

## Inputs you MUST read

- `TREE-PRHSHARP-ABORTED.md` (run 2's tree, same directory)
- `argument/lemmas/lem-prh-sharpness.md` (the byte-frozen row)
- `argument/lemmas/cor-classical-sharpness.md` (the consumer)
- `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md` sect-7
- `DESIGN-EXHUME-SHARPNESS-V2.md` sect-2.1, 4.1, 5.1, 5.3 (the census)
- `docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md` (the ratified
  factoring precedent and format)
- `definitions/def-stochastic.md`, `def-positive-approximate-retract.md`
- `CLAUDE.md` sect-1 (L4 brittleness), sect-6; FINDINGS.md 2026-08-08

## Deliverable

Write EXACTLY ONE file:
`docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-PRHSHARP-FACTOR.md`:
(a) complete land-ready text of each new sub-lemma shard; (b) the main
row's revised `deps:` line (contract byte-identical); (c) af skeleton per
target incl. the dedicated final-clause node in the main row; (d) seeding
package per target (def-adds; the main row's externals = the two new
sub-lemmas at literal proofs/<id> paths, byte-verbatim); (e) elevation
order + budgets; (f) ranked risks for the fresh hostile audit.
Head with: `Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR
PROMOTE — pending fresh hostile audit and user ratification.`

## Discipline

Write ONLY the deliverable file. No other edits, no git, no af mutations.
Final message: <=8 lines — the split, budgets, main-row deps delta.
