<!--
ROLE: the project-optimization remediation plan (user-mandated audit, 2026-07-10).
  Synthesized from five parallel read-only audits: gates/scripts (opus), registry/DAG
  health (opus), docs architecture (sonnet), report-registry sync (sonnet),
  process/controllers (sonnet). Full audit texts: session-14 fr log cycle ~340 context.
STATUS: PLAN — no item applied until user go-ahead; each phase is independently
  executable; proof-leaf work (the six open leaves) resumes alongside per the standing
  directive that all mathematical effort stays on the leaves.
-->

# Project remediation plan (2026-07-10)

## What the audit found HEALTHY (no action — preserve these)

- **Status hygiene is genuinely sound**: all 29 af-validated shards consistent; 15/15
  spot-checked proved shards carry prover + separate hostile verifier provenance; zero
  proved-on-numerics; all 7 proved-with-conjecture-deps shards are explicitly
  conditional. No HIGH integrity violation found in the registry.
- **The hostile-verification pipeline does real work**: across W54-W59, ~35% of author
  output passed clean, ~48% needed corrections, ~15% was killed outright — never a
  rubber stamp. Keep it mandatory. The W56 batched per-shard verification (10 shards,
  one verifier pass) is the proven efficiency pattern → make it the DEFAULT for
  routine multi-lemma harvests; reserve single-target adversarial round-trips for
  architecture decisions.
- Pre-commit gate, check-defs, check-runs, argument.py's pure DAG checks: solid and
  tested. README.md's version-agnostic style is the model for other docs.

## PHASE 0 — same-day hotfixes (trivial effort, do first)

1. **Fix the two live HANDOFF self-contradictions**: mid-file "(sketch v20)" (line 38)
   -> v24; "af-validated 28" (line 36) -> 29. [2-line edit]
2. **Fix `seed-af-workspaces.py`**: `flip_af_seeded` must also insert
   `workspace: proofs/<id>` when absent (CRITICAL — 62/151 shards lack the field, so
   the gate-breaking seed bug recurs on EVERY new elevation). [~3 lines]
3. **`git mv conj-halo-collapse -> lem-halo-collapse`** (+ update its 3 importers'
   deps): a proved/af-validated result must not wear a conj- id. [mechanical]
4. **Bead hygiene**: close `aism-2fi`, `aism-n7i` (superseded by W54); re-scope
   `aism-88r` (frozen quartet -> live elevation queue) and `aism-yxq` (retired
   target); defer `aism-pld` (needs re-eval vs the three-cell surface); convert
   `aism-z98` to DAG-blocked (dep on conj-b-restricted) — it is not actually awaiting
   a user reply. [six bd commands]

## PHASE 1 — gate integrity (the safety net itself; ~1 session, HIGHEST protection)

5. **`test_check_provenance.py` with red->green fixtures** for OVERCLAIM, stale-hash,
   label-drift; wire into the check-all test loop. (CRITICAL: the detector guarding
   the project's cardinal sin currently has ZERO test coverage, and the file falsely
   claims a test exists.)
6. **Un-vacuum `check-refs`**: absent refs payload in --check mode = hard ERROR (or
   prepend `fetch-refs.py --require-all` to check-all). (CRITICAL: today the
   fabrication gate verifies nothing — 19/19 externals skip — and false-greens on a
   clean checkout.)
7. **Quota fast-fail in `af-orchestrate.run_codex`**: inspect returncode + scan for
   the usage-limit marker -> ERROR sentinel; abort the round loop on consecutive
   all-empty/error rounds (independent of open_ch). (HIGH: today's 14 burned rounds.)
8. **Widen the prover-overreach guard**: flag ANY dirty path outside the prover's own
   `proofs/<rid>/`, not just definitions/ + argument/. (HIGH: a workspace-write
   prover can currently edit refs/, report/, even scripts/ gates untripped.)
9. **Anchor whitelist**: `report/UNWIRED.md` (tracked list of intentionally-unwired
   ids) + `check_anchor` promotes unwhitelisted unanchored ids WARN -> ERROR. Turns
   107 permanently-ignored warnings back into a regression gate. [~5 lines + one file]
10. **Realign the brittleness threshold**: NODE_THRESHOLD 12 vs node-cap 40 vs
    validated trees at 14-52 nodes -> one shared constant (~26 per CLAUDE.md §6);
    deletes 20 permanent noise warnings. Factor only the two extremes
    (lem-residual-upper 52, lem-residual-lower 36) if ever re-validated.
11. Low-priority: fix `oracles/af-validated.py` hardcoded AF path (env-var pattern);
    `check_brittleness` `.get('workspace')`; add `--build` (undefined-\Cref scan) to
    the check-all report step; red-green tests for seed-af-workspaces + fetch-refs.

## PHASE 2 — knowledge-base structure (the single biggest integrity lever; 1-2 sessions)

12. **Encode the goal->frontier reduction as DAG edges.** `conj-ex` — nominally THE
    frontier — is an isolated singleton; ~20 open conjectures and ~130 of 151 shards
    are NOT ancestors of `op-classical`; the reduction the whole project rests on
    lives in sketch prose, unverifiable by the linker (L4 gap). Wire the existing
    prose bridges (several already exist as conditional lemmas) into deps so the
    linker can certify the reduction's completeness and acyclicity. THE headline item.
13. **Shard the ~10 undefined project-original technical nouns** (L2 naked-symbol
    risk), led by `zero-face` (22 shards, no canonical definition), then dual
    witness/certificate, cluster/near-cluster, pivot, slab/top-slab, top support
    functional, deficit, co-top, exposedness margin, actor hull. (NB: exposer/row
    vertex/visible set/hidden top are ALREADY defined — do not re-shard.)
14. **Shorten the 7 monster contracts** (373w/299w/269w/250w/237w/222w/193w) by
    moving their inlined notation preambles to the new defs; single minimal
    implication each. Directly unblocks af elevation of the top queue
    (lem-top-deficit-price: 8 consumers, gated on this).
15. **Dep-hygiene spot fix**: audit `lem-top-concentration` (+ re-scan the empty-deps
    proved set) for undeclared premise edges; declare any real ones.

## PHASE 3 — docs & process streamlining (recurring-tax removal)

16. **`docs/plans/CURRENT.md` generated pointer** (3-line generator, gated in
    check-all): all pins (CLAUDE.md router, AGENTS.md, HANDOFF §2, the bd memory)
    reference CURRENT.md once, never sed-bumped again. Kills the pin-sprawl bug class
    (4 bumps today, 1 missed).
17. **Two-tier sketch versioning**: sub-50-line single-wave deltas -> rolling
    `docs/plans/CHANGELOG.md` (append-only, no pin bump); a new numbered sketch file
    ONLY at session close or when the Tier-1 leaf set changes. (Today's v20-v24 = 5
    files + 5 pin rounds would have been 1 file + 4 changelog lines.)
18. **`scripts/codex-dispatch.sh`** — reusable quota-probe + retry-with-backoff +
    durable logging wrapper (generalizes the twice-proven scratchpad dispatcher; no
    hardcoded epochs).
19. **`scripts/build-workspace.sh <target-id> [--include-waves ...]`** — reproducible
    self-contained worker-workspace assembly from repo state (the W56 rebuild cost is
    the recorded incident).
20. **`scripts/register-oracle.py <rid>`** — appends the parametric af-validated
    oracle entry (replaces 29 hand-copied portfolio.json edits).
21. **Reconcile `.frontier/portfolio.json` arms with reality**: arm B's text is ~40
    cycles stale (Rule-9 drift in the controller); re-seed the arms as the six live
    leaves (H-D, H-I, H-X-generalization, SL1b, L6.5-residuals, L5-minimax), park the
    vestigial A/C/D/E/F/G with an explicit tier1-override tag.
22. **Backfill the W59 wave-close doc** (verbatim verdict first-lines; source
    material already in worklog + af ledger) — the arc's highest-rigour artifact is
    the one missing its record.
23. **FINDINGS.md topic-index header**: group the 46 section anchors under
    DEAD-ROUTE / WALL / CONSTANT / CERTIFICATE tags (Rule-13 lookup should not depend
    on guessing the right grep term across 918 lines).
24. **Re-scope `report/` as the paper-track** (T0 results + thin open spine, NOT a
    registry mirror; update CLAUDE.md §5 + the stale "seven af-validated" sentence in
    00_overview.tex) and **write the 13 missing T0 shards** — 13 fully rigorous
    results including lem-starvation-completion-obstruction currently have zero
    presence in the document meant to narrate what is proved. [batched routine wave]
25. **Beads cross-device sync — USER DECISION** (file as a bead): recommend option
    (b) committed JSONL export riding the existing git backbone (no new external
    dependency, consistent with Rule 12); alternatives: DoltHub remote (real merges,
    external credential) or explicit accept-local-only. The failure already occurred
    once (the cycle-319 reconciliation).

## Sequencing recommendation

Phase 0 today (minutes). Phase 1 before the next proof wave — the fixes protect every
subsequent wave and two of them are CRITICAL holes in the fabric-of-trust. Phase 2 as
one dedicated codification wave (it is registry work — schedule it when no af
orchestration is running, per the overreach guard). Phase 3 items 16-21 opportunistic
(each is standalone); 22-24 as one batched docs wave; 25 awaits the user.
