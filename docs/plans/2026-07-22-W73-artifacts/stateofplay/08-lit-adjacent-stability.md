# Literature: adjacent stability results (quantum/operator-algebraic + structural)

## Kitaev arXiv:2405.02434 (v2 Feb 2025) — the key adjacent work
- Explicitly poses the quantum sibling of op-classical as OPEN (§1.2): approximate η-idempotent UCP maps by idempotent ones with accuracy O(√η), dimension-free? "Open problem; at least, I do not know of a solution."
- Naive θ(2Φ−1) via holomorphic calculus: exact idempotent, ‖Φ̃−Φ‖_cb ≤ O(η) (eq 1.12) but NOT completely positive (Example 1.3, explicit qubit witness); a genuinely CP idempotent exists at O(√η) in that instance — positivity is the source of the √η vs η gap.
- What he proves instead: ε-C*-algebra of almost-invariant observables (Choi–Effros product X⋆Y = Φ(XY)) and Thm 2.3: any finite-dim ε-C*-algebra is O(ε)-isomorphic to a genuine C*-algebra, UNIVERSAL constant. Thm 12.3: approximate encode/decode factorization Φ ≈ ΔΥ, ‖ΥΔ−1_B‖ ≤ O(η) — linear, but ΔΥ not exactly idempotent.
- MECHANISMS (untried classically): (i) Hochschild-cohomology coboundary argument (H³=0 via a diagonal element built from Haar measure over the approximate unitary group); (ii) implicit-function-theorem construction of a C¹ approximate unitary group inside the ε-algebra; (iii) Lefschetz–Hopf fixed-point theorem to guarantee a nontrivial approximate projection as fixed point of U ↦ U⁻¹; (iv) incremental merging/extension construction of a diagonal (commutative!) target algebra block by block.
- Recommended close read: §6 (existence of nontrivial projection), §11.3, §12.

## SBD arXiv:2405.01532 — fixed-point robustness (sibling problem)
- Thm 5.2 (classical, countable alphabet, dimension-free): TP ≈_ε P ⟹ ∃ S,Q with Q≈_{√ε}P, S≈_{√ε}T, SQ=Q. Sharp (Remark 5.4, explicit 3-state example).
- Mechanism: compose with generalized depolarizing channel Φ=(1−λ)id+λTr(·)ρ; M:=Φ∘N is a strict contraction, M^k converges geometrically (Lemma 5.5), unique fixed state σ with ‖σ−ρ‖₁ ≤ ‖M(ρ)−ρ‖₁/λ; set λ=√ε. Elementary, constructive, NOT compactness.
- Same paper: Prop 4.1 compactness gives existence-only (no rate); Cor 7.3 proves an explicit structural class (bipartite, trivial on one factor) where rapid fixability PROVABLY FAILS — dimension-dependence unavoidable there. Textbook illustration: soft compactness never yields the rate; only constructive mechanisms do, and only where they exist.
- Transfer caveat: targets a single stationary vector / rank-one idempotent per orbit; op-classical needs multi-block E approximating the whole operator. But the pattern — mix Q with an already-idempotent operator at λ ~ √η + contraction argument — is concrete and UNTRIED (test first on the single-recurrent-class/near-ergodic regime).

## Negative/structural findings
- Gowers–Hatami (arXiv:1510.04085) and graph-limit stability: L²/Frobenius/cut-norm geometry, wrong for ∞→∞; no sup-norm stability-of-projection results exist in property testing. Honest negative.
- Hoffman constants (Peña–Vera–Zuluaga arXiv:2312.09858, 1905.02894, 2302.02193): fundamentally matrix/dimension-dependent, NP-hard; no dimension-free Hoffman bound for stochastic-idempotent face systems. Clean negative — do not re-open this arm.
- Tian–Xu–Fu arXiv:2312.01233 + companion: in operator norm there is NO unique nearest projection to an idempotent (unlike Frobenius) — supports combinatorial (partition+support) rather than continuous nearest-point selection.
- Ulam stability of x²=x on ordered structures: no quantitative literature. Band projections in Banach lattice algebras (arXiv:2407.09149): exact classification only.
- The exposed-hull/hidden-mass bottleneck shape (Kernel/(EX)) is NOT a named phenomenon elsewhere — project-original.
- Ultraproducts: soft only; tracial stability (Atkinson–Kunnawalkam Elayavalli arXiv:1907.03359) qualitative.

## Markov/metastability angle (second researcher)
- Deuflhard–Huisinga–Fischer–Schütte 2000 + Huisinga thesis: reversible L²(μ) spectral machinery; metastability bounds 1+κλ₂ ≤ p(τ,B,B)+p(τ,C,C) ≤ 1+λ₂ with κ ≥ 1−8cε, c=‖v₂‖_∞ NOT dimension-free; reversibility load-bearing. PCCA+ extracts soft memberships. Not transferable as-is.
- Meyer stochastic complementation / Simon–Ando / Courtois: O(ε) aggregation error, condition-number constants, known partition presupposed.
- Higher-order Cheeger (Lee–Oveis Gharan–Trevisan JACM 2014): k-way constants C(k) dimension-free in n — encouraging in spirit — but L²/reversible and extracts sets, not stochastic idempotents. GAP: nobody has redone Cheeger-type almost-invariant-set extraction in sup-norm non-reversible setting with √η guarantee.
- Dobrushin coefficients (Gaubert–Qu arXiv:1307.4649 cones/Hilbert metric): the native dual language (τ(Q)=½max_{ij}‖Q_i−Q_j‖₁), but measures single-fixed-point contraction; a near-block-diagonal Q has τ(Q)≈1 always. No literature bridge to idempotent distance.
- Newton–Schulz X ↦ 3X²−2X³: preserves row sums, NOT entrywise nonnegativity — same functional-calculus positivity failure; Kato–Chatelin eigenprojection bounds linear but resolvent/conditioning-dependent (non-normal Q) — provably insufficient alone.
- Cesàro/regularized power limit (Agaev–Chebotarev arXiv:1109.3948): exists as a genuine stochastic idempotent for ANY stochastic Q, but no rate in ‖Q²−Q‖. (NB: possible fresh angle — rate analysis of the Cesàro limit under the η-idempotence hypothesis.)
