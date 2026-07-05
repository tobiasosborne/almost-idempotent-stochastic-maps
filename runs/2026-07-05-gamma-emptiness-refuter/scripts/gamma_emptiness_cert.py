#!/usr/bin/env python3
"""Wave 15 exact checker for capped Gamma-emptiness.

All arithmetic is fractions.Fraction.  Floats are used only in optional
display helpers, never in assertions.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JSON_OUT = ROOT / "certificate.json"
REPORT_OUT = ROOT / "REPORT.md"


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


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
        raise ValueError("singular chart")
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


def coordinates(L: list[list[F]], U: tuple[int, int, int], i: int) -> tuple[F, F, F]:
    return tuple(row_times_mat(L[i], inv3([L[u] for u in U])))  # type: ignore[return-value]


def row_neg(row: list[F]) -> F:
    return sum(neg(x) for x in row)


def delta_of(P: list[list[F]]) -> F:
    return max(row_neg(row) for row in P)


def P_of(L: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    I3 = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    assert matmul(B, L) == I3, "B*L=I3"
    P = matmul(L, B)
    assert matmul(P, P) == P, "P^2=P"
    assert sum(P[i][i] for i in range(len(P))) == 3, "rank/trace is 3"
    assert all(sum(row) == 1 for row in P), "all row sums are 1"
    return P


def E_of(a: tuple[F, F, F], r: int) -> F:
    return pos(sum(neg(a[q]) for q in range(3) if q != r) - (1 - a[r]))


@dataclass(frozen=True)
class Chart:
    U: tuple[int, int, int]
    volume: F
    m: F
    phi: tuple[F, F, F]
    Phi: F
    coords: tuple[tuple[F, F, F], ...]


def chart_data(L: list[list[F]], P: list[list[F]]) -> list[Chart]:
    vols: dict[tuple[int, int, int], F] = {}
    for U in combinations(range(len(L)), 3):
        v = abs(det3([L[u] for u in U]))
        if v > 0:
            vols[U] = v
    vmax = max(vols.values())
    out: list[Chart] = []
    for U, v in vols.items():
        coords = tuple(coordinates(L, U, i) for i in range(len(L)))
        phi = tuple(
            sum(pos(P[U[r]][i]) * E_of(coords[i], r) for i in range(len(L)))
            for r in range(3)
        )
        out.append(Chart(U, v, v / vmax, phi, max(phi), coords))
    return sorted(out, key=lambda c: (c.Phi, c.U))


def theta_charts(charts: list[Chart]) -> list[Chart]:
    return [c for c in charts if c.m >= F(1, 2)]


def theta_argmins(charts: list[Chart]) -> list[Chart]:
    eligible = theta_charts(charts)
    best = min(c.Phi for c in eligible)
    return [c for c in eligible if c.Phi == best]


def pivot_phi(
    L: list[list[F]], P: list[list[F]], U: tuple[int, int, int], s: int, j: int
) -> tuple[tuple[int, int, int], tuple[F, F, F]]:
    V = list(U)
    V[s] = j
    Vt = tuple(V)  # chart ordering is part of the coordinate convention
    coords = tuple(coordinates(L, Vt, i) for i in range(len(L)))
    phi = tuple(
        sum(pos(P[Vt[r]][i]) * E_of(coords[i], r) for i in range(len(L)))
        for r in range(3)
    )
    return Vt, phi


def mass_A(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(pos(P[U[r]][i]) * pos(coords[i][s]) for i in range(len(P)))


def mass_B(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(pos(P[U[r]][i]) * neg(coords[i][s]) for i in range(len(P)))


def mass_C(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(neg(P[U[r]][i]) * pos(coords[i][s]) for i in range(len(P)))


def mass_D(P: list[list[F]], coords: tuple[tuple[F, F, F], ...], U: tuple[int, int, int], r: int, s: int) -> F:
    return sum(neg(P[U[r]][i]) * neg(coords[i][s]) for i in range(len(P)))


def ci_import(
    P: list[list[F]],
    coords: tuple[tuple[F, F, F], ...],
    U: tuple[int, int, int],
    s: int,
    r: int,
    j: int,
) -> tuple[F, F, F, F, F, F]:
    t = next(q for q in range(3) if q not in (r, s))
    c = coords[j][s]
    d_r = coords[j][r]
    d_t = coords[j][t]
    assert c > 0
    total = F(0)
    for i, a in enumerate(coords):
        R = (1 / c - 1) * neg(a[s]) + pos(a[s] * d_t / c) - a[s] * d_r / c
        total += pos(P[U[r]][i]) * pos(R)
    alpha_B = (pos(1 - c) + neg(d_t) + pos(d_r)) / c
    alpha_A = (pos(d_t) + neg(d_r)) / c
    return total, c, d_r, d_t, alpha_B, alpha_A


def matrix_json(M: list[list[F]]) -> list[list[str]]:
    return [[fstr(x) for x in row] for row in M]


def chart_json(charts: list[Chart]) -> list[dict]:
    return [
        {
            "U": list(c.U),
            "volume": fstr(c.volume),
            "m": fstr(c.m),
            "phi": [fstr(x) for x in c.phi],
            "Phi": fstr(c.Phi),
        }
        for c in charts
    ]


def g10_witness() -> dict:
    L = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(3, 5), F(-2, 5), F(4, 5)],
        [F(-1, 5), F(4, 5), F(2, 5)],
    ]
    B = [
        [F(2, 5), F(13, 30), F(-23, 30), F(59, 60), F(-1, 20)],
        [F(23, 100), F(12, 25), F(-3, 50), F(-1, 5), F(11, 20)],
        [F(-3, 20), F(-1, 5), F(1, 2), F(2, 5), F(9, 20)],
    ]
    P = P_of(L, B)
    assert delta_of(P) == F(49, 60)
    th = theta_charts(chart_data(L, P))
    expected = {
        (0, 1, 2): (F(1), (F(0), F(0), F(2, 25))),
        (0, 3, 4): (F(4, 5), (F(0), F(0), F(163, 1500))),
        (0, 2, 4): (F(4, 5), (F(0), F(1, 5), F(163, 1000))),
        (1, 2, 3): (F(3, 5), (F(23, 100), F(0), F(7, 125))),
        (0, 1, 3): (F(4, 5), (F(0), F(11, 40), F(0))),
    }
    assert {c.U for c in th} == set(expected)
    for cdata in th:
        vol, phi = expected[cdata.U]
        assert cdata.volume == vol and cdata.phi == phi
    arg = theta_argmins(chart_data(L, P))
    assert len(arg) == 1 and arg[0].U == (0, 1, 2)
    cd = arg[0]
    V, phiV = pivot_phi(L, P, cd.U, 2, 3)
    assert V == (0, 1, 3)
    assert phiV == (F(0), F(11, 40), F(0))
    assert phiV[2] < cd.Phi <= max(phiV[0], phiV[1])
    return {
        "delta": fstr(delta_of(P)),
        "argmin": list(cd.U),
        "M": fstr(cd.Phi),
        "branch": {"s": 2, "j": 3, "V": list(V), "Psi": fstr(phiV[2]), "Gamma": fstr(max(phiV[0], phiV[1]))},
        "theta_charts": chart_json(th),
    }


def g11_near_miss() -> dict:
    L = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(3, 5), F(-2, 5), F(4, 5)],
        [F(-1, 5), F(4, 5), F(2, 5)],
    ]
    B = [
        [F(169, 200), F(7, 100), F(-6, 25), F(11, 40), F(1, 20)],
        [F(9, 40), F(1, 2), F(-1, 20), F(-1, 5), F(21, 40)],
        [F(-1, 4), F(0), F(1, 2), F(1, 2), F(1, 4)],
    ]
    P = P_of(L, B)
    assert delta_of(P) == F(1, 4)
    th = theta_charts(chart_data(L, P))
    expected = {
        (0, 1, 2): (F(1), (F(0), F(0), F(1, 10))),
        (0, 1, 3): (F(4, 5), (F(0), F(21, 80), F(69, 250))),
        (0, 2, 4): (F(4, 5), (F(0), F(1, 4), F(579, 2000))),
        (0, 3, 4): (F(4, 5), (F(0), F(69, 500), F(193, 1000))),
        (1, 2, 3): (F(3, 5), (F(9, 40), F(0), F(217, 500))),
    }
    assert {c.U for c in th} == set(expected)
    for cdata in th:
        vol, phi = expected[cdata.U]
        assert cdata.volume == vol and cdata.phi == phi
    arg = theta_argmins(chart_data(L, P))
    assert len(arg) == 1 and arg[0].U == (0, 1, 2)
    cd = arg[0]
    V, phiV = pivot_phi(L, P, cd.U, 2, 3)
    assert V == (0, 1, 3)
    assert phiV == (F(0), F(21, 80), F(69, 250))
    assert cd.Phi == F(1, 10)
    assert phiV[2] > cd.Phi and max(phiV[0], phiV[1]) > cd.Phi
    return {
        "delta": fstr(delta_of(P)),
        "argmin": list(cd.U),
        "M": fstr(cd.Phi),
        "branch": {
            "s": 2,
            "j": 3,
            "V": list(V),
            "Psi": fstr(phiV[2]),
            "Gamma": fstr(max(phiV[0], phiV[1])),
            "failure_margin_Psi_minus_M": fstr(phiV[2] - cd.Phi),
        },
        "theta_charts": chart_json(th),
    }


def capped_refuter() -> dict:
    L = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(2, 25), F(-3, 50), F(49, 50)],
        [F(1, 25), F(197, 200), F(-1, 40)],
        [F(-1, 100), F(51, 100), F(1, 2)],
    ]
    B = [
        [F(1), F(0), F(0), F(0), F(0), F(0)],
        [F(-1, 50), F(203, 400), F(1, 80), F(0), F(1, 2), F(0)],
        [F(-55319, 1000000), F(7269, 1000000), F(5599, 20000), F(7, 10), F(0), F(681, 10000)],
    ]
    P = P_of(L, B)
    delta = delta_of(P)
    assert F(0) < delta <= F(1, 4)
    assert delta == F(55319, 1000000)
    charts = chart_data(L, P)
    th = theta_charts(charts)
    expected_theta = {
        (0, 2, 4): (F(197, 200), (F(0), F(679, 24625), F(219870541, 7880000000))),
        (0, 1, 3): (F(49, 50), (F(0), F(11, 2450), F(273601, 9800000))),
        (0, 1, 2): (F(1), (F(0), F(1, 200), F(7, 250))),
        (0, 3, 4): (F(4819, 5000), (F(0), F(2188808, 75296875), F(5736622297, 192760000000))),
        (0, 3, 5): (F(2649, 5000), (F(0), F(4651217, 441500000), F(1629659223, 1766000000))),
        (0, 4, 5): (F(2021, 4000), (F(0), F(579658699, 40420000000), F(39261793, 40420000))),
        (0, 2, 5): (F(51, 100), (F(0), F(931, 8500), F(33986577, 34000000))),
        (0, 1, 5): (F(1, 2), (F(0), F(121, 4000), F(1002487, 1000000))),
    }
    assert {c.U for c in th} == set(expected_theta)
    for cdata in th:
        vol, phi = expected_theta[cdata.U]
        assert cdata.volume == vol and cdata.phi == phi
    arg = theta_argmins(charts)
    assert len(arg) == 1 and arg[0].U == (0, 2, 4)
    cd = arg[0]
    s = 2
    j = 1
    assert cd.phi[s] == cd.Phi
    assert cd.phi[0] < cd.Phi and cd.phi[1] < cd.Phi
    assert cd.coords[j] == (F(-8, 197), F(5, 197), F(200, 197))
    assert abs(cd.coords[j][s]) * cd.m == F(1)
    V, phiV = pivot_phi(L, P, cd.U, s, j)
    assert V == (0, 2, 1)
    assert phiV == (F(0), F(7, 250), F(1, 200))
    psi = phiV[s]
    gamma = max(phiV[r] for r in range(3) if r != s)
    assert psi < cd.Phi <= gamma
    assert P[j][j] == F(203, 400) > F(1, 2)
    assert E_of(cd.coords[j], s) == F(11, 197)
    r = 1
    A = mass_A(P, cd.coords, cd.U, r, s)
    Bmass = mass_B(P, cd.coords, cd.U, r, s)
    C = mass_C(P, cd.coords, cd.U, r, s)
    D = mass_D(P, cd.coords, cd.U, r, s)
    assert A == F(42, 985) and Bmass == F(42, 985) and C == 0 and D == 0
    assert A == Bmass + C - D
    assert C <= 2 * delta
    I, c, d_r, d_t, alpha_B, alpha_A = ci_import(P, cd.coords, cd.U, s, r, j)
    assert (c, d_r, d_t) == (F(200, 197), F(5, 197), F(-8, 197))
    assert I == F(21, 9850)
    assert alpha_B == F(13, 200) and alpha_A == 0
    assert I >= cd.Phi - cd.phi[r]
    return {
        "L": matrix_json(L),
        "B_left_inverse": matrix_json(B),
        "P": matrix_json(P),
        "delta": fstr(delta),
        "row_negative_masses": [fstr(row_neg(row)) for row in P],
        "theta_charts": chart_json(th),
        "argmin": {"U": list(cd.U), "m": fstr(cd.m), "phi": [fstr(x) for x in cd.phi], "M": fstr(cd.Phi)},
        "branch": {
            "s": s,
            "j": j,
            "a_j": [fstr(x) for x in cd.coords[j]],
            "V": list(V),
            "phiV": [fstr(x) for x in phiV],
            "Psi": fstr(psi),
            "Gamma": fstr(gamma),
            "M_minus_Psi": fstr(cd.Phi - psi),
            "Gamma_minus_M": fstr(gamma - cd.Phi),
            "theta_admissibility_product": fstr(abs(cd.coords[j][s]) * cd.m),
            "P_jj": fstr(P[j][j]),
            "E_s_j": fstr(E_of(cd.coords[j], s)),
        },
        "import_anatomy": {
            "r": r,
            "A": fstr(A),
            "B": fstr(Bmass),
            "C": fstr(C),
            "D": fstr(D),
            "ci_import": fstr(I),
            "c": fstr(c),
            "d_r": fstr(d_r),
            "d_t": fstr(d_t),
            "alpha_B": fstr(alpha_B),
            "alpha_A": fstr(alpha_A),
            "M_minus_Phi_r": fstr(cd.Phi - cd.phi[r]),
        },
    }


def build_report(data: dict) -> str:
    ref = data["capped_refuter"]
    lines = [
        "# Wave 15 Gamma-emptiness exact report",
        "",
        "Verdict: REFUTED (T0 exact certified counterexample to the unqualified contract).",
        "",
        "Rerun command: `python3 waves-scratch/w15-gamma-emptiness/gamma_emptiness_cert.py`.",
        "",
        "## Refuter",
        "",
        "Coordinate rows `L`:",
        "",
        "```text",
        *["[" + ", ".join(row) + "]" for row in ref["L"]],
        "```",
        "",
        "Left inverse `B` (`B L = I_3`):",
        "",
        "```text",
        *["[" + ", ".join(row) + "]" for row in ref["B_left_inverse"]],
        "```",
        "",
        "`P = L B`:",
        "",
        "```text",
        *["[" + ", ".join(row) + "]" for row in ref["P"]],
        "```",
        "",
        f"Row negative masses: `{ref['row_negative_masses']}`.",
        "",
        f"`delta(P) = {ref['delta']} <= 1/4`; the unique theta-half Phi-argmin is `U={tuple(ref['argmin']['U'])}` with `Phi={ref['argmin']['phi']}` and maximal pivot `s={ref['branch']['s']}`.",
        f"For non-chart row `j={ref['branch']['j']}`, old coordinates are `a(j)={ref['branch']['a_j']}`, and `|a_s(j)|m_U={ref['branch']['theta_admissibility_product']}`.",
        f"The pivot-removing chart is `V={tuple(ref['branch']['V'])}` with `Phi(V)={ref['branch']['phiV']}`.",
        f"Thus `Psi_j={ref['branch']['Psi']} < M={ref['argmin']['M']} <= Gamma_j={ref['branch']['Gamma']}`.",
        f"Margins: `M-Psi={ref['branch']['M_minus_Psi']}`, `Gamma-M={ref['branch']['Gamma_minus_M']}`.",
        "",
        "## Complete theta-half enumeration for the refuter",
        "",
        "| chart | volume | m | Phi vector | max Phi |",
        "|---|---:|---:|---:|---:|",
    ]
    for c in ref["theta_charts"]:
        lines.append(
            f"| `{tuple(c['U'])}` | `{c['volume']}` | `{c['m']}` | `{tuple(c['phi'])}` | `{c['Phi']}` |"
        )
    lines.extend(
        [
            "",
            "## Proof-side residual",
            "",
            "The validated c>0 import machinery gives only",
            "`M - Phi_r(U) <= I_{r,j} <= alpha_B B_{r,s} + alpha_A A_{r,s}`.",
            "Using `A=B+C-D` and `C<=2 delta` gives the residual inequality",
            "`M-Phi_r(U) <= (alpha_B+alpha_A)B_{r,s}+2 alpha_A delta`.",
            "With the theta-half Cramer box `c>=1/2`, `|d_r|,|d_t|<=2`, this only yields",
            "`M-Phi_r(U) <= 17 B_{r,s}+16 delta` in the worst c>0 case.",
            "For c<0, the reviewed equality-form split gives",
            "`M-Phi_r(U) <= (gamma_A+gamma_B)B_{r,s}+2 gamma_A delta`,",
            "where `gamma_A=((1+d_t^-+d_r)^+)/(-c)` and",
            "`gamma_B=(((d_t^+-d_r)/(-c)-1)^+)`; the same box gives at best",
            "`M-Phi_r(U) <= 17 B_{r,s}+20 delta`.",
            "For the refuter, `alpha_B=13/200`, `alpha_A=0`, `B=42/985`,",
            f"`I={ref['import_anatomy']['ci_import']}`, while `M-Phi_r(U)={ref['import_anatomy']['M_minus_Phi_r']}`.",
            "So the current proof route has no contradiction; it needs a real bound on `B_{r,s}` or a stronger Gamma-specific principle.",
            "",
            "## Calibration / near miss",
            "",
            f"G10 witness reconstructed with `delta={data['g10']['delta']}` and clean Gamma margins outside the cap.",
            f"G11 capped near miss has `delta={data['g11_near_miss']['delta']}` but fails clean Gamma by `Psi-M={data['g11_near_miss']['branch']['failure_margin_Psi_minus_M']}`.",
            "",
            "## Hard asserts",
            "",
            "- For every matrix: `B_left*L=I3`, `P=L*B_left`, `P^2=P`, and every row sum is `1`.",
            "- Explicit `trace(P)=3`, hence rank `3` for the idempotent.",
            "- Exact `delta(P)` and row-negative masses for the refuter.",
            "- Complete theta-half chart enumeration for G10, G11 near miss, and the refuter.",
            "- Unique argmin and maximal pivot for the refuter.",
            "- Pivot-removing chart, transformed coordinates, `Psi`, `Gamma`, and clean inequalities.",
            "- Cross-pivot cancellation `A=B+C-D`, `C<=2 delta`, and literal CI import values.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    data = {
        "g10": g10_witness(),
        "g11_near_miss": g11_near_miss(),
        "capped_refuter": capped_refuter(),
    }
    JSON_OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    REPORT_OUT.write_text(build_report(data))
    print("[gamma-emptiness] exact certificate OK")
    print(f"wrote {JSON_OUT}")
    print(f"wrote {REPORT_OUT}")


if __name__ == "__main__":
    main()
