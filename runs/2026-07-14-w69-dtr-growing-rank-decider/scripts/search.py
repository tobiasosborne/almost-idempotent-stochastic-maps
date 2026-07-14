#!/usr/bin/env python3
"""W69 exact L3 decider for the DTR growing-rank target.

This program supplies constructive/numerical evidence only, never a proof.
Every scalar is a fractions.Fraction, every matrix identity and every printed
claim is asserted exactly, and a mismatch raises AssertionError (nonzero exit).

The growing-rank family realizes the local convexification/tail geometry of
DTR with genuine recurrent rank growth.  It is deliberately retained as a
near-miss: the probe carrier population is not root-owned, the public center
is not a hidden vertex, tallness and the B4 shallow ledger fail, and D_leaf is
positive.  Hence it does not enter (1.22) and is not a refuter.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Sequence

Z, O = F(0), F(1)
CM = F(1, 4)
B_SMALL = CM / 128
KB = CM * B_SMALL / 64
ONE_160 = F(1, 160)
RANK_SCALE = 2**20


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


def neg(a: Sequence[F]) -> F:
    return sum((-x for x in a if x < Z), Z)


def positive(a: Sequence[F]) -> list[F]:
    return [max(x, Z) for x in a]


def sign(a: Sequence[F]) -> list[F]:
    return [F(1 if x > Z else -1 if x < Z else 0) for x in a]


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    assert a and b and len(a[0]) == len(b)
    bt = list(zip(*b))
    return [[dot(row, col) for col in bt] for row in a]


def identity(n: int) -> list[list[F]]:
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def convex(weights: Sequence[F], points: Sequence[Sequence[F]]) -> list[F]:
    assert weights and len(weights) == len(points) and sum(weights, Z) == O
    assert all(w >= Z for w in weights)
    return [sum((weights[i] * points[i][j] for i in range(len(points))), Z)
            for j in range(len(points[0]))]


def sup_overflow(mu: Sequence[F], nu: Sequence[F]) -> F:
    assert len(mu) == len(nu)
    return sum((max(x - y, Z) for x, y in zip(mu, nu)), Z)


def assert_factorization(L: Sequence[Sequence[F]], B: Sequence[Sequence[F]],
                         P: Sequence[Sequence[F]], delta: F) -> None:
    rank = len(B)
    assert matmul(B, L) == identity(rank)
    assert matmul(L, B) == [list(row) for row in P]
    assert matmul(P, P) == [list(row) for row in P]
    assert all(sum(row, Z) == O for row in P)
    assert all(neg(row) <= delta for row in P)


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


def pf(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


def delta_rt() -> F:
    return min(F(1, 2**16), (CM / 4) ** 2, (CM * B_SMALL / 120) ** 2)


def rotating_retraction(m: int, include_matrix: bool = False) -> dict[str, Any]:
    """Exact rank-m local-DTR spine, with m genuine absorbing row points.

    B selects the m absorbing anchor rows, so BL=I_m.  The other rows are
    full-support carrier probes and one public center.  Rank growth is caused
    by the distinct recurrent anchors, never by the transient probes.
    """
    assert m >= 4
    tau = F(1, RANK_SCALE * m)
    delta = tau * tau
    D0 = 2 + 4 * delta
    e_delta = 2 * delta * (O + delta)
    n = 2 * m + 1
    anchors = list(range(m))
    carriers = list(range(m, 2 * m))
    v = 2 * m
    labels = ([f"a{j}" for j in range(m)] +
              [f"u{s}" for s in range(m)] + ["v=f*"])

    basis = identity(m)
    center = [F(1, m)] * m
    directions: list[list[F]] = []
    carrier_factors: list[list[F]] = []
    for s in range(m):
        d = [Z] * m
        d[s] = -O
        d[(s + 1) % m] = O
        directions.append(d)
        carrier_factors.append(add(center, scale(tau / 20, d)))
    positive_normer_supports = [{j for j, x in enumerate(d) if x > Z}
                                for d in directions]
    negative_normer_supports = [{j for j, x in enumerate(d) if x < Z}
                                for d in directions]
    assert set.intersection(*positive_normer_supports) == set()
    assert set.intersection(*negative_normer_supports) == set()

    L = basis + carrier_factors + [center]
    B = [[O if j == i else Z for j in range(n)] for i in range(m)]
    # The slightly verbose expression above makes the support convention
    # explicit: B[i,a_i]=1 and every non-anchor column is zero.
    P = matmul(L, B)
    assert_factorization(L, B, P, delta)
    assert max(neg(row) for row in P) == Z
    assert all(P[j] == B[j] for j in anchors)
    assert len({tuple(P[j]) for j in anchors}) == m
    assert len({tuple(P[u]) for u in carriers}) == m

    rho = 4 * tau
    kappa = tau / 4
    assert delta <= delta_rt()

    # The public center is the uniform convex combination of the m recurrent
    # anchors.  It is not a vertex; H=0 and hidden-top/tallness both fail.
    p_v = P[v]
    assert p_v == convex(center, [P[j] for j in anchors])
    H = Z
    hidden_top = False
    tall_margin = H - 16 * tau
    assert tall_margin == -16 * tau < Z

    # A legal far mass exists at this diagnostic center: all recurrent
    # anchors are rho-far and P_v gives them total mass one.  Its barycenter
    # is p_v, so the true ray diagnostic is exactly zero at Lambda=0.
    anchor_center_distances = [l1(P[j], p_v) for j in anchors]
    assert all(d >= rho and d > F(1, 2) for d in anchor_center_distances)
    selected_mass = sum((P[v][j] for j in anchors), Z)
    q_A = convex([P[v][j] for j in anchors], [P[j] for j in anchors])
    assert selected_mass == O and q_A == p_v
    Z_ray = l1(sub(p_v, q_A))
    assert Z_ray == Z

    probe_weight = F(1, 8 * m)
    eta_mass = probe_weight * m
    assert eta_mass == F(1, 8) > ONE_160
    eta_vector = [Z] * n
    for u in carriers:
        eta_vector[u] = probe_weight

    carrier_panels: list[dict[str, Any]] = []
    union: set[int] = set()
    hes_mass = Z
    local_dtr_mass = Z
    eta_tail_integral = Z
    for s, u in enumerate(carriers):
        d_factor = scale(tau / 2, directions[s])
        qtilde_factor = add(carrier_factors[s], d_factor)
        x_factor = sub(carrier_factors[s], scale(4, d_factor))
        assert qtilde_factor == add(center, scale(11 * tau / 20, directions[s]))
        assert x_factor == sub(center, scale(39 * tau / 20, directions[s]))
        assert all(x >= Z for x in qtilde_factor + x_factor)
        assert sum(qtilde_factor, Z) == sum(x_factor, Z) == O

        qtilde = convex(qtilde_factor, [P[j] for j in anchors])
        x = convex(x_factor, [P[j] for j in anchors])
        D = sub(qtilde, P[u])
        assert l1(D) == tau
        assert tau / 2 <= l1(D) <= 2 * tau
        assert sub(P[u], scale(4, D)) == x

        # x is in the row hull with a full-support m-row certificate.  Its
        # distance to every actual row is nevertheless macroscopic at tau
        # scale; the exact minimum is attained at v and adjacent carriers.
        hull_distance = Z
        distances = [l1(row, x) for row in P]
        min_actual = min(distances)
        nearest = [labels[i] for i, d in enumerate(distances) if d == min_actual]
        assert min_actual == F(39, 10) * tau > 3 * delta
        assert len([w for w in x_factor if w > Z]) == m

        chi_values = [dot(sign(D), sub(row, P[u])) / l1(D) for row in P]
        incidence = [j for j in range(n)
                     if P[u][j] > Z and abs(chi_values[j]) > O]
        expected = sorted([s, (s + 1) % m])
        assert incidence == expected
        tail = sum((P[u][j] for j in incidence), Z)
        assert tail == F(2, m) > tau / 8
        union.update(incidence)
        eta_tail_integral += probe_weight * tail
        local_dtr_mass += probe_weight

        carrier_panels.append({
            "carrier": labels[u],
            "A_tilde": F(4),
            "ell=norm_D": l1(D),
            "g_proxy=A*ell": 4 * l1(D),
            "q_tilde": qtilde,
            "x": x,
            "hull_weights": x_factor,
            "hull_support": [labels[j] for j in anchors],
            "hull_distance": hull_distance,
            "3delta": 3 * delta,
            "min_actual_row_distance": min_actual,
            "nearest_actual_rows": nearest,
            "actual_row_margin": min_actual - 3 * delta,
            "chi_values": chi_values,
            "receiver_incidence": [labels[j] for j in incidence],
            "Tail_1": tail,
            "tail_threshold": tau / 8,
            "tail_margin": tail - tau / 8,
        })

    assert hes_mass < ONE_160
    assert local_dtr_mass == eta_mass > ONE_160
    assert union == set(anchors)
    assert eta_tail_integral == F(1, 4 * m)

    # TU's common receiver conclusion is strong on the probe: the root row
    # gives the recurrent union mass one.  The R0 foldback inequality also
    # passes, but the prior carrier-submeasure ownership eta<=P_f^+ fails.
    U = sorted(union)
    Pf_plus = positive(P[v])
    Pf_U = sum((Pf_plus[j] for j in U), Z)
    assert Pf_U == O > tau / 2560
    Pi = [sum((probe_weight * positive(P[u])[j] for u in carriers), Z)
          for j in range(n)]
    assert all(Pi[j] == F(1, 8 * m) for j in anchors)
    assert all(Pi[j] == Z for j in range(m, n))
    r0_foldback_overflow = sup_overflow(Pi, Pf_plus)
    eta_domination_excess = sup_overflow(eta_vector, Pf_plus)
    assert r0_foldback_overflow == Z <= e_delta
    assert eta_domination_excess == eta_mass == F(1, 8)

    # At the flat/non-top diagnostic center every recurrent receiver is both
    # exterior and shallow.  This makes EC negative but leaves D_leaf positive,
    # exactly illustrating why the two diagnostics are not interchangeable.
    E_star = [i for i, row in enumerate(P) if l1(row, p_v) >= F(1, 2)]
    depth = [Z] * n
    L_v = [i for i, d in enumerate(depth) if d <= tau / 4]
    assert E_star == anchors and L_v == list(range(n))
    U_E = sorted(set(U).intersection(E_star))
    U_L = sorted(set(U).intersection(L_v))
    assert U_E == U_L == anchors
    Pv_E = sum((max(P[v][j], Z) for j in E_star), Z)
    Pv_L = sum((max(P[v][j], Z) for j in L_v), Z)
    assert Pv_E == Pv_L == O
    ell_T = delta + (4 * tau / 63) * (D0 + tau / 4)
    assert ell_T < 2 * tau / 15
    assert not (Pv_L < ell_T)
    exterior_floor = tau * selected_mass / 8
    assert Pv_E >= exterior_floor
    all_center_shallow_countervalue = Pv_E
    all_center_threshold = tau * selected_mass / 16
    assert not (all_center_shallow_countervalue < all_center_threshold)
    far_G_mass = Z
    assert far_G_mass < all_center_threshold

    D_EC = Z_ray - Pv_E / 8 + (CM / 16) * Pv_L
    D_leaf = Z_ray - CM * tau / 64 + (CM / 16) * Pv_L
    assert D_EC == -F(7, 64) < Z
    assert D_leaf == F(1, 64) - tau / 256 > Z

    for cp in carrier_panels:
        inc = [labels.index(name) for name in cp["receiver_incidence"]]
        cp["incidence_intersection_E_star"] = [labels[j] for j in sorted(set(inc) & set(E_star))]
        cp["incidence_intersection_L_v"] = [labels[j] for j in sorted(set(inc) & set(L_v))]
        assert cp["incidence_intersection_E_star"] == cp["receiver_incidence"]
        assert cp["incidence_intersection_L_v"] == cp["receiver_incidence"]

    # The numeric M-ledger is intentionally not promoted to a certificate:
    # R0.1 already proves that these probe carriers cannot be the original
    # selected-corner D population.  Therefore R1 and B1--B5 are unavailable.
    MX, MI, MD = Z, Z, eta_mass
    ledger_numbers_pass = MX <= F(1, 8) and MI < F(1, 16) and MD > F(1, 16)
    assert ledger_numbers_pass
    fixed_D_certificate_legal = False
    r0_all_outputs = False
    b1_b5_outputs = False
    r1_output = False
    b5_label = "NOT_REACHED"

    gate = {
        "exact_factorization_and_idempotence": True,
        "delta=tau^2": delta == tau * tau,
        "all_row_negativity<=delta": all(neg(row) <= delta for row in P),
        "genuine_rank_growth_source": "m distinct absorbing anchors",
        "rank_not_from_transients": True,
        "public_center_is_hidden_vertex": hidden_top,
        "H>16tau": H > 16 * tau,
        "legal_far_selected_mass": selected_mass > Z,
        "all_center_shallow_package": all_center_shallow_countervalue < all_center_threshold,
        "all_center_far_G_package": far_G_mass >= all_center_threshold,
        "nonempty_ultra_omega": False,
        "theta<tau/D0": Z < tau / D0,
        "routine_ceiling": delta <= delta_rt(),
        "fixed_D_certificate": fixed_D_certificate_legal,
        "R0_all_outputs": r0_all_outputs,
        "B1-B5_all_outputs": b1_b5_outputs,
        "R1_output": r1_output,
        "strict_HES_failure_guard": hes_mass < ONE_160,
        "local_DTR_predicate_mass>1/160": local_dtr_mass > ONE_160,
        "all_carrier_Tail_1>tau/8": all(cp["Tail_1"] > tau / 8 for cp in carrier_panels),
        "P_fstar_plus_U>tau/2560": Pf_U > tau / 2560,
        "D_leaf<0": D_leaf < Z,
    }
    full_dtr_entry = all(value is True for key, value in gate.items()
                         if key != "genuine_rank_growth_source")
    assert not full_dtr_entry

    trend = {
        "m": m,
        "ambient_n": n,
        "certified_rank": m,
        "genuine_recurrent_support": m,
        "synthetic_hull_support": m,
        "tau": tau,
        "delta": delta,
        "max_single_row_negativity": Z,
        "max_negativity_over_tau2": Z,
        "max_hull_distance": Z,
        "min_actual_row_distance": F(39, 10) * tau,
        "actual_row_margin_over_3delta": F(39, 10) * tau - 3 * delta,
        "min_Tail_1": F(2, m),
        "tail_margin_over_tau/8": F(2, m) - tau / 8,
        "P_fstar_plus_U": Pf_U,
        "union_margin_over_tau/2560": Pf_U - tau / 2560,
        "H_minus_16tau": tall_margin,
        "R0_carrier_domination_excess": eta_domination_excess,
        "B4_shallow_margin=ell_T-PvL": ell_T - Pv_L,
        "D_EC": D_EC,
        "D_leaf": D_leaf,
        "full_DTR_entry": full_dtr_entry,
    }

    result = {
        "id": f"rotating_retraction_m{m}",
        "verdict": "PARTIAL_LOCAL_DTR_ONLY",
        "warning": "L3 evidence only, never a proof; not a full DTR entrant",
        "parameters": {"m": m, "tau": tau, "delta": delta, "D0": D0,
                       "e_delta": e_delta, "delta_rt": delta_rt(),
                       "c_m": CM, "rho": rho, "kappa": kappa},
        "dimensions": {"ambient_n": n, "rank": m,
                       "rank_certificate": "B*L=I_m",
                       "recurrent_anchor_count": m,
                       "transient_probe_count_not_used_as_rank": m + 1},
        "labels": labels,
        "row_negative_masses": [neg(row) for row in P],
        "max_single_row_negativity": Z,
        "attempted_I_base": {
            "public_center": labels[v], "center_is_vertex": False,
            "H": H, "H_minus_16tau": tall_margin,
            "selected_A": [labels[j] for j in anchors], "S": selected_mass,
            "q_A": q_A, "Z_v(q_A)": Z_ray,
            "all_center_shallow_countervalue": all_center_shallow_countervalue,
            "all_center_threshold": all_center_threshold,
            "far_G_mass": far_G_mass, "omega_nonempty": False,
            "theta": Z, "theta_threshold": tau / D0,
        },
        "probe_D_population": {
            "eta_mass": eta_mass, "eta_weight_each": probe_weight,
            "numeric_M_ledger": {"M_X": MX, "M_I": MI, "M_D": MD,
                                 "inequalities_pass": ledger_numbers_pass},
            "legal_fixed_D_certificate": fixed_D_certificate_legal,
            "binding_reason": "eta_D* is not <= P_f*+ on carrier fibers",
            "R0_carrier_domination_excess": eta_domination_excess,
            "R0_foldback_overflow": r0_foldback_overflow,
            "R0_e_delta": e_delta,
        },
        "strict_HES_guard": {"HES_mass": hes_mass, "threshold": ONE_160,
                             "strict_failure": hes_mass < ONE_160},
        "local_DTR_probe": {
            "predicate_mass": local_dtr_mass, "threshold": ONE_160,
            "mass_margin": local_dtr_mass - ONE_160,
            "carriers": carrier_panels,
            "eta_weighted_Tail_1_aggregate": eta_tail_integral,
            "U_tail": [labels[j] for j in U],
            "U_tail_intersection_E_star": [labels[j] for j in U_E],
            "U_tail_intersection_L_v": [labels[j] for j in U_L],
            "P_fstar_plus_U_tail": Pf_U,
            "union_threshold": tau / 2560,
            "common_positive_normer_coordinate": None,
            "common_negative_normer_coordinate": None,
            "full_hypothesis_entry": full_dtr_entry,
        },
        "B4_and_residual_panel": {
            "P_v_plus_E_star": Pv_E,
            "P_v_plus_L_v": Pv_L,
            "ell_T": ell_T,
            "two_tau_over_15": 2 * tau / 15,
            "exterior_floor=tau*S/8": exterior_floor,
            "Z_v(q_A)": Z_ray,
            "D_EC": D_EC,
            "D_EC_negative": D_EC < Z,
            "D_leaf": D_leaf,
            "D_leaf_negative": D_leaf < Z,
        },
        "R0_B1-B5_R1_status": {
            "R0_all_outputs": r0_all_outputs,
            "B1-B5_all_outputs": b1_b5_outputs,
            "R1_output": r1_output,
            "B5_label_status": b5_label,
            "B5_population_warning": (
                "B5 is not reached; even in a legal run its population would be "
                "different from eta_D*, never identified carrierwise"),
        },
        "gate": gate,
        "trend": trend,
    }
    if include_matrix:
        result["L"] = L
        result["B"] = B
        result["P"] = P
    return result


def w66_plateau_unit() -> dict[str, Any]:
    """Reconstruct the exact W66/W63 k=2048 plateau regression."""
    k = 2048
    tau = F(1, k)
    delta = tau * tau
    t0 = tau / 8
    e = 2 * tau
    L = [
        [O, Z, Z],
        [O + delta * (O - t0), delta * t0, -delta],
        [Z, O, Z],
        [Z, Z, O],
        [Z, delta, O - delta],
        [Z, -delta, O + delta],
        [O - e, -e * delta, e * (O + delta)],
    ]
    B = [
        [O, Z, Z, Z, Z, Z, Z],
        [Z, Z, O, Z, Z, Z, Z],
        [Z, Z, Z, F(1, 2), F(1, 4), F(1, 4), Z],
    ]
    P = matmul(L, B)
    assert_factorization(L, B, P, delta)
    u, zrow, orow, arow, xrow, yrow, frow = range(7)

    alpha = (O + delta) / (O + 2 * delta)
    closest = convex([alpha, O - alpha], [P[zrow], P[yrow]])
    H = l1(P[u], closest)
    r = (O - 2 * delta * t0) / (O + 2 * delta)
    dual = [O, Z, -O, r, r, r, Z]
    hstar = t0 - delta * (O - t0)
    hvals = [Z, Z, O, t0, delta + (O - delta) * t0, hstar, e * hstar]
    constant = -dot(dual, P[zrow])
    phi = [dot(dual, row) + constant for row in P]
    assert phi[u] == H and all(phi[i] <= Z for i in [zrow, orow, yrow])
    assert H < 16 * tau

    kT = sub(P[frow], P[u])
    kO = scale(e * hstar, sub(P[orow], P[u]))
    A = e * (O + delta) / delta
    ell = l1(P[zrow], P[u])
    g = l1(kT, kO)
    assert add(kT, scale(A, sub(P[zrow], P[u]))) == kO
    assert g == A * ell == 4 * tau * (O + delta) > tau
    assert A > 4
    assert ell == 2 * delta < tau / 2
    route = "C0"
    eta_mass = O - e
    assert eta_mass == F(1023, 1024)
    MX = MI = Z
    MD = eta_mass
    assert MX <= F(1, 8) and MI < F(1, 16) and MD > F(1, 16)

    Z_ray = Z
    Pv_L = O
    D_leaf = Z_ray - CM * tau / 64 + (CM / 16) * Pv_L
    assert D_leaf > Z
    return {
        "id": "w66_w63_plateau_k2048", "L": L, "B": B, "P": P,
        "tau": tau, "delta": delta, "M_X": MX, "M_I": MI, "M_D": MD,
        "g": g, "A": A, "ell": ell, "ell_over_tau": ell / tau,
        "route": route, "H": H, "H_minus_16tau": H - 16 * tau,
        "D_leaf": D_leaf,
    }


def w55_unit() -> dict[str, Any]:
    """Canonical W55 A0=5: exact finance rejection and DTR routing guard."""
    tau, target_delta, A = F(1, 256), F(1, 65536), F(5)
    a = tau / (O + tau)
    L = [
        [O, Z, Z],
        [O + A * a - a * target_delta, -A * a, a * target_delta],
        [O + A - target_delta, -A, target_delta],
        [Z, O, Z],
        [Z, Z, O],
    ]
    B = [
        [O - tau, tau + target_delta, -target_delta, Z, Z],
        [Z, Z, Z, O, Z],
        [Z, Z, Z, Z, O],
    ]
    P = matmul(L, B)
    # Its exact idempotence is valid, but the target delta bound is not.
    assert matmul(B, L) == identity(3)
    assert matmul(L, B) == P and matmul(P, P) == P
    assert all(sum(row, Z) == O for row in P)
    nus = [neg(row) for row in P]
    finance = A + (O + A - target_delta) * target_delta
    assert nus[2] == finance == max(nus)
    assert finance == F(21475229695, 4294967296) > target_delta

    v, w, frow, zrow, orow = range(5)
    dz = sub(P[zrow], P[v])
    df = sub(P[frow], P[v])
    do = sub(P[orow], P[v])
    assert add(df, scale(A, dz)) == scale(target_delta, do)
    ell = l1(dz)
    qtilde = add(P[v], scale(2 * tau / ell, dz))
    Atilde = A * ell / (2 * tau)
    D = sub(qtilde, P[v])
    x = sub(P[v], scale(Atilde, D))
    actor_residual = l1(P[frow], x)
    min_actual = min(l1(row, x) for row in P)
    assert actor_residual == target_delta * l1(do) <= 3 * target_delta
    assert min_actual <= actor_residual <= 3 * target_delta
    routes_to_DTR = min_actual > 3 * target_delta
    assert not routes_to_DTR

    chi = [dot(sign(D), sub(row, P[v])) / l1(D) for row in P]
    tail = sum((max(P[v][j], Z) for j in range(len(P)) if abs(chi[j]) > O), Z)
    assert tail == F(257, 65536) > tau / 8 > target_delta
    return {
        "id": "w55_A0_5", "L": L, "B": B, "P": P,
        "tau": tau, "target_delta=tau^2": target_delta,
        "row_negative_masses": nus, "finance_nu": finance,
        "excess_over_tau2": finance - target_delta,
        "q_tilde": qtilde, "A_tilde": Atilde, "x": x,
        "actor_residual": actor_residual, "min_actual_row_distance": min_actual,
        "3delta": 3 * target_delta, "Tail_1": tail,
        "routes_to_DTR": routes_to_DTR,
        "classification": "REJECTED by order-one finance negativity; routes away from DTR",
    }


def print_family(c: dict[str, Any]) -> None:
    p = c["parameters"]
    tr = c["trend"]
    local = c["local_DTR_probe"]
    b4 = c["B4_and_residual_panel"]
    root = c["probe_D_population"]
    status = c["R0_B1-B5_R1_status"]
    print(f"FAMILY {c['id']}: PARTIAL_LOCAL_DTR_ONLY — rank={tr['certified_rank']}, "
          f"support={tr['genuine_recurrent_support']}, tau={fstr(p['tau'])}, "
          f"max-row-neg={fstr(tr['max_single_row_negativity'])}; full DTR entry=FAIL.")
    print("  FACTOR P=LB, BL=I, P^2=P; delta=tau^2="
          f"{fstr(p['delta'])}; max nu/tau^2={fstr(tr['max_negativity_over_tau2'])}.")
    print("  HES strict guard: mass=0 < 1/160; local DTR predicate mass="
          f"{fstr(local['predicate_mass'])} > 1/160 (margin "
          f"{fstr(local['mass_margin'])}).")
    for cp in local["carriers"]:
        print("  CARRIER " + cp["carrier"] + ": h=" + fstr(cp["hull_distance"]) +
              " <= 3delta=" + fstr(cp["3delta"]) + "; min-row=" +
              fstr(cp["min_actual_row_distance"]) + " > 3delta; Tail_1=" +
              fstr(cp["Tail_1"]) + " > tau/8=" + fstr(cp["tail_threshold"]) +
              "; incidence={" + ",".join(cp["receiver_incidence"]) + "}; " +
              "incidence∩E*={" + ",".join(cp["incidence_intersection_E_star"]) +
              "}; incidence∩L_v={" + ",".join(cp["incidence_intersection_L_v"]) + "}.")
    print("  AGGREGATE eta-weighted Tail_1=" +
          fstr(local["eta_weighted_Tail_1_aggregate"]) + "; U_tail={" +
          ",".join(local["U_tail"]) + "}; P_f*+(U_tail)=" +
          fstr(local["P_fstar_plus_U_tail"]) + " > tau/2560=" +
          fstr(local["union_threshold"]) + ".")
    print("  R0 carrier ownership eta<=P_f*+: FAIL by excess " +
          fstr(root["R0_carrier_domination_excess"]) + "; foldback overflow=" +
          fstr(root["R0_foldback_overflow"]) + " <= e_delta=" +
          fstr(root["R0_e_delta"]) + ".")
    print("  B5 label=" + status["B5_label_status"] + ". WARNING: " +
          status["B5_population_warning"])
    print("  D_EC=Z-(1/8)P_v+(E*)+(c_m/16)P_v+(L_v)=" +
          fstr(b4["D_EC"]) + " < 0: " + pf(b4["D_EC_negative"]) + ".")
    print("  D_leaf=Z-c_m*tau/64+(c_m/16)P_v+(L_v)=" +
          fstr(b4["D_leaf"]) + " < 0: " + pf(b4["D_leaf_negative"]) + ".")
    print("  BINDING H-16tau=" + fstr(tr["H_minus_16tau"]) +
          "; ell_T-P_v+(L_v)=" + fstr(tr["B4_shallow_margin=ell_T-PvL"]) +
          "; R0-domination excess=" + fstr(tr["R0_carrier_domination_excess"]) + ".")


def build() -> dict[str, Any]:
    ranks = [4, 8, 16, 32]
    members = [rotating_retraction(m, include_matrix=(m == ranks[-1])) for m in ranks]
    assert all(not c["local_DTR_probe"]["full_hypothesis_entry"] for c in members)
    assert [c["dimensions"]["rank"] for c in members] == ranks
    assert [c["dimensions"]["recurrent_anchor_count"] for c in members] == ranks
    assert all(c["max_single_row_negativity"] == Z for c in members)
    plateau = w66_plateau_unit()
    w55 = w55_unit()
    return {
        "schema": "w69-dtr-growing-rank-exact-l3-v1",
        "arithmetic": "fractions.Fraction; JSON values are exact rational strings",
        "warning": "L3 constructive/numerical evidence only; never a proof",
        "verdict": "PARTIAL",
        "family": {
            "name": "rotating_retraction",
            "formula": "m>=4, tau=1/(2^20*m), rank=m, m distinct absorbing anchors",
            "finding": (
                "local DTR convexification/tail/rotation with max negativity 0; "
                "full entry blocked by R0 ownership, hidden tallness, B4 shallow mass, and D_leaf"),
            "members": members,
        },
        "rank_trend": [c["trend"] for c in members],
        "best_near_miss": members[-1],
        "unit_tests": {"W66_W63_plateau": plateau, "W55_A0_5": w55},
        "genuine_full_DTR_entries": 0,
        "genuine_refuters": 0,
        "bycatch": (
            "rank-growing local DTR geometry and rotating tail incidence; not an entrant "
            "to any full leaf class"),
    }


def main() -> None:
    data = build()
    Path("certificates.json").write_text(json.dumps(qstr(data), indent=2) + "\n")
    for candidate in data["family"]["members"]:
        print_family(candidate)
    print("RANK TREND: max single-row negativity is exactly 0 for ranks 4,8,16,32; "
          "H/tau=0, R0 ownership excess=1/8, P_v+(L_v)=1, and D_leaf>0 at every rank.")
    w66 = data["unit_tests"]["W66_W63_plateau"]
    print("UNIT W66/W63 plateau: PASS — ell/tau=" + fstr(w66["ell_over_tau"]) +
          "=2*tau; R1=C0; H>16tau=FAIL(expected); D_leaf=" +
          fstr(w66["D_leaf"]) + ">0.")
    w55 = data["unit_tests"]["W55_A0_5"]
    print("UNIT W55 A0=5: PASS — finance nu=" + fstr(w55["finance_nu"]) +
          " > tau^2=" + fstr(w55["target_delta=tau^2"]) +
          "; min-row<=3delta, so routes AWAY from DTR.")
    print("SUMMARY: PARTIAL — 0 full DTR entries and 0 refuters; exact L3 evidence only, never a proof.")


if __name__ == "__main__":
    main()
