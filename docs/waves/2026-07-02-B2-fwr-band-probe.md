<!--
ROLE: verbatim harvest artifact of fr arm B, wave 2 (2026-07-02). Worker: opus:prover (subagent).
STATUS: HEURISTIC exploration report (L0) — EXCEPT the s5 rational arithmetic, which the orchestrator
independently recomputed over exact Fractions (P^2=P, delta=1841/1600000, ||p4-p5||_1=2003/2000,
eps=2681/400000, X inside the forbidden gap): all True. The dichotomy DERIVATION and the
corner-saturation argument remain unreviewed heuristics. Referenced by .frontier/log.jsonl (arm B,
wave 2, died) and bd aism-yxq.
-->

# Arm B · wave 2 · F-WR wiggle rigidity vs the shallow band — harvest (verbatim report)

**Bottom line up front:** OBSTRUCTION (named, sharpened). F-WR cannot ground the shallow near-top band. Two independent hypotheses fail on the band (self-indexing is not clone-invariant; the web-radius bound is exactly the missing input), and I derive+verify a self-referential *coincidence-or-antipodality dichotomy* from F-WR itself which the s5 certificate lands **strictly inside the forbidden gap** of — an exact-rational proof that s5's band is not a common-pattern web. F-WR bounds pairwise ℓ¹-distance, never the *number* of distinct shallow classes; the simplex-corner configuration saturates its wide branch with dimension-many classes. The anti-splitting residual is unchanged.

## 1. READ (one line each; F-WR hypotheses quoted verbatim)

- `docs/waves/2026-07-02-B1-dual-localization.md` — wave-1 verdict OBSTRUCTION; obs-deep-leakage caps deep/visible positive mass by `(2+4δ)δ/H`, so v's mass leaks into the shallow band; residual = anti-splitting; NEXT-PULL #3 flags F-WR as the one non-dead δ-scale rigidity to test.
- `argument/lemmas/obs-deep-leakage.md` / `lem-canonical-separator.md` — codified forms (status `heuristic` / `proved-mod-audit`); deficit `g=Pg`, `g≥0`, `g_v=0`, `Ω≤2+4δ`; all quantities clone-invariant.
- `06-day1-belt.tex:158-166` — **F-WR verbatim**: *"For self-indexed common-pattern webs with row decompositions \(x_i=\bar\pi+w_i\), web radius \(\|w_i\|_1\le r_{\mathrm{web}}\), small \(\delta\), and local external masses \(s_i\), \(\|w_i-w_j\|_1\le 2.1(s_i+s_j)+4\delta+2r_{\mathrm{web}}^2\). The \(\rho\)-separation corollary additionally assumes \(r_{\mathrm{web}}\le 2\rho\)."* — plus `:118-119` **self-indexed verbatim**: *"Self-indexed means row labels also serve as coefficient coordinates."* — and `:97-103` **X1 one-mode wall**: *"An exact nonconstant shell has rows \(p_i=q+t_i r\)… \((\max_i t_i-\min_i t_i)\|r\|_1\ge 2\). Therefore the shell has \(\ell^1\)-diameter at least 2, so a nonconstant exact one-mode shell cannot hide inside a sub-\(\rho\) skinny cluster."* — L2' ρ-shadow `:32-36`: *"The recursion to a fresh hidden vertex is not banked."*
- `kernel-conjecture.tex:232-235` — **shallow band verbatim**: *"For a threshold \(t\in(0,\kappa\Omega]\), the shallow band is \(S_t=\{i: g_i<t\}\), the band block is \(P_{S_tS_t}\), and the carrier graph is the directed graph on \(S_t\) with an edge \(i\to j\) when \(P_{ij}>0\)."* — anti-splitting `:318-322`: *"high hidden height provably forces aggregate shallow off-\(C_\W\) carrier mass \(\ge(B/3-4)\tau\), but pinning a \(c\tau\) share into one closed quotient component needs a dimension-free bound on the number of geometrically distinct shallow classes hit by \(P_v^+\) — which no audited tool supplies."*
- `10-refutations-dead-routes.tex:101-108` — s5 downgrade (all-shallow faces exist, height-conditional); `:172` **log-staircase/shell route DEAD**: *"Exactness and the one-mode wall kill the common pattern; no counterexample was produced."*; `:196-208` — final open = height-conditioned shallow-web exclusion (signed quantitative Baake–Sumner).
- `02-geometry-exposedness.tex:163-172` + `05-corner-theorem.tex:182-183` — **s5 invariants**: `W={1,2,3}`, hidden `4,5`, `σ̃=1/2000`, `H=1/1000`, `δ=1841/1600000`, `g_5=0`, witness on far row 5.
- `experiments/d14_leakage.py:293-303` — **the explicit exact-rational s5 matrix** (`build_s5`), forced_v=row 4.
- `STATUS-LEDGER.md:53` — F-WR row: *"PROVED-mod-audit… Side conditions: self-indexing, small delta; separation corollary needs web radius bound."*; `:47` X1 *"subsumed by F-WR in common-pattern case."*
- `FINDINGS.md` — DEAD routes (cloning obstruction ⇒ clone-invariant-only; canonical-g energy; ψ-gap; finite-corner); 2026-07-02 constants entry.

## 2. ANSWER (a) — does the shallow band form self-indexed common-pattern web(s)?

The shallow band `S_t={g_i<t}` is a **sublevel set of one affine functional** `φ` (deficit `g=H−φ`). F-WR needs an **ℓ¹-geometric** skinny web. Match:

| F-WR hypothesis (06:158-166,118) | what the band provides | tag |
|---|---|---|
| **H1 self-indexed** — "row labels also serve as coefficient coordinates" | the carrier graph (kernel:234) is a **raw-index** object `i→j when P_ij>0`; self-indexing is the private-site / identity-frame gauge. Cloning `P̂_ab=α_b P_{π(a),π(b)}` splits one site into M coordinates, destroying the row↔coordinate bijection. Raw-index carrier structure is exactly what the **cloning obstruction** forbids in a proof (kernel:268-282; FINDINGS). | **[fails]** — not clone-invariant; would need an (unaudited) quotient reformulation |
| **H2 common pattern** `x_i=π̄+w_i` | trivially satisfiable (any set has a barycenter); content is empty until a radius is bounded | **[holds trivially / vacuous]** |
| **H3 web radius** `‖w_i‖₁≤r_web` small | `g_i<t` bounds closeness only in the **single** direction `φ`; `φ` is flat along the top face of `C_W`, so band rows can differ by the **transverse** spread up to `diam(topface)≈2`. Small deficit ⇏ small ℓ¹ radius. | **[fails]** = the recorded "web radius bound needed" (LEDGER:53) |
| **H4 small δ** | holds (δ≤¼) | **[holds]** |
| **H5 local external masses `s_i`** | in the *dangerous* regime the anti-splitting antecedent forces aggregate off-`C_W` carrier mass `≥(B/3−4)τ` (kernel:319) ⇒ `s_i=Θ(τ)`, not `O(δ)` | **[holds but Θ(τ)-scale]** |
| **H6 (corollary) `r_web≤2ρ=8τ`** | not supplied; and X1 (06:97-103) shows a nonconstant **exact** common-pattern shell has ℓ¹-diameter ≥2 ⇒ `r_web≥1≫8τ`. Exactness forbids a skinny *nonconstant* self-indexed shell. | **[fails]** |

**Verdict (a):** the band does **not** form self-indexed common-pattern webs in the sense F-WR requires. The gap between "deficit-shallow" (grouping by one functional `φ`) and "ℓ¹-skinny" (what F-WR needs) is exactly the transverse spread — which is uncontrolled and is precisely the frame-specific→frame-free / web-radius / anti-splitting-class-count gap under three names. Two of the failures are hard: **H1** violates the binding clone-invariance constraint, and **H6** is refuted by the proved X1 wall for any genuinely nonconstant band.

## 3. ANSWER (b) — the s5 falsifier, worked EXACTLY (rational)

I recovered the explicit matrix (`d14_leakage.py:293-303`) and verified `P²=P` **exactly**, `Σrows=1`, `δ=max ν_i=1841/1600000` (attained at archetype row 2). The two hidden vertices are rows 4,5 (both at deficit `g=0`, i.e. the very top of the band). Their exact separation:

```
p_4 − p_5 = ( 0 , −2001/4000 , +2001/4000 , −1/2000 , +1/2000 )
‖p_4 − p_5‖₁ = 2003/2000 = 1.0015          (EXACT)
```

So two rows **at identical deficit `g=0`** sit at **ℓ¹-distance ≈ 1** — the concrete mechanism: their difference is a **mass swap of `2001/4000` between coordinates 1↔2**, which live on the top face of `C_W` where `φ` is flat, so `φ(p_4)=φ(p_5)` while `‖p_4−p_5‖₁≈1`.

**Is s5's band a common-pattern web?** Test the hypotheses concretely:
- **H1 self-indexed — FAILS exactly.** Rows 4,5 carry their mass on the **archetype** coordinates: `P_{4·}` has `1989/40000≈0.0497` on col 1 and `3801099/4000000≈0.9503` on col 2, but only `P_{45}=1/2000` **internally**. Web-internal weights are `1/2000` each (`P_{45}=P_{54}=1/2000`); the rows are **not** indexed by their own coordinates.
- **H3/H6 skinny radius — FAILS exactly.** Best-centered `r_web=‖p_4−p_5‖₁/2=2003/4000≈0.50075`, versus `2ρ=8τ≈0.2714`. So `r_web>2ρ`.
- **F-WR numerically, forced onto {4,5}:** with `s_4=s_5=P_{45}=1/2000`,
  `RHS = 2.1(1/2000+1/2000)+4δ+2r_web² = 0.5082…` while `LHS=‖p_4−p_5‖₁=1.0015`. **`1.0015 ≤ 0.508` is FALSE.** F-WR's conclusion is *violated* — so its hypotheses provably do not hold on {4,5} (a precise hypothesis-failure = SUCCESS).

**The self-referential dichotomy (new artifact).** For a centered 2-web, `r_web=X/2` with `X=‖p_i−p_j‖₁`, so F-WR reads `X ≤ ε + X²/2` with `ε:=2.1(s_i+s_j)+4δ`, i.e. `X²/2−X+ε≥0`, giving the **forbidden gap** `X∉(≈ε, 2−ε)`: a valid exact self-indexed common-pattern 2-web is either **coincident to O(ε)** or **ℓ¹-diameter ≥ 2−O(ε)** — the quantitative X1 wall. For s5, `ε=0.0067025`, forbidden gap `X∈(0.006725, 1.99327)`, and **actual `X=1.0015` lands squarely inside**. So s5 is an exact-rational certificate that its own shallow band is *not* a common-pattern web — it is genuinely mid-separated, which F-WR forbids.

**Scope note:** s5 has `σ̃/τ=0.0147≪1` and `H/τ=0.0295≪1`, so it lives in the **proved** small-`σ̃` branch (`H≤2(1+2δ)max(σ̃,ν)`), *not* the open web regime (`σ̃>τ, H>Bτ`). It is a low-height existence certificate of two well-separated hidden vertices, handled already by the s8 cap — F-WR is neither needed for it nor powered by it.

## 4. ANSWER (c) — composed sketch, with tags

Target: use F-WR to pin a `cτ` share of `P_v⁺`'s shallow mass into one closed quotient component (⇒ component finisher ⇒ exposed ⇒ contradicts hiddenness ⇒ HLC).

- **C1 [solid]** obs-deep-leakage/L5': `P_v⁺` mass sits in the shallow band `S_t`; anti-splitting antecedent forces aggregate off-`C_W` carrier mass `≥(B/3−4)τ` (kernel:319).
- **C2 [gap]** *"`S_t` (or each carrier-graph SCC) is a self-indexed common-pattern web."* — Blocked at **H1** (self-indexing is not clone-invariant; s5 shows mass lands on archetype coordinates, not own labels) and at **H3/H6** (deficit ⇏ ℓ¹ radius; s5 exhibits `r_web≈0.5≫8τ` at deficit 0).
- **C3 [gap→obstruction]** *Even granting a web:* F-WR gives, per pair, `‖p_i−p_j‖₁ ≤ 2.1(s_i+s_j)+4δ+2r_web²`. With `s_i=Θ(τ)` (C1) this is at best a **τ-scale** (√δ) pairwise collapse, and the self-referential dichotomy (§3) forces each pair to be **either O(τ)-coincident or ℓ¹-diameter ≥2−O(τ)**. There is no intermediate skinny-but-distinct web at the ρ-scale.
- **C4 [obstruction, named]** The wide branch (diameter ≥ 2) is saturated by the **simplex-corner configuration**: rows near distinct corners `e_1,…,e_n` are pairwise ℓ¹-distance 2 and can all have small deficit. F-WR collapses *within* a corner-cluster but **cannot merge corners**, and places **no dimension-free cap on the number of clusters**. So it cannot pin `cτ` into *one* component.

**Composition cannot start productively.** In the skinny regime F-WR's pairwise collapse is redundant with existing near-coincidence machinery (rows within `2ρ` are already in one ρ-cluster); in the wide regime it is vacuous. It reduces "bound #distinct shallow classes" to "bound #F-WR-skinny sub-webs the band splits into" — the **same** anti-splitting number, unshrunk.

## 5. DEAD-ROUTE AUDIT

- **Clone-invariant only** ✅ — the load-bearing quantities (`‖p_i−p_j‖₁=2003/2000`, `δ`, `σ̃`, `g`, `s_i`) are clone-invariant. I *use* H1's non-clone-invariance only to **diagnose** F-WR's failure; I never rely on a raw-index structure in a positive step. (New finding: this is an independent clone-invariance obstruction to F-WR.)
- **No convexity-only** ✅ — every step uses `P²=P` (deficit harmonicity, X1 biorthogonality).
- **No canonical-g energy** ✅ — `g` used only to *define* the band's level sets, never as quadratic `Γ=P(g²)−g²`.
- **No raw-index path products** ✅ — explicitly flagged as the reason H1 fails.
- **No "rows within ρ of conv W"** ✅ — s5 shows band rows at ℓ¹-distance ≈1, refuting any such assumption.
- **Log-staircase / one-mode-shell route (DEAD, 10:172)** ✅ — I do **not** attempt to prove via the shell route; I use the *proved* X1 wall to diagnose, and my verdict **reinforces** that certificate ("exactness + one-mode wall kill the common pattern").
- Not re-walked: unlocalized dual descent, quasi-stationary potentials, maximality-without-localization, rank induction, literal ψ-gap, finite-corner-as-asymptotic (s5 explicitly kept as an exact certificate, not an asymptotic claim). ✅

## 6. VERDICT — OBSTRUCTION (named)

**F-WR wiggle rigidity is a coincidence-or-antipodality dichotomy, not a clustering bound.** It requires (i) a web-radius bound the shallow band does not supply (deficit-shallow ≠ ℓ¹-skinny; the transverse spread is free, exact-witnessed by s5 at `‖p_4−p_5‖₁=2003/2000` with `g=0`), and (ii) self-indexing, which is **not clone-invariant** (violates the binding constraint). Even when applicable it bounds only pairwise ℓ¹-distance and forces each pair to be O(τ)-coincident or ℓ¹-diameter ≥ 2 — the simplex-corner configuration saturates the wide branch with **dimension-many** distinct shallow classes. Hence F-WR — the last non-dead δ-scale exactness rigidity — **provably cannot** supply the "dimension-free bound on the number of geometrically distinct shallow classes hit by `P_v⁺`" (kernel:320-322). The anti-splitting residual is unchanged; this consolidates it with the log-staircase/shell dead-route.

*(Not a REDUCTION: no new smaller residual. The residual is identical to the record — "the band splits into O(1)-many F-WR-skinny sub-webs" ≡ the anti-splitting class-count.)*

Honesty: F-WR is `proved-mod-audit`; the dichotomy and the corner-saturation argument are **heuristic** (mine), un-reviewed. The s5 arithmetic is exact (`P²=P` verified over ℚ). Everything else is heuristic until adversarially validated.

## 7. NEXT PULL

1. **Escalate to strategist — wave-1 open #2 resolved negatively.** Both the linear law (`H≤2δ`) and the sufficient √δ HLC (`H≤Cτ`) bottleneck on the **identical** class-count bound: F-WR's external-mass term is already `Θ(τ)`, so re-scoping to √δ gives **no relief**. Do not spend arm B on a "weaker √δ recursion" hoping to dodge anti-splitting.
2. **Arm B's v-local / web-rigidity family is exhausted** (obs-deep-leakage closed the local handle; F-WR now closed the last rigidity). The class-count bound needs a genuinely **new clone-invariant tool** — a *packing* statement in the **quotient** (conj:quotient-floor, kernel:284-306), where classes are ℓ¹-separated by construction: *how many pairwise-separated shallow quotient classes can carry ≥cτ of `[v]` under one exact idempotent `P̄` with `δ(P̄)≤δ`?* This is the signed quantitative Baake–Sumner statement (08:198-209) directly.
3. Register the derived **F-WR forbidden-gap dichotomy** and the **exact s5 separation `‖p_4−p_5‖₁=2003/2000`** as a bankable heuristic artifact (candidate `obs-fwr-gap`): it is the quantitative X1 wall and the clean reason web-rigidity cannot count classes — any future closure must consume or evade it.
