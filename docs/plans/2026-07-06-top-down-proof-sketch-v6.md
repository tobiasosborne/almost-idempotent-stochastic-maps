<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 6 (session 10,
  round 3) — THE CANONICAL STRATEGIC MAP. Supersedes
  docs/plans/2026-07-06-top-down-proof-sketch-v5.md (kept intact — banked artifacts cite its
  line numbers) after wave W25 (the step-4 decider): step 4 is REDUCED to the single conjecture
  conj-min-a-w4 plus ONE named missing input — HIDDENNESS consumption (t*(v) < kappa) — with the
  verified lem-top-concentration as the first brick and an exact INSUFFICIENCY certificate
  pre-refuting any attempt from the bare scalar fact-list. The once-applied maximum principle's
  yield is a LOWER bound on the deep hidden web (it pushes mass IN, not out).
STEWARDSHIP CONTRACT (user mandate, 2026-07-06, BINDING): this sketch is the MOST DYNAMIC AND
  FLUID artifact in the project. Keeping it reconciled with newly acquired knowledge is a
  FIRST-CLASS DELIVERABLE of every session — a wave that changes the map without updating the
  sketch is INCOMPLETE WORK (Rule 9). At every session close: reconcile every banked wave
  against this file; move anything killed into RETIRED (with its certificate); re-price the
  OPEN LEDGER; keep the UNSCOPED-SURFACE list current. Supersede by a NEW dated file (never
  edit history out of an old version); update the pins (HANDOFF START-HERE, CLAUDE.md router,
  bd memory 'proof-sketch-stewardship') when the filename changes.
STATUS DISCIPLINE (L0): a SKETCH — promotes nothing. Tags: [rigorous] = af-validated in-repo;
  [reviewed] = independent-review-approved paper proof; [mod-audit] = inherited/unreviewed;
  [worker-T1] = fresh-codex paper proof, unreviewed; [priced: X] = gap-table price;
  [OPEN] = missing mechanism; [DEAD] = refuted, certificate cited.
MEASURE OF PROGRESS: unscoped/unpriced surface SHRINKING — never activity counts.
PROVENANCE: v5 + the session-10 round-3 banked wave (docs/waves/2026-07-06-W25-step4-decider)
  + the codifications lem-top-concentration (reviewed) and conj-min-a-w4 (conjecture).
-->

# Top-down proof sketch v6: op-classical (2026-07-06, session 10 round 3)

## THEOREM (op-classical) — unchanged

There exist universal constants eta0, C > 0 (independent of dimension n) such that: for every
row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta0 there is a stochastic idempotent E
with ||Q-E||_{inf->inf} <= C*sqrt(eta). The exponent 1/2 is optimal.

Global objects as in v1/v2 (delta, nu_i, tau = sqrt(delta), W(P), H, chart machinery). Frame
unchanged from v2: **the trunk is Kernel-rooted**; the (EX)/chart engine is an attack route
INTO the trunk, not an equivalent restatement (DC4; session 9 reinforced the redraw twice —
Route A sharpened under pressure while the (EX)=>Kernel edge did not move).

## TRUNK (the theorem-facing chain; prices from DC4, unchanged by session 9)

**<2>1. Signed normalization.** P := theta(2Q-I). [rigorous: lem-classical-equiv; anchor
Kitaev 2405.02434 Prop 3.1 — ref still unpinned, aism-5de]
**<2>2. Reduction to signed rounding.** [elementary]
**<2>3. Affine frame + row reproduction.** [rigorous-elementary]
**<2>4. THE INPUT — Kernel Conjecture (conj-kernel).** Universal delta_0, B: W(P) nonempty and
every hidden row vertex v with sigma~_v > tau has dist_1(p_v, conv W) <= B*tau. [OPEN — the
single theorem-facing input; Route A primary, Route B held; fallbacks below]
**<2>5. Kernel => HLC.** [DONE at reviewed tier (W22, session 10 round 2):
`lem-kernel-implies-hlc` (proved/af:none, hostile-verifier VALID; C_1 = max{B,3}); `op-hlc`
registered as the trunk's middle DAG node; `op-exposed-hull` rewired to consume it. Raw sigma
is FALSE as a cap quantity — always halo-robust sigma_g.]
**<2>6. HLC => op-exposed-hull.** [mod-audit; moderate; never independently checked here]
**<2>7. Clusters + rounding.** [mod-audit with THREE priced interface gaps (DC4): cluster
interface; approx-simplex interface; JB identification]
**<2>8. Distance accounting.** [T1 short, after <2>5-<2>7]
**<2>9. Sharpness.** ex-hume + SBD Rem 5.4. [mod-audit + anchors; not blocking]

**⚠ TRUNK STALENESS RULE (session 9; session-10 round 2 PAID the debt — <2>5 done at reviewed
tier via W22). The rule stands for what remains: <2>6 (HLC ⇒ op-exposed-hull re-audit) and
<2>7 (the three interface gaps) are now the ONLY unreviewed links between a proved Kernel and
op-classical — one of them enters every session's wave mix.** They cap the value of ALL
upstream work (a proved Kernel would still land on a mod-audit chain with priced holes).
STANDING RULE: every session promotes at least one trunk item
(<2>6 re-audit / one <2>7 interface lemma; tracker aism-23b; aism-pu0 CLOSED by W22)
into its wave mix. Cheap, parallelizable, de-risks everything.

## ROUTE A to <2>4 — direct geometric (PRIMARY)

**THE PROOF OBLIGATION (MIN-A, minimal form — new in v3, from W18-R1's refinement):**

> If an exact signed idempotent P (0 < delta <= delta_0, W nonempty) has H > (29/8)*tau, then
> SOME hidden top vertex v has sigma_g(v) <= 1/2. (Contradiction closes the height bound: in a
> tall configuration the validated collapse forces EVERY hidden top above 1/2.)

This is strictly weaker than v2's CAP-1/2-for-all-hidden-tops. **CAP-1/2** (sigma_g <= 1/2 at
every hidden top, ANY height) remains the clean SEARCH/REFUTER surface — a single exact
realization of sigma_g > 1/2 stresses the route; certified record after W19:
`sigma_g = 5991/80000 ~ 0.075` (~6.7x margin; three not-an-emptiness stamps). Chain to Kernel:
MIN-A => H <= (29/8)*tau [via the af-validated collapse; D1 assembly twice worker-derived,
exact constants 29/16 & 29/8, UNCODIFIED — aism-yxa] — plus W-nonemptiness [genuine gap,
untouched] and the delta=0 endpoint [short]. CAP-1/2 and the height bound are NOT equivalent
(both W18 workers independently; never cite them interchangeably).

**THE WALL, renamed (W19): EXPOSEDNESS ABSORPTION — not capacity, not the ledger.** The exact
LP relaxation places 5/4 mass on designated outside recipients; exact geometry then absorbs
high-mass recipients into W (H = 0). A proof must show absorption is FORCED at the 1/2 level;
a refuter must defeat it. The B3 one-sided-ledger and B4 class-count walls do NOT bind CAP-1/2
as stated (W18: TRANSFERRED / BINDS-ONLY-O(1)); the surviving named residual is the
**constant-mass shallow-genuine exclusion** (mass at dist > tau/4 with separator-depth < tau/4
must stay <= 1/2 - 4*tau*(2+4*delta)).

**Mechanism surfaces (redrawn in v3, ranked):**
- **M1 — absorption forcing via THE G-BOOTSTRAP (USER-ADOPTED target of record; session-10
  status: steps 1+2 STAND, steps 3+4 open, the a-gap named).** Skeleton:
  (1) for the genuine set `G_a = {j : dist_1(p_j, C_W) > a*tau}` (halo width `a` TUNABLE), the
  observable `g := P*1_{G_a}` (SIGNED row mass on G) is EXACTLY P-harmonic — `Pg = P^2 1_G
  = P 1_G = g`, one line from idempotence, clone-safe; and `sigma_g(v) - nu_v <= g_v <=
  sigma_g(v)`, so the MIN-A contradiction antecedent reads `g > 1/2 - delta` on every hidden
  top. [rigorous on arrival; realized in W20: 1842 exact harmonicity + 9564 sandwich checks,
  clone-transport realized on an example]
  (2) LEMMA A: visible rows are g-small — **PROVED (C = 4, a >= 4): -nu_w <= g_w <= 4*tau**,
  exposer-pairing against row reproduction, `a >= 4` used exactly once (the halo-to-rho-far
  inclusion); fresh-codex prover + SEPARATE fresh-codex adversarial verifier VALID (7/7) +
  mutually-blind refuter converged NOT-REFUTED. Codified `lem-visible-g-small` [reviewed;
  af: none — elevation proposal aism-88r]. Refuter frontier: `g_w = sqrt(147/569)*tau ~ 0.508*tau`
  at `a = 1/4` (largest certified; harmless to the a >= 4 claim). (W21)
  **THE A-GAP — CLOSED mod-review (W23, round 2):** `lem-parametric-halo-collapse` [reviewed]
  generalizes the af-validated collapse to ANY width: `H(1-sigma_a) <= (sigma-sigma_a)*a*tau
  + nu*(2+4delta)`; forced-mass curve **T(a) = 5a/2 + 3** (T(1/4) = 29/8 exactly = W18's
  constant; **T(4) = 13**). MIN-A's antecedent updates to **H > 13*tau**: above it every
  hidden top has `sigma_4 > 1/2`, hence `g^{(4)} > 1/2 - delta`, at the SAME width where
  Lemma A caps visible rows at 4*tau. Genuine numerical gap iff **delta < (17-12*sqrt2)/2
  ~ 0.0147** (delta_0 for the bootstrap must sit below this — universal, acceptable). Route
  (ii) (small-a Lemma A) is OPEN-BOTH-SIDES and MOOT (W23 worker I: the (a*tau, 4*tau) annulus
  is priced by no tool; no exact family enters G_{15/4}; L3 bundle) — do not fund unless
  step 4 turns out to need a < 4. D1 codification (aism-yxa) should now target the parametric
  form (B = 13 at width 4).
  (3) disintegration — **DONE at reviewed tier (W24): `lem-genuine-disintegration`**:
  `g_i <= M_i^a + sum_{j in G_a} P_ij^+ (H-d_j)/(H-a*tau)` with M_i^a supported entirely on
  HIDDEN row vertices at depth (a*tau, H]. Honest limits kept loud: no vertex count, no web
  structure, no uniform slack bound.
  (4) **DECIDED INTO A CONJECTURE + A NAMED INPUT (W25, round 3).** The once-applied maximum
  principle CANNOT close from the reviewed fact-set: (i) its actual yield is now a REVIEWED
  lemma — `lem-top-concentration`: at hidden tops, sum_{j notin G_a} P_vj^+ <=
  nu_v(2+4delta)/(H-a*tau), forcing the deep hidden-web mass UP (M_v^4 > 1/2 - delta -
  tau(2+4delta)/9 in tall width-4 configs) — the local principle pushes mass INTO the near-top
  band; (ii) an exact INSUFFICIENCY certificate (3x3 idempotent, L3 bundle
  runs/2026-07-06-w25-step4-decider/, orchestrator-recomputed 17/17) satisfies EVERY banked
  scalar fact with a sustained web while its labeled-hidden top is ACTUALLY exposed — so any
  proof MUST consume HIDDENNESS: t*(v) < kappa, the failure of every admissible exposer against
  some rho-far row, which NO banked lemma uses. THE FRONTIER STATEMENT (codified):
  **conj-min-a-w4** — in tall width-4 configs SOME hidden top has sigma_4 <= 1/2; with the
  parametric collapse this closes H <= 13*tau (delta <= delta_1), the Kernel height side at
  B = 13. [OPEN — attack aism-n7i: exposer-failure witnesses + the two-observable machinery
  (mass-g + affine deficit H - phi, both harmonic; the support functional of
  lem-top-concentration is the deficit's first-principles form); sub-target: re-establish
  lem-canonical-separator (mod-audit) if the deficit is used beyond first principles.
  obs-deep-leakage: still demoted; the hiddenness input, NOT the depth ledger, is what W25
  proved mandatory.]
  Wall-evasion audit (unchanged from v3, all held under W20/W21 pressure): B3/c15 one-sided
  ledger — `g = Pg` is an IDENTITY; c10/obs-fwr-gap class count — g is one aggregated scalar
  field; B4 FAIL-1 — exposedness is CONSUMED at W (Lemma A's proof does exactly this), never
  produced; cloning — g clones consistently (realized); sterile iteration — max principle
  applied once. KILL CRITERIA (standing, both UNREALIZED in W20/W21): a certified visible row
  with `g >> tau` at `a >= 4` (kills Lemma A — now would CONTRADICT a reviewed proof, i.e.
  expose a definition-level error); a certified band-supported family with `g >= 1/2`
  coexisting with `g|_W <= C*tau` (kills step 4 — prerequisite: any construction with depth
  `> 1*tau`, which is itself unrealized).
  Subsumed: the earlier block-idempotence idea — `g` is the row-sum shadow of the
  `P[.,G]` block identity. The old M1 phrasing ("global mass dichotomy") is the SHAPE this
  candidate instantiates; the uniform pointwise version stays dead (B4 FAIL-1).
- **M2 — external quotient packing at C/tau** via `conj-external-poke-charge(A)` [UNCODIFIED —
  aism-pld; MANDATORY self-mass exclusion: the self-inclusive form is T0-refuted by instance B
  (229/3200 > 1/20)]. If the poke charge holds at any constant, CAP-1/2 follows from
  #classes <= C/tau, which NO recorded certificate blocks (W19-B consequence table). The
  per-class folklore as previously written is RETIRED (below). [OPEN, conditional]
- **M3 — the genuine-SELF-mass cap (NEW surface, named by W19-A's record mode).** The current
  sigma_g record is carried by the hidden top's OWN row sitting beyond the halo; no recorded
  bound caps genuine self-mass below 1/2, and M2's external lemma says nothing about it. Any
  MIN-A proof must handle this mode explicitly. [OPEN, previously unnamed]
- **M4 — chart-toolkit transport.** Blocked by the same D5 weight bridge as Route B's <3>3;
  keep last. [OPEN, blocked]

**obs-deep-leakage (RE-PRICED, round 2):** status HEURISTIC; the historical depth-ledger steps
consumed it, but the round-2 width-4 surface (parametric collapse + Lemma A + disintegration)
was derived WITHOUT it. It is no longer a standing Route-A blocker; the step-4 wave design
decides whether it is consumed at all (aism-tq3, check-at-design). Any assembled argument that
DOES consume it stays non-rigorous until its re-establishment.

**Deciders (re-ranked 2026-07-06 session 10 round 3; aism-7pe DONE — the wave, not the step):**
(1) **aism-n7i (P0) — conj-min-a-w4 via HIDDENNESS consumption** (exposer-failure witnesses +
two-observable machinery; lem-canonical-separator re-establishment as sub-target); (2) trunk
<2>6 re-audit (the staleness rule's next debtor); (3) aism-88r extended — af elevation of the
reviewed QUINTET (+ lem-top-concentration, deps: none — USER DECISION); (4) aism-yxa re-aimed —
the parametric assembly (B = 13); (5) aism-pld (M2 fallback; gated on depth > 1*tau).

## ROUTE B to <2>4 — via the chart engine (DEMOTED in v3: held at the K3 decision point)

Why demoted: (i) the <3>3 edge ((EX) => Kernel/HLC) is priced possibly-Kernel-sized (W17: D5
weight transport = THE wall, D4 quantifier bridge, D7 self-support); (ii) zero movement in
session 9 while Route A sharpened; (iii) the engine's sole open K3 link `conj-b-restricted` is
fragile (amplifier wall 0.77764 with/without the block; direct-FE floor collapsed to 23/1000).

**The ONE sanctioned Route-B action:** the **alpha->1 continuation** (kill/rescue for the
direct-FE route into conj-b-restricted; queued since session 8; follow-up waves MUST emit full
matrices). If it KILLS: K3 needs a new mechanism — reassess the whole route. If it RESCUES:
the isolated theorem to prove is the D_J/B floor, and the route re-opens for funding.
Otherwise arms A/D/G are FROZEN (sunk cost is not a reason to pull; 43 pulls accumulated).

Structure retained for the record (details + line-cited prices live in v2, kept intact):
<3>1 (EX) [OPEN] -> <3>2 lem-factorization [rigorous] -> <3>3 the dictionary [OPEN, priced by
W17: D1/D8 proved short; D4+D5+D7 genuine gaps; D6 dead]. Engine block K1-K5 as in v2
(K1 taxonomy [bookkeeping]; K2 unified financing horn [hard]; K3 = conj-b-restricted [sole
open link, K >= 0.7708 forced, K_G = 17K+20]; K4 nesting-aware assembly [bookkeeping-hard;
v1's additive formula remains RED]; K5 rank transfer [moderate]).

**Route-independent assets (NOT demoted):** the 16 af-validated results — fan-payment trio,
pivot/import/cancellation toolkit, collapse/residual/mass-split geometry — serve any route.

## Fallbacks (rescoped by session 9)

- **Arm E (error-bound route): fallback with ONE live question, NOT a shortcut.** DEAD, both
  with certificates: black-box Luo-Pang (E1: Assumption 4.1 blocker — (E^2-E)_ij is
  sign-indefinite on P_n; fixed-n sqrt not free, staged Ex. 4.2 exponent <= 1/4) and the
  nonnegative-QUADRATIC residual at every n (E2 KILL-1, twice-independent: interior rank-one
  idempotent continuum + boundary idempotent force clone-invariant blindness). LIVE: E-int-1
  (fixed-n feasible-slice sqrt bound with stratum-data constants, then measure n-dependence)
  + the degree->=3 / stratified residual (exact n=2 cubic hatch F_2=(a-b)^2((1-a)+b) <= eta
  with zero set exactly S_2; needs a non-Cor-4.1 engine). Standing constraints: clone-lift
  invariance (proved for the (EB) formulation itself); aff(S_n) = full stochastic affine space
  (SOS-of-linear permanently dead). [aism-5an]
- **SBD reset-trick transfer probe** (fixed-vector -> idempotent-map; Lemma 5.5): queued,
  unrun (aism-1qd).
- **Kitaev-style incremental bootstrap**: unprobed alternative to one-shot charts.

## RETIRED in this redraw (do not re-walk; certificates cited)

1. **conj-no-free-frontier as a live mechanism.** Wall-blocked since B4; its per-class prose is
   unprovable-as-written and its self-inclusive reading is T0-contradicted (W19-B). ACTION
   PENDING: formal supersession by conj-external-poke-charge(A) at codification (aism-pld) —
   until then do not cite it as a route.
2. **The old cap phrasings** `sigma_v <= 1 - c*tau` (raw) and `sigma_g <= 1 - c`: superseded by
   MIN-A + CAP-1/2. (fr arm-B target string updated to match, 2026-07-06.)
3. **The "12x census slack" framing** and any equivalence-flavored citation of D1 (cap <=/=>
   height bound; W18 both workers).
4. **The per-class hostable-mass folklore as written** (W19-B: only M_X <= 1+delta is
   derivable; two missing charges named).
5. **E-int-2** (nonnegative-quadratic residual): E2 KILL-1, clone-invariant, every n.
6. **Black-box Luo-Pang application** (E1). Never re-derive arm-E plans from lit-review §1.3
   without its 2026-07-05 correction note.
7. (Carried from v2:) raw-sigma cap statements; K<1>6 additive master formula (RED, DC3);
   broad conj-nsc; capped Gamma-emptiness; the v1 sigma-door prose as a proved edge.
8. **Zoo/adversarial g-MEASUREMENT as a step-4 decider** (new, session 10): W20 certified that
   `G_a` is empty zoo-wide for every `a >= 1` — no known construction enters the band, so
   measuring g further decides nothing about the band-web residual. Certificate:
   `runs/2026-07-06-w20-g-zoo-measurement/` + docs/waves/2026-07-06-W20. (Constructions
   realizing depth `> 1*tau` would REOPEN this — that realization problem is the actual
   frontier, folded into aism-pld/aism-sg6.)
9. **Lemma A as an open surface** (session 10): proved + reviewed (`lem-visible-g-small`,
   W21); only its af elevation (aism-88r) and the a-gap extension (aism-sg6) remain. Do not
   re-run prove-or-refute waves on the a >= 4 statement.
10. **THE A-GAP as an open front** (session 10 round 2): CLOSED mod-review by
    `lem-parametric-halo-collapse` (W23; T(a) = 5a/2+3, T(4) = 13). Do not re-open unless the
    step-4 argument fails specifically at the width-4 threshold.
11. **Small-a Lemma A waves (route ii)** (session 10 round 2): OPEN-BOTH-SIDES and MOOT (W23
    worker I, L3 `runs/2026-07-06-w23-a-gap/`); fund only if step 4 turns out to need a < 4.
12. **Step-3 disintegration as an open surface** (session 10 round 2): done at reviewed tier
    (`lem-genuine-disintegration`, W24).
13. **Step-4 attempts from the bare scalar fact-list** (session 10 round 3): pre-refuted by the
    W25 insufficiency certificate (`runs/2026-07-06-w25-step4-decider/`, 3x3 exact idempotent,
    orchestrator-recomputed) — any attack on conj-min-a-w4 MUST consume hiddenness (t* < kappa)
    or some other true fact absent from the list. The once-applied principle alone yields only
    the LOWER bound (lem-top-concentration).

## THE OPEN LEDGER v5 (everything between here and a full proof, priced)

Trunk (blocking regardless of route):
1. <2>4 Kernel — THE input. [OPEN]
2. <2>5 Kernel ⇒ HLC. [DONE reviewed — lem-kernel-implies-hlc + op-hlc wiring, W22]
3. <2>6 re-audit. [moderate; NOW THE OLDEST DEBT — next session's mandatory trunk item]
4. <2>7 three interface gaps. [moderate-to-genuine; STALE]

Route A (primary): 5. MIN-A via M1 = THE G-BOOTSTRAP [round-3 state: steps 1-3 reviewed;
step 4 REDUCED to **conj-min-a-w4** + the named HIDDENNESS input (W25; lem-top-concentration
reviewed = the verified half; insufficiency certificate pre-refutes bare-fact-set attempts);
M2 poke-charge = fallback; M3 subsumed]; 6. obs-deep-leakage [demoted; W25 proved the missing
input is hiddenness, not the depth ledger; aism-tq3 dormant]; 7. W-nonemptiness [genuine;
SBD reset import aism-1qd is the candidate tool; consumed by conj-kernel itself — Kernel(i)];
8. delta=0 endpoint [short]; 9. D1 codification re-aimed at the parametric form [bookkeeping,
aism-yxa].

Route B (held): 10. alpha->1 continuation [the kill/rescue gate]; everything else frozen
behind it (K2 hard; K3 open; K4 bookkeeping-hard; K5 moderate; <3>3 possibly Kernel-sized).

Fallback: 11. arm E E-int-1 / degree->=3 residual [open; funded only if Route A stalls].

Sharpness: closed mod-audit (not blocking).

## Unscoped surface remaining (drives the next BFS round)

- conj-min-a-w4's proof mechanism: how to turn t*(v) < kappa (a universal statement over
  admissible exposers — the definition of hiddenness) into the width-4 cap sigma_4 <= 1/2.
  This is now the sole unscoped mathematics of Route A (aism-n7i). Everything else about
  step 4 is scoped: the verified concentration lower bound, the insufficiency boundary, the
  exact constants.
- M3, the genuine-self-mass cap: inside the g-frame by construction (g counts self), but no
  standalone bound if the bootstrap dies. Keep named.
- The distinct-multi-class question (absorption classwise vs accumulation): decider designed,
  unrun (aism-pld).
- conj-external-poke-charge(A): uncodified; its prove-or-refute wave unrun.
- The constant-mass shallow-genuine exclusion: mechanism unknown (the W18 residual).
- alpha->1 continuation: unrun (Route B's gate).
- Trunk <2>6-<2>7: <2>5 paid (W22); <2>6 is now the oldest debt (mandatory next trunk item).
- obs-deep-leakage: heuristic; demoted from standing blocker to step-4 design question.
- E2's degree-3 hatch: single n=2 witness; generalization unprobed.
- Refs unpinned: Kitaev, SBD (aism-5de); Mangasarian-Shiau 1986+1987, Facchinei-Pang, Kollar,
  D'Acunto-Kurdyka (aism-1nh).

## What this sketch is for — and how to keep it alive

Wave design (every wave names its node HERE), honest scoping, and orientation for every future
agent. A sketch promotes NOTHING (L0). **Stewardship (binding, see header):** reconcile after
every banked wave; retire with certificates; re-price the ledger; keep the unscoped list
current; supersede by dated file with pins updated (HANDOFF, CLAUDE.md router, bd memory).
v2 remains on disk, superseded, for line-number citations by banked artifacts.
