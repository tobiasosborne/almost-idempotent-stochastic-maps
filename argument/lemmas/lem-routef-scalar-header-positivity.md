---
id: lem-routef-scalar-header-positivity
kind: lemma
contract: Route F scalar-header positivity: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K is finite with K >= 1, rho_fac > 0, and eta_K > 0, these scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions, and eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr, rho_2 <= rho_Delta', rho_2 <= rho_Delta, rho_fac <= rho_DeltaUpsilon <= rho_Upsilon <= rho_Upsilon', rho_fac <= rho_mult, and rho_fac <= rho_UpsilonDelta.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation
status: stated
af: seeded
provenance: definitions/def-routef-raw-factor-setting.md equations (1.1)-(1.8) and the global scalar-header witness exported by lem-routef-raw-factor-setting-formation; factoring and pre-forall quantifier repair designed in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile audit and user ratification.
owner: A
workspace: proofs/lem-routef-scalar-header-positivity
---

**Status.** `stated`, `af: none`. This is a new elementary scalar-header proof obligation.
It promotes no part of the former paper ledger.

**Quantifier scope.** Select the global `W_RF` from
[[lem-routef-raw-factor-setting-formation]] and stop before entering that lemma's
`for every H,Phi,eta`. Equations (1.1)--(1.8) of
[[def-routef-raw-factor-setting]] contain no setting datum or input variable. Hence all
conclusions here are genuinely pre-input and apply to the same `W_RF` later used by the
packet family.

**Scalar route.** The formation header gives positive finite primitive data. Finite
sums, products, reciprocals, minima, and maxima then give positivity and finiteness of
all derived coefficients and radii. The coordinate inequalities of the displayed minima
give the domain chain. In particular `K` is a finite maximum containing `1`,
`rho_fac` is a positive finite minimum, and `eta_K` is a positive finite minimum.

**Designed af budget.** Four designed nodes; honest live expectation 6--12 under the
observed 1.5--3x expansion; at most 3 rounds; hard cap 14. The 3x endpoint 12 is strictly
below 14.
