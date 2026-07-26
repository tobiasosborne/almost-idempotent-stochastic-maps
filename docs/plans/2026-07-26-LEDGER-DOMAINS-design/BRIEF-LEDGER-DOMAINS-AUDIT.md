# BRIEF — hostile audit of DESIGN-LEDGER-DOMAINS.md (second stage, fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-LEDGER-DOMAINS.md` and must assume it is wrong until proven
otherwise. It claims 13 of the 14 reserved K-ledger rows close via a serial
local-domain DAG and that the 14th (`lem-routef-threshold-minimum`) is a GAP
with two causes. Attack BOTH directions: a falsely-closed row poisons an
elevation campaign; a falsely-declared GAP stalls the route. Finding an error
in either direction is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS.md`.

## Audit against (read all)

1. `docs/plans/2026-07-26-LEDGER-DOMAINS-design/BRIEF-LEDGER-DOMAINS.md`
   (what was asked).
2. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   §§2.5–2.6, 3.4, R24–R28, R36–R38; and `VERDICT-FUDW-DECOMP-V3.md:69-102`
   (the binding domain warning).
3. `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md` and
   `VERDICT-W74F-G-KLEDGER.md` — CHECK EVERY cited locus; the design's radii
   must be derivable from what the verdict actually verified, not from the
   withdrawn claims.
4. `refs/kitaev-2405.02434/approximate_algebras.tex` ~2780–2830 (degree
   estimates) for the mechanism steps.
5. The landed shards: `argument/lemmas/lem-routef-ai-defect-linearization.md`,
   `lem-routef-functional-calculus-closeness.md`, `lem-kitaev-almost-idemp-audit.md`,
   `lem-maincb-error-improvement.md`, and `argument/INDEX.md` — verify the
   design's registry-absence claim for `lem-maincb-reset-constant-ledger`.

## Specific attack surface

- **The GAP claim**: is `lem-maincb-reset-constant-ledger` really absent from
  the registry? Is the ε_max^cb shortfall in the v4.1 reset minimum real
  (recheck `lem-maincb-error-improvement.md` lines 4, 13–19 against v4.1
  line 216)? Could the threshold row close some other way without the reset
  package (if so, the GAP is OVERSTATED)?
- **The 13 closing rows**: for each, recompute the local radius formula from
  the cited upstream constants. Hunt for: a radius using η_A outside AI-defect
  linearization (R24 violation); a forward/dangling dependency; a guard
  weaker than what the G-verdict demanded; an unexpanded O(·).
- **Serial well-foundedness**: is the DAG acyclic with k-finiteness and
  threshold-minimum last, per the brief?
- **Dimension-freeness**: attack the finite-dimensional norm selection in the
  componentwise Υ′ construction — the design itself flags this as the
  delicate point; verify no constant depends on n.
- **Reconnection map**: do the corrected deps for the two degree rows and the
  proposed k-ledger parent wiring match v4.1 §3.4 with the DO-NOT-REWIRE
  guard kept explicit?

## Deliverable — write `docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS.md`

- Verdict per row (all 14) and per GAP cause: VALID / VALID-WITH-CORRECTIONS
  (exact) / REFUTED (show the defect).
- Final disposition: LAND-13-HOLD-1 (with corrections) / REDESIGN /
  ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS.md`.
- No repairs beyond stating corrections; no status promotion; nothing here is
  rigorous. NOT IN LOCAL REFS discipline applies.
