<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (currently v25) + the rolling
   `docs/plans/CHANGELOG.md` — the seven W63/W64 entries plus the **2026-07-13 W65
   entry** carry the map deltas (I-horn + I-cap + D-cap decompositions, 25 proved
   shards across them).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) the objective function of every Tier-1 attack is DECOMPOSITION into
   lower-complexity pieces (task decomposition, case analysis, multiple small lemmas
   assembling to the target — user, 2026-07-10); (iii) creativity mandate for
   proof-strategy subagents, FINDINGS dead routes absolute; (iv) mostly serial;
   Fable = author-only for the hardest creative steps; verification
   fresh-codex-only, BATCHED by default (CLAUDE.md §6); (v) no progress theatre;
   (vi) **codex effort CAPPED at xhigh (user, 2026-07-13): ultra is unstable and
   spawns subagents indiscriminately — the cap is enforced in af-orchestrate.py
   (CODEX_EFFORTS/EFFORT_CAP + run_codex clamp) and CLAUDE.md §6; xhigh creative /
   xhigh verify / high routine.**
4. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push.
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-13, session 18 — W65 banked)

**Rigorous (af-validated, T0): 34. Registry: 187 (+7 proved this session, all
fresh-codex hostile-verified).** Session 18 enforced the xhigh effort cap
(commit 0371dd8), then ran the decomposition pipeline once end-to-end on the
D-cap leaf — the FIRST full wave at the cap, quality on par with the ultra-era
waves, zero rework:

- **W65 D-cap decomposition (`docs/waves/2026-07-13-W65-artifacts/`):**
  `conj-w63-I-disjoint-diagonal-corner-exclusion` decomposed on the proved
  interface. SEVEN routine nodes proved 7/7 (six VALID + B5
  VALID-WITH-CORRECTION) and codified (`lem-dcap-*`, registry 180→187):
  root closure (D-mass > 1/16, display field, R2-closed receivers,
  g_u ≤ A_u·ℓ_u with the (R0.6) gauge implication), score-bulk transfer,
  arbitrary-kernel census, common ownership, tall same-center packet
  (exact T-spend < 2τ/15 + E once at p_{f*}), closed overlay (B5 —
  contract restated per the verifier-confirmed (B5.C) Ξ_X correction), and
  the five-way 1/80 priority completion split. B1–B5 were REDERIVED
  kernel-arbitrarily on the D-cap class — zero I-cap-scoped `lem-icap-*`
  consumption (the verifier reopened all 11 consumed shards to confirm).
- **KEY STRUCTURAL SHARPENING: the higher-rank "slab escape" is dead as a
  diffuse threat.** `lem-hx-robust-scalar-starvation` is rank- and slab-free
  once actorized, so what escapes `lem-starvation-completion-obstruction`'s
  rank-3/slab hypotheses on the D cell is EXACTLY two named completion
  packages with pinned refuter shapes: **A-esc** (actorization escape: the
  synthetic zero-face displacement stays > 3δ from every actual row
  displacement on constant D mass; refuter = growing-rank actor-escape
  completion) and **T-esc** (scalar-tail escape: actual 3δ-residual actors
  exist but Tail₁(u) > δ rotates with the carrier; refuter = rotating-tail
  crown). The other three leaves (N near-hulls, G<4 low-gauge, C0 collapsed
  cloud) retain the non-escape cases honestly. Common leaf target:
  Z_v(q_A) ≥ c_m·τ/64 − (c_m/16)·P_v^+(L_v); assembly γ_dis = 7c_m/960 with
  an explicit emptiness ceiling.
- **Pipeline note (process):** strategist-prover (xhigh) → independent routine
  prover (high) → batched hostile verifier (xhigh) → transcription codifier
  (high) + orchestrator audit. The routine prover SELF-FLAGGED a genuine
  defect in the strategy doc (Ξ_X undefined) and the verifier adjudicated the
  unique correction — the third genuine defect caught upstream of
  codification in two weeks (after W61 A>0 and W64 priority guards). Never
  skip the hostile pass.

**Open surface after session 18:** the L5-GAP-1 tree has THREE proved
reduction layers below the W62 S/C/I trichotomy. Creative leaves: S, C (W62);
D, W, Sh, X (W63); X_gap/X_near/I_far/I_near/D_gap/D_near (W64, replacing
I-cap); N/G<4/C0/A-esc/T-esc (W65, replacing D-cap). Every leaf is a proper
constant-mass package. Plus the unchanged fronts: H-X route fork (aism-ur9,
USER DECISION), H-D, H-I, SL1b, L6.5, E1-E5 codification, small-gauge bridge,
af-elevation queue (aism-88r; 25 W63/W64/W65 L5 shards are candidates).

## Next steps (ranked) — W66+

0. **W65 §4.2 pre-creative L3 decider batch (aism-nrag, NEW):** exact-rational
   decider shapes for the five D-cap leaves, incl. the decisive A-esc
   growing-rank actor-escape and T-esc rotating-tail crown, the mandatory
   print panel, the D_leaf deficit (4.3), and the two unit tests (W63 plateau
   must route to D and fail tallness; W55 A₀=5 must reproduce its order-one
   negativity). Workers codex xhigh, exact Fractions, orchestrator
   reproduction before banking (L3 bundle discipline).
1. **Creative queue (aism-72zn, in progress):** after the deciders — A-esc,
   T-esc, G<4, C0, N (W65 §4.3 order); then the W64 leaves (I_far/I_near own
   the closed sign-cube packet; X_gap has the exact M_X ledger fixture), then
   X, Sh, W, D, then S and C (W62) with their decider fixtures. EVERY proof
   attempt must show where tallness is consumed AND identify the exact line
   producing the c_m·τ/64 term from E at p_{f*} — ledger-only proofs rejected
   before review.
2. **The route fork (aism-ur9, USER DECISION, fully decider-informed)** — Route A
   (codex named-H-X via X2/X3F/X3N/X4) vs Route B (Fable gamma-renegotiation via
   N4+N5/N6; N5 restatement prerequisite). Both consume the T0 engine bank.
3. **assembly-bridge repair (aism-pus)** — register the L5 premise as the
   L5-GAP-1 statement on the proved W62/W63 interface; codify l2-attack §2.6-2.7.
4. **af-elevation queue (aism-88r):** candidates now incl.
   lem-dcap-five-way-completion-split + lem-dcap-root-closure (the D-cap
   reduction spine) alongside the W63/W64 picks. Remember: af orchestrations
   STRICTLY SERIAL, repo-wide overreach guard, tree clean while live.
5. **E1-E5 codification + small-gauge bridge** (batched); **SL1b**, **H-D/H-I**
   (creative mechanism waves; Fable candidates).
6. Parked: aism-l1a (P2 polish), aism-cei (af→Lean scoping), refs ingest
   (aism-5de), aism-nlg / aism-z98 (user decisions).

## Standing rules (delta from session 17)

Everything in CLAUDE.md §6 (batched verification default; codex = gpt-5.6-sol,
**effort CAPPED at xhigh — ultra retired 2026-07-13**; xhigh creative / xhigh
verify / high routine). Decomposition is the standing objective function for
Tier-1 attacks (user, 2026-07-10). Codification may be delegated to a fresh
codex transcription worker IF the orchestrator audits
frontmatter/deps/hypothesis-block fidelity and the linker gates pass;
verifier-mandated corrections are codified in corrected form with the
correction named in provenance (W61/W64/W65 precedent).

## What is intentionally NOT here

- Any claim more than THIRTY-FOUR results are af-validated. The 25 W63/W64/W65
  lem-ihorn-*/lem-icap-*/lem-dcap-* shards are L5-tier (fresh-codex
  hostile-verified), NOT af-validated.
- Any claim any creative leaf (S, C, D, W, Sh, X; the W64 six; the W65 five),
  the huddle charge, the Kernel Conjecture, or op-classical is proved.
  L5-GAP-1 itself remains OPEN — only its reduction interface is proved.
  D-cap is NOT proved: γ_dis = 7c_m/960 is conditional on five open leaves.
- Any claim of emptiness from the refuter batches: five consecutive tallness
  binds are L3 evidence, not a theorem; the I cell "never entered" is a
  statement about the tested families only.
- Any claim the route fork is decided — it remains with the user (aism-ur9).
- `lem-huddle-charge-assembly` remains INVALID-as-stated / DO-NOT-CONSUME
  (aism-pus).
