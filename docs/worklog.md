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

## 2026-07-04 (session 6) — G9 decides V/P; dual-localization retired; arm-G codified; 13th rigorous result

- **Wave G9 (arm G, codex): per-branch (PRT) realizability.** (V) volume-inadmissible branch REALIZED
  (exact certified argmin, score-degenerate M=0, charge ratio 624/4427); (P) Psi-blocked branch REALIZED
  (genuine blocker 91/300 >= M=1/12, ratio 240/451); amplification probes bounded on both families;
  (G) Gamma/collateral branch neither realized nor proved empty ⇒ (PRT) OPEN, narrowed to the (G)
  branch. Both certificates orchestrator-recomputed in exact Fractions (complete theta-half enumeration,
  argmin, branch conditions, ratios) — reproduced exactly. Artifact `docs/waves/2026-07-04-G9-*`.
- **USER DECISIONS (2): (a)** arm-G codification uses FULLY-INLINE contracts (no def shards while the
  vocabulary moves); **(b)** `lem-dual-localization` superseded, not rewritten in place.
- **Supersession:** `conj-skinny-shadow-cap` registered (skinny two-shadow cap at the sqrt(delta) scale);
  `lem-dual-localization` retired to `obstruction` (transcribed contract = distance tautology, confirmed
  by independent codex verifier; upstream DELIVERABLE2:86 mislabelled it). First `docs/LEARNINGS.md`
  entry; CLAUDE/AGENTS callout, FINDINGS, RESEARCH_NOTES, report ledger updated. Independent codex
  reviewer APPROVE (A–E PASS).
- **Codification (aism-l70):** `conj-rh` (floor C_RH>=4 in body), `conj-sc` (body records (PRT) + G9
  narrowing), `obs-orphan-amplifier` (proved-mod-audit; contract identities orchestrator-recomputed at
  4 parameter values), `lem-pivot-removing-move`. Codex drafted → independent codex review
  REQUEST-CHANGES (4 transcription fixes: Schur volume factor |det C| wording, lambda-positive
  strict-legal cover, silent-row quantifier, Phi/delta→1) → fixes applied verbatim → fresh confirm-pass
  CONFIRM. deps left EMPTY per conjecture precedent. (Also caught+fixed: orchestrator extraction regex
  truncated two shard bodies at inner code fences.)
- **13th rigorous result:** `lem-pivot-removing-move` af-VALIDATED (run 1, 9-node tree, 3 rounds, ZERO
  challenges, taint 9/9). Export written, oracle registered, `fr verify` PASS, banked (arm R,
  EXPLOIT G). The (G)-branch attack now stands on a rigorous disjunction.
- **Lab-book:** shards AISM-08..12 for rigorous results 8–12 (contracts verbatim); status ledger
  renumbered to `13_discussion.tex`; caught a false-green: `check-provenance.py` hard-coded the ledger
  filename (red/green probed the fix). AISM-14 (pivot-removing section) filed as follow-up.
- **Queued:** arm G wave 10 — the (G) collateral-branch decider (construct or prove empty; new bd issue);
  AISM-14 section shard; elevation backlog (D5 ledger, G5 ledger, G6 identity) still needs codification.
- Process: codex workers for wave/draft/review/confirm (4 dispatches + 8-worker orchestration); three
  independent codex reviewers used (reviewer ≠ author throughout); commits signed per repo convention.

## 2026-07-04 (session 6 continuation) — AISM-14; wave G10: (G) cap-blocked locally, (CI) banked

- **AISM-14 landed:** section shard for `lem-pivot-removing-move`; the report reproduces all THIRTEEN
  rigorous results; status ledger shrunk accordingly (aism-t5c closed).
- **Wave G10 (arm G, codex): the collateral-branch decider.** (G) OPEN but narrowed BOTH ways:
  (i) the Γ-only sign pattern (`Psi_j=0 < M=2/25`, `Gamma_j=11/40 > M`) is EXACTLY realizable at a fully
  argmin-certified 5×5 instance — but at `delta=49/60` (cap violated; tooling only); no capped instance
  in the two/three-B-row sweeps (evidence, not emptiness). (ii) NEW T1 tool banked: the
  **collateral-import inequality (CI)** `Phi_r(V_j) <= Phi_r(U) + I_{r,j}` with explicit positive-part
  import, derived FROM the validated `lem-pivot-removing-move` transform, SHARP (zero slack) on the
  witness. A clean (G) branch forces `M - Phi_r(U) <= I_{r,j}` ⇒ (PRT)'s collateral question is now:
  charge `I_{r,j}` at the cap, or prove capped emptiness. Orchestrator recomputation reproduced the
  witness, all branch/budget values, ratio `1600/4897`, and (CI) sharpness exactly.
- **Queued:** codify+elevate `lem-collateral-import` (aism-bof, priority — puts wave 11 on rigorous
  ground); arm G wave 11 = the capped charge/emptiness decider (aism-izb). fr: G progress T1, EXPLORE R.

## 2026-07-04 (session 6 continuation, part 2) — 14th rigorous result; waves G11: the cross-pivot residual

- **14th rigorous result:** `lem-collateral-import` — the (CI) bound `Phi_r(V_j) <= Phi_r(U) + I_{r,j}`
  — codified (independent codex review APPROVE, no corrections) and af-VALIDATED same-day (run 1,
  32-node tree, 6 rounds, zero open challenges, taint 32/32; imports the validated
  pivot-removing move). Oracle registered, `fr verify` pass, banked (arm R, EXPLOIT G). AISM-15
  section shard filed.
- **Wave G11 (arm G, codex): the capped charge decider.** (CHARGE) PARTIAL — T1 tools banked:
  the exact B-L cross-pivot cancellation `sum_i beta_r(i)a_s(i)=0` (so `A_{r,s}=B_{r,s}+C_{r,s}-D_{r,s}`)
  and the universal import reduction (4). The dominant import term reduces to `B_{r,s}+C_{r,s}` —
  cross-pivot masses NOT in the pivot-s unified budget: **the (PRT) residual is now the cross-pivot
  charge question** (pay it, reshape the budget with a transverse-pivot term à la the G5→G6 SIGMA
  repair, or realize a capped (G)). No capped clean (G) in 360k exact sweeps; certified capped near
  miss only (`delta=1/4`, `Psi=69/250` AND `Gamma=21/80` both `> M=1/10`). All exhibits + the identity
  orchestrator-recomputed exactly.
- **Queued:** codify+elevate the two G11 tools (separate minimal shards); arm G wave 12 = the
  cross-pivot charge / budget-reshape / seeded-construction decider.

## 2026-07-04 (session 6 continuation, part 3) — audit, kill test, the B-question decided

- **Sober audit (user-requested):** assessed ~half the day's output as self-documentation/ritual
  elevation; flagged the budget-epicycle risk and the 5-pull single-wall pattern; policy set: no
  ritual elevations, decision-checks before narrowing waves. Logged in fr.
- **15th rigorous result (weight discounted per audit):** `lem-cross-pivot-cancellation` af-VALIDATED
  (23-node run-1 tree, clean) — near-definitional B-L identity; elevated as in-flight completion only.
  `lem-import-reduction` deliberately NOT elevated pre-decision.
- **Kill test banked** (`runs/2026-07-04-cross-pivot-kill-test/`, L3, known-value invariants):
  `B_{r,s}=0` on all six prior certified instances; `C_{r,s} <= 2δ` trivially (chart-row negativity ×
  Cramer box); worst `(B+C)/budget ≈ 1.82`. Reframed wave 12 to the falsifiable B-question.
- **Wave G12 (arm G, codex): DECIDED both sub-questions.** (i) `B=0` at capped argmins is FALSE —
  exact certified argmin with `B=2/57` at `δ=1/4` (complete enumeration; orchestrator-recomputed) —
  but sub-δ; non-argmin `B/δ` unbounded (50 at ε=1/100) and minimality pivots it away. (ii) The
  intended assembly is rate-tolerant (no step needs o(δ)); only a contract-level naked-δ bookkeeping
  question remains. **Pre-factored 7-step collateral skeleton banked**: 3 links VALIDATED
  (disjunction, (CI), cancellation), 2 elementary (import reduction mod-audit; `C<=2δ` box), ONE open
  link = the branch-sensitive **B-lemma** (`B <= K·δ` at clean high-self Γ-branches).
- **Queued:** wave 13 = the B-lemma (prove via minimality incl. the c<0 move — the named tool gap —
  or amplify at argmins); USER decision filed on the `+C_δ·δ` contract amendment (mechanism-derived,
  arrives with its financing proof — distinct from the audit's epicycle pattern).

## 2026-07-04 (session 7) — operational audit + literature sweep (no proof waves; knowledge banking)

- **User-mandated sober audit (4 read-only sonnet auditors):** DAG census (44 results, not 46; 6 of 15
  validated results substantive; ONE validated result on the wired critical path), fr process audit
  (83% single-mechanism concentration A→D→G; breaker structurally defeated by `progress` self-tagging;
  budget-patch pattern ×3 confirmed; C/E never dispatched), full gap map (B-lemma ≈ 1–5% of remaining
  work; dominant unpriced risks = rank-3-only scoping + unaudited inherited downstream chain + unproven
  ex⟺kernel equivalence), evidence audit (gate green; B-lemma data all at δ∈{0.233,0.2498,1/4}; kernel
  numerics n≤9; (BN) unregistered; zero cited leaves). Banked: `docs/audits/2026-07-04-operational-audit.md`.
- **User-mandated literature sweep (7 read-only sonnet web scouts):** NO lane found op-classical stated
  or solved anywhere. Tier-1: Kitaev arXiv:2405.02434 poses the noncommutative lift VERBATIM AS OPEN
  (3 scouts converged, full-text verified); Salzmann–Bergh–Datta arXiv:2405.01532 Thm 5.2 = √ε
  dimension-free + sharp for approximate fixed distributions (reset-trick Lemma 5.5 transferable);
  Luo–Pang/Mangasarian–Shiau degenerate-complementarity mechanism explains the ½ exponent and backs the
  never-dispatched arm E. Negative space banked to FINDINGS (TVKW, Mehta, incoherence mismatch, B–S
  web-stability unsubstantiated). Banked: `docs/lit-review/2026-07-04-literature-sweep.md`;
  RESEARCH_NOTES queue extended (12 sources); arm-D's B–S-stability line corrected.
- **Adopted sequencing (audit §7):** deciders BEFORE wave 13 — rank-4/5 skeleton stress test; small-δ
  certified argmin sweep; ex⟺kernel adversarial audit + HLC/finisher wiring; SBD reset-trick probe;
  ex-hume vs SBD sharpness cross-check; arm E decision-check wave. `aism-z98` recommendation: DEFER.
- Process: all dispatches read-only subagents; no registry/definitions edits; fr `orient` logged per
  turn + `fr discover` for the tier-1 finds; bd issues filed for every follow-up.

## 2026-07-04 (session 7, continued) — de-risk decider #1 banked: the skeleton transfers to rank 4/5

- **`runs/2026-07-04-rank4-transfer-decider/` (L3, codex-built, orchestrator-recomputed):** no rank-4/5
  violation of the pivot-removing disjunction (48 exact θ-half moves) or of the natural `c>0` rank-4
  (CI) transcription (144 pairs, worst slack exactly 0 — sharp); `Φ/δ` plateau intact (5/4 at rank 4,
  4/3 at rank 5, the known slow climb toward 2); first nonzero-B instances beyond rank 3
  (cycle-coupling family), all sub-δ (max `B/δ = 27031/82920`). Convention caution recorded: over ALL
  ordered pairs the no-center rank-4 instance realizes `B=δ` exactly at a NON-maximal pivot — do not
  conflate with the G12 maximal-pivot convention. Verdict: the "machinery visibly breaks at rank 4"
  kill scenario is OFF; rank generalization stays open as proof work. fr: F progress T0.
- Decider #2 (small-δ certified argmin sweep) still in flight (codex background worker).

## 2026-07-04 (session 7, continued) — de-risk decider #2 banked: B/delta ≈ 0.771 at small delta; wave 13 GO

- **`runs/2026-07-04-small-delta-b-sweep/` (L3, codex-built, orchestrator-recomputed):** the evidence-audit
  blind spot is filled and the picture CHANGES — `B/δ` does not vanish at small δ, it rises: max certified
  `B/δ = 8400000/10897843 ≈ 0.771` at `δ ≈ 0.055` (compensated-insert family, clean high-self non-fan
  Γ-branch, UNIQUE certified θ-½ argmin; orchestrator independently re-derived δ, the 8-chart θ-half
  census, the argmin, and `B=42/985` via its own Gaussian-elimination/Gram code). Ten certified points in
  `[0.69, 0.771]` across two families. Every amplification attempt was obstructed by argmin switching
  (non-argmin `B/δ` up to 50 never survives certification — reproducing G12), Ψ-flips, or high-self loss —
  minimality binds. Consequences: "all capped-argmin data is sub-δ" was a δ≈cap artifact; the B-lemma
  needs `K ≥ 0.771` (δ-scale, not ε); `aism-z98` gains direct evidence that a full δ-scale B term must be
  absorbed. **Wave 13 GO** (both deciders passed); frontier updated in fr. fr: G progress T0.

## 2026-07-04 (session 7, continued) — wave 13 prover harvested: c<0 tool banked; B-lemma reduced to NSC

- **Wave G13 prover (codex): T1 + T2 + a structural reframe.** (i) T1: the c<0 pivot-removing transform
  (sign-agnostic, verified) + the c<0 pointwise/summed import bound `Phi_r(V_j) <= Phi_r(U) + I^-_{r,j}`
  with explicit `R^-` — the algebra genuinely differs from validated (CI) (the `1/|c|` term lands on A,
  the B-coefficient carries a subtractive −1); exact-verified on the 0.771 maximizer, two-carrier-B, and
  G12 (slack 0 somewhere ⇒ sharp). (ii) T2: the B-lemma proved CONDITIONAL on one named minimal subclaim
  **NSC(K0)** (`B_{r,s} <= K0·Σ_carriers β_r^+·ν_i` ⇒ `K = 5K0/4` under the cap). (iii) STRUCTURAL
  HEADLINE: in all three certified stress instances the ENTIRE B-mass sits on volume-INADMISSIBLE
  carriers — pivot-removing minimality is blind to them; Ψ-blocks escape the transverse import bound
  (pivot β-row changes); Γ-blocks give only forward forcing. NSC empirics: B/weighted-ν ∈
  {≈1.14, 2.25, ≈2.79} — testable law, K0 ≈ 3 would do. Artifact (verbatim):
  `docs/waves/2026-07-04-G13-b-lemma-conditional.md`; orchestrator re-ran the verification (exit 0).
  fr: G progress T1; frontier now = NSC(K0). Independent codex review dispatched pre-codification;
  amplifier branch still in flight.

## 2026-07-04 (session 7, continued) — wave 13 complete: review APPROVE; amplifier law 0.77764; frontier = NSC

- **Independent codex review of the prover draft: APPROVE** (adversarial exact grid over every case
  split, 0 failures; one sharpening: the I^- bound is an EQUALITY with the standard A/B definitions).
  The c<0 import tool and the conditional NSC(K0) structure are reviewer-cleared (reviewer ≠ author).
  Artifact: waves-scratch review dir (session scratchpad); verdict recorded in the wave doc header.
- **Wave G13 amplifier harvested** (`docs/waves/2026-07-04-G13-b-amplifier.md` +
  `runs/2026-07-04-b-amplifier-hunt/`, L3): new record `B/δ ≈ 0.77764` with an ALGEBRAIC family-limit
  law (irrational row-loss balance, certified rationals approach from both sides); crossing 1: NO;
  cloning does not amplify (clone-invariance holds); alternative shapes lose the clean Γ-branch. At the
  record point B exceeds the literal (CI)-financed total and the G12 pivot-s budget ×4.24 —
  **orchestrator correction recorded**: the wave prompt's "kill" criterion (iii) was mis-specified (the
  skeleton bounds I BY B); the true content is that B needs its OWN δ-scale financing (NSC / aism-z98
  shape). Orchestrator independently recomputed the record incl. the (0,1,3)/(0,2,4) argmin tie.
- **Frontier after wave 13: NSC(K0)** — a self-support/row-negativity principle at the argmin (not a
  chart-move comparison; all certified B-mass is volume-inadmissible), empirical K0 ≈ 2.8. Wave 14 =
  prove NSC via idempotence/self-support, or refute via ν-starved carrier families. fr: G progress T0.

## 2026-07-04 (session 7, close+) — top-down full proof sketch banked

- **User-requested strategist deliverable banked:** `docs/plans/2026-07-04-top-down-proof-sketch.md`
  — the complete Lamport-style top-down architecture of op-classical (10-step main chain + 7-step
  Lemma K block), with per-step mechanism, connections, honest status tags, the single point where
  sqrt(delta) enters (the exposedness window, main <1>7 — matching sharpness), designated fallbacks
  (arm E error-bound route, SBD reset-trick, incremental bootstrap), and the compressed ledger:
  exactly FOUR open mechanisms (NSC; orphan budget; fan-lift; master decomposition + rank transfer)
  — everything else is assembly or transcription. HANDOFF START-HERE updated to point at it. Wave
  design and the DAG-wiring issue are to be built against this document.

## 2026-07-05 (session 8) — BFS scoping: sketch v2; two conjectures killed by certificate; Kernel-rooted redraw

- **User redirections (binding):** breadth-first top-down scoping ("af per node, refine the
  hardest leaf after SOTA recon"); mid-session: **no progress theatre** — the deliverable is a
  fully scoped workable proof, progress = unscoped surface shrinking (memory + bd remember).
- **Codified + seeded:** wave-13 tools (`lem-negative-pivot-import` proved-mod-audit; `conj-nsc`
  broad-form with loud scope note) at 43ce90b; 10 sketch-node af workspaces seeded (8784594);
  `lem-import-reduction` af-VALIDATED = 16th rigorous (81e247e; bookkeeping-grade).
- **4-lane sonnet recon banked** (3f69029, `docs/recon/2026-07-05-open-mechanism-recon.md`):
  difficulty ranking + the D/G COUPLING hypothesis + unrecorded K⟨1⟩6 composition risks.
- **Idempotent Atlas published** (user-requested interactive proof explainer; opus build from
  orchestrator spec; 3 reading lenses, 4 live instruments incl. the certified G12 specimen).
- **Decision-check wave DC1-DC4** (533be01): DC1 fusion SUPPORTED (D-line demands financed by the
  G-line budget, worst ratio 1); **DC2 broad `conj-nsc` REFUTED** (zero-denominator certificate,
  orchestrator-independently recomputed; carrier entrywise nonnegative at a certified argmin);
  DC3 K⟨1⟩6 additive master formula RED (FanRes realized>0 + absent; silent rows tribeless;
  SC-in-RH nesting double-charge); DC4 `conj-ex ⟺ conj-kernel` UNPROVED both directions (three
  named mismatches; redraw recommended).
- **User decisions:** adopt the DC4 redraw (PRD + shards edited: Kernel = theorem-facing input;
  (EX) = attack route; "equivalently" cut) + Γ-emptiness-first successor. Sketch v2 banked
  (c1b4daf, updated 7ed4d0e/e6ec340/fb84a37) — the phase deliverable, with the priced OPEN
  LEDGER + unscoped-surface list.
- **W15: `conj-gamma-emptiness` REFUTED** (b490ea4) — the FIRST certified capped clean Γ-block
  (δ≈0.055, Ψ=1/200 < M ≤ Γ=7/250, refuting row high-self); G11's 0/352 was coverage. T1
  residual: `M − Φ_r ≤ 17B + 20δ` ⇒ **`conj-b-restricted`** codified as THE K3 link (hypothesis
  class certified NONEMPTY, K ≥ 0.7708 forced, K_G = 17K+20 explicit).
- **W16/W16b:** clean-block sup B/δ = 0.77764 (the wave-13 record instance ITSELF carries a
  clean block — wall binds with/without); direct-FE identity + conditional theorem; adversarial
  floor collapsed 157/500 → 23/1000 (genuine point) — direct-FE route FRAGILE; residual = α→1
  continuation. (7ed4d0e, fb84a37)
- **W17/W17b:** ⟨3⟩3 dictionary priced — D1 low-halo reduction proved short (only σ_g > 1/2
  matters; constant cap ⇒ Kernel with B = 29/8), D5 weight-transport = the wall, possibly
  Kernel-sized; door-ratio census REGIME-EMPTY-SO-FAR (514 instances, max σ_g = 1/25) ⇒ ≥12×
  empirical slack on the **Route-A constant cap** — the wall re-read is session 9's top item.
  (7ed4d0e, e6ec340)
- **Discipline notes:** two freshly codified conjectures killed by bounded prove-or-refute waves
  within hours each — falsifiable contracts + certified-grippable hypothesis classes work; every
  status-changing certificate independently recomputed from matrices alone; W16b banked with an
  explicit verification-scope limitation (fresh-point JSON lacked matrices).
