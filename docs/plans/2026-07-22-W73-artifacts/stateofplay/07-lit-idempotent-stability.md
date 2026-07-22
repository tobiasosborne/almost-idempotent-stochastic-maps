# Literature: quantitative stability of almost-idempotents

## Headline
- Kitaev, "Almost-idempotent quantum channels and approximate C*-algebras," arXiv:2405.02434 (v2 Feb 2025) EXPLICITLY poses the noncommutative generalization of op-classical as OPEN (§1.2 after eq 1.12): "Is it possible to approximate all η-idempotent UCP maps by idempotent ones with accuracy O(√η)? ... open problem." UCP under cb-norm subsumes classical stochastic under ∞→∞ (positive maps between commutative C*-algebras are automatically CP, cb = op norm).
- Salzmann–Bergh–Datta arXiv:2405.01532: sharp √ε "rapid fixability" for the SIBLING problem (approximate fixed point → exact fixed point of an exactly-repaired channel), dimension-free, incl. explicitly classical Theorem 5.2.

## Thread 1: Banach-algebra folklore
‖a²−a‖≤η<1/4 ⟹ holomorphic calculus idempotent ã=θ(2a−1) with ‖ã−a‖ ≤ O(η) (LINEAR). Spectral mapping: σ(a) within O(η) of {0,1}. The catch is precisely positivity: ã need not be positive/stochastic; the √η cost is specifically the price of the positivity repair. No standalone quantitative Hyers-Ulam-idempotent paper exists; the fact lives inside K-theory lifting lemmas.

## Thread 2: AMNM (Johnson 1986, J. London Math. Soc. 34, 489–510)
δ-multiplicative maps near multiplicative when A amenable etc. NO AMNM-type result targets positivity/CP/stochastic structure — a genuine gap ("positive AMNM" unexplored; check for negative results first). Adjacent: Oikhberg–Tradacete "Almost Band Preservers" arXiv:1610.02557 (ε-band-preserving operators on Banach lattices; stability + counterexample) — closest positive-structure analogue found.

## Thread 3: exact stochastic idempotent structure
Row-stochastic idempotent E: partition into recurrent classes C_1..C_k; within C_s all rows identical (a common distribution on C_s), zero across classes; transient rows arbitrary convex combinations of class distributions. Sinkhorn 1968 doubly-stochastic case (partitions, 1/m blocks). Refs: "A geometric study of cores of idempotent stochastic matrices" (LAA 2017); Agaev–Chebotarev arXiv:1109.3948 (regularized power limit). Descriptive only — no stability estimates.

## Thread 4: NCD/aggregation (Simon–Ando 1961, Courtois 1977, PCCA+, Michels–Siegle arXiv:2403.07618)
Aggregated stationary distribution error O(ε) given a KNOWN a-priori partition; constants depend on conditioning of aggregates. Structural mismatch: does not DISCOVER the partition from ‖Q²−Q‖≤η alone and is not dimension-free. Evidence the partition-discovery step is exactly our problem's isolated difficulty.

## Thread 5: quantum program (the key thread)
- Kitaev Example 1.3: rank-2 2×2 quantum example where θ(2Φ−1) is not CP; genuine idempotent UCP map only at cost O(√η) — same mechanism (positivity repair costs the square root).
- Kitaev Thm 2.3: finite-dim ε-C*-algebra is O(ε)-isomorphic to a genuine C*-algebra, DIMENSION-FREE constant (uses approximate conditional-expectation/"diagonal" techniques à la Johnson).
- Kitaev Thm 12.3: constructs genuine finite-dim C*-algebra B and UCP Δ,Υ with ‖ΔΥ−Φ‖_cb ≤ O(η), ‖ΥΔ−1_B‖_cb ≤ O(η) — approximate factorization LINEAR in η, but ΔΥ not exactly idempotent. Stops short of the open question.
- No later paper resolves it (checked citing works through Nov 2025, incl. arXiv:2511.16299 Delsol–Fawzi–Gao–Rahaman on emulation capacity between idempotent channels).
- SBD Thm 5.1/5.2 (classical): given N(ρ)≈_ε ρ, construct exact fixed-point pair: σ≈_{√ε}ρ, M≈_{√ε}N, M(σ)=σ, DIMENSION-FREE, via generalized-depolarizing blend Φ=(1−√ε)·id + √ε·Tr(·)ρ (classical: M=(1−√ε)N + √ε·(rank-one onto repaired ρ)). Remark 5.4: √ε optimal via explicit classical 3-state example T_ε = [[1−√ε, √ε],[√ε, 1−√ε]] ⊕ [1] — the classical cousin of ex-hume. Norm: sup_x Σ_y |T_xy − S_xy| (≡ ∞→∞ up to convention).

## Thread 6: ultraproducts/compactness
Compactness could convert a UNIFORM qualitative statement into a non-explicit C(η)→0, but cannot bypass a genuine finite-dim quantitative argument and yields no exponent. SBD themselves use "a compactness argument" for the general non-explicit case. Quantitative K-theory ((ε,r,N)-idempotents, arXiv:1611.08790 line) is aimed at K-invariants, not norm-distance stability, no positivity.

## Strategic flags
1. SBD's depolarizing blend is the most concrete reusable machinery: candidate for building E row-by-row / repairing structures at √η blending cost. Note the blend trick pays √ε ONCE, globally — mirrors the "one unit of transverse moment vs O(τ) supply" starvation mechanism.
2. Kitaev's ε-C*-algebra machinery (approximate conditional expectations, dimension-free O(ε) rigidity) specialized to the commutative case has NOT been mined.
3. "Positive AMNM" is an unexplored program.
4. Independent corroboration: the sharp exponent and the "positivity is the hard part" diagnosis are confirmed by sources with no connection to this project.
