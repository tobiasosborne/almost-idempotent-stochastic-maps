#!/usr/bin/env python3
"""W62 node-I exact-rational refuter search and certificate verifier.

This is an L3 computation.  It constructs exact signed projections and checks
all claimed identities with fractions.Fraction.  A successful run is only a
verification of the finite certificates below; it is not a proof of node I or
of any obstruction beyond the explicitly parameterized families.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable, Sequence


ZERO = F(0)
ONE = F(1)


def dot(x: Sequence[F], y: Sequence[F]) -> F:
    return sum((a * b for a, b in zip(x, y)), ZERO)


def add(x: Sequence[F], y: Sequence[F]) -> list[F]:
    return [a + b for a, b in zip(x, y)]


def sub(x: Sequence[F], y: Sequence[F]) -> list[F]:
    return [a - b for a, b in zip(x, y)]


def scale(a: F, x: Sequence[F]) -> list[F]:
    return [a * b for b in x]


def convex(weights: Sequence[F], points: Sequence[Sequence[F]]) -> list[F]:
    assert len(weights) == len(points) and sum(weights, ZERO) == ONE
    return [sum((weights[i] * points[i][j] for i in range(len(points))), ZERO)
            for j in range(len(points[0]))]


def l1(x: Sequence[F], y: Sequence[F] | None = None) -> F:
    if y is None:
        return sum((abs(a) for a in x), ZERO)
    return sum((abs(a - b) for a, b in zip(x, y)), ZERO)


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    bt = list(zip(*b))
    return [[dot(row, col) for col in bt] for row in a]


def matvec(a: Sequence[Sequence[F]], x: Sequence[F]) -> list[F]:
    return [dot(row, x) for row in a]


def neg_mass(row: Sequence[F]) -> F:
    return sum((-x for x in row if x < 0), ZERO)


def delta_of(p: Sequence[Sequence[F]]) -> F:
    return max(neg_mass(row) for row in p)


def assert_projection(p: Sequence[Sequence[F]], claimed_delta: F) -> None:
    n = len(p)
    assert n > 0 and all(len(row) == n for row in p)
    assert all(sum(row, ZERO) == ONE for row in p)
    assert matmul(p, p) == [list(row) for row in p]
    assert delta_of(p) == claimed_delta


def assert_h_values(p: Sequence[Sequence[F]], h: Sequence[F]) -> None:
    """On row points, affine-value vectors are exactly fixed vectors P h=h."""
    assert matvec(p, h) == list(h)
    assert all(ZERO <= x <= ONE for x in h)


def far_set(p: Sequence[Sequence[F]], v: int, rho: F) -> list[int]:
    return [i for i in range(len(p)) if l1(p[i], p[v]) >= rho]


def qstr(x: Any) -> Any:
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, dict):
        return {k: qstr(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [qstr(v) for v in x]
    return x


def simplex_local_family(m: int, tau: F, shape: str) -> dict[str, Any]:
    """Corank-one simplex near-miss.

    Index 0 is v; indices 1..m are fan actors; m+1 is positive
    ballast b; m+2 is the negative financier f.  All rows except v are
    coordinate rows.  The top row has actor mass 1/(4m), ballast mass
    3/4+delta, and financier coefficient -delta.
    """
    assert shape in {"spike", "fan"}
    assert m >= 1 and ZERO < tau <= F(1, 8)
    delta = tau * tau
    rho, kappa = 4 * tau, tau / 4
    n = m + 3
    v = 0
    actors = list(range(1, m + 1))
    ballast, financier = m + 1, m + 2
    labels = ["v"] + [f"q{i}" for i in range(1, m + 1)] + ["b", "f"]

    p = [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    p[v] = [ZERO] * n
    for i in actors:
        p[v][i] = F(1, 4 * m)
    p[v][ballast] = F(3, 4) + delta
    p[v][financier] = -delta
    assert_projection(p, delta)

    # All coordinate rows are vertices and visible.  These exact affine-value
    # vectors exhibit their margins.  The row v is the sole hidden vertex.
    visible = actors + [ballast, financier]
    visibility: dict[str, Any] = {}
    for target in actors + [ballast]:
        h = [ZERO] * n
        for i in visible:
            h[i] = ZERO if i == target else ONE
        h[v] = dot(p[v], h)
        assert_h_values(p, h)
        far = far_set(p, target, rho)
        margin = min(h[i] for i in far)
        assert margin >= kappa
        assert h[target] == 0 and all(h[i] > 0 for i in range(n) if i != target)
        visibility[labels[target]] = {"h_values": h, "far_margin": margin}

    h_f = [ZERO] * n
    for i in actors + [ballast]:
        h_f[i] = ONE / (ONE + delta)
    h_f[financier] = ZERO
    h_f[v] = ONE
    assert_h_values(p, h_f)
    far_f = far_set(p, financier, rho)
    margin_f = min(h_f[i] for i in far_f)
    assert margin_f >= kappa
    visibility[labels[financier]] = {"h_values": h_f, "far_margin": margin_f}

    hidden_margin = delta / (ONE + delta)
    h_v = [ZERO] * n
    for i in actors + [ballast]:
        h_v[i] = hidden_margin
    h_v[financier] = ONE
    h_v[v] = ZERO
    assert_h_values(p, h_v)
    far_v = far_set(p, v, rho)
    assert set(actors + [ballast, financier]).issubset(far_v)
    assert min(h_v[i] for i in far_v) == hidden_margin
    # Upper certificate: 0=h(v)=sum_pos w_i h_i-delta*h_f, so the
    # positive weighted average is <= delta and one positive far row has
    # h_i <= delta/(1+delta).
    assert sum((p[v][i] for i in actors + [ballast]), ZERO) == ONE + delta
    assert hidden_margin < kappa

    # Height H=2 delta: normalize the positive part for a primal closest
    # point and use the sign vector y for the matching l1 dual certificate.
    closest = [ZERO] * n
    for i in actors + [ballast]:
        closest[i] = p[v][i] / (ONE + delta)
    assert sum(closest, ZERO) == ONE and all(closest[i] >= 0 for i in visible)
    height = 2 * delta
    assert l1(p[v], closest) == height
    y = [ZERO] * n
    for i in actors + [ballast]:
        y[i] = ONE
    y[financier] = -ONE
    dual_constant = -ONE
    assert max(abs(a) for a in y) == ONE
    phi = [dot(y, row) + dual_constant for row in p]
    assert phi[v] == height
    assert all(phi[i] <= 0 for i in visible)
    assert all(l1(row, closest) <= height for row in [p[v]])

    # Singleton full fibers.  A is either the one spike actor (m=1) or all
    # fan actors.  Its quotient barycenter is the uniform actor point.
    selected = [actors[0]] if shape == "spike" else actors
    mass = sum((max(p[v][i], ZERO) for i in selected), ZERO)
    expected_mass = F(1, 4) if shape == "fan" or m == 1 else F(len(selected), 4 * m)
    assert mass == expected_mass
    mu = [max(p[v][i], ZERO) / mass for i in selected]
    q_a = convex(mu, [p[i] for i in selected])
    if shape == "fan":
        assert all(x == F(1, m) for x in mu)
        assert all(p[v][i] == F(1, 4 * m) for i in actors)
    else:
        assert p[v][selected[0]] == F(1, 4)

    # Every selected actor is far/deep.  Since H-8tau<0 and C_W is the
    # coordinate simplex, Sh is empty and every visible row is deep.
    assert height - 8 * tau < 0
    distances_to_cw = [height] + [ZERO] * (n - 1)
    g_set = [i for i in range(n)
             if l1(p[i], p[v]) >= rho and distances_to_cw[i] > height - 8 * tau]
    sh_set = [i for i in range(n) if distances_to_cw[i] <= height - 8 * tau]
    assert not sh_set
    assert set(selected).issubset(g_set)

    # The true Z is bracketed exactly: y is dual feasible and the ray pair
    # Lambda=3,c=e_b has exactly the same objective 2 delta.
    h_c = max(y[i] for i in visible)
    assert dot(y, p[v]) - h_c == height
    z_lower = dot(y, sub(p[v], q_a))
    ray_lambda = F(3)
    ray_c = p[ballast]
    ray_vec = add(sub(p[v], q_a), scale(ray_lambda, sub(p[v], ray_c)))
    ray_objective = l1(ray_vec) - ray_lambda * height
    z_value = 2 * delta
    assert z_lower == z_value == ray_objective

    # omega is the complete positive top measure on G.  Its barycenter is
    # the normalized positive part, and the drift is exactly 2 delta.
    omega_indices = [i for i in g_set if p[v][i] > 0]
    omega_mass = sum((p[v][i] for i in omega_indices), ZERO)
    assert omega_indices == actors + [ballast]
    assert omega_mass == ONE + delta
    omega_weights = [p[v][i] / omega_mass for i in omega_indices]
    r_omega = convex(omega_weights, [p[i] for i in omega_indices])
    drift = l1(r_omega, p[v])
    assert r_omega == closest and drift == 2 * delta < F(1, 8)

    # Exact Omega.  On these coordinate points an affine 1-Lipschitz
    # functional has freely chosen values in [-1,1].  Convexity puts a
    # maximizer at a sign vector, so finite sign enumeration is exact.
    omega_width = ZERO
    width_signs: tuple[int, ...] | None = None
    for signs in itertools.product((-1, 1), repeat=len(omega_indices)):
        mean = sum((w * s for w, s in zip(omega_weights, signs)), ZERO)
        mad = sum((w * abs(F(s) - mean) for w, s in zip(omega_weights, signs)), ZERO)
        if mad > omega_width:
            omega_width, width_signs = mad, signs
    width_formula = (3 + 4 * delta) / (4 * (ONE + delta) ** 2)
    assert omega_width == width_formula and width_signs is not None

    # For every c with ||c-p_v||_1<=1/4, reverse triangle inequality puts
    # every selected actor strictly outside B_1(c,1/2).  Hence the exact
    # selected mass itself is a center-uniform co-top lower certificate.
    actor_separation = min(l1(p[i], p[v]) for i in selected) - F(1, 4)
    assert actor_separation > F(1, 2)
    local_cotop_mass_lower = mass
    local_floor = tau * mass / 16
    assert ZERO < local_floor < local_cotop_mass_lower
    shallow_mass_upper = ZERO
    assert shallow_mass_upper < local_floor

    tall_margin = height - 16 * tau
    assert tall_margin < 0

    return {
        "id": f"simplex_{shape}_m{m}_tau_{tau.denominator}",
        "classification": "best_near_miss_not_L5_datum",
        "labels": labels,
        "matrix": p,
        "parameters": {"m": m, "tau": tau, "delta": delta, "rho": rho,
                       "kappa": kappa, "c_m": F(1, 4)},
        "fibers": [{"row_point": labels[i], "indices": [i]} for i in range(n)],
        "visible_set": [labels[i] for i in visible],
        "visibility_certificates": visibility,
        "hidden_top_candidate": {
            "v": "v", "t_star": hidden_margin, "h_values": h_v,
            "upper_identity": "sum_positive(P_vj*h_j)=delta*h_f<=delta",
        },
        "height_certificate": {
            "H": height, "closest_point": closest, "dual_y": y,
            "dual_constant": dual_constant, "phi_values": phi,
            "H_minus_16tau": tall_margin,
        },
        "selected_submeasure": {
            "A": [labels[i] for i in selected], "fiber_masses": [p[v][i] for i in selected],
            "S": mass, "mu": mu, "q_A": q_a,
        },
        "geography": {
            "G_v": [labels[i] for i in g_set], "Sh_v": [labels[i] for i in sh_set],
            "dist_to_CW": distances_to_cw,
        },
        "ray_formula_certificate": {
            "Z_v(q_A)": z_value, "Z_over_tau": z_value / tau,
            "Lambda": ray_lambda, "c": ray_c, "ray_vector": ray_vec,
            "ray_objective": ray_objective, "dual_y_value": z_lower,
        },
        "omega_certificate": {
            "indices": [labels[i] for i in omega_indices], "mass": omega_mass,
            "weights": omega_weights, "r_omega": r_omega, "drift": drift,
            "Omega": omega_width, "Omega_optimizer_signs": list(width_signs),
            "Omega_minus_1/16": omega_width - F(1, 16),
        },
        "local_center_certificate": {
            "actor_distance_after_1/4_shift_lower": actor_separation,
            "forall_c_cotop_mass_lower": local_cotop_mass_lower,
            "required_cotop_floor_tauS/16": local_floor,
            "cotop_margin": local_cotop_mass_lower - local_floor,
            "forall_c_shallow_mass_upper": shallow_mass_upper,
            "required_shallow_strict_ceiling_tauS/16": local_floor,
        },
        "failed_gates": {
            "H>16tau": False,
            "H_minus_16tau": tall_margin,
            "Omega<1/16": omega_width < F(1, 16),
        },
    }


def graft_matrix(k: int) -> list[list[F]]:
    tau = F(1, k)
    delta = tau * tau
    t0 = tau / 8
    u = [ONE, ZERO, ZERO, ZERO, ZERO, ZERO]
    z = [ONE + delta * (ONE - t0), ZERO, delta * t0,
         -delta / 2, -delta / 4, -delta / 4]
    o = [ZERO, ZERO, ONE, ZERO, ZERO, ZERO]
    a = [ZERO, ZERO, ZERO, F(1, 2), F(1, 4), F(1, 4)]
    x = add(scale(delta, o), scale(ONE - delta, a))
    y = add(scale(-delta, o), scale(ONE + delta, a))
    return [u, z, o, a, x, y]


def verify_graft(k: int) -> dict[str, Any]:
    p = graft_matrix(k)
    tau, delta, t0 = F(1, k), F(1, k * k), F(1, 8 * k)
    rho, kappa = 4 * tau, tau / 4
    assert_projection(p, delta)
    labels = ["u", "z", "o", "a", "x", "y"]
    u, z, o, a, x, yrow = range(6)

    h_u = [ZERO, ZERO, ONE, t0,
           delta + (ONE - delta) * t0,
           -delta + (ONE + delta) * t0]
    assert_h_values(p, h_u)
    hidden_margin = h_u[yrow]
    assert hidden_margin == t0 - delta * (ONE - t0) < kappa
    assert min(h_u[i] for i in far_set(p, u, rho)) == hidden_margin
    # Upper identity: h_z>=0 gives h_a<=t0*h_o, and
    # h_y=(1+delta)h_a-delta*h_o <= hidden_margin.

    h_z = [delta * (ONE - t0) / (ONE + delta * (ONE - t0)),
           ZERO, ONE, ONE, ONE, ONE]
    h_o = [ONE, ZERO, ZERO, ONE / (ONE + delta),
           (ONE - delta) / (ONE + delta), ONE]
    h_o[z] = dot(p[z], h_o)
    h_y = [ZERO, ONE, ONE, delta / (ONE + delta),
           2 * delta / (ONE + delta), ZERO]
    numerator = ONE - delta * t0 + delta * delta / (ONE + delta)
    h_y[u] = numerator / (ONE + delta * (ONE - t0))
    exposers = {"z": h_z, "o": h_o, "y": h_y}
    visibility = {}
    for name, h in exposers.items():
        target = labels.index(name)
        assert_h_values(p, h)
        margin = min(h[i] for i in far_set(p, target, rho))
        assert margin >= kappa
        visibility[name] = {"h_values": h, "far_margin": margin}

    # a and x are on [o,y], so the visible hull is conv{z,o,y}.
    assert p[a] == convex([delta / (ONE + delta), ONE / (ONE + delta)], [p[o], p[yrow]])
    assert p[x] == convex([2 * delta / (ONE + delta), (ONE - delta) / (ONE + delta)],
                          [p[o], p[yrow]])
    alpha = (ONE + delta) / (ONE + 2 * delta)
    closest = convex([alpha, ONE - alpha], [p[z], p[yrow]])
    height = l1(p[u], closest)
    r = (ONE - 2 * delta * t0) / (ONE + 2 * delta)
    dual_y = [ONE, ZERO, -ONE, r, r, r]
    dual_constant = -dot(dual_y, p[z])
    phi = [dot(dual_y, row) + dual_constant for row in p]
    assert max(abs(q) for q in dual_y) == ONE
    assert phi[z] == phi[yrow] == ZERO and phi[o] <= 0
    assert phi[u] == height
    assert all(phi[i] <= 0 for i in [z, o, a, x, yrow])
    tall_margin = height - 16 * tau
    assert tall_margin < 0

    return {
        "id": f"w61_thin_transient_graft_k{k}",
        "classification": "seed_near_miss_not_tall",
        "labels": labels, "matrix": p,
        "parameters": {"k": k, "tau": tau, "delta": delta, "t0": t0,
                       "rho": rho, "kappa": kappa},
        "visible_set": ["z", "o", "y"],
        "visibility_certificates": visibility,
        "hiddenness_certificate": {
            "v": "u", "t_star": hidden_margin, "h_values": h_u,
            "upper_identity": "h_z>=0 => h_a<=t0*h_o => h_y<=t0-delta*(1-t0)",
        },
        "height_certificate": {
            "H": height, "closest_weights_on_z_y": [alpha, ONE - alpha],
            "closest_point": closest, "dual_y": dual_y,
            "dual_constant": dual_constant, "phi_values": phi,
            "H_minus_16tau": tall_margin,
        },
    }


def verify_financer_k16() -> dict[str, Any]:
    k = 16
    tau = F(1, 2**k)
    delta, eps = tau * tau, tau * tau / 2
    tstar, kappa, rho = tau / 8, tau / 4, 4 * tau
    eta = eps * tstar
    big_k = ONE + delta - eta
    q = eps / (big_k - eps)
    theta = F(4503599627894783, 1180591620992288948224)
    arow = [ONE + q, -q, ZERO, ZERO, ZERO, ZERO]
    zrow = [big_k, -eps, ZERO, eta, -eps, ZERO]
    crow = [ZERO, ZERO, ZERO, ONE, ZERO, ZERO]
    drow = [ZERO, ZERO, ZERO, ZERO, ONE, ZERO]
    xrow = add(scale(ONE - theta, arow), scale(theta, crow))
    p = [arow, arow[:], zrow, crow, drow, xrow]
    labels = ["a0", "a1", "z", "c", "d", "x"]
    assert_projection(p, delta)

    h_a = [ZERO, ZERO, ZERO, ONE, tstar, theta]
    assert_h_values(p, h_a)
    assert min(h_a[i] for i in far_set(p, 0, rho)) == tstar < kappa
    # Exact hiddenness upper witness: (D-A)+(1/eps)(Z-A)=tstar(C-A).
    balance_left = add(sub(p[4], p[0]), scale(ONE / eps, sub(p[2], p[0])))
    balance_right = scale(tstar, sub(p[3], p[0]))
    assert balance_left == balance_right

    h_z_a = (eps - eta) / (big_k - eps)
    h_z = [h_z_a, h_z_a, ZERO, ONE, ONE,
           (ONE - theta) * h_z_a + theta]
    h_c = [ONE, ONE, ONE - eta, ZERO, ONE, ONE - theta]
    h_d_a = (ONE - eta) / (big_k - eps)
    h_d = [h_d_a, h_d_a, ONE, ONE, ZERO,
           (ONE - theta) * h_d_a + theta]
    visibility = {}
    for target, h in [(2, h_z), (3, h_c), (4, h_d)]:
        assert_h_values(p, h)
        margin = min(h[i] for i in far_set(p, target, rho))
        assert margin >= kappa
        visibility[labels[target]] = {"h_values": h, "far_margin": margin}

    # X has the following exact convex representation in C_W.
    x_weights = [
        F(20282332237121568059768013062144, 20282409610735211141602218606593),
        F(77371252468847048883437567, 20282409610735211141602218606593),
        F(2361174234785322106882, 20282409610735211141602218606593),
    ]
    assert convex(x_weights, [p[2], p[3], p[4]]) == p[5]
    wz = ONE / (big_k - eps)
    wd = ONE - wz
    assert wz >= 0 and wd >= 0
    closest = convex([wz, wd], [p[2], p[4]])
    height = 2 * eta / (big_k - eps)
    assert l1(p[0], closest) == height
    dual_y = [ONE, ONE - 2 * tstar, ZERO, -ONE, ONE, ZERO]
    dual_constant = -ONE
    phi = [dot(dual_y, row) + dual_constant for row in p]
    assert max(abs(a) for a in dual_y) == ONE
    assert phi[0] == phi[1] == height
    assert all(phi[i] <= 0 for i in [2, 3, 4, 5])
    tall_margin = height - 16 * tau
    assert tall_margin < 0

    return {
        "id": "w61_dyadic_leak_financer_k16",
        "classification": "seed_near_miss_not_tall",
        "labels": labels, "matrix": p,
        "fibers": [
            {"row_point": "A", "indices": [0, 1]},
            {"row_point": "Z", "indices": [2]},
            {"row_point": "C", "indices": [3]},
            {"row_point": "D", "indices": [4]},
            {"row_point": "X", "indices": [5]},
        ],
        "parameters": {"k": k, "tau": tau, "delta": delta, "eps": eps,
                       "t_star_A": tstar, "rho": rho, "kappa": kappa,
                       "eta": eta, "K": big_k, "q": q, "theta": theta},
        "visible_set": ["Z", "C", "D"],
        "visibility_certificates": visibility,
        "hiddenness_certificate": {
            "v": "A", "t_star": tstar, "h_values": h_a,
            "witness": {"lambda_D": ONE, "alpha_Z": ONE / eps, "beta_C": tstar},
            "balance_left": balance_left, "balance_right": balance_right,
        },
        "height_certificate": {
            "H": height, "closest_weights_on_Z_D": [wz, wd],
            "closest_point": closest, "dual_y": dual_y,
            "dual_constant": dual_constant, "phi_values": phi,
            "X_weights_on_Z_C_D": x_weights, "H_minus_16tau": tall_margin,
        },
    }


def w55_coordinate_attempt() -> dict[str, Any]:
    """Pinned W55 A=5 scalar tableau and the canonical rank-three attempt.

    The scalar reproduction is exact.  The most direct left inverse makes the
    finance row pay a coefficient -A on the z fiber, so it fails the global
    negativity gate by an exact margin.  This is only one concrete attempted
    completion; the separately proved bounded-slab obstruction has wider scope.
    """
    tau, t, A = F(1, 256), F(1, 65536), F(5)
    a = tau / (ONE + tau)
    # Affine coordinates p=p_v+xD+yE, written as (1-x-y,x,y).
    coords = [
        [ONE, ZERO, ZERO],
        [ONE + A * a - a * t, -A * a, a * t],
        [ONE + A - t, -A, t],
        [ZERO, ONE, ZERO],
        [ZERO, ZERO, ONE],
    ]
    labels = ["v", "w", "f", "z", "o"]
    b0 = [ONE - tau, tau + t, -t, ZERO, ZERO]
    b1 = [ZERO, ZERO, ZERO, ONE, ZERO]
    b2 = [ZERO, ZERO, ZERO, ZERO, ONE]
    b = [b0, b1, b2]
    assert matmul(b, coords) == [[ONE, ZERO, ZERO], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]]
    p = matmul(coords, b)
    assert all(sum(row, ZERO) == ONE for row in p)
    assert matmul(p, p) == p
    assert p[0] == b0
    # Exact top reproduction in the pinned scalar tableau.
    assert (tau + t) * a == t
    assert add(scale(tau + t, sub(p[1], p[0])),
               scale(-t, sub(p[2], p[0]))) == [ZERO] * 5
    row_negative_masses = [neg_mass(row) for row in p]
    expected_f = A + (ONE + A - t) * t
    assert row_negative_masses[2] == expected_f
    global_delta = max(row_negative_masses)
    assert global_delta == expected_f > t
    negativity_margin = global_delta - t

    return {
        "id": "w55_A5_g5tau_canonical_rank3_attempt_tau_1_256",
        "classification": "failed_completion_global_negativity_gate",
        "labels": labels, "matrix": p, "affine_coordinates": coords,
        "parameters": {"A0": A, "g": A * tau, "tau": tau, "target_delta": t,
                       "a": a},
        "top_fiber_coefficients": {"v": ONE - tau, "w": tau + t, "f": -t},
        "row_negative_masses": row_negative_masses,
        "actual_global_delta": global_delta,
        "global_delta_minus_target_tau2": negativity_margin,
        "binding_identity": "nu_f=A+(1+A-t)*t in the canonical disjoint-support left inverse",
        "proved_family_obstruction_consulted": "lem-starvation-completion-obstruction",
    }


def build_certificates() -> dict[str, Any]:
    spike_sweep = [simplex_local_family(1, F(1, k), "spike") for k in (32, 64, 128, 256)]
    fan_specs = [(3, F(1, 64)), (4, F(1, 128)), (8, F(1, 256))]
    fan_sweep = [simplex_local_family(m, tau, "fan") for m, tau in fan_specs]
    graft_sweep = [verify_graft(k) for k in (512, 1024, 2048)]
    financer = verify_financer_k16()
    w55 = w55_coordinate_attempt()

    # delta tends to zero on the displayed rational parameter sequences; the
    # finite sweep records decreasing samples and the formulas above are valid
    # for every allowed denominator.
    assert all(spike_sweep[i + 1]["parameters"]["delta"] < spike_sweep[i]["parameters"]["delta"]
               for i in range(len(spike_sweep) - 1))
    assert all(fan_sweep[i + 1]["parameters"]["delta"] < fan_sweep[i]["parameters"]["delta"]
               for i in range(len(fan_sweep) - 1))

    return {
        "schema": "w62-I-horn-exact-L3-v1",
        "warning": "L3 exact constructive/numerical evidence only; no entry is a proof.",
        "verdicts": {
            "heavy_summit_axis_spike": "BLOCKED_IN_ATTEMPTED_FAMILY_BY_H_EQUALS_2DELTA",
            "growing_low_width_dual_simplex_fan": "BLOCKED_IN_ATTEMPTED_FAMILY_BY_OMEGA_AND_TALLNESS",
            "tall_seed_completions": "BLOCKED_IN_TESTED_COMPLETION_CLASSES",
        },
        "shape_1": {
            "family": "corank-one simplex spike; exact for every rational tau<=1/8",
            "tested_tau_denominators": [32, 64, 128, 256],
            "best_near_miss": spike_sweep[-1],
            "sweep": [{
                "tau": x["parameters"]["tau"], "delta": x["parameters"]["delta"],
                "H": x["height_certificate"]["H"],
                "H_minus_16tau": x["height_certificate"]["H_minus_16tau"],
                "spike_mass": x["selected_submeasure"]["S"],
                "Z_over_tau": x["ray_formula_certificate"]["Z_over_tau"],
            } for x in spike_sweep],
        },
        "shape_2": {
            "family": "corank-one simplex fan with exact c_m/m actor masses",
            "tested_m_tau": [[m, tau] for m, tau in fan_specs],
            "best_near_miss": fan_sweep[-1],
            "sweep": [{
                "m": x["parameters"]["m"], "tau": x["parameters"]["tau"],
                "delta": x["parameters"]["delta"], "H": x["height_certificate"]["H"],
                "Z_over_tau": x["ray_formula_certificate"]["Z_over_tau"],
                "drift": x["omega_certificate"]["drift"],
                "Omega": x["omega_certificate"]["Omega"],
                "local_floor_margin": x["local_center_certificate"]["cotop_margin"],
            } for x in fan_sweep],
        },
        "shape_3": {
            "graft_tested_k": [512, 1024, 2048],
            "graft_best_near_miss": graft_sweep[-1],
            "graft_sweep": [{
                "k": x["parameters"]["k"], "tau": x["parameters"]["tau"],
                "delta": x["parameters"]["delta"], "H": x["height_certificate"]["H"],
                "H_minus_16tau": x["height_certificate"]["H_minus_16tau"],
            } for x in graft_sweep],
            "financer_tested_context_range": "dyadic exponents k=8..16; k=16 reverified here",
            "financer_best_near_miss": financer,
            "w55_attempt": w55,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true", help="print regenerated certificates JSON")
    parser.add_argument("--no-compare", action="store_true", help="do not compare certificates.json")
    args = parser.parse_args()
    exact = qstr(build_certificates())
    if not args.no_compare:
        path = Path(__file__).with_name("certificates.json")
        with path.open("r", encoding="utf-8") as fh:
            checked_in = json.load(fh)
        assert checked_in == exact, "certificates.json is stale; run search.py --emit and update it"
    if args.emit:
        print(json.dumps(exact, indent=2, sort_keys=False))
    else:
        print("EXACT CHECKS PASSED: 3 BLOCKED-family verdicts; 0 genuine L5 refuters.")
        print("L3 EVIDENCE ONLY — this computation is not a proof.")


if __name__ == "__main__":
    main()
