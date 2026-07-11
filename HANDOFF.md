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
   `docs/plans/CHANGELOG.md` — the SEVEN 2026-07-10/11 W63/W64 entries carry this
   session's map deltas (S/C deciders; I-horn decomposition + 10 proved shards;
   six-shape decider; I-cap decomposition + 8 proved shards incl. the corrected R).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) the objective function of every Tier-1 attack is DECOMPOSITION into
   lower-complexity pieces (task decomposition, case analysis, multiple small lemmas
   assembling to the target — user, 2026-07-10); (iii) creativity mandate for
   proof-strategy subagents, FINDINGS dead routes absolute; (iv) mostly serial;
   Fable = author-only for the hardest creative steps; verification
   fresh-codex-only, BATCHED by default (CLAUDE.md §6); (v) no progress theatre.
4. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push.
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-11, session 17 — W63 + W64 banked)

**Rigorous (af-validated, T0): 34. Registry: 180 (+18 proved this session, all
fresh-codex hostile-verified).** Session 17 ran the decomposition pipeline twice
end-to-end on the L5 minimax front (strategist-prover ultra → batched hostile
verifier xhigh → codification), plus three exact L3 decider batches:

- **W63 S/C deciders (`runs/2026-07-10-w63-sc-decider/`):** both pre-creative
  shapes BLOCKED. The C width bouquet satisfies C's ENTIRE antecedent incl. the
  engine payment and fails ONLY tallness — the missing C step is isolated to the
  chord-demand-to-ray-certificate coupling under tallness.
- **W63 I-horn decomposition (`docs/waves/2026-07-10-W63-artifacts/`):** node I
  == asymptotically an EMPTINESS theorem (priced ray: Z_v(q_A) <= 3*tau^2/c_m);
  hard core = tall completion obstruction. TEN routine nodes proved 10/10 VALID
  and codified (`lem-ihorn-*`, registry 162→172): priced-ray package, tall halo
  saturation (1 - sigma_g = O(tau)), dual co-top geography (13/16), universal
  exterior package, drift/width payer extraction at scale b*tau = c_m*tau/128,
  ultra compression, rim-to-SL1b package, co-top SL1a package (constants
  STRONGER than registered SL1a thresholds), selected-corner extraction.
  **STRUCTURAL UNIFICATION: the ultra-isotropic core of the L5 minimax routes
  into the same X/I/D selected-corner cell trichotomy as the SL1a fronts.**
  Six creative leaves: D, W, Sh, X, I-cap, D-cap.
- **W63 six-shape decider (`runs/2026-07-11-w63-ihorn-six-shape-decider/`):** ALL
  BLOCKED, zero I-base entrants, **5th consecutive tallness bind**; the natural
  diagonal plateau gets M_I = 0 EXACTLY and routes to the D cell (the sign-cube
  I cell has NEVER been entered); first exact M_X > 1/8 corner ledger (X-leaf
  fixture). Pre-creative decider program for all nine W62+W63 creative surfaces
  COMPLETE.
- **W64 I-cap decomposition (`docs/waves/2026-07-11-W64-artifacts/`):** objective
  (a) achieved — EIGHT routine nodes proved (7/8 VALID + R
  VALID-WITH-CORRECTION: the six-way residual split needed priority guards to be
  disjoint; verifier exhibited exact overlaps and the fix, constants preserved)
  and codified (`lem-icap-*`, registry 172→180): score-bulk census (>1/14
  score-good), arbitrary-kernel X/I/D bulk census (one cell >= 1/42), common
  receiver statistic with constant top ownership (P_v^+ > c_m/512 / c_m/1536),
  explicit T-spend (shallow mass < 2*tau/15), internally-closed diagonal-flow
  package (c_m/1024 outer-halo covered flow), type-I structural cost (singleton
  far-tight family impossible — exactly why the plateau had M_I = 0), priority
  residual split. **Hard core in one sentence: an exact high-rank sign cube must
  carry constant top mass on alpha-free cancellation vertices while its two-fold
  positive flow is covered inside the saturated halo and every common scalar
  demand stays O(delta).** NEW exact 4x4/8x8 I-cell calibrations (verified by
  the hostile pass) show intersection alone is NOT the obstruction — tall TOP
  OWNERSHIP is: coupling a multi-ray I module into a tall ultra web is the cost.
  Six strictly smaller creative leaves: X_gap, X_near, I_far, I_near, D_gap,
  D_near.

**Open surface after session 17:** the L5-GAP-1 tree has TWO proved reduction
layers below the W62 S/C/I trichotomy. Creative leaves: S, C (W62); D, W, Sh,
X, D-cap (W63); X_gap/X_near/I_far/I_near/D_gap/D_near (W64, replacing I-cap).
Every leaf is a proper constant-mass package; every refuter search (5/5) died at
tallness and/or the negativity budget. Plus the unchanged fronts: H-X route fork
(aism-ur9, USER DECISION), H-D, H-I, SL1b, L6.5, E1-E5 codification, small-gauge
bridge, af-elevation queue (aism-88r; the 18 new L5 shards are candidates).

**Process (validated this session):** the full pipeline strategist-prover(ultra)
→ batched hostile verifier(xhigh) → codification (orchestrator or fresh codex
transcription with orchestrator audit) ran twice with zero rework; the hostile
pass caught TWO genuine defects ultra provers missed (W61 financing-floor A>0;
W64 R priority guards) — never skip it. Decider workers: codex xhigh, exact
Fractions, orchestrator reproduction before banking. All wrapper logs outside
the repo; workspaces via scripts/build-workspace.sh in the scratchpad.

## Next steps (ranked) — W65+

0. **Creative queue on the decomposed L5 front (aism-72zn, in progress):** per
   the W63+W64 dispatch orders — D-cap next (strongest positive mechanism:
   bounded-slab + robust starvation), then the W64 leaves (I_far/I_near own the
   closed sign-cube packet; X_gap has the exact M_X ledger fixture), then X, Sh,
   W, D, then S and C (W62) with their decider fixtures. EVERY proof attempt
   must show where tallness (lem-ihorn-tall-halo-saturation or a parent height
   budget) is consumed — ledger-only proofs rejected before review. L3 decider
   shapes for the W64 leaves are listed in ICAP-ATTACK-W64.md §4.2.
1. **The route fork (aism-ur9, USER DECISION, fully decider-informed)** — Route A
   (codex named-H-X via X2/X3F/X3N/X4) vs Route B (Fable gamma-renegotiation via
   N4+N5/N6; N5 restatement prerequisite). Both consume the T0 engine bank.
   Convergent signal: the winning mechanism must consume H > 16*tau
   quantitatively — same wall as the L5 front.
2. **assembly-bridge repair (aism-pus)** — register the L5 premise as the
   L5-GAP-1 statement on the proved W62/W63 interface; codify l2-attack §2.6-2.7.
3. **af-elevation queue (aism-88r):** prime candidates from this session:
   lem-ihorn-cotop-sl1a-package, lem-ihorn-selected-corner-extraction,
   lem-icap-kernel-bulk-census, lem-icap-priority-residual-split (the load-bearing
   reduction spine). Remember: af orchestrations STRICTLY SERIAL, repo-wide
   overreach guard, tree clean while live.
4. **E1-E5 codification + small-gauge bridge** (batched); **SL1b**, **H-D/H-I**
   (creative mechanism waves; Fable candidates).
5. Parked: aism-l1a (P2 polish), aism-cei (af->Lean scoping), refs ingest
   (aism-5de), aism-nlg / aism-z98 (user decisions).

## Standing rules (delta from session 16)

Everything in CLAUDE.md §6 (batched verification default; codex = gpt-5.6-sol,
ultra creative / xhigh verify / high routine). NEW (session 17): decomposition is
the standing objective function for Tier-1 attacks (user directive 2026-07-10);
codification may be delegated to a fresh codex transcription worker IF the
orchestrator audits frontmatter/deps/hypothesis-block fidelity and the linker
gates pass; verifier-mandated corrections are codified in corrected form with
the correction named in provenance (W61/W64 precedent).

## What is intentionally NOT here

- Any claim more than THIRTY-FOUR results are af-validated. The 18 new lem-ihorn-*/
  lem-icap-* shards are L5-tier (fresh-codex hostile-verified), NOT af-validated.
- Any claim any creative leaf (S, C, D, W, Sh, X, D-cap, X_gap, X_near, I_far,
  I_near, D_gap, D_near), the huddle charge, the Kernel Conjecture, or
  op-classical is proved. L5-GAP-1 itself remains OPEN — only its reduction
  interface is proved.
- Any claim of emptiness from the refuter batches: five consecutive
  tallness binds are L3 evidence, not a theorem; the I cell "never entered" is a
  statement about the tested families only.
- Any claim the route fork is decided — it remains with the user (aism-ur9).
- `lem-huddle-charge-assembly` remains INVALID-as-stated / DO-NOT-CONSUME
  (aism-pus).
