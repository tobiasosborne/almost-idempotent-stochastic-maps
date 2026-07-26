<!--
ROLE: orientation for the campaign-statistics GENERATED layer. Everything else in this directory is
  machine-written; this file is the only hand-maintained one.
UPDATE POLICY: hand-maintained, in lockstep with scripts/gen-report-stats.py (CLAUDE.md Rule 9).
-->

# `report/generated/stats/` — generated campaign-statistics layer

**Never hand-edit `preamble.tex`, `headline.tex`, `body.tex`, or `campaign-extract.json`.**
`scripts/check-all.sh` runs `python3 scripts/gen-report-stats.py --check`, which re-renders the three
`.tex` files and byte-compares them; a hand edit is a hard gate failure.

| File | Written by | Consumed by |
|------|-----------|-------------|
| `campaign-extract.json` | `--extract` (mines both repositories) | the render half; nothing else |
| `preamble.tex` | render | `report/main.tex` preamble (`\input`) |
| `headline.tex` | render | `report/main.tex`, right after `\maketitle` (`\input`) |
| `body.tex` | render | `report/sections/40_campaign_statistics.tex` (`\input`) |

## The two halves, and why

```
EXTRACT   sources ───────────────────────────────► campaign-extract.json   (explicit, human-run)
RENDER    campaign-extract.json ─────────────────► preamble/headline/body  (deterministic, GATED)
```

Campaign statistics depend on git history, the `fr` controller log, and the `af` ledgers — all of
which change on every commit. A byte-freshness gate over a generator that reads them live would be
permanently red, because the commit landing the regenerated tables changes their inputs again. So
only **render** is gated. The gate is therefore stable across ordinary commits and fails exactly when
it should: a hand-edited generated file, or a renderer change without a re-render.

The *numbers* go stale silently by design. `--check` prints a non-fatal **drift advisory** comparing
a few cheap live counts (controller records, registry size, `af` roots) against the snapshot, so a
badly stale snapshot is visible without blocking a commit. The rendered section states its own
snapshot timestamp in the frontmatter headline and in its colophon.

## Commands

```bash
python3 scripts/gen-report-stats.py --extract   # re-mine BOTH repos into the snapshot, then render
python3 scripts/gen-report-stats.py             # render from the committed snapshot
python3 scripts/gen-report-stats.py --check     # the gate (also: cd report && make stats-check)
cd report && make stats-refresh                 # = --extract
```

## Sources mined

`.frontier/log.jsonl` + `portfolio.json` · `proofs/*/ledger/*.json` · `argument/lemmas/*.md` ·
`definitions/*.md` · `runs/` · `docs/{waves,plans,audits,lit-review,recon,tooling-feedback,ingest}/` ·
`docs/worklog.md` · `FINDINGS.md` · `docs/LEARNINGS.md` · `.beads/issues.jsonl` ·
`refs/manifest/` · `scripts/` · `report/sections/` · `git log`.

The progenitor repository `../almost-idempotent-positive-maps` is mined the same way **when it is
present**; when it is absent the previously committed progenitor block is carried forward and flagged
`carried_forward: true`. Set `AISM_PROGENITOR=<path>` to point elsewhere. The render half never
touches the sibling, so the gate is green on machines that do not have it.

## What is deliberately NOT in the extract

Token counts, context sizes, wall-clock durations, and cost. Neither repository ever recorded them,
and the generator does not estimate them — see the "What is counted, and what cannot be" subsection
of the generated section. Job counts (`af` node-claim events) are the exact, mechanically derived
substitute.
