#!/usr/bin/env python3
"""Exact L3 deciders for the W63 S/C pre-creative shapes.

All arithmetic that participates in a certificate is fractions.Fraction.  The
program exits nonzero on every internal mismatch.  It deliberately distinguishes
an exact projection from a genuine L5 datum: several exact projections below are
rejected because the hidden-top or global-negativity gate fails.

This is constructive/numerical evidence, never a proof of S, C, or L5-GAP-1.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Sequence

Z = F(0)
O = F(1)


def dot(a: Sequence[F], b: Sequence[F]) -> F:
    return sum((x * y for x, y in zip(a, b)), Z)


def add(a: Sequence[F], b: Sequence[F]) -> list[F]:
    return [x + y for x, y in zip(a, b)]


def sub(a: Sequence[F], b: Sequence[F]) -> list[F]:
    return [x - y for x, y in zip(a, b)]


def scale(t: F, a: Sequence[F]) -> list[F]:
    return [t * x for x in a]


def l1(a: Sequence[F], b: Sequence[F] | None = None) -> F:
    if b is None:
        return sum((abs(x) for x in a), Z)
    return sum((abs(x - y) for x, y in zip(a, b)), Z)


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    bt = list(zip(*b))
    return [[dot(row, col) for col in bt] for row in a]


def matvec(a: Sequence[Sequence[F]], x: Sequence[F]) -> list[F]:
    return [dot(row, x) for row in a]


def convex(weights: Sequence[F], points: Sequence[Sequence[F]]) -> list[F]:
    assert weights and len(weights) == len(points) and sum(weights, Z) == O
    return [sum((weights[i] * points[i][j] for i in range(len(points))), Z)
            for j in range(len(points[0]))]


def neg_mass(row: Sequence[F]) -> F:
    return sum((-x for x in row if x < 0), Z)


def delta_of(p: Sequence[Sequence[F]]) -> F:
    return max(neg_mass(row) for row in p)


def assert_projection(p: Sequence[Sequence[F]], delta: F | None = None) -> None:
    n = len(p)
    assert n and all(len(row) == n for row in p)
    assert all(sum(row, Z) == O for row in p)
    assert matmul(p, p) == [list(row) for row in p]
    if delta is not None:
        assert delta_of(p) == delta


def assert_fixed_values(p: Sequence[Sequence[F]], h: Sequence[F]) -> None:
    assert matvec(p, h) == list(h)
    assert all(Z <= x <= O for x in h)


def qstr(x: Any) -> Any:
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, dict):
        return {k: qstr(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [qstr(v) for v in x]
    return x


def w61_factorization(tau: F, eta: F, theta: F = F(1, 64)) -> dict[str, Any]:
    """The W61 dyadic leak-financer in explicit P=L B, B L=I coordinates."""
    delta = tau * tau
    eps = delta / 2
    K = O + delta - eta
    alpha = K - eps
    assert Z < eta < K and alpha > Z
    q = eps / alpha
    # affine rank-three coordinates A,C,D
    L = [
        [O, Z, Z], [O, Z, Z], [alpha, eta, -eps],
        [Z, O, Z], [Z, Z, O], [O - theta, theta, Z],
    ]
    B = [
        [O + q, -q, Z, Z, Z, Z],
        [Z, Z, Z, O, Z, Z],
        [Z, Z, Z, Z, O, Z],
    ]
    assert matmul(B, L) == [[O, Z, Z], [Z, O, Z], [Z, Z, O]]
    p = matmul(L, B)
    assert_projection(p, delta)
    labels = ["a0", "a1", "z", "c", "d", "x"]

    # Exact distance from A to conv{Z,C,D}; the same primal/dual pair is
    # valid throughout the dial range used below.
    wz = O / alpha
    wd = O - wz
    H_sep = 2 * eta / alpha
    closest: list[F] | None = None
    if Z <= wz <= O and Z <= wd <= O:
        closest = convex([wz, wd], [p[2], p[4]])
        assert l1(p[0], closest) == H_sep
    t = eta / eps
    dual_y = [O, O - 2 * t, Z, -O, O, Z]
    if t <= O:
        phi = [dot(dual_y, row) - O for row in p]
        assert max(abs(x) for x in dual_y) == O
        assert phi[0] == H_sep and all(phi[i] <= Z for i in [2, 3, 4, 5])

    return {"labels": labels, "L": L, "B": B, "matrix": p, "delta": delta,
            "eps": eps, "eta": eta, "alpha": alpha, "q": q, "theta": theta,
            "t_star_parameter": t, "H_separation": H_sep,
            "closest_weights_ZD": [wz, wd], "closest_point": closest,
            "dual_y_when_t_le_1": dual_y}


def s_base_seed(tau: F) -> dict[str, Any]:
    delta = tau * tau
    eps = delta / 2
    tstar = tau / 8
    eta = eps * tstar
    d = w61_factorization(tau, eta)
    p = d["matrix"]
    rho, kappa = 4 * tau, tau / 4
    h_A = [Z, Z, Z, O, tstar, d["theta"]]
    assert_fixed_values(p, h_A)
    far = [i for i, row in enumerate(p) if l1(row, p[0]) >= rho]
    assert min(h_A[i] for i in far) == tstar < kappa
    # Exact upper witness from W61.
    left = add(sub(p[4], p[0]), scale(O / d["eps"], sub(p[2], p[0])))
    right = scale(tstar, sub(p[3], p[0]))
    assert left == right
    H = d["H_separation"]
    assert H < 8 * tau < 16 * tau
    # Exact visibility certificates for the full visible set W={Z,C,D}.
    hza = (d["eps"] - d["eta"]) / d["alpha"]
    h_z = [hza, hza, Z, O, O, (O-d["theta"])*hza+d["theta"]]
    h_c = [O, O, O-d["eta"], Z, O, O-d["theta"]]
    hda = (O - d["eta"]) / d["alpha"]
    h_d = [hda, hda, O, O, Z, (O-d["theta"])*hda+d["theta"]]
    visibility: dict[str, Any] = {}
    for target, h in [(2, h_z), (3, h_c), (4, h_d)]:
        assert_fixed_values(p, h)
        far_target = [i for i, row in enumerate(p) if l1(row, p[target]) >= rho]
        margin = min(h[i] for i in far_target)
        assert margin >= kappa
        visibility[d["labels"][target]] = {"h_values": h, "far_margin": margin}
    # X lies in the visible hull with these exact affine weights.
    wxz = (O - d["theta"]) / d["alpha"]
    wxc = d["theta"] - wxz*d["eta"]
    wxd = wxz*d["eps"]
    xweights = [wxz, wxc, wxd]
    assert all(w >= Z for w in xweights) and sum(xweights, Z) == O
    assert convex(xweights, [p[2], p[3], p[4]]) == p[5]
    dual_y = d["dual_y_when_t_le_1"]
    phi = [dot(dual_y, row) - O for row in p]
    assert phi[0] == phi[1] == H
    assert all(phi[i] <= Z for i in [2, 3, 4, 5])
    return {
        "id": f"S_w61_base_tau_1_{tau.denominator}",
        "classification": "exact_seed_not_L5_datum",
        **d,
        "tau": tau, "rho": rho, "kappa": kappa,
        "fibers": [{"row_point": "A", "indices": [0, 1]},
                   {"row_point": "Z", "indices": [2]},
                   {"row_point": "C", "indices": [3]},
                   {"row_point": "D", "indices": [4]},
                   {"row_point": "X", "indices": [5]}],
        "visible_set": ["z", "c", "d"], "visibility_certificates": visibility,
        "X_visible_hull_weights_ZCD": xweights,
        "hiddenness_h_values": h_A,
        "hiddenness_far_indices": far, "t_star": tstar,
        "hiddenness_balance_left": left, "hiddenness_balance_right": right,
        "H": H, "height_primal_closest_point": d["closest_point"],
        "height_primal_weights_ZD": d["closest_weights_ZD"],
        "height_dual_y": dual_y, "height_dual_phi_values": phi,
        "H_over_tau": H / tau, "H_minus_16tau": H - 16 * tau,
        "failed_gates": {"H>16tau": False,
                         "C_is_shallow": Z <= H - 8 * tau,
                         "selected_far_deep_mass_S>=1/4": False},
    }


def s_height_dial(tau: F, ratio: F) -> dict[str, Any]:
    """Dial dist(A,conv{Z,C,D})/tau to ratio and certify visibility failure."""
    target = ratio * tau
    eps = tau * tau / 2
    # Solve target = 2 eta/(1+eps-eta) exactly.
    eta = target * (O + eps) / (2 + target)
    d = w61_factorization(tau, eta)
    assert d["H_separation"] == target
    # The formal W61 height formula demands a convex Z/D closest point.
    # At every tall target its D weight is already negative.
    assert d["closest_weights_ZD"][1] < Z and d["closest_point"] is None
    p = d["matrix"]
    rho, kappa = 4 * tau, tau / 4
    # A legal affine exposer: in L coordinates h=l_C+l_D.  Its values are
    # eta-eps on Z, one on C,D, and theta on X.
    h = [Z, Z, eta - eps, O, O, d["theta"]]
    assert_fixed_values(p, h)
    far = [i for i, row in enumerate(p) if l1(row, p[0]) >= rho]
    far_margin = min(h[i] for i in far)
    assert far_margin >= kappa
    assert d["t_star_parameter"] > kappa
    return {
        "ratio_requested": ratio, "tau": tau, "target_delta": tau * tau,
        "matrix": p, "L": d["L"], "B": d["B"], "eta": eta,
        "formal_height_target": target,
        "formal_target_minus_16tau": target - 16 * tau,
        "failed_primal_weights_ZD": d["closest_weights_ZD"],
        "negative_D_weight_margin": -d["closest_weights_ZD"][1],
        "hiddenness_parameter_eta_over_eps": d["t_star_parameter"],
        "required_hidden_ceiling_kappa": kappa,
        "hiddenness_failure_margin": d["t_star_parameter"] - kappa,
        "visible_exposer_h_values": h, "far_indices": far,
        "visible_exposer_far_margin": far_margin,
        "visible_margin_over_kappa": far_margin - kappa,
        "actual_status": "formal height dial leaves the convex face and A is visible",
    }


def s_attachment_budget(tau: F, selected_mass: F = F(1, 4)) -> dict[str, Any]:
    """Exact clone-safe coefficient budget for attaching C and D receiver fibers.

    A positive clone and a compensating negative clone preserve B L=I exactly.
    C is the proposed shallow exterior payer and D is the far actor.  The matrix
    is an exact projection, but its actual negativity exposes the binding gate.
    """
    base = w61_factorization(tau, tau**3 / 16)
    L = [row[:] for row in base["L"]] + [[Z, O, Z], [Z, Z, O]]
    shallow = tau * selected_mass / 16
    B = [row[:] + [Z, Z] for row in base["B"]]
    # Add +shallow on a C clone, -shallow on C; +S on a D clone, -S on D.
    B[0][3] -= shallow
    B[0][4] -= selected_mass
    B[0][6] = shallow
    B[0][7] = selected_mass
    assert matmul(B, L) == [[O, Z, Z], [Z, O, Z], [Z, Z, O]]
    p = matmul(L, B)
    assert_projection(p)
    actual = delta_of(p)
    target = tau * tau
    q = base["q"]
    top_negative = neg_mass(p[0])
    assert top_negative == q + shallow + selected_mass
    assert actual >= top_negative > target
    # Even omitting the actor, the required shallow clone exceeds the spare
    # top-row negative budget for the complete sweep range.
    spare = target - q
    assert spare > Z and selected_mass + shallow > spare
    return {
        "tau": tau, "target_delta": target, "selected_actor_mass_S": selected_mass,
        "required_shallow_mass_tauS_over_16": shallow,
        "base_top_negative_q": q, "target_negative_spare_delta_minus_q": spare,
        "shallow_floor_minus_spare": shallow - spare,
        "shallow_alone_exceeds_spare": shallow > spare,
        "L": L, "B": B, "matrix": p, "BL": matmul(B, L),
        "actual_global_delta": actual, "actual_delta_minus_target": actual - target,
        "top_negative_mass": top_negative,
        "binding_inequality": "q + m_sh + S <= tau^2 (fails already at m_sh <= tau^2-q)",
    }


def exact_scalar_width(weights: Sequence[F]) -> tuple[F, tuple[int, ...]]:
    """Exact MAD supremum on coordinate row points by extreme-sign enumeration."""
    best, arg = Z, tuple()
    for signs in itertools.product((-1, 1), repeat=len(weights)):
        mean = sum((w * s for w, s in zip(weights, signs)), Z)
        value = sum((w * abs(F(s) - mean) for w, s in zip(weights, signs)), Z)
        if value > best:
            best, arg = value, signs
    return best, arg


def c_width_bouquet(m: int, tau: F) -> dict[str, Any]:
    """Two co-top groups in the exact corank-one simplex completion."""
    assert m >= 2 and m % 2 == 0 and tau <= F(1, 32)
    delta = tau * tau
    n = m + 3
    v, actors, ballast, payer = 0, list(range(1, m + 1)), m + 1, m + 2
    labels = ["v"] + [f"q{i}" for i in range(1, m + 1)] + ["b", "f"]
    p = [[O if i == j else Z for j in range(n)] for i in range(n)]
    p[v] = [Z] * n
    for i in actors:
        p[v][i] = F(1, 4 * m)
    p[v][ballast] = F(3, 4) + delta
    p[v][payer] = -delta
    assert_projection(p, delta)
    rho, kappa = 4 * tau, tau / 4

    visible = actors + [ballast, payer]
    visibility: dict[str, Any] = {}
    for target in actors + [ballast]:
        h = [Z] * n
        for i in visible:
            h[i] = Z if i == target else O
        h[v] = dot(p[v], h)
        assert_fixed_values(p, h)
        far = [i for i in range(n) if l1(p[i], p[target]) >= rho]
        margin = min(h[i] for i in far)
        assert margin >= kappa
        visibility[labels[target]] = {"h_values": h, "far_margin": margin}
    h_f = [F(1, 1 + delta)] * n
    h_f[payer] = Z
    h_f[v] = O
    assert_fixed_values(p, h_f)
    assert min(h_f[i] for i in range(n) if l1(p[i], p[payer]) >= rho) >= kappa
    visibility["f"] = {"h_values": h_f, "far_margin": F(1, 1 + delta)}

    tstar = delta / (1 + delta)
    h_v = [Z] * n
    for i in actors + [ballast]:
        h_v[i] = tstar
    h_v[payer] = O
    assert_fixed_values(p, h_v)
    assert tstar < kappa

    closest = [Z] * n
    for i in actors + [ballast]:
        closest[i] = p[v][i] / (1 + delta)
    H = 2 * delta
    assert l1(p[v], closest) == H
    y = [Z] * n
    for i in actors + [ballast]:
        y[i] = O
    y[payer] = -O
    phi = [dot(y, row) - O for row in p]
    assert phi[v] == H and all(phi[i] <= Z for i in visible)

    # Quotient A, q_A, and exact ray formula certificate.
    S = F(1, 4)
    mu = [F(1, m)] * m
    qA = convex(mu, [p[i] for i in actors])
    assert sum((max(p[v][i], Z) for i in actors), Z) == S
    G = [i for i in range(n) if l1(p[i], p[v]) >= rho and Z > H - 8 * tau]
    Sh = [i for i in range(n) if Z <= H - 8 * tau]
    assert not Sh and set(actors).issubset(G)
    ray_lambda, ray_c = F(3), p[ballast]
    ray_vec = add(sub(p[v], qA), scale(ray_lambda, sub(p[v], ray_c)))
    ray_obj = l1(ray_vec) - ray_lambda * H
    z_lower = dot(y, sub(p[v], qA))
    Zvalue = 2 * delta
    assert ray_obj == z_lower == Zvalue

    omega_indices = [i for i in G if p[v][i] > Z]
    assert omega_indices == actors + [ballast]
    M = 1 + delta
    weights = [p[v][i] / M for i in omega_indices]
    r = convex(weights, [p[i] for i in omega_indices])
    drift = l1(r, p[v])
    assert drift == 2 * delta < F(1, 8)
    width, signs = exact_scalar_width(weights)
    width_formula = (3 + 4 * delta) / (4 * (1 + delta) ** 2)
    assert width == width_formula >= F(1, 16)

    # Use the exact optimizer to form the two conditional barycenters and
    # verify C(b)'s weighted chord, not merely the width value.
    plus = [j for j, s in enumerate(signs) if s == 1]
    minus = [j for j, s in enumerate(signs) if s == -1]
    splus = sum((weights[j] for j in plus), Z)
    sminus = sum((weights[j] for j in minus), Z)
    assert splus > Z and sminus > Z and splus + sminus == O
    qplus = convex([weights[j] / splus for j in plus], [p[omega_indices[j]] for j in plus])
    qminus = convex([weights[j] / sminus for j in minus], [p[omega_indices[j]] for j in minus])
    chord = splus * sminus * l1(qplus, qminus)
    assert chord == width / 2 >= F(1, 32)
    D0 = 2 + 4 * delta
    pre_fold_floor = M / (64 * D0) - 2 * M * delta

    # Reconstruct C(b)'s actual level-set engine for the chord endpoints.
    chord_L = l1(qplus, qminus)
    norm_sign = [F(1 if a > b else -1 if a < b else 0)
                 for a, b in zip(qplus, qminus)]
    chi = [dot(norm_sign, sub(row, qminus)) / chord_L for row in p]
    ell_fib = l1(sub(qplus, qminus))  # singleton full fibers here
    Alev = O / (2 * ell_fib)
    engine_F = [i for i, value in enumerate(chi) if abs(value) > Alev]
    assert Alev > Z and ell_fib > Z
    endpoint_finance = sum((max(qplus[i], Z) + max(qminus[i], Z)
                            for i in engine_F), Z)
    endpoint_floor = chord_L / (2 * D0) - 2 * delta
    assert endpoint_finance >= endpoint_floor
    Tomega = sum((p[v][i] * sum((max(p[i][j], Z) for j in engine_F), Z)
                  for i in omega_indices), Z)
    top_F = sum((max(p[v][j], Z) for j in engine_F), Z)
    assert Tomega >= pre_fold_floor and top_F >= pre_fold_floor

    # For every ||c-p_v||<=1/4, reverse triangle inequality places every
    # selected actor in E_c.  This is an exact uniform certificate.
    center_distance_lower = min(l1(p[i], p[v]) for i in actors) - F(1, 4)
    assert center_distance_lower > F(1, 2)
    local_floor = tau * S / 16
    assert S >= local_floor and Z < local_floor
    assert H - 16 * tau < Z

    return {
        "id": f"C_width_bouquet_m{m}_tau_1_{tau.denominator}",
        "classification": "best_near_miss_not_L5_datum",
        "labels": labels, "matrix": p, "delta": delta, "tau": tau,
        "fibers": [{"row_point": labels[i], "indices": [i]} for i in range(n)],
        "visible_set": [labels[i] for i in visible],
        "visibility_certificates": visibility,
        "hidden_top_certificate": {"v": "v", "t_star": tstar, "h_values": h_v},
        "height_certificate": {"H": H, "closest_point": closest, "dual_y": y,
                               "phi_values": phi, "H_minus_16tau": H - 16 * tau},
        "selected_submeasure": {"A": [labels[i] for i in actors], "S": S,
                                "mu": mu, "q_A": qA},
        "geography": {"G_v": [labels[i] for i in G], "Sh_v": []},
        "ray_formula": {"Z_v(q_A)": Zvalue, "Z_over_tau": Zvalue / tau,
                        "Lambda": ray_lambda, "c": ray_c, "ray_vector": ray_vec,
                        "ray_objective": ray_obj, "dual_y_value": z_lower},
        "local_center_antecedent": {
            "forall_c_actor_distance_lower": center_distance_lower,
            "forall_c_cotop_mass_lower": S, "required_tauS_over_16": local_floor,
            "cotop_margin": S - local_floor, "forall_c_shallow_mass_upper": Z,
            "shallow_strict_margin": local_floor,
        },
        "omega": {"indices": [labels[i] for i in omega_indices], "M": M,
                  "weights": weights, "r_omega": r, "drift": drift,
                  "drift_branch": drift >= F(1, 8), "Omega": width,
                  "width_branch": width >= F(1, 16), "optimizer_signs": signs,
                  "s_plus": splus, "s_minus": sminus, "q_plus": qplus,
                  "q_minus": qminus, "weighted_chord": chord,
                  "weighted_chord_margin": chord - F(1, 32),
                  "engine_norming_sign": norm_sign, "engine_chi_values": chi,
                  "engine_A_level": Alev,
                  "engine_F": [labels[i] for i in engine_F],
                  "endpoint_joint_positive_mass_F": endpoint_finance,
                  "endpoint_financing_floor": endpoint_floor,
                  "T_omega_F": Tomega, "P_v_positive_F": top_F,
                  "C_b_pre_foldback_floor": pre_fold_floor,
                  "pre_foldback_margin": Tomega - pre_fold_floor},
        "failed_gates": {"H>16tau": False, "H_minus_16tau": H - 16 * tau},
    }


def c_drift_routing_attempt(tau: F, u: F) -> dict[str, Any]:
    """Factorized attempt to route ballast to a near transient row.

    The b anchor pays the reusable routing column.  BL=I forces negative
    coefficients -u/8 on both actor columns, hence nu_b=u/4 exactly.
    """
    delta = tau * tau
    lv = [F(1, 8), F(1, 8), F(3, 4) + delta, -delta]
    lx = [F(1, 8), F(1, 8), F(3, 4), Z]
    L = [lv, [O, Z, Z, Z], [Z, O, Z, Z], [Z, Z, O, Z],
         [Z, Z, Z, O], lx]
    # B rows correspond to q+,q-,b,f.  Only the b row owns x with mass u.
    B = [
        [Z, O, Z, Z, Z, Z],
        [Z, Z, O, Z, Z, Z],
        [Z, -u/8, -u/8, O - 3*u/4, Z, u],
        [Z, Z, Z, Z, O, Z],
    ]
    I4 = [[O if i == j else Z for j in range(4)] for i in range(4)]
    assert matmul(B, L) == I4
    p = matmul(L, B)
    assert_projection(p)
    nu_b = neg_mass(p[3])
    assert nu_b == u / 4
    actual = delta_of(p)
    assert actual >= nu_b
    legal_u_max = 4 * delta
    if u > legal_u_max:
        assert actual > delta
    # x is genuinely near v in the target metric whenever the target budget
    # is respected; this checks that the intended receiver is geometrically
    # the right kind, even though not enough mass can be routed to it.
    near_distance = l1(p[0], p[5])
    if u <= legal_u_max:
        assert near_distance < 4 * tau
    top_x_mass = max(p[0][5], Z)
    legal_top_x_upper = (F(3, 4) + delta) * legal_u_max
    return {
        "tau": tau, "target_delta": delta, "routing_parameter_u": u,
        "L": L, "B": B, "BL": matmul(B, L), "matrix": p,
        "actual_global_delta": actual, "ballast_row_negative_mass_u_over_4": nu_b,
        "legal_u_max_4delta": legal_u_max,
        "negativity_margin": actual - delta,
        "v_to_transient_x_distance": near_distance,
        "top_positive_mass_on_x": top_x_mass,
        "legal_top_x_mass_upper": legal_top_x_upper,
        "drift_branch_reached": False,
        "binding_inequality": "u/4 <= tau^2, so u <= 4 tau^2 and only O(tau^2) ballast can be routed",
    }


def build() -> dict[str, Any]:
    taus = [F(1, 32), F(1, 64), F(1, 128), F(1, 256)]
    ratios = [F(20), F(18), F(17), F(33, 2), F(16)]
    s_seeds = [s_base_seed(t) for t in taus]
    s_sweep = [s_height_dial(F(1, 256), r) for r in ratios]
    s_budgets = [s_attachment_budget(t) for t in taus]
    c_width = [c_width_bouquet(4, t) for t in taus]
    c_drift_legal = [c_drift_routing_attempt(t, 4*t*t) for t in taus]
    c_drift_forced = [c_drift_routing_attempt(t, F(1)) for t in taus]

    # Sequence-level asymptotics are checked as exact monotonic statements.
    assert all(s_seeds[i+1]["H_over_tau"] < s_seeds[i]["H_over_tau"]
               for i in range(len(s_seeds)-1))
    assert all(c_width[i+1]["ray_formula"]["Z_over_tau"] <
               c_width[i]["ray_formula"]["Z_over_tau"]
               for i in range(len(c_width)-1))
    assert all(c_width[i]["omega"]["width_branch"] for i in range(len(c_width)))
    assert not any(c_width[i]["omega"]["drift_branch"] for i in range(len(c_width)))
    return {
        "schema": "w63-sc-deciders-exact-v1",
        "arithmetic": "Every numeric invariant is serialized from fractions.Fraction.",
        "rigour_scope": "L3 constructive/numerical evidence only; never a proof.",
        "verdicts": {"S": "BLOCKED", "C": "BLOCKED"},
        "shape_S": {
            "family": "W61 factorization plus exact C/D clone receiver attachment",
            "base_seed_sequence": s_seeds,
            "height_ratio_sweep_tau_1_256": s_sweep,
            "attachment_budget_sequence": s_budgets,
            "binding_inequalities": [
                "H=2 eps t*/(1+eps-eps t*) with hiddenness t*<tau/4",
                "m_sh=tau S/16 > tau^2-q for S=1/4",
                "adding the actor and shallow clone pairs gives nu_A=q+S+m_sh>tau^2",
            ],
        },
        "shape_C": {
            "family": "two-prong corank-one bouquet plus transient-ballast drift routing",
            "width_branch_sequence": c_width,
            "drift_branch_legal_budget_sequence": c_drift_legal,
            "drift_branch_forced_routing_sequence": c_drift_forced,
            "binding_inequalities": [
                "width bouquet: H=2 tau^2, hence H-16tau<0",
                "drift routing: nu_b=u/4<=tau^2 forces u<=4tau^2",
            ],
        },
        "genuine_L5_data_found": 0,
        "I_bycatch_found": 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="certificates.json")
    args = parser.parse_args()
    data = build()
    out = Path(args.output)
    out.write_text(json.dumps(qstr(data), indent=2) + "\n")
    # Round-trip and rational-string presence audit.
    frozen = json.loads(out.read_text())
    assert frozen["verdicts"] == {"S": "BLOCKED", "C": "BLOCKED"}
    assert frozen["genuine_L5_data_found"] == 0
    print("S: BLOCKED — hiddenness/negative-mass inequalities bind exactly.")
    print("C: BLOCKED — width near-refuter fails only tallness; drift routing fails negativity.")
    print("EXACT CHECKS PASSED; L3 EVIDENCE ONLY — this computation is not a proof.")


if __name__ == "__main__":
    main()
