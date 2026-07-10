<!--
ROLE: the top-down FULL proof sketch of op-classical, VERSION 25 (W60 engine-bank delta).
  Supersedes v24; everything not restated here is unchanged from v24 (hence v23).
STATUS DISCIPLINE (L0): a SKETCH / STRATEGY artifact; promotes nothing.
-->

# Top-down proof sketch v25: op-classical (2026-07-10, W60 engine-bank delta)

## UNCHANGED from v24

The trunk, the three-cell SL1a surface, all dead routes, the other five leaves
(H-D, H-I, SL1b, L6.5 residuals, L5 minimax), T0 count 29 af-validated.

## Map change 1: the W60 ENGINE BANK is proved (L5) — registry 153 -> 158

Five new lemmas (W60 wave, aism-bgh; codex prover + fresh hostile batched codex
verifier, corrections applied as prescribed; artifacts in
`docs/waves/2026-07-10-W60-artifacts/`):

- `lem-hx-transverse-moment-identity` — basis-free unit transverse moment at
  row-hull endpoint pairs (rank-free W59 Claim 2).
- `lem-hx-signed-variation-ledger` — sign-union budget converter at synthetic
  rows (slab-free W59 Claim 4 pattern).
- `lem-hx-financing-floor` — THE ENGINE: two separated rows must jointly finance
  (1 - A*l_chi)/Lambda - nu(a) - nu(b) positive mass on every high-lever fiber
  set; recentred-ball instantiation with Lambda = (2+4delta)/l.
- `lem-hx-robust-scalar-starvation` — the T0 generalization proper: explicit
  universal ceiling delta_R = min(2^-16, 1/(4H^2)), H = 2L+6B; fiberwise zero-top
  replaced by an O(delta) top-tail cap; metric pin replaced by the window
  [tau/2, 2tau]; NO rank hypothesis. T0 sits at calibration (3,1,0).
- `lem-hx-forced-exterior-coupling` — first forced long-range positive-financing
  lower bound (feeds L6.5); exact vacuity threshold l <= 8delta+16delta^2.

**Consequence for the W59 §HONEST LIMITS gap inventory:** gap 1 (rank > 3) and
gap 2 (slab confinement) are RETIRED at the mechanism level; gap 4's removable
half (the metric/coefficient pins) is de-pinned to a window. The remaining open
content of the T0 -> H-X bridge is: producing, from a bad H-X datum, the actor
scaffold (A, q), the norming functional, and the O(delta) top-tail cap that
`lem-hx-robust-scalar-starvation` consumes — i.e. gap 3 generalized (confinement)
and/or the same-carrier selection (gap 4's hard half).

## Map change 2: the H-X hard residual is a two-route FORK (USER DECISION aism-ur9)

Two independent W60 strategists (Fable + codex ultra; both trees banked in the
wave artifacts) converged on the engine bank but proposed different hard
residuals:

- **Route A (codex, `DECOMPOSITION-W60-CODEX.md`):** prove NAMED H-X exactly:
  X2 microfreight exclusion (prove-or-refute lane; thin transient graft is the
  refuter shape) + X3F/X3N far/near actor selection + X4 top-tail regularization.
  4 creative-hard nodes; no surface change; H-X-selector fallback available.
- **Route B (Fable, `DECOMPOSITION-W60-FABLE.md`):** gamma-fattened three-cell
  renegotiation (N4; gamma = tau/4 vs delta^(3/4) DIAL) + two confinement
  conjectures N5/N6. 2 creative-hard nodes + 1 routine-hard; REQUIRES a surface
  change (strengthened H-I^gamma/H-D^gamma sibling burdens) — user + sibling
  sign-off mandatory.

Cheap L3 deciders exist for both (X2 graft search; leak-financing refuter) and
should run before creative spend. Until the user decides, the engine bank is
consumable by BOTH routes and by L6.5.

## Tier-1 order (updated)

0. Route decision (aism-ur9) + the two L3 deciders that inform it.
1. af-elevation of the engine bank (prime candidate:
   lem-hx-robust-scalar-starvation; all five are single minimal contracts).
2. L5 minimax (aism-vuc, double-valued), E1-E5 codification / small-gauge bridge,
   assembly-bridge repair (aism-pus), SL1b, H-D/H-I — unchanged from v24.
