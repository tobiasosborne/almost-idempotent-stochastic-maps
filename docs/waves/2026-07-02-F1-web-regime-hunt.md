<!--
ROLE: verbatim harvest artifact of fr arm F, wave 1 (2026-07-02). Worker: opus:prover (subagent).
STATUS: L3 numerical evidence / heuristic (L0). The headline instance was independently recomputed by
the orchestrator (fresh Fractions code: P^2=P, delta=49/2000, both hidden rows at exactly 1/20 from
conv W) and the wave's own verify_instance.py re-run (primal=dual=LP=1/20, exposedness/hiddenness
certificates). Scripts re-homed under L3 discipline: runs/2026-07-02-web-regime-hunt/.
Referenced by .frontier/log.jsonl (arm F, progress) and bd aism-kpl.
-->

# Arm F · wave 1 · exact web-regime construction probe — harvest (verbatim report)

(verbatim deliverable follows)

## 1. READ + pipeline calibration

Read (loci, not paraphrase): `CONVENTIONS.md` (a–f); `kernel-conjecture.tex` Setting/§Kernel/§stronger (def:esi/scales/vertex/exposed/height/sigt lines 55–147, conj 151–166, s8-cap remark 176–189, shallow-band/carrier 223–322); `05-corner-theorem.tex` (corner family laws `H=2δ`, `t*=δ/(1+δ)`, edge `τ*=2−√3`, lines 15–76); `09-numerics-record.tex:60–120` (d8–d13 record: `H/τ≈min(σ̃,0.536)`, d13 "hidden heights track `H≈2δ`"); `d1_infra.py`/`d3_vertexfix.py` (the operational LP pipeline — `well_exposed_set_robust`, `t*≥κ`); `FINDINGS.md`; `docs/waves/2026-07-02-B2-...`.

I built an **exact (ℚ) reimplementation** of the operational pipeline (exact two-phase simplex validated vs scipy over 300 LPs, maxerr 7e-15). All regime predicates are exact rational: `σ̃>τ ⟺ σ̃²>δ`, `‖·‖₁≥ρ ⟺ ‖·‖₁²≥16δ`, `t*≥κ ⟺ 16t*²≥δ`.

**s5 reproduced exactly** (`calibrate_s5.py`): δ=**1841/1600000**, H=**1/1000**, σ̃=**1/2000** (both hidden rows), W=**{0,1,2}**, hidden=**{3,4}**, ‖p₄−p₅‖₁=**2003/2000**; σ̃/τ=0.01474, H/τ=0.02948. Clone-invariance sanity (clone row 0 ×3): δ, H, σ̃ all invariant. **The record's own float pipeline agrees on every load-bearing instance below.** Pipeline trusted.

## 2. Families tried (Task-4 table)

| family (script) | params | max σ̃/τ | H/τ there | max H/τ (hidden) | binding constraint at stall |
|---|---|---|---|---|---|
| pure face-poke, single/twin, R2=0 (`exp3`) | poke p from **mid-edge** | 0 (σ̃≡0) | — | **0.500** at δ=1/16 | **EXPOSEDNESS**: `t*=δ/(1+δ)`; poke past δ*⇒ vertex exposes (H→0). `H=2δ` exact |
| reach *past a corner* (`exp2`) | N | 0 | — | 0 | reaching row becomes an **exposed endpoint**; corner goes interior; H=0 |
| twin near-edge + tail feed (`exp5`) | p, ρ | 0.24 | ~0.16 | H/δ up to **2.04** | δ-budget: feeding raises δ faster than H+σ̃ |
| random near-corner (`search1`, 1.2k) | — | **3.97** (δ=0.063, below corner) | 0.027 | 0.068 | σ̃ (self/near mass) is **inert for height** |
| aggressive tail+web (`search2`, 12k) | k≤5,m≤5 | 2.39 | 0.076 | 0.36 | collapse bound / σ̃–H anti-correlation |
| hill-climb max H/δ (`exp6`, 7.2k) | free C,R2 | 0.13 @ maxH | — | **0.502** (δ=0.060) | exposedness cap `H/τ<0.536`; `H/δ→2` as δ→0 |
| σ̃→1 push (heavy feed) | p, ρ | 0.24 | drops | drops | δ blows past 1/4 before σ̃→1; **anti-correlation** |

**Aggregate: over ~48,000 exact idempotents (~500 certified hidden vertices), `H > Bτ` (B=0.536) occurred ZERO times. σ̃>τ occurred often (up to σ̃/τ≈4). The JOINT never.**

## 3. Best instances

**(a) Max-height hidden vertex** (`exp6` s5): δ=6451283/108000000≈**0.0597**, **H/τ=0.5023**, H/δ=2.055, σ̃/τ=0.128 — a hidden vertex right at the corner cap, σ̃ small.

**(b) Max σ̃/τ, below corner** (`search1`): δ≈**0.0626**, **σ̃/τ=3.97**, H/τ=**0.027** — σ̃≫τ crossable below corner, but height negligible.

**(c) Certified clean exhibit** (`verify_instance.py`, the one worth banking), δ=**49/2000**, generator `build_from_LambdaC(C,R2)`, C=[[½−x,½+x+p,−p],[½+x,½−x+p,−p]], x=p/3, p=1/40, ρ=1/100:
```
P = [ 99/100    -21/2000    1/2000    1/100  1/100
      -1/100    1979/2000   1/2000    1/100  1/100
      -1/100    -21/2000    2001/2000 1/100  1/100
      289/600   3137/6000  -49/2000   1/100  1/100     <- hidden vertex v
      299/600   3037/6000  -49/2000   1/100  1/100  ]  <- hidden vertex
```
P²=P exact; W={0,1,2} (exposed, t*≈0.50/0.48/0.98); rows 3,4 **hidden** (t*=1/41, 16t*²=16/1681<δ; far rows exist). **H=1/20 certified** by matching primal (7/15·p₀+8/15·p₁) and dual (1-Lipschitz φ, ‖a‖∞=1, φ|W≤0, φ(v)=1/20). ν_v=δ=49/2000 ⇒ **H/δ = 100/49 ≈ 2.0408**. Clone-invariant (verified). **Anti-splitting antecedent NOT realized**: σ̃/τ=0.128<1, H/τ=0.319<B.

## 4. The web regime was NOT entered — binding constraints + structural reason

Two independent binding walls, both exact-witnessed:

- **W1 — Exposedness caps height at the corner.** A hidden vertex's poke is `t*=ν_v/(1+ν_v)` (reproduced exactly: 1/101, 1/51, 1/21); hidden requires `t*<κ=τ/4`, i.e. `τ<2−√3`. So a *pure-negativity* poke gives `H=2δ`, `H/τ=2√δ ≤ 0.536`, and **exposes** (H→0) the instant the poke exceeds the corner scale. Max H/τ found for any hidden vertex = **0.502** (≈ corner). Reaching *past a corner* (not from a face middle) just manufactures a new exposed vertex.
- **W2 — σ̃ is inert / anti-correlated with height (the non-bootstrapping web).** σ̃>τ is trivially crossable (self-mass on the diagonal, or feeding on *nearby* hidden rows), but every such config has H/τ tiny. The **s8 collapse bound `H·(1−σ̃) ≤ ν(2+4δ)` held with 0 violations over all ~500 hidden vertices.** Since ν≤δ, escaping `H=O(δ)` requires `σ̃→1`, not merely `σ̃>τ` — and driving σ̃ up (heavy feeding) *raises δ faster than H*, so δ hits 1/4 first.

**[check] OBSTRUCTION-CANDIDATE (structural, heuristic).** *A hidden vertex cannot bootstrap height by feeding on a shallow web.* By row reproduction `p_v=Σ_j P_{vj}p_j`, v's invisible-positive mass σ̃ sits on **hidden** rows, which are themselves ≤ H from conv W (v is the top ⇒ they are no farther out). So `dist(p_v,C_W) ≤ σ̃·H + ν·(2+4δ)`, giving `H(1−σ̃) ≤ ν(2+4δ)`. **Height is self-referentially capped at O(δ) unless σ̃→1.** The only rows at O(τ)/O(1) distance are the *exposed* corners (in C_W, contributing 0 height). Hence below the corner scale, `σ̃>τ ∧ H>Bτ` is (candidate-)**empty**: the antecedent's two clauses live at opposite ends of a tradeoff (`H/τ≈min(2√δ, σ̃-driven-but-collapsed)`), matching `09-numerics-record.tex:77` exactly.

**Certified side-finding (report loudly, precisely):** the *empirical* linear law **"δ ≥ H/2 with zero exceptions" is FALSE at finite δ.** Certified counterexample `H/δ = 100/49 ≈ 2.0408` (instance (c)); search max ≈ **2.055**. Mechanism = **hull-dip**: giving the *visible* archetypes their own negativity (≤δ) recedes conv W, so a hidden vertex sits farther per unit of its negativity budget. The record's generators kept visible/recurrent rows non-negative (as at δ=0), so never saw this. **This does NOT touch the kernel conjecture:** the exceedance is an O(δ) finite-size term — scaling the family down gives `H/δ → 2` and `H/τ → 0` (2.0408→2.0202→…→2.0000). The *asymptotic* linear-law constant is exactly 2; the *global finite-δ* constant is `> 2` (≥100/49). It also does NOT contradict any proved result (the tangent-cone lemma `Ḣ⁺≤2δ̇` is infinitesimal at H–M points; the global `H≤2δ` is open, `kernel-conjecture.tex:406–419`).

## 5. VERDICT

**STALL-MAP** (dangerous web regime NOT entered; two named binding constraints W1/W2 + a [check] non-bootstrapping obstruction-candidate) **+ a bankable certified OBSERVATION** (finite-δ exceedance of the empirical linear law, `H/δ=100/49`, clone-invariant, cross-checked against the record's own pipeline; kernel-safe because `H/δ→2`, `H/τ→0`).

## 6. NEXT PULL for arm F

1. **Bank two heuristic artifacts** (candidate shards): `obs-height-collapse` — `H(1−σ̃) ≤ ν(2+4δ)` (0/500 violations; the exact non-bootstrapping mechanism, the clone-invariant sharpening of the s8 cap that makes W2 quantitative); and `obs-linear-law-finite-delta` — the certified `H/δ=100/49` hull-dip instance (refines FINDINGS "H/δ exactly 2" to "→2 asymptotically, `>2` finite"). File a `bd` note so a later agent does not re-quote "δ≥H/2, zero exceptions".
2. **The residual is unchanged and now sharper:** the frontier is `σ̃→1` (not `σ̃>τ`). Ask whether an exact idempotent can have a hidden top vertex with `1−σ̃ = O(τ)` at small δ — the only door the collapse bound leaves open. My families cannot approach it (δ→¼ first); a genuinely new *rank-growing* construction (hidden rows on fresh coordinates kept hidden by shielding) is needed, or a proof that `σ̃≤1−cτ` for hidden vertices (which would *close* the kernel conjecture via the collapse bound).
3. **Do not** spend arm F re-attacking `σ̃>τ` as the antecedent — it is cheap and inert (W2). Re-scope the antecedent to `σ̃→1`, or hand `obs-height-collapse` to an `af` elevation as the candidate finisher.
