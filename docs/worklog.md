<!--
ROLE: append-only narrative session history (the accreting counterpart to the always-"now" HANDOFF.md).
UPDATE POLICY: APPEND a dated entry each session close; never rewrite past entries. HOW-to-work is CLAUDE.md.
-->

# Worklog — append-only session history

## 2026-07-02 — repository stand-up (day 1)

Stood up the scientific-exploration infrastructure, synthesised from the sister repos
(`perturbation-frontier-explorer` skeleton + rigour ladder; `extension-property` CI + `af` orchestration;
`arithmetic-quantum-mechanics` sharded-lab-book enforcement; `frontier`/`fr` controller; `vibefeld`/`af`
formaliser). Concretely:

- **Governance:** `CLAUDE.md` (== `AGENTS.md`), `PRD.md`, `README.md`, `CONVENTIONS.md` (rigour-rung table
  incl. the repo-specific `proved-mod-audit` rung + stochastic/signed notation), `FINDINGS.md` (founding
  faithfulness flags + inherited dead-route certificates), `RESEARCH_NOTES.md` (fr arms A–F), `INDEX.md`,
  this worklog, `docs/LEARNINGS.md`.
- **CI spine (Layer 3):** ported the gate scripts (`check-defs.py`, `argument.py` linker with a
  `proved-mod-audit` status, `check-refs.py`, `check-provenance.py`, `check-runs.py`, `fetch-refs.py`,
  `af-orchestrate.py`, `seed-af-workspaces.py`, tests) and added the AQM `check-report-shards.sh`
  (re-prefixed `AISM-`, adapted to the `report/main.tex` + `report/sections/` layout). `af` paths
  parameterised via `AF=${AF:-…/vibefeld/af}`. `scripts/check-all.sh` is **GREEN** on the scaffold and the
  LaTeX report builds.
- **Ingest / defs / refs:** ingested the curated classical-portfolio core into `docs/ingest/` (honestly
  re-tagged); seeded the Definitions DB with the core stochastic/signed vocabulary; set up the `refs/`
  manifest (Baake–Sumner, Högnäs–Mukherjea) + staged the contractive-projection/error-bound background.
- **Knowledge DAG:** seeded `argument/` from the ingested reduction chain
  (`op-classical ⇐ op-exposed-hull ⇐ HLC ⇐ Kernel/(EX)`), each node honestly tagged.
- **Controller:** `fr` campaign initialised (goal = `op-classical`; FRONTIER = the Kernel/(EX) conjecture;
  arms A–F).

**Nothing is rigorous in-repo yet** — the DAG is seeded from the classical-portfolio with honest status; the
first `af` elevation target is `lem-classical-equiv`. See `HANDOFF.md` and `bd ready`.

## 2026-07-02 (session 2) — sync-beads live, chain wired, FIRST RIGOROUS RESULT banked

- Implemented `argument.py --sync-beads` (pure planner + serialized bd executor; idempotent;
  reviewer-hardened: `--limit 0`, `--type blocks`, injectable-runner tests 80/80) — `bd ready` now == the
  proof frontier. Commits `17c9293`, fix `a2d78ce` context in `e68d1b6` chain. Independent opus review:
  REQUEST-CHANGES (1 MAJOR latent truncation-duplication, 1 MINOR dep-type, 2 NIT) → all fixed → APPROVE.
- Wired the missing final edge of the reduction chain: `op-classical` deps =
  `thm-classical-factorization; prop-approx-simplex` (ONE composed route, AND not OR — ingest-cited).
  Commit `c2d828f`. North star now correctly BLOCKED over 8 ancestors down to `conj-kernel`.
- **Banked `lem-classical-equiv`** (commit `e68d1b6`): af orchestration run 1 (8 rounds) built a 28-node
  tree, converged to 16 validated, exit classification = 1 MISSING fact (negative-mass formula) + sibling
  dep hygiene; orchestrator provisioned `def-negative-mass` + `def-almost-idempotent` onto the shard
  (`a2d78ce`); resumed `--phase verify` → root `validated`, taint 29/29 clean, in 7 more rounds. Oracle
  `af-lem-classical-equiv` registered; `fr verify` PASS; `fr log R banked` (new support arm R), tier T0.
  Brittleness WARN (29 nodes) accepted, factoring decision filed `aism-6ec`.
- Roles set by user: orchestrator = knowledge/strategy overview + direction evaluation, NEVER proof
  verification; no Fable subagents without permission (codex/opus/sonnet).
- Strategy review filed 2 constant-hygiene issues: `aism-8bi` (C₀ 1 vs ≥5/4 tension), `aism-z48`
  (H/δ = 2.000000000013 fuzz in an "exact" record). Standing fr decision: EXPLORE arm B next.

## 2026-07-02 (session 2, continued) — three waves harvested; frontier re-scoped to σ̃→1

- Arm B wave 1 (opus): OBSTRUCTION — obs-deep-leakage (heuristic shard) closes local-at-v routes;
  arm re-aimed at anti-splitting. Wave 2 (opus): OBSTRUCTION — obs-fwr-gap (heuristic shard) closes the
  web-rigidity family; s5 arithmetic independently recomputed over ℚ. lem-canonical-separator +
  lem-wiggle-rigidity imported as proved-mod-audit inputs. Commits fb305e7, 99e098c.
- Arm F wave 1 (opus): STALL-MAP over ~48k exact idempotents — dangerous regime never entered; collapse
  bound H(1−σ̃) ≤ ν(2+4δ) 0/500 (obs-height-collapse, the CANDIDATE FINISHER: + σ̃ ≤ 1−cτ ⇒ kernel
  closes); CERTIFIED finite-δ linear-law exceedance H/δ = 100/49 (hull-dip; kernel-safe; FINDINGS
  corrected). L3 bundle runs/2026-07-02-web-regime-hunt/ (first bundle through check-runs); headline
  certificate independently recomputed by the orchestrator. Commit 41218bf.
- obs-height-collapse seeded (861a737) and its codex orchestration launched in background.
- Tooling feedback for the fr/af maintainer agents: docs/tooling-feedback/{FR,AF}-FEEDBACK.md (5ddf3ca).
- fr decisions this stretch: B died→died (frontier reduced twice), F progress (T1), standing decision
  EXPLORE R (elevation in flight). Registry at 23 nodes; only lem-classical-equiv rigorous.

## 2026-07-02 (session 2, close) — SECOND rigorous result: the collapse bound, af-validated

- obs-height-collapse run 1 ABORTED [STUCK] (compound contract — my seeding error); contract narrowed
  to the bare inequality (0<delta, consequences to body), re-seeded, run 2 VALIDATED: 19/19 nodes,
  taint clean, 6 rounds. Banked via oracle af-obs-height-collapse (fr verify PASS, arm R pull 2, T0).
  Commits 30dada7, a2df348, + banking commit. The FIRST NEW (non-inherited) rigorous result.
- Frontier now: af-validated collapse bound + OPEN sigma-cap (sigma_v <= 1-c*tau for hidden top
  vertices) => Kernel Conjecture. Arm B re-aimed at the sigma-cap with a pre-registered kill
  (an exact instance with sigma->1, H>B*tau at small delta kills the route).
- Process lesson banked (bd remember): af elevation contracts = single minimal statements.
- Known WARNs (accepted): two validated trees >12 nodes (29 + 19) trip brittleness on every gate run;
  factoring decisions tracked in aism-6ec / feedback item 10.

## 2026-07-02 (session 2, final) — B3+F2 synthesis; halo-robust finisher staged; wind-down at quota

- Arm B wave 3: OBSTRUCTION "one-sided ledger" — sigma-cap asks for the lower bound on the quantity
  the validated collapse caps from above; only route = anti-splitting; sigma-cap => kernel RIGOROUS
  (the one validated bridge). Arm F wave 2 (decider/refuter): eps=0 cap EXACTLY FALSE (instance C,
  sigma=5343/5000>1 pure self-mass, orchestrator-recomputed); halo-robust cap survives with margin
  (sigma_g <= 0.37tau over ~25k). Bundles: runs/2026-07-02-sigma-cap-refuter/. Shards:
  obs-sigma-halo-nonrobust (numerical), conj-halo-collapse + conj-no-free-frontier (conjecture).
- conj-halo-collapse elevation run 1: ABORTED [BALLOON] 49>40 (structural: inline re-derivation of
  mass-split + residual-distance bookkeeping). Follow-ups filed: aism-q7e (factor+re-seed+re-run,
  quota-gated 16:00), aism-5yk (no-free-frontier walls-check wave, opus, can run pre-16:00).
- Session totals: 2 af-validated banked results (lem-classical-equiv, obs-height-collapse), 26-node
  registry, 2 L3 bundles, 5 wave artifacts, sync-beads mirror live, 2 oracles registered, tooling
  feedback filed (af dry-run bug already fixed upstream in 0.1.4). Codex quota ~exhausted; wound down
  per user instruction.

## 2026-07-02 (session 3, Claude orchestrator + codex workers) — B4 walls-check; factoring; 3rd rigorous result

- **Arm B wave 4 (walls-check on `conj-no-free-frontier`)**: CONDITIONAL — one-sided ledger DODGED
  (positional statement, upper-bound target), anti-splitting wall HIT (class-count reduction to c10) +
  FAIL-1 soundness worry (uniform κ=τ/4 pointwise margin). DO-NOT-ELEVATE codified (shard + FINDINGS);
  fr arm B pull logged died, frontier reduced to bridge-only. Artifact
  `docs/waves/2026-07-02-B4-walls-check.md`.
- **aism-q7e factoring**: `conj-halo-collapse` factored into `lem-mass-split`, `lem-residual-lower`,
  `lem-residual-upper` (single-statement contracts; residual pair frame-free ℓ¹ convex geometry);
  fresh codex reviewer PASS pre-commit; seeded; orchestrated.
- **`lem-mass-split` af-VALIDATED (9 nodes, clean) → 3rd rigorous result**; fr verify PASS, banked.
  Residual pair stalled on the 16:00 codex quota mid-verify (lower: challenges all resolved, 12/30
  validated; upper: 17/37, 4 open scoping challenges); resume plan in HANDOFF.
- **aism-4el**: inherited 67k (EX) record re-homed as L3 bundle `runs/2026-07-02-ex-enumeration-rehome`
  (invariant independently recomputed PASS).
- **aism-136**: dual-localization contract confirmed trivially-true-as-stated (codex, read-only);
  candidate corrected contracts in bd notes; flagged `bd human` for the user.
- Process: overreach-guard near-miss (registry edit during live runs) neutralized by fast commit;
  lesson banked to bd memory. Node-cap miscalibration (15 < natural 24–38 tree size) cost one abort
  cycle on each residual lemma.

## 2026-07-02 (session 3 close) — the finisher bridge is RIGOROUS: six banked results

- **`conj-halo-collapse` af-VALIDATED (run 2, 20-node tree, 20/20 clean)** — the halo-robust
  height-collapse bridge `H(1−σ̃_g) ≤ (σ̃−σ̃_g)τ/4 + ν(2+4δ)` is now rigorous, importing the three
  factored deps as af externals. Run 1 (pre-factoring) ballooned 49>40; the factoring discipline
  (single-minimal contracts + registry sub-lemmas) cured it. fr verify PASS; aism-q7e closed.
- **`lem-residual-lower` (32 live nodes) and `lem-residual-upper` (49) af-VALIDATED + banked** after
  verify resumes across the quota stall (all challenges were af dependency-scoping hygiene, resolved
  by bridge nodes; zero mathematical objections).
- **Lab-book started:** 7 report shards (overview + one per rigorous result + full status ledger),
  all 29 registry results anchored, provenance 0/0, codex-reviewed for overclaim (PASS).
  Bridge banking propagated to the report in lockstep (hash + status rows).
- **Frontier at close:** cap (OPEN) ⇒ [bridge RIGOROUS] ⇒ H=O(√δ) ⇒ Kernel ⇒ op-classical. THE open
  input = halo-robust cap `σ̃_g ≤ 1−c`; mechanism `conj-no-free-frontier` wall-blocked (B4). Next:
  arm A scoping wave (aism-vip) or the B4 FAIL-1 exact-instance decider (arm F).
- Session totals: 4 new T0 results banked (mass-split, residual pair, bridge), 1 wave harvested
  (B4), 1 L3 bundle re-homed (67k record), aism-136 flagged for user decision, 2 process memories
  banked. Quota management: one stall bridged cleanly by stop/resume.

## 2026-07-02/03 (session 4 close) — arm A campaign: 7 codex waves, 7th rigorous result, plateau-2

- **Arm A opened and driven through 7 serial codex waves (A1–A7, all in `docs/waves/`):**
  - A1 scoping: existential (EX) suffices downstream (w42 audit: no quantifier slip); walls-check
    verdict — aggregate proofs dodge the recorded B-walls, per-class proofs re-import class-count;
    "C₀=1 empirically" exposed as RANK-3-ONLY (FINDINGS entry).
  - A2 (L3 bundle `ex-no-center-highrank`): path family certified `Φ/δ = 2−2/(k−2)` through k=30 —
    PLATEAU toward 2, not growth. Orchestrator recomputed k=10 (7/4) independently.
  - A3 (L3 bundle `ex-multiblock-coupling`): 25 certified rows over 5 decoupled coupling designs —
    all < 2; the θ-class decouples to one signed pivot per anchor (average-distance mechanism).
    Orchestrator recomputed star-f9 (23/16).
  - A4 proof skeleton: argmin interface clean; beta-LP-only route KILLED (exact two-atom witness);
    GAP A/GAP B isolated; `Φ ≤ 2δ` passes the full exact bench.
  - A5 averaged selection: naive chart averaging KILLED in all three natural measures (sigma-cap-B
    certificate: best chart perfect, θ-average ~10×); max-vs-sum crux articulated.
  - A6 (L3 bundle `undercap-killers`): the δ=1/2 mechanism-killers do NOT port under the cap;
    NEW certified witness kills unnormalized `Σ_s Φ_s` (repeated anchors: sum=11g/8·δ, max=11/8·δ);
    `V_s ≤ Φ_s/2` proved inline. Orchestrator recomputed the 512-chart repeated-star row.
  - A7 coupled anchors: coupling REDUCES the ratio (best new certified 3/2, anchor-mixing to rank
    121); **cheap-adversary program CLOSED — plateau-2 unbroken across 7 design families.**
- **`lem-factorization` af-VALIDATED (run 1 clean, 5 rounds, 11 live nodes, 12/12 taint) → 7th
  rigorous result, banked (fr verify PASS, new oracle registered).** Contract narrowed to the single
  self-contained inequality first (single-minimal discipline; tightness (2,6) NOT elevated). The
  (EX) composition link `S*_s ≤ 2Φ_s + 6δ ⇒ C_sf = 2C₀+6` is now RIGOROUS.
- **Lab-book grown to 9 shards:** AISM-06 (conj-halo-collapse) + AISM-07 (lem-factorization) added
  with full lockstep (catalog/README/PROVENANCE/counts); provenance 0/0 throughout.
- FINDINGS: three new dated entries (rank-3-only C₀; sum-interface dead route; session-4 roll-up:
  plateau-2 picture + killed mechanisms). aism-6ec: accept-and-defer recommendation recorded.
- Frontier at close: TWO chains to op-classical, each one open input — A-side: the max-based argmin
  charge (GAP B / plateau-2 lemma); B-side: the halo-robust cap (unchanged). aism-136 still awaits
  the user decision.
- Session totals: 7 codex waves harvested + 1 af orchestration validated; 3 new L3 bundles (all
  headlines orchestrator-recomputed); 1 T0 result banked; 8 bd issues created/closed; ~10 commits.

## 2026-07-03 (session 4 continuation) — the reduction cascade: 5 more rigorous results (8th-12th)

- **Waves A8-A12 + D1-D2 (7 more codex waves)** drove the (EX) argmin charge through a full
  reduction cascade: GAP B split into payment + legal-collateral horns (A8); exact accounting +
  disjunction, circular routes killed (A9); WOP isolated, all-mass fan payment PROVED inline (A10);
  D-restricted fan inequality PROVED with SHARP constant 2+sqrt(2), C=2 exactly refuted (A11); the
  lift made exact — payment horn reduced to (TT) conj-degenerate-transport (A12); H-M Thm 1.12
  applied — (TT) is a B-row inequality, quotient harmonicity, delta=0 refuter excluded (D1); exact
  source split + class-negative budget proved, (SI)+(BN) isolated with a 4-piece factoring (D2).
- **Five af-validated results banked (8th-12th):** lem-zerosum-triangle (10 nodes),
  lem-weighted-min (8), lem-fan-payment (15, after a 39/47 double balloon cured by factoring),
  lem-negpart-subadditive (16), lem-fan-payment-restricted (27, run 1 clean — the sharp 2+sqrt(2)
  theorem). The fan-payment family is genuinely NEW mathematics produced by this session's waves.
- **Two new registry conjectures codified:** conj-degenerate-payment (A8 payment horn),
  conj-degenerate-transport (A12 (TT), owner D). Registry at 36 results.
- **Arm D opened** (2 pulls, both progress): the H-M structure side reached the same object as the
  argmin side; the old all-row tax wall is dodged in the delta=0/aggregate senses.
- Process: one network outage bridged cleanly (weighted-min verify resume); one node-cap
  miscalibration (30 vs standard 40) cost an abort cycle; pre-factoring adopted for linear-chain
  proofs (DRF validated run-1 clean with pre-factored dep).
- HANDOFF checkpoint-rewritten mid-session (frontier materially changed). Lab-book sections for
  results 8-12 pending (ledger rows exist).

## 2026-07-03 (session 4 close, part 2) — the D-line descent: ledger exact, horns coupled

- **Waves D3-D6 (4 more codex waves):** (SI) REFUTED exactly (centered-fan argmin certificate;
  own-negativity is the missing source) => (RSI) isolated, unbroken, C_src=1 sharp; (BN) first
  exact beta-negative tests pass (3/32); D4 import decomposition PROVED-inline + B-block
  contraction KILLED exactly (rho_B=21/20); D5 exact beta-stationarity financing ledger
  PROVED-inline (D4 refuter financed to the penny) + the WIE->RSI composition shown TAUTOLOGICAL
  (legal baseline L_mu leaks) => horns COUPLED, (FIN) isolated; D6 legal leak REALIZED (exact
  argmin certificates L_mu/delta ~ 1, F_L>0) — the argmin-mechanism impossibility lemma is FALSE.
- **Two FINDINGS dead-route entries** ((SI) death; legal-leak certificates + horn coupling).
- **Session-4 grand totals:** 19 codex waves (A1-A12, D1-D6, + the af orchestrations), 5 af
  orchestration arcs, 12 rigorous results (5 new + re-established), 2 registry conjectures
  codified, 3 L3 bundles, ~35 commits, every wave harvested + fr-logged + committed.
- **End-state:** both GAP-B horns need genuinely new mechanisms and are provably coupled ((FIN));
  the provable wave-artifact lemmas (ledger, splits, class budget, lambda-correction,
  perturbed-DRF) are the elevation backlog. Codex quota exhausted at close (probe timeout).

## 2026-07-03 (session 5) — arm G: the flow-conservation engine survives contact; (SC)→(PRT) isolated

- **Eight codex waves (G1–G8), every one harvested + fr-logged + committed** (single-arm EXPLOIT run;
  arm yielded to EXPLORE R after two consecutive OPEN waves per the breaker).
- **G1/G2 — fan horn stands:** fan-matched negative-coordinate weights `w=a_t(j)⁻/μ_j` telescope every
  certified legal leak (incl. exact F_L) with residual constant 0; unoriented weightings FAIL (uniform
  leaves +9/14·δ on D6-A) — signed orientation FORCED. Adversarial stress survived (worst 814/2149).
- **G3/G4 — orphan rows are real, both exclusions die:** exact rank-3 certificates (λ-positive AND
  active E_s>0) with empty fan family; leaks exactly class-financed (257/1680; ratio 1 with payment);
  one-B-row orphan ratio bounded, sup=1 (T1), trend → 2 with A9 payment ⇒ C_orph ≥ 2.
- **G5 — the amplifier:** exact two-orphan cancellation family starves the class/signed budget for
  EVERY finite constant (OD/budget = 1/(2h)−2 → ∞) while Φ_s/δ → 1 (NOT an (EX) refuter). The
  (SI)→(RSI) own-negativity pattern repeats: repair = Σβν budget (floor 4 forced).
- **G6 — (RH) stands, silent subtlety found:** unified budget survives everything (G5 = exactly sup 4);
  pointwise domination ν_j ≥ a_r(j)⁻ FALSE (self-support carries chart negativity at vanishing ambient
  cost) — but the argmin catches the exact counterexample family via a pivot-REMOVING move. E_s ≤ μ_s
  closed (T1) on rank-3 active orphans.
- **G7/G8 — toolkit banked, target OPEN twice:** pivot-removing disjunction M ≤ max(Ψ,Γ) with volume
  factor |a_s(j)| (T1, the first minimality-using tool); B-block transfer system + β-weighted
  financed-excess identity (T1, reproduces D5's financing on the D4 refuter to the penny). (SC) reduced
  to ONE sub-gap: (PRT), the high-self pivot-removing blocker/import theorem.
- **Five FINDINGS death certificates** (both orphan exclusions, C_legal=0, class/signed-only orphan
  budget, pointwise silent domination) + the ambient-vs-chart non-conflation caveat.
- **No promotions:** still 12 rigorous results; all session-5 output honestly T0/T1/T2 wave material.
- **Queued:** (PRT) fresh-angle attack (aism-qkv); registry codification of conj-rh/conj-sc/
  obs-orphan-amplifier/lem-pivot-removing-move blocked on a user def-vocabulary decision (aism-l70);
  elevation backlog grew (G5 ledger, G6 identity, G7 formulas).
- Process: codex quota fresh all session (8 waves, no outage); wave prompts/answers/transcripts in the
  session scratchpad; commits signed Claude Fable 5 (orchestrator model this session).
