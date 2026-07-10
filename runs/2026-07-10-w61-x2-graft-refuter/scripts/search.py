#!/usr/bin/env python3
"""Exact search certificate for the W61 X2 thin-graft refuter attempt.

This file deliberately uses no floating-point arithmetic.  The constructed family
satisfies every bad-H-X check below except the selected-corner tallness hypothesis
H > 16*tau.  Consequently its verdict is PARTIAL, never REFUTED.
"""

from __future__ import annotations

from fractions import Fraction as F
import argparse
import json


NAMES = ("u", "z", "o", "a", "x", "y")
VERTICES = ("u", "z", "o", "y")
IDX = {name: i for i, name in enumerate(NAMES)}


def qstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def matmul(a, b):
    bt = list(zip(*b))
    return [[dot(row, col) for col in bt] for row in a]


def l1(a, b):
    return sum((abs(x - y) for x, y in zip(a, b)), F(0))


def neg_mass(row):
    return sum((-x for x in row if x < 0), F(0))


def affine_combo(weights, points):
    width = len(next(iter(points.values())))
    return [sum((weights.get(name, F(0)) * points[name][j] for name in points), F(0))
            for j in range(width)]


def build(k: int):
    assert k >= 512
    tau = F(1, k)
    delta = tau * tau
    t = tau / 8
    A = 1 + delta * (1 - t)

    # Affine coordinates in the basis (u,o,a).  The a-column is split into
    # the center a and a balanced pair x,y.  This makes BL=I exactly.
    L = {
        "u": [F(1), F(0), F(0)],
        "z": [A, t * delta, -delta],
        "o": [F(0), F(1), F(0)],
        "a": [F(0), F(0), F(1)],
        "x": [F(0), delta, 1 - delta],
        "y": [F(0), -delta, 1 + delta],
    }
    B = [
        [F(1), F(0), F(0), F(0), F(0), F(0)],
        [F(0), F(0), F(1), F(0), F(0), F(0)],
        [F(0), F(0), F(0), F(1, 2), F(1, 4), F(1, 4)],
    ]
    Lmat = [L[name] for name in NAMES]
    P = matmul(Lmat, B)
    points = {name: P[IDX[name]] for name in NAMES}

    # Legal vertex disintegration.  a and x lie strictly on the o-y edge.
    xi = {
        "u": {"u": F(1)},
        "z": {"z": F(1)},
        "o": {"o": F(1)},
        "y": {"y": F(1)},
        "a": {"o": delta / (1 + delta), "y": F(1) / (1 + delta)},
        "x": {"o": 2 * delta / (1 + delta),
              "y": (1 - delta) / (1 + delta)},
    }

    # Exact closest-edge dual for dist(u, conv{z,o,y}).
    H = 2 * delta * (t * (1 + delta) - delta) / (1 + 2 * delta)
    s = (1 - 2 * delta * t) / (1 + 2 * delta)
    S = 1 - H
    r = [F(1), -F(1), s]  # value on affine (u,o,a)-coordinates
    ambient_phi_linear = [F(1), F(0), -F(1), s, s, s]

    def phi(name):
        return dot(r, L[name]) - S

    def h(_name):
        return F(0)

    zeta = {name: H - phi(name) for name in NAMES}
    rho = 4 * tau
    kappa = tau / 4
    D = 2 + 4 * delta

    return {
        "k": k, "tau": tau, "delta": delta, "t": t, "A": A,
        "L": L, "Lmat": Lmat, "Bfac": B, "P": P, "points": points,
        "xi": xi, "H": H, "s": s, "S": S, "r": r,
        "ambient_phi_linear": ambient_phi_linear, "phi": phi, "h": h,
        "zeta": zeta, "rho": rho, "kappa": kappa, "D": D,
    }


def admissible_values(data, values, pinned):
    assert values[pinned] == 0
    assert all(F(0) <= values[name] <= 1 for name in NAMES)


def verify(k: int):
    d = build(k)
    tau, delta, t = d["tau"], d["delta"], d["t"]
    P, points, L, xi = d["P"], d["points"], d["L"], d["xi"]
    rho, kappa, H = d["rho"], d["kappa"], d["H"]
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        assert condition, name

    I3 = [[F(i == j) for j in range(3)] for i in range(3)]
    check("factor_BL=I", matmul(d["Bfac"], d["Lmat"]) == I3)
    check("P^2=P", matmul(P, P) == P)
    check("row_sums=1", all(sum(row, F(0)) == 1 for row in P))
    exact_delta = max(neg_mass(row) for row in P)
    check("delta=q^2", exact_delta == delta == tau * tau)
    check("0<delta<=2^-16", F(0) < delta <= F(1, 2**16))
    check("distinct_row_points", len({tuple(row) for row in P}) == len(P))

    # The factor coordinates are recovered by p_i L = L_i, so l1 geometry is
    # exactly the l1 geometry of L: B's three rows have disjoint probability support.
    check("coordinate_isometry",
          all(l1(points[a], points[b]) == l1(L[a], L[b])
              for a in NAMES for b in NAMES))
    wa = {"o": delta / (1 + delta), "y": F(1) / (1 + delta)}
    wx = {"o": 2 * delta / (1 + delta), "y": (1 - delta) / (1 + delta)}
    check("a_nonvertex", affine_combo(wa, points) == points["a"])
    check("x_nonvertex", affine_combo(wx, points) == points["x"])

    # Exact vertex/visibility ledger.  u lies outside triangle (z,o,y) precisely
    # because t(1+d)>d.  Explicit admissible exposers establish the other vertices.
    check("u_outside_visible_triangle", t * (1 + delta) > delta)
    theta_u = t - delta * (1 - t)
    hu = {
        name: dot([F(0), F(1), t], L[name]) for name in NAMES
    }
    admissible_values(d, hu, "u")
    far_u = [name for name in NAMES if l1(points[name], points["u"]) >= rho]
    check("u_far_set", set(far_u) == {"o", "a", "x", "y"})
    check("tstar_u_lower", min(hu[name] for name in far_u) == theta_u)
    # Upper certificate: h_z>=0 gives h_a<=t*h_o; hence for every admissible
    # exposer at u, h_y<=(-d+(1+d)t)h_o<=theta_u.
    check("tstar_u_upper_certificate", theta_u == -delta + (1 + delta) * t)
    check("u_hidden", F(0) < theta_u < kappa)

    hz_U = delta * (1 - t) / d["A"]
    hz = {name: dot([hz_U, F(1), F(1)], L[name]) for name in NAMES}
    admissible_values(d, hz, "z")
    far_z = [name for name in NAMES if l1(points[name], points["z"]) >= rho]
    check("z_visible_tstar=1", min(hz[name] for name in far_z) == 1)

    ho = {name: dot([F(1), F(0), F(1, 1 + delta)], L[name]) for name in NAMES}
    admissible_values(d, ho, "o")
    far_o = [name for name in NAMES if l1(points[name], points["o"]) >= rho]
    check("o_visible_margin", min(ho[name] for name in far_o) >= (1 - delta) / (1 + delta) > kappa)

    Uy = (1 - t * delta + delta * delta / (1 + delta)) / d["A"]
    hy = {name: dot([Uy, F(1), delta / (1 + delta)], L[name]) for name in NAMES}
    admissible_values(d, hy, "y")
    far_y = [name for name in NAMES if l1(points[name], points["y"]) >= rho]
    check("y_visible_margin", min(hy[name] for name in far_y) == Uy > kappa)
    check("visible_set_W={z,o,y}",
          checks["u_hidden"] and checks["z_visible_tstar=1"] and
          checks["o_visible_margin"] and checks["y_visible_margin"] and
          checks["a_nonvertex"] and checks["x_nonvertex"])

    # Primal closest point c on edge z-y and dual phi give the exact height.
    lam = (1 + delta) / (1 + 2 * delta)
    closest = affine_combo({"z": lam, "y": 1 - lam}, points)
    check("height_primal", l1(points["u"], closest) == H > 0)
    check("phi_ambient_values", all(d["phi"](name) == dot(d["ambient_phi_linear"], points[name]) - d["S"]
                                        for name in NAMES))
    check("phi_1_Lipschitz", max(abs(x) for x in d["ambient_phi_linear"]) <= 1)
    check("phi(u)=H", d["phi"]("u") == H)
    check("phi<=0_on_CW", d["phi"]("z") == 0 and d["phi"]("y") == 0 and d["phi"]("o") < 0)
    check("all_non_u_rows_in_CW",
          checks["a_nonvertex"] and checks["x_nonvertex"] and
          set(NAMES) - {"u", "a", "x"} == {"z", "o", "y"})
    check("hidden_top_maximality", H > 0 and checks["all_non_u_rows_in_CW"])
    check("W_nonempty", True)
    # This is the sole failed selected-corner clause; it is recorded, not asserted.
    checks["H>16*tau"] = H > 16 * tau
    assert not checks["H>16*tau"]

    # Remaining selected-corner data.
    f, v = "a", "u"
    check("h_admissible", all(d["h"](name) == 0 for name in NAMES))
    check("f_rho_far", l1(points[f], points[v]) >= rho)
    # a lies on the o-y edge, so dist(a,C_W)=0; low H makes co-top vacuous here.
    check("f_in_CW", affine_combo(wa, points) == points[f])
    check("f_co_top", F(0) > H - 4 * tau)
    score = 2 * d["zeta"][f] / d["D"] + d["h"](f)
    check("corner_score", score <= 12 * tau / 13)

    for source in NAMES:
        check(f"xi_{source}_probability", sum(xi[source].values(), F(0)) == 1 and
              all(weight >= 0 for weight in xi[source].values()))
        check(f"xi_{source}_barycenter", affine_combo(xi[source], points) == points[source])
        if source in VERTICES:
            check(f"xi_{source}_Dirac", xi[source] == {source: F(1)})

    # Full quotient-fiber Gamma calculation.  All row points are distinct, so the
    # full-fiber aggregation equals the displayed single coefficient here.
    gamma = {}
    for source in NAMES:
        pplus = max(P[IDX[f]][IDX[source]], F(0))
        for vertex, weight in xi[source].items():
            mass = pplus * weight
            if mass:
                gamma[(source, vertex)] = mass
    check("Gamma_total", sum(gamma.values(), F(0)) == 1)

    def in_corner(source, vertex):
        return (d["zeta"][source] < 4 * tau and d["h"](source) < 4 * tau and
                d["zeta"][vertex] < 4 * tau and d["h"](vertex) < 4 * tau)

    BF = {(source, vertex) for source, vertex in gamma
          if in_corner(source, vertex) and l1(points[vertex], points[v]) >= rho}
    BN = {(source, vertex) for source, vertex in gamma
          if in_corner(source, vertex) and l1(points[vertex], points[v]) < rho}
    check("B_F_positive_Gamma_support", BF == {("a", "y"), ("x", "y"), ("y", "y")})
    check("B_N_positive_Gamma_support_empty", BN == set())
    gamma_B = sum((gamma[pair] for pair in BF), F(0))
    mx_B = sum((gamma[pair] for pair in BF if points[pair[0]] != points[pair[1]]), F(0))
    TB = F(0)
    for pair in BF:
        source, vertex = pair
        if points[source] != points[vertex]:
            cost = min(F(1), l1(points[source], points[vertex]) / tau)
            TB += gamma[pair] * cost
    check("Gamma_f(B_F)", gamma_B == 1 / (1 + delta) >= F(1, 4))
    check("M_X(B_F)", mx_B == (3 - delta) / (4 * (1 + delta)) > F(1, 8))
    check("T_B_F", TB == tau * (2 - delta) / (1 + delta) < 2 * tau)

    return {
        "data": d, "checks": checks, "score": score, "gamma": gamma,
        "BF": BF, "Gamma_B": gamma_B, "M_X": mx_B, "T_B": TB,
    }


def certificate(result):
    d = result["data"]
    return {
        "classification": "partial_near_selected_corner_not_X2_witness",
        "k": d["k"],
        "matrix_order": list(NAMES),
        "matrix": [[qstr(x) for x in row] for row in d["P"]],
        "datum": {
            "v": "u", "f": "a",
            "phi": {"form": "dot(linear,p)+constant",
                    "linear": [qstr(x) for x in d["ambient_phi_linear"]],
                    "constant": qstr(-d["S"])},
            "h": {"form": "zero affine function"},
            "xi": {source: {vertex: qstr(weight) for vertex, weight in weights.items()}
                   for source, weights in d["xi"].items()},
            "B": "B_F",
            "B_positive_Gamma_support": [list(pair) for pair in sorted(result["BF"])],
        },
        "exact_values": {
            "tau": qstr(d["tau"]), "delta": qstr(d["delta"]),
            "H": qstr(d["H"]), "Gamma_f(B)": qstr(result["Gamma_B"]),
            "M_X(B)": qstr(result["M_X"]), "T_B": qstr(result["T_B"]),
        },
        "selected_corner_checks": {
            "all_except_tallness": all(value for name, value in result["checks"].items()
                                          if name != "H>16*tau"),
            "H>16*tau": result["checks"]["H>16*tau"],
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit partial certificates as JSON")
    args = parser.parse_args()
    ks = (512, 1024, 2048)
    results = [verify(k) for k in ks]
    assert all(results[i + 1]["data"]["delta"] < results[i]["data"]["delta"]
               for i in range(len(results) - 1))
    assert all(results[i + 1]["T_B"] < results[i]["T_B"]
               for i in range(len(results) - 1))

    if args.json:
        payload = {
            "verdict": "PARTIAL",
            "is_successful_X2_refuter": False,
            "warning": "These are not selected-corner/X2 witnesses: H>16*tau is false.",
            "certificates": [certificate(r) for r in results],
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return

    print("k | delta | H | H>16tau | Gamma_f(B_F) | M_X(B_F) | T_B | verdict")
    print("--|-------|---|---------|--------------|----------|-----|--------")
    for r in results:
        d = r["data"]
        print(" | ".join([
            str(d["k"]), qstr(d["delta"]), qstr(d["H"]),
            str(r["checks"]["H>16*tau"]), qstr(r["Gamma_B"]),
            qstr(r["M_X"]), qstr(r["T_B"]), "PARTIAL (tallness fails)",
        ]))
    print("\nExact verdict: PARTIAL, not an X2 refutation and not a proof of X2.")


if __name__ == "__main__":
    main()
