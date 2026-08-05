# BRIEF — hostile audit of DESIGN-KITAEV-PAIR-ELEVATION

Date: 2026-08-05. You are a FRESH hostile auditor with NO prior context; you did
not write the design. **Finding a real gap is a BIG SUCCESS.**

## Target and inputs

- TARGET: `docs/plans/2026-08-05-KITAEV-PAIR-ELEVATION/DESIGN-KITAEV-PAIR-ELEVATION.md`
- `BRIEF-KITAEV-PAIR-ELEVATION.md` (same dir): the commissioning constraints
  (FROZEN contracts; repair-first order; design-only).
- The two shards: `argument/lemmas/lem-kitaev-diagonal-repair.md`,
  `argument/lemmas/cor-kitaev-diagonal-cpization.md`.
- The underlying paper-proofs:
  `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-B-DIAGONAL.md` (§§2-3, §4.1)
  and the batch verdict VERDICT-W74F-BATCH.md §B.
- Ground truth: `refs/kitaev-2405.02434/approximate_algebras.tex` (the false
  printed diagonal at :1254 and :2780-2783; verify every quoted external
  byte-verbatim yourself with grep -F).

## Mandatory attacks (explicit verdict line each)

1. Root freeze: both skeleton roots byte-equal the shard contracts (verify
   independently).
2. Refutation clause: does the repair skeleton genuinely DISCHARGE the "the
   printed formula is false (already for B = C (+) C)" clause — an explicit
   counterexample node with the printed formula imported byte-verbatim as a GT
   external, evaluated concretely? Attack any hand-waving.
3. Construction clause: does the skeleton prove EVERY property of D —
   existence with unitary W_t, q_t >= 0 summing to 1, centrality ZD = DZ for
   ALL Z in B (not just generators), pi(D) = I_B, projective norm EXACTLY 1,
   and block-count/dimension independence? Attack the projective-norm
   computation (the ||W_t^dagger||*||W_t|| = 1 factorization) and the
   phase-balance argument for arbitrary M_{d_r} blocks.
4. CP-ization: is complete positivity genuinely dischargeable from exact
   centrality WITHOUT multiplicativity of tilde-Delta, per the skeleton's
   argument (Choi/positive-sum structure)? Does the skeleton use the
   involution-preservation hypothesis where needed and nowhere else? Is the
   UCP Phi hypothesis used only where claimed?
5. Seeding packages: def lists sufficient and duplicate-free (incl. the
   design's L2 finding that the corollary defs: line needs def-ucp-map —
   verify that claim and whether anything else is missing);
   externals exact (names, loci, verbatim text — byte-check each);
   repair-first banking order enforced.
6. Budgets: realistic against this session's record (fresh builds ran 1.5-3x
   naive projections); caps below the repo ceiling 26.
7. The design's own ranked risks: dispose each explicitly.
8. Fresh under-specification hunt: what is STILL missing?

## Output

`docs/plans/2026-08-05-KITAEV-PAIR-ELEVATION/AUDIT-KITAEV-PAIR-ELEVATION.md`:
verdict LAND / LAND-WITH-EXACT-CORRECTIONS / DESIGN-REJECTED; numbered
findings (severity, locus, exact correction); disposition of attacks 1-8.
Change NOTHING outside that one new file. Nothing you write promotes anything.
