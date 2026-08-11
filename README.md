# almost-idempotent-stochastic-maps

A research lab that searched for, found, and adversarially validated a proof of a classical stability
theorem about almost-idempotent stochastic matrices. The search was run by orchestrated LLM agents under a
strict rigour regime — one canonical definition per term, byte-verbatim provenance for every citation, an
enforced acyclic contract DAG, reviewer never author, and machine-adversarial proof trees in which a fresh
prover and a separate fresh verifier per node are rewarded for breaking the argument. The proof, the
search log, the dead routes, and the retraction ledger are all in the open.

## The theorem

<!-- statement + constants: argument/lemmas/op-classical.md (contract line, and the T0 note giving
     eta_0 = eta_K, C = K+4*sqrt(2K)); identical statement in paper/main.tex Theorem 1 (thm:main). -->

> **`op-classical`.** There are universal constants `η₀, C > 0`, independent of the dimension `n`, such
> that every row-stochastic `Q : ℓ∞ⁿ → ℓ∞ⁿ` with
>
>     ‖Q² − Q‖_{∞→∞} ≤ η ≤ η₀
>
> admits a stochastic idempotent `E` (row-stochastic, `E² = E`) with
>
>     ‖Q − E‖_{∞→∞} ≤ C·√η .
>
> The exponent `1/2` is sharp: no uniform estimate with `η^β`, `β > 1/2`, can replace it (carried by
> `cor-classical-sharpness`, below).

**Upper bound: proved · af-validated (2026-08-08)** — via Route F (an exact diagonal seam into the
completely bounded setting, Kitaev's approximate-algebra factorization with an audited repair of its
diagonal step, then a descent back to the stochastic category).
**Sharpness: proved · af-validated (2026-08-09)** — carried by `cor-classical-sharpness` on an explicit
4×4 witness family.
<!-- both dates + both statuses: argument/lemmas/op-classical.md, argument/lemmas/cor-classical-sharpness.md
     (status: proved / af: validated), echoed in HANDOFF.md START HERE and llms.txt "Status". -->

### The honest boundary

- **`af`-validated is rung (b) of this repo's rigour ladder** (`CLAUDE.md` L0): validated in an `af`
  workspace by the adversarial protocol. It is **machine-adversarial validation, not a Lean/mathlib
  proof** (rung (c), the top rung) and **not peer-reviewed publication**. **No Lean proof of anything in
  this repo exists.** Per inference, `af` is weaker than a proof-assistant kernel check. <!-- proofs/README.md "The honest
  boundary"; GLOSSARY.md "rigour ladder / rung (b)"; paper/main.tex footnote after Theorem 1. -->
- **The constant is not numerically pinned down.** The validated ledger gives `η₀ = η_K` and
  `C = K + 4√(2K)` for a universal `K ≥ 1` inherited from unnamed constants in the source, so only
  `C ≥ 1 + 4√2 ≈ 6.657` is known. <!-- argument/lemmas/lem-routef-k-ledger.md contract; paper/main.tex
  §1 ("For the explicit universal K>=1 …"); the numeric floor is stated in the sibling repo's
  README (aic_stoch section) citing its paper/FINDINGS.md §C24. -->
- **Sharpness in the signed (`δ`) parameter has no rigorous carrier**, and the earlier `ex-hume` contract
  is retracted as `disproved`. <!-- HANDOFF.md §"What is intentionally NOT here"; docs/LEARNINGS.md
  2026-08-08 entry. -->
- Everything below rung (b) is tagged in the open: `proved-mod-audit`, `conjecture`, `heuristic`,
  `numerical`, `stated`. Numerical agreement is evidence, never proof.

## The Swiss-Cheese Defense

The claim this repo makes about *itself* is defence in depth: six error-catching layers — vocabulary and
provenance, the contract DAG and its linker, hostile review with reviewer ≠ author, `af` adversarial
proof trees, meta-audit sweeps, and oracles/numerics/tripwires — each with known holes, whose holes do not
line up. Each retraction so far was caught downstream of layers that had already passed it. The
backstop is the retraction ledger `docs/LEARNINGS.md`, whose own header calls a retraction "a SUCCESS of
the rigour machinery, not an embarrassment".

Measured record (all figures generated from the repo by `scripts/gen-site-data.py` into
[`site/data/defense.json`](site/data/defense.json); never quote a defence number from prose):

- **435** challenges raised and **428** resolved across **2,819** node validations by fresh verifiers who
  never proved the node they judged;
- **7** dated retractions, each attributed to the layer that caught it (3 at hostile review, 1 in an `af`
  tree, 3 in meta-audit sweeps) — the attribution is a keyword heuristic over the ledger text, as
  `site/data/defense.json` says in its own notes;
- **16** balloon-tripwire aborts (a proof tree outgrowing its node budget is treated as a symptom, not
  something to push through) and **3** registry claims disproved.

The full story, layer by layer with its known holes, is the site's Defense page
([`site/defense.html`](site/defense.html)).

## Where to start

**If you are a mathematician.** Read [`paper/main.tex`](paper/main.tex) — 4 pages, self-contained, the
statement and the route. Then [`report/main.pdf`](report/main.pdf) — the 302-page internal lab book, one
`\section` per shard, reproducing the af-validated results with a provenance row each. Then the
interactive site: [`site/`](site/) — the Theorem page with a live 4×4 sharpness witness
([`site/index.html`](site/index.html)), the Defense page ([`site/defense.html`](site/defense.html)) and
the Proof Atlas ([`site/atlas.html`](site/atlas.html)), all rendering from the machine-readable layer
([`site/data/*.json`](site/data/) — DAG, statuses, contracts, retractions, runs, defence counts). View
locally with `python3 -m http.server -d site`; the hosted URL is pending the GitHub Pages flip.
<!-- 4 pp and 302 pp verified by pdfinfo on paper/main.pdf and report/main.pdf; paper/main.pdf is
     gitignored, hence the link to the .tex. -->

**If you are an auditor.** Start at [`proofs/README.md`](proofs/README.md) — it contains a 20-minute audit
recipe that walks from the root export down through an import chain to a challenge, its resolution, and a
byte-matched quote, naming the real files and event ids. [`GLOSSARY.md`](GLOSSARY.md) decodes the process
vocabulary (`af`, `fr`, T0, banking, waves, arms, the rungs). [`docs/LEARNINGS.md`](docs/LEARNINGS.md) is
the retraction ledger and [`FINDINGS.md`](FINDINGS.md) the dead-route certificates. Then check the whole
thing yourself:

```sh
sh scripts/check-all.sh        # the single gate; prints "[check-all] OK"
```

Stdlib Python 3 and `sh` only — no network, no CI, no API keys, no dependencies to install; a few seconds
on a laptop (plus an optional LaTeX rebuild when `latexmk` is installed). It runs the definitions gate, the byte-verbatim refs provenance gate (**1,133** registered
externals: 30 quotes string-matched against local sources, 1,080 workspace-to-workspace imports, 23
carrying no extractable quote), the argument linker (acyclicity, contract-match, status propagation), the
numerics gate, the generated report layers, and the site-data freshness gate. A stale or overclaimed
number fails the build. The gate certifies provenance, structure and freshness — never mathematical
truth; only reading the `af` ledgers (the audit recipe above) does that. <!-- steps: scripts/check-all.sh lines 10-61; externals split:
site/data/defense.json L1 metrics and proofs/README.md; timing measured at 6 s on this machine. -->

**If you are curious about the method.** The site's Defense page ([`site/defense.html`](site/defense.html))
is the headline exhibit; its specification, and the whole communication plan, is
[`docs/plans/2026-08-11-communication-artifacts-plan.md`](docs/plans/2026-08-11-communication-artifacts-plan.md).
The search itself is in [`.frontier/`](.frontier/) — an append-only log of 1,300+ recorded exploration
decisions (which direction was pulled, what came back, whether it was banked, made progress, died, or was
refuted), plus the portfolio of research arms it allocated attention across.
<!-- .frontier/log.jsonl: 1,302 records at time of writing; stats.json records 1,301 (one appended since
     the last generation). "1,300+" is the safe form. -->

## Run the theorem

The sibling repository [`almost-idempotent-channels`](https://github.com/tobiasosborne/almost-idempotent-channels)
ships `aic_stoch`, a constructive implementation of this theorem in exact rational arithmetic (FLINT
`fmpq`, no floating point, no tolerances): give it any row-stochastic `Q` and it returns an **exact**
stochastic idempotent `E` together with an exact certificate — `η`, `δ = ‖Q−E‖_{∞→∞}` and the ratio
`r² = δ²/η` as exact rationals, with `E² = E` and row-stochasticity checked with zero tolerance. Because
`C` is non-explicit, the certificate reports the achieved ratio rather than asserting the theorem's
constant; the test suite pins per-fixture envelopes and keeps the 4×4 sharpness floor `δ ≥ √(η/2)` as a
live test tooth — an implementation that beats that floor has returned a wrong `E`.
<!-- every claim in this paragraph is from that repo's README.md, "The classical stochastic module
     (C, exact rational)" section; git remote confirms the GitHub URL. -->

## Repo map

| Path | What it is |
|---|---|
| [`PRD.md`](PRD.md) · [`CLAUDE.md`](CLAUDE.md) (== [`AGENTS.md`](AGENTS.md)) · [`HANDOFF.md`](HANDOFF.md) | scope · the working laws and gates · current state and next steps |
| [`definitions/`](definitions/) | one canonical, provenance-gated shard per term (47 of them); drift is a build failure |
| [`argument/`](argument/) | one shard per result: a one-line contract, its imports, and an honest status — the knowledge DAG (374 results, **200 of them af-validated**; generated [`INDEX.md`](argument/INDEX.md) and Mermaid [`DAG.md`](argument/DAG.md)) |
| [`proofs/`](proofs/) | the `af` workspaces: append-only event ledgers, byte-matched imports, and rendered `export.md` proof trees |
| [`report/`](report/) | the sharded LaTeX lab book ([`main.pdf`](report/main.pdf), 302 pp) with a provenance row per reproduced claim |
| [`paper/`](paper/) | the paper track — [`main.tex`](paper/main.tex), 4 pages |
| [`runs/`](runs/) | 38 numerical run bundles, each with a re-run command, a schema and a checkable invariant — evidence, never proof |
| [`refs/`](refs/) | ground truth: source payloads (gitignored for copyright and size) plus a tracked SHA256 manifest |
| [`site/`](site/) | the browsable site (Theorem · Defense · Atlas) and the generated machine-readable data layer it renders from |
| [`docs/`](docs/) | history and the inherited record: [`LEARNINGS.md`](docs/LEARNINGS.md) (retractions), `worklog.md`, `plans/`, `waves/`, `ingest/` — see [`docs/README.md`](docs/README.md) |
| [`GLOSSARY.md`](GLOSSARY.md) · [`CONVENTIONS.md`](CONVENTIONS.md) · [`FINDINGS.md`](FINDINGS.md) · [`INDEX.md`](INDEX.md) · [`llms.txt`](llms.txt) | process vocabulary · notation and rungs · gotchas and dead routes · the evidence manifest · the machine-readable map |
<!-- counts: site/data/stats.json (definitions 47, registry_total 374, run_bundles 38); page counts by
     pdfinfo; every path checked to exist with ls. -->

## Tooling

Two external tools of the same author drive the machinery: **`af`**, the Adversarial Proof Framework that
hosts the proof trees ([github.com/tobiasosborne/vibefeld](https://github.com/tobiasosborne/vibefeld)), and
**`fr`**, the explore/exploit controller that ran the search (link forthcoming). The `af` provers and
verifiers are external `codex` runs; the orchestrating agent dispatches them and never judges a proof.

**Verifying this repository needs neither tool** — `sh scripts/check-all.sh` is stdlib Python and `sh`.
Extending it (new `af` trees, new exploration waves) needs `af`, `fr` and the `codex` CLI.

## Licence and citation

Licensed under the **GNU Affero General Public License v3.0** — see [`LICENSE`](LICENSE). The network
clause (§13) applies: if you run a modified version to offer a service over a network, you must make the
modified source available to its users. Copyright © 2026 Tobias J. Osborne.

If you cite this work, cite the repository (naming the commit, and the status verbatim from
`argument/INDEX.md` — "af-validated" is neither "Lean-verified" nor "peer-reviewed"), together with the
quantum theorem whose classical shadow this is:

> A. Kitaev, *Almost-idempotent quantum channels and approximate C\*-algebras*, arXiv:2405.02434v2, 2025.
<!-- bibitem verbatim from paper/main.tex thebibliography; refs/kitaev-2405.02434/ is the pinned local
     source that Route F's quotes byte-match against. -->
