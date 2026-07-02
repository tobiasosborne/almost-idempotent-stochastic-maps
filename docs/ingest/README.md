<!--
ROLE: ingest manifest + honest re-tag map for the inherited classical-portfolio campaign record.
This directory is READ-MOSTLY and is NEVER cited as rigorous (repo CLAUDE.md L0/L1).
Nothing here is re-established under this repo's discipline until it re-enters argument/ with its own status.
-->

# `docs/ingest/` — the inherited **classical-portfolio** campaign record (object of re-establishment)

## (a) What this directory is

This is a curated, byte-for-byte **ingest** of the `classical-portfolio` exploration from the upstream
repo, copied verbatim from the absolute source path

```
/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/
```

It is the **campaign record** that reduced the OPEN classical stability problem `op-classical`, through a
mix of audited and *mod-audit* steps, to a single open **Kernel / (EX) conjecture**. It is the **object of
re-establishment** for this repo — a *starting point, not an oracle*. Per this repo's `CLAUDE.md`
**L0/L1**: everything here is **read-mostly** and **NEVER cited as rigorous**. A claim that appears in this
ingest is at best `stated` / `proved-mod-audit` / `conjecture` / `numerical`; it becomes rigorous in *this*
repo only when it re-enters `argument/` and clears an independent reviewer, an `af`-validated tree, a
byte-matched `refs/` source, or a Lean proof (L0/L5). Anything **not** copied below still lives at the
absolute source path above (and, where noted, in the upstream **main repo**
`/home/tobias/Projects/almost-idempotent-positive-maps/`). Do not paraphrase from memory — go read the
source.

---

## (b) MANIFEST — copied vs. deliberately skipped

### Copied into `docs/ingest/` (relative structure preserved)

| path in `docs/ingest/` | source (relative to the classical-portfolio source dir unless noted) | approx size |
|---|---|---|
| `OVERVIEW.md` | `OVERVIEW.md` | 24K |
| `HANDOFF.md` | `HANDOFF.md` | 12K |
| `ORCHESTRATION.md` | `ORCHESTRATION.md` | 20K |
| `LLM-LEARNINGS.md` | `LLM-LEARNINGS.md` | 8K |
| `report/kernel-conjecture.tex` + `.pdf` | `report/kernel-conjecture.{tex,pdf}` | 24K + 392K |
| `report/kernel-conjecture-v2.tex` + `.pdf` | **UPSTREAM MAIN REPO** `../../report/kernel-conjecture-v2.{tex,pdf}` — **NOT in the classical-portfolio source** (see gap (i)) | 24K + 392K |
| `report/main.tex` + `.pdf` | `report/main.{tex,pdf}` | 8K + 688K |
| `report/sections/*.tex` (13 shards `00`–`11`, `99`) | `report/sections/*.tex` | 168K |
| `report/STATUS-LEDGER.md` | `report/STATUS-LEDGER.md` | 28K |
| `report/NOTATION.md`, `report/PLAN.md`, `report/REVISION-BRIEF.md` | same | 16K + 16K + 4K |
| `report/reviews/{overclaim-audit,readability-review}.md` | `report/reviews/*.md` | 16K |
| `experiments/DELIVERABLE{1,2,3}_*.md` | `experiments/DELIVERABLE{1,2,3}_*.md` | 3×8K |
| `experiments/asq_*.py` (13 scripts) | `experiments/asq_*.py` | ~64K |
| `experiments/d*.py` (43 scripts, `d1`–`d14`) | `experiments/d*.py` | ~500K |
| `experiments/out/w40_ndg/` (rank-2 (NDG) + Part-A) | `experiments/out/w40_ndg/` | 56K |
| `experiments/out/w41_ex/` (rank-3 (EX) enumeration) | `experiments/out/w41_ex/` | 812K |
| `experiments/out/w42_factor_audit/` (factorization audit) | `experiments/out/w42_factor_audit/` | 68K (`__pycache__` dropped) |
| `experiments/out/w43_kernel_doc/` (kernel-doc closeout) | `experiments/out/w43_kernel_doc/` | 12K |
| **total** | | **≈ 3.4M** |

Notes on the copy:
- **LaTeX build artifacts skipped** under `report/` (`*.aux *.log *.out *.toc *.fls *.fdb_latexmk build*.log`,
  ≈ 300K of regenerable junk); only sources + compiled PDFs were taken. Re-`make` from source if needed.
- No `out/` result dir exceeded the 20 MB blob threshold, so **all four were copied in full** (largest single
  file: `w41_ex/rank3_results.json`, 772K). Nothing was truncated; **no big-blob skip occurred.**
- The four `out/` dirs are the ones that reproduce the headline evidence: `w40_ndg`/`w41_ex` carry the
  **(NDG)/(EX) rank-2/rank-3 enumeration**, and the seed `d*.py` + `asq_*.py` scripts + the campaign
  `HANDOFF.md`/`OVERVIEW.md` point at the **67k-instance record** (whose bulk JSON lives in the un-copied
  `out/d*` and `notes/` trees — pointer below).

### Deliberately NOT copied (left at the absolute source path; go there to read)

| skipped | why | pointer |
|---|---|---|
| `notes/swarm-answers/` | bulk swarm-worker archive | `…/classical-portfolio/notes/swarm-answers/` |
| `notes/wave1 … wave5*, wave8*` | wave dumps | `…/classical-portfolio/notes/wave*` |
| ~110 `notes/*.md` worker notes (`d0`–`d14`, `fable-*`, `mrp-*`, `literature-sweep-*`, `endgame-*`, …) | per-worker lab notes; the STATUS-LEDGER already distils them | `…/classical-portfolio/notes/*.md` |
| `notes/briefs/` | dispatch briefs | `…/classical-portfolio/notes/briefs/` |
| `experiments/out/` **except** the four `w4x` dirs (≈ 50 other result dirs + loose `d*.json/.npy/.log`) | bulk numerical outputs (incl. the raw 67k-instance JSON, `d14_leakage.json` 629K, etc.) | `…/classical-portfolio/experiments/out/` |
| `experiments/__pycache__`, `experiments/test_lp_robustness.py`, `experiments/w8_witness_check.py` | non-headline helpers | `…/classical-portfolio/experiments/` |
| `report/*.aux/.log/.fls/.fdb_latexmk/.out/.toc`, `build*.log` | regenerable LaTeX artifacts | `…/classical-portfolio/report/` |

---

## (c) THE HONEST RE-TAG TABLE (the single most important deliverable)

**Re-tag mapping to this repo's L0 rigour rungs.** Upstream statuses are quoted **verbatim** from
`report/STATUS-LEDGER.md`, the three `experiments/DELIVERABLE*.md`, and the upstream **argument registry**
(`…/almost-idempotent-positive-maps/argument/INDEX.md`, which tags the reduction-chain theorems `proved`
with an `af` column). Nothing is upgraded.

- upstream `PROVED-mod-audit` → **`proved-mod-audit`**
- upstream `NUMERICAL` → **`numerical`**  *(L3 — evidence, never proof)*
- upstream `CONJECTURAL` → **`conjecture`**
- upstream `OPEN` → **`open`**
- upstream `REFUTED` → **`disproved`**
- upstream plain `PROVED` (registry `proved` / ledger "prose proof exists") → **`proved-mod-audit`**
  *(a paper-proof that has NOT cleared a reviewer/`af`/Lean pass **here** — L0)*
- upstream `RETRACTED/DOWNGRADED` → **`disproved`** *(the stronger reading is withdrawn; carry only as a
  caution — any narrowed survivor re-enters at its own, weaker rung)*
- upstream `DEAD ROUTE` → **`disproved` / dead-route** *(recorded death certificate; do NOT re-walk — Rule 13 / `FINDINGS.md`)*
- upstream `OPEN / NUMERICAL` → **`open`** *(numerically supported; still not proved)*
- upstream `CITED-background` / `LITERATURE-SWEEP` / `TO-ACQUIRE` → **`stated`** *(unchecked until byte-matched to `refs/` — L1)*
- **special case — `lem-classical-equiv`:** it was **`af`-VALIDATED upstream** (upstream `proved / af: validated`), but per the ingest discipline it **RE-ENTERS here as `proved-mod-audit` until re-validated under this repo's own `af`/reviewer protocol.** Nothing is rigorous in this repo until re-established here.

### Table 1 — CORE reduction chain + named argument-registry results (seed the `argument/` DAG from this)

| id | one-line statement | upstream status (verbatim) | HONEST re-tag here |
|---|---|---|---|
| `op-classical` | ∃ universal `η₀,C>0` (n-free): every row-stochastic `Q` with `‖Q²−Q‖≤η≤η₀` is within `C√η` of a stochastic idempotent (sharp exponent ½). | `OPEN` (ledger) / registry `open, af:none` | **open** |
| `op-exposed-hull` | Global exposed-hull lemma: with `ρ=C√δ`, `W_{ρ,κ}` (`κ=c√δ`), every row is within `C√δ` of `conv W_{ρ,κ}`; implies `op-classical` via `thm-classical-factorization`. | `OPEN` (ledger) / registry `open, af:none` | **open** |
| **Kernel Conjecture** (`conj:kernel` ≡ HLC) | ∃ universal `δ₀,B`: for exact signed idempotent `P` with `δ≤δ₀`, `W(P)≠∅` and every hidden vertex `v` with `σ̃_v>τ=√δ` has `dist(p_v, conv{p_w:w∈W}) ≤ Bτ` (⇔ `δ ≥ H²/C₁²`). | `CONJECTURAL` (v2 doc: "evidence only, not a proof"); HLC in ledger = `OPEN` (numerically supported) | **conjecture** |
| **(EX) conjecture** (v2 kernel) | ∃ universal `C₀<∞`: every exact signed row-stochastic idempotent `P` with `δ(P)≤¼` has an actual-row basis `U∈M_{1/2}(P)` with `max_s Φ_s(U) ≤ C₀·δ(P)` (empirical `C₀=1`). | `CONJECTURAL / OPEN` — v2: audit "explicitly leaves (EX) open"; `C₀=1` is "evidence only, not a proof" | **conjecture** |
| `lem-classical-equiv` | Signed-idempotent ⇔ stochastic-idempotent formulations equivalent up to universal constants. | ledger `PROVED` / registry `proved, **af: validated**` | **proved-mod-audit** *(af-validated upstream; re-enters mod-audit until re-validated here)* |
| `thm-cluster` | `P` with pairwise-separated `(ρ,κ)`-exposed representatives + off-cluster rows within `γ` ⇒ ∃ stochastic idempotent `E` within `C(ρ+γ+δ/κ+δ)`; C free of m,n,#transient. | ledger `PROVED` / registry `proved, af:none` | **proved-mod-audit** |
| `thm-classical-factorization` | `Q` with `‖Q²−Q‖≤η₀` + `thm-cluster` geometry ⇒ ∃ commutative special JB-algebra `J`, unital positive `Δ,Υ` with `ΥΔ=id`, `‖ΔΥ−Q‖≤C√η`, `Υ(Δx·Δy)=x∗y`. | registry `proved, af:none` | **proved-mod-audit** |
| `thm-simplex` | Signed affine retraction `P` (`δ≤δ₀`) whose row polytope is dim ≤1 or a simplex with vertices among rows ⇒ ∃ stochastic idempotent `E` within `C√δ`; C free of m,n. | registry `proved, af:none` | **proved-mod-audit** |
| `thm-rank-one` | Every rank-one signed affine retraction `P=I−uvᵀ` (`Σvⱼ=0, vᵀu=1`, `δ≤δ₀`) is within `C√δ` of a stochastic idempotent; contains Hume's sharp family (`ex-hume`). | registry `proved, af:none` | **proved-mod-audit** |
| `thm-well-exposed` | `P` (`δ≤δ₀`) with every vertex pairwise-separated & `(ρ,κ)`-exposed (`ρ≤C√δ, κ≥c√δ`) ⇒ vertices affinely independent (K a simplex), `thm-simplex` gives `E` within `C√δ`. | registry `proved, af:none` | **proved-mod-audit** |
| `prop-approx-simplex` | Rows with `γ`-approximate simplex coordinates (`λ_a` nonneg. or `O(δ)` coeff neg mass) ⇒ ∃ stochastic idempotent `E` within `C(√δ+γ)`; reduces `op-classical` to producing `γ=O(√δ)` coords. | registry `proved, af:none` | **proved-mod-audit** |
| `lem-exposed-circuit` | For signed affine retraction (`δ`): (i) a `(ρ,κ)`-exposed vertex concentrates `‖v−π_v‖≤C(δ/κ+δ)`; (ii) separated exposed vertices satisfy `‖Σc_a v_a‖ ≥ (1−C(δ/κ+δ))Σ|c_a|`; both `1−O(√δ)` when `κ≥c√δ`. | registry `proved, af:none` | **proved-mod-audit** |
| `lem-leakage` | Affine-face leakage: `Q` (`‖Q²−Q‖≤η`), affine `h`, `d_i=m−h(q_i)` ⇒ `q_i({j:h≤m−γ}) ≤ (d_i+η)/γ`; a maximiser leaks ≤ `√η` below level `m−√η`; no `O(η)` closure. | registry `proved, af:none` | **proved-mod-audit** |
| `ex-hume` (sharpness obstruction) | Explicit 3×3 family `P_s=I−u_s v_sᵀ` with `δ=s²` and distance `2√δ+O(δ)` to every stochastic idempotent ⇒ no exponent `β>½` holds; exponent ½ in `op-classical` is sharp. | registry `proved, af:none` | **proved-mod-audit** |
| **factorization lemma (F)** `S*≤2Φ+6δ` | For every `θ=½` chart `U`, pivot `s`: `S*_s(U) ≤ 2Φ_s(U) + 6δ(P)`; constants `(2,6)` tight, class-wide, no hidden `δ≤¼` dependence. | v2 doc: **"PROVED and audited"** | **proved-mod-audit** |
| **corner-constants theorem** (corner closed forms) | For the measured family: `τ_*=2−√3`, wall `2(2−√3)`, floor `(7+4√3)/4`. | ledger **`PROVED-mod-audit + NUMERICAL`** (algebra confirmed; `t*` optimality/family-equality numerical) | **proved-mod-audit** *(optimality/family-equality part `numerical`)* |
| `lem-dual-localization` | Frame-free residual: for a skinny mutual-shadow pair (`μ→1`) each failing `(ρ,κ)`-exposedness, force `‖Ēbar‖₁ ≥ H` from `P²=P` (not from convex weights). The one inequality blocking the transferable (ASQ) proof. | `OPEN` (DELIVERABLE2/3: "genuine gap", "SURVIVES … sharpened to one inequality") | **open** |
| (ASQ) / `lem-asq-frame` (k=2 anchored cost) | `dist₁(row, conv W) ≤ 2·max-neg`, giving `‖P‖_{∞→∞} ≥ 1+cH²`; PROVED **only in the canonical simplex frame** `R=[I_r|0]` via `lem-bary-dist-neg → lem-archetypes-in-W → lem-asq-frame`. | DELIVERABLE2/3: **"PROVED in the canonical simplex frame … NOT PROVED transferably"** | **proved-mod-audit** *(frame-specific only; general case = `lem-dual-localization`, open)* |
| `lem-bary-dist-neg` | Exact identity: `dist₁(λ,Δ) = 2·neg(λ)` for any barycentric `λ` (Σλ=1). | DELIVERABLE2: `PROVED, exact` | **proved-mod-audit** |
| Deliverable-1 n=4 2\|2 circuit dichotomy | rank-3 `P=I−uvᵀ` genuine-quadrilateral: either `min(a,b,c,d)≥kτ` (all four vertices well-exposed) or a controlling coeff `<kτ` and that vertex collapses to the opposite edge (`(b/a)D`). | DELIVERABLE1: **"VERDICT: the dichotomy is correct as stated"** (structure symbolic, margins/collapse numeric) — a *lower-bound* certificate (clarif. G1) | **proved-mod-audit** *(margins/collapse constants `numerical`)* |

### Table 2 — full STATUS-LEDGER re-tag (sections A–H, verbatim statuses)

#### A. Main chain and terminal residual
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| `op-exposed-hull ⇐ HLC` (if HLC `δ≥aH²`, exposed-hull follows, `C'=max(4A,1/√a)`) | `PROVED-mod-audit` | proved-mod-audit |
| `HLC` (hidden localization `δ≥aH²`) | `OPEN` | open (numerically supported) |
| `HLC ⇐ historical σ_v-wall` | `PROVED-mod-audit` | proved-mod-audit |
| historical Branch A (`H≤B_A σ τ`) | `OPEN / NUMERICAL` | open (numerically supported) |
| historical Branch B (`B_B≈0.536`) | `OPEN / NUMERICAL` | open (numerically supported) |
| `σ_v` branch variable (overloaded; use `σ_v^{off}` vs `σ̃_v`) | `RETRACTED/DOWNGRADED` | disproved (notation retracted) |
| existential DMF ⇒ HLC | `PROVED-mod-audit` | proved-mod-audit |
| `DMF` (deep-witness mass forcing) | `OPEN` | open (numerically supported in corner/budget; web case open) |
| quantitative Baake–Sumner web stability | `OPEN` | open |

#### B. Day-1 audited belt
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| L1 lone-far-row (margin `ρ/(2+4δ)`) | `PROVED` | proved-mod-audit |
| L2 far/high row to vertex | `PROVED` | proved-mod-audit |
| L2′ ρ-shadow | `PROVED-mod-audit` (recursion gapped/vacuous at scale) | proved-mod-audit |
| C10 failed-exposedness dual (α mass uncontrolled) | `PROVED` | proved-mod-audit |
| L4 frame-clipping | `PROVED` | proved-mod-audit |
| L5′ leakage at global maximizer (general-row version false) | `PROVED-mod-audit` | proved-mod-audit |
| L6 identity-frame linear bound (`δ≥H/2`; metric transfer open) | `PROVED-mod-audit` | proved-mod-audit |
| N1 nilpotent-chain off-chain forcing | `PROVED` | proved-mod-audit |
| F1 skinny near-coincidence | `PROVED` | proved-mod-audit |
| X1 one-mode wall | `PROVED` | proved-mod-audit |
| X2 stochastic-complement rank preservation | `PROVED` | proved-mod-audit |
| F-SS sharp shadow | `PROVED` | proved-mod-audit |
| F-ND near-delta exposure | `PROVED` | proved-mod-audit |
| F-E kernel energy | `PROVED` | proved-mod-audit |
| F-GB g-budget | `PROVED` | proved-mod-audit |
| F-WR wiggle rigidity | `PROVED-mod-audit` (side conditions; web-radius bound needed) | proved-mod-audit |
| F-BC blocker cap | `PROVED` | proved-mod-audit |
| F-2R private two-shell collapse | `PROVED-mod-audit` (private-site case) | proved-mod-audit |
| original F-psi | `RETRACTED/DOWNGRADED` | disproved (literal gap refuted) |
| PC private-cluster exposure | `PROVED-mod-audit / DOWNGRADED` (α loophole; not a closed theorem) | proved-mod-audit (downgraded) |
| RC energy endgame | `OPEN` | open |
| MRP day-1 residual | `OPEN at day 1; later NUMERICAL-safe` | open (later numerically safe) |

#### C. Wave-5 to Wave-7 harvest
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| supplier-deficit lower bound | `OPEN` | open |
| top-slab/top-band localization | `OPEN` | open |
| C10-exchange | `PROVED` | proved-mod-audit |
| self-starvation | `PROVED-mod-audit` (needs banking if used) | proved-mod-audit |
| height-energy anti-lemma (canonical-`g` energy can't prove Branch A) | `PROVED / dead-route` | proved-mod-audit (negative result / dead route) |
| literal psi-gap | `REFUTED` | disproved |
| canonical-W conditioned F-psi | `PROVED-mod-audit` | proved-mod-audit |
| financing-row no-gain | `PROVED / dead-route` | proved-mod-audit (dead route) |
| positive-carrier sharp shadow | `PROVED-mod-audit` | proved-mod-audit |
| carrier-blocker coupling | `OPEN / CONJECTURAL` | conjecture (open; d11 numerical support) |
| reciprocal-carrier lemma | `OPEN / CONJECTURAL` | conjecture (open; partly artifact) |
| column-carrier propagation | `PROVED-mod-audit` (gauge warning) | proved-mod-audit |
| raw `RΛ=I` argument | `REFUTED / dead-route` | disproved (gauge; dead route) |
| binding-height identity (= LP slackness, not exactness) | `RETRACTED/DOWNGRADED` | disproved (demystified) |
| column-shadow lemma | `PROVED-mod-audit` | proved-mod-audit |
| aggregate pinning reduction (inequality not proved) | `PROVED-mod-audit` | proved-mod-audit (reduction only) |

#### D. Wave-8 lemmas, corner, audit corrections
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| `(◇)` dual identity | `PROVED` | proved-mod-audit |
| W2 sharp exchange | `PROVED` | proved-mod-audit |
| W3 witness residual identities (not a closure) | `PROVED / warning` | proved-mod-audit |
| RF return-flow (needs hypotheses/fix) | `PROVED-mod-audit` | proved-mod-audit |
| ND′ near-delta depth (threshold correction) | `PROVED-mod-audit` | proved-mod-audit |
| SF supply-forcing (reduction, not closure) | `PROVED` | proved-mod-audit |
| FC far-row coefficient cap | `PROVED` | proved-mod-audit |
| CPL transpose-coupling | `PROVED-mod-audit` | proved-mod-audit |
| NG′ no-gain lemma (stronger consistency not derived) | `RETRACTED/DOWNGRADED` | disproved (keep dead-route guidance only) |
| MC margin cap | `PROVED` | proved-mod-audit |
| RW generalized row-witness | `PROVED` | proved-mod-audit |
| WL W-locality | `PROVED-mod-audit` | proved-mod-audit |
| ladder analysis (not a theorem) | `CONJECTURAL / analysis` | conjecture |
| corner closed forms (see Table 1) | `PROVED-mod-audit + NUMERICAL` | proved-mod-audit (+ numerical) |
| finite-corner calibration | `RETRACTED/DOWNGRADED` (R-handling bug; asymptotic-only) | disproved |
| DMF + CEL ⇒ σ-wall/HLC | `PROVED-mod-audit` | proved-mod-audit |
| CEL cluster-exposure lemma | `OPEN` | open |
| all-shallow witness obstruction map | `PROVED-mod-audit as obstruction map; not a theorem excluding it` | proved-mod-audit (obstruction map only) |
| Baake–Sumner `δ=0` anchor | `PROVED-mod-audit` (source byte-pinned in main repo) | proved-mod-audit |

#### E. Wave-9 and post-d12 sharpening
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| existential-DMF suffices | `PROVED-mod-audit` | proved-mod-audit |
| corrected `a` formula | `PROVED-mod-audit` | proved-mod-audit |
| `t*=0` chain case | `PROVED-mod-audit` | proved-mod-audit |
| top-vertex WLOG | `PROVED-mod-audit` | proved-mod-audit |
| W-rows deep (`w∈W ⇒ g_w≥H`) | `PROVED` | proved-mod-audit |
| `σ̃` height-collapse | `PROVED` | proved-mod-audit |
| top-separator nonnegative | `PROVED-mod-audit` | proved-mod-audit |
| optimal-witness vacuous depth (small-σ case) | `PROVED-mod-audit` | proved-mod-audit |
| direct-two-site exclusion | `PROVED-mod-audit` | proved-mod-audit |
| disjoint-two-ball exclusion | `PROVED-mod-audit` | proved-mod-audit |
| non-skinny payment (`δ≥cH²`) | `PROVED-mod-audit` | proved-mod-audit |
| skinny spread-mass regime | `OPEN` | open |
| d12 broad "DMF supported" interpretation | `RETRACTED/DOWNGRADED` | disproved (scope narrowed) |
| small-delta σ regime (`σ̃_v→1`, web forced) | `PROVED-mod-audit` | proved-mod-audit |
| decisive unmeasured datum | `OPEN / NUMERICAL-GAP` | open (numerical gap) |

#### F. Numerical campaign inventory (all L3 — evidence, never proof)
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| 67k+ exact instances (no counterexample) | `NUMERICAL` | numerical |
| d8 MRP decider (`δ/H²≈3.484` @ `H/τ≈0.536`) | `NUMERICAL` | numerical |
| d8 σ-wall law (`H/τ≈min(σ,0.536)`) | `NUMERICAL` | numerical |
| d8 `k_groups` effect | `NUMERICAL` | numerical |
| d9 dual certificates | `NUMERICAL` | numerical |
| d9 budget/wall table (3.48 floor) | `NUMERICAL` | numerical |
| d10 far top-band feed (`M_far≈2.045–2.141`) | `NUMERICAL` | numerical |
| d10 financier law (`δ_min=½g_f`) | `NUMERICAL` (reinterpreted by d11) | numerical |
| d10 scale degeneracy catch | `RETRACTED/DOWNGRADED for original interpretation` | disproved (orig. interpretation) |
| d11 scale sweep (`g_f=H=2δ` budget line) | `NUMERICAL` | numerical |
| d11 aggregate coupling `M` (`min M/τ≥1.075`) | `NUMERICAL` | numerical |
| d12 DMF probe (100% deep, `m*=1`) | `NUMERICAL` | numerical |
| d12 σ̃ finding | `NUMERICAL; later downgraded in scope` | numerical (scope downgraded) |
| d12 all-shallow search | `NUMERICAL; limited scope` | numerical (limited scope) |

#### G. Refuted, downgraded, dead routes (do NOT re-walk — Rule 13)
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| literal psi-gap route | `REFUTED` | disproved |
| general-row leakage | `REFUTED / scoped` | disproved (only global-maximizer survives) |
| top-band localization as `T_far=∅` | `REFUTED / NUMERICAL` | disproved |
| canonical-`g` kernel energy proof | `DEAD ROUTE` | disproved (dead route) |
| row exactness at financier | `DEAD ROUTE` | disproved (dead route) |
| diagonal exactness at blocker | `DEAD ROUTE` | disproved (dead route) |
| raw factorization gauge route (`RΛ=I` not gauge-invariant) | `DEAD ROUTE / REFUTED` | disproved |
| finite-corner equals asymptotic proof | `RETRACTED/DOWNGRADED` | disproved |
| broad d12 DMF proof | `RETRACTED/DOWNGRADED` | disproved |
| averaging/quasi-stationary potentials | `DEAD ROUTE` | disproved (dead route) |
| height tests for projection norm excess | `DEAD ROUTE` | disproved (dead route) |
| raw circuit bounds | `DEAD ROUTE` | disproved (dead route) |
| unlocalized dual descent (`~¼ ≫ H`) | `DEAD ROUTE` | disproved (dead route) |
| maximality contradictions without localization | `DEAD ROUTE` | disproved (dead route) |
| rank induction via stochastic complement | `DEAD ROUTE` | disproved (dead route) |
| KKT localization-energy dichotomy | `DEAD ROUTE` | disproved (dead route) |
| pure convex shadow composition (vacuous as `μ→1`) | `DEAD ROUTE` | disproved (dead route) |
| log-staircase/shells | `DEAD ROUTE` | disproved (dead route) |

#### H. Literature / external-status notes (unchecked until byte-matched to `refs/` — L1)
| id | upstream status (verbatim) | re-tag |
|---|---|---|
| HLC originality (no known quantitative Douglas–Ando stability theorem) | `LITERATURE-SWEEP / not theorem` | stated |
| exact Douglas–Ando/Seever case | `CITED-background` | stated (needs `refs/` byte-match) |
| Baake–Sumner equal-input normal form (`baake-sumner-2007.11433`) | `CITED-background` | stated (in main-repo refs; cite precisely) |
| Hadwin-Li / Curgus-Jewett / Douglas / Ando follow-ups | `TO-ACQUIRE / provenance caveat` | stated (to-acquire) |

---

## (d) Known gaps / cautions

**(i) `kernel-conjecture-v2.tex` (the (EX) interface doc): FOUND — but not where the source layout implied.**
It is **NOT** present in the classical-portfolio source dir
(`…/agent-A/explorations/classical-portfolio/report/` has only `kernel-conjecture.tex`), and **NO**
`/tmp/codex-sigma-wall/…` volatile scratch tree exists on this machine (checked — the path is absent). The
file was located instead in the **upstream main repo** at
`/home/tobias/Projects/almost-idempotent-positive-maps/report/kernel-conjecture-v2.tex` (+ `.pdf`), and has
been **copied into `docs/ingest/report/kernel-conjecture-v2.{tex,pdf}`**. So: **not lost; recovered from the
main-repo `report/`, with its true provenance recorded here** (it is not part of the classical-portfolio
subtree). It carries the `(EX)` statement, the `(P1)/(DEF)` machinery, the `S*≤2Φ+6δ` factorization (F),
the rank-2 theorem, and the "irreducibility of selection" refutations.

**(ii) The honest headline is LINEAR, not quadratic.** Along the realizable family the tight relation is
**`δ = H/2`** (see DELIVERABLE2/3 and ledger L6). The **`δ ≳ H²`** form is **only the worst-case envelope**,
binding *only because `H` is capped at `O(√δ)`** by the exposedness window. Reporting "`δ ≳ H²`" without
"`δ ≳ H` and `H ≲ √δ`" understates what is actually true. (The `√η` exponent in `op-classical` is
nonetheless **sharp** — `ex-hume`.) Do not present the frame-specific `dist₁(λ,Δ)=2·neg(λ)` proof as the
general one; the transferable statement is exactly the open `lem-dual-localization`.

**(iii) Raw-index path-products are REFUTED (cloning obstruction).** Index-level path-product floors do not
survive: the **cloning obstruction** refutes them (per this repo's `CLAUDE.md` §3 / `FINDINGS.md`, for any
`δ₀ ≥ 0.233`). **Only clone-invariant (quotient) quantities may appear in a proof** — this killed a whole
family of attempts (see the raw-`RΛ=I` / raw-circuit dead routes in Table 2 §C/§G). Any re-established
argument must be phrased in clone-invariant terms.
