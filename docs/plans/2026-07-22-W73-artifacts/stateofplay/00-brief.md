# STATE-OF-PLAY BRIEF — op-classical strategy reset (2026-07-22)

READ THIS FIRST, then the numbered files in this directory:
01-sketch-v27-tree.md (current top-down proof tree), 02-argument-dag-census.md (what is proved, at what rigour), 03-dead-routes-and-walls.md (REFUTED routes + load-bearing walls — binding constraints), 04-numerical-evidence.md (L3 evidence), 05-definitions-glossary.md (precise vocabulary), 06-wave-history.md (18 attack waves + meta-pattern), 07-lit-idempotent-stability.md + 08-lit-adjacent-stability.md (fresh literature).

## The problem (OPEN)
op-classical: ∃ universal η₀, C > 0 (dimension-free) such that every row-stochastic Q (any finite n) with ‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀ admits a row-stochastic idempotent E with ‖Q−E‖_{∞→∞} ≤ C√η. Exponent 1/2 sharp. Independently posed (noncommutative form) as open by Kitaev arXiv:2405.02434.

Equivalent working picture (lem-classical-equiv, validated, two-sided constants): exact signed idempotent P (P²=P, P1=1) with row negative mass δ = δ(P); find stochastic idempotent within C√δ. τ:=√δ.

## Where the campaign stands
- Reduction spine: op-classical ⇐ op-exposed-hull ⇐ op-hlc (H(P) ≤ C₁√δ, "height-linear cap"). op-hlc has two routes: (1) conj-kernel (ONE conjecture: hidden row vertex with halo-robust invisible mass > τ has height ≤ Bτ) — dormant, no registered attack; (2) MIN-A chain — the live route, decomposed through 4 conjectures (SL1a/SL1b/L6.5/L5-GAP-1) and then five levels deeper to current leaves RDSE + LDHR-48 (pending verification).
- 34 af-validated engine lemmas (see 02); the strongest: obs-height-collapse H·(1−σ_v) ≤ ν_v·(2+4δ); the harmonic deficit g = Pg; the foldback/ray machinery; the starvation obstruction (idempotence demands one unit of transverse moment vs O(τ) supply).
- THE EMPIRICAL SIGNATURE: 7 consecutive independent exact refuter campaigns all died at the SAME wall (tallness/exposedness absorption: pushing mass toward a hidden recipient makes it visible, H→0, before any cap is threatened). Symmetrically, every PROOF attempt stalls at the same dual wall: local ledgers are free, but turning a per-instance ledger into a class-wide (rank-uniform) bound is where everything stalls (w_*-dilution escape). 18 waves: never a counterexample, never a proof.

## Binding constraints (from 03 — non-negotiable)
1. Only clone-invariant (quotient) quantities may appear (cloning obstruction).
2. Per-class/per-wedge decompositions reimport the unproven class-count bound (anti-splitting); aggregate/global arguments dodge it.
3. Capacity arguments must live in affine-circuit-coefficient-ratio language, not raw mass (absorption/ρ-halo).
4. Dual certificates only UPPER-bound hiddenness; a primal exposer-construction mechanism is missing (dual-direction wall).
5. Near-optimal LP-dual values certify nothing; whole-optimal-face always-tightness is the terminal Route-A bottleneck.
6. Any new financing lemma: check WHICH direction it actually proves.
Numerics: linear law δ ≈ H/2 on realizable families; H/δ can exceed 2 (certified 100/49); the dangerous regime (σ̃>τ AND H>Bτ) has never been entered by any exact instance.

## Fresh assets (from 07/08 — none yet exploited)
- SBD depolarizing blend: M=(1−λ)N + λ(collapse), λ=√ε, geometric contraction, dimension-free sharp √ε for fixed-point repair (classical Thm 5.2). Untried for multi-block idempotent repair.
- Kitaev's ε-C*-algebra machinery: approximate diagonals/conditional expectations, dimension-free O(ε) rigidity; block-by-block merging construction of a commutative target algebra; Lefschetz–Hopf fixed-point existence of approximate projections. Never specialized to commutative case.
- Cesàro/regularized power limit is always a stochastic idempotent — no rate analysis exists under ‖Q²−Q‖≤η.
- Cheeger-type almost-invariant-set extraction has never been done in sup-norm/non-reversible setting.
- The quotient chain P̄ (clone classes) is itself an exact stochastic idempotent-compatible object with δ(P̄)≤δ(P), deficit descends harmonically — never re-established/exploited in-repo.
- Structure of exact stochastic idempotents: recurrent classes with one shared distribution each + transient rows convex combinations thereof. E-construction = partition discovery + distribution choice + transient assignment.
- The deficit g := H − φ(p) is EXACTLY harmonic (g = Pg) — potential theory/maximum principle never used as the engine.

## Honest rigour discipline
Anything you produce is a STRATEGY/SKETCH (conjecture-level) until proved through this repo's pipeline. Mark every step: [KNOWN-T0], [KNOWN-L5], [KNOWN-mod-audit], [NEW-ROUTINE] (you believe a competent prover closes it in one sitting), [NEW-HARD] (genuine open content), [RISK] (why it might be false/vacuous). A strategy whose hard content is hidden inside an innocuous-looking step is worse than useless — expose the hard core precisely.
