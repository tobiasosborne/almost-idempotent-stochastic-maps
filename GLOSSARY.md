<!--
ROLE: plain-language glossary of this repo's process jargon, for a reader arriving from outside.
Terms of ART about the machinery, not mathematical definitions — those live one-per-shard in
definitions/ (47 shards) and are indexed by definitions/INDEX.md.
UPDATE POLICY: add an entry when a term starts appearing in commits, HANDOFF, or shard prose.
-->

# GLOSSARY — the working vocabulary

Alphabetical. Mathematical terms are **not** here: every mathematical term has exactly one canonical
shard under `definitions/` (`CLAUDE.md` L2), listed in `definitions/INDEX.md`.

**`af`** — the Adversarial Proof Framework, the external tool that hosts this repo's machine-checked-by-
adversary proof trees. Public repository: `github.com/tobiasosborne/vibefeld`. Locally the binary is
addressed as `AF=${AF:-…}`; the workspaces it produces live in `proofs/<id>/` and are described in
`proofs/README.md`. The protocol wrapped around it is `CLAUDE.md` §6, driven by
`scripts/af-orchestrate.py`.

**arm** — a named research direction in the `fr` portfolio, the unit across which attention is
allocated. `.frontier/portfolio.json` currently holds 10: `A`, `B`, `C`, `D`, `E`, `F`, `R`, `G`, `FH`,
`XE`, each with a one-paragraph statement of what it is trying to prove. Arms are informal by design —
they are *directions*, not claims, and nothing in `argument/` depends on them.

**balloon** — a proof tree growing past its node budget, taken as a symptom rather than something to
push through. `scripts/af-orchestrate.py` aborts on it (the "balloon tripwire") and the abort is
classified: a missing fact, a dependency that should be factored into its own registry lemma, or a
genuine gap. The shared size constant is `NODE_SOFT_CAP = 26` in `scripts/af_constants.py`, read by
both the orchestrator and the linker so the two cannot drift.

**banking** — recording an exploration result as *achieved*. A result is banked only when an external
oracle passes, never on the agent's own say-so; for `af` work the oracle is
`scripts/oracles/af-validated.py`, which re-reads the workspace ledger and passes only if the root
statement matches the registry contract, the root state is `validated`, and every node's taint is
clean. Its docstring puts the reason plainly: "The oracle's authority is the codex-built af ledger — an
artifact external to the orchestrator (reviewer ≠ author)."

**`bd` / beads** — the issue tracker, backed by a local Dolt database under `.beads/`. All task
tracking goes through it; markdown TODO lists are forbidden (`CLAUDE.md` Rule 8). Issue ids look like
`aism-xvcq`.

**byte-matched / ground-truth ref** — the strongest provenance this repo can offer for a claim taken
from the literature: the quoted text is string-matched, character for character, against a local copy
of the source under `refs/`. Enforced by `scripts/check-refs.py` on every commit (current run: 1133
externals, 0 failed). Anything weaker — a paraphrase, a recollection, an unlocated citation — is not
`cited` and may not be used as though it were. `refs/` payloads are gitignored for copyright and size;
`refs/manifest/checksums.sha256` is the tracked record of what was matched.

**circuit breaker** — the `fr` mechanism that stops a session from grinding on a stalled direction.
`fr check --hook stop` is wired as the harness `Stop` hook in `.claude/settings.json`, so a turn that
ran a wave cannot end until the wave's outcome is logged and a decision (EXPLOIT / EXPLORE / PIVOT) is
recorded. A stalled arm must yield. `CLAUDE.md` Rule 5 marks the breaker non-negotiable.

**`codex`** — the external LLM runner (`codex exec`, model `gpt-5.6-sol`) that supplies the `af`
provers and verifiers. It matters that it is *external*: the orchestrating agent dispatches codex
workers and does bookkeeping, and never judges a proof itself. Reasoning effort is capped at `xhigh`.

**`conj-` prefix** — **a naming artifact, not a status.** Registry ids keep the prefix they were born
with. `conj-extcb` and `conj-hcb` both read `status: proved`, `af: validated` in `argument/INDEX.md`
despite the prefix; `conj-kernel` and `conj-ex` really are conjectures. **Read the status column, never
the id.** The same applies in reverse to the other prefixes (`lem-`, `thm-`, `prop-`, `cor-`, `op-`,
`obs-`) — they say what kind of statement it is, not how well established it is.

**contract** — the one-line statement of a result, carried in the `contract:` field of its
`argument/lemmas/<id>.md` shard. It is the anti-drift single source of truth: the lab-book and the
proof workspaces *reference* it rather than restating it, and `scripts/argument.py` fails the build if
an `af` workspace's root conjecture stops matching it verbatim ("contract drift", `argument.py:247`).

**dead route / death certificate** — an approach recorded as closed, with the reason written down so it
is not silently re-walked. They accumulate in `FINDINGS.md`, dated, often with an explicit
counterexample. `CLAUDE.md` Rule 13 forbids re-walking them without first reading the certificate and
escalating.

**`fr`** — the explore/exploit controller CLI that runs the search campaign. State is
`.frontier/log.jsonl` (append-only, 1300 records) plus `.frontier/portfolio.json`. It defines the turn
ritual — dispatch, harvest, log one record per arm pulled, end on a decision — and enforces it through
the circuit breaker. Its own help text is the reference: `fr help`, `fr help <topic>`. (`fr` is a
public repository of the same author; the URL is not yet wired into this repo.)

**harvest** — collecting a wave's subagent results and logging the outcome to `fr`, one record per arm
pulled. The permitted outcomes are `banked` (requires an oracle pass), `progress` (requires a named
artifact), `died` (requires the point of death), `refuted`, and `null`. Turns that ran no wave are
recorded separately and do not count as pulls.

**L0–L5** — the five Laws in `CLAUDE.md` §1, the constitution of the repo.
L0: the rigour ladder is sacred and non-rigour is flagged loudly.
L1: ground truth before claims — every cited claim byte-matches a local source.
L2: one canonical definition per term, no naked symbols.
L3: numerics are evidence, never proof, and reproducibility is part of the result.
L4: atomic, validated, accretive — the argument is an enforced acyclic DAG.
L5: reviewer ≠ author; internal convergence is not correctness.

**mod-audit / `proved-mod-audit`** — the registry status for a paper-proof that has *not* cleared an
independent reviewer or an `af` pass in this repo. `CONVENTIONS.md` §(a) lists it as **not rigorous**
and calls it "the workhorse status for inherited results". It is the honest tag for most of what
arrived from the inherited campaign in `docs/ingest/`. The linker refuses to let an `af: validated`
result depend on one.

**rigour ladder / rung (b)** — the ordering that decides what may be called rigorous (`CLAUDE.md` L0,
tabulated in `CONVENTIONS.md` §(a)). Rigorous: **(a)** byte-matched to a genuine theorem in a local
published source; **(b)** `af`-formalised, i.e. validated in an `af` workspace by the adversarial
protocol; **(c)** Lean-formalised, `sorry`-free against mathlib — the top rung. Everything else —
`stated`, `proved-mod-audit`, `conjecture`, `heuristic`, `numerical` — is non-rigorous and must say so.
Almost all of this repo's rigorous content sits at rung **(b)**. **No Lean proof exists here**, so no
claim in this repo has reached rung (c).

**T0** — shorthand for the `af`-validated tier: a result "is at T0" when its `argument/` shard carries
`af: validated`. Written as a count, "T0 = 200" means 200 of the 374 rows in `argument/INDEX.md` carry
that field. It is a count of rung-(b) results, not of theorems believed true.

**wave** — one dispatch of subagents against a task, and the unit of exploration accounting: one turn
= one wave = one `fr log` per arm pulled. Wave outputs are written up as dated artifacts under
`docs/waves/` (early) or `docs/plans/*-artifacts/` and `*-design/` (later); see `docs/README.md`.

**W\<number\>** — the wave counter used in commit messages, `HANDOFF.md`, and directory names, e.g.
`docs/plans/2026-07-22-W73-artifacts/`, `docs/plans/2026-08-09-W140-REPORT-SYNC/`. Numbering runs
forward across the whole campaign; W140 is the highest referenced in `docs/`. Not every wave left a
directory, so the numbers have gaps.
