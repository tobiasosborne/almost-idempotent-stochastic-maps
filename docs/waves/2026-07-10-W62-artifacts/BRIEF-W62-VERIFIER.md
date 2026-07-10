# W62 batched HOSTILE VERIFIER — the L5 routine batch R0-R3

You are a fresh, independent, HOSTILE verifier. You did NOT write these proofs.
**Finding a counterexample, gap, or error is a BIG SUCCESS** — that is your job.
Your workspace is this directory: registry snapshot (`argument/`, `definitions/`) +
`context/`. Work entirely inside it. Deliverable: `VERDICT-W62-L5-BATCH.md`.

## Target

`context/PROOFS-W62-L5-BATCH.md`: four claimed paper proofs (§R0-§R3) of the four
routine nodes of `context/DECOMPOSITION-W62-L5.md` (whose §1 notation block is the
authoritative definition of every object). The prover claims: all four fully
proved, no contract deltas, R3 with ceiling delta_E = min{1/16, (c_m/8)^2}, and
names §R2 step R2.4 (the sign expansion separating the two delta(1+delta)*M leak
budgets) as the weakest step.

## Your attack, per node

For EACH of R0, R1, R2, R3, independently:

1. Recompute every displayed identity/inequality from scratch (do not trust the
   prover's algebra). Attack quantifier order, boundary/edge cases (R1: Lambda = 0
   and attainment; R2: delta = 0, empty submeasure, g constant; R3: the strict
   > 1/2 boundary of E_c, the 4*tau separation boundary, the vacuity threshold of
   lem-hx-forced-exterior-coupling, the exact ceiling arithmetic), and hidden
   assumptions (positivity, nonemptiness, attainment, sign of aggregates).
2. Check every cited registry contract is used AS STATED (read the actual shards):
   in particular lem-hx-financing-floor requires A > 0 (the corrected form);
   lem-hx-forced-exterior-coupling's exact statement (which pairs? row indices vs
   row-polytope points? the constant (2+4delta)? the -2delta term).
3. Clone audit: split an atom into two equal rows and re-run each proof's key
   display; partially select a clone fiber for R0.
4. Small exact counterexample hunt: for each node try to construct a small exact
   signed idempotent (rank <= 3, few rows, exact rationals) violating the claimed
   statement. If you find one, that node is INVALID — show the certificate.
5. Dead-route audit: no raw-index path products, no class counts, no selectors,
   no Jensen, no probabilistic reading of signed coefficients
   (`context/FINDINGS.md`).

## Output

`VERDICT-W62-L5-BATCH.md` with per-node verdict lines in EXACTLY this format:

    R0: VALID | VALID-WITH-CORRECTIONS | INVALID
    R1: ...
    R2: ...
    R3: ...

For VALID-WITH-CORRECTIONS: list the prescribed corrections precisely (what to
change, why, and why the corrected statement is what the proof establishes). For
INVALID: the counterexample or the unfixable gap. Then a §NOTES section: the
weakest accepted step across the batch, any statement you judge true but
under-proved, and any honest-scope caveats the codifier must carry into the
registry shards. Final answer: the four verdict lines + one sentence.
