# BRIEF — fresh hostile RE-AUDIT of DESIGN-LEDGER-DOMAINS-v2.md (third stage)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-LEDGER-DOMAINS-v2.md` and you did NOT write the first audit. Assume
v2 is wrong until proven otherwise. It claims ALL fourteen reserved K-ledger
rows now close (the first design claimed 13-of-14 and the first audit found
its terminal-GAP claim OVERSTATED and its Υ′ radius defective — both
directions have already flipped once). A falsely-closed row poisons an
elevation campaign; a wrong radius poisons every consumer. Finding a defect
is a BIG SUCCESS.

## Your target

`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md` —
closed scalar ledger (§1), full corrected serial DAG (§2), per-row radius
derivations (§3.1–3.5, incl. the corrected componentwise Υ′ row §3.3 and the
terminal threshold §3.5), independent acyclicity + fully-expanded finite
minimum (§4), dimension-freeness audit (§5), reconnection map + proposed
parent wiring (§6), disposition of first-audit findings (§7).

## Audit against (read all)

1. `docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS.md` —
   the binding first audit. Verify EVERY correction it demanded is applied
   VERBATIM in v2 (the (2C_R)^{-1} factor; the five dependency-list fixes;
   the terminal-threshold rework), and verify v2 §7 dispositions every other
   finding. A correction applied approximately is a finding.
2. `BRIEF-LEDGER-DOMAINS.md`, `DESIGN-LEDGER-DOMAINS.md` (same dir) — what
   was asked; what changed v1→v2; check nothing was silently narrowed.
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`
   §§2.5–2.6, 3.4, R24–R28, R36–R38; and `VERDICT-FUDW-DECOMP-V3.md:69-102`
   (the binding domain warning).
4. `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md` and
   `VERDICT-W74F-G-KLEDGER.md` — every radius must be derivable from what
   the verdict actually VERIFIED, not from the withdrawn claims.
5. `refs/kitaev-2405.02434/approximate_algebras.tex` ~2749–2899 (degree
   estimates) for the mechanism steps.
6. Landed shards: `argument/lemmas/lem-routef-ai-defect-linearization.md`,
   `lem-routef-functional-calculus-closeness.md` (verify the ρ_θ = 1/8,
   C_θ = 12(√2−1) extraction at its lines 4–9),
   `lem-kitaev-almost-idemp-audit.md`, `lem-maincb-error-improvement.md`,
   and — most critically — `lem-thmainext-conditional.md`.

## Specific attack surface (check each, then hunt beyond)

- **The black-box thmainext consumption (the load-bearing v2 move; §3.5).**
  v2 sets the terminal threshold η_K = min{ρ_fac, (24K)⁻¹, 1} using the
  LANDED `lem-thmainext-conditional` contract as the producer of C_E, ε_E,
  claiming the unlanded MAIN reset package is NOT imported. Attack this from
  every side: (a) read the landed contract literally — does it actually
  produce C_E, ε_E under hypotheses the ledger rows can supply, or does one
  of its hypotheses smuggle the MAIN reset package (or a G-S1-gated Stage-1
  producer) back in? (b) `lem-thmainext-conditional` is CONDITIONAL — list
  its condition set explicitly and check each is either a landed leaf or an
  output of an earlier ledger row; (c) is there a circularity through K
  itself (K appears inside η_K's own formula — verify K is produced upstream
  of, and independent of, the threshold row); (d) does the first audit's
  "terminal GAP was overstated" conclusion survive YOUR independent reading,
  or was the original GAP claim right after all?
- **The corrected Υ′ radius (§3.3).** Recompute the componentwise
  construction with the (2C_R)⁻¹ factor, C_R = C_V + C_Δ + C_2: does it
  really force every Choi multiplicity space used to be nonzero? Is the
  factor in the right place (a radius vs a defect bound)? Does any consumer
  of the Υ′ row need the OLD (larger) radius to close its own guard — i.e.
  does shrinking the radius break a downstream row's arithmetic?
- **Per-row radius recomputation (§3.1–3.4).** For every row: rederive the
  local radius formula from the cited upstream constants. Hunt for: η_A used
  outside AI-defect linearization (R24); a normalization guard weaker than
  R25 demands; a forward or dangling dependency; a guard weaker than what
  VERDICT-W74F-G-KLEDGER actually verified; an unexpanded O(·).
- **The five dependency corrections.** Verify each is applied at the exact
  row the first audit named, and that applying them did not create a NEW
  cycle or forward edge elsewhere in the §2 DAG.
- **The fully-expanded finite minimum (§4.2).** Check term by term: every
  entry a closed universal scalar; the minimum over a FINITE index set whose
  finiteness is itself produced by a row landing EARLIER
  (`lem-routef-k-finiteness` last, threshold-minimum after it, per R27/R36
  and the §D serial order); no entry depends on n, block sizes, or
  amplification level.
- **Dimension-freeness (§5).** The finite-dimensional norm selection in the
  componentwise construction is the design's self-flagged delicate point:
  verify no constant (esp. C_R and anything entering through Choi
  multiplicities) depends on n or on the number/sizes of simple blocks.
- **Reconnection map + parent wiring (§6).** Do the corrected deps for the
  two degree rows match v4.1 §3.4? Is the proposed `lem-routef-k-ledger`
  parent wiring still PROPOSED-ONLY with the DO-NOT-REWIRE guard explicit?
  Any instruction in v2 that would rewire before ratification is a finding.

## Deliverable — write `docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS-v2.md`

- Verdict per row (all 14), for the Υ′ correction, for the terminal
  threshold/black-box consumption, for the finite minimum, and for the
  wiring proposal: VALID / VALID-WITH-CORRECTIONS (exact) / REFUTED (show
  the defect).
- Final disposition: LAND-14 (with any corrections) / LAND-PARTIAL (which
  rows hold back and why) / REDESIGN / ROUTE-ALARM.
- Cite every check with exact loci.

## Hard constraints

- Write ONLY `docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS-v2.md`.
  Touch nothing else.
- No repairs beyond stating corrections; no status promotion; nothing here
  is rigorous. NOT IN LOCAL REFS discipline applies.
