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
  canonical simplex frame** (proved); the transferable (frame-free) statement is now carried by
  `conj-skinny-shadow-cap` (`lem-dual-localization` was RETIRED 2026-07-04 — its transcribed contract was
  a distance tautology; see the 2026-07-04 entry below; Route B is vacuous in the skinny `μ→1` regime).
  Never present the frame-specific proof as the general one.
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

## 2026-07-03 — orphan-row certificate (arm G wave 3): the fan-financing family can be EMPTY

- ⛔ **"Every strict legal β-positive row with μ_j>0 at a θ-½ Φ-argmin has a volume-permitted negative
  coordinate" is FALSE — and with it the pure-legal circulation inequality at `C_legal=0` (do not
  re-walk either).** Exact rank-3 one-B-row certificate (G3,
  `docs/waves/2026-07-03-G3-orphan-row.md`): `o=(7/12,−1/12,1/2)`, `α=(−1/5,−1/4,1/20)`, `δ=1/4`,
  unique θ-½ argmin `(c0,c1,c2)`. The orphan row is legal through its POSITIVE coordinate `7/12>1/2`
  while its only negative coordinate `−1/12` is sub-threshold ⇒ the G1 fan-matched financing family is
  EMPTY, yet `L_μ+F_L = 257/57600 > 0`. NOT an amplifier: the leak is paid by the class aggregate
  `G_class⁻ = 7/240` (ratio `257/1680`), and the financier is structural —
  `Γ_{s,0} = −β_o·a_0(o) < 0` is forced by legality-through-the-positive-coordinate itself. Scope
  caveat: the certificate is λ-positive (`E_s(o)=0`, no A9 same-pivot payment owed); the ACTIVE-row
  orphan exclusion (`E_s(j)>0 ⇒` volume-permitted negative coordinate) remains OPEN. Consequence: any
  circulation/financing lemma must carry a class-aggregate orphan horn — negative-coordinate fan
  weights alone cannot see λ-positive orphan leakage.
- ⛔ **The ACTIVE-row orphan exclusion (`E_s(j)>0 ⇒` volume-permitted negative coordinate) is ALSO
  FALSE (G4, `docs/waves/2026-07-03-G4-orphan-financing.md`) — do not re-walk any orphan-exclusion
  route.** Exact rank-3 certificate (`p=3/5, e=2/5, α=(5/16,−1/4,7/64)`, `δ=1/4`, θ-½ argmin
  `(c0,c1,c2)`): `E_s(o)=1/5>0`, only negative coordinate `−2/5` sub-threshold — an active orphan
  owing A9 payment with an empty fan family. Still exactly financed: `Γ_0=−21/320` pays it at ratio
  exactly 1 (payment included). Quantitatively (T1 on the one-B-row family): the orphan ratio
  `(L_μ+F_L)/budget` is BOUNDED with `sup = 1`, not attained (cap = the θ-half volume boundary
  `p↓½, e↑½` with `δ=¼` active, not an argmin switch); charging active A9 payment to the same horn
  pushes the trend to `2` ⇒ `C_orph ≥ 1` (≥ 2 with payment). Suggestive killed design: a second
  legal row built to CANCEL the financier `Γ_0` was rejected by `δ = 1001/1600 > 1/4` —
  financier-cancellation may be δ-expensive (unproved; the conjectured conservation mechanism). The
  surviving target is the aggregate ACTIVE-ORPHAN-FINANCING lemma: post-fan orphan demand
  (incl. `βE_s`, cancellations before positive parts) `≤ C_orph·(G_class⁻+S⁻^μ+R_D^ν)`.
- ⛔ **That aggregate orphan-financing lemma is FALSE for EVERY finite `C_orph` (G5,
  `docs/waves/2026-07-03-G5-orphan-financing-lemma.md`) — the class/signed budget CAN be starved; do
  not re-walk any orphan horn budgeted only by `G_class⁻+S⁻^μ+R_D^ν`.** Exact two-orphan amplifying
  family (`o0=(p,−e,q), o1=(−e,p,q)`, `β=¼` each, `0<h<1/6`): `δ(P)=¼−h²/p<¼`, unique θ-½ argmin,
  both rows active strict-legal orphans, fan family empty, `OD = ½−2h` against budget
  `G_class⁻ = h` ⇒ ratio `1/(2h)−2 → ∞`. Mechanism (T1 exact ledger, eq. (4)–(5) of the artifact):
  `P_r^O = N_r^O − H_r − Γ_r` — each orphan's positive legal coordinate is canceled by the OTHER
  orphan's sub-threshold negative coordinate, whose own leak sits in OD, not in the budget.
  **NOT an (EX) refuter**: on the same family `Φ_s/δ → 1` (plateau-2 intact) — it kills only the
  budget choice. Forced repair (the (SI)→(RSI) own-negativity pattern repeating): the orphan budget
  must include orphan own row-negative mass — `Σ_{active orphan} β_j ν_j` (coefficient ≥ 4 forced) or
  cruder `+C_δ·δ(P)` (`C_δ ≥ 2` forced). Watch the next hole: "silent" β-positive B rows (no
  volume-permitted coordinate at all) could cancel financiers while contributing to neither OD nor any
  budget term — the repaired budget may need `Σβ_jν_j` over ALL β-positive B rows.
- ❌ **Do NOT conflate ambient own-negativity `ν_j` with chart negativity (G6,
  `docs/waves/2026-07-03-G6-repaired-horn.md`).** The pointwise domination `ν_j ≥ a_r(j)⁻` is FALSE:
  row reproduction gives `(1−P_jj)·a_r(j) = Σ_{i≠j} P_ji·a_r(i)`, so a large positive self-coefficient
  `P_jj` carries chart negativity at arbitrarily small ambient cost — exact silent-algebra family with
  `β·a⁻/β·ν = 1/κ → ∞` (checkpoint `e=1/4, κ=1/100`: ratio 100, `δ=1/400`). BUT it is not an (RH)
  refuter: the θ-half Φ-argmin PIVOTS ONTO the self-supported row (chart volume 5/4, max Φ = 0) — the
  pathology is eaten by minimality via a pivot-REMOVING chart move, a swap family the A9
  active-preserving disjunctions do not cover. Status after G6: the unified own-negativity horn (RH)
  `OD ≤ C_RH·(G⁻+S⁻^μ+Σ_{β>0}βν)` is OPEN and survives ALL certified instances (G5 family = exactly
  sup 4 ⇒ `C_RH ≥ 4`; D6 certs have OD=0 after fan separation); small closed piece (T1, rank 3): on
  active orphan rows `E_s ≤ μ_s`, so the payment term is ≤ a factor-2 overhead on `L_μ`. THE isolated
  missing statement is **(SC)**: at a θ-half Φ-argmin, the β-weighted transverse negative chart mass of
  non-fan β-positive B rows is `≤ C·(G⁻+S⁻^μ+Σβν)` + fan-collateral residual — i.e. an argmin
  self-support/cancellation control, provable only by USING minimality (pivot-removing moves).

## 2026-07-04 — literature negative space (7-lane sweep; sources `stated`, none byte-matched — L1)

*(Full sweep record: `docs/lit-review/2026-07-04-literature-sweep.md`. These are "easy to get wrong"
imports a future agent might reach for — read before importing ANY external tool.)*

- ❌ **Do NOT route the within-class distribution rounding through hitting-time / fundamental-matrix
  sensitivity.** The sharpest entrywise stationary-distribution perturbation theorem
  (Thiede–Van Koten–Weare, SIMAX 2015, arXiv:1410.1431, scout-verified full text) has coefficients
  `Q_{ij}(S)^{-1}` provably growing EXPONENTIALLY in state count, and the theorem degenerates to trivial
  exactly at the reducibility boundary — the regime a near-idempotent Q lives in. Any sub-argument
  inheriting these coefficients is presumptively NOT dimension-free.
- ❌ **Do NOT import generic "spectral gap ⇒ structure" lemmas for non-reversible chains.** Mehta et al.
  (arXiv:1909.12497, scout-verified): for doubly-stochastic A, `φ(A) ≥ Δ(A)/(35n)` with a matching
  `φ ≤ Δ/√n` family — the n-loss is NECESSARY. (Our entrywise hypothesis is stronger than a gap, so this
  does not refute op-classical; it kills the generic import.)
- ❌ **The modern entrywise/ℓ∞ eigenvector program (Abbe–Fan–Wang–Zhong etc.) is keyed to INCOHERENCE**
  — delocalized eigenvectors. Our target subspace is indicator-like (maximally coherent): those theorems
  give no improvement over weak Davis–Kahan here. Wrong regime, not just weak constants. (Deterministic
  exceptions worth knowing: Cape–Tang–Priebe Thm 4.2 — symmetric only; Damle–Sun Thm 5.1 — template only.)
- ❌ **"Quantitative Baake–Sumner web stability" does not exist.** The full citation tree of
  arXiv:2007.11433 (9 works, checked 2026-07-04) is exclusively Markov-embeddability. The inherited
  campaign's pointer is unsubstantiated — do not cite it as a route unless a locus in `docs/ingest/` is
  produced.
- ⚠ **The unconstrained/pre-structured versions of our problem are LINEAR-rate and easy** — Riesz
  projection / Kitaev Prop 3.1 (signed fix at O(η)); Kazhdan ε-representations (2δ); Gowers–Hatami
  (Cε, normalized HS); Christensen near-inclusions (14d). The ½ exponent enters WITH the positivity
  cone (degenerate-complementarity mechanism, Luo–Pang 1994 — see the sweep §1.3). Do not "borrow" a
  linear-rate theorem and expect it to survive stochasticity.
- ⚠ **Kitaev arXiv:2405.02434 poses the noncommutative lift of op-classical as OPEN** (§1.2 of the
  paper, scout-verified). Two easy-to-get-wrong details: the commutative-case reduction (cb-norm →
  ∞→∞) is OUR inference, not in the paper — verify before citing; and the claim "published in Nature"
  circulating in search engines is FALSE (arXiv preprint, math.OA).

## 2026-07-05 — decision-check wave DC1–DC4 (session 8): the sketch's ledger redrawn by exact certificates

- ⛔ **Broad NSC charging is DEAD (zero-denominator death certificate).** A carrier row can hold
  `B_{r,s} > 0` chart-negativity while being **entrywise nonnegative** (`ν_i = 0`) — AT a certified
  unique capped θ-half Φ-argmin (`runs/2026-07-05-nsc-zero-denominator-refuter/`,
  orchestrator-independently recomputed). Chart-negativity of a carrier needs NO ambient negativity
  on that row even at the argmin: the G6 decoupling, previously known only away from the argmin
  mechanism, is realized at one. Any future B-financing must NOT charge carrier row-negativity
  alone. The refuter has `B ≪ δ` and `Φ ≡ 0` (no Γ-branch), so the branch-restricted B-lemma
  target `B ≤ K·δ` is untouched. `conj-nsc` is `disproved` (broad form); successor shape = user
  decision.
- ❌ **"ex ⟺ kernel" has NO proof in either direction** (DC4, `docs/waves/2026-07-05-DC4-equiv-assembly-audit.md`):
  registry-prose only, both directions priced GENUINE GAP, with three named mismatches
  (chart-vs-vertex quantifiers; `P_vj` vs `P_{u_s j}` weights; maximal-pivot drift). Until an
  `EX ⇒ Kernel/HLC` edge is proved, (EX)-side results do NOT feed op-classical. Never write
  "equivalently" for these two statements.
- ❌ **The K⟨1⟩6 additive master formula is RED as written** (DC3, T0): `FanRes_s(U) > 0` is
  REALIZED (D6 legal-leak instances) while the master formula has no FanRes term; silent rows are
  REALIZED with NO tribe under the sketch's fan/orphan/self-supported trichotomy (D3, D6); the
  high-self G13 stress rows are chargeable through BOTH the C_RH budget and the naked δ term
  (double-charge). Assembly must be nesting-aware (SC → RH), FanRes-explicit, and silent-row-aware.
- ✅ **Fusion evidence (DC1, T0/T2):** on the D3/D4/D6 certificates every D-line demand (M_D, L_μ,
  F_L, FIN_lhs) is financed by the G-line contract budget (worst ratio exactly 1, D3 via Σβν; no
  demand-positive/budget-zero escape) — supports treating the fan/orphan/self-support financing as
  ONE budget in sketch v2. Finite evidence, not proof.

## 2026-07-05 — wave 15: Gamma-emptiness DEAD; the branch-restricted B-lemma regime is REAL

- ⛔ **Capped (G)-emptiness is REFUTED** (`runs/2026-07-05-gamma-emptiness-refuter/`,
  orchestrator-independently recomputed): the FIRST certified capped clean Gamma-block exists
  (delta ~ 0.055, unique theta-half argmin, Psi_j = 1/200 < M <= Gamma_j = 7/250). **G11's 0/352
  capped search was a coverage artifact, not emptiness evidence** — never treat a failed search
  census as support for an emptiness conjecture without a coverage argument. The refuting row is
  high-self (P_11 = 203/400), so the high-self-restricted variant is refuted too.
- ✅ **The (PRT) collateral horn now has ONE explicit missing ingredient** (wave-15 T1 residual):
  `M − Φ_r ≤ 17·B_{r,s} + 16δ` (c>0) / `+ 20δ` (c<0) under the theta-half Cramer box — so
  `conj-b-restricted` (`B ≤ K·δ` at capped argmins carrying a clean Gamma-block) closes the branch
  with `K_G = 17K + 20`. Its hypothesis class is NONEMPTY for the first time (the refuter itself:
  `B/δ = 0.7708`, forcing `K ≥ 0.7708`; the wave-13 family law suggests `K ≥ 0.77764`).
- Successor discipline confirmed twice in one day: bounded prove-or-refute waves on freshly
  codified conjectures killed two wrong shapes (broad NSC, Gamma-emptiness) within hours of
  codification, each leaving a sharper, certified-nonvacuous target. Cost of each kill: one wave.

## 2026-07-05 — W18 (session 9): Route-A wall re-read — WALL-NARROWED, not wall-blocked; D1 confirmed twice

- ✅ **The recorded B3/B4 walls do NOT bind the constant cap `σ_g ≤ 1/2` as stated** (W18,
  `docs/waves/2026-07-05-W18-route-a-wall-reread.md`, worker T1/T2 — no status change):
  B3's one-sided ledger was a wall for a *lower* bound on visible-pot mass; CAP-1/2 is an *upper*
  bound on genuine-outside mass (B4's dodge), but the burden TRANSFERS intact to a named residual —
  the **constant-mass shallow-genuine exclusion**: positive mass on rows with `dist₁(·,C_W) > τ/4`
  AND canonical-separator depth `< τ/4` must be `≤ 1/2 − 4τ(2+4δ)`. The class-count dead route
  (c10/quotient packing) **BINDS-ONLY-O(1)**: CAP-1/2 tolerates `C/τ` (or `C/δ`) genuine classes,
  which NO recorded killer family excludes — and no recorded construction pushes total `σ_g`
  toward 1/2 (F2 maxima: `σ_g = 5991/80000`, `229/3200`; W17b census max `1/25`).
- ❗ **Two honesty flags on the narrowed route.** (i) The per-class "hostable mass ∝ poke depth"
  bound is NOT a proved lemma (conjecture-body prose, `conj-no-free-frontier`), with two
  undisambiguated scale readings — `O(τ)` (poke parameter) vs `O(δ)` (row negativity); which one
  holds changes the needed class count by a factor `1/τ`. (ii) The depth-ledger steps consume
  `obs-deep-leakage`, whose status is **heuristic** — the "deep slice is paid" step is itself an
  unproved input until that shard is re-established.
- ✅ **W17's D1 is now twice-independently re-derived** (W18 R1 under an independence discipline +
  R2's Q4(b)): cap `σ_g ≤ 1/2` on hidden top vertices ⇒ `H ≤ (29/8)τ`, exact constants `29/16`,
  `29/8` confirmed; STRENGTHENED — under the cap ALL rows land within `(29/8)τ` of `conv W` (the
  Kernel raw antecedent `σ̃_v > τ` is unused; no raw-to-halo bridge needed). Residuals for
  "cap ⇒ Kernel": W-nonemptiness (genuine gap), `δ = 0` endpoint (short). Still worker-T1, NOT
  af-validated.
- ❌ **CAP-1/2 is NOT equivalent to the height bound** (orchestrator wave-brief hypothesis,
  REFUTED independently by both workers): the validated collapse gives cap ⇒ height bound and
  `H > (29/8)τ ⇒ every hidden top has σ_g > 1/2`, but NOT the converse — the cap additionally
  excludes the low-height/high-`σ_g` region. Consequence: the W17b census slack is *stronger*
  evidence than "no tall instance found", and refuter searches should target `σ_g > 1/2` at ANY
  height. Do not cite the cap and the height bound as interchangeable.

## 2026-07-05 — E1 (session 9): arm E decision-check — Luo–Pang is NOT a black-box ½; route retargeted GO-CONDITIONAL

- ❌ **The lit-review §1.3 attribution does not survive the staged primary** (E1,
  `docs/waves/2026-07-05-E1-error-bound-decision-check.md`, worker A, text-grounded
  [STAGED-quote] audit): Luo–Pang 1994's ½-exponent results (Thm 4.1 / Cor 4.1) require
  **Assumption 4.1 — every quadratic NONNEGATIVE on the polyhedron** — and the idempotence
  entries `(E²−E)_ij` are **sign-indefinite** on the stochastic polytope (T1 witness at n=2).
  The general analytic theorems (2.1/2.2) give fixed-n bounds with UNSPECIFIED exponent and
  instance/compact-set constants. **Fixed-n √ is not even free**: the staged Example 4.2 is a
  quadratic system with error-bound exponent ≤ 1/4. Norm conversions add `n^{3/4}` (Frobenius)
  to `n` (entrywise-ℓ1) on top. Never cite "Luo–Pang gives ½ for our system".
- ❗ **Citation drift caught** (staged bibliography, refs [26]/[27]): the monotone-LCP error
  bound is Mangasarian–Shiau, *Math. Programming* **36 (1986)** 81–89; "SIAM JCO 25 (1987)"
  is their SEPARATE Lipschitz-continuity paper. The lit-review §1.3 line conflated them
  (correction note added there). Acquisition queue updated accordingly.
- ✅ **The (EB) formulation passes the clone/block smell tests in the theorem direction**
  (worker A T1: weighted clone lift preserves row-residuals, distances, and idempotency;
  block sums are maxima) — independently confirmed exactly by the E1b pilot. Consequence:
  any future arm-E proof charging by raw index counts / active-constraint counts / Euclidean
  dimension is suspect unless shown clone-lift invariant. Euclidean black-box constants FAIL
  this test.
- ✅ **Pilot (L3, `runs/2026-07-05-e1-uniformity-pilot/`): no visible n-blowup** — largest
  certified ratio `r ≈ 1.375` at the stochasticized ex-hume anchor with TRUE n=3 minimum;
  coupled n=4..12 family bounded. A pilot, never a uniformity certificate; decision-grade
  wave-2 criteria recorded in the bundle.
- **Arm E retarget (GO-CONDITIONAL, worker A):** not "apply Luo–Pang" but a bespoke,
  clone-invariant feasible-slice error bound for the stochastic-idempotent variety. Two named
  intermediates: (E-int-1) fixed-n local √ bound with the constant expressed in stratum data,
  then measure n-dependence; (E-int-2) find nonnegative-on-P_n quadratics `R_n` with zero set
  exactly the idempotents and `R_n(Q) ≤ K·η`, K n-free — that WOULD make Cor 4.1 applicable by
  construction. Kill criteria recorded in the wave doc (incl.: a feasible family with
  `dist/√η → ∞` kills op-classical itself, not just the arm).

## 2026-07-06 — E2 (session 9): E-int-2 DEAD — nonnegative-quadratic residuals are BLIND (death certificate)

- ⛔ **DEAD ROUTE (do not re-walk): quadratic Assumption-4.1 residuals for the stochastic-idempotent
  variety.** E2 (`docs/waves/2026-07-06-E2-nonneg-residual-decider.md`): two mutually blind
  adversarial workers independently proved the same n=2 no-go lemma — **every quadratic
  nonnegative on `P_2` and vanishing on `S_2` is identically zero on `P_2`** (divisibility by
  `(a−b)`; two-sided nonnegativity across the interior rank-one continuum forces `c(a−b)²`; the
  isolated idempotent `I₂` forces `c = 0`) — and the weighted clone lift transports the
  blindness into every `P_n`. So condition (b) (zero set = `S_n`) is impossible at EVERY n;
  there is no `K(n)` to bound (the failure precedes the domination condition, which was the
  easy direction). Witness at which every admissible quadratic vanishes:
  `Q* = ((1/3,2/3),(2/3,1/3))`, `η = 4/9`. Structural cause: an interior idempotent CONTINUUM
  + an extra boundary idempotent in one two-state quotient. Orchestrator: both scripts exit 0
  + independent exact recomputation (witness, residual formula, clone identity, cubic hatch,
  retraction idempotents).
- ✅ **Two survivors, banked T1 (worker-attributed, uncodified):** (i) the **degree-3 escape
  hatch** — `F₂(a,b) = (a−b)²((1−a)+b)` is nonnegative on `P_2`, has zero set EXACTLY `S_2`,
  and satisfies `F₂ ≤ η`: higher-degree nonnegative residuals are NOT blocked (Luo–Pang §4 is
  degree-2-specific — a different engine or a stratified application is needed downstream);
  (ii) **`aff(S_n)` = the full row-stochastic affine space** (deterministic retractions
  `R_{i→j}` span all row-sum-zero directions) — no linear form vanishes on `S_n`;
  SOS-of-linear is permanently dead.
- ❗ Honesty limits: this kills only the quadratic-residual CONSTRUCTION route into the staged
  Cor 4.1; it does NOT disprove fixed-n √ error bounds by other means (worker C, T2). Arm E's
  remaining content: E-int-1 (stratum-data constants) + the degree-≥3 / stratified residual
  question. Third same-shape confirmation of the bounded prove-or-refute discipline: a freshly
  named target killed within hours, leaving sharper certified survivors.

## 2026-07-06 — W19 (session 9): Route-A deciders — the per-class folklore is unprovable-as-written; the σ_g wall is ABSORPTION, not capacity

- ❌ **The per-class "hostable mass ∝ poke depth = O(τ)" folklore is NOT provable at any
  nontrivial scale from the current toolkit** (W19-B, `docs/waves/2026-07-06-W19-route-a-deciders.md`):
  only the trivial `M_X ≤ 1+δ` is derivable; the folklore needs BOTH a sound
  exposedness-production rule (B4-FAIL-1-wounded) AND a previously unnamed **coefficient-poke
  charge** linking geometric poke depth to `P_vj` mass. **T0: the self-inclusive reading is
  exactly contradicted by banked instance B** (ρ-component mass `229/3200 > 1/20` = the poke
  value) — every future cluster lemma must carry an explicit self-mass exclusion. External
  calibration `0.2468·δ` = `0.0533·τ`: consistent with both scales; asymptotics open. Named
  codification target: **`conj-external-poke-charge(A)`** (a conjecture — do NOT codify the
  folklore as written).
- ✅ **The σ_g > 1/2 wall is exposedness ABSORPTION, not mass capacity** (W19-A, L3,
  `runs/2026-07-06-w19-sigma-frontier/`): the exact LP relaxation places `5/4` mass on
  designated outside recipients, but the exact-geometry optimizer point has `W = [3,4,5]`,
  `H = 0` — recipients become visible. New certified record `σ_g = 5991/80000 ≈ 0.075`
  (rank 5, genuine SELF recipient; above the W17b census max `1/25`, still ~6.7× below the
  cap). Duplicate-splitting leaves total `σ_g` exactly unchanged (single quotient class);
  the hidden/absorbed frontier on that design sits in `(5/84, 1/16]`. NOT an emptiness claim.
- ❗ **Named residual (both workers jointly):** geometrically DISTINCT multi-class designs —
  many recipients in different quotient classes each near its per-class ceiling — remain
  untested. That is the direct empirical probe of the `C/τ`-count opening (W18) and of the
  poke-charge conjecture, and the sharpest next decider on Route A.

## 2026-07-06 — W20 (session 10): g-bootstrap decider 1 — no kill; the zoo CANNOT populate G_a for a ≥ 1

- ✅ **Both pre-registered g-bootstrap kills UNREALIZED** (W20,
  `docs/waves/2026-07-06-W20-g-zoo-measurement.md`, L3 bundle
  `runs/2026-07-06-w20-g-zoo-measurement/`): full exact sweep (307 unique certified matrices, 1842
  `(matrix, a)` cases, 1842 harmonicity `Pg = g` + 9564 sandwich `σ_g − ν ≤ g ≤ σ_g` checks, 4
  banked calibrations) + a mutually-blind adversarial constructor. At `a = 1/4` the visible-row
  frontier is `g_w = 7/80` (`(g_w/τ)² = 105/569`, ≈ 0.43τ); no row anywhere reached `g ≥ 1/2`.
- ❗ **The load-bearing structural fact: `G_a` is EMPTY zoo-wide for every `a ≥ 1`** — the deepest
  genuine geometry ever banked sits within 1·τ of `conv W` (consistent with the 25k-sweep
  `H ≤ 0.462τ`). Consequence: **zoo measurement is EXHAUSTED as a step-4 decider** — the band-web
  kill zone is unreachable by every known construction. Evidence FOR MIN-A; an emptiness claim of
  nothing.
- ✅ The M1 clone-safety claim realized on an example: weighted row-cloning transports `G_{1/4}` and
  preserves old-row `g` exactly (worker B). Binding constraint in all adversarial designs:
  exposedness absorption (the W19 wall), again identified by the LP-vs-exact-geometry comparison.

## 2026-07-06 — W21 (session 10): LEMMA A (visible rows are g-small) PROVED (C = 4, a ≥ 4) + verified + refuter-converged; the a-gap is the new named front

- ✅ **Lemma A is proved at exact constants and independently verified** (W21,
  `docs/waves/2026-07-06-W21-lemma-a-decider.md`): fresh-codex prover — `−ν_w ≤ g_w ≤ 4τ` for every
  visible row `w`, every halo width `a ≥ 4` (mechanism: exposer-pairing against row reproduction;
  `a ≥ 4` used exactly once, in `G_a ⊆ {ρ-far from p_w}`); SEPARATE fresh-codex adversarial verifier
  returned VALID on all 7 checklist items; the mutually-blind refuter converged NOT-REFUTED and
  independently derived the same ρ-far inclusion from the opposite mandate (second occurrence of the
  E2 adversarial-convergence pattern). Codified as `lem-visible-g-small` (`status: proved`,
  `af: none` — NOT L0-rigorous; af elevation filed). The g-bootstrap's steps 1+2 now stand.
- ✅ **New refuter frontier certificate** (L3, `runs/2026-07-06-w21-lemma-a-decider/`): visible row
  with `g^{(1/4)} = 49/400`, `K = √(147/569) ≈ 0.508` at `δ = 27881/480000` — the largest certified
  visible-row `g/τ` to date (beats W20's 0.43); absorption companion: scaling `λ: 7/5 → 29/20` flips
  the deep row visible (`H = 0`). At `a ∈ {4,5,6}` the refuter could not populate `G_a` at all.
- ❗ **The constants fight is now exact — the `(29τ/8, 4τ]` a-gap band:** Lemma A's mechanism needs
  `a ≥ 4`; MIN-A's tall antecedent guarantees depth only `> 29τ/8 = 3.625τ`; nothing banked realizes
  depth `> 1τ`. Either step 3/4 must place deep-band mass beyond `4τ` (obs-deep-leakage territory,
  aism-tq3), or Lemma A must be extended into `a ∈ (29/8, 4)` by a NEW mechanism (the ρ-far
  inclusion genuinely fails there), or the collapse constant must improve. Do not cite Lemma A at
  `a < 4`.

## 2026-07-06 — W22 (session 10, round 2): trunk <2>5 re-derived + reviewed — Kernel ⇒ HLC codified; HLC is now a DAG node

- ✅ **`lem-kernel-implies-hlc` (proved, reviewed):** Kernel(δ₀, B) ⇒ H(P) ≤ max{B,3}·√δ for
  δ ≤ min{δ₀, 1/4} (W22, `docs/waves/2026-07-06-W22-kernel-implies-hlc.md`): fresh-codex prover
  independent of the ingest text; s8 cap re-derived from mass-split + the row-diameter clause
  (H(1−σ̃) ≤ ν(2+4δ)); separate hostile verifier VALID 7/7 (incl. a 17-fixture exact test of the
  intermediate inequality). Trunk staleness debt PAID — `<2>5` moves from "recorded T1, not a
  shard" to reviewed + codified.
- ✅ **`op-hlc` registered + finisher wiring:** HLC is now a first-class open-problem node;
  `op-exposed-hull` rewired to dep on it (faithful <2>6 consumption); the linker sees the full
  chain conj-kernel → lem-kernel-implies-hlc → op-hlc → op-exposed-hull → op-classical.
  Consequence: **<2>6 and <2>7 are now the ONLY unreviewed links between a proved Kernel and
  op-classical** — the trunk debt has a precise shape.

## 2026-07-06 — W23 (session 10, round 2): THE A-GAP CLOSED (mod-review) — parametric halo collapse, T(a) = 5a/2 + 3

- ✅ **`lem-parametric-halo-collapse` (proved, reviewed):** for a hidden top v of height H and ANY
  halo width a > 0: `H(1−σ_a) ≤ (σ−σ_a)·aτ + ν(2+4δ)` (W23, `docs/waves/2026-07-06-W23-a-gap.md`);
  the af-validated conj-halo-collapse is exactly the a = 1/4 case (verifier-checked, no off-by-4);
  verifier expanded the residual-split proof independently and passed exact tests. Consequences:
  forced-mass curve **T(a) = 5a/2 + 3** (T(1/4) = 29/8 = the W18 constant, exact; **T(4) = 13**);
  **MIN-A at width 4**: H > 13τ forces every hidden top to `g^{(4)} > 1/2 − δ`, pairing with the
  proved Lemma A (visible ≤ 4τ) into a genuine gap iff **δ < (17−12√2)/2 ≈ 0.0147**. The
  g-bootstrap's contradiction surface is now width-compatible; MIN-A's tall threshold updates
  29τ/8 → 13τ.
- ❗ **Route (ii) (small-a Lemma A) is OPEN-BOTH-SIDES and MOOT** (worker I, L3
  `runs/2026-07-06-w23-a-gap/`): prove side structurally blocked (the (aτ, 4τ) annulus is priced by
  no tool — the exposer starts at ρ = 4τ); refute side could not enter G_{15/4} on any tested family
  (δ-inflation + absorption named). Do not fund further small-a waves unless step 4 turns out to
  need a < 4.
- ❗ Follow-up re-aim: D1 codification (aism-yxa) should target the parametric form directly —
  the cap-⇒-Kernel assembly now runs through T(a) with B = 13 at width 4.

## 2026-07-06 — W24 (session 10, round 2): g-bootstrap step 3 (disintegration) derived + reviewed

- ✅ **`lem-genuine-disintegration` (proved, reviewed):** S3.1–S3.4 (W24,
  `docs/waves/2026-07-06-W24-step3-disintegration.md`): every j ∈ G_a is a hidden vertex or
  non-vertex row; vertex disintegration with μ_j(θ) ≥ (d_j−θ)/(H−θ); the consumable ledger
  `g_i ≤ M_i^a + Σ_{j∈G_a} P_ij⁺(H−d_j)/(H−aτ)` with M_i^a supported entirely on hidden vertices
  at depth (aτ, H]. Hostile verifier VALID (exact tests on banked rank-3/rank-5; one presentation
  caveat folded into the shard).
- ❗ **Honest limits kept loud:** no vertex count, no web structure, no uniform slack bound — rows
  barely past the halo can lose most disintegrated weight to shallow vertices. That residue IS
  step 4.
- ✅ **The bootstrap's remaining mathematical content is now exactly ONE open step:** for
  δ < (17−12√2)/2 and H > 13τ — harmonic g^{(4)}, hidden tops > 1/2 − δ, visible rows ≤ 4τ, deep
  mass disintegrating onto hidden vertices — the once-applied maximum principle must produce a
  contradiction (anti-splitting, analytic form). Plus the standing trunk items (<2>6, <2>7),
  W-nonemptiness, and the δ₀-endpoint bookkeeping.

## 2026-07-06 — W25 (session 10, round 3): step 4 decided into a conjecture + a named missing input; the once-applied principle's yield is a LOWER bound

- ✅ **`lem-top-concentration` (proved, reviewed):** the once-applied maximum principle with an
  affine ℓ1/ℓ∞ support functional gives `Σ_{j∉G_a} P_vj⁺ ≤ ν_v(2+4δ)/(H−aτ)` at hidden tops, and
  the same bound on the disintegration slack; in tall width-4 configs the deep hidden-web mass is
  FORCED UP: `M_v⁴ > 1/2 − δ − τ(2+4δ)/9` (W25,
  `docs/waves/2026-07-06-W25-step4-decider.md`; verifier VALID incl. an exact LP support-functional
  test). **The recorded wall in its precise form: the local principle pushes mass INTO the
  near-top hidden band.** Closing step 4 needs the opposite (upper) cap.
- ⛔ **INSUFFICIENCY CERTIFICATE (do not re-attempt step 4 from the current fact-list):** a 3×3
  exact idempotent (`δ = 1/100`; L3 bundle `runs/2026-07-06-w25-step4-decider/`, orchestrator
  recompute 17/17 from printed values) satisfies EVERY banked scalar fact (harmonicity, collapse
  conclusion, Lemma-A conclusion, disintegration, row facts) under labels with a sustained web and
  labeled `H = 20τ` — while the labeled-hidden top is ACTUALLY (ρ,κ)-exposed (explicit exposer,
  margin 100/101). **The mandatory missing input is HIDDENNESS: t*(v) < κ — the failure of every
  admissible exposer against some ρ-far row — which NO banked lemma consumes.** Any future step-4
  attempt without a hiddenness input is pre-refuted by this certificate.
- ✅ **Step 4 reduced to `conj-min-a-w4`** (codified conjecture): in tall width-4 configs
  (`δ ≤ (17−12√2)/2`, `H > 13τ`) SOME hidden top has `σ₄ ≤ 1/2`. With the reviewed parametric
  collapse this yields `H ≤ 13τ` — the height side of Kernel at B = 13. Blind convergence (third
  E2-pattern occurrence): the prover's minimal missing cap and the obstructor's violated-fact
  diagnosis are the same statement from opposite sides. Next attack filed: `aism-n7i` (P0) —
  hiddenness consumption via exposer-failure witnesses + the two-observable machinery;
  `lem-canonical-separator` re-establishment as sub-target.

## 2026-07-06 — W26 (session 11): hiddenness consumed — the LP-dual witness; the two dual FORMS differ (α family)

- **The witness (reviewed).** `lem-hiddenness-dual-witness`: a hidden row vertex v yields λ ∈ Δ(F_v),
  α, β ≥ 0 with Σβ = t*(v) < κ and Σλ_f(p_f−p_v) + Σα_i(p_i−p_v) = Σβ_i(p_i−p_v). Pairing with an
  affine ψ (ψ(p_v)=0, 0 ≤ ψ ≤ E, **E > 0 required for strictness** — VP's correction) gives a ρ-far
  row with ψ(p_f) < κE. First banked fact that CONSUMES hiddenness (the W25-mandated input).
- ❌ **Easy to get wrong: the two dual forms are NOT interchangeable.** Worker Q's "gauge" form
  (far barycenter within κ·(2+4δ) of p_v, NO positive-slack family) matches its exact fixtures
  (rank-5: ‖q_far−p_v‖₁ = t*·D exactly) but was NOT independently verified; VP's validated dual
  RETAINS the α family, so in general the far combination reproduces p_v only up to the
  (1+A−B)-scaling with A unbounded a priori. Cite only the validated form; reconciling them
  (when can α be dropped?) is an open presentation question.
- **The W25 insufficiency certificate is DEAD under canonical geometry** (worker Q, exact): the
  3×3's labeled-hidden top has t* = 100/101 (visible), W = {v,s}, H = 0. Insufficiency arguments
  must now respect the F9/F10 canonical classification — label games are closed.
- **The remaining step-4 gap, sharpened:** nothing couples the witness to row-v's OWN coefficients
  (σ₄). Q's interface for any future refuter: a sustained G₄ web where EVERY hidden carrier has a
  ρ-far barycenter returning within κ(2+4δ) — no such construction exists (bounded search, T3).

## 2026-07-06 — W27 (session 11): trunk <2>6 paid — and the registered op-exposed-hull contract has a loose-δ mismatch

- **<2>6 re-derived + hostile-verified** (`lem-hlc-implies-exposed-hull`, c = 1/4, C = max{4,C₁}):
  under the direct registered HLC form the inherited localization detour (C' = max(4A,1/√a)) is
  unnecessary. W-nonemptiness made an EXPLICIT hypothesis (def-height needs it; op-hlc's contract
  is silent — same gap W30 attacks independently).
- ❌ **AUDIT FINDING: op-exposed-hull's registered contract, read literally, is NOT what the
  assembly proves.** With a FREE upper bound δ ≥ δ(P) the threshold κ = c√δ GROWS while the
  proven margin stays √(δ(P))/4 — the implication only holds at δ = δ(P). Closing the literal
  wording needs the robustness lemma W_{4√d,√d/4} ⊆ W_{C√δ,c√δ} (d ≤ δ ≤ δ₀) — OPEN, named.
- ❌ **The nearby matrix Q is row-sum-one signed with δ(Q) ≤ d — NOT proved stochastic, NOT
  idempotent.** The <2>7 consumer (thm-classical-factorization) must be audited against exactly
  this interface; do not quietly assume a stochastic idempotent was produced at <2>6.

## 2026-07-06 — W28 (session 11): the parametric assembly is codified; the δ=0 endpoint rides on def-exposed's non-strict ≥

- `lem-min-a-implies-height` (conditional on conj-min-a-w4): H ≤ 13τ for 0 < δ ≤ (17−12√2)/2,
  W nonempty — the D1 assembly at B = 13, now a registry edge (aism-yxa scope closed).
- ❌ **δ=0 endpoint definition-sensitivity** (`lem-delta-zero-endpoint`): at τ = 0 the far set
  includes v itself and every admissible exposer has minimum EXACTLY 0; visibility holds because
  def-exposed tests t*(v) ≥ κ (non-strict). Any future definition change to strict > would BREAK
  the endpoint — the shard body carries this warning.

## 2026-07-06 — W30 (session 11): W-nonemptiness first bricks; the anchor obstruction named

- **Kernel(i) strata now reviewed:** δ=0 (lem-delta-zero-endpoint, W28), simplex row polytopes
  (lem-simplex-visibility), rank ≤ 2 (cor-rank-two-visible), sharp vertices
  (lem-sharp-vertex-visibility — hull over geometrically DISTINCT other rows, nonempty; the
  singleton case is excluded by hypothesis). Rank ≥ 3 non-simplex is the OPEN production theorem.
- **The candidate mechanism, blind-convergent three ways** (T's gap == U's obstruction == the W26
  witness): hiddenness needs VISIBLE ANCHORS — every hidden vertex's far barycenter leaned on
  visible rows in every construction (297 exact audits, found_W_empty=False). Next wave shape:
  assume W = ∅, every vertex hidden, apply the dual witness at an extremal vertex, contradict.
- ❌ **Easy to get wrong:** lem-sharp-vertex-visibility does NOT assert sharp vertices exist;
  existence is the open question. And the simplex hypothesis is genuinely restrictive (the
  banked rank-5 W19 matrix: 6 vertices, affine rank 4 — not a simplex, W nonempty anyway).

## 2026-07-07 — W29 (session 11): depth-Markov banked with WEAKENED hypotheses; the pincer certified end-to-end

- **lem-hiddenness-depth-markov holds for ANY witness at ANY delta > 0** (VW's correction
  strengthened the lemma): the c-parametric bound needs only Σβ < κ; tallness + δ ≤ δ₁ enter
  only the 2√2/3 G₄-corollary (exact: 1/2 + δ₁ = 3(3−2√2), strict even at the endpoint).
  No complementary slackness is used ANYWHERE in the reviewed witness toolkit — CS (the
  optimal exposer h* = t* on λ-support / 1 on β-support / 0 on α-support, paired with row
  reproduction: v's positive mass on {h* ≥ s} is ≤ ν_v/s) is an UNTOUCHED coupling channel.
- ❌ **α on the top slab is uncontrollable** (lem-hiddenness-alpha-slab-leakage bounds ONLY the
  deep slab, in absolute mass): α-mass at v itself is invisible to the balance equation. Any
  coupling argument must live with top-slab α or eliminate it structurally.
- **The pincer, now exact-certified from the refuter side (W29-X):** true-hidden constructions
  fold back before depth 4τ (best certified frontier H/τ = √(5/99) ≈ 0.225, G₄ = ∅, σ₄ ≡ 0,
  with exact witnesses at both hidden tops); tall attempts die by absorption. Bounded search,
  NO emptiness claim — but any future refuter must beat this certified interface.

## 2026-07-07 — W31+W32 (session 11): ONE mechanism under both open ledger items

- **The strategic convergence:** conj-min-a-w4's gap (couple the witness lambda / low-exposer
  slab to the row coefficients P_vj^+ — W29/W32) and the W-nonemptiness rank>=3 gap (upgrade
  the tangent-companion slab defect from O(tau) to O(tau^2) — W31) are the SAME missing shape.
  Any mechanism that charges slab/witness geometry to row coefficients (or squares the defect)
  closes BOTH. Registered attack surface: conj-low-slab-coefficient-cap (W32's successor
  statement) + the theta-flexible target CAP_{a,theta} (ANY universal theta>0 wins; B = K_a/theta).
- **lem-cs-low-slab-pincer shape (pending VZ):** for ANY admissible exposer h at v, positive
  row mass on {h >= s} is <= nu_v/s [row reproduction + sign split]. Consequence: a cap
  counterexample packs > 1-theta-4tau of the top's positive mass into G_a ∩ {h* < kappa} —
  the SAME slab hiddenness forces >94% of the witness mass into (depth-Markov). The two
  measures cohabit; nothing yet relates them.
- ❌ **Easy to get wrong:** the CS channel bounds mass ONLY where exposers are HIGH; the low
  slab (including all self/top-cluster mass at h(p_v)=0) is invisible to it. Do not cite the
  pincer as a sigma_a cap — it is exactly half of one.

## 2026-07-07 — W35 (session 11): absorption round 1 — proximity is real but sub-scale; the transition captured exactly

- **No lone mule** (lem-single-heavy-recipient-rho-shadow): a (1−τ)-heavy recipient of a row's
  mass sits INSIDE the ρ-ball (27τ/8 < 4τ at δ ≤ 1/16) — cap counterexamples must SPREAD deep
  mass. And receiving mass = proximity in general (lem-received-mass-proximity).
- ❌ **Proximity ≠ absorption.** At the cap scale (σ_A > 1−θ−4τ) the proximity bound
  ~ D(θ+4τ) EXCEEDS ρ even at θ = 0 — after the CS pincer spends 4τ, proximity alone can
  never reach the exposedness-exempt scale. The cap's true content is
  **cluster-to-EXPOSEDNESS**, not cluster-to-proximity.
- **The absorption transition is now an exact object** (W35-AD bundle): one 1-parameter rank-5
  family, hidden with R_{1/4} ≈ 0.105 at s = 1403/1000, absorbed (t*₅ = 51/569, H = 0) at
  s = 351/250; R₄ = 0 in every certified true-hidden construction; the δ = 1/4 LP comparison
  shows coefficient capacity is NOT the blocker — exact geometry is. W36 target: identify the
  functional that crosses zero at the transition and generalize the exposer that appears.

## 2026-07-07 — W36 (session 11): the absorption mechanism NAMED — the rho-halo exemption; the bridge in final form

- **Absorption spends the halo exemption, not coefficient capacity** (exact, twice-computed:
  AE + hostile VAE re-solved the LP from scratch): in the certified W35 transition family the
  exposer margin is a RATIO of affine-circuit coefficients (negative anchors / FAR positive
  support), and t* JUMPS (17/417 → 51/569) when the heavy circuit partner enters the ρ-ball —
  the crossing quantity is the clone-invariant ρ-excess ‖p_j − p_v‖₁² − 16δ. No t* = κ
  crossing occurs; visibility flips with the far set.
- ❌ **Easy to get wrong:** the ρ-far set vs the far POSITIVE CIRCUIT support are different
  sets (VAE's correction); and with the ≥ρ convention the partner is still far AT the
  threshold equality.
- **THE BRIDGE (the program's last named gap, 4th independent confirmation, sharpest form):**
  shipped row mass (P_vj⁺) vs affine-circuit mass (witness/dependency coefficients — note the
  hiddenness dual witness IS a circuit through p_v). Untried hybrid for W37: substitute row
  reproduction into the witness balance ONCE — the resulting second circuit has coefficients
  λ_f·P_fk, a genuine row/circuit hybrid object.

## 2026-07-07 — W37+W38 (session 11): the dual-direction wall; the residual cancellation; ONE conjecture left

- **The dual-direction wall (VAF-confirmed):** every feasible circuit (incl. v's own row,
  normalized — lem-row-far-dual-certificate, SHARP on the W29 frontier: nu/L_F = t* exactly)
  UPPER-bounds t*; hiddenness cannot be run backward through upper bounds, and rho-NEAR mass
  contributes ZERO to L_F. The lambda*P hybrid is non-amplifying (lem-hybrid-dual-certificate).
- **The residual cancellation (worker AG, VAG verifying):** in the self-cluster split the
  far-deep term cancels EXACTLY (A(H-a*tau) <= nu(H+D)); a pure rho-near cluster with
  S = 1 - O(tau) is CONSISTENT with every banked identity — the renormalized budget
  nu/(1-S) exactly pays the height at 1-S = O(tau). The self-cluster route via residuals is
  DEAD as attempted.
- ❌ **def-exposed normalizes by VALUE, not Lipschitz constant** (worker AG's catch): rows
  4tau-close need NOT have comparable exposedness LPs — any near-cluster interlock needs a
  conditioning lemma first. Do not assume exposer transfer across near rows.
- **EVERYTHING now converges on ONE conjecture: conj-near-cluster-absorption** (== the W36
  rho-halo mechanism made universal == cluster-to-exposedness == conj-low-slab-cap's residual
  content): in the tall regime, heavy positive mass on the rho-near deep cluster of a hidden
  top forces exposedness of some cluster vertex. Five independent routes (witness coupling,
  rank-3 tangent, CS pincer, absorption proximity, residual cancellation) all bottom out here.

## 2026-07-07 — W39 (session 11): levers (a)/(c)/(d) all reduce to TWO primitives

- **Lever (a) closed:** t* does NOT transfer across 4τ-near rows (value normalization has no
  gradient control along thin hull directions — the cloning escape; basepoint shifts break
  the box). **Lever (c):** the deepest-vertex collapse is a corollary of banked material and
  forces TOTAL deep mass, not ρ-near deep mass. **Lever (d):** far-set shift fails at scale;
  the aggregated-witness circuit carries unbounded center coefficients (1 + A_u − B_u).
- **THE TWO PRIMITIVES under conj-near-cluster-absorption:** (i) the ALPHA-GAUGE lemma — the
  dual's alpha is objective-free (a free ray); does a minimal-alpha optimal witness have
  controlled A (complementary slackness structure)? (ii) PRIMAL EXPOSER construction — dual
  circuits only upper-bound t*; exposure needs an explicit margin-κ exposer (the W36 anatomy)
  or a lower bound over ALL duals. Everything else is bookkeeping around these two.

## 2026-07-07 — W40 (session 11): the alpha gauge solved; THE BLOW-UP IS REAL; the fork

- **The witness free ray is exactly priced** (lem-zero-face-alpha-gauge): minimal alpha = the
  zero-face conic gauge of the tangential residual; clone-only zero faces give alpha-free
  witnesses (all banked fixtures: A_min = 0). CS geography: alpha lives ON the optimal
  exposer's zero face (not transverse — the orchestrator's guess was corrected).
- ⛔ **LP-only alpha bounds are DEAD** (obs-realized-alpha-blowup, VERIFIER-STRENGTHENED): an
  explicit exact 4x4 signed idempotent (delta = eps) has a hidden vertex whose EVERY optimal
  witness carries alpha = 1/eps — a thin zero-face row forces it. Do not re-run alpha-bound
  attempts without tall-cluster structure.
- **The general capacity threshold** (lem-row-zero-capacity): admissible harmonic candidates
  vanishing at row i pay kappa*(far-target mass) <= nu_i — the W36 anatomy in general
  position; full-exposer feasibility is EQUIVALENT to non-hiddenness (LP duality — the primal
  and dual routes are formally one).
- **THE FORK (sketch v10):** (i) does the alpha blow-up coexist with the TALL heavy-cluster
  mode (exact-certificate decider; the alpha-slab leakage bound controls alpha only OFF the
  top slab, and the blow-up alpha sits ON it — genuinely open both ways)? or (ii) assemble a
  non-aggregation finisher from the capacity threshold + residual cancellation. Fund (i)
  first: it is decidable and either branch re-prices everything.

## 2026-07-07 — W41 (session 11): topness vs the blow-up; radial thickness = the priced endgame

- **The conditional bound (lem-radial-alpha-bound, VAN-corrected):** A_min = ||R||_1 / (radial
  reach of the residual direction in the CONVEX HULL of zero-face displacements) — hull, not
  cone (the free conic mass normalizes); R = 0 gives A_min = 0. Thickness mu =>
  A_min <= (1+tau/4)(2+4delta)/mu. ONE-WAY only.
- **The certified dichotomy (W41 bundle, four exact families, double-rerun):** the alpha
  blow-up and the hidden-TOP condition are mutually exclusive in every certificate — forcing
  v to stay top collapses A_min to 0. Support for conj-tall-zero-face-radial-thickness exactly
  at tops; no tall thin-zero-face instance exists in the record.
- ❌ **Easy to get wrong:** radial thickness implies the alpha bound, NOT conversely; and
  bounded alpha only unblocks witness AGGREGATION — the dual-direction conversion (feasible
  circuits vs primal exposer) remains a separate wall. The endgame stack is now:
  conj-tall-zero-face-radial-thickness -> tall alpha control -> aggregation -> (still) the
  primal conversion -> conj-near-cluster-absorption -> conj-low-slab-cap -> [two RIGOROUS
  engine links] -> Kernel height clause.

## 2026-07-07 — W42 (session 11): residual cancellation is the mechanism; the cluster-uniform correction

- ❌ **The thickness route's hard stop, exact:** value-normalized exposedness NEVER turns
  "h* = O(delta) on the cluster" into "h* = 0" — the missing LP statement is optimal-face
  selection (min over optimal h* of h(p_j) for a near-deep nonclone row = 0). Do not re-run
  thickness waves without an optimal-face selection idea.
- **The mechanism in the certificates is RESIDUAL CANCELLATION** (VAO-reconfirmed: the W41
  TOP-preserving optimal witness has alpha = 0, R = 0): topness acts by making the optimal
  face contain an R = 0 datum, not by measurable hull reach. Reformulated terminal target.
- **The cluster-uniform correction (AP, VAO-confirmed scope):** conj-tall-zero-face-radial-
  thickness controls only v's OWN datum; the aggregation needs alpha control for witnesses of
  EVERY mass-carrying cluster vertex. The single-statement alternative: the row-to-circuit
  absorption bridge (cheap bounded-alpha witnesses everywhere on the cluster => v ships mass
  outside C or some cluster vertex is exposed).
- **L2 flags honored:** the heavy-cluster low-slab and top-residual-slab statements are
  DUPLICATES of banked material (pincer corollary; alpha-slab/depth-Markov engine) — not
  codified. One new shard only: lem-bounded-alpha-top-slab-reduction.

## 2026-07-07 — W43 (session 11): the terminal node in final geometric form

- **The alpha-free/R=0 condition is EXACTLY a convex intersection** (VAQ VALID):
  conv{always-tight far displacements} ∩ t*·conv{always-tight upper displacements} ≠ ∅.
  Predicts every banked certificate residual-by-residual. VAQ's strengthening: any dual
  optimum complements EVERY primal optimum; O empty is impossible for alpha-free at t* > 0.
- **THE program's remaining Route-A content, final form:** prove the intersection nonempty
  CLUSTER-UNIFORMLY at tall heavy near-cluster tops ((T1)), or the row-to-circuit bridge
  ((T2)). Membership in T/O is always-tightness on the WHOLE optimal face (the W42 hard stop
  stands — near-zero values certify nothing).

## 2026-07-07 — W49/W50 (session 12): the tightness-promotion wall named; literature negative space

- **The two Tier-1 faces reduce to ONE difficulty: whole-optimal-face TIGHTNESS PROMOTION
  under tall/heavy.** (F1)'s residual (promote row-positive far balance-witnesses into T,
  BF) and (F2)'s residual (select fat blockers / exclude thin near-clones, BD) are the same
  wall — the W42 hard stop in sharper clothes. Ledger-only proofs are certified dead on both
  faces (the BD thin-blocker graft gadget: kappa-high mass t*eps; verification VBD pending).
- **In-class disjointness has NEVER been realized** (BE exact frontier): every starving-
  blocker/disjointness construction dies at G_4 = C_4 = empty, H < 4*tau; restoring topness
  restores the intersection. The faces are two shots at one truth.
- **DEAD ROUTE (literature, W50): spectral-gap => structure imports for (F2).**
  Hartfiel–Meyer, LAA 272 (1998) 193–203 [stated, not byte-matched]: subdominant eigenvalue
  near 1 forces near-uncoupling only at FIXED n, threshold degrading with n. The whole
  Simon–Ando/NCD/metastability apparatus is dimension-DEPENDENT — the (F2) mass floor must
  be built natively and clone-invariantly. Do not re-walk.
- **The solved sibling + its trap (W50):** Salzmann–Bergh–Datta arXiv:2405.01532 Thm 5.2
  fixes a VECTOR (sqrt-eps, dimension-free, sharp; Lemma 5.5 reset-trick importable); the
  abstract foregrounds the dimension-DEPENDENT application — triage from §5, not the
  abstract. Our problem fixes a MAP; per-vector-to-global reassembly IS the Kernel content.

## 2026-07-07 — W49F (session 12): the faces merge; the tall class has never been realized

- **(F2) == (T1) on the restricted domain** ([[prop-f2-t1-equivalence]], VFP2-verified):
  c0 was a certificate of emptiness, not a constant to hunt. The exposure horn is VOID in
  tall regimes (ball-cluster reading). The terminal node is ONE face.
- **NO banked instance is in-class** (VFP2 exact recomputation: all three census H^2/delta
  ratios < 16). Every (T1)-domain claim to date is about an EMPTY certified record —
  refutation is gated behind the never-solved tall-construction problem; TALL-EMPTINESS
  (= the height clause, via the huddle anatomy of lem-zero-face-vertex-support) is a live
  candidate theorem, not just a fallback.
