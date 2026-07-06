<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 2 (session 8) — the
  canonical strategic map. Supersedes docs/plans/2026-07-04-top-down-proof-sketch.md after the
  DC1-DC4 decision-check wave and two user decisions (2026-07-05): (D1) Kernel is the
  theorem-facing input, (EX) is a separate attack route with an explicitly OPEN edge (DC4 redraw);
  (D2) the broad-NSC successor is capped Gamma-emptiness first (conj-gamma-emptiness), with the
  delta-financed branch-restricted B-lemma as recorded fallback.
STATUS DISCIPLINE (L0): a SKETCH — promotes nothing. Tags: [rigorous] = af-validated in-repo;
  [reviewed] = independent-review-approved paper proof; [mod-audit] = inherited/unreviewed;
  [priced: X] = DC4 gap-table price; [OPEN] = missing mechanism; [DEAD] = refuted, certificate cited.
UPDATE POLICY: rewrite as the architecture changes; keep the open-ledger and the unscoped-surface
  list current. Measure of progress = UNSCOPED SURFACE SHRINKING, never activity counts.
PROVENANCE: strategist synthesis over DC1-DC4 (docs/waves/2026-07-05-DC*.md, all banked verbatim),
  the 4-lane recon (docs/recon/2026-07-05-open-mechanism-recon.md), and the session-7 v1 sketch.
-->

# Top-down proof sketch v2: op-classical (2026-07-05)

## THEOREM (op-classical) — unchanged

There exist universal constants eta0, C > 0 (independent of dimension n) such that: for every
row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta0 there is a stochastic idempotent E with
||Q-E||_{inf->inf} <= C*sqrt(eta). The exponent 1/2 is optimal.

Global objects as in v1 (delta, nu_i, tau = sqrt(delta), W(P), H, chart machinery). One structural
change of frame: **the trunk is Kernel-rooted**. The (EX)/chart engine is an attack route INTO the
trunk, not an equivalent restatement of it (DC4: no proved implication in either direction;
chart-vs-vertex quantifier, weight `P_vj` vs `P_{u_s j}`, and maximal-pivot mismatches all named).

## TRUNK (the theorem-facing chain; every link priced by DC4)

**<2>1. Signed normalization.** P := theta(2Q-I); P^2 = P exact, ||P-Q|| <= c1*eta,
delta(P) <= c1*eta. [rigorous: lem-classical-equiv; anchor Kitaev arXiv:2405.02434 Prop 3.1]

**<2>2. Reduction to signed rounding.** Suffices: every exact signed idempotent P with
delta <= delta0 admits stochastic idempotent E, ||P-E|| <= c2*sqrt(delta). [elementary]

**<2>3. Affine frame + row reproduction.** k = tr P; rows in a (k-1)-dim affine subspace;
p_i = sum_j P_ij p_j; everything downstream clone-invariant. [rigorous-elementary]

**<2>4. THE INPUT — Kernel Conjecture (conj-kernel).** Universal delta_0, B: W(P) nonempty and
every hidden row vertex v with invisible mass sigma~_v > tau has dist_1(p_v, conv W) <= B*tau.
[OPEN — the single theorem-facing input; two routes below]

**<2>5. Kernel => HLC (height cap).** All rows within O(tau) of conv W. [priced: T1 short proof,
recorded at kernel-conjecture.tex:176-221 — needs in-repo transcription + audit; NOT yet a shard]
Upper side already rigorous: obs-height-collapse + conj-halo-collapse (H(1-sigma) <= nu(2+4delta))
[rigorous]. Caution: raw sigma is FALSE as a cap quantity (obs-sigma-halo-nonrobust — exact
sigma > 1 witness); every cap statement must use the halo-robust sigma_g.

**<2>6. HLC => op-exposed-hull.** [mod-audit; priced: moderate; re-audit queued — the first
downstream link that has never been independently checked here]

**<2>7. Clusters + rounding.** op-exposed-hull => thm-cluster / prop-approx-simplex =>
thm-classical-factorization => exact stochastic E. [mod-audit with THREE priced interface gaps
(DC4): (i) cluster interface — dist(rows, conv W) = O(tau) is WEAKER than separated exposed
representatives + disjoint clusters; (ii) approx-simplex interface — near-hull geometry does not
by itself give affine coordinates with O(delta) coefficient negative mass; (iii) JB
identification — the factorization outputs (J, Delta, Upsilon), not an explicit stochastic
idempotent matrix E. Each needs a bridging lemma or a re-derivation.]

**<2>8. Distance accounting.** ||P-E|| <= O(sqrt(delta)). [T1 short, after <2>5-<2>7]

**<2>9. Sharpness.** ex-hume + SBD arXiv:2405.01532 Rem 5.4 + Luo-Pang mechanism. [mod-audit +
anchors; not blocking]

## ROUTE A to <2>4 — direct geometric (the old B-arm line)

Target redrawn by W18 (2026-07-05, session 9; `docs/waves/2026-07-05-W18-route-a-wall-reread.md`):
**CAP-1/2** — universal `delta_0` such that every hidden top vertex has halo-robust
`sigma_g <= 1/2`. With the [rigorous] collapse bound this gives `H <= (29/8)*tau` (D1,
twice-independently worker-derived, exact constants confirmed; STRENGTHENED: cap bounds ALL rows,
the Kernel raw antecedent is unused) and closes Kernel modulo W-nonemptiness [genuine gap] + the
delta=0 endpoint [short]. NOTE: CAP-1/2 is strictly STRONGER than the paired height bound (not
equivalent — both W18 workers independently; it also excludes the low-height/high-sigma_g region).

STATE: **WALL-NARROWED** (was: wall-blocked). W18 verdicts: B3 one-sided ledger TRANSFERRED (not
binding as stated) — the named minimal residual is the **constant-mass shallow-genuine
exclusion**: mass on rows with `dist_1(.,C_W) > tau/4` AND separator-depth `< tau/4` must be
`<= 1/2 - 4*tau*(2+4*delta)`; the class-count dead route BINDS-ONLY-O(1) — CAP-1/2 tolerates
`C/tau` (or `C/delta`) classes, which no recorded family excludes. Honesty flags: the per-class
hostable-mass bound is UNPROVED with ambiguous scale (O(tau) poke vs O(delta) row-negativity);
the depth-ledger steps consume obs-deep-leakage [heuristic — needs re-establishment before any
rigorous assembly]. Ranked surviving mechanisms (W18 Q5(ii), each with kill criterion + decider):
(1) delta-dependent quotient packing + per-class hostable-mass lemma; (2) mass dichotomy
(visibility-or-halo at constant mass; killed-as-uniform-pointwise by B4 FAIL-1, needs a global
form); (3) chart-toolkit transport (blocked by the D5 weight bridge, same as <3>3). [OPEN]

W19 decider results (2026-07-06, `docs/waves/2026-07-06-W19-route-a-deciders.md`): the
per-class hostable-mass folklore is UNPROVABLE-AS-WRITTEN (only trivial M_X <= 1+delta; needs
a sound production rule + a coefficient-poke charge; self-inclusive reading exactly
contradicted by instance B — T0); named codification target conj-external-poke-charge(A).
The sigma_g frontier attack identified the binding constraint = EXPOSEDNESS ABSORPTION (LP mass
capacity is 5/4; geometry absorbs high-mass recipients into W); record sigma_g = 5991/80000
~ 0.075 (rank-5 genuine self), duplicate-splitting inert (one quotient class). Mechanism (2)
is thereby STRENGTHENED as the live shape (absorption IS a mass dichotomy in action); the
sharpest next decider = geometrically DISTINCT multi-class optimization (does absorption bind
classwise, or can total sigma_g accumulate across classes?).

## ROUTE B to <2>4 — via the chart engine ((EX), the arm A/D/G machine)

**<3>1. (EX) (conj-ex).** max_s Phi_s(U0) <= C0*delta at a theta-half Phi-argmin. [OPEN]

**<3>2. Coordinate cleansing.** S*_s <= 2*Phi_s + 6*delta. [rigorous: lem-factorization]

**<3>3. THE NEW NAMED GAP — (EX) => Kernel/HLC.** No proved edge exists (DC4). What a proof must
supply: a dictionary from the chart/pivot frame to the hidden-vertex frame crossing all three
mismatches — (i) one existential argmin chart vs all hidden vertices; (ii) pivot-row weights
beta_s(j) = P_{u_s j} vs vertex-row weights P_vj; (iii) the maximal-pivot restriction vs
arbitrary vertices (needs a pivot/vertex selection lemma). v1's <1>7 "sigma-door financing"
prose was the sketch of this edge; it is hereby demoted to a proof OBLIGATION.
[PRICED by wave 17 (docs/waves/2026-07-05-W17-ex-kernel-dictionary.md): factored D0-D8; proved
short (worker T1): D0, D8, and D1 = only hidden top vertices with halo-robust sigma_g > 1/2
matter (H <= 29tau/8 otherwise, from the validated halo-collapse); GENUINE GAPS: D4 quantifier
bridge + D5 THE WALL (no lemma transports row-v weights P_vj into pivot weights P_{u_s j}) + D7
self-support replacement; D2 (W nonempty) moderate, untouched; D6 carrier-nu DEAD (DC2).
Closability estimate: possibly Kernel-sized — relative value shifts toward Route A. Named
decider: the door ratio max_s S*_s(U)/(sigma_g*H).]

**The (EX) engine itself (Lemma-K block, restructured by DC1/DC2/DC3):**

- **K1. Exhaustive taxonomy.** v1's fan/orphan/self-supported trichotomy is NOT exhaustive:
  silent rows are realized with no tribe (DC3, T0: D3 p/m; D6 p_B). The registered NF_s taxonomy
  (active orphan / lambda-positive orphan / silent) + fan rows + B-carrier auxiliaries is the
  working partition; a shard-level exhaustiveness lemma is REQUIRED. [OPEN, bookkeeping]
- **K2. Unified financing horn.** DC1 (T0 evidence): every certified D-line demand (M_D, L_mu,
  F_L, FIN_lhs) is financed by the ONE G-line budget G_class^- + S_-^mu + SIGMA + FanRes (worst
  ratio exactly 1). The fan lemmas are [rigorous] (2, and 2+sqrt(2) sharp restricted). The open
  content: prove the unified budget inequality (the fused (RSI)+(FIN)+(RH) statement) — this
  REPLACES v1's separate fan-lift (K<1>2) and orphan horn (K<1>3) as one mechanism. [OPEN; hard;
  the single biggest open surface of Route B]
- **K3. Self-support horn.** The (PRT) skeleton chain is [rigorous/reviewed] end-to-end
  (disjunction, (CI) c>0, c<0 import [reviewed], import reduction, cross-pivot cancellation), and
  wave 15's T1 residual makes its assembly EXPLICIT: `M - Phi_r <= 17*B_{r,s} + 20*delta` under
  the box. The single open link is **conj-b-restricted** (`B_{r,s} <= K*delta` at capped argmins
  carrying a clean Gamma-block) [OPEN; hypothesis class certified NONEMPTY by the wave-15
  instance, B/delta = 0.7708 there, so K >= 0.7708 forced; closes the branch with K_G = 17K+20].
  DEAD, both orchestrator-verified: broad NSC (zero-denominator certificate,
  runs/2026-07-05-nsc-zero-denominator-refuter/ — never charge carrier row-negativity) and
  capped Gamma-emptiness (runs/2026-07-05-gamma-emptiness-refuter/ — the FIRST certified capped
  clean Gamma-block; G11's 0/352 was coverage, and the refuting row is high-self, so the
  high-self-restricted emptiness variant died with it).
  Wave-16 state (UNDECIDED, banked runs/2026-07-05-w16-clean-block-b/): sup B/delta = 0.77764
  over 9 certified clean-block instances — the wave-13 record instance ITSELF carries a clean
  block, so the wall binds with and without it; direct-FE identity (T1 exact) + conditional
  theorem: a uniform floor on the carrier self-defect D_J/B (seed 157/500) plus D_J <= C*delta
  gives B <= (C/lambda)*delta. Named decider: minimize D_J/B over clean-block instances.
- **K4. Master assembly, nesting-aware (DC3 restatement).** Phi_s assembled by: (a) the nested
  SC -> RH route on ALL non-fan NF_s demand (incl. silent/high-self rows — charged ONCE); (b) the
  fan-cover payment WITH its explicit FanRes_s(U) residual (FanRes > 0 is realized; either keep
  the term or prove FanRes = O(delta)); (c) the B/self-support delta-term ONLY for auxiliary
  B-carrier mass not already counted in (a). [OPEN as a written shard; v1's additive three-term
  formula is RED (DC3, T0) — do not prove horns against it]
- **K5. Rank transfer.** [OPEN; moderate] Named residuals only: clean Gamma-branch and c<0 move
  untested at rank 4 (decider #1 predates wave 13); extend the existing decider. Fallback:
  Kitaev-style incremental bootstrap.

## Designated fallbacks (unchanged from v1, still unprobed)

- Route B collapses => arm E: dimension-free Holder-1/2 error bound for {E^2=E, E>=0, E1=1}
  directly. STATE after E1+E2 (2026-07-05/06): Luo-Pang is NOT black-box (Assumption 4.1
  blocker, E1); the nonnegative-QUADRATIC residual route is DEAD at every n (E2 KILL-1,
  twice-independent n=2 no-go + clone propagation); survivors = E-int-1 (fixed-n stratum-data
  sqrt constants, then n-uniformity) + the degree->=3 residual (exact n=2 cubic hatch
  F_2 <= eta with correct zero set) / stratified route. Standing constraint: clone-lift
  invariance (E1). [aism-5an re-scoped]
- K2 resists => SBD reset-trick per class (arXiv:2405.01532 Lemma 5.5; composition probe unrun).
- K5 resists => incremental bootstrap becomes primary.

## THE OPEN LEDGER v2 (everything between here and a full proof, priced)

Trunk (blocking regardless of route):
1. <2>4 Kernel Conjecture — THE input. [OPEN]
2. <2>5 Kernel=>HLC transcription + audit. [short-proof, recorded]
3. <2>6 HLC=>op-exposed-hull re-audit. [moderate]
4. <2>7 three interface gaps (cluster / approx-simplex / JB). [moderate-to-genuine]

Route A: 5. CAP-1/2 (`sigma_g <= 1/2` at hidden tops). [OPEN, wall-NARROWED by W18: minimal
residual = constant-mass shallow-genuine exclusion; delta-dependent class-count opening; plus
W-nonemptiness (genuine) + obs-deep-leakage re-establishment (currently heuristic) + delta=0
endpoint (short) for the full Kernel closure]

Route B: 6. (EX) itself via K1-K5: exhaustiveness [bookkeeping], unified financing horn [hard],
conj-b-restricted [open; certified-nonempty hypothesis class; K >= 0.7708 forced; explicit
downstream constants], nesting-aware assembly shard [bookkeeping-hard], rank transfer
[moderate]; PLUS 7. the (EX)=>Kernel edge <3>3. [PRICED (wave 17): D1/D8 proved short; D4+D5+D7
genuine gaps (D5 = the weight-transport wall); possibly Kernel-sized]

Sharpness: closed mod-audit (ex-hume; not blocking).

## Unscoped surface remaining (drives the next BFS round)

- The door-ratio decider (wave 17's named test): max_s S*_s(U)/(sigma_g*H) over rank-3
  families — a single exact counterexample to the door lower bound redraws v3 toward Route A;
  a persistent floor rescues the <3>3 dictionary despite the D5 wall.
- The D_J/B floor decider (wave 16's named test): D_J/B -> 0 kills the direct-FE route for
  conj-b-restricted; a floor isolates the exact theorem to prove.
- ~~Route A's wall record has not been re-read against the new import toolkit~~ DONE (W18,
  session 9): WALL-NARROWED. New named surfaces it exposed:
  - the constant-mass shallow-genuine exclusion (Route A's minimal residual) — no mechanism yet;
  - the per-class hostable-mass lemma: W19-B settled the STATUS (unprovable-as-written; needs
    the coefficient-poke charge; self-mass exclusion mandatory) but NOT the scale — live form is
    conj-external-poke-charge(A) [uncodified]; empirical probe = the distinct-multi-class
    optimization (W19 joint residual);
  - obs-deep-leakage is only [heuristic] but is consumed by every depth-ledger step — needs
    re-establishment (elevation candidate) before any rigorous Route-A assembly;
  - D1 (cap => H <= 29tau/8) is twice worker-derived but uncodified — registry shard pending
    (bd follow-up), NOT yet af-validated.
- FanRes = O(delta): unproved, now load-bearing for K4.
- Silent-row exhaustiveness lemma: unwritten.
- Rank-4 Gamma/c<0 decider extension: not run.
- SBD reset composition probe + arm E decision-check: queued, unrun (aism-78w).
- Refs still unpinned: Kitaev 2405.02434, SBD 2405.01532 (staged; aism-5de).

## What this sketch is for

Wave design (each wave names its node here), the DAG-wiring issue, honest scoping. A sketch
promotes NOTHING (L0). v1 is superseded but kept intact — banked artifacts cite its line numbers.
