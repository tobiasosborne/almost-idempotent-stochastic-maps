<!--
ROLE: living orchestration log for the classical-portfolio sidequest (Agent A, exploration lane).
Branch: agent-a/classical-portfolio. Canonical promotions go through Recipe A→B on main ONLY.
UPDATE POLICY: rewritten sections as state changes; delegation ledger is append-only.
-->

# Classical portfolio — orchestration

**Goal.** A fully rigorous, dimension-free proof of `op-classical` (every row-stochastic Q with
‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀ is within C√η of a stochastic idempotent, C universal) **or** an explicit
counterexample. Equivalent exact form (`lem-classical-equiv`, validated): P signed affine retraction
(P1=1, P²=P, neg(p_i) ≤ δ) ⇒ stochastic idempotent within C√δ.

**Done criteria (user-approved 2026-06-10).**
- PROOF-DONE: complete prose proof, every lemma verified by **two independent model families**
  (Claude-family + gpt-5.5/codex) with ≥1 adversarial pass; every external fact byte-grounded in
  `refs/`. af-validation = follow-on phase (beads filed).
- COUNTEREXAMPLE-DONE: explicit exact-rational family + verification script (P1=1, P²=P, neg ≤ δ,
  dist to EVERY stochastic idempotent ≥ K_n√δ, K_n → ∞), reproduced by two model families.
- HONEST-STALL: all lanes blocked on named precise obstructions → obstruction map to user.

**Mode.** Serial delegation (one subagent at a time, economy + continuous learning). I (Agent A,
orchestrator) write briefs, review every hand-back, log learnings, raise beads, switch lanes.

**Switching rules.** Switch lane when (a) a kill criterion fires; (b) a blocker survives two
independent attacks by different model families; (c) another lane's finding opens a cheaper door.
Every switch logged here + worklog.

**Tooling on this machine.** mosek, gurobi (`gurobi_cl`; gurobipy 13.0.1), numpy/scipy/HiGHS,
`codex exec` (gpt-5.5, xhigh default; see docs/codex-delegation.md). **2026-06-12: TIB VPN and
wolframscript UNAVAILABLE** — refs acquisition paused, symbolic work via sympy/exact rationals.
Concurrency cap (user, 2026-06-12): ≤ 2–3 codex in parallel; opus serial; sonnet free.

**Interruption-resilience protocol (user directive 2026-06-12: "brace for frequent network
interruptions; plan future work accordingly").** Codex/opus/sonnet delegation ALL need network;
local python/HiGHS/gurobi (outside the codex sandbox) and git commits do NOT. Therefore:
- **Snapshot volatile state into the repo EAGERLY**: copy /tmp workdir artifacts to
  `experiments/out/<wave>/` as soon as a worker passes a meaningful stage, not only at landing;
  re-copy at landing. Briefs are archived to `notes/briefs/` AT LAUNCH (already standing).
- **Commit early, push often; tolerate push failure**: commit locally after every harvest; if
  `git push` fails (network), retry later — NEVER let unpushed work block local progress; re-push
  at every subsequent harvest.
- **Briefs small and bounded**: one named question per worker, expected runtime ≤ ~30 min, so an
  interruption loses at most one bounded attempt. Workers already write progress.md + artifacts
  eagerly (observability protocol) — an interrupted run is harvestable from its workdir.
- **Resume path**: a died codex run → check `events.jsonl` tail + workdir artifacts; prefer
  `codex exec resume --last` (thread intact) else relaunch from the archived brief amended with
  the partial findings.
- **Local-first fallback**: when the network is down, the orchestrator continues productively
  WITHOUT delegation: run the numerics/LP experiments locally (codex-written scripts run fine
  outside the sandbox, incl. gurobi), do derivation work directly, write docs/briefs for the next
  wave, and queue commits. Delegation resumes when the network does.

**Observability protocol (user directive 2026-06-10): verbosity + eager flush in ALL activities.**
- Every long-running delegated process streams a live trace to a file: codex → `--json` events
  (never `--ephemeral`); python → `python3 -u` (+ per-iteration prints); shell pipelines →
  `stdbuf -oL -eL`; solvers → native log files (gurobi LogFile, mosek log).
- Heartbeat rule: any run expected >2 min must emit progress at least every ~60s; silence beyond
  ~3× the expected cadence ⇒ byte-flow check (`/proc/<pid>/io` rchar delta over 15s) ⇒ kill+resume.
  Watchdog timeouts on all launches.
- Process-hygiene: never `pkill -f`/`pgrep -f` with a pattern contained in your own command line
  (self-match kills your own shell); use bracket-grep `[c]odex` or kill by recorded PID.

**Delegation matrix (initial; evolves via LLM-LEARNINGS.md).**
| Step type | Worker |
|---|---|
| Ideation / reformulation | gpt-5.5 codex (read-only) |
| Lemma proving / derivation | Opus 4.8 high |
| Cross-check of load-bearing derivation | codex xhigh (second family) |
| Numerics write+run | codex workspace-write (gurobi/mosek) or sonnet |
| Lit scouting / refs byte-pinning | sonnet |
| Adversarial verify (suspect, load-bearing) | Opus xhigh; fable only if survives opus and still suspect |

---

## Lanes

### Lane D — plateau analysis / global potential (REFORMULATED 2026-06-10)
Original form (opus strategist): global transport-duality contradiction (m-average of dual potential
= O(δ) vs √δ plateau). **Orchestrator analysis (UNVERIFIED — delegation D0 cross-checks):** the
m-average potential argument appears VACUOUS at the relevant scale. Sketch: the ℓ¹-dist dual
potential φ automatically has ‖φ‖_∞ ≤ 1 (so the "Lip blowup" killer test is trivially green =
ill-posed); the repair identity makes the capped-convex potential φ̌ = max(φ−cap,0) a 4δ-submartingale
along the q-chain; quasi-stationary slop ‖mq−m‖₁ ~ 2/L times max φ̌ ~ τ is O(δ) — same order as the
hoped-for gain. The argument only re-derives the C1/C2 lifetime dichotomy. A τ-plateau (quasi-closed
bad block at φ-height ~τ, internal circulation, O(τ) exit) is NOT excluded by averages; only vertex/
exposedness geometry can kill it. Reframe: bad configuration ⟺ a 4δ-submartingale plateau with
Ω(1/τ) lifetime and no new (ρ,κ)-exposed vertex. Question: can an exact retraction support one?
- D0 (DONE 2026-06-10): codex CONFIRMED vacuity (all 5 steps "correct"); proposed feedback identity
  UV = A(I−A) + W-exclusion (EXP: exposed vertex's own row sends ≤ δ/κ into far rows) + candidate
  augmentation lemma ("long-lived far block ⇒ contains a well-exposed vertex" = sharpened C14).
- D′ (DONE 2026-06-10, opus): REFUTED the order-one-return consequence — μUV = μA(I−A) = rA with
  r = μ(I−A), ‖r‖₁ ≤ 2/L + 3δ = O(τ) (orchestrator re-verified; 2-family confirmation pending).
  So the block identity gives an UPPER bound (small net exit), the wrong sign for the contradiction.
  Also: W-exclusion has two loopholes (~1/τ joint carriers; silence on non-exposed shell rows);
  shell ratchet descends Θ(log 1/δ) layers ⇒ would break the δ-free rate. New required inputs
  N1 (common separating functional), N2 (carrier control), N3 (lifetime persistence).
- VERDICT SHIFT: evidence now tilts toward a COUNTEREXAMPLE template — `cex-log-staircase`
  (multi-layer self-feeding shell, heights 2^{-m}Dτ, exit ε~τ, per-row neg η~δ, exact P²=P closed
  via UV = A(I−A)). If realizable ⇒ refutes the augmentation lemma and likely op-exposed-hull as
  stated (dist/τ ~ log(1/δ) → ∞). If provably obstructed ⇒ the obstruction IS the real lemma
  (idempotent-rigidity/spectral, not flow accounting). Agent-B's 4500-sample numerics could not
  have seen this (adversarial, measure-zero structure).
- D1 (NEXT): attempt explicit construction of a MINIMAL self-feeding shell (1–2 layers, small n)
  exactly — symbolic (wolframscript) + numeric (gurobi nonlinear/LP). Either an exact instance,
  or the precise over-constraint that kills it.
- Status: ACTIVE (D1). The lane has transformed from "proof via duality" into "decide the
  counterexample"; this now leads the whole portfolio (a counterexample would also moot lanes B/E).

### Lane B — Baake–Sumner probabilistic (quantitative stability of the idempotent classification)
B–S/Högnäs–Mukherjea (refs/baake-sumner-2007.11433, byte-pinned): exact stochastic idempotents =
equal-input absorbing blocks + proportional transient rows. Equal-input = one-step-mixing; Q²≈Q =
"two steps ≈ one step". Plan:
- B1: within-class lemma — strong q-communication ⇒ ‖q_i−q_j‖₁ = O(√δ) (coupling/Dobrushin). Opus.
- B2: class detection at scale √δ (the hard core — approximate recurrent classes well-defined?).
- B3: transient-row proportionality. B4: assembly into B–S normal form (uses thm-cluster's m-free
  assembly). Kill criterion: B1 already needs a spectral floor.
- Status: QUEUED.

### Lane E — variational skeleton (repair of agent-B's stuck campaign)
Replace maximal 4ρ-separated skeleton by minimizer of Φ(R) = Σ_i dist₁(p_i, conv R) + λ·Σ_{v∈R}
(κ−e_v(ρ))₊. KKT multipliers at the minimizer should bound the C12 α-mass by construction; improving
swaps replace the maximality contradiction. Reuses banked C0–C10 machinery.
- E0 (numerics): KKT α-multipliers under variational selection on sampled bad instances (codex +
  gurobi). Kill: multipliers ~1/√δ on clean small-δ samples.
- E1: variational anchoring lemma. E2: splice into C0–C10 chain.
- Status: QUEUED.

### Lane G — ultraproduct hedge (qualitative-first)
One opus pass: draft the limit argument (counterexample sequence → exact positive affine retraction
on limit algebra → B–S rigidity) + name the idempotent-lifting lemma precisely. Then PARKED.
- Status: QUEUED (one-shot).

### Lane C — cohomological (commutative Layer-1)
Advances through the main-branch `prop-comm-scalar`/`cor-adjoint-benchmark` campaign anyway.
Slow-rolled here; escalate only if D/B/E all stall. Risks: error-reduction iteration unbuilt;
positivity-capable output (`op-layer1-gap`).
- Status: PARKED (dual-use with main campaign).

### Cross-cutting
- X1: byte-pin Priority-0 refs via TIB (Blackwell 1942, Schwarz 1964, Hoffman 1952,
  Choquet–Corson–Klee 1966, Straszewicz 1935) — sonnet, when a lane first needs one (lazy, L1).
- X2: bank agent-B C0–C10 contracts into canonical registry LAZILY via Recipe A→B on main.
- X3: two-scale conjecture (exposedness at √δ, hull-distance at O(δ)) — primary numerical target in D1.

---

## Delegation ledger (append-only)
| # | Date | Lane | Worker (model/effort) | Task | Verdict |
|---|---|---|---|---|---|
| 1 | 06-10 | — | opus-4.8 (one-shot strategist) | independent strategy generation | HIGH value breadth/critique; 2 concrete constructions flawed (see LLM-LEARNINGS) |
| 2 | 06-10 | infra | codex gpt-5.5@xhigh | observability smoke test (stationary dist, 3 steps) | PASS: 5 streamed items, math correct, 2.3k out-tokens |
| 3 | 06-10 | D0 | codex gpt-5.5@xhigh | adversarial check of vacuity claim + τ-plateau | DELIVERED (after resume): (a) vacuity CONFIRMED all 5 steps; (b) plateau scalar-consistent; (c) feedback identity UV=A(I−A) + W-exclusion + candidate augmentation lemma |
| 4 | 06-10 | D′ | opus-4.8 (pure reasoning, 0 tool calls) | rigorous develop/verify of feedback-accounting attack | REFUTED the order-one-return step (μUV = rA, ‖r‖₁=O(τ): upper bound, inverted inequality); shell-height lemma proved mod N1; ratchet costs Θ(log 1/δ); proposed cex-log-staircase template + sub-lemma DAG. Orchestrator re-verified the key algebra |
| 5 | 06-10 | D′ | codex@xhigh (thread resume) | 2-family confirmation of the refutation | CONFIRMED ("algebraically correct; my consequence was too strong"); re-assessment of lemma truth in answer2.md |
| 6 | 06-10 | D1 | opus+tools (138 calls, 40min) | plateau counterexample hunt | NO counterexample (7000+ exact idempotents); 3 obstructions; LP-presolve artifact found+pinned red→green; "PROVED scaling" overclaim flagged by orchestrator AND codex independently |
| 7 | 06-10 | D2 | codex@xhigh (+script read) | verify obstructions; HCC attempt | lone-far-row lemma PROVED (κ≥ρ/(2+4δ)); HCC reduced to anchored-circuit cost; staircase reconciliation (real δ scales with height) |
| 8 | 06-10 | D3 | opus+tools (105 calls, 50min) | adversarial envelope mining | p=2 EXACTLY, a∈[2.4,3.5]; recursion-no-base-case skeleton; coincident-vertex bug found+pinned red→green |
| 9 | 06-10 | D4 | codex@xhigh (resume, 316k cached) | MCC proof attempt | 4 reductions PROVED; 3 opens named; operator-norm reframing ‖P‖≥1+cH²; skinny-quadrilateral = next target |
| 10 | 06-10 | D5 | opus+tools (53 calls, 40min) | ASQ via agent-B n=4 | n=4 dichotomy VERIFIED; ASQ proved in canonical frame (LINEAR δ≥H/2!); two-shadow composition proved vacuous; gap = frame transfer |
| 11 | 06-10 | D6 | codex@xhigh (resume, 420k cached) | frame-transfer attack | frame-clipping + intrinsic-leakage lemmas PROVED; gap compressed to FTI-2 + no-staircase (beads aipm-nhj, aipm-mox); P(true)=0.85, P(programme)=0.65 |
| 12 | 06-10 | D7 | opus+tools | FTI-2 numerical decider | LAUNCHED (running) |

## Lane-switch log
- 2026-06-10: start. Lane D first (D0 cross-check of orchestrator's vacuity analysis).

---
## STATE SNAPSHOT — 2026-06-10 end of day (supersedes lane-D details above)
**Conditional theorem (2-family verified):** op-exposed-hull ⟸ HLC, C′ = max(4A, 1/√a)
(notes/wave2/W2d-grand-assembly.md + assembly-verification-opus.md). HLC = aipm-e71.
**Proved belt (all independently audited; constants per notes/wave4/audit-summary.md):**
L1 lone-far-row; L2/L2'; C10 dual; L4 clipping; L5' maximizer leakage; L6 identity-frame linear;
N1 nilpotent chains; F1 skinny near-coincidence; X1 one-mode wall; X2 complement rank-preservation;
F-SS; F-ND (c=0.85); F-E kernel energy (R-explicit); F-GB g-budget; F-WR wiggle rigidity (side
conditions!); F-BC (κ+δ); F-2R. CONDITIONAL: F-ψ (needs ψ-gap lemma: "ρ-far non-S-full rows have
ψ-gap ≥ κZ"). VACUOUS-AT-SCALE: R1 descent (needs dual localization).
**Numerics (validated pipeline, multiplicity-correct W, honest τ):** no counterexample in 67k+
verified exact instances across 4 independent campaigns; floor δ/H² = 3.484 @ H/τ = 0.536 (d3, d7,
d8 concur); σ_v-wall law H/τ ≈ min(σ_v, 0.536), certificates: budget(=F-GB) / margin-pinned-at-κ.
**Residual opens:** (1) Branch-A budget analyticization (σ_v ≤ 1/2 ⇒ δ ≥ a₁H²); (2) Branch-B
margin-pinning (σ_v ≥ 1/2 ⇒ exposed unless H ≤ A₂τ); (3) ψ-gap lemma. Endgame codex push running
(/tmp/codex-endgame/). Literature: HLC is virgin ground = quantitative Douglas–Ando stability
(notes/literature-sweep-hlc.md).
**Process state:** ~30 codex runs (resume-chains + waves; user quota fine), 8 opus workers, 1 fable
(file-protocol mandatory — see LLM-LEARNINGS), 4 sonnet. All notes under notes/{wave1..4,*}.md.
**Next after endgame returns:** if branches close → full prose write-up + 2-family verify (done-bar)
→ Recipe A→B banking on main + report sections. If partial → residual is 1-2 named inequalities;
consider fable closer pass, then honest obstruction write-up (PRD-legitimate outcome).

---
## STATE SNAPSHOT — 2026-06-12 (supersedes 2026-06-10 snapshot; lockstep repair after the w32 pause)
**Where the campaign stands.** Waves 24–32 (2026-06-11, post-merge) ran the Högnäs–Mukherjea 1.12
coordinate route to its core. Chain (each link written, audited or refuted as marked):
1.12-autopsy (w25, PARTIALLY: right coordinates mod merge/conditioning) → clustered chart L2
dimension-free, A=1 max-volume basis (w26, audited) → O(δ) concentration REFUTED, in-class
concentration + cross-cluster leakage ≤ 2δ/(1−η) banked (w27) → bridge ⇒ representative
displacement lemma (w28) → general-row version REFUTED at δ=0; max-volume form is the kernel
(w29) → telescope: no contraction from idempotence alone; maxvol: displacement ⇐ transverse tax,
C_D ≤ 2(1+2δ₀)(2+C_μ) (w30) → tax split: deficit ≤ 2δ PROVED; residual = **signed-face excess
(SF)** = THE single open core (w31; P(tax true)=0.62, P(small-δ cex)=0.18) → w32 LP/extremal
prover PAUSED at stage 2 (network maintenance); banked: coefficient-only relaxation too weak at
δ=0 — geometry load-bearing from round one. All 44 wave-14..32 briefs archived `notes/briefs/`.
**SF ⇒** tax (C_μ=2+C_sf) ⇒ displacement ⇒ face estimate ⇒ L4 assembly ⇒ global W-free O(√δ).
**Wave 33 (launched 2026-06-12):** w33_sf_geom (codex prover: geometry-first gurobi LP loop +
1.12-converse exact parametrization) ∥ w33_cex (codex refuter: realize the transverse-pair
conspiracy via the 1.12 converse; either a stacking mechanism or the per-pair-cost obstruction
lemma) ∥ sonnet H-M book-mining catalog (→ `notes/hm-book-mining.md`). Briefs archived.
