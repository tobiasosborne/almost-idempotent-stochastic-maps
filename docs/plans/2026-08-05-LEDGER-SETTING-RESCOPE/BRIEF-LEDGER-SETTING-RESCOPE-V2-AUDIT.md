# BRIEF — hostile re-audit of DESIGN-LEDGER-SETTING-RESCOPE-V2

Date: 2026-08-05. You are a FRESH hostile auditor with NO prior context. You did
NOT write the v1 design, the v1 audit, or the v2 design. **Finding a real gap is
a BIG SUCCESS.** Do not defer to any prior document's self-assessment.

## Target and inputs (read in order)

1. `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/AUDIT-LEDGER-SETTING-RESCOPE.md`
   — the v1 audit: 8 numbered findings (3 BLOCKER, 2 HIGH, 2 MEDIUM, 1 LOW) and
   a 6-point redesign gate. These are the acceptance criteria.
2. `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md`
   — the TARGET.
3. `BRIEF-LEDGER-SETTING-RESCOPE.md` (original problem + verifier challenge
   texts), `DESIGN-LEDGER-SETTING-RESCOPE.md` (v1, rejected),
   `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md`
   (the ratified mathematics), the 16 landed shards
   `argument/lemmas/lem-routef-*.md`, the exemplars
   `definitions/def-maincb-witness-ledger.md` /
   `definitions/def-stage1-polar-witness-data.md`, and the two live af ledgers
   (`AF=~/go/bin/af; $AF status -d proofs/<id>`).

## Mandatory attacks (explicit verdict line each)

1. **Finding-by-finding closure**: for EACH of the v1 audit's 8 findings, state
   CLEARED or NOT-CLEARED with the exact v2 locus. A single NOT-CLEARED BLOCKER
   = DESIGN-REJECTED.
2. **Deletion test, re-run from scratch** on the v2 definition AND the
   formation lemma: delete each of the three producer rows
   (`lem-routef-ai-defect-linearization`, `lem-kitaev-almost-idemp-audit`,
   `lem-thmainext-conditional`) from a hypothetical consumer; verify NOTHING of
   their conclusions survives via the definition alone. The definition must be
   data-and-typing only; ALL existence/estimates must sit in the formation
   lemma's contract.
3. **Formation lemma soundness**: is its contract actually provable from its
   declared deps (check against the v2 LEDGER-DOMAINS design §3.1 derivations)?
   Is the quantifier order genuinely one-global-W_RF-first? Is nonvacuity for
   every admissible (H, Phi, eta) with 0 <= eta <= rho_id^corr actually
   delivered? Is its projected af budget plausible?
4. **Byte-suffix re-diff, independently**: for the 15 prefix-only rows, delete
   the prefix and diff against the landed `contract:` byte-for-byte (do the
   extraction yourself; do not trust the designer's claim).
5. **Row 14 revision**: is the new scalar-interface contract (a) exactly the
   scalar inequalities derivable per DESIGN-LEDGER-DOMAINS-v2 §3.5, (b) free of
   any phantom F2/F3/PRH interface, (c) still adequate for the strengthened
   K-ledger to consume (where the map data get bound)? Does anything now
   OVERclaim or UNDERclaim relative to the ratified mathematics?
6. **Dependency-edge audit**: verify every edge the v1 audit required (its
   finding-4 row-by-row list) is present in the v2 `deps:` lines; verify no new
   edge creates a cycle; verify "furnished/successive" is now canonical (typed
   data or direct edges), not prose.
7. **Binder audit**: every displayed matrix variable (X, Y, Z) and every
   amplification level universally bound in each contract.
8. **Vocabulary/provisioning plan**: def-ucp-map and all referenced defs
   provisioned exactly once per workspace; no duplicates; L2 respected (no
   restating).
9. **af continuation plans**: consistent with the corrected contracts;
   validated-children preservation claims consistent with af semantics;
   budgets plausible.
10. **Fresh under-specification hunt**: assume something is STILL missing;
    hunt for it. Also check linker/check-defs mechanics of the full landing
    package (formation row + definition + 16 contract/defs/deps edits + af
    amends) — is the package COMPLETE, i.e., is every change needed to make
    the roots dischargeable enumerated in the design?

## Output

Write `docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/AUDIT-LEDGER-SETTING-RESCOPE-V2.md`:
verdict **LAND / LAND-WITH-EXACT-CORRECTIONS / DESIGN-REJECTED**; numbered
findings table (severity, locus, exact correction); explicit disposition of
attacks 1-10. Design-only round: change NOTHING outside that one new file.
Nothing you write promotes anything; all 16 rows stay `stated`.
