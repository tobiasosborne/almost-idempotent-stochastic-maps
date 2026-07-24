# BRIEF — F2/F3 bridge extraction: close the two uncontracted Route F glue steps (aism-0163)

You are a FRESH PROVER (codex, independent context). Your job: extract, state as
closed hypothesis blocks, and FULLY PROVE the two Route F bridge steps that every
prior review found audit-valid as prose but never stated as contracts:

- **F2 (positive-unital compression):** from the Route F factorization data,
  construct the positive unital maps `A: ℓ∞(k) → ℓ∞(n)` and
  `M: ℓ∞(n) → ℓ∞(k)` that `lem-routef-prh-finish` consumes.
- **F3 (retract-defect):** from the preceding UCP estimates, derive the
  quantitative retract bound `‖MA − I‖_{∞→∞} ≤ 3Kη/(1−3Kη)` (or the exact
  bound the material actually supports — if it differs, say so LOUDLY; do not
  force the target constant).

This is proof work, not transcription: you may derive, but every derivation must
be grounded in the permitted material below — you may NOT import unproved claims
from the Kitaev source (its printed proofs are invalid; only its definitions are
sound) and may NOT assume any quarantined/GAP row.

## Read first

1. `CLAUDE.md` (Laws L0–L5) — binding; honest statuses; dimension-free constants.
2. `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` — where F0/F2/F3
   were audited VALID as prose; your primary extraction source.
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP-V3.md`
   §2.6 context + the two GAP reservations (`gap-routef-f2-…`, `gap-routef-f3-…`)
   — what a "closed hypothesis block" must mean here.
4. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v3.md`
   — the `lem-routef-prh-finish` row (§2.5) whose hypotheses your F2/F3 outputs
   must exactly feed, and the quarantined ledger context.
5. `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md` §§3–5 (the
   K/η_K evaluation your bounds must be compatible with) and
   `PROOF-W74F-B-DIAGONAL.md` / `AUDIT-W74F-D-ALMOSTIDEMP.md` in
   `docs/plans/2026-07-23-W74F-artifacts/` as needed for the CP-ization and
   almost-idempotent interfaces.
6. `argument/lemmas/lem-prh.md` (the af-validated consumer) and
   `definitions/def-positive-approximate-retract.md`.

## Requirements on the outputs

- TWO single minimal contracts (one per step), each a one-line statement with a
  fully quantified closed hypothesis block — no "hence", no reference to "the
  preceding estimates", every input named. They must compose: F2's conclusion +
  F3's conclusion must literally supply `lem-routef-prh-finish`'s hypotheses.
- Full proofs from the permitted material, with per-step source loci. All
  constants relative and dimension-free (no decimals for unnamed source big-O
  constants). State every threshold explicitly.
- If either step CANNOT be closed from the permitted material, that is a
  finding, not a failure: write the sharpest possible statement of the missing
  ingredient (a named GAP), prove everything up to it, and say so in line 1 of
  your answer file.

## Output (ONLY these two files; no other repo edits, no git)

1. `docs/plans/2026-07-24-fudw-decomposition-artifacts/PROOF-F2F3-BRIDGE.md` —
   §0 the two contracts verbatim; §1 F2 setup+proof; §2 F3 setup+proof;
   §3 composition check against `lem-routef-prh-finish`'s hypothesis list;
   §4 constant/threshold ledger; §5 hypothesis hygiene; §6 LOUD defect register.
2. `docs/plans/2026-07-24-fudw-decomposition-artifacts/ANSWER-F2F3.md` —
   ≤12 lines: the two contracts, closed-or-GAP status per step, constants.

Hard boundaries: no edits outside the two files; no git; nothing from the
Kitaev source but sound definitions; no use of quarantined rows or GAP ids as
inputs; honest scope — a named gap beats a smuggled assumption.
