<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 4 (session 10) —
  THE CANONICAL STRATEGIC MAP. Supersedes docs/plans/2026-07-06-top-down-proof-sketch-v3.md
  (kept intact — banked artifacts cite its line numbers) after the session-10 waves W20
  (g-zoo measurement, aism-vmt) and W21 (Lemma A prove-or-refute + independent verification,
  aism-0b1): a surgical delta of v3 — M1 step 2 is now PROVED+reviewed (lem-visible-g-small),
  the a-gap band (29τ/8, 4τ] is the newly named front, zoo measurement retired as a step-4
  decider.
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
PROVENANCE: v3 (strategist synthesis over v2 + session-9 waves) + session-10 banked waves
  (docs/waves/2026-07-06-W20-g-zoo-measurement, 2026-07-06-W21-lemma-a-decider) + the
  lem-visible-g-small codification.
-->

# Top-down proof sketch v4: op-classical (2026-07-06, session 10)

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
**<2>5. Kernel => HLC.** [priced: T1 short proof recorded at kernel-conjecture.tex:176-221 —
needs in-repo transcription + audit; NOT yet a shard. Upper side rigorous: obs-height-collapse
+ conj-halo-collapse. Raw sigma is FALSE as a cap quantity — always halo-robust sigma_g.]
**<2>6. HLC => op-exposed-hull.** [mod-audit; moderate; never independently checked here]
**<2>7. Clusters + rounding.** [mod-audit with THREE priced interface gaps (DC4): cluster
interface; approx-simplex interface; JB identification]
**<2>8. Distance accounting.** [T1 short, after <2>5-<2>7]
**<2>9. Sharpness.** ex-hume + SBD Rem 5.4. [mod-audit + anchors; not blocking]

**⚠ TRUNK STALENESS RULE (session 9; VIOLATED in session 10 — the g-bootstrap waves consumed
the session on user direction; the debt is explicit: trunk item FIRST in session 11's wave
mix).** <2>5-<2>7 have not moved in THREE sessions, yet
they cap the value of ALL upstream work (a proved Kernel would still land on a mod-audit chain
with three priced holes). STANDING RULE: every session promotes at least one trunk item
(<2>5 transcription / <2>6 re-audit / one <2>7 interface lemma; tracker aism-pu0, aism-23b)
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
  **THE A-GAP (new named front, replaces the loose "constants fight"):** the mechanism needs
  `a >= 4` but MIN-A's tall antecedent guarantees depth only `> 29*tau/8 = 3.625*tau` — the
  band `(29tau/8, 4tau]` is uncovered. Closures: (i) improve the collapse constant past 4;
  (ii) a NEW mechanism for `a in (29/8, 4)` (the rho-far inclusion genuinely fails there);
  (iii) step 3/4 placing the deep-band mass beyond `4*tau` (obs-deep-leakage territory).
  [OPEN — decider aism-sg6]
  (3) disintegration: genuine mass lands on HIDDEN vertices in the depth band, via
  lem-residual-upper [validated] + exposed-vertices-are-in-W. [short, expected T1 — still
  underived; cheap next]
  (4) once-applied maximum principle (delta-slack paid ONCE — no iteration; idempotence makes
  P^t = P, so dynamic/mixing arguments are sterile BY DESIGN and are not used): the web
  `{g >= 1/2}` must be band-self-sustaining while g is small on W and depth-capped on the deep
  side [deep side consumes obs-deep-leakage — elevation aism-tq3 is a blocking dep]. THE
  HONEST RESIDUAL: can a harmonic class-observable hold >= 1/2 on a band-supported set while
  <= C*tau on W? Anti-splitting in ANALYTIC (count-free) form. [OPEN — the kill zone.
  Session-10 pricing: EMPIRICALLY UNREACHABLE — W20 found `G_a` EMPTY zoo-wide for every
  `a >= 1` (deepest banked geometry < 1*tau), so no known construction even enters the band;
  the residual is now purely analytic, and further zoo measurement is RETIRED as a decider.]
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

**Blocking dependency:** `obs-deep-leakage` is status HEURISTIC yet every Route-A depth-ledger
step consumes it — no assembled Route-A argument can be rigorous before its re-establishment/
elevation (aism-tq3). Treat as a prerequisite of any Route-A af work, not hygiene.

**Deciders (re-ranked 2026-07-06 session 10; aism-vmt and aism-0b1 are DONE — W20/W21):**
(1) aism-sg6 — the a-gap band (29tau/8, 4tau]: price/decide closure routes (i) collapse-constant
improvement vs (ii) small-a Lemma-A mechanism vs (iii) deep-mass routing; (2) obs-deep-leakage
elevation (aism-tq3 — blocking dep of step 4's deep side AND route (iii) of the a-gap);
(3) step 3 (disintegration) T1 derivation — short, cheap, underived; (4) aism-pld — poke-charge
codification + distinct-multi-class optimization (M2 fallback AND the only remaining step-4
stress with any teeth, since zoo measurement is exhausted — but note its constructions must
first realize depth > 1*tau to matter); (5) aism-88r — af elevation of lem-visible-g-small
(proposal; user opt-in required).

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

## THE OPEN LEDGER v3 (everything between here and a full proof, priced)

Trunk (blocking regardless of route):
1. <2>4 Kernel — THE input. [OPEN]
2. <2>5 transcription + audit. [short-proof, recorded; STALE 2 sessions]
3. <2>6 re-audit. [moderate; STALE]
4. <2>7 three interface gaps. [moderate-to-genuine; STALE]

Route A (primary): 5. MIN-A via M1 = THE G-BOOTSTRAP [target of record 2026-07-06; session-10
state: step 1 realized; step 2 = Lemma A PROVED+reviewed (lem-visible-g-small; af proposal
aism-88r); step 3 short, underived; step 4 = the analytic anti-splitting residual — kill
criteria standing but empirically unreachable (W20); THE A-GAP (29tau/8, 4tau] = the new named
sub-front (aism-sg6); M2 poke-charge = fallback; M3 inside the g-frame]; 6. obs-deep-leakage
elevation [blocking dep of step 4 + a-gap route (iii)]; 7. W-nonemptiness [genuine; SBD reset
import aism-1qd is the candidate tool]; 8. delta=0 endpoint [short]; 9. D1 codification +
review [bookkeeping, aism-yxa].

Route B (held): 10. alpha->1 continuation [the kill/rescue gate]; everything else frozen
behind it (K2 hard; K3 open; K4 bookkeeping-hard; K5 moderate; <3>3 possibly Kernel-sized).

Fallback: 11. arm E E-int-1 / degree->=3 residual [open; funded only if Route A stalls].

Sharpness: closed mod-audit (not blocking).

## Unscoped surface remaining (drives the next BFS round)

- The g-bootstrap step 4: the band-web question (the analytic anti-splitting residual) —
  still unscoped ANALYTICALLY; empirically unreachable (W20), so scoping must come from proof
  attempts or from a depth->1tau-realization breakthrough, not measurement.
- THE A-GAP (29tau/8, 4tau] (aism-sg6): named, unpriced — none of its three closure routes has
  a worked estimate yet.
- The g-bootstrap step 3 (disintegration): expected-short, still underived.
- M3, the genuine-self-mass cap: inside the g-frame by construction (g counts self), but no
  standalone bound if the bootstrap dies. Keep named.
- The distinct-multi-class question (absorption classwise vs accumulation): decider designed,
  unrun (aism-pld).
- conj-external-poke-charge(A): uncodified; its prove-or-refute wave unrun.
- The constant-mass shallow-genuine exclusion: mechanism unknown (the W18 residual).
- obs-deep-leakage: heuristic, load-bearing.
- alpha->1 continuation: unrun (Route B's gate).
- Trunk <2>5-<2>7: unmoved in THREE sessions (staleness rule VIOLATED in session 10 — debt due
  session 11).
- E2's degree-3 hatch: single n=2 witness; generalization unprobed.
- Refs unpinned: Kitaev, SBD (aism-5de); Mangasarian-Shiau 1986+1987, Facchinei-Pang, Kollar,
  D'Acunto-Kurdyka (aism-1nh).

## What this sketch is for — and how to keep it alive

Wave design (every wave names its node HERE), honest scoping, and orientation for every future
agent. A sketch promotes NOTHING (L0). **Stewardship (binding, see header):** reconcile after
every banked wave; retire with certificates; re-price the ledger; keep the unscoped list
current; supersede by dated file with pins updated (HANDOFF, CLAUDE.md router, bd memory).
v2 remains on disk, superseded, for line-number citations by banked artifacts.
