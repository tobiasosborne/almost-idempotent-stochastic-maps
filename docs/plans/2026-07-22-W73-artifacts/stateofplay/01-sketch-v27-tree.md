# Sketch v27 — full top-down tree (2026-07-16)

Structural note: below conj-l5-gap-1 only POTI-0/POTI+ are registered conjecture shards; the intermediate nodes (S/C/I, I-cap, D-cap, A-esc, T-esc, G<4, C0, N, HES, DTR, the I-horn and I-cap six-leaf sets) exist only in wave strategy docs.

## Root and trunk
- op-classical (open) ⇐ prose route via op-exposed-hull; registry deps thm-classical-factorization + prop-approx-simplex (proved-mod-audit).
- Signed normalization lem-classical-equiv (T0): P:=θ(2Q−I), P²=P exact, δ(P)≤Cη; converse row-normalization.
- Affine frame + row reproduction: rank k=tr P, rows in (k−1)-dim affine subspace; everything downstream clone-invariant (the only known route past the cloning obstruction).
- op-exposed-hull (open): every row within C√d of conv W. Deps: lem-hlc-implies-exposed-hull + op-hlc.
- op-hlc (open): H(P)≤C₁√δ. Disjunctive routes: [lem-kernel-implies-hlc; conj-kernel] OR [lem-min-a-implies-height].
- Sharpness: ex-hume (proved-mod-audit) 3×3 family P_s=I−u_s v_sᵀ + SBD arXiv:2405.01532 Rem 5.4 anchor.

## Route "Kernel" — DORMANT since ~v9/W44
conj-kernel OPEN (W≠∅ + hidden v with σ̃_v>τ ⟹ dist ≤ Bτ). conj-ex separate route, never proved equivalent (DC4). Lemma-K engine stalled at conj-degenerate-transport (af: seeded), conj-rh, conj-sc.

## Route "MIN-A" — THE LIVE ROUTE
- lem-min-a-implies-height (proved; assuming conj-min-a-w4: H ≤ 13√δ at δ≤(17−12√2)/2).
- conj-min-a-w4 OPEN: at H>13τ some hidden top v has σ₄(v)≤1/2.
- ⇐ lem-low-slab-cap-implies-min-a (proved; near part conj-low-slab-cap + far part lem-cs-low-slab-pincer T0).
- conj-low-slab-cap OPEN (theta-flexible): at H>((5a/4+3/2)/θ)τ some hidden top has ≤1−θ−4τ mass on the θ-shadowed near-slab.
- ⇐ lem-absorption-implies-low-slab-cap (proved; deps conj-near-cluster-absorption + conj-far-low-slab-cap).
- conj-near-cluster-absorption OPEN ("five-route convergence point"): near-cluster mass ≤ 1−θ₀.
- ⇐ lem-huddle-charge-assembly (proved CONDITIONAL, DO-NOT-CONSUME): assuming SL1a + SL1b + L6.5 + conj-l5-gap-1, no P with H>16τ carries ≥7/8 positive mass on its 4τ-near >16τ-deep cluster.

CONDITIONAL SURFACE = EXACTLY FOUR CONJECTURES (W68):
(a) SL1a conj-straddling-web-exclusion — reduced (proved) to three σ-cells:
    H-D conj-sl1a-deep-diagonal-cell; H-I conj-sl1a-intersection-diagonal-cell; H-X conj-sl1a-off-diagonal-cell (ACTIVE — Route A: X2 microfreight, X3F/X3N, X4; consumes T0 H-X engine bank W60/W61).
(b) SL1b conj-shallow-counterweight-exclusion — graded most attackable; small-gauge bridge {SL1a+SL1b ⇒ impossible} hostile-checked at A₀≤3/32 but UNCODIFIED.
(c) L6.5 conj-cotop-web-coupling — the λ-vs-P⁺ wall. Gauge-split: small (bridged), moderate (needs NEW "mixed co-top straddle exclusion"), large (global projection-completion obstruction in P=LB, BL=I).
(d) conj-l5-gap-1 — dual-face mass minimax: some φ with Σ_{j∈A}P_vj⁺(H−φ(p_j)) ≥ c₅·c_m·τ.
    Decomposition (wave-doc tier): → S/C/I → I → I-cap → D-cap → {A-esc, T-esc, G<4, C0, N} → A-esc = HES + DTR → DTR ⇒(W70 verified) POTI-0 + POTI+ via lem-dtr-poti-assembly.

## Open-leaf state
- S: blocked at hiddenness + top-row τ² budget. C: complete near-refuter except tallness. I-cap: exact calibrations with ZERO top ownership — tall top ownership is the obstruction, not intersection. D-cap: canonical gadget fails negativity by order one. A-esc: no family reaches the actorization window. T-esc: only with order-one finance-row negativity. POTI-0: W69/W71 deciders blocked (rank-uniform global-gate failures; exact ownership law family-specific). POTI+: untouched. HES: untouched (macroscopic h_u≥τ/32 subcase planned).
- W72 (UNVERIFIED): POTI-0 == S0+RX+O48+ASM2 (routine, standalone-proved) + RDSE + LDHR-48 (creative, open).
- Parked legacy conjectures: tall-zero-face-radial-thickness, zero-face-elimination, rank3-cluster-zero-face-reach, summit-cylinder-exclusion, tall-bounded-alpha, top-deficit-coupling, downhill-zero-face-lower-mass, b-restricted, degenerate-payment, no-free-frontier, skinny-shadow-cap.

## Conditional (never consume conclusions unconditionally)
lem-huddle-charge-assembly; lem-dtr-poti-assembly; lem-min-a-implies-height; lem-low-slab-cap-implies-min-a; lem-absorption-implies-low-slab-cap.

## Constants ledger (per-node)
τ=√δ. MIN-A calibration (a,θ)=(4,1/2) → H≤13τ at δ≤(17−12√2)/2. Huddle: δ₀=min{δ_a,δ_b,δ_c,δ_5(c*/2),1/4,(c₅c*/6)²}, 7/8 threshold. L5 tree: c_m=1/4, b=c_m/128, δ_rt=min(2⁻¹⁶,(c_m/4)²,(c_m·b/120)²), D₀=2+4δ, Tail₁>τ/8 (τ/15 fixed-K, ceiling δ≤(3K+19)⁻²), guarded hull split 1/160, common-tail floor τ/2560, TC loss r₀αλ/(16S), D-cap γ_dis=7c_m/960, POTI target Z_v(q_A) ≥ (1/8)P_v⁺(E*) − (c_m/16)P_v⁺(L_v). SL1a cells δ∈(0,2⁻¹⁶]; barycenter ≤11√δ/5, exposer ≤4√δ/13. Starvation obstruction ceiling τ≤1/256. Kernel B ≥ 2(2−√3)≈0.536.

## v25→v27 diffs
v26: D-cap deciders all blocked (6th bind); A-esc decomposed on proved τ/8-tail interface; assembly bridge repaired (four-conjecture surface exact). v27: DTR→POTI verified (cleanest batch), registry 200, Route A decided. Pending v28: W72 verification → lem-poti0-*×4 + conj-poti0-*×2 (registry ~206); Tier-1 leaf set becomes POTI-0 == RDSE + LDHR-48.
