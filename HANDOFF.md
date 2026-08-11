<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. The proof sketch is `docs/plans/CURRENT.md` → **v53** (current).
3. **BOTH HALVES OF `op-classical` ARE AT THE AF-VALIDATED RUNG.**
   T0 = **200**, registry = **374**. Upper bound: `op-classical`
   (discharged 2026-08-08, Route F). Sharpness: `cor-classical-sharpness`
   (banked 2026-08-09). Honest boundary: af-validated rung only — **NO
   Lean/mathlib proof exists**; `ex-hume` remains `disproved`;
   signed-parameter (δ) sharpness has NO carrier.
4. **THE PROJECT GOAL HAS PIVOTED (user, 2026-08-10): make the repo
   SHAREABLE and WELL-DOCUMENTED.** The mathematical campaign is parked
   (paper polish + optional Lean/legacy remain user-elevation-only).
   The new campaign epic is **`aism-xvcq`**. This session (47) ran the
   whole-repo state survey (9 parallel sonnet surveyors, one per area);
   the findings are synthesized below and are the working basis for the
   documentation campaign. **Session ended before the user answered the
   three framing questions (§ "USER DECISION PENDING") — get those
   answers (or proceed on Phase-1 hygiene, which needs no answers).**

## SESSION-47 RECORD (2026-08-10, repo-state survey)

Nine read-only subagent surveys: root docs · definitions · argument ·
proofs · report+paper · runs · refs+ingest · scripts+infra · docs
history. `check-all.sh` independently re-verified green (~9.5s). No
repo content was changed this session (survey + this handoff only).

### Survey synthesis — the bottom line

Repo **content** is healthy: theorem genuinely banked, all gates green,
statuses honest, integrity layers pass. The repo's **front door is
broken**: `README.md` still says the theorem is UNSOLVED, and nothing
at root level points an outsider at the proof. The shareability gap is
a documentation/navigation gap, not a content gap.

### Assets to build on (verified this session)

- `paper/main.tex` — finished, readable, self-contained 4-page paper
  (seam → factorization ledger → descent → §5 with the explicit 4×4
  sharpness witness `A_λ`,`M_λ`,`Q_λ`), honest rigour footnote. THE
  natural public artifact. Bead `aism-aywn` holds it for user polish
  only (note: that bead's "sharpness human-audited only" note text is
  itself stale — the footnote correctly says af-validated).
- `report/main.pdf` — 300pp, committed, current with HEAD (incl. W140
  shards 52–72).
- Argument DAG — 374 results, 0 linker errors (15 cosmetic brittleness
  warnings). Proved core: `op-classical` = 156-node af-validated
  Route-F closure, disjoint from the 44-node legacy signed route
  (honestly blocked on 12 conjectures). `cor-classical-sharpness` is a
  3-ancestor island. `--closure-min op-classical` reproduces the
  156/44 split; it is written down NOWHERE — a doc target.
- `proofs/` — 202 validated workspaces with human-readable `export.md`;
  registry↔workspace bijective, zero orphans; gitignore discipline
  correct. Bulk = 69MB/17.5k ledger JSONs (legitimate audit trail).
- Integrity: defs 47 shards 0 errors (11 expected draft warnings —
  exactly the 10 backup-route "huddle-charge" defs + θ-idempotent);
  refs all 23 payloads SHA-OK, 0 byte-match failures across 1133
  externals; runs 38 bundles 0 errors, exact rational arithmetic,
  spot-rerun reproduced output byte-for-byte.
- `docs/LEARNINGS.md` — 8 dated retractions incl. 9 af-validated
  results de-banked for inference bugs + the ex-hume disproof. The
  credibility engine; candidate headline material when sharing.
- `.frontier/` — 1283-entry log + portfolio: full 46-session "show
  your work" record, tracked and shareable.
- `report/generated/defs/` already renders 46/47 definitions as a
  dependency-ordered 3-layer LaTeX tour — point readers THERE, not at
  raw `definitions/` (only `def-pivot` is dropped, by policy).

### Defects found (ranked; Phase-1 hygiene targets)

1. **`README.md` contradicts reality** (frozen 2026-07-07): says the
   central question is unsolved; never mentions paper/report PDFs.
   Biggest single fix.
2. **Stale report-layer counters**: meta-shards 39–41 still say
   "forty-seven results reproduced" and MAIN-CB "not reproduced here"
   (false since shards 52–72); `report/PROVENANCE.md` header says
   "112 af-validated" vs true T0=200. `paper/main.pdf` (local,
   untracked) is one commit behind `main.tex` → rebuild before sharing.
3. **Evidence-layer manifests half-stale**: root `INDEX.md`
   script→output table stops at W25 (19 bundles missing);
   `data/SCHEMA.md` misses `nsc_pair_table.csv` + `floor_table.csv`;
   `check-runs.py` does not gate SCHEMA sync (staleness invisible to
   the gate — consider adding the check).
4. **External-cloner breakage**: hardcoded `/home/tobias/...` (wrong
   user!) AF fallbacks at `scripts/af-orchestrate.py:45`,
   `scripts/seed-af-workspaces.py:26`, `scripts/oracles/af-validated.py:29`;
   absolute repo path at `scripts/land-ledger-domains-rows.py:36`;
   tracked prose points at private siblings (`../vibefeld`,
   `../almost-idempotent-positive-maps`); NO setup/install docs for
   the four bespoke CLIs (`fr`, `bd`, `af`, `codex` — af/fr not
   public); only 3/10 refs auto-fetch-reproducible (7 cache-only; 3 of
   those are open-access URLs a human can refetch; the
   `absent-acknowledged.json` digest-bound WARN mechanism is the
   existing precedent for missing payloads). GOOD NEWS: the
   read/verify path (`check-all.sh`) is stdlib-only and runs anywhere.
5. **Navigation vacuum**: no `proofs/README.md` (workspace anatomy —
   ledger/externals/meta tracked, export.md = the readable artifact —
   must be reverse-engineered); no `docs/README.md` (worklog/plans/
   waves split unexplained; `docs/waves/` silently stops ~W70/2026-07-16,
   later waves live in `docs/plans/*-artifacts|*-design`); `argument/DAG.md`
   unbrowsable at 374 nodes/860 edges; 53 superseded proof sketches
   unindexed (only CURRENT.md disambiguates); repo-wide unglossed
   jargon (T0, af, fr, bd, banking, waves, arms, rigour rungs);
   `conj-extcb`/`conj-hcb` etc. are PROVED despite the `conj-` prefix
   (naming artifact worth a note).
6. **Minor**: `scripts/tests/test_gen_report_stats.py` not wired into
   the check-all test loop; ~157 empty local-only stub dirs in
   `proofs/` (untracked, safe to delete); 129MB stale
   `.claude/worktrees/`; redundant promoted subdirs in `refs-staging/`
   (untracked); `docs/ingest/OVERVIEW.md` refs `refs/hognas-mukherjea-2011/`
   (actual dir has no `-2011`); 3 pinned refs uncited by any shard
   (baake-sumner, salzmann-bergh-datta, cairns-1935 — parked, cairns
   superseded by munkres per SOURCES.md).

No deletions needed for size/licensing: copyrighted PDFs correctly out
of git, no secrets found (checked .beads config, .claude/settings.json).

## NEXT SESSION (ranked)

**THE CAMPAIGN PLAN IS RATIFIED (2026-08-11):
`docs/plans/2026-08-11-communication-artifacts-plan.md` — "The
Glass-Box Lab". Headline deliverable: the QUANTIFIED Swiss-Cheese
Defense (user mandate: this is more than a Lean formalisation — six
independent error-catching layers whose composition catches what each
misses; counts in the plan: 435 verifier challenges / 2,819 node
validations / 381 amendments / 9 de-banked certificates / 16 balloon
aborts / 3 disproofs / 8 attributed retractions). Rendered proposal:
https://claude.ai/code/artifact/6d0be821-6f3d-4780-b65d-d546b30989b2**

1. **Phase 0 — hygiene pass** (plan §Phases; needs NO user input):
   fix defects 1–3 + 6 above; rebuild `paper/main.pdf`; path
   fallbacks; wire the missing test; bead triage. Gate + commit per
   step. (README rewrite moved to Phase 2 — content-bearing,
   reviewer ≠ author.)
2. **Phase 1 — site data layer** (plan slate J): JSON exporters +
   `llms.txt` + `check-site` gate.
3. **Phase 2 — front door + core**: README (A) · Theorem page (B) ·
   Defense headline page (G) · Proof Atlas MVP (C).
4. Paper polish (`aism-aywn`) — still awaiting user feedback.
5. Lean/mathlib — top rung, ONLY on user elevation.

## USER DECISIONS (asked 2026-08-10 — ANSWERED 2026-08-11, ratified)

1. **Audience/venue:** public GitHub repo + GitHub Pages (committed
   `site/`, no Actions — Rule 12 intact) + arXiv eventually.
2. **Honesty story:** FRONT PAGE — folded into the Swiss-Cheese
   Defense headline.
3. **Tooling:** premise corrected — `af`
   (github.com/tobiasosborne/vibefeld) and `fr` are BOTH public repos
   of the user; link + document install on the Defense page. Verify
   path stays stdlib-only. (fr repo URL: get from user in Phase 2.)
4. **Site residence:** in-repo `site/`, lockstep with the gates.

## Worked-pattern reminders (BINDING, carried forward)

- Elevation cadence, remedy ladder, and BALLOON discipline: see the
  session-46 HANDOFF (git 52af30fe) + docs/worklog.md 2026-08-09 entry.
  Unchanged: codex = `gpt-5.6-sol`, effort capped `xhigh` (`ultra`
  forbidden); fresh prover ≠ fresh verifier ≠ designer ≠ auditor;
  Claude orchestrates only and judges nothing.
- Report authoring at scale: the W140 pipeline
  (`docs/plans/2026-08-09-W140-REPORT-SYNC/README.md`); always check
  audit outputs for per-item verdicts (VACUOUS-run precedent recorded).
- Survey subagent reports (session 47) are NOT in the repo — this
  synthesis is the canonical record of them (conversation is not
  canonical; everything load-bearing was folded in here).

## Open beads

**`aism-xvcq` (NEW, P1 epic — the shareability campaign, this is the
live thread)**; `aism-aywn` (paper, awaiting user feedback);
`aism-wazy`, `aism-xjnc`, carried P1s unchanged. NOTE: many of the 45
"ready" beads (W55/W60-era waves, arm A/B attacks) predate the
discharge and are effectively superseded — a triage pass is a natural
Phase-1 side-task (close or defer with a note, don't silently delete).

## Gate

`sh scripts/check-all.sh` → `[check-all] OK` (verified this session,
~9.5s). No repo content changed this session besides HANDOFF.md,
docs/worklog.md, and the new bead. In flight at close: NOTHING (no af
runs, no codex, no worktrees).

## What is intentionally NOT here

- Any claim above the af-validated rung: **no Lean proof exists**.
- Any claim about signed-parameter (δ) sharpness: NO rigorous carrier.
- Any reopening of the legacy signed chain — user portfolio decision
  (sketch v53 §4 records the bridge idea and its risks).
