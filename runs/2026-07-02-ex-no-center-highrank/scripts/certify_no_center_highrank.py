#!/usr/bin/env python3
"""Exact L3 numerics for the high-rank no-center path family.

This reuses the construction from docs/ingest/experiments/out/w40_ndg:
foreign unit rows, signed adjacent edge rows, a constrained left inverse B with
BL=I, and P=LB.  All certified quantities are SymPy rationals/integers.
"""
from __future__ import annotations

import csv
import itertools
import math
from decimal import Decimal, getcontext
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "no_center_highrank.csv"
A0 = sp.Rational(1, 100)


def pos(x):
    return x if x > 0 else sp.Integer(0)


def neg(x):
    return -x if x < 0 else sp.Integer(0)


def qstr(x):
    return str(sp.factor(x))


def decstr(x, places=12):
    q = sp.Rational(x)
    getcontext().prec = places + 8
    d = Decimal(int(q.p)) / Decimal(int(q.q))
    return format(d.quantize(Decimal(1).scaleb(-places)), "f")


def signed_start(k):
    return k - 1


def signed_info(k, idx):
    off = idx - signed_start(k)
    edge = off // 2 + 1
    eps = sp.Integer(1) if off % 2 == 0 else sp.Integer(-1)
    return eps, edge, edge + 1


def no_center_path(k, a=A0):
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
    B = sp.zeros(k, n)
    val = sp.Rational(1, 2 * (k - 2))
    for j in range(signed_start(k), n):
        B[0, j] = val
    for r in range(1, k):
        B[r, r - 1] = 1
    return L, B


def row_neg(row):
    return sp.factor(sum(neg(x) for x in list(row)))


def delta_of(P):
    return max(row_neg(P.row(i)) for i in range(P.rows))


def checks(L, B):
    P = sp.simplify(L * B)
    n = P.rows
    return P, {
        "BL": sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols),
        "P2": sp.simplify(P * P - P) == sp.zeros(n, n),
        "rowsum": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(n)),
    }


def theta_bases_reduced(k):
    units = tuple(range(k - 1))
    return [units + (j,) for j in range(signed_start(k), 3 * k - 5)]


def det_abs_no_center(k, basis, a=A0):
    signed = [idx for idx in basis if idx >= signed_start(k)]
    if not signed:
        return sp.Integer(0)
    q = len(signed) - 1
    if q == 0:
        return sp.Integer(1)
    selected_units = {idx + 1 for idx in basis if idx < signed_start(k)}
    omitted = [c for c in range(1, k) if c not in selected_units]
    eps0, u0, v0 = signed_info(k, signed[0])
    rows = []
    for idx in signed[1:]:
        eps, u, v = signed_info(k, idx)
        row = []
        for c in omitted:
            val = eps * ((1 if c == u else 0) - (1 if c == v else 0))
            val -= eps0 * ((1 if c == u0 else 0) - (1 if c == v0 else 0))
            row.append(sp.Integer(val))
        rows.append(row)
    return abs(sp.Matrix(rows).det()) * a**q


def full_enumeration_certificate(k, a=A0):
    vols = {}
    total = math.comb(3 * k - 5, k)
    for basis in itertools.combinations(range(3 * k - 5), k):
        d = det_abs_no_center(k, basis, a)
        if d:
            vols.setdefault(d, []).append(basis)
    best = max(vols)
    theta = sorted(b for vol, bs in vols.items() if 2 * vol >= best for b in bs)
    reduced = sorted(theta_bases_reduced(k))
    if best != 1 or theta != reduced:
        raise SystemExit(f"theta reduction mismatch at k={k}")
    return total, sum(len(v) for v in vols.values()), len(theta), best


def coeff_row(k, a, basis_signed, row_idx):
    out = [sp.Integer(0)] * k
    if row_idx < signed_start(k):
        out[row_idx] = sp.Integer(1)
        return out
    eps, u, v = signed_info(k, row_idx)
    eps0, u0, v0 = signed_info(k, basis_signed)
    out[-1] = sp.Integer(1)
    for c in range(1, k):
        val = eps * a * ((1 if c == u else 0) - (1 if c == v else 0))
        val -= eps0 * a * ((1 if c == u0 else 0) - (1 if c == v0 else 0))
        out[c - 1] = sp.factor(val)
    return out


def beta_row(k, a, row_idx):
    n = 3 * k - 5
    out = [sp.Integer(0)] * n
    if row_idx < signed_start(k):
        out[row_idx] = sp.Integer(1)
        return out
    eps, u, v = signed_info(k, row_idx)
    out[u - 1] += eps * a
    out[v - 1] -= eps * a
    val = sp.Rational(1, 2 * (k - 2))
    for j in range(signed_start(k), n):
        out[j] += val
    return [sp.factor(x) for x in out]


def chart_metrics(k, a, basis):
    rows = [coeff_row(k, a, basis[-1], j) for j in range(3 * k - 5)]
    phi_by_s, sstar_by_s, def_ok = [], [], True
    for s, u in enumerate(basis):
        beta = beta_row(k, a, u)
        phi = sstar = defsum = sp.Integer(0)
        for j, Arow in enumerate(rows):
            lam = sp.factor(1 - Arow[s])
            mu = sp.factor(sum(neg(Arow[t]) for t in range(k) if t != s))
            sigma = sp.factor(sum(pos(Arow[t]) for t in range(k) if t != s))
            E = pos(mu - lam)
            bp = pos(beta[j])
            phi += bp * E
            sstar += bp * (sigma + 2 * neg(lam))
            defsum += beta[j] * lam
        def_ok = def_ok and sp.factor(defsum) == 0
        phi_by_s.append(sp.factor(phi))
        sstar_by_s.append(sp.factor(sstar))
    return {
        "basis": basis,
        "phi": max(phi_by_s),
        "phi_by_s": phi_by_s,
        "sstar_max": max(sstar_by_s),
        "sstar_by_s": sstar_by_s,
        "def_ok": def_ok,
    }


def certify_one(k, a=A0, certification="certified_reduction"):
    L, B = no_center_path(k, a)
    P, ck = checks(L, B)
    delta = delta_of(P)
    if delta != a or not all(ck.values()):
        raise SystemExit(f"failed instance checks at k={k}, a={a}: delta={delta}, checks={ck}")

    bases = theta_bases_reduced(k)
    charts = [chart_metrics(k, a, b) for b in bases]
    if not all(c["def_ok"] for c in charts):
        raise SystemExit(f"harmonic identity failure at k={k}, a={a}")
    charts.sort(key=lambda c: (sp.Rational(c["phi"]), c["basis"]))
    star = charts[0]
    ratio = sp.factor(star["phi"] / delta)
    expected = sp.factor(2 - sp.Rational(2, k - 2))
    if ratio != expected:
        raise SystemExit(f"pattern mismatch k={k}: got {ratio}, expected {expected}")
    return {
        "k": k,
        "family": f"no_center_path_a{qstr(a).replace('/', '_')}",
        "delta": delta,
        "ratio": ratio,
        "sstar_ratio": sp.factor(star["sstar_max"] / delta),
        "certification": certification,
        "charts_checked": len(bases),
        "star_basis": list(star["basis"]),
        "checks": ck,
    }


def main():
    rows = []
    full = {6: full_enumeration_certificate(6), 8: full_enumeration_certificate(8)}
    for k in [6, 8, 10, 12, 14, 16, 20, 30]:
        cert = "full_enumeration" if k in full else "certified_reduction"
        rec = certify_one(k, A0, cert)
        if k in full:
            total, actual, theta, best = full[k]
            note = f"full bases={total}; actual={actual}; theta={theta}; max_vol={best}; "
        else:
            note = "determinant reduction; theta class all unit rows plus one signed row; "
        note += f"star={rec['star_basis']}; Sstar/delta={qstr(rec['sstar_ratio'])}; checks={rec['checks']}"
        rows.append([rec["k"], rec["family"], qstr(rec["delta"]), qstr(rec["ratio"]),
                     decstr(rec["ratio"]), rec["certification"], rec["charts_checked"], note])

    for k, a in [(14, sp.Rational(1, 200)), (14, sp.Rational(1, 20)), (20, sp.Rational(1, 200))]:
        rec = certify_one(k, a, "certified_reduction")
        note = ("delta-scale variant; determinant reduction still applies; "
                f"star={rec['star_basis']}; Sstar/delta={qstr(rec['sstar_ratio'])}; checks={rec['checks']}")
        rows.append([rec["k"], rec["family"], qstr(rec["delta"]), qstr(rec["ratio"]),
                     decstr(rec["ratio"]), rec["certification"], rec["charts_checked"], note])

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["k", "family", "delta_exact", "phi_over_delta_exact",
                    "phi_over_delta_float", "certification", "charts_checked", "notes"])
        w.writerow(["# caveat", "all rows are L3 numerical evidence, not rigorous proof of (EX)",
                    "", "", "", "", "", "floats are decimal display only"])
        w.writerow(["# caveat", "repeated-shear notes were not present in copied repo files",
                    "", "", "", "", "", "only no-center delta-scale variants are included"])
        w.writerows(rows)

    for row in rows:
        print("k={k} family={fam} delta={d} Phi/delta={r} cert={cert} charts={charts}".format(
            k=row[0], fam=row[1], d=row[2], r=row[3], cert=row[5], charts=row[6]))
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
