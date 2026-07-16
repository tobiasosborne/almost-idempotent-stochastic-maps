<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v27**, the
   2026-07-16 W69-W70 delta) + the rolling `docs/plans/CHANGELOG.md` (three
   2026-07-16 entries: v27/W70, W71, W72 — the W72 entry records a PENDING
   verification, see below).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) the objective function of every Tier-1 attack is DECOMPOSITION into
   lower-complexity pieces (user, 2026-07-10, reaffirmed 2026-07-16); (iii) creativity
   mandate for proof-strategy subagents, FINDINGS dead routes absolute; (iv) mostly
   serial; Fable = author-only for the hardest creative steps; verification
   fresh-codex-only, BATCHED by default (CLAUDE.md §6); (v) no progress theatre;
   (vi) codex effort CAPPED at xhigh; xhigh creative / xhigh verify / high routine.
4. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push.
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-16, session 21 close — W70 + W71 + W72)

**Rigorous (af-validated, T0): 34. Registry: 200 (+4 proved L5 + 2
conjectures registered this session, all through the validated pipeline).**

- **W70 (aism-cmk0 CLOSED): DTR == POTI-0 + POTI+ — VERIFIED.** The W69
  reduction ran the full pipeline: routine prover (high) → batched hostile
  verifier (xhigh) → **4/4 VALID, ZERO corrections** (the campaign's
  cleanest batch; verifier confirmed the z-scope is
  `lem-top-deficit-price`'s literal scope at EVERY row index, and the
  dualization is literally about the un-normalized m_A) → codifier +
  orchestrator audit. New shards: `lem-dtr-canonical-overlap`,
  `lem-dtr-oriented-tail-ray-conversion` (POTI-R: S*Z_v(q_A) >= G_phi),
  `lem-dtr-tail-coherent-conversion` (TC — the FIRST proved
  quantitatively-weakened theorem on the A-esc front; actor-free, exact
  loss r_0*alpha*lambda/(16S)), `lem-dtr-poti-assembly` (conditional exact
  (EC) + strict 7*c_m*tau/960; conclusion NOT consumable unconditionally),
  + registered `conj-dtr-zero-oriented-surplus-exclusion` (POTI-0) and
  `conj-dtr-positive-oriented-surplus-gap-exclusion` (POTI+). The
  diagnostics are proved ORDERED: D_leaf >= D_EC >= D_POTI/S. Sketch v27.
- **W71 (banked): the ownership trade-off law.**
  `runs/2026-07-16-w71-poti0-zero-overlap-decider/` (L3, reproduced):
  BLOCKED — but the exact law max_i nu(P_i) = beta*a makes R0 root
  ownership (beta >= 1/8) exactly incompatible with the negativity gate
  (beta <= tau^2/a) at every rank/tau: **the root-ownership repair cost
  tends to 1/8 and does NOT distribute with rank** (inverts W69 one level
  up: local DTR geometry free, root ownership order-one). Support
  disjointness (rho(1)=0) survives only OUTSIDE the gate; orientation
  starvation never reached; SEVENTH consecutive tallness bind.
- **W72 (aism-x0up, IN PROGRESS — VERIFICATION PENDING): POTI-0
  DECOMPOSED, unverified.** `POTI0-ATTACK-W72.md` (objectives (a)+(c)):
  POTI-0 == [S0 exact cause split rho(1)=0 vs orientation starvation] +
  [RX zero-overlap exchange ledger, exact price sigma_B >= w_*M_B -
  e_delta] + [O48 fixed-level starvation ledger on the single public slab
  V_48 = {z < 48*tau}] + TWO disjoint creative residuals: **RDSE**
  (root-dilution selected-support exchange, owns rho(1)=0; exact escape =
  selected-root dilution w_*->0, unbounded below on the interface) and
  **LDHR-48** (low-deficit huddle ray, owns starvation). KEY negative: the
  W71 law is FAMILY-SPECIFIC, not the general mechanism. The routine batch
  (S0/RX/O48/ASM2) is proved standalone
  (APPENDIX-W72-poti0-proofs.md, independent prover, zero self-reported
  defects) but **the batched hostile verifier was INTERRUPTED (task
  stopped externally) before any verdict — NOTHING of W72 is verified or
  codified. Registry unchanged at 200; sketch NOT bumped.**

## Next steps (ranked) — W73+

0. **FIRST: re-run the W72 hostile verifier (aism-x0up).** Rebuild the
   workspace (`bash scripts/build-workspace.sh <ws> --waves
   2026-07-14-W67-artifacts/AESC-ATTACK-W67.md,2026-07-13-W65-artifacts/DCAP-ATTACK-W65.md,2026-07-10-W63-artifacts/DECOMPOSITION-W63-I.md,2026-07-14-W69-artifacts/DTR-ATTACK-W69.md`
   + copy `POTI0-ATTACK-W72.md` → `POTI0-ATTACK.md` and
   `APPENDIX-W72-poti0-proofs.md` → `APPENDIX-poti0-proofs.md` at the
   workspace root + fixtures W69/W71 run bundles), dispatch
   `BRIEF-W72-POTI0-VERIFIER.md` (xhigh, fresh). #1 hostile checks:
   selected-root provenance w_* > 0 (the lem-ihorn-* literal statements
   incl. partially selected clone fibers), both foldback undivided
   ledgers (1.8)/(1.17), O48's coefficient-vs-row-mass scope in (1.15).
   Then codifier (lem-poti0-* ×4 + conj-poti0-* ×2 → registry ~206, W68
   deps semantics), gates, **sketch v28** (Tier-1 leaf set changes:
   POTI-0 == RDSE + LDHR-48), CHANGELOG, fr log.
1. **The RDSE / LDHR-48 creative attacks** (decider-informed): RDSE first
   (the W71 witness family + the w_*-dilution escape define the refuter
   shape); LDHR-48 needs its own L3 decider (no exact orientation-starved
   family exists — untouched territory for both sides).
2. **af-elevation queue (aism-88r) — PRIORITY RISING:** L5:T0 ≈ 66:34 and
   widening. Prime candidates: lem-dtr-oriented-tail-ray-conversion
   (single-conclusion, engine-adjacent), lem-dtr-canonical-overlap (small,
   measure-theoretic), lem-aesc-synthetic-finance-tail-amplification,
   lem-intersection-branch-production, the D-cap spine. af orchestrations
   STRICTLY SERIAL, repo-wide overreach guard, tree clean while live.
3. **Route A execution (aism-ur9, decided 2026-07-14):** the named H-X
   wave — X2 microfreight exclusion (W61 graft fixture = refuter shape),
   X3F/X3N, X4; consumes the T0 engine bank.
4. **The other bridge conjectures:** SL1b, conj-cotop-web-coupling (L6.5,
   aism-zm8), H-D/H-I creative waves; then POTI+ z-level attack, HES
   macroscopic subcase (aism-x0up).
5. Remaining L5 leaves in decider-informed order; EVERY proof attempt must
   show where tallness is consumed AND the exact line producing
   c_m*tau/64 from E at p_f* — ledger-only proofs rejected.
6. Parked: aism-l1a, aism-cei, aism-5de, aism-nlg, aism-z98 (user
   decisions), rank>3/unbounded-K gadget LPs.

## Standing rules (delta from session 20)

Everything in CLAUDE.md §6 unchanged (batched verification default; codex =
gpt-5.6-sol, effort CAPPED at xhigh; xhigh creative / xhigh verify / high
routine). Decomposition is the standing objective function. Codification may
be delegated to a fresh codex transcription worker IF the orchestrator
audits fidelity and the gates pass (W70 precedent adds: judgment calls
flagged loudly in INSTALL-NOTES). Shard `deps` are unconditional proof
imports; conjecture registrations have empty deps (W68 ruling). Conditional
lemmas name conjecture premises in BOTH the contract ("Assume ... hold") and
deps (lem-huddle-charge-assembly / lem-dtr-poti-assembly pattern).

## What is intentionally NOT here

- Any claim more than THIRTY-FOUR results are af-validated. The ~66
  lem-*-tier shards incl. the four new lem-dtr-* are L5 (fresh-codex
  hostile-verified), NOT af-validated.
- Any claim that W72's decomposition (S0/RX/O48/RDSE/LDHR-48) is verified —
  the hostile verdict is PENDING; the appendix is a prover artifact only.
- Any claim POTI-0, POTI+, DTR, any creative leaf, the Kernel Conjecture,
  conj-l5-gap-1, or op-classical is proved. lem-dtr-poti-assembly is a
  proved CONDITIONAL implication — its conclusion may not be consumed
  unconditionally.
- Any emptiness claim from the seven consecutive tallness-bound decider
  batches: L3 evidence about tested families only. The W71 trade-off law
  is family-specific (the W72 strategist's analysis of WHY is itself
  unverified).
