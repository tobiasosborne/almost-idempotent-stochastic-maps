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
obs-gamma-capacity-scale-blind
obs-gamma-two-level-class-count-wall
obs-rank3-t1-boundary
obs-realized-alpha-blowup
obs-thin-zero-face-blocker-graft
obs-zero-face-perturbation-collapse
op-hlc
prop-f2-t1-equivalence
```
