# Argument Registry Census (200 results; linker clean, 32 ready / 94 blocked)

## Rigour census
- proved (in-repo paper proof): 147 · conjecture: 31 total conj- shards (29 open + conj-ex) · proved-mod-audit (inherited): 14 · open trunk: 3 (op-classical, op-exposed-hull, op-hlc) · numerical: 2 (obs-linear-law-finite-delta, obs-sigma-halo-nonrobust) · heuristic: 2 (obs-deep-leakage, obs-fwr-gap) · disproved: 2 (conj-gamma-emptiness, conj-nsc) · obstruction: 1 (lem-dual-localization, retired).
- af: validated 34, seeded 10, none 156.
- Every result touching the geometric spine toward op-classical bottoms out in at least one open conj-*.

## The af-validated T0 core (34) — the engine bank
Pure convex/linear-algebra primitives: lem-weighted-min; lem-negpart-subadditive (n(x+y) ≤ n(x)+n(y)); lem-zerosum-triangle; lem-fan-payment (min_{i*} Σ p_i n(w_i−w_{i*}) ≤ 2Σ p_i n(w_i) for zero-sum-barycenter family); lem-fan-payment-restricted (constant 2+√2); lem-residual-lower (convex outsourcing); lem-residual-upper.

Signed-idempotent structural identities: lem-mass-split (Σ a_j^+ = 1+ν_v); lem-harmonic-affine-bridge (Pg=g iff g_i=u·p_i); lem-row-zero-capacity; lem-row-far-dual-certificate; lem-hiddenness-dual-witness; lem-hiddenness-depth-markov; lem-always-tight-dual-support; lem-cs-low-slab-pincer; the height-collapse family lem-halo-collapse / lem-depth-d-halo-collapse / lem-parametric-halo-collapse / obs-height-collapse: H·(1−σ_v) ≤ ν_v·(2+4δ) — the single most-used validated lemma; lem-top-concentration; lem-top-slab-companion; lem-genuine-disintegration.

Rank-3 pivot/chart calculus: lem-collateral-import, lem-cross-pivot-cancellation, lem-import-reduction, lem-factorization, lem-pivot-removing-move.

HX/starvation engine (owner B): lem-hx-transverse-moment-identity, lem-hx-signed-variation-ledger, lem-hx-financing-floor, lem-hx-forced-exterior-coupling, lem-hx-robust-scalar-starvation, lem-starvation-completion-obstruction.

Bridge: lem-classical-equiv (signed ↔ stochastic up to universal constants; re-validated in-repo 2026-07-02, 29-node tree).

## The L5 tier (proved, reviewer≠author, NOT af)
DTR/POTI chain (owner B): lem-dtr-poti-assembly — Assume conj-dtr-zero-oriented-surplus-exclusion AND conj-dtr-positive-oriented-surplus-gap-exclusion. Then every I-base datum satisfies Z_v(q_A) ≥ (1/8)·P_v^+(E_*) − (c_m/16)·P_v^+(L_v). Feeders: lem-dtr-canonical-overlap, lem-dtr-oriented-tail-ray-conversion (S·Z_v(q_A) ≥ G_φ), lem-dtr-tail-coherent-conversion (Z_v(q_A) > (r_0αλ/(16S))·τ), AESC family. NOTE: NOT wired into op-classical's 44-result ancestor closure — currently an orphaned side-arm.

On-spine conditional bridges (all "consuming conclusion unconditionally is illegal"):
- lem-kernel-implies-hlc (Kernel ⇒ HLC, H ≤ max{B,3}·τ)
- lem-hlc-implies-exposed-hull (HLC ⇒ pinned-δ exposed-hull; loose-δ robustness clause NOT proved)
- lem-min-a-implies-height (conj-min-a-w4 ⇒ H ≤ 13τ, B=13)
- lem-low-slab-cap-implies-min-a (conj-low-slab-cap at a=4,θ=1/2 ⇒ conj-min-a-w4)
- lem-absorption-implies-low-slab-cap (conj-near-cluster-absorption + conj-far-low-slab-cap ⇒ conj-low-slab-cap)
- lem-blocker-capacity-bridge (conj-downhill-zero-face-lower-mass ⇒ (T2) capacity contradiction)
- lem-huddle-charge-assembly (conj-straddling-web-exclusion + conj-shallow-counterweight-exclusion + conj-cotop-web-coupling + conj-l5-gap-1 ⇒ ≥7/8 mass-exclusion at a tall hidden top)
- lem-sl1a-three-cell-reduction (three conj-sl1a-* cells ⇒ SL1a bridge measure bound)

## All open conjectures (verbatim gist)
Route-2 MIN-A spine: conj-low-slab-cap (universal a>0, θ, δ_0: tall hidden top's optimal exposer has low-slab genuine-mass ≤ 1−θ−4τ); conj-near-cluster-absorption ("THE remaining Route-A conjecture — five-route convergence point": mass v places on its ρ-near deep cluster ≤ 1−θ_0); conj-far-low-slab-cap; conj-straddling-web-exclusion (SL1a — "the unified rigidity core": no P admits a probability λ on ρ-far co-top rows with barycenter within 2.2τ of p_v and average value ≤ (16/13)κ); conj-shallow-counterweight-exclusion (SL1b, "attack FIRST"); conj-cotop-web-coupling (Σ far/co-top P_vj^+ ≥ c_*); conj-l5-gap-1 (some φ: Σ_{j∈A} P_vj^+·(H−φ(p_j)) ≥ c_5·c_m·τ); conj-sl1a-off/deep/intersection-diagonal-cell (M_X/M_I/M_D caps); conj-downhill-zero-face-lower-mass.

Route 1: conj-kernel — universal δ_0>0, B<∞ (n-free): every exact signed idempotent P with δ≤δ_0 has W(P)≠∅ and every hidden row vertex v with σ̃_v > τ=√δ satisfies dist_1(p_v, C_W) ≤ B·τ. Feeds op-hlc via lem-kernel-implies-hlc. NO active proof attempt registered; deps empty.

Third route (unconnected either way, DC4 audit): conj-ex — every rank≥3 P with δ≤1/4 admits a θ-1/2 actual-row chart U0 with Vol ≥ (1/2)Vol_max and max_s Φ_s(U0) ≤ C0·δ (C0=1 empirically; C0<1 refuted).

Zero-face/absorption family: conj-zero-face-elimination, conj-rank3-cluster-zero-face-reach, conj-tall-zero-face-radial-thickness, conj-tall-bounded-alpha, conj-top-deficit-coupling, conj-summit-cylinder-exclusion, conj-no-free-frontier, conj-skinny-shadow-cap (supersedes retired lem-dual-localization; "the frame-free transferable statement").

DTR/POTI residuals: conj-dtr-zero-oriented-surplus-exclusion (POTI-0), conj-dtr-positive-oriented-surplus-gap-exclusion (POTI+).

Rank-3 orphan-repair (0 dependents): conj-rh, conj-sc, conj-b-restricted, conj-degenerate-payment, conj-degenerate-transport.

## The dependency spine
```
op-classical ⇐ thm-classical-factorization[pma] AND prop-approx-simplex[pma]
thm-classical-factorization ⇐ thm-cluster[pma] AND op-exposed-hull
op-exposed-hull ⇐ lem-hlc-implies-exposed-hull[L5] AND op-hlc
op-hlc ⇐ {Route 1: conj-kernel[OPEN] + lem-kernel-implies-hlc[L5]}
       OR {Route 2: lem-min-a-implies-height[L5] ⇐ conj-min-a-w4[OPEN]}
conj-min-a-w4 ⇐ lem-low-slab-cap-implies-min-a[L5] ⇐ conj-low-slab-cap[OPEN] + lem-cs-low-slab-pincer[T0]
conj-low-slab-cap ⇐ lem-absorption-implies-low-slab-cap[L5] ⇐ conj-near-cluster-absorption[OPEN] AND conj-far-low-slab-cap[OPEN]
conj-near-cluster-absorption ⇐ lem-huddle-charge-assembly[L5] ⇐ SL1a + SL1b + conj-cotop-web-coupling + conj-l5-gap-1 [all OPEN]
conj-straddling-web-exclusion ⇐ lem-sl1a-three-cell-reduction[L5] ⇐ three conj-sl1a-* cells [OPEN]
```
Full ancestor closure of op-classical: 44 nodes, 12 open conjectures.
- Route 1 (Kernel): ONE open conjecture closes everything — shortest route, but conj-kernel has no registered attack.
- Route 2 (MIN-A): 11 open conjectures, all recent effort (W38–W68).
- conj-ex: third, unconnected route.

## Linker frontier
0 errors; 6 brittleness WARNs (oversized af trees: lem-residual-upper 52 nodes etc.). 32 ready shards (af-elevation candidates incl. lem-top-deficit-price, lem-ihorn-tall-halo-saturation, lem-wedderburn-deflation, lem-signed-carre-du-champ, lem-clone-invariant-row-complexity...). 94 blocked (everything downstream of conj-*).
