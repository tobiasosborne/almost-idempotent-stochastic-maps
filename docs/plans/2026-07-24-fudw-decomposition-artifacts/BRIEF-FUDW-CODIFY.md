# BRIEF — aism-fudw codification: transcribe the verdict-blessed SAFE SUBSET into the registry

You are a FRESH TRANSCRIPTION WORKER (codex, independent context). Your job is
**faithful codification, not proving, not verifying, not designing**: transcribe
into registry shards ONLY the rows of the fudw decomposition that the v3 hostile
verdict names as the safe seed-first subset, WITH the verdict's corrections
applied. You add NO mathematics of your own. The orchestrator audits your output
line by line against the artifacts.

## Read first (in this order)

1. `CLAUDE.md` — Laws L0–L5. Binding.
2. `argument/README.md` + `definitions/README.md` — the shard schemas.
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP-V3.md`
   — THE authority. Its registry-impact section defines: the exact withdrawals,
   the corrected deps/contracts, the 77-row honest inventory, and the SAFE
   SEED-FIRST SUBSET (COMP/H rows, the independent EXT and Stage-1 fronts, the
   functional-calculus/AI leaves, the detached PRH finish). Where it corrects a
   row, its text WINS over the design's.
4. `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v3.md`
   — the base design the verdict corrects (row bodies, loci, def lists).
5. The proof artifacts in `docs/plans/2026-07-24-W74F-wave2-artifacts/` — for
   provenance loci only (you cite them; you do not re-derive).
6. `docs/plans/2026-07-24-W74F-wave2-artifacts/BRIEF-W74F-CODIFY.md` +
   `CODIFY-W74F-REPORT.md` — the validated codification pattern you follow
   (status law, anchoring, report format).

## Scope (strict)

- Transcribe ONLY safe-subset rows, as corrected by the v3 verdict. Do NOT
  transcribe: withdrawn rows, MAIN-CB assembly rows, ledger rows, any row the
  verdict left defective, or any GAP id (GAP-EA, GAP-S1-POLAR-CONTRACT,
  GAP-MAIN-STRUCTURE, GAP-LEDGER-DOMAINS, F2/F3). Those remain design-doc-only.
- If the verdict is ambiguous about whether a specific row is in the safe
  subset, EXCLUDE it and list it in your report's deferred register. When in
  doubt, leave it out.
- Existing parent shards (`conj-hcb`, `conj-extcb`, `lem-thmainext-conditional`,
  `lem-routef-k-ledger`, `lem-prh`, …): do NOT change their `contract` or
  `status`. You MAY add `deps` entries to `conj-hcb`/`conj-extcb` ONLY if the
  verdict's registry-impact section explicitly wires them and every named dep is
  transcribed in this pass; otherwise leave parents untouched and record the
  intended wiring in your report.

## Status law (the cardinal sin is overclaiming)

- Verified-proof-section transcriptions: `proved-mod-audit`. Verdict-designated
  `stated` rows: `stated`. NOTHING gets `proved`, `cited`, or an `af:` value
  other than `none`.
- Definitions: transcribe the def shards the safe-subset contracts need (from
  the design's provisioning list as corrected). ALL new defs: `status: draft`,
  listed under `RATIFICATION NEEDED` in your report. Prefer `cited` candidates
  ONLY where a byte-verbatim quote from the pinned
  `refs/kitaev-2405.02434/approximate_algebras.tex` passes
  `python3 scripts/check-refs.py --check`; otherwise tag `original`/`consensus`
  (draft) with an honest source-locus pointer in the body. Do NOT shard
  BSc/MSc textbook notions (L2).
- Every shard body: one-paragraph status note + provenance line
  (artifact §locus + verdict file). Bodies stay short; contracts are ONE line.

## Gates (ALL must pass before you finish)

```
python3 scripts/check-defs.py --check && python3 scripts/check-defs.py --generate-index
python3 scripts/argument.py            # check + generate INDEX/DAG
python3 scripts/check-refs.py --check
python3 scripts/check-provenance.py --check
sh scripts/check-all.sh                # must print "[check-all] OK"
```

New registry ids must be anchored once in the report status ledger
(`report/sections/13_discussion.tex`) or whitelisted in `report/UNWIRED.md` —
follow the existing pattern for proved-mod-audit ids (UNWIRED is the default for
this off-paper-track material). If you touch a report shard keep it ≤~200 lines
(hard guard 280) and run `cd report && make`.

## Hard boundaries

- Do NOT touch: `proofs/`, `runs/`, `.beads/`, `.frontier/`, `HANDOFF.md`,
  `refs/`, any existing shard's mathematical content beyond the explicitly
  allowed parent `deps` wiring, `docs/plans/*` (except reading).
- Do NOT run any `git` command. Do NOT commit. The orchestrator audits then
  commits.
- Do NOT "improve" mathematics; transcribe faithfully; flag oddities in the
  report's defect register.

## Output

1. The new shards + regenerated indexes + minimal UNWIRED/ledger anchoring.
2. `docs/plans/2026-07-24-fudw-decomposition-artifacts/CODIFY-FUDW-REPORT.md`
   starting `STATUS: UNAUDITED TRANSCRIPTION`, listing: every file created or
   edited; every shard id with status + one-line contract; the RATIFICATION
   NEEDED def list; the deferred/excluded-row register (with reasons); intended-
   but-not-applied parent wiring; gate outputs (paste the final `[check-all] OK`);
   defect register.
3. `docs/plans/2026-07-24-fudw-decomposition-artifacts/ANSWER-CODIFY-FUDW.md` —
   ≤12-line summary (shards created, defs created, excluded rows, gates).
