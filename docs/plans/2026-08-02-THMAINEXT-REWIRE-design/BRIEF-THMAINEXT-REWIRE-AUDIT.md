# BRIEF — hostile audit of DESIGN-THMAINEXT-REWIRE.md (fresh verifier)

You are a fresh, independent, HOSTILE auditor. You did NOT write
`DESIGN-THMAINEXT-REWIRE.md` and must assume it is wrong until proven
otherwise. It re-validates the ratified DESIGN-MAIN-STRUCTURE-v5 sect-10
step-15 dependency rewire for `lem-thmainext-conditional` (retaining the
seven-dep line verbatim, contract byte-UNCHANGED) against the CURRENT
post-MAINCB-repair T0 contracts. Finding an error in EITHER direction —
a missing provider (under-wiring) or a false coverage claim
(over-claiming) — is a BIG SUCCESS.

## Your target

`docs/plans/2026-08-02-THMAINEXT-REWIRE-design/DESIGN-THMAINEXT-REWIRE.md`.

## Audit against (read all; never a paraphrase)

1. `docs/plans/2026-08-02-THMAINEXT-REWIRE-design/BRIEF-THMAINEXT-REWIRE.md`
   — every deliverable and constraint delivered?
2. `argument/lemmas/lem-thmainext-conditional.md` — the contract the deps
   must serve, byte-current.
3. `docs/plans/2026-07-26-MAIN-STRUCTURE-design/DESIGN-MAIN-STRUCTURE-v5.md`
   sect-10 step 15 — is the design's line truly VERBATIM the ratified one?
4. The W74F proof-record artifacts named in the thmainext provenance
   (`docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md`,
   `PROOF-W74F-H-STAGE1.md`, the VERDICT files) — check the design's
   coverage table: does EVERY analytic input used there map to a quoted
   clause of a CURRENT dep contract (read the current shard bytes of all
   seven deps and, where af: validated, their exports)? Attack the M28
   consumption claim specifically: the repaired M28 exports
   B=oplus_C M_{|C|}, the extended W.c0_cb*W.K_call*epsilon-isomorphism,
   the unit estimate, and witnesses C_struct,e_struct — does the
   thmainext assembly need anything beyond that which no dep supplies
   (e.g. the OLD M28 form, a reset-ledger fact NOT transitively
   available, an EXT/HCB clause the conj rows do not carry)?
5. The design's W-ledger coherence statement (C_E, epsilon_E choosable
   from one fixed W without contract change): is the argument sound at
   the typed-witness level (docs/LEARNINGS.md 2026-07-28 laws), and is
   anything that should be FLAGGED as a future escalation silently
   absorbed instead?
6. The DAG/linker claims: no cycle; a proved-mod-audit row may import
   T0 + conj rows (check scripts/argument.py's status rules if needed);
   the transitivity correction (reset ledger through M28, not M19-R) —
   verify against `python3 scripts/argument.py --show` output or the
   INDEX.
7. No-T0-invalidation + workspace disposition: deps-only shard edit;
   nothing else touched; the `proofs/lem-thmainext-conditional` workspace
   note is accurate.

## Deliverable — write `docs/plans/2026-08-02-THMAINEXT-REWIRE-design/AUDIT-THMAINEXT-REWIRE.md`

- Verdict per deliverable (1-7 of the design): VALID /
  VALID-WITH-CORRECTIONS (exact corrected text) / REFUTED (show why).
- Final disposition: DESIGN-CONFIRMED / DESIGN-REFUTED / ROUTE-ALARM.
- Cite every check with exact loci (file:line).

## Hard constraints

- Write ONLY the audit file. No repairs beyond exact corrections; no
  status promotion; nothing here is rigorous. L1 discipline: a claimed
  ground truth absent at its cited locus is a FINDING.
