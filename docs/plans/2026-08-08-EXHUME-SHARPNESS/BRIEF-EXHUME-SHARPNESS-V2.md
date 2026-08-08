# BRIEF — v2 design: repair DESIGN-EXHUME-SHARPNESS.md per the hostile audit

You are a fresh design worker (you wrote neither the v1 design nor the
audit). `AUDIT-EXHUME-SHARPNESS.md` (same directory) REJECTED v1 with two
FATAL packaging findings while CLEARING the mathematics (findings 4-7: the
4x4 witness arithmetic, the stochastic defect computation, the corollary's
registry hygiene subject to 1-2, and the paper action). Produce the v2
package: carry the cleared material forward VERBATIM and repair exactly
the findings.

## Binding repairs

1. **Finding 1 — the retracted `ex-hume` shard.** The retraction must make
   the false proposition PRECISE before disproving it: full quantifiers
   (`0<s<1`, the per-idempotent universal quantifier on the claimed
   equality, the limit variable in the O(delta), the op-npps clause
   dropped or separately precise), the OLD wording quoted byte-verbatim
   in the body as a historical record, and the counterexample exhibited
   in the body (the audit's own computation: with a = 1-s+s^2,
   ||P_s - I_3||_{inf->inf} = ||u_s v_s^T|| = 2a while the claimed common
   value is 2sa; difference 2(1-s)a > 0). Status per the repo's
   retraction discipline (`status: refuted`? check what the linker's
   status vocabulary allows — `scripts/argument.py` — and use the correct
   retraction status; docs/LEARNINGS.md entry mandatory; dated
   FINDINGS.md record mandatory).
2. **Finding 2 — close the manifest over EVERY citation locus.** The
   audit's enumeration is BINDING and complete; incorporate it verbatim:
   - `AGENTS.md:105` + `CLAUDE.md:105` (edit BOTH, keep byte-identical),
     `CONVENTIONS.md:57`, `FINDINGS.md:36-37` + the new dated record,
     `RESEARCH_NOTES.md:97,145`, `refs/manifest/SOURCES.md:25,84`.
   - `thm-rank-one` (nonvalidated): its CONTRACT at line 4 and body line
     14 call ex-hume a sharp family — design the exact corrected contract
     text (this is a landed-contract change: flag for ratification).
   - `op-classical` (VALIDATED): contract/deps/routes UNTOUCHABLE; design
     the exact body/provenance pointer repairs for lines 10, 20-22,
     28-29, 33-35 (sharpness pointer must now go to the new corollary;
     line 38 stays visibly historical).
   - `docs/ingest/README.md:114,119,297` + `docs/ingest/OVERVIEW.md:98`
     (honest re-tag annotations; ingest text itself stays quoted history).
   - The report sweep of v1 (sections list) carries forward; the paper §5
     action per audit finding 7.
   - INDEX.md:27, lem-signed-carre-du-champ fixture, and the
     lem-routef-f0-assembly negative statement: add the explicit
     "historical matrix-family reference, not an import of the false
     contract" clarifications the audit says keep them truthful.
3. **Finding 3 — provenance disposition:** fold the audit's exact
   counterexample computation into the retraction record; dated
   FINDINGS.md entry included in the manifest.

## Carried forward VERBATIM from v1 (audit-cleared — do not silently change)

The `lem-prh-sharpness` elevation design (verified-constants table, af
skeleton, budget 12-24/cap 26, seeding package), the new
`cor-classical-sharpness` shard (subject only to any wording your finding-2
repairs force — flag any delta), its skeleton/budget 9-18/cap 20 and
seeding, the elevation order, and the stale-workspace deletion of
proofs/ex-hume. Byte-diff discipline applies: if you change cleared text,
flag it loudly with justification.

## Deliverable

Write EXACTLY ONE file:
`docs/plans/2026-08-08-EXHUME-SHARPNESS/DESIGN-EXHUME-SHARPNESS-V2.md`,
self-contained (reader needs neither v1 nor the audit): the three repairs
each headed `## Repair of audit finding N`, then the complete package
((a)-(h) as in the original brief, with the closed manifest). Head it
with: `Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR
PROMOTE — pending fresh hostile re-audit and user ratification.`

## Discipline

Write ONLY the deliverable file. No other edits, no git, no af mutations.
Final message: <=8 lines — retraction status chosen, manifest locus count,
any cleared text changed.
