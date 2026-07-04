<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (**15 green nodes** — but read the honesty
   note below), `FINDINGS.md` (2026-07-03 orphan section + 2026-07-04 frame-free callout),
   `docs/LEARNINGS.md` (first entry: the lem-dual-localization tautology), `report/main.pdf`
   (15 shards; results 1–13 sectioned, 14–15 ledger-row-only pending `aism-av0`).
3. Wave artifacts in `docs/waves/` (B1–B4, F1–F2, A1–A12, D1–D6, **G1–G12**); L3 bundles in `runs/`
   (7 — newest: `2026-07-04-cross-pivot-kill-test`, the decision-check pattern).
4. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-04, session 6 CLOSE, incl. continuation) — FIFTEEN rigorous results

**Rigorous (af-validated in-repo, banked, T0):** results 1–12 (see `argument/INDEX.md`) plus, this
session: **13. `lem-pivot-removing-move`** (the max-stationarity disjunction + exact transform; 9-node
run-1 tree, zero challenges), **14. `lem-collateral-import`** (the (CI) bound
`Phi_r(V_j) ≤ Phi_r(U) + I_{r,j}`; 32-node run-1 tree, zero open challenges), **15.
`lem-cross-pivot-cancellation`** (`Σ_i β_r(i)a_s(i) = 0`; 23-node run-1 tree). **Honesty note (session
audit):** 13 and especially 15 are near-definitional; the counter overstates content — the substantive
rigorous core remains ~6 results. All three `fr verify` pass; oracles registered (15 total).

**The headline of the session — the (PRT) collateral horn is now a 7-step pre-factored skeleton with
ONE open link** (G12, `docs/waves/2026-07-04-G12-b-question.md`):

```text
disjunction (VALIDATED) → (CI) (VALIDATED) → import reduction (mod-audit, elementary)
→ cross-pivot cancellation (VALIDATED) → [B-lemma: OPEN] + [C ≤ 2δ: elementary via box]
→ collateral conclusion M − Phi_r(U) ≤ K_G·δ → G8 three-blocker ledger → (PRT) high-self input.
```

- **The open link — the B-lemma:** at a capped θ-½ argmin carrying a clean high-self non-fan
  Γ-branch, `B_{r,s} = Σ_i β_r(i)⁺ a_s(i)⁻ ≤ K·δ`. Facts bracketing it: `B = 0` is FALSE (G12: exact
  certified capped argmin with `B = 2/57`), but all capped-argmin data is sub-δ; non-argmin `B/δ` is
  unbounded (50 at ε=1/100) and **minimality pivots the offending chart away** — minimality is
  demonstrably the operative constraint. Named tool gap: the `c < 0` pivot-removing move (validated
  (CI) covers only `c > 0`).
- **Assembly is rate-tolerant** (G12 Q2): no step of the G6/G7/G8 chain needs `o(δ)`; the only issue
  is contract-level (the naked `+C_δ·δ` term — USER decision `aism-z98`).
- **How we got here:** wave G9 realized the (V)/(P) blocker branches exactly (bounded ratios); G10
  realized the Γ-pattern locally (δ=49/60, cap-blocked) and derived (CI); the kill-test bundle
  (`runs/2026-07-04-cross-pivot-kill-test/`, L3) found `B ≡ 0` on all prior instances and
  `C ≤ 2δ` trivially; G12 refuted the `B ≡ 0` extrapolation and delivered the skeleton.

**Session audit (user-requested, logged in fr; POLICY — respect it):** ~half the session's output was
self-documentation/ritual elevation; the budget was patched reactively twice before (G5→SIGMA,
G6→silent rows) — watch the epicycle pattern (the pending `+C_δ·δ` term is different: it arrives WITH
its financing derivation). Policies now standing: **no near-definitional elevations by default**
(`lem-import-reduction` stays proved-mod-audit pre-decision); **cheap decision-checks before
narrowing waves** (the kill-test pattern); trivial-lemma weight discounted in the rigorous counter.

**Also this session:** `lem-dual-localization` retired (contract was a distance tautology; superseded
by `conj-skinny-shadow-cap` — user decision; first `docs/LEARNINGS.md` entry); arm-G session-5
outputs codified with fully-inline contracts (user decision; `conj-rh`, `conj-sc`,
`obs-orphan-amplifier`, plus the elevated tools); lab-book shards AISM-08..14; `check-provenance.py`
false-green fixed (hard-coded ledger filename); registry at 46 results, linker green.

## Next steps (ranked) — RESUME HERE

1. **Arm G wave 13 (`aism-5sc`): the B-lemma** — prove `B_{r,s} ≤ K·δ` at clean high-self Γ-branches
   via minimality on the B-carrying rows (likely needs the `c < 0` pivot-removing analogue first — a
   small codify step; elevate only if the audit policy's bar is met), or amplify `B/δ` along
   certified capped argmin families (G12 instance as seed). This is the ONLY open link of the
   collateral skeleton.
2. **USER DECISION (`aism-z98`):** do `conj-sc`/`conj-rh` contracts admit an explicit `+C_δ·δ(P)`
   term (the G12 C-financing)? Options: amend now (mechanism-derived, comes with proof) / require
   reabsorption in the proof / defer until the B-lemma decides.
3. **Lab-book sections for results 14–15 (`aism-av0`)** — ledger rows exist; sections pending
   (extend the issue to cover `lem-cross-pivot-cancellation` too).
4. **af-elevation backlog — FILTERED by the audit policy** (elevate only what a proof will lean on
   under adversarial pressure): the D5 ledger lemma, D2 source split, `ΣΓ⁻ ≤ δ` budget, A12
   λ-correction, G5 harmonic ledger, G6 ambient/chart identity. All need codification first
   (fully-inline convention). `lem-import-reduction`: elevate only when the skeleton assembles.
5. **(BN)** `S⁻^μ ≤ C₋δ`: one more adversarial hunt then elevate or codify.
6. **B-side** when diversifying (audit: diversification is due if wave 13 stalls): the sigma-cap is
   the live target; `conj-skinny-shadow-cap` is the corrected Route-B statement.

## Standing rules (see CLAUDE.md + bd memories; audit additions in bold)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af contracts;
pre-factor linear chains; node-cap 40; no argument//definitions edits while an orchestration runs
(commit BEFORE launching — the overreach guard is git-porcelain-based); numerics = exact-ℚ with
orchestrator recomputation; waves = verbatim docs/waves/ artifacts, honest T0–T3 tiers, fr log per
pull, workers told no fr/bd; wave prompts/answers/transcripts in the session scratchpad. **Audit
policies: decision-check before narrowing wave; no ritual elevations; discount trivial-lemma weight;
watch reactive budget patches.**

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
fr verify proofs/<id>/export.md --oracle af-<id>   # 15 oracles registered
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>   # wave
cd proofs/<id> && "$AF" export -f markdown > export.md && "$AF" export -f latex > export.tex
# decision-check pattern: runs/2026-07-04-cross-pivot-kill-test/ (deterministic exact-Q,
#   known-value asserts, INDEX rows) — cheap and decisive BEFORE dispatching a wave.
```

## What is intentionally NOT here

- Any claim that more than FIFTEEN results are rigorous — and the counter itself overstates content
  (see the audit note; ~6 carry substantive weight).
- Any claim (EX)/Kernel/op-classical is closed — open inputs: the B-lemma ⇒ (PRT) collateral horn,
  then (PRT)'s other branches' charges, (SC) low-self side, (RH) assembly, the fan interface, (BN),
  and the B-side sigma-cap. The skeleton is pre-factored, NOT proved.
- A naked `+C_δ·δ` term in `conj-sc`/`conj-rh` — pending the USER decision (`aism-z98`).
- `C_legal = 0`, any orphan budget without `Σβν`, pointwise `ν_j ≥ a_t(j)⁻`, the retired
  dual-localization framing (see `docs/LEARNINGS.md`).
- A git remote (local-only by decision).
