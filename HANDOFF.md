<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v29**, the 2026-07-24
   W74F-wave-2 delta — *both `th_main_ext` gaps close at L5; the W72 debt is
   discharged*) + the rolling `docs/plans/CHANGELOG.md` (newest entry = v29).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. Then read `docs/plans/2026-07-24-W74F-wave2-artifacts/` — the wave-2 proofs and
   verdicts (`PROOF-W74F-E-HCB.md` + `VERDICT-W74F-E-HCB.md`, `PROOF-W74F-F-EXTCB.md`
   + `VERDICT-W74F-F-EXTCB.md`), and the codification reports.
4. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) decomposition is the objective function of every Tier-1 attack;
   (iii) creativity mandate for proof-strategy subagents, FINDINGS dead routes
   absolute; (iv) mostly serial; Fable = author-only for the hardest creative steps;
   verification fresh-codex-only, BATCHED by default (CLAUDE.md §6); (v) no progress
   theatre; (vi) codex effort CAPPED at xhigh; (vii) **Route F is the P0 direction**
   (2026-07-23); (viii) RDSE/LDHR-48 creative attacks PAUSED (2026-07-23).
5. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push.
6. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-24, session 23 — W74F wave 2 + W72 discharge)

**Rigorous (af-validated, T0): 34 — unchanged. Registry: 214 (was 200).**
Session 23 was an orchestration session under the user mandate "orchestrate work on
the ultimate proof; delegate all work to codex gpt-5.6-sol xhigh": five prover/verifier
/codifier dispatches, every landing banked, verified (fresh hostile codex), codified,
and gated.

### The headline: `th_main_ext` — Route F's principal blocker — is CLOSED at L5

- **H-CB proved** (`conj-hcb` → `proved-mod-audit`, aism-wwur closed). Fresh prover +
  separate fresh hostile verifier (VALID-WITH-CORRECTIONS). `C_H = 4000c`,
  `e_H = 1/(10000c)`, relative to the sanctioned COMP-CB/COL-HILB constants;
  dimension-free; no `n`-growth family. Genuine finding: the unconditional `h_{P,P}`
  inverse is FALSE (exact `ℂ⊕ℂ` counterexample); the contract now carries the
  verifier's exact conditional-inverse clause — precisely what `lem_extension`
  consumes. A refinement, not an escalation.
- **EXT-CB proved** (`conj-extcb` → `proved-mod-audit`, dep `conj-hcb`, aism-9lb7
  closed). VALID-WITH-CORRECTIONS. One level-one unitary carries every amplification
  via the transported-corner construction (verifier-confirmed);
  `C_ext = C_merge[1+5C_H+20C_app(C_H+1)]`; one proof-level correction (`e_sel`
  enlargement), no contract amendment.
- Through `lem-thmainext-conditional`, **`th_main_ext` holds at the proved-mod-audit
  rung**. The Route F chain F0–F5 is proved-mod-audit end-to-end **except** the
  unconditional `K`/`η_K` extraction; conditional finish `‖Q−E‖ ≤ (K+4√(2K))√η`.
- **NOTHING new is af-validated.** All wave-2 statuses rest on single fresh hostile
  codex passes (the batched-verification default) — one rung below T0, honestly
  tagged.

### Also this session

- **Wave-1 survivors codified** (aism-zbcm closed; registry 200 → 208): `lem-prh` +
  `lem-prh-sharpness` (constant settled at `2√2`; the PRH reduction *op-classical ⇐
  positive-approximate-retract-exists* is now a registry fact), diagonal repair +
  CP-ization, the two gap conjectures (since closed), the conditional assembly, the
  `th_almost_idemp` audit import. **Four draft definitions AWAIT USER RATIFICATION:**
  `def-positive-approximate-retract` (original), `def-extended-epsilon-cstar-algebra`,
  `def-ha-map`, `def-fd-cstar-diagonal` (cited byte-verbatim, SHA-verified).
- **W72 debt discharged** (aism-x0up): the interrupted POTI-0 batched hostile verifier
  was re-run from a rebuilt `build-workspace.sh` snapshot — **S0/RX/O48/ASM2 all
  VALID**, cross-cutting clean — then codified (registry 208 → 214): S0/RX/O48 +
  conditional assembly `proved-mod-audit`; RDSE + LDHR-48 registered as `conjecture`
  (empty deps, attacks PAUSED). POTI-0 == RDSE + LDHR-48 is now a proved-mod-audit
  conditional reduction on the signed trunk.
- **IN FLIGHT at session close: the wave-3 unconditional `K`/`η_K` ledger prover**
  (aism-xpxk, fresh codex xhigh, `BRIEF-W74F-G-KLEDGER.md` →
  `LEDGER-W74F-G-K.md`). If its output is not yet banked when you read this, check
  `docs/plans/2026-07-24-W74F-wave2-artifacts/` for the artifact; it must go through
  a fresh hostile verifier before any codification (no third state).

## Next steps (ranked)

0. **Land wave 3** (aism-xpxk): bank the K-ledger prover output RAW, dispatch a fresh
   hostile verifier, then codify the closed relative `K`/`η_K` chain (statuses per
   verdict). The one possibly-new inequality is the raw-step/reset threshold check
   (DECOMP §7 item 10) — if the prover flags it unclosable, that is a named gap, not
   a footnote.
1. **PRH af-elevation** (aism-h9qc, unblocked): the first Route F node to attempt T0.
   CLAUDE.md §6 verbatim; seed with the `lem-prh` contract; strictly serial; registry
   tree clean while the orchestration runs (banking flips AFTER it lands).
2. **User decisions pending:** (a) ratify or amend the four draft definitions;
   (b) whether to af-elevate the H-CB/EXT-CB chain next (both are large — factor per
   §6 playbook before seeding); (c) the parked decisions (aism-ur9, aism-z98,
   aism-l1a, aism-cei, aism-nlg).
3. **Route X deciders** (aism-ea2f): cheap kill-or-confirm; keeps the fallback priced
   while Route F converges. Do not start a Route X proof campaign before they run.
4. **af-elevation queue** (aism-88r): L5:T0 now ≈ 86:34 and widening — the queue is
   the long-term debt sink. Prime candidates unchanged.
5. Signed-trunk surface (SL1a cells, sigma-cap, halo-robust finisher): behind Route F
   in priority, not retired. POTI+/HES/RDSE/LDHR-48 stay PAUSED until the user lifts
   the pause.

## Standing rules (delta from session 22)

CLAUDE.md §6 unchanged. New precedent this session: **verdict-driven contract
amendment** — when a hostile verifier's contract-impact note supplies an exact
replacement clause, the orchestrator applies it as a MECHANICAL reflection of the
external verdict (recorded in the shard body + commit), never as its own judgment.
Literature-import discipline unchanged: a theorem whose printed proof is invalid is
not importable until repaired HERE (th_main_ext is now such a repair, at L5).

## What is intentionally NOT here

- Any claim that op-classical is proved, or that Route F is rigorous. The chain is
  `proved-mod-audit` end-to-end modulo the in-flight `K`/`η_K` extraction; L0 rigour
  = af-validated/byte-cited/Lean ONLY; **T0 is still 34**.
- Any numerical `K` or `η_K` — the source's unnamed big-O constants make the ledger
  relative by construction.
- Any claim that the four new definitions are ratified (pending user sign-off).
- Any claim that RDSE/LDHR-48 moved (registered, paused), or that the strategists'
  altitude diagnosis became a theorem (banked interpretation).
- Any emptiness claim from the tallness-bound decider batches: L3 evidence only.
