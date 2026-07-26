# BRIEF — final hostile re-verify: corrected + wave-3c report shards

You are a FRESH HOSTILE REVIEWER (codex, independent context — none of the
prior authors/appliers/reviewers). Finding a flaw is a BIG SUCCESS. This is the
gate before these shards land in the repo.

## History (read first)

`VERDICT-PROSE-W3.md` (the first batch review: 7/11 VALID; findings on shards
26/27/28 and the then-35 status outlook, plus WIRING §G2) →
`CHANGES-PROSE-FIX.md` (verdict corrections applied) → wave 3c (see
`AUTHOR-NOTES.md` last section): conj-extcb validated in-repo, so a NEW
`35_extcb.tex` was authored, the validated status was propagated through
29/32/34 (+G1 revisions), the outlook moved to `36_status_outlook.tex` and was
recounted against the CURRENT index.

## Ground truth (`repo-inputs/`)

`conj-extcb-registry.md` (front matter: proved / af: validated — CURRENT),
`conj-extcb-export.md` (the validated 554-line tree),
`argument-INDEX.md` (CURRENT generated index; 70 proved/validated rows),
`lem-hcb4-canonical-inverse-registry.md` (post-hygiene-fix), the other
`<id>-registry.md`/`<id>-export.md` files, `main.tex`, `CONVENTIONS.md`,
`lemmas-dir-listing.txt`, and the three off-route registry shards.

## Review scope (only these; the 7 previously-VALID untouched shards 25/30/31/33 and unchanged 26/27 parts are NOT re-litigated except where edited)

1. **`35_extcb.tex` (NEW — full review):** statement byte-match to the
   conj-extcb registry contract; prose proof a faithful compression of the
   export tree (no editorial mathematics; archived nodes not narrated as
   mathematics; the two-constant-ledger honesty note preserved — the shard
   must NOT assert the registry body's expanded C_ext form and the tree's
   C_merge(D_0+1) coincide); status text matches the recorded validation
   facts; mechanics (single section, header, ≤280, label conj:extcb).
2. **Corrections verified (shards 26/27/28):** the VERDICT-PROSE-W3 findings
   are actually resolved — no challenge-history metadata, no reproduced
   counterexamples, no unsupported material remains; nothing else changed
   beyond the verdict's corrections + (28 only) the G3-flagged defs-line
   sentence fix (check it against the post-fix registry file supplied).
3. **`36_status_outlook.tex`:** recompute yourself from `argument-INDEX.md`:
   70 proved/validated rows; 37 reproduced ids (the 36 + conj-extcb — check
   the shard's explicit list); the 33-row complement table exactly the
   index-ordered complement; every derivation comment accurate; conj-extcb
   nowhere still described as pending.
4. **Propagation (29/32/34 + any other shard mentioning conj-extcb):** every
   reference reflects proved/af:validated; no stale pending/seeded text
   anywhere in the 12 shards (grep them all).
5. **WIRING.md:** §E hash rows well-formed and dated post-8d0a5061; §F
   UNWIRED removal list consistent (13 removals incl. conj-extcb; the three
   off-route ids retained); §G1/G2/G3 replacement texts factually correct
   against the supplied registry ground truth.

## Output (ONLY these two files, in this directory)

1. `VERDICT-PROSE-W3C.md` — first line `VERDICT: <n-VALID>/<m-reviewed>`;
   per-item verdict lines (35_extcb, 26, 27, 28, 36, propagation-set,
   WIRING); findings with severity + ready-to-paste corrections.
2. `ANSWER-PROSE-W3C.md` — ≤12-line summary.

## Hard boundaries

Do NOT touch anything under /home/tobias/Projects/almost-idempotent-stochastic-maps.
No git. Only the two output files. Do not soften findings; do not fix shards
yourself.
