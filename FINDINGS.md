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
