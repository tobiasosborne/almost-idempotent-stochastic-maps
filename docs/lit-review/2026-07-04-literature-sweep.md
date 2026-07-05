<!--
ROLE: canonical record of the 2026-07-04 seven-lane literature sweep (user-mandated re-research).
PROVENANCE: 7 parallel read-only sonnet web-research subagents, one lane each; full scout transcripts
  live outside the repo (session scratchpad) — THIS FILE is the durable summary. Where a scout verified
  a statement against the primary full text (pdftotext/ar5iv) it is marked [scout-verified]; everything
  else is [abstract/secondary]. L1 WARNING: NOTHING here is byte-matched to refs/ yet — every claim in
  this file has repo-status `stated` until a source is pinned under refs/ and quoted verbatim.
UPDATE POLICY: append corrections only (never silently rewrite a finding); promote items to
  refs/manifest/SOURCES.md + FINDINGS.md/RESEARCH_NOTES.md as they are verified.
-->

# 2026-07-04 — Literature sweep: seven lanes against op-classical

## 0. Headline

**No lane found a prior statement or solution of `op-classical`** (row-stochastic `Q`, `‖Q²−Q‖_{∞→∞} ≤ η`
⇒ ∃ stochastic idempotent `E`, `‖Q−E‖ ≤ C√η`, dimension-free) — in Markov theory, operator algebras,
NMF/simplex geometry, spectral perturbation, semigroup theory, equation stability, or quantum information.
**The problem is genuinely open AND now externally recognized as open**: Kitaev (2024/25) poses the
noncommutative generalization verbatim as an open problem (§1.1).

## 1. Tier-1 findings

### 1.1 Kitaev, *Almost-idempotent quantum channels and approximate C\*-algebras*, arXiv:2405.02434 (v2 Feb 2025) [scout-verified, 3 independent scouts]

- Setup: UCP map Φ with `‖Φ²−Φ‖_cb ≤ η` ("η-idempotent"). Prop 3.1 (Banach-algebra, no positivity):
  `‖P²−P‖ ≤ δ < 1/4` ⇒ sign-function `P̃=θ(2P−1)` is an EXACT idempotent with `‖P̃−P‖ ≤ ‖2P−I‖·O(δ)`
  — **linear**. Then, verbatim per scouts: *"Unfortunately, Φ̃ is not guaranteed to be completely
  positive."* Example 1.3 = explicit qubit family where positivity genuinely fails (his `γ` matrix
  non-positive), with `‖Φ²−Φ‖_cb = η√(1−η)` and the remark that an idempotent UCP map O(√η)-close exists
  for that instance.
- **The open-problem statement (scout-transcribed verbatim, §1.2 p.5–6):** *"Is it possible to approximate
  all η-idempotent UCP maps by idempotent ones with accuracy O(√η) or some other function of η that does
  not depend on the space dimensionality or other parameters? This seems to be an open problem; at least,
  I do not know of a solution."*
- Theorem 12.3 (what he actually proves): approximate encode/decode factorization `Φ ≈ Δ∘Υ` through a
  genuine finite-dim C\*-algebra, both errors O(η) — sidesteps, does not solve, the positivity-correction.
- Theorem 1.2: exact idempotent UCP maps = Choi–Effros conditional-expectation structure — the
  noncommutative lift of the Högnäs–Mukherjea/Baake–Sumner partition-block classification.
- **Technique-donor lead:** §§5–9 build the target algebra *incrementally* (partitioned-index merge-and-
  extend, error-reduction bootstrap Cor 8.3 "δ-inclusion ⇒ O(ε)-inclusion independent of δ",
  Lefschetz–Hopf fixed-point existence) — a structurally different strategy from our one-shot argmin-chart
  selection; candidate alternative attack shape for Kernel/(EX).
- ⚠ CAVEATS: (i) the reduction "cb-norm on commutative domain ⇒ `‖·‖_{∞→∞}`, so classical case ≡
  op-classical" is the SCOUTS' inference, standard but NOT verified in-repo — verify before relying;
  (ii) a search engine claimed "published in Nature 638 (2025)" — checked against arXiv metadata and
  FALSE (hallucination); it is an arXiv math.OA preprint.
- Strategic value: solving op-classical resolves the commutative case of a named open problem of Kitaev.

### 1.2 Salzmann–Bergh–Datta, *Robustness of fixed points of quantum channels…*, arXiv:2405.01532 (2024) [scout-verified]

- **Theorem 5.2 (classical case):** stochastic `T`, distribution `P`, `½‖TP−P‖₁ ≤ ε` ⇒ ∃ stochastic `S`,
  distribution `Q` with `Q ≈_√ε P`, `S ≈_√ε T`, `SQ = Q` EXACTLY. **√ε, dimension-free** (Remark 5.3
  notes this *corrects a dimension-dependent thesis bound* — dimension-freeness had to be earned).
- **Remark 5.4: the √ε rate is OPTIMAL** — explicit 3-state near-swap family. → cross-check vs `ex-hume`
  (are these the same extremal mechanism?).
- **Mechanism (Lemma 5.5), transferable:** mix in a reset channel at rate λ (`M=(1−λ)N+λ·reset`), forcing
  a strict contraction; `‖P(ρ)−ρ‖ ≤ ‖M(ρ)−ρ‖/λ`; optimize `λ ~ √ε`. The gap to our problem: their
  hypothesis fixes a VECTOR (`TP≈P`), ours an idempotent MAP (`Q²≈Q`); reassembling per-class fixes into
  ONE globally consistent partition is exactly Kernel/(EX) content.
- Calibration negatives in the same paper: bipartite/local-channel case genuinely dimension-DEPENDENT
  (Cor 7.3); unital fixed-STATE version only `7d^{5/3}ε^{1/6}` (Thm 6.13).

### 1.3 The degenerate-complementarity ½-exponent mechanism [abstract/secondary — needs primary verification]

> **CORRECTION (2026-07-05, E1 primary-source audit — `docs/waves/2026-07-05-E1-error-bound-decision-check.md`):**
> the staged Luo–Pang 1994 primary does NOT make the ½ exponent directly applicable to
> `E²=E, E≥0, E𝟙=𝟙`: its ½ theorems require every quadratic NONNEGATIVE on the polyhedron
> (Assumption 4.1), and `(E²−E)_ij` is sign-indefinite on the stochastic polytope; fixed-n √ is
> not free either (staged Example 4.2: exponent ≤ ¼). Also a citation conflation below: the
> monotone-LCP error bound is Mangasarian–Shiau, Math. Programming 36 (1986) 81–89; SIAM JCO 25
> (1987) is their separate Lipschitz paper. This section's mechanism claim stands only as the
> RETARGETED arm-E programme (bespoke clone-invariant feasible-slice error bound), not as a
> citable theorem.

- Mangasarian–Shiau (SIAM J. Control Optim. 25, 1987) + Luo–Pang (Math. Programming 67, 1994; canonical
  monograph Facchinei–Pang 2003): Hölder/Łojasiewicz error bounds for quadratic systems with nonnegativity;
  **exponent exactly 1/2 at DEGENERATE solutions** (active constraint + vanishing dual slack), linear at
  nondegenerate ones. `E²=E, E≥0, E𝟙=𝟙` is literally such a system; our exposedness window (`H` capped at
  `O(√δ)`) is textbook degeneracy. **Constants are instance-dependent in the classical theorems — the
  dimension-free uniformity is exactly the open work.**
- Cross-lane coherence: everywhere the structure is UNCONSTRAINED or pre-structured, stability is LINEAR
  and dimension-free (Kazhdan 1982 amenable ε-representations, ‖φ−ψ‖ ≤ 2δ; Gowers–Hatami arXiv:1510.04085
  normalized-HS, Cε [scout-verified via ar5iv]; Christensen/Kadison–Kastler near-inclusions 14·d;
  Riesz-projection folklore = Kitaev Prop 3.1). **The positivity cone is what degrades 1 → 1/2.**
- NOTE: `RESEARCH_NOTES.md` had already queued Hoffman 1952 + Luo–Pang 1994 under arm E — the arm with
  zero pulls to date. The sweep independently re-derived arm E's rationale and strengthens it.

## 2. Tools / templates (tier 2)

- **Cape–Tang–Priebe** (Ann. Statist. 2019, arXiv:1705.10735) **Thm 4.2** [scout-verified]: deterministic,
  SYMMETRIC `X,E`; eigengap hypothesis in OUR `‖·‖_∞` norm (`|λ_r| ≥ 4‖E‖_∞`) ⇒
  `‖Û−UW‖_{2→∞} ≤ 14(‖E‖_∞/|λ_r|)‖U‖_{2→∞}`, **no incoherence needed, dimension-free**. Candidate engine
  for a reversible/symmetrizable sub-case of op-classical (comparison lemma only; rounding still ours).
- **Damle–Sun** (SIMAX 2020, arXiv:1905.07865) **Thm 5.1** [scout-verified]: the ONLY deterministic
  row-wise subspace-perturbation theorem found for NON-NORMAL matrices (Schur form; new hypothesis
  `‖T12‖₂ ≤ gap/10` = non-normality control). Not importable (2-norm hypotheses cost √n); the PROOF
  TEMPLATE redone natively in `∞→∞` using row-stochasticity is a genuine research direction.
- **Pinsker/CMI route** [abstract-verified]: classically, `I(X:Z|Y)` = exact KL to the nearest Markov law;
  Pinsker ⇒ `ℓ1 ≤ √(2·CMI)` — a dimension-free, clone-invariant √-mechanism (Fawzi–Renner lineage,
  arXiv:1410.0664). Speculative new proof shape: an entropy functional vanishing iff Q is
  partition-generated, controlled by η ⇒ √η by Pinsker.
- **Maxvol / quasi-dominance** (Goreinov–Tyrtyshnikov–Zamarashkin 1997; Mikhalev–Oseledets
  arXiv:1502.07838 restatement): swap-determinant identity ⇒ at a θ-half chart every coordinate
  `|a_t(j)| ≤ 2`, dimension-free. **This is our existing Cramer box** — external citable anchor, not new
  math. ⚠ The scout's mapping to `β_s(i)` was WRONG (β is a P-entry, not a chart coefficient).
- **Kachkovskiy–Safarov** (JAMS 2016, arXiv:1403.2021): almost-commuting ⇒ near-commuting at dimension-free
  SHARP exponent 1/2 under a structural (self-adjointness) constraint — the mature template for arguing
  "structural obstruction ⇒ √ is unavoidable". History caution (Lin's theorem): compactness proofs gave no
  constants; explicit rates took a decade of different work — expect the same for any existence-only (EX)
  proof.
- **Salzmann–Bergh–Datta Lemma 5.5 reset-trick** — see §1.2.

## 3. Negative space (verified warnings — candidate FINDINGS entries)

1. **Hitting-time/fundamental-matrix routes are NOT dimension-free** [scout-verified]:
   Thiede–Van Koten–Weare (SIMAX 2015, arXiv:1410.1431) sharp entrywise bounds have coefficients
   `Q_{ij}(S)^{-1}` that grow exponentially in state count; the theorem also degenerates to TRIVIAL at the
   reducibility boundary — exactly our regime.
2. **"Spectral gap ⇒ dimension-free separation" is provably FALSE for non-reversible doubly-stochastic
   matrices** [scout-verified]: Mehta et al. (arXiv:1909.12497): `φ(A) ≥ Δ(A)/(35n)` with a matching
   `φ ≤ Δ/√n` construction — the n-dependence is NECESSARY. (Does not touch our stronger entrywise
   hypothesis; kills generic eigengap⇒structure imports.)
3. **The modern entrywise/ℓ∞ eigenvector program is keyed to INCOHERENCE** [scout-verified across
   Abbe–Fan–Wang–Zhong, Fan–Wang–Zhong, Eldridge–Belkin–Wang, arXiv:2304.00328]: our target subspace
   (indicator-like vectors) is maximally coherent — these theorems give no improvement over weak
   Davis–Kahan here. Wrong regime, not just unlucky constants.
4. **NMF/simplex-identifiability SOTA is nowhere dimension-free** [scout-verified for Gillis–Vavasis
   arXiv:1208.1237 Thm 2 ((K/ω)² factors) and Fu et al. arXiv:2511.04291 Thm 1 (r^{9/2}, 1/σ_r)]. Our (EX)
   demand is strictly stronger than the field's best; conversely no ready-made tool exists there.
5. **Regularity/removal-lemma routes carry tower-type constants** — independent confirmation of the
   cloning/counting dead-route class (Rule 13).
6. **"Quantitative Baake–Sumner web stability" DOES NOT EXIST in the literature** [scout-checked: full
   citation tree of arXiv:2007.11433 = 9 works, all embeddability]. The inherited pointer is
   unsubstantiated — treat as a garbled upstream idea unless a locus in `docs/ingest/` is produced.
7. **PCCA+/lumpability communities explicitly lack a perturbation theory** for their own methods
   [secondary]; aggregation/lumping bounds are trajectory-error, wrong-norm, partition-as-INPUT — the
   converse of our question.
8. **The cloning obstruction is unnamed in every adjacent field** — no literature handles adversarial
   vertex-splitting; genuinely novel territory (and a publishable observation in its own right).

## 4. Acquisition queue additions (→ refs-staging/, promote per-def)

| Source | ID | Priority | Why |
|---|---|---|---|
| Kitaev 2024/25 | arXiv:2405.02434 | HIGH | open-problem statement; Prop 3.1; incremental toolkit |
| Salzmann–Bergh–Datta 2024 | arXiv:2405.01532 | HIGH | Thm 5.2 + Rem 5.4 sharpness + Lemma 5.5 reset trick |
| Luo–Pang 1994 | (already staged) | HIGH | ½-exponent mechanism — now with specific framing |
| Mangasarian–Shiau 1987 | SIAM JCO 25 | MED | companion to Luo–Pang |
| Cape–Tang–Priebe 2019 | arXiv:1705.10735 | MED | Thm 4.2 (reversible sub-case engine) |
| Damle–Sun 2020 | arXiv:1905.07865 | MED | Thm 5.1 non-normal template |
| Kachkovskiy–Safarov 2016 | arXiv:1403.2021 | MED | sharpness-argument template |
| Mikhalev–Oseledets 2015 | arXiv:1502.07838 | LOW | citable anchor for the Cramer box |
| Thiede–Van Koten–Weare 2015 | arXiv:1410.1431 | LOW | negative-space certificate |
| Mehta et al. 2019 | arXiv:1909.12497 | LOW | negative-space certificate |
| Ipsen–Selee 2011 | SIMAX 32 | LOW | ∞-norm ergodicity coefficients (π_c rounding tool; UNVERIFIED — PDF defeated scouts) |
| González-Torres 2017 | LAA (paywalled) | LOW | geometry of idempotent cores (UNVERIFIED) |

## 5. Strategic actions mirrored into bd / fr

1. Activate **arm E** (error-bound/complementarity route) — decision-check wave first (bd issue).
2. **SBD reset-trick transfer probe** + **ex-hume vs SBD sharpness family cross-check** (bd issues).
3. Ingest the two HIGH-priority sources (bd issue); verify Kitaev's commutative reduction in-repo.
4. Bank §3 items 1–2, 6 into FINDINGS.md (done same day); correct arm D's Baake–Sumner-stability line.
5. The sweep does NOT close or shortcut Kernel/(EX): the combinatorial machinery remains necessary; the
   sweep adds two genuinely different candidate proof shapes (error-bound; entropy/Pinsker) at probe cost.
