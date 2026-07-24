# BRIEF — aism-fudw decomposition REPAIR (v2): fix the five blockers, keep everything the verdict upheld

You are a FRESH REPAIR ARCHITECT (codex, independent context — you are neither the
v1 architect nor the reviewer). The v1 decomposition design was hostile-reviewed
and rejected: `VERDICT: INVALID`, five BLOCKERs plus MAJOR/MINOR findings, with
exact corrections where the verified packets support them and named GAPs where
they do not. Your job: produce a COMPLETE, STANDALONE v2 design that (a) applies
every correction the verdict marked as mechanical/ready-to-paste, (b) repairs
every BLOCKER exactly as scoped by the verdict, (c) keeps everything the verdict
did not fault, and (d) carries every unresolved bridge forward as an explicit,
honestly-tagged GAP — you do NOT invent mathematics to close a GAP.

## Read first (in this order)

1. `CLAUDE.md` (Laws, §6) and `argument/README.md` (shard schema).
2. `docs/plans/2026-07-24-fudw-decomposition-artifacts/BRIEF-FUDW-DESIGN.md` —
   the v1 brief: ALL its binding design rules, def-provisioning mandates, status
   law, and hard boundaries apply to you verbatim (envelope ≤~10 nodes / depth ≤3,
   single minimal contracts, no parent-contract changes, faithful transcription
   only).
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP.md` —
   the rejection. This is your work order. Every BLOCKER, MAJOR, MINOR, corrected
   row, and GAP must be dispositioned in v2.
4. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP.md` —
   the v1 design (the object under repair).
5. The verified sources (same list as the v1 brief §Read-first item 4–5): the four
   wave-2 proofs + verdicts in `docs/plans/2026-07-24-W74F-wave2-artifacts/` and
   `docs/plans/2026-07-23-W74F-artifacts/DECOMP-W74F-C-THMAINEXT.md`. Where the
   verdict says a subtree is missing (COMP-CB) or an assembly must be factored
   (MAIN-CB), go back to these sources for the factoring — cite loci.
6. The existing parent shards (read-only): `argument/lemmas/conj-hcb.md`,
   `conj-extcb.md`, `lem-thmainext-conditional.md`, `lem-routef-k-ledger.md`,
   `lem-prh.md`.

## The five blockers (repair each exactly as the verdict scopes it)

1. **Missing COMP-CB subtree** — add the COMP-CB result subtree (or deps) that
   H-CB consumes, factored to the envelope, with loci.
2. **EXT-CB hidden semantic cycle** — child contracts must be self-contained
   statements that never reference `conj-extcb` (restate the needed content
   inline; parent references only flow downward via `deps`).
3. **Stage-1 packet** — split the compound/circular packet into acyclic single
   statements; retag anything not carried by a verified proof section (the
   verdict says which); move polar/IFT content out of the definition into result
   shards.
4. **MAIN-CB assembly** — factor the structural assembly out of the single root
   into explicit sub-lemmas until the projected root tree is credibly ≤10/depth 3.
5. **Ledger finish** — restore PRH's positive-unital hypotheses and add the
   F2/F3 stochastic-retract bridge nodes (as `stated` GAP-flagged nodes if no
   verified proof section carries them — check the verdict's disposition).

Also fix the non-blocker findings: dropped smallness hypotheses, and the two
composite defs the verdict says are not citable as written (split/retag per its
correction text).

## Output (ONLY these two files; no other repo edits, no git)

1. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v2.md`
   — complete standalone v2 (same required sections as the v1 brief: proposal
   table, assembly wiring, def-provisioning list + Stage-1 external-input
   register, phase map, risk register) PLUS a leading **DISPOSITION TABLE**: one
   row per verdict finding (BLOCKER/MAJOR/MINOR/GAP) → what v2 does about it and
   where.
2. `docs/plans/2026-07-24-fudw-decomposition-artifacts/ANSWER-REPAIR.md` —
   ≤15-line summary (counts; blockers dispositioned 5/5; remaining GAPs).

Hard boundaries: identical to the v1 brief. Do NOT touch `definitions/`,
`argument/`, `proofs/`, `report/`, `refs/`, `.beads/`, `.frontier/`, or any
existing file; transcribe faithfully; flag, never fix, anything that looks wrong
in the sources.
