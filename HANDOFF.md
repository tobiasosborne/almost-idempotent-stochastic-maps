<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md`, then `CLAUDE.md` (== `AGENTS.md` — esp. L0 rigour ladder, Rule 13 dead routes).
2. Read the two session-7 canonical reviews — they reshaped the plan:
   **`docs/audits/2026-07-04-operational-audit.md`** (sober 4-lane audit) and
   **`docs/lit-review/2026-07-04-literature-sweep.md`** (7-lane sweep; Kitaev poses our problem's
   noncommutative lift as OPEN — arXiv:2405.02434).
3. Run `fr board` and `bd ready`. Skim `argument/DAG.md` (15 green nodes — ~6 substantive, per the
   honesty note), `FINDINGS.md` (now incl. the 2026-07-04 literature negative-space section),
   `docs/LEARNINGS.md`, `report/main.pdf`.
4. Wave artifacts in `docs/waves/` (newest: **G13 prover / G13 amplifier / G13 review**); L3 bundles in
   `runs/` (**10** — newest: rank4-transfer-decider, small-delta-b-sweep, b-amplifier-hunt).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-04, session 7 CLOSE) — frontier is NSC(K0); fifteen rigorous (unchanged)

**Rigorous (af-validated, T0):** the same 15 as session 6 (`argument/INDEX.md`); honesty note stands
(~6 substantive). Nothing entered the rigorous record this session — by design (audit policies).

**Session 7 was strategy + de-risk + wave 13.** In order:

1. **Operational audit (4 sonnet lanes, banked):** one validated result on the wired critical path
   (`lem-classical-equiv`); B-lemma ≈ 1–5% of remaining work; dominant unpriced risks = rank-3-only
   scoping, the unaudited inherited downstream chain (`thm-classical-factorization`/JB, HLC), and the
   prose-only `conj-ex ⟺ conj-kernel` equivalence; fr breaker structurally defeated by `progress`
   self-tagging; registry count is 44 (session-6 HANDOFF's "46" was stale).
2. **Literature sweep (7 sonnet lanes, banked):** NOBODY states `op-classical` anywhere. Tier-1:
   **Kitaev arXiv:2405.02434** poses the noncommutative generalization verbatim as open (sign-function
   fix is linear but loses positivity — his Prop 3.1/Example 1.3; his §§5–9 incremental toolkit is an
   alternative strategy source); **Salzmann–Bergh–Datta arXiv:2405.01532** Thm 5.2 = √ε dimension-free +
   SHARP for approximate fixed *distributions* (reset-trick Lemma 5.5 transferable); **Luo–Pang /
   Mangasarian–Shiau** degenerate-complementarity mechanism explains the ½ exponent and backs the
   never-dispatched **arm E**. Negative space banked in FINDINGS (TVKW hitting-times not dimension-free;
   Mehta spectral-gap wall; incoherence mismatch; "quantitative Baake–Sumner web stability" DOES NOT
   EXIST — inherited pointer unsubstantiated). PDFs staged in `refs-staging/` (SHA256s in worklog);
   formal pinning is an open bd issue.
3. **De-risk deciders (both PASS, banked as runs/ bundles, orchestrator-recomputed):**
   `rank4-transfer-decider` — the skeleton transfers to rank 4/5 in bounded exact search (disjunction +
   c>0 (CI) hold, 48 moves/144 pairs, CI slack 0; Φ/δ plateau intact: 5/4, 4/3); `small-delta-b-sweep` —
   the old "all capped-argmin B data is sub-δ" was a δ≈cap artifact: **B/δ rises to ≈0.771 at δ≈0.055**,
   bounded by argmin switching (minimality binds).
4. **Wave 13 (both branches + independent review, aism-5sc CLOSED):**
   - **Prover (T1+T2, review APPROVE):** the `c<0` pivot-removing transform + import bound
     `Φ_r(V_j) ≤ Φ_r(U) + I⁻_{r,j}` (equality form per the reviewer) — the named tool gap is closed at
     reviewed-paper-proof level. The B-lemma is proved CONDITIONAL on one minimal subclaim:
     **NSC(K0): `B_{r,s} ≤ K0·Σ_{carriers} β_r(i)⁺·ν_i(P)`** ⇒ `K = 5K0/4` under the cap.
   - **STRUCTURAL HEADLINE:** in every certified stress instance the ENTIRE B-mass sits on
     **volume-inadmissible carriers** — pivot-removing minimality is blind to it; Ψ-blocks escape the
     transverse import bound; Γ-blocks give only forward forcing. NSC must come from a
     self-support/idempotence principle at the argmin, NOT chart moves.
   - **Amplifier (L3, banked):** record `B/δ ≈ 0.77764` with an ALGEBRAIC family-limit law; crossing 1:
     NO; cloning does not amplify; **B exceeds the literal (CI)-financed total and the G12 pivot-s
     budget ×4.24** — B needs its OWN δ-scale financing (orchestrator correction on the wave prompt's
     mis-specified "kill" criterion is recorded in the bundle README and wave header — read it).
   - Empirical NSC ratios on all certified data: `B/weighted-ν ∈ {≈1.14, 2.25, ≈2.79}` → K0 ≈ 3 would do.

**Adopted sequencing** (audit §7 + wave-13 outcome): wave 14 = NSC; the rest of the de-risk queue
(ex⟺kernel audit, arm E, refs ingest, probes, hygiene) remains open in bd.

## Next steps (ranked) — RESUME HERE

1. **Arm G wave 14: NSC(K0)** (bd: "fr arm G wave 14: NSC(K0) — prove ... or refute") — prove
   `B ≤ K0·Σ_carriers β⁺ν` via `P²=P` self-support at the argmin (the G6 warning applies: pointwise
   `ν_i ≥ const·a_s(i)⁻` is FALSE away from the argmin mechanism — NSC must genuinely use argmin
   structure), or refute via ν-starved carrier families. Stress instance = the 0.77764 record
   (`runs/2026-07-04-b-amplifier-hunt/`). Consider a cheap NSC-refuter decision-check FIRST (audit policy).
2. **Codify the wave-13 tools** (bd issue filed): `lem-negative-pivot-import` (proved-mod-audit,
   review-approved, equality form) + `conj-nsc` — fully-inline contracts; no af elevation until wave 14
   shows what the proof leans on.
3. **Adversarial codex audit: `conj-ex ⟺ conj-kernel` + HLC shard + finisher DAG wiring** (bd issue) —
   the campaign's justification is prose-only; same risk profile as the retired dual-localization.
4. **Arm E wave 1 (decision-check)** (bd issue): complementarity reformulation + Luo–Pang applicability +
   numeric uniformity probe on the instance zoo. Portfolio medicine: this is the second genuine arm.
5. **Refs ingest** (bd issue): pin Kitaev 2405.02434 + SBD 2405.01532 (staged in `refs-staging/`);
   verify the scouts' cb→∞-norm commutative reduction in-repo before anything cites it.
6. **SBD probes** (bd issues): reset-trick transfer; ex-hume vs SBD sharpness-family cross-check.
7. **Hygiene batch** (bd issue): chart-apparatus def-shards (L2 drift, af-facing), register (BN),
   `lem-dual-localization` kind fix. (The "46 results" HANDOFF error is fixed by this rewrite: 44.)
8. **Downstream re-audit thread** (bd issue): `thm-classical-factorization` JB identification (top
   mod-audit risk) — codex reviewer pass, independent of frontier work.
9. **Lab-book sections 14–15 (`aism-av0`)** still pending; extend to cover session-7 results when the
   report next builds.
10. **`aism-z98` (+C_δ·δ): DEFER until wave 14** — if NSC is proved, financing arrives at proof level
    (no contract change); if NSC weakens, the amendment is the fallback. Notes on the issue.

## Standing rules (see CLAUDE.md + bd memories; session-7 additions in bold)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af contracts;
pre-factor linear chains; node-cap 40; no argument//definitions edits while an orchestration runs;
numerics = exact-ℚ with orchestrator recomputation; waves = verbatim docs/waves/ artifacts, honest
T0–T3 tiers, fr log per pull, workers told no fr/bd; wave prompts/answers in the session scratchpad.
Audit policies: decision-check before narrowing wave; no ritual elevations; discount trivial-lemma
weight; watch reactive budget patches. **Session-7 additions: independent codex review BEFORE
codifying worker tools (reviewer ≠ author — G13 pattern works); orchestrator must recompute worker
headline certificates with INDEPENDENT code before banking any runs/ bundle; when a wave prompt
mis-specifies a criterion, correct it LOUDLY in the banked artifact (see the G13 amplifier README);
all literature enters as `stated` until byte-matched (L1) — the lit-sweep doc is the queue.**

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
fr verify proofs/<id>/export.md --oracle af-<id>   # 15 oracles registered
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>   # wave worker
# wave-13 harvest pattern (works): dispatch prover+amplifier codex in parallel -> orchestrator
#   recomputes with independent code -> bank runs/ bundle + verbatim docs/waves artifact ->
#   dispatch fresh codex REVIEWER before any codification -> fr log per pull.
# decision-check pattern: runs/2026-07-04-cross-pivot-kill-test/ (and the three session-7 bundles).
```

## What is intentionally NOT here

- Any claim that more than FIFTEEN results are rigorous (~6 substantive; the wave-13 tools are
  REVIEW-APPROVED PAPER-PROOFS, i.e. proved-mod-audit at best once codified — NOT af-validated).
- Any claim the B-lemma is proved — it is CONDITIONAL on NSC(K0), which is OPEN (wave 14).
- Any claim (EX)/Kernel/op-classical is closed — open inputs beyond NSC: (V)/(Ψ) branch charging,
  (SC) assembly, the fan-lift, the master decomposition, ex⟺kernel equivalence, rank ≥ 3
  generalization (decider #1 removed only the visible-break scenario), the inherited downstream
  re-audit, (BN), and the B-side sigma-cap.
- A skeleton kill from the amplifier's "(iii) YES" — mis-specified criterion, corrected in place; the
  true content is that B needs its own δ-scale financing.
- A naked `+C_δ·δ` term in `conj-sc`/`conj-rh` — deferred pending wave 14 (`aism-z98`).
- A git remote (local-only by decision) — session close = commits + bd close, no push.
