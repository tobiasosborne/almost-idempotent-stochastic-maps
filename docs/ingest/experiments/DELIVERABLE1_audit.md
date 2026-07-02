# Deliverable 1 — Audit of the agent-B n=4 2|2 circuit dichotomy

**Status of import:** claimed-proved by agent-B (exploratory lane). I re-derived the
structural core symbolically (`asq_verifyB.py`) and the margin/collapse quantitatives
numerically (`asq_verifyB2.py`). **VERDICT: the dichotomy is correct as stated**, with
two clarifications below. I now treat its *coefficient-level* statement as VERIFIED for reuse.

## What is proved (restated precisely)

Setup: `P` is 4×4 row-stochastic (`P1=1`) exact idempotent (`P²=P`) of rank 3, so
`P = I − u vᵀ` with `Σ_i v_i = 0`, `vᵀu = 1`. In the only genuine-quadrilateral case the
signs of `v` split 2|2; after permutation/normalization `v = (a,b,−c,−d)`, `a,b,c,d>0`,
`a+b = c+d = 1`.

- **(S1) Structure** [VERIFIED symbolically]: `P1=1 ⟺ Σv=0`; `P²=P ⟺ vᵀu=1`
  (`P²−P = u(vᵀu−1)vᵀ`). The rows then satisfy the positive 2|2 affine circuit
  `a p₀ + b p₁ = c p₂ + d p₃` (C), because `vᵀP = (1−vᵀu)vᵀ = 0`.
- **(S2) Row-diameter** [VERIFIED, standard]: `‖p_i‖₁ ≤ 1+2δ`, so `D := diam₁{p_i} ≤ 2+4δ`.
- **(S3) Exposing certificates** [VERIFIED symbolically + LP]: the value vectors
  `y(p₀)=(0,1,b,b)`, `y(p₁)=(1,0,a,a)`, `y(p₂)=(d,d,0,1)`, `y(p₃)=(c,c,1,0)` each
  (i) satisfy the circuit `C_h: a y₀+b y₁ = c y₂+d y₃`, (ii) lie in `[0,1]`, (iii) vanish
  at their own vertex. Since an affine functional on `conv(rows)` is the linear
  interpolation of its vertex values, `y∈[0,1]` at all 4 rows ⟹ `h∈[0,1]` on all of `K`.
  Hence the exposing margin (min over rows that are ρ-far) is **≥ min of the other three
  values = the controlling coefficient**: `e_{p₀}≥b, e_{p₁}≥a, e_{p₂}≥d, e_{p₃}≥c` for EVERY ρ.
  LP cross-check: the measured margin is always ≥ this closed form (often = 1 when the near
  mate is dropped from the far set).
- **(S4) Collapse** [VERIFIED numerically, tight]: if the controlling coefficient is small,
  the vertex is near the opposite edge:
  `dist₁(p₀,conv{p₂,p₃}) ≤ (b/a)D`, and cyclically. Measured: `dist(p₀,conv{p₂,p₃})` matches
  `(b/a)D` to within ~5% across the P_t family and asymmetric variants.

**Dichotomy** (with `τ=√δ`, `κ=kτ`, `k≤1/8`, `δ≤1/2`): either `min(a,b,c,d) ≥ kτ` and all
four vertices are `(ρ,κ)`-well-exposed at *every* ρ; or some controlling coefficient `ε<kτ`
and that vertex is within `(ε/(1−ε))D ≤ 8kτ ≤ τ` of the opposite edge.

## Gaps / clarifications found

- **(G1) The margin bound is a LOWER bound only.** Agent-B writes `e_{p₀}(ρ) ≥ b`, and that
  is what is proved. The *true* margin can be much larger (LP shows 1.0) because dropping the
  near mate from the ρ-far set only relaxes constraints. This is fine for the dichotomy
  (we only need that the controlling coefficient *upper*-bounds when exposedness can fail),
  **but it means agent-B's certificate does NOT by itself say "failing exposedness ⟹ coefficient
  small"** — it says "coefficient large ⟹ exposed". The converse (failing ⟹ collapse) needs the
  contrapositive packaged carefully: failing `(ρ,κ)`-exposedness with this *specific* certificate
  is not failing exposedness simpliciter (some other `h` might expose). For the n=4 isolated
  case agent-B handles this by the collapse statement being about *the opposite edge*, which is a
  geometric fact independent of the certificate. **I re-prove the direction I actually need below
  (D2) rather than importing this converse.**
- **(G2) The collapse constant** `(b/a)D` was asserted; I confirmed it numerically and it is the
  correct order. The clean derivation: from (C), `p₀ = (1/a)(c p₂ + d p₃ − b p₁)`, and using
  `a+b=1, c+d=1`, `p₀ − (c p₂+d p₃) = (b/a)((c p₂+d p₃) − p₁)`, whose ℓ¹ norm is `≤ (b/a)D`.
  This is exact, not just numerical. **VERIFIED.**

## What transfers to the EMBEDDED setting (ASQ)

The n=4 result lives where **the circuit rows are ALL the rows** — there is exactly one affine
dependency (corank one), and the four exposing certificates use *only* the circuit. In (ASQ) the
circuit rows `{v₁,v₂,anchors}` sit inside a LARGER row set; other rows can shadow `v₁,v₂` and the
single global certificate need not exist. What transfers:

1. **The circuit-coefficient → margin link (S3)** is local: if a *sub-circuit*
   `a v₁ + b v₂ = (anchor combination)` exists among the rows, the same value-vector construction
   gives an exposing certificate for `v₁` with margin ≥ (coefficient of v₂ + anchors), **provided**
   that certificate extends to `h∈[0,1]` on the *whole* (larger) hull. That provided-clause is the
   embedded obstruction: extra rows impose extra `0≤h≤1` constraints. This is exactly why (ASQ)
   needs failed exposedness of *both* high vertices to do real work — it is the embedded analogue of
   "controlling coefficient small".
2. **The collapse algebra (G2)** transfers verbatim to any affine relation among rows.
3. **The structure `P=I−uvᵀ` does NOT transfer** (that was corank-one specific). In (ASQ) we only
   keep: `v₁,v₂` are rows, each has its own row-expansion `p_{v_j}=Σ_l P_{v_j,l}p_l` with the SAME
   matrix whose ‖·‖_{∞→∞} we bound, and `Σ_l P_{v_j,l}=1`. That is the exactness hook for D3 below.

**Net:** agent-B gives the right *mechanism picture* (failed exposedness ⟺ a near-degenerate
circuit coefficient ⟺ collapse toward the opposite face) and a clean, reusable collapse identity.
It does NOT directly give (ASQ): (ASQ) is the embedded, two-high-vertex, anchored version where the
cost must be extracted from the *composition* of two failed certificates, and where exactness
(P²=P) must rule out the zero-cost transient circuit. That composition is the new content below.
