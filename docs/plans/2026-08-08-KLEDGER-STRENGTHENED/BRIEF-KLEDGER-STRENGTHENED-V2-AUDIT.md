# BRIEF — fresh hostile re-audit of DESIGN-KLEDGER-STRENGTHENED-V2.md

You are a fresh hostile auditor (independent context; you wrote neither
design nor the round-1 audit). The v1 design was REJECTED by
`AUDIT-KLEDGER-STRENGTHENED.md` (1 FATAL + 3 HIGH, 10 attacks cleared). The
v2 design (`DESIGN-KLEDGER-STRENGTHENED-V2.md`, same directory) claims to
repair all four findings. Your job is to find the error that survives into
the registry. Finding a fatal flaw is a BIG SUCCESS. Assume v2 is wrong
until it survives your attack.

## What is at stake

If ratified: the landed `lem-routef-k-ledger` contract is REPLACED, three
NEW helper rows and `lem-routef-f0-assembly` are landed verbatim, and all
five are af-elevated. This is the penultimate layer before the
`op-classical` root rewire.

## Mandatory attack list

### A. The four repairs (adjudicate each against the round-1 finding)

1. **Finding 1 (FATAL, cap compliance).** The v2 factoring: three helper
   rows with claimed budgets designed/expected/cap = 4/6–12/14, 5/8–15/18,
   5/8–15/18; parent 6/9–18/21; F0 2/3–6/8. Attack: (i) are the helper
   CONTRACTS complete, self-contained, correctly same-datum-quantified
   first-class registry rows (full frontmatter, family prefix pattern where
   applicable, deletion test against the design prose)? (ii) re-derive each
   node count yourself from the skeletons; is EVERY 3x endpoint STRICTLY
   below its cap? (iii) does the composite of the three helpers + slimmed
   parent still discharge the FULL parent contract (no conclusion dropped
   at a helper seam)? (iv) is the helper dependency order acyclic and
   T0-only (helpers may dep on helpers if acyclic)?
2. **Finding 2 (quantifier hoist).** v2 takes option (a): K >= 1 and
   eta_K > 0 derived pre-forall from header-only scalar formulas. Attack:
   verify from `definitions/def-routef-raw-factor-setting.md` (1.1)–(1.8)
   that K and eta_K really are functions of the W_RF header scalars ALONE
   (no packet, no input, no B, no Delta/Upsilon); that the formation row's
   contract exports the header with the definitional formulas binding; and
   that the frozen row-13/row-14 contracts are then consistent with (not
   contradicted by, and not silently re-proved outside their packet
   binding) the pre-forall projection. If the projection needs any fact
   rows 13/14 prove only inside a packet, the repair fails — say so.
3. **Finding 3 (census).** The 30-item census: is it COMPLETE against the
   skeletons (walk every node; list any silently-invoked fact missing from
   the census), and is each item's classification (L2 common-knowledge vs
   provisioned) defensible? An unprovisioned non-L2 fact = finding.
4. **Finding 4 (stale prose).** Does the manifest now enumerate
   `report/sections/41_status_outlook.tex:97–111`,
   `36_routef_prh_finish.tex:124–127`, `44_routef_f2_f3.tex:199–203`, AND
   did the design's re-sweep miss any other stale locus? Run your own grep
   over `report/` (thmainext, k-ledger, proved-mod-audit, quarantine) and
   compare.

### B. Preservation of the round-1 cleared material

5. **Byte-identity check.** The parent replacement contract, the F0-assembly
   contract, and the 15 dep externals must be byte-identical to v1's
   cleared text (the design claims only the parent deps line changed, by
   appending three helper ids). Diff them. Any other delta = finding.
6. **New-risk hunt on the helpers.** The three helper rows are NEW
   contracts the round-1 audit never saw. Apply the full standard battery
   to them: ambient-binding completeness (every symbol resolves —
   FINDINGS.md 2026-08-05), interface projection (parent consumes only what
   helper CONTRACTS export), no definition-as-theorem laundering, no
   status/provenance dishonesty, dimension-freeness of every constant they
   introduce, seeding-package byte-exactness at literal `proofs/<id>`
   paths.
7. **Deps-line legality.** The parent deps line = the ratified 15-id block
   + the three helper ids. Confirm nothing else moved; confirm the
   rescope-v2 §6.2 BINDING requirement (formation + rows 5/6/8/9 direct)
   still holds; confirm no dep is non-T0 at elevation time other than the
   helpers themselves (and that the elevation ORDER validates helpers
   before the parent).
8. **Guard/root/status invariants.** `stated`/`af: none` everywhere; no
   `op-classical` edit; guard release scoped to the K-ledger landing only;
   superseded W74F history stays history.

## Verdict format

Write EXACTLY ONE file:
`docs/plans/2026-08-08-KLEDGER-STRENGTHENED/AUDIT-KLEDGER-STRENGTHENED-V2.md`,
headed by one of:
- `VERDICT: LAND`
- `VERDICT: LAND-WITH-EXACT-CORRECTIONS` (each correction as an exact
  old-string/new-string pair you have VERIFIED restores soundness)
- `VERDICT: REJECT` (fatal flaw first)

Then a numbered findings list, most severe first, each with exact locus and
one-sentence consequence. Explicitly dispose all four round-1 findings, all
eight attacks above, and the design's own ranked-risk list.

## Discipline (non-negotiable)

Write ONLY the verdict file. Do NOT edit anything else. Do NOT run git
commit/push or `af` mutations. Final message: the verdict line + top three
findings in <=6 lines.
