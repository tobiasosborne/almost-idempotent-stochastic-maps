# BRIEF — batched hostile prose-vs-export review: the session-25 legacy shards

You are a FRESH HOSTILE REVIEWER (codex, independent context — you did not
author any of this). Finding a discrepancy is a BIG SUCCESS. This discharges
the remaining scope of review bead aism-h0mp: the session-25 opus-authored
prose shards have NEVER been hostile-reviewed (the newer shards 25–36 were,
separately; they are not in scope here).

## Objects under review

The 25 files in `shards/` (00_overview.tex … 24_hcb3_diagonal_inverse.tex).
Shards that are pure narrative (overview/orientation) are reviewed for factual
status honesty only; every shard that presents a registry result gets the full
per-shard check.

## Ground truth

`registry/` — ALL 255 registry shards (`contract:` line = the only admissible
statement; front-matter `status:`/`af:` = the only admissible status).
`exports/` — every af workspace's validated `export.md` (named
`<id>-export.md`); the only admissible proof content for an af-validated id.
`main.tex` (macros), `CONVENTIONS.md` (notation).

## Per result-bearing shard, check hostilely

1. **Statement fidelity:** the contract-quote environment byte-matches the
   registry `contract:` line (literal comparison).
2. **Proof faithfulness:** the prose proof is a compression of the export
   tree — no editorial mathematics, no steps the export lacks, no gaps the
   export lacks; children cited where the export factors.
3. **Status honesty:** af-validated presented as exactly that; nothing
   non-validated presented as a theorem; NOTE the current facts — `conj-hcb`
   and `conj-extcb` are both `proved`/`af: validated` now, and nine of these
   shards had status-text repairs landed recently (commit-level fixes), so
   judge against the registry files supplied here, not against what you guess
   the text used to say.
4. **Mechanics:** one \section, SHARD-ID/TITLE/SUMMARY/KEYWORDS header,
   ≤280 lines, label transforms, macros defined in main.tex.

## Output (ONLY these two files, in this directory)

1. `VERDICT-PROSE-LEGACY.md` — first line `VERDICT: <n-VALID>/<m-reviewed>`;
   one verdict line per shard (VALID | VALID-WITH-CORRECTIONS | INVALID —
   one-line reason); findings with severity + ready-to-paste corrections.
2. `ANSWER-PROSE-LEGACY.md` — ≤15-line summary.

## Hard boundaries

Do NOT touch anything under /home/tobias/Projects/almost-idempotent-stochastic-maps
— everything you need is in this directory. No git. Only the two output
files. Do not soften findings; do not fix shards yourself.
