#!/usr/bin/env python3
"""Independent exact verifier for w40 Part A.

This script recomputes the theta=1/2 chart class, the Phi-minimizer, and the
repaired pointwise inequality without importing any w39 repair code.
"""
from __future__ import annotations

import itertools
import json
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


def coeffs(L, basis):
    return sp.simplify(L * L[list(basis), :].inv())


def all_bases(L):
    by_vol = {}
    for basis in itertools.combinations(range(L.rows), L.cols):
        d = sp.factor(L[list(basis), :].det())
        if d == 0:
            continue
        by_vol.setdefault(abs(d), []).append(basis)
    best = max(by_vol)
    return best, by_vol


def theta_bases(L, theta=sp.Rational(1, 2)):
    best, by_vol = all_bases(L)
    bases = []
    for vol, bs in by_vol.items():
        if vol >= theta * best:
            bases.extend(bs)
    return best, sorted(bases)


def per_row(Arow, s):
    lam = sp.factor(1 - Arow[s])
    mu = sp.factor(sum(neg(Arow[t]) for t in range(len(Arow)) if t != s))
    sigma = sp.factor(sum(pos(Arow[t]) for t in range(len(Arow)) if t != s))
    E = pos(mu - lam)
    return lam, mu, sigma, E


def chart_metrics(P, L, basis):
    A = coeffs(L, basis)
    sf = []
    splus = []
    sstar = []
    V = []
    M = []
    defs = []
    p1_fail = []
    r_fail = []
    overshoot_pos = []
    vid_fail = []
    for s, u in enumerate(basis):
        SF = Splus = Sstar = VV = MM = Def = Dpos = Dneg = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.factor(P[u, j])
            bp = pos(beta)
            bn = neg(beta)
            lam, mu, sigma, E = per_row(list(A.row(j)), s)
            if sp.simplify(E - pos(sigma - 2 * lam)) != 0:
                r_fail.append([s, int(u), j, qstr(lam), qstr(mu), qstr(sigma), qstr(E)])
            if sp.simplify(E - pos(2 * mu - sigma)) != 0:
                r_fail.append(["R2", s, int(u), j, qstr(lam), qstr(mu), qstr(sigma), qstr(E)])
            bound = sp.factor(sigma + 2 * neg(lam))
            if sp.simplify(bound - E) < 0:
                p1_fail.append([s, int(u), j, qstr(lam), qstr(sigma), qstr(E), qstr(bound)])
            Def += beta * lam
            if bp:
                SF += bp * E
                Splus += bp * sigma
                Sstar += bp * bound
                VV += bp * neg(lam)
                MM += bp * mu
                Dpos += bp * pos(lam)
                if lam < 0:
                    overshoot_pos.append(
                        {
                            "s": s,
                            "u": int(u),
                            "j": j,
                            "beta": qstr(beta),
                            "lambda": qstr(lam),
                            "V_contribution": qstr(bp * neg(lam)),
                            "E": qstr(E),
                            "sigma": qstr(sigma),
                        }
                    )
            if bn:
                Dneg += bn * lam
        if sp.simplify(VV - (Dpos - Dneg)) != 0:
            vid_fail.append([s, int(u), qstr(VV), qstr(Dpos), qstr(Dneg)])
        sf.append(sp.factor(SF))
        splus.append(sp.factor(Splus))
        sstar.append(sp.factor(Sstar))
        V.append(sp.factor(VV))
        M.append(sp.factor(MM))
        defs.append(sp.factor(Def))
    return {
        "basis": list(basis),
        "A_box": qstr(max(abs(x) for x in list(A))),
        "phi": max(sf),
        "sf": sf,
        "splus": splus,
        "sstar": sstar,
        "V": V,
        "M": M,
        "def": defs,
        "R_ok": not r_fail,
        "P1_ok": not p1_fail,
        "VID_ok": not vid_fail,
        "r_fail": r_fail[:5],
        "p1_fail": p1_fail[:5],
        "vid_fail": vid_fail[:5],
        "overshoot_pos": overshoot_pos,
    }


def select_chart(P, L, bases=None):
    if bases is None:
        _, bases = theta_bases(L)
    charts = [chart_metrics(P, L, b) for b in bases]
    charts.sort(key=lambda r: (Fraction(r["phi"]), tuple(r["basis"])))
    return charts, bases


def transverse_pair(a):
    L = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, a, -a], [1, -a, a]])
    c = sp.factor(a / (1 + 4 * a * a))
    B = sp.Matrix(
        [
            [0, 0, 0, sp.Rational(1, 2), sp.Rational(1, 2)],
            [0, 1 - 2 * a * c, 2 * a * c, c, -c],
            [0, 2 * a * c, 1 - 2 * a * c, -c, c],
        ]
    )
    return L, B


def dense_pair_k7():
    m = 3
    k = 2 * m + 1
    a = sp.Rational(1, 4)
    sig = [0] + [1] * m + [-1] * m
    rows = []
    for i in range(k):
        row = [sp.Integer(0)] * k
        row[i] = 1
        rows.append(row)
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = 1
    for t in range(1, k):
        xp[t] = a * sig[t]
        xm[t] = -a * sig[t]
    rows += [xp, xm]
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    c = sp.Rational(3, 34)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sig[r] * sig[t] * c
        B[r, k] = sig[r] * sp.Rational(3, 17)
        B[r, k + 1] = -sig[r] * sp.Rational(3, 17)
    return L, B


def staircase(m, eps=None):
    k = 2 * m + 1
    sig = [0] + [1] * m + [-1] * m
    rows = []
    for i in range(k):
        row = [sp.Integer(0)] * k
        row[i] = 1
        rows.append(row)
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    if eps is None:
        xp[0] = xm[0] = 1
        for t in range(1, k):
            xp[t] = sp.Rational(sig[t], 2)
            xm[t] = -sp.Rational(sig[t], 2)
    else:
        h = 1 - eps
        d = eps / (2 * m)
        xp[0] = xm[0] = h
        for t in range(1, k):
            xp[t] = d + sp.Rational(sig[t], 2)
            xm[t] = d - sp.Rational(sig[t], 2)
    rows += [xp, xm]
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
    if eps is not None:
        B[0, 0] = eps
        for t in range(1, k):
            B[0, t] = -eps / (2 * m)
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sp.Rational(sig[r] * sig[t], 2 * m)
        B[r, k] = sp.Rational(sig[r], 2 * m)
        B[r, k + 1] = -sp.Rational(sig[r], 2 * m)
    return L, B


def no_center_path(k, a=sp.Rational(1, 100)):
    rows = []
    for i in range(1, k):
        row = [sp.Integer(0)] * k
        row[i] = 1
        rows.append(row)
    for u, v in zip(range(1, k - 1), range(2, k)):
        plus = [sp.Integer(0)] * k
        minus = [sp.Integer(0)] * k
        plus[0] = minus[0] = 1
        plus[u] = a
        plus[v] = -a
        minus[u] = -a
        minus[v] = a
        rows += [plus, minus]
    L = sp.Matrix(rows)
    n = L.rows
    Bsym = sp.Matrix(k, n, lambda i, j: sp.Symbol(f"b_{i}_{j}"))
    eqs = []
    BL = Bsym * L
    for i in range(k):
        for j in range(k):
            eqs.append(sp.Eq(BL[i, j], 1 if i == j else 0))
    signed_start = k - 1
    val = sp.Rational(1, 2 * (k - 2))
    for j in range(signed_start, n):
        eqs.append(sp.Eq(Bsym[0, j], val))
    sol = sp.solve(eqs, list(Bsym), dict=True)
    if not sol:
        raise RuntimeError(f"no_center_path k={k}: no B solution")
    sol = sol[0]
    B = Bsym.subs(sol).subs({x: 0 for x in Bsym if x not in sol})
    return L, sp.simplify(B)


def no_center_theta_bases(k):
    units = tuple(range(k - 1))
    signed = range(k - 1, (k - 1) + 2 * (k - 2))
    return [units + (j,) for j in signed]


def audit_case(name, L, B, forced_bases=None, forced_best=None):
    print(f"auditing {name}", flush=True)
    P = sp.simplify(L * B)
    delta = delta_of(P)
    if forced_bases is None:
        best, bases = theta_bases(L)
    else:
        best, bases = forced_best, forced_bases
    charts, _ = select_chart(P, L, bases)
    star = charts[0]
    whole_p1 = all(c["P1_ok"] for c in charts)
    whole_R = all(c["R_ok"] for c in charts)
    whole_VID = all(c["VID_ok"] for c in charts)
    ratio = lambda x: qstr(sp.Rational(x / delta)) if delta != 0 else "inf"
    return {
        "name": name,
        "n": L.rows,
        "k": L.cols,
        "delta": qstr(delta),
        "max_volume": qstr(best),
        "theta_class_size": len(bases),
        "star_basis": star["basis"],
        "R_ok_all_theta": whole_R,
        "P1_ok_all_theta": whole_p1,
        "DEF_zero_star": all(sp.simplify(x) == 0 for x in star["def"]),
        "VID_ok_all_theta": whole_VID,
        "Phi/delta": ratio(star["phi"]),
        "Sstar/delta": [ratio(x) for x in star["sstar"]],
        "Sstar_max/delta": ratio(max(star["sstar"])),
        "Splus/delta": [ratio(x) for x in star["splus"]],
        "V/delta": [ratio(x) for x in star["V"]],
        "V_max/delta": ratio(max(star["V"])),
        "M/delta": [ratio(x) for x in star["M"]],
        "overshoot_positive_count_star": len(star["overshoot_pos"]),
        "overshoot_positive_examples_star": star["overshoot_pos"][:6],
        "checks": {
            "BL": bool(sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)),
            "P2": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
            "rowsum": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
        },
    }


def main():
    cases = [
        ("transverse_pair_a1_4",) + transverse_pair(sp.Rational(1, 4)) + (None, None),
        ("dense_pair_k7",) + dense_pair_k7() + (None, None),
        ("staircase_m2",) + staircase(2) + (None, None),
        ("staircase_m3",) + staircase(3) + (None, None),
        ("perturbed_staircase_m5_eps1_1000",) + staircase(5, sp.Rational(1, 1000)) + (None, None),
        ("no_center_path_k6",) + no_center_path(6) + (no_center_theta_bases(6), sp.Integer(1)),
        ("no_center_path_k8",) + no_center_path(8) + (no_center_theta_bases(8), sp.Integer(1)),
    ]
    records = [audit_case(name, L, B, bases, best) for name, L, B, bases, best in cases]
    Path("part_a_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for r in records:
        lines.append(
            f"{r['name']}: delta={r['delta']} class={r['theta_class_size']} "
            f"star={r['star_basis']} Phi/d={r['Phi/delta']} "
            f"S*/d_max={r['Sstar_max/delta']} V/d_max={r['V_max/delta']} "
            f"P1_all={r['P1_ok_all_theta']} DEF_star={r['DEF_zero_star']} "
            f"VID_all={r['VID_ok_all_theta']} overshoot_pos_star={r['overshoot_positive_count_star']} "
            f"checks={r['checks']}"
        )
        for ex in r["overshoot_positive_examples_star"][:2]:
            lines.append(f"  overshoot_pos {ex}")
    Path("part_a_results.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
