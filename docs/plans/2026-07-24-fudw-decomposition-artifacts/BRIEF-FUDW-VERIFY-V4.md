# BRIEF — aism-0163 decomposition v4: FRESH HOSTILE RE-REVIEW

You are a FRESH HOSTILE REVIEWER (codex, independent context — none of the prior
workers; the written artifacts in this directory and `inputs/` are your only
inputs). Finding a flaw is a BIG SUCCESS.

## Object under review

`DESIGN-FUDW-DECOMP-v4.md` (in your working directory), produced by a fresh
repair architect from `BRIEF-FUDW-REPAIR-V4.md` (also here — read it as the
repair work-order).

## Read first

Everything in `inputs/BRIEF-FUDW-VERIFY.md` §Read-first (governs verbatim), PLUS
the full lineage in `inputs/`: `VERDICT-FUDW-DECOMP.md` (v1),
`VERDICT-FUDW-DECOMP-V2.md`, `VERDICT-FUDW-DECOMP-V3.md` (the work-order whose
Registry impact A/B/C the v4 claims to apply), `DESIGN-FUDW-DECOMP-v3.md` (the
object under repair), `BRIEF-FUDW-VERIFY-V2.md`/`BRIEF-FUDW-VERIFY-V3.md`
(attack-surface items carry over), `PROOF-W74F-H-STAGE1.md` +
`VERDICT-W74F-H-STAGE1.md` (the constant ledger §A transcribes — check
byte-fidelity against `PROOF-W74F-H-STAGE1.md:389-423`).

## Attack surface

Items 1–8 of `inputs/BRIEF-FUDW-VERIFY.md` applied to v4 as a standalone object,
plus disposition completeness against ALL THREE prior verdicts, plus
repair-introduced regressions. Hostile priorities:

1. **A-fidelity:** is `lem-maincb-reset-constant-ledger` inserted with contract,
   defs, deps, provenance EXACTLY as the v3 verdict's §A table prints them, and
   is `lem-routef-main-radius-ledger` deleted EVERYWHERE (no surviving
   reference, dep, or count)?
2. **B-fidelity:** are the four replacement contracts byte-faithful to the v3
   verdict's §B table, with defs/provenance unchanged? Are the
   exact-unit-rectification and prh-finish dep corrections in place?
3. **C-fidelity:** do the polar row and all 14 ledger-domain ids appear ONLY as
   uncontracted GAP inventory reservations (no `contract:`/`status:`/`deps:`),
   represented in the result inventory rather than commentary, with NO row
   anywhere keeping a dangling dep on a withdrawn id?
4. **Counts:** recompute the inventory yourself (77 contracted = 55
   proved-mod-audit + 15 stated + 7 cited-candidate; 17 GAP reservations is the
   v4 self-report) — verify or refute every stated count.
5. **F2/F3 adjudication (NEW SURFACE):** the v4 answer flags an OPEN-QUESTION
   that the closed F2/F3 bridge contracts were unavailable to the repair
   architect. `inputs/` now contains `PROOF-F2F3-BRIDGE.md`,
   `VERDICT-F2F3-BRIDGE.md` (VALID-WITH-CORRECTIONS), and the two REGISTERED
   registry shards `lem-routef-f2-positive-unital-compression.md` /
   `lem-routef-f3-retract-defect.md` (status proved-mod-audit). Adjudicate: must
   v4's F2/F3 GAP reservations be closed against these registered contracts (and
   the counts updated), or is keeping them as design-level GAPs correct? Give a
   ready-to-paste correction either way.
6. **GAP honesty:** are GAP-EA, GAP-S1-POLAR-CONTRACT, GAP-MAIN-STRUCTURE,
   GAP-LEDGER-DOMAINS honestly scoped rather than quietly load-bearing inside
   any `proved-mod-audit` contract?
7. **§D partition:** is the safe-to-transcribe-and-seed-first section faithful
   to the v3 verdict's §D, and does v4 refrain from promoting any status based
   on the H-CB/EXT-CB elevation news?

## Verdict semantics (IMPORTANT)

Same as the v3 review: v4 self-declares "repaired architecture; not globally
seedable" because of its named GAPs. Judge it against THAT claim.
VALID / VALID-WITH-CORRECTIONS / INVALID, with the safe-to-transcribe subset
stated explicitly.

## Output (ONLY these two files, in your working directory)

`VERDICT-FUDW-DECOMP-V4.md` + `ANSWER-VERIFY-V4.md`, exactly per
`inputs/BRIEF-FUDW-VERIFY.md` §Output (VERDICT line first; per-surface findings
with severity + ready-to-paste corrections; registry-impact section including
the safe-to-transcribe subset; ≤10-line summary).

## Hard boundaries

Identical to `inputs/BRIEF-FUDW-VERIFY.md`: ONLY your two output files, written
to the working directory; do NOT touch anything under
`/home/tobias/Projects/almost-idempotent-stochastic-maps` (a live proof
orchestration aborts on any repository write — everything you need is local);
no git; do not soften findings.
