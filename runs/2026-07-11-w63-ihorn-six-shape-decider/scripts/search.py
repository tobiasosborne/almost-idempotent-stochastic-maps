#!/usr/bin/env python3
"""Exact L3 search for the six W63 I-horn pre-creative shapes.

Every certificate calculation uses fractions.Fraction.  The constructions are
near-misses, not proofs and not genuine I-base data unless every gate says so.
The program writes certificates.json and exits nonzero on an assertion failure.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Sequence

Z, O = F(0), F(1)
CM = F(1, 4)
B = CM / 128                 # 1/512
KB = CM * B / 64             # 1/131072


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


def convex(weights: Sequence[F], points: Sequence[Sequence[F]]) -> list[F]:
    assert weights and len(weights) == len(points) and sum(weights, Z) == O
    return [sum((weights[i] * points[i][j] for i in range(len(points))), Z)
            for j in range(len(points[0]))]


def neg(row: Sequence[F]) -> F:
    return sum((-x for x in row if x < Z), Z)


def delta_of(p: Sequence[Sequence[F]]) -> F:
    return max(neg(row) for row in p)


def assert_projection(p: Sequence[Sequence[F]], delta: F | None = None) -> None:
    assert p and all(len(row) == len(p) for row in p)
    assert all(sum(row, Z) == O for row in p)
    assert matmul(p, p) == [list(row) for row in p]
    if delta is not None:
        assert delta_of(p) == delta


def qstr(x: Any) -> Any:
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, dict):
        return {k: qstr(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [qstr(v) for v in x]
    return x


def scalar_width(weights: Sequence[F]) -> tuple[F, tuple[int, ...]]:
    """Exact affine 1-Lipschitz MAD for coordinate row points."""
    best, arg = Z, tuple()
    for signs in itertools.product((-1, 1), repeat=len(weights)):
        mean = sum((w * s for w, s in zip(weights, signs)), Z)
        val = sum((w * abs(F(s) - mean) for w, s in zip(weights, signs)), Z)
        if val > best:
            best, arg = val, signs
    return best, arg


def simplex_probe(tau: F, shape: str) -> dict[str, Any]:
    """Old coordinate fan, retained only as an exact D/W calibration."""
    m, delta = 4, tau * tau
    n = m + 3
    v, actors, ballast, financier = 0, list(range(1, 5)), 5, 6
    labels = ["v", "q1", "q2", "q3", "q4", "b", "f"]
    p = [[O if i == j else Z for j in range(n)] for i in range(n)]
    p[v] = [Z] * n
    for i in actors:
        p[v][i] = F(1, 16)
    p[v][ballast], p[v][financier] = F(3, 4) + delta, -delta
    assert_projection(p, delta)

    H = 2 * delta
    closest = [Z] * n
    for i in actors + [ballast]:
        closest[i] = p[v][i] / (O + delta)
    assert l1(p[v], closest) == H
    y = [Z] * n
    for i in actors + [ballast]:
        y[i] = O
    y[financier] = -O
    phi = [dot(y, row) - O for row in p]
    assert phi[v] == H and all(phi[i] <= Z for i in actors + [ballast, financier])

    S = CM
    qA = convex([F(1, 4)] * 4, [p[i] for i in actors])
    ray_lambda, ray_c = F(3), p[ballast]
    ray_vec = add(sub(p[v], qA), scale(ray_lambda, sub(p[v], ray_c)))
    ray_obj = l1(ray_vec) - ray_lambda * H
    z_lower = dot(y, sub(p[v], qA))
    assert ray_obj == z_lower == 2 * delta

    # H-8tau<0 makes every coordinate row deep; the positive G restriction
    # is the complete positive part of row v.
    assert H - 8 * tau < Z
    omega_idx = actors + [ballast]
    M = O + delta
    weights = [p[v][i] / M for i in omega_idx]
    r = convex(weights, [p[i] for i in omega_idx])
    drift = l1(r, p[v])
    assert drift == 2 * delta
    width, signs = scalar_width(weights)
    assert width == (3 + 4 * delta) / (4 * (O + delta) ** 2)

    plus = [j for j, s in enumerate(signs) if s == 1]
    minus = [j for j, s in enumerate(signs) if s == -1]
    sp = sum((weights[j] for j in plus), Z)
    sm = sum((weights[j] for j in minus), Z)
    qp = convex([weights[j] / sp for j in plus], [p[omega_idx[j]] for j in plus])
    qm = convex([weights[j] / sm for j in minus], [p[omega_idx[j]] for j in minus])
    chord = sp * sm * l1(qp, qm)
    assert chord == width / 2

    # Uniform all-local-center certificate: every selected actor remains
    # outside the half-ball after any 1/4 center shift.
    center_lower = min(l1(p[i], p[v]) for i in actors) - F(1, 4)
    floor = tau * S / 16
    assert center_lower > F(1, 2) and S > floor > Z

    common_receiver = [i for i in range(n) if i in (v, ballast, financier)]
    common_payment = sum((max(p[v][i], Z) for i in common_receiver), Z)
    assert common_payment == F(3, 4) + delta

    # ED construction for the natural-drift endpoint tau=1/1024.
    diff = sub(r, p[v])
    L = l1(diff)
    norm_sign = [F(1 if x > 0 else -1 if x < 0 else 0) for x in diff]
    ell = sum((abs(x) for x in diff), Z)  # singleton fibers
    Alev = O / (2 * ell)
    chi = [dot(norm_sign, sub(row, p[v])) / L for row in p]
    Fchi = [i for i, value in enumerate(chi) if abs(value) > Alev]
    payer_mass = sum((max(p[v][i], Z) for i in Fchi), Z)
    if drift >= B * tau:
        assert ell > Z and Alev > Z
    # This calibration is outside ED's contract (it violates the I parent
    # width and the tiny routine ceiling), so the theorem's payer floor is
    # deliberately not asserted.  Direct construction gives zero P_v^+ mass.
    assert payer_mass == Z
    payer_top_deficits = {labels[i]: H - phi[i] for i in Fchi}

    return {
        "id": f"{shape}_old_fan_tau_1_{tau.denominator}",
        "classification": "exact_calibration_not_genuine_I_base",
        "labels": labels, "matrix": p,
        "parameters": {"tau": tau, "delta": delta, "b": B, "k_b": KB,
                       "c_m": CM, "D0": 2 + 4 * delta},
        "fibers": [{"point": labels[i], "indices": [i]} for i in range(n)],
        "visible_set": labels[1:], "hidden_top": "v",
        "height": {"H": H, "closest": closest, "dual_y": y,
                   "phi": phi, "H_minus_16tau": H - 16 * tau},
        "selected": {"A": [labels[i] for i in actors], "S": S, "q_A": qA},
        "all_center": {"shallow_mass_upper": Z, "far_G_mass_lower": S,
                       "required_tauS/16": floor, "distance_lower": center_lower},
        "ray": {"Z": ray_obj, "Z_over_tau": ray_obj / tau,
                "Lambda": ray_lambda, "c": ray_c, "ray_vector": ray_vec,
                "dual_lower": z_lower},
        "omega": {"mass": M, "weights": weights, "r": r, "drift": drift,
                  "drift_minus_btau": drift - B * tau, "Omega": width,
                  "Omega_minus_btau": width - B * tau,
                  "Omega_minus_1/16": width - F(1, 16),
                  "optimizer_signs": signs, "s_plus": sp, "s_minus": sm,
                  "q_plus": qp, "q_minus": qm, "weighted_chord": chord,
                  "common_receiver": [labels[i] for i in common_receiver],
                  "common_receiver_payment": common_payment},
        "ED": {"L": L, "norm_sign": norm_sign, "ell": ell, "A_lev": Alev,
               "chi_values": chi, "F_chi": [labels[i] for i in Fchi],
               "P_v_plus_F_chi": payer_mass,
               "contract_applicable": False,
               "reason_inapplicable": "Omega<1/16 and delta<=delta_rt both fail",
               "payer_top_deficits_for_actual_ray_phi": payer_top_deficits},
        "failed_gates": {"tallness": H <= 16 * tau,
                         "parent_Omega<1/16": width >= F(1, 16)},
    }


def w61_factorization(tau: F, eta: F) -> tuple[list[list[F]], list[list[F]], list[list[F]], F]:
    delta, eps, theta = tau * tau, tau * tau / 2, F(1, 64)
    alpha = O + eps - eta
    q = eps / alpha
    L = [[O, Z, Z], [O, Z, Z], [alpha, eta, -eps],
         [Z, O, Z], [Z, Z, O], [O - theta, theta, Z]]
    Bt = [[O + q, -q, Z, Z, Z, Z], [Z, Z, Z, O, Z, Z],
          [Z, Z, Z, Z, O, Z]]
    assert matmul(Bt, L) == [[O, Z, Z], [Z, O, Z], [Z, Z, O]]
    p = matmul(L, Bt)
    assert_projection(p, delta)
    return L, Bt, p, q


def shallow_probe(tau: F) -> dict[str, Any]:
    delta, S = tau * tau, CM
    eta = tau ** 3 / 16
    L0, Bt0, base, q = w61_factorization(tau, eta)
    alpha = O + delta / 2 - eta
    H = 2 * eta / alpha
    assert H < 16 * tau
    m_sh = tau * S / 16
    L = [row[:] for row in L0] + [[Z, O, Z], [Z, Z, O]]
    Bt = [row[:] + [Z, Z] for row in Bt0]
    Bt[0][3] -= m_sh
    Bt[0][4] -= S
    Bt[0][6], Bt[0][7] = m_sh, S
    assert matmul(Bt, L) == [[O, Z, Z], [Z, O, Z], [Z, Z, O]]
    p = matmul(L, Bt)
    assert_projection(p)
    actual = delta_of(p)
    spare = delta - q
    assert neg(p[0]) == q + m_sh + S and actual > delta
    return {
        "id": "Sh_W61_receiver_attachment_tau_1_256",
        "classification": "rejected_exact_projection_wrong_negativity_and_not_tall",
        "labels": ["a0", "a1", "z", "c", "d", "x", "c_clone", "d_clone"],
        "matrix": p, "L": L, "B_left_inverse": Bt,
        "parameters": {"tau": tau, "target_delta": delta, "S": S,
                       "required_theta_floor_tau/D0": tau / (2 + 4 * delta)},
        "base_height": {"H": H, "H_over_tau": H / tau,
                        "H_minus_16tau": H - 16 * tau},
        "receiver_budget": {"base_top_negative_q": q, "m_sh=tauS/16": m_sh,
                            "spare_tau2_minus_q": spare,
                            "m_sh_minus_spare": m_sh - spare,
                            "top_negative": neg(p[0]), "actual_delta": actual,
                            "actual_delta_minus_tau2": actual - delta},
        "binding": "q + m_sh + S <= tau^2 fails; for this endpoint m_sh alone exceeds tau^2-q",
    }


def graft(k: int) -> dict[str, Any]:
    tau, delta, t0 = F(1, k), F(1, k * k), F(1, 8 * k)
    u = [O, Z, Z, Z, Z, Z]
    z = [O + delta * (O - t0), Z, delta * t0, -delta / 2, -delta / 4, -delta / 4]
    o = [Z, Z, O, Z, Z, Z]
    a = [Z, Z, Z, F(1, 2), F(1, 4), F(1, 4)]
    x = add(scale(delta, o), scale(O - delta, a))
    yrow = add(scale(-delta, o), scale(O + delta, a))
    p = [u, z, o, a, x, yrow]
    assert_projection(p, delta)
    assert all(neg(row) <= delta for row in p)

    alpha = (O + delta) / (O + 2 * delta)
    closest = convex([alpha, O - alpha], [p[1], p[5]])
    H = l1(p[0], closest)
    r = (O - 2 * delta * t0) / (O + 2 * delta)
    dual = [O, Z, -O, r, r, r]
    constant = -dot(dual, p[1])
    phi = [dot(dual, row) + constant for row in p]
    assert phi[0] == H and all(phi[i] <= Z for i in [1, 2, 3, 4, 5])
    assert H < 16 * tau

    hstar = t0 - delta * (O - t0)
    hvals = [Z, Z, O, t0, delta + (O - delta) * t0, hstar]
    assert all(dot(row, hvals) == hvals[i] for i, row in enumerate(p))
    assert hstar < tau / 4
    return {"p": p, "tau": tau, "delta": delta, "t0": t0, "H": H,
            "phi": phi, "dual": dual, "constant": constant,
            "closest": closest, "hstar": hstar, "hvals": hvals}


def corner_x_probe() -> dict[str, Any]:
    d = graft(2048)
    p, tau, delta, H, phi = d["p"], d["tau"], d["delta"], d["H"], d["phi"]
    labels = ["u", "z", "o", "a", "x", "y"]
    # Legal vertex kernel.  a and x disintegrate on the vertices o,y.
    xi = {
        "u": {"u": O}, "z": {"z": O}, "o": {"o": O}, "y": {"y": O},
        "a": {"o": delta / (O + delta), "y": O / (O + delta)},
        "x": {"o": 2 * delta / (O + delta), "y": (O - delta) / (O + delta)},
    }
    for xname in labels:
        weights = xi[xname]
        assert sum(weights.values(), Z) == O
        assert convex(list(weights.values()), [p[labels.index(u)] for u in weights]) == p[labels.index(xname)]

    f = 3  # selected row a
    eta = {
        "(a,y)": p[f][3] * xi["a"]["y"],
        "(x,y)": p[f][4] * xi["x"]["y"],
        "(y,y)": p[f][5],
    }
    eta_mass = sum(eta.values(), Z)
    MX = eta["(a,y)"] + eta["(x,y)"]
    MD = MI = Z
    assert eta_mass >= F(1, 4) and MX > F(1, 8)
    # Every retained pair is in C_f and B_F.  h=0; y is rho-far and co-top.
    assert all(H - phi[i] < 4 * tau for i in (3, 4, 5))
    assert l1(p[3], p[0]) >= 4 * tau and l1(p[5], p[0]) >= 4 * tau
    score = 2 * (H - phi[f]) / (2 + 4 * delta)
    assert score <= 12 * tau / 13
    large_gap_mass = Z
    for key in ("(a,y)", "(x,y)"):
        xname = key[1:key.index(",")]
        if l1(p[labels.index(xname)], p[5]) >= B * tau:
            large_gap_mass += eta[key]
    assert Z < large_gap_mass < MX
    return {
        "id": "X_W61_exact_selected_corner_k2048",
        "classification": "definition_level_X_corner_not_SC_output_and_not_I_base",
        "labels": labels, "matrix": p,
        "parameters": {"tau": tau, "delta": delta, "b": B},
        "height": {"H": H, "H_minus_16tau": H - 16 * tau,
                   "phi": phi, "dual": d["dual"], "closest": d["closest"]},
        "certificate": {"v": "u", "f": "a", "h_values": [Z] * 6,
                        "phi": phi, "corner_score": score, "kernel_xi": xi,
                        "block": "B_F", "eta": eta, "eta_mass": eta_mass,
                        "M_X": MX, "M_I": MI, "M_D": MD,
                        "M_X_minus_1/8": MX - F(1, 8),
                        "mass_with_pair_distance_ge_btau": large_gap_mass,
                        "near_freight_mass_below_btau": MX - large_gap_mass},
        "binding": "H-16*tau<0; without an I-base/L0 measure this definition-level ledger is not an SC output",
    }


def diagonal_d_corner_probe() -> dict[str, Any]:
    d = graft(2048)
    p0, tau, delta = d["p"], d["tau"], d["delta"]
    # Append a transient row f=(1-e)u+e*y with e=2*tau.  The y endpoint is
    # co-top, so the row is rho-far while retaining a large u coefficient.
    p = [row + [Z] for row in p0]
    e = 2 * tau
    frow = add(scale(O - e, p0[0]), scale(e, p0[5])) + [Z]
    p.append(frow)
    assert_projection(p, delta)
    labels = ["u", "z", "o", "a", "x", "y", "f_transient"]
    phi = d["phi"] + [(O - e) * d["phi"][0] + e * d["phi"][5]]
    H = d["H"]
    assert l1(p[6], p[0]) >= 4 * tau
    assert H < 4 * tau  # co-top is automatic since H-4tau<0
    score = 2 * (H - phi[6]) / (2 + 4 * delta)
    assert score <= 12 * tau / 13

    # B_N retains (x,u)=(u,u), of mass 1/2.  The kernel is Dirac at vertices.
    eta_mass = O - e
    assert eta_mass >= F(1, 4)

    xi = {
        "u": {"u": O}, "z": {"z": O}, "o": {"o": O}, "y": {"y": O},
        "a": {"o": delta / (O + delta), "y": O / (O + delta)},
        "x": {"o": 2 * delta / (O + delta), "y": (O - delta) / (O + delta)},
        "f_transient": {"u": O - e, "y": e},
    }
    for xname in labels:
        weights = xi[xname]
        assert sum(weights.values(), Z) == O
        assert convex(list(weights.values()), [p[labels.index(u)] for u in weights]) == p[labels.index(xname)]

    # Exact exposedness LP at u.  From h(z)>=0,
    # h(a)<=t0*h(o)<=t0 and hence h(y)<=hstar.  Since
    # h(f)=e*h(y), the appended far row lowers the optimum to e*hstar.
    t0, hstar = d["t0"], d["hstar"]
    assert hstar == t0 - delta * (O - t0)
    assert d["hvals"][5] == hstar and d["hvals"][2] == O
    hstar_new = e * hstar
    hvals = d["hvals"] + [hstar_new]
    assert all(dot(row, hvals) == hvals[i] for i, row in enumerate(p))
    # Thus T={f_transient}, O={o}; their singleton hull gap is exact.
    KT = sub(p[6], p[0])
    KO = scale(hstar_new, sub(p[2], p[0]))
    g = l1(KT, KO)
    assert g > Z
    MX, MI, MD = Z, Z, eta_mass
    assert MX <= F(1, 8) and MI < F(1, 16) and MD > F(1, 16)
    return {
        "id": "diagonal_D_transient_corner_k2048",
        "classification": "definition_level_D_corner_not_SC_output_not_tall_and_rank_three",
        "labels": labels, "matrix": p,
        "parameters": {"tau": tau, "delta": delta, "rank": 3},
        "height": {"H": H, "H_minus_16tau": H - 16 * tau, "phi": phi},
        "certificate": {"v": "u", "f": "f_transient", "h_values": [Z] * 7,
                        "corner_score": score, "kernel_xi": xi, "block": "B_N",
                        "eta": {"(u,u)": eta_mass}, "eta_mass": eta_mass,
                        "M_X": MX, "M_I": MI, "M_D": MD,
                        "eta_mass_minus_1/4": eta_mass - F(1, 4)},
        "always_tight": {"new_t_star": hstar_new, "attaining_h_values": hvals,
                         "T": ["f_transient"], "O": ["o"], "K_T_point": KT,
                         "K_O_point": KO, "g_u": g, "g_u_over_tau": g / tau,
                         "distribution_g_u_over_tau": [{"mass": eta_mass, "value": g / tau}]},
        "I_cap_failure": {"M_X<=1/8": True, "M_I>=1/16": False,
                          "M_I_minus_1/16": -F(1, 16)},
        "D_cap_failure": {"H>16tau": False, "rank_above_3": False,
                          "escapes_rank_three_slab_theorem": False},
    }


def w55_attempt() -> dict[str, Any]:
    tau, t, A = F(1, 256), F(1, 65536), F(5)
    a = tau / (O + tau)
    L = [[O, Z, Z], [O + A * a - a * t, -A * a, a * t],
         [O + A - t, -A, t], [Z, O, Z], [Z, Z, O]]
    Bt = [[O - tau, tau + t, -t, Z, Z], [Z, Z, Z, O, Z], [Z, Z, Z, Z, O]]
    assert matmul(Bt, L) == [[O, Z, Z], [Z, O, Z], [Z, Z, O]]
    p = matmul(L, Bt)
    assert_projection(p)
    nus = [neg(row) for row in p]
    expected = A + (O + A - t) * t
    assert nus[2] == expected == delta_of(p) and expected > t
    return {"id": "Dcap_W55_A5_canonical_rank3_tau_1_256",
            "classification": "rejected_W55_completion_wrong_negativity_and_in_proved_class",
            "labels": ["v", "w", "f", "z", "o"], "matrix": p,
            "affine_coordinates": L, "left_inverse": Bt,
            "parameters": {"tau": tau, "target_delta": t, "A0": A,
                           "g": A * tau, "g_over_tau": A, "rank": 3},
            "row_negative_masses": nus, "actual_delta": expected,
            "actual_delta_minus_tau2": expected - t,
            "binding": "nu_f=A0+(1+A0-tau^2)tau^2; rank three and canonical slab",
            "proved_obstruction": "lem-starvation-completion-obstruction"}


def build() -> dict[str, Any]:
    Dprobe = simplex_probe(F(1, 1024), "D")  # equality at drift=b*tau
    Wprobe = simplex_probe(F(1, 2048), "W")  # strict small drift
    Shprobe = shallow_probe(F(1, 256))
    Xprobe = corner_x_probe()
    Dcorner = diagonal_d_corner_probe()
    W55 = w55_attempt()

    assert Dprobe["omega"]["drift"] == B * Dprobe["parameters"]["tau"]
    assert Wprobe["omega"]["drift"] < B * Wprobe["parameters"]["tau"]
    assert Wprobe["omega"]["Omega"] >= B * Wprobe["parameters"]["tau"]

    return {
        "schema": "w63-ihorn-six-shape-exact-l3-v1",
        "arithmetic": "fractions.Fraction; JSON rationals are numerator/denominator strings",
        "warning": "L3 evidence only; no entry is a proof and no genuine I-base datum was found",
        "constants": {"c_m": CM, "b": B, "k_b": KB},
        "verdicts": {
            "D": "BLOCKED", "W": "BLOCKED", "Sh": "BLOCKED",
            "X": "PARTIAL", "I-cap": "BLOCKED", "D-cap": "BLOCKED",
        },
        "shapes": {
            "D": {"best_near_miss": Dprobe,
                  "binding": "old fan enters drift at equality but Omega-1/16>0 and H-16tau<0"},
            "W": {"best_near_miss": Wprobe,
                  "binding": "old fan has correct drift side and a paid chord, but Omega-1/16>0 and is not a candidate"},
            "Sh": {"best_near_miss": Shprobe,
                   "binding": "receiver attachment violates q+m_sh+S<=tau^2 and base H<16tau"},
            "X": {"best_near_miss": Xprobe,
                  "binding": "definition-level M_X>1/8 ledger found locally; no I-base/L0 input exists and tallness fails"},
            "I-cap": {"best_near_miss": Dcorner,
                      "binding": "definition-level corner has M_I=0<1/16 and routes to D; it is not an SC output and tallness fails"},
            "D-cap": {"best_diagonal_corner": Dcorner, "w55_attempt": W55,
                      "binding": "D corner is short rank three; W55 A0=5 completion has order-one nu_f"},
        },
        "genuine_I_base_count": 0,
        "cell_bycatch": {"X_corner": True, "I_corner": False, "D_corner": True,
                         "all_are_pre_I_base_local_ledgers": True},
    }


def main() -> None:
    data = build()
    Path("certificates.json").write_text(json.dumps(qstr(data), indent=2) + "\n")
    print("D: BLOCKED — drift equality is reached, but the old fan violates Omega<1/16 and tallness.")
    print("W: BLOCKED — the paid weighted chord is the forbidden wide old fan; tallness also fails.")
    print("Sh: BLOCKED — q+m_sh+S<=tau^2 fails and the legal seed is cubic-height.")
    print("X: PARTIAL — an exact definition-level M_X>1/8 ledger exists, but no I-base/L0 input does.")
    print("I-cap: BLOCKED — the definition-level diagonal ledger has M_I=0 and routes to D; it is not tall.")
    print("D-cap: BLOCKED — the D ledger is short rank three; W55's canonical completion has order-one negativity.")
    print("SUMMARY: exact checks passed; 0 genuine I-base data; L3 evidence only, never a proof.")


if __name__ == "__main__":
    main()
