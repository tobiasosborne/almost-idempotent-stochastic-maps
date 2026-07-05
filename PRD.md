<!--
ROLE: WHAT this project is and what may/may not be changed (scope). The entry point — read first.
UPDATE POLICY: edit when scope, success criteria, or the open-question set changes. Date-stamp the
  "Current state" section. HOW-to-work lives in CLAUDE.md == AGENTS.md.
TRIGGER: a scope decision by the user, a result being verified/withdrawn, or a milestone change.
-->

# PRD — almost-idempotent-stochastic-maps

## Mission

Stand up a rigorous, byte-provenanced **research lab-book + exploration harness** for developing a theory
that delivers a **fully mathematically rigorous proof of the classical (stochastic) stability result**
`op-classical`. This is an **open research programme**, not a manuscript to transcribe: the classical case
was largely pursued in `../almost-idempotent-positive-maps` (the `classical-portfolio` sidequest), which
reduced it — through audited and *mod-audit* steps — to a single open input, but **no link of the chain is
rigorous in this repo yet**. The machinery here exists to keep that search honest and to close the gap at
the strictest level of rigour.

**The north-star theorem (`op-classical`, OPEN).** There exist universal constants `η₀, C > 0`
(independent of the dimension `n`) such that every row-stochastic matrix `Q ∈ ℝ^{n×n}` with
`‖Q² − Q‖_{∞→∞} ≤ η ≤ η₀` admits a stochastic idempotent `E` (row-stochastic, `E² = E`) with
`‖Q − E‖_{∞→∞} ≤ C·√η`. The exponent `1/2` is **sharp** (Hume's explicit 3×3 family `ex-hume`).

## The reduction chain (the thesis)

The classical result is studied through an equivalent **signed** formulation with EXACT idempotence
(`def-signed-idempotent`), linked to the stochastic picture up to universal constants by the (upstream
`af`-validated, here `proved-mod-audit`) equivalence `lem-classical-equiv`. Upstream reduced `op-classical`
through the chain

> `op-classical  ⇐  op-exposed-hull  ⇐  HLC (hull-linear-cap)  ⇐  Kernel/(EX) conjecture`

with the downstream steps `proved` / `proved-mod-audit` and the **single missing theorem-facing
input** (OPEN):
- **Kernel Conjecture** (geometric): universal `δ₀, B` s.t. every exact signed idempotent `P` with
  `δ(P) ≤ δ₀` has `W(P) ≠ ∅` and every hidden row vertex `v` with invisible mass `σ̃_v > τ = √δ` satisfies
  `dist₁(p_v, conv{p_w : w ∈ W}) ≤ B·τ`.

A second conjecture is a **separate attack route, NOT an equivalent form** (decision 2026-07-05,
adopting the DC4 audit redraw — no proved implication exists in either direction; see
`docs/waves/2026-07-05-DC4-equiv-assembly-audit.md`):
- **(EX) conjecture**: every rank-≥3 signed idempotent `P` with `δ ≤ ¼` has a θ-½ actual-row chart
  `U₀` with `max_s Φ_s(U₀) ≤ C₀·δ` (empirically `C₀ = 1`). With the (proved-mod-audit)
  factorization `S*_s ≤ 2Φ_s + 6δ` this composes to `C_sf = 8`; it would discharge `op-classical`
  only through the **OPEN edge `(EX) ⇒ Kernel/HLC`**.

**Honest headline.** The realizable-family relation is **linear, `δ = H/2`**; the `δ ≳ H²` form is only the
worst-case envelope (H capped at `O(√δ)` by the exposedness window). The `√η` exponent is nonetheless sharp.
**The north star is OPEN.**

The single failure mode guarded against: **a confident, plausible, WRONG-or-overclaimed result leaking into
the rigorous record.** Nothing is "rigorous" here until it is byte-matched to a published theorem,
`af`-formalised, or Lean-proved (the rigour ladder, `CLAUDE.md` L0). The ingested classical-portfolio is a
*starting point*, not an oracle.

## Scope

**In scope.**
- Ingesting the classical-portfolio's accumulated knowledge into `docs/ingest/`, honestly re-tagged, and
  codifying its implication structure as an acyclic **knowledge DAG** (`argument/DAG.md`) with an **honest
  rigour status** per node (`proved-mod-audit` for the inherited paper-proofs; `conjecture` / `numerical` /
  `open` as appropriate).
- Byte-verifying the load-bearing classical/Markov references into `refs/` (Baake–Sumner equal-input
  idempotent Markov structure; Högnäs–Mukherjea the δ=0 anchor; the contractive-projection / error-bound
  background).
- Running an **explore/exploit campaign** with `fr`: informal directions (prove the Kernel/(EX) conjecture,
  frame-free dual-localization, the H–M Thm 1.12 route, the Łojasiewicz/error-bound route, …) are arms; the
  FRONTIER is the single live open question; progress is banked only via an external oracle.
- **Numerical experiments** (exact-arithmetic LP enumeration, certified instances, δ–H measurement) as
  reproducible `runs/` bundles — evidence, never proof.
- Re-establishing inherited results **rigorously**: elevating specific conjectures to **`af` formalisation**
  (codex prover/verifier protocol) when the portfolio or the user calls for it; Lean/mathlib is the top rung
  but not the current goal.

**Out of scope (anti-goals).**
- Claiming any classical stability bound as rigorous without a certificate that is byte-matched,
  `af`-validated, or Lean-proved. **Overclaiming is the cardinal sin** (L0).
- Re-walking the recorded **dead routes** (raw-index path-product floors — refuted by the cloning
  obstruction; coefficient-only LP support-cleanup; universal `C ≤ 2`; exists-exact-max-volume selectors;
  Jensen/convexity; canonical-`g` energy method; finite-corner-as-asymptotic). See `FINDINGS.md`.
- Presenting the frame-specific `δ = H/2` proof as the general (frame-free) statement.
- The general **positive-maps / Jordan (JB) Layer-1** structure theorem — that lives in
  `../almost-idempotent-positive-maps`; here we pursue only its **commutative (stochastic) shadow**.
- Remote CI / GitHub Actions (local `scripts/check-all.sh` is the only gate); standing up `af`/Lean before a
  conjecture is elevated.

## Success criteria

1. Every term used resolves to exactly one canonical `definitions/` shard (no drift); no naked symbols
   beyond BSc/MSc common knowledge.
2. The classical-portfolio's claims form an **acyclic, fully-resolved DAG** in `argument/`, each with an
   **honest rigour status**; every `cited` claim has a byte-verified `refs/` provenance row.
3. `refs/` ground truth is ingested and `sha256sum -c` passes for present payloads.
4. The `fr` campaign is live: a portfolio of research directions, a named FRONTIER (the Kernel/(EX)
   conjecture), and a banking gate.
5. The internal `report/` compiles and every rigorous result it reproduces has a `PROVENANCE.md` row.
6. The **gate is green** (`scripts/check-all.sh` → `[check-all] OK`).
7. **No result is called rigorous unless it is byte-matched, `af`-validated, or Lean-proved.**

## Canonical artifacts (file → invariant)

- `definitions/` — one canonical definition per term; `check-defs.py` enforces no drift.
- `argument/` — one contract per result; `argument.py` enforces an acyclic, rigour-ladder-typed DAG.
- `runs/` — numerical bundles; `check-runs.py` enforces reproducibility + no masquerading as rigorous.
- `report/` — the sharded LaTeX lab-book; `check-report-shards.sh` enforces master purity + shard headers +
  index/catalog sync; `report/PROVENANCE.md` binds each reproduced claim to a source.
- `refs/manifest/` — the ground-truth ledger; `checksums.sha256` is authoritative.
- `.frontier/` — the `fr` campaign record (append-only `log.jsonl` + `portfolio.json`).
- `docs/ingest/` — the ingested classical-portfolio (read-mostly; never cited as rigorous, L1).

## Current state (2026-07-02)

**Repository stood up (day 1).** Governance (`CLAUDE.md`==`AGENTS.md`, this `PRD.md`, `HANDOFF.md`,
`README.md`, `CONVENTIONS.md`, `FINDINGS.md`, `RESEARCH_NOTES.md`), the layered architecture
(`definitions/`, `argument/`, `proofs/`, `report/`, `runs/`, `refs/`, `docs/ingest/`), the local-CI gates
(`scripts/`, incl. the AQM-style `check-report-shards.sh`), and the `fr` controller are being put in place;
the classical-portfolio is being ingested and honestly re-tagged, and the knowledge DAG seeded from it.
`scripts/check-all.sh` is green on the scaffold. `af` is **designed-in but opt-in** (`af: none` everywhere;
codex protocol per `CLAUDE.md` §6); the first elevation target is `lem-classical-equiv` (re-validate the
signed↔stochastic bridge). **No mathematics is rigorous in-repo yet.** See `HANDOFF.md` and `bd ready`.

## Escalation (stop and ask the user)

- A scope question this PRD doesn't answer (esp.: whether to elevate a conjecture to `af`; which reference
  to ingest next; whether to relax the `fr` circuit-breaker).
- A definitional choice with no obvious right answer (it ripples everywhere — get consensus first).
- A claim whose ground truth is **not in `refs/`** (don't paraphrase from memory — L1).
- You're about to **promote a status up the rigour ladder** (numerical/conjecture/proved-mod-audit →
  rigorous) without a byte-matched ref, an `af`-validated tree, a Lean proof, or an independent reviewer.
- You're tempted onto a recorded **dead route** (Rule 13 / `FINDINGS.md`).
