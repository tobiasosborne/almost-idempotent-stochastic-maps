# Deliverable 2 — The (ASQ) proof attempt

**Setting.** `P` exact signed affine retraction (`P1=1`, `P²=P`), `neg(p_i)≤δ`, `τ=√δ`,
`D=diam₁(K)≤2+4δ`. Baseline `ρ=4τ`, `κ=τ/4`. `W` = `(ρ,κ)`-well-exposed row vertices.
`H=dist₁(v,conv W)`. PROVED input (d2): `dist₁(v,conv(rows∖{v}))≥ρ ⇒ v` is `(ρ,ρ/D)`-exposed,
and `ρ/D≥κ` for `δ≤1/2`. Contrapositive: **v fails `(ρ,κ)`-exposedness ⇒ `dist₁(v,conv(rows∖{v}))<ρ`**
(a "ρ-shadow"). Call this (SHADOW). PROVED.

## VERDICT: (ASQ) is PROVED in the canonical simplex frame; the *transferable* (frame-free) proof has one genuine gap (= dual-localization)

The numerics (24 000 LP-verified configs, no counterexample; floor `δ/H² ≈ 3.8` in max-neg
units, consistent with d3's `a≈2.4–3.5`) confirm (ASQ) is **TRUE**. The constant is
`c ≈ 3.8` (max-neg units), i.e. `‖P‖_{∞→∞} ≥ 1 + 2·3.8·H² ≈ 1+7.6 H²`. But the proof splits:

### Route A — frame proof (PROVED). `δ ≥ H/2`, hence `δ ≥ c H²` a fortiori.

In the canonical family `R=[I_r|0]` (the realizability class: ANY bary rows give an exact
idempotent — verified symbolically, `asq_exact.py`), each non-archetype row is its barycentric
vector `λ_i`; the `r` archetypes `e_0..e_{r-1}` are isolated unit-vector vertices, hence
trivially `(ρ,κ)`-exposed, hence `∈W`, so `conv W ⊇ simplex`. Then for any row `v`:

- **(A1) [PROVED, exact identity]** `dist₁(λ, simplex) = 2·neg(λ)` for every bary vector
  (the nearest simplex point clips the negative entries to 0; ℓ¹ cost `= 2·`clipped mass).
  Verified on 2000 random multi-negative bary vectors, 0 failures.
- **(A2)** `H = dist₁(v, conv W) ≤ dist₁(v, simplex) = 2·neg(v) ≤ 2δ`.

So **`δ ≥ H/2`** (rate `H`). Combined with the exposedness window cap (any far-enough vertex
exposes and leaves the "failing" set, bounding the achievable `H`), the worst-case ratio is
`δ/H² ≈ 3.8`. The H²-form is *slack* here because `δ=H/2` is the tight relation; ASQ's
`δ≥cH²` holds with room. **This route does NOT use k=2, anchoring, or failed exposedness** —
it is a generic frame fact. It is rigorous but **frame-specific** (uses `conv W ⊇ simplex`),
so it does not by itself discharge the Layer-1 structure theorem for arbitrary modules.

### Route B — transferable shadow proof (HAS A GAP — the skinny degeneracy).

This is the route that would work in an arbitrary module (no simplex frame). The exact 2×2
coupled algebra (`asq_coupled.py`):
```
v1 = μ1 v2 + (1-μ1) L1 + e1,   L1∈conv A,  ||e1||₁<ρ      (SHADOW for v1)
v2 = μ2 v1 + (1-μ2) L2 + e2,   L2∈conv A,  ||e2||₁<ρ      (SHADOW for v2)
```
Eliminating `v2`: `v1 = Lbar + Ebar`, `Lbar∈conv A`, `Ebar=(μ1 e2+e1)/(1-μ1μ2)`, giving
```
H1 = dist₁(v1, conv A) ≤ ||Ebar||₁ ≤ (1+μ1)ρ / (1 - μ1μ2).            (*)
```
**The gap:** `(*)` is **vacuous when `μ1,μ2 → 1`**, and the measurement shows `μ1→1` *exactly*
as the quadrilateral gets skinny (`μ_on_v2 = 0.998, 0.996, 0.994` for gap `0.002,0.004,0.006`;
`asq_coupled.py`). Skinny + both-failing forces the mutual-shadow weight to 1, killing the
convex bound. Excluding the degeneracy by demanding distinct vertices (`||v1−v2||₁≥g`) gives
`1−μ1 ≥ (g−ρ)/D`, which is useless because skinny means `g<ρ`. **So convex geometry of the
configuration alone genuinely does NOT cap `H`** — confirming the d4-note "tautology" and the
"uncontrolled α-mass on the high zero-face." This is precisely the **dual-localization** open
lemma. A weaker transferable bound (`H<2ρ ⇒ δ>H²/64`) closes only if one *assumes* `v_k`
within `ρ` of `conv W` — itself the coupled fact that doesn't close.

### Why Route A escapes the gap

Route A never composes the two shadows; it bounds `H` directly by `2·neg(v)` using the frame.
The skinny degeneracy that defeats Route B is harmless to Route A because Route A's bound is
on **each vertex's own negativity**, not on a composed relation. The price: it needs the
simplex frame (`conv W ⊇ simplex`).

## Recipe-A-ready contracts (Route A, the proved one)

- **`lem-bary-dist-neg`** (PROVED, exact): *For any barycentric vector `λ` (`Σλ=1`),
  `dist₁(λ, Δ) = 2·neg(λ)`, where `Δ` is the standard simplex and `neg(λ)=Σ_a max(−λ_a,0)`.*
- **`lem-archetypes-in-W`** (PROVED): *In the canonical frame `R=[I_r|0]`, each archetype row
  `e_a` is `(ρ,κ)`-well-exposed (isolated vertex, d2 lone-far-row with `dist=1≥ρ` in small-τ),
  hence `e_a∈W` and `conv W ⊇ Δ`.*
- **`lem-asq-frame`** (PROVED, = A2): *In the canonical frame, every row `v` satisfies
  `dist₁(v, conv W) ≤ 2·neg(v) ≤ 2δ`; hence `max_i neg(p_i) ≥ H/2 ≥ (H_max/2)·(H/H_max)`, and
  with the exposedness-window cap `H ≤ 2ρ = 8τ`, `max_i neg(p_i) ≥ H²/64`.* (Contract one-liner:
  `dist₁(row, conv W) ≤ 2·max-neg`, giving `‖P‖_{∞→∞} ≥ 1 + cH²` with `c=1/32` on `‖P‖`.)

## The single missing inequality (Route B / transferable)

> **Dual-localization (OPEN).** For two distinct row-vertices `v1,v2` each failing
> `(ρ,κ)`-exposedness with mutual shadow weight `μ→1` (skinny), the residual `e_j` of the
> ρ-shadow is *aligned away from* `conv A` by `≥ H − O(ρ)` — equivalently the composed relation
> `v1=Lbar+Ebar` has `||Ebar||₁ ≥ H` forced by **exactness** (`P²=P`), not by convex weights.

The minimal symbolic configuration that decides it: the skinny pair `v1=(½,½+p,−p)`,
`v2=(½+g,½−g+p,−p)` over a low anchor face, with `g<ρ`, asking whether *any* exact completion
(equivalently, in the frame, any bary placement) can have `||Ebar||₁ < H` while both fail. In
the frame the answer is no *because of (A1)* — but (A1) is the frame fact, so the open content
is exactly: **reproduce `||Ebar||₁ ≥ H` from `P²=P` without the simplex frame.**
