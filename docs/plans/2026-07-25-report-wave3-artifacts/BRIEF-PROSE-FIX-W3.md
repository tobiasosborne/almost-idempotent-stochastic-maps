# BRIEF — apply the prose-review verdict's corrections (waves 3+3b)

You are a CORRECTIONS APPLIER (codex, fresh context). The batched hostile
review `VERDICT-PROSE-W3.md` (this directory) returned 7-VALID/11 with
findings and ready-to-paste corrections for shards 26, 27, 28, 35 and for
WIRING.md §G2. Apply them faithfully; do not touch the 7 VALID shards.

## Rules

1. Apply every ready-to-paste correction exactly. Where the verdict orders
   REMOVAL of content not supported by the export/registry ground truth
   (challenge-history metadata in 26/27, the reproduced counterexamples /
   "Corrections of record" material in 28, the unsupported §G2 claim), remove
   it — do not soften, summarize, or relocate it.
2. Shard 35 (status outlook): the verdict found its global counts and off-route
   table unsupported by the supplied ground truth. `repo-inputs/` now ALSO
   contains `argument-INDEX.md` (the full generated registry index),
   `lemmas-dir-listing.txt`, and the three off-route registry shards
   (`lem-collateral-import`, `lem-cross-pivot-cancellation`,
   `lem-import-reduction`). Recompute every count and every table row in shard
   35 directly from `argument-INDEX.md` (NOTE: it predates the conj-extcb root
   validation — `conj-extcb` may appear there as proved-mod-audit; state
   conj-extcb's status the way the shard's forward-reference text already
   handles pending items, or per the verdict's correction if it specifies).
   Every number in the corrected shard 35 must be derivable from the supplied
   files; add a LaTeX comment line above each count naming its derivation.
3. Keep all shard mechanics intact (single \section, header lines, ≤280 lines,
   labels unchanged).
4. Anything the verdict leaves genuinely undetermined → do NOT improvise;
   record it under AMBIGUOUS.

## Output

Edit shards 26_*.tex, 27_*.tex, 28_*.tex, 35_*.tex and WIRING.md in place
(this directory), and write `CHANGES-PROSE-FIX.md`: one row per applied
correction (verdict locus → file/lines → description), an AMBIGUOUS section
(empty if none), and a self-check that every number in shard 35 traces to a
supplied file.

## Hard boundaries

Do NOT touch anything under /home/tobias/Projects/almost-idempotent-stochastic-maps.
No git. Only the named files in this directory.
