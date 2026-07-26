# BRIEF — batched hostile prose-vs-export review, report waves 3+3b

You are a FRESH HOSTILE REVIEWER (codex, independent context — you are not the
author of any file here). Finding a discrepancy is a BIG SUCCESS. This is the
project's standard batched verification pattern: ONE pass over the batch,
a per-shard verdict line for every shard.

## Objects under review

The 11 LaTeX prose shards in this directory (25_*.tex through 35_*.tex),
authored as write-ups of af-validated results, plus WIRING.md's §G1/§G2
stale-status corrections. The authors are NOT to be trusted; their
AUTHOR-NOTES.md is a claim inventory, not evidence.

## Ground truth (in `repo-inputs/`)

- `<id>-registry.md` — the registry shard; its `contract:` line is the ONLY
  admissible theorem statement.
- `<id>-export.md` — the af-validated proof tree; the ONLY admissible proof
  content.
- `main.tex` (macro definitions), `CONVENTIONS.md` (notation registry),
  `20_*.tex`/`21_*.tex` (existing accepted shards, for convention conformance).

## Per shard, check hostilely

1. **Statement fidelity:** the \contractquote (or equivalent statement env)
   byte-matches the registry `contract:` line — verify by literal comparison,
   not by mathematical equivalence. Any strengthening, weakening, or silent
   notational change = INVALID.
2. **Proof faithfulness:** the prose proof is a compression of the export tree
   — every prose step must be traceable to a validated node; any step that is
   editorial mathematics (new argument, new bound, reordered dependency that
   changes what is assumed) = finding. Gaps the export does not have = finding.
3. **Status honesty:** af-validated results presented as such and nothing else;
   `conj-extcb` only ever a tagged pending forward-reference; no
   proved-mod-audit content stated as theorem; the status-outlook shard's
   counts and lists consistent with the registry files provided.
4. **Mechanics:** one \section, SHARD-ID/TITLE/SUMMARY/KEYWORDS header,
   ≤280 lines, labels follow the first-hyphen→colon transform of the registry
   id, macros all defined in main.tex.
5. **WIRING §G1/§G2:** each old→new text replacement is factually correct
   against the registry ground truth (no replacement may overclaim).

## Output (ONLY these two files, in this directory)

1. `VERDICT-PROSE-W3.md` — first line `VERDICT: <n-VALID>/<m-total>`; then one
   verdict line per shard (`<file>: VALID | VALID-WITH-CORRECTIONS | INVALID —
   <one-line reason>`); then findings with severity and ready-to-paste
   corrections; then a §G1/§G2 adjudication section.
2. `ANSWER-PROSE-W3.md` — ≤15-line summary.

## Hard boundaries

Do NOT touch anything under /home/tobias/Projects/almost-idempotent-stochastic-maps
(a live proof orchestration aborts on any repository write; everything you need
is in this directory and `repo-inputs/`). No git. Only the two output files.
Do not soften findings; do not fix shards yourself.
