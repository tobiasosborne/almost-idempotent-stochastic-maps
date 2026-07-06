<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 7 (session 11,
  round 1) — THE CANONICAL STRATEGIC MAP. Supersedes
  docs/plans/2026-07-06-top-down-proof-sketch-v6.md (kept intact — banked artifacts cite its
  line numbers) after the session-11 round-1 triple bank (commit cff8647): W26 (hiddenness
  CONSUMED — the LP-dual witness + top-slab companion, both reviewed), W27 (trunk <2>6 PAID at
  reviewed tier, pinned-delta form, TWO named interface residuals), W28 (the parametric
  assembly CODIFIED — conditional height bound B = 13 + the unconditional delta=0 endpoint).
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
PROVENANCE: v6 + the session-11 round-1 banked waves (docs/waves/2026-07-06-W26/W27/W28) +
  commit cff8647 (five reviewed lemmas) + the in-flight W29/W30 dispatch + the
  lem-parametric-halo-collapse af orchestration (resumed after the overreach-guard restart).
-->

# Top-down proof sketch v7: op-classical (2026-07-06, session 11 round 1)

## THEOREM (op-classical) — unchanged

There exist universal constants eta0, C > 0 (independent of dimension n) such that: for every
row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta0 there is a stochastic idempotent E
with ||Q-E||_{inf->inf} <= C*sqrt(eta). The exponent 1/2 is optimal.

Global objects as in v1/v2 (delta, nu_i, tau = sqrt(delta), W(P), H, chart machinery). Frame
unchanged from v2: **the trunk is Kernel-rooted**; the (EX)/chart engine is an attack route
INTO the trunk, not an equivalent restatement (DC4).

## TRUNK (the theorem-facing chain)

**<2>1. Signed normalization.** P := theta(2Q-I). [rigorous: lem-classical-equiv; anchor
Kitaev 2405.02434 Prop 3.1 — ref still unpinned, aism-5de]
**<2>2. Reduction to signed rounding.** [elementary]
**<2>3. Affine frame + row reproduction.** [rigorous-elementary]
**<2>4. THE INPUT — Kernel Conjecture (conj-kernel).** [OPEN — the single theorem-facing
input; Route A primary. NEW in v7: the height clause is now REVIEWED-conditional on
conj-min-a-w4 (lem-min-a-implies-height, B = 13, delta <= delta_1 = (17-12*sqrt2)/2) and the
delta=0 endpoint is UNCONDITIONAL (lem-delta-zero-endpoint); Kernel(i) (W-nonemptiness at
delta > 0) is the only other input — W30 in flight, simplex-visibility partial [worker-T1].]
**<2>5. Kernel => HLC.** [DONE reviewed (W22): `lem-kernel-implies-hlc`, C_1 = max{B,3};
`op-hlc` the trunk's middle DAG node.]
**<2>6. HLC => op-exposed-hull.** [DONE reviewed (W27, session 11): `lem-hlc-implies-exposed-hull`
— PINNED-delta form (d = delta(P)), W-nonemptiness EXPLICIT, c = 1/4, C = max{4, C_1}; the
inherited localization constant C' = max(4A, 1/sqrt a) is unnecessary. TWO NAMED RESIDUALS
(FINDINGS 2026-07-06 W27): (a) the registered loose-delta contract wording is NOT covered —
robustness lemma W_{4 sqrt d, sqrt d/4} ⊆ W_{C sqrt delta, c sqrt delta} OPEN [small];
(b) the produced nearby matrix Q is row-sum-one signed, NOT stochastic, NOT idempotent — the
<2>7 consumer must be audited against exactly this interface.]
**<2>7. Clusters + rounding.** [mod-audit with THREE priced interface gaps (DC4) + NEW: the
Q-not-stochastic input interface from <2>6. NOW THE ONLY unreviewed trunk link below <2>4 —
the staleness rule's next mandatory debtor (aism-23b: thm-classical-factorization audit).]
**<2>8. Distance accounting.** [T1 short, after <2>5-<2>7]
**<2>9. Sharpness.** ex-hume + SBD Rem 5.4. [mod-audit + anchors; not blocking]

**⚠ TRUNK STALENESS RULE: <2>5 paid (W22), <2>6 paid (W27). What remains: <2>7 (the three DC4
interface gaps + the new stochasticity interface). Every session promotes at least one trunk
item into its wave mix — next: the thm-classical-factorization audit (aism-23b).**

## ROUTE A to <2>4 — direct geometric (PRIMARY)

**THE PROOF OBLIGATION is now EXACTLY ONE conjecture:**

> **conj-min-a-w4** — for every exact signed idempotent P with 0 < delta <= delta_1 =
> (17-12*sqrt2)/2, W(P) nonempty, H > 13*tau: SOME hidden top vertex has sigma_4 <= 1/2.

Everything else on Route A below <2>4 is reviewed:
`conj-min-a-w4 ⇒ H <= 13*tau` [reviewed: lem-min-a-implies-height, W28] `⇒ Kernel height
clause at B = 13 (delta <= delta_1)`; the delta = 0 endpoint unconditional [reviewed:
lem-delta-zero-endpoint, W28]; the ONLY other Kernel input is **W-nonemptiness at delta > 0**
[OPEN, W30 in flight: simplex-visibility partial (every simplex-row-polytope vertex visible at
delta <= 1/4; rank <= 2 corollary; sharp-vertex criterion) — worker-T1, verifier pending;
named gap = the dimension-free production theorem].

**THE G-BOOTSTRAP state (M1; steps renumbered to the v6 scheme):**
- (1) harmonic observable g = P*1_{G_a} [realized, W20]; (2) Lemma A [reviewed:
  lem-visible-g-small, C = 4, a >= 4]; (2') parametric collapse [reviewed:
  lem-parametric-halo-collapse, T(a) = 5a/2 + 3, T(4) = 13; **af orchestration LIVE
  (resumed), 9/14 nodes validated at the guard-restart**]; (3) disintegration [reviewed:
  lem-genuine-disintegration]; (3') top concentration [reviewed: lem-top-concentration].
- (4) **HIDDENNESS CONSUMED (W26, session 11) — the input W25 proved mandatory now has
  reviewed carriers:**
  - **lem-hiddenness-dual-witness** [reviewed]: hidden v ⇒ dual witness (lambda on rho-far
    rows, slack alpha, beta with sum beta = t*(v) < kappa, balance equation); pairing
    consequence for affine psi >= 0 vanishing at p_v (E > 0). The validated form RETAINS the
    alpha family — the alpha-free "gauge" variant (worker Q) is fixture-true but UNREVIEWED
    (FINDINGS W26); do not build on it.
  - **lem-top-slab-companion** [reviewed]: tall configs force a rho-far G_4 inhabitant within
    (1/2+delta)*tau of top height — G_4 is provably NONEMPTY in every tall configuration
    (contrast W20's empty zoo: tall configs, if any exist, are forced into the band).
  - The W25 insufficiency certificate is DEAD under canonical geometry (its labeled-hidden
    top is visible, t* = 100/101 exact — worker Q). Label games are closed; any refuter must
    satisfy the witness constraint at EVERY hidden carrier.
  - **THE SOLE REMAINING UNSCOPED MATH: the coupling** — turn the witness (+ the reviewed
    quintet) into sigma_4 <= 1/2 at some hidden top. W29 IN FLIGHT (aism-hhf, P0), attack
    directions ranked: (i) depth-Markov on the witness at the top (lambda-most witness rows
    deep AND far — codifiable refinement); (ii) structural cascade at deep carriers
    (disintegration hands mass to hidden vertices; each has its own witness; extremal choice,
    no mixing); (iii) complementary-slackness location of witness rows vs row-v support +
    top-concentration; (iv) the two-observable triangle (g, deficit psi = H - phi — both
    P-harmonic — + the witness).
- Wall-evasion audit (unchanged, all held): B3/c15 one-sided ledger — g = Pg is an identity;
  c10/obs-fwr-gap class count — g aggregated; B4 FAIL-1 — exposedness consumed at W, and the
  witness CONSUMES hiddenness (concluding "assumed-hidden is visible — contradiction" is the
  legal exposedness entry); cloning — clone-invariant; sterile iteration — max principle once,
  cascades must be structural-extremal (P^t = P).
- KILL CRITERIA (standing): a certified tall instance where EVERY hidden top has sigma_4 > 1/2
  under canonical geometry + the witness constraint (kills conj-min-a-w4 outright — W29-X
  hunts exactly this); a certified visible row with g >> tau at a >= 4 (would contradict a
  reviewed proof = definition-level error).
- M2 (poke-charge, aism-pld) and M3 (self-mass cap) unchanged as fallbacks; M4 blocked.

**obs-deep-leakage:** demoted, unchanged (aism-tq3 dormant).

**Deciders (re-ranked, session 11 round 1):** (1) W29 = the coupling (aism-hhf, P0, IN FLIGHT);
(2) W30 = W-nonemptiness (aism-jwg, IN FLIGHT; on harvest: hostile-verify + codify the simplex
partial); (3) af elevation queue (aism-88r, IN PROGRESS: lem-parametric-halo-collapse live;
then lem-genuine-disintegration, lem-top-concentration, lem-hiddenness-dual-witness — deps all
af-validated or none); (4) trunk <2>7 audit (aism-23b — the last unreviewed link); (5) the
loose-delta robustness lemma (small, closes op-exposed-hull's literal wording).

## ROUTE B to <2>4 — held at the K3 decision point (unchanged from v6)

Demoted; the ONE sanctioned action remains the alpha->1 continuation (kill/rescue for
direct-FE into conj-b-restricted). Arms A/D/G FROZEN otherwise. Structure and prices in v2/v6.

**Route-independent assets:** the 16 af-validated results + (pending) the parametric collapse
elevation.

## Fallbacks (unchanged from v6)

Arm E: E-int-1 + the degree>=3/stratified residual [aism-5an]; SBD reset-trick probe
(aism-1qd — NOTE: W30-T's sharp-vertex criterion is a first in-repo brick toward Kernel(i)
without the SBD import); Kitaev-style incremental bootstrap unprobed.

## RETIRED in this redraw (cumulative; certificates cited)

1-13. As in v6 (conj-no-free-frontier; old cap phrasings; 12x census slack; per-class
folklore; E-int-2; black-box Luo-Pang; v2 carries; zoo g-measurement as step-4 decider;
Lemma A as open; the a-gap; small-a waves; step-3 as open; bare-fact-set step-4 attempts).
14. **The W25 insufficiency certificate as a live object** (session 11, W26): VISIBLE under
    canonical geometry (t* = 100/101 exact, W = {v,s}, H = 0). Its LESSON stands (consume
    hiddenness); the instance itself decides nothing further.
15. **The localization-form <2>6 constant** C' = max(4A, 1/sqrt a) (session 11, W27): the
    direct registered HLC form gives c = 1/4, C = max{4, C_1} with no high-shell alternative.
    Do not re-import the A/a parametrization.
16. **HIDDENNESS as an unconsumed input** (session 11, W26): it now has reviewed carriers
    (dual witness + top-slab companion). Do not re-run "name the missing input" waves; the
    open question is the COUPLING, not the input.

## THE OPEN LEDGER v7 (everything between here and a full proof, priced)

Trunk (blocking regardless of route):
1. <2>4 Kernel — reduced to: **conj-min-a-w4** [THE open question] + **W-nonemptiness at
   delta > 0** [OPEN; simplex partial worker-T1; W30 in flight]. (Height clause + delta=0
   endpoint: DONE reviewed, W28.)
2. <2>5 Kernel ⇒ HLC. [DONE reviewed — W22]
3. <2>6 HLC ⇒ exposed-hull. [DONE reviewed — W27, pinned-delta; residuals: loose-delta
   robustness lemma (small); Q-not-stochastic interface (folded into <2>7's audit scope)]
4. <2>7 interface gaps (three DC4 gaps + the stochasticity interface). [moderate-to-genuine;
   NOW THE ONLY unreviewed trunk link; next mandatory trunk item — aism-23b]

Route A (primary):
5. **conj-min-a-w4 = the witness-to-sigma_4 coupling** [THE sole unscoped Route-A math;
   W29 in flight with four ranked directions]
6. W-nonemptiness (Kernel(i)) [genuine; first bricks: simplex visibility + sharp-vertex
   criterion, worker-T1 pending review; named gap = dimension-free production theorem]
7. obs-deep-leakage [demoted, dormant]
8. Rigour ladder: af elevation of the reviewed EIGHT (visible-g-small, parametric-halo-collapse
   [LIVE], kernel-implies-hlc, genuine-disintegration, top-concentration,
   hiddenness-dual-witness, top-slab-companion, min-a-implies-height, delta-zero-endpoint,
   hlc-implies-exposed-hull) [in progress, one at a time — aism-88r]

Route B (held): 9. alpha->1 continuation [the kill/rescue gate]; everything else frozen.

Fallback: 10. arm E E-int-1 / degree>=3 residual [open; funded only if Route A stalls].

Sharpness: closed mod-audit (not blocking).

## Unscoped surface remaining (drives the next BFS round)

- **conj-min-a-w4's coupling mechanism** — the sole unscoped mathematics of Route A (W29 in
  flight; the four ranked directions are scoped ATTACKS, the mechanism itself is still open).
- **W-nonemptiness dimension-free production theorem** (named by W30-T): force one
  sufficiently-exposed vertex from P^2 = P at small delta on non-simplex polytopes.
- The loose-delta robustness lemma (small, named, W27).
- The dual-form reconciliation (alpha-free gauge vs validated witness — presentation-level,
  FINDINGS W26).
- M3 self-mass cap; distinct-multi-class decider (aism-pld); conj-external-poke-charge(A)
  codification; constant-mass shallow-genuine exclusion (the W18 residual) — all unchanged.
- alpha->1 continuation (Route B's gate) — unrun.
- Trunk <2>7 audit scope (three DC4 gaps + stochasticity interface).
- E2's degree-3 hatch generalization — unprobed.
- Refs unpinned: Kitaev, SBD (aism-5de); Mangasarian-Shiau etc. (aism-1nh).

## What this sketch is for — and how to keep it alive

Wave design (every wave names its node HERE), honest scoping, and orientation for every future
agent. A sketch promotes NOTHING (L0). **Stewardship (binding, see header):** reconcile after
every banked wave; retire with certificates; re-price the ledger; keep the unscoped list
current; supersede by dated file with pins updated (HANDOFF, CLAUDE.md router, bd memory).
v6 remains on disk, superseded, for line-number citations by banked artifacts.
