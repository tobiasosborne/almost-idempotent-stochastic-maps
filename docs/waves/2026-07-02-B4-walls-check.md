<!--
ROLE: verbatim harvest artifact of fr arm B, wave 4 (2026-07-02). Worker: opus (adversarial walls-check subagent).
STATUS: L0 exploration report. Mixed tiers, tagged inline T0-T3 (T0 = exact/independently recomputed;
T1 = solid heuristic; T2 = plausible heuristic; T3 = speculative). Nothing here is rigorous. One exact
recomputation inline (instance B arithmetic, tau/kappa/recipient units). Target: conj-no-free-frontier.
Answers bd aism-5yk (a)/(b)/(c). Referenced by .frontier/log.jsonl (arm B wave 4).
NB per L0/§6: this artifact makes NO af elevation and edits no registry/definition/proof shard.
-->

# Arm B · wave 4 · WALLS-CHECK on `conj-no-free-frontier` — harvest (verbatim report)

**Adversarial mandate:** decide whether the exposedness-absorption mechanism *structurally evades* two
recorded obstructions — (a) the one-sided ledger (B3) and (b) the anti-splitting / quotient-packing
class-count dead route. A death certificate is as valuable as an attack plan. I do **not** try to prove
the conjecture.

## 0. The target (contract quoted VERBATIM from `argument/lemmas/conj-no-free-frontier.md`)

> No free frontier (exposedness absorption): for an exact signed idempotent P with 0 < delta(P) <= 1/4 and
> nonempty W(P), every row vertex that is extremal in some C_W-separating direction (a 1-Lipschitz affine
> functional nonpositive on conv W) and whose strictly nearer rows in that direction all lie within ell-1
> distance rho = 4*sqrt(delta) of it is (rho,kappa)-well-exposed with kappa = sqrt(delta)/4.

Read carefully, this contract contains **no coefficient of P**. Its hypothesis and conclusion are purely
*positional* (row locations `p_j`, a direction `u`, `ell-1` distances, an exposedness margin `t*`). It
does not mention `P_vj`, `sigma`, `sigma_g`, or the hidden vertex `v`'s row identity. It is a
membership-in-`W` production rule: *a certain geometric configuration certifies `(rho,kappa)`-exposedness*.
That single fact drives the entire verdict below. **[T0 — reading of the shard.]**

The *intended use* (F2 [check] + the shard's Role field) is the composed cap
`sigma_g <= 1 - c` (equivalently `1 - sigma_g >= c`), which with `conj-halo-collapse`
`H(1-sigma_g) <= (sigma - sigma_g)*tau/4 + nu(2+4delta)` yields `H = O(tau) = O(sqrt delta)`.

---

## 1. Wall (a) — the one-sided ledger. VERDICT: **DODGED (genuinely).** [T1]

B3 (`docs/waves/2026-07-02-B3-sigma-cap.md`, Step B) states the wall precisely. In the primal mass ledger
`Sum_j P_vj^+ = 1 + nu_v`, split into pot 1 `pi_v` (C_W-mass), pot 2 (deep-outside), pot 3 (shallow-outside):

- `sigma-cap (eps=0) <=> pi_v >= nu_v + c*tau` — a **lower bound on pot 1** `pi_v`.
- The harmonic identity `0 = g_v = Sum a_j g_j` (obs-deep-leakage, obs-height-collapse) delivers only
  `M_{>=H} = Sum_{g_j>=H} a_j^+ <= delta(2+4delta)/H`, i.e. **upper** bounds on pots 1+2. The residual
  `1 + nu_v - O(delta)/H` is *forced into pot 3*, which the ledger cannot touch.
- **Named obstruction:** every campaign tool upper-bounds pot 1; the eps=0 cap needs a *lower* bound on the
  identical quantity. One-sided.

**Why conj-no-free-frontier is a different species (a genuine dodge):**

1. *It carries no coefficient of P at all* (§0). It cannot BE a coefficient-mass lower bound at `v`; it is a
   statement about which rows land in `W`. So its own content is orthogonal to the ledger's sign. **[T0.]**

2. *The halo-robust reframing retargets the quantity from a lower bound to an upper bound.* The finisher
   the mechanism feeds is `sigma_g <= 1 - c`, an **upper** bound on the *genuine-outside* mass
   `sigma_g = Sum_{dist_1(p_j,C_W) > tau/4} P_vj^+`. It is emphatically **not** the eps=0 lower bound on
   `pi_v`. The move that makes this legal is the halo escape hatch documented in
   `obs-sigma-halo-nonrobust` / `def-invisible-mass`: the residual mass B3 forced out of pots 1+2 is now
   permitted to live in the `<= tau/4`-halo of `C_W` (dist in `(0, tau/4]`), which is *excluded* from
   `sigma_g`. Instance C realises the extreme: `sigma = 1.069 > 1` (all self-mass at `0.02tau`) while
   `sigma_g = 0`. So we never have to prove "mass is in `C_W`"; we only have to prove "mass is not on
   genuinely-far recipients." That is an upper bound, and upper bounds are exactly the sign the harmonic
   ledger produces. **[T1 — this is the substantive structural gain of the halo-robust program.]**

**Consequence.** Wall (a) as B3 stated it (lower-bound `pi_v`) does **not** apply to the composition
`conj-no-free-frontier => sigma_g <= 1-c`. The quantitative content has been *moved off the ledger's
one-sided axis* onto a positional/exposedness axis. This is real and worth banking.

**Caveat, not a re-instatement of (a):** the harmonic identity only upper-bounds the *deep* part of
`sigma_g`; the *shallow-outside genuine* part (dist `> tau/4` but on the shallow side of the canonical
separator) is precisely pot 3, which the ledger still cannot bound. The mechanism's job is to kill that
shallow-genuine part by exposedness, not by the ledger. So the burden did not vanish — it *transferred*,
intact, to wall (b). This is exactly B3 Step C ("the only lower-bound route = excluding a self-sustaining
shallow web = the anti-splitting / signed quantitative Baake-Sumner frontier"). **[T1.]**

---

## 2. Wall (b) — anti-splitting / quotient-packing class-count. VERDICT: **HITS IT (reduction to the dead route).** [T1/T2]

Two independent failures, either sufficient.

### 2a. Soundness of the conjecture itself at *uniform* kappa = tau/4. [T2]

The hypothesis controls only "strictly nearer rows **in that direction**." Fix the separating direction `u`
with `v` extremal. Build the natural exposer `h(x) = (u.p_v - u.x)/L`. Rows strictly `u`-nearer and within
`rho` are exempt (the `rho`-ball exemption in def-exposed). The margin
`t*(v) = sup_h min{h(p_j) : ||p_j - p_v||_1 >= rho}` is then controlled by rows that are **far in distance
(`>= rho`) yet at near-equal `u`-extremity** (`u.p_j` only slightly below `u.p_v`) — "side rows" off the
top, orthogonal to `u`. Such a row is *not* "strictly nearer in direction `u`," so the hypothesis says
**nothing** about it, yet it drives `t*(v) -> 0` for `u`. To recover margin one needs a *different*
functional, and the hypothesis provides no such control. This is exactly the configuration def-exposed
flags: *"A pointwise exposed-or-redundant dichotomy is provably insufficient (dense regular polygons) — the
gap must be stated globally."* conj-no-free-frontier is a **pointwise** exposedness production rule with a
**uniform** margin `tau/4`; the dense-regular-polygon / equal-extremity-side-row family is the recorded
witness that a uniform pointwise margin is false. **The conjecture is very plausibly false as literally
stated at uniform kappa**, and even the numerics do not test this (see §3). **[T2 — I did not construct an
exact `n`-large signed-idempotent witness; the geometric family is the recorded insufficiency example, not
yet instantiated as an exact P here.]**

### 2b. The composition re-imports the class count. [T1]

Grant, for argument, per-frontier exposure. The finisher must bound the **total**
`sigma_g = Sum_{j genuine-outside} P_vj^+`. The absorption mechanism removes **one** recipient per
separating direction (the frontier extremum joins `W`, `C_W` extends, near-`rho` rows absorbed). To account
for *all* of `sigma_g` one must sum the surviving mass over **every** separating direction / exposed
frontier `v` sees. The shard's own escape — "only mutually-shielding near-coincident twins persist, hostable
mass bounded by poke depth ∝ nu = O(tau)" — is a **per-cluster** bound. Then

  `sigma_g <= (number of distinct surviving genuine-outside quotient classes) x O(tau).`

This is bounded away from `1` (or is `O(tau)`) **iff the class count is dimension-free.** But:

- **No dimension-free bound on the number of quotient classes exists** — the recorded dead route
  (FINDINGS.md; B3 residuals R2/§7.3; the open "signed quantitative Baake-Sumner" / shallow-web-exclusion).
- **obs-fwr-gap** already closed the nearest tool: F-WR "cannot merge simplex-corner clusters and places no
  dimension-free cap on their number; the wide branch is saturated by simplex-corner configurations with
  dimension-many classes." That is *precisely* dimension-many distinct genuine-outside recipient classes.
- The **cloning obstruction** (FINDINGS.md, Rule 13) confirms the axis: cloning a recipient into `N` near-
  coincident copies is a single *quotient* class (twins merge) — so the wall is not about clone-inflated
  index counts but about *geometrically distinct* classes, which high dimension supplies freely.

So the "poke-depth ∝ nu" claim is a TOTAL bound *only if* the class count is `O(1)`, i.e. it silently
assumes the very quotient-packing statement that is the open wall. **The composition reduces
conj-no-free-frontier's cap to the recorded quotient-packing / anti-splitting dead route** — the same
residual B3 §7.3 named ("dimension-free bound on the number of distinct shallow classes hit by `P_v^+`").
This is a *reduction to a dead route*, i.e. a death certificate for the "free progress past the wall"
reading. **[T1.]**

### 2c. The self-defeating branch (why the naive "expose everyone" is not an escape). [T1]

If instead *all* dimension-many distinct genuine-outside recipients were exposed, they would all enter `W`,
`C_W` would become their hull, and `v` (a convex combination of rows) would sit *inside* `conv W` giving
`H = 0` — not a hidden top vertex. So the dangerous configuration necessarily has the surviving classes
*hidden* (mutual-shields), and §2b applies. The mechanism cannot have it both ways: either the classes
expose (then `v` is not a hidden top vertex) or they persist (then their count is the wall). **[T1.]**

---

## 3. Concrete trace on a certified instance (question c) + why the numerics are silent on (b). [T0/T1]

Reusing the exact 5x5 instances of `runs/2026-07-02-sigma-cap-refuter/` (F2 wave). **Instance B** (max
`H/tau` with a *distinct genuine* recipient), independently recomputed here over `Fraction`:

```
delta_B = 74551/1600000 = 0.046594375           tau = sqrt(delta) = 0.2158573...   kappa = tau/4 = 0.0539643...
hidden top vertex v = 3,  H = 0.4617 tau = 0.099661
recipients of positive mass genuinely outside C_W (dist_1 > tau/4):
   self  (row 3) at 0.462 tau,  mass 961/16000 = 0.0600625  ( = 0.2783 tau )
   row 4         at 0.323 tau,  mass  23/2000  = 0.0115     ( = 0.0533 tau ),  dist 0.0697 > kappa 0.0540
```
**[T0 — exact recomputation inline above.]**

Trace of the mechanism on this instance:

- Row 4 is a **genuine-outside recipient that is NOT in `W`** (if it were, `dist(row4, C_W) = 0`, contradicting
  `0.323 tau`). So the mechanism is forced to classify row 4 as a *mutual-shield twin* (case §2b), not to
  expose it. Its hosted mass `0.053 tau` is consistent with the per-cluster `O(tau)` poke-depth claim — for a
  **single** class. **[T1.]**
- This is a **single-class** witness: the certified instances exhibit at most `{self} + {one partner}`
  genuine-outside classes. The multi-class amplification that wall (b) is about — dimension-many distinct
  row-4's each hosting `O(tau)` — **cannot occur in 5x5** (dimension ~5) and never appeared in F2's ~25k
  float search (`k <= 5, m <= 4`). The corner-saturation / cloning obstruction is a *high-dimension*
  phenomenon; small exact instances are structurally blind to it. Hence F2's headline
  `sigma_g <= 0.37 tau`, `1 - sigma_g >= 0.92` is a **low-dimension margin (T3 as evidence for the
  dimension-free cap)** — strong that the cap is not killed by a *cheap* self/halo trick, silent on whether
  it survives dimension-many genuine classes. This matches CLAUDE.md §3 ("Below the corner scale the
  dangerous antecedent has never been entered — that is evidence, not a proof").

## 4. Relation to existing exposedness machinery (question c). [T1]

- `lem-exposed-circuit`, `thm-well-exposed` **consume** exposedness (exposed vertices => concentration =>
  simplex => `O(sqrt delta)`). conj-no-free-frontier is on the **producing** side — a local sufficient
  condition for membership in `W`.
- The producing side's canonical open statement is `op-exposed-hull` ("every row within `C sqrt delta` of
  `conv W_{rho,kappa}`"), which is `>= conj-kernel` and reduces `op-classical`. **conj-no-free-frontier is a
  local shard of exactly that open target**, not a bypass of it. B3 already found `sigma-cap => conj-kernel`
  (possibly strictly stronger). So the mechanism does **not** shortcut the open gap; it *re-expresses* it as
  a pointwise exposedness rule and, per §2, inherits the same anti-splitting/class-count obstruction. It
  neither reduces to nor strengthens `lem-exposed-circuit`; it sits beside `op-exposed-hull` on the open
  producing frontier. **[T1.]**

---

## 5. VERDICT — **CONDITIONAL: dodges wall (a), hits wall (b) [reduction to the quotient-packing dead route].**

- **Wall (a) — one-sided ledger: DODGED, genuinely. [T1]** conj-no-free-frontier carries no P-coefficient
  (§0); it is an exposedness/positional statement, not a mass lower bound at `v`. Composed under the
  *halo-robust* framing, its target is an **upper** bound on `sigma_g` (genuine-outside mass), with the
  residual mass legally parked in the `tau/4`-halo (obs-sigma-halo-nonrobust). This moves the quantity off
  B3's one-sided axis. Real structural gain — bank it.

- **Wall (b) — anti-splitting / quotient-packing: NOT DODGED. [T1/T2]** Two failing steps:
  - **(FAIL-1, T2)** the conjecture's uniform `kappa = tau/4` is a *pointwise* exposedness margin; its
    hypothesis does not control far side-rows at near-equal `u`-extremity, the recorded dense-regular-polygon
    insufficiency (def-exposed) — so the conjecture is plausibly **false as literally stated** at uniform
    kappa (not instantiated here as an exact large-`n` `P`; that is the decider, see below).
  - **(FAIL-2, T1)** even granting per-frontier exposure, bounding the *total* `sigma_g` sums surviving twin
    mass over separating directions and needs the number of **distinct genuine-outside quotient classes**
    dimension-free — exactly the recorded dead route (no dimension-free class count; obs-fwr-gap
    corner-saturation; B3 §7.3 residual). The "hostable mass ∝ nu = O(tau)" claim is per-cluster and is a
    total bound *only if* the class count is `O(1)` — i.e. it silently assumes the wall. **This is a
    reduction to the quotient-packing dead route (Rule 13).**

- **What would decide it (the single crux):** a **dimension-free bound on the number of geometrically
  distinct, genuinely-outside (`dist_1(., C_W) > tau/4`) row-vertex classes that a single hidden top vertex
  can place positive mass on while remaining hidden.** Equivalently the open signed quantitative
  Baake-Sumner / shallow-web-exclusion (B3 R2). If that count is `O(1)` dimension-free, the mechanism
  closes (and one must additionally repair FAIL-1 by strengthening the conjecture's hypothesis to control
  side-rows). If it is dimension-many (the corner-saturation prior), the halo-robust cap is false and the
  correct retarget is the **height-conditional** kernel (B3 Step D / Outcome B).

- **Do NOT `af`-elevate conj-no-free-frontier as the cap route.** Per §6 tripwire and B3 §7.2 it would
  balloon straight into the genuine anti-splitting gap (the class count is a `DAG dep` / `genuine gap`, not
  a `MISSING fact`). The bankable, ledger-immune piece is the *collapse* half (`conj-halo-collapse`, already
  seeded) after its bookkeeping/residual-distance sub-lemmas are factored; the *cap* half remains the open
  quotient-packing wall.

## 6. NEXT PULL

1. Record: the halo-robust reframing is the honest way past wall (a); the cap route's entire residual is now
   the dimension-free class count (unchanged from B3 R2 / §7.3). No new opening — a *localisation* of the
   wall, plus a soundness worry (FAIL-1) about the conjecture as literally written.
2. Cheap decider for FAIL-1: search for an exact signed idempotent with a row `v` extremal in a
   `C_W`-separating direction, all strictly-`u`-nearer rows within `rho`, but a far side-row at near-equal
   `u`-extremity forcing `t*(v) < tau/4` — a direct counter-witness to the conjecture at uniform kappa
   (needs `n` above the corner scale; small exact instances are blind, §3).
3. Do not re-run the low-dimension `sigma_g <= 0.37 tau` search as evidence for the dimension-free cap — it
   is structurally silent on wall (b).
