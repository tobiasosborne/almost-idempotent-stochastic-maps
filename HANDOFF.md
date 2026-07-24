<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v30**, the 2026-07-24
   wave-3 delta — *Route F is proved-mod-audit COMPLETE; the remaining open work is
   L0 closure*) + the rolling `docs/plans/CHANGELOG.md` (newest entry = v30).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. The full W74F wave-2/3 record lives in
   `docs/plans/2026-07-24-W74F-wave2-artifacts/` (briefs, proofs, and — decisive —
   the verdicts: `VERDICT-W74F-E-HCB.md`, `VERDICT-W74F-F-EXTCB.md`,
   `VERDICT-W74F-G-KLEDGER.md` (INVALID — instructive), `VERDICT-W74F-H-STAGE1.md`).
4. **STANDING DIRECTIVES (user, binding):** (i) all mathematical capacity on the open
   leaves; (ii) decomposition as objective function; (iii) creativity mandate,
   FINDINGS dead routes absolute; (iv) mostly serial; verification fresh-codex-only,
   batched by default (§6); (v) no progress theatre; (vi) codex capped at xhigh;
   (vii) Route F is P0; (viii) RDSE/LDHR-48 attacks PAUSED.
5. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push (run with **bash**, not sh).
6. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-24, session 23 close — W74F waves 2, 3, 3b + W72 discharge)

**Rigorous (af-validated, T0): 34 — unchanged. Registry: 215 (was 200).**

### The headline: ROUTE F IS `proved-mod-audit` COMPLETE

Every node of
`op-classical ⇐ F0 cb-lift ⇐ th_factorization (⇐ th_main_ext ⇐ H-CB + EXT-CB +
Stage-1 packet; + th_almost_idemp interface; + repaired diagonal) ⇐ F2/F3 ⇐ PRH ⇐
finish` is now hostile-verified (fresh codex prover ≠ fresh codex verifier, per node)
and codified. Final composite: universal relative `K ≥ 1`, `η_K > 0`
(dimension/amplification/block-free) with
`‖Q−E‖_{∞→∞} ≤ (K+4√(2K))√η` for `η ≤ η_K` — the sharp exponent 1/2 preserved.

Session flips (each a mechanical reflection of an external verdict):
- `conj-hcb` → `proved-mod-audit`, contract amended to the verifier's exact
  conditional-inverse clause (the unconditional inverse is FALSE — exact `ℂ⊕ℂ`
  counterexample).
- `conj-extcb` → `proved-mod-audit` (transported-corner construction confirmed; dep
  `conj-hcb`).
- `lem-thmainext-conditional` restated to the endorsed `C_E`/`ε_E` assembly contract.
- `lem-routef-k-ledger` NEW at `proved-mod-audit` — closed after a genuine hostile
  REJECTION: the first ledger (wave 3) was INVALID for one missing Stage-1 packet
  (`lem_nontriv_projection`, `tex:1419-1425`); wave 3b extracted `C_split`/`e_split`
  and the corrected reset chain, and its own fresh verifier closed it.
- W72 discharged: POTI-0 batch verified 4/4 VALID + codified (6 shards); POTI-0 ==
  RDSE + LDHR-48 at `proved-mod-audit`; residuals registered, PAUSED.

**Rigour honesty (the only sentence that matters): NOTHING above is rigorous by L0.**
`proved-mod-audit` = hostile-verified paper proof, one rung below T0. The repaired
chain is not byte-verbatim citable (the source's printed proof was invalid); af/Lean
is the only approved route up.

### Pending USER decisions

1. **Ratify the four draft definitions** (`def-positive-approximate-retract`
   original; `def-extended-epsilon-cstar-algebra`, `def-ha-map`,
   `def-fd-cstar-diagonal` cited byte-verbatim, SHA-verified).
2. **Sanction the L0-closure campaign shape** (next steps 0–1 below) — af-elevation
   order and how to factor the large chain.
3. Parked: aism-ur9, aism-z98, aism-l1a, aism-cei, aism-nlg.

## Next steps (ranked) — the new Tier-1 face is L0 closure

0. **PRH af-elevation** (aism-h9qc): small, elementary, self-contained — the natural
   first T0 attempt of the Route F chain. CLAUDE.md §6 verbatim: seed with the
   `lem-prh` contract via `seed-af-workspaces.py`, `af-orchestrate.py` backgrounded,
   strictly serial, registry tree CLEAN while live (banking flips only after it
   lands).
1. **Decomposition pass for the large chain** (file a bead): H-CB, EXT-CB, Stage-1,
   the assembly, and the ledger each exceed the af brittleness envelope as single
   trees. The task is to factor them into registry sub-lemmas below `>12`-node/depth-3
   before ANY af seeding. Decomposition-first is the standing objective function.
2. **Route X deciders** (aism-ea2f): cheap kill-or-confirm; keeps the fallback priced.
3. **af-elevation queue** (aism-88r): L5:T0 ≈ 87:34 and widening.
4. Signed trunk (SL1a cells, sigma-cap, halo-robust finisher): parked behind Route F;
   POTI+/HES/RDSE/LDHR-48 PAUSED until the user lifts the pause.

## Standing rules (delta from session 22)

Two precedents added this session:
- **Verdict-driven contract amendment/restatement**: when a hostile verdict's
  registry-impact note supplies exact contract text, the orchestrator applies it as a
  mechanical reflection (recorded in body + commit), never as its own judgment.
- **A hostile REJECTION is a normal, valuable cycle** (wave 3 → 3b): bank the INVALID
  verdict, dispatch the named repair, re-verify fresh. Banked work is verified or
  explicitly retired — no third state (upheld twice this session: W72, wave 3).

## What is intentionally NOT here

- Any claim that op-classical is proved/rigorous, that T0 moved off **34**, or that
  any hostile verdict equals af-validation.
- Any numerical `K`/`η_K` (relative expressions only — the source prints no decimals
  and none were invented).
- Any claim that the four draft definitions are ratified.
- Any claim that RDSE/LDHR-48 or the signed trunk moved (they did not), or that the
  strategists' altitude diagnosis became a theorem (banked interpretation).
- Any emptiness claim from the tallness-bound decider batches: L3 evidence only.
