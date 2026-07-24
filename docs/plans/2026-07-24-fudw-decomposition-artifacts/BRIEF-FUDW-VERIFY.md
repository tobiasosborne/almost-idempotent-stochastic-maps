# BRIEF — aism-fudw decomposition design: HOSTILE ARCHITECTURE REVIEW

You are a FRESH HOSTILE REVIEWER (codex, independent context — you are NOT the
architect and have seen none of their reasoning). Finding a flaw in this design is a
BIG SUCCESS. This is a full single-target adversarial review: the design is an
architecture decision (CLAUDE.md §6 reserves full adversarial rounds for exactly
this).

## Object under review

`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP.md` — a
proposal factoring the Route F chain into af-sized registry sub-lemmas.

## Read first

1. `CLAUDE.md` (§1 Laws, §6) and `argument/README.md` (shard schema, brittleness).
2. `docs/plans/2026-07-24-af-elevation-campaign.md` (the campaign the design serves).
3. The design itself.
4. The verified sources it factors (ALL in
   `docs/plans/2026-07-24-W74F-wave2-artifacts/`): `PROOF-W74F-E-HCB.md`,
   `PROOF-W74F-F-EXTCB.md`, `PROOF-W74F-H-STAGE1.md`, `LEDGER-W74F-G-K.md`, their
   four `VERDICT-…` files, and
   `docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md`.
5. The existing parent shards: `argument/lemmas/conj-hcb.md`, `conj-extcb.md`,
   `lem-thmainext-conditional.md`, `lem-routef-k-ledger.md`.

## Attack surface (check ALL; report per-item verdicts)

1. **Coverage**: does the union of sub-lemma contracts + assembly wiring actually
   reconstruct each parent contract, with nothing silently dropped (hypotheses,
   quantifiers, constants, uniformity-in-n clauses)? Hunt for a clause of a parent
   contract no sub-lemma carries.
2. **Faithfulness**: does any proposed contract strengthen, weaken, or "fix" what the
   verified artifact proves at the cited locus? Byte-compare the mathematical content.
3. **Contract hygiene**: is any contract compound ("hence", corollary gloss,
   meta-commentary, degenerate boundary hypotheses)? These thrash af to STUCK.
4. **DAG soundness**: cycles, dangling deps, deps that skip a phase boundary, a
   sub-lemma consuming a sibling that phase ordering has not yet validated.
5. **Envelope realism**: are the projected af node/depth counts credible against the
   length/structure of the corresponding proof sections? Flag optimistic projections.
6. **Def provisioning**: is any contract using vocabulary with no existing or proposed
   def? Is any proposed `cited` def actually citable (definitions sound in the source)
   vs needing `original`/`consensus`? Is the Stage-1 external-input register complete
   against what PROOF-W74F-H actually consumes?
7. **Status law**: any proposal above its honest rung (glue nodes must be `stated`;
   verified-section transcriptions `proved-mod-audit`; nothing higher)?
8. **Gap honesty**: did the architect invent glue mathematics instead of flagging a
   GAP?

## Output

Write `docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP.md`:

- Line 1: `VERDICT: VALID` | `VALID-WITH-CORRECTIONS` | `INVALID`.
- Per-attack-surface findings (numbered 1–8 as above), each with a verdict and, for
  every defect: severity (BLOCKER / MAJOR / MINOR), the exact design row/line, and the
  exact correction text if one exists (corrections are applied mechanically — write
  them ready-to-paste).
- A final "registry impact" section: the corrected proposal table rows (only the rows
  you changed), ready for mechanical transcription.

Also write a ≤10-line `ANSWER-VERIFY.md` summary.

## Hard boundaries

You create ONLY the two output files above. Do NOT edit the design, the registry,
`definitions/`, `proofs/`, `refs/`, or anything else. Do NOT run git. Do NOT
soften findings — INVALID with a named repair is a success, not a failure.
