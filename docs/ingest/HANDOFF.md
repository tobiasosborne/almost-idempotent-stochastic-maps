<!--
ROLE: crash-safe handoff for the classical-portfolio sidequest (Agent A exploration lane).
Branch: agent-a/classical-portfolio. Rewritten at session close (2026-06-11, day-2 end).
-->

# HANDOFF — classical-portfolio sidequest (op-classical / op-exposed-hull)

> ## START HERE (next agent)
> 0. **Read FIRST: `OVERVIEW.md`** (this directory) — the bird's-eye onboarding map
>    (2026-06-11, twice-reviewed): plain-language conjectures, all definitions, the
>    full strategy map with statuses, the frontier, the do-not-retry list. It
>    supersedes this file's narrative below (which is the DAY-2 state; the dossier's
>    waves 14-23 sections carry what happened since: the variety programme, the
>    audited lemma chain, the broken local-law assembly, the Theorem-1.12 lead).
> 1. Branch **`agent-a/classical-portfolio`** (exploration lane; canonical layers via
>    Recipe A→B + reviewer ≠ author only — repo CLAUDE.md). NOW MERGED TO MAIN
>    (2026-06-11, user direction) — main carries this work.
> 2. **Then: `report/kernel-conjecture.tex`** — the precise statements (Kernel
>    Conjecture, the chain, the working forms with their cloning caveats) and the
>    evidence/constraints ledger.
> 3. Then: repo gate files → this file → **`notes/wave5-sigma-wall-parallel.md`**
>    (THE day-2 dossier: waves 5–13, read the FINAL sections first — they supersede
>    earlier ones) → `notes/swarm-answers/` (45+ archived worker verdicts, every died-at
>    in display math) → `report/` (the 49pp self-contained LaTeX report, v3, delivered).
> 4. Day-1 material: `ORCHESTRATION.md` + `notes/wave4/audit-summary.md` (audited
>    constants) + `notes/fable-hlc-attack.md`. Numerics: d1–d14 in `experiments/`.
> 5. Beads: `bd show aipm-3u6` (carries THE KERNEL) → `aipm-e9p` (Högnäs–Mukherjea:
>    ACQUIRED — refs/hognas-mukherjea-2011/ ingested, manifest lockstep done; the
>    real-proof AUTOPSY was in flight at handoff: check
>    `/tmp/codex-sigma-wall/w14_autopsy/answer.md` (volatile!) — if present, archive to
>    `notes/swarm-answers/w14_autopsy.md` and synthesize into the dossier; if absent,
>    relaunch from the brief pattern in the worklog 2026-06-11(cont.) entry) →
>    `aipm-e71` (HLC) → epic `aipm-and`. Report bead `aipm-sjw` done.

> ## FRONTIER 2026-06-13 (CURRENT — supersedes everything below; full trail in notes/swarm-answers/w25..w42)
> **THE OPEN KERNEL IS NOW (EX)** (after 18 further waves, w25–w42, each archived):
>   every row-stochastic idempotent P with δ(P) ≤ 1/4 has an actual-row basis U with
>   Vol(U) ≥ (1/2)·Vol_max(P) such that max_s Φ_s(U) ≤ C₀·δ(P)
> (Φ_s = Σ_j (β_s)₊E_s(j), the weighted signed-face excess in U's chart; all notation in
> report/kernel-conjecture v2 — w43 doc, and the swarm-answer headers).
> **PROVED MACHINERY (statuses honest):** (P1) pointwise E ≤ σ + 2(−λ)₊ (2-family);
> FACTORIZATION S*_s ≤ 2Φ_s + 6δ — class-wide, constants tight (codex w41 + opus w42, both
> 0.99) ⇒ (EX) with C₀ composes to the registry SF contract with C_sf = 2C₀+6 ⇒
> w35_quantifier chain (θ=1/2, A=2, one routing caveat) ⇒ global W-free O(√δ) ⇒ op-classical.
> **RANK-2 THEOREM PROVED** (w40: every Φ-argmin chart has S* ≤ 2δ; max-diameter mechanism;
> codex-only — opus pass = bead filed). **θ = 1/2 IS MANDATORY** (w36_audit B6 perturbed
> staircase refutes exact-tie selection). **SELECTION IRREDUCIBLE** (w37_opus: pointwise/
> σ-only/single-swap each refuted exactly). **(EX) EVIDENCE:** rank 3 = 278 exact instances,
> 53 adversarial, worst min-chart ratio EXACTLY 1 (C₀ = 1 empirical); blow-ups exist only at
> δ = 1/2 (staircase, ratio = m) — δ₀ ≤ 1/4 is comfortable. **DEAD ROUTES** (do not retry):
> coefficient-only LP; universal C ≤ 2; exists-exact-max-volume; pointwise ME; σ-only;
> single-swap; Jensen/convexity (w33 §6); (SIG) without overshoot (w38 refutation, repaired w39).
> **LIVE MECHANISM for (EX) at rank ≥ 3:** the two-horn multi-row swap dichotomy
> (volume-permitted ⇒ minimality bites / near-degenerate ⇒ (NDG)) + the rank-2 template.
> **CONSOLIDATION IN FLIGHT (w43):** kernel-conjecture v2 (the (EX) interface document) being
> drafted; banking beads filed (rank-2 opus audit; Recipe A→B of the belt). Worklog
> 2026-06-12/13 entries carry the day-by-day. BRANCH: work lives on **main** (user direction).
> ACQUISITIONS: 7/8 wave-18 refs staged in refs-staging/ (manifest lockstep PENDING);
> Chakraborty–Mukherjea Contemp. Math. 516 needs a manual TIB browser download.
> TOOLING: gurobi OK outside the codex sandbox only; wolframscript flaky-first-call; network
> intermittent — interruption-resilience protocol in ORCHESTRATION.md is in force.

## THE KERNEL (superseded 2026-06-12, see UPDATE above — kept for the w5–w13 record)
**Path-product floor:** for the band component C of any hidden top vertex with σ̃ > τ,
  Π_C ≳ τ − O(Lδ)  (thin-chain exclusion).
- TRUE ⇒ component finisher (PROVED, w12) + s8 branch (PROVED) ⇒ **LINEAR LAW δ ≥ cH**
  ⇒ HLC ⇒ op-exposed-hull ⇒ op-classical. Every other link proved or proved-mod-audit.
- FALSE ⇒ first-ever H ≫ δ instance (two refuters failed to build one; quantified
  failure maps archived).
- Empirics: the ENTIRE record (67k+ instances, d8–d14) fits δ ≥ ~H/2; the √δ "flat
  floor" was a corner extrapolation (d13, high strength).

## Landmark results of day 2 (all in the dossier, statuses per its tags)
- **Corner theorem** (2-family): τ* = 2−√3, wall H/τ = 2(2−√3) = 0.53590, floor
  δ/H² = (7+4√3)/4 = 3.48205 — finite-δ corner, NOT asymptotic.
- **σ̃-height-collapse** (proved): σ̃ ≤ s ⇒ H ≤ δΩ/(1−s); contrapositive σ̃ ≥ 1 − δΩ/H.
- **s8 branch** (proved): σ̃ ≤ τ ⇒ H ≤ 3τ ⇒ δ ≥ H²/9 (HLC direct there).
- **t10 Birkhoff finisher** (proved): bounded projective diameter + ε-idempotence ⇒
  row collapse (no spectral gap); **w12 component finisher** (proved): fat components
  collapse-and-expose; survivor = thin chains.
- **d14**: positive kernel closes exactly (λ⁺ = 0); only v's δ-budget negatives cross.
- **Refuted/downgraded:** literal ψ-gap (×2, conditioned variant proved instead);
  literal T_far = ∅; NG′; the linear financier law's scale claim; d12's broad verdict.
- **s5**: exact all-shallow optimal face EXISTS (low height only — σ̃ < τ).
- **Wave-10 meta-theorem:** "hiddenness IS the LP frame" (5 strategy kinds collapsed);
  canonical W-free statement = B–S normal-form distance (audited: target, not route).
- **Source discovery:** Baake–Sumner cite Högnäs–Mukherjea WITHOUT proof — the δ=0
  anchor needs its own byte-pin (bead filed; TIB).

## NEXT (priority order)
1. **Harvest the H–M real-proof autopsy** (launched 2026-06-11; see START-HERE item 5 —
   archive or relaunch). DONE already: acquisition + ingestion + manifest lockstep
   (`refs/hognas-mukherjea-2011/`, §2.2 is the structure theorem; provenance is
   extraction-level — byte-quote against the .txt). The autopsy's SIGN-ROBUST/SIGN-RIGID
   step table is the input for the next proof wave: the campaign's perturbation is
   "exactness free, only positivity perturbed" — sharper than generic almost-idempotence.
2. **Chain-specialized SOS/certificate search** (small n, the REDUCED thin-chain
   inequality — distinct from wave-10's collapsed full-problem SOS).
3. If both stall: **the honest-stall write-up is PRD-sanctioned and ~95% done** —
   report v3 (delivered) + kernel-conjecture.tex (the distilled interface) + the
   dossier's FINAL STATE section = the obstruction map; then Recipe A→B banking of the
   proved belt on main (large: batch as registry shards + af workspaces; the af
   follow-on phase per the done-bar).
4. Periodic-component patch for the w12 finisher (its declared primitivity gap —
   refuter #2's dichotomy suggests it's benign; prove it).
5. Discharge the kernel-conjecture.tex §5 anchor caveat once H–M loci are pinned
   (update the document's item 5 and recompile).

## Protocol (hard-won; LLM-LEARNINGS.md + memory)
- Codex swarms liberal (user standing order); opus serial; fable per-approval with
  the file-protocol MANDATORY. Briefs: progress-protocol, verdict-first, died-at in
  display math, calibrated P's, anti-collapse rule for strategy diversity.
- Watchdogs on every detached fleet; archive every answer into notes/swarm-answers/
  IMMEDIATELY (tmp is volatile); harvest file updated per landing, committed per wave.
- All numerics: presolve OFF, multiplicity-correct vertices (d3_vertexfix), honest
  τ = √δ from the instance's own δ. Violations fabricate structure.

## Hygiene
- `agent-A/lean-formalisation-coverage.md` working-tree mod predates the sidequest — leave.
- `CODEX_DELEGATION.md` (repo root) untracked, user-owned — leave.
- Report PDF is gitignored; rebuild via `cd report && latexmk -pdf main.tex`.
- `bd export -o .beads/issues.jsonl` before committing issue changes; full check-all
  (incl. latexmk) runs on every commit — let it.
