<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md`).
2. Read the sketch named in **`docs/plans/CURRENT.md`** (now **v28**, the
   2026-07-23 W73/W73b/W74F delta — *a second, independent route enters the map*)
   + the rolling `docs/plans/CHANGELOG.md` (newest entry = v28).
   **STEWARDSHIP (user mandate, binding): reconciling the sketch/CHANGELOG with newly
   banked evidence is a FIRST-CLASS DELIVERABLE of every session (Rule 9).**
3. Then read, in this order: `docs/plans/2026-07-22-strategy-reset-w73.md` (§2 Route F,
   §3 Route X) and `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md`
   (executive verdicts, Correction ledger, **Residual risk register** — that register is
   the current Tier-1 face).
4. **STANDING DIRECTIVES (user, binding):** (i) ALL mathematical capacity on the open
   leaves; (ii) the objective function of every Tier-1 attack is DECOMPOSITION into
   lower-complexity pieces (2026-07-10, reaffirmed 2026-07-16); (iii) creativity mandate
   for proof-strategy subagents, FINDINGS dead routes absolute; (iv) mostly serial;
   Fable = author-only for the hardest creative steps; verification fresh-codex-only,
   BATCHED by default (CLAUDE.md §6); (v) no progress theatre; (vi) codex effort CAPPED
   at xhigh; xhigh creative / xhigh verify / high routine;
   **(vii) NEW 2026-07-23: concerted effort on Route F — it is the P0 direction.**
5. `fr board` + `bd ready`. Beads sync: `scripts/beads-sync.sh import` after pull /
   `export` before push.
6. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-23, session 22 — W73 · W73b · W74-F wave 1)

**Rigorous (af-validated, T0): 34. Registry: 200. Unchanged — W73/W73b/W74F have
produced strategy, an audit verdict, and dispatched provers, not registry results.**

### The headline: op-classical now has two candidate routes, and the new one is P0

- **Route F (factorization–hardening)** bypasses the entire signed-geometry trunk. Two of
  four independent W73 strategists converged on it. Skeleton F0–F5 in sketch v28 §"Map
  change 1". Its shape: lift `Q` to `Φ = J∘Q∘D` on `M_n` → import Kitaev's approximate
  factorization → force commutativity (Pauli commutator gap 2) → compress back to
  stochastic `A`, `M` with `‖MA−I_k‖ ≤ ε` → **PRH** hardens the approximate retract into
  an exact stochastic idempotent at `√`-cost → `‖Q−E‖ ≤ (K+4√(2K))√η`.
- **The W73b hostile audit (aism-u4x5, closed) is the decisive fact.** Fresh codex,
  xhigh, source-first against the byte-verified tex: **Q1 VALID · Q2
  VALID-WITH-CORRECTIONS · Q3 INVALID · Q4 VALID · Q5 VALID.** Verbatim bottom line:
  *"F0–F3 are sound conditional on Theorem 12.3, but Theorem 12.3 is not rigorously
  established by the supplied TeX as written."*
  - The real flaw is **smaller and sharper** than the sibling repo believed: the printed
    **direct-sum diagonal formula** at `tex:1254` / `tex:2780-2783` is false (exact `ℂ⊕ℂ`
    counterexample). It is NOT the `Δ̃`-multiplicativity diagnosis of sibling FINDINGS
    C14 — the auditor **proved** the positivity argument entrywise given an exact central
    diagonal and supplied an elementary Haar / phase-balanced repair; `lem_RC` and the
    `Υ'` construction survive fully.
  - The **principal blocker is `th_main_ext`** (`tex:1538-1540`), whose proof
    (`tex:1542-1557`) is an adaptation outline that never exhibits one map carrying all
    the uniform amplified bounds; plus a printed omitted-squares typo at `tex:1551-1555`.
  - Universality is claimed explicitly (paper convention, `tex:458`) but never extracted.
    For op-classical a numerical `K` is unnecessary; **universality is necessary**.
- **Both papers are ingested and pinned** under `refs/` (aism-5de, closed):
  `refs/kitaev-2405.02434/approximate_algebras.tex` (SHA256 `e7eb512a…`) and
  `refs/salzmann-bergh-datta-2405.01532/`.

### W74-F wave 1 — DONE and hostile-verified 4/4

Four fresh codex `gpt-5.6-sol` **xhigh** workers, one per disjoint register item (epic
**aism-enze** P0; all four issues now CLOSED), then a single fresh **batched hostile
verifier** over the whole batch (`VERDICT-W74F-BATCH.md`, tex SHA re-checked, W73b audit
not treated as an oracle): **A · B · C · D all VALID, no correction required to any
target.** Artifacts under `docs/plans/2026-07-23-W74F-artifacts/`:

| wave | register item | verified result |
|---|---|---|
| A `PROOF-W74F-A-PRH.md` | 6 — PRH | `‖MA−I_k‖≤ε<1/2` ⟹ stochastic idempotent `E`, `‖AM−E‖≤2√(2ε)`; `√ε` **intrinsically sharp** (family with every `F` at `≥√(ε/2)`). Constant dispute settled at `2√2`. |
| B `PROOF-W74F-B-DIAGONAL.md` | 3+4 | `tex:1254`/`2780-2783` formula non-central; finite **phase-balanced** repair exact, projective norm **1, block-count-free**, diagonal of the *exact* `ℬ`; CP-ization entrywise; **no cone shortcut**. |
| C `DECOMP-W74F-C-THMAINEXT.md` | 1+2 | `th_main_ext` == **H-CB + EXT-CB** (only two gaps); rest established/mechanical; `tex:1551-1555` squared correction proved; ledger conditional on those two. |
| D `AUDIT-W74F-D-ALMOSTIDEMP.md` | 5 | diagrammatic core dimension-free at **10η** after local source type/index fixes; extended interface survives. |

Cross-target (verified): constants consistent once `ε_AI` / `K` / `ε_PRH` are kept
distinct; conditional finish `‖Q−E‖ ≤ (K+4√(2K))√η`; **no circularity**. This does NOT
close Route F: it leaves **H-CB, EXT-CB, the unconditional `K`/`η_K` ledger**, and
this-repo codification/provenance open. A hostile-verified L5 result is **not**
af-validated and **not yet a registry shard** — registry unchanged at 200, T0 at 34.

### Why PRH matters independently of Kitaev

PRH (F4) is the **only** Route F step that is ours rather than the literature's, and it
is elementary. Proved, it installs a new reduction on the map — *op-classical ⇐ "a
positive approximate retract exists"* (`‖AM−Q‖ = O(η)`, `‖MA−I‖ = O(η)`, `A`, `M`
stochastic) — a cleaner target than anything the signed picture currently offers,
**whether or not the import ever closes**. Two independent derivations disagree on the
constant (`2√2` vs `3`); settling that is part of W74F-A.

### Carried forward, unchanged

- **The W72 verification debt (aism-x0up) is still owed.** POTI-0's decomposition
  (S0 / RX / O48 / RDSE / LDHR-48) is proved-standalone by an independent prover but its
  batched hostile verifier was interrupted before any verdict: **UNVERIFIED, uncodified**.
  Banked work gets verified or explicitly retired — there is no third state.
- **RDSE / LDHR-48 creative attacks are PAUSED** (user directive 2026-07-23). Stated
  reason: strategists B and D independently argued those leaves sit at the wrong altitude
  (`w_*` is not a charge; the dilution escape `w_*→0` is real). That diagnosis is itself
  unverified.
- Route X (RTS / APAL / QCMP) is the in-repo fallback shape if F1 dies; deciders filed
  (aism-ea2f), carrier/quotient shards filed (aism-h9qc). Nothing of it is proved or
  decided.

## Next steps (ranked) — W74-F and after

0. **Codify the four hostile-verified survivors (aism-zbcm, P0).** Registry shards at
   `proved-mod-audit` / `stated` (NOT af-validated, NOT proved). PRH first — it is
   standalone, complete, and the load-bearing independent asset; state it as
   *op-classical ⇐ "a positive approximate retract exists"*. Needs a def-vocabulary pass
   (stochastic idempotent, approximate retract, extended ε-C*-algebra, diagonal, Ha-map)
   — some defs may need user ratification (arm-G aism-l70 precedent → **Stop condition**,
   escalate before adding/changing a definition). May be delegated to a fresh codex
   transcription worker IF the orchestrator audits fidelity and gates pass (W70). Blocks
   PRH af-elevation (aism-h9qc).
1. **Wave 2 = prove-or-refute H-CB (aism-wwur, P0), then EXT-CB (aism-9lb7).** H-CB is the
   first `th_main_ext` gap: uniform-in-`n` column-Hilbert / operator-module estimates for
   `1_{M_n}⊗Ha^Q_{P,R}`; the danger is a hidden `n`-factor behind the source's
   "straightforward" (`tex:1555`). One fresh prover, decomposition-first. **CRITICAL
   FORK:** a *counterexample* to H-CB challenges `th_main_ext`'s claimed dimension-free
   uniformity — that re-routes the whole campaign and must be **escalated**, not worked
   around. EXT-CB assumes H-CB. Then the unconditional `K`/`η_K` ledger.
2. **af-elevate PRH** (aism-h9qc, after codification): small, self-contained, the natural
   next af workspace — CLAUDE.md §6, strictly serial, tree clean while live.
3. **Discharge the W72 debt** (aism-x0up): re-dispatch `BRIEF-W72-POTI0-VERIFIER.md`
   (workspace rebuild recipe in `docs/plans/CHANGELOG.md`'s W72 entry), or retire the
   batch explicitly with a certificate.
4. **Route X deciders (aism-ea2f)** — cheap, exact, kill-or-confirm; the fallback if F1
   dies. Do not start a Route X proof campaign before its deciders run.
5. **af-elevation queue (aism-88r):** L5:T0 ≈ 66:34 and widening. Prime candidates
   unchanged (lem-dtr-oriented-tail-ray-conversion, lem-dtr-canonical-overlap,
   lem-aesc-synthetic-finance-tail-amplification, lem-intersection-branch-production,
   the D-cap spine).
6. Route A execution (aism-ur9); SL1b; conj-cotop-web-coupling (L6.5, aism-zm8);
   H-D/H-I; then POTI+ / HES if Route F stalls and the pause is lifted.
7. Parked: aism-l1a, aism-cei, aism-nlg, aism-z98 (user decisions),
   rank>3/unbounded-K gadget LPs.

## Standing rules (delta from session 21)

CLAUDE.md §6 unchanged (batched verification default; codex = `gpt-5.6-sol`, effort
CAPPED at xhigh — never `ultra`; xhigh creative / xhigh verify / high routine).
Decomposition remains the standing objective function. Codification may be delegated to a
fresh codex transcription worker IF the orchestrator audits fidelity and the gates pass.
Shard `deps` are unconditional proof imports; conjecture registrations have empty deps;
conditional lemmas name conjecture premises in BOTH contract and deps.

**New this session:** literature-import work carries the same rigour ladder as our own —
a theorem *stated* in a pinned paper is `stated`, and a theorem whose *printed proof* an
audit found invalid is **not importable at all** until the repair is proved here. Route F
is a conditional reduction, never "op-classical modulo a citation".

## What is intentionally NOT here

- Any claim more than **34** results are af-validated, or that the registry moved off
  **200**. W73, W73b and W74F wave 1 produced no registry results.
- Any claim that Route F proves op-classical. F0/F2/F3/F5 are audit-VALID **conditional
  on F1**, and F1's printed proof is INVALID as it stands.
- Any claim that PRH is proved, or that its constant is `2√2` rather than `3`.
- Any claim that Kitaev's theorem is **false**. The audit's finding is about the printed
  proof; the theorem may well be true and provable — that is what W74F-B/C/D test.
- Any claim that W72's decomposition (S0/RX/O48/RDSE/LDHR-48) is verified, or that the
  POTI subtree is retired — it is paused with its verification debt outstanding.
- Any claim that the strategists' altitude diagnosis of RDSE/LDHR-48, or their
  interpretation of the 18-wave empirical record, is a theorem. Both are banked
  interpretation.
- Any emptiness claim from the seven consecutive tallness-bound decider batches: L3
  evidence about tested families only.
