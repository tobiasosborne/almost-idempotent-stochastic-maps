<!--
ROLE: the orchestrator's methodology assessment of the fr + af + bd stack (user-requested,
  2026-07-10, session 14), with its recommendations converted to P0 work items.
STATUS: assessment + decisions of record. The user directive (2026-07-10): these findings
  must not be lost and are P0 — implement so future work immediately benefits.
-->

# Methodology assessment: the fr + af + bd stack (2026-07-10)

## What demonstrably works (preserve; do not relitigate)

1. **Status as a type + promotion through adversaries/oracles.** Registry audit: ZERO
   integrity violations in 151 shards. Wave economics W54-W59: ~48% of author output
   corrected, ~15% killed by fresh hostile verifiers — never a rubber stamp; two whole
   architecture attempts killed, the kills converging on a real theorem (the
   free-preprocessing wall). The bank gate caught the orchestrator's own overclaim
   (the halo-rename 'verify PASS' commit message).
2. **Repo-as-canon.** Cross-session/device/model knowledge accumulation works because
   nothing lives in conversations. (The cycle-319 cross-device merge succeeded for
   exactly this reason.)
3. **The per-turn forcing functions** (stop hook, fr orient/log, ▣-needs-oracle) are
   the strongest anti-progress-theatre devices in the stack.

## The weaknesses, each with its decided remedy

| # | Finding | Remedy | Status |
|---|---------|--------|--------|
| 1 | Hand-maintained discipline decays; only gated discipline holds (the audit's cross-cutting result) | Mechanize the meta-layer (CURRENT.md, anchor whitelist, quota fast-fail, JSONL beads sync) | DONE 2026-07-10 |
| 2 | **AND-only dep semantics cannot express proof strategy (OR-routes)** — the op-hlc blocker: the live 29-node surface is disconnected from op-classical's closure because two alternative routes cannot both be declared | **Implement OR-route support in the linker** (`routes:` front-matter field; closure/status logic treats routes disjunctively; acyclicity over the union), then wire op-hlc's two routes | P0 — bead aism-<or-node>; resolves aism-hse via its option (a), the user's preference |
| 3 | fr's multi-arm bandit is vestigial under the Tier-1 lock (40+ consecutive EXPLOIT-B) | Arms reconciled + parked with explicit override tags (done); revisit the abstraction only if the Tier-1 lock lifts | DONE / deferred by design |
| 4 | The rigour ceiling is codex; L5 tower can rest on `stated` bridges | (a) Hostile pass on all stated bridges is MANDATORY before consumption (aism-bbv);  (b) af->Lean: DECLINED by user 2026-07-10 — out of scope; the user has the know-how and will initiate if/when wanted | (a) P0 queued; (b) P1 scoping bead |
| 5 | Verification is the cost center; strict 1:1 serial verify is slow | **Batched per-shard verification is the DEFAULT for routine multi-lemma harvests** (empirically validated in W56: 10 shards, one hostile pass, 0 INVALID); single-target adversarial rounds reserved for architecture decisions | P0 — standing rule, codified in CLAUDE.md §6 + bd memory today |
| 6 | bd clock-staleness misses content-staleness (dead-framing beads survive pivots) | Session-close habit: sweep in_progress/P0-P1 beads against the newest sketch; close-as-superseded on pivot waves | Standing rule in HANDOFF close protocol |

## Decision log

- 2026-07-10 (user): findings are P0; implement now. OR-nodes named explicitly.
  aism-hse (the op-hlc OR-route USER DECISION) is thereby resolved via option (a):
  linker disjunction support, keeping BOTH the Kernel route and the MIN-A route
  declared without falsely asserting their conjunction.
