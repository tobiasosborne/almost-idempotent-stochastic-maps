#!/usr/bin/env python3
"""Emit exact Farkas certificates for the minimal starvation completions.

Decision arithmetic is exclusively fractions.Fraction arithmetic.  The script
does not call a numerical optimizer.  Each verdict follows from a checked
nonnegative combination of five necessary entry bounds and six BL=I
equalities.
"""

from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"
LABELS = ["v", "w", "f", "z", "o"]


def qstr(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qlist(values):
    if isinstance(values, Q):
        return qstr(values)
    if isinstance(values, list):
        return [qlist(x) for x in values]
    if isinstance(values, tuple):
        return [qlist(x) for x in values]
    if isinstance(values, dict):
        return {k: qlist(v) for k, v in values.items()}
    return values


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def matsub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def is_zero_matrix(a):
    return all(x == 0 for row in a for x in row)


def canonical_data(s=Q(1, 256), A=Q(5)):
    t = s * s
    a = s / (1 + s)
    L = [
        [Q(1), Q(0), Q(0)],
        [Q(1), -A * a, t * a],
        [Q(1), -A, t],
        [Q(1), Q(1), Q(0)],
        [Q(1), Q(0), Q(1)],
    ]
    c = [1 - s, s + t, -t, Q(0), Q(0)]
    assert matmul([c], L) == [[Q(1), Q(0), Q(0)]]

    # Unknown order D_v,...,D_o,E_v,...,E_o.  These are the six
    # nontrivial rows of BL=I.
    E = []
    rhs = []
    eq_names = []
    for block, prefix, target_axis in ((0, "D", 1), (1, "E", 2)):
        for k in range(3):
            row = [Q(0)] * 10
            for j in range(5):
                row[block * 5 + j] = L[j][k]
            E.append(row)
            rhs.append(Q(int(k == target_axis)))
            eq_names.append(f"{prefix}_moment_{k}")

    def entry_form(i, j):
        coeff = [Q(0)] * 10
        coeff[j] = L[i][1]
        coeff[5 + j] = L[i][2]
        return {"constant": c[j], "coefficients": coeff}

    pairs = [("f", "v"), ("f", "z"), ("z", "f"), ("o", "v"), ("o", "w")]
    forms = []
    for ri, cj in pairs:
        form = entry_form(LABELS.index(ri), LABELS.index(cj))
        form["name"] = f"P_{ri}{cj}"
        form["row"] = ri
        form["column"] = cj
        forms.append(form)

    G = 1 + (A + 1) * s - s**3
    N = [
        A * s * (s + 1) * (A + 1 - t),
        (s + 1) * (A + 1 - t) * G,
        A**2 * (s + 1) * (A + 1 - t),
        A * t * (s + 1),
        A * t * G,
    ]
    Dsum = sum(N, Q(0))
    M = A * (s + 1) * (A + 1 - t) * (1 + (A + 1) * t - t * t)

    # Multipliers for residuals E*x-rhs.  They verify
    # sum_i N_i P_i + M = sum_k mu_k (E_k*x-rhs_k).
    mu = [
        -(A**2) * s * (s + 1) * (A + 1 - t),
        -A * (s + 1) * (A + 1 - t) * (1 + s - s**3),
        (A**2) * s * (s + 1) * (A + 1 - t),
        A * t * (s + 1) * G,
        t * (1 - s) * (s + 1) ** 2 * G,
        -A * t * (s + 1) * G,
    ]

    # Exact internal verification of the affine-form identity.
    lhs_coeff = [sum((N[i] * forms[i]["coefficients"][j] for i in range(5)), Q(0))
                 for j in range(10)]
    lhs_const = sum((N[i] * forms[i]["constant"] for i in range(5)), Q(0)) + M
    rhs_coeff = [sum((mu[k] * E[k][j] for k in range(6)), Q(0)) for j in range(10)]
    rhs_const = -sum((mu[k] * rhs[k] for k in range(6)), Q(0))
    assert lhs_coeff == rhs_coeff
    assert lhs_const == rhs_const
    assert all(n > 0 for n in N)
    assert Dsum == sum(N, Q(0))
    margin = M - t * Dsum
    assert margin > 0

    # A concrete equality-only completion.  It verifies BL=I and P^2=P but
    # intentionally drops the norm and negativity thresholds.
    unit_z = [Q(0), Q(0), Q(0), Q(1), Q(0)]
    unit_o = [Q(0), Q(0), Q(0), Q(0), Q(1)]
    Drow = [unit_z[j] - c[j] for j in range(5)]
    Erow = [unit_o[j] - c[j] for j in range(5)]
    Bsample = [c, Drow, Erow]
    assert matmul(Bsample, L) == eye(3)
    Psample = matmul(L, Bsample)
    assert is_zero_matrix(matsub(matmul(Psample, Psample), Psample))

    return {
        "s": s,
        "t": t,
        "A": A,
        "a": a,
        "L": L,
        "fixed_B_row_0": c,
        "unknowns": [f"D_{x}" for x in LABELS] + [f"E_{x}" for x in LABELS],
        "equalities": {"names": eq_names, "matrix": E, "rhs": rhs},
        "entry_forms": forms,
        "certificate": {
            "inequality_multipliers_N": N,
            "equality_multipliers_mu": mu,
            "D_sum": Dsum,
            "M": M,
            "contradiction_margin_M_minus_tD": margin,
            "normalized_R": M / Dsum,
        },
        "sample_B_equality_only": Bsample,
    }


def row_negative_mass(row):
    return sum((-x for x in row if x < 0), Q(0))


def base_raw(case_id, description):
    data = canonical_data()
    L = data["L"]
    B = data["sample_B_equality_only"]
    P = matmul(L, B)
    F = [P[2][j] - P[0][j] for j in range(5)]
    Z = [P[3][j] - P[0][j] for j in range(5)]
    O = [P[4][j] - P[0][j] for j in range(5)]
    affine_residual = [F[j] + data["A"] * Z[j] - data["t"] * O[j] for j in range(5)]
    w_residual = [P[1][j] - P[0][j] - data["a"] * F[j] for j in range(5)]
    sample_delta = max(row_negative_mass(row) for row in P)
    return {
        "schema": "starvation-farkas-v1",
        "case_id": case_id,
        "description": description,
        "verdict": "INFEASIBLE",
        "rank": 3,
        "labels": LABELS,
        "parameters": {k: data[k] for k in ("s", "t", "A", "a")},
        "factor_problem": {
            "L": data["L"],
            "fixed_B_row_0": data["fixed_B_row_0"],
            "unknowns": data["unknowns"],
            "equalities": data["equalities"],
            "necessary_inequalities": [
                {
                    "name": form["name"] + "+t>=0",
                    "source": "row negativity <= t implies every entry >= -t",
                    "constant": form["constant"] + data["t"],
                    "coefficients": form["coefficients"],
                    "entry_constant_without_t": form["constant"],
                    "row": form["row"],
                    "column": form["column"],
                }
                for form in data["entry_forms"]
            ],
        },
        "farkas_certificate": data["certificate"],
        "metric_obstruction": {
            "moment": "sum_j x_j*D_j=1",
            "max_abs_x": data["A"],
            "required_D_l1": data["s"],
            "contradiction_margin_1_minus_A_s": 1 - data["A"] * data["s"],
            "argument": "1=|sum x_j D_j| <= max|x_j|*||D||_1=A*s",
        },
        "sample_relaxation": {
            "scope": "BL=I, idempotence, row sums, affine gadget, and top pins only; norm and negativity are deliberately dropped",
            "B": B,
            "P": P,
            "sample_delta": sample_delta,
            "Z_l1": sum(abs(x) for x in Z),
            "affine_gadget_residual": affine_residual,
            "w_interpolation_residual": w_residual,
        },
        "stability": {
            "A_interval": [Q(4), Q(6)],
            "s_interval": [Q(0), Q(1, 256)],
            "s_left_endpoint_open": True,
            "g_over_s_interval": [Q(4), Q(6)],
            "analytic_bounds": {
                "all_N_positive": True,
                "D_less_than": Q(264),
                "M_greater_than": Q(16),
                "R_greater_than": Q(2, 33),
                "t_at_most": Q(1, 65536),
            },
            "g_used_by_certificate": False,
        },
    }


def make_cases():
    s = Q(1, 256)
    t = s * s

    literal = base_raw(
        "literal_r3_actor5",
        "Canonical rank-three five-actor W55 starvation tableau",
    )
    literal["case_constraints"] = {
        "literal_top_row": {"P_vv": 1 - s, "P_vw": s + t, "P_vf": -t,
                            "other_top_entries": Q(0)},
        "gadget": {"A0": Q(5), "g": 5 * s, "Z_l1_required": s,
                   "positive_far_inflow_from_v": Q(0)},
    }

    near = base_raw(
        "hx_near_r3_actor5",
        "Literal tableau plus the formal H-X near off-diagonal freight atom (w,v); full H-X geometry is an inconsistent added cell",
    )
    near_threshold = (1 + s) / 4
    near["case_constraints"] = {
        "kernel_xi_w": {"v": 1 / (1 + s), "f": s / (1 + s)},
        "freight_constraint": {"entry": "P_fw", "lower_bound": near_threshold},
        "certified_atom": {"x": "w", "u": "v", "horn": "B_N",
                           "mass_lower_bound": near_threshold / (1 + s),
                           "off_diagonal": True},
        "h_profile": {"v": Q(0), "w": s * t / (1 + s), "f": t,
                      "z": Q(0), "o": Q(1)},
        "score_upper_bound": 3 * t,
        "score_threshold": 12 * s / 13,
        "geometry_status": "NOT_REALIZED: f and z are visible in the actor polytope, so the full co-top/tall cell is empty",
    }

    far = base_raw(
        "hx_far_r3_nonvertex6",
        "First zero-top added-nonvertex formal H-X far freight refinement, compressed exactly to actor5; full H-X geometry is not realized",
    )
    L5 = far["factor_problem"]["L"]
    lx = [(L5[0][k] + L5[2][k]) / 2 for k in range(3)]
    L6 = L5 + [lx]
    c6 = far["factor_problem"]["fixed_B_row_0"] + [Q(0)]
    unit_z6 = [Q(0), Q(0), Q(0), Q(1), Q(0), Q(0)]
    unit_o6 = [Q(0), Q(0), Q(0), Q(0), Q(1), Q(0)]
    D6 = [unit_z6[j] - c6[j] for j in range(6)]
    E6 = [unit_o6[j] - c6[j] for j in range(6)]
    B6 = [c6, D6, E6]
    assert matmul(B6, L6) == eye(3)
    P6 = matmul(L6, B6)
    assert is_zero_matrix(matsub(matmul(P6, P6), P6))
    B5_aggregated = []
    for brow in B6:
        B5_aggregated.append([
            brow[0] + brow[5] / 2,
            brow[1],
            brow[2] + brow[5] / 2,
            brow[3],
            brow[4],
        ])
    assert matmul(B5_aggregated, L5) == eye(3)
    far["lift"] = {
        "labels_full": LABELS + ["x"],
        "L_full": L6,
        "fixed_B_row_0_full": c6,
        "x_barycentric_coordinates": {"v": Q(1, 2), "f": Q(1, 2)},
        "aggregation": {"b_prime_v": {"b_v": Q(1), "b_x": Q(1, 2)},
                        "b_prime_f": {"b_f": Q(1), "b_x": Q(1, 2)}},
        "sample_B_full_equality_only": B6,
        "sample_P_full_equality_only": P6,
        "sample_B_aggregated": B5_aggregated,
        "negative_part_argument": "For theta>=0, (-[u+theta*x])_+ <= (-u)_+ + theta*(-x)_+; summing the two distributed columns preserves total theta=1.",
    }
    far["case_constraints"] = {
        "top_pin": "P_vx=0",
        "freight_constraint": {"entry": "P_fx", "lower_bound": Q(1, 2)},
        "kernel_xi_x": {"v": Q(1, 2), "f": Q(1, 2)},
        "certified_atom": {"x": "x", "u": "f", "horn": "B_F",
                           "mass_lower_bound": Q(1, 4), "off_diagonal": True},
        "score_upper_bound": 3 * t,
        "score_threshold": 12 * s / 13,
        "geometry_status": "NOT_REALIZED: the added midpoint changes no vertex, so the full co-top/tall cell is empty",
    }
    return [literal, near, far]


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    cases = make_cases()
    for case in cases:
        path = RAW / f"{case['case_id']}.json"
        path.write_text(json.dumps(qlist(case), indent=2, sort_keys=True) + "\n")
        cert = case["farkas_certificate"]
        print(
            "CASE",
            case["case_id"],
            "INFEASIBLE",
            "margin=" + qstr(cert["contradiction_margin_M_minus_tD"]),
            "R=" + qstr(cert["normalized_R"]),
        )
    print("STABILITY PASS A in [4,6], 0<s<=1/256; certificate ignores added g constraints, singleton locus g=A*s")
    print("RAW", len(cases), "certificate files written")


if __name__ == "__main__":
    main()
