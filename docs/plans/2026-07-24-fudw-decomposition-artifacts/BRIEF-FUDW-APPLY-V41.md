# BRIEF — mechanical application of the V4 verdict's ready-to-paste corrections

You are a MECHANICAL APPLIER (codex, fresh context). The hostile verdict
`VERDICT-FUDW-DECOMP-V4.md` (in this directory) returned VALID-WITH-CORRECTIONS
on `DESIGN-FUDW-DECOMP-v4.md` with fully-specified, line-anchored ready-to-paste
corrections. Your ONLY job is to apply them byte-faithfully. You add no
mathematics, reword nothing the verdict did not order, and resolve nothing by
judgment — if any instruction is ambiguous or its line anchor does not match,
STOP applying that instruction and record it under AMBIGUOUS in your answer
file instead of improvising.

## Inputs (this directory)

- `DESIGN-FUDW-DECOMP-v4.md` — the object to correct (do not modify in place).
- `VERDICT-FUDW-DECOMP-V4.md` — the correction source. Apply EVERY instruction
  marked "Ready-to-paste correction" in the findings sections AND the whole of
  section "B. Consequential ready-to-paste design corrections" (B.1 counts,
  B.2 dispositions, B.3 k-ledger wiring), plus the two authoritative YAML field
  blocks and the instruction to take exact LaTeX contract texts from
  `inputs/VERDICT-F2F3-BRIDGE.md:214,218` verbatim (never paraphrase).
- `inputs/VERDICT-F2F3-BRIDGE.md`, `inputs/lem-routef-f2-positive-unital-compression.md`,
  `inputs/lem-routef-f3-retract-defect.md` — byte sources for the F2/F3 rows.

## Output (ONLY these two files, in this directory)

1. `DESIGN-FUDW-DECOMP-v4.1.md` — the complete corrected standalone design
   (v4 + all verdict corrections, nothing else). Add a short provenance header
   line under the title: "v4.1 = v4 with the VALID-WITH-CORRECTIONS paste
   blocks of VERDICT-FUDW-DECOMP-V4.md applied mechanically; no other change."
2. `CHANGES-V41.md` — one row per applied correction: verdict locus → design
   locus (v4 line range) → one-line description; plus an AMBIGUOUS section
   (empty if none) and a final self-check that the corrected inventory counts
   printed in v4.1 (79 = 57/15/7; 15 reservations; definitions 20) are the ones
   the document now actually contains (count them yourself).

## Hard boundaries

Do NOT touch anything under /home/tobias/Projects/almost-idempotent-stochastic-maps
(a live proof orchestration aborts on any repository write). No git. Only the
two output files above.
