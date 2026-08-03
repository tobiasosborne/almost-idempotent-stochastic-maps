Created [DESIGN-THMAINEXT-ELEVATION-V2.md](/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps/docs/plans/2026-08-03-THMAINEXT-ELEVATION-design/DESIGN-THMAINEXT-ELEVATION-V2.md).

Verdict: the re-scoped contract follows via a three-node tree: frozen root → existential repackaging → M28. The six non-M28 deps are registered but deliberately unused. Base `def-epsilon-cstar-algebra` is provisioned.

Verified:

- Frozen root and all seven external contracts byte-match current shards.
- Six unique `def-add` entries.
- `git diff --check` passes.
- `sh scripts/check-all.sh` → `[check-all] OK`.

No registry, definition, proof workspace, or status was changed. The pre-existing `.frontier/log.jsonl` modification was left untouched.