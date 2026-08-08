# BRIEF — fresh hostile re-audit of DESIGN-EXHUME-SHARPNESS-V2.md

You are a fresh hostile auditor (you wrote none of: the briefs, the v1
design, the round-1 audit, the v2 design). v1 was REJECTED by
`AUDIT-EXHUME-SHARPNESS.md` (2 FATAL packaging + 1 HIGH, mathematics
CLEARED). The v2 design claims to repair all findings. Find what survives
into the registry. A fatal flaw found is a BIG SUCCESS.

## Mandatory attacks

### A. The two repairs

1. **Finding-1 repair (the precise retraction).** The retracted `ex-hume`
   contract must now be a complete, fully-quantified FALSE proposition
   (0<s<1 domain, the per-idempotent universal equality, limit variable,
   op-npps clause resolved), with the OLD wording quoted byte-verbatim as
   history and the counterexample exhibited in-body. Re-verify the
   counterexample yourself (with a=1-s+s^2: ||P_s-I_3||_{inf->inf}=2a vs
   the claimed 2sa; difference 2(1-s)a>0) and check the chosen status
   (`disproved`) is legal in `scripts/argument.py`'s status vocabulary
   and correctly handled by status propagation (nothing T0 may depend on
   a disproved row — verify no such edge exists; check the linker treats
   it as terminal, not as available).
2. **Finding-2 repair (manifest closure).** The v2 claims 50 loci. Run
   your OWN repo-wide sweep (grep ex-hume + "sharp" + "sharpness"
   across *.md, *.tex, refs/manifest, argument/, definitions/, docs/,
   report/, paper/, INDEX.md) and diff against the manifest. Any live
   canonical locus left asserting the disproved row certifies sharpness
   = FATAL. Check AGENTS.md/CLAUDE.md stay byte-identical under the
   proposed edits; check the thm-rank-one contract correction is exact
   and flagged for ratification; check op-classical body/provenance
   repairs touch NO contract/deps/routes line of that validated shard.

### B. Preservation + standard battery

3. **Byte-diff the cleared v1 material** (prh-sharpness elevation design,
   corollary shard, budgets, seeding, workspace deletion): any silent
   change = finding.
4. **The corollary contract** under the v2 wording: fully bound
   quantifiers, dischargeable negative (no meta-quantification), deps
   T0-or-in-package only, honest status at landing, seeding byte-exact,
   census complete.
5. **Elevation order + budgets:** recount skeletons; 3x endpoints
   strictly under caps.
6. **Paper §5 + footnote action** consistent with finding 7 of round 1
   and with whatever contracts now land.

## Verdict format

Write EXACTLY ONE file:
`docs/plans/2026-08-08-EXHUME-SHARPNESS/AUDIT-EXHUME-SHARPNESS-V2.md`,
headed `VERDICT: LAND` / `VERDICT: LAND-WITH-EXACT-CORRECTIONS`
(verified old/new pairs) / `VERDICT: REJECT` (fatal first). Numbered
findings, most severe first, exact loci; dispose all round-1 findings and
all attacks above.

## Discipline

Write ONLY the verdict file. No other edits, no git, no af mutations.
Final message: verdict line + top three findings, <=6 lines.
