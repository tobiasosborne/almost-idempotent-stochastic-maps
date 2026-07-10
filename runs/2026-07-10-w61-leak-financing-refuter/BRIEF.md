# W61 decider B — LEAK-FINANCING REFUTER at the N5(ii)/N6 constants (L3, exact arithmetic)

You are a fresh, independent worker. Your workspace is this directory: a snapshot of
the registry (`argument/`, `definitions/`) plus context docs (`context/`). Everything
you produce stays INSIDE this directory. This is an L3 (numerical/constructive
evidence) job: **nothing you produce is a proof**, and your report must say so.

## Background

`context/DECOMPOSITION-W60-FABLE.md` proposes two creative-hard confinement
conjectures N5/N6 (fat near/far cell exclusion). Their priced likeliest death is THE
CONSTANTS FIGHT: the proved engine (`argument/lemmas/lem-hx-financing-floor.md`,
instantiated as `argument/lemmas/lem-hx-forced-exterior-coupling.md`) demands that a
separated row pair (r,s) at l1-distance l jointly finance roughly

    demand(l) ~ (1 - A*l) / Lambda  - nu_r - nu_s,   ball form: ~ l/(2+4*delta) - 2*delta

positive coefficient mass on high-lever (far-from-center) fiber sets, while the
BANKED confinement ledgers only cap leaks at scale ~3*tau/4:

- z-leak at v: positive v-mass at fibers with z >= 4*tau is <= delta*(2+4delta)/(4tau)
  (via `lem-top-deficit-price`),
- h-leak at v: <= nu_v/(4tau) (h-reproduction via `lem-harmonic-affine-bridge` + sign
  split),
- and the freight rows x and carriers u have NO banked confinement at all;
  aggregation runs through row f whose corner ledger
  (`lem-sl1a-corner-ledger`) leaves <= 1/2 + nu_f available outside the corner.

N5(ii) (huddle-internal band tau/4 < l <= 8*tau) and N6 (far cell) claim this
financing is IMPOSSIBLE for selected-corner data below a universal delta ceiling.
Read the N5/N6 sections (contracts, mechanisms, priced deaths) in full.

## Your job: try to REFUTE the confinement constants

Search for an exact configuration — an exact signed idempotent P (P^2 = P exactly,
rational arithmetic) with a row pair in the N5(ii)/N6 geometry — that FINANCES the
engine demand entirely through leaks the banked ledgers PERMIT, i.e. a configuration
where:

1. delta(P) <= 2^-16 (or a family with delta -> 0),
2. there is a row pair (or row/row-hull-point pair) at separation l in the band
   tau/4 < l <= 8*tau (near variant) and/or the far variant geometry (carrier u
   rho-far from v, co-top, hidden — see N6(b)),
3. the positive mass demanded by lem-hx-financing-floor on the high-lever fibers is
   actually present, and it sits ENTIRELY in fiber sets where every applicable
   banked ledger (z-leak, h-leak, corner ledger at f, mass-split, top-deficit-price,
   zero-face capacity kills, hiddenness dual witness — check each shard you invoke)
   is satisfied with slack.

Such an instance shows the N5/N6 close CANNOT follow from the currently banked
ledgers at the stated constants — the conjectures would need restating (new budgets
or different constants) BEFORE any creative prover burns on them. That is the
decision this search feeds.

Calibrate against the banked frontier families first: `context/w29-README.md`
(witness-coupling frontier) and `context/w35-README.md` (absorption threshold) —
their instance shapes are the natural starting stock; then deform (deepen leak
fibers, thin the corner, push mass to z ~ Omega(1) fibers "priced by NO banked
ledger at better than demand scale", per N6's detection-gap paragraph).

You do NOT need a full selected-corner witness to be decisive: a configuration
matching the pair geometry + ledger-slack financing pattern already moves the
decision (say honestly which selected-corner clauses you did/did not verify).

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational construction + ledger-accounting
   script. For each candidate: verify P^2 = P exactly; compute delta, tau, the pair
   separation l, the engine demand (exact, from the lem-hx-financing-floor contract
   with your chosen (psi, N, A, Lambda) instantiation), and the exact per-ledger
   accounting (each banked bound: its exact value vs its cap). Every check asserts
   an exact invariant.
2. `certificates.json` — the exact matrices and the full ledger table for any
   financing instance (or the best near-misses).
3. `REPORT.md` — the decider verdict:
   - **FINANCING INSTANCE FOUND**: the constants fight is real at the stated
     budgets; name which ledger(s) had slack and by how much. => N5/N6 need
     restating before creative spend.
   - **SEARCH FAILED**: for every shape attempted, name the exact banked
     inequality that killed the financing (which ledger ran out first, with the
     exact margin). This is the standard non-proof green light — say so.
   - **PARTIAL**: honestly scoped.
   Record shapes tried, parameter ranges, dead ends.

## Discipline

- Read `context/FINDINGS.md` dead routes BEFORE constructing. All masses/distances
  on the row-point quotient (full fibers), never raw indices (cloning obstruction).
- The engine floor is UNIVERSAL and proved — do not "refute" it; you are testing
  whether its demand can be met inside the banked leak allowances (a statement about
  the LEDGER SET, not about the floor).
- Signed picture throughout; no stochastic crossing.
- Work entirely inside this directory. Final answer: a one-paragraph summary of
  REPORT.md's verdict.
