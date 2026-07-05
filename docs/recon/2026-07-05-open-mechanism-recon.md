<!--
RECON: breadth-first sketch program (bd aism-aqf), session 8 — 2026-07-05.
WORKERS: four fresh sonnet lanes (read-only repo sweep + web), one per OPEN mechanism of
  docs/plans/2026-07-04-top-down-proof-sketch.md. Worker answers below VERBATIM (transport
  HTML-entity unescaping only). Workers did not edit tracked files and did not run fr/bd/git.
ORCHESTRATOR SYNTHESIS: §0 (difficulty ranking + hardest-leaf decision) is the orchestrator's,
  built ONLY on the lanes' cited loci; everything in §§1-4 is worker-attributed.
STATUS DISCIPLINE (L0): recon promotes NOTHING. Lane claims tagged fact/inference/speculation by
  the workers themselves; external literature enters as `stated` until byte-matched (L1).
-->

# Open-mechanism recon — four lanes + synthesis (2026-07-05)

## §0 ORCHESTRATOR SYNTHESIS — difficulty ranking and the hardest-leaf decision

Ranking (hardest first), from the lanes' evidence:

1. **Fan-lift K⟨1⟩2 (`conj-degenerate-transport`) — hard, bordering very-hard, and likely
   COUPLED.** Six D-waves narrowed but never closed even the restricted transport statement; both
   "easy" repairs died on exact rank-3 certificates ((SI) false at D3; B-block contraction false at
   D4, ρ_B = 21/20). Lane 3's central inference (moderately confident): the D-line (fan/legal) and
   G-line (orphan/self-support) engines converge on the SAME missing budget (Σβν) and the same
   import block — **possibly one gap wearing two names**. The sketch's own "genuine-gap risk" tag
   is corroborated.
2. **Orphan budget K⟨1⟩3 (`conj-rh`) — hard, bordering very-hard.** Fifth budget-repair cycle;
   survived ~500k+ targeted-random samples with the G11 residual (bound `B_{r,s}+C_{r,s}` by the
   pivot-s budget) pinned but undecided in 3 dedicated waves. The floor C_RH ≥ 4 is exact.
3. **NSC K⟨1⟩5 (`conj-nsc`) — hard.** Strong empirical headroom (K0 ≈ 3 suffices; the only
   explored amplifier family caps at an algebraic 0.77764), but the entire chart-move toolkit is
   PROVABLY blind to every certified carrier (all volume-inadmissible); no replacement mechanism
   exists even in sketch form.
4. **Master decomposition K⟨1⟩6 — hard (bookkeeping-hard, not math-hard).** Lane 4 surfaced REAL
   composition risks nobody had recorded: (a) SC feeds RH *nested*, not additive — the sketch's
   three-term master formula risks double-charging the self-support rows; (b) FanRes appears in
   both registered contracts but is silently absent from the master identity; (c) the "silent row"
   class of NF_s maps onto neither "orphan" nor "self-supported" — K⟨1⟩1 exhaustiveness is
   unverified. Rate side is clean (lane-4 arithmetic: every budget term is individually O(δ)).
5. **Rank transfer K⟨1⟩7 — moderate.** Narrow named residuals only: the Γ-branch/NSC and the c<0
   move were never tested at rank 4 (decider #1 predates wave 13).

**Decision (the most difficult leaf): K⟨1⟩2, the fan-lift — attacked through the COUPLING
hypothesis.** Not NSC (currently frontier by momentum, but strictly easier by the evidence), and
not RH in isolation (if lane 3's coupling inference is right, RH and the fan-lift must be priced
together). The refinement proposal, per the user's breadth-first directive, is in HANDOFF and the
session log; headline: run the three cheap decision-checks FIRST (audit policy) —
  (i) **fusion check**: recompute the D4 ρ_B = 21/20 refuter and the D6 legal-leak certificates
      against the G-line unified budget (pure exact recomputation; decides lane 3's candidate #1);
  (ii) **NSC-ratio direct search**: maximize B/Σβν itself over multi-carrier ν-starved families
      (the objective nobody has run; decides whether conj-nsc is stable ground);
  (iii) **K⟨1⟩6 discharging trace**: on one certified instance with FanRes ≠ 0, trace which master
      term each leaking row is charged to (red/green double-charge check).
Then the refinement wave proper on the fused statement, with the SBD reset-trick composition probe
(lane 3 §4) as the designated fallback branch.

---

## §1 Lane 1 (sonnet): NSC(K0) — verbatim

# NSC(K0) — "Negative Self-Support Charge": State-of-the-Art Brief

## 1. In-repo state (status + locus)

- **`conj-nsc`** — OPEN, `status: conjecture`, `af: seeded`. Contract: `B_{r,s} ≤ K0·Σ_{carriers} β_r(i)⁺·ν_i(P)` at every capped (`δ≤1/4`) θ-½ Φ-argmin, broad form (no branch restriction). `argument/lemmas/conj-nsc.md`.
- **`lem-pivot-removing-move`** — PROVED, `af: validated` (9-node tree). The Schur-swap disjunction `Φ_s(U) ≤ max(Ψ_j,Γ_j)`. `argument/lemmas/lem-pivot-removing-move.md`.
- **`lem-collateral-import`** — PROVED, `af: validated` (32-node tree), **c>0 only**. `argument/lemmas/lem-collateral-import.md`.
- **`lem-negative-pivot-import`** — proved-mod-audit, independent-review APPROVE (not af-validated), the **c<0** companion; exact split gives equality, not just `≤`. `argument/lemmas/lem-negative-pivot-import.md`.
- **`lem-cross-pivot-cancellation`** — PROVED, `af: validated` (23-node tree), near-definitional B-L duality `A=B+C−D`. `argument/lemmas/lem-cross-pivot-cancellation.md`.
- **`conj-sc`** — OPEN, the parent self-support/cancellation conjecture that NSC feeds via the B-lemma. `argument/lemmas/conj-sc.md`.
- **Conditional B-lemma** (review-APPROVED paper proof, not codified as a shard yet): `NSC(K0) ⇒ B_{r,s} ≤ (5K0/4)·δ`. `docs/waves/2026-07-04-G13-b-lemma-conditional.md` §4, review `docs/waves/2026-07-04-G13-review.md`.
- **L3 data**: empirical `B/Σβν` ∈ {≈1.14, 2.79, 2.25} on three certified instances ⇒ any universal `K0 ≥ 2.79`; a family-limit law `sup B/δ ≈ 0.77764` (algebraic, clone-invariant) in the explored "compensated-insert" family. `runs/2026-07-04-b-amplifier-hunt/`, `runs/2026-07-04-small-delta-b-sweep/`.

## 2. Dead routes / obstructions

- **G6 silent-family warning**: pointwise `ν_j ≥ const·a_r(j)⁻` is **FALSE** — an exact family gives ratio `1/κ→∞` for arbitrarily self-supported rows. It is *not* a refuter of the parent (RH) only because the θ-½ argmin pivots away onto the self-supported row itself, killing its own leakage. `docs/waves/2026-07-03-G6-repaired-horn.md` T1/T0.
- **Volume-inadmissible carriers dominate everything certified**: in all three checked stress instances (incl. the 0.77764 maximizer) 100% of the `B`-mass sits where `|a_s(i)|·m_U < 1/2` — the pivot-removing-move machinery is *structurally blind* here (no admissible comparison chart exists). Crucially, this is the **opposite** geometry from G6's rescue: there the argmin *could* pivot onto the offending row; for NSC carriers the pivot swap is definitionally inadmissible, so the G6 escape hatch is unavailable. `docs/waves/2026-07-04-G13-b-lemma-conditional.md` §3a, reviewed.
- **Ψ-blocked admissible carriers**: even when admissible, swapping in the carrier changes the pivot's own left-inverse row to `P_i`, so the transverse import bound (which needs an unchanged left-inverse row) doesn't apply at all. Same source, §3b.
- **Γ-blocked admissible carriers**: the `c<0` import bound only gives a *lower forcing* `Φ_s(U)−Φ_q(U) ≤ I⁻_{q,i}(U)` — a diagnostic, not an upper charge on `β_r(i)⁺a_s(i)⁻`. Same source, §3c.
- **Cloning does not amplify**: duplicate n=7/9 inserts reproduce the identical ratio — consistent with (and a mild positive check of) the repo's clone-invariance discipline (Rule 13); rules out the cheapest amplification strategy. `runs/2026-07-04-b-amplifier-hunt/README.md`.
- **General Rule-13 dead routes** apply if tempted: raw-index path products (cloning-refuted `δ₀≥0.233`), Jensen/convexity, canonical-`g` energy method, pointwise/σ-only selectors — none of these are NSC-specific but any "smooth it with convexity" or "per-row bound" instinct dies the same way G6 already shows for the closest analogous quantity. `FINDINGS.md`.

## 3. Proof-mechanism candidates (ranked)

1. **Argmin-native self-support/idempotence charging (the repo's own designated mechanism, unbuilt).** Since chart-move comparisons are provably blind at every certified carrier, the fix must use `P²=P` row-reproduction *directly* on the carrier rows (not via a pivot swap) — e.g. a second application of idempotence expressing `β_r(i)=P_{u_r,i}` through row `i`'s own image, tying it algebraically to `ν_i` without going through a comparison chart. Supported by: the top-down sketch's own framing of `<1>5` as "row reproduction cannot generate the [G6] balance for free... post-pivot the pattern re-prices with genuine ν on the carriers" (`docs/plans/2026-07-04-top-down-proof-sketch.md` §K<1>5). **Failure mode**: this is exactly the mechanism G13 said it lacked ("NSC must genuinely use argmin/self-support/idempotence structure, not per-row sign accounting") — nobody has produced the actual inequality yet; risk it doesn't exist in this form. **Decisive test**: attempt it symbolically on the 0.77764 stress instance (a concrete, fully certified rational witness already in hand) — if it can't close there, the mechanism is likely dead in general.
2. **Adapt G8's beta-weighted transfer-financing identity `(FE)` to `B_{r,s}` directly.** G8 already proved a structurally similar decomposition — `κ_j W_j ≤ S_j⁻ + Σ P_ji⁺W_i` — for a *different* excess quantity (`W_j`), discharging it via stationarity plus class/SIGMA financing. `docs/waves/2026-07-03-G8-transfer-financing.md` T1 eq.(1)/(FE). Applying the same "multiply-by-β-and-sum, use `P²=P` stationarity to get an exact identity, then split signed" recipe to `B_{r,s}` is untried. **Failure mode**: `(FE)` explicitly controls only `κ_j·W_j`, not `W_j` itself, for high-self (`κ→0`) rows — if NSC's dominant carriers are exactly high-self (plausible, since they're the rows attracted as *near*-pivot candidates), this hits the same wall G8 hit.
3. **SBD reset-trick as a new move-type, not a chart pivot.** Salzmann–Bergh–Datta's Lemma 5.5 (`M=(1−λ)N+λ·reset`) suggests mixing carrier rows toward a canonical positive representative at rate `λ~√δ` rather than swapping charts — this would sidestep volume-admissibility entirely (a genuinely new operation class). Not attempted anywhere in the repo. **Failure mode**: speculative; no existing tool computes what "reset" means for a signed idempotent's row space.
4. **Fallback (repo-designated, bypasses NSC rather than proving it):** if NSC resists, arm E (Luo–Pang/Mangasarian–Shiau degenerate-complementarity Hölder bound applied directly to `{E²=E,E≥0,E𝟙=𝟙}`) replaces Lemma K wholesale — explicitly recorded as the substitution point in `docs/plans/2026-07-04-top-down-proof-sketch.md` "Substitution points". Ranked last because it abandons rather than resolves NSC.

## 4. Refutation candidates (ν-starved carrier families)

To kill NSC one needs a certified capped θ-½ Φ-argmin with a carrier `i` (`β_r(i)>0`, `a_s(i)<0`) contributing large `B`-mass while `ν_i(P)` stays small. Constraints observed to block this so far:
- **Per-row cap from volume-inadmissibility itself**: `|a_s(i)| < 1/(2m_U) ≲ 1`, so a single carrier's contribution is bounded by `β_r(i)`; blowing up the ratio needs *many* small-`ν` carriers, not one huge one.
- **Minimality keeps pulling the "good" nu-starved row into the argmin** (the G6 mechanism) or into a Γ/Ψ-blocking role, exactly as seen in every attempted amplifier construction (G11's 352-candidate sweep found 0 clean-branch instances; G12's amplification probes always lost argmin status).
- **Cloning provably doesn't help** (§2), closing the cheapest "spread mass across many identical nu-starved copies" strategy.
- **The single cheapest untried refuter test**: every existing sweep (`b-amplifier-hunt`, `small-delta-b-sweep`) optimized `B/δ` or `B`/budget as the objective, **not** `B/Σβν` directly — nobody has run a search that directly maximizes the NSC ratio itself, e.g. over families with `k≥3` simultaneous volume-inadmissible carriers each individually low-`ν`. This is a concrete, well-posed, cheap experiment that hasn't been done.

## 5. External literature

- **Kitaev, arXiv:2405.02434** (v2 Feb 2025), §1.2 poses the noncommutative version open verbatim; Prop 3.1 (linear sign-function fix, loses positivity); §§5–9 build an "incremental toolkit" (partitioned-index merge/extend, error-reduction bootstrap Cor 8.3 "δ-inclusion ⇒ O(ε)-inclusion", Lefschetz–Hopf). *Adaptable, not directly-applicable to NSC*: I could not retrieve full-text detail on §§5–9 (arXiv abstract page only exposes the abstract/versions, not section content); the repo's own literature sweep (`docs/lit-review/2026-07-04-literature-sweep.md` §1.1) already flags this as "a structurally different strategy… candidate alternative attack shape" but has not mined it for an NSC-specific self-consistency inequality. Treat as **inspiration-only** pending a real read of the PDF.
- **Salzmann–Bergh–Datta, arXiv:2405.01532**, Thm 5.2 (√ε dimension-free, fixed *distributions*) + Lemma 5.5 reset trick. *Adaptable*: candidate 3 above (§3). Already flagged for a different probe (`aism` reset-trick transfer issue) in `HANDOFF.md`.
- **Goreinov–Tyrtyshnikov / Mikhalev–Oseledets, arXiv:1502.07838** (maxvol): repo already imports the swap-determinant Cramer box `|a_t(j)|≤2` as a **cited** anchor (`docs/lit-review` §2). Targeted web search for "weighted negative coordinate mass at a maxvol-argmin controlled by row residuals" returned only generic maxvol/cross-approximation error-norm results (`‖A−A_maxvol‖ ≤ (r+1)σ_{r+1}`) — nothing matching NSC's shape. **Not found**; no additional tool beyond the Cramer box already in use.
- **Hoffman error bounds / LP duality / complementary slackness** (Hoffman 1952, Luo–Pang 1994, Mangasarian–Shiau 1987): already queued in-repo for arm E's *global* Hölder-1/2 argument, not for NSC. Web search returned only generic Hoffman-constant literature (distance-to-polyhedron bounds, no LP formulation matching a signed-idempotent chart argmin). The idea that NSC is "complementary slackness at a Φ-minimizing chart" (violated-constraint mass `B` bounded by a dual/residual quantity `ν`) is a **formally plausible but currently unsubstantiated parallel** — tag as **speculation**, not backed by any located paper.

## 6. Difficulty verdict

**HARD** (not "very-hard," not "moderate"). Justification: (a) empirical support is strong and consistent — all three ratio-witnesses sit in `[1.14, 2.79]` and the one explored amplification family caps at an algebraic `≈0.7776`, far from any runaway; the statement plausibly has real headroom (`K0≈3`). (b) But the repo's *own* tool built to attack it (chart-move minimality, both `c>0` and `c<0` forms, independently reviewed) has been shown, on every certified instance, to be **structurally blind** to the entire carrier mass — this is not a missing bookkeeping step but a proven inadequacy of the only mechanism developed so far, and no replacement (genuine self-support/idempotence charging) yet exists even in sketch form.

**Most informative first wave, prove-side**: apply G8's `(FE)` stationarity recipe directly to `B_{r,s}` on the existing 0.77764 certified stress instance (cheap — reuses proven machinery and an already-certified exact witness); if it can't reach δ-scale there, the "transfer-financing" strategy class is likely dead for NSC just as it was insufficient alone for `(SC)`.

**Most informative first wave, refute-side**: run an exact search that directly maximizes `B_{r,s}/Σ_{carriers}β_r(i)⁺ν_i(P)` (not `B/δ`) over multi-carrier (`k≥3`), individually-ν-starved families — the one natural adversarial construction that has never actually been the search objective.

---

## §2 Lane 2 (sonnet): orphan budget / (RH) — verbatim

# Brief: Orphan Budget / Repaired Orphan Horn (RH) — K⟨1⟩3 of op-classical

## 1. In-repo state

- **`conj-rh`** (`argument/lemmas/conj-rh.md`) — status `conjecture`, `af: seeded`, workspace `proofs/conj-rh`. Contract: `OD_s^orph(U) ≤ C_RH·(G_class^-(s,U) + S_-^mu(s,U) + SIGMA_s(U)) + C_RH_fan·FanRes_s(U)`, where `OD` = orphan legal demand (`L_mu^orph + F_L^orph + Σ β_s(j)E_s(j)` over *active* orphans), `SIGMA` = `Σ_{β_s(j)>0} β_s(j)ν_j` over **all** beta-positive non-chart rows including silent ones. [fact, locus above]
- **Floor is exact, not heuristic**: the shard itself records `[[obs-orphan-amplifier]]` forces `C_RH ≥ 4` (`argument/lemmas/obs-orphan-amplifier.md`, status `proved-mod-audit`, `af: none`) — a rank-3 two-orphan family `P(h)` with `δ(P(h))=e(1/4+h)/p<1/4` where `OD(h)/(class-only budget) → ∞` but `OD(h)/(class-only budget + SIGMA(h)) → exactly 4`, and simultaneously `Φ_2(U)/δ(P(h)) → 1` (still inside the plateau‑2 evidence, i.e. not an (EX) refuter). [fact, `docs/waves/2026-07-03-G5-orphan-financing-lemma.md` §T0/T1 eqs.(6)-(10); replayed in `docs/waves/2026-07-03-G6-repaired-horn.md` §T0 eq.(5)]
- **`conj-sc`** (`argument/lemmas/conj-sc.md`) — status `conjecture`, `af: seeded`. This is the *literal isolated missing step*: bound the beta-weighted non-fan chart-negative mass (`Σ_{j∈NF} β_s(j)·W_s(j)`) by the same budget. Everything else needed to assemble `(RH)` from `(SC)` is bookkeeping (G7 §"(RH) Assembly Status": if `(SC)` held with constant `C_SC`, plus the closed rank‑3 fact `E_s(j)≤μ_s(j)` on active orphans, RH assembles, necessarily with `C_RH≥4`). [fact, locus in shard + G7]
- **"Every leak has an exact identified financier" means**: across every certified exact instance to date (G3, G4, G5, G6, G9, G10, G11 certificates), no orphan/silent leak has ever gone *unpaid* by SOME term in `{G_class^-, S_-^mu, SIGMA, FanRes}` — the leaks are always traceable to a structural negative-mass source (a class aggregate `Γ_r<0` forced by legality-through-a-positive-coordinate, or the leaking row's own `ν_j`) — but the payment ratio is only *bounded on tested families*, never proved bounded universally. [fact, synthesized across G3–G11 verdicts]
- **Fine-grained sub-DAG (all `docs/waves/`, 2026-07-03/04, worker codex, tier T0-T2, none rigorous)**: G3 orphan rows real (refutes naive orphan-exclusion) → G4 refutes active-orphan-exclusion, gives ratio bound 1 (or 2 with payment) on **one-B-row** family → G5 refutes the class-only budget for **every finite constant** via the 2-orphan cancellation family, forces the `SIGMA` repair with floor 4 → G6 shows ambient `ν_j` and chart negativity are provably *distinct* (silent-row amplifier, ratio `1/κ→∞`) but this survives RH only because the Φ-argmin always **pivots away** onto the self-supported row → G7 derives the exact pivot-removing Schur-move algebra and disjunction `Φ_s(U) ≤ max(Ψ_j, Γ_j)`, isolates `(SC)` as blocked on a **PRC/import control** → G8 derives the exact transfer/stationarity identity `(FE)` (financed-excess is exactly financed by class/signed/legal terms, not a contraction) and pins the residual to a **high-self pivot-removing theorem `(PRT)`** → G9 realizes two of PRT's three branches exactly ((V) ratio 624/4427, (Ψ) ratio 240/451) but the **(Γ) collateral branch is left undecided** → G10 finds a clean (Γ)-pattern witness only *outside* the cap (`δ=49/60`), derives the exact collateral-import inequality `(CI)` → G11 reduces `(CI)`'s dominant term to an exact cross-pivot orthogonality identity `Σ_i β_r(i)a_s(i)=0`, pinning the whole remaining gap to bounding `B_{r,s}+C_{r,s}` (cross-pivot cancellation mass) — **not done**; verdict "(CHARGE): PARTIAL." [fact, all loci above]
- **Frozen since 2026-07-04 G11.** The top-down sketch (`docs/plans/2026-07-04-top-down-proof-sketch.md`, node K⟨1⟩3) lists the orphan budget as 1 of exactly 4 genuinely OPEN mechanisms; subsequent waves G12/G13 pivoted to NSC/the B-lemma (K⟨1⟩5), a *different* open mechanism — RH/SC/(PRT)/(Γ) have had no further work since G11. [fact]

## 2. Dead routes / obstructions

- **Cloning obstruction bans raw index/class counting** (CLAUDE.md Rule 13, `FINDINGS.md`): all budget terms (`G_class^-`, `S_-^mu`, `SIGMA`) must be per-row, beta-weighted, clone-invariant sums — never a naive count of "how many rows in a class." This is *why* the natural first fix ("just weight by class size") is structurally unavailable.
- **The moving-financier problem (G4→G5→G6), the central obstruction.** G4's honest first guess — orphan demand ≤ `C·(G_class^- + S_-^mu + R_D^ν)` — is refuted for **every finite `C`**: two orphans, each legal through its own positive coordinate, cancel each other's would-be class financier (`Γ_r`) via sub-threshold negative coordinates that are *invisible* to the class budget but *are* part of `OD`. The financier doesn't disappear, it **moves into the orphans' own row-negative mass**, which the naive budget doesn't track (`FINDINGS.md` 2026-07-03). The `SIGMA` repair (own-row `ν_j` of every beta-positive row) exactly catches this move — up to the floor 4. [fact]
- **Silent rows are the second escape hatch, structurally analogous but resolved by a different mechanism.** A beta-positive row with *no* volume-permitted coordinate at all can still carry chart-negative mass at arbitrarily small `ν_j` cost via a large positive self-coefficient `P_jj` (row reproduction: `(1-P_jj)a_r(j) = Σ_{i≠j}P_ji·a_r(i)`). This is **not** closed by SIGMA's accounting — it survives only because the Φ-argmin always pivots a pivot-**removing** chart move onto that row and kills `Φ` there (G6/G7). Formalizing "the argmin always saves you" as a universal theorem is precisely `(SC)`/`(PRT)`. [fact]
- **Why per-pivot, per-branch discipline is enforced:** the pivot-removing disjunction `(7)` (G7) is not an error term but a genuine structural trichotomy (volume-inadmissible / Ψ-blocked / Γ-blocked), and `(PRT)` explicitly requires charging **each branch separately** — you cannot average over branches without smuggling in exactly the kind of aggregate "it evens out" reasoning that the cloning obstruction and the G5 refutation both already killed elsewhere in this campaign.
- **What survived, i.e., is NOT a dead route (still live):** G9's (V)/(Ψ) realizations (bounded ratios, understood mechanism); G11's exact reduction of the (Γ)-branch import to `B_{r,s}+C_{r,s}` (a well-defined open target, not a refuted one).

## 3. Proof-mechanism candidates (ranked)

1. **Extend the G8/G11 cross-pivot stationarity algebra one more step.** Mechanism: `Σ_i β_r(i)a_s(i)=0` (B-L duality, already proved) forces `A_{r,s} ≤ B_{r,s}+C_{r,s}`; try to bound `B_{r,s}` (beta_r-positive, `a_s`-negative rows) and `C_{r,s}` (beta_r-negative rows against `a_s`-positive) directly using the *same* row-negative-mass Cramer-box argument that already closed `S_j^-≤4ν_j` in G8 §"(FE)". Support: G8's `(FE)` and G11's `(CI)`/`(4)` are both proved identities, this is their natural continuation, explicitly flagged as the "narrower" open question at the end of G11. Likely failure: `B_{r,s}` is *collateral pivot r's* own budget territory, not pivot s's — mixing pivots may violate the per-pivot-s contract that `conj-rh`/`conj-sc` are literally stated in. Decisive test: build a capped exact instance where `B_{r,s}` is large **specifically relative to `SIGMA_s(U)`** (not `SIGMA_r`) — this is the concrete gap G11 names but does not test.
2. **Prove capped `(Γ)`-emptiness (i.e. show `δ(P)≤1/4` forces `Ψ_j≥M` whenever `Γ_j≥M`, so `(V)∪(Ψ)` exhausts the cap).** Support: G10's *only* clean `(Γ)` pattern lives at `δ=49/60`, far outside the cap; combined capped randomized sweeps in G10+G11 (~500k+ rational samples) found **zero** clean capped `(Γ)` instances. Likely failure: absence of a randomized hit is evidence, not proof — G10/G11 explicitly flag "failed designs are not infeasibility results," and the campaign has three prior instances (D3, G5, G6) where a budget survived random probing only to fall to a *targeted* construction. Decisive test: a **structured** (not random) dilution of the G10 witness's single-row `49/60` cap-violation across `k≥3` auxiliary near-silent rows, attempting to push `δ` under `1/4` while preserving the clean `Ψ_j=0<M≤Γ_j` pattern — this is literally G11's untried "spread/offset" direction, done adversarially rather than by uniform random sampling.
3. **Global conservation/potential (discharging-style) argument.** Mechanism: treat `β_j` as "charge," `P_ji` as edge capacity, and use `P·1=1` as global charge conservation across *all* rows simultaneously (not one pivot-removing swap at a time) to bound total chart-negative mass. Support: the row-reproduction identity is already, structurally, a discharging rule (mass moves from row `i` to row `j` at rate `P_ji`). Likely failure: a global/averaged argument risks reproducing exactly the G5 failure mode — global conservation doesn't prevent *local* concentration of cancellation onto two orphans, which is exactly what defeated the G4 budget. Decisive test: check whether this approach can even mechanically *reproduce* the known floor 4 on the G5 family without an extra per-orphan correction term; if it can't recover a known result it is too weak.
4. **Import a Hoffman/Luo-Pang-style degenerate error bound directly onto the local argmin system** (arm-E style, see §5). Support: the top-down sketch's own `<1>10` already invokes Luo-Pang for the *global* sharp-1/2 exponent; RH is a local instance of the same complementarity degeneracy. Likely failure (flagged in-repo already, different context): imported perturbation/error-bound constants have a documented history in this campaign of failing dimension-freeness (`FINDINGS.md` 2026-07-04, Thiede–Van-Koten–Weare precedent, unrelated tool but same disease). Decisive test: check whether the natural Hoffman-type constant for `{P²=P, row sums 1, sign pattern}` is provably independent of rank/embedding dimension on the G5 family before investing further — if it isn't, stop.

## 4. Refutation candidates

- **What would refute RH:** a *capped* (`δ≤1/4`) exact instance with a genuine clean `(Γ)` branch (`Ψ_j<M≤Γ_j`) where `B_{r,s}+C_{r,s}` (equivalently `I_{r,j}`) is large relative to `G_class^-(s,U)+S_-^mu(s,U)+SIGMA_s(U)+FanRes_s(U)` — driving the ratio unboundedly, per family. This is the exact, pinned, well-specified adversarial target left open by G11. [inference from G11's own "Task 3 Synthesis"]
- **Already tried and SURVIVED** (do not re-attempt as stated): the G5 2-orphan cancellation family (ratio → exactly 4, the canonical near-refuter, now the floor witness); the G6 silent-row amplifier (`ratio→∞` in `κ`, survives because the argmin pivots away); G9's (V)/(Ψ) realizations (bounded, non-amplifying); every multi-row/two-B-row/"spread" construction attempted in G10/G11 to build a capped `(Γ)` amplifier (all either broke `δ≤1/4` or lost the argmin or stayed budget-compliant). [fact, per-wave verdicts]
- **Untried refutation directions (speculative):** a rank-≥4 or higher-multiplicity generalization of the G5 trick — more than two orphans cyclically cancelling across *both* transverse coordinates at once, potentially routing the "moving financier" through a third row invisible to `SIGMA` itself (rather than just to the class aggregate); or exploiting `FanRes_s` as an under-tested escape (all G3–G11 certificates have `FanRes=0`). [speculation, no certificate exists]

## 5. External literature

No directly-applicable external result was found for the exact mechanism (charging a legality-constrained, argmin-dependent, sign-decomposed "demand" by a per-pivot aggregate "supply" under a minimality/pivoting rescue clause) — this negative finding itself corroborates the operational audit's read that this is frontier/original territory.

- **Discharging method** (Wikipedia; Cranston-Yancey survey arXiv:1306.4434) — *inspiration-only*: same "conservation + redistribution, absence of violation forces a configuration" shape; the repo's row-reproduction identity is already, independently, a discharging rule. No borrowable signed/continuous machinery found.
- **Hall's marriage theorem, deficiency form** (Wikipedia) — *inspiration-only*: the "deficiency ≤ max over subsets" shape matches "OD as deficiency, budget as resource," but Hall's theorem is a 0/1 combinatorial existence statement with no obvious quantitative signed-mass bridge.
- **Amortized analysis / potential method** (standard CLRS-style refs) — *inspiration-only*: reframes `Φ(U) - budget` as a potential and pivot-removing moves as "operations"; this is implicitly what G7/G8 already do without the vocabulary.
- **Hoffman error bounds / duality** (Peña-Vera-Zuluaga school; "Duality of Hoffman constants," arXiv:2312.09858) — *adaptable with a strong caveat*: right shape (residual ≤ constant·aggregate constraint-violation) but the repo has an in-house precedent (Thiede-Van-Koten-Weare, flagged `FINDINGS.md` 2026-07-04) of imported error-bound/perturbation constants failing dimension-freeness; any Hoffman-style route would need its own from-scratch dimension-free proof.
- **Högnäs–Mukherjea** (*Probability Measures on Semigroups*) / **Baake–Sumner** equal-input matrices (arXiv:2404.11222) — checked directly; found **no quantitative class-aggregate perturbation statement** of the needed kind (their results are structural/algebraic classification and embeddability, not error bounds). The repo's own sketch already cites this literature only for the *downstream* rounding step (`<1>8`), not for RH — likely the wrong shelf regardless. Tag: **not applicable**.
- **Complementary slackness / saddle-point duality** (standard LP texts) — *inspiration-only*: G7's `Ψ_j`/`Γ_j` disjunction is already complementary-slackness-flavored; no new external quantitative tool found beyond the textbook shape already used informally.
- **Hahn–Jordan decomposition** (standard measure theory) — common-knowledge background already implicit in "cancellation before positive parts"; no new tool.

## 6. Difficulty verdict

**Hard, bordering on very-hard.** Two independent signals converge: (1) this is the *fourth* successive budget-repair cycle in this campaign (D3→R_D^ν, G4→G5, G5→SIGMA, G6→silent-row awareness) each defeated by an adversarial exact family before being patched — a pattern the operational audit independently flagged as suspect "reactive budget-patching" — and the current sub-target `(SC)/(PRT)/(Γ)` is a *fifth* attempt that has now survived 3 dedicated waves (G9-G11) without falling either way; (2) the gap is narrowed to a crisp, well-posed algebraic question (bound `B_{r,s}+C_{r,s}` by pivot-s's own budget) that a competent prover *could* close quickly if it's true, but G11 explicitly could not close it, and no counterexample exists despite ~500k+ targeted-random rational samples — a genuine knife-edge.

**Single most informative first wave — prove-side:** directly attack G11's pinned residual: attempt to bound `B_{r,s}+C_{r,s}` by `C·(G_class^-(s,U)+S_-^mu(s,U)+SIGMA_s(U))+C_fan·FanRes_s(U)` using the same B-L orthogonality/Cramer-box toolkit that closed D4/G5/G8, OR produce the counterexample where `B_{r,s}` is large specifically against `SIGMA_s` (not `SIGMA_r`).

**Single most informative first wave — refute-side:** a *structured* (not uniform-random) dilution of G10's exact `δ=49/60` clean-`(Γ)`-pattern witness across `k≥3` auxiliary near-silent rows, targeting `δ≤1/4` while preserving `Ψ_j=0<M≤Γ_j` — the one search direction G10/G11 named but never executed adversarially.

---

## §3 Lane 3 (sonnet): the fan-lift — verbatim

# The fan-lift (K⟨1⟩2 / `conj-degenerate-transport`) — state-of-the-art brief

Scope: node K⟨1⟩2 of `docs/plans/2026-07-04-top-down-proof-sketch.md`, the only mechanism the top-down sketch tags "genuine-gap risk." All repo loci below are exact file paths; FACT = read directly from a repo file or a locally-held PDF; INFERENCE = my synthesis; SPECULATION = flagged explicitly.

## 1. In-repo state

**What's rigorous (af-validated).** Five discrete lemmas about abstract weighted "fans" (finite families `(w_i,p_i)`, coordinate-sum-zero, weighted barycenter zero): `lem-zerosum-triangle`, `lem-weighted-min`, `lem-negpart-subadditive` (all trivial, validated), `lem-fan-payment` (constant `2`, all-mass denominator), and the sharp one, `lem-fan-payment-restricted` (**D-restricted**, denominator only over rows with positive distance to the pivot, sharp constant `2+√2`, matched by an exact `k→∞` direct-sum family crossing at pivot mass `q₀=1−1/√2`). All five `argument/lemmas/*.md`, `status: proved`, `af: validated`. FACT.

**What the lift needs (`conj-degenerate-payment`, `conj-degenerate-transport`).** At a θ-½ Φ-argmin chart `U`, pivot `s`, `D_s` = rows with `β_s(j)>0`, `E_s(j)>0`, and every covering Schur swap volume-degenerate (`|det C|≤1/2`). The payment horn needs `Σ_{D_s} β_s(j)E_s(j) ≤ C·δ`; the fan lemmas supply this **given** the transverse coordinates `a_t(j)` of `D_s` rows reduce to a zero-sum-zero-barycenter fan with `D_s` as the active/denominator set `A`. That reduction is `conj-degenerate-transport` — `status: conjecture`, `af: seeded`, explicitly "Do NOT af-elevate until a proof sketch exists (genuine-gap abort predicted)." FACT (`argument/lemmas/conj-degenerate-transport.md`, `conj-degenerate-payment.md`).

**A12 (2026-07-03) closed the coordinate half exactly**, `docs/waves/2026-07-03-A12-lift.md`: `|E_j−n(w_j)|≤2|λ_j|` and the positive-β barycenter defect is sourced *exactly* by pivot-row negativity (`B₊·n(b₊) ≤ Σβ⁻·n(w_j)`). What's left is purely the transport statement `(TT): Σ_{D_s}β⁺mu_j ≤ C_tr·δ`. FACT.

**Arm D (waves 1–6, all `docs/waves/2026-07-03-D*`) attacked (TT) and only narrowed it, did not close it:**
- D1: recast (TT) in Högnäs–Mukherjea 1.12 coordinates; row-negativity-only pointwise payment is FALSE (balanced-staircase `e0`: `μ/δ=37873/29970` but `rowneg/δ=121/30000`).
- D2: exact class-aggregate split; proposed `(SI): M_D ≤ C(G_class⁻+S₋^μ)`.
- D3: **(SI) is FALSE** — exact rank-3 death certificate (`δ=1/10` centered fan, `M_D=δ/2`, `G_class⁻=S₋^μ=0`); repaired to `(RSI): M_D ≤ C_src(G_class⁻+S₋^μ+R_D^ν)` with `R_D^ν=Σ_{D_s}β⁺ν_j` (own row-negativity). `(BN): S₋^μ≤C₋δ` proposed, engineered adversarial instances found no break (`worst 3/32`).
- D4: import-decomposition + **B-block "contraction" mechanism killed** (`ρ_B(21/20)>1`, exact certificate) — but that certificate does *not* refute (RSI), only the naive contraction proof route.
- D5: exact β-stationarity ledger; **WIE→RSI composition is tautological** — a legal (non-fan) row's baseline mass `L_μ` leaks into the same import block; names `(FIN)` as the real residual statement.
- D6: **legal leak REALIZED** — exact θ-½ argmin certificates with strict legal (non-`D_s`) rows carrying `μ>0, E>0` alongside active `D_s` tax (`L_μ/δ` up to `999959/1000000`; `F_L>0` realized); `(FIN)` at constant 1 is stressed (`592875/591017>1`).

Verdict of every D-wave: **UNDECIDED**, `Verdict: UNDECIDED` stated verbatim in D2–D5's headers; D6's headline is explicitly a negative ("leak REALIZED"). No wave has attacked (TT)/(RSI)/(BN)/(FIN) since 2026-07-03 — `fr board` shows arm D at 6 pulls, `best:T1`, role `support`, superseded in attention by arm G. FACT (`fr board` output, `.frontier/log.jsonl` cycles 64–81).

**Arm G (waves 1–13+) is a *different*, parallel engine** that took over the legal/orphan/self-support territory D5–D6 exposed, converging on `(RH)`→`(SC)`→`(PRT)`→`NSC(K0)` — now the portfolio's live frontier (`fr board`: "OPEN: (PRT) collateral horn... open link = NSC(K0)"). This is the top-down sketch's K⟨1⟩3–5 (orphan + self-support horns), a *sibling* open mechanism, not K⟨1⟩2. INFERENCE, but strongly supported: G1 (cycle 76, 11:15) launched 33 min after D6 (cycle 71, 10:42) closed with "legal side needs the collateral theorem," and G's early definitions (`L_μ`, `F_L`, class financing `Γ`) are lifted verbatim from D5/D6.

## 2. Relevant dead routes / obstructions

- ⛔ **(SI)** `M_D≤C(G_class⁻+S₋^μ)` — FALSE (D3 centered fan, `M_D=δ/2` vs budget `0`). Own row-negativity `R_D^ν` is unavoidable.
- ⛔ **B-block geometric-series contraction** (`ρ_B := max_j Σ_{l∈B}P_jl⁺ < 1`) — FALSE (D4, exact `ρ_B=21/20`, matched pivot class + Schur-degenerate rows). Any transport proof that tries to bound `M_D` by iterating a positive import operator on the H-M `B`-block dies here.
- ⛔ **"legal β-positive rows with `μ>0` are impossible/absorbable at a Φ-argmin"** — FALSE (D6, `L_μ/δ→1` with `M_D>0` simultaneously; only the A9 max-stationarity disjunction survives, and it gives no useful lower bound on the collateral branch).
- ⛔ **Pointwise `μ_j≤C·ν_j` / per-coordinate slab summation** — dead already at D1 (staircase `e0`); the Schur slab (`|a_t(j)|≤1/2`) gives only `μ_j≤(k-1)/2`, dimension-dependent, useless.
- **Rule-13 class**: any per-coordinate, per-class, or per-near-degenerate-block summation re-imports the class-count wall. The two named red tests every candidate must survive: **no-center `k=6`** (all 7 non-pivot rows in `D_s`, class pressure, `M_D/δ=3/2`) and **balanced staircase** (`e0` tiny `β`, huge `μ/ν` ratio — pointwise-payment killer). Both FACT, D1/D2/D3 tables.

## 3. Proof-mechanism candidates (ranked)

1. **Fuse the D-line and G-line engines (prove `(RSI)+(BN)` jointly with the orphan/self-support financing machinery instead of separately).** *Mechanism:* D5's `(FIN)` needs exactly a bound on legal-row leakage `L_μ` into the H-M `B`-import block — which is structurally the same cross-pivot cancellation ledger arm G built for its `(RH)`/`NSC(K0)` (`Γ_r` class-financing, own-negativity `Σβν`). *Support:* both lines independently converge on `Σβ⁺ν_j` as the missing budget term (D3→R_D^ν, D-line; G5→Σβν, G-line) — the "(SI)→(RSI) pattern repeating" is explicitly noted at both D3 and G5/G6. *Failure mode:* if this fusion is real, the fan-lift may not be closable **before** `NSC(K0)` — contradicting the top-down sketch's implicit treatment of K⟨1⟩2 and K⟨1⟩5 as independent open items. *Decisive test:* re-run D4's `21/20`-refuter and D6's legal-leak certificate through arm G's current best financing constant (`K0~2.8` empirical) and check whether it closes `(FIN)`.
2. **Prove `(RSI)` alone, on the `D_s`-restricted problem, accepting `(FIN)`'s coupling as a separate composed term** (i.e., prove the fan horn *conditional on* a to-be-supplied legal-horn bound `C_legal`, exactly as the top-down sketch's K⟨1⟩6 assembly already assumes additive separation). *Support:* D3/D4's stress tables show `C_src≥1` is forced but never exceeded on the current zoo. *Failure mode:* D5/D6 already show the "conditional on legal horn" framing is not free — the import operator genuinely mixes `D` and `L`; no wave has found a way to bound `M_D` *without* touching `L_μ`. *Decisive test:* a rank-3 exact instance search for `M_D/δ→∞` while `L_μ,F_L=0` (would refute (RSI) outright) vs. one with `M_D` bounded but `L_μ` growing without bound relative to `M_D` (would show the additive split in K⟨1⟩6 is architecturally wrong, not just unproved).
3. **Abandon the H-M-quotient route entirely; attack `(TT)` via row-reproduction + Schur slab directly**, using the fan lemmas' own barycenter machinery (A12 T2) rather than beta-stationarity. *Support:* A12 already gets the λ-defect and barycenter-defect *exactly* — the only gap is `N_D:=Σβ⁺n(w_j)≤Cδ`, which is TT restated in fan coordinates, so this is not new leverage; noted honestly in A12 itself ("The discrete fan lemma is no longer the obstruction... sourcing the right transverse mass"). Low-ranked because it's circular as stated.
4. **Strengthen the chart selector** (make `U0` argmin of a *joint* functional Φ_s + legal/self-support charge, not Φ alone) so the coupling vanishes by construction. *Failure mode:* K⟨1⟩3–5 (orphan, self-support) and the af-validated `lem-pivot-removing-move`/`conj-rh`/`conj-sc` machinery are built on Φ-argmin minimality specifically; changing the selector risks invalidating already-banked arm-G results, forcing a costly re-verification cascade. SPECULATION — no wave has tried this; flagged as a candidate only.

## 4. Fallback analysis: SBD reset-trick (arXiv:2405.01532)

Read directly from the locally-held PDF (`refs-staging/salzmann-bergh-datta-2405.01532/2405.01532.pdf`, extracted to scratch, pp. 24–28). FACT, byte-level.

**Lemma 5.5 (exact statement).** For a channel `N` on separable `H`, state `τ`, `λ∈(0,1]`: `M=(1−λ)N+λ·Tr(·)τ` has a **unique** fixed state `σ=lim M^k`, and for *every* state `ρ`: `‖σ−ρ‖₁ ≤ ‖M(ρ)−ρ‖₁/λ`. Elementary geometric-series proof (contraction rate exactly `λ` per iterate), no dimension dependence anywhere.

**Theorem 5.2 (classical case).** Stochastic `T`, distribution `P`, `TP≈_ε P` ⇒ ∃ stochastic `S`, distribution `Q`: `Q≈_{√ε}P`, `S≈_{√ε}T`, **`SQ=Q` exactly**. Proof: apply Lemma 5.5 with `τ=P`, `λ=√ε`.

**Remark 5.4 (sharpness).** `max{f(ε),g(ε)}=Ω(√ε)` is forced; explicit 3-state family, **can be taken classical** — a direct sharpness sibling to `ex-hume`, flagged in the repo (`RESEARCH_NOTES.md`) as an uncompleted cross-check.

**What it would concretely prove if applied per class.** SBD's theorem fixes **one distribution under one map** (`SQ=Q`); it does not construct an idempotent *matrix*. Op-classical/Lemma K needs `E²=E` — every row of `E` self-consistently fixed under `E` itself, simultaneously across all `k` classes. Applying the reset trick "per class" (SPECULATION on mechanics, since the repo only designates the *shape*, not the construction) would give, per H-M class `C_t`, a nearby stochastic map and law with an *exact* fixed point at cost `O(√δ)` — but reassembling `k` such per-class fixes into **one** globally-consistent stochastic idempotent is exactly the content the literature sweep flags as unaddressed by SBD: *"reassembling per-class fixes into ONE globally consistent partition is exactly Kernel/(EX) content"* (`docs/lit-review/2026-07-04-literature-sweep.md` §1.2). FACT (the quoted sentence) + INFERENCE (the "per-class" operationalization).

**Transfer risks:**
- **Norm match** — good: SBD's diamond-norm/TV-distance on classical channels/distributions reduces to row-sup TV, close to `‖·‖_{∞→∞}`. Low risk.
- **Dimension-dependence** — none in Lemma 5.5 itself (a genuine asset over the combinatorial fan/orphan machinery, which is fighting dimension-dependence at every step).
- **Distribution-vs-matrix gap** — **severe**: SBD's hypothesis is a fixed **vector**, ours a fixed **map**; nothing in Theorem 5.2 forces the `k` per-class reset channels to compose into a single `E` with `E²=E`. This is the "designated fallback shape," not a completed alternative proof — remaining work is comparable in kind (not obviously smaller) than the H-M-quotient assembly the fan/orphan/self-support horns already attempt.
- No repo wave has yet run the "reset-trick transfer probe" flagged in `RESEARCH_NOTES.md` line 139-140 ("Cheap probe before any resourcing" — still unexecuted as of this recon).

## 5. External literature

| Ref | Locus | Applicability |
|---|---|---|
| Salzmann–Bergh–Datta arXiv:2405.01532 | Thm 5.2, Lem 5.5, Rem 5.4 (pp.24-27, verified) | **Adaptable** (fallback shape for K⟨1⟩2, not a drop-in; see §4) |
| Luo–Pang, *Math. Programming* 67 (1994) | degenerate-complementarity error bounds, exponent ½ | **Inspiration-only** — targets arm E (whole-of-Lemma-K replacement), not the fan-lift transport step specifically; constants are instance-dependent in the classical theorem, dimension-free uniformity is exactly our open work |
| Mangasarian–Shiau, SIAM JCO 25 (1987) | companion ½-exponent mechanism | Inspiration-only, same caveat |
| Högnäs–Mukherjea Thm 1.12 | `refs/hognas-mukherjea/hognas-mukherjea-2011.txt:2246-2277` | **Directly used already** — the D-line's coordinate frame *is* H-M 1.12; it gives the class/`B`-row taxonomy for free but "does not itself bound the deviation by δ(P)" (D1, verbatim finding) |
| Kitaev arXiv:2405.02434 | Prop 3.1 (linear signed fix), §1.2 (open-problem statement), §§5-9 incremental construction | **Inspiration-only** for K⟨1⟩2 specifically — the incremental/bootstrap strategy is designated as the K⟨1⟩7 (rank-transfer) fallback, not the fan-lift's |
| Mikhalev–Oseledets arXiv:1502.07838 (maxvol) | Cramer/theta-half box anchor | Already used (cited at main <1>4); not a new lever for the transport gap itself |

No lane in the 2026-07-04 seven-lane sweep found a prior treatment of the transverse-coefficient-tax/degenerate-transport problem itself; it is genuinely novel combinatorics (FACT, sweep headline).

## 6. Difficulty verdict

**Hard, bordering on very-hard.** Two independent reasons: (1) six full waves (D1–D6) narrowed but did not close even the *restricted* (`D_s`-only) transport statement, and the two "easy" repair attempts (`(SI)`, B-block contraction) both died on exact rank-3 certificates — this is not a shallow gap; (2) the D5/D6 evidence that the H-M import block mechanically mixes fan (`D_s`) and legal (`L`) rows suggests K⟨1⟩2 may not be solvable in isolation from K⟨1⟩3–5 (arm G's `NSC(K0)`/`(RH)`/`(SC)`), which is itself the sketch's other still-open innermost mechanism — i.e., this could be one gap wearing two names, not two independent gaps (INFERENCE, moderately confident).

**Most informative first wave, prove-side:** re-run D4's exact `21/20` B-block refuter and D6's legal-leak certificates *through* arm G's current-best financing constants (the `K0~2.8` empirical NSC bound and the `Σβν` repaired-orphan-horn budget) and check numerically/exactly whether `(FIN)` closes at any finite constant when the two engines' budgets are combined. This is cheap (pure recomputation on existing exact instances, no new proof machinery) and would immediately confirm or refute candidate #1 in §3.

**Most informative first wave, fallback-side:** execute the still-unrun "reset-trick transfer probe" from `RESEARCH_NOTES.md` — construct the SIMPLEST possible per-class application of Lemma 5.5 on a rank-3 exact instance from the existing zoo (e.g. the D3 centered fan or the D4 refuter, both already exact-Fraction-verified) and check by direct computation whether the two per-class reset fixed points compose into anything resembling a genuine idempotent `E`, or whether the composition gap is itself `Ω(1)` (which would kill the fallback outright rather than leave it as an untested "designated shape").

---

## §4 Lane 4 (sonnet): master decomposition + rank transfer — verbatim

# Brief: The Fourth Open Mechanism — Master Decomposition (K‹1›6) & Rank Transfer (K‹1›7)

Scope: `docs/plans/2026-07-04-top-down-proof-sketch.md` Lemma K block, `argument/lemmas/conj-{sc,rh,ex,nsc}.md`, `docs/waves/2026-07-04-G12-b-question.md`, `runs/2026-07-04-rank4-transfer-decider/`, the 2026-07-04 audit + lit-sweep, `FINDINGS.md`. Read-only recon; no repo file touched.

## 1. In-repo state — the three horn interfaces, side by side (fact, with loci)

`conj-sc.md:4` and `conj-rh.md:4` share, **verbatim, character-for-character**, the definitions of `G_class^-(s,U)`, `S_-^mu(s,U)`, `nu_j`, `SIGMA_s(U)`, and `FanRes_s(U)`. This is not a coincidence of notation — it is the identical budget currency reused across two nominally different "horns":

| term | conj-sc target | conj-rh target | K‹1›6 master formula |
|---|---|---|---|
| `G_class^-+S_-^mu+SIGMA` | RHS of `Σ_{NF_s} β_s(j)W_s(j) ≤ C_SC·(…) + C_fan'·FanRes` | RHS of `OD_s^orph ≤ C_RH·(…) + C_RH_fan·FanRes` | appears once, as `C_RH·(G^-+S_-^mu+Σβν)` |
| `FanRes_s(U)` | additive term, coefficient `C_fan_prime` | additive term, coefficient `C_RH_fan` | **absent** from the written master identity |
| self-support (`B_{r,s}`/NSC) | not in conj-sc's contract at all | not in conj-rh's contract at all | flat `(5K0/4+2)·delta` term |

`conj-sc`'s own role line (`conj-sc.md:16`) says it is "the isolated missing step for `conj-rh`"; `conj-rh`'s reduction-status line (`conj-rh.md:20`) says RH "is expected to assemble from `conj-sc` plus the fan horn, but no proof is recorded here." So **(SC) is a proof-internal ingredient of (RH)**, not a parallel additive horn.

`lem-collateral-import.md:31` states explicitly that the (PRT) collateral question is "whether `I_{r,j}` is charged to `G_class^- + S_-^mu + SIGMA + FanRes` … for high-self non-fan rows `j` (`conj-sc`)" — i.e. the *self-support* Γ-branch (NSC/PRT, K‹1›4-5) is meant to resolve **inside `conj-sc`'s proof**, for `conj-sc`'s high-self sub-case (`docs/waves/2026-07-03-G8-transfer-financing.md:287-290`: display `(PRT)` is stated "for `J=NF` and every high-self [row]" — `NF` = `conj-sc`'s own `NF_s`, restricted). So the dependency is nested: **NSC ⊆ PRT ⊆ (high-self slice of) SC ⊆ RH**, not three siblings.

## 2. Composition risks (inference, flagged explicitly as such)

- **Likely double-charge, not yet resolved:** the top-down sketch's K‹1›6 formula sums fan + `C_RH·(budget)` + `(5K0/4+2)·delta` as three *independent additive* terms. But per §1, the self-support contribution is architecturally *nested inside* the derivation of `C_RH` (via SC), not disjoint from it. If `C_RH` is ever derived by a route that already spends the NSC/high-self bound internally, adding `(5K0/4+2)·delta` again on top double-counts the same leaking rows. No shard resolves this; it is exactly the kind of gap the mission asked to surface. [inference from §1 loci, not stated anywhere in-repo]
- **`FanRes` silently dropped.** Both registered contracts carry an explicit additive `FanRes` term; the master identity does not. `obs-orphan-amplifier.md` shows a family where `FanRes(h)=0` and the `C_RH≥4` floor is tight *without* `FanRes` — so `FanRes=0` is not universal, it's family-specific. No lemma bounds `FanRes_s(U) = O(delta)` anywhere found; its omission from K‹1›6 is either an unstated absorption claim or a real gap.
- **Taxonomy exhaustiveness is unverified.** K‹1›1 claims leaking rows partition exhaustively into fan-financed / orphans / self-supported. The *registered* taxonomy (`conj-sc.md:4`'s `NF_s`) instead splits non-fan rows into active-orphan / lambda-positive-orphan / **silent row** (defined purely by a Schur-volume-factor covering criterion, ≤1/2 for every cover). Nothing in-repo maps "silent row" onto either "orphan" or "self-supported" — it reads as a genuinely separate geometric case. If silent rows are non-empty and not covered by any of the three K‹1›6 budget terms, the decomposition isn't exhaustive. [inference — flagged, not resolved in-repo]
- **No horn's budget contains `Phi_s` itself** — checked directly: `G_class^-`, `S_-^mu`, `SIGMA`, `FanRes`, `B_{r,s}`, `nu_s` are all defined independent of `Phi`. No literal circularity found at the definition level. `FanRes_s(U)` does reference `Phi_s(U - u_t + j)` (a *different chart's* `Phi_s`), which is legitimate (comparison, not self-reference) but is the one place `Phi` enters a budget term — worth double-checking under composition.
- **Naked-delta caveat (G12 §Q2, `aism-z98`):** confirmed **no rate obstruction** — no assembly step needs `o(delta)`, only universal constants (`docs/waves/2026-07-04-G12-b-question.md:199-227`). But "`conj-sc`/`conj-rh` as registered do not literally include a naked `+C_δ·delta` term" (G12 verbatim) — the PRT skeleton's step 6 (`C_{r,s} ≤ 2·delta`) is exactly such a naked term, currently unabsorbed into either contract. `HANDOFF.md:94` / `FINDINGS.md:135`: deferred to wave 14, contingent on how NSC resolves.
- **Independent rate check (I performed this arithmetic, not found pre-computed in-repo):** each of `nu_s`, `G_class^-`, `SIGMA`, `S_-^mu` is individually `O(delta)` given `nu_i≤delta` by definition and the θ-half Cramer box (`|a_t|≤2`, <1>4) — e.g. `SIGMA ≤ delta·(1+delta) ≤ (5/4)delta` using the row-sum identity `Σβ_s(j)^+ = 1+Σβ_s(j)^-`. So the *rate* of K‹1›6 looks sound; the *bookkeeping/double-charge* risk above is the live one, not a rate risk.

## 3. Rank-transfer state (fact, with loci)

`conj-sc`, `conj-rh`, `conj-nsc` **all literally state "for every rank-3 exact signed idempotent P"** in their registered contracts (grep-confirmed, `conj-{sc,rh,nsc}.md:4`). `conj-ex` states "rank>=3". So every horn feeding Lemma K is written at rank 3 only; the target is not.

`runs/2026-07-04-rank4-transfer-decider/README.md` certified (exact ℚ, orchestrator-recomputed):
- Pivot-removing disjunction and the **`c>0`** (CI) transcription hold at rank 4 (48 moves, 144 pairs, worst CI slack exactly 0) and at 3 rank-5 probes.
- No blow-up: `Φ/δ` plateau intact (max 5/4 rank-4, 4/3 rank-5, "slow climb toward 2").
- `B/δ ≤ 0.326` at rank 4 — first nonzero-B instances outside rank 3, still sub-δ.

**Explicitly NOT tested** (README §4, honest scope): the `c<0` pivot-removing move; any clean high-self non-fan Γ-branch at rank 4 (**zero** certified — same 0/352 emptiness pattern as rank 3, `conj-nsc.md:29`); the NSC/B-lemma inequality itself was never run at rank 4 (this decider predates wave 13/14); only 2 rank-4 families × 3 scales + 3 rank-5 probes — a finite deterministic enumeration, not a search over all rank-4 signed idempotents. Convention note: over *all* ordered pivot pairs the same rank-4 instance realizes `B/δ=1` at a *non-maximal* pivot — harmless for the stated (pivot-specific) B-lemma but a reminder the two conventions aren't interchangeable.

**Verdict already in-repo:** "decider #1 PASSES — no evidence the skeleton is rank-3-parochial; the rank-generalization risk stays open as *proof* work but loses its 'machinery visibly breaks at rank 4' kill scenario" (README, audit §7).

## 4. Mechanism candidates

**K‹1›6 (master identity), ranked:**
1. **Resolve the SC→RH nesting first, then write K‹1›6 as a genuine sum over a *verified-disjoint* partition** — pin down whether `C_RH` is meant to be derived *using* `conj-sc`'s bound (making the self-support delta-term redundant) or whether K‹1›6's three terms are meant to charge three *provably disjoint* row sets. This is a bookkeeping/definition task, not new mathematics — cheapest high-value move.
2. **Bound `FanRes_s(U) = O(delta)` explicitly (or prove it's dominated by the fan term `nu_s`)** — currently an unstated absorption; needed before the master formula can be honestly "mechanical given the horns."
3. **Settle the "silent row" taxonomy gap** — either show silent rows are a (possibly empty, possibly dominated) subset of orphans/self-supported, or add a fourth term.
4. Only once 1–3 are settled: write the single registry shard the sketch already flags as mandatory ("MUST be codified as one shard so the linker sees the wiring," `<1>6`).

**K‹1›7 (rank transfer), ranked:**
1. **Direct transfer, extended decider** — cheapest: rerun the rank-4/5 decider machinery but *specifically* hunting a clean high-self non-fan Γ-branch (never certified at any rank) and the `c<0` move at rank 4, since these are exactly what wave 13/14 need and what decider #1 didn't test. If the skeleton keeps transferring, K‹1›7 likely falls out of the rank-3 proofs by literal re-derivation (the sketch's own claim: "per-pivot, clone-invariant, boxed, per-row-budgeted — no index/class counting").
2. **Kitaev-style incremental bootstrap** — designated fallback only; heavier, changes proof architecture (one-shot argmin → monotone refinement). Reserve for if (1) finds a genuine rank-4 break.

## 5. External literature (fact, tagged; one primary-text fetch attempt failed — see caveat)

- **Kitaev, arXiv:2405.02434** (v2, scout-verified in-repo, `docs/lit-review/…md:24-48`): Prop 3.1 = our `<1>1` (linear sign-function idempotent fix, cited already in the sketch). §1.2 states the general (noncommutative) analogue of `op-classical` as explicitly open. §§5–9 build the target C*-algebra *incrementally* (partitioned-index merge-and-extend), landing at Cor 8.3 "δ-inclusion ⇒ O(ε)-inclusion independent of δ" plus a Lefschetz–Hopf fixed-point existence step. **Caveat (my own attempt, this session):** I tried to fetch/verify §§5-9 directly (arxiv abs page, raw PDF, ar5iv) and all three failed to yield readable text in this environment — the description above is the *already scout-verified* in-repo summary, not independently re-checked by me today. Applicability: **adaptable, not directly applicable** — his induction is on an algebra built from merged index-classes, dimension-independence comes from the merge rule only depending on local overlap sizes, not ambient dimension; porting to the commutative/chart setting would mean replacing the one-shot θ-half argmin chart by an incrementally-refined chart sequence, which is precisely the sketch's own designated fallback shape.
- **Salzmann–Bergh–Datta, arXiv:2405.01532**, Lemma 5.5 reset-trick: **inspiration-only** for K‹1›6 (their financing is per-fixed-vector, not per-idempotent-map; already noted in-repo as the fan-lift's fallback, not the master-decomposition's).
- **Discharging method (graph coloring)** — general web survey found (Wikipedia; "A Guide to the Discharging Method"), confirms the standard hygiene requirement for any assembly/partition-of-demand argument: **every discharging rule must preserve the total charge sum** (no rule may create or destroy charge, only move it) — directly names the risk in §2 above: K‹1›6 must show its three terms are charging *disjoint* row-sets exactly once, not that each term independently bounds an overlapping superset. No literature found specific to non-double-counting in *non-graph* assembly/budget arguments (searched; nothing closer than the general discharging-method literature was found).
- **Rank-induction for structured-matrix stability** — searched; found only generic finite-rank-perturbation operator theory (Jordan chains, spectral idempotents under finite-rank perturbation) with no rank-*induction* scheme resembling what K‹1›7 would need; **inspiration-only at best**, nothing adaptable identified.

## 6. Difficulty verdict

**K‹1›6 (master decomposition): HARD.** Not because any single inequality is missing, but because the *interfaces don't obviously compose*: SC feeds RH (nested, not additive), FanRes is dropped without justification, and the K‹1›1 taxonomy doesn't verifiably match the registered `NF_s`/`O_act` split (silent rows unaccounted). This is bookkeeping-hard, not math-hard — but until it's untangled, "mechanical given the horns" is an unverified claim, not a fact. **Most informative first wave:** a pure definitional-audit wave (no new proof) that traces, for one certified instance with nonzero `FanRes` and a nonempty silent-row set, exactly which K‹1›6 term each leaking row's `Phi_s` contribution is charged to — a red/green discharging-consistency check, cheap and decisive.

**K‹1›7 (rank transfer): MODERATE.** Decider #1 already killed the "visible break at rank 4" scenario for the disjunction and `c>0` (CI); the risk that remains is narrow and named (Γ-branch/NSC untested at rank 4, `c<0` untested). **Most informative first wave:** extend the existing rank-4/5 decider script to specifically hunt a clean high-self non-fan Γ-branch and a `c<0` pivot-removing instance at rank 4 — same machinery, narrow scope, would directly settle whether K‹1›7 needs anything beyond literal re-derivation or must fall back to the Kitaev-style bootstrap.
