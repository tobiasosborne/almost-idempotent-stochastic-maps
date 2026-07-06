#!/usr/bin/env python3
"""W29 self-contained exact verifier.

Stdlib only.  Verifies the printed frontier/failed-construction matrices with
Fraction arithmetic and exact LPs:
  * P^2=P, row sums, delta.
  * canonical row vertices, exposedness t*, W, H.
  * G_4, hidden tops, sigma_4.
  * hiddenness dual/gauge witness alpha=t* for hidden vertices.
"""
from fractions import Fraction as F


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
            f = T[r][enter]
            if f:
                T[r] = [a - f * bb for a, bb in zip(T[r], T[leave])]
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
            inn = add(-c[i])
            transforms.append(([(ip, F(1)), (inn, F(-1))], F(0)))
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
        val = base + sum(co * xnew[idx] for idx, co in terms)
        x.append(val)
    return {"status": "optimal", "fun": sum(c[i] * x[i] for i in range(nx)), "x": x}


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def neg_mass(row):
    return sum(max(-x, F(0)) for x in row)


def delta(P):
    negs = [neg_mass(r) for r in P]
    return max(negs), negs


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


def exposed_tstar(P, i, d):
    n = len(P)
    far = [k for k in range(n) if k != i and l1(P[k], P[i]) ** 2 >= 16 * d]
    if not far:
        return None
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
    res = linprog_exact(
        c, A_ub=A_ub, b_ub=b_ub, A_eq=[hrow(i)], b_eq=[F(0)],
        bounds=[(None, None)] * (n + 1) + [(None, F(1))]
    )
    assert res["status"] == "optimal"
    return -res["fun"]


def dist1_to_conv(P, W, i):
    n = len(P)
    m = len(W)
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
    tstars = {i: exposed_tstar(P, i, d) for i in vertices}
    W = []
    for i in vertices:
        t = tstars[i]
        if t is None or (t >= 0 and 16 * t * t >= d):
            W.append(i)
    dists = [dist1_to_conv(P, W, i) for i in range(len(P))]
    hidden = [i for i in vertices if i not in W]
    return d, negs, vertices, tstars, W, dists, hidden


def gauge(P, v, d):
    far = [j for j in range(len(P)) if j != v and l1(P[j], P[v]) ** 2 >= 16 * d]
    if not far:
        return None
    n = len(P)
    m = len(far)
    c = [F(0)] * m + [F(1)] * n
    A_eq, b_eq = [], []
    for coord in range(n):
        row = [F(0)] * (m + n)
        for r, j in enumerate(far):
            row[r] = P[j][coord]
        for i in range(n):
            row[m + i] = -(P[i][coord] - P[v][coord])
        A_eq.append(row)
        b_eq.append(P[v][coord])
    A_eq.append([F(1)] * m + [F(0)] * n)
    b_eq.append(F(1))
    res = linprog_exact(c, A_eq=A_eq, b_eq=b_eq, bounds=[(F(0), None)] * (m + n))
    assert res["status"] == "optimal"
    return far, res["x"][:m], res["x"][m:], res["fun"]


def delta1_ok(d):
    rhs = F(17) - 2 * d
    return rhs > 0 and rhs * rhs > F(288)


def audit(name, P, expected):
    n = len(P)
    assert matmul(P, P) == P
    assert all(sum(r) == 1 for r in P)
    d, negs, vertices, tstars, W, dists, hidden = visible_data(P)
    H = max(dists)
    tops = [i for i in hidden if dists[i] == H]
    G4 = [i for i in range(n) if dists[i] ** 2 > 16 * d]
    sig4 = {v: sum(max(P[v][j], F(0)) for j in G4) for v in tops}
    g = matvec(P, [F(1) if i in G4 else F(0) for i in range(n)])
    assert matvec(P, g) == g
    print(f"\n{name}")
    print(f"delta={q(d)} delta_window={delta1_ok(d)} tau^2={q(d)}")
    print(f"W={W} vertices={vertices} hidden={hidden} tops={tops}")
    print(f"H={q(H)} H^2/delta={q(H * H / d) if d else 'inf'}")
    print(f"dists={[q(x) for x in dists]} G4={G4} g={qvec(g)} sigma4={{{', '.join(str(k)+': '+q(v) for k,v in sig4.items())}}}")
    for i in vertices:
        print(f"vertex {i}: t*={q(tstars[i])}")
    for v in hidden:
        far, mu, beta, alpha = gauge(P, v, d)
        assert alpha == tstars[v]
        print(f"hidden witness {v}: alpha={q(alpha)} far={far} mu={[q(x) for x in mu]} beta={[q(x) for x in beta]}")
    for row, nu in zip(P, negs):
        print(f"  {qvec(row)}  nu={q(nu)}")
    assert W == expected["W"]
    assert hidden == expected["hidden"]
    assert H == expected["H"]
    assert G4 == expected["G4"]
    assert sig4 == expected["sig4"]
    print("PASS")


def main():
    cases = []
    cases.append((
        "failed high web: W25 labels collapse under canonical visibility",
        [
            [F(1), F(0), F(0)],
            [F(0), F(1), F(0)],
            [F(101, 100), F(-1, 100), F(0)],
        ],
        {"W": [1, 2], "hidden": [], "H": F(0), "G4": [], "sig4": {}},
    ))
    cases.append((
        "frontier A: random true-hidden delta-window record",
        [
            [F(1), F(0), F(0), F(0), F(0), F(0)],
            [F(0), F(1), F(0), F(0), F(0), F(0)],
            [F(0), F(0), F(1), F(0), F(0), F(0)],
            [F(0), F(0), F(0), F(1), F(0), F(0)],
            [F(0), F(103, 300), F(2, 3), F(-1, 100), F(0), F(0)],
            [F(0), F(3, 5), F(2, 5), F(0), F(0), F(0)],
        ],
        {"W": [0, 1, 2, 3], "hidden": [4], "H": F(1, 50), "G4": [], "sig4": {4: F(0)}},
    ))
    cases.append((
        "frontier B: calibrated duplicate-split slice, best delta-window record",
        [
            [F(199, 200), F(-41, 8000), F(1, 8000), F(1, 200), F(1, 200)],
            [F(-1, 200), F(7959, 8000), F(1, 8000), F(1, 200), F(1, 200)],
            [F(-1, 200), F(-41, 8000), F(8001, 8000), F(1, 200), F(1, 200)],
            [F(589, 1200), F(12277, 24000), F(-99, 8000), F(1, 200), F(1, 200)],
            [F(599, 1200), F(12077, 24000), F(-99, 8000), F(1, 200), F(1, 200)],
        ],
        {"W": [0, 1, 2], "hidden": [3, 4], "H": F(1, 40), "G4": [], "sig4": {3: F(0), 4: F(0)}},
    ))
    for name, P, expected in cases:
        audit(name, P, expected)


if __name__ == "__main__":
    main()
