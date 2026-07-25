# BRIEF — aism-0163 decomposition REPAIR (v4): apply the v3 verdict's Registry impact

You are a FRESH REPAIR ARCHITECT (codex, independent context — you are none of the
prior workers; the written artifacts in `inputs/` are your ONLY inputs). Design v3
was hostile-reviewed: the v3 verdict CONFIRMED the overall architecture and the
safe-to-transcribe subset (its §D), but QUARANTINED the MAIN/ledger rows and
recorded EXACT mechanical corrections as its "Registry impact" sections A/B/C.
Your job is the narrowest possible v4: apply the v3 verdict's Registry impact
faithfully, change nothing the verdict did not fault, and produce a complete
standalone v4 design.

## Read first (all under `inputs/` in your working directory)

1. `BRIEF-FUDW-DESIGN.md` then `BRIEF-FUDW-REPAIR.md` then `BRIEF-FUDW-REPAIR-V3.md`
   (all binding rules and hard boundaries carry over verbatim: envelope, single
   minimal contracts, no parent-contract changes, faithful transcription, GAPs
   flagged never filled).
2. `VERDICT-FUDW-DECOMP-V3.md` — your work order. Every finding gets a
   disposition row in v4; its "Registry impact" A/B/C are your exact edits.
3. `DESIGN-FUDW-DECOMP-v3.md` — the object under repair.
4. `VERDICT-FUDW-DECOMP-V2.md` and `VERDICT-FUDW-DECOMP.md` — ensure no earlier
   repair regresses.
5. `PROOF-W74F-H-STAGE1.md` (esp. lines 389-423) and `VERDICT-W74F-H-STAGE1.md`
   (esp. lines 181-250) — the already-hostile-verified constant ledger that
   Registry impact A transcribes. Transcribe; do not re-derive or "improve".

## The v3 Registry impact to apply (disposition each; use the verdict's exact text)

1. **A — new upstream MAIN constant row.** Insert `lem-maincb-reset-constant-ledger`
   immediately before the three raw-reset rows, with the contract, defs, deps,
   provenance, and projected-af EXACTLY as printed in the verdict's §A table.
   DELETE the `lem-routef-main-radius-ledger` proposal everywhere it appears;
   re-point every threshold-aggregation (and any other) dependency on the deleted
   id at `lem-maincb-reset-constant-ledger`.
2. **B — exact replacement rows.** Replace the `contract:`/`deps:` of
   `lem-maincb-stage1-raw-reset-bound`, `lem-maincb-stage2-raw-reset-bound`,
   `lem-maincb-stage3-raw-reset-bound`, and `lem-maincb-uniform-reset-chain`
   with the verdict's §B table values byte-faithfully (defs/provenance unchanged).
   Confirm (and record in the disposition table) that the
   `lem-stage1-exact-unit-rectification` and `lem-routef-prh-finish` dep
   corrections are already reflected; if the v3 design text disagrees with the
   verdict, the verdict wins.
3. **C — exact withdrawals.** `lem-stage1-polar-chart-control`: NO result row —
   replace by the uncontracted `gap-stage1-polar-chart-contract` reservation per
   the verdict. The 14 `GAP-LEDGER-DOMAINS` ids: NO result rows — retain the ids
   ONLY as `GAP / DO NOT SHARD OR SEED` reservations, with no `contract:`,
   `status:`, or `deps:`. Per the verdict's §8.2: the quarantine must be
   REPRESENTED IN THE RESULT INVENTORY (as explicit GAP inventory rows), not in
   commentary. No row anywhere in v4 may keep a dangling dependency on a
   withdrawn id; degree-two/degree-three contracts may remain in the design but
   must not be marked transcribable while their deps dangle.
4. **Counts.** Recompute every row/status/GAP count the design states so the
   inventory, phase map, and summary agree with the post-A/B/C reality.
5. **§D partition.** Reproduce the verdict's safe-to-transcribe-and-seed-first
   subset as an explicit, standalone section of v4 (COMP first; H after COMP +
   `def-hcb-datum`; independent EXT front end; independent Stage-1 front end;
   independent ledger/finish leaves; topology rows blocked on refs acquisition;
   MAIN reset/structural rows, degree rows, telescopes, threshold, and every
   parent downstream of a named GAP remain design-only until blockers close).
   Note in v4 that H-CB and EXT-CB elevations have since completed (conj-hcb
   af-validated; conj-extcb parent in final elevation), so §A's H/EXT dep
   availability is imminent — but do NOT promote any status on that basis.

## Output (ONLY these two files, written to your working directory; nothing else)

1. `DESIGN-FUDW-DECOMP-v4.md` — complete standalone v4, same required sections as
   v3 (disposition table covering ALL prior verdicts' findings including v3's,
   proposal table, assembly wiring, def-provisioning + Stage-1 external register,
   phase map, risk register, plus the §D partition section above).
2. `ANSWER-REPAIR-V4.md` — ≤15-line summary (counts; v3 findings dispositioned
   n/n; remaining GAPs; any ambiguity the verdict left genuinely undetermined,
   flagged as OPEN-QUESTION — never silently resolved).

Hard boundaries: identical to the prior briefs. Only the two files above, in the
working directory. Do NOT touch anything under
`/home/tobias/Projects/almost-idempotent-stochastic-maps` (a live proof
orchestration aborts on any repository write; everything you need is in
`inputs/`). No git. Transcribe faithfully; never invent mathematics to close a
GAP.
