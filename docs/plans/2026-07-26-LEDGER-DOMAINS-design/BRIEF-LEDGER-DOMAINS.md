# BRIEF — GAP-LEDGER-DOMAINS design job (de-risk front #3)

You are a fresh, independent, HOSTILE design mathematician. Your target is
**GAP-LEDGER-DOMAINS**: fourteen Route-F relative-ledger results whose
`proved-mod-audit` status was WITHDRAWN because their proofs asserted
inequalities on domains stronger than the verified ledger — the single
linearization radius η_A was silently reused as a global radius, when each
row needs its own dependency-produced local radius. The mechanisms were
verified; the domains were not. Your job: design the closed local-domain DAG
that repairs this — or find that a required radius cannot be derived. Either
outcome is a SUCCESS; do not guess radii to make the DAG close.

RISK CALIBRATION: the underlying estimates (Kitaev arXiv:2405.02434 +
the campaign K-ledger) are presumed sound; the realistic failure modes are
(i) a radius that cannot be produced from the named dependencies without
strengthening them, (ii) a circular or empty finite-minimum aggregation,
(iii) — ROUTE-LEVEL ALARM if found — a radius that is NOT dimension-free.

## The fourteen reserved ids (v4.1 §2.6 — currently uncontracted, DO NOT SHARD OR SEED)

`lem-routef-raw-factor-norms`, `lem-routef-raw-factor-units`,
`lem-routef-raw-factor-identities`, `lem-routef-raw-product-estimate`,
`lem-routef-delta-prime-closeness`, `lem-routef-delta-normalization-closeness`,
`lem-routef-delta-phi-product`, `lem-routef-upsilon-prime-closeness`,
`lem-routef-upsilon-normalization-closeness`, `lem-routef-delta-upsilon-telescope`,
`lem-routef-multiplicative-telescope`, `lem-routef-upsilon-delta-telescope`,
`lem-routef-k-finiteness`, `lem-routef-threshold-minimum`.
Also blocked consumers to reconnect: `lem-routef-degree-two-estimate`,
`lem-routef-degree-three-estimate` (v4.1 §2.5, DESIGN-ONLY), and ultimately
the `lem-routef-k-ledger` parent (DO NOT REWIRE OR SEED — your design may
PROPOSE its wiring but must keep that guard explicit).

## Context (read these, in this order)

1. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   — §2.5, §2.6, §3.4 (`lem-routef-k-ledger`), risk rows R24–R28, R36–R38;
   also VERDICT-FUDW-DECOMP-V3.md §2.1 (the BLOCKER that withdrew the rows).
2. `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md` (the
   original K-ledger proofs whose mechanisms were verified) and
   `VERDICT-W74F-G-KLEDGER.md` (the hostile verdict identifying the exact
   domain defects — treat its findings as binding).
3. The validated/mod-audit upstream rows (read the landed shards in
   `argument/lemmas/`): `lem-kitaev-almost-idemp-audit`,
   `lem-routef-functional-calculus-closeness` (C_θ = 12(√2−1), η ≤ 1/8),
   `lem-routef-ai-defect-linearization` (C_A, η_A — the ONLY legitimate use
   of η_A), `lem-maincb-reset-constant-ledger` (the closed constant package
   every threshold aggregation must import — R27/R36).
4. `refs/kitaev-2405.02434/approximate_algebras.tex` ~lines 2780–2830 (the
   degree estimates) as ground truth for the mechanism steps.

## Deliverable — write `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS.md`

1. **The local-domain DAG**: for each of the fourteen ids, a closed
   replacement contract in the v4.1 §2.5 table style: proposed id (reusing
   the reserved id is permitted ONLY with its dependency-produced local
   radius stated in the contract), one-line `contract:` with the EXPLICIT
   local radius as a closed formula in the upstream constants (e.g. the
   normalization guards (C_T+C_Δ′)η ≤ 1/2 and (C_T+C_Υ′)η ≤ 1/2 — R25),
   defs, deps (existing registry ids or earlier rows of your table — NO
   forward or dangling references), provenance loci, projected af node count
   (≤12 / depth ≤3). Derivation order must be serial and well-founded, with
   `lem-routef-k-finiteness` and `lem-routef-threshold-minimum` LAST;
   `lem-routef-threshold-minimum` must import `lem-maincb-reset-constant-ledger`
   plus every named guard producer (R27).
2. **Per-row radius derivation plan**: exactly how the local radius is
   produced from the named dependencies — which constant comes from which
   shard, and the arithmetic that closes it. If a radius CANNOT be derived
   without strengthening an upstream contract, mark the row **GAP** and state
   precisely what is missing (this is a success — never guess).
3. **The finite-minimum audit** (R27): show the threshold aggregation is a
   finite minimum over NAMED, produced constants, non-circular, and nonempty.
4. **Dimension-freeness audit**: every radius and constant independent of
   dimension, amplification, block data, stage index — verify per row; any
   leak is a ROUTE-LEVEL ALARM, flag it LOUDLY.
5. **Reconnection map**: the corrected dependency lists for
   `lem-routef-degree-two-estimate` and `lem-routef-degree-three-estimate`,
   and the PROPOSED (not enacted) complete parent wiring for
   `lem-routef-k-ledger` per v4.1 §3.4, guard intact.

## Hard constraints

- DESIGN ONLY. Write ONLY inside `docs/plans/2026-07-26-LEDGER-DOMAINS-design/`.
  Do NOT touch `definitions/`, `argument/`, `proofs/`, or any other path.
- No status promotion; nothing you write is rigorous; the fourteen ids stay
  reservations until a hostile audit passes and the user authorizes landing.
- v4.1 discipline: no guessed radii; no compound contracts; η_A appears ONLY
  in AI-defect linearization (R24); every future aggregation imports the
  reset-constant package.
- Cite loci exactly (file + line ranges). If a needed fact is NOT in the
  local sources listed above, say NOT IN LOCAL REFS and stop on that point —
  do not paraphrase literature from memory.
