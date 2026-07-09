<!--
ROLE: how-to-work / process rules for any AI agent (Claude, codex, …) on this repo. (WHAT/scope lives in PRD.md.)
UPDATE POLICY: this file is IDENTICAL to AGENTS.md — edit both in the same commit (or `cp -f CLAUDE.md AGENTS.md`); never let them drift. Keep the BEADS INTEGRATION block (bd-managed) intact.
TRIGGER: a process/convention/tooling change, or a new standing rule from the user.
-->

# CLAUDE.md — how to work on `almost-idempotent-stochastic-maps`

> **This file is identical to `AGENTS.md`.** Edit both together; never let them drift (`cp -f CLAUDE.md AGENTS.md`).
>
> **Router.** *What is this project / what may I change?* → **`PRD.md`** (the entry point — read it first).
> *How do I work?* → this file. *Current state / next task?* → **`HANDOFF.md`** then `bd ready`.
> *Where's the exploration portfolio?* → `fr board` (the explore/exploit controller).
> *Where's the LIVE PROOF STRATEGY?* → the newest `docs/plans/*top-down-proof-sketch*` file
> (**v18, 2026-07-09 session 13 close**) — the MOST DYNAMIC artifact in this repo. **Keeping it reconciled with
> newly banked evidence is a first-class deliverable of every session (user mandate,
> 2026-07-06): a wave that changes the map without updating the sketch is incomplete work
> (Rule 9). Supersede by dated file; old versions stay intact for line citations.** *Notation?* →
> `CONVENTIONS.md`. *Open directions / refs to ingest?* → `RESEARCH_NOTES.md`. *Gotchas / dead routes?* →
> `FINDINGS.md`. *Retracted claims?* → `docs/LEARNINGS.md`. *The knowledge DAG?* → `argument/DAG.md`
> (Mermaid, generated). *The inherited campaign record?* → `docs/ingest/` (the classical-portfolio, honestly re-tagged).

**This is a *scientific-exploration* repo, not a manuscript-verification repo.** Our north star is an
**OPEN** problem: *a fully mathematically rigorous proof of the classical (stochastic) stability result*
`op-classical` — there exist universal constants `η₀,C>0` (dimension-free) such that every row-stochastic
`Q` with `‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀` admits a stochastic idempotent `E` with `‖Q−E‖_{∞→∞} ≤ C·√η` (sharp
exponent 1/2). We do not have the proof; we are searching for it. The starting ground truth is the
**ingested `classical-portfolio`** from `../almost-idempotent-positive-maps` (which reduced `op-classical`,
through audited and *mod-audit* steps, to a single open **Kernel / (EX) conjecture**) plus the pinned
classical/Markov literature (`PRD.md`, `refs/`).

**The single failure mode this project guards against: a confident, plausible, WRONG-or-overclaimed result
leaking into the rigorous record.** Everything below exists to make that hard — a strict rigour ladder with
loud flagging, ground truth before claims, one canonical definition per term, an enforced acyclic knowledge
DAG, reviewer ≠ author, an external verify gate, and an explore/exploit controller the model cannot skip.
**The repo is canonical; the conversation, memory, and prior-session summaries are NOT.** And in particular:
**the ingested classical-portfolio is a *starting point*, not an oracle — almost none of it is rigorous by
this repo's L0, and it must be re-established here, honestly tagged (§3).**

---

## 0. Read-order gate (by file name, not by number)

Before you ADD or CHANGE any mathematical content, you must have read: **`PRD.md`**, **this file**,
**`HANDOFF.md`**, **`definitions/INDEX.md`**, **`argument/INDEX.md`**, and run **`fr board`** (the live
portfolio). To add/edit a definition or a registry result also read the relevant schema
(`definitions/README.md` / `argument/README.md`); before any script/run/figure work read `runs/README.md` +
`data/SCHEMA.md`; before touching a flagged item or a dead route read `FINDINGS.md`; before ingesting from
the classical-portfolio read `docs/ingest/README.md`. If you have not read them, **STOP**: file a `bd` issue
blocked on the pre-read, and stop — do not improvise.

---

## 1. The Laws (non-negotiable)

- **L0 — The rigour ladder is sacred; non-rigour is flagged LOUDLY.** Every claim carries an honest
  `status:`. A result may be called **rigorous** ONLY if it is (a) **ground-truth ref'd** — byte-verbatim
  string-matched to a LOCAL published source under `refs/` (a genuine *theorem* there, not a heuristic); OR
  (b) **af-formalised** — validated in an `af` workspace by the adversarial protocol (§6); OR (c)
  **Lean-formalised** — a `sorry`-free Lean proof against mathlib (Lean is *not* our current goal, but it is
  the top rung). **Everything else is non-rigorous and must say so in the open**: `numerical` (never
  rigorous — L3), `heuristic` (asymptotic/informal arguments), `conjecture`, `stated` (transcribed,
  unchecked), and — the workhorse status for the inherited campaign — `proved-mod-audit` (a paper-proof
  that has NOT cleared an independent reviewer / af pass here). A non-rigorous claim used as if rigorous is
  the cardinal sin. **When in doubt, flag it.**
- **L1 — Ground truth before claims.** Every `cited` claim string-matches **byte-verbatim** to a local
  source under `refs/` (recompute the SHA256, `grep -F` the quote). No `cited` claim without a provenance
  row. If the source isn't in `refs/`, **STOP and ask** — never paraphrase from memory. PDF/extraction-level
  provenance is **flagged honestly**, never passed off as byte-verified. **A claim appearing in the ingested
  classical-portfolio (or in any paper) is `stated`/`proved-mod-audit`, not rigorous** — those are objects of
  study, not oracles of truth.
- **L2 — One canonical definition; no naked symbols.** Each term is defined **exactly once** in
  `definitions/`; `report/`, `argument/`, `proofs/`, `runs/` *reference* `def-<slug>` and never restate it.
  Two shards sharing a term/alias = drift = build failure. **No symbol may be used without a definition** —
  but **BSc/MSc-level textbook notions are common knowledge** (do not shard "stochastic matrix", "operator
  norm", "convex hull", "probability simplex"). A definition enters the DB only with a **local ground-truth
  provenance** (a `refs/` source id) or an explicit `consensus`/`original` tag. **Drift is death.**
- **L3 — Numerics are evidence, never proof; reproducibility is part of the result.** A numerical result
  (an LP/exact-arithmetic enumeration, a certified instance, a δ–H measurement) is **never rigorous** (L0).
  It is admissible only as a *run bundle*: `runs/<YYYY-MM-DD>-<slug>/` with a `README.md` (parameters,
  seeds, command line, headline finding, **honest scope**), the producing script, a `data/SCHEMA.md`
  contract, an `INDEX.md` row, and a checkable invariant (a known value, an exact certificate, or an
  independent recomputation). A number without a re-run command and a SHA256 is not a finding. *(The
  ingested 67k-instance record is exactly this: strong evidence for the linear law and (EX), and rigorous
  proof of nothing.)*
- **L4 — Atomic / validated / accretive; the argument is an enforced DAG.** Every result gets its own tiny
  registry shard with a one-line `contract` and honest `status`; **all knowledge is codified as an acyclic
  DAG of implications** (`argument/`, the linker enforces acyclicity). A proof tree that balloons (`>12`
  nodes / depth `>3`) is a **brittleness FAILURE** → factor into sub-lemmas. One atomic step per commit.
- **L5 — Reviewer ≠ author; internal convergence ≠ correctness.** A result is "rigorous" only when an agent
  who is **not** its author independently checks the statement AND the proof/provenance and signs off
  (verdict in the commit under a `Review:` line). For `af`, the *verifier* is a **fresh** agent, never the
  prover (§6). `fr check`/the linker certify **provenance and protocol**, not truth; only an external
  oracle (`fr verify`, a byte-matched ref, an `af`-validated tree, a Lean proof) reaches toward truth.

---

## 2. The Rules (numbered)

0. **Don't overclaim — tag status honestly.** The north star is OPEN. The honest headline of the inherited
   work is *not* "δ ≳ H²": along the realizable family the tight relation is **linear, `δ = H/2`**, and the
   `δ ≳ H²` envelope binds only because `H` is capped at `O(√δ)` by the exposedness window. The `√η`
   exponent in `op-classical` is nonetheless **sharp** (`ex-hume`). Never silently promote a
   `proved-mod-audit` / `numerical` / `conjecture` to `proved`.
1. **"Runs without errors" is never a passing test.** Every test/check asserts an invariant against a
   known-correct value (for gates: red→green — perturb to confirm RED, then restore; for numerics: an exact
   certificate or independent recomputation, not "it produced a number").
2. **Get feedback fast.** After any non-trivial change run the relevant gate (§4). The single local gate is
   `sh scripts/check-all.sh`.
3. **Reviewer ≠ author** for every substantive change. Pure-mechanical ops (`git mv`, regenerating an INDEX,
   a verbatim user-specified edit, an ingest-copy) are exempt — but say so.
4. **~200-LOC sharding everywhere.** One def per file, one result per registry shard, report/lab-book
   sections ≤~200 lines with a shard-metadata header; stable greppable ids
   (`def-`/`lem-`/`thm-`/`prop-`/`cor-`/`op-`/`obs-<slug>`); the generated `INDEX`/`DAG` files and the
   report `SHARD_CATALOG.md` are the lookup tables (**never hand-edit the generated ones**). No monolith.
5. **`fr` runs the exploration; you do not tunnel-vision.** Informal research directions are registered as
   `fr` **arms**; each exploration wave logs one `fr log` pull per harvested result; the FRONTIER is the
   single live open question (currently the Kernel/(EX) conjecture). The Stop hook's circuit-breaker is
   **non-negotiable** — a stalled arm must yield to EXPLORE/PIVOT. Never satisfy the referee with a
   paraphrased residual (§5 anti-gaming). Off-goal finds → `fr discover`, not a silent tangent.
6. **`af` (Layer 2) and Lean are opt-in per conjecture.** `af` orchestration (§6) is stood up for conjectures
   the user (or the portfolio) elevates — **Claude ONLY orchestrates; a fresh codex proves and a *separate*
   fresh codex verifies. Claude NEVER judges/verifies a proof.** Lean/mathlib is the top rigour rung but not
   our current goal; do not start a Lean or `af` workspace on a whim — follow the playbook in `HANDOFF.md`.
7. **A definition is never `(proved)`.** Tag literature defs `cited` (byte-matched), adopted defs
   `consensus`, project-introduced defs `original`. `consensus`/`original` lock only on recorded sign-off.
8. **Cross-session state → beads, never markdown TODO.** `bd` for ALL task tracking (no TodoWrite / markdown
   TODO lists). Persistent project knowledge → `bd remember`. (The harness's own `~/.claude` memory is the
   agent's private cross-session memory and is orthogonal — do not create in-repo `MEMORY.md` files.)
9. **Docs move in lockstep with content.** A change that leaves `HANDOFF.md`, a README, an `INDEX`, a
   report `SHARD_CATALOG.md`/`PROVENANCE.md` row, a `SCHEMA.md`, or a ledger stale is **incomplete work**,
   not a follow-up.
10. **Re-read these rules after every context compaction.** Then re-orient from the repo + `fr board`, not
    from the conversation summary.
11. **Non-interactive shell.** Use `cp -f` / `mv -f` / `rm -f` (`-i` aliases hang the agent). Do not run
    multiple `bd` commands in parallel (exclusive Dolt lock).
12. **No remote automation by default.** Local validation only (`scripts/check-all.sh` wired into
    `.beads/hooks/pre-commit`). No `.github/workflows/` unless the user asks. Never disable the pre-commit
    hook (no `core.hooksPath=/dev/null`).
13. **Do NOT re-walk the inherited dead routes.** They are recorded in `FINDINGS.md` with death certificates
    (e.g. raw-index path-product floors — refuted by the **cloning obstruction** for any `δ₀ ≥ 0.233`;
    coefficient-only LP support-cleanup; universal `C ≤ 2`; exists-exact-max-volume selectors;
    Jensen/convexity; canonical-`g` energy method; finite-corner-as-asymptotic). If tempted, read the
    certificate first and escalate.

---

## 3. Faithfulness callouts (things easy to get wrong here)

*(Live, dated detail + dead-route certificates in `FINDINGS.md`; retracted claims, once any exist, in
`docs/LEARNINGS.md`.)*

- ❌ **Treating the ingested classical-portfolio as rigorous.** It is a *campaign record*, honestly
  self-tagged PROVED-mod-audit / NUMERICAL / CONJECTURAL / OPEN / REFUTED. Only **one** classical result
  cleared an `af` validation upstream (`lem-classical-equiv`, the signed↔stochastic bridge). Everything
  else re-enters here as `stated`/`proved-mod-audit`/`conjecture`/`numerical` until re-established under L0.
- ❌ **"δ ≳ H²" as the mechanism.** The realizable-family relation is **linear `δ = H/2`**; the quadratic
  form is only the worst-case envelope (H capped at `O(√δ)`). State which one a claim rests on.
- ❌ **Raw-index path products.** Index-level path-product floors are refuted (cloning obstruction). Only
  **clone-invariant (quotient)** quantities may appear in a proof — this killed a whole family of attempts.
- ❌ **Frame-specific → frame-free.** The exact identity `dist₁(λ,Δ)=2·neg(λ)` gives `δ ≥ H/2` **in the
  canonical simplex frame**; the transferable (frame-free) statement is now carried by
  `conj-skinny-shadow-cap` (`lem-dual-localization` retired 2026-07-04: its transcribed contract was a
  distance tautology — see `docs/LEARNINGS.md`; Route B is vacuous in the skinny `μ→1` regime). Do not
  present the frame-specific proof as the general one.
- ❌ **Signed vs stochastic formulation drift.** Results live in an equivalent **signed** picture (exact
  idempotence, negative mass `δ`) linked to the stochastic picture by `lem-classical-equiv` up to universal
  constants. Always say which picture a bound is stated in, and cite the equivalence when crossing.
- ❌ **Numerical agreement ⇒ theorem.** 67k+ exact instances with `0` (EX)-violations is `numerical` (L3),
  quarantined to `runs/`, never promoted. Below the corner scale (`δ≈0.233`) the dangerous antecedent has
  *never been entered* — that is evidence, not a proof.

---

## 4. Build & test (verified commands)

```bash
sh scripts/check-all.sh                        # THE gate → prints "[check-all] OK"; non-zero fails commit
                                               #   = check-defs + check-refs + argument linker + check-provenance
                                               #     + runs-index check + report-shards check + TDD tests + report build
python3 scripts/check-defs.py --check          # definitions: drift/dedup + required fields + cited sha256 vs manifest
python3 scripts/check-defs.py --generate-index # regenerate definitions/INDEX.md  (generated — don't hand-edit)
python3 scripts/argument.py --check            # the LINKER (acyclic · imports · contract-match · status · brittleness · orphans)
python3 scripts/argument.py --generate         # regenerate argument/INDEX.md + argument/DAG.md  (generated Mermaid)
python3 scripts/argument.py                     # default: check + generate + print the ready/blocked frontier
python3 scripts/argument.py --show <id>        # one result's contract + deps/dependents + closures
python3 scripts/check-refs.py --check          # verbatim-quote provenance gate (byte-match af externals to refs/)
python3 scripts/check-provenance.py --check    # report/lab-book ↔ registry sync (labels/sources/status/overclaim)
python3 scripts/check-runs.py --check          # numerics: every runs/ bundle has README+schema+INDEX row + invariant
sh scripts/check-report-shards.sh              # sharded lab-book: master purity, shard headers, INDEX/CATALOG sync
python3 scripts/fetch-refs.py --status         # reproducible refs/ reconstruction: present/fetchable/cache/missing
cd refs && sha256sum -c manifest/checksums.sha256     # ground-truth integrity (payload gitignored)
cd report && make                              # latexmk -pdf → report/main.pdf (the internal sharded lab-book)

fr board                                       # the exploration portfolio + FRONTIER (run at session start)
fr status                                      # human-readable portfolio summary
fr help [<cmd>|<topic>]                         # the CLI self-documents — start here for fr
"$AF" --version                                # the af (Adversarial Proof Framework) binary (Layer 2, opt-in)
```

Tool locations (parameterise, do not assume PATH inside scripts): `fr` is on PATH (`~/.local/bin/fr`); the
`af` binary is `AF=${AF:-/home/tobias/Projects/vibefeld/af}` (or `~/go/bin/af`); the `af` prover/verifier
workers are fresh `codex exec` runs (require the `codex` CLI + `jq`). No API keys live in this repo.

---

## 5. Architecture — layers of the exploration

Mental model: **definitions = the vocabulary/types · each result = a module whose *contract* is its
one-line statement and whose *imports* are the defs/lemmas it uses · a linker enforces the contracts and
renders the knowledge DAG · `fr` allocates attention across research directions · `af`/Lean discharge
elevated conjectures to the top rigour rungs.**

- **Layer 0 — `definitions/`**: one `def-<slug>.md` shard per term (provenance-gated). Gate: `check-defs.py`.
- **Layer 1 — `argument/lemmas/<id>.md`**: one shard per result; `contract` (one line) is the anti-drift
  single source of truth; `defs`/`deps` are the imports/DAG edges; `status`/`af`/`owner`. This is
  **the codified knowledge DAG of implications** — generated `INDEX.md` + `DAG.md` (Mermaid). Gate:
  `argument.py`.
- **Layer 2 — `proofs/<id>/`** (OPT-IN, `af`): one tiny `af` workspace per elevated conjecture; root
  conjecture **==** the registry `contract` (linker-enforced contract-match). Orchestrated per §6.
- **Sharded lab book — `report/`** (rigorous narrative, LaTeX, one ≤~200-line shard per `\section`, each
  with a `% SHARD-ID/TITLE/SUMMARY/KEYWORDS` header, indexed by `report/SHARD_CATALOG.md` +
  `report/PROVENANCE.md`) + **`runs/`** (numerical experiments, bundle-per-run) + **`INDEX.md`** (the
  evidence-layer manifest). Gates: `check-report-shards.sh`, `check-provenance.py`, `check-runs.py`.
- **Controller — `.frontier/`**: `fr`'s append-only `log.jsonl` + `portfolio.json`. Research **directions =
  arms**; a wave = a subagent dispatch; the FRONTIER = the one live open question. Derived board injected
  every turn; Stop-hook circuit-breaker enforces explore/exploit.
- **Ground truth — `refs/`**: `refs/<source-id>/` (local source payload, gitignored) + `refs/manifest/`
  (`SOURCES.md` + `checksums.sha256` + `sources.lock.json`, tracked). `refs-staging/` is untracked scratch
  for acquired-but-not-yet-ingested sources; promotion to `refs/` is a deliberate per-def step (L1).
- **Ingest — `docs/ingest/`**: the copied classical-portfolio material (OVERVIEW, kernel-conjecture,
  STATUS-LEDGER, DELIVERABLEs, seed experiments), read-mostly, the object of re-establishment. Never cited
  as rigorous (L1).
- **Layer 3 — `scripts/`**: the gates (`argument.py`, `check-defs.py`, `check-refs.py`,
  `check-provenance.py`, `check-runs.py`, `check-report-shards.sh`, `check-all.sh`, `fetch-refs.py`) +
  `af-orchestrate.py` + `seed-af-workspaces.py` + `oracles/` + `tests/`; `.beads/` mirrors the DAG as tasks.

**Anti-gaming (why the gates exist).** Internal convergence ≠ correctness. `fr check` certifies protocol,
the linker certifies structure, `check-refs` certifies provenance — none certify *truth*. A residual can't
be paraphrased away to satisfy the breaker; a self-reported "it's fine" is `stated`, never rigorous; a
non-zero oracle can't be upgraded by self-report. Only a byte-matched ref, an `af`-validated tree, a Lean
proof, or a passing external `fr verify` moves a claim up the rigour ladder.

**View the knowledge DAG:** `argument/DAG.md` (Mermaid, generated) + `argument/INDEX.md` (table);
`python3 scripts/argument.py` prints the live ready/blocked frontier. INDEX/DAG are generated — never
hand-edit them.

---

## 6. `af` formalisation (Layer 2, opt-in) — the extension-property orchestration protocol

`af` = Adversarial Proof Framework (`../vibefeld`; binary `AF=${AF:-/home/tobias/Projects/vibefeld/af}`). It
is **not** stood up on every result — only for a conjecture the user or the portfolio elevates. We adopt
**`../extension-property`'s protocol verbatim** (the codex prover/verifier discipline; that repo has 18
`af`-validated results, so the workflow is battle-tested) — **USER-MANDATED and non-negotiable**:

1. **Claude (the orchestrator) ONLY orchestrates — NEVER verifies.** Dispatch codex workers, run
   `af status/jobs/get`, do the shard/graph/commit bookkeeping. **Never re-derive/judge a proof, and never
   run `af accept`/`af challenge` yourself.** Reasoning about a step's correctness poisons your context (L5).
2. **Provers = fresh codex; verifiers = *separate* fresh codex; roles never mix.** Every prover is a
   brand-new `codex exec` (independent context); **every node is validated ONLY by a fresh codex verifier**
   — a new `codex exec`, told that finding a counterexample/gap/error is a BIG SUCCESS. Fresh per node;
   prover ≠ verifier ≠ challenger; bottom-up (a node reaches a verifier only once all its live children are
   `validated`). Quick form:
   `echo "PROMPT" | codex exec --skip-git-repo-check -C <repo> -s workspace-write -o ANSWER -`.
3. **Driver:** `python3 scripts/af-orchestrate.py <id> --workers N --max-rounds M [--node-cap 40]` run in the
   **background** (a single backgrounded call — no `nohup`/`&` wrapping that orphans it). One prover *build*,
   then rounds of {prover-fix ∥ fresh-per-node verifier} until root node `1` is `validated`. Guardrails:
   **prover-overreach guard** (abort if a prover dirties `definitions/`/`argument/` — so never edit those
   while an orchestration runs), **balloon tripwire** (abort at the node-cap with a classification:
   `MISSING fact` → provision a byte-matched def; `DAG dep` → FACTOR into registry sub-lemmas; `genuine gap`
   → stop — don't just bump rounds), and **stuck guard**.
4. **Contract-match:** seed with `af init -d proofs/<id> -c "<contract VERBATIM from the registry shard>"`
   (via `scripts/seed-af-workspaces.py`, `af: none→seeded`); register imports as byte-matched
   `af def-add`/`af add-external` (dep imports carry the literal `proofs/<dep-id>` path so `check-refs`
   recognises them). The linker enforces root ≡ registry `contract`. On clean `validated`, `af export` →
   `proofs/<id>/export.{md,tex}`, flip the shard `status`→`proved`/`af: validated` (a *mechanical* reflection
   of the codex ledger, not your judgment), regenerate, gate, commit. Track only `ledger/` + `externals/` +
   `meta.json`; gitignore the rebuildable caches.

The linker (`argument.py`) enforces: acyclic deps · imports resolve · **contract-match** · status
propagation (an `af: validated` result can never rest on a non-rigorous dep — a dep is available iff it is
itself `af: validated` or a `cited` leaf) · brittleness (`>12`/depth `>3` ⇒ REFACTOR) · orphans (registry ↔
`proofs/`).

---

## 7. Validation gates (declare which you exercised, per commit) — M/D/C/R/I

- **M**echanical — `check-all.sh` (and `cd report && make` if the lab-book changed) passes.
- **D**efinitional — every term used resolves to a `definitions/` shard; no restating; no naked symbols.
- **C**ross-reference — a cited claim byte-matches its `refs/` source at the recorded locus.
- **R**eviewer — an independent agent (≠ author) signed off.
- **I**dempotent — re-running the generators/gate yields the same state.

Risk tiers: trivial/mechanical = `M I`; an ingest-copy = `M I` (+ honest re-tag); a new numerical run =
`M I` + run-bundle discipline (L3); a new rigorous result = `M D C R I`.

---

## 8. Commit discipline

One atomic step per commit; split if two landed together. Message = imperative subject + a body that states
**what** and **why** and (for math) cites the source locus + which gates passed + a `Review:` line + the
`status`/rigour tag touched. Never amend a pushed commit. End every commit message with:
`Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.

---

## 9. Stop conditions (escalate to the user, don't improvise)

- A claim's ground truth is **not in `refs/`** (don't paraphrase from memory — L1).
- You'd add something **out of scope** per `PRD.md`.
- You're about to **promote a status up the rigour ladder** (numerical/heuristic/stated/proved-mod-audit →
  rigorous) without a byte-matched ref, an `af`-validated tree, a Lean proof, or an independent reviewer
  (L0/L5).
- A **contract drift / cycle / orphan** the linker reports that you can't resolve cleanly.
- A definition would need to **change** (it ripples through everything that references it).
- The `fr` circuit-breaker would need to be **relaxed**, or a PRD-locked decision changed.
- You're tempted onto a **recorded dead route** (Rule 13 / `FINDINGS.md`) and think "but this time…".

---

## 10. File map (canonical layout)

```
PRD.md                  WHAT/scope — the entry point (read first)
CLAUDE.md == AGENTS.md  HOW/process — this file
HANDOFF.md              current state + START HERE + next steps (rewritten each session, ≤500 lines)
README.md               public-facing "what is this / where to start"
CONVENTIONS.md          notation/normalisation registry (append-only, lettered) + rigour-rung table
FINDINGS.md             live subtleties/gotchas + dead-route certificates (dated)
RESEARCH_NOTES.md       open directions + reference-acquisition queue + deferred decisions
INDEX.md                evidence-layer manifest: script → run bundle → data → report shard
definitions/            Layer 0 — def-<slug>.md shards + README (schema) + INDEX (generated)
argument/               Layer 1 — lemmas/<id>.md shards + README + INDEX + DAG (generated Mermaid)
proofs/<id>/            Layer 2 — af workspaces (OPT-IN; orchestrated per §6)
report/                 internal sharded LaTeX lab-book (main.tex + sections/NN_*.tex) + SHARD_CATALOG.md
                        + PROVENANCE.md + Makefile
runs/<date>-<slug>/     numerical experiments — one bundle per run (README + data + figures)  [L3]
data/SCHEMA.md          CSV/column contracts for run outputs
refs/                   ground truth — <source-id>/ (gitignored payload) + manifest/ (tracked)
refs-staging/           untracked scratch for acquired-not-yet-ingested sources
docs/ingest/            the copied classical-portfolio (object of re-establishment; never cited as rigorous)
.frontier/              fr controller state — log.jsonl (append-only) + portfolio.json
scripts/                Layer 3 — check-all.sh · check-defs.py · check-refs.py · check-provenance.py ·
                        check-runs.py · check-report-shards.sh · argument.py · af-orchestrate.py ·
                        seed-af-workspaces.py · fetch-refs.py · oracles/ · tests/
docs/                   worklog.md (append-only history) · LEARNINGS.md (retracted claims) · plans/ · ingest/
```

## 11. Landing the plane (session close)

File follow-up issues → run gates → **log the exploration wave with `fr`** → update issue status →
`git pull --rebase` + `bd sync` + `git push` → verify → hand off. Work is **not** done until `git push`
succeeds — you push; never "ready to push when you are". Rewrite `HANDOFF.md` (don't append) and append a
dated `docs/worklog.md` entry. The mandatory checklist is the **Session Completion** block below (bd-managed).

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
