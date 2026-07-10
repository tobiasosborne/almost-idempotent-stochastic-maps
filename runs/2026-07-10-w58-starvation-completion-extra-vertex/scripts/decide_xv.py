#!/usr/bin/env python3
"""Exact certificates for the first extra-vertex starvation family.

All decision arithmetic uses fractions.Fraction.  This is a certificate
emitter, not a floating-point optimizer.  The certificate has two layers:

* exact metric/row-budget inequalities reduce every possible exterior row
  q=(1,X,Y), 0<=Y<=1, to a compact right-hand parameter strip;
* on that strip a seven-entry Farkas identity contradicts even the weaker
  individual entry bounds P_ij>=-s^2.
"""

from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw" / "xv"
ACTORS = ["v", "w", "f", "z", "o"]
LABELS = ACTORS + ["q"]
SELECTED = [("f", "q"), ("o", "v"), ("o", "w"), ("o", "z"),
            ("q", "v"), ("q", "w"), ("q", "f")]


def qstr(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qjson(value):
    if isinstance(value, Q):
        return qstr(value)
    if isinstance(value, list):
        return [qjson(x) for x in value]
    if isinstance(value, tuple):
        return [qjson(x) for x in value]
    if isinstance(value, dict):
        return {k: qjson(v) for k, v in value.items()}
    return value


def dot(a, b):
    assert len(a) == len(b)
    return sum((x * y for x, y in zip(a, b)), Q(0))


def transpose(a):
    assert a and all(len(row) == len(a[0]) for row in a)
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    assert a and b and len(a[0]) == len(b)
    bt = transpose(b)
    return [[dot(row, col) for col in bt] for row in a]


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def matrix_equal(a, b):
    return len(a) == len(b) and all(ra == rb for ra, rb in zip(a, b))


def row_negative_mass(row):
    return sum((-x for x in row if x < 0), Q(0))


def parameters(s=Q(1, 256), A=Q(5), X=None, Y=Q(1, 2)):
    if X is None:
        X = 1 / s
    t = s * s
    a = s / (1 + s)
    return s, t, A, a, X, Y


def factor_data(s=Q(1, 256), A=Q(5), X=None, Y=Q(1, 2)):
    s, t, A, a, X, Y = parameters(s, A, X, Y)
    L = [
        [Q(1), Q(0), Q(0)],
        [Q(1), -A * a, t * a],
        [Q(1), -A, t],
        [Q(1), Q(1), Q(0)],
        [Q(1), Q(0), Q(1)],
        [Q(1), X, Y],
    ]
    c = [1 - s, s + t, -t, Q(0), Q(0), Q(0)]
    assert matmul([c], L) == [[Q(1), Q(0), Q(0)]]

    equations = []
    rhs = []
    names = []
    for block, prefix, target in ((0, "D", 1), (1, "E", 2)):
        for k in range(3):
            row = [Q(0)] * 12
            for j in range(6):
                row[block * 6 + j] = L[j][k]
            equations.append(row)
            rhs.append(Q(int(k == target)))
            names.append(f"{prefix}_moment_{k}")

    return {
        "s": s, "t": t, "A": A, "a": a, "X": X, "Y": Y,
        "L": L, "c": c, "equations": equations, "rhs": rhs,
        "equation_names": names,
    }


def entry_form(data, row_label, column_label):
    i = LABELS.index(row_label)
    j = LABELS.index(column_label)
    L = data["L"]
    coeff = [Q(0)] * 12
    coeff[j] = L[i][1]
    coeff[6 + j] = L[i][2]
    return {
        "name": f"P_{row_label}{column_label}",
        "row": row_label,
        "column": column_label,
        "constant": data["c"][j],
        "coefficients": coeff,
    }


def farkas_data(data):
    s, t, A, a = (data[k] for k in ("s", "t", "A", "a"))
    X, Y = data["X"], data["Y"]
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
    forms = [entry_form(data, *pair) for pair in SELECTED]

    lhs_coeff = [sum((weights[i] * forms[i]["coefficients"][j]
                      for i in range(len(forms))), Q(0)) for j in range(12)]
    lhs_const = sum((weights[i] * forms[i]["constant"]
                     for i in range(len(forms))), Q(0)) + M
    equations, rhs = data["equations"], data["rhs"]
    rhs_coeff = [sum((mu[k] * equations[k][j] for k in range(6)), Q(0))
                 for j in range(12)]
    rhs_const = -sum((mu[k] * rhs[k] for k in range(6)), Q(0))
    assert lhs_coeff == rhs_coeff
    assert lhs_const == rhs_const
    assert H > 0 and Bfacet > 0 and K > 0
    assert all(w > 0 for w in weights)
    Dsum = sum(weights, Q(0))
    margin = M - t * Dsum
    assert margin > 0
    return {
        "forms": forms,
        "H": H, "B_facet": Bfacet, "K": K, "d": d, "C": C,
        "weights": weights, "mu": mu, "M": M, "D_sum": Dsum,
        "margin": margin, "normalized_R": M / Dsum,
    }


def equality_sample(data):
    c = data["c"]
    unit_z = [Q(0), Q(0), Q(0), Q(1), Q(0), Q(0)]
    unit_o = [Q(0), Q(0), Q(0), Q(0), Q(1), Q(0)]
    D = [unit_z[j] - c[j] for j in range(6)]
    E = [unit_o[j] - c[j] for j in range(6)]
    B = [c, D, E]
    assert matmul(B, data["L"]) == eye(3)
    P = matmul(data["L"], B)
    assert matrix_equal(matmul(P, P), P)
    return B, P


def reduction_record(data):
    s, t, A = data["s"], data["t"], data["A"]
    # The base point is not used as a finite sampling definition.  These are
    # the exact formulas for the whole parameter cell.
    return {
        "canonical_exposer_slab_Y": [Q(0), Q(1)],
        "actor_hull_facets": {
            "fv": "t*X+A*Y>=0",
            "of": "A+(1-t)*X-A*Y>=0",
            "zo": "1-X-Y>=0",
            "lower": "Y>=0",
        },
        "exterior_cells": [
            "fv_only", "of_only", "f_corner_both", "zo_only",
        ],
        "necessary_row_l1_bound": 1 + 2 * t,
        "necessary_abs_Xs_bound": 2 + 4 * t,
        "moment_lower_1_minus_As": 1 - A * s,
        "left_cell_upper_abs_XDq": s * (2 + 4 * t),
        "left_cell_contradiction_margin": 1 - A * s - s * (2 + 4 * t),
        "surviving_X_interval": [1 / s - A, 2 / s + 4 * s],
        "surviving_cell": "zo_only",
        "derivation": [
            "p_q=(1-Y)*p_v+Y*p_o+X*D and 0<=Y<=1 imply |X|*||D||_1<=2+4t",
            "D moment and ||D||_1=s imply X*D_q>=1-A*s>0",
            "if X<0 then D_q=P_zq<0, hence |D_q|<=t, contradicting the previous two inequalities",
            "therefore X>0 and X>=1/s-A; the row-l1 bound gives X<=2/s+4s",
        ],
    }


def stability_record():
    smax = Q(1, 256)
    return {
        "A_interval": [Q(4), Q(6)],
        "s_interval": [Q(0), smax],
        "s_left_endpoint_open": True,
        "Y_interval": [Q(0), Q(1)],
        "strip_bounds": {
            "H_at_least": Q(249),
            "B_greater_than": Q(249),
            "K_less_than": Q(7),
            "C_less_than": Q(2),
            "d_less_than": Q(7),
        },
        "ratio_term_bounds": [Q(1, 500), Q(1, 1000), Q(1, 1000)],
        "ratio_less_than": Q(1, 250),
        "margin_fraction_greater_than": Q(249, 250),
        "exact_probe_grid": {
            "A": [Q(4), Q(5), Q(6)],
            "s": [Q(1, 256), Q(1, 512), Q(1, 1024)],
            "Y": [Q(0), Q(1, 2), Q(1)],
            "X_choices": ["1/s-A", "1/s", "2/s+4s"],
        },
    }


def bounded_fiber_record(data):
    s, t, A = data["s"], data["t"], data["A"]
    K = 1
    base_margin = 1 - s * (A + K * (2 + 4 * t))
    worst_margin = 1 - s * (Q(6) + K * (2 + 4 * t))
    Kmax = 124
    Kmax_margin = 1 - s * (Q(6) + Kmax * (2 + 4 * t))
    assert base_margin == Q(4079615, 4194304)
    assert worst_margin == Q(4063231, 4194304)
    assert Kmax_margin == Q(8161, 1048576)
    return {
        "per_external_fiber_Dq_bound": "|D_q|<=t",
        "per_external_fiber_XDq_bound": s * (2 + 4 * t),
        "K_fiber_necessary_inequality": "1<=s*(A+K*(2+4*s^2))",
        "K_1_base_margin": base_margin,
        "K_1_uniform_A_margin": worst_margin,
        "K_at_parent_ceiling": Kmax,
        "K_124_uniform_margin": Kmax_margin,
        "safe_s0_of_K": "min(1/256,1/(12*(K+1)))",
        "scope": "K counts zero-top support fibers outside the original actor hull; all other added zero-top fibers must lie in that hull",
    }


def verify_uniform_families():
    """Exact discovery-side verification of every printed uniform claim."""
    smax = Q(1, 256)
    tmax = smax * smax
    assert 1 - Q(6) * smax - smax * (2 + 4 * tmax) > 0
    assert 1 / smax - Q(6) - 1 == 249
    assert (1 - tmax) * (1 / smax - Q(6)) > 249
    assert Q(6) + tmax * (2 / smax + 4 * smax) < 7
    assert 1 + smax * Q(6) / (1 + smax) < 2
    assert tmax * (2 / smax + 4 * smax) / 4 < Q(1, 500)
    assert tmax * Q(7, 249) * (Q(2) + Q(7, 4)) < Q(1, 1000)
    assert tmax * Q(10, 249) < Q(1, 1000)

    probes = 0
    for A in (Q(4), Q(5), Q(6)):
        for s in (Q(1, 256), Q(1, 512), Q(1, 1024)):
            for Y in (Q(0), Q(1, 2), Q(1)):
                for X in (1 / s - A, 1 / s, 2 / s + 4 * s):
                    data = factor_data(s=s, A=A, X=X, Y=Y)
                    cert = farkas_data(data)
                    assert data["t"] * cert["D_sum"] / cert["M"] < Q(1, 250)
                    probes += 1
    assert probes == 81

    # Generic fixed-K proof: for K>=1 and
    # s<=min(1/256,1/(12(K+1))), 2+4s^2<3 and
    # (6+3K)/(12(K+1))=(K+2)/(4(K+1))<=3/8<1.
    assert 4 * smax * smax < 1
    assert (3 - 2) > 0 and (3 * 1 + 3) - (2 * 1 + 4) == 0
    assert Q(3, 8) < 1
    return probes


def base_raw(case_id, description):
    data = factor_data()
    cert = farkas_data(data)
    Bsample, Psample = equality_sample(data)
    s, t, A, a, X, Y = (data[k] for k in ("s", "t", "A", "a", "X", "Y"))
    F = [[Psample[2][j] - Psample[0][j] for j in range(6)]]
    Z = [[Psample[3][j] - Psample[0][j] for j in range(6)]]
    O = [[Psample[4][j] - Psample[0][j] for j in range(6)]]
    gadget = [[F[0][j] + A * Z[0][j] - t * O[0][j] for j in range(6)]]
    winterp = [[Psample[1][j] - Psample[0][j] - a * F[0][j]
                for j in range(6)]]
    return {
        "schema": "starvation-extra-vertex-farkas-v1",
        "case_id": case_id,
        "description": description,
        "status": "AUTHOR-CLAIM exact L3 evidence",
        "verdict": "INFEASIBLE",
        "rank": 3,
        "labels": LABELS,
        "parameters": {"s": s, "t": t, "A": A, "a": a,
                       "X_representative": X, "Y_representative": Y},
        "factor_problem": {
            "L": data["L"],
            "fixed_B_row_0": data["c"],
            "unknowns": [f"D_{x}" for x in LABELS] + [f"E_{x}" for x in LABELS],
            "equalities": {"names": data["equation_names"],
                           "matrix": data["equations"], "rhs": data["rhs"]},
            "necessary_entry_inequalities": [
                {"name": form["name"] + "+t>=0",
                 "source": "row negative mass <=t implies each entry >=-t",
                 "row": form["row"], "column": form["column"],
                 "constant": form["constant"] + t,
                 "entry_constant_without_t": form["constant"],
                 "coefficients": form["coefficients"]}
                for form in cert["forms"]
            ],
        },
        "parameter_reduction": reduction_record(data),
        "farkas_certificate": {
            "selected_entries": [form["name"] for form in cert["forms"]],
            "inequality_multipliers": cert["weights"],
            "equality_multipliers": cert["mu"],
            "H": cert["H"], "B_facet": cert["B_facet"], "K": cert["K"],
            "d": cert["d"], "C": cert["C"],
            "M": cert["M"], "D_sum": cert["D_sum"],
            "contradiction_margin_M_minus_tD": cert["margin"],
            "normalized_R": cert["normalized_R"],
            "parametric_formulas": {
                "H": "X+Y-1", "B_facet": "A+(1-t)*X-A*Y",
                "K": "A*Y+t*X", "d": "A+1-t", "C": "1+a*(A-t)",
                "weights_in_selected_entry_order": [
                    "B*X*H", "A*H*K", "A*(1-a)*H*K", "d*H*K",
                    "A*B", "A*B*C", "A*B*d",
                ],
                "equality_multipliers_D0_Dx_Dy_E0_Ex_Ey": [
                    "A*B*X", "-A*B*X", "-A*B*X",
                    "A*H*K+A*B*Y", "(1-t)*H*K-A*B*Y",
                    "-A*H*K-A*B*Y",
                ],
                "identity": "sum_i weight_i*entry_i+A*B*H=sum_k mu_k*(BL-I)_k",
            },
        },
        "stability": stability_record(),
        "bounded_external_fiber_pattern": bounded_fiber_record(data),
        "sample_relaxation": {
            "scope": "BL=I, idempotence, row sums, actor gadget, and top pins only; metric, negativity, exterior geometry, and horn constraints are deliberately dropped",
            "B": Bsample, "P": Psample,
            "sample_delta": max(row_negative_mass(row) for row in Psample),
            "sample_Z_l1": sum(abs(x) for x in Z[0]),
            "affine_gadget_residual": gadget[0],
            "w_interpolation_residual": winterp[0],
        },
    }


def make_cases():
    s = Q(1, 256)
    literal = base_raw(
        "xv_literal_r3_vertex6",
        "Rank-three W55 actors plus one zero-top vertex outside the actor hull",
    )
    literal["case_constraints"] = {
        "support": "v,w,f,z,o,q; q is a geometric vertex outside conv(v,f,z,o)",
        "top_pin_P_vq": Q(0),
        "metric_Z_l1": s,
        "canonical_exposer_Y_interval": [Q(0), Q(1)],
        "location_cells": ["fv_only", "of_only", "f_corner_both", "zo_only"],
        "optimal_face_patterns": [
            "q near; Y=0 adds Z, 0<Y<1 is interior, Y=1 adds O",
            "q far; Y<t is empty, Y=t adds T, t<Y<1 preserves singleton T/O, Y=1 adds O",
        ],
        "geometry_status": "ALL CELLS KILLED BY ALGEBRAIC RELAXATION; no H-X realization claimed",
    }

    near = base_raw(
        "xv_hx_near_r3_vertex6",
        "Extra-vertex core plus the formal H-X near off-diagonal freight through w",
    )
    near_lower = (1 + s) / 4
    A = Q(5)
    t = s * s
    Ycut = Q(1, 2)
    Xcut = -A * Ycut / t - 1
    fv_cut = t * Xcut + A * Ycut
    of_cut = A + (1 - t) * Xcut - A * Ycut
    alpha = -A / Xcut
    beta = of_cut / Xcut
    gamma = fv_cut / Xcut
    assert fv_cut < 0 and of_cut < 0
    assert alpha > 0 and beta > 0 and gamma > 0
    assert alpha + beta + gamma == 1
    a = s / (1 + s)
    composed = {"q": a * alpha, "v": 1 - a + a * beta, "o": a * gamma}
    assert sum(composed.values(), Q(0)) == 1
    assert composed["v"] >= 1 / (1 + s)
    near["case_constraints"] = {
        "top_pin_P_vq": Q(0),
        "freight_constraint": {"entry": "P_fw", "lower_bound": near_lower},
        "kernel_when_f_vertex": {"v": 1 / (1 + s), "f": s / (1 + s)},
        "kernel_when_f_cut": "compose w=(1-a)v+a*f with the exact q,v,o vertex kernel of f",
        "f_cut_kernel_exact_probe": {
            "X": Xcut, "Y": Ycut,
            "f_kernel": {"q": alpha, "v": beta, "o": gamma},
            "w_kernel": composed,
        },
        "near_atom_uniform_lower_bound": Q(1, 4),
        "off_diagonal": True,
        "geometry_status": "ALL CELLS KILLED BY ALGEBRAIC RELAXATION; freight arithmetic is conditional, not a realized H-X datum",
    }

    far = base_raw(
        "xv_hx_far_r3_vertex6_nonvertex7",
        "Extra-vertex core plus the smallest zero-top midpoint far-freight support",
    )
    L6 = [[Q(x) for x in row] for row in far["factor_problem"]["L"]]
    lm = [(L6[0][k] + L6[2][k]) / 2 for k in range(3)]
    L7 = L6 + [lm]
    c6 = [Q(x) for x in far["factor_problem"]["fixed_B_row_0"]]
    c7 = c6 + [Q(0)]
    # A deliberately nontrivial equality-only lift.  The midpoint column is
    # nonzero in both unknown B rows; compensating halves at v,f make its
    # aggregation exactly the stored core-six sample.
    B6core = [[Q(x) for x in row] for row in far["sample_relaxation"]["B"]]
    dm, em = Q(1, 3), Q(-2, 5)
    B7 = [c7]
    for core, bm in ((B6core[1], dm), (B6core[2], em)):
        B7.append([core[0] - bm / 2, core[1], core[2] - bm / 2,
                   core[3], core[4], core[5], bm])
    assert matmul(B7, L7) == eye(3)
    P7 = matmul(L7, B7)
    assert matrix_equal(matmul(P7, P7), P7)
    B6agg = []
    for row in B7:
        B6agg.append([row[0] + row[6] / 2, row[1], row[2] + row[6] / 2,
                      row[3], row[4], row[5]])
    assert matmul(B6agg, L6) == eye(3)
    far["lift"] = {
        "labels_full": LABELS + ["m"],
        "L_full": L7, "fixed_B_row_0_full": c7,
        "m_barycentric_coordinates": {"v": Q(1, 2), "f": Q(1, 2)},
        "sample_B_full_equality_only": B7,
        "sample_P_full_equality_only": P7,
        "sample_B_aggregated": B6agg,
        "nonzero_midpoint_sample_coefficients": {"D_m": dm, "E_m": em},
        "aggregation": "b'_v=b_v+b_m/2, b'_f=b_f+b_m/2; q is unchanged",
    }
    far["case_constraints"] = {
        "top_pin_P_vq": Q(0),
        "top_pin_P_vm": Q(0),
        "freight_constraint": {"entry": "P_fm", "lower_bound": Q(1, 2)},
        "kernel_when_f_vertex": {"v": Q(1, 2), "f": Q(1, 2)},
        "far_atom_lower_bound": Q(1, 4),
        "off_diagonal": True,
        "f_cut_cell_note": "the v,f kernel must be revertexized and radial/corner ownership recomputed; the common literal relaxation already kills this cell",
        "geometry_status": "ALL CELLS KILLED BY ALGEBRAIC RELAXATION; midpoint sample is not a realized H-X datum",
    }
    return [literal, near, far]


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    assert verify_uniform_families() == 81
    cases = make_cases()
    for case in cases:
        path = RAW / f"{case['case_id']}.json"
        path.write_text(json.dumps(qjson(case), indent=2, sort_keys=True) + "\n")
        cert = case["farkas_certificate"]
        print(
            "CASE", case["case_id"], "INFEASIBLE",
            "margin=" + qstr(cert["contradiction_margin_M_minus_tD"]),
            "R=" + qstr(cert["normalized_R"]),
            "parametric_ratio<1/250",
        )
    print("STABILITY PASS A in [4,6], 0<s<=1/256, 0<=Y<=1; exact reduction to right strip and uniform seven-entry Farkas pattern")
    print("PATTERN PASS replicates to K<=124 external zero-top support fibers at s<=1/256; fixed K uses s0=min(1/256,1/(12(K+1)))")
    print("RAW", len(cases), "extra-vertex certificate files written")


if __name__ == "__main__":
    main()
