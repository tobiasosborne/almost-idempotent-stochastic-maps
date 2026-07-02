<!--
ROLE: living feature-request / bug report for the `fr` CLI (~/.local/bin/fr), written by the
orchestrator agent from real usage in this repo. Hand to the fr maintainer agent.
UPDATE POLICY: append dated entries; strike items when fixed (note the fix version).
-->

# fr — bugs, irritations, feature requests (from the aism campaign)

All observations from real usage, 2026-07-02, campaign `almost-idempotent-stochastic-maps`
(`.frontier/log.jsonl` has the full records; cycle ids referenced below).

## P0 — bugs

1. **`died --at` residuals leak into the DEAD ROUTES board section (semantics inversion).**
   Repro: `fr log B died "..." --at "shallow-web exclusion / anti-splitting: ..." ...` (cycle c9),
   then the injected board shows `DEAD ROUTES (do not re-walk): shallow-web exclusion /
   anti-splitting… (c9); quotient packing: … (c10)`. But the `--at` text is the *residual the
   attempt died AT* — i.e. the LIVE frontier — not the route that died. Right now the board
   simultaneously says arm B's target is "quotient packing" and "do not re-walk: quotient packing".
   Actively misleading for any fresh agent that trusts the board.
   Suggested fix: the dead-route ledger entry should be the *approach* (e.g. the note, or a new
   `--route "<approach that died>"` field); `--at` should feed the FRONTIER/residual display only.
   Migration: re-label existing entries from the note field.

2. **`fr log <arm> banked` rejects a passing verdict unless the verified claim EQUALS the logged
   `--artifact` string — undocumented, unhelpful error.**
   Repro: `fr verify lem-classical-equiv --oracle af-lem-classical-equiv` → pass. Then
   `fr log R banked "..." --artifact proofs/lem-classical-equiv/export.md ...` → REJECTED
   ("▣ banked needs a passing audit verdict from an oracle other than the author"). Re-running
   verify with the artifact path as the claim (`fr verify proofs/lem-classical-equiv/export.md
   --oracle …`) made the same log call succeed.
   Suggested fix: (a) document the claim↔artifact binding in `fr help log`/`bank-gate`; (b) error
   message should say *what* verdict lookup failed: "no verdict for artifact '<x>'; found a passing
   verdict for claim '<y>' — verify the artifact itself or log with --artifact '<y>'".

## P1 — irritations

3. **NO-WAVE TURNS counter semantics are opaque and look broken.**
   The board reached `NO-WAVE TURNS: ×7` and STAYED at ×7 across turns that DID log pulls
   (cycles c9, c10 were logged in those turns). Either the counter is cumulative-per-campaign (then
   rename, e.g. `orient turns total: 7`, so it doesn't read as live breaker pressure) or the reset
   on `fr log` is broken. Fresh agents will misread this as "the breaker is about to trip".

4. **Background waves don't fit the per-turn ritual.** Dispatch and harvest happen in different
   turns (subagents run in background). The dispatch turn has no outcome yet, so it must be
   `fr orient`-logged, inflating the no-wave counter while a wave is literally in flight.
   Feature: `fr dispatch <arm> "<note>"` — records an in-flight pull (no outcome), suppresses
   no-wave accounting for that turn, and pairs with the later `fr log <arm> <outcome>` (could
   auto-link dispatch→outcome cycles).

5. **Verdict filenames choke on long claims.** Already noted in
   `scripts/oracles/af-validated.py` docstring ("fr's verdict filenames choke on
   full-contract-length claims"): the workaround is id-form claims. Fix: name verdict files by a
   short hash of the claim; store the full claim inside the verdict record.

## P2 — feature requests

6. **`fr verdicts` (list recorded verdicts + staleness state).** Today the only way to inspect
   verdicts is reading `.frontier/verdicts/` by hand. A `fr verdicts [--stale]` listing
   (claim, oracle, pass/fail, fresh/stale, bound inputs) would make the bank gate auditable at a
   glance.

7. **FRONTIER trail growth.** The injected FRONTIER context now carries the full reduction trail
   (`(trail: A → B → C)`). After many reductions this will bloat every turn's injected context.
   Policy: keep the last 2 hops + a count ("…3 earlier hops, `fr frontier --trail` for all").

8. **Arm-scoped artifact/wave index.** `fr log` records artifacts per cycle; a
   `fr arm show B` that lists its cycles with outcomes/artifacts/residual evolution would replace
   my manual bd-notes mirroring (bd issue aism-yxq currently duplicates what the log knows).

9. **Doc note in `fr help arms`:** off-arm bankable work (infra elevations, chain
   re-establishment) needs a home arm; the natural pattern is a `support` arm like our arm R
   ("re-establish the inherited chain via af"). One sentence in the help would have saved a
   detour.
