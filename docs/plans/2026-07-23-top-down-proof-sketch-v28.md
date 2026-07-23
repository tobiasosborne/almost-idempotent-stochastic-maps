<!--
ROLE: the top-down FULL proof sketch of op-classical, VERSION 28 (W73/W73b/W74-F delta).
  Supersedes v27; everything not restated here is unchanged from v27 (hence v26/v25/v24).
STATUS DISCIPLINE (L0): a SKETCH / STRATEGY artifact; promotes nothing. Route F is a
  CONDITIONAL reduction resting on a literature theorem whose printed proof was found
  INVALID-as-printed by a hostile audit. Nothing here is rigorous by this repo's L0.
-->

# Top-down proof sketch v28: op-classical (2026-07-23, W73–W74F delta — a second, independent route enters the map)

## UNCHANGED from v27

The signed-geometry trunk (op-classical ⇐ op-exposed-hull ⇐ HLC ⇐ Kernel/(EX)),
the three-cell SL1a surface, all dead routes (FINDINGS.md, Rule 13), H-D, H-I,
SL1b, L6.5, E1–E5 codification, the small-gauge bridge, the repaired conditional
assembly bridge and its four-conjecture surface. **T0 count 34 af-validated;
registry 200.** No registry change in W73/W73b/W74F wave 1.

The DTR ⇒ POTI reduction of v27 stands exactly as banked (W70, 4/4 VALID). The W72
decomposition of POTI-0 (S0 / RX / O48 / RDSE / LDHR-48) remains **UNVERIFIED** — its
batched hostile verifier was interrupted before any verdict, and that debt is still owed.

---

## Map change 1: op-classical now has a SECOND, independent candidate route — Route F

Everything in v27 and before attacks op-classical through the signed picture: exposed
hulls, hidden vertices, charts, heights, the Kernel/(EX) conjecture. **Route F bypasses
that entire apparatus.** It was produced by the W73 fresh-perspective reset
(`docs/plans/2026-07-22-strategy-reset-w73.md`), where two of four independent codex
strategists converged on the same architecture without seeing each other's work.

Skeleton (statuses are this repo's, not the strategists'):

- **F0 — the lift** `Φ = J∘Q∘D` on `M_n` (`J` diagonal inclusion, `D` diagonal
  conditional expectation), with `‖Φ²−Φ‖_cb = ‖Q²−Q‖_{∞→∞} ≤ η`.
  *Status: VALID per the W73b hostile audit (Q4 — the cb-lift identity proved both
  directions). Not yet a registry shard.*
- **F1 — the import.** Kitaev `th_factorization` (arXiv:2405.02434v2, `tex:2730`): a
  finite-dimensional C*-algebra `ℬ` and UCP `Δ: ℬ → 𝔅(ℋ)`, `Υ: 𝔅(ℋ) → ℬ` with
  `‖ΔΥ−Φ‖_cb ≤ O(η)` and tensor-extended approximate multiplicativity
  `‖Υ_n(Δ_n X · Δ_n Y) − XY‖ ≤ O(η)‖X‖‖Y‖`, hence `‖ΥΔ−1_ℬ‖_cb ≤ O(η)`, all constants
  universal. *Status: the STATEMENT is exactly what Route F needs (audit Q1 VALID, incl.
  the tensor-extended form and the orientations); the PRINTED PROOF is **INVALID as it
  stands** (audit Q3). This is the whole risk of the route.*
- **F2 — commutativity forcing.** `ran Φ` diagonal ⟹ `‖[Δx,Δy]‖ ≤ 8Kη` ⟹ (via F1's
  multiplicativity, both orders) `‖[x,y]‖ ≤ 10Kη` in `ℬ`; any noncommutative
  finite-dimensional C*-algebra contains two contractions with commutator norm **exactly
  2** (embed the Pauli pair), so `10Kη < 2` forces `ℬ ≅ ℓ∞(k)`.
  *Status: VALID conditional on F1 (audit Q5c).*
- **F3 — diagonal compression.** `A = DΔ`, `M = ΥJ` row-stochastic; `‖AM−Q‖ ≤ Kη`; the
  near-isometry `‖Ax‖ ≥ (1−3Kη)‖x‖` (through the exact identity `ΦΔ = JQA` — **never**
  `ΦΔ = JA`) yields `‖MA−I_k‖ ≤ ε := 3Kη/(1−3Kη)`.
  *Status: VALID conditional on F1 (audit Q5d/Q5e).*
- **F4 — PRH, the one step that is ours.** Positive unital `A: ℓ∞(k)→ℓ∞(n)`,
  `M: ℓ∞(n)→ℓ∞(k)` with `‖MA−I_k‖ ≤ ε < 1/2` ⟹ a stochastic idempotent `E` with
  `‖AM−E‖_{∞→∞} ≤ C√ε`. Construction: threshold `λ = √(ε/2)`, cores
  `C_s = {a_{is} > 1−λ}` (disjoint because two coordinates of a probability vector cannot
  both exceed `1−λ > 1/2`), condition `μ_s → ν_s` on `C_s`, harden memberships; then
  `N Â = I_k` **exactly** and `E = Â N` is a stochastic idempotent. The `√` is born at the
  threshold/conditioning balance `ε/λ + 2λ`.
  *Status: UNVERIFIED. Two independent derivations disagree on the constant (`2√2` vs `3`).
  Under proof in W74F-A (aism-6m8v).*
- **F5 — conclusion.** `‖Q−E‖ ≤ Kη + 2√(2ε) ≤ (K + 4√(2K))·√η` for
  `η ≤ min{η_K, 1, (24K)^{-1}}`. *Status: VALID conditional on F1 + F4 (audit, Root 5
  constants re-derived).*

**Why this could be true while Kitaev's quantum question stays open:** the hardening step
is genuinely commutative — "two coordinates of one probability vector cannot both exceed
`1−λ > 1/2`" has no noncommutative analogue. A classical-easier / quantum-open split is
what one expects, not a red flag by itself.

**Wall audit (both strategists concurring, design intent not proof):** no raw indices (so
the cloning obstruction does not bite), no per-block error sums, no capacity/absorption
language, fully primal, no LP faces, Markov used only in its valid direction.

---

## Map change 2: the W73b hostile audit — where Route F actually stands

`docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` (fresh codex, xhigh,
source-first, against the byte-verified tex; SHA256 `e7eb512a…`). Verdicts: **Q1 VALID ·
Q2 VALID-WITH-CORRECTIONS · Q3 INVALID · Q4 VALID · Q5 VALID.** The bottom line, verbatim:

> F0–F3 are sound conditional on Theorem 12.3, but Theorem 12.3 is not rigorously
> established by the supplied TeX as written.

Two findings restructure the route, and both are **more favourable than they sound**:

1. **The real flaw is smaller and sharper than the sibling repo believed.** The failure is
   the printed **direct-sum diagonal formula** at `tex:1254` (repeated `tex:2780-2783`) —
   Cartesian products of per-block unitary designs need not give a diagonal of a direct sum
   (exact `ℂ⊕ℂ` counterexample). It is **not** the `Δ̃`-multiplicativity diagnosis the
   sibling FINDINGS C14 blamed: the auditor **proved** the positivity argument entrywise
   *given an exact central diagonal*, and supplied an elementary repair (full Haar, or
   phase-balanced/random-sign so all cross-block first moments vanish). `lem_RC` and the
   `Υ'` construction survive fully. No cone-projection shortcut is needed — and if one were
   retained it would require an unproved dimension-free cb distance-to-CP-cone theorem.
2. **The principal blocker is `th_main_ext`** (`tex:1538-1540`), whose proof
   (`tex:1542-1557`) is an *adaptation outline* — "straightforward", "should be adapted",
   "only trivial modifications" — that never exhibits one map carrying **all** the uniform
   amplified bounds. Plus a printed typo at `tex:1551-1555` (omitted squares; corrected
   form `|⟨X,X⟩ − ‖X‖²_{n,1}| ≤ O(δ+ε)‖X‖²_{n,1}`).

Universality is *claimed* explicitly and consistently (the paper's own convention at
`tex:458`: each big-O "stands for a concrete function, not depending on any additional
data"), but never *extracted*. For op-classical a numerical `K` is unnecessary;
**universality is necessary**.

### The residual risk register (the new Tier-1 face)

Between Route F and a rigorous op-classical stand exactly:

1. a complete proof of `th_main_ext` at the amplified strength — **principal blocker**;
2. a universal-constant ledger across functional calculus → approximate algebra → error
   reduction → tensor extension → CP → normalization;
3. the exact whole-algebra diagonal repair at `tex:1254` + `tex:2780-2783`, with every
   centrality / norm-one use site rechecked;
4. no unproved cone-projection shortcut;
5. a full audit of `th_almost_idemp` (`tex:2239-2723`) with explicit constants;
6. **PRH** (F4) proved standalone;
7. rigour-status/provenance closure under this repo's protocol.

---

## Map change 3: W74-F wave 1 — the register is under attack, one worker per item

Dispatched 2026-07-23 (fresh codex `gpt-5.6-sol` xhigh, disjoint targets, briefs in
`docs/plans/2026-07-23-W74F-artifacts/`; epic aism-enze):

| wave | items | issue | deliverable |
|---|---|---|---|
| W74F-A | 6 | aism-6m8v | PRH proved standalone, constant settled, `ε=0` endpoint, sharpness |
| W74F-B | 3+4 | aism-0m77 | diagonal repair lemma (universal norm bound) + use-site recheck ledger + re-proved CP-ization |
| W74F-C | 1+2 | aism-2r3m | **decomposition** of `th_main_ext` into amplified lemmas, each (a) established / (b) mechanical / (c) gap, + the universality ledger |
| W74F-D | 5 | aism-7gqw | per-block hostile audit of `th_almost_idemp` with explicit constants |

All four are PROVER/AUDITOR output only. **Hostile verification is a separate batched
pass** (CLAUDE.md §6); nothing from this wave enters the registry before it clears one.

**PRH is the load-bearing independent asset.** Even if the Kitaev import never closes,
PRH establishes a new, clean reduction on the map — *op-classical ⇐ "a positive
approximate retract exists"* (`‖AM−Q‖ = O(η)`, `‖MA−I‖ = O(η)`, `A, M` stochastic) —
which is a strictly better formulation of the target than anything the signed picture
currently offers, and it is elementary.

---

## Map change 4: Route X registered as the in-repo successor shape (not yet attacked)

The same reset produced **Route X** — one theorem shape at three altitudes: **RTS** (at
L5-GAP-1, pre-S/C/I), **APAL/PAT** (at kernel level, with the elementary positive-recipient
carrier lemma `‖mT−m‖₁ ≤ 4δ(1+δ)` as its engine), **QCMP** (`H² ≤ 2¹²·δ·Cap_P̄(v)`, capacity
language, cheapest decider). Shared design constraints by construction: quotient-first,
one global coupling, coefficient-ratio capacities, primal separator output. Its deciders are
filed as aism-ea2f; its bridge/carrier/quotient shards as aism-h9qc. **Nothing of Route X is
proved, decided, or registered** — it is the fallback shape if Route F's import dies.

**Altitude diagnosis (strategists B and D, independently; STATED, unverified):** the W72
leaves RDSE / LDHR-48 sit at the wrong altitude — `w_*` is not a charge, and lower-bounding a
selected atom of a proof-dependent disintegration is the anti-splitting bound in disguise
(the dilution escape `w_*→0` is real). POTI-0 is "the residue left after the global
alternative has been conditioned away."

---

## Tier-1 order (updated — user directive 2026-07-23: concerted effort on Route F)

0. **Route F closure (aism-enze, P0).** W74F-A/B/C/D → batched hostile verification →
   codification of survivors → af-elevation of the elementary ones (PRH first). Wave 2 is
   determined by W74F-C's (c)-nodes: those are the actual mathematics remaining.
1. **PRH through the full pipeline regardless of F1** (aism-6m8v then aism-h9qc): it is
   the independent asset and the cleanest new reduction target on the map.
2. **The owed W72 verification** (aism-x0up): banked work is verified or explicitly
   retired — no third state. Creative attacks on RDSE / LDHR-48 remain **PAUSED** pending
   Route F triage (user directive; strategist altitude diagnosis is the reason, and that
   diagnosis is itself unverified).
3. **Route X deciders** (aism-ea2f) — cheap, exact, kill-or-confirm before any proof
   campaign; the fallback if F1 dies.
4. **af-elevation queue (aism-88r):** L5:T0 ≈ 66:34 and widening. Prime candidates
   unchanged (lem-dtr-oriented-tail-ray-conversion, lem-dtr-canonical-overlap,
   lem-aesc-synthetic-finance-tail-amplification, lem-intersection-branch-production,
   the D-cap spine).
5. Route A execution (aism-ur9), SL1b, conj-cotop-web-coupling (L6.5), H-D/H-I.
6. Parked: aism-l1a, aism-cei, aism-nlg, aism-z98 (user decisions), rank>3/unbounded-K
   gadget LPs.

## What v28 explicitly does NOT claim

- Not that Route F proves op-classical. It is a **conditional** reduction whose sole large
  import has an **INVALID-as-printed** proof; the repair is specified but unproved.
- Not that any of F0–F5 is a registry result: registry is unchanged at 200, T0 at 34.
  F0/F2/F3/F5 are audit-VALID *conditional on F1*, which is not established.
- Not that PRH is proved — two unverified derivations with disagreeing constants.
- Not that the Kitaev statement is wrong. The audit's finding is about the **printed
  proof**, not the theorem; the theorem may well be true and provable.
- Not that the W72/POTI subtree is retired — only paused, with its verification still owed.
- Not that the strategists' altitude diagnosis of RDSE/LDHR-48 is correct; it is banked
  interpretation, not a theorem.
