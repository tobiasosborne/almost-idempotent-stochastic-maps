## Findings

1. **Critical laundering hole: the acknowledgment does not bind the verified quote.**

   The rescue key is only `(path, workspace, external name)` at [check-refs.py:182](/home/tobias/Projects/almost-idempotent-stochastic-maps/scripts/check-refs.py:182) and [check-refs.py:213](/home/tobias/Projects/almost-idempotent-stochastic-maps/scripts/check-refs.py:213). It does not bind:

   - The quoted text or `source`
   - The external JSON filename
   - A digest of the external record
   - The historical banking commit

   Therefore, any of the four acknowledged external files can have its quote replaced with arbitrary fabricated text while retaining its name, path, and workspace. The result is green.

   Worse, multiple new JSON files can reuse the same internal `"name"`. I reproduced this with two brand-new files containing different fabricated quotes and one acknowledged tuple:

   ```text
   failures=0 skips=2
   GT-listed-name skip_absent_ack
   GT-listed-name skip_absent_ack
   ```

   The claim that this “can never launder a NEW quote” at [check-refs.py:164](/home/tobias/Projects/almost-idempotent-stochastic-maps/scripts/check-refs.py:164) is false.

2. **Critical process failure: the supposedly tracked acknowledgment file is not tracked.**

   [.gitignore:9](/home/tobias/Projects/almost-idempotent-stochastic-maps/.gitignore:9) ignores every `refs/manifest/*` file except three explicit exceptions. `absent-acknowledged.json` is not excepted.

   Live evidence:

   ```text
   git ls-files: path did not match any file known to git
   git check-ignore: .gitignore:9:/refs/manifest/*
   git status --ignored: !! refs/manifest/absent-acknowledged.json
   ```

   Thus the submitted change does not include the policy file in Git. A fresh checkout gets the changed gate but not the acknowledgments and hard-fails the four externals. Locally, edits to this ignored policy file are invisible to review and to the porcelain-based overreach guard at [af-orchestrate.py:159](/home/tobias/Projects/almost-idempotent-stochastic-maps/scripts/af-orchestrate.py:159).

3. **The advertised SHA protection is nonexistent.**

   The loader never reads or validates `sha256`. It neither checks syntax nor compares it with `checksums.sha256`. The tests explicitly use a fake all-zero hash at [test_check_refs.py:125](/home/tobias/Projects/almost-idempotent-stochastic-maps/scripts/tests/test_check_refs.py:125) and still expect rescue.

   Consequently, an acknowledgment can name an arbitrary absent path that was never pinned or previously verified. The “pinned unchanged” justification is prose, not an enforced invariant.

4. **Path matching is exact, but path policy is still under-validated.**

   There is no wildcard or prefix rescue: line suffixes are stripped, matching is case-sensitive, and Unicode is excluded by the regex. The stale-present branch correctly resumes byte verification.

   However, the regex permits `..` and repeated separators, and neither loader nor matcher requires a canonical path inside `refs/` or membership in the checksum manifest. That should hard-fail at acknowledgment-load time.

5. **Semantic drift is limited only for genuinely distinct keys.**

   A different external name over the same absent path still fails, and a present payload cannot be rescued. Malformed acknowledgment data generally crashes fail-closed.

   But “anyone not listed remains protected” is still false: a new external file can impersonate a listed external by reusing its internal name. Altering the listed external’s quote also passes. Exit code becomes zero in both cases.

6. **The tests pass but miss the attack that matters.**

   All 11 tests pass. The three new assertions cover exact rescue, a different name, and stale-present behavior. They do not cover:

   - Changed quote with the same tuple
   - Duplicate external files sharing an acknowledged name
   - Workspace-only and path-only mismatches
   - Invalid or manifest-mismatched acknowledgment SHA
   - Noncanonical/out-of-`refs` paths
   - Whether the acknowledgment file is tracked
   - CLI `--check` exit behavior for an impersonating duplicate

   The test’s `by_name` dictionary would itself collapse duplicate-name records, potentially hiding this attack.

7. **Prover residual risk is real.**

   If the acknowledgment file were actually tracked, a prover edit outside its own proof workspace should appear in `git status` and trigger the overreach guard. Currently it is ignored, so that defense does not exist.

   This is not qualitatively worse than the existing ability to modify ignored reference payloads: `check-refs` does not recompute their pinned SHA, and `check-defs` only checks manifest membership/presence. A prover can already inject a fabricated quote into an ignored payload. But this change adds another ignored mutable trust input—and, for the four acknowledged identities, laundering requires no acknowledgment or payload edit at all.

Minimum correction: track the file explicitly; bind each acknowledgment to a unique external JSON path and cryptographic digest of its exact `source`/quote; reject duplicate names; validate acknowledgment SHA against the checksum manifest; enforce canonical in-`refs` paths; add adversarial tests for all of those invariants.

VERDICT: REJECT — altered and brand-new fabricated quotes can reach a green gate, and the alleged tracked policy file is currently ignored.