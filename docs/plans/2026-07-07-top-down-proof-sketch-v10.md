<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 10 (session 11,
  round 7) — THE CANONICAL STRATEGIC MAP. Supersedes
  docs/plans/2026-07-07-top-down-proof-sketch-v9.md (kept intact for line citations) after
  W39-W41 + elevations #4-#5 (20th: lem-hiddenness-dual-witness, b4038d2; 21st:
  lem-cs-low-slab-pincer, 3689e2c) — commits abda2b5, 0f7cdb4, bb129f1.
STEWARDSHIP CONTRACT (binding): reconcile after every banked wave; retire with certificates;
  re-price; supersede by dated file; update pins on filename change.
STATUS DISCIPLINE (L0): a SKETCH — promotes nothing. Tags as in v8/v9.
MEASURE OF PROGRESS: unscoped/unpriced surface SHRINKING.
-->

# Top-down proof sketch v10: op-classical (2026-07-07, session 11 round 7)

## THEOREM — unchanged. TRUNK — unchanged from v9 (<2>7 + the loose-delta lemma are the only
non-reviewed links below <2>4).

## THE ENDGAME STACK (fully priced; the session's terminal object)

conj-tall-zero-face-radial-thickness  [OPEN — THE bottom question]
  ⇒ (lem-radial-alpha-bound, reviewed)  tall-mode alpha control
  ⇒ (W39-AI aggregation, now coefficient-bounded)  aggregated witness circuits
  ⇒ [OPEN #2: THE PRIMAL CONVERSION — feasible circuits only upper-bound t*; absorption needs
     the margin-kappa exposer or a lower bound over ALL duals (formally equivalent to
     non-hiddenness; lem-row-zero-capacity is the capacity template)]
  ⇒ conj-near-cluster-absorption  [the five-route convergence point, v9]
  ⇒ conj-low-slab-cap  (theta-flexible)
  ⇒ [lem-cs-low-slab-pincer — RIGOROUS #21] sigma_a <= 1 - theta
  ⇒ [lem-parametric-halo-collapse — RIGOROUS #17] H <= (K_a/theta)*tau
  ⇒ Kernel height clause at B = K_a/theta
  ⇒ [reviewed chain: lem-kernel-implies-hlc, lem-hlc-implies-exposed-hull] op-exposed-hull
  ⇒ [<2>7 mod-audit] op-classical.
PLUS: Kernel(i) W-nonemptiness at rank >= 3 [OPEN, shares the cluster/anchor mechanism];
the loose-delta robustness lemma [small].

**The TWO open questions of the stack, priced:**
1. **Radial thickness (why does TOPNESS fatten the zero face?).** Evidence: the certified
   W41 dichotomy — in every exact construction, forcing the blow-up vertex to remain a hidden
   TOP collapses A_min to 0; the blow-up needs a thin zero-face row, and thinness has never
   survived topness. Candidate mechanism: at a top the residual direction points "downhill"
   where near/cluster rows supply hull thickness. VAN-confirmed: slab leakage, depth-Markov,
   and the pincer all miss r_Z — a new mechanism is required.
2. **The primal conversion.** Even with alpha control, aggregated circuits UPPER-bound t*.
   Absorption needs exposure (t* >= kappa) at some cluster vertex. By LP duality this is
   equivalent to the NON-existence of any cheap witness — so the conversion = showing the
   tall heavy-cluster mode kills ALL witnesses of some vertex (not just gauge-fixing one).
   The capacity threshold (lem-row-zero-capacity: kappa*B <= nu at zero rows) is the
   quantitative template; the W36 anatomy is the exact local model.

## The rigour ladder (aism-88r)

af-validated: **21** — session 11 added #17 parametric-halo-collapse, #18
genuine-disintegration, #19 top-concentration, #20 hiddenness-dual-witness, #21
cs-low-slab-pincer. LIVE: lem-harmonic-affine-bridge (#22 candidate, orchestration resumed).
QUEUE: lem-row-far-dual-certificate, lem-depth-d-halo-collapse, lem-top-slab-companion,
lem-hiddenness-depth-markov (deps now af-validated).

## RETIRED in this redraw (new; 1-22 as in v8/v9)

23. **LP-only alpha bounds** (W40): obs-realized-alpha-blowup is the death certificate.
24. **The exact-equivalence reading of radial thickness** (W41, VAN): thickness ⇒ alpha bound
    is ONE-WAY; do not cite the converse.
25. **Cone-reach phrasings of the alpha gauge** (W41, VAN): the correct object is radial
    reach in the CONVEX HULL of zero-face displacements.

## THE OPEN LEDGER v10

1. conj-tall-zero-face-radial-thickness [OPEN — mechanism question #1].
2. The primal conversion [OPEN — mechanism question #2].
   (1 + 2 together close conj-near-cluster-absorption ⇒ conj-low-slab-cap ⇒ height clause.)
3. Kernel(i) W-nonemptiness rank >= 3 [OPEN; anchor/cluster mechanism; reviewed strata banked].
4. Trunk <2>7 (three DC4 gaps + the stochasticity interface) [mod-audit; aism-23b].
5. The loose-delta robustness lemma [small].
6. Rigour ladder queue [in progress]; Route B alpha->1 [held]; arm E [fallback]; refs
   (aism-5de, aism-1nh); report labels (aism-av0, 40+ warn-level).

## Unscoped surface remaining

- The radial-thickness mechanism (question 1) and the primal conversion (question 2) — the
  ONLY unscoped mathematics. Everything else above is priced bookkeeping or held routes.

## How to keep this alive — as in v9 (pins: HANDOFF, CLAUDE.md router, bd memory).
