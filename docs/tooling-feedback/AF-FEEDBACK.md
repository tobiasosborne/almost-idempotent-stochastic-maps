<!--
ROLE: living feature-request / bug report for the `af` binary (../vibefeld; af 0.1.3) AND for this
repo's orchestration driver scripts/af-orchestrate.py, written by the orchestrator agent from real
usage. Hand the "af binary" section to the af maintainer agent; the "driver" section can be fixed
in-repo.
UPDATE POLICY: append dated entries; strike items when fixed (note the fix version).
-->

# af — bugs, irritations, feature requests (from the aism campaign)

Context: two orchestration runs on `proofs/lem-classical-equiv` (2026-07-02), 8+8 rounds,
29-node tree, root validated clean. af version 0.1.3.

## af binary

### P0 — bugs

1. ~~**`af def-add --dry-run` MUTATES the workspace.**~~ **FIXED in af 0.1.4.** Root cause was
   broader than def-add: `--dry-run` (and `--verbose`) were registered global persistent flags
   advertised in `af --help`, but no command ever read them — so `--dry-run` was a global no-op
   and every mutating command wrote anyway. Fix: a global guard now *refuses* `--dry-run` on any
   command that hasn't implemented it (loud error, non-zero exit, no write) instead of silently
   mutating; `af def-add --dry-run` now previews without writing and warns when the name already
   exists. Original report (fix-1.1.3.7 log): "`af def-add --dry-run` still wrote a duplicate
   definition key `negative mass delta(P)`."

### P2 — feature requests

2. ~~**Bottom-up-ready job filter.**~~ **DONE in af 0.1.5.** `af jobs --ready` lists only verifier
   jobs whose direct children are all cleared (validated/admitted/archived) — the same allowlist
   `af accept` uses — so a node shown is acceptable now. Drops the per-round children_of + state
   scan. Combine with `--format json`; `--ready --role prover` errors as contradictory.

3. ~~**`af init` should drop a workspace `.gitignore`.**~~ **DONE in af 0.1.5.** `af init` now
   writes a `.gitignore` ignoring `locks/`, `.af/`, `nodes/`, `defs/`, `lemmas/` and tracking
   `ledger/`, `assumptions/`, `externals/`, `meta.json`. Note: the original suggestion said "track
   only ledger/ + externals/ + meta.json" but **assumptions/ is filesystem-primary** (written
   directly, not replayed from the ledger), so it is tracked too — ignoring it would have dropped
   assumption data. A pre-existing `.gitignore` is never clobbered.

4. ~~**Machine-readable challenge classification.**~~ **DONE in af 0.1.5.** `af challenge --category`
   accepts a typed, optional value (`gap`, `missing`, `dependency`, `incorrect`, `unclear`,
   `other`), validated at raise time. `af challenges` gains a `--category` filter and includes
   `category` in `--format json`, so the §6.3 guardrail classification can be exact instead of a
   text grep.

## scripts/af-orchestrate.py (our driver — fixable in-repo)

### P1 — bugs / sharp edges

5. **`--phase all` on an EXISTING tree re-dispatches a full prover build.** The build block is
   gated only on `a.phase in ("all","prove")` — nothing checks whether node 1 already has
   children. Resume-with-default-phase would graft a second tree onto the ledger. We avoided it
   only because the DONE banner recommends `--phase verify`. Fix: skip the build automatically
   when the tree is non-empty (or require an explicit `--force-rebuild`).

6. **Exit codes conflate "healthy but out of rounds" with real failure.** Run 1 exited 1 after
   hitting `--max-rounds` while CONVERGING (root pending, 16/28 validated, clear classification,
   resumable) — the harness surfaced it as a task FAILURE. Suggested map: 0 root validated ·
   2 max-rounds-hit-resumable · 3 prover-overreach · 4 balloon · 5 stuck; document in --help.

7. **Worker-answer log truncation keeps only the TAIL.** `' '.join(out.split())[-280:]` produced
   garbled log lines like "prover build done: ause the shard has no deps." Keep head+tail
   (e.g. first 120 + last 160 chars) so the log line carries the summary sentence workers lead
   with.

8. **`--phase verify` is misnamed.** It also (correctly!) dispatches prover-FIX jobs for open
   challenges — but the name suggests verify-only, and we had to read the loop source to confirm
   resuming under it would still fix challenged nodes. Rename to `--resume` (alias the old name)
   or document prominently.

### P2 — features

9. **Continuous scheduling instead of round barriers.** Rounds are lock-step: each round waits for
   its slowest codex worker before computing the next job set. On our deepest chain
   (1.1.3.7 → 1.1.3 → 1.1 → 1) rounds 3-7 of the resume were essentially serial with one worker
   active per round. An event-driven scheduler (re-poll jobs as each worker returns) would cut
   wall-clock substantially at the same quota.

10. **Per-shard brittleness acknowledgement (scripts/argument.py, related).** The validated
    29-node tree now trips `WARN REFACTOR … (>12)` on EVERY gate run — accepted debt tracked in
    bd (aism-6ec), but the WARN is permanent noise that will train agents to skim warnings. A
    frontmatter key like `brittleness-accepted: aism-6ec` (WARN once with the issue id, then
    stay quiet) would keep the signal honest without the spam.
