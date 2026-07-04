#!/usr/bin/env python3
"""Exact-rational small/mid-delta decider for the G12 B-question.

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
    return sum(P[U[r]][i] * neg(coords[i][s]) for i in range(len(P)))


def D_mass(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(neg(P[U[r]][i]) * neg(coords[i][s]) for i in range(len(P)))


def budget(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], s: int) -> tuple[F, F, F, F]:
    Bset = [i for i in range(len(P)) if i not in U]
    Gc = sum(neg(P[U[s]][u]) for u in U)
    Smu = sum(neg(P[U[s]][i]) * sum(neg(coords[i][q]) for q in range(3) if q != s) for i in Bset)
    SIG = sum(P[U[s]][i] * row_neg(P[i]) for i in Bset if P[U[s]][i] > 0)
    return Gc, Smu, SIG, Gc + Smu + SIG


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


def write_outputs(records: list[dict], amp: list[dict], calib: dict) -> None:
    JSON_PATH.write_text(
        json.dumps(
            {
                "calibration": {k: fstr(v) for k, v in calib.items()},
                "records": [serialize_rec(r) for r in records],
                "amplification_failures": jsonable(amp),
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
                "delta",
                "U",
                "s",
                "r",
                "B",
                "C",
                "A",
                "D",
                "B_over_delta",
                "clean_gamma_js",
                "gamma_js",
            ]
        )
        for rec in records:
            for c in rec["argmins"]:
                clean_js = [str(b["j"]) for b in c["branches"] if b["clean_gamma"]]
                gamma_js = [str(b["j"]) for b in c["branches"] if b["branch_type"] == "Gamma"]
                for m in c["masses"]:
                    w.writerow(
                        [
                            rec["name"],
                            rec["family"],
                            fstr(rec["delta"]),
                            " ".join(map(str, c["U"])),
                            m["s"],
                            m["r"],
                            fstr(m["B"]),
                            fstr(m["C"]),
                            fstr(m["A"]),
                            fstr(m["D"]),
                            fstr(m["B_over_delta"]),
                            " ".join(clean_js),
                            " ".join(gamma_js),
                        ]
                    )
    best = max(records, key=lambda r: r["best_B_over_delta"])
    best_mass = None
    best_chart = None
    for c in best["argmins"]:
        for m in c["masses"]:
            if m["B_over_delta"] == best["best_B_over_delta"]:
                best_mass = m
                best_chart = c
                break
        if best_mass:
            break
    assert best_mass and best_chart
    lines = []
    lines.append("# Exact-rational small/mid-delta B-decider")
    lines.append("")
    lines.append("Status: L3 numerical evidence only; not a proof.")
    lines.append("")
    lines.append("## Headline")
    lines.append("")
    lines.append(
        f"Max certified `B/delta` observed with `delta < 3/20` is "
        f"`{fstr(best['best_B_over_delta'])}` at `delta={fstr(best['delta'])}` "
        f"({best['family']})."
    )
    lines.append("")
    lines.append(
        f"The maximizing mass is on `U={best_chart['U']}`, `s={best_mass['s']}`, "
        f"`r={best_mass['r']}` with `B={fstr(best_mass['B'])}` and "
        f"`C={fstr(best_mass['C'])}`."
    )
    lines.append("")
    lines.append("Calibration assert: the G12 instance recomputes `delta=1/4`, `B=2/57`, `B/delta=8/57`.")
    lines.append("")
    lines.append("## Full Maximizing Instance")
    lines.append("")
    lines.append(f"Family: `{best['family']}`")
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
    lines.append("## Certified Argmins and Branches")
    lines.append("")
    for rec in records:
        lines.append(
            f"- `{rec['name']}`: delta `{fstr(rec['delta'])}`, best B/delta "
            f"`{fstr(rec['best_B_over_delta'])}`, clean Gamma `{rec['has_clean_gamma']}`."
        )
        for c in rec["argmins"]:
            lines.append(f"  Argmin `U={c['U']}`, volume `{fstr(c['volume'])}`, m `{fstr(c['m'])}`, phi `{tuple(fstr(x) for x in c['phi'])}`.")
            for b in c["branches"]:
                if b["branch_type"] == "Gamma" or b["clean_gamma"]:
                    lines.append(
                        f"  Branch row `{b['j']}`: type `{b['branch_type']}`, clean `{b['clean_gamma']}`, "
                        f"self `{fstr(b['self'])}`, beta_s `{fstr(b['beta_s'])}`, E_s `{fstr(b['E_s'])}`, "
                        f"Psi `{fstr(b['Psi']) if b['Psi'] is not None else 'NA'}`, "
                        f"Gamma `{fstr(b['Gamma']) if b['Gamma'] is not None else 'NA'}`."
                    )
    lines.append("")
    lines.append("The complete machine-readable list is in `certified_points.json`; row-level masses are in `certified_points.csv`.")
    lines.append("")
    lines.append("## Amplification Attempts and Obstructions")
    lines.append("")
    for a in amp:
        if a["kind"] == "non_argmin_amplifier":
            lines.append(
                f"- Non-argmin amplifier eps `{fstr(a['eps'])}`: base-chart delta `{fstr(a['delta'])}`, "
                f"B/delta `{fstr(a['B_over_delta'])}`, but theta-half argmin switches to "
                f"`U={a['argmin_U']}` with Phi `{fstr(a['argmin_Phi'])}` while base Phi is `{fstr(a['base_Phi'])}`."
            )
        else:
            reason = "clean Gamma lost"
            branches = a.get("branches", [])
            if branches:
                b = branches[0]
                reason = (
                    f"argmin `{a['argmins'][0]}` branch row `{b['j']}` is `{b['branch_type']}`, "
                    f"high-self `{b['high_self']}`"
                )
            lines.append(
                f"- `{a['name']}` ({a['family']}): delta `{fstr(a['delta'])}`, "
                f"argmins `{a['argmins']}`; obstruction: {reason}."
            )
    lines.append("")
    lines.append(
        "- Grid amplification inside the two certified families was obstructed by either the theta-half "
        "argmin switching away from the designed chart, the branch becoming Psi/mixed instead of Gamma, "
        "loss of high-self (`P_jj <= 1/2`), or delta leaving `[1/100,3/20]`."
    )
    lines.append("")
    lines.append("## Honest Scope")
    lines.append("")
    lines.append(
        "Covered exactly two construction families: a 5-row two-carrier sparse-left-inverse family and a "
        "6-row compensated-insertion family that adds one actual row and preserves `BL=I` by identity-column "
        "compensation. Both enumerate all actual-row charts for each retained instance; the maximizing "
        "6-row records enumerate 20 charts."
    )
    lines.append("")
    lines.append(
        "The retained points and obstruction probes are the finite rational parameter list encoded in "
        "`decider_small_delta.py` (including the inserted-weight boundary near `681/10000`). This is not "
        "an exhaustive search over rank-3 idempotents or over all support patterns."
    )
    ANSWER_PATH.write_text("\n".join(lines) + "\n")


def main() -> None:
    calib = calibration_g12()
    records = certified_candidate_records()
    amp = amplification_obstructions()
    write_outputs(records, amp, calib)
    print(f"calibration: delta={fstr(calib['delta'])} B={fstr(calib['B'])} B/delta={fstr(calib['B_over_delta'])}")
    print(f"certified clean Gamma records: {len(records)}")
    best = max(records, key=lambda r: r["best_B_over_delta"])
    print(f"best: {best['family']} delta={fstr(best['delta'])} B/delta={fstr(best['best_B_over_delta'])}")
    print(f"wrote {CSV_PATH}")
    print(f"wrote {JSON_PATH}")
    print(f"wrote {ANSWER_PATH}")


if __name__ == "__main__":
    main()
