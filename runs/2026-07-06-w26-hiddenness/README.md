# Run bundle: W26 hiddenness wave — INTERRUPTED (network outage, user-directed stop) — 2026-07-06/07

**Status: WAVE IN FLIGHT, KILLED MID-RUN — NO worker output was produced or banked. This bundle
exists solely to preserve the two wave briefs verbatim for relaunch (the session scratchpad does
not survive across sessions). Nothing here is evidence of anything (L3 vacuously).**

## Hypothesis (the wave's question, unanswered)

bd `aism-n7i` (P0), sketch v6 M1 step 4: prove `conj-min-a-w4` by consuming HIDDENNESS
(worker P: LP-dual witness of t*(v) < κ + the two-observable machinery), adversarially paired
with the round-2 insufficiency game (worker Q: models must now hard-assert TRUE hiddenness via
exact t* LPs — a second insufficiency certificate or forced structure both decide).

## What happened

Both codex workers were dispatched 2026-07-06 ~16:53 (mutually blind), ran ~1h+ (worker Q's log
tail before the kill: dual-certificate encoding underway; its randomized/hill-climb search could
not enter the tall regime with true hidden vertices — best hidden height far below τ — CONSISTENT
with all prior absorption findings, but UNBANKED and worker-asserted only). Network outage →
user-directed stop → both workers and the watcher killed before any ANSWER file was written. No
repo files were produced by the workers.

## Command (re-run = relaunch the wave)

```bash
SCR=<fresh session scratchpad>/W26 && mkdir -p "$SCR" && cp runs/2026-07-06-w26-hiddenness/prompts/PROMPT-P.md runs/2026-07-06-w26-hiddenness/prompts/PROMPT-Q.md "$SCR/"
codex exec --skip-git-repo-check -C /home/tobias/Projects/almost-idempotent-stochastic-maps -s workspace-write -o "$SCR/ANSWER-P.md" - < "$SCR/PROMPT-P.md"   # background, ONE call, no & wrapping
codex exec --skip-git-repo-check -C /home/tobias/Projects/almost-idempotent-stochastic-maps -s workspace-write -o "$SCR/ANSWER-Q.md" - < "$SCR/PROMPT-Q.md"   # background, ONE call, no & wrapping
```

NOTE (process gotcha, learned this wave): launch each codex worker as its OWN backgrounded call —
wrapping two `codex exec ... &` inside one backgrounded shell orphans them (no completion
notification; needed a polling watcher + manual kill).

## Invariant / checkable

The preserved briefs are byte-frozen: `sha256sum runs/2026-07-06-w26-hiddenness/prompts/*.md` →
`90003292b3e4affb5c6eb2114e9c57aca32d58602991074f9467c51fbc06d49b  PROMPT-P.md`,
`c3da733c1b2b7c6fc18d82d483250c6cd099322630b6430e288f2878ce1879ec  PROMPT-Q.md`.

## Next

Relaunch verbatim (the briefs are self-contained and current w.r.t. sketch v6 / the 55-result
registry). On harvest: hostile verifier on any claimed proof; orchestrator recompute; bank per the
session-10 pattern; then rewrite this README as the wave's real bundle (or fold worker Q's
certificates in) — this interrupted-marker text is superseded at that point.
