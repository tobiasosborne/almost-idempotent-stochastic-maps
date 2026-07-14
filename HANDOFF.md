<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v26**, the
   2026-07-14 W66-W68 delta) + the rolling `docs/plans/CHANGELOG.md` (three
   new 2026-07-14 entries: W66, W67, W68).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) the objective function of every Tier-1 attack is DECOMPOSITION into
   lower-complexity pieces (user, 2026-07-10, reaffirmed 2026-07-14); (iii) creativity
   mandate for proof-strategy subagents, FINDINGS dead routes absolute; (iv) mostly
   serial; Fable = author-only for the hardest creative steps; verification
   fresh-codex-only, BATCHED by default (CLAUDE.md §6); (v) no progress theatre;
   (vi) codex effort CAPPED at xhigh (ultra retired 2026-07-13); xhigh creative /
   xhigh verify / high routine.
4. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push.
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-14, session 20 close — W69 pair banked; session 19 = W66+W67+W68)

**Session 20 (wind-up):** the H-X route fork **aism-ur9 is DECIDED: ROUTE A**
(codex named-H-X via X2/X3F/X3N/X4) — strategist decision under explicit user
delegation ("no strong feeling"); rationale on the issue (no surface change +
decider-informed; Route B = recorded fallback); the issue stays open as the
Route A execution item. Then the W69 DTR pair (AESC-ATTACK-W67 §4.3):

- **W69 decider (runs/2026-07-14-w69-dtr-growing-rank-decider/, L3,
  orchestrator-reproduced):** PARTIAL — the sharpest decider finding to date:
  growing rank (certified 4..32) realizes the LOCAL DTR geometry with exactly
  ZERO finance negativity (rank really distributes W55's cost; local
  D_EC < 0), but every GLOBAL gate fails by exact rank-uniform margins (R0
  ownership excess 1/8, H/tau = 0, shallow mass 1, empty ultra omega) and
  D_leaf > 0 throughout; NO margin improves with rank. Zero entrants/refuters.
  **Creative implication: the DTR proof must price root-to-top
  synchronization, not local negativity.**
- **W69 attack (docs/waves/2026-07-14-W69-artifacts/DTR-ATTACK-W69.md,
  banked RAW, objective (c), UNVERIFIED):** DTR reduced to the named **POTI**
  problem (pinned-deficit oriented-tail-incidence) via the canonical root/top
  overlap rho = min{m_A, eta_D*|_B} and the claimed-routine conversion
  S*Z_v(q_A) >= G_phi (POTI-R); two proper residuals POTI-0/POTI(+) + an
  actor-free weakened conversion with exact loss. **NOTHING verified yet —
  the downstream pipeline is bd `aism-cmk0` (FIRST TASK NEXT SESSION):**
  independent routine prover (high) on the routine batch incl. POTI-R,
  batched hostile verifier (xhigh), codifier + orchestrator audit,
  CHANGELOG/sketch reconciliation. Circularity guard stands: the repaired
  bridge is NOT consumable inside the DTR tree.

## Session-19 state (registry 194, sketch v26 — unchanged below)

**Rigorous (af-validated, T0): 34. Registry: 194 (+7 proved L5 + 1 conjecture
registered + 1 rewrite this session, all fresh-codex hostile-verified).**
Session 19 ran the full pipeline three times end-to-end:

- **W66 (aism-nrag, CLOSED):** the five-leaf D-cap L3 decider batch
  (`runs/2026-07-14-w66-dcap-five-leaf-decider/`, orchestrator-reproduced).
  ALL FIVE leaves BLOCKED in the tested exact families; C0 PARTIAL
  definition-level entrant (the factorized W63 plateau, eta_D*(C0) = 1-2*tau —
  adverse fixture); zero I-base data; zero refuters; **tallness binds for the
  SIXTH consecutive exact batch**. No tested family reaches the A-esc window
  (ell < tau/2 routes to C0 first); the T-esc shape only coexists with
  order-one finance negativity. Both unit tests pass.
- **W67 (aism-72zn, continues):** **A-esc DECOMPOSED**
  (`docs/waves/2026-07-14-W67-artifacts/AESC-ATTACK-W67.md`). Routine batch
  5/5 hostile-verified (SEP VALID-WITH-CORRECTION — affine functional applied
  to a displacement, corrected to the linear part; 4th genuine defect caught
  upstream). Five `lem-aesc-*` shards installed (187→192). **KEY MECHANISM
  EXTENSION: the starvation engine now prices SYNTHETIC finance rows** —
  hull-near missing actors pay Tail_1(u) > tau/8 (tau-scale, rank/slab-free);
  one-foldback tail union gives P_f*^+(U_tail) > tau/2560. A-esc == exactly
  TWO strictly smaller residuals: **HES** (rotating-separator crown refuter)
  and **DTR** (diffuse-tail ray conversion; rotating-incidence growing-rank
  refuter), both targeting the stronger same-center inequality (EC) with the
  exact E-line accounting. Fixed-K fallback removes A-esc at 1/160 loss.
- **W68 (aism-pus, CLOSED): THE ASSEMBLY BRIDGE IS REPAIRED**
  (`docs/waves/2026-07-14-W68-artifacts/`; 3/3 VALID-WITH-CORRECTION, all
  corrections metadata-level). `conj-l5-gap-1` REGISTERED (the W62-W67
  reduction tree now has its parent formally in the DAG);
  `lem-intersection-branch-production` PROVED (L5; the missing Branch-II
  implication, with the honest B1-B4/lem-top-witness-third-actor dependency
  repair); `lem-huddle-charge-assembly` REWRITTEN stated/DO-NOT-CONSUME →
  **proved (conditional)** on exactly {SL1a, SL1b, conj-cotop-web-coupling,
  conj-l5-gap-1}. **The known broken link between the L5 minimax campaign and
  the SL1a/kernel trunk is CLOSED.** Unconditional consumption of the bridge
  conclusion remains illegal (it rests on four open conjectures — the body
  says so).

**Open surface after session 19:** the tall near-cluster charge ==
four named conjectures through a proved conditional chain: SL1a (three
conj-sl1a-* cells), SL1b, conj-cotop-web-coupling (L6.5), conj-l5-gap-1.
L5-GAP-1's creative leaves: S, C (W62); D, W, Sh, X (W63);
X_gap/X_near/I_far/I_near/D_gap/D_near (W64); N/G<4/C0/T-esc (W65) +
HES/DTR (W67, replacing A-esc). Unchanged fronts: H-X route fork (aism-ur9,
USER DECISION), H-D, H-I, SL1b, L6.5, E1-E5, small-gauge bridge,
af-elevation queue (aism-88r).

## Next steps (ranked) — W70+

0. **aism-cmk0 (FIRST): the W69 downstream pipeline** — routine-prove +
   batched hostile-verify + codify DTR-ATTACK-W69.md (the POTI-R conversion
   is the highest-value hostile check: it claims exact row reproduction +
   mass-barycenter dualization + an attained ray certificate produce
   S*Z_v(q_A) >= G_phi); then HES (macroscopic h_u >= tau/32 subcase first).
1. **Route A execution (aism-ur9, DECIDED 2026-07-14):** stand up the named
   H-X wave — X2 microfreight exclusion (prove-or-refute; the W61 graft
   fixture is the refuter shape), X3F/X3N far/near actor selection, X4
   top-tail regularization; all consume the T0 engine bank.
2. **af-elevation queue (aism-88r):** prime candidates:
   lem-aesc-synthetic-finance-tail-amplification (engine-adjacent, single
   minimal contract), lem-intersection-branch-production (bridge-critical),
   lem-dcap-root-closure + lem-dcap-five-way-completion-split. The L5:T0
   ratio (~60:34) must not keep widening. af orchestrations STRICTLY SERIAL,
   repo-wide overreach guard, tree clean while live.
3. **The other three bridge conjectures:** SL1b and conj-cotop-web-coupling
   (L6.5, aism-zm8) now carry direct trunk value — every one closed shrinks
   the bridge's conditional surface. H-D/H-I creative waves (Fable
   candidates).
4. Remaining L5 leaves in decider-informed order (W64 six, then
   T-esc/G<4/C0/N, then X/Sh/W/D, then S/C with their fixtures). EVERY
   proof attempt must show where tallness is consumed AND the exact line
   producing c_m*tau/64 from E at p_f* — ledger-only proofs rejected.
5. Parked: aism-l1a (P2 polish), aism-cei (af→Lean scoping), refs ingest
   (aism-5de), aism-nlg / aism-z98 (user decisions).

## Standing rules (delta from session 18)

Everything in CLAUDE.md §6 unchanged (batched verification default; codex =
gpt-5.6-sol, effort CAPPED at xhigh; xhigh creative / xhigh verify / high
routine). Decomposition is the standing objective function (user, 2026-07-10,
reaffirmed 2026-07-14). Codification may be delegated to a fresh codex
transcription worker IF the orchestrator audits fidelity and the gates pass;
verifier-mandated corrections are codified in corrected form with the
correction named in provenance (W61/W64/W65/W67/W68 precedent). NEW
(W68 verifier ruling, now precedent): **shard `deps` are unconditional proof
imports, not bibliography/attack-tree arrows** — a conjecture registration
has empty deps; reduction-tree relations live in the body.

## What is intentionally NOT here

- Any claim more than THIRTY-FOUR results are af-validated. The ~60
  lem-ihorn-*/lem-icap-*/lem-dcap-*/lem-aesc-*/lem-l5-* + the W68 pair are
  L5-tier (fresh-codex hostile-verified), NOT af-validated.
- Any claim any creative leaf, the Kernel Conjecture, conj-l5-gap-1, or
  op-classical is proved. conj-l5-gap-1 is a REGISTRATION of an open
  conjecture. The repaired bridge is a proved CONDITIONAL implication — its
  conclusion may not be consumed unconditionally.
- Any claim of emptiness from the six decider batches: tallness binds are L3
  evidence about tested families only.
- Any claim the route fork is decided — it remains with the user (aism-ur9).
