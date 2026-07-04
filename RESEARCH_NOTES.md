<!--
ROLE: open research directions + reference-acquisition queue + deferred decisions. The "what next / what
  to read" file. HOW-to-work is in CLAUDE.md; live gotchas in FINDINGS.md; current state in HANDOFF.md.
UPDATE POLICY: append/curate; mirror the live directions into `fr` arms and the acquisition queue into
  refs/manifest/SOURCES.md. TRIGGER: a new open question, a reference to acquire, or a deferred decision.
-->

# RESEARCH_NOTES — open directions, refs queue, deferred decisions

## The north star (open)

Deliver a **fully mathematically rigorous proof of `op-classical`**: universal `η₀, C > 0` (dimension-free)
s.t. every row-stochastic `Q` with `‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀` is within `C·√η` of a stochastic idempotent
(sharp exponent 1/2). Upstream reduced this — through audited / mod-audit steps — to a single open input,
the **Kernel / (EX) conjecture** (`PRD.md`). Our job is to make one full path rigorous (byte-matched refs
where the literature suffices, `af`-validated where new reasoning is needed).

## Live exploration directions (mirrored in `fr` arms — run `fr board`)

- **A (primary)** — Prove the **(EX) kernel at rank ≥ 3**: every rank-≥3 signed idempotent `P` with `δ ≤ ¼`
  has a θ-½ actual-row chart `U₀` with `max_s Φ_s(U₀) ≤ δ` (empirical `C₀=1`). Obstruction: a geometric
  tie-selection argument for max-volume actual-row charts, charging the two rank-3 bad wedges at each vertex
  to the pivot row's negative mass without losing to positive-β cancellations. (`C₀<1` refuted.)
- **B (primary)** — The **sigma-cap** (`σ_v ≤ 1−c·τ` for hidden top vertices; see the fr board), plus the
  corrected Route-B statement **`conj-skinny-shadow-cap`** (skinny two-shadow cap at the `√δ` scale).
  `lem-dual-localization` was RETIRED 2026-07-04: its transcribed contract ("reproduce `‖Ēbar‖₁ ≥ H` from
  `P²=P`") is a distance tautology (B1 + independent codex verifier; `docs/LEARNINGS.md`). Minimal deciding
  config recorded upstream (skinny pair `v₁=(½,½+p,−p)`, `v₂=(½+g,½−g+p,−p)`, `g<ρ`).
- **C (support)** — **Repair the local-linear-law assembly**: combine the four audited variety lemmas
  (tangent-cone, ambient fixed-mass visibility, mass-removed boundary-recoding, stratified distance) into
  `H ≤ C_loc·δ` near the Högnäs–Mukherjea locus, via a nearest-branch recoding (the prior attempt broke by
  factors 12.8–128 on a nearest-branch test).
- **D (support)** — **Global gap via Högnäs–Mukherjea Theorem 1.12** (the signed structure theorem):
  quantify how near-positivity forces proportional-row classes toward equal-input blocks; the single named
  open of the w25–w31 line is the transverse coefficient tax
  `Σ_j (P_{u_s j})₊ · Σ_{t≠s} (−a_t(j))₊ ≤ C_μ·δ`. Also: signed quantitative **Baake–Sumner** stability.
- **E (exploratory)** — **Łojasiewicz / error-bound route**: frame the linear law as a semialgebraic error
  bound (Hoffman 1952, Luo–Pang 1994) and/or as quantitative stability of norm-one (contractive) projections
  on `ℓ∞_n` à la Douglas–Andô (the H–M family is the norm-one case, `‖P‖ = 1+2δ`). Plus the higher-rank NDG
  multi-row-swap horn and the band-edge sup-vs-averaged leakage bound (`λ_T ≤ c(1−q)τ`).
- **F (exploratory)** — **Numerical cross-checks**: exact-arithmetic LP enumeration / certified instances of
  candidate bounds and of (EX) at higher rank. NON-rigorous — feeds `runs/` bundles only, never promoted.

*(Refine as re-establishment surfaces sharper sub-questions; add arms with `fr arm add`. DEAD routes are in
`FINDINGS.md` — do not register them as arms.)*

## Reference-acquisition queue

Ingested / to byte-verify (`refs/manifest/SOURCES.md`):
- `baake-sumner-2007.11433` — equal-input & monotone Markov matrices (the commutative idempotent structure).
  arXiv e-print reproducible.
- `hognas-mukherjea` — *Probability Measures on Semigroups* (2011): the δ=0 anchor, Thms 1.11 / 1.12 / 1.16
  (idempotent probability measures; signed structure theorem). Copyright — cache-only; byte-quote the `.txt`.

Staged (in `refs-staging/`, to promote per-def when cited): Douglas 1965 (contractive projections on `L₁`),
Andô 1966 (contractive projections in `Lp`), Flor 1969 (groups of non-negative matrices), Hoffman 1952
(error bounds for linear inequalities — the Łojasiewicz anchor), Luo–Pang 1994 (error bounds for analytic
systems), Meyer 1989 (stochastic complementation / uncoupling Markov chains), Chakraborty–Rao 2001
(convolution powers of probabilities on stochastic matrices).

## Deferred decisions (escalate before resolving)

- **First `af` elevation target:** `lem-classical-equiv` (re-validate the upstream-validated signed↔stochastic
  bridge — the low-risk warm-up that gives the first in-repo-rigorous result). Then a `proved-mod-audit`
  theorem (`thm-rank-one` or the `S*≤2Φ+6δ` factorization).
- **Which finer vocabulary to shard next** (`def-actual-row-chart`, `def-phi-excess`, `def-row-polytope`):
  add when the (EX) working-form lemmas are seeded into `argument/`.
- **Banking oracle design** — register a claim-specific oracle only when the first bankable claim exists
  (`FINDINGS.md`).

## 2026-07-03 — strategist synthesis at session-4 close: the conjectured shape of the full proof

Three-tier architecture: (1) the reduction scaffold (signed equivalence + factorization, rigorous;
exposed-hull chain re-establishable); (2) THE ENGINE — conjectured to be a signed
**circulation/flow-conservation argument over the family of volume-permitted swaps at the
Phi-argmin**: weighted sum of the A9 stationarity disjunctions arranged so collaterals telescope
against the D5 financing ledger, with the rigorous fan lemmas (2 and 2+sqrt(2)) as the local
exchange rate and the proved delta-budgets (Gamma^-, beta^-, R^nu) as the boundary terms. Evidence:
every exact identity sought was provable; every one-sided estimate died or went tautological
(cancellation-dependence); the horns coupled (D5/D6). The single missing lemma: "the beta-weighted
excess of the argmin chart, summed against the stationarity disjunctions of all legal swaps,
telescopes to the delta-budgets." First campaign statement that would genuinely USE minimality.
(3) the sqrt-delta envelope only at the exposedness window + ex-hume sharpness. Alternative
writeup of (2): constructive H-M rounding via the Thm 1.12 CONVERSE (cluster at sqrt(delta) scale,
MERGE classes — never select — then project B-rows onto the (1.2)/(1.3) nonnegative polytope);
same engine, cleaner narrative. Constants: C0=2 conjectured true (fan rate); a circulation proof
lands C0 ~ 20, C_sf ~ 50, op-classical C in the low hundreds. Credence (EX) true: ~80/20; the
refutation program shares the same next object (amplify vs telescope the D6 leak).

## 2026-07-03 — session-5 (arm G, waves G1–G8) synthesis: the engine survived contact and has ONE sub-gap

The flow-conservation conjecture above survived eight adversarial/proof waves and is now REALIZED as a
concrete architecture: **fan horn** (G1/G2: fan-matched weights `w=a_t(j)⁻/μ_j` telescope every certified
legal leak, incl. exact F_L, residual constant 0) **+ repaired orphan horn (RH)** (`OD ≤
C_RH·(G⁻+S⁻^μ+Σ_{β>0}βν)`, exact floor `C_RH ≥ 4`, survives every certified instance) **+ (SC)** the
argmin self-support/cancellation control, itself reduced to **(PRT)** — charge the three pivot-removing
blocker branches (volume-inadmissible / Ψ-blocked / Γ-blocked) to `G⁻+S⁻^μ+SIGMA+FanRes`. The evidence
pattern across all 8 waves: **every exact leak found has an exactly identifiable financier** (class
aggregate → own-negativity → pivot-removing moves), and each refuted candidate died only by a budget that
was too small, never by an (EX)-threatening amplifier (the G5 family has `Φ_s/δ → 1`). Toolkit banked at
T1 (worker paper-proofs, unreviewed): G5 harmonic/cancellation ledger, G6 ambient/chart identity +
`E_s ≤ μ_s` payment overhead, G7 pivot-removing disjunction `M ≤ max(Ψ_j,Γ_j)` (the first statement that
uses minimality), G8 transfer financed-excess identity (reproduces D5's financing on the D4 refuter to
the penny). Dead this session (FINDINGS): both orphan exclusions, the class/signed-only orphan budget,
pointwise silent domination `ν_j ≥ a_r(j)⁻`, and rank-3 pure-legal `C_legal=0`. Credence (EX) true:
unchanged ~80/20, with the refutation program now sharing (PRT) (an unpayable blocker family = the
reshaped kill). Next attack on (PRT): per-branch exact realizability FIRST (build or exclude each blocker
type at an argmin), not another aggregate pass — two aggregate waves (G7, G8) went OPEN.
