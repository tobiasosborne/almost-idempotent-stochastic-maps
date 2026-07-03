<!--
ROLE: live subtleties/gotchas — "true and easy to get wrong", dated. NOT retracted claims (those go in
  docs/LEARNINGS.md). HOW-to-work is in CLAUDE.md; scope in PRD.md.
UPDATE POLICY: append dated entries; prune only when a gotcha is fully internalised into a gate/def.
TRIGGER: discovering a subtlety that a future agent (or you post-compaction) would plausibly get wrong.
-->

# FINDINGS — live subtleties (dated; "true and easy to get wrong")

## 2026-07-02 — founding faithfulness flags (the inherited classical-portfolio is mostly NON-rigorous)

- ❌ **Treating the ingested classical-portfolio as rigorous.** It is a *campaign record* from
  `../almost-idempotent-positive-maps`, honestly self-tagged PROVED-mod-audit / NUMERICAL / CONJECTURAL /
  OPEN / REFUTED. Only **one** classical result cleared an `af` validation upstream (`lem-classical-equiv`,
  the signed↔stochastic bridge) — and it re-enters here as `proved-mod-audit` until re-validated in-repo.
  Everything else is `proved-mod-audit`/`conjecture`/`numerical`/`open` (`CLAUDE.md` L0).
- ❌ **"δ ≳ H²" as the mechanism.** The realizable-family relation is **linear `δ = H/2`**; the quadratic is
  only the worst-case envelope, binding because `H` is capped at `O(τ)=O(√δ)` by the exposedness window.
  State which one a claim rests on (`CONVENTIONS.md` (c)). The `√η`/`√δ` distance exponent is nonetheless
  **sharp** (`ex-hume`, Hume's 3×3 family).
- ❌ **Frame-specific ⇒ frame-free.** The exact identity `dist₁(λ,Δ) = 2·neg(λ)` gives `δ ≥ H/2` **in the
  canonical simplex frame** (proved); the transferable (frame-free) statement is exactly the OPEN
  `lem-dual-localization` gap (Route B is vacuous in the skinny `μ→1` regime). Never present the
  frame-specific proof as the general one.
- ❌ **Signed vs stochastic drift.** Bounds live in an equivalent **signed** picture (exact idempotence,
  negative mass `δ`) linked to the stochastic picture (`‖Q²−Q‖ ≤ η`) by `lem-classical-equiv` up to
  universal constants. Always say which picture a bound is in; cite the equivalence when crossing.
- ❌ **Numerical agreement ⇒ theorem.** 67k+ exact instances with `0` (EX)-violations (worst
  `min_U max_s Φ_s/δ = 1`; worst `H/δ = 2.000000000013`) is `numerical` (L3), quarantined to `runs/`, never
  promoted. Below the corner scale (`δ ≈ 0.233`) the dangerous antecedent has *never been entered* — that is
  evidence, not a proof.

## 2026-07-02 — DEAD ROUTES (do NOT re-walk; Rule 13). Read the certificate before "but this time…".

- ⛔ **Raw-index path-product floors.** Index-level path products are **refuted outright for any
  `δ₀ ≥ 0.233`** (the *cloning obstruction*): duplicating a state ("cloning") leaves the map invariant but
  breaks any raw-index floor. **Only clone-invariant (quotient) quantities may appear in a proof.** This
  killed conjectures 2–3's naive forms.
- ⛔ **Coefficient-only LP support-cleanup** (the "pushed-witness death certificate").
- ⛔ **Universal `C ≤ 2`** (refuted); **`C₀ < 1`** in (EX) (refuted — transverse pair at `a=¼` gives
  `Φ/δ = 5/4`); **exists-exact-max-volume** selectors and arbitrary max-volume tie-selection (fail).
- ⛔ **Pointwise / σ-only / single-swap selectors**, **Jensen/convexity**, the **canonical-`g` energy
  method**, the **literal ψ-gap**, and **finite-corner-as-asymptotic** — all recorded refuted upstream.

*(Full death certificates live in the ingested `docs/ingest/report/main.tex §10` and
`docs/ingest/report/STATUS-LEDGER.md`. When the ingest agent finishes, cross-link them here.)*

## 2026-07-02 — infrastructure notes

- The `argument.py` linker carries a repo-specific status token **`proved-mod-audit`** (beyond the ported
  set) for inherited paper-proofs; it colours ORANGE (dashed, non-rigorous) in `argument/DAG.md` and
  status-propagation treats it like `stated`: **an `af:validated` result can never rest on one.**
- `check-report-shards.sh` (ported from `../arithmetic-quantum-mechanics`, re-prefixed `AISM-`) is invoked
  with **`bash`** (not `sh`) from `check-all.sh` — it uses `mapfile`/`declare -A`/`pipefail`. It passes an
  empty scaffold cleanly (0 includes + 0 shard files).
- `af` binary path is parameterised via `AF=${AF:-/home/tobias/Projects/vibefeld/af}` in
  `af-orchestrate.py` / `seed-af-workspaces.py` (also resolves `af` on PATH — it is at `~/go/bin/af`).
- `fr` banking oracles are **deferred**: banking a claim (`▣`) needs a claim-specific external oracle (an
  `af` workspace validation, or a numerical certificate re-run). Register one in
  `.frontier/portfolio.json → config.oracles` when the first bankable claim exists — do NOT register a
  coarse "gate" oracle (it would pass any claim, defeating the anti-gaming purpose).

## 2026-07-02 — constants PINNED (strategist read of the ingest record; closes aism-8bi / aism-z48)

- ✅ **C₀ in (EX): the EXISTENTIAL constant is exactly 1 empirically; 5/4 is a SELECTOR floor.** Over the
  278 valid rank-3 `δ≤¼` exact instances (w41_ex), worst `min_U max_s Φ_s(U)/δ = 1`, ATTAINED (transverse
  pairs `a=1/8`, `a=1/4`; no-center paths) — so `C₀<1` is impossible and `C₀=1` is tight for the
  existential form. The `5/4` belongs to cheap SELECTORS (worst max-volume tie / peeled / min-neg-mass;
  3–4 violators each; sharp witness = transverse pair `a=¼`: Φ-argmin gives `Φ/δ=1`, bad tie `5/4`).
  Loci: `docs/ingest/experiments/out/w41_ex/proof.md` (selector + family tables);
  `docs/ingest/report/kernel-conjecture-v2.tex:223–235`. **Strategic consequence (Arm A): `C_sf=2C₀+6`
  tolerates ANY universal `C₀` (1→8, 5/4→8.5) — do not fight for the aesthetic 1; a robust selector with
  any universal constant discharges `op-classical`.**
- ✅ **`H/δ = 2.000000000013` is FLOAT noise from LOCAL numerics — NOT the exact record.** The figure comes
  from the local (float) search near the H–M locus (`docs/ingest/report/kernel-conjecture.tex:418`, "local
  numerics give worst stable ratio"); the 67k exact record supports `δ ≥ H/2` with zero exceptions
  (`docs/ingest/OVERVIEW.md:87` conflates the two sources). The linear-law constant is exactly 2
  conjecturally (`δ = H/2` tight on realizable families); `H ≤ 2δ` is the right Arm B/C target. Do NOT
  quote `2.000000000013` as an exact-arithmetic exceedance — it corrects the attribution in the founding
  entry above ("worst `H/δ = 2.000000000013`" under "67k+ exact instances").

## 2026-07-02 — web-regime hunt (arm F wave 1): collapse bound, σ̃→1 re-scope, and a linear-law CORRECTION

- ✅ **CORRECTION to the entry above: "δ ≥ H/2 with zero exceptions" is FALSE at finite δ.** A certified
  exact 5×5 instance (`runs/2026-07-02-web-regime-hunt/`, `verify_instance.py`; independently recomputed
  by the orchestrator) has `δ = 49/2000`, `H = 1/20`, so **`H/δ = 100/49 ≈ 2.0408 > 2`** (search max
  ≈ 2.055). Mechanism = *hull-dip*: visible archetypes carrying their own negativity recede `conv W`. The
  inherited record's generators kept visible rows nonnegative, so it never saw this. **Asymptotically the
  linear-law constant is still 2** (`H/δ → 2`, `H/τ → 0` in the family — an O(δ) finite-size term,
  kernel-safe). Do not quote `H ≤ 2δ` as exception-free at finite δ; the global finite-δ constant is > 2.
- ✅ **The dangerous kernel antecedent re-scopes to `σ̃ → 1`.** Over ~48,000 exact idempotents (~500
  certified hidden vertices, 7 families): `H > Bτ` occurred ZERO times; `σ̃ > τ` is cheap (up to σ̃/τ ≈ 4)
  but INERT for height; the joint never occurred. The collapse bound `H(1−σ̃) ≤ ν(2+4δ)`
  (`obs-height-collapse`, heuristic, 0/500 violations) is the structural reason: height is capped at
  O(δ) unless `σ̃ → 1`. **Strategic consequence:** proving `σ̃ ≤ 1−cτ` for hidden vertices would CLOSE the
  Kernel Conjecture via the collapse bound; hunting `σ̃ > τ` instances is a waste (W2 inertness).

## 2026-07-02 — obs-height-collapse af-VALIDATED (addendum to the entry above)

- ✅ The collapse bound `H(1−σ̃) ≤ ν(2+4δ)` is now **af-validated in-repo** (19-node tree, root
  validated, taint clean; narrowed single-inequality contract with `0 < δ ≤ ¼`, `W ≠ ∅`) — upgraded from
  heuristic/0-of-500. The kernel antecedent's re-scope to `σ̃ → 1` is therefore RIGOROUS (L0 rung b) modulo
  nothing. **The live question of the whole campaign is now the σ̃-cap: `σ̃_v ≤ 1 − cτ` for hidden top
  vertices** (proves the Kernel Conjecture via the collapse bound) **vs a rank-growing construction with
  `1−σ̃ = O(τ)`** (kills this route). Process lesson banked (bd memory): af contracts must be single
  minimal statements — the run-1 STUCK abort was caused by a compound contract, not by the mathematics.

## 2026-07-02 — σ̃-cap refuter sweep (arm F wave 2): halo non-robustness + the surviving halo-robust cap

- ❌ **Never state the σ̃-cap at ε=0.** The ε=0 invisible mass counts v's OWN self-coefficient once v is
  (however slightly) outside `C_W`; an exact idempotent can have `P_vv = 5343/5000 > 1` on a hidden top
  vertex, so `σ̃ > 1` and `1−σ̃ < 0` — exact certificate, `runs/2026-07-02-sigma-cap-refuter/` instance C
  (recipient at 0.02τ, pure halo; halo-restricted σ̃ = 0; orchestrator-recomputed). Any finisher must use
  the halo-robust `σ̃_g` (recipients at dist ≥ τ/4) — the halo-robustness caveat in `def-invisible-mass`,
  now realized by an exact instance.
- ✅ **The halo-robust cap survives with margin**: over ~25k searched hidden top vertices,
  `σ̃_g ≤ ≈0.37τ` (so `1−σ̃_g ≥ 0.92`); max `H/τ = 0.462 < 0.536`; the dangerous joint regime remains
  un-entered. Killing the cap is EQUIVALENT (via the af-validated collapse bound) to entering the
  dangerous regime — no cheap kill exists. Wall mechanism candidate: `conj-no-free-frontier`
  (exposedness absorption); self-mass-immune bridge candidate: `conj-halo-collapse`
  (`H(1−σ̃_g) ≤ (σ̃−σ̃_g)τ/4 + ν(2+4δ)`, exact on all certified instances).

## 2026-07-02 — walls-check on `conj-no-free-frontier` (arm B wave 4): cap-mechanism route wall-blocked

- ✅ **Wall (a) — one-sided ledger — genuinely dodged.** The conjecture's contract carries no
  P-coefficient at all: it is a positional exposedness-production rule, and its composed target is an
  *upper* bound on `σ̃_g`, not the coefficient-mass *lower* bound at v that B3's ledger cannot supply.
  A real structural gain worth remembering for future mechanism design (T1,
  `docs/waves/2026-07-02-B4-walls-check.md` §1).
- ❌ **Wall (b) — anti-splitting/quotient-packing — HIT.** The composed cap `σ̃_g ≤ 1−c` sums surviving
  twin mass over separating directions and needs the number of geometrically distinct genuine-outside
  quotient classes bounded dimension-free — exactly dead route c10. The shard's "hostable mass ∝ ν"
  is per-cluster; it totals only if the class count is O(1) (silently assuming the wall). Plus
  **FAIL-1**: the uniform `κ = τ/4` margin is pointwise and vulnerable to the dense-regular-polygon
  insufficiency — the conjecture is *plausibly false as literally written* (B4 §2, T1/T2).
- **Strategic consequence:** do NOT af-elevate `conj-no-free-frontier`; the bankable finisher piece is
  the bridge `conj-halo-collapse` only. A future cap needs a NEW mechanism that is both ledger-immune
  AND class-count-free, or must first settle the class-count decider (open signed quantitative
  Baake–Sumner). F2's `σ̃_g ≤ 0.37τ` margin is low-dimension evidence and silent on wall (b).

## 2026-07-03 — legal-leak certificates: the argmin does NOT exclude legal rows (do not re-walk)

- ⛔ **"β-positive legal rows with μ>0 are impossible/absorbable at a Φ-argmin" is FALSE.** Exact
  two-scale transverse certificates (D6, `docs/waves/2026-07-03-D6-legal-leak.md`): `L_μ/δ` up to
  `999959/1000000` coexisting with `M_D>0` at a θ-½ Φ-argmin; `F_L>0` realizable; the (FIN)
  constant-1 version already stressed (`592875/591017`). The only argmin fact is the A9 max-
  stationarity DISJUNCTION (same-pivot payment OR collateral rise) — collateral has no useful
  universal lower bound. Consequence: the payment and legal horns of GAP B are genuinely coupled;
  the legal horn needs a real collateral theorem (`strict legal contributor at a maximal pivot ⇒
  Φ ≤ C_legal·δ`), not ledger bookkeeping; (FIN) must carry `C_fin > 1`.

## 2026-07-03 — (SI) death certificate: external sources alone can NOT pay the degenerate tax

- ⛔ **`M_D ≤ C·(G_class⁻ + S⁻^μ)` (the D2 "(SI)" source inequality) is FALSE — do not re-walk.**
  Exact realized refuter (D3, `docs/waves/2026-07-03-D3-si-bn.md` §T1-PROVED-INLINE): rank-3, n=5,
  δ=1/10 centered fan whose θ-½ Φ-argmin has two Schur-degenerate active rows with `M_D = δ/2`
  while the pivot row is fully nonnegative (`G⁻ = S⁻ = 0`). Slab, argmin, AND realizability are all
  present — none of them excludes centered internal transport. The missing source is the degenerate
  rows' OWN weighted negativity `R_D^ν = Σ β⁺ν_j` (equal to `M_D` exactly on the refuter). Any
  transport/source argument must carry `R_D^ν`; the surviving statement is (RSI)
  `M_D ≤ C·(G⁻ + S⁻^μ + R_D^ν)` — which is the A10 WOP quantity re-emerging in H-M quotient
  language (the A-line and D-line have converged on it). The rigorous fan lemmas are PAYMENT
  machinery, not source machinery (their barycenter estimate points the wrong way).

## 2026-07-03 — arm A session-4 roll-up: the plateau-2 picture and the killed proof mechanisms

- ✅ **Plateau-2 is the standing empirical law (7 adversarial design families, all certified < 2).**
  min-max `Φ/δ` over θ-½ charts: path family `2−2/(k−2)` → 2 (A2, k≤30); five decoupled couplings
  (A3); balanced-staircase rescales + repeated anchors (A6); five COUPLED designs incl. anchor-mixing
  to rank 121 (A7 — coupling *reduces* the ratio; best new certified value 3/2). The unbroken-unproved
  candidate lemma: `max_s Φ_s(U*) ≤ 2δ(P)` at every θ-½ Φ-argmin, `δ ≤ ¼`. All wave artifacts
  `docs/waves/2026-07-02-A2…2026-07-03-A7`; headlines orchestrator-recomputed per bundle.
- ⛔ **Proof mechanisms KILLED this session (exact certificates; do not re-walk):** fixed-chart
  beta-LP-only (A4 two-atom moment witness — realizability `P=LB`, `BL=I` must enter); naive chart
  averaging in all three natural measures (A5 sigma-cap-B certificate: best chart Φ=0, θ-class average
  ~10× δ); unnormalized `Σ_s Φ_s ≤ Cδ` (A6 repeated-anchor witness, see the dead-route entry above);
  pointwise `E ≤ Cδ`, `σ ≤ 2δ`, `V=0` at argmin (named witnesses in A4/A6).
- ✅ **What survives:** the argmin interface (existential (EX) ⟺ argmin bound, lossless); argmin
  Schur-swap COMPARISON (≠ dead single-swap descent); the probabilistic-method interface only in
  max-based/normalized form; `V_s ≤ Φ_s/2` (elementary, every chart/pivot); and the rigorous
  composition link `lem-factorization` (af-validated 2026-07-03) turning any universal (EX) `C₀` into
  `C_sf = 2C₀+6`. The δ=1/2 mechanism-killers (B6, perturbed staircase) do NOT port under the cap
  (A6 rescale tradeoff): under-cap witnesses are structurally tamer — the cap is load-bearing.

## 2026-07-02 — (EX) chart scoping (arm A wave 1): "C₀ = 1 empirically" is RANK-3-ONLY

- ❌ **Do not quote "C₀ = 1 empirically" (the `conj-ex` contract parenthesis) as the (EX) target.** It is
  the rank-3 record only (278 exact `δ≤¼` instances, worst `min_U max_s Φ_s/δ = 1`, attained). The exact
  higher-rank stress records already sit ABOVE 1: `no_center_path_k6: Φ/δ = 3/2`, `no_center_path_k8:
  Φ/δ = 5/3` (both `δ = 1/100`, exact `BL/P²/rowsum` checks true —
  `docs/ingest/experiments/out/w40_ndg/part_a_results.txt:7–8`, orchestrator-verified), and kernel-v2
  notes float scans "climbing toward 2" (`docs/ingest/report/kernel-conjecture-v2.tex:434–440`). The
  ratios fit `2 − 2/(k−2)` (T2 pattern-read), so the working hypothesis is a PLATEAU at 2 (⇒ `C₀ = 2`,
  `C_sf = 2·2+6 = 10`) — but plateau-vs-growth is UNDECIDED and is the arm-A viability decider before
  any (EX) proof wave. Any universal `C₀` still discharges `op-classical` (the composition tolerates it).
- ⛔ **Unnormalized `Σ_s Φ_s ≤ C·δ` is FALSE dimension-free (do not re-walk the sum interface).** Certified
  under-cap witnesses (`runs/2026-07-02-undercap-killers/`, repeated decoupled anchors, orchestrator-
  recomputed): `g` anchor copies give `sum Φ/δ = 11g/8` (g = 2,3,5 certified) while `max Φ/δ = 11/8`
  stays fixed. Decoupled anchors amplify the SUM, never the MAX — any (EX) proof must be max-based or
  carry a normalization/quotient that kills anchor multiplicity. This corrects the A5 "probabilistic
  `Σ_s` interface" (docs/waves/2026-07-02-A5-averaged-selection.md): the interface lemma is fine, its
  aggregate hypothesis is unsatisfiable unnormalized. Also from the same wave (A6): the δ=1/2
  mechanism-killers do NOT port under the cap (B6 staircase high-E/many-active/high-sum collapse before
  δ≤1/4; only tiny `V>0` ports), plateau-2 remains unbroken, and `V_s ≤ Φ_s/2` holds for every chart
  and pivot by an elementary one-line argument (`docs/waves/2026-07-02-A6-undercap-killers.md` §T3).
- ✅ **The (EX) existential form suffices downstream — no constructive selector is needed.** The
  composition chooses a `Φ`-argmin over the finite class `M_{1/2}(P)` and the hostile w42 audit confirms
  no quantifier slip (`docs/ingest/experiments/out/w42_factor_audit/audit.md:144–168`). Pure
  variational/compactness arguments are admissible. Walls caveat (A1 walls-check, T1): aggregate/global
  proofs (dual certificate, clone-quotient measure compression) dodge both recorded B-walls; any
  per-class / per-wedge / per-block proof re-imports the class-count wall in chart language. See
  `docs/waves/2026-07-02-A1-ex-chart-scoping.md`.
