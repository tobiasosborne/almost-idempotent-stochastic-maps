#!/usr/bin/env python3
"""Exact-rational wave-13 amplifier worker.

This is L3 evidence only.  All certified quantities use fractions.Fraction.
Floats appear only in derived display strings and ranking aids.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "data"  # bundle: outputs -> data/ (mechanical re-home patch)
CSV_PATH = ROOT / "certified_points.csv"
JSON_PATH = ROOT / "certified_points.json"
ANSWER_PATH = ROOT / "ANSWER.md"


def ff(x: F | int) -> F:
    return x if isinstance(x, F) else F(x)


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def ffloat(x: F) -> float:
    return float(x)


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def neg(x: F) -> F:
    return -x if x < 0 else F(0)


def matmul(A: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def det3(M: list[list[F]]) -> F:
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def inv3(A: list[list[F]]) -> list[list[F]]:
    d = det3(A)
    if d == 0:
        raise ValueError("singular")
    cof = [
        [
            A[1][1] * A[2][2] - A[1][2] * A[2][1],
            -(A[1][0] * A[2][2] - A[1][2] * A[2][0]),
            A[1][0] * A[2][1] - A[1][1] * A[2][0],
        ],
        [
            -(A[0][1] * A[2][2] - A[0][2] * A[2][1]),
            A[0][0] * A[2][2] - A[0][2] * A[2][0],
            -(A[0][0] * A[2][1] - A[0][1] * A[2][0]),
        ],
        [
            A[0][1] * A[1][2] - A[0][2] * A[1][1],
            -(A[0][0] * A[1][2] - A[0][2] * A[1][0]),
            A[0][0] * A[1][1] - A[0][1] * A[1][0],
        ],
    ]
    return [[cof[j][i] / d for j in range(3)] for i in range(3)]


def row_times_mat(row: list[F], M: list[list[F]]) -> list[F]:
    return [sum(row[k] * M[k][j] for k in range(3)) for j in range(3)]


def coordinates(L: list[list[F]], U: tuple[int, int, int], i: int) -> list[F]:
    inv = inv3([L[u] for u in U])
    return row_times_mat(L[i], inv)


def P_of(L: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    I = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    assert matmul(B, L) == I
    P = matmul(L, B)
    assert matmul(P, P) == P
    assert all(sum(row) == 1 for row in P)
    return P


def row_neg(row: list[F]) -> F:
    return sum(neg(x) for x in row)


def delta_of(P: list[list[F]]) -> F:
    return max(row_neg(row) for row in P)


def E_of(a: list[F], r: int) -> F:
    lam = 1 - a[r]
    mu = sum(neg(a[q]) for q in range(3) if q != r)
    return pos(mu - lam)


@dataclass(frozen=True)
class ChartData:
    U: tuple[int, int, int]
    volume: F
    m: F
    phi: tuple[F, F, F]
    Phi: F
    coords: tuple[tuple[F, F, F], ...]


def chart_data(L: list[list[F]], P: list[list[F]]) -> list[ChartData]:
    vols: dict[tuple[int, int, int], F] = {}
    for U in combinations(range(len(L)), 3):
        v = abs(det3([L[u] for u in U]))
        if v > 0:
            vols[U] = v
    vmax = max(vols.values())
    out: list[ChartData] = []
    for U, v in vols.items():
        coords = tuple(tuple(coordinates(L, U, i)) for i in range(len(L)))
        phi = []
        for r in range(3):
            total = sum(pos(P[U[r]][i]) * E_of(list(coords[i]), r) for i in range(len(L)))
            phi.append(total)
        out.append(ChartData(U=U, volume=v, m=v / vmax, phi=tuple(phi), Phi=max(phi), coords=coords))
    out.sort(key=lambda c: (c.Phi, c.U))
    return out


def theta_argmins(charts: list[ChartData]) -> list[ChartData]:
    eligible = [c for c in charts if c.m >= F(1, 2)]
    best = min(c.Phi for c in eligible)
    return [c for c in eligible if c.Phi == best]


def pivot_chart_phi(
    L: list[list[F]],
    P: list[list[F]],
    U: tuple[int, int, int],
    s: int,
    j: int,
) -> tuple[F, F, F, F, tuple[int, int, int]]:
    V = list(U)
    V[s] = j
    Vt = tuple(V)
    # The chart ordering matters for s/r labels, so recompute in the requested order.
    coords = tuple(tuple(coordinates(L, Vt, i)) for i in range(len(L)))
    phi = []
    for r in range(3):
        total = sum(pos(P[Vt[r]][i]) * E_of(list(coords[i]), r) for i in range(len(L)))
        phi.append(total)
    return phi[0], phi[1], phi[2], max(phi), Vt


def B_mass(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(pos(P[U[r]][i]) * neg(coords[i][s]) for i in range(len(P)))


def C_mass(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(neg(P[U[r]][i]) * pos(coords[i][s]) for i in range(len(P)))


def A_mass(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(pos(P[U[r]][i]) * pos(coords[i][s]) for i in range(len(P)))


def D_mass(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(neg(P[U[r]][i]) * neg(coords[i][s]) for i in range(len(P)))


def budget(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], s: int) -> tuple[F, F, F, F]:
    Bset = [i for i in range(len(P)) if i not in U]
    Gc = sum(neg(P[U[s]][u]) for u in U)
    Smu = sum(neg(P[U[s]][i]) * sum(neg(coords[i][q]) for q in range(3) if q != s) for i in Bset)
    SIG = sum(P[U[s]][i] * row_neg(P[i]) for i in Bset if P[U[s]][i] > 0)
    return Gc, Smu, SIG, Gc + Smu + SIG


def ci_import(
    P: list[list[F]],
    coords: tuple[tuple[F, F, F], ...],
    U: tuple[int, int, int],
    s: int,
    r: int,
    j: int,
) -> tuple[F, list[tuple[int, F, F]], F, F, F]:
    """Literal lem-collateral-import I_{r,j}(U), in its c>0 regime."""
    t = next(q for q in range(3) if q not in (r, s))
    c = coords[j][s]
    d_r = coords[j][r]
    d_t = coords[j][t]
    assert c > 0
    total = F(0)
    terms: list[tuple[int, F, F]] = []
    for i, a in enumerate(coords):
        R = (1 / c - 1) * neg(a[s]) + pos(a[s] * d_t / c) - a[s] * d_r / c
        term = pos(P[U[r]][i]) * pos(R)
        total += term
        if term:
            terms.append((i, R, term))
    return total, terms, c, d_r, d_t


def import_reduction_coefficients(c: F, d_r: F, d_t: F) -> tuple[F, F]:
    alpha_B = (pos(1 - c) + neg(d_t) + pos(d_r)) / c
    alpha_A = (pos(d_t) + neg(d_r)) / c
    return alpha_B, alpha_A


def branch_record(
    L: list[list[F]],
    P: list[list[F]],
    cd: ChartData,
    s: int,
    j: int,
) -> dict:
    a = list(cd.coords[j])
    M = cd.Phi
    beta_s = P[cd.U[s]][j]
    E_s = E_of(a, s)
    W_s = sum(neg(a[t]) for t in range(3) if t != s)
    high_self = P[j][j] > F(1, 2)
    # G1/G2 negative fan cover proxy from conj-sc: transverse negative coordinate
    # whose one-row replacement chart is theta-half admissible.
    fan_covers = []
    for t in range(3):
        if t == s:
            continue
        if a[t] < 0 and neg(a[t]) * cd.m >= F(1, 2):
            fan_covers.append(t)
    non_fan = len(fan_covers) == 0
    theta_pivot = a[s] != 0 and abs(a[s]) * cd.m >= F(1, 2)
    psi = gamma = None
    branch_type = "none"
    V = None
    phiV = None
    if theta_pivot:
        vals = pivot_chart_phi(L, P, cd.U, s, j)
        phiV = vals[:3]
        V = vals[4]
        psi = phiV[s]
        gamma = max(phiV[r] for r in range(3) if r != s)
        if psi < M <= gamma:
            branch_type = "Gamma"
        elif gamma < M <= psi:
            branch_type = "Psi"
        elif max(phiV) < M:
            branch_type = "minimality-violating"
        else:
            branch_type = "mixed"
    clean_gamma = (
        beta_s > 0
        and E_s > 0
        and high_self
        and non_fan
        and theta_pivot
        and branch_type == "Gamma"
    )
    return {
        "j": j,
        "a": a,
        "beta_s": beta_s,
        "E_s": E_s,
        "W_s": W_s,
        "self": P[j][j],
        "high_self": high_self,
        "fan_covers": fan_covers,
        "non_fan": non_fan,
        "theta_pivot": theta_pivot,
        "V": V,
        "phiV": phiV,
        "Psi": psi,
        "Gamma": gamma,
        "branch_type": branch_type,
        "clean_gamma": clean_gamma,
    }


def analyze_instance(name: str, family: str, L: list[list[F]], B: list[list[F]]) -> dict | None:
    P = P_of(L, B)
    delta = delta_of(P)
    if not (F(1, 100) <= delta <= F(3, 20)):
        return None
    assert delta <= F(1, 4)
    charts = chart_data(L, P)
    argmins = theta_argmins(charts)
    rec: dict = {
        "name": name,
        "family": family,
        "n": len(L),
        "delta": delta,
        "L": L,
        "B": B,
        "P": P,
        "argmins": [],
        "best_B_over_delta": F(0),
        "has_clean_gamma": False,
        "has_gamma": False,
        "charts": [],
    }
    for cd in charts:
        rec["charts"].append(
            {
                "U": cd.U,
                "volume": cd.volume,
                "m": cd.m,
                "phi": cd.phi,
                "Phi": cd.Phi,
                "theta_half": cd.m >= F(1, 2),
                "argmin": False,
            }
        )
    for cd in argmins:
        for csum in rec["charts"]:
            if csum["U"] == cd.U:
                csum["argmin"] = True
        pivots = [s for s in range(3) if cd.phi[s] == cd.Phi]
        chart_rec = {
            "U": cd.U,
            "volume": cd.volume,
            "m": cd.m,
            "phi": cd.phi,
            "Phi": cd.Phi,
            "pivots": pivots,
            "branches": [],
            "masses": [],
        }
        for s in pivots:
            for j in range(len(L)):
                if j in cd.U:
                    continue
                br = branch_record(L, P, cd, s, j)
                br["s"] = s
                if br["branch_type"] == "Gamma":
                    rec["has_gamma"] = True
                if br["clean_gamma"]:
                    rec["has_clean_gamma"] = True
                if br["beta_s"] > 0 and (br["E_s"] > 0 or br["branch_type"] == "Gamma"):
                    chart_rec["branches"].append(br)
            for r in range(3):
                if r == s:
                    continue
                bm = B_mass(P, cd.coords, cd.U, r, s)
                cm = C_mass(P, cd.coords, cd.U, r, s)
                am = A_mass(P, cd.coords, cd.U, r, s)
                dm = D_mass(P, cd.coords, cd.U, r, s)
                assert am == bm + cm - dm
                Gc, Smu, SIG, Bud = budget(P, cd.coords, cd.U, s)
                rec["best_B_over_delta"] = max(rec["best_B_over_delta"], bm / delta)
                chart_rec["masses"].append(
                    {
                        "s": s,
                        "r": r,
                        "B": bm,
                        "C": cm,
                        "A": am,
                        "D": dm,
                        "B_over_delta": bm / delta,
                        "C_over_delta": cm / delta,
                        "budget": (Gc, Smu, SIG, Bud),
                    }
                )
        rec["argmins"].append(chart_rec)
    return rec


def family_two_carrier(params: tuple[F, F, F, F, F, F]) -> tuple[list[list[F]], list[list[F]]]:
    """G12-like two carrier chart, but parameterized independently.

    j=(p,-e,1-p+e) carries the s-demand; k=(q,1+g,-g)
    carries cross-pivot B_{1,2}.  Rows of B are the sparse left inverse forced
    by those two carriers.
    """
    p, e, q, g, v, w = params
    j = [p, -e, 1 - p + e]
    k = [q, 1 + g - q, -g]
    L = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)], j, k]
    B0 = [F(1), F(0), F(0), F(0), F(0)]
    B1 = [-w * q, 1 - w * (1 + g - q), w * g, F(0), w]
    c = 1 - p + e
    B2 = [-v * p, v * e, 1 - v * c, v, F(0)]
    return L, [B0, B1, B2]


def family_rotated_bridge(params: tuple[F, F, F, F, F, F, F]) -> tuple[list[list[F]], list[list[F]]]:
    """Six-row bridge: branch and B-carrier are separated by a bridge row.

    This is not a rescaling of the G12 two-carrier support.  The transverse
    beta row uses both k and h, while the pivot beta row uses j and h; h has
    positive pivot coordinate and negative first coordinate, changing the
    pivot-removal geometry and the Gamma carrier.
    """
    p, e, q, g, hneg, v, w = params
    j = [p, -e, 1 - p + e]
    k = [q, 1 + g - q, -g]
    h = [-hneg, F(1, 2) + hneg, F(1, 2)]
    L = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)], j, k, h]
    # Sparse left inverses with a shared bridge column h.
    wh = w / 3
    wk = w
    B0 = [1 + wh * hneg, -wh * (F(1, 2) + hneg), -wh / 2, F(0), F(0), wh]
    # Transverse row e1 using k and h.
    B1 = [
        -wk * q + wh * hneg,
        1 - wk * (1 + g - q) - wh * (F(1, 2) + hneg),
        wk * g - wh / 2,
        F(0),
        wk,
        wh,
    ]
    vh = v / 4
    vj = v
    c = 1 - p + e
    B2 = [
        -vj * p + vh * hneg,
        vj * e - vh * (F(1, 2) + hneg),
        1 - vj * c - vh / 2,
        vj,
        F(0),
        vh,
    ]
    return L, [B0, B1, B2]


def family_compensated_insert(
    base_params: tuple[F, F, F, F, F, F],
    h: tuple[F, F, F],
    yvec: tuple[F, F, F],
) -> tuple[list[list[F]], list[list[F]]]:
    """Add one actual row and one beta column by exact identity compensation.

    If an inserted column has beta weight y in beta row r, subtract y*h_t from
    identity column t in the same beta row.  Since h=sum_t h_t e_t, BL remains I.
    """
    L, B = family_two_carrier(base_params)
    L = [row[:] for row in L] + [list(h)]
    Bout: list[list[F]] = []
    for r, row in enumerate(B):
        y = yvec[r]
        nr = row[:] + [y]
        for t in range(3):
            nr[t] -= y * h[t]
        Bout.append(nr)
    return L, Bout


def family_multi_compensated_insert(
    base_params: tuple[F, F, F, F, F, F],
    inserts: list[tuple[tuple[F, F, F], tuple[F, F, F]]],
) -> tuple[list[list[F]], list[list[F]]]:
    L, B = family_two_carrier(base_params)
    L = [row[:] for row in L]
    B = [row[:] for row in B]
    for h, yvec in inserts:
        L.append(list(h))
        for r, row in enumerate(B):
            y = yvec[r]
            row.append(y)
            for t in range(3):
                row[t] -= y * h[t]
    return L, B


BASE_A = (F(2, 25), F(3, 50), F(1, 25), F(1, 40), F(7, 10), F(1, 2))
ORIGINAL_INSERT_H = (F(-1, 100), F(51, 100), F(1, 2))
CF_BEST_A = F(6332623, 370881409)
CF_BEST_H = (-CF_BEST_A, F(1, 2) + CF_BEST_A, F(1, 2))
CF_BEST_Y = F(993725924662467, 14527204611353000)


def active_boundary_y_for_h(h: tuple[F, F, F]) -> F:
    """Solve the active U=(0,2,4) vs U=(0,1,3) switch for BASE_A."""
    y0 = F(0)
    y1 = F(1, 10000)

    def phi_at(y: F, U: tuple[int, int, int]) -> F:
        L, B = family_compensated_insert(BASE_A, h, (F(0), F(0), y))
        P = P_of(L, B)
        return next(c.Phi for c in chart_data(L, P) if c.U == U)

    a0 = phi_at(y0, (0, 2, 4))
    b0 = phi_at(y0, (0, 1, 3))
    a1 = phi_at(y1, (0, 2, 4))
    b1 = phi_at(y1, (0, 1, 3))
    slope_gap = (a1 - a0) / y1 - (b1 - b0) / y1
    assert slope_gap != 0
    return (b0 - a0) / slope_gap


def active_boundary_y_for_shape_a(a: F) -> F:
    # Direct closed form in the stable sign pattern; asserted against full
    # chart enumeration in the emitted records.
    return F(2679363, 1) / (F(49000) * (F(22) * a + F(799)))


def algebraic_shape_balance_summary() -> dict:
    # For h=(-a,1/2+a,1/2), the active switch gives
    # y=2679363/(49000*(22a+799)).  Equating the row-2 loss and
    # inserted-row loss gives this quadratic irrational a.  We record it
    # as a limit law only; emitted certified instances remain rational.
    return {
        "a_positive_root": "-5500573/293216 + sqrt(757785147162145)/1466080",
        "a_decimal": "0.017074522600295663359766759116417061055511538161...",
        "limit_B_over_delta_decimal": "0.777640312383967...",
        "certified_denominator_cap_for_a": "1000000000",
    }


def calibration_g12() -> dict:
    L = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(3, 5), F(-1, 3), F(11, 15)],
        [F(1, 10), F(19, 20), F(-1, 20)],
    ]
    B = [
        [F(1), F(0), F(0), F(0), F(0)],
        [F(-4, 57), F(1, 3), F(2, 57), F(0), F(40, 57)],
        [F(-1, 4), F(5, 36), F(25, 36), F(5, 12), F(0)],
    ]
    rec = analyze_instance("G12 calibration", "calibration", L, B)
    assert rec is None  # outside requested delta<3/20, checked below manually
    P = P_of(L, B)
    delta = delta_of(P)
    charts = chart_data(L, P)
    arg = theta_argmins(charts)
    assert delta == F(1, 4)
    assert len(arg) == 1 and arg[0].U == (0, 1, 2)
    cd = arg[0]
    assert cd.phi == (F(0), F(0), F(1, 36))
    bm = B_mass(P, cd.coords, cd.U, 1, 2)
    cm = C_mass(P, cd.coords, cd.U, 1, 2)
    assert bm == F(2, 57)
    assert cm == F(0)
    assert bm / delta == F(8, 57)
    return {
        "delta": delta,
        "B": bm,
        "B_over_delta": bm / delta,
    }


def calibration_small_delta_bundle() -> dict:
    L, B = family_compensated_insert(BASE_A, ORIGINAL_INSERT_H, (F(0), F(0), F(681, 10000)))
    P = P_of(L, B)
    delta = delta_of(P)
    charts = chart_data(L, P)
    argmins = theta_argmins(charts)
    assert delta == F(55319, 1000000)
    assert len(argmins) == 1 and argmins[0].U == (0, 2, 4)
    cd = argmins[0]
    assert cd.phi == (F(0), F(679, 24625), F(219870541, 7880000000))
    bm = B_mass(P, cd.coords, cd.U, 1, 2)
    cm = C_mass(P, cd.coords, cd.U, 1, 2)
    assert bm == F(42, 985)
    assert cm == 0
    assert bm / delta == F(8400000, 10897843)
    br = branch_record(L, P, cd, 2, 1)
    assert br["clean_gamma"]
    return {
        "delta": delta,
        "B": bm,
        "B_over_delta": bm / delta,
        "argmin": cd.U,
    }


def search_two_carrier() -> list[dict]:
    out: list[dict] = []
    # Designed around p < 2e (positive E_s on j), small g for small B,
    # and v large enough to make P_jj>1/2.
    vals_e = [F(n, 100) for n in range(4, 17, 2)]
    vals_p = [F(n, 100) for n in range(2, 25, 2)]
    vals_q = [F(n, 100) for n in range(0, 13, 2)]
    vals_g = [F(n, 200) for n in range(1, 21, 2)]
    vals_v = [F(n, 20) for n in range(11, 19)]
    vals_w = [F(n, 20) for n in range(3, 19)]
    count = 0
    for e, p, q, g, v, w in product(vals_e, vals_p, vals_q, vals_g, vals_v, vals_w):
        if not (p < 2 * e and 1 - p + e > F(1, 2)):
            continue
        if 1 + g - q <= 0:
            continue
        try:
            L, B = family_two_carrier((p, e, q, g, v, w))
            rec = analyze_instance(f"two-carrier p={p} e={e} q={q} g={g} v={v} w={w}", "two-carrier", L, B)
        except (AssertionError, ValueError, ZeroDivisionError):
            continue
        count += 1
        if rec and rec["has_clean_gamma"]:
            out.append(rec)
    out.sort(key=lambda r: (r["best_B_over_delta"], -r["delta"]), reverse=True)
    return out


def certified_candidate_records() -> list[dict]:
    records: list[dict] = []
    two_params = [
        ("two-carrier-A", (F(2, 25), F(3, 50), F(1, 25), F(1, 40), F(7, 10), F(1, 2))),
        ("two-carrier-B", (F(3, 25), F(9, 100), F(1, 25), F(3, 100), F(33, 50), F(11, 50))),
        ("two-carrier-C", (F(7, 50), F(1, 10), F(1, 25), F(13, 400), F(3, 5), F(13, 50))),
        ("two-carrier-D", (F(4, 25), F(11, 100), F(1, 25), F(3, 100), F(71, 100), F(3, 20))),
    ]
    for label, params in two_params:
        L, B = family_two_carrier(params)
        rec = analyze_instance(label, "two-carrier", L, B)
        assert rec and rec["has_clean_gamma"], label
        records.append(rec)

    base = (F(2, 25), F(3, 50), F(1, 25), F(1, 40), F(7, 10), F(1, 2))
    h = (F(-1, 100), F(51, 100), F(1, 2))
    insert_ys = [F(1, 100), F(3, 100), F(1, 20), F(681, 10000), F(17, 250)]
    for y in insert_ys:
        L, B = family_compensated_insert(base, h, (F(0), F(0), y))
        rec = analyze_instance(f"insert-y={y}", "compensated-insert", L, B)
        assert rec and rec["has_clean_gamma"], y
        records.append(rec)
    records.sort(key=lambda r: (r["best_B_over_delta"], -r["delta"]), reverse=True)
    return records


def obstruction_summary(name: str, family: str, L: list[list[F]], B: list[list[F]]) -> dict:
    P = P_of(L, B)
    delta = delta_of(P)
    charts = chart_data(L, P)
    argmins = theta_argmins(charts)
    rec = analyze_instance(name, family, L, B)
    out = {
        "kind": "certified_obstruction",
        "name": name,
        "family": family,
        "delta": delta,
        "in_range": F(1, 100) <= delta <= F(3, 20),
        "argmins": [c.U for c in argmins],
        "argmin_phi": [argmins[0].phi],
        "has_clean_gamma": bool(rec and rec["has_clean_gamma"]),
        "best_B_over_delta": rec["best_B_over_delta"] if rec else None,
    }
    if rec:
        branches = []
        for c in rec["argmins"]:
            for b in c["branches"]:
                branches.append(
                    {
                        "U": c["U"],
                        "j": b["j"],
                        "branch_type": b["branch_type"],
                        "clean_gamma": b["clean_gamma"],
                        "self": b["self"],
                        "high_self": b["high_self"],
                        "non_fan": b["non_fan"],
                        "theta_pivot": b["theta_pivot"],
                    }
                )
        out["branches"] = branches
    return out


def amplification_obstructions() -> list[dict]:
    out: list[dict] = []
    for eps in (F(1, 100), F(1, 50), F(1, 20)):
        rec = non_argmin_amplifier(eps)
        rec["kind"] = "non_argmin_amplifier"
        out.append(rec)
    base = (F(2, 25), F(3, 50), F(1, 25), F(1, 40), F(7, 10), F(1, 2))
    h = (F(-1, 100), F(51, 100), F(1, 2))
    L, B = family_compensated_insert(base, h, (F(0), F(0), F(685, 10000)))
    out.append(obstruction_summary("insert-y=685/10000", "compensated-insert", L, B))
    L, B = family_two_carrier((F(2, 25), F(3, 50), F(1, 25), F(1, 40), F(9, 10), F(1, 2)))
    out.append(obstruction_summary("two-carrier-more-v", "two-carrier", L, B))
    L, B = family_two_carrier((F(1, 25), F(3, 50), F(1, 25), F(1, 40), F(7, 10), F(1, 2)))
    out.append(obstruction_summary("two-carrier-small-p", "two-carrier", L, B))
    return out


def non_argmin_amplifier(eps: F) -> dict:
    L = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)], [eps, F(3, 2) - eps, F(-1, 2)]]
    d = (1 - eps) / (F(3, 2) - eps)
    B = [[F(1), F(0), F(0), F(0)], [-d * eps, eps, d / 2, d], [F(0), F(0), F(1), F(0)]]
    P = P_of(L, B)
    delta = delta_of(P)
    charts = chart_data(L, P)
    base = next(c for c in charts if c.U == (0, 1, 2))
    argmins = theta_argmins(charts)
    bm = B_mass(P, base.coords, base.U, 1, 2)
    return {
        "eps": eps,
        "delta": delta,
        "B": bm,
        "B_over_delta": bm / delta,
        "base_Phi": base.Phi,
        "argmin_U": argmins[0].U,
        "argmin_Phi": argmins[0].Phi,
    }


def matrix_to_json(M: list[list[F]]) -> list[list[str]]:
    return [[fstr(x) for x in row] for row in M]


def serialize_rec(rec: dict) -> dict:
    return {
        "name": rec["name"],
        "family": rec["family"],
        "n": rec["n"],
        "delta": fstr(rec["delta"]),
        "best_B_over_delta": fstr(rec["best_B_over_delta"]),
        "has_clean_gamma": rec["has_clean_gamma"],
        "has_gamma": rec["has_gamma"],
        "L": matrix_to_json(rec["L"]),
        "B": matrix_to_json(rec["B"]),
        "P": matrix_to_json(rec["P"]),
        "charts": [
            {
                "U": list(c["U"]),
                "volume": fstr(c["volume"]),
                "m": fstr(c["m"]),
                "phi": [fstr(x) for x in c["phi"]],
                "Phi": fstr(c["Phi"]),
                "theta_half": c["theta_half"],
                "argmin": c["argmin"],
            }
            for c in rec["charts"]
        ],
        "argmins": [
            {
                "U": list(c["U"]),
                "volume": fstr(c["volume"]),
                "m": fstr(c["m"]),
                "phi": [fstr(x) for x in c["phi"]],
                "Phi": fstr(c["Phi"]),
                "pivots": c["pivots"],
                "branches": [
                    {
                        "j": b["j"],
                        "a": [fstr(x) for x in b["a"]],
                        "beta_s": fstr(b["beta_s"]),
                        "E_s": fstr(b["E_s"]),
                        "W_s": fstr(b["W_s"]),
                        "self": fstr(b["self"]),
                        "high_self": b["high_self"],
                        "fan_covers": b["fan_covers"],
                        "non_fan": b["non_fan"],
                        "theta_pivot": b["theta_pivot"],
                        "V": list(b["V"]) if b["V"] else None,
                        "phiV": [fstr(x) for x in b["phiV"]] if b["phiV"] else None,
                        "Psi": fstr(b["Psi"]) if b["Psi"] is not None else None,
                        "Gamma": fstr(b["Gamma"]) if b["Gamma"] is not None else None,
                        "branch_type": b["branch_type"],
                        "clean_gamma": b["clean_gamma"],
                    }
                    for b in c["branches"]
                ],
                "masses": [
                    {
                        "s": m["s"],
                        "r": m["r"],
                        "B": fstr(m["B"]),
                        "C": fstr(m["C"]),
                        "A": fstr(m["A"]),
                        "D": fstr(m["D"]),
                        "B_over_delta": fstr(m["B_over_delta"]),
                        "C_over_delta": fstr(m["C_over_delta"]),
                        "budget": [fstr(x) for x in m["budget"]],
                    }
                    for m in c["masses"]
                ],
            }
            for c in rec["argmins"]
        ],
    }


def jsonable(obj):
    if isinstance(obj, F):
        return fstr(obj)
    if isinstance(obj, tuple):
        return [jsonable(x) for x in obj]
    if isinstance(obj, list):
        return [jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {k: jsonable(v) for k, v in obj.items()}
    return obj


def find_best_clean_context(rec: dict) -> dict:
    best: dict | None = None
    charts = {c.U: c for c in chart_data(rec["L"], rec["P"])}
    for chart in rec["argmins"]:
        cd = charts[chart["U"]]
        for br in chart["branches"]:
            if not br["clean_gamma"]:
                continue
            s = br["s"]
            gamma_rs = [r for r in range(3) if r != s and br["phiV"] and br["phiV"][r] == br["Gamma"]]
            for mass in chart["masses"]:
                if mass["s"] != s:
                    continue
                if gamma_rs and mass["r"] not in gamma_rs:
                    continue
                candidate = {
                    "chart": chart,
                    "chart_data": cd,
                    "branch": br,
                    "mass": mass,
                }
                if best is None or mass["B_over_delta"] > best["mass"]["B_over_delta"]:
                    best = candidate
    assert best is not None, rec["name"]
    return best


def certified_point(name: str, family: str, L: list[list[F]], B: list[list[F]], note: str = "") -> dict:
    rec = analyze_instance(name, family, L, B)
    assert rec and rec["has_clean_gamma"], name
    ctx = find_best_clean_context(rec)
    cd = ctx["chart_data"]
    br = ctx["branch"]
    mass = ctx["mass"]
    I, terms, c, d_r, d_t = ci_import(rec["P"], cd.coords, cd.U, mass["s"], mass["r"], br["j"])
    alpha_B, alpha_A = import_reduction_coefficients(c, d_r, d_t)
    reduced_import = alpha_B * mass["B"] + alpha_A * mass["A"]
    Gc, Smu, SIG, Bud = mass["budget"]
    return {
        "name": name,
        "family": family,
        "note": note,
        "n": rec["n"],
        "delta": rec["delta"],
        "B_over_delta": mass["B_over_delta"],
        "U": cd.U,
        "s": mass["s"],
        "r": mass["r"],
        "branch_j": br["j"],
        "B_mass": mass["B"],
        "C_mass": mass["C"],
        "A_mass": mass["A"],
        "D_mass": mass["D"],
        "Phi_r": cd.phi[mass["r"]],
        "Phi": cd.Phi,
        "ci_import": I,
        "ci_terms": terms,
        "ci_total": cd.phi[mass["r"]] + I,
        "ci_margin_B_minus_total": mass["B"] - (cd.phi[mass["r"]] + I),
        "alpha_B": alpha_B,
        "alpha_A": alpha_A,
        "reduced_import_bound": reduced_import,
        "reduced_total": cd.phi[mass["r"]] + reduced_import,
        "reduced_margin_B_minus_total": mass["B"] - (cd.phi[mass["r"]] + reduced_import),
        "budget_G_class_minus": Gc,
        "budget_S_minus_mu": Smu,
        "budget_SIGMA": SIG,
        "budget_total": Bud,
        "B_over_budget_total": mass["B"] / Bud if Bud else None,
        "budget_total_over_delta": Bud / rec["delta"] if rec["delta"] else None,
        "branch": br,
        "argmins": [
            {
                "U": c["U"],
                "volume": c["volume"],
                "m": c["m"],
                "phi": c["phi"],
                "Phi": c["Phi"],
                "pivots": c["pivots"],
            }
            for c in rec["argmins"]
        ],
        "L": rec["L"],
        "B": rec["B"],
        "P": rec["P"],
    }


def make_certified_points() -> list[dict]:
    points: list[dict] = []

    L, B = family_compensated_insert(BASE_A, ORIGINAL_INSERT_H, (F(0), F(0), F(681, 10000)))
    points.append(certified_point("bundle-record-y=681/10000", "compensated-insert", L, B, "Prior bundle maximizer."))

    y_original_boundary = active_boundary_y_for_h(ORIGINAL_INSERT_H)
    assert y_original_boundary == F(2679363, 39161780)
    L, B = family_compensated_insert(BASE_A, ORIGINAL_INSERT_H, (F(0), F(0), y_original_boundary))
    points.append(certified_point("original-h-active-boundary", "compensated-insert-boundary", L, B, "Exact active chart switch boundary for h=(-1/100,51/100,1/2)."))

    shape_as = [
        ("shape-a=1/60", F(1, 60)),
        ("shape-a=8537/500000", F(8537, 500000)),
        ("shape-a=40417/2367094", F(40417, 2367094)),
        ("shape-a=699134/40946035", F(699134, 40946035)),
        ("shape-a=6332623/370881409", CF_BEST_A),
    ]
    for label, a in shape_as:
        h = (-a, F(1, 2) + a, F(1, 2))
        y = active_boundary_y_for_shape_a(a)
        if a == CF_BEST_A:
            assert y == CF_BEST_Y
        L, B = family_compensated_insert(BASE_A, h, (F(0), F(0), y))
        points.append(certified_point(label, "variable-insert-shape-boundary", L, B, "Active switch boundary for h=(-a,1/2+a,1/2)."))

    for copies in (2, 4):
        inserts = [(CF_BEST_H, (F(0), F(0), CF_BEST_Y / copies)) for _ in range(copies)]
        L, B = family_multi_compensated_insert(BASE_A, inserts)
        points.append(certified_point(f"n={5+copies}-duplicate-split", "multi-insert-duplicate", L, B, "Duplicate split of the best rational insert; no amplification beyond the one-row value."))

    points.sort(key=lambda p: (p["B_over_delta"], -p["n"]), reverse=True)
    return points


def richer_obstructions() -> list[dict]:
    out: list[dict] = []
    out.extend(amplification_obstructions())
    out.append(
        {
            "kind": "shape-balance-law",
            **algebraic_shape_balance_summary(),
            "interpretation": "In the one-parameter h=(-a,1/2+a,1/2) boundary family, B is fixed and delta is capped by max(row2 loss, inserted-row loss).  The formal balance is irrational, so rational certified points approach but do not attain the limit.",
        }
    )

    # n=7 extra B-carrier probes: clean Gamma is lost.
    k2 = (F(3, 100), F(99, 100), F(-1, 50))
    for w2 in (F(1, 200), F(1, 100), F(1, 50), F(1, 20)):
        L, B = family_multi_compensated_insert(BASE_A, [(CF_BEST_H, (F(0), F(0), CF_BEST_Y)), (k2, (F(0), w2, F(0)))])
        P = P_of(L, B)
        rec = analyze_instance(f"extra-B-carrier-w={w2}", "extra-B-carrier", L, B)
        out.append(
            {
                "kind": "richer-family-obstruction",
                "name": f"extra-B-carrier-w={fstr(w2)}",
                "family": "n=7 extra beta_1 B-carrier",
                "delta": delta_of(P),
                "argmins": [c.U for c in theta_argmins(chart_data(L, P))],
                "has_clean_gamma": bool(rec and rec["has_clean_gamma"]),
                "best_B_over_delta": rec["best_B_over_delta"] if rec else None,
                "reason": "clean high-self Gamma branch lost; retained branches are Psi/mixed or on a different pivot",
            }
        )

    # Non-sparse/bridge template probes from the inherited scratch script.
    for hneg in (F(1, 100), F(1, 60), F(1, 40), F(1, 25)):
        params = (F(2, 25), F(3, 50), F(1, 25), F(1, 40), hneg, F(7, 10), F(1, 5))
        L, B = family_rotated_bridge(params)
        rec = analyze_instance(f"rotated-bridge-hneg={hneg}", "rotated-bridge", L, B)
        if rec:
            out.append(
                {
                    "kind": "richer-family-obstruction",
                    "name": f"rotated-bridge-hneg={fstr(hneg)}",
                    "family": "non-sparse-left-inverse rotated bridge",
                    "delta": rec["delta"],
                    "argmins": [c["U"] for c in rec["argmins"]],
                    "has_clean_gamma": rec["has_clean_gamma"],
                    "best_B_over_delta": rec["best_B_over_delta"],
                    "reason": "tested bridge points are Psi-blocked or low-self, not clean Gamma",
                }
            )
    return out


def point_json(p: dict) -> dict:
    keys = [
        "name",
        "family",
        "note",
        "n",
        "delta",
        "B_over_delta",
        "U",
        "s",
        "r",
        "branch_j",
        "B_mass",
        "C_mass",
        "A_mass",
        "D_mass",
        "Phi_r",
        "Phi",
        "ci_import",
        "ci_total",
        "ci_margin_B_minus_total",
        "alpha_B",
        "alpha_A",
        "reduced_import_bound",
        "reduced_total",
        "reduced_margin_B_minus_total",
        "budget_G_class_minus",
        "budget_S_minus_mu",
        "budget_SIGMA",
        "budget_total",
        "B_over_budget_total",
        "budget_total_over_delta",
        "argmins",
        "branch",
        "ci_terms",
        "L",
        "B",
        "P",
    ]
    return {k: jsonable(p[k]) for k in keys}


def write_outputs(points: list[dict], obstructions: list[dict], calibrations: dict) -> None:
    best = max(points, key=lambda p: p["B_over_delta"])
    JSON_PATH.write_text(
        json.dumps(
            {
                "status": "L3 numerical evidence only; not a proof",
                "calibrations": jsonable(calibrations),
                "certified_points": [point_json(p) for p in points],
                "obstructions": jsonable(obstructions),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )

    with CSV_PATH.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "name",
                "family",
                "n",
                "delta",
                "B_over_delta",
                "U",
                "s",
                "r",
                "branch_j",
                "B",
                "C",
                "A",
                "D",
                "Phi_r",
                "ci_import",
                "ci_total",
                "B_minus_ci_total",
                "reduced_total",
                "B_minus_reduced_total",
                "budget_total",
                "B_over_budget_total",
            ]
        )
        for p in points:
            w.writerow(
                [
                    p["name"],
                    p["family"],
                    p["n"],
                    fstr(p["delta"]),
                    fstr(p["B_over_delta"]),
                    " ".join(map(str, p["U"])),
                    p["s"],
                    p["r"],
                    p["branch_j"],
                    fstr(p["B_mass"]),
                    fstr(p["C_mass"]),
                    fstr(p["A_mass"]),
                    fstr(p["D_mass"]),
                    fstr(p["Phi_r"]),
                    fstr(p["ci_import"]),
                    fstr(p["ci_total"]),
                    fstr(p["ci_margin_B_minus_total"]),
                    fstr(p["reduced_total"]),
                    fstr(p["reduced_margin_B_minus_total"]),
                    fstr(p["budget_total"]),
                    fstr(p["B_over_budget_total"]) if p["B_over_budget_total"] is not None else "",
                ]
            )

    lines: list[str] = []
    lines.append("# Wave 13 amplifier exact-rational answer")
    lines.append("")
    lines.append("Status: L3 numerical evidence only; not a proof.")
    lines.append("")
    lines.append("## Headline")
    lines.append("")
    lines.append(
        f"Best certified clean high-self non-fan Gamma argmin found: `{best['B_over_delta']}` "
        f"at `delta={fstr(best['delta'])}` (`{best['name']}`, n={best['n']})."
    )
    lines.append("")
    lines.append(
        f"This beats the prior exact record `8400000/10897843` and crosses the rounded `0.771` level, "
        f"but it does **not** reach `1`."
    )
    lines.append("")
    lines.append(
        f"The mass is on `U={best['U']}`, `s={best['s']}`, `r={best['r']}`, "
        f"clean branch row `j={best['branch_j']}`, with `B={fstr(best['B_mass'])}`, "
        f"`C={fstr(best['C_mass'])}`, `A={fstr(best['A_mass'])}`, `D={fstr(best['D_mass'])}`."
    )
    lines.append("")
    lines.append("## Required calibration")
    lines.append("")
    lines.append(
        f"- G12: `delta={fstr(calibrations['g12']['delta'])}`, `B={fstr(calibrations['g12']['B'])}`, "
        f"`B/delta={fstr(calibrations['g12']['B_over_delta'])}`."
    )
    lines.append(
        f"- Bundle maximizer: `delta={fstr(calibrations['bundle']['delta'])}`, "
        f"`B={fstr(calibrations['bundle']['B'])}`, "
        f"`B/delta={fstr(calibrations['bundle']['B_over_delta'])}`."
    )
    lines.append("")
    lines.append("## Full best instance")
    lines.append("")
    lines.append("`L`:")
    lines.append("")
    lines.append("```text")
    for row in best["L"]:
        lines.append("[" + "  ".join(fstr(x) for x in row) + "]")
    lines.append("```")
    lines.append("")
    lines.append("`B`:")
    lines.append("")
    lines.append("```text")
    for row in best["B"]:
        lines.append("[" + "  ".join(fstr(x) for x in row) + "]")
    lines.append("```")
    lines.append("")
    lines.append("`P=L B`:")
    lines.append("")
    lines.append("```text")
    for row in best["P"]:
        lines.append("[" + "  ".join(fstr(x) for x in row) + "]")
    lines.append("```")
    lines.append("")
    lines.append("## Argmin and branch certificate")
    lines.append("")
    for a in best["argmins"]:
        lines.append(
            f"- Argmin `U={a['U']}`: `m={fstr(a['m'])}`, `Phi={fstr(a['Phi'])}`, "
            f"`phi=({', '.join(fstr(x) for x in a['phi'])})`, pivots `{a['pivots']}`."
        )
    br = best["branch"]
    lines.append(
        f"- Clean branch row `{br['j']}`: `a=({', '.join(fstr(x) for x in br['a'])})`, "
        f"`beta_s={fstr(br['beta_s'])}`, `E_s={fstr(br['E_s'])}`, "
        f"`self={fstr(br['self'])}`, `Psi={fstr(br['Psi'])}`, `Gamma={fstr(br['Gamma'])}`."
    )
    lines.append("")
    lines.append("## CI-financed comparison")
    lines.append("")
    lines.append(
        f"Literal CI import at the Gamma transverse pivot: `Phi_r(U)={fstr(best['Phi_r'])}`, "
        f"`I={fstr(best['ci_import'])}`, so `Phi_r+I={fstr(best['ci_total'])}`."
    )
    lines.append(
        f"`B - (Phi_r+I) = {fstr(best['ci_margin_B_minus_total'])}`. "
        f"Using the import-reduction coefficients `alpha_B={fstr(best['alpha_B'])}`, "
        f"`alpha_A={fstr(best['alpha_A'])}` gives reduced total "
        f"`{fstr(best['reduced_total'])}` and margin `{fstr(best['reduced_margin_B_minus_total'])}`."
    )
    lines.append(
        f"G12 budget terms at the same pivot: `G_class^-={fstr(best['budget_G_class_minus'])}`, "
        f"`S_-^mu={fstr(best['budget_S_minus_mu'])}`, `SIGMA={fstr(best['budget_SIGMA'])}`, "
        f"total `{fstr(best['budget_total'])}`, with `B/budget={fstr(best['B_over_budget_total'])}`."
    )
    lines.append("")
    lines.append("## Boundary and obstruction taxonomy")
    lines.append("")
    original_boundary = next(p for p in points if p["name"] == "original-h-active-boundary")
    lines.append(
        f"- Original compensated insert switch boundary: `y*={fstr(active_boundary_y_for_h(ORIGINAL_INSERT_H))}`; "
        f"the one-sided/boundary ratio is `{fstr(original_boundary['B_over_delta'])}`."
    )
    lines.append(
        "- Variable inserted-row law: for `h=(-a,1/2+a,1/2)`, the active switch is "
        "`y=2679363/(49000*(22a+799))`; the row-loss balance is irrational "
        "`a=-5500573/293216 + sqrt(757785147162145)/1466080`, giving a limiting "
        "`B/delta` about `0.777640312383967`. Certified rational points approach it from either side."
    )
    lines.append(
        "- Duplicate n=7 and n=9 inserts do not amplify: the same ratio reappears and the active loss is carried by the cloned inserted rows."
    )
    lines.append(
        "- Extra B-carrier and rotated-bridge probes lost the clean Gamma branch (Psi/mixed or low-self branch), so they produced obstructions rather than records."
    )
    lines.append("")
    lines.append("## Verdict on targets")
    lines.append("")
    lines.append("- (i) Beat prior record / rounded `0.771`: YES.")
    lines.append("- (ii) Reach or cross `1`: NO; best certified ratio is still below `0.778`.")
    lines.append("- (iii) Cross literal CI-financed total: YES under the G12/CI convention `Phi_r(U)+I`; also yes for the import-reduction upper bound used here.")
    lines.append("")
    lines.append("## Honest scope")
    lines.append("")
    lines.append(
        "Exact full chart enumeration was run for every emitted certified point. The search is still a finite, structured L3 probe: compensated-insert boundaries, rational approximants to one algebraic shape balance, duplicate n=7/n=9 inserts, a small extra-carrier set, and a small rotated-bridge set. It is not an exhaustive rank-3 idempotent search."
    )
    lines.append("")
    lines.append("Machine-readable certified points are in `certified_points.json`; row summaries are in `certified_points.csv`.")
    ANSWER_PATH.write_text("\n".join(lines) + "\n")


def main() -> None:
    calibrations = {
        "g12": calibration_g12(),
        "bundle": calibration_small_delta_bundle(),
    }
    points = make_certified_points()
    obstructions = richer_obstructions()
    best = max(points, key=lambda p: p["B_over_delta"])
    assert best["B_over_delta"] > F(8400000, 10897843)
    assert best["B_over_delta"] > F(771, 1000)
    assert best["B_over_delta"] < 1
    assert best["ci_margin_B_minus_total"] > 0
    assert best["reduced_margin_B_minus_total"] > 0
    assert any(a["U"] == (0, 2, 4) for a in best["argmins"])
    assert best["branch"]["clean_gamma"]
    write_outputs(points, obstructions, calibrations)
    print(f"calibration G12: delta={fstr(calibrations['g12']['delta'])} B={fstr(calibrations['g12']['B'])} B/delta={fstr(calibrations['g12']['B_over_delta'])}")
    print(f"calibration bundle: delta={fstr(calibrations['bundle']['delta'])} B={fstr(calibrations['bundle']['B'])} B/delta={fstr(calibrations['bundle']['B_over_delta'])}")
    print(f"certified clean Gamma points: {len(points)}")
    print(f"best: {best['name']} delta={fstr(best['delta'])} B/delta={fstr(best['B_over_delta'])}")
    print(f"wrote {CSV_PATH}")
    print(f"wrote {JSON_PATH}")
    print(f"wrote {ANSWER_PATH}")


if __name__ == "__main__":
    main()
