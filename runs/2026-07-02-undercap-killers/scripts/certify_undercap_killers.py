#!/usr/bin/env python3
"""Exact certificates for arm A wave 6 under-cap mechanism killers.

All arithmetic is SymPy Rational/integer arithmetic.  The script writes one CSV
and asserts the headline invariant: a certified under-cap theta-half Phi-argmin
with at least two active pivots Phi_s > delta/2.
"""
from __future__ import annotations

import csv
import itertools
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "undercap_killers.csv"
EPS = sp.Rational(1, 1000)
A0 = sp.Rational(1, 100)


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


def theta_bases_full(L):
    vols = []
    for basis in itertools.combinations(range(L.rows), L.cols):
        d = sp.factor(L[list(basis), :].det())
        if d != 0:
            vols.append((abs(d), basis))
    best = max(v for v, _ in vols)
    return best, sorted(b for v, b in vols if 2 * v >= best)


def per_row(Arow, s):
    lam = sp.factor(1 - Arow[s])
    mu = sp.factor(sum(neg(Arow[t]) for t in range(len(Arow)) if t != s))
    sigma = sp.factor(sum(pos(Arow[t]) for t in range(len(Arow)) if t != s))
    E = pos(mu - lam)
    return lam, mu, sigma, E


def chart_metrics(P, L, basis):
    A = coeffs(L, basis)
    phis = []
    sstars = []
    vvals = []
    max_e = sp.Integer(0)
    def_ok = True
    for s, u in enumerate(basis):
        phi = sstar = vval = defsum = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.factor(P[u, j])
            bp = pos(beta)
            lam, _mu, sigma, E = per_row(list(A.row(j)), s)
            max_e = max(max_e, E)
            defsum += beta * lam
            phi += bp * E
            sstar += bp * (sigma + 2 * neg(lam))
            vval += bp * neg(lam)
        def_ok = def_ok and sp.factor(defsum) == 0
        phis.append(sp.factor(phi))
        sstars.append(sp.factor(sstar))
        vvals.append(sp.factor(vval))
    return {
        "basis": basis,
        "phi": sp.factor(max(phis)),
        "sum_phi": sp.factor(sum(phis)),
        "phis": phis,
        "sstar": sp.factor(max(sstars)),
        "V": sp.factor(max(vvals)),
        "max_E": sp.factor(max_e),
        "def_ok": def_ok,
    }


def edge(f, u, v):
    row = [sp.Integer(0)] * f
    row[u] = 1
    row[v] = -1
    return tuple(row)


def signed_closure(base):
    out = []
    for w in base:
        w = tuple(sp.Integer(x) for x in w)
        out.append(w)
        out.append(tuple(-x for x in w))
    return tuple(out)


def star_group(f, center=0):
    return signed_closure(edge(f, center, v) for v in range(f) if v != center)


def complete_group(f):
    return signed_closure(edge(f, u, v) for u in range(f) for v in range(u + 1, f))


def neg_l1(w):
    return sp.factor(sum(neg(x) for x in w))


def neg_l1_diff(w, w0):
    return sp.factor(sum(neg(w[i] - w0[i]) for i in range(len(w))))


def max_shear_norm_sq(groups):
    return max(sp.factor(sum(x * x for x in w)) for group in groups for w in group)


def build_multiblock(groups, a=A0):
    anchors = len(groups)
    foreign = len(groups[0][0])
    rows = []
    for i in range(foreign):
        row = [sp.Integer(0)] * (anchors + foreign)
        row[anchors + i] = 1
        rows.append(row)
    for h, group in enumerate(groups):
        for w in group:
            row = [sp.Integer(0)] * (anchors + foreign)
            row[h] = 1
            for i, val in enumerate(w):
                row[anchors + i] = a * val
            rows.append(row)
    L = sp.Matrix(rows)
    B = sp.zeros(L.cols, L.rows)
    for i in range(foreign):
        B[anchors + i, i] = 1
    offset = foreign
    for h, group in enumerate(groups):
        mass = sp.Rational(1, len(group))
        for j in range(len(group)):
            B[h, offset + j] = mass
        offset += len(group)
    return L, B


def multiblock_reduced_basis(groups, a=A0):
    anchors = len(groups)
    foreign = len(groups[0][0])
    offsets = []
    off = foreign
    for group in groups:
        offsets.append(off)
        off += len(group)
    chosen = []
    per_anchor = []
    delta = a * max(neg_l1(w) for group in groups for w in group)
    for h, group in enumerate(groups):
        candidates = []
        for idx, w0 in enumerate(group):
            phi = sp.factor(a * sum(neg_l1_diff(w, w0) for w in group) / len(group))
            candidates.append((sp.factor(phi / delta), offsets[h] + idx))
        candidates.sort()
        per_anchor.append(candidates[0][0])
        chosen.append(candidates[0][1])
    return tuple(range(foreign)) + tuple(chosen), per_anchor


def add_multiblock_row(rows, family, params, groups):
    L, B = build_multiblock(groups)
    P = sp.simplify(L * B)
    delta = delta_of(P)
    basis, per_anchor = multiblock_reduced_basis(groups)
    metrics = chart_metrics(P, L, basis)
    active = sum(1 for x in metrics["phis"] if x > delta / 2)
    r2 = max_shear_norm_sq(groups)
    reduction = sp.factor(4 * r2 * A0 * A0)
    bl_ok = sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)
    rowsum_ok = all(sp.factor(sum(P.row(i)) - 1) == 0 for i in range(P.rows))
    assert bl_ok and rowsum_ok and delta <= sp.Rational(1, 4)
    assert reduction < sp.Rational(1, 4)
    assert metrics["def_ok"]
    rows.append(
        {
            "family": family,
            "params": params,
            "k": L.cols,
            "n_rows": L.rows,
            "delta_exact": qstr(delta),
            "under_cap": str(delta <= sp.Rational(1, 4)),
            "phi_over_delta_exact": qstr(metrics["phi"] / delta),
            "sum_phi_over_delta_exact": qstr(metrics["sum_phi"] / delta),
            "active_pivots_gt_delta_half": active,
            "max_E_over_delta_exact": qstr(metrics["max_E"] / delta),
            "V_over_delta_exact": qstr(metrics["V"] / delta),
            "certification": "certified_reduction",
            "charts_checked": sp.prod(len(group) for group in groups),
            "notes": (
                f"basis={list(basis)}; per_anchor_min={[qstr(x) for x in per_anchor]}; "
                f"Hadamard 4*R2*a^2={qstr(reduction)}<1/4; "
                f"BL={bl_ok}; P2_via_BL={bl_ok}; rowsum={rowsum_ok}; DEF={metrics['def_ok']}"
            ),
        }
    )


def optimal_stair_u(m, a):
    return sp.factor(m * a / (1 + 2 * a * (m - 1) + 4 * m * m * a * a))


def staircase(m, a, eps=EPS, u=None):
    if u is None:
        u = optimal_stair_u(m, a)
    k = 2 * m + 1
    sig = [0] + [1] * m + [-1] * m
    h = 1 - eps
    d = eps / (2 * m)
    rows = []
    for i in range(k):
        row = [sp.Integer(0)] * k
        row[i] = 1
        rows.append(row)
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = h
    for t in range(1, k):
        xp[t] = d + a * sig[t]
        xm[t] = d - a * sig[t]
    rows += [xp, xm]
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
    B[0, 0] = eps
    for t in range(1, k):
        B[0, t] = -d
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    c = 2 * a * u
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - c * sig[r] * sig[t]
        B[r, k] = u * sig[r]
        B[r, k + 1] = -u * sig[r]
    return L, sp.simplify(B), u


def add_staircase_row(rows, family, params, m, a, u=None):
    L, B, used_u = staircase(m, a, u=u)
    P = sp.simplify(L * B)
    delta = delta_of(P)
    _best, bases = theta_bases_full(L)
    charts = [chart_metrics(P, L, b) for b in bases]
    charts.sort(key=lambda c: (sp.Rational(c["phi"]), c["basis"]))
    metrics = charts[0]
    active = sum(1 for x in metrics["phis"] if x > delta / 2)
    bl_ok = sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)
    p2_ok = sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)
    rowsum_ok = all(sp.factor(sum(P.row(i)) - 1) == 0 for i in range(P.rows))
    assert bl_ok and p2_ok and rowsum_ok and metrics["def_ok"]
    rows.append(
        {
            "family": family,
            "params": f"{params}; m={m}; a={qstr(a)}; eps={qstr(EPS)}; u={qstr(used_u)}",
            "k": L.cols,
            "n_rows": L.rows,
            "delta_exact": qstr(delta),
            "under_cap": str(delta <= sp.Rational(1, 4)),
            "phi_over_delta_exact": qstr(metrics["phi"] / delta),
            "sum_phi_over_delta_exact": qstr(metrics["sum_phi"] / delta),
            "active_pivots_gt_delta_half": active,
            "max_E_over_delta_exact": qstr(metrics["max_E"] / delta),
            "V_over_delta_exact": qstr(metrics["V"] / delta),
            "certification": "full_enumeration",
            "charts_checked": len(bases),
            "notes": (
                f"basis={list(metrics['basis'])}; nonzero_phi="
                f"{[qstr(x / delta) for x in metrics['phis'] if x]}; "
                f"BL={bl_ok}; P2={p2_ok}; rowsum={rowsum_ok}; DEF={metrics['def_ok']}"
            ),
        }
    )


def main():
    rows = []
    add_multiblock_row(
        rows,
        "two_anchor_overlapping_stars",
        "a=1/100; foreign=5; centers=0,4",
        (star_group(5, 0), star_group(5, 4)),
    )
    for anchors in [3, 5]:
        add_multiblock_row(
            rows,
            "multi_anchor_repeated_star",
            f"a=1/100; foreign=5; anchors={anchors}; repeated center=0 star",
            tuple(star_group(5, 0) for _ in range(anchors)),
        )
    add_multiblock_row(
        rows,
        "two_anchor_complete_vs_star",
        "a=1/100; foreign=4; anchor0=complete; anchor1=star(center=0)",
        (complete_group(4), star_group(4, 0)),
    )
    add_multiblock_row(
        rows,
        "two_anchor_complete_vs_star",
        "a=1/100; foreign=8; anchor0=complete; anchor1=star(center=0)",
        (complete_group(8), star_group(8, 0)),
    )

    add_staircase_row(
        rows,
        "archived_staircase",
        "original B6 normalization, outside cap",
        5,
        sp.Rational(1, 2),
        u=sp.Rational(1, 10),
    )
    for a in [
        sp.Rational(1, 5),
        sp.Rational(1, 6),
        sp.Rational(1, 8),
        sp.Rational(1, 10),
        sp.Rational(1, 12),
        sp.Rational(1, 16),
        sp.Rational(1, 20),
    ]:
        add_staircase_row(rows, "balanced_staircase_m5", "balanced dual scale", 5, a)
    for m in [2, 3, 4, 5, 6, 8]:
        add_staircase_row(rows, "balanced_staircase_cap_scale", "a=1/(4m)", m, sp.Rational(1, 4 * m))

    active_hits = [
        r for r in rows
        if r["under_cap"] == "True" and int(r["active_pivots_gt_delta_half"]) >= 2
    ]
    assert active_hits, "expected at least one under-cap active-pivot witness"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "family",
        "params",
        "k",
        "n_rows",
        "delta_exact",
        "under_cap",
        "phi_over_delta_exact",
        "sum_phi_over_delta_exact",
        "active_pivots_gt_delta_half",
        "max_E_over_delta_exact",
        "V_over_delta_exact",
        "certification",
        "charts_checked",
        "notes",
    ]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(
            {
                "family": "# caveat",
                "params": "all rows are L3 numerical evidence, not rigorous proof of (EX)",
                "notes": "exact fields are rational strings; no float fields are certified evidence",
            }
        )
        writer.writerows(rows)

    print(f"wrote {OUT.relative_to(ROOT)}")
    for r in active_hits:
        print(
            "active witness: {family} {params} delta={delta_exact} "
            "Phi/d={phi_over_delta_exact} sumPhi/d={sum_phi_over_delta_exact} "
            "active={active_pivots_gt_delta_half}".format(**r)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
