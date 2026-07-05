<!--
ROLE: current state + START HERE + ranked next steps. The always-"now" file.
UPDATE POLICY: REWRITTEN (not appended) at each session close; keep ≤500 lines. Narrative history goes in
  docs/worklog.md (append-only); this file is always "now".
TRIGGER: session close, or a material change in the current frontier / next task.
-->

# HANDOFF — almost-idempotent-stochastic-maps

## START HERE

1. Read `PRD.md` (REDRAWN 2026-07-05: Kernel is THE theorem-facing input; (EX) is a separate
   attack route — the two are NOT equivalent), then `CLAUDE.md` (== `AGENTS.md`).
2. Read **`docs/plans/2026-07-05-top-down-proof-sketch-v2.md`** — the canonical strategic map
   (v1 superseded in place; banked artifacts cite v1 line numbers). Every wave names its node
   there. The OPEN LEDGER + UNSCOPED-SURFACE list at its end IS the progress metric.
3. **THE PHASE DISCIPLINE (user, 2026-07-05, binding): no progress theatre.** We work top-down,
   breadth-first; the deliverable is a fully scoped workable proof. Progress = unscoped/unpriced
   surface shrinking — never commit/seeding/elevation counts. Trivial elevations are bookkeeping,
   reported as such. (bd memory `bfs-phase-discipline`; agent memory `no-progress-theatre`.)
4. Run `fr board` and `bd ready`. Newest wave artifacts: `docs/waves/2026-07-05-*` (DC1-DC4, W15,
   W16, W16b, W17, W17b); newest bundles: `runs/2026-07-05-*` (5). `FINDINGS.md` has the
   2026-07-05 entries (two death certificates + the census lesson).
5. Gate: `sh scripts/check-all.sh` → `[check-all] OK`.

## Current state (2026-07-05, session 8 CLOSE) — sketch v2 rules; 16 af-validated

**Rigorous (af-validated, T0): 16** (`argument/INDEX.md`) — session 8 added `lem-import-reduction`
(10-node run 1 clean; bookkeeping-grade content, discount accordingly). Honesty note stands
(~6 substantive).

**Session 8 in one paragraph.** User redirected to breadth-first scoping of the full proof. Four
decision-checks (DC1-4) + five waves (W15/16/16b/17/17b) + a 4-lane recon rewrote the map: the
prose-only `conj-ex ⟺ conj-kernel` equivalence has NO proof in either direction (DC4) — PRD +
shards redrawn (user decision) with **Kernel as the theorem-facing input** and (EX) an attack
route with the explicit open edge ⟨3⟩3; **broad `conj-nsc` DISPROVED** (DC2, zero-denominator
certificate: a B-carrier can be entrywise nonnegative at a certified argmin) and
**`conj-gamma-emptiness` DISPROVED** (W15: the FIRST certified capped clean Γ-block — G11's
0/352 was search coverage; the refuting row is high-self) — both orchestrator-independently
recomputed, both leaving sharper certified-nonvacuous successors; the K3 horn is now exactly
**`conj-b-restricted`** (`B ≤ K·δ` at clean-block argmins; hypothesis class NONEMPTY, K ≥ 0.7708
forced; W15 residual closes the branch with K_G = 17K+20); the K⟨1⟩6 additive master formula is
RED as written (DC3: FanRes realized>0 but absent; silent rows tribeless; SC-in-RH nesting);
DC1 supports fusing the fan/orphan/self-support budgets into ONE horn (K2). W17 priced ⟨3⟩3:
D5 (weight transport P_vj → P_{u_s j}) is the wall, possibly Kernel-sized. W17b census (514
instances): NO hidden top with σ_g > 1/2 realized (max 1/25) — with W17's D1 reduction
(**constant cap σ_g ≤ 1/2 ⇒ Kernel with B = 29/8** via the af-validated halo-collapse), Route A
has ≥12× empirical slack. W16/16b: clean-block B/δ walls at 0.77764 (same as unconstrained);
direct-FE route fragile (floor collapsed to 23/1000; α→1 continuation = kill/rescue). Also: the
Idempotent Atlas artifact published (interactive proof explainer,
https://claude.ai/code/artifact/1ac53413-23d8-4ec5-99ab-1a3afd05924e).

**Registry deltas:** + `lem-negative-pivot-import` (proved-mod-audit, review-approved c<0 tool);
+ `conj-nsc` (disproved), + `conj-gamma-emptiness` (disproved), + `conj-b-restricted` (conjecture,
THE K3 link); `conj-ex`/`conj-kernel` contracts/bodies redrawn; 10 sketch-node af workspaces
seeded (seed-only; orchestration only on paper-proved nodes, one at a time).

## Next steps (ranked by today's evidence) — RESUME HERE

1. **Route-A wall re-read (top item).** Do the B4 death certificates (exposedness-absorption
   kill, one-sided-ledger walls) even BIND the CONSTANT cap `σ_g ≤ 1/2` for hidden top vertices
   at δ ≤ 1/4? They were built against the tighter `σ_g ≤ 1 − c·τ` and a specific mechanism. D1
   (W17, worker T1 — re-derive before leaning on it): constant cap ⇒ Kernel with B = 29/8 via the
   validated halo-collapse. Census slack ≥12× (max realized σ_g = 1/25; upstream ~25k census
   σ_g ≲ 0.37τ). A scoping wave: re-read the wall records against the constant-cap target +
   check whether the new import toolkit (c<0 tool, cross-pivot ledger — both postdate the walls)
   gives a mechanism. THIS is the shortest currently-visible path to the whole theorem.
2. **σ_g > 1/2 exact-feasibility attack** (W17b's named follow-up): branch-and-bound
   realizability instead of family search; diagnostic banked ("high self-mass makes rows visible
   or stays in-halo"). Either a realization (stress for #1) or structured non-realization insight.
3. **α→1 continuation** (W16b residual): kills or rescues the direct-FE route for
   `conj-b-restricted`. Follow-up waves MUST emit full matrices for headline points (W16b bundle
   limitation, noted in its README).
4. **K2 unified financing horn** (the fused (RSI)+(FIN)+(RH) statement — DC1 evidence supports
   ONE budget) + **K4 nesting-aware assembly shard** (DC3's proposed restatement; needs the
   FanRes = O(δ) lemma + silent-row exhaustiveness).
5. Standing queue: refs ingest (Kitaev + SBD, `aism-5de`); arm E decision-check (`aism-78w`);
   trunk ⟨2⟩5 Kernel⇒HLC transcription + ⟨2⟩6/⟨2⟩7 re-audit (`aism-pu0` remaining half — HLC
   shard + DAG wiring, now against the v2 redraw); rank-4 Γ/c<0 decider extension; report
   sections 14-15 (`aism-av0`; four anchor warnings pending: conj-nsc, conj-gamma-emptiness,
   conj-b-restricted, lem-negative-pivot-import).

## Standing rules (see CLAUDE.md + bd memories; session-8 additions in bold)

Codex workers only (no Fable subagents); ONE af orchestration at a time; single-minimal af
contracts; no argument//definitions edits while an orchestration runs; numerics = exact-ℚ with
orchestrator recomputation; waves = verbatim docs/waves/ artifacts, honest tiers, fr log per
pull, workers told no fr/bd; wave prompts/answers in the session scratchpad; independent codex
review before codifying worker tools; correct mis-specified wave criteria LOUDLY in the banked
artifact; literature enters as `stated` until byte-matched. **Session-8 additions: (i) the
no-theatre/BFS discipline (START-HERE #3); (ii) bounded prove-or-refute waves on freshly codified
conjectures work — two wrong shapes killed within hours each, at one wave each; keep contracts
falsifiable and data-grippable (certified-nonempty hypothesis classes); (iii) orchestrator
INDEPENDENTLY recomputes every status-changing certificate from the matrices alone (DC2/W15
standard) — and requires workers to emit full matrices for headline points; (iv) a failed search
census is NEVER emptiness evidence (W15 vs G11's 0/352); (v) never charge B-mass to carrier
row-negativity (DC2), never argue the Γ-branch away (W15).**

## Recipes

```bash
sh scripts/check-all.sh
python3 scripts/seed-af-workspaces.py <id>       # then COMMIT before orchestrating
python3 scripts/af-orchestrate.py <id> --workers 8 --max-rounds 14 --node-cap 40   # background
fr verify <claim> --oracle <name>                # 18 oracles registered (+2 refuter oracles)
codex exec --skip-git-repo-check -C <repo> -s workspace-write -o <answer> - < <prompt>
# session-8 wave pattern (works): codify falsifiable contract -> bounded codex prove-or-refute
#   wave -> orchestrator-independent recomputation (matrices only) -> bank runs/ + verbatim wave
#   doc -> flip status honestly -> successor fires per the recorded fallback -> fr log.
```

## What is intentionally NOT here

- Any claim more than SIXTEEN results are rigorous (~6 substantive; wave-13/15/16/17 worker T1
  proofs are worker-attributed paper arguments, NOT af-validated).
- Any claim `conj-b-restricted` is true (0.77764 wall + nonempty class = evidence only) or that
  the direct-FE route works (floor 23/1000, α→1 open).
- Any claim Route A is unblocked (the wall re-read has NOT been done — it is next session's job);
  D1's constant-cap reduction is a worker T1 derivation, not yet independently re-derived.
- Any (EX)⇒Kernel edge (D5 weight-transport wall; possibly Kernel-sized; door regime unrealized).
- Any emptiness claim from the W17b census (evidence-of-absence only).
- A git remote (local-only by decision) — session close = commits + bd close, no push.
