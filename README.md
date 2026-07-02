# almost-idempotent-stochastic-maps

A rigorous research lab-book and exploration harness for a **fully mathematically rigorous proof of the
classical (stochastic) almost-idempotence stability result**: every row-stochastic `Q` that is *almost*
idempotent (`‖Q²−Q‖_{∞→∞} ≤ η`) is close (within `C·√η`, exponent sharp) to a genuine stochastic idempotent.

This is an **open research programme**. The classical case was largely pursued in
`../almost-idempotent-positive-maps` (the `classical-portfolio`), which reduced it — through audited and
*mod-audit* steps — to a single open **Kernel / (EX) conjecture**. That work is ingested here (honestly
re-tagged) as a *starting point*, not an oracle. The infrastructure exists to keep the search honest: a
strict **rigour ladder** (nothing is "rigorous" unless byte-matched to a published theorem, `af`-formalised,
or Lean-proved), an enforced acyclic **knowledge DAG**, byte-verified ground truth, and an explore/exploit
controller the model cannot skip.

## Where to start

| You want… | Read |
|-----------|------|
| Scope / what this is | `PRD.md` |
| How to work here | `CLAUDE.md` (== `AGENTS.md`) |
| Current state / next task | `HANDOFF.md`, then `bd ready` |
| The exploration portfolio | `fr board` |
| The knowledge DAG | `argument/DAG.md` (Mermaid, generated) |
| Notation + rigour rungs | `CONVENTIONS.md` |
| Open directions / refs queue | `RESEARCH_NOTES.md` |
| Gotchas + dead routes | `FINDINGS.md` |
| The ingested prior work | `docs/ingest/` (read-mostly; never cited as rigorous) |

## The north star (open)

`op-classical`: universal `η₀, C > 0` (dimension-free) s.t. every row-stochastic `Q` with
`‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀` admits a stochastic idempotent `E` with `‖Q−E‖_{∞→∞} ≤ C·√η`. Exponent 1/2 sharp.
Reduces (through `op-exposed-hull ⇐ HLC`) to the open **Kernel / (EX) conjecture**. **No link is rigorous
in-repo yet.**

## Starting ground truth (in `refs/`)

- `baake-sumner-2007.11433` — *On equal-input and monotone Markov matrices* (the commutative idempotent structure)
- `hognas-mukherjea` — *Probability Measures on Semigroups* (the δ=0 classification anchor)
- staged: Douglas'65, Andô'66, Flor'69, Hoffman'52, Luo–Pang'94, Meyer'89, Chakraborty–Rao'01 (`refs-staging/`)

## The gate

```bash
sh scripts/check-all.sh      # the only CI — defs · refs · argument DAG · runs · provenance · report shards · tests · report build
fr board                     # the explore/exploit portfolio
```

No remote CI. The local gate is wired into `.beads/hooks/pre-commit`.

## Architecture (layers)

- **Layer 0** `definitions/` — one canonical, provenance-gated definition per term.
- **Layer 1** `argument/` — one shard per result; the rigour-ladder-typed knowledge DAG.
- **Layer 2** `proofs/<id>/` — `af` workspaces (opt-in; codex prover/verifier protocol).
- **Lab-book** `report/` (rigorous LaTeX, sharded AQM-style) + `runs/` (numerical bundles — never rigorous).
- **Ground truth** `refs/` — byte-verified sources (payload gitignored, manifest tracked).
- **Controller** `.frontier/` — the `fr` campaign. **Ingest** `docs/ingest/` — the prior work, re-tagged.

License: AGPL-3.0.
