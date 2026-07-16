# W71 L3 decider — the POTI-0 zero-overlap growing-rank refuter (exact arithmetic)

You are a fresh, independent worker. Your workspace is this directory
(registry snapshot `argument/` + `definitions/` + `context/` + seeds).
Everything you produce stays inside it. This is an L3 (constructive/numerical
evidence) job: **nothing you produce is a proof**, and your report must say so.

## Target

`context/DTR-ATTACK-W69.md` §4.2 **POTI-0 target** (and §1.5): the registered
conjecture `conj-dtr-zero-oriented-surplus-exclusion` — can it be refuted, or
its hypothesis class even ENTERED, by an exact growing-rank family? Its proof
side is now the sole zero-surplus obstacle between the verified POTI-R
conversion (`lem-dtr-oriented-tail-ray-conversion`, S*Z_v(q_A) >= G_phi, L5)
and exact (EC) via `lem-dtr-poti-assembly`. Read `context/DTR-ATTACK-W69.md`
IN FULL FIRST (it pins the datum from context/AESC-ATTACK-W67.md §1.6, which
adopts DCAP-ATTACK-W65.md §1.1 and DECOMPOSITION-W63-I.md §§0-1.1 — read
those too). The verified interface is in the six lem-dtr-*/conj-dtr-* shards
in argument/ — consume their statements, never re-derive them.

## The gate (exact rationals — unchanged W67/W69 gate)

Every candidate is an exact rational factorization P_k = L_k B_k, B_k L_k = I
(certifying P_k^2 = P_k), tau_k -> 0, delta_k = tau_k^2, every row negativity
<= delta_k, the FULL I-base/all-center package, H_k > 16*tau_k, a LEGAL far
selected mass, NONEMPTY ultra omega, theta_k < tau_k/D_{0,k}, the fixed
D-certificate (M_X <= 1/8, M_I < 1/16, M_D > 1/16), all R0/B1-B5/R1 outputs,
and the true ray value. Cloning and transient rank inflation DO NOT count as
rank growth.

**DTR entry (after the strict HES failure guard):**
  eta_D*{u : h_u <= 3*delta, min_f ||p_f - x_u||_1 > 3*delta} > 1/160
with h_u = dist_1(x_u, K(P)), x_u = p_u - A~_u(q~_u - p_u); carrierwise
Tail_1(u) > tau/8 and the union floor P_f*^+(U_B) > tau/2560.

**The NEW panel — every run prints, exactly (DTR-ATTACK-W69.md (4.1)-(4.5)):**
  rho(1)  (the canonical overlap mass, rho(Q) = min{m_A(Q), eta_D*(B cap Q)}),
  per-carrier t_phi(u), [t_phi(u) - D_0*delta]_+, the aggregate G_phi,
  r_{alpha,lambda} for the fixed rational (r_0, alpha, lambda) you pre-declare,
  D_POTI := G_phi - (S/8)*P_v^+(E_*) + (c_m*S/16)*P_v^+(L_v),
  D_EC   := Z_v(q_A) - (1/8)*P_v^+(E_*) + (c_m/16)*P_v^+(L_v),
  D_leaf := Z_v(q_A) - c_m*tau/64 + (c_m/16)*P_v^+(L_v),
the full incidence table (u,R) -> (rho(u), (c_{u,R})_+, chi_u(p_R), z(p_R),
1_{E_*}(R), 1_{L_v}(R)), its four radial bins relative to p_f* AND p_v, the
shallow/deep split, and the realized B5 label WITH an explicit warning that
the B5 population is not eta_D*. Assert the proved orderings
D_EC >= D_POTI/S and D_leaf >= D_EC on every certified instance (they are
now L5 theorems — a violation means your instance fails a hypothesis;
diagnose which). The three diagnostics are NOT interchangeable; report all.

## The POTI-0 refuter (the decisive shape)

Require the full gate + DTR entry + exact G_phi = 0 + D_EC < 0. The sharpest
shape has rho(1) = 0: root-owned (eta_D*|_B) and top-selected (m_A) supports
mutually singular on the row-point quotient at growing GENUINE rank. A
W65-leaf refuter additionally needs D_leaf < 0. Print which of the two
G_phi-vanishing mechanisms is realized: (i) rho(1) = 0 (support
disjointness), or (ii) rho(1) > 0 but every overlapped carrier moment
t_phi(u) <= D_0*delta (orientation starvation) — DTR-ATTACK-W69.md §1.5(e)'s
split. These are DIFFERENT refuter shapes; certify which one you can reach.

**POTI+ by-catch:** any certified instance in the (POG.0) window
(0 < G_phi < (S/8)*P_v^+(E_*) - (c_m*S/16)*P_v^+(L_v)) with D_EC < 0 refutes
`conj-dtr-positive-oriented-surplus-gap-exclusion`; print Delta_POG and
kappa_POTI := G_phi / (S*(P_v^+(E_*)/8 - c_m*P_v^+(L_v)/16)) for every
entrant to the window, refuter or not.

**TC calibration:** pre-declare rational (r_0, alpha, lambda); wherever
r_{alpha,lambda} >= r_0 and delta <= min{delta_rt, (alpha*lambda/48)^2},
check the proved (TC) bound Z_v(q_A) > r_0*alpha*lambda*tau/(16*S) as an
assertion (it is an L5 theorem — a violation means a hypothesis fails;
diagnose which).

## What the W69 seed already established (do not re-discover it)

`context/seeds/2026-07-14-w69-dtr-growing-rank-decider/` (REPORT.md +
certificates.json + scripts/search.py): growing rank (certified 4..32)
realizes the LOCAL DTR geometry at exactly ZERO finance negativity (local
D_EC = -7/64 < 0) but EVERY global gate fails by exact rank-uniform margins
(R0 ownership excess exactly 1/8; H/tau = 0; shallow mass 1; empty ultra
omega) and D_leaf > 0 throughout; no margin improves with rank. YOUR job
starts there: attack the global gates. For each failing gate, either (a)
repair it within an exact family while preserving the local DTR geometry and
print the new panel (does rho(1) = 0 survive the repair? tallness has bound
SIX consecutive exact batches — the H/tau = 0 wall is the first target), or
(b) certify an exact TREND (gate margin vs rank and vs tau) showing the
repair is blocked, with the binding inequality named. An exact trend on
non-entrant families is valuable evidence; a half-verified REALIZED is not.

## Unit tests (all three must pass in search.py)

1. The W66/W63 plateau (from context/seeds/2026-07-14-w66-dcap-five-leaf-
   decider/): must still route to C0 (ell/tau = 2*tau), fail tallness, and
   keep D_leaf > 0.
2. The W55 A0 = 5 completion: must reproduce its exact order-one finance-row
   negativity and be rejected — its actor residual is SMALL (T-esc shape,
   not DTR: assert min_f ||p_f - x_u||_1 <= 3*delta there).
3. The W69 rank-8 family (reconstruct from the seed's certificates.json):
   must reproduce its exact panel — local D_EC = -7/64, R0 ownership excess
   1/8, H/tau = 0, empty ultra omega — and additionally print its NEW POTI
   panel (rho(1), G_phi, D_POTI) as the calibration baseline.

## Deliverables (all inside this directory)

1. `search.py` — self-contained exact-rational (fractions.Fraction)
   construction + verification; EVERY claim an exact assertion; exit nonzero
   on any mismatch; deterministic. Per-family verdict lines, the full panel
   incl. rho(1)/G_phi/D_POTI/D_EC/D_leaf separately, the gate-repair trend
   tables, the three unit-test lines, one final summary line.
2. `certificates.json` — exact rational matrices + all panel quantities for
   any hit or best near-miss, plus every trend table.
3. `REPORT.md` — verdict: REALIZED / BLOCKED (exact binding inequality per
   family, with margins) / PARTIAL; which G_phi-vanishing mechanism (support
   disjointness vs orientation starvation) is reachable; where tallness
   binds; any POTI+ window entrant; any by-catch entrant to ANY leaf class.
   State explicitly this is L3 evidence, never proof.

## Discipline

- context/FINDINGS.md dead routes absolute; clone-invariant quantities only
  (full fibers, row points, ell^1); signed picture; no probabilistic
  readings.
- The proved orderings and (TC) are assertions, not findings — violating
  them flags YOUR instance, not the theorems.
- Timebox: prefer honest BLOCKED-with-named-margins + exact trends over a
  half-verified REALIZED.
- Final answer: one verdict line, the mechanism one-liner, the trend
  one-liner, three unit-test lines, one sentence.
