#!/usr/bin/env python3
"""Exact rank-2 selected-chart checks for w40 Part B.

Rank-2 rows are represented by a scalar x with L_i=(1-x_i, x_i).
Given any two rows p,q used to define B by the LB/BL=I converse, P=L B is
row-stochastic and idempotent.  We then enumerate the theta=1/2 chart class.
"""
from __future__ import annotations

import itertools
import json
import random
from fractions import Fraction
from pathlib import Path

import sympy as sp


def pos(x):
    x = sp.factor(x)
    return x if x > 0 else sp.Integer(0)


def neg(x):
    x = sp.factor(x)
    return -x if x < 0 else sp.Integer(0)


def qstr(x):
    return str(sp.factor(x))


def row_neg(row):
    return sp.factor(sum(neg(x) for x in list(row)))


def delta_of(P):
    return max(row_neg(P.row(i)) for i in range(P.rows))


def L_from_x(xs):
    return sp.Matrix([[1 - x, x] for x in xs])


def B_from_dual_pair(xs, i, j):
    p = xs[i]
    q = xs[j]
    den = q - p
    if den == 0:
        raise ValueError("singular pair")
    B = sp.zeros(2, len(xs))
    # Row 0 has moments (sum=1, x-moment=0); row 1 has (sum=1, x-moment=1).
    B[0, i] = sp.factor(q / den)
    B[0, j] = sp.factor(-p / den)
    B[1, i] = sp.factor((q - 1) / den)
    B[1, j] = sp.factor((1 - p) / den)
    return B


def coeffs(xs, basis):
    p = xs[basis[0]]
    q = xs[basis[1]]
    den = q - p
    vals = []
    for x in xs:
        vals.append([sp.factor((q - x) / den), sp.factor((x - p) / den)])
    return vals


def all_theta_pairs(xs):
    R = max(xs) - min(xs)
    pairs = []
    for i, j in itertools.combinations(range(len(xs)), 2):
        vol = abs(xs[j] - xs[i])
        if vol >= sp.Rational(1, 2) * R and vol != 0:
            # Orient the basis by increasing x for stable lambda signs.
            if xs[i] <= xs[j]:
                pairs.append((i, j))
            else:
                pairs.append((j, i))
    return sorted(set(pairs)), sp.factor(R)


def chart(P, xs, basis):
    A = coeffs(xs, basis)
    R = max(xs) - min(xs)
    vol = abs(xs[basis[1]] - xs[basis[0]])
    threshold = sp.factor(R / (2 * vol))
    sf = []
    sstar = []
    V = []
    carrier = []
    for s, u in enumerate(basis):
        SF = SS = VV = sp.Integer(0)
        carr = []
        for j in range(len(xs)):
            beta = sp.factor(P[u, j])
            bp = pos(beta)
            lam = sp.factor(1 - A[j][s])
            other = A[j][1 - s]
            # In rank 2, lambda_s is exactly the one transverse coordinate.
            sigma = pos(other)
            E = 2 * neg(lam)
            g = sp.factor(sigma + 2 * neg(lam))
            if bp:
                term = sp.factor(bp * g)
                SF += bp * E
                SS += term
                VV += bp * neg(lam)
                if term > 0:
                    asj = A[j][s]
                    permitted = abs(asj) * vol >= sp.Rational(1, 2) * R
                    carr.append(
                        {
                            "j": j,
                            "x": qstr(xs[j]),
                            "beta": qstr(beta),
                            "lambda": qstr(lam),
                            "a_s": qstr(asj),
                            "term": qstr(term),
                            "swap_permitted": bool(permitted),
                        }
                    )
        sf.append(sp.factor(SF))
        sstar.append(sp.factor(SS))
        V.append(sp.factor(VV))
        carrier.append(carr)
    return {
        "basis": list(basis),
        "volume": qstr(vol),
        "threshold": qstr(threshold),
        "phi": max(sf),
        "sf": sf,
        "sstar": sstar,
        "V": V,
        "carrier": carrier,
    }


def audit_instance(name, xs, dual_pair):
    xs = [sp.Rational(x) for x in xs]
    L = L_from_x(xs)
    B = B_from_dual_pair(xs, *dual_pair)
    P = sp.simplify(L * B)
    pairs, R = all_theta_pairs(xs)
    charts = [chart(P, xs, b) for b in pairs]
    charts.sort(key=lambda c: (Fraction(c["phi"]), tuple(c["basis"])))
    delta = delta_of(P)
    phi_min = charts[0]["phi"]
    argmins = [c for c in charts if sp.simplify(c["phi"] - phi_min) == 0]
    max_sstar_argmin = max(max(c["sstar"]) for c in argmins)
    max_V_argmin = max(max(c["V"]) for c in argmins)
    overshoot_pos = 0
    ndg_term = sp.Integer(0)
    permitted_term = sp.Integer(0)
    for c in argmins:
        for carr in c["carrier"]:
            for item in carr:
                term = sp.Rational(item["term"])
                if sp.Rational(item["lambda"]) < 0:
                    overshoot_pos += 1
                if item["swap_permitted"]:
                    permitted_term += term
                else:
                    ndg_term += term
    checks = {
        "BL": bool(sp.simplify(B * L - sp.eye(2)) == sp.zeros(2, 2)),
        "P2": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
        "rowsum": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
    }
    ratio = lambda z: "inf" if delta == 0 and z != 0 else ("0" if delta == 0 else qstr(sp.Rational(z / delta)))
    return {
        "name": name,
        "xs": [qstr(x) for x in xs],
        "dual_pair": list(dual_pair),
        "range": qstr(R),
        "theta_class_size": len(pairs),
        "delta": qstr(delta),
        "phi_min": qstr(phi_min),
        "argmin_count": len(argmins),
        "max_Sstar_argmin": qstr(max_sstar_argmin),
        "max_Sstar_argmin/delta": ratio(max_sstar_argmin),
        "max_V_argmin": qstr(max_V_argmin),
        "max_V_argmin/delta": ratio(max_V_argmin),
        "overshoot_positive_carriers_argmin": overshoot_pos,
        "permitted_carrier_term_sum_argmins": qstr(permitted_term),
        "ndg_carrier_term_sum_argmins": qstr(ndg_term),
        "first_argmin": {
            "basis": charts[0]["basis"],
            "sf": [qstr(x) for x in charts[0]["sf"]],
            "sstar": [qstr(x) for x in charts[0]["sstar"]],
            "V": [qstr(x) for x in charts[0]["V"]],
            "carrier": charts[0]["carrier"],
        },
        "checks": checks,
    }


def random_instances():
    rng = random.Random(40613)
    vals = [
        sp.Rational(-1, 1),
        sp.Rational(-2, 3),
        sp.Rational(-1, 2),
        sp.Rational(-1, 3),
        sp.Rational(0, 1),
        sp.Rational(1, 5),
        sp.Rational(1, 3),
        sp.Rational(1, 2),
        sp.Rational(2, 3),
        sp.Rational(1, 1),
        sp.Rational(4, 3),
        sp.Rational(3, 2),
        sp.Rational(5, 3),
        sp.Rational(2, 1),
    ]
    out = []
    for n in range(12):
        xs = sorted(set([sp.Rational(0), sp.Rational(1)] + rng.sample(vals, 4)))
        i = xs.index(sp.Rational(0))
        j = xs.index(sp.Rational(1))
        if rng.random() < 0.4:
            pair = tuple(sorted(rng.sample(range(len(xs)), 2), key=lambda t: xs[t]))
        else:
            pair = (i, j)
        out.append((f"random_{n:02d}", xs, pair))
    return out


def main():
    exact_cases = [
        ("endpoint_symmetric_eps1_3", [sp.Rational(-1, 3), 0, sp.Rational(1, 2), 1, sp.Rational(4, 3)], (1, 3)),
        ("endpoint_wide", [-1, 0, sp.Rational(1, 4), 1, 2], (1, 3)),
        ("dual_on_extremes", [-1, 0, sp.Rational(1, 3), 1, 2], (0, 4)),
        ("near_degenerate_cluster", [0, sp.Rational(9, 20), sp.Rational(11, 20), 1, sp.Rational(3, 2)], (0, 3)),
        ("adversarial_many_near_other_pivot", [-sp.Rational(1, 10), 0, sp.Rational(3, 5), sp.Rational(4, 5), 1, sp.Rational(11, 10)], (1, 4)),
    ]
    cases = exact_cases + random_instances()
    records = [audit_instance(name, xs, pair) for name, xs, pair in cases]
    Path("rank2_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for r in records:
        lines.append(
            f"{r['name']}: delta={r['delta']} theta_pairs={r['theta_class_size']} "
            f"phi_min={r['phi_min']} argmins={r['argmin_count']} "
            f"maxS*/d={r['max_Sstar_argmin/delta']} maxV/d={r['max_V_argmin/delta']} "
            f"overshoot_pos={r['overshoot_positive_carriers_argmin']} checks={r['checks']}"
        )
    Path("rank2_results.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
