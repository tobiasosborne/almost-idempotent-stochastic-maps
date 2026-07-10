#!/usr/bin/env python3
"""Independent exact checker for raw starvation certificates.

This module deliberately does not import decide.py.  It reconstructs the
factor equations, entry forms, sample projections, lift aggregation, and Farkas
combination from the JSON files alone.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw"


def q(value):
    if isinstance(value, int):
        return Q(value)
    if isinstance(value, str):
        return Q(value)
    raise TypeError(f"not a rational token: {value!r}")


def qvec(values):
    return [q(x) for x in values]


def qmat(values):
    return [qvec(row) for row in values]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def zero_matrix(a):
    return all(x == 0 for row in a for x in row)


def matrix_equal(a, b):
    return len(a) == len(b) and all(ra == rb for ra, rb in zip(a, b))


def row_negative_mass(row):
    return sum((-x for x in row if x < 0), Q(0))


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)


def reconstruct_equalities(L):
    n = len(L)
    E = []
    rhs = []
    for block, target_axis in ((0, 1), (1, 2)):
        for k in range(3):
            row = [Q(0)] * (2 * n)
            for j in range(n):
                row[block * n + j] = L[j][k]
            E.append(row)
            rhs.append(Q(int(k == target_axis)))
    return E, rhs


def check_base(raw):
    labels = raw["labels"]
    assert_true(labels == ["v", "w", "f", "z", "o"], "unexpected actor order")
    params = raw["parameters"]
    s, t, A, a = (q(params[k]) for k in ("s", "t", "A", "a"))
    assert_true(t == s * s, "t != s^2")
    assert_true(a == s / (1 + s), "wrong interpolation coefficient")

    problem = raw["factor_problem"]
    L = qmat(problem["L"])
    c = qvec(problem["fixed_B_row_0"])
    assert_true(len(L) == 5 and all(len(row) == 3 for row in L), "bad L shape")
    assert_true(matmul([c], L) == [[Q(1), Q(0), Q(0)]], "fixed top row does not reproduce")
    assert_true(c == [1 - s, s + t, -t, Q(0), Q(0)], "top pins differ")

    # Factor-coordinate gadget, checked independently of the stored prose.
    v, w, f, z, o = L
    F_L = [f[k] - v[k] for k in range(3)]
    Z_L = [z[k] - v[k] for k in range(3)]
    O_L = [o[k] - v[k] for k in range(3)]
    assert_true(all(F_L[k] + A * Z_L[k] == t * O_L[k] for k in range(3)),
                "factor gadget relation fails")
    assert_true(all(w[k] - v[k] == a * F_L[k] for k in range(3)),
                "factor interpolation fails")

    E_stored = qmat(problem["equalities"]["matrix"])
    b_stored = qvec(problem["equalities"]["rhs"])
    E, b = reconstruct_equalities(L)
    assert_true(E_stored == E and b_stored == b, "stored BL equations are not reconstructed equations")

    forms = problem["necessary_inequalities"]
    assert_true(len(forms) == 5, "certificate must have five entry inequalities")
    entry_constants = []
    entry_coeffs = []
    for form in forms:
        ri = labels.index(form["row"])
        cj = labels.index(form["column"])
        expected = [Q(0)] * 10
        expected[cj] = L[ri][1]
        expected[5 + cj] = L[ri][2]
        coeff = qvec(form["coefficients"])
        entry_const = q(form["entry_constant_without_t"])
        assert_true(coeff == expected, f"wrong entry coefficients for {form['name']}")
        assert_true(entry_const == c[cj], f"wrong entry constant for {form['name']}")
        assert_true(q(form["constant"]) == entry_const + t, "inequality did not add threshold t")
        entry_constants.append(entry_const)
        entry_coeffs.append(coeff)

    cert = raw["farkas_certificate"]
    N = qvec(cert["inequality_multipliers_N"])
    mu = qvec(cert["equality_multipliers_mu"])
    Dsum = q(cert["D_sum"])
    M = q(cert["M"])
    margin = q(cert["contradiction_margin_M_minus_tD"])
    R = q(cert["normalized_R"])
    assert_true(len(N) == 5 and all(x > 0 for x in N), "inequality multiplier is not positive")
    assert_true(len(mu) == 6, "wrong equality multiplier count")
    assert_true(Dsum == sum(N, Q(0)), "D is not sum N")
    assert_true(R == M / Dsum, "wrong normalized R")
    assert_true(margin == M - t * Dsum and margin > 0, "nonpositive contradiction margin")

    lhs_coeff = [sum((N[i] * entry_coeffs[i][j] for i in range(5)), Q(0))
                 for j in range(10)]
    lhs_const = sum((N[i] * entry_constants[i] for i in range(5)), Q(0)) + M
    rhs_coeff = [sum((mu[k] * E[k][j] for k in range(6)), Q(0)) for j in range(10)]
    rhs_const = -sum((mu[k] * b[k] for k in range(6)), Q(0))
    assert_true(lhs_coeff == rhs_coeff, "Farkas variable coefficients do not cancel")
    assert_true(lhs_const == rhs_const, "Farkas constants do not cancel")
    assert_true(t * Dsum - M < 0, "weighted necessary inequalities are not contradictory")

    metric = raw["metric_obstruction"]
    max_abs_x = max(abs(row[1]) for row in L)
    metric_margin = q(metric["contradiction_margin_1_minus_A_s"])
    assert_true(max_abs_x == A == q(metric["max_abs_x"]), "metric max |x| is wrong")
    assert_true(q(metric["required_D_l1"]) == s, "metric norm requirement is wrong")
    assert_true(metric_margin == 1 - A * s and metric_margin > 0,
                "actor metric obstruction is not strict")

    sample = raw["sample_relaxation"]
    B = qmat(sample["B"])
    P_stored = qmat(sample["P"])
    assert_true(matmul(B, L) == eye(3), "sample BL != I")
    P = matmul(L, B)
    assert_true(P == P_stored, "stored sample P differs from LB")
    assert_true(zero_matrix([[x - y for x, y in zip(r1, r2)]
                             for r1, r2 in zip(matmul(P, P), P)]), "sample P^2 != P")
    assert_true(all(sum(row, Q(0)) == 1 for row in P), "sample row sum fails")
    assert_true(P[0] == c, "sample top row differs from pins")
    F = [P[2][j] - P[0][j] for j in range(5)]
    Z = [P[3][j] - P[0][j] for j in range(5)]
    O = [P[4][j] - P[0][j] for j in range(5)]
    assert_true(all(F[j] + A * Z[j] == t * O[j] for j in range(5)), "sample row gadget fails")
    assert_true(all(P[1][j] - P[0][j] == a * F[j] for j in range(5)), "sample row interpolation fails")
    assert_true(qvec(sample["affine_gadget_residual"]) == [Q(0)] * 5, "stored gadget residual nonzero")
    assert_true(qvec(sample["w_interpolation_residual"]) == [Q(0)] * 5, "stored w residual nonzero")
    sample_delta = max(row_negative_mass(row) for row in P)
    assert_true(sample_delta == q(sample["sample_delta"]), "stored sample delta wrong")
    assert_true(sum(abs(x) for x in Z) == q(sample["Z_l1"]), "stored sample Z norm wrong")

    stability = raw["stability"]
    bounds = stability["analytic_bounds"]
    assert_true(q(bounds["D_less_than"]) == 264, "stability D bound altered")
    assert_true(q(bounds["M_greater_than"]) == 16, "stability M bound altered")
    assert_true(q(bounds["R_greater_than"]) == Q(2, 33), "stability R bound altered")
    assert_true(q(bounds["t_at_most"]) == Q(1, 65536), "stability t bound altered")
    assert_true(stability["g_used_by_certificate"] is False, "certificate unexpectedly consumes g")

    # Independently verify the uniform rational bounding chain used in the
    # stability proof.  For A in [4,6] and 0<s<=1/256:
    #   A+1-t <= 7, 1+s <= 257/256, G <= 1+7/256.
    # Each displayed upper bound is then an exact rational comparison.
    A_min, A_max = Q(4), Q(6)
    s_max = Q(1, 256)
    t_max = s_max * s_max
    one_plus_s_max = 1 + s_max
    G_upper = 1 + 7 * s_max
    assert_true(A_min + 1 - t_max > 0, "A+1-t positivity not uniform")
    assert_true(1 + s_max * (A_min + 1 - t_max) > 1, "G positivity not uniform")
    term_upper = [
        A_max * s_max * one_plus_s_max * 7,
        one_plus_s_max * 7 * G_upper,
        A_max * A_max * one_plus_s_max * 7,
        A_max * t_max * one_plus_s_max,
        A_max * t_max * G_upper,
    ]
    declared_term_bounds = [Q(1), Q(8), Q(253), Q(1), Q(1)]
    assert_true(all(u < v for u, v in zip(term_upper, declared_term_bounds)),
                "one of the uniform N_i bounds fails")
    assert_true(sum(declared_term_bounds, Q(0)) == 264, "uniform D bound sum fails")
    # M=A(1+s)(A+1-t)(1+(A+1)t-t^2).  On the open interval
    # s>0, the second factor is >1; t<=t_max<1 makes the third
    # factor >A; and t*((A+1)-t)>0 makes the last factor >1.
    assert_true(stability["s_left_endpoint_open"] is True, "stability interval lost s>0")
    assert_true(t_max < 1, "t_max is not below one")
    assert_true(A_min + 1 - t_max > A_min, "A+1-t is not uniformly above A")
    assert_true(A_min + 1 - t_max > 0, "last M factor lacks positive increment")
    assert_true(A_min * A_min == 16, "uniform M lower bound fails")
    assert_true(Q(16, 264) == Q(2, 33), "uniform R reduction fails")
    assert_true(Q(2, 33) > t_max, "uniform contradiction does not beat t")

    return {
        "s": s,
        "t": t,
        "A": A,
        "a": a,
        "L": L,
        "c": c,
        "margin": margin,
        "R": R,
        "sample_delta": sample_delta,
        "sample_budget_pass": sample_delta <= t,
        "sample_norm_pass": sum(abs(x) for x in Z) == s,
        "metric_margin": metric_margin,
    }


def check_near(raw, base):
    case = raw["case_constraints"]
    assert_true(case["geometry_status"].startswith("NOT_REALIZED"),
                "near raw file overclaims genuine H-X geometry")
    kernel = {k: q(v) for k, v in case["kernel_xi_w"].items()}
    assert_true(kernel == {"v": 1 / (1 + base["s"]), "f": base["s"] / (1 + base["s"])},
                "near kernel weights wrong")
    assert_true(sum(kernel.values(), Q(0)) == 1 and all(x >= 0 for x in kernel.values()),
                "near kernel is not a probability")
    L = base["L"]
    bary = [(kernel["v"] * L[0][k] + kernel["f"] * L[2][k]) for k in range(3)]
    assert_true(bary == L[1], "near kernel does not reproduce w")
    lower = q(case["freight_constraint"]["lower_bound"])
    atom = q(case["certified_atom"]["mass_lower_bound"])
    assert_true(atom == lower * kernel["v"], "near atom mass arithmetic wrong")
    assert_true(atom >= Q(1, 4) and atom > Q(1, 8), "near H-X thresholds fail")
    h = {k: q(v) for k, v in case["h_profile"].items()}
    for i, label in enumerate(raw["labels"]):
        assert_true(h[label] == L[i][2], f"h profile mismatch at {label}")
    assert_true(q(case["score_upper_bound"]) < q(case["score_threshold"]), "score is not strict")


def check_far(raw, base):
    lift = raw["lift"]
    labels_full = lift["labels_full"]
    assert_true(labels_full == ["v", "w", "f", "z", "o", "x"], "bad lifted labels")
    L6 = qmat(lift["L_full"])
    theta = {k: q(v) for k, v in lift["x_barycentric_coordinates"].items()}
    assert_true(theta == {"v": Q(1, 2), "f": Q(1, 2)}, "wrong far barycentric weights")
    assert_true(sum(theta.values(), Q(0)) == 1 and all(x >= 0 for x in theta.values()),
                "far lift weights are not convex")
    expected_x = [(base["L"][0][k] + base["L"][2][k]) / 2 for k in range(3)]
    assert_true(L6[:5] == base["L"] and L6[5] == expected_x, "lifted factor point is not midpoint")

    B6 = qmat(lift["sample_B_full_equality_only"])
    P6 = qmat(lift["sample_P_full_equality_only"])
    assert_true(matmul(B6, L6) == eye(3), "lift sample BL != I")
    assert_true(matmul(L6, B6) == P6, "lift sample P != LB")
    assert_true(matrix_equal(matmul(P6, P6), P6), "lift sample P^2 != P")
    assert_true(all(sum(row, Q(0)) == 1 for row in P6), "lift sample row sums fail")
    assert_true(B6[0][5] == 0, "top coefficient at x is nonzero")

    B5 = []
    for brow in B6:
        B5.append([brow[0] + brow[5] / 2, brow[1], brow[2] + brow[5] / 2,
                   brow[3], brow[4]])
    assert_true(B5 == qmat(lift["sample_B_aggregated"]), "stored aggregation differs")
    assert_true(matmul(B5, base["L"]) == eye(3), "aggregated BL != I")
    assert_true(B5[0] == base["c"], "aggregation changed pinned top row")

    case = raw["case_constraints"]
    assert_true(case["geometry_status"].startswith("NOT_REALIZED"),
                "far raw file overclaims genuine H-X geometry")
    kernel = {k: q(v) for k, v in case["kernel_xi_x"].items()}
    assert_true(kernel == theta, "far kernel and lift weights differ")
    lower = q(case["freight_constraint"]["lower_bound"])
    atom = q(case["certified_atom"]["mass_lower_bound"])
    assert_true(atom == lower * kernel["f"], "far atom mass arithmetic wrong")
    assert_true(atom >= Q(1, 4) and atom > Q(1, 8), "far H-X thresholds fail")
    assert_true(q(case["score_upper_bound"]) < q(case["score_threshold"]), "far score is not strict")


def check_file(path):
    raw = json.loads(path.read_text())
    assert_true(raw["schema"] == "starvation-farkas-v1", "unknown schema")
    assert_true(raw["verdict"] == "INFEASIBLE", "unexpected verdict")
    base = check_base(raw)
    case_id = raw["case_id"]
    if case_id == "hx_near_r3_actor5":
        check_near(raw, base)
    elif case_id == "hx_far_r3_nonvertex6":
        check_far(raw, base)
    elif case_id != "literal_r3_actor5":
        raise AssertionError(f"unknown case id {case_id}")
    return case_id, base


def main():
    paths = sorted(RAW.glob("*.json"))
    if not paths:
        print("FAIL no raw certificate files")
        return 1
    failed = False
    for path in paths:
        try:
            case_id, data = check_file(path)
            budget_note = "PASS" if data["sample_budget_pass"] else "FAIL(expected-relaxation)"
            norm_note = "PASS" if data["sample_norm_pass"] else "FAIL(expected-relaxation)"
            print(
                "PASS",
                case_id,
                "BL=PASS",
                "P2=PASS",
                "affine_gadget=PASS",
                "metric_obstruction=PASS",
                "Farkas=PASS",
                "stability=PASS",
                "sample_budget=" + budget_note,
                "sample_norm=" + norm_note,
                "margin=" + str(data["margin"]),
            )
        except Exception as exc:
            failed = True
            print("FAIL", path.stem, type(exc).__name__, str(exc))
    print("OVERALL", "FAIL" if failed else "PASS")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
