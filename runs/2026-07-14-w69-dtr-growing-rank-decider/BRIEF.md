# W69 L3 decider — the DTR growing-rank completion refuter (exact arithmetic)

You are a fresh, independent worker. Your workspace is this directory
(registry snapshot `argument/` + `definitions/` + `context/`). Everything you
produce stays inside it. This is an L3 (constructive/numerical evidence) job:
**nothing you produce is a proof**, and your report must say so.

## Target

`context/AESC-ATTACK-W67.md` §4.2, the **DTR target** (and its §1.6(c) "role
of growing rank" analysis): can the diffuse-tail ray conversion residual
`conj-w67-aesc-diffuse-tail-ray-conversion` be refuted — or its hypothesis
class (1.22) even ENTERED — by an exact growing-rank family, before creative
spend? Read AESC-ATTACK-W67.md IN FULL (notation §1.1; it adopts
DCAP-ATTACK-W65.md §1.1 and DECOMPOSITION-W63-I.md §§0-1.1 — read those too).

## The gate (exact rationals — §4.2)

Every candidate is an exact rational factorization P_k = L_k B_k, B_k L_k = I
(certifying P_k^2 = P_k), tau_k -> 0, delta_k = tau_k^2, every row negativity
<= delta_k, the FULL I-base/all-center package, H_k > 16*tau_k, a LEGAL far
selected mass, NONEMPTY ultra omega, theta_k < tau_k/D_{0,k}, the fixed
D-certificate (M_X <= 1/8, M_I < 1/16, M_D > 1/16), all R0/B1-B5/R1 outputs,
and the true ray value. Cloning and transient rank inflation DO NOT count as
rank growth.

**DTR entry (4.5), after the strict HES failure guard (4.3):**
  eta_D*{u : h_u <= 3*delta, min_f ||p_f - x_u||_1 > 3*delta} > 1/160
with h_u = dist_1(x_u, K(P)), x_u = p_u - A~_u(q~_u - p_u) (the (1.6)
normalization). The run must print, carrierwise and in aggregate (4.6):
  Tail_1(u) > tau/8   and   P_f*^+(U_tail) > tau/2560,
plus the exact receiver incidence, its intersections with E_* and L_v, the
realized B5 label, and an explicit warning that the B5 population is
different from eta_D*.

**The decisive refuter** has convex-hull distance <= 3*delta, actual-row
distance > 3*delta, rank and GENUINE support complexity growing (no clones,
no transients), all negativities O(tau^2), tall, and NEGATIVE leaf deficit:
  D_leaf := Z_v(q_A) - c_m*tau/64 + (c_m/16)*P_v^+(L_v) < 0        (4.2)
Also print the residual-contract diagnostic
  D_EC := Z_v(q_A) - (1/8)*P_v^+(E_*) + (c_m/16)*P_v^+(L_v)        (4.1)
**D_EC and D_leaf are NOT interchangeable:** negative D_EC refutes only the
stronger residual contract (EC); a genuine refuter of the pinned A-esc/DTR
leaf needs D_leaf < 0 with the full priority package. Report them separately.

This directly tests §1.6(c): whether growing rank can (i) put x_u within
3*delta of a hull of MANY rows while every single row stays > 3*delta away,
(ii) rotate the normers chi_u so the union keeps incidence but loses a common
scalar sign, and (iii) DISTRIBUTE W55's order-one finance negativity across
many rows. Measure (iii) explicitly: for your best families print the maximum
single-row negativity as a function of rank — does distributing the finance
vector drive it below tau^2 while the other gates stay satisfied, or does
some gate (tallness / far selection / ultra omega / the D ledger) degrade as
rank grows? An exact TREND (gate margin vs rank), even on non-entrant
families, is valuable evidence.

## Unit tests (both must pass in search.py)

1. The W66/W63 plateau (reconstruct from
   context/seeds/2026-07-14-w66-dcap-five-leaf-decider/): must still route to
   C0 (ell/tau = 2*tau), fail tallness, and keep D_leaf > 0.
2. The W55 A0 = 5 completion: must reproduce its exact order-one finance-row
   negativity and be rejected — its actor residual is SMALL (it is a T-esc
   shape, not DTR: check min_f ||p_f - x_u||_1 <= 3*delta there and assert
   it routes AWAY from DTR).

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational (fractions.Fraction)
   construction + verification; EVERY claim an exact assertion; exit nonzero
   on any mismatch; deterministic. Per-family verdict lines, the §4.2 print
   panel incl. D_EC and D_leaf separately, the rank-trend table, the two
   unit-test lines, one final summary line.
2. `certificates.json` — exact rational matrices + all panel quantities for
   any hit or best near-miss, plus the rank-trend table.
3. `REPORT.md` — verdict: REALIZED / BLOCKED (exact binding inequality per
   family, with margins) / PARTIAL; where tallness binds; the rank-trend
   finding; any by-catch entrant to ANY leaf class. State explicitly this is
   L3 evidence, never proof.

## Discipline

- context/FINDINGS.md dead routes absolute; clone-invariant quantities only
  (full fibers, row points, ell^1); signed picture; no probabilistic
  readings.
- Timebox: prefer honest BLOCKED-with-named-margins + an exact rank trend
  over a half-verified REALIZED.
- Final answer: one verdict line, the rank-trend one-liner, two unit-test
  lines, one sentence.
