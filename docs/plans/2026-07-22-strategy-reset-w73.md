# W73 (2026-07-22) — Strategy reset: fresh-perspective synthesis

**STATUS: STRATEGY / UNVERIFIED.** Nothing in this document is proved by this repo's standards
(L0). Every mathematical claim below is conjecture-level until it clears the pipeline
(fresh-prover → batched hostile verifier → codifier, or af). Literature claims are
web-sourced and NOT yet byte-verified against `refs/` (L1) — the Kitaev and SBD papers are
**not yet ingested** (see `aism-5de`).

**Provenance.** User-mandated fresh-perspective session (2026-07-22): 6 repo-state
summarizers + 3 literature researchers (sonnet), then 4 independent codex `gpt-5.6-sol`
xhigh strategists (A: clean-slate architectures; B: local-to-global synchronization;
C: literature-transfer direct proof; D: kernel-route absorption). Full reports in
`docs/plans/2026-07-22-W73-artifacts/` (+ the state-of-play pack used as their input).
Orchestrator synthesis below.

---

## 1. Headline findings

**1a. The problem is confirmed open — and freshly bracketed — in the 2024-25 literature.**
Kitaev (arXiv:2405.02434, v2 Feb 2025) poses the noncommutative generalization of
op-classical verbatim as an open problem, identifies the same mechanism (functional-calculus
idempotent is O(η) but loses positivity; positivity repair costs √η), and proves an
adjacent dimension-free theorem: an O(η) approximate encode/decode **factorization**
Φ ≈ ΔΥ through a genuine finite-dim C*-algebra with ‖ΥΔ−1_B‖ ≤ O(η) (his Thm 12.3).
Salzmann–Bergh–Datta (arXiv:2405.01532) prove the sharp dimension-free √ε repair for the
classical *fixed-point* sibling (Thm 5.2 + optimality Rem 5.4) via a depolarizing-blend
contraction. Neither resolves op-classical. [STATED — papers not yet in refs/]

**1b. Two independent convergences among the four strategists.**
- Strategists A and C, working independently, converged on the **same new architecture**
  (Route F below): Kitaev factorization → force commutativity → compress to stochastic
  maps → an elementary "hardening" lemma that converts an approximate retract into an
  exact stochastic idempotent at √-cost. C moreover closed the gap A had flagged
  (commutative inheritance), by a quantitative commutator argument.
- Strategists B, D (and A's second architecture) converged on the **same missing in-repo
  theorem shape** (Route X below): a conserved *aggregate* quantity (an L¹ current /
  carrier measure, never a selected atom), an O(δ) harmonic sink, and an
  **exchange-or-expose alternative** whose failure branch *constructs a primal exposer*.
  This shape simultaneously explains both sides of the 18-wave empirical record.

**1c. Diagnosis of the current front.** B argues (and D independently supports) that the
W72 leaves RDSE/LDHR-48 sit at the wrong altitude: `w_*` is not a charge (lower-bounding a
selected atom of a proof-dependent disintegration is the forbidden anti-splitting bound in
disguise; the dilution escape `w_*→0` is real), and POTI-0 "is the residue left after the
global alternative has been conditioned away." The decisive battle belongs at L5-GAP-1
(pre-S/C/I) — or at the kernel level in D's formulation.

---

## 2. Route F — Factorization–Hardening (new primary candidate)

Bypasses the entire signed-geometry reduction (no exposed hulls, hidden vertices, charts).
Skeleton (details in `STRATEGIST-C-factorization.md`, cross-checked by
`STRATEGIST-A-clean-slate.md` §I):

- **F0** [NEW-ROUTINE] Lift: Φ = J∘Q∘D on M_n (J diagonal inclusion, D diagonal
  conditional expectation); claim ‖Φ²−Φ‖_cb = ‖Q²−Q‖_{∞→∞} ≤ η.
- **F1** [IMPORT — the sole large risk] Kitaev Thm 12.3: finite-dim C*-algebra B and UCP
  Δ: B→M_n, Υ: M_n→B with ‖ΔΥ−Φ‖_cb ≤ Kη, approximate multiplicativity
  ‖Υ(Δx·Δy) − xy‖ ≤ Kη‖x‖‖y‖ (hence ‖ΥΔ−I_B‖ ≤ Kη), universal K.
  **Must be audited line-by-line against the actual paper** — statement, orientations,
  constants, dimension-freedom, applicability to the diagonal (entanglement-breaking) lift.
- **F2** [NEW-ROUTINE] Commutativity forcing: ran(Φ) is diagonal ⟹ ‖[Δx,Δy]‖ ≤ 8Kη ⟹
  (via F1's multiplicativity, both orders) ‖[x,y]‖ ≤ 10Kη in B; a matrix summand M_m,
  m≥2, contains contractions with ‖[x,y]‖ = 2 ⟹ B ≅ ℓ∞(k) for η < 1/(5K).
- **F3** [NEW-ROUTINE] Diagonal compression: A = DΔ, M = ΥJ row-stochastic;
  ‖AM−Q‖ ≤ Kη; the near-isometry lower bound ‖Ax‖ ≥ (1−3Kη)‖x‖ recovers
  ‖MA−I_k‖ ≤ ε := 3Kη/(1−3Kη).
- **F4** [NEW-ROUTINE, central new lemma — **Positive-Retract Hardening (PRH)**]:
  If positive unital A: ℓ∞(k)→ℓ∞(n), M: ℓ∞(n)→ℓ∞(k) satisfy ‖MA−I_k‖ ≤ ε < 1/2, then
  there is a stochastic idempotent E with ‖AM−E‖_{∞→∞} ≤ 2√(2ε).
  Construction: membership rows a_i, decoder measures μ_s; average impurity
  Σ_i μ_s(i)(1−a_is) ≤ ε/2; threshold λ = √(ε/2), cores C_s = {a_is > 1−λ} (disjoint by
  the simplex constraint), condition μ_s to ν_s on C_s (cost 2β_s ≤ 2λ), harden
  memberships to e_s on C_s; then N·Â = I_k exactly and E = Â·N is a stochastic
  idempotent; total cost 4λ = 2√(2ε). The √ is born exactly at the threshold/conditioning
  balance ε/λ + 2λ — a two-scale configuration saturates it, consistent with ex-hume.
  (A's I.2 is the same lemma, independently derived, constants 3√ε.)
- **F5** [NEW-ROUTINE] Conclusion: ‖Q−E‖ ≤ Kη + 2√(2ε) ≤ (K+4√(2K))·√η for
  η ≤ min{η_K, (24K)⁻¹}.

**Wall audit** (both reports, concurring): all six walls bypassed — no raw indices
(cloning ok), no per-block error sums (max over rows; Σ_s a_is = 1 handles transients),
no capacity/absorption language, fully primal construction, no LP faces, Markov
inequality used only in its valid direction.

**Why this could be true while Kitaev's quantum question stays open:** the hardening step
is genuinely commutative — disjoint supports via "two coordinates of one probability
vector cannot both exceed 1−λ > 1/2" has no noncommutative analogue. A classical-easier /
quantum-open split is exactly what one expects.

**Honest risk:** if this worked this simply, Kitaev plausibly would have remarked on the
commutative case. The suspicion must be directed at F1 (does Thm 12.3 really give the
two-sided O(η) with approximate multiplicativity, dimension-free, for this lift?) and F0
(cb-norm bookkeeping). It fails, if it fails, at a sharply identifiable point.

**Decisive test (W73, first priority):** fetch + pin both papers (`aism-5de`), then a
fresh hostile codex audit of F0–F3 against the actual text of Thm 12.3 (extract one K,
verify the three implications C lists). In parallel, run PRH standalone through the
routine-prover + batched-verifier pipeline — PRH is valuable regardless of F1: it reduces
op-classical to "**a positive approximate retract exists**" (‖AM−Q‖ = O(η), ‖MA−I‖ = O(η)
with A, M stochastic), a brand-new, clean reduction target worth registering on its own.

## 3. Route X — the Exchange-or-Expose family (the in-repo battle)

Three formulations of one theorem shape, at three altitudes:

- **RTS** (B; at L5-GAP-1, pre-S/C/I): for every admissible pre-split datum, either
  t*(v) ≥ τ/4 (visible — contradiction) or some top functional collects
  Σ_{x∈A} P̄_vx⁺ z_x^φ ≥ c_syn·S·τ (which the T0 budget Q_v(φ) ≤ (2+4δ)δ forbids at small
  τ). Mechanism: aggregate L¹ transverse current (unit moments integrated against the
  full m_A — no selected root), one global transport LP, Farkas failure branch = primal
  exposer, orientation cancellation killed by the minimax
  t*(v) = min_λ max_h Σ λ_f h(p_f). Hard core: the polar identity (whole-face) step and
  separator repair. Full detail + four falsification tests in
  `STRATEGIST-B-synchronization.md`.
- **PAT/APAL** (D; at kernel level): σ̃_g(v) ≤ 1/2 + 48τ for hidden tops (⟹ Kernel with
  B = 9/8 via the T0 collapse bound, closing Route 1). Engine: the **positive-recipient
  carrier lemma** — m := P_v⁺ satisfies ‖mT−m‖₁ ≤ 4δ(1+δ) for the row-normalized kernel
  T (elementary, exact, registrable NOW), plus the aggregate peak-or-leak alternative
  (APAL): excess carrier mass > 1/2 either exchanges into near current or a Farkas
  potential, projected by P̄, yields an explicit exposer h with the κ-vs-small-β
  contradiction. Includes the correction that the naive lower ledger "z_x ≳ τ for far
  recipients" is FALSE (W54 re-entry geometry) — the tangential mechanism is the right
  one. Full detail in `STRATEGIST-D-kernel-absorption.md`.
- **QCMP** (A §II): H² ≤ 2¹²·δ·Cap_P̄(v) — same shape in capacity language; comes with
  the cheapest decider (one LP family over the existing exact bank).

**Shared design constraints** (all three, by construction): quotient-first (clone-proof),
one global coupling (anti-splitting-proof), coefficient-ratio capacities
(absorption-proof), primal separator output (dual-direction-proof), explicit direction
checks (ledger-proof).

**Why this shape explains the record:** proofs failed locally because local finance is
free; refuters failed globally because keeping finance disjoint from top ownership
creates the very cut that exposes the top. Exposedness is the min-cut certificate of the
conserved current.

**Decisive tests (cheap, exact, specified in the reports):** (i) D's multi-class
aggregate-peak decider (targets the one untested empirical residual: genuinely
multi-class outsourcing); (ii) A's QCMP ratio R = H²/(δ·Cap) over the 67k bank;
(iii) B's quotient-refinement and cross-financing tests on the W69/W71 families.

## 4. Route P — Abel cores (fallback, A §III)

R_α = αQ(I−(1−α)Q)⁻¹ at α = √η gives ‖R−Q‖ ≤ √η [elementary]; then a nonreversible
sup-norm cut-or-coalesce theorem (ACC) extracts disjoint cores + core laws with SBD
repair per core (max, not sum, over cores). Hard core: ACC. C's analysis shows the
infinite-time limits make the wrong slow-mode decision (two-state Q_a example) — any
power/Cesàro route must stop at horizon ~η^{−1/2}; and level-set extraction cannot work
from almost-harmonicity alone (co-area cancellation; exact-idempotent transient-row
counterexample) — it needs positive near-Boolean class coordinates first, i.e. exactly
what Route F's F1 supplies. Keep as fallback; its exact-rational decider is specified in
A §III.4.

## 5. Consequences for the live tree (proposals, not actions)

1. **W72 verification stays queued** (banked work should be verified or explicitly
   retired) — but the RDSE/LDHR-48 *creative attacks* should be PAUSED pending Route F/X
   triage. B's altitude diagnosis + D's independent support say the leaves are
   fighting where the needed structure has been conditioned away. [USER DECISION]
2. The quotient apparatus (P̄ exactly idempotent, δ(P̄) ≤ δ(P), harmonic descent) must be
   re-established as first-class registry shards — all four strategists demanded it; it
   is currently only ingest prose. [NEW-ROUTINE]
3. D's positive-recipient carrier lemma ((4)–(8) of his report) is elementary, exact, and
   should be registered + verified immediately. [NEW-ROUTINE]
4. PRH (F4) should be proved through the pipeline immediately — it upgrades the map
   "op-classical ⟸ positive approximate retract" regardless of Kitaev. [NEW-ROUTINE]
5. Sketch v28 should record this reset once (a) W72's verdict lands and (b) the user
   ratifies the reprioritization. (Rule 9 stewardship — not done unilaterally here.)

## 6. Proposed W73–W76 execution order

- **W73a** (routine, parallel): fetch/pin Kitaev + SBD (`aism-5de`); PRH through
  prover+verifier; carrier lemma through prover+verifier; quotient shards.
- **W73b** (the decisive audit): fresh hostile codex audit of Route F steps F0–F3 against
  the actual Kitaev text. Outcome A: survives ⟹ op-classical reduces to already-verified
  elementary lemmas + one cited theorem — escalate to user for the af/writing campaign.
  Outcome B: fails ⟹ the failure point is itself the sharpest known formulation of the
  positivity obstruction; feed it to Route X.
- **W74**: the three Route X deciders (aggregate-peak, QCMP ratio, quotient-refinement /
  cross-financing). Kill or confirm APAL/QCMP/RTS cheaply before any proof campaign.
- **W75**: formulate + register the surviving Route X statement (likely RTS at L5-GAP-1
  or APAL at kernel) as a conjecture with its bridge lemma; begin the creative attack
  with the full engine bank.
- **W76**: re-assess; sketch v28; retire or absorb the POTI subtree accordingly.

## 7. What is explicitly NOT claimed

- No step of Route F is verified; F1 is an unaudited literature import; the lift identity
  F0 is unchecked; PRH's constants are unchecked (two independent derivations agree on
  shape, differ in constants — 2√(2ε) vs 3√ε).
- RTS/APAL/QCMP are conjectures with named hard cores and named failure modes; their
  wall-compatibility is design intent, not proof.
- The strategist reports are codex output banked verbatim; nothing has passed
  reviewer≠author verification. The empirical "explanations" of the 18-wave record are
  interpretations, not theorems.
