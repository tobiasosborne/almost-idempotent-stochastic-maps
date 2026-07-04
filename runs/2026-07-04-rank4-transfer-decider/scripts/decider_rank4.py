#!/usr/bin/env python3
"""Rank-4 exact-rational numerics decider.

L3 evidence only.  Certified quantities use fractions.Fraction throughout.
Floats appear only in human-readable decimal display fields.
"""

from __future__ import annotations

import csv
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent / "data"  # bundle: outputs -> data/ (mechanical re-home patch)
DATA = ROOT / "certified_points.csv"
JSON_DATA = ROOT / "certified_points.json"
ANSWER = ROOT / "ANSWER.md"
THETA = F(1, 2)
DELTA_CAP = F(1, 4)


def q(x: F | int) -> F:
    return x if isinstance(x, F) else F(x)


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def neg(x: F) -> F:
    return -x if x < 0 else F(0)


def qstr(x: F | int) -> str:
    x = q(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def dec(x: F, places: int = 10) -> str:
    return f"{float(x):.{places}f}"


def matmul(A: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    assert A and B and len(A[0]) == len(B)
    return [
        [sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def eye(n: int) -> list[list[F]]:
    return [[F(1 if i == j else 0) for j in range(n)] for i in range(n)]


def zeros(n: int, m: int) -> list[list[F]]:
    return [[F(0) for _ in range(m)] for _ in range(n)]


def det(M: list[list[F]]) -> F:
    n = len(M)
    assert n and all(len(row) == n for row in M)
    A = [row[:] for row in M]
    sign = F(1)
    out = F(1)
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if A[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            return F(0)
        if pivot != col:
            A[col], A[pivot] = A[pivot], A[col]
            sign = -sign
        pv = A[col][col]
        out *= pv
        for r in range(col + 1, n):
            factor = A[r][col] / pv
            if factor:
                for c in range(col, n):
                    A[r][c] -= factor * A[col][c]
    return sign * out


def inverse(M: list[list[F]]) -> list[list[F]]:
    n = len(M)
    assert n and all(len(row) == n for row in M)
    A = [M[i][:] + eye(n)[i] for i in range(n)]
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if A[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != col:
            A[col], A[pivot] = A[pivot], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(n):
            if r == col:
                continue
            factor = A[r][col]
            if factor:
                A[r] = [A[r][c] - factor * A[col][c] for c in range(2 * n)]
    return [row[n:] for row in A]


def row_times(row: list[F], M: list[list[F]]) -> list[F]:
    return [sum(row[t] * M[t][j] for t in range(len(M))) for j in range(len(M[0]))]


def submatrix_rows(M: list[list[F]], rows: tuple[int, ...]) -> list[list[F]]:
    return [M[i][:] for i in rows]


def left_inverse_from_basis(L: list[list[F]], basis: tuple[int, ...]) -> list[list[F]]:
    k = len(L[0])
    inv = inverse(submatrix_rows(L, basis))
    B = zeros(k, len(L))
    for local_col, row_index in enumerate(basis):
        for r in range(k):
            B[r][row_index] = inv[r][local_col]
    return B


def weighted_left_inverse(
    L: list[list[F]], weighted_bases: list[tuple[F, tuple[int, ...]]]
) -> list[list[F]]:
    k = len(L[0])
    n = len(L)
    B = zeros(k, n)
    total = sum(w for w, _ in weighted_bases)
    assert total != 0
    for w, basis in weighted_bases:
        Binv = left_inverse_from_basis(L, basis)
        ww = w / total
        for r in range(k):
            for i in range(n):
                B[r][i] += ww * Binv[r][i]
    return B


def row_neg(row: list[F]) -> F:
    return sum(neg(x) for x in row)


def delta_of(P: list[list[F]]) -> F:
    return max(row_neg(row) for row in P)


def check_instance(L: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    k = len(L[0])
    n = len(L)
    assert all(sum(row) == 1 for row in L)
    assert matmul(B, L) == eye(k)
    assert [sum(row) for row in B] == [F(1)] * k
    P = matmul(L, B)
    assert matmul(P, P) == P
    assert all(sum(row) == 1 for row in P)
    assert len(P) == n and all(len(row) == n for row in P)
    return P


def no_center_path(rank: int, a: F) -> tuple[list[list[F]], list[list[F]]]:
    rows: list[list[F]] = []
    for i in range(1, rank):
        row = [F(0)] * rank
        row[i] = F(1)
        rows.append(row)
    for u, v in zip(range(1, rank - 1), range(2, rank)):
        plus = [F(0)] * rank
        minus = [F(0)] * rank
        plus[0] = minus[0] = F(1)
        plus[u] = a
        plus[v] = -a
        minus[u] = -a
        minus[v] = a
        rows.extend([plus, minus])
    n = len(rows)
    B = zeros(rank, n)
    val = F(1, 2 * (rank - 2))
    for j in range(rank - 1, n):
        B[0][j] = val
    for r in range(1, rank):
        B[r][r - 1] = F(1)
    return rows, B


def cycle_coupling_rows(rank: int, a: F) -> list[list[F]]:
    rows = eye(rank)
    for base in range(rank):
        plus = [F(0)] * rank
        minus = [F(0)] * rank
        plus[base] = minus[base] = F(1)
        plus[(base + 1) % rank] += a
        plus[(base + 2) % rank] -= a
        minus[(base + 1) % rank] -= a
        minus[(base + 2) % rank] += a
        assert sum(plus) == 1 and sum(minus) == 1
        rows.extend([plus, minus])
    return rows


def g12_rank4_coupled_lift() -> tuple[list[list[F]], list[list[F]]]:
    """A non-decoupled rank-4 lift of the G12 B>0 example.

    The old five rows get a small fourth-coordinate shear; the new sixth row
    is an actual row.  B is a convex mixture of two exact left inverses, so
    BL=I and row-stochastic idempotence are certified by algebra, not floats.
    """

    old = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(3, 5), F(-1, 3), F(11, 15)],
        [F(1, 10), F(19, 20), F(-1, 20)],
    ]
    shears = [F(0), F(0), F(0), F(1, 8), F(-1, 10)]
    L: list[list[F]] = []
    for row, z in zip(old, shears):
        L.append([row[0] * (1 - z), row[1] * (1 - z), row[2] * (1 - z), z])
    L.append([F(1, 7), F(1, 5), F(-1, 10), F(53, 70)])
    for row in L:
        assert sum(row) == 1
    B = weighted_left_inverse(L, [(F(5, 6), (0, 1, 2, 5)), (F(1, 6), (0, 1, 3, 5))])
    return L, B


@dataclass
class Chart:
    basis: tuple[int, ...]
    volume: F
    coords: list[list[F]]
    phi_s: list[F]
    phi: F
    E: list[list[F]]


@dataclass
class Instance:
    name: str
    family: str
    L: list[list[F]]
    B: list[list[F]]
    rank5_probe: bool = False


def chart_metrics(P: list[list[F]], L: list[list[F]], basis: tuple[int, ...]) -> Chart:
    k = len(L[0])
    inv_basis = inverse(submatrix_rows(L, basis))
    coords = [row_times(row, inv_basis) for row in L]
    phi_s: list[F] = []
    E_by_s: list[list[F]] = []
    for s, u in enumerate(basis):
        phi = F(0)
        E_col: list[F] = []
        for i, Arow in enumerate(coords):
            lam = F(1) - Arow[s]
            mu = sum(neg(Arow[t]) for t in range(k) if t != s)
            E = pos(mu - lam)
            E_col.append(E)
            phi += pos(P[u][i]) * E
        phi_s.append(phi)
        E_by_s.append(E_col)
    return Chart(
        basis=basis,
        volume=abs(det(submatrix_rows(L, basis))),
        coords=coords,
        phi_s=phi_s,
        phi=max(phi_s),
        E=E_by_s,
    )


def all_charts(P: list[list[F]], L: list[list[F]]) -> tuple[F, list[Chart]]:
    k = len(L[0])
    charts: list[Chart] = []
    maxvol = F(0)
    for basis in itertools.combinations(range(len(L)), k):
        vol = abs(det(submatrix_rows(L, basis)))
        if vol == 0:
            continue
        if vol > maxvol:
            maxvol = vol
        charts.append(chart_metrics(P, L, basis))
    assert maxvol > 0
    theta = [c for c in charts if 2 * c.volume >= maxvol]
    theta.sort(key=lambda c: (c.phi, c.basis))
    return maxvol, theta


def cross_masses(P: list[list[F]], chart: Chart, r: int, s: int) -> dict[str, F]:
    assert r != s
    basis = chart.basis
    A = B = C = D = F(0)
    signed = F(0)
    for i, Arow in enumerate(chart.coords):
        beta = P[basis[r]][i]
        as_i = Arow[s]
        A += pos(beta) * pos(as_i)
        B += pos(beta) * neg(as_i)
        C += neg(beta) * pos(as_i)
        D += neg(beta) * neg(as_i)
        signed += beta * as_i
    assert signed == 0
    assert A == B + C - D
    return {"A": A, "B": B, "C": C, "D": D}


def pivot_move_checks(
    P: list[list[F]], L: list[list[F]], maxvol: F, chart: Chart, s: int
) -> list[dict[str, object]]:
    k = len(L[0])
    out: list[dict[str, object]] = []
    U = chart.basis
    Uset = set(U)
    for j in range(len(L)):
        if j in Uset:
            continue
        c = chart.coords[j][s]
        if c == 0:
            continue
        V = list(U)
        V[s] = j
        Vt = tuple(V)
        vol_v = abs(det(submatrix_rows(L, Vt)))
        assert vol_v == abs(c) * chart.volume
        if 2 * vol_v < maxvol:
            continue
        moved = chart_metrics(P, L, Vt)
        psi = moved.phi_s[s]
        gamma = max(moved.phi_s[r] for r in range(k) if r != s)
        disjunction_rhs = max(psi, gamma)
        disjunction_ok = chart.phi_s[s] <= disjunction_rhs
        assert disjunction_ok
        ci_rows = []
        if c > 0:
            for r in range(k):
                if r == s:
                    continue
                d_r = chart.coords[j][r]
                transverse = [q for q in range(k) if q not in (r, s)]
                I = F(0)
                for i, Arow in enumerate(chart.coords):
                    R = (F(1, 1) / c - 1) * neg(Arow[s])
                    R += sum(pos(Arow[s] * chart.coords[j][q] / c) for q in transverse)
                    R -= Arow[s] * d_r / c
                    I += pos(P[U[r]][i]) * pos(R)
                lhs = moved.phi_s[r]
                rhs = chart.phi_s[r] + I
                assert lhs <= rhs
                ci_rows.append(
                    {
                        "r": r,
                        "I": I,
                        "lhs": lhs,
                        "old_phi_r": chart.phi_s[r],
                        "slack": rhs - lhs,
                        "transverse": transverse,
                    }
                )
        out.append(
            {
                "j": j,
                "c": c,
                "volume": vol_v,
                "psi": psi,
                "gamma": gamma,
                "rhs": disjunction_rhs,
                "slack": disjunction_rhs - chart.phi_s[s],
                "ci": ci_rows,
                "ci_checked": len(ci_rows),
            }
        )
    return out


def analyze_instance(inst: Instance) -> dict[str, object]:
    P = check_instance(inst.L, inst.B)
    rank = len(inst.L[0])
    delta = delta_of(P)
    assert delta <= DELTA_CAP
    maxvol, theta = all_charts(P, inst.L)
    assert theta
    min_phi = theta[0].phi
    argmins = [c for c in theta if c.phi == min_phi]
    best_b = F(0)
    best_bc = F(0)
    best_b_row = None
    move_count = ci_count = positive_ci_move_count = 0
    max_phi_s_over_delta = F(0) if delta else F(0)
    worst_ci_slack = None
    all_move_summaries = []
    for chart in argmins:
        max_phi_s_over_delta = max(
            max_phi_s_over_delta,
            max((x / delta if delta else F(0)) for x in chart.phi_s),
        )
        maximal = [s for s, val in enumerate(chart.phi_s) if val == chart.phi]
        for s in maximal:
            for r in range(rank):
                if r == s:
                    continue
                masses = cross_masses(P, chart, r, s)
                Bmass = masses["B"]
                BC = masses["B"] + masses["C"]
                if delta and Bmass / delta > best_b:
                    best_b = Bmass / delta
                    best_b_row = {
                        "basis": chart.basis,
                        "s": s,
                        "r": r,
                        **masses,
                    }
                if delta and BC / delta > best_bc:
                    best_bc = BC / delta
            moves = pivot_move_checks(P, inst.L, maxvol, chart, s)
            move_count += len(moves)
            for move in moves:
                if move["c"] > 0:
                    positive_ci_move_count += 1
                ci_count += int(move["ci_checked"])
                for ci in move["ci"]:
                    slack = ci["slack"]
                    if worst_ci_slack is None or slack < worst_ci_slack:
                        worst_ci_slack = slack
            all_move_summaries.extend(
                {
                    "basis": chart.basis,
                    "s": s,
                    "j": move["j"],
                    "c": move["c"],
                    "psi": move["psi"],
                    "gamma": move["gamma"],
                    "slack": move["slack"],
                    "ci_checked": move["ci_checked"],
                }
                for move in moves
            )
    return {
        "name": inst.name,
        "family": inst.family,
        "rank": rank,
        "n": len(inst.L),
        "delta": delta,
        "maxvol": maxvol,
        "theta_charts": len(theta),
        "argmin_count": len(argmins),
        "argmin_basis": argmins[0].basis,
        "phi": min_phi,
        "phi_over_delta": min_phi / delta if delta else F(0),
        "argmin_phi_s": argmins[0].phi_s,
        "max_phi_s_over_delta": max_phi_s_over_delta,
        "max_B_over_delta": best_b,
        "max_BC_over_delta": best_bc,
        "max_B_witness": best_b_row,
        "pivot_moves_checked": move_count,
        "positive_c_moves": positive_ci_move_count,
        "ci_pairs_checked": ci_count,
        "worst_ci_slack": worst_ci_slack if worst_ci_slack is not None else F(0),
        "rank5_probe": inst.rank5_probe,
        "moves_sample": all_move_summaries[:8],
        "P": P,
        "L": inst.L,
        "B": inst.B,
    }


def interesting_cycle_instance(rank: int, a: F, weight: F) -> Instance:
    L = cycle_coupling_rows(rank, a)
    maxvol = F(0)
    bases: list[tuple[int, ...]] = []
    for basis in itertools.combinations(range(len(L)), rank):
        vol = abs(det(submatrix_rows(L, basis)))
        if vol == 0:
            continue
        if vol > maxvol:
            maxvol = vol
            bases = [basis]
        elif vol == maxvol:
            bases.append(basis)
    standard = tuple(range(rank))
    chosen = sorted([b for b in bases if b != standard] or bases)[0]
    B = weighted_left_inverse(L, [(weight, standard), (F(1) - weight, chosen)])
    return Instance(
        name=f"cycle_coupling_rank{rank}_a{qstr(a).replace('/', '_')}_w{qstr(weight).replace('/', '_')}",
        family="cycle-coupling-mixture",
        L=L,
        B=B,
        rank5_probe=(rank == 5),
    )


def build_instances() -> list[Instance]:
    out: list[Instance] = []
    L3, B3 = no_center_path(3, F(1, 100))
    out.append(Instance("CALIBRATION_no_center_rank3_a1_100", "calibration", L3, B3))
    for a in [F(1, 100), F(1, 20), F(1, 4)]:
        L, B = no_center_path(4, a)
        out.append(Instance(f"no_center_rank4_a{qstr(a).replace('/', '_')}", "no-center", L, B))
    out.append(interesting_cycle_instance(4, F(1, 5), F(15, 16)))
    out.append(interesting_cycle_instance(4, F(1, 12), F(1, 2)))
    out.append(interesting_cycle_instance(4, F(1, 30), F(1, 2)))
    for a in [F(1, 100), F(1, 20)]:
        L, B = no_center_path(5, a)
        out.append(Instance(f"rank5_probe_no_center_a{qstr(a).replace('/', '_')}", "no-center", L, B, True))
    out.append(interesting_cycle_instance(5, F(1, 8), F(15, 16)))
    return out


def serial(obj):
    if isinstance(obj, F):
        return qstr(obj)
    if isinstance(obj, tuple):
        return list(obj)
    if isinstance(obj, list):
        return [serial(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): serial(v) for k, v in obj.items()}
    return obj


def write_outputs(records: list[dict[str, object]]) -> None:
    fieldnames = [
        "name",
        "family",
        "rank",
        "n",
        "delta",
        "theta_charts",
        "argmin_count",
        "argmin_basis",
        "phi",
        "phi_over_delta",
        "max_phi_s_over_delta",
        "max_B_over_delta",
        "max_BC_over_delta",
        "pivot_moves_checked",
        "positive_c_moves",
        "ci_pairs_checked",
        "worst_ci_slack",
        "rank5_probe",
    ]
    with DATA.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rec in records:
            writer.writerow(
                {
                    key: (
                        " ".join(map(str, rec[key]))
                        if key == "argmin_basis"
                        else qstr(rec[key])
                        if isinstance(rec[key], F)
                        else rec[key]
                    )
                    for key in fieldnames
                }
            )
    JSON_DATA.write_text(json.dumps(serial(records), indent=2, sort_keys=True) + "\n", encoding="utf-8")

    rank4 = [r for r in records if r["rank"] == 4]
    rank5 = [r for r in records if r["rank"] == 5]
    max_phi = max(rank4, key=lambda r: r["phi_over_delta"])
    max_b = max(rank4, key=lambda r: r["max_B_over_delta"])
    max_bc = max(rank4, key=lambda r: r["max_BC_over_delta"])
    total_moves = sum(int(r["pivot_moves_checked"]) for r in rank4)
    total_ci = sum(int(r["ci_pairs_checked"]) for r in rank4)
    worst_slack = min(r["worst_ci_slack"] for r in rank4)
    lines = [
        "# Rank-4 Exact-Rational Numerics Decider",
        "",
        "**Status:** L3 numerical evidence only.  All certified arithmetic in `decider_rank4.py` uses `fractions.Fraction`; decimal displays are non-certified readability only.",
        "",
        "## Headline Verdicts",
        "",
        f"- **Pivot-removing disjunction:** no rank-4 violation found.  Exact asserts checked {total_moves} theta-half pivot-removing moves at certified Phi-argmins.",
        f"- **Collateral import (CI):** no rank-4 violation found under the natural `c>0` transcription.  Exact asserts checked {total_ci} transverse CI inequalities; smallest slack was `{qstr(worst_slack)}`.",
        f"- **Max rank-4 Phi/delta observed:** `{qstr(max_phi['phi_over_delta'])}` on `{max_phi['name']}`.  The no-center rank-4 edge case gives Phi/delta `5/4`; the cheap rank-5 no-center probe gives `4/3`, matching `2 - 2/(5-2)`.",
        f"- **Max rank-4 B/delta observed:** `{qstr(max_b['max_B_over_delta'])}` on `{max_b['name']}`.  Max `(B+C)/delta` observed: `{qstr(max_bc['max_BC_over_delta'])}` on `{max_bc['name']}`.",
        "- **Blow-up trend:** none seen in this bounded exact search.  Rank-5 cheap probes reproduced the no-center law at `4/3 = 2 - 2/(5-2)` and produced no transfer violation.",
        "",
        "## Rank-4 Transcription Used",
        "",
        "For a chart `U=(u_0,...,u_{k-1})`, coordinates are `p_i = sum_t a_t(i) p_{u_t}`, `beta_r(i)=P_{u_r i}`, and",
        "",
        "`E_r(i)=max(sum_{q != r} max(-a_q(i),0) - (1-a_r(i)), 0)`,  `Phi_r(U)=sum_i max(beta_r(i),0) E_r(i)`.",
        "",
        "For rank 4 CI, with pivot `s`, transverse beta row `r`, and the two remaining transverse indices `T={q: q notin {r,s}}`, I used",
        "",
        "`R_{r,j}^{(4)}(i) = (1/c-1) a_s(i)^- + sum_{q in T} max(a_s(i) d_q/c,0) - a_s(i)d_r/c`,",
        "",
        "where `c=a_s(j)>0` and `d_q=a_q(j)`.  The checked inequality is",
        "",
        "`Phi_r(V_j) <= Phi_r(U) + sum_i beta_r(i)^+ max(R_{r,j}^{(4)}(i),0)`.",
        "",
        "For cross-pivot mass I kept the validated pairwise split for every ordered pair `r != s`:",
        "",
        "`B_{r,s}=sum_i beta_r(i)^+ a_s(i)^-`, `C_{r,s}=sum_i beta_r(i)^- a_s(i)^+`, with `A=B+C-D` asserted exactly.  In rank 4 the reported value is the maximum over the three transverse choices `r` for each maximal pivot `s`.",
        "",
        "## Certified Points",
        "",
        "| instance | rank | n | delta | theta charts | Phi/delta | max B/delta | max (B+C)/delta | moves | CI pairs |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for rec in records:
        lines.append(
            f"| `{rec['name']}` | {rec['rank']} | {rec['n']} | `{qstr(rec['delta'])}` | {rec['theta_charts']} | "
            f"`{qstr(rec['phi_over_delta'])}` | `{qstr(rec['max_B_over_delta'])}` | `{qstr(rec['max_BC_over_delta'])}` | "
            f"{rec['pivot_moves_checked']} | {rec['ci_pairs_checked']} |"
        )
    lines.extend(
        [
            "",
            "## Calibration And Hard Asserts",
            "",
            "- The script first reproduces the known rank-3 no-center value: `delta=1/100`, `Phi/delta=1`.",
            "- Every emitted instance asserts `BL=I`, `P^2=P`, row sums equal `1`, `delta<=1/4`, exact chart volumes, exact pivot-removing volume identity `Vol(V_j)=|a_s(j)| Vol(U)`, the disjunction, CI for `c>0`, and cross-pivot cancellation.",
            "- Re-run command: `python3 runs/2026-07-04-rank4-transfer-decider/scripts/decider_rank4.py`.",
            "",
            "## Honest Scope",
            "",
            "- Rank 4 coverage is explicit and finite: three no-center scales and three cyclic coupling mixtures.",
            "- Rank 5 was only a cheap probe: two no-center scales and one cyclic coupling mixture.",
            "- CI was checked only in its stated `c>0` regime.  Negative-pivot moves were included for the disjunction but skipped for CI because the registered CI statement does not cover them.",
            "- This is not a proof and does not search all rank-4 signed idempotents.  It rules out only violations in the deterministic families enumerated here.",
        ]
    )
    if rank5:
        lines.extend(["", "## Rank-5 Probe Notes", ""])
        for rec in rank5:
            lines.append(
                f"- `{rec['name']}`: Phi/delta `{qstr(rec['phi_over_delta'])}`, "
                f"max B/delta `{qstr(rec['max_B_over_delta'])}`, moves `{rec['pivot_moves_checked']}`."
            )
    ANSWER.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    instances = build_instances()
    records = [analyze_instance(inst) for inst in instances]
    calib = records[0]
    assert calib["name"] == "CALIBRATION_no_center_rank3_a1_100"
    assert calib["delta"] == F(1, 100)
    assert calib["phi_over_delta"] == F(1)
    write_outputs(records)
    print(f"wrote {DATA.relative_to(Path.cwd())}")
    print(f"wrote {JSON_DATA.relative_to(Path.cwd())}")
    print(f"wrote {ANSWER.relative_to(Path.cwd())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
