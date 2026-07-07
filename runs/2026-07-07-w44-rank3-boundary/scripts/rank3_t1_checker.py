#!/usr/bin/env python3
"""Exact rational helpers for the W44 rank-3 T1 decider.

This is scratch-only code.  It imports no repo modules and writes no repo files.
"""
from fractions import Fraction as F
from itertools import combinations


def q(x):
    if x is None:
        return "inf"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qvec(v):
    return "[" + ", ".join(q(x) for x in v) + "]"


def simplex_standard(c, A, b, nvar):
    m = len(A)
    A = [row[:] for row in A]
    b = b[:]
    for i in range(m):
        if b[i] < 0:
            b[i] = -b[i]
            A[i] = [-v for v in A[i]]
    total = nvar + m
    T = []
    for i in range(m):
        row = A[i][:] + [F(0)] * m + [b[i]]
        row[nvar + i] = F(1)
        T.append(row)
    basis = [nvar + i for i in range(m)]

    def pivot(leave, enter):
        piv = T[leave][enter]
        T[leave] = [v / piv for v in T[leave]]
        for r in range(m):
            if r == leave:
                continue
            fac = T[r][enter]
            if fac:
                T[r] = [a - fac * bb for a, bb in zip(T[r], T[leave])]
        basis[leave] = enter

    def run(cost, phase1=False):
        while True:
            cB = [cost[basis[i]] for i in range(m)]
            enter = -1
            for j in range(total):
                if j in basis:
                    continue
                if not phase1 and j >= nvar:
                    continue
                rc = cost[j] - sum(cB[i] * T[i][j] for i in range(m))
                if rc < 0:
                    enter = j
                    break
            if enter < 0:
                return "optimal"
            leave = -1
            best = None
            for i in range(m):
                if T[i][enter] > 0:
                    ratio = T[i][-1] / T[i][enter]
                    if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                        best = ratio
                        leave = i
            if leave < 0:
                return "unbounded"
            pivot(leave, enter)

    phase1_cost = [F(0)] * total
    for j in range(nvar, total):
        phase1_cost[j] = F(1)
    run(phase1_cost, phase1=True)
    art_val = sum(T[i][-1] for i in range(m) if basis[i] >= nvar)
    if art_val > 0:
        return "infeasible", None, None
    for i in range(m):
        if basis[i] >= nvar:
            for j in range(nvar):
                if j not in basis and T[i][j] != 0:
                    pivot(i, j)
                    break
    cost = c[:] + [F(0)] * m
    status = run(cost, phase1=False)
    if status != "optimal":
        return status, None, None
    x = [F(0)] * nvar
    for i in range(m):
        if basis[i] < nvar:
            x[basis[i]] = T[i][-1]
    return "optimal", sum(c[j] * x[j] for j in range(nvar)), x


def linprog_exact(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    nx = len(c)
    c = [F(v) for v in c]
    A_ub = [] if A_ub is None else [[F(v) for v in r] for r in A_ub]
    b_ub = [] if b_ub is None else [F(v) for v in b_ub]
    A_eq = [] if A_eq is None else [[F(v) for v in r] for r in A_eq]
    b_eq = [] if b_eq is None else [F(v) for v in b_eq]
    bounds = [(F(0), None)] * nx if bounds is None else bounds

    new_c = []
    transforms = []
    extra = []

    def add(coef):
        new_c.append(coef)
        return len(new_c) - 1

    for i, (lb, ub) in enumerate(bounds):
        lb = None if lb is None else F(lb)
        ub = None if ub is None else F(ub)
        if lb is None and ub is None:
            ip = add(c[i])
            im = add(-c[i])
            transforms.append(([(ip, F(1)), (im, F(-1))], F(0)))
        elif lb is not None and ub is None:
            iy = add(c[i])
            transforms.append(([(iy, F(1))], lb))
        elif lb is None and ub is not None:
            iy = add(-c[i])
            transforms.append(([(iy, F(-1))], ub))
        else:
            iy = add(c[i])
            transforms.append(([(iy, F(1))], lb))
            extra.append((iy, ub - lb))

    def expand(row):
        d = {}
        const = F(0)
        for i, a in enumerate(row):
            if a == 0:
                continue
            terms, base = transforms[i]
            const += a * base
            for idx, co in terms:
                d[idx] = d.get(idx, F(0)) + a * co
        return d, const

    cons = []
    for r, rhs in zip(A_ub, b_ub):
        d, const = expand(r)
        cons.append((d, rhs - const, "<="))
    for r, rhs in zip(A_eq, b_eq):
        d, const = expand(r)
        cons.append((d, rhs - const, "="))
    for iy, cap in extra:
        cons.append(({iy: F(1)}, cap, "<="))

    nnew = len(new_c)
    nslack = sum(1 for _, _, s in cons if s == "<=")
    total = nnew + nslack
    A = []
    b = []
    sp = nnew
    for d, rhs, sense in cons:
        row = [F(0)] * total
        for idx, co in d.items():
            row[idx] = co
        if sense == "<=":
            row[sp] = F(1)
            sp += 1
        A.append(row)
        b.append(rhs)
    cost = new_c + [F(0)] * nslack
    if not A:
        if any(v < 0 for v in cost):
            return {"status": "unbounded", "fun": None, "x": None}
        xnew = [F(0)] * total
    else:
        status, _, xnew = simplex_standard(cost, A, b, total)
        if status != "optimal":
            return {"status": status, "fun": None, "x": None}
    x = []
    for terms, base in transforms:
        x.append(base + sum(co * xnew[idx] for idx, co in terms))
    return {"status": "optimal", "fun": sum(c[i] * x[i] for i in range(nx)), "x": x}


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def neg_mass(row):
    return sum(max(-x, F(0)) for x in row)


def delta(P):
    negs = [neg_mass(r) for r in P]
    return max(negs), negs


def rank_matrix(A):
    A = [row[:] for row in A if any(row)]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                fac = A[i][c]
                A[i] = [a - fac * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r


def is_row_vertex(P, i):
    n = len(P)
    others = [k for k in range(n) if k != i and l1(P[k], P[i]) > 0]
    if not others:
        return True
    m = len(others)
    nv = m + n
    c = [F(0)] * m + [F(1)] * n
    A_ub, b_ub = [], []
    for coord in range(n):
        rp = [F(0)] * nv
        rn = [F(0)] * nv
        for kk, k in enumerate(others):
            rp[kk] = P[k][coord]
            rn[kk] = -P[k][coord]
        rp[m + coord] = F(-1)
        rn[m + coord] = F(-1)
        A_ub += [rp, rn]
        b_ub += [P[i][coord], -P[i][coord]]
    res = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, A_eq=[[F(1)] * m + [F(0)] * n], b_eq=[F(1)])
    assert res["status"] == "optimal"
    return res["fun"] > 0


def exposed_primal(P, v, d, force_t=None):
    n = len(P)
    far = [k for k in range(n) if k != v and l1(P[k], P[v]) ** 2 >= 16 * d]
    if not far:
        return far, None, None
    nv = n + 2
    c = [F(0)] * (n + 1) + [F(-1)]
    A_ub, b_ub = [], []

    def hrow(k):
        row = [F(0)] * nv
        for j in range(n):
            row[j] = P[k][j]
        row[n] = F(1)
        return row

    for k in range(n):
        hk = hrow(k)
        A_ub.append(hk[:])
        b_ub.append(F(1))
        A_ub.append([-x for x in hk])
        b_ub.append(F(0))
    for k in far:
        hk = hrow(k)
        row = [-x for x in hk]
        row[-1] = F(1)
        A_ub.append(row)
        b_ub.append(F(0))
    A_eq = [hrow(v)]
    b_eq = [F(0)]
    if force_t is not None:
        row = [F(0)] * nv
        row[-1] = F(1)
        A_eq.append(row)
        b_eq.append(F(force_t))
    res = linprog_exact(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=[(None, None)] * (n + 1) + [(None, F(1))],
    )
    assert res["status"] == "optimal"
    return far, -res["fun"], res["x"]


def h_value(P, x, i):
    n = len(P)
    return sum(x[j] * P[i][j] for j in range(n)) + x[n]


def face_opt(P, v, d, tstar, coeff, sense="min"):
    n = len(P)
    far = [k for k in range(n) if k != v and l1(P[k], P[v]) ** 2 >= 16 * d]
    nv = n + 2
    c = coeff[:] if sense == "min" else [-z for z in coeff]
    A_ub, b_ub = [], []

    def hrow(k):
        row = [F(0)] * nv
        for j in range(n):
            row[j] = P[k][j]
        row[n] = F(1)
        return row

    for k in range(n):
        hk = hrow(k)
        A_ub.append(hk[:])
        b_ub.append(F(1))
        A_ub.append([-x for x in hk])
        b_ub.append(F(0))
    for k in far:
        hk = hrow(k)
        row = [-x for x in hk]
        row[-1] = F(1)
        A_ub.append(row)
        b_ub.append(F(0))
    A_eq = [hrow(v)]
    b_eq = [F(0)]
    row = [F(0)] * nv
    row[-1] = F(1)
    A_eq.append(row)
    b_eq.append(tstar)
    res = linprog_exact(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=[(None, None)] * (n + 1) + [(None, F(1))],
    )
    assert res["status"] == "optimal"
    return res["fun"] if sense == "min" else -res["fun"], res["x"]


def always_tight_sets(P, v, d, tstar):
    n = len(P)
    far = [k for k in range(n) if k != v and l1(P[k], P[v]) ** 2 >= 16 * d]
    T = []
    O = []
    far_ranges = {}
    upper_ranges = {}
    for k in far:
        coeff = P[k][:] + [F(1), F(0)]
        mn, _ = face_opt(P, v, d, tstar, coeff, "min")
        mx, _ = face_opt(P, v, d, tstar, coeff, "max")
        far_ranges[k] = (mn, mx)
        if mn == tstar and mx == tstar:
            T.append(k)
    for k in range(n):
        coeff = P[k][:] + [F(1), F(0)]
        mn, _ = face_opt(P, v, d, tstar, coeff, "min")
        mx, _ = face_opt(P, v, d, tstar, coeff, "max")
        upper_ranges[k] = (mn, mx)
        if mn == F(1) and mx == F(1):
            O.append(k)
    return far, T, O, far_ranges, upper_ranges


def hull_intersection(P, v, T, O, tstar):
    n = len(P)
    if not T or not O:
        return False, None
    nv = len(T) + len(O)
    c = [F(0)] * nv
    A_eq = []
    b_eq = []
    for coord in range(n):
        row = [F(0)] * nv
        for a, f in enumerate(T):
            row[a] = P[f][coord] - P[v][coord]
        for b, i in enumerate(O):
            row[len(T) + b] = -tstar * (P[i][coord] - P[v][coord])
        A_eq.append(row)
        b_eq.append(F(0))
    A_eq.append([F(1)] * len(T) + [F(0)] * len(O))
    b_eq.append(F(1))
    A_eq.append([F(0)] * len(T) + [F(1)] * len(O))
    b_eq.append(F(1))
    res = linprog_exact(c, A_eq=A_eq, b_eq=b_eq, bounds=[(F(0), None)] * nv)
    return res["status"] == "optimal", res


def dist1_to_conv(P, W, i):
    n = len(P)
    m = len(W)
    if not W:
        return None
    nv = m + n
    c = [F(0)] * m + [F(1)] * n
    A_ub, b_ub = [], []
    for coord in range(n):
        rp = [F(0)] * nv
        rn = [F(0)] * nv
        for kk, w in enumerate(W):
            rp[kk] = P[w][coord]
            rn[kk] = -P[w][coord]
        rp[m + coord] = F(-1)
        rn[m + coord] = F(-1)
        A_ub += [rp, rn]
        b_ub += [P[i][coord], -P[i][coord]]
    res = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, A_eq=[[F(1)] * m + [F(0)] * n], b_eq=[F(1)])
    assert res["status"] == "optimal"
    return res["fun"]


def visible_data(P):
    d, negs = delta(P)
    vertices = [i for i in range(len(P)) if is_row_vertex(P, i)]
    tstars = {}
    for i in vertices:
        far, t, _ = exposed_primal(P, i, d)
        tstars[i] = t
    W = []
    for i in vertices:
        t = tstars[i]
        if t is None or (t >= 0 and 16 * t * t >= d):
            W.append(i)
    dists = [dist1_to_conv(P, W, i) for i in range(len(P))]
    hidden = [i for i in vertices if i not in W]
    return d, negs, vertices, tstars, W, dists, hidden


def audit_t1(P, name, rows=None):
    print(f"\n== {name} ==")
    print(f"n={len(P)} rank={rank_matrix(P)} idempotent={matmul(P, P) == P} rowsum={all(sum(r)==1 for r in P)}")
    d, negs, vertices, tstars, W, dists, hidden = visible_data(P)
    H = max(dists) if W else None
    tops = [i for i in hidden if dists[i] == H]
    print(f"delta={q(d)} negs={[q(x) for x in negs]}")
    print(f"vertices={vertices} W={W} hidden={hidden} H={q(H)} tops={tops}")
    print(f"dists={[q(x) for x in dists]}")
    rows = hidden if rows is None else rows
    for v in rows:
        if v not in hidden:
            print(f"row {v}: not hidden, skipped")
            continue
        far, tstar, x = exposed_primal(P, v, d)
        print(f"row {v}: t*={q(tstar)} far={far} kappa^2=delta/16={q(d/16)}")
        if tstar is None or tstar <= 0:
            print("  t* not positive; W43 characterization not applicable")
            continue
        far, T, O, far_ranges, upper_ranges = always_tight_sets(P, v, d, tstar)
        ok, res = hull_intersection(P, v, T, O, tstar)
        print(f"  T={T} O={O} intersection={ok}")
        if ok:
            xh = res["x"]
            print(f"  weights_T={qvec(xh[:len(T)])} weights_O={qvec(xh[len(T):])}")
        else:
            print(f"  far_ranges={{ {', '.join(str(k)+':('+q(a)+','+q(b)+')' for k,(a,b) in far_ranges.items())} }}")
            print(f"  upper_ranges={{ {', '.join(str(k)+':('+q(a)+','+q(b)+')' for k,(a,b) in upper_ranges.items())} }}")


WEB = [
    [F(99, 100), F(-21, 2000), F(1, 2000), F(1, 100), F(1, 100)],
    [F(-1, 100), F(1979, 2000), F(1, 2000), F(1, 100), F(1, 100)],
    [F(-1, 100), F(-21, 2000), F(2001, 2000), F(1, 100), F(1, 100)],
    [F(289, 600), F(3137, 6000), F(-49, 2000), F(1, 100), F(1, 100)],
    [F(299, 600), F(3037, 6000), F(-49, 2000), F(1, 100), F(1, 100)],
]


def append_stationary(P0, r):
    return [row + [F(0)] for row in P0] + [r + [F(0)]]


def web_append(y, z, eps=F(1, 100), t=F(1, 100)):
    v = 3
    r = [WEB[v][k] + eps * (t * (WEB[z][k] - WEB[v][k]) - (WEB[y][k] - WEB[v][k])) for k in range(len(WEB))]
    return append_stationary(WEB, r)


def web_block_self(y=3, z=1, eps=F(1, 100), t=F(1, 1000)):
    n = len(WEB)
    rows = [[F(1)] + [F(0)] * n + [F(0)]]
    rows += [[F(0)] + row + [F(0)] for row in WEB]
    v = rows[0]
    yext = [F(0)] + WEB[y] + [F(0)]
    zext = [F(0)] + WEB[z] + [F(0)]
    rows.append([v[k] + eps * (t * (zext[k] - v[k]) - (yext[k] - v[k])) for k in range(n + 2)])
    return rows


def obs4(eps=F(1, 100), t=F(1, 100)):
    return [
        [F(1), F(0), F(0), F(0)],
        [F(1) + eps * (1 - t), F(0), t * eps, -eps],
        [F(0), F(0), F(1), F(0)],
        [F(0), F(0), F(0), F(1)],
    ]


if __name__ == "__main__":
    cases = [
        ("OBS4", obs4()),
        ("HEIGHT+A", web_append(1, 2)),
        ("TOP-preserving", web_append(4, 0)),
        ("SELF-heavy", web_block_self()),
    ]
    for name, P in cases:
        audit_t1(P, name)
