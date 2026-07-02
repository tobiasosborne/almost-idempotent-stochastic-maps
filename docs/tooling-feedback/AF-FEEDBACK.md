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

1. **`af def-add --dry-run` MUTATES the workspace.** Worker-reported during round 1 of the resumed
   run (fix-1.1.3.7 log): "Note: `af def-add --dry-run` still wrote a duplicate definition key
   `negative mass delta(P)` with the same canonical content." A dry-run flag that writes is a
   correctness bug for any scripted orchestration (and it produced a duplicate def key in our
   ledger — harmless here, but noise in the record).

### P2 — feature requests

2. **Bottom-up-ready job filter.** `af jobs --role verifier` vets a node as reviewable, but NOT
   whether all its live children are already `validated` — our driver re-implements that gate
   itself (children_of + state scan each round). A `--ready` (all live children validated) filter
   server-side would remove a whole failure class from every driver.

3. **`af init` should drop a workspace `.gitignore`.** The workspace working caches
   (`.af/pending_defs`, `nodes/`, `defs/`, `locks/`…) had to be gitignored by hand at the repo
   level; `af init` writing a one-line `.gitignore` for its own rebuildable state would make the
   "track only ledger/ + externals/ + meta.json" policy the default everywhere.

4. **Machine-readable challenge classification.** Our driver classifies open challenges by
   grepping their text (MISSING fact / DAG dep / genuine gap) to decide the §6.3 guardrail action.
   If `af challenge` records carried a typed `category` field (set by the challenger), the abort
   classification would be exact instead of heuristic.

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
