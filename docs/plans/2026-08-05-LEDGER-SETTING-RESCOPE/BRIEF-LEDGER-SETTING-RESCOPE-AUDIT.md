# BRIEF — hostile audit of DESIGN-LEDGER-SETTING-RESCOPE

Date: 2026-08-05. Author: orchestrator (Claude). You are a FRESH hostile auditor
with NO prior context and NO stake in the design. **Finding a real gap, error, or
laundering vector is a BIG SUCCESS** — you are rewarded for kills, not for
approvals. Do not defer to the designer; do not assume the orchestrator checked
anything mathematical (it is forbidden from doing so).

## Target

`docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE.md`
— a proposed repair for a verifier-caught, family-wide contract
under-specification in the 16 LEDGER-DOMAINS registry rows. Context (read
first): `BRIEF-LEDGER-SETTING-RESCOPE.md` (same directory, includes the three
decisive verifier challenge texts verbatim);
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md`
(the ratified mathematical design); the 16 landed shards
`argument/lemmas/lem-routef-*.md`; the two live af ledgers
(`proofs/lem-routef-raw-factor-norms`, `proofs/lem-routef-raw-factor-identities`;
inspect with `AF=~/go/bin/af; $AF status -d proofs/<id>`).

## Mandatory attacks (each gets an explicit verdict line)

1. **The deletion test on the definition** (the design's own Risk 1): does
   `def-routef-raw-factor-setting` smuggle THEOREM content into a definition —
   i.e., does any clause assert existence/properties that only
   `lem-routef-ai-defect-linearization`, `lem-kitaev-almost-idemp-audit`, or
   `lem-thmainext-conditional` may furnish? A definition that proves is a
   laundering vector; kill it.
2. **Byte-suffix check, all 16 rows**: delete the proposed prefix from each
   re-scoped contract and diff the remainder against the landed `contract:`
   line byte-for-byte. Any drift — a changed constant, a reworded quantifier,
   a normalized space — is a FINDING.
3. **Binding adequacy**: for each row, do the prefix + registered defs now
   supply EVERY symbol and hypothesis the row's proof needs (per the v2 design
   §3 derivations)? Recheck specifically: `rho_AI := eta_A`; the domain
   `0 <= eta <= rho_id^corr` of the setting datum vs each row's stated radius
   (any row whose radius could exceed the datum's domain of definition is a
   FINDING); rows quantifying over X, Y, Z and amplification levels; row 14's
   imports of F2/F3/PRH contracts; D2/D3.
4. **Hidden narrowing / hidden strengthening**: does any re-scoped contract
   claim less than the landed one (silent domain shrink) or more (the setting
   definition granting properties the landed contract did not presuppose)?
5. **defs-line corrections**: is dropping `def-almost-idempotent` from all 16
   rows right? Is anything else on the lines wrong or missing (L2: no naked
   symbols, no restatement)?
6. **The af continuation plan**: does `af amend` on roots/interior nodes
   genuinely preserve the validated children per af semantics (check the af
   binary's behavior, not the design's assertion)? Is the claimed
   node/round budget plausible? Would any validated node's statement become
   unsupported under the amended root?
7. **Blast radius**: proposed `lem-routef-k-ledger` wiring and the F0-assembly
   design — is the re-scoped family still consumption-compatible? Does the
   DO-NOT-REWIRE guard stay untouched?
8. **The design's own ten risks (§6)**: dispose each explicitly
   (CLEARED / NOT-CLEARED with reason).
9. **Under-specification hunt**: the previous audit of the LEDGER-DOMAINS
   design missed exactly this class of defect. Assume something is STILL
   under-specified; hunt for it (e.g., is the choice/uniqueness of the witness
   package datum handled? Is "every amplification" bound inside or outside the
   datum? Does the definition pin the SAME v across rows that must share it?).
10. **Linker/gate mechanics**: will the re-scoped contracts pass the linker's
    contract-match after af re-seed/amend; will `check-defs` accept the new
    shard (schema, provenance tag `original`, no drift with existing defs)?

## Output

Write `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/AUDIT-LEDGER-SETTING-RESCOPE.md`
with: verdict **LAND / LAND-WITH-EXACT-CORRECTIONS / DESIGN-REJECTED**; a
numbered findings table (severity, locus, exact correction where applicable);
explicit disposition of attacks 1-10. Design-only round: change NOTHING outside
that one new file. All 16 rows stay `stated`; nothing you write promotes
anything.
