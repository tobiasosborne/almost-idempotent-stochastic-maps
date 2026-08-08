# BRIEF — fresh hostile audit of DESIGN-EXHUME-SHARPNESS.md

You are a fresh hostile auditor (you wrote neither the brief nor the
design). The design claims to deliver sharpness of the exponent 1/2 in
`op-classical` at T0 via elevating `lem-prh-sharpness` plus a new
`cor-classical-sharpness`, while quarantining the landed `ex-hume` as
false-as-literally-stated. Finding a fatal flaw is a BIG SUCCESS. Assume
the design is wrong until it survives.

## Mandatory attacks

1. **The mathematics of the witness.** Re-derive from
   `docs/plans/2026-07-23-W74F-artifacts/PROOF-W74F-A-PRH.md` §7 (and the
   batch verdict) the explicit A, M: verify epsilon_lambda = 2*lambda^2
   EXACTLY, verify the for-every-F lower bound ||AM-F|| >= lambda
   including the l_inf operator norm convention (max row l^1 norm), and
   independently verify the corollary's defect computation
   ||(AM)^2-AM|| <= (claimed constant)*lambda^2 via (AM)^2-AM = A(MA-I)M
   with the correct contractivity facts. Any constant or direction error
   = REJECT.
2. **Dischargeability of the negative.** The corollary's "no beta > 1/2"
   clause: is it phrased as a concrete, af-dischargeable statement (a
   family with defect -> 0 and distance bounded below, plus an explicit
   quantified non-existence over (C, beta) with beta > 1/2 tested against
   the family), free of meta-quantification? Attempt to construct a
   verifier challenge that the phrasing cannot answer.
3. **The ex-hume disposition.** The design quarantines `ex-hume` as
   disproved-as-stated rather than rescoping. Adjudicate: (i) is the
   literal falsity claim itself CORRECT (exhibit the witness — e.g. the
   identity is a stochastic idempotent at a different distance)? (ii) is
   the proposed status/provenance treatment honest and consistent with
   the repo's retraction discipline (docs/LEARNINGS.md for retracted
   claims; FINDINGS.md for the record) and does it preserve the
   historical 3x3 family content somewhere truthful? (iii) does anything
   still depend on or cite ex-hume in a way that breaks (op-classical
   body text, PRD, README, report, the paper §5, docs/ingest)? Enumerate
   every citation site and check the design's manifest covers it.
4. **Registry hygiene.** New/changed shards: full frontmatter, honest
   statuses at landing (nothing promoted), deps T0-only and acyclic,
   contract-quantifier completeness (every symbol bound), no edit to any
   validated row's contract/deps.
5. **Budgets + seeding.** Recount the skeletons; every 3x expansion
   endpoint strictly under its cap; seeding packages byte-exact; the
   fact census complete (explicit matrix arithmetic, norm conventions,
   infimum-over-set facts).
6. **Paper consistency.** `paper/main.tex` §5 currently presents the 3x3
   family with the corrected formulas. If the design lands, is the paper
   still faithful (does §5 need to switch to the 4x4 witness, keep the
   3x3 as prose with the corrected statement, or both)? The manifest
   must say exactly what happens to §5 and to the footnote's "sharpness
   ... human audit" clause after the corollary reaches T0.

## Verdict format

Write EXACTLY ONE file:
`docs/plans/2026-08-08-EXHUME-SHARPNESS/AUDIT-EXHUME-SHARPNESS.md`,
headed `VERDICT: LAND` / `VERDICT: LAND-WITH-EXACT-CORRECTIONS` (exact
old/new pairs you have VERIFIED) / `VERDICT: REJECT` (fatal flaw first).
Numbered findings, most severe first, each with exact locus and
consequence; dispose every design risk and every attack above.

## Discipline

Write ONLY the verdict file. No other edits, no git, no af mutations.
Final message: verdict line + top three findings, <=6 lines.
