# BRIEF — W72 POTI-0 codifier: transcribe the hostile-verified routine batch into the registry (aism-x0up)

You are a FRESH TRANSCRIPTION WORKER. Your job is **faithful codification, not proving
and not verifying**: turn the four hostile-verified W72 POTI-0 results into registry
shards with honest status tags, passing every repository gate. You add NO mathematics of
your own; fidelity to the artifacts is the whole job and the orchestrator audits it.

## Read first (in this order)

1. `CLAUDE.md` (Laws L0–L5) and `argument/README.md` (shard schema).
2. Your ONLY mathematical sources:
   - `docs/waves/2026-07-16-W70-artifacts/POTI0-ATTACK-W72.md` (pinned contracts,
     §§1.2–1.6 and §2)
   - `docs/waves/2026-07-16-W70-artifacts/APPENDIX-W72-poti0-proofs.md` (the proofs)
   - `docs/waves/2026-07-16-W70-artifacts/VERDICT-poti0-batch.md` (fresh hostile
     verdict: S0 · RX · O48 · ASM2 all VALID, cross-cutting clean — this licenses
     `proved-mod-audit` and nothing more)

## Status law

- Hostile-verified L5 results are **`proved-mod-audit`** — NEVER `proved` (af-only).
- The two creative residuals RDSE and LDHR-48 are **`conjecture`** with EMPTY deps.
- The assembly is conditional: it names its two conjecture premises in BOTH the
  `contract` text AND `deps`.
- `af: none` everywhere.

## Shards to create (ids from the attack doc's own pinning; adjust only for schema/lint)

1. S0 — the exact cause split (attack §1.2; verdict S0 VALID) — `proved-mod-audit`.
2. RX — the root-selection exchange ledger (attack §1.3-ish; verdict RX VALID,
   including the partially-selected-clone-fiber bridge) — `proved-mod-audit`.
3. O48 — the fixed-level starvation ledger (verdict O48 VALID) — `proved-mod-audit`.
4. The ASM2 assembly reduction (attack §2.1–2.2; verdict ASM2 VALID) —
   `proved-mod-audit`, conditional on the RDSE and LDHR-48 conjectures (contract AND
   deps).
5. `conj`-shards for RDSE and LDHR-48 exactly as pinned in the attack doc —
   `conjecture`, empty deps. (These are the creative residuals; their attack is PAUSED
   by user directive — register the statements only.)

Deps discipline: each lemma's `deps` lists exactly the registry shards its appendix
proof literally consumes (the verdict's cross-cutting section confirms the legal-
consumption set; e.g. the lem-ihorn-* extraction/package shards,
`lem-l5-positive-flow-foldback`, the cited lem-aesc-* tail shard). NO `lem-icap-*`,
NO `lem-huddle-charge-assembly`, NO `lem-intersection-branch-production`, NO
`lem-dtr-poti-assembly` — the verifier certified these are NOT consumed.

Contracts must be transcribed from the attack doc's pinned statements (quantifier order
and clone-invariance clauses intact). If the pinned contract and the appendix-proved
statement differ, transcribe the PROVED statement and flag the difference in your
report's defect register.

## Definitions

Reuse the existing vocabulary (the POTI/DTR campaign defs are already registered). Add
NO new definitions unless a contract term is genuinely unregistered and non-textbook; if
one is needed, `status: draft`, listed under `RATIFICATION NEEDED` in your report.

## Gates (must ALL pass)

```
python3 scripts/check-defs.py --check && python3 scripts/check-defs.py --generate-index
python3 scripts/argument.py
python3 scripts/check-provenance.py --check
sh scripts/check-all.sh    # must print "[check-all] OK"
```

Anchor every new id once in the status ledger (`report/sections/13_discussion.tex`,
follow the existing proved-mod-audit/conjecture row pattern, keep the shard ≤280 lines)
or whitelist in `report/UNWIRED.md` — match how the existing POTI/DTR-era ids are
handled (check both files first). If you touch the ledger, run `cd report && make`.

## Hard boundaries

Do NOT touch: `proofs/`, `runs/`, `.beads/`, `.frontier/`, `HANDOFF.md`, `refs/`,
`docs/plans/*`, any existing shard's mathematical content, any existing definition,
anything under `docs/plans/2026-07-24-W74F-wave2-artifacts/` (another worker is live
there). No `git` commands. No mathematical "improvements" — transcribe and flag.

## Output

1. The new shards + regenerated `argument/INDEX.md` / `argument/DAG.md` (+
   `definitions/INDEX.md` only if a def was added) + minimal ledger/UNWIRED anchoring.
2. A report `docs/waves/2026-07-16-W70-artifacts/CODIFY-W72-POTI0-REPORT.md` starting
   `STATUS: UNAUDITED TRANSCRIPTION`: files touched, shard ids + statuses + one-line
   contracts, gate outputs (paste the final `[check-all] OK`), defect register.
