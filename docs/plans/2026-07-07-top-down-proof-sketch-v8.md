<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 8 (session 11,
  round 3) — THE CANONICAL STRATEGIC MAP. Supersedes
  docs/plans/2026-07-06-top-down-proof-sketch-v7.md (kept intact — banked artifacts cite its
  line numbers) after the session-11 rounds 2-3 banks (commits 415eb60, 240b616, aa40787,
  95d2e1a, bc622d4): the witness toolkit completed (depth-Markov + alpha-slab + CS pincer +
  pencil bound), the harmonic-affine bridge, the W-nonemptiness strata (simplex / sharp-vertex
  / rank-2 / rank-3 tangent), THE UNIFIED FRONTIER STATEMENT conj-low-slab-cap
  (theta-flexible), and the first af elevation (lem-parametric-halo-collapse, 17th rigorous).
STEWARDSHIP CONTRACT (user mandate, 2026-07-06, BINDING): reconcile after every banked wave;
  retire with certificates; re-price the OPEN LEDGER; keep the UNSCOPED-SURFACE list current;
  supersede by a NEW dated file; update the pins (HANDOFF START-HERE, CLAUDE.md router, bd
  memory 'proof-sketch-stewardship') when the filename changes.
STATUS DISCIPLINE (L0): a SKETCH — promotes nothing. Tags: [rigorous] = af-validated in-repo;
  [reviewed] = independent-review-approved paper proof; [mod-audit] = inherited/unreviewed;
  [worker-T1] = fresh-codex paper proof, unreviewed; [OPEN] = missing mechanism;
  [DEAD] = refuted, certificate cited.
MEASURE OF PROGRESS: unscoped/unpriced surface SHRINKING — never activity counts.
PROVENANCE: v7 + docs/waves/2026-07-06-W29 (dispatch date; harvested 07-07), 2026-07-06-W30,
  2026-07-07-W31/W32/W33 + the af validation of lem-parametric-halo-collapse (915891a).
-->

# Top-down proof sketch v8: op-classical (2026-07-07, session 11 round 3)

## THEOREM (op-classical) — unchanged

There exist universal constants eta0, C > 0 (independent of dimension n) such that: for every
row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta0 there is a stochastic idempotent E
with ||Q-E||_{inf->inf} <= C*sqrt(eta). The exponent 1/2 is optimal.

## TRUNK (the theorem-facing chain)

**<2>1-<2>3.** Unchanged (rigorous / elementary; Kitaev ref still unpinned, aism-5de).
**<2>4. THE INPUT — Kernel Conjecture.** [OPEN, now split EXACTLY as:
(height clause) ⇐ **conj-low-slab-cap** [reviewed-conditional chain, see Route A] and
(Kernel(i), W-nonemptiness) [OPEN at rank >= 3 non-simplex; reviewed strata: delta = 0,
simplex, rank <= 2 — W28/W30; rank-3 all-hidden configs structurally cornered by the tangent
lemma, W31].]
**<2>5. Kernel => HLC.** [DONE reviewed — W22, lem-kernel-implies-hlc.]
**<2>6. HLC => op-exposed-hull.** [DONE reviewed — W27, lem-hlc-implies-exposed-hull,
pinned-delta form; residuals: loose-delta robustness lemma [small, OPEN]; the produced Q is
row-sum-one signed NOT stochastic — folded into <2>7's audit scope.]
**<2>7. Clusters + rounding.** [mod-audit; three DC4 gaps + the stochasticity interface; THE
ONLY unreviewed trunk link below <2>4; next mandatory trunk item — aism-23b.]
**<2>8-<2>9.** Unchanged.

## ROUTE A to <2>4 — the g-bootstrap, now witness-powered (PRIMARY)

**THE FRONTIER STATEMENT (theta-flexible, registered): conj-low-slab-cap** — universal
(a, theta, delta_0): every tall configuration (H > (K_a/theta)*tau, K_a = 5a/4 + 3/2) has some
hidden top whose optimal exposer h* has low-slab coefficient mass
P_v^+(G_a ∩ {h* < kappa}) <= 1 - theta - 4*tau. Composition (all reviewed/rigorous):
cap + [[lem-cs-low-slab-pincer]] ⇒ sigma_a <= 1 - theta ⇒ (af-validated
[[lem-parametric-halo-collapse]]) H <= (K_a/theta)*tau — the Kernel height clause at
B = K_a/theta, for ANY universal (a, theta). conj-min-a-w4 = the (4, 1/2) calibration point
(NOT load-bearing; lem-min-a-implies-height consumes that form).

**The reviewed witness/coupling toolkit (session 11; all L5, af-elevation queue aism-88r):**
- [[lem-hiddenness-dual-witness]] — hiddenness as an LP-dual object (W26).
- [[lem-top-slab-companion]] + [[lem-hiddenness-depth-markov]] — > 94% of every witness's mass
  is simultaneously rho-far AND deep in tall configs (W26/W29).
- [[lem-hiddenness-alpha-slab-leakage]] — alpha controlled on the deep slab ONLY (W29).
- [[lem-cs-low-slab-pincer]] — P_v^+{h >= s} <= nu_v/s for ANY admissible h; SHARP; minimal
  hypotheses (W32). CS can NEVER cap the low slab (VZ gap-honesty).
- [[lem-harmonic-affine-bridge]] — {g : Pg = g} = affine-in-position (u = g); the g-machinery
  IS the exposer machinery (W33).
- [[lem-conditional-g-near-exposer]] — at the g-max hidden vertex (automatic hidden in tall
  windows), hiddenness forces rho-far high-g company (W33).
- [[lem-two-observable-pencil-bound]] — both coupling channels for every admissible affine F;
  the pencil alone yields NO infeasibility (W33).

**The certified pincer picture (W29-X + Q, exact):** true-hidden constructions fold back
before depth 4*tau (best certified frontier H/tau = sqrt(5/99), G_4 empty, sigma_4 = 0, exact
witnesses); tall attempts die by absorption. Any refuter must beat the full reviewed interface.

**Live attack channels on conj-low-slab-cap (aism-2fi, P0):**
1. **g-max self-consistency (W34 IN FLIGHT):** at the g-max hidden vertex r the harmonicity
   ledger sum_j P_rj (g_r - g_j) = 0 concentrates r's mass on near-max-g rows up to O(delta);
   sub-target = the DEPTH-d parametric collapse (re-run the af-validated collapse proof at
   arbitrary hidden vertices — identifies the top-vs-g-max mismatch's correction term).
2. Two-exposer pairing across the deep-carrier web (untried).
3. The quadratic-slab upgrade at rank 3 ([[lem-rank3-maxchart-hidden-tangent]] side, W31:
   area gain Theta(tau^2) vs slab defect Theta(tau) — a coefficient coupling squares it).

**THE UNIFIED MECHANISM (the session's central discovery, FINDINGS 2026-07-07):** the
conj-low-slab-cap coupling gap and the W-nonemptiness rank>=3 production gap are ONE missing
shape — charge slab/witness geometry to row coefficients, or square the slab defect. One
mechanism closes both open ledger items.

**Wall-evasion audit:** unchanged from v7 and held under W29-W33 pressure (identities not
ledgers; aggregated scalars not class counts; exposedness consumed at contradictions only;
clone-robust bridge; single-application ledgers with extremal choices).

## ROUTE B / Fallbacks — unchanged from v7 (held; alpha->1 continuation is the sole
sanctioned Route-B action; arm E fallback per v6).

## RETIRED in this redraw (cumulative; new items only — 1-16 as in v7)

17. **conj-min-a-w4 as THE frontier statement** (session 11 round 2): superseded as attack
    target by the theta-flexible conj-low-slab-cap (the 1/2 is calibration, not mechanism);
    the shard stays (lem-min-a-implies-height consumes it; cap at (4,1/2) implies it).
18. **The pencil-LP infeasibility hope in raw form** (W33): both pencil channels point the
    same way; no infeasibility without a low-slab input. Do not re-run bare pencil waves.
19. **CS/optimality as a standalone cap route** (W32, VZ): mass at h = 0 is invisible to the
    CS identity — a low-slab cap can never come from CS alone.

## THE OPEN LEDGER v8

1. **conj-low-slab-cap** (theta-flexible) — THE Route-A input. [OPEN; W34 in flight]
2. **W-nonemptiness at rank >= 3 non-simplex** (Kernel(i)). [OPEN; same mechanism as 1;
   reviewed strata banked; anchorless route priced at linear-vs-quadratic]
3. Trunk <2>7 (three DC4 gaps + stochasticity interface). [mod-audit; the only unreviewed
   trunk link; next mandatory trunk item, aism-23b]
4. The loose-delta robustness lemma (op-exposed-hull literal wording). [small, named]
5. Rigour ladder: af elevation queue (aism-88r) — DONE: lem-parametric-halo-collapse (17th
   rigorous, 915891a); LIVE: lem-genuine-disintegration; QUEUE: top-concentration,
   hiddenness-dual-witness, cs-low-slab-pincer, harmonic-affine-bridge (all deps-none/clean).
6. Route B alpha->1 continuation [held]; arm E [fallback]; refs unpinned (aism-5de, aism-1nh).

## Unscoped surface remaining

- **The unified coupling mechanism** (ledger items 1+2) — the ONLY unscoped mathematics on
  Route A. Scoped attacks: g-max self-consistency (W34), depth-d collapse sub-target,
  two-exposer pairing, quadratic-slab upgrade.
- Trunk <2>7 audit scope; the loose-delta lemma; dual-form reconciliation (alpha-free gauge,
  presentation-level); M3 self-mass cap, aism-pld, alpha->1 — all unchanged.

## How to keep this alive

Reconcile after every banked wave; retire with certificates; re-price; supersede by dated
file with pins updated (HANDOFF, CLAUDE.md router, bd memory). v7 remains on disk for line
citations.
