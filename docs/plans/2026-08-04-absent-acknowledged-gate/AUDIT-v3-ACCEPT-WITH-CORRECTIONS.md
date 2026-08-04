No surviving laundering path through the acknowledgment mechanism was found. The path, workspace, name, filename, and exact source digest are all enforced; symlink confinement also works. The existing `_REFS_RE` weakness is not widened and is tracked as open P1 `aism-ccso`.

Evidence:

- With the ack absent, all 959 result rows and counts exactly matched `HEAD`: 4 failures, 932 skips, exit 1.
- With the valid ack, exactly the four listed Munkres externals changed from `fail` to `skip_absent_ack`; nothing else changed.
- The policy contains one absent, manifest-pinned payload and four externals. Every live filename, name, and source digest matches.
- Restore bead `aism-l4uw` is open P1.
- Focused tests: 26/26 passed. Full `scripts/check-all.sh`: passed.
- Malformed/duplicate manifest lines aborting the gate is appropriate fail-closed behavior for a tracked trust input, not an unacceptable DoS.

Corrections required:

- The traversal test is not isolated as claimed: removing the segment guard still rejects `refs/../…` through resolved-path confinement. Add a pinned in-refs `refs/a/./b` or `refs/a/../b` mutation-killing test.
- Add a dedicated symlink-escape regression test. The implementation works, but no test protects it.
- The stale-entry test remains green if the loader’s stale guard is removed because acknowledgments are only consulted for `absent_path`. Assert loader exclusion/warning directly. Also make stale/schema tests hermetic instead of skipping on clean clones.
- “Device-local” is misleading: the tracked policy applies to every checkout where the payload is absent. Use “repository-tracked, activated by local payload absence.”
- The policy and `.gitignore` are staged, but both modified scripts are currently unstaged. Stage them before committing; otherwise the pre-commit test can exercise code that the commit omits.

VERDICT: ACCEPT-WITH-CORRECTIONS (add discriminating canonical-path, symlink, and hermetic stale tests; correct the device-local wording; stage both modified scripts)