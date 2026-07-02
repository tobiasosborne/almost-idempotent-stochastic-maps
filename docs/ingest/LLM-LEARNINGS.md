# LLM-delegation learnings (classical-portfolio sidequest)

Meta-experiment: large-scale math research with LLM subagents. One entry per delegation
(or notable orchestrator observation). Durable lessons also go to `bd remember`.

Format: `- [date] [worker@effort] [task type] — what happened; lesson.`

## Entries

- 2026-06-10 [opus-4.8@default, one-shot strategist, distilled brief] — strategy generation:
  produced 5 genuinely distinct routes + sharp architectural critique of the stuck campaign
  (maximality = no optimality slack; C9 = measure-controls-rows category error). HIGH value.
  BUT two of its concrete constructions contain errors a careful reader catches: (i) Strategy 1's
  E = lim q^{k!} kills the near-1 modes it must keep (2-state counterexample: Q=[[1,0],[ε,1−ε]]);
  (ii) Strategy 3's killer test (Lip of optimal dual potential) is trivially green — the ℓ¹-dist
  dual is ‖φ‖_∞ ≤ 1 BY CONSTRAINT. Lesson: opus one-shot ideation = excellent breadth + critique;
  every concrete construction needs an independent derivation pass before resources are committed.
- 2026-06-10 [codex/gpt-5.5@xhigh, infra] — WEDGED-SOCKET failure mode: a wifi blip mid-run left
  codex retrying ("Reconnecting 2/5..4/5"), then it hung indefinitely on an ESTAB-but-dead TLS
  socket — no output, no exit, for ~25 min. Undetectable without event streaming. FIXES (now
  standard for all codex runs): (1) never `--ephemeral` on long runs (it kills `codex exec resume`);
  (2) always `--json` events to a file — "thinking" vs "stuck" must be observable; (3) a 10-second
  low-effort smoke test cleanly separates pipeline-health from run-health before relaunching.
  Also: kill+relaunch cost ≈ nothing (the wedged run generated almost no tokens).
- 2026-06-10 [codex/gpt-5.5, infra #2] — ROOT CAUSE of the wedges: "idle timeout waiting for
  websocket" — long silent xhigh reasoning ⇒ idle websocket ⇒ flaky network path drops it ⇒
  reconnect attempts can exhaust/hang. MITIGATIONS THAT WORK: (1) PROGRESS PROTOCOL — instruct the
  model to emit a short message after each deliverable; keeps the stream warm, makes stalls
  observable, AND checkpoints partial results server-side (the resumed thread retained the finished
  audit). (2) `codex exec resume <thread-id>` genuinely continues with full context — but exec-level
  flags (-C/-s/--json/-o) must come BEFORE the `resume` subcommand token, only --skip-git-repo-check
  etc. after. (3) Monitor + bounded watchdog + kill/resume loop = robust against arbitrary flakes.
- 2026-06-10 [codex/gpt-5.5@xhigh, D0 math] — second-family adversarial audit WORKS: codex verified
  the orchestrator's vacuity analysis step-by-step (ℓ¹-dual identification, truncation sign,
  bookkeeping orders) rather than deferring to it — exactly the independent-check value we wanted
  from a non-Claude family. Quality of partial output: high, precise, no hedging.
- 2026-06-10 [sonnet Explore x4, parallel summarization, async] — branch-corpus summarization:
  all four faithful and precise on first pass; the registry agent (37 tool uses) correctly
  distinguished proved/conjectured/numerical throughout. Lesson: sonnet Explore is the right
  tool for corpus distillation; give it explicit "keep proved/conjectured/numerical distinct"
  instructions and it complies.
- 2026-06-10 [day-1 meta, serial multi-model] — the alternating prover/verifier pattern ACROSS model
  families (opus proves → codex verifies → codex proposes → opus refutes → ...) caught an inverted
  inequality, an overclaim, two numerics artifacts, and one vacuous proof route in a single day —
  each catch by a DIFFERENT party than the author. Thread-resume on codex is the efficiency key
  (420k cached tokens by D6; each continuation costs only the new reasoning). Opus tool-workers
  self-debugged honestly (both red→green pins were their own initiative). Calibrated-probability
  asks ("P(true)? P(provable)?") produced usefully honest numbers from codex, not flattery.
- 2026-06-10 [process] — "progress message after each deliverable" doubles as wedge-detection AND
  server-side checkpointing for codex resume; now standard in every brief. Monitor harness with
  answer-file/process-death/stall detection made 6 long runs babysittable at near-zero attention.
- 2026-06-10 [fable@max, HLC attack #1] — FAILURE MODE: 64-minute run died at the END with "response
  exceeded the 64000 output token maximum" — the entire hour of reasoning lived in the final message
  and was lost (31 tool calls were all reads; nothing on disk; SendMessage continuation unavailable
  in this harness). LESSON (now standard for ALL long math subagents): the deliverable is a FILE,
  written INCREMENTALLY after each proof stage; the final message is a ≤300-word pointer+verdict.
  Same principle as the codex progress-protocol — checkpoint to durable storage, never accumulate
  the payload in the terminal message.
- 2026-06-11 [wave-5: 8 parallel codex@xhigh, mandated-diverse strategies + 1 unsteered control] —
  PARALLEL DIVERSITY EXPERIMENT (user: "vive la différence"), results:
  (1) CONVERGENCE AS SIGNAL: 6/6 A/B provers independently adopted the same deficit frame
  (g = H−φ, g = Pg, F-GB top-band) and died at the SAME inequality (top-band localization) despite
  3 disjoint mandated technologies (LP-dual / spectral / functional) — independent convergence on
  both the frame AND the death-point is strong evidence the residual is genuinely ONE lemma, not an
  artifact of one prover's blind spot. The unsteered CONTROL choosing the same route as a mandated
  worker is itself a validity signal for that route.
  (2) MANDATED-ANGLE value: even DEAD angles paid — the spectral worker's anti-lemma (canonical-g
  energy ≤ δR² — route provably insufficient) and the duality worker's C10-exchange identity are
  reusable facts a single-prover session would not have produced.
  (3) OPPOSITE-BIAS PAIRS on the same target (ψ prove-bias vs ψ2 refute-bias): both refuted the
  literal lemma with DIFFERENT counterexamples; the refuter ALSO found why its own cex dies under
  the intended reading, yielding the minimal fix. Bias-pairing produced both the kill AND the
  rescue — cheaper than a prove-then-audit chain.
  (4) Asking every worker for "the precise failing inequality in display math" made the 8-way
  cross-comparison mechanical; the died-at lines aligned almost verbatim.
  (5) Logistics: 8 concurrent codex@xhigh ran clean (no wedges; progress-protocol in every brief);
  wall-clock ~35-75 min each; answers landed asynchronously — harvest file written incrementally
  per landing (crash-safe), convergence table filled as a running artifact.

## 2026-06-12 — gurobi unusable inside the codex sandbox (HostID license mismatch)
w33_cex: `gurobi_cl`/`gurobipy` import fine but OPTIMIZE fails inside `codex exec -s
workspace-write` with a HostID license mismatch (the sandbox's hostname/network isolation
breaks the machine-locked license; failures saved in experiments/out/w33_cex/
tiny_gurobi_test.out, sf_gurobi_failure.out). Gurobi works fine OUTSIDE the sandbox
(orchestrator-verified same day). PATTERN going forward: (a) prefer SciPy HiGHS in codex
briefs — and note that fixed-L searches are LINEAR once BL=I enforces idempotence, so HiGHS
suffices there; (b) for genuinely nonconvex gurobi work (NonConvex=2 bilinear), have codex
WRITE the script and the ORCHESTRATOR run it outside the sandbox. Update future briefs:
do not promise in-sandbox gurobi.
