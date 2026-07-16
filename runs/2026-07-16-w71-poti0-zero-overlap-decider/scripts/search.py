#!/usr/bin/env python3
"""W71 exact L3 POTI-0 growing-rank decider.

Constructive/numerical evidence only: this program is not a proof.  Every
number used for a claim is a fractions.Fraction.  Every printed equality or
inequality is asserted first, and any mismatch exits nonzero.

The main construction is a one-parameter exact factorization P=L B.  The
parameter beta is the mass with which the public root owns the probe-carrier
fibers.  It gives an exact repair tradeoff:

    max_i nu(P_i) = beta * (1 - 1/m + tau/20).

The delta-calibrated branch passes max negativity <= tau^2 but retains an
order-one R0 ownership defect.  The ownership-repaired branch sets beta=1/8,
repairs that one inequality, and pays order-one negativity.  Both branches
retain the local DTR geometry and formal POTI-0 support disjointness, but both
have H=0 because all factor rows lie in the visible-anchor simplex.  Neither
enters the registered hypothesis class.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Sequence

Z, O = F(0), F(1)
CM = F(1, 4)
B_SMALL = CM / 128
ONE_160 = F(1, 160)
ETA_TOTAL = F(1, 8)
R0, ALPHA, LAMBDA = F(1, 320), F(1, 2), F(1, 2)
DEFAULT_SCALE_POWER = 20


def dot(a: Sequence[F], b: Sequence[F]) -> F:
    assert len(a) == len(b)
    return sum((x * y for x, y in zip(a, b)), Z)


def add(a: Sequence[F], b: Sequence[F]) -> list[F]:
    assert len(a) == len(b)
    return [x + y for x, y in zip(a, b)]


def sub(a: Sequence[F], b: Sequence[F]) -> list[F]:
    assert len(a) == len(b)
    return [x - y for x, y in zip(a, b)]


def scale(t: F, a: Sequence[F]) -> list[F]:
    return [t * x for x in a]


def l1(a: Sequence[F], b: Sequence[F] | None = None) -> F:
    if b is None:
        return sum((abs(x) for x in a), Z)
    assert len(a) == len(b)
    return sum((abs(x - y) for x, y in zip(a, b)), Z)


def negative_mass(a: Sequence[F]) -> F:
    return sum((-x for x in a if x < Z), Z)


def sign(a: Sequence[F]) -> list[F]:
    return [F(1 if x > Z else -1 if x < Z else 0) for x in a]


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    assert a and b and len(a[0]) == len(b)
    return [[dot(row, col) for col in zip(*b)] for row in a]


def identity(n: int) -> list[list[F]]:
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def convex(weights: Sequence[F], points: Sequence[Sequence[F]]) -> list[F]:
    assert weights and len(weights) == len(points)
    assert sum(weights, Z) == O and all(w >= Z for w in weights)
    return [sum((weights[i] * points[i][j] for i in range(len(points))), Z)
            for j in range(len(points[0]))]


def sup_overflow(mu: Sequence[F], nu: Sequence[F]) -> F:
    assert len(mu) == len(nu)
    return sum((max(x - y, Z) for x, y in zip(mu, nu)), Z)


def delta_rt() -> F:
    return min(F(1, 2**16), (CM / 4) ** 2, (CM * B_SMALL / 120) ** 2)


def qstr(x: Any) -> Any:
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, dict):
        return {str(k): qstr(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [qstr(v) for v in x]
    return x


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def pf(value: bool) -> str:
    return "PASS" if value else "FAIL"


def factorization_checks(L: list[list[F]], B: list[list[F]], P: list[list[F]]) -> None:
    r = len(B)
    assert matmul(B, L) == identity(r)
    assert matmul(L, B) == P
    assert matmul(P, P) == P
    assert all(sum(row, Z) == O for row in P)


def beta_for(mode: str, m: int, tau: F) -> F:
    a = O - F(1, m) + tau / 20
    assert a > Z
    if mode == "seed":
        return Z
    if mode == "delta_calibrated":
        return tau * tau / a
    if mode == "ownership_repaired":
        return ETA_TOTAL
    raise AssertionError(mode)


def repair_family(m: int, mode: str, scale_power: int = DEFAULT_SCALE_POWER,
                  include_matrix: bool = False) -> dict[str, Any]:
    """Build and verify one member of the beta repair family."""
    assert m >= 4
    tau = F(1, (2**scale_power) * m)
    delta = tau * tau
    D0 = 2 + 4 * delta
    n = 2 * m + 1
    anchors = list(range(m))
    carriers = list(range(m, 2 * m))
    v = 2 * m
    fstar = v
    labels = ([f"a{j}" for j in range(m)] +
              [f"u{s}" for s in range(m)] + ["v=f*"])

    basis = identity(m)
    center = [F(1, m)] * m
    directions: list[list[F]] = []
    probe_factors: list[list[F]] = []
    for s in range(m):
        d = [Z] * m
        d[s] = -O
        d[(s + 1) % m] = O
        directions.append(d)
        probe_factors.append(add(center, scale(tau / 20, d)))
    assert len({tuple(x) for x in probe_factors}) == m
    assert all(all(x > Z for x in row) and sum(row, Z) == O
               for row in probe_factors)

    beta = beta_for(mode, m, tau)
    a_cost = O - F(1, m) + tau / 20
    L = basis + probe_factors + [center]
    B: list[list[F]] = []
    for s in range(m):
        row = [Z] * n
        for j in anchors:
            row[j] = (O if s == j else Z) - beta * probe_factors[s][j]
        row[m + s] = beta
        B.append(row)
    P = matmul(L, B)
    factorization_checks(L, B, P)
    assert len({tuple(P[j]) for j in anchors}) == m
    assert len({tuple(P[u]) for u in carriers}) == m
    assert len({tuple(row) for row in P}) == n

    row_nus = [negative_mass(row) for row in P]
    max_nu = max(row_nus)
    expected_nu = beta * a_cost
    assert all(row_nus[j] == expected_nu for j in anchors)
    assert all(row_nus[i] == Z for i in carriers + [v])
    assert max_nu == expected_nu
    if mode == "delta_calibrated":
        assert max_nu == delta
    if mode == "seed":
        assert max_nu == Z
    if mode == "ownership_repaired":
        assert max_nu > delta

    # The anchor factor rows are vertices and have explicit admissible
    # exposers h_s(l)=1-l_s.  Every factor row lies in their simplex, so the
    # full row polytope equals the visible-anchor hull and H is exactly zero.
    for s in range(m):
        hvals = [O - row[s] for row in L]
        assert hvals[s] == Z and all(Z <= h <= O for h in hvals)
        far_hvals = [hvals[i] for i in range(n) if l1(P[i], P[s]) >= 4 * tau]
        assert far_hvals and min(far_hvals) >= tau / 4
    p_v = P[v]
    assert p_v == convex(center, [P[j] for j in anchors])
    H = Z
    tall_margin = H - 16 * tau
    assert tall_margin == -16 * tau < Z
    depths = [Z] * n
    L_v = list(range(n))

    # Original selected set: anchor indices only.  Its row-point support is
    # disjoint from the D probe support even after root ownership is added.
    m_A = [Z] * n
    for j in anchors:
        m_A[j] = max(P[v][j], Z)
    assert len(set(m_A[j] for j in anchors)) == 1
    S = sum(m_A, Z)
    assert S == O - beta >= CM
    q_A = convex([m_A[j] / S for j in anchors], [P[j] for j in anchors])
    assert q_A == p_v
    Z_ray = Z  # true value because q_A=p_v, including the Lambda=0 ray.

    selected_far = [j for j in anchors if l1(P[j], p_v) >= 4 * tau]
    assert selected_far == anchors
    # At H=0 these are only formal co-top diagnostics.  Tallness fails first.
    theta = Z
    assert theta < tau / D0

    eta_weight = ETA_TOTAL / m
    eta = [Z] * n
    for u in carriers:
        eta[u] = eta_weight
    assert sum(eta, Z) == ETA_TOTAL > ONE_160
    pf_plus = [max(x, Z) for x in P[fstar]]
    ownership_excess = sup_overflow(eta, pf_plus)
    expected_excess = max(ETA_TOTAL - beta, Z)
    assert ownership_excess == expected_excess
    ownership_pass = ownership_excess == Z
    assert ownership_pass == (beta >= ETA_TOTAL)

    # The receiver foldback is benign: the eta-average of the probe rows is
    # exactly (1/8) times the public row.
    Pi = [sum((eta_weight * max(P[u][j], Z) for u in carriers), Z)
          for j in range(n)]
    assert Pi == scale(ETA_TOTAL, pf_plus)
    foldback_overflow = sup_overflow(Pi, pf_plus)
    assert foldback_overflow == Z

    carrier_panels: list[dict[str, Any]] = []
    incidence_tables: list[dict[str, Any]] = []
    U: set[int] = set()
    local_mass = Z
    for s, u in enumerate(carriers):
        qtilde_factor = add(probe_factors[s], scale(tau / 2, directions[s]))
        x_factor = sub(probe_factors[s], scale(2 * tau, directions[s]))
        assert all(x > Z for x in qtilde_factor + x_factor)
        assert sum(qtilde_factor, Z) == sum(x_factor, Z) == O
        qtilde = convex(qtilde_factor, [P[j] for j in anchors])
        x = convex(x_factor, [P[j] for j in anchors])
        D = sub(qtilde, P[u])
        ell = l1(D)
        assert tau / 2 <= ell <= 2 * tau
        assert sub(P[u], scale(4, D)) == x
        h_u = Z
        distances = [l1(row, x) for row in P]
        min_actual = min(distances)
        assert min_actual > 3 * delta
        nearest = [labels[i] for i, value in enumerate(distances) if value == min_actual]

        chi = [dot(sign(D), sub(row, P[u])) / ell for row in P]
        T = [R for R in range(n) if abs(chi[R]) > O]
        incidence = [R for R in T if P[u][R] > Z]
        tail = sum((max(P[u][R], Z) for R in T), Z)
        assert tail > tau / 8
        assert incidence
        U.update(incidence)
        local_mass += eta_weight

        # The flat diagnostic has phi=H=0, hence z=0 on every row.
        t_phi = Z
        surplus = max(t_phi - D0 * delta, Z)
        assert surplus == Z
        table = []
        for R in range(n):
            table.append({
                "R": labels[R],
                "rho(u)": Z,
                "(c_uR)_+": max(P[u][R], Z),
                "chi_u(p_R)": chi[R],
                "z(p_R)": Z,
                "1_Estar(R)": l1(P[R], P[fstar]) > F(1, 2),
                "1_Lv(R)": True,
            })
        incidence_tables.append({"carrier": labels[u], "rows": table})
        carrier_panels.append({
            "carrier": labels[u], "A_tilde": F(4), "ell": ell,
            "g_proxy=A_tilde*ell": 4 * ell, "q_tilde": qtilde, "x": x,
            "h_u": h_u, "3delta": 3 * delta,
            "min_actual_row_distance": min_actual,
            "actor_residual_margin": min_actual - 3 * delta,
            "nearest_actual_rows": nearest, "Tail_1": tail,
            "tail_threshold": tau / 8, "tail_margin": tail - tau / 8,
            "T_u": [labels[R] for R in T],
            "positive_tail_incidence": [labels[R] for R in incidence],
            "t_phi(u)": t_phi, "[t_phi(u)-D0*delta]_+": surplus,
        })
    assert local_mass == ETA_TOTAL > ONE_160
    assert U
    Pf_U = sum((pf_plus[R] for R in U), Z)
    assert Pf_U > tau / 2560

    E_star = [R for R in range(n) if l1(P[R], P[fstar]) > F(1, 2)]
    assert E_star == anchors
    Pv_E = sum((pf_plus[R] for R in E_star), Z)
    Pv_L = sum(pf_plus, Z)
    assert Pv_E == O - beta and Pv_L == O
    ell_T = delta + (4 * tau / 63) * (D0 + tau / 4)
    assert ell_T < 2 * tau / 15 < O
    shallow_margin = ell_T - Pv_L
    assert shallow_margin < Z

    # Canonical POTI quantities on the row-point quotient (all fibers are
    # singleton and distinct).  Selected and D supports are disjoint.
    rho_by_fiber = [min(m_A[R], eta[R]) for R in range(n)]
    rho_total = sum(rho_by_fiber, Z)
    assert rho_total == Z
    G_phi = sum((rho_by_fiber[u] * cp["[t_phi(u)-D0*delta]_+"]
                 for u, cp in zip(carriers, carrier_panels)), Z)
    assert G_phi == Z

    coherent = []
    for u, cp in zip(carriers, carrier_panels):
        coherent_mass = sum((max(P[u][R], Z) for R in range(n)
                             if R in [labels.index(x) for x in cp["T_u"]]
                             and Z >= LAMBDA), Z)
        # z=0<lambda, so the level-set sum is empty.
        assert coherent_mass == Z < ALPHA * cp["Tail_1"]
        coherent.append(False)
    r_alpha_lambda = sum((rho_by_fiber[u] for u, good in zip(carriers, coherent)
                          if good), Z)
    assert r_alpha_lambda == Z
    delta_coh = min(delta_rt(), (ALPHA * LAMBDA / 48) ** 2)
    tc_ceiling = delta <= delta_coh
    tc_trigger = tc_ceiling and r_alpha_lambda >= R0
    tc_rhs = R0 * ALPHA * LAMBDA * tau / (16 * S)
    if tc_trigger:
        assert Z_ray > tc_rhs
    assert not tc_trigger

    D_POTI = G_phi - S * Pv_E / 8 + CM * S * Pv_L / 16
    D_EC = Z_ray - Pv_E / 8 + CM * Pv_L / 16
    D_leaf = Z_ray - CM * tau / 64 + CM * Pv_L / 16
    assert D_EC == D_POTI / S
    assert D_leaf >= D_EC
    assert D_EC < Z < D_leaf
    assert D_POTI < Z
    poti_order_1 = D_EC >= D_POTI / S
    poti_order_2 = D_leaf >= D_EC
    assert poti_order_1 and poti_order_2

    pog_upper = S * (Pv_E / 8 - CM * Pv_L / 16)
    pog_window = Z < G_phi < pog_upper
    assert not pog_window
    delta_pog = pog_upper - G_phi
    kappa_poti = None

    radial_bins = {
        "fstar_far__v_far": [], "fstar_far__v_near": [],
        "fstar_near__v_far": [], "fstar_near__v_near": [],
    }
    for R in range(n):
        ff = l1(P[R], P[fstar]) > F(1, 2)
        vf = l1(P[R], p_v) >= 4 * tau
        key = ("fstar_far" if ff else "fstar_near") + "__" + ("v_far" if vf else "v_near")
        radial_bins[key].append(labels[R])
    assert radial_bins["fstar_far__v_far"] == [labels[j] for j in anchors]
    assert radial_bins["fstar_far__v_near"] == []
    assert radial_bins["fstar_near__v_far"] == []
    assert radial_bins["fstar_near__v_near"] == [labels[j] for j in carriers + [v]]
    shallow_deep = {"shallow_d<=tau/4": labels[:], "deep_d>tau/4": []}

    legal_negativity = max_nu <= delta
    gate = {
        "P=LB_BL=I_P2=P": True,
        "prescribed_delta=tau^2": delta == tau * tau,
        "actual_delta(P)=tau^2": max_nu == delta,
        "all_row_negativity<=tau^2": legal_negativity,
        "genuine_rank=m": True,
        "rank_not_clones_or_transients": True,
        "full_I_base_all_center_package": False,
        "H>16tau": H > 16 * tau,
        "legal_far_selected_mass": selected_far == anchors and S >= CM,
        "nonempty_ultra_omega": False,
        "theta<tau/D0": theta < tau / D0,
        "fixed_D_certificate": False,
        "M_X<=1/8": True,
        "M_I<1/16": True,
        "M_D>1/16": ETA_TOTAL > F(1, 16),
        "formal_R0_carrier_ownership_scalar": ownership_pass,
        "R0_all_outputs": False,
        "B1-B5_all_outputs": False,
        "R1_output": False,
        "strict_HES_failure_guard": True,
        "DTR_local_mass>1/160": local_mass > ONE_160,
        "all_Tail_1>tau/8": all(cp["Tail_1"] > tau / 8 for cp in carrier_panels),
        "union_floor": Pf_U > tau / 2560,
        "G_phi=0": G_phi == Z,
        "D_EC<0": D_EC < Z,
    }
    full_entry = all(gate[k] for k in [
        "P=LB_BL=I_P2=P", "prescribed_delta=tau^2",
        "actual_delta(P)=tau^2", "all_row_negativity<=tau^2",
        "full_I_base_all_center_package", "H>16tau", "legal_far_selected_mass",
        "nonempty_ultra_omega", "theta<tau/D0", "fixed_D_certificate",
        "R0_all_outputs", "B1-B5_all_outputs", "R1_output",
        "strict_HES_failure_guard", "DTR_local_mass>1/160",
        "all_Tail_1>tau/8", "union_floor"])
    assert not full_entry

    trend = {
        "mode": mode, "m": m, "rank": m, "ambient_n": n,
        "scale_power": scale_power, "tau": tau, "tau^2": delta,
        "beta": beta, "ownership_cost_factor_a": a_cost,
        "max_row_negativity=beta*a": max_nu,
        "negativity_margin=tau^2-max_nu": delta - max_nu,
        "R0_ownership_excess=max(1/8-beta,0)": ownership_excess,
        "H/tau": H / tau, "H-16tau": tall_margin,
        "P_v_plus(L_v)": Pv_L, "ell_T-P_v_plus(L_v)": shallow_margin,
        "rho(1)": rho_total, "G_phi": G_phi, "D_POTI": D_POTI,
        "D_EC": D_EC, "D_leaf": D_leaf,
    }

    result: dict[str, Any] = {
        "id": f"beta_{mode}_m{m}_p{scale_power}",
        "verdict": "BLOCKED_NON_ENTRANT",
        "warning": "L3 exact constructive/numerical evidence only; never a proof",
        "parameters": {"m": m, "tau": tau, "delta=tau^2": delta,
                       "actual_delta(P)": max_nu, "D0": D0, "beta": beta,
                       "a=1-1/m+tau/20": a_cost, "c_m": CM,
                       "r0": R0, "alpha": ALPHA, "lambda": LAMBDA,
                       "delta_rt": delta_rt()},
        "dimensions": {"ambient_n": n, "certified_rank": m,
                       "rank_certificate": "B*L=I_m",
                       "genuine_distinct_anchor_rows": m,
                       "rank_growth_not_from_clones_or_transients": True},
        "labels": labels, "row_negative_masses": row_nus,
        "max_row_negativity": max_nu,
        "height_panel": {
            "visible_anchor_exposers": "h_s(l)=1-l_s",
            "all_factor_rows_in_anchor_simplex": True,
            "H": H, "H/tau": H / tau, "H-16tau": tall_margin,
            "binding_inequality": "K(P)=conv{p_a}; hence H=0<16*tau",
            "legal_ultra_omega_package_reached": False,
            "certified_ultra_omega_population": Z,
        },
        "selected_panel": {"A": [labels[j] for j in anchors], "S": S,
                           "m_A": m_A, "q_A": q_A, "Z_v(q_A)": Z_ray,
                           "theta": theta, "theta_threshold": tau / D0},
        "root_and_local_DTR": {
            "eta_D_star": eta, "eta_D_star(B)": ETA_TOTAL,
            "P_fstar_plus_on_each_carrier": beta / m,
            "R0_ownership_excess": ownership_excess,
            "R0_ownership_pass": ownership_pass,
            "receiver_foldback_overflow": foldback_overflow,
            "carriers": carrier_panels, "U_B": [labels[R] for R in sorted(U)],
            "P_fstar_plus(U_B)": Pf_U, "union_threshold": tau / 2560,
        },
        "POTI_panel": {
            "rho_by_fiber": rho_by_fiber, "rho(1)": rho_total,
            "vanishing_mechanism": "(i) support disjointness",
            "per_carrier": [{"carrier": cp["carrier"],
                              "t_phi(u)": cp["t_phi(u)"],
                              "[t_phi(u)-D0*delta]_+": cp["[t_phi(u)-D0*delta]_+"]}
                             for cp in carrier_panels],
            "G_phi": G_phi,
            "TC": {"predeclared": {"r0": R0, "alpha": ALPHA, "lambda": LAMBDA},
                   "r_alpha_lambda": r_alpha_lambda, "delta_coh": delta_coh,
                   "ceiling_pass": tc_ceiling, "antecedent_triggered": tc_trigger,
                   "TC_rhs": tc_rhs},
            "P_v_plus(E_star)": Pv_E, "P_v_plus(L_v)": Pv_L,
            "D_POTI": D_POTI, "D_EC": D_EC, "D_leaf": D_leaf,
            "ordering_D_EC>=D_POTI/S": poti_order_1,
            "ordering_D_leaf>=D_EC": poti_order_2,
            "POG_window": pog_window, "Delta_POG": delta_pog,
            "kappa_POTI": kappa_poti,
        },
        "incidence_table": incidence_tables,
        "radial_bins_relative_to_fstar_and_v": radial_bins,
        "shallow_deep_split": shallow_deep,
        "B5": {"label": "NOT_REACHED",
               "warning": "B5 population is not eta_D*; no identification is made"},
        "B4": {"ell_T": ell_T, "P_v_plus(L_v)": Pv_L,
               "shallow_margin=ell_T-PvL": shallow_margin,
               "P_v_plus(E_star)": Pv_E},
        "gate": gate, "full_DTR_entry": full_entry,
        "formal_POTI0_refuter": full_entry and G_phi == Z and D_EC < Z,
        "formal_W65_leaf_refuter": full_entry and G_phi == Z and D_leaf < Z,
        "trend": trend,
    }
    if include_matrix:
        result["L"] = L
        result["B"] = B
        result["P"] = P
    return result


def w66_plateau_unit() -> dict[str, Any]:
    """Exact W66/W63 k=2048 regression."""
    k = 2048
    tau = F(1, k)
    delta = tau * tau
    t0 = tau / 8
    e = 2 * tau
    L = [
        [O, Z, Z],
        [O + delta * (O - t0), delta * t0, -delta],
        [Z, O, Z], [Z, Z, O], [Z, delta, O - delta],
        [Z, -delta, O + delta],
        [O - e, -e * delta, e * (O + delta)],
    ]
    B = [[O, Z, Z, Z, Z, Z, Z],
         [Z, Z, O, Z, Z, Z, Z],
         [Z, Z, Z, F(1, 2), F(1, 4), F(1, 4), Z]]
    P = matmul(L, B)
    factorization_checks(L, B, P)
    assert all(negative_mass(row) <= delta for row in P)
    u, zrow, orow, arow, xrow, yrow, frow = range(7)
    alpha = (O + delta) / (O + 2 * delta)
    closest = convex([alpha, O - alpha], [P[zrow], P[yrow]])
    H = l1(P[u], closest)
    r = (O - 2 * delta * t0) / (O + 2 * delta)
    dual = [O, Z, -O, r, r, r, Z]
    hstar = t0 - delta * (O - t0)
    phi = [dot(dual, row) - dot(dual, P[zrow]) for row in P]
    assert phi[u] == H
    kT = sub(P[frow], P[u])
    kO = scale(e * hstar, sub(P[orow], P[u]))
    A = e * (O + delta) / delta
    ell = l1(P[zrow], P[u])
    g = l1(kT, kO)
    assert add(kT, scale(A, sub(P[zrow], P[u]))) == kO
    assert g == A * ell and ell / tau == 2 * tau
    assert ell < tau / 2 and H < 16 * tau
    D_leaf = -CM * tau / 64 + CM / 16
    assert D_leaf > Z
    return {"id": "w66_w63_plateau_k2048", "L": L, "B": B, "P": P,
            "tau": tau, "delta": delta, "g": g, "A": A, "ell": ell,
            "ell/tau": ell / tau, "route": "C0", "H": H,
            "H-16tau": H - 16 * tau, "D_leaf": D_leaf}


def w55_unit() -> dict[str, Any]:
    """Exact W55 A0=5 finance and actor-residual regression."""
    tau, target_delta, A = F(1, 256), F(1, 65536), F(5)
    a = tau / (O + tau)
    L = [[O, Z, Z],
         [O + A * a - a * target_delta, -A * a, a * target_delta],
         [O + A - target_delta, -A, target_delta],
         [Z, O, Z], [Z, Z, O]]
    B = [[O - tau, tau + target_delta, -target_delta, Z, Z],
         [Z, Z, Z, O, Z], [Z, Z, Z, Z, O]]
    P = matmul(L, B)
    factorization_checks(L, B, P)
    nus = [negative_mass(row) for row in P]
    finance = A + (O + A - target_delta) * target_delta
    assert max(nus) == nus[2] == finance == F(21475229695, 4294967296)
    assert finance > target_delta
    v, w, frow, zrow, orow = range(5)
    dz, df, do = sub(P[zrow], P[v]), sub(P[frow], P[v]), sub(P[orow], P[v])
    assert add(df, scale(A, dz)) == scale(target_delta, do)
    ell = l1(dz)
    qtilde = add(P[v], scale(2 * tau / ell, dz))
    Atilde = A * ell / (2 * tau)
    x = sub(P[v], scale(Atilde, sub(qtilde, P[v])))
    actor_residual = l1(P[frow], x)
    min_actual = min(l1(row, x) for row in P)
    assert min_actual <= actor_residual <= 3 * target_delta
    chi = [dot(sign(sub(qtilde, P[v])), sub(row, P[v])) / l1(sub(qtilde, P[v]))
           for row in P]
    tail = sum((max(P[v][j], Z) for j in range(len(P)) if abs(chi[j]) > O), Z)
    assert tail == F(257, 65536) > tau / 8
    return {"id": "w55_A0_5", "L": L, "B": B, "P": P,
            "tau": tau, "target_delta=tau^2": target_delta,
            "row_negative_masses": nus, "finance_nu": finance,
            "finance_excess": finance - target_delta, "A0": A,
            "actor_residual": actor_residual,
            "min_actual_row_distance": min_actual, "3delta": 3 * target_delta,
            "Tail_1": tail, "routes_to_DTR": False,
            "classification": "T-esc shape; rejected by order-one negativity"}


def print_candidate(c: dict[str, Any]) -> None:
    p, tr = c["parameters"], c["trend"]
    pot, root = c["POTI_panel"], c["root_and_local_DTR"]
    print(f"FAMILY {c['id']}: BLOCKED_NON_ENTRANT rank={tr['rank']} "
          f"tau={fstr(p['tau'])} beta={fstr(p['beta'])} "
          f"max-nu={fstr(c['max_row_negativity'])}; full gate=FAIL.")
    print("  FACTOR P=LB, BL=I, P^2=P: PASS; actual delta(P)=tau^2: " +
          pf(c["gate"]["actual_delta(P)=tau^2"]) +
          "; all-row negativity<=tau^2: " + pf(c["gate"]["all_row_negativity<=tau^2"]) + ".")
    print("  ROOT ownership excess=" + fstr(root["R0_ownership_excess"]) +
          " (scalar pass=" + pf(root["R0_ownership_pass"]) +
          "); receiver foldback overflow=" + fstr(root["receiver_foldback_overflow"]) + ".")
    print("  HEIGHT H/tau=" + fstr(c["height_panel"]["H/tau"]) +
          ", H-16tau=" + fstr(c["height_panel"]["H-16tau"]) +
          "; ultra omega=EMPTY/NOT-REACHED; B4 ell_T-PvL=" +
          fstr(c["B4"]["shallow_margin=ell_T-PvL"]) + ".")
    for cp in root["carriers"]:
        print("  CARRIER " + cp["carrier"] + ": h=" + fstr(cp["h_u"]) +
              "; min-row=" + fstr(cp["min_actual_row_distance"]) +
              ">3delta=" + fstr(cp["3delta"]) + "; Tail_1=" +
              fstr(cp["Tail_1"]) + ">tau/8=" + fstr(cp["tail_threshold"]) +
              "; t_phi=" + fstr(cp["t_phi(u)"]) + "; surplus=" +
              fstr(cp["[t_phi(u)-D0*delta]_+"]) + ".")
    print("  POTI rho(1)=" + fstr(pot["rho(1)"]) + "; mechanism=" +
          pot["vanishing_mechanism"] + "; G_phi=" + fstr(pot["G_phi"]) +
          "; r_alpha,lambda=" + fstr(pot["TC"]["r_alpha_lambda"]) + ".")
    print("  DIAGNOSTICS D_POTI=" + fstr(pot["D_POTI"]) +
          "; D_EC=" + fstr(pot["D_EC"]) + "; D_leaf=" + fstr(pot["D_leaf"]) +
          "; orderings D_EC>=D_POTI/S and D_leaf>=D_EC: PASS/PASS.")
    print("  TC fixed (r0,alpha,lambda)=(" + fstr(R0) + "," + fstr(ALPHA) + "," +
          fstr(LAMBDA) + "): ceiling=" + pf(pot["TC"]["ceiling_pass"]) +
          ", antecedent=" + pf(pot["TC"]["antecedent_triggered"]) + ".")
    print("  GLOBAL GATE full-I-base=FAIL; fixed-D-certificate=FAIL; "
          "R0-all=FAIL; B1-B5-all=FAIL; R1=FAIL; POTI+=NOT-ENTERED.")
    print("  RADIAL " + json.dumps(qstr(c["radial_bins_relative_to_fstar_and_v"]),
                                         separators=(",", ":")))
    print("  SHALLOW/DEEP " + json.dumps(qstr(c["shallow_deep_split"]),
                                               separators=(",", ":")))
    for table in c["incidence_table"]:
        print("  INCIDENCE " + table["carrier"] + " " +
              json.dumps(qstr(table["rows"]), separators=(",", ":")))
    print("  B5 label=" + c["B5"]["label"] + ". WARNING: " + c["B5"]["warning"] + ".")


def build() -> dict[str, Any]:
    ranks = [4, 8, 16, 32]
    calibrated = [repair_family(m, "delta_calibrated",
                                include_matrix=(m == 32)) for m in ranks]
    ownership = [repair_family(m, "ownership_repaired",
                               include_matrix=(m == 32)) for m in ranks]
    seed8 = repair_family(8, "seed", include_matrix=True)

    # Mandatory W69 rank-8 calibration.
    assert seed8["POTI_panel"]["D_EC"] == -F(7, 64)
    assert seed8["root_and_local_DTR"]["R0_ownership_excess"] == F(1, 8)
    assert seed8["height_panel"]["H/tau"] == Z
    assert seed8["height_panel"]["certified_ultra_omega_population"] == Z
    assert seed8["POTI_panel"]["rho(1)"] == Z
    assert seed8["POTI_panel"]["G_phi"] == Z
    assert seed8["POTI_panel"]["D_POTI"] == -F(7, 64)

    # Exact tau trend at fixed genuine rank 8.
    tau_sweep_members = [repair_family(8, "delta_calibrated", power)
                         for power in [16, 18, 20, 22]]
    tau_trend = [c["trend"] for c in tau_sweep_members]
    assert all(t["max_row_negativity=beta*a"] == t["tau^2"] for t in tau_trend)
    assert all(t["H/tau"] == Z and t["P_v_plus(L_v)"] == O for t in tau_trend)

    tradeoff = []
    for c_cal, c_own in zip(calibrated, ownership):
        p = c_cal["parameters"]
        a = p["a=1-1/m+tau/20"]
        beta_max = p["delta=tau^2"] / a
        beta_min = ETA_TOTAL
        gap = beta_min - beta_max
        assert gap > Z
        assert c_cal["parameters"]["beta"] == beta_max
        assert c_own["parameters"]["beta"] == beta_min
        assert c_own["max_row_negativity"] == beta_min * a > p["delta=tau^2"]
        tradeoff.append({
            "m": p["m"], "tau": p["tau"], "a": a,
            "negativity_requires_beta<=tau^2/a": beta_max,
            "R0_ownership_requires_beta>=1/8": beta_min,
            "incompatibility_gap": gap,
            "nu_at_ownership_repair": beta_min * a,
            "excess_nu_over_tau^2": beta_min * a - p["delta=tau^2"],
        })

    plateau, w55 = w66_plateau_unit(), w55_unit()
    assert all(not c["full_DTR_entry"] for c in calibrated + ownership)
    assert all(c["POTI_panel"]["rho(1)"] == Z for c in calibrated + ownership)
    assert all(c["POTI_panel"]["G_phi"] == Z for c in calibrated + ownership)
    assert not any(c["POTI_panel"]["POG_window"] for c in calibrated + ownership)
    return {
        "schema": "w71-poti0-exact-l3-v1",
        "arithmetic": "fractions.Fraction; JSON scalar values are rational strings",
        "warning": "L3 constructive/numerical evidence only; never a proof",
        "verdict": "BLOCKED",
        "predeclared_TC": {"r0": R0, "alpha": ALPHA, "lambda": LAMBDA},
        "family_law": {
            "beta_axis": "nu_max=beta*(1-1/m+tau/20)",
            "binding_inequalities": ["beta>=1/8 for this R0 ownership repair",
                                     "beta<=tau^2/(1-1/m+tau/20) for negativity"],
            "height_wall": "all factor rows in visible-anchor simplex => H=0",
        },
        "families": {"delta_calibrated": calibrated,
                     "ownership_repaired": ownership},
        "best_near_misses_with_exact_matrices": {
            "negativity_legal_rank32": calibrated[-1],
            "ownership_repaired_rank32": ownership[-1],
        },
        "rank_trends": {"delta_calibrated": [c["trend"] for c in calibrated],
                        "ownership_repaired": [c["trend"] for c in ownership]},
        "tau_trend_fixed_rank8": tau_trend,
        "ownership_negativity_tradeoff": tradeoff,
        "unit_tests": {"W66_W63_plateau": plateau, "W55_A0_5": w55,
                       "W69_rank8_with_POTI": seed8},
        "full_DTR_entries": 0, "POTI0_refuters": 0,
        "W65_leaf_refuters": 0, "POTI_plus_window_entries": 0,
        "full_creative_leaf_bycatch": [],
        "reachable_only_outside_gate": "POTI-0 mechanism (i), rho(1)=0 support disjointness",
    }


def main() -> None:
    data = build()
    Path("certificates.json").write_text(json.dumps(qstr(data), indent=2) + "\n")
    for c in data["families"]["delta_calibrated"]:
        print_candidate(c)
    for c in data["families"]["ownership_repaired"]:
        print_candidate(c)
    for mode, rows in data["rank_trends"].items():
        for row in rows:
            print("RANK-TREND " + mode + " m=" + str(row["m"]) +
                  " tau=" + fstr(row["tau"]) + " beta=" + fstr(row["beta"]) +
                  " nu=" + fstr(row["max_row_negativity=beta*a"]) +
                  " tau^2-nu=" + fstr(row["negativity_margin=tau^2-max_nu"]) +
                  " ownership-excess=" +
                  fstr(row["R0_ownership_excess=max(1/8-beta,0)"]) +
                  " H/tau=" + fstr(row["H/tau"]) + " PvL=" +
                  fstr(row["P_v_plus(L_v)"]) + " D_leaf=" + fstr(row["D_leaf"]) + ".")
    for row in data["tau_trend_fixed_rank8"]:
        print("TAU-TREND rank=8 power=" + str(row["scale_power"]) +
              " tau=" + fstr(row["tau"]) + " beta=" + fstr(row["beta"]) +
              " nu=" + fstr(row["max_row_negativity=beta*a"]) +
              " ownership-excess=" +
              fstr(row["R0_ownership_excess=max(1/8-beta,0)"]) +
              " H/tau=" + fstr(row["H/tau"]) + " PvL=" +
              fstr(row["P_v_plus(L_v)"]) + ".")
    for row in data["ownership_negativity_tradeoff"]:
        print("TRADEOFF m=" + str(row["m"]) + " tau=" + fstr(row["tau"]) +
              " beta_max_neg=" + fstr(row["negativity_requires_beta<=tau^2/a"]) +
              " beta_min_owner=" + fstr(row["R0_ownership_requires_beta>=1/8"]) +
              " gap=" + fstr(row["incompatibility_gap"]) +
              " nu_owner-tau^2=" + fstr(row["excess_nu_over_tau^2"]) + ".")
    print("RANK TREND: beta=tau^2/a gives exact delta(P)=tau^2 but ownership excess "
          "1/8-beta and H/tau=0; beta=1/8 repairs ownership but gives "
          "nu=(1/8)a>tau^2 at ranks 4,8,16,32.")
    print("TAU TREND (rank 8): powers 16,18,20,22 all have delta(P)=tau^2, "
          "H/tau=0, P_v+(L_v)=1, rho(1)=G_phi=0, and ownership excess=1/8-beta.")
    print("BINDING: in this exact repair family beta>=1/8 (R0 ownership) conflicts "
          "with beta<=tau^2/(1-1/m+tau/20) (row negativity), with a positive exact "
          "gap in every rank and tau row.")
    w66 = data["unit_tests"]["W66_W63_plateau"]
    print("UNIT W66/W63 plateau: PASS — ell/tau=" + fstr(w66["ell/tau"]) +
          "=2*tau; route=C0; tallness=FAIL; D_leaf=" + fstr(w66["D_leaf"]) + ">0.")
    w55 = data["unit_tests"]["W55_A0_5"]
    print("UNIT W55 A0=5: PASS — finance nu=" + fstr(w55["finance_nu"]) +
          ">tau^2=" + fstr(w55["target_delta=tau^2"]) +
          "; min-row<=3delta; T-esc, not DTR.")
    w69 = data["unit_tests"]["W69_rank8_with_POTI"]
    p = w69["POTI_panel"]
    print("UNIT W69 rank-8: PASS — local D_EC=" + fstr(p["D_EC"]) +
          ", R0 excess=1/8, H/tau=0, ultra omega empty; rho(1)=" +
          fstr(p["rho(1)"]) + ", G_phi=" + fstr(p["G_phi"]) +
          ", D_POTI=" + fstr(p["D_POTI"]) + ".")
    print("SUMMARY: BLOCKED — 0 full entries, 0 POTI-0 refuters, 0 POTI+ entrants, "
          "0 full leaf by-catch; exact L3 evidence only, never a proof.")


if __name__ == "__main__":
    main()
