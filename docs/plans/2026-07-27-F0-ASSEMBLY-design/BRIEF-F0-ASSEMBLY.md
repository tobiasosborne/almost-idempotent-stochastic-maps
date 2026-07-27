# BRIEF — F0/root assembly design job (front #4 of the critical-path risk register)

You are a fresh, independent design mathematician. This is the LAST
undesigned front of the Route-F critical path
(`docs/plans/2026-07-26-critical-path-risk-register.md` §4): the F0/root
composition

> `op-classical` ⇐ F2 + F3 + PRH + the K-ledger

for which NO registry row is designed (v4.1 phase 5 step 4). Your job is a
design + feasibility audit: closed row contracts for the root composition,
an end-to-end single-K discipline check, and a wiring proposal — NOT a
proof, NOT a registry mutation.

## The pieces at the seam (read the shards; contracts are authoritative)

- `argument/lemmas/op-classical.md` — the OPEN root: universal η₀, C > 0
  (n-free) such that ‖Q²−Q‖∞→∞ ≤ η ≤ η₀ ⇒ ∃ stochastic idempotent E with
  ‖Q−E‖∞→∞ ≤ C√η.
- `argument/lemmas/lem-routef-f2-positive-unital-compression.md` (T0) —
  from (Δ, Υ, Φ = JQD) with the three K·η estimates, produces positive
  unital A, M with ‖Q−AM‖ ≤ Kη, ‖QA−A‖ ≤ 2Kη, ‖Ax‖ ≥ (1−3Kη)‖x‖, under
  0 ≤ η ≤ min{(24K)⁻¹, 1}.
- `argument/lemmas/lem-routef-f3-retract-defect.md` (T0) — those outputs
  give ‖MA−I‖ ≤ 3Kη/(1−3Kη) when 3Kη < 1.
- `argument/lemmas/lem-routef-prh-finish.md` (T0) — ‖Q−AM‖ ≤ Kη and
  ‖MA−I‖ ≤ 3Kη/(1−3Kη) with 0 ≤ η ≤ min{(24K)⁻¹, 1} give a stochastic
  idempotent E with ‖Q−E‖ ≤ (K+4√(2K))√η.
- `argument/lemmas/lem-routef-k-ledger.md` (proved-mod-audit;
  **DO-NOT-REWIRE-OR-SEED guard ACTIVE**) — the ledger producing universal
  K ≥ 1 and η_K > 0 and the three K·η estimates for the repaired Kitaev
  factorization. Its PROPOSED future parent wiring is
  `DESIGN-LEDGER-DOMAINS-v2.md` §6.2 (deps = the three telescopes,
  k-finiteness, threshold-minimum, F2, F3, PRH), which just passed a fresh
  hostile re-audit (`AUDIT-LEDGER-DOMAINS-v2.md`, disposition LAND-14 with
  two corrections; note its terminal threshold η_K = min{ρ_fac, (24K)⁻¹, 1}
  already CONTAINS the F2/PRH guard (24K)⁻¹ and the PRH entry 1).
- The upstream producers of (Δ, Υ, Φ) and the three estimates:
  `lem-routef-ai-defect-linearization.md`,
  `lem-routef-functional-calculus-closeness.md`,
  `cor-kitaev-diagonal-cpization.md`, `lem-kitaev-almost-idemp-audit.md`,
  `lem-thmainext-conditional.md` — read each contract to confirm what the
  K-ledger's antecedent (η with ‖Q²−Q‖ ≤ η) consumes and produces.
- Also read: `docs/plans/2026-07-26-top-down-proof-sketch-v34.md` (the
  governing sketch), `DESIGN-FUDW-DECOMP-v4.1.md` phase 5, and
  `argument/README.md` (row schema; the linker enforces acyclicity and
  contract-match).

## Your deliverables — write `docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md`

1. **The F0 row design.** Closed one-line contract(s) for the root
   composition — expect ONE thin row, e.g.
   `lem-routef-f0-assembly` ("if the K-ledger's contract holds then
   op-classical's contract holds with η₀ = η_K and C = K+4√(2K)"), plus, if
   genuinely needed, at most one or two glue rows. Each with: exact deps by
   id, defs, provenance, projected af budget (≤12 nodes / depth ≤3). No
   compound contracts; no new constants beyond those the deps export.
2. **Single-K end-to-end audit.** Walk ONE constant K and ONE threshold
   through the whole seam: the K-ledger's (K, η_K) into F2's hypotheses
   (are the three cb-estimates the ledger exports EXACTLY the three F2
   antecedent estimates — same norms, same Φ, same quantifiers?), F2's
   outputs into F3's hypotheses, F2+F3 outputs into PRH's hypotheses, and
   PRH's conclusion into op-classical's contract. Flag EVERY mismatch:
   a norm read differently (cb vs ∞→∞), a missing "for all x", a threshold
   entry present in one row and absent in another, an η vs ε_AI(η)
   conversion, the ‖Q²−Q‖ ≤ η antecedent's entry point. An interface
   mismatch found = SUCCESS; classify it (contract-correction needed vs
   new glue row vs genuine gap).
3. **Root wiring proposal.** The exact future deps of `op-classical`
   (PROPOSED ONLY — the DO-NOT-REWIRE guards on `lem-routef-k-ledger` and
   `op-classical` remain; nothing is rewired until user ratification), and
   how this composes with the ledger v2 §6.2 parent wiring. Check for
   double-counting: F2/F3/PRH appear in the ledger's proposed parent deps
   AND at the F0 seam — state clearly which row consumes which, so the DAG
   has each edge exactly once.
4. **Sharpness/equivalence side-check.** Confirm the composition claims
   only the √η exponent op-classical states (C = K+4√(2K)); note where
   `ex-hume` (sharpness) and `lem-classical-equiv` (signed bridge) sit
   relative to F0 — they must NOT become deps of the root row unless the
   root contract needs them.
5. **Dimension-freeness audit.** η₀ and C must inherit n-freeness from the
   ledger's K alone; verify no step of the composition introduces any
   other quantity.
6. **Feasibility verdict + landing order.** Per-row feasibility
   (elevation-ready after which gates?); where F0 sits in the serial
   campaign (after ledger landing; independent of / dependent on the
   MAIN+polar fronts ONLY through the ledger's thmainext black box —
   verify and state this decoupling explicitly).

## Hard constraints

- Design only. Write ONLY inside `docs/plans/2026-07-27-F0-ASSEMBLY-design/`.
- No registry, definitions/, or proofs/ mutation; no status promotion; the
  DO-NOT-REWIRE guards stay; everything you produce is ESCALATED for user
  ratification.
- No guessed constants: every constant in your contracts must be exported
  by a named dep.
- NOT IN LOCAL REFS discipline: if a needed fact is not in the local
  sources/shards, say so — do not fill from memory.
- An honestly reported interface mismatch beats a papered-over one.
