# Run bundle: W71 POTI-0 zero-overlap growing-rank decider — BLOCKED: the root-ownership repair cost does NOT distribute with rank (exact trade-off law); 0 entrants, 0 refuters; seventh consecutive tallness bind (2026-07-16, session 21)

## Hypothesis

bd `aism-cmk0` follow-on / DTR-ATTACK-W69.md §§1.5, 4.2 (POTI-0 target): can
the freshly registered `conj-dtr-zero-oriented-surplus-exclusion` (G_phi = 0
=> exact (EC)) be refuted — or its hypothesis class even ENTERED — by an
exact growing-rank family in the zero-overlap regime rho(1) = 0, starting
from the W69 seed (which realized the LOCAL DTR geometry at zero finance
negativity but failed every global gate rank-uniformly)? A genuine POTI-0
refuter needs the full pinned package + exact G_phi = 0 + D_EC < 0 (a
W65-leaf refuter additionally D_leaf < 0). The verified W70 interface
(lem-dtr-* L5) supplies the panel: rho(1), t_phi, G_phi, D_POTI, and the
proved orderings D_EC >= D_POTI/S, D_leaf >= D_EC as ASSERTIONS. (Rigour
tag: `numerical` — exact rational L3 evidence, never proof.)

## Finding

**BLOCKED on both exact repair families; no full hypothesis-class entrant,
no POTI-0 refuter, no POTI+ window entrant, no full leaf by-catch.** Fresh
codex xhigh worker, exact rationals, orchestrator-reproduced 2026-07-16
(exit 0). Family-level verdict, NOT an emptiness claim — the conjecture
remains undecided. Key structural findings:

- **The exact trade-off law (the headline):** in the m-anchor/m-probe/one-
  public-row family (tau = 1/(2^20 m), a = 1 - 1/m + tau/20, exact
  P = LB, BL = I_m, genuine rank m in {4,8,16,32}), the maximum row
  negativity obeys the exact law max_i nu(P_i) = beta*a, where beta is the
  public-root mass on the probe-carrier fibers. R0 carrier ownership
  (eta_D* <= P_f*^+) needs beta >= 1/8, while the negativity gate needs
  beta <= tau^2/a — a positive exact gap at every rank and every tau
  (table in REPORT.md). **Repairing ownership at beta = 1/8 drives the max
  single-row negativity to (1/8)*a -> 1/8 with rank: the root-ownership
  repair cost does NOT distribute with rank.** This inverts the W69 lesson
  one level up: local DTR geometry is free, but root ownership is
  order-one expensive in this family — exactly the root-to-top
  synchronization price the POTI-0 proof must formalize.
- **Mechanism reached: (i) support disjointness only.** rho(1) = 0 and
  G_phi = 0 survive both repairs at all ranks — but only OUTSIDE the full
  gate. Mechanism (ii) (positive overlap with orientation starvation,
  t_phi <= D_0*delta) was NOT reached by any tested family.
- **Tallness binds for the SEVENTH consecutive exact batch:** both families
  have K(P) = conv{anchors} inside the visible hull, H = 0, so
  H - 16*tau < 0 at every rank and tau; shallow mass P_v^+(L_v) = 1; ultra
  omega not reached; B5 label NOT_REACHED (with the mandatory warning that
  the B5 population is not eta_D*).
- **The proved W70 orderings pass exactly on every certified instance**
  (D_EC >= D_POTI/S with equality throughout; D_leaf >= D_EC), and the TC
  antecedent is honestly false on these families (r_{alpha,lambda} = 0 at
  the predeclared (r_0, alpha, lambda) = (1/320, 1/2, 1/2)).
- Negative D_EC values on non-entrants (e.g. -3/32 in the ownership-
  repaired family) are formal diagnostics, NOT refutations; D_leaf > 0
  throughout.

## Unit tests (all three pass; red-green discipline)

1. W66/W63 plateau: routes to C0 (ell/tau = 2*tau), fails tallness,
   D_leaf = 8191/524288 > 0.
2. W55 A0 = 5: order-one finance negativity reproduced
   (21475229695/4294967296 > tau^2); small actor residual => T-esc shape,
   routes AWAY from DTR.
3. W69 rank-8 baseline: exact panel reproduced (local D_EC = -7/64, R0
   excess 1/8, H/tau = 0, empty ultra omega) + its NEW POTI panel
   (rho(1) = 0, G_phi = 0, D_POTI = -7/64) as calibration.

## Honest scope

Exact rational (fractions.Fraction) L3 evidence about TWO constructed
families and their repair axes only. The binding inequality
(beta >= 1/8 vs beta <= tau^2/a) is family-specific, NOT a dimension-free
obstruction, and proves nothing about `conj-dtr-zero-oriented-surplus-
exclusion`. No statement about all growing-rank families is made. Nothing
here is promoted; the conjecture remains OPEN.

## Command

```bash
cd runs/2026-07-16-w71-poti0-zero-overlap-decider
PYTHONDONTWRITEBYTECODE=1 python3 -u scripts/search.py   # deterministic, no seed; exact Fractions
```

## Invariant (checkable)

Every claim is an exact `fractions.Fraction` assertion in `search.py`:
P = LB and BL = I entrywise (hence P^2 = P), certified genuine rank = m,
row sums, the exact negativity law max_i nu(P_i) = beta*a per family
member, the ownership/negativity trade-off table (beta >= 1/8 vs
beta <= tau^2/a with the exact gap per rank and tau), the full POTI panel
(rho(1), t_phi, G_phi, D_POTI, D_EC, D_leaf reported separately), the
proved-ordering ASSERTIONS D_EC >= D_POTI/S and D_leaf >= D_EC on every
certified instance, and all three regression fixtures. Exits nonzero on
any mismatch; prints per-family verdicts + trade-off/trend tables + three
unit-test lines + "BLOCKED — ... exact L3 evidence only, never a proof"
(orchestrator-reproduced 2026-07-16, exit 0). `data/certificates.json`
freezes all exact values (sha256
ade9a9eef53063424f1313b32c71e5456f5d29ce2a429b0e4b77ebaa1fff12a1).
Worker: fresh codex (gpt-5.6-sol, xhigh), brief in `BRIEF.md`.

## Next

Feeds the POTI-0 creative wave: the exact trade-off law names the
mechanism to formalize — carrier ownership (eta_D* <= P_f*^+) plus the
delta negativity budget must force either positive canonical overlap
(rho(1) > 0) or an order-one, rank-undistributable cost. A future refuter
attempt must simultaneously repair tallness (H = 0 here, the seventh
consecutive bind) and root ownership while keeping negativity at tau^2 —
no tested family moved ANY of those margins with rank or scale.
Orientation starvation (mechanism (ii)) is untouched territory for both
refuters and provers.

## Files

- `BRIEF.md` — the dispatched worker brief (W71)
- `REPORT.md` — the worker's verdict report (exact tables)
- `scripts/search.py` — self-contained exact-rational search + verifier
- `data/certificates.json` — exact certificates for every family member,
  panels, trade-off and tau-trend tables
