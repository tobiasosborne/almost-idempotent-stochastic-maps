#!/usr/bin/env python3
"""W30 Worker U scratch audit: exact W-emptiness hunt.

This script writes nothing.  It imports the repo's exact Fraction LP checker
and exact idempotent generators, then audits:
  1. W25's 3x3 model under canonical W;
  2. the true-hidden rank-5 calibration;
  3. a symmetrized edge-hidden family;
  4. a bounded random Lambda-C search.

All verdict-critical LPs are exact rational LPs from exact_lp.py.
"""
from fractions import Fraction as F
import argparse
import random
import sys
from pathlib import Path

ROOT = Path("/home/tobias/Projects/almost-idempotent-stochastic-maps")
PIPE = ROOT / "runs" / "2026-07-02-web-regime-hunt" / "scripts"
sys.path.insert(0, str(PIPE))

from exact_lp import linprog_exact
from gen import build_from_LambdaC
from pipeline import delta, is_idempotent, l1, visible_set


def q(x):
    if x is None:
        return "inf"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def neg_mass(row):
    return sum(max(-x, F(0)) for x in row)


def audit_visible(P):
    ok, idem, rowsum = is_idempotent(P)
    assert ok, (idem, rowsum)
    d, nus = delta(P)
    assert d > 0
    assert d <= F(1, 4)
    W, info = visible_set(P, d)
    vertices = [i for i in range(len(P)) if info.get(i, {}).get("vertex")]
    hidden = [i for i in vertices if not info[i].get("exposed")]
    return d, nus, W, info, vertices, hidden


def print_audit(label, P, show_matrix=False):
    d, nus, W, info, vertices, hidden = audit_visible(P)
    print(f"\n[{label}] delta={q(d)} vertices={vertices} W={W} hidden={hidden}")
    for i in vertices:
        ts = info[i]["tstar"]
        score = None if ts is None else 16 * ts * ts / d
        far = [j for j in range(len(P)) if j != i and l1(P[j], P[i]) ** 2 >= 16 * d]
        print(f"  v{i}: t*={q(ts)} score16t2/d={q(score) if score is not None else 'inf'} far={far} nu={q(nus[i])}")
    if show_matrix:
        print("  matrix:")
        for row in P:
            print("    [" + ", ".join(q(x) for x in row) + "]")
    return {"delta": d, "W": W, "vertices": vertices, "hidden": hidden, "info": info}


def w25_model():
    return [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(101, 100), F(-1, 100), F(0)],
    ]


def known_hidden_family():
    p = F(1, 40)
    rho = F(1, 100)
    x = p / 3
    C = [
        [F(1, 2) - x, F(1, 2) + x + p, -p],
        [F(1, 2) + x, F(1, 2) - x + p, -p],
    ]
    R2 = [[rho, rho], [rho, rho], [rho, rho]]
    P, _, _ = build_from_LambdaC(C, R2)
    return P


def sym_edge_C(p):
    x = p / 3
    rows = []
    for c, (a, b) in [(2, (0, 1)), (0, (1, 2)), (1, (0, 2))]:
        r = [F(0), F(0), F(0)]
        r[a] = F(1, 2) - x
        r[b] = F(1, 2) + x + p
        r[c] = -p
        rows.append(r)
        r = [F(0), F(0), F(0)]
        r[a] = F(1, 2) + x
        r[b] = F(1, 2) - x + p
        r[c] = -p
        rows.append(r)
    return rows


def sym_edge_model(p, rho):
    C = sym_edge_C(p)
    R2 = [[rho for _ in C] for __ in range(3)]
    P, _, _ = build_from_LambdaC(C, R2)
    return P


def random_C(rng, m, k):
    denoms = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 40, 50, 100]
    C = []
    for _ in range(m):
        home = rng.randrange(k)
        row = [F(0)] * k
        budget_den = rng.choice([2, 3, 4, 6, 10, 20])
        budget = F(rng.randint(0, budget_den), budget_den)
        used = F(0)
        others = [j for j in range(k) if j != home]
        rng.shuffle(others)
        for j in others:
            if used >= budget:
                break
            den = rng.choice(denoms)
            raw = F(rng.randint(0, den), den)
            amt = raw * (budget - used)
            sign = rng.choice([F(1), F(-1), F(-1), F(-2)])
            row[j] += sign * amt
            used += abs(amt)
        row[home] = F(1) - sum(row)
        C.append(row)
    return C


def random_R2(rng, k, m):
    denoms = [20, 50, 100, 200]
    mode = rng.random()
    if mode < 0.20:
        return [[F(0)] * m for _ in range(k)]
    if mode < 0.55:
        rho = F(rng.choice([0, 1, 1, 2, 3, 5]), rng.choice([100, 200, 400]))
        return [[rho for _ in range(m)] for __ in range(k)]
    return [
        [F(rng.randint(-2, 6), rng.choice(denoms) * rng.choice([1, 2, 4])) for _ in range(m)]
        for __ in range(k)
    ]


def hiddenness_gauge_lp(P, v, d):
    far = [j for j in range(len(P)) if j != v and l1(P[j], P[v]) ** 2 >= 16 * d]
    if not far:
        return None
    n = len(P)
    m = len(far)
    nv = m + n
    c = [F(0)] * m + [F(1)] * n
    A_eq = []
    b_eq = []
    for coord in range(n):
        row = [F(0)] * nv
        for r, j in enumerate(far):
            row[r] = P[j][coord]
        for i in range(n):
            row[m + i] = -(P[i][coord] - P[v][coord])
        A_eq.append(row)
        b_eq.append(P[v][coord])
    A_eq.append([F(1)] * m + [F(0)] * n)
    b_eq.append(F(1))
    r = linprog_exact(c, A_eq=A_eq, b_eq=b_eq, bounds=[(F(0), None)] * nv)
    assert r["status"] == "optimal", r
    return r["fun"], far, r["x"][:m], r["x"][m:]


def random_search(samples, seed):
    rng = random.Random(seed)
    audited = 0
    hidden_records = 0
    best = None
    best_payload = None
    found = None
    for s in range(samples):
        k = rng.choice([2, 3, 3, 4, 4, 5])
        m = rng.choice([1, 2, 2, 3, 4, 5, 6])
        if k + m > 11:
            continue
        C = random_C(rng, m, k)
        R2 = random_R2(rng, k, m)
        try:
            P, _, _ = build_from_LambdaC(C, R2)
            ok, _, _ = is_idempotent(P)
            if not ok:
                continue
            d, _ = delta(P)
            if d == 0 or d > F(1, 4):
                continue
            W, info = visible_set(P, d)
        except Exception:
            continue
        vertices = [i for i in range(len(P)) if info.get(i, {}).get("vertex")]
        if not vertices:
            continue
        hidden = [i for i in vertices if not info[i].get("exposed")]
        audited += 1
        hidden_records += len(hidden)
        finite_scores = []
        infinite = 0
        for i in vertices:
            ts = info[i]["tstar"]
            if ts is None:
                infinite += 1
            else:
                finite_scores.append(16 * ts * ts / d)
        max_score = None if infinite else max(finite_scores)
        key = (len(W), max_score if max_score is not None else F(10**9), -len(hidden))
        if best is None or key < best:
            best = key
            best_payload = (P, d, W, info, vertices, hidden, s)
        if vertices and not W:
            found = (P, d, W, info, vertices, hidden, s)
            break
    return audited, hidden_records, best, best_payload, found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=2500)
    ap.add_argument("--seed", type=int, default=30031)
    args = ap.parse_args()

    print("[T0] exact canonical audits")
    print_audit("W25 canonical", w25_model(), show_matrix=True)
    rec = print_audit("known true-hidden rank-5", known_hidden_family(), show_matrix=True)
    P = known_hidden_family()
    d = rec["delta"]
    for v in rec["hidden"]:
        alpha, far, mu, beta = hiddenness_gauge_lp(P, v, d)
        print(f"  gauge v{v}: alpha={q(alpha)} far={far} mu=" + "{" + ", ".join(f"{j}:{q(w)}" for j, w in zip(far, mu) if w) + "}")

    print("\n[T0/T3] symmetrized edge-hidden family")
    for p in [F(1, 40), F(1, 20), F(1, 10), F(1, 6), F(1, 5), F(1, 4)]:
        for rho in [F(0), F(1, 200), F(1, 100), F(1, 50), F(1, 20)]:
            P = sym_edge_model(p, rho)
            d, _ = delta(P)
            if d == 0 or d > F(1, 4):
                continue
            W, info = visible_set(P, d)
            vertices = [i for i in range(len(P)) if info.get(i, {}).get("vertex")]
            hidden = [i for i in vertices if not info[i].get("exposed")]
            print(f"  p={q(p)} rho={q(rho)} delta={q(d)} |V|={len(vertices)} |W|={len(W)} hidden={len(hidden)} W={W}")

    print(f"\n[T3] bounded random Lambda-C search seed={args.seed} samples={args.samples}")
    audited, hidden_records, best, best_payload, found = random_search(args.samples, args.seed)
    print(f"  audited={audited} hidden_vertex_records={hidden_records} found_W_empty={found is not None}")
    if found is not None:
        P, d, W, info, vertices, hidden, s = found
        print(f"  FOUND at sample={s} delta={q(d)} vertices={vertices} W={W} hidden={hidden}")
        for row in P:
            print("    [" + ", ".join(q(x) for x in row) + "]")
    elif best_payload is not None:
        P, d, W, info, vertices, hidden, s = best_payload
        print(f"  best sample={s} key={best} delta={q(d)} vertices={vertices} W={W} hidden={hidden}")
        for i in vertices:
            ts = info[i]["tstar"]
            score = None if ts is None else 16 * ts * ts / d
            print(f"    v{i}: t*={q(ts)} score16t2/d={q(score) if score is not None else 'inf'} exposed={info[i].get('exposed')}")
        print("  best matrix:")
        for row in P:
            print("    [" + ", ".join(q(x) for x in row) + "]")


if __name__ == "__main__":
    main()
