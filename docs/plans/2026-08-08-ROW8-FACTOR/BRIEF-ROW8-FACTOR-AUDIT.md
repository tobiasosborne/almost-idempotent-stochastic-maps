# BRIEF — fresh hostile audit of DESIGN-ROW8-FACTOR.md

You are a fresh hostile auditor. You did NOT write
`docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md` and your job is to
find the error that gets a wrong or undischargeable contract into the
registry. Finding a fatal flaw is a BIG SUCCESS, not a failure of the
process. Assume the design is wrong until it survives your attack.

## What is at stake

The design factors the user-ratified ledger row 8
(`lem-routef-upsilon-prime-closeness`) into two new sub-lemma registry rows
plus a slimmed main row, because the honest one-tree size (~29 nodes)
exceeds the L4 brittleness ceiling (26). If the package is ratified, the two
sub-lemma shards will be landed VERBATIM and af-elevated, and the main row's
deps line edited. A contract error here poisons everything downstream (rows
9–14 all funnel through row 8).

## Mandatory attack list (do all of these, then anything else you find)

1. **Byte-identity of the main contract.** Diff the design's main-row text
   against `argument/lemmas/lem-routef-upsilon-prime-closeness.md`
   `contract:` line. ANY byte difference = REJECT.
2. **Ambient-binding completeness (the family's known killer).** For EACH
   sub-lemma contract: every symbol must resolve to (W_RF,S) fields/derived
   notation per `definitions/def-routef-raw-factor-setting.md`, to a declared
   dep's contract text, or to an in-contract definition. Hunt specifically
   for symbols living only in the design prose (V, W_j, U_js, xi_j, C_j,
   E_j, F, L_j, iota_js, hat-U_js, p_js, R_j, alpha_j, C_N, C_R, C_L,
   rho_UpsilonPrime — each must have a home). This exact failure killed the
   16-row family once (FINDINGS.md 2026-08-05); apply the deletion test:
   delete the design doc — are the contracts still fully typed?
3. **Interface completeness between the pieces.** Does sub-lemma 2 consume
   objects (the components UpsilonPrime_j, the isometries, the vector
   states) that sub-lemma 1's CONTRACT actually exports — not merely its
   proof? Does the slimmed main row consume only what the two sub-lemma
   CONTRACTS export plus its other deps? A dependency on a proof-internal
   object that the contract does not export = REJECT (this is the
   interface-projection failure mode, FINDINGS.md 2026-08-05).
4. **Scalar-ledger fidelity.** Check every constant/radius (C_N, C_R, C_L,
   C_UpsilonPrime, rho_UpsilonPrime, the (2C_R)^{-1} clause, the >=1/2
   multiplicity bound) against `def-routef-raw-factor-setting` (1.3)/(1.4)
   and DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 8 (TeX 2831-2895; K-ledger
   228-245; audit 181-209). Any silent renaming, weakening, or strengthening
   = REJECT (the composite must still deliver the frozen main contract).
5. **Dep availability + acyclicity.** Every dep of every new row must be
   af-validated T0 TODAY (check `argument/lemmas/<id>.md` af: lines), and
   the sub-lemma order must be acyclic.
6. **Budget honesty.** With the observed 1.5–3x expansion, is each target's
   honest expectation strictly under its cap, and every cap <= 26? The
   aborted tree (TREE-ROW8-ABORTED.md) is evidence: its 1.2–1.4 branch alone
   was ~11 live nodes — does sub-lemma 1's budget survive that datum?
7. **No definition-as-theorem laundering.** If the design introduces any new
   definition or notational device, apply the deletion test from
   AUDIT-LEDGER-SETTING-RESCOPE.md: a definition may carry data/typing only,
   never an existence or estimate claim.
8. **Seeding-package exactness.** Are the def-add and add-external lists
   complete for each workspace (compare against what row 5's elevation
   taught: the diagonal-repair and ai-defect-linearization facts must be
   available wherever consumed)? A missing external that forces a re-derive
   = the balloon that started this.

## Verdict format

Write EXACTLY ONE file:
`docs/plans/2026-08-08-ROW8-FACTOR/AUDIT-ROW8-FACTOR.md`, headed by one of:
- `VERDICT: LAND` (no corrections),
- `VERDICT: LAND-WITH-EXACT-CORRECTIONS` (list each correction as an exact
  old-string/new-string pair; only corrections you have VERIFIED restore
  soundness),
- `VERDICT: REJECT` (state the fatal flaw first, then all other findings).

Then a numbered findings list, most severe first, each with the exact locus
(file + section/line) and a one-sentence consequence.

## Discipline (non-negotiable)

Write ONLY the verdict file. Do NOT edit the design, the registry,
`definitions/`, `proofs/`, or anything else. Do NOT run git commit or git
push. Do NOT run `af` mutations. Your final message: the verdict line plus
your top three findings in <=6 lines.
