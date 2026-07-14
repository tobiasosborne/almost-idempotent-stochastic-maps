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

## Current state (2026-07-14, session 19 — W66+W67+W68 banked)

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

## Next steps (ranked) — W69+

0. **DTR creative attack (aism-72zn)** — W67 §4.3 order: one root, one
   canonical common receiver set, tau/2560 floor, one B4 center, one top
   ray; target is the exact (EC) line, not a ledger. Run its growing-rank
   L3 decider IN PARALLEL (shapes pinned in AESC-ATTACK-W67.md §4.2:
   D_EC and D_leaf diagnostics are NOT interchangeable). Then HES
   (macroscopic h_u >= tau/32 subcase first).
1. **The route fork (aism-ur9, USER DECISION, decider-informed since W60)**
   — Route A (codex named-H-X) vs Route B (Fable gamma-renegotiation).
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
