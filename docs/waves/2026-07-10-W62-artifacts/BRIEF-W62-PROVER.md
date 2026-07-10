# W62 prover — the L5 routine batch: R0, R1, R2, R3

You are a fresh, independent PROVER. Your workspace is this directory: the full
registry snapshot (`argument/`, `definitions/`) + context docs (`context/`). Work
entirely inside it. Deliverable: `PROOFS-W62-L5-BATCH.md`.

## Task

Prove, as four self-contained paper proofs, the four routine/routine-hard nodes of
`context/DECOMPOSITION-W62-L5.md` (read its §1 in FULL first — the shared
clone-quotient notation block defines every object; read each node's (a)-(e)):

1. **R0 `conj-w62-mass-barycenter-dualization`** — the mass-to-one-point
   conversion: sup_{y in Y_v} sum_{j in A} (P_vj)_+ * z_y(j) = S * Z_v(q_A).
2. **R1 `conj-w62-top-face-primal-ray-formula`** — the LP-dual outward
   visible-ray certificate formula for Z_v(q). Include the Lambda = 0 edge case
   and attainment. Use `lem-top-support-dual-face` as the description of Y_v.
3. **R2 `conj-w62-positive-flow-foldback`** — the one-step aggregate foldback
   from P^2 = P with the explicit error 2*delta*(1+delta)*M. Prove it for
   arbitrary full-fiber submeasures m <= P_v^+ and arbitrary g: fibers -> [0, M].
4. **R3 `conj-w62-universal-exterior-payer`** — consume the af-validated
   `lem-hx-forced-exterior-coupling` (T0; read its shard for the exact statement,
   including the strict ||p_Q - c||_1 > 1/2 boundary and the vacuity threshold)
   pairwise over the charged fibers, aggregate with the submeasure, fold back with
   YOUR OWN R2, and derive first the exact intermediate inequality
   (1+S)*V >= S*(tau/(1+2delta) - 2delta) - 2delta*(1+delta), then the clean
   corollary P_v^+(E_c) >= tau*S/8 for every c in K(P) under an explicit ceiling
   delta_E (derive the ceiling honestly; the artifact suggests the shape
   min{1/16, (c_m/32)^2} — verify or correct it).

## Rules

- SIGNED picture; exact signed idempotents; no stochastic crossing.
- Every quantity full-fiber / affine / l1 (clone-invariant). No raw-index path
  products, no class counts, no dimension constants, no selectors.
- Cite banked registry results by exact id and use their contracts as stated (do
  NOT re-prove them; do NOT strengthen them silently). Available and relevant:
  `lem-top-support-dual-face`, `lem-affine-barycenter-identity`, `lem-mass-split`,
  `lem-top-deficit-price`, `lem-negpart-subadditive`,
  `lem-hx-transverse-moment-identity`, `lem-hx-signed-variation-ledger`,
  `lem-hx-financing-floor` (NOTE: its contract requires A > 0 — the W61 corrected
  form), `lem-hx-forced-exterior-coupling`, `lem-delta-zero-endpoint`.
- One single minimal contract per node (af-elevation-shaped): restate the contract
  you actually prove at the top of each section VERBATIM-quotable; if you must
  deviate from the artifact's pinned contract (a wording defect, a needed boundary
  hypothesis), FLAG the deviation loudly in a "CONTRACT DELTA" line and justify it.
- Fixtures (include the checks in the proofs file):
  - R0: a partially selected clone fiber (split one atom into two equal rows and
    select half) — S, q_A, and both sides of the identity must be unchanged.
  - R1: the one-dimensional test C_W = {0}, p_v = 1; and a two-point visible hull.
  - R2: g = indicator and g = z_y; the delta = 0 case must reduce to exact
    stochastic flow conservation.
  - R3: verify the vacuity/threshold arithmetic at the boundary
    ||p_Q - p_v||_1 = 4*tau, and check the constants against the W61 dyadic
    leak-financer shape (context: the W61 wave doc is in the sketch; the financer
    pays a LOCAL demand — show where the for-all-centers floor blocks it or note
    honestly if it does not).
- Honest status discipline: these are your paper proofs — they will face a fresh
  hostile batched verifier. Every estimate explicit; every sign split named; no
  "clearly".

## Output format

`PROOFS-W62-L5-BATCH.md` with sections §R0-§R3, each: CONTRACT (verbatim statement
proved) / PROOF (complete, self-contained modulo cited registry ids) / FIXTURES
(worked) / CONTRACT DELTA (if any) / TOOLS (ids consumed). Final answer: one
paragraph — which nodes you consider fully proved, which have contract deltas, and
the single weakest step across the batch.
