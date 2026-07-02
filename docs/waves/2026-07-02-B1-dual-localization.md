<!--
ROLE: verbatim harvest artifact of fr arm B, wave 1 (2026-07-02). Worker: opus:prover (subagent).
STATUS: HEURISTIC exploration report — nothing here is rigorous (L0); registry entries derived from it
carry their own honest status. Referenced by .frontier/log.jsonl (arm B, died) and bd aism-yxq.
-->

# Arm B · wave 1 · lem-dual-localization — harvest (verbatim report)

Verdict: OBSTRUCTION. Loci spot-checked by the orchestrator against the ingest sources
(kernel-conjecture.tex:225-232 separator/harmonicity/Omega; :316-322 anti-splitting) — quotes faithful.

---
(report follows verbatim)

## 1. READ
- `argument/lemmas/lem-dual-localization.md` — contract: "reproduce ‖Ē‖₁ ≥ H from P²=P WITHOUT the canonical simplex frame"; status open, deps empty, owner A.
- `docs/ingest/experiments/DELIVERABLE2_asq_proof.md` — Route A (frame, PROVED, `dist₁(λ,Δ)=2·neg(λ)`) vs Route B (shadow composition, vacuous as μ→1); the crisp open statement (lines 77–86).
- `docs/ingest/experiments/DELIVERABLE3_verdict_dag.md` — (ASQ) TRUE numerically; dual-localization "SURVIVES and is SHARPENED" to the skinny μ→1 inequality.
- `FINDINGS.md` — dead routes (cloning obstruction, convexity, canonical-g energy); 2026-07-02 constants entry (`δ=H/2` linear tight; `H≤2δ` the Arm B target; `2.000000000013` is float noise).
- `docs/ingest/report/kernel-conjecture.tex` — canonical separator + harmonicity `g=Pg` (227–232), `Ω≤2+4δ`, the exact row identity `p_i=Σ_j P_ij p_j` (183, 231), cloning obstruction (268–282), anti-splitting/shallow-fan frontier (318–322).
- `CONVENTIONS.md` — δ, τ=√δ, ρ=4τ, κ=τ/4; signed vs stochastic pictures; status rungs.
- `docs/ingest/report/sections/06-day1-belt.tex` — L4 clipping, L5' leakage, L6 identity-frame, X1 one-mode wall (biorthogonality), F1 skinny, F-SS sharp shadow, F-WR wiggle rigidity.
- `docs/ingest/report/sections/10-refutations-dead-routes.tex` — the dead-route table (crucial: "unlocalized dual descent", "quasi-stationary potentials", "maximality without localization", "rank induction", "raw factorization gauge route", "pure convex shadow composition" all DEAD).
- `docs/ingest/report/STATUS-LEDGER.md` — RW row-witness (proved), W3 "pushing witness through P loses sign structure", C10 "α-mass uncontrolled".

## 2. ATTACK LINE
I pursued angle (i)+(ii)+(iv) unified: exploit the *full* invariant content of P²=P at the hidden top vertex — **row-exactness** (each row is a stationary signed measure, `p_v P = p_v`) and **column-exactness** (columns of P are P-harmonic) — via the canonical separator's harmonic deficit `g=Pg`, working entirely in clone-invariant (geometric-class) quantities, to force the O(√δ)→O(δ) improvement that convex shadow composition (Route B) cannot. All picture-work is in the **signed** picture (exact P²=P, δ), never crossing to stochastic. The line terminates in a clean frame-free identity that turns out to be the *wrong-signed* bound — which is itself the obstruction.

## 3. THE ARGUMENT

Signed picture throughout. `v` = hidden top vertex, `φ` = canonical separator (`φ` affine, ℓ¹-1-Lipschitz, `φ≤0` on `C_W`, `sup_{C_W}φ=0`, `φ(p_v)=H`; exists by ℓ¹/ℓ∞ duality — `kernel-conjecture.tex:227-229`). `g_i:=H−φ(p_i)`.

**S1 [solid]** `p_v P = p_v`, i.e. `p_v = Σ_j P_vj p_j` exactly, with `Σ_j P_vj=1`, `Σ_j (P_vj)⁻=ν_v≤δ` (row v of P²=P; `kernel-conjecture.tex:231`). *Clone-invariant:* net class weights `Σ_{b∈class}P_vb` are cloning-stable.

**S2 [solid]** `g=Pg`, `g≥0`, `g_v=0`, `Ω_g:=max g−min g≤2+4δ`, and `min g=0` (attained at v) (`kernel-conjecture.tex:230-232`). For any row, `φ(p_i)≤dist₁(p_i,C_W)≤H` (1-Lipschitz + `φ≤0` on C_W + H maximal), so `g_i≥0`. Define the **deep side** `D:={j : φ(p_j)≤0} ⊇ W`; for `j∈D`, `g_j=H−φ(p_j)≥H`. All clone-invariant (φ, g, D are functions of geometric rows).

**S3 [solid]** Harmonic identity at v: `0=g_v=Σ_j P_vj g_j`, so
`Σ_j (P_vj)⁺ g_j = Σ_j (P_vj)⁻ g_j ≤ Ω_g·ν_v ≤ (2+4δ)δ`.

**S4 [solid]** Lower-bound the LHS on the deep side (`g_j≥H`, `(P_vj)⁺≥0`):
`H·M⁺_deep ≤ (2+4δ)δ`,  where **`M⁺_deep := Σ_{j∈D}(P_vj)⁺`** = positive coefficient mass v places on the deep side. (`M⁺_deep` clone-invariant: `Σ_{b∈class}(P_vb)⁺=(P_v,class)⁺` since fiber weights αb>0 preserve sign.)

**Corollary [solid]** Positive mass v places on the *visible* hull satisfies `Σ_{w∈W}(P_vw)⁺ ≤ M⁺_deep ≤ (2+4δ)δ/H`.

**S5 [solid, but this is the wall]** S4 is an **upper** bound on deep/visible mass — the frame-free, clone-invariant re-derivation of L5' leakage (`06-day1-belt.tex:58-66`; `M⁺_deep` is L5''s `Σ_{dist≤H/2}α_j` up to the `(1+ν)` normalization). To *close* the linear law via S4 I would need the **opposite**, a lower bound `M⁺_deep ≥ c>0`, giving `H ≤ (2+4δ)δ/c = O(δ)`.

**S6 [gap → refuted]** `M⁺_deep ≥ c` is **false**. S4 itself forces `M⁺_deep ≤ (2+4δ)δ/H = O(√δ)→0` (since `H` can reach the window scale O(√δ)). Equivalently: exactness makes v's positive mass *leak upward* into the shallow near-top band `{0<φ(p_j)<H}`, not down onto C_W. The s5 exact-rational 5×5 all-shallow certificate (`10-refutations-dead-routes.tex:101-108`) realizes exactly this. So S4 cannot be inverted.

**S7 [gap = recorded frontier]** With `M⁺_deep≈0`, v's mass sits on other near-top rows, which recurse (L2' ρ-shadow, whose recursion is explicitly "not banked", `06-day1-belt.tex:32-36`). Grounding this shallow band to C_W at O(δ) cost = the "shallow-web exclusion" / "anti-splitting" gap: "pinning a cτ share into one closed quotient component needs a dimension-free bound on the number of geometrically distinct shallow classes hit by `P_v⁺`" (`kernel-conjecture.tex:318-322`).

## 4. RESIDUAL(S)
The load-bearing NEW artifact is the frame-free, clone-invariant identity (S1–S4), stated as a bankable candidate:

> **obs-deep-leakage [heuristic→could be af-elevated].** For the hidden top vertex v with canonical separator φ and deep side `D={φ(p_j)≤0}`, `H·Σ_{j∈D}(P_vj)⁺ ≤ (2+4δ)·δ`. In particular v's positive coefficient mass on the visible hull is ≤ (2+4δ)δ/H. [solid modulo the two proved-mod-audit inputs: canonical-separator existence and `Ω_g≤2+4δ`.]

This is a genuine frame-free extraction of the *right δ-scale* on the wrong side of the ledger. The residual that remains is **unchanged from the record**: the height-conditioned shallow-web exclusion (`10-refutations-dead-routes.tex:196-208`). My work does not shrink it; it explains, from P²=P alone, *why* it is the sole residual — the risk-carrying steps are S6/S7 (they are not gaps in a proof, they are the confirmed obstruction).

Bonus reformulation [check]: since P is a rank-k projection, `P=Σ_{a≤k} u_a ψ_aᵀ` (biorthogonal, `Pu_a=u_a`, `ψ_aᵀP=ψ_aᵀ`), giving **every row `p_v=Σ_a (u_a)_v ψ_a`** over a *fixed* basis of k stationary measures — the frame-free analog of barycentric coordinates. Frame-free linear law ⟺ P admits such a factorization with the dual measures ψ_a within O(δ) of C_W and row-coordinates `(u_a)_v` of negative part O(δ). Route A is the special gauge where the archetypes are visible. This is gauge-invariant as an *existence* statement (so not killed by the "raw factorization gauge route" dead cert, which only kills a *fixed* frame) but is equivalent to, not smaller than, the open lemma.

## 5. DEAD-ROUTE AUDIT (item by item)
- **NO convexity-only:** every step uses P²=P (S1 row-exactness, S2 harmonicity). The failure (S6) is precisely that convex shadow composition is vacuous — I diagnose it, don't repeat it. ✅
- **Clone-invariant only:** g, φ, D, ν_v, `M⁺_deep`, the corollary, the factorization existence — all defined on geometric classes / net class weights; verified cloning-stable (fiber weights αb>0 preserve sign and sum). No raw-index path products anywhere. ✅
- **No canonical-g energy method:** g is used *linearly* (the identity `g_v=ΣP_vj g_j`), never as a quadratic energy `Γ=P(g²)−g²`. ✅
- **No ψ-gap, no max-volume/pointwise/σ-only/single-swap selectors, no finite-corner-as-asymptotic.** ✅
- **Did NOT assume v within ρ of C_W** (the coupled fact that doesn't close) — S4 derives mass bounds, assumes nothing. ✅
- **Frame fact `conv W ⊇ Δ` not used** — Route A only inspired the "clip negatives" idea; the deep-side split replaces it frame-freely. ✅
- Honest additional note: S3–S4 re-derive L5' (mod-audit); the biorthogonal reformulation is adjacent to the recorded "raw factorization gauge route" (dead) but survives as an existence statement; the overall angle overlaps the recorded DEAD routes "unlocalized dual descent" and "maximality contradictions without localization" (`10-refutations-dead-routes.tex:167-168`) — which is the point of the verdict.

## 6. VERDICT: OBSTRUCTION
Named structural reason the Arm B angle cannot close the frame-free linear law: **the exact harmonic identity at the hidden top vertex (obs-deep-leakage) upper-bounds the deep-side/visible positive coefficient mass by O(δ)/H; exactness thus provably pushes v's positive mass into the shallow near-top band, so no argument local to v's row identity can produce the required lower bound.** The linear law therefore necessarily requires a *global* band-grounding argument, which is exactly the recorded shallow-web-exclusion / anti-splitting frontier. This consolidates five separately-recorded dead routes (unlocalized dual descent, quasi-stationary potentials, maximality-without-localization, rank induction, convex shadow composition) into a single obstruction with one explicit clone-invariant identity, and confirms that the "reproduce ‖Ē‖₁≥H" framing is the convex-shadow-composition dead route in disguise (‖Ē‖₁≥H is trivially true; the needed `‖Ē‖₁≤Cδ` fails at exactly M⁺_deep≈0). Feed to the dead-route ledger.

Secondary deliverable: **obs-deep-leakage** is a clean [solid-mod-audit] frame-free/clone-invariant lemma worth banking (it is the correct-scale statement, and any future closure must consume it or its band-aggregate form `A_v(S_t∖C_W)≥(B/3−4)τ`).

## 7. NEXT PULL (wave 2)
1. **Do not seek an independent δ-scale handle at v.** obs-deep-leakage proves the deep-side mass is O(δ)/H — the "gain=slop" wall the ledger already flagged for quasi-stationary potentials. Arm B should **merge into the kernel-conjecture anti-splitting attack** (bound the number of geometrically distinct shallow quotient classes hit by `P_v⁺`), not pursue a separate linear-law route.
2. **Strategic re-scoping worth escalating to the user:** op-classical needs only the **√δ HLC** bound (`δ≥H²/C²`), not the linear `H≤Cδ`. But the frame-free √δ bound is *also* open at the *same* point — the L2' ρ-shadow recursion is "not banked" (`06-day1-belt.tex:36`). So targeting the weaker, sufficient √δ recursion-closure may be a better Arm B objective than the harder (and downstream-unnecessary) linear law. Confirm with the strategist which target Arm B should own.
3. **The one δ-scale exact rigidity that is NOT dead:** F-WR wiggle rigidity (`06-day1-belt.tex:158-166`), `‖w_i−w_j‖₁ ≤ 2.1(s_i+s_j)+4δ+2r_web²` — its `r_web²` term makes it δ-scale in a *skinny* (small-radius) web, exactly the regime where Route B dies. It is mod-audit and restricted to "self-indexed common-pattern webs." Wave 2 could test whether F-WR's mechanism grounds a skinny near-top band (i.e., whether the shallow near-top rows of S7 form a common-pattern web), the only recorded δ-scale exactness rigidity that could plausibly break M⁺_deep≈0.
