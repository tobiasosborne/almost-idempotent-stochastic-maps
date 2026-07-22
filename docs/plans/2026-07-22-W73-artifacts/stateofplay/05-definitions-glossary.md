# Vocabulary & Framing Dossier

## 1. Two pictures and the target
- op-classical (OPEN): ∃ universal η₀,C>0 (dimension-free): every row-stochastic Q with ‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀ is within C√η (max-row-ℓ¹) of a stochastic idempotent. Sharp exponent ½ (ex-hume: 3×3 family P_s=I−u_sv_sᵀ, δ=s², distance 2√δ+O(δ) to every stochastic idempotent).
- def-stochastic: row-stochastic Q≥0, Q1=1, Q²=Q; unital positive self-map of ℓ∞_n / affine retraction of Δ_n.
- def-almost-idempotent: ‖Q²−Q‖_{∞→∞}≤η, η∈[0,¼) (spectral-idempotent binomial series converges). Operator norm = max row ℓ¹ — this is WHY the bridge exponent is √η not η.
- def-signed-idempotent P (primary working object): P1=1, P²=P exactly; rows are signed measures of mass 1. Σⱼ|pᵢⱼ|≤1+2δ; pairwise ℓ¹ distance ≤2+4δ. Stochastic idempotent = signed idempotent with δ(P)=0.
- def-negative-mass: δ(P):=maxᵢ Σⱼ max(−Pᵢⱼ,0). Row polytope K:=conv{p₁..pₙ}.
- def-near-positive-projection (operator-algebra parent, UNDERUSED): exact unital idempotent R that is δ-positive (Rx≥−δ1 for 0≤x≤1). Motivating example: spectral idempotent P=θ(2Φ−1) of an almost-idempotent Φ, δ=O(η).

Signed↔stochastic dictionary (lem-classical-equiv, af-validated IN-REPO 2026-07-02):
Q stochastic, ‖Q²−Q‖≤η ⟹ P=θ(2Q−1) signed affine retraction, ‖P−Q‖≤Cη, δ(P)≤Cη. Conversely row-normalizing p_i^+ of signed P gives stochastic Q with ‖P−Q‖≤2δ, ‖Q²−Q‖≤6δ+4δ². Two-sided, quantitative.

## 2. Exposedness geometry
- Row vertex: p_v ∉ conv{other distinct rows} (coincident duplicates one point — clone-invariance built in).
- Admissible exposer h: affine, h(p_v)=0, 0≤h(p_j)≤1 all rows. t*(v):=sup_h min{h(p_j): ‖p_j−p_v‖₁≥ρ} (+∞ if no ρ-far row).
- Three scales: τ:=√δ, ρ:=4τ, κ:=τ/4. (ρ,κ)-exposed if t*(v)≥κ; else hidden.
- Visible set W(P) = (ρ,κ)-exposed row vertices; C_W = conv{p_w}. At δ=0: W = distinct rows of recurrent blocks (Högnäs–Mukherjea normal form).
- Height H(P):=maxᵢ dist₁(pᵢ, C_W); max attained at a row vertex; if H>0 that vertex is hidden (hidden top vertex). HLC target: H ≤ C√δ.
- Invisible mass σ̃_v := Σ_{j: dist₁(p_j,C_W)>0} max(P_vj,0) — includes self-mass (hazard: obs-sigma-halo-nonrobust has σ̃=5343/5000>1 all self-mass; MUST use halo-robust σ̃_g, recipients dist≥τ/4).
- Hiddenness dual witness (λ,α,β): LP dual at hidden v; λ probability on ρ-far set F_v; Σβ_i=t*(v)<κ (small-beta); balance Σλ_f(p_f−p_v)+Σα_i(p_i−p_v)=Σβ_i(p_i−p_v). Reduced: supp(λ)⊆T, supp(β)⊆O, supp(α)⊆Z (always-tight families).
- Zero-face Z(u): rows tight on the whole optimal face; every zero-face row is ρ-near u.
- Actor hull/huddle: K_T(u):=conv{p_f−p_u: f∈T(u)}, K_O(u):=t*(u)·conv{p_i−p_u: i∈O(u)}. Disjoint (g>0) = huddle/Branch I; intersecting = Branch II. Root split S1 of W54 tree.
- Co-top: row f with d_f>H−cτ (c∈{4,8}). Starved set: co-top AND ρ-far — dual-required/primal-starved tension (heart of huddle charge and conj-cotop-web-coupling).
- Top support functional φ: affine, φ(p_v)=H, φ≤0 on C_W, 1-Lipschitz. Top-deficit z_j:=H−φ(p_j)≥0; charging identity from P²=P: Σⱼa_j⁺z_j=Σⱼa_j⁻z_j≤ν_v(2+4δ).
- Slab: low/deep/very-low = exposer-value cut {h*(p_j)<s}; top/far = depth cut {d_j>H−cτ}. V_48 = {z < 48τ} (W72 wave-level, not yet a def shard).
- Near-cluster C(v): {j: ‖p_j−p_v‖₁<4τ and d_j>aτ}. Heavy top: cluster mass ≥1−θ₀.
- Selected-corner configuration: hidden-top setup with selected corner row f (ρ-far, co-top, corner inequality 2(H−φ(p_f))/D+h(p_f)≤12τ/13) + disintegration kernel ξ_x(u). Corner masses M_X (off-diagonal), M_I (diagonal intersecting), M_D (diagonal disjoint) — the X/I/D three-cell surface (SL1a).
- Pivot/chart (rank-3): actual-row chart U=(u₀,u₁,u₂); Φ_r(U)=Σᵢ max(P_{u_r i},0)E_r(i); theta-half chart (m_U≥½ max Gram volume); factorization lemma (F): S*_s(U)≤2Φ_s(U)+6δ.

## 3. Halo, gauge, starvation, foldback
- Halo: ε-neighbourhood of C_W making σ̃ robust. lem-halo-collapse (T0): H·(1−σ̃_g) ≤ (σ̃−σ̃_g)·τ/4 + ν_v(2+4δ).
- Gauge: lem-zero-face-alpha-gauge — minimal α-mass of a dual witness = conic-gauge LP on the zero face; can blow up (obs-realized-alpha-blowup A_min=1/ε).
- Starvation: lem-starvation-completion-obstruction (T0) — no rank-3 completion of the 5-actor gadget with exterior support in the canonical slab; lem-hx-robust-scalar-starvation (T0) — rank/slab-free tableau-window generalization. Mechanism: idempotence demands one unit of transverse moment vs O(τ) supply.
- Foldback: lem-l5-positive-flow-foldback — aggregate P²=P allocation bound; "no double-charging a reusable actor payer".
- DTR/POTI diagnostics (W69/W70): D_POTI := G_φ − (S/8)P_v⁺(E_*) + (c_m S/16)P_v⁺(L_v); D_EC := Z_v(q_A) − (1/8)P_v⁺(E_*) + (c_m/16)P_v⁺(L_v); D_leaf := Z_v(q_A) − c_m·τ/64 + (c_m/16)P_v⁺(L_v); proved ordered D_leaf ≥ D_EC ≥ D_POTI/S. POTI-R: S·Z_v(q_A) ≥ G_φ.

## 4. Kernel/(EX) verbatim + chain
- Kernel Conjecture: ∃ universal δ₀>0, B<∞ (n-free): every P with δ(P)≤δ₀ has (i) W(P)≠∅; (ii) every hidden v with σ̃_v>τ=√δ has dist₁(p_v,C_W)≤Bτ. B ≥ 2(2−√3)≈0.536 (corner analysis). No verified instance with σ̃_v>τ AND H>0.1τ ever produced.
- Minimality: complementary regime is the proved s8-cap: σ̃_v≤τ ⟹ H≤2(1+2δ)max{σ̃_v,ν_v}≤3τ. Kernel = exactly the missing dichotomy branch.
- (EX): ∃ C₀<∞: every P with δ≤¼ has a θ=½ actual-row basis U with max_s Φ_s(U)≤C₀δ (empirically C₀=1). With factorization: S*_s ≤ (2C₀+6)δ.
- Chain: conj-kernel ⟹ HLC (H≤C₁√δ, C₁=max{B,3}) ⟹ op-exposed-hull (P within C₂√δ of matrix with rows in C_W) ⟹ op-classical (via thm-cluster + lem-classical-equiv). All inherited arrows re-enter as proved-mod-audit.
- Stronger working form: canonical separator φ; deficit g:=H−φ(p_i) with g≥0, g_v=0, g=Pg HARMONIC, Ω≤2+4δ. Shallow band S_t={i: g_i<t}; carrier graph. Raw path-product floor REFUTED (cloning); quotient-floor (conj:quotient-floor) with clone-classes overlineP_{[i][j]}:=Σ_{b∈[j]}P_{ib} is the multiplicity-correct replacement.

## 5. Frame story
- Canonical simplex frame: R=[I_r|0] in P=ΛR, RΛ=I. Exact identity dist₁(λ,Δ)=2·neg(λ) (lem-bary-dist-neg) upgrades to (ASQ): dist₁(row, conv W) ≤ 2·max-neg, giving δ≥H/2 — PROVED ONLY IN THAT FRAME.
- Frame-free carrier now conj-skinny-shadow-cap (lem-dual-localization retired as a distance tautology; Route B vacuous in skinny μ→1 regime).

## 6. Underused angles (agent's observations)
- def-near-positive-projection: operator-algebra framing (spectral projection perturbation) essentially unexplored in-repo; natural bridge to positive-maps sibling repo.
- def-pivot chart/volume machinery: rank-3-scoped, only 3 shards use it; the (EX)/chart route is much less traveled than the LP-dual route.
- obs-sigma-halo-nonrobust / obs-realized-alpha-blowup: guardrails never mined as positive attack surfaces (when does gauge blowup regime get excluded a priori?).
- def-selected-corner's disintegration kernel ξ_x(u): general measure-theoretic tool used only inside SL1a corner-cell surface.
- QUOTIENT/CLONE-INVARIANCE APPARATUS (overlineP_{[i][j]}, quotient carrier graph; proved upstream: quotient weights clone-invariant, overlineP exactly idempotent stochastic with δ(overlineP)≤δ(P), deficit descends harmonically) — stated only in ingest kernel-conjecture.tex, NEVER re-established as argument/ shards, despite clone-invariance being mandatory (Rule 13).
