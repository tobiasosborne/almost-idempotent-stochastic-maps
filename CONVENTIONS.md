<!--
ROLE: notation / normalisation registry (append-only, lettered). Record a convention BEFORE relying on it.
UPDATE POLICY: append a new lettered entry; never silently repurpose a letter. HOW-to-work is in CLAUDE.md.
TRIGGER: introducing or changing any notational / sign / indexing / normalisation / tolerance choice.
-->

# CONVENTIONS

Every notational, sign, indexing, normalisation, scale, or tolerance choice must be recorded here
**before** it is relied upon (a scientific bug is a convention bug until proved otherwise). Definitions
themselves live in `definitions/` (one shard per term); this file records the *global conventions* that cut
across shards. Append-only, lettered.

## (a) Claim status = rigour rung (mirror of CLAUDE.md L0)

Every `argument/` shard carries a `status:` that IS its rung on the rigour ladder:

| status | rigorous? | meaning |
|--------|:---------:|---------|
| `cited` | ✅ | byte-matched to a genuine theorem in a `refs/` source |
| `proved` | ✅ | independently proved / `af`-validated in-repo |
| `consensus` | ✅ | agreed project-internal (recorded sign-off) |
| `stated` | ❌ | transcribed from a source, unchecked |
| `proved-mod-audit` | ❌ | a paper-proof from the ingested classical-portfolio, NOT yet independently reviewed / `af`-validated **here** (the workhorse status for inherited results) |
| `conjecture` | ❌ | an explicit conjecture (incl. the Kernel/(EX) conjecture) |
| `heuristic` | ❌ | informal / asymptotic argument |
| `numerical` | ❌ | supported only by a `runs/` bundle — NEVER rigorous |
| `open` / `obstruction` / `disproved` | ❌ | the frontier / the no-gos / refuted |

A `proved-mod-audit`/`conjecture`/`heuristic`/`numerical`/`stated` result may NOT be a dependency of an
`af:validated` result — the linker enforces this (only `cited` leaves and `af:validated` deps are
"available"). **`lem-classical-equiv` was `af`-validated upstream but re-enters here as `proved-mod-audit`
until re-validated in-repo** — nothing is rigorous until re-established under this repo's discipline.

## (b) Stochastic and signed formulations

- `ℓ∞_n = ℝⁿ` with the sup norm; the probability simplex `Δ_n = {x ≥ 0 : Σx_i = 1}`.
- A **row-stochastic matrix** `Q` (`Q ≥ 0` entrywise, `Q1 = 1`) is a unital positive map of `ℓ∞_n` / an
  affine self-map of `Δ_n`. A **stochastic idempotent** `E` is row-stochastic with `E² = E`.
- **Map norm.** `‖·‖_{∞→∞}` is the operator (row-sum) norm on maps of `ℓ∞_n`; "almost idempotent with defect
  η" means `‖Q² − Q‖_{∞→∞} ≤ η`, `η ∈ [0, ¼)` (the range that makes the spectral-idempotent binomial series
  converge). Always state which norm; record any deviation at point of use.
- **Signed formulation (exact idempotence).** A **signed affine retraction / signed idempotent** `P` has
  `P1 = 1` and `P² = P` **exactly**, rows are signed measures of total mass 1. This is the primary working
  object; results are frequently stated here and transferred to the stochastic picture via
  `lem-classical-equiv` **up to universal constants**. Always name which picture (stochastic `Q` vs signed
  `P`) a bound lives in, and cite the equivalence when crossing.

## (c) Scales, negative mass, and the geometry

- **Negative mass** `δ = δ(P) = max_i Σ_j max(−P_ij, 0)` (the signed-picture defect). Range of interest
  `δ ≤ ¼`; the **corner scale** is `δ ≈ 0.233` (above it, tall hidden configurations exist and are certified;
  below it the dangerous antecedent has never been entered).
- **Derived scales:** `τ = √δ`, `ρ = 4τ`, `κ = τ/4` (the (ρ,κ)-exposedness window).
- **Height** `H = H(P)`, **invisible mass** `σ̃_v` of a row vertex `v`, **visible/exposed set** `W(P)`
  (see `def-height`, `def-invisible-mass`, `def-visible-set`). **Sharp exponent:** distance-to-idempotent
  scales like `√δ` (equivalently `√η`), certified sharp by `ex-hume`.
- **The linear law.** The realizable-family relation is `δ = H/2` (LINEAR); the `δ ≳ H²` form is only the
  worst-case envelope and binds only because `H ≤ O(τ) = O(√δ)`. State which one a claim rests on
  (`FINDINGS.md`).

## (d) Charts and the (EX)/factorization vocabulary

- **θ-½ actual-row chart** `U` (`def-actual-row-chart`, deferred until first used): an actual-row basis with
  `P = LB`, `BL = I_k` in the θ=½ frame. **Weighted signed-face excess** `Φ_s(U)` and the class score `S*_s`.
  The proved-mod-audit factorization is `S*_s(U) ≤ 2·Φ_s(U) + 6·δ(P)` (constants `(a,b)=(2,6)`, tight);
  composing with (EX) `max_s Φ_s ≤ C₀·δ` gives `C_sf = 2·C₀ + 6` (= 8 at `C₀ = 1`).

## (e) Numerical hygiene (mirror of runs/README.md + data/SCHEMA.md)

- Prefer **exact / rational / interval arithmetic** and boolean/LP certificates over floats (the inherited
  67k-instance record is exact-arithmetic). CSV column suffixes `_exact` / `_float` / `_residual`; a
  `#`-leading first cell is a sentinel comment, not data. Floating diagnostics declare tolerance and norm.
- A numerical result is `numerical` (L3) forever — quarantined to a `runs/` bundle with a re-run command
  and a SHA256; "0 violations over N instances" is evidence, never a theorem.

## (f) Identifiers

- Definitions: `def-<kebab-slug>`. Results: `lem-|thm-|prop-|cor-|op-|obs-|conj-<kebab-slug>` (`op-` =
  open-problem, `obs-` = observation/obstruction, `conj-` = conjecture). Source-ids: `baake-sumner-2007.11433`,
  `hognas-mukherjea`, … (see `refs/manifest/SOURCES.md`). Report shards: `AISM-NN-LABEL`. `fr` arms are
  single letters `A,B,C,…`.
