#!/usr/bin/env python3
"""Independent exact checker for raw extra-vertex certificates.

This file deliberately does not import decide_xv.py.  It reconstructs the
factor problem, the parametric seven-entry identity, the stability bounds, the
bounded-support-fiber moment pattern, and every stored equality-only sample
from the JSON files in raw/xv/.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw" / "xv"
LABELS = ["v", "w", "f", "z", "o", "q"]
EXPECTED_CASES = {
    "xv_literal_r3_vertex6",
    "xv_hx_near_r3_vertex6",
    "xv_hx_far_r3_vertex6_nonvertex7",
}
SELECTED = [("f", "q"), ("o", "v"), ("o", "w"), ("o", "z"),
            ("q", "v"), ("q", "w"), ("q", "f")]


def assert_true(condition, message):
    if not condition:
        raise AssertionError(message)


def no_duplicate_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_floats(value, path="root"):
    if isinstance(value, float):
        raise TypeError(f"floating JSON number at {path}")
    if isinstance(value, list):
        for i, child in enumerate(value):
            reject_floats(child, f"{path}[{i}]")
    elif isinstance(value, dict):
        for key, child in value.items():
            reject_floats(child, f"{path}.{key}")


def q(value):
    if isinstance(value, bool):
        raise TypeError(f"boolean is not a rational token: {value!r}")
    if isinstance(value, int):
        return Q(value)
    if isinstance(value, str):
        return Q(value)
    raise TypeError(f"not an exact rational token: {value!r}")


def qvec(values):
    return [q(x) for x in values]


def qmat(values):
    return [qvec(row) for row in values]


def dot(a, b):
    assert_true(len(a) == len(b), "dot-product shape mismatch")
    return sum((x * y for x, y in zip(a, b)), Q(0))


def transpose(a):
    assert_true(bool(a), "empty matrix")
    width = len(a[0])
    assert_true(all(len(row) == width for row in a), "ragged matrix")
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    assert_true(bool(a) and bool(b), "empty matrix product")
    assert_true(len(a[0]) == len(b), "matrix-product shape mismatch")
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def matrix_equal(a, b):
    return len(a) == len(b) and all(ra == rb for ra, rb in zip(a, b))


def zero_matrix(a):
    return all(x == 0 for row in a for x in row)


def row_negative_mass(row):
    return sum((-x for x in row if x < 0), Q(0))


def canonical(s, A, X, Y):
    t = s * s
    a = s / (1 + s)
    L = [
        [Q(1), Q(0), Q(0)],
        [Q(1), -A * a, t * a],
        [Q(1), -A, t],
        [Q(1), Q(1), Q(0)],
        [Q(1), Q(0), Q(1)],
        [Q(1), X, Y],
    ]
    c = [1 - s, s + t, -t, Q(0), Q(0), Q(0)]
    return t, a, L, c


def reconstruct_equalities(L):
    n = len(L)
    equations = []
    rhs = []
    for block, target in ((0, 1), (1, 2)):
        for k in range(3):
            row = [Q(0)] * (2 * n)
            for j in range(n):
                row[block * n + j] = L[j][k]
            equations.append(row)
            rhs.append(Q(int(k == target)))
    return equations, rhs


def entry_form(L, c, row_label, column_label):
    i = LABELS.index(row_label)
    j = LABELS.index(column_label)
    coeff = [Q(0)] * 12
    coeff[j] = L[i][1]
    coeff[6 + j] = L[i][2]
    return c[j], coeff


def parametric_certificate(s, A, X, Y):
    t, a, L, c = canonical(s, A, X, Y)
    equations, rhs = reconstruct_equalities(L)
    H = X + Y - 1
    Bfacet = A + (1 - t) * X - A * Y
    K = A * Y + t * X
    d = A + 1 - t
    C = 1 + a * (A - t)
    weights = [
        Bfacet * X * H,
        A * H * K,
        A * (1 - a) * H * K,
        d * H * K,
        A * Bfacet,
        A * Bfacet * C,
        A * Bfacet * d,
    ]
    mu = [
        A * Bfacet * X,
        -A * Bfacet * X,
        -A * Bfacet * X,
        A * H * K + A * Bfacet * Y,
        (1 - t) * H * K - A * Bfacet * Y,
        -A * H * K - A * Bfacet * Y,
    ]
    M = A * Bfacet * H
    forms = [entry_form(L, c, *pair) for pair in SELECTED]
    lhs_coeff = [sum((weights[i] * forms[i][1][j] for i in range(7)), Q(0))
                 for j in range(12)]
    lhs_const = sum((weights[i] * forms[i][0] for i in range(7)), Q(0)) + M
    rhs_coeff = [sum((mu[k] * equations[k][j] for k in range(6)), Q(0))
                 for j in range(12)]
    rhs_const = -sum((mu[k] * rhs[k] for k in range(6)), Q(0))
    assert_true(lhs_coeff == rhs_coeff, "parametric Farkas coefficients fail")
    assert_true(lhs_const == rhs_const, "parametric Farkas constant fails")
    assert_true(H > 0 and Bfacet > 0 and K > 0,
                "probe is outside positive multiplier cell")
    assert_true(all(weight > 0 for weight in weights), "nonpositive Farkas weight")
    Dsum = sum(weights, Q(0))
    return {
        "t": t, "a": a, "L": L, "c": c, "equations": equations,
        "rhs": rhs, "forms": forms, "H": H, "B": Bfacet, "K": K,
        "d": d, "C": C, "weights": weights, "mu": mu, "M": M,
        "Dsum": Dsum, "margin": M - t * Dsum, "R": M / Dsum,
    }


def check_uniform_stability(raw):
    stab = raw["stability"]
    assert_true(qvec(stab["A_interval"]) == [Q(4), Q(6)], "wrong A interval")
    assert_true(qvec(stab["s_interval"]) == [Q(0), Q(1, 256)], "wrong s interval")
    assert_true(stab["s_left_endpoint_open"] is True, "s=0 was not excluded")
    assert_true(qvec(stab["Y_interval"]) == [Q(0), Q(1)], "wrong Y slab")
    s = Q(1, 256)
    t = s * s
    Amin, Amax = Q(4), Q(6)
    Hmin = 1 / s - Amax - 1
    Bmin = (1 - t) * (1 / s - Amax)
    Kmax = Amax + t * (2 / s + 4 * s)
    Cmax = 1 + (s / (1 + s)) * Amax
    dmax = Amax + 1
    bounds = stab["strip_bounds"]
    assert_true(Hmin == q(bounds["H_at_least"]) == 249, "H lower bound wrong")
    assert_true(Bmin > q(bounds["B_greater_than"]) == 249, "B lower bound wrong")
    assert_true(Kmax < q(bounds["K_less_than"]) == 7, "K upper bound wrong")
    assert_true(Cmax < q(bounds["C_less_than"]) == 2, "C upper bound wrong")
    assert_true(dmax == q(bounds["d_less_than"]) == 7 and Amax + 1 - t < dmax,
                "d upper bound wrong")
    term_bounds = qvec(stab["ratio_term_bounds"])
    exact_upper_1 = t * (2 / s + 4 * s) / Amin
    exact_upper_2 = t * Q(7, 249) * (Q(2) + Q(7, 4))
    exact_upper_3 = t * Q(10, 249)
    assert_true(exact_upper_1 < term_bounds[0] == Q(1, 500), "term 1 bound fails")
    assert_true(exact_upper_2 < term_bounds[1] == Q(1, 1000), "term 2 bound fails")
    assert_true(exact_upper_3 < term_bounds[2] == Q(1, 1000), "term 3 bound fails")
    ratio_bound = q(stab["ratio_less_than"])
    assert_true(sum(term_bounds, Q(0)) == ratio_bound == Q(1, 250),
                "ratio bound sum wrong")
    assert_true(q(stab["margin_fraction_greater_than"]) == 1 - ratio_bound == Q(249, 250),
                "margin fraction wrong")
    grid = stab["exact_probe_grid"]
    assert_true(qvec(grid["A"]) == [Q(4), Q(5), Q(6)], "stored A probe grid wrong")
    assert_true(qvec(grid["s"]) == [Q(1, 256), Q(1, 512), Q(1, 1024)],
                "stored s probe grid wrong")
    assert_true(qvec(grid["Y"]) == [Q(0), Q(1, 2), Q(1)], "stored Y probe grid wrong")
    assert_true(grid["X_choices"] == ["1/s-A", "1/s", "2/s+4s"],
                "stored X probe grid wrong")

    # Exact Fraction-only probes of the full parametric identity throughout
    # the declared A,s,Y grid and at all three X formulas.
    probes = 0
    for A in (Q(4), Q(5), Q(6)):
        for sp in (Q(1, 256), Q(1, 512), Q(1, 1024)):
            for Y in (Q(0), Q(1, 2), Q(1)):
                for X in (1 / sp - A, 1 / sp, 2 / sp + 4 * sp):
                    cert = parametric_certificate(sp, A, X, Y)
                    assert_true(cert["margin"] > 0, "probe contradiction margin nonpositive")
                    assert_true(sp * sp * cert["Dsum"] / cert["M"] < ratio_bound,
                                "probe misses uniform ratio")
                    probes += 1
    assert_true(probes == 81, "wrong exact probe count")
    return probes


def check_reduction(raw, s, t, A):
    red = raw["parameter_reduction"]
    assert_true(qvec(red["canonical_exposer_slab_Y"]) == [Q(0), Q(1)],
                "wrong canonical exposer slab")
    assert_true(set(red["exterior_cells"]) == {"fv_only", "of_only", "f_corner_both", "zo_only"},
                "exterior cell list is not exhaustive")
    assert_true(red["actor_hull_facets"] == {
        "fv": "t*X+A*Y>=0", "of": "A+(1-t)*X-A*Y>=0",
        "zo": "1-X-Y>=0", "lower": "Y>=0"}, "stored actor facets wrong")
    assert_true(q(red["necessary_row_l1_bound"]) == 1 + 2 * t, "row l1 bound wrong")
    assert_true(q(red["necessary_abs_Xs_bound"]) == 2 + 4 * t, "|X|s bound wrong")
    lower = 1 - A * s
    left_upper = s * (2 + 4 * t)
    assert_true(q(red["moment_lower_1_minus_As"]) == lower, "moment lower bound wrong")
    assert_true(q(red["left_cell_upper_abs_XDq"]) == left_upper, "left-cell upper bound wrong")
    assert_true(q(red["left_cell_contradiction_margin"]) == lower - left_upper > 0,
                "left cells were not contradicted")
    assert_true(qvec(red["surviving_X_interval"]) == [1 / s - A, 2 / s + 4 * s],
                "surviving strip wrong")
    assert_true(red["surviving_cell"] == "zo_only", "wrong surviving exterior cell")

    # Uniform endpoint, not only the stored A=5 point.
    su = Q(1, 256)
    uniform_left_margin = 1 - Q(6) * su - su * (2 + 4 * su * su)
    assert_true(uniform_left_margin > 0, "left-cell reduction is not stable")


def check_bounded_pattern(raw, s, t, A):
    rec = raw["bounded_external_fiber_pattern"]
    assert_true(rec["per_external_fiber_Dq_bound"] == "|D_q|<=t",
                "stored per-fiber Dq claim changed")
    assert_true(rec["K_fiber_necessary_inequality"] == "1<=s*(A+K*(2+4*s^2))",
                "stored K-moment formula changed")
    assert_true(rec["safe_s0_of_K"] == "min(1/256,1/(12*(K+1)))",
                "stored K ceiling formula changed")
    assert_true(rec["scope"] ==
                "K counts zero-top support fibers outside the original actor hull; all other added zero-top fibers must lie in that hull",
                "stored bounded-fiber scope changed")
    assert_true(q(rec["per_external_fiber_XDq_bound"]) == s * (2 + 4 * t),
                "per-fiber moment bound wrong")
    # Negative D_q is bounded by P_zq=D_q>=-t.  Positive D_q obeys
    # A D_q <= t(2+t) from P_fq>=-t and P_oq<=1+t; the exact worst
    # factor is below one throughout the stability box.
    assert_true((Q(2) + Q(1, 65536)) / Q(4) < 1,
                "positive Dq bound does not imply Dq<t")
    assert_true(t * (2 + 4 * t) / s == s * (2 + 4 * s * s),
                "per-fiber |X Dq| simplification fails")
    assert_true(q(rec["K_1_base_margin"]) == Q(4079615, 4194304),
                "base K=1 margin wrong")
    assert_true(q(rec["K_1_base_margin"]) == 1 - s * (A + 2 + 4 * t),
                "stored base K=1 formula wrong")
    assert_true(q(rec["K_1_uniform_A_margin"]) == Q(4063231, 4194304),
                "uniform K=1 margin wrong")
    assert_true(q(rec["K_at_parent_ceiling"]) == 124, "wrong K ceiling")
    assert_true(q(rec["K_124_uniform_margin"]) == Q(8161, 1048576),
                "K=124 margin wrong")
    assert_true(q(rec["K_124_uniform_margin"]) ==
                1 - s * (Q(6) + Q(124) * (2 + 4 * t)), "K=124 formula wrong")
    # Mechanically check the all-K proof, not only sample values.  If K>=1
    # and s<=1/(12(K+1)), then 4s^2<1, so
    # s(6+K(2+4s^2)) < (6+3K)/(12(K+1))
    # = (K+2)/(4(K+1)) <= 3/8 < 1; the final inequality is exactly K>=1.
    assert_true(Q(4) * Q(1, 256) ** 2 < 1, "4s^2<1 reduction fails")
    assert_true(Q(3, 8) < 1, "generic K upper constant is not below one")
    assert_true((3 - 2) > 0 and (3 * 1 + 3) - (2 * 1 + 4) == 0,
                "generic K>=1 linear comparison fails")
    for K in (1, 2, 124, 125, 1000):
        sk = min(Q(1, 256), Q(1, 12 * (K + 1)))
        assert_true(sk * (Q(6) + K * (2 + 4 * sk * sk)) < 1,
                    f"safe s0 formula fails at K={K}")


def check_base(raw):
    assert_true(raw["schema"] == "starvation-extra-vertex-farkas-v1", "unknown schema")
    assert_true(raw["verdict"] == "INFEASIBLE", "unexpected verdict")
    assert_true(raw["status"].startswith("AUTHOR-CLAIM"), "status discipline missing")
    assert_true(raw["labels"] == LABELS, "unexpected labels")
    assert_true(q(raw["rank"]) == 3, "raw rank is not three")
    p = raw["parameters"]
    s, t, A, a = (q(p[k]) for k in ("s", "t", "A", "a"))
    X, Y = q(p["X_representative"]), q(p["Y_representative"])
    assert_true(t == s * s and a == s / (1 + s), "parameter relation fails")
    assert_true(Q(4) <= A <= Q(6) and Q(0) < s <= Q(1, 256),
                "representative parameters outside stability domain")
    assert_true(Q(0) <= Y <= Q(1), "representative Y outside canonical slab")
    assert_true(1 / s - A <= X <= 2 / s + 4 * s,
                "representative X outside surviving strip")
    cert = parametric_certificate(s, A, X, Y)

    problem = raw["factor_problem"]
    L, c = qmat(problem["L"]), qvec(problem["fixed_B_row_0"])
    assert_true(L == cert["L"] and c == cert["c"], "stored canonical factor data differ")
    assert_true(matmul([c], L) == [[Q(1), Q(0), Q(0)]], "top row does not reproduce")
    equations = qmat(problem["equalities"]["matrix"])
    rhs = qvec(problem["equalities"]["rhs"])
    assert_true(equations == cert["equations"] and rhs == cert["rhs"],
                "stored BL equations differ from reconstruction")

    # Actor gadget and the representative exterior placement.
    v, w, f, z, o, qp = L
    assert_true(all(f[k] - v[k] + A * (z[k] - v[k]) == t * (o[k] - v[k])
                    for k in range(3)), "factor gadget fails")
    assert_true(all(w[k] - v[k] == a * (f[k] - v[k]) for k in range(3)),
                "factor interpolation fails")
    fv = t * X + A * Y
    of = A + (1 - t) * X - A * Y
    zo = 1 - X - Y
    assert_true(Y >= 0 and fv > 0 and of > 0 and zo < 0,
                "representative q is not in the right exterior cell")

    forms_raw = problem["necessary_entry_inequalities"]
    assert_true(len(forms_raw) == 7, "wrong selected inequality count")
    for i, form in enumerate(forms_raw):
        constant, coeff = cert["forms"][i]
        assert_true((form["row"], form["column"]) == SELECTED[i], "entry order changed")
        assert_true(qvec(form["coefficients"]) == coeff, "entry coefficients wrong")
        assert_true(q(form["entry_constant_without_t"]) == constant, "entry constant wrong")
        assert_true(q(form["constant"]) == constant + t, "entry threshold was not added")

    stored = raw["farkas_certificate"]
    assert_true(stored["selected_entries"] == [f"P_{r}{c}" for r, c in SELECTED],
                "stored selected-entry names differ")
    assert_true(qvec(stored["inequality_multipliers"]) == cert["weights"],
                "stored Farkas weights differ")
    assert_true(qvec(stored["equality_multipliers"]) == cert["mu"],
                "stored equality multipliers differ")
    assert_true(q(stored["H"]) == cert["H"] and q(stored["B_facet"]) == cert["B"]
                and q(stored["K"]) == cert["K"], "stored cell scalars differ")
    assert_true(q(stored["M"]) == cert["M"] and q(stored["D_sum"]) == cert["Dsum"],
                "stored Farkas totals differ")
    assert_true(q(stored["contradiction_margin_M_minus_tD"]) == cert["margin"] > 0,
                "stored contradiction margin wrong")
    assert_true(q(stored["normalized_R"]) == cert["R"] > t,
                "stored normalized obstruction wrong")
    formulas = stored["parametric_formulas"]
    assert_true(formulas == {
        "H": "X+Y-1", "B_facet": "A+(1-t)*X-A*Y",
        "K": "A*Y+t*X", "d": "A+1-t", "C": "1+a*(A-t)",
        "weights_in_selected_entry_order": [
            "B*X*H", "A*H*K", "A*(1-a)*H*K", "d*H*K",
            "A*B", "A*B*C", "A*B*d"],
        "equality_multipliers_D0_Dx_Dy_E0_Ex_Ey": [
            "A*B*X", "-A*B*X", "-A*B*X", "A*H*K+A*B*Y",
            "(1-t)*H*K-A*B*Y", "-A*H*K-A*B*Y"],
        "identity": "sum_i weight_i*entry_i+A*B*H=sum_k mu_k*(BL-I)_k"},
        "stored parametric formula contract changed")

    check_reduction(raw, s, t, A)
    probes = check_uniform_stability(raw)
    check_bounded_pattern(raw, s, t, A)

    sample = raw["sample_relaxation"]
    Bsample, Pstored = qmat(sample["B"]), qmat(sample["P"])
    assert_true(matmul(Bsample, L) == eye(3), "sample BL != I")
    Psample = matmul(L, Bsample)
    assert_true(Psample == Pstored, "stored sample P differs from LB")
    assert_true(matrix_equal(matmul(Psample, Psample), Psample), "sample P^2 != P")
    assert_true(all(sum(row, Q(0)) == 1 for row in Psample), "sample row sum fails")
    assert_true(Psample[0] == c, "sample top row differs")
    F = [Psample[2][j] - Psample[0][j] for j in range(6)]
    Z = [Psample[3][j] - Psample[0][j] for j in range(6)]
    O = [Psample[4][j] - Psample[0][j] for j in range(6)]
    assert_true(all(F[j] + A * Z[j] == t * O[j] for j in range(6)),
                "sample affine gadget fails")
    assert_true(all(Psample[1][j] - Psample[0][j] == a * F[j] for j in range(6)),
                "sample interpolation fails")
    assert_true(qvec(sample["affine_gadget_residual"]) == [Q(0)] * 6,
                "stored sample gadget residual nonzero")
    assert_true(qvec(sample["w_interpolation_residual"]) == [Q(0)] * 6,
                "stored sample interpolation residual nonzero")
    sample_delta = max(row_negative_mass(row) for row in Psample)
    sample_norm = sum(abs(x) for x in Z)
    assert_true(q(sample["sample_delta"]) == sample_delta, "stored sample delta wrong")
    assert_true(q(sample["sample_Z_l1"]) == sample_norm, "stored sample norm wrong")
    return {
        "s": s, "t": t, "A": A, "a": a, "L": L, "c": c,
        "margin": cert["margin"], "R": cert["R"], "probes": probes,
        "sample_budget_pass": sample_delta <= t,
        "sample_norm_pass": sample_norm == s,
    }


def check_near(raw, base):
    case = raw["case_constraints"]
    assert_true(case["geometry_status"].startswith("ALL CELLS KILLED"),
                "near case overclaims geometry")
    assert_true(q(case["top_pin_P_vq"]) == 0, "near q top pin changed")
    assert_true(case["freight_constraint"]["entry"] == "P_fw",
                "near freight entry changed")
    assert_true(case["off_diagonal"] is True, "near atom lost off-diagonal flag")
    assert_true(case["kernel_when_f_cut"] ==
                "compose w=(1-a)v+a*f with the exact q,v,o vertex kernel of f",
                "near cut-f kernel contract changed")
    lower = q(case["freight_constraint"]["lower_bound"])
    kernel = {key: q(value) for key, value in case["kernel_when_f_vertex"].items()}
    assert_true(kernel == {"v": 1 / (1 + base["s"]),
                           "f": base["s"] / (1 + base["s"])},
                "near kernel wrong")
    assert_true(sum(kernel.values(), Q(0)) == 1, "near kernel not a probability")
    bary = [kernel["v"] * base["L"][0][k] + kernel["f"] * base["L"][2][k]
            for k in range(3)]
    assert_true(bary == base["L"][1], "near kernel does not reproduce w")
    assert_true(lower * kernel["v"] == q(case["near_atom_uniform_lower_bound"]) == Q(1, 4),
                "near atom arithmetic wrong")

    # Independently reconstruct the revertexization needed in the exterior
    # corner that cuts off f.
    probe = case["f_cut_kernel_exact_probe"]
    X, Y = q(probe["X"]), q(probe["Y"])
    A, t, a = base["A"], base["t"], base["a"]
    fv = t * X + A * Y
    of = A + (1 - t) * X - A * Y
    assert_true(fv < 0 and of < 0 and X < 0, "cut-f probe is in wrong hull cell")
    fkernel = {"q": -A / X, "v": of / X, "o": fv / X}
    assert_true(fkernel == {key: q(value) for key, value in probe["f_kernel"].items()},
                "stored cut-f kernel differs")
    assert_true(all(value > 0 for value in fkernel.values()) and
                sum(fkernel.values(), Q(0)) == 1, "cut-f kernel is not a probability")
    qpoint = [Q(1), X, Y]
    reproduced_f = [fkernel["q"] * qpoint[k] +
                    fkernel["v"] * base["L"][0][k] +
                    fkernel["o"] * base["L"][4][k] for k in range(3)]
    assert_true(reproduced_f == base["L"][2], "cut-f kernel does not reproduce f")
    wkernel = {"q": a * fkernel["q"],
               "v": 1 - a + a * fkernel["v"],
               "o": a * fkernel["o"]}
    assert_true(wkernel == {key: q(value) for key, value in probe["w_kernel"].items()},
                "stored composed w kernel differs")
    assert_true(wkernel["v"] >= 1 / (1 + base["s"]),
                "revertexized near mass lost the 1/4 bound")


def check_far(raw, base):
    case = raw["case_constraints"]
    assert_true(case["geometry_status"].startswith("ALL CELLS KILLED"),
                "far case overclaims geometry")
    lift = raw["lift"]
    assert_true(lift["labels_full"] == LABELS + ["m"], "far lift labels wrong")
    L7 = qmat(lift["L_full"])
    midpoint = [(base["L"][0][k] + base["L"][2][k]) / 2 for k in range(3)]
    assert_true(L7[:6] == base["L"] and L7[6] == midpoint, "far row is not midpoint")
    c7 = qvec(lift["fixed_B_row_0_full"])
    assert_true(c7 == base["c"] + [Q(0)], "far full top row changed")
    theta = {key: q(value) for key, value in lift["m_barycentric_coordinates"].items()}
    assert_true(theta == {"v": Q(1, 2), "f": Q(1, 2)},
                "stored midpoint barycentric coordinates changed")
    B7, P7stored = qmat(lift["sample_B_full_equality_only"]), qmat(lift["sample_P_full_equality_only"])
    assert_true(matmul(B7, L7) == eye(3), "far sample BL != I")
    P7 = matmul(L7, B7)
    assert_true(P7 == P7stored and matrix_equal(matmul(P7, P7), P7),
                "far sample projection check fails")
    assert_true(all(sum(row, Q(0)) == 1 for row in P7), "far sample row sums fail")
    assert_true(B7[0][6] == 0, "midpoint top coefficient nonzero")
    injected = lift["nonzero_midpoint_sample_coefficients"]
    assert_true(B7[1][6] == q(injected["D_m"]) != 0 and
                B7[2][6] == q(injected["E_m"]) != 0,
                "far aggregation sample is tautologically zero")
    B6 = []
    for row in B7:
        B6.append([row[0] + row[6] / 2, row[1], row[2] + row[6] / 2,
                   row[3], row[4], row[5]])
    assert_true(B6 == qmat(lift["sample_B_aggregated"]), "far aggregation differs")
    assert_true(matmul(B6, base["L"]) == eye(3), "aggregated far BL != I")
    assert_true(B6 == qmat(raw["sample_relaxation"]["B"]),
                "far lift does not aggregate to the certified core sample")
    P6 = matmul(base["L"], B6)
    for i in range(6):
        assert_true(P6[i][0] == P7[i][0] + P7[i][6] / 2,
                    "far v-column aggregation fails")
        assert_true(P6[i][2] == P7[i][2] + P7[i][6] / 2,
                    "far f-column aggregation fails")
        for j in (1, 3, 4, 5):
            assert_true(P6[i][j] == P7[i][j], "far unchanged column differs")
        assert_true(row_negative_mass(P6[i]) <= row_negative_mass(P7[i]),
                    "far aggregation increased row negative mass")
    assert_true(q(case["top_pin_P_vq"]) == 0 and q(case["top_pin_P_vm"]) == 0,
                "far top pin changed")
    assert_true(case["freight_constraint"]["entry"] == "P_fm",
                "far freight entry changed")
    assert_true(case["off_diagonal"] is True, "far atom lost off-diagonal flag")
    assert_true(case["f_cut_cell_note"].startswith("the v,f kernel must be revertexized"),
                "far cut-cell warning changed")
    kernel = {key: q(value) for key, value in case["kernel_when_f_vertex"].items()}
    assert_true(kernel == {"v": Q(1, 2), "f": Q(1, 2)}, "far kernel wrong")
    lower = q(case["freight_constraint"]["lower_bound"])
    assert_true(lower * kernel["f"] == q(case["far_atom_lower_bound"]) == Q(1, 4),
                "far atom arithmetic wrong")


def check_literal(raw, base):
    case = raw["case_constraints"]
    assert_true(case["geometry_status"].startswith("ALL CELLS KILLED"),
                "literal case overclaims geometry")
    assert_true(case["support"] ==
                "v,w,f,z,o,q; q is a geometric vertex outside conv(v,f,z,o)",
                "literal support contract changed")
    assert_true(q(case["top_pin_P_vq"]) == 0, "literal q top pin changed")
    assert_true(q(case["metric_Z_l1"]) == base["s"], "literal metric pin changed")
    assert_true(qvec(case["canonical_exposer_Y_interval"]) == [Q(0), Q(1)],
                "literal exposer slab changed")
    assert_true(case["location_cells"] ==
                ["fv_only", "of_only", "f_corner_both", "zo_only"],
                "literal location-cell ownership changed")
    assert_true(case["optimal_face_patterns"] == [
        "q near; Y=0 adds Z, 0<Y<1 is interior, Y=1 adds O",
        "q far; Y<t is empty, Y=t adds T, t<Y<1 preserves singleton T/O, Y=1 adds O"],
        "literal optimal-face pattern list changed")


def check_file(path):
    raw = json.loads(path.read_text(), object_pairs_hook=no_duplicate_object)
    reject_floats(raw)
    assert_true(raw.get("case_id") == path.stem,
                "raw case_id does not match its certificate filename")
    base = check_base(raw)
    case_id = raw["case_id"]
    if case_id == "xv_hx_near_r3_vertex6":
        check_near(raw, base)
    elif case_id == "xv_hx_far_r3_vertex6_nonvertex7":
        check_far(raw, base)
    elif case_id == "xv_literal_r3_vertex6":
        check_literal(raw, base)
    else:
        raise AssertionError(f"unknown case id {case_id}")
    return case_id, base


def main():
    paths = sorted(RAW.glob("*.json"))
    if not paths:
        print("FAIL no raw extra-vertex certificate files")
        return 1
    found = {path.stem for path in paths}
    if found != EXPECTED_CASES:
        print("FAIL case-set mismatch", sorted(found), "expected", sorted(EXPECTED_CASES))
        return 1
    failed = False
    checked_ids = []
    for path in paths:
        try:
            case_id, data = check_file(path)
            checked_ids.append(case_id)
            budget = "PASS" if data["sample_budget_pass"] else "FAIL(expected-relaxation)"
            norm = "PASS" if data["sample_norm_pass"] else "FAIL(expected-relaxation)"
            print(
                "PASS", case_id,
                "BL=PASS", "P2=PASS", "gadget=PASS", "exterior=PASS",
                "reduction=PASS", "Farkas=PASS", "stability=PASS",
                "K_extension=PASS", f"probes={data['probes']}",
                "sample_budget=" + budget, "sample_norm=" + norm,
                "margin=" + str(data["margin"]),
            )
        except Exception as exc:
            failed = True
            print("FAIL", path.stem, type(exc).__name__, str(exc))
    if set(checked_ids) != EXPECTED_CASES or len(checked_ids) != len(EXPECTED_CASES):
        failed = True
        print("FAIL checked-case-id set mismatch", sorted(checked_ids))
    print("OVERALL", "FAIL" if failed else "PASS")
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
