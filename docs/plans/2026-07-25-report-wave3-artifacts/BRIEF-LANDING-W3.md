# BRIEF — execute the report waves 3/3b/3c landing per WIRING.md

You are a LANDING EXECUTOR (codex, fresh context). The 12 hostile-reviewed
LaTeX shards in
/tmp/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/7089d8ca-e119-4d06-89a2-78b6a317864d/scratchpad/report-wave3/
(files 25_*.tex through 36_*.tex) must be landed into the repo
/home/tobias/Projects/almost-idempotent-stochastic-maps exactly per that
directory's WIRING.md. WIRING.md is your complete instruction sheet; this
brief only frames it.

## Execute

1. WIRING §A–§F literally: copy the 12 shards into report/sections/; update
   report/README.md (order), report/SHARD_CATALOG.md (rows), report/PROVENANCE.md
   (rows — §E gives the hash rows; recompute every hash yourself against the
   live repo at landing time and use YOUR computed values, flagging any that
   disagree with §E's printed values), report/main.tex (\input list),
   report/UNWIRED.md (the 13 removals; retain everything else).
2. WIRING §G1 + §G2: apply the old→new text replacements to the named EXISTING
   shards in report/sections/. §G3 requires nothing at landing.
3. Then run, from the repo root, and include full tail output in your answer:
   - `cd report && make` (must produce main.pdf; report page count)
   - `sh scripts/check-report-shards.sh`
   - `python3 scripts/check-provenance.py --check`
   If any gate fails: fix ONLY landing-mechanics defects (a missed row, a
   typo'd label, a stale hash) and rerun; NEVER touch mathematical content,
   statuses, or registry files. If a gate failure would require a content
   change, STOP and record it under BLOCKED.

## Hard boundaries

Write ONLY: report/sections/*.tex (the 12 new + the §G-named existing),
report/README.md, report/SHARD_CATALOG.md, report/PROVENANCE.md,
report/main.tex, report/UNWIRED.md, and build outputs under report/. Do NOT
touch argument/, definitions/, proofs/, docs/, scripts/, .frontier/, .beads/.
NO git commands of any kind.

## Output

Write LANDING-REPORT.md into the scratchpad directory above: files
copied/edited (with counts), every §G replacement applied (file: yes/no),
hash recomputations (any deviation from §E printed values), gate outputs
(tails), AMBIGUOUS/BLOCKED sections (empty if none).
