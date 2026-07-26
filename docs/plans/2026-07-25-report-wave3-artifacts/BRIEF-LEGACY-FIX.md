# BRIEF — apply the legacy-review verdict's corrections in report/sections/

You are a CORRECTIONS APPLIER (codex, fresh context). The batched hostile
review `VERDICT-PROSE-LEGACY.md` (in
/tmp/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/7089d8ca-e119-4d06-89a2-78b6a317864d/scratchpad/report-review-legacy/)
returned 16-VALID/25 with ready-to-paste corrections for the 9
VALID-WITH-CORRECTIONS shards (00, 03, 06, 14, 16, 17, 21, 22, 24 — by the
verdict's own file names). Apply them to the LIVE repo files under
/home/tobias/Projects/almost-idempotent-stochastic-maps/report/sections/.

## Rules

1. Apply every ready-to-paste correction exactly; touch ONLY the 9 named
   shard files, only at the faulted loci. The 16 VALID shards and everything
   else in the repo are off-limits.
2. Where a correction targets prose whose live text has drifted from the
   verdict's quoted "was" text (the review ran on copies), match by content;
   if you cannot locate an unambiguous anchor, skip it and record it under
   AMBIGUOUS — never improvise.
3. After applying: run `cd report && make` (must exit 0) and
   `bash scripts/check-report-shards.sh` (must pass) from the repo root, and
   include their tails in your answer. Fix only your own application
   mechanics if they fail; nothing else.
4. NO git commands. Do not touch argument/, definitions/, proofs/, docs/,
   scripts/, .frontier/, .beads/, report/PROVENANCE.md, report/main.tex.

## Output

Write `CHANGES-LEGACY-FIX.md` into the scratchpad directory named above:
one row per applied correction (verdict finding → file → description),
AMBIGUOUS section (empty if none), gate tails.
