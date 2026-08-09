# UNWIRED.md — registry ids intentionally OUT of the paper (report/) track

**Policy.** `scripts/check-provenance.py`'s `check_anchor` flags every `argument/lemmas/*.md`
result that maps to ZERO `report/` `\label{}` (an *unanchored* statement — never wired into the
sharded lab-book). Historically that was a silent WARN, so a brand-new result could be dropped from
the paper unnoticed. This file is the **explicit whitelist**: an unanchored id that appears here
stays a (silent) WARN; an unanchored id **NOT** here is a hard **ERROR** that fails `check-all`.

The intent: the *exploration frontier* (conjectures, scaffolding lemmas, observations) legitimately
lives ahead of the written narrative and need not be anchored yet — but adding a result to this list
is a **deliberate, reviewable act**, not an accident. When a result is later written into `report/`,
delete its line here.

**Format.** One registry id per line inside the fenced block(s) below. Blank lines and `#` comments
are ignored by the parser (`load_unwired`). Two sections:

- **Frontier (permanent-ish):** exploration-track results with no current paper home.

## Frontier (exploration-track, unanchored by design)

```
# --- 2026-08-09 W140 report sync: 90 af-VALIDATED results anchored into report/sections/52-72 and delisted here (kitaev pair follows with shard 69) ---
# --- 2026-07-27 W80 step-1 F0 seam rows: af-VALIDATED and now anchored in report/sections/42_routef_f0_seam.tex (delisted 2026-07-27) ---
# --- 2026-07-30 MAIN campaign rows (DESIGN-MAIN-STRUCTURE-v5, user-ratified 2026-07-30): pre-elevation; anchor into report on af validation ---
# --- 2026-07-30 S1-ENDGAME ratified rows (DESIGN-S1-ENDGAME-v5, audit v5 LAND): pre-elevation; anchor into report on af validation ---
# --- 2026-07-26 GAP-EA discharge rows (aism-fbh8): pre-elevation; anchor into report on af validation ---
lem-extcb-exact-target-approximation
# --- 2026-07-25 report rescope: off-live-route results, registry records retained ---
conj-degenerate-payment
conj-degenerate-transport
conj-ex
conj-kernel
conj-no-free-frontier
conj-rh
conj-sc
conj-skinny-shadow-cap
ex-hume
lem-always-tight-dual-support
lem-canonical-separator
lem-collateral-import
lem-cross-pivot-cancellation
lem-cs-low-slab-pincer
lem-depth-d-halo-collapse
lem-dual-localization
lem-exposed-circuit
lem-factorization
lem-fan-payment
lem-fan-payment-restricted
lem-genuine-disintegration
lem-halo-collapse
lem-harmonic-affine-bridge
lem-hiddenness-depth-markov
lem-hiddenness-dual-witness
lem-hx-financing-floor
lem-hx-forced-exterior-coupling
lem-hx-robust-scalar-starvation
lem-hx-signed-variation-ledger
lem-hx-transverse-moment-identity
lem-import-reduction
lem-leakage
lem-mass-split
lem-negpart-subadditive
lem-parametric-halo-collapse
lem-pivot-removing-move
lem-residual-lower
lem-residual-upper
lem-row-far-dual-certificate
lem-row-zero-capacity
lem-starvation-completion-obstruction
lem-top-concentration
lem-top-slab-companion
lem-weighted-min
lem-wiggle-rigidity
lem-zerosum-triangle
obs-deep-leakage
obs-fwr-gap
obs-height-collapse
obs-linear-law-finite-delta
obs-orphan-amplifier
obs-sigma-halo-nonrobust
op-exposed-hull
prop-approx-simplex
thm-classical-factorization
thm-cluster
thm-corner-constants
thm-rank-one
thm-simplex
thm-well-exposed
conj-b-restricted
conj-cotop-web-coupling
conj-downhill-zero-face-lower-mass
conj-far-low-slab-cap
conj-gamma-emptiness
conj-low-slab-cap
conj-min-a-w4
conj-near-cluster-absorption
conj-nsc
conj-rank3-cluster-zero-face-reach
conj-shallow-counterweight-exclusion
conj-sl1a-deep-diagonal-cell
conj-sl1a-intersection-diagonal-cell
conj-sl1a-off-diagonal-cell
conj-straddling-web-exclusion
conj-summit-cylinder-exclusion
conj-tall-bounded-alpha
conj-tall-zero-face-radial-thickness
conj-top-deficit-coupling
conj-zero-face-elimination
cor-rank-two-visible
lem-absorption-implies-low-slab-cap
lem-huddle-charge-assembly
lem-intersection-branch-production
conj-l5-gap-1
lem-low-slab-cap-implies-min-a
lem-affine-barycenter-identity
lem-affine-exposer-row-capacity
lem-averaged-deficit-charge
lem-ball-cluster-exposure-void
lem-blocker-capacity-bridge
lem-bounded-alpha-forced-far-slab
lem-bounded-alpha-top-slab-reduction
lem-censoring-exactness
lem-clone-invariant-row-complexity
lem-cluster-return-flow
lem-conditional-g-near-exposer
lem-cotop-witness-pinning
lem-delta-zero-endpoint
lem-disjoint-hulls-forced-alpha
lem-disjointness-huddle-reduction
lem-downhill-cotop-conic-mass
lem-gmax-web-concentration
lem-harmonic-line-coordinate-row-balance
lem-hiddenness-alpha-slab-leakage
lem-hlc-implies-exposed-hull
lem-hybrid-dual-certificate
lem-intersection-witness-confinement
lem-kernel-implies-hlc
lem-l2-core-collapse
lem-l5-mass-barycenter-dualization
lem-l5-positive-flow-foldback
lem-l5-top-face-ray-formula
lem-l5-universal-exterior-payer
lem-ihorn-priced-ray-package
lem-ihorn-tall-halo-saturation
lem-ihorn-dual-cotop-geography
lem-ihorn-universal-exterior-package
lem-ihorn-drift-payer-extraction
lem-ihorn-width-payer-extraction
lem-ihorn-ultra-compression
lem-ihorn-rim-sl1b-package
lem-ihorn-cotop-sl1a-package
lem-ihorn-selected-corner-extraction
lem-icap-single-root-receiver-cap
lem-icap-score-bulk-production
lem-icap-kernel-bulk-census
lem-icap-common-receiver-ownership
lem-icap-tallness-spend
lem-icap-closed-diagonal-flow
lem-icap-type-i-structural-cost
lem-icap-priority-residual-split
lem-dcap-root-closure
lem-dcap-score-bulk-transfer
lem-dcap-kernel-bulk-census
lem-dcap-common-ownership
lem-dcap-tall-same-center-packet
lem-dcap-closed-overlay
lem-dcap-five-way-completion-split
lem-aesc-synthetic-finance-tail-amplification
lem-aesc-synthetic-finance-fixed-k
lem-aesc-guarded-hull-split
lem-aesc-common-tail-union
lem-aesc-separation-geography
lem-dtr-canonical-overlap
lem-dtr-oriented-tail-ray-conversion
lem-dtr-tail-coherent-conversion
lem-dtr-poti-assembly
conj-dtr-zero-oriented-surplus-exclusion
conj-dtr-positive-oriented-surplus-gap-exclusion
conj-w72-poti0-exact-cause-split
conj-w72-poti0-root-selection-exchange-ledger
conj-w72-poti0-fixed-level-starvation-ledger
conj-w72-poti0-root-dilution-selected-support-exchange
conj-w72-poti0-low-deficit-huddle-ray-48
conj-w72-poti0-routine-conditional-assembly
lem-min-a-implies-height
lem-negative-pivot-import
lem-optimal-face-alpha-free-characterization
lem-optimal-face-conic-reduction
lem-positive-exposedness-margin
lem-positive-row-straddle-gamma-lower
lem-psi-corner-trap
lem-radial-alpha-bound
lem-radial-horn-partition
lem-rank3-downhill-dichotomy
lem-rank3-maxchart-hidden-tangent
lem-rank3-optimal-face-interval-reduction
lem-rank3-row-support-tight-spread-criterion
lem-rank3-supporting-functional-pinning
lem-rank3-zero-face-anatomy
lem-rank3-zero-face-min-mass
lem-received-mass-proximity
lem-rho-near-residual-cancellation
lem-self-defect-shadow
lem-separator-zero-face-obstruction
lem-sharp-vertex-visibility
lem-signed-carre-du-champ
lem-simplex-visibility
lem-single-heavy-recipient-rho-shadow
lem-sl1a-corner-ledger
lem-sl1a-score-selector
lem-sl1a-three-cell-reduction
lem-tight-far-geography
lem-top-deficit-price
lem-top-support-dual-face
lem-top-witness-third-actor
lem-two-observable-pencil-bound
lem-visible-g-small
lem-wedderburn-deflation
lem-zero-face-alpha-gauge
lem-zero-face-capacity-kill
lem-zero-face-exchange-identity
lem-zero-face-localization
lem-zero-face-one-sixteenth-capacity-kill
lem-zero-face-vertex-support
# (lem-routef-functional-calculus-closeness, lem-routef-ai-defect-linearization,
#  lem-routef-f2-positive-unital-compression, lem-routef-f3-retract-defect delisted
#  2026-07-27: af-VALIDATED and anchored in report/sections/43_routef_ai_ledger.tex
#  and report/sections/44_routef_f2_f3.tex)
obs-gamma-capacity-scale-blind
obs-gamma-two-level-class-count-wall
obs-rank3-t1-boundary
obs-realized-alpha-blowup
obs-thin-zero-face-blocker-graft
obs-zero-face-perturbation-collapse
op-hlc
prop-f2-t1-equivalence
# Stage-1 topology leaves (landed 2026-07-26, phase-4 prerequisites; to be wired
# into the report with the Stage-1 narrative when phase 4 reaches the paper track)
# Stage-1 polar campaign rows (landed 2026-07-27 per DESIGN-S1-POLAR-v6 sect-9,
# AUDIT-S1-POLAR-v6 LAND, ratified W78 sect-5 step 2; to be wired into the report
# with the Stage-1 narrative when phase 4 reaches the paper track).
# 2026-07-27: the eleven af-VALIDATED polar rows (rows 1-9 plus the two group-law
# children) are now WIRED into report/sections/45-48 and their lines deleted here.
# The rows still listed are unproved or not yet on the paper track.
# 2026-07-28: lem-stage1-smooth-polar-inverse, lem-stage1-smooth-unitary-operations and
# lem-stage1-polar-scalar-arithmetic WIRED into report/sections/49_stage1_smooth_upgrades.tex;
# their lines deleted here.
# 2026-07-28: the six transport rows (13a-d, 13f, 13g) WIRED into
# report/sections/50_stage1_polar_transports.tex + 51_stage1_polar_transports_ii.tex;
# their lines deleted here.
# 2026-07-28 (binder sweep): wiring is independent of status — six of the rows above were
# later RETRACTED the same day (smooth-unitary-operations, maurer-cartan-transport,
# polar-path-transport, inversion-derivative-transport, plus approximate-group-laws and
# inversion-derivative-control in shards 47-48); they stay ANCHORED as conjectures with
# retraction notes, hence correctly absent from this whitelist. Status of record:
# each shard's Status block + report/PROVENANCE.md + docs/LEARNINGS.md.
# 2026-07-28 (W97 landing): the three NEW explicit-binder bridge shards of the endorsed
# rebuild (DESIGN-13E-BINDER-v3.md as amended by v3.1/v3.2; AUDIT-13E-BINDER-v3.2.md LAND);
# unanchored at initial landing per AUDIT-13E-BINDER-v3.md finding 3 — anchor into the
# report (and delete these lines) when the elevation queue validates them.
# 2026-07-29: the three explicit-binder bridges validated and are now WIRED into
# report/sections/49b_stage1_explicit_bridges.tex; their lines deleted here.
# 2026-07-29: lem-stage1-approximate-group-laws-transport, lem-stage1-polar-constant-ledger and
# lem-finite-polyhedron-maximal-simplex-placement af-VALIDATED and WIRED into
# report/sections/51b_stage1_ledger_keystone.tex; their lines deleted here.
# 2026-08-03: the LAND-14 ledger-domains package (14 reserved rows + D2/D3 reconnections)
# landed as stated/af: none. 2026-08-08: the entire ledger-domains queue is af-VALIDATED (T0);
# the rows stay whitelisted here only until the aism-9kmt report sync anchors them on the paper track.
# 2026-08-05: the LEDGER-SETTING-RESCOPE formation row (user-ratified landing,
# LAND-WITH-EXACT-CORRECTIONS); whitelist until af-validated and anchored.
# 2026-08-08: the KLEDGER-STRENGTHENED v2 package (user-ratified; hostile re-audit
# AUDIT-KLEDGER-STRENGTHENED-V2.md VERDICT LAND): the strengthened lem-routef-k-ledger
# replacement (entry retained above) plus three helper rows and the F0 assembly.
# All five af-VALIDATED (T0) later the same day, followed by the user-ratified root
# discharge of op-classical; rows stay whitelisted only until the report sync
# (aism-9kmt) anchors/reproduces them on the paper track.
# 2026-08-08 (W139, user-ratified): the sharpness package — cor-classical-sharpness landed
# stated/none (whitelisted until its Stage-D report anchoring); ex-hume retracted to
# disproved (entry retained above as the historical record's whitelist line).
# 2026-08-08 (W139 factoring, user-ratified; AUDIT-PRHSHARP-FACTOR.md LAND-WITH-EXACT-CORRECTIONS):
```
