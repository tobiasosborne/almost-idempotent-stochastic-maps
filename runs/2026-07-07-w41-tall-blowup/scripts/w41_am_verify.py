#!/usr/bin/env python3
"""W41-AM exact verifier for the alpha-blowup/tall-cluster obstruction search.

Stdlib only.  All arithmetic is Fraction-exact.  The script verifies:
  * exact signed idempotence and row sums,
  * delta, row vertices, visible set W, hidden rows, heights,
  * exact hiddenness A_min LP: minimize sum alpha among optimal witnesses,
  * near/deep cluster mass S_4 at the conjectural a=4 scale.
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
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=[hrow(i)],
        b_eq=[F(0)],
        bounds=[(None, None)] * (n + 1) + [(None, F(1))],
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


def amin_witness(P, v, d, tstar):
    n = len(P)
    far = [j for j in range(n) if j != v and l1(P[j], P[v]) ** 2 >= 16 * d]
    m = len(far)
    nv = m + n + n
    c = [F(0)] * m + [F(1)] * n + [F(0)] * n
    A_eq, b_eq = [], []
    for coord in range(n):
        row = [F(0)] * nv
        for r, j in enumerate(far):
            row[r] = P[j][coord] - P[v][coord]
        for i in range(n):
            row[m + i] = P[i][coord] - P[v][coord]
            row[m + n + i] = -(P[i][coord] - P[v][coord])
        A_eq.append(row)
        b_eq.append(F(0))
    A_eq.append([F(1)] * m + [F(0)] * (2 * n))
    b_eq.append(F(1))
    A_eq.append([F(0)] * (m + n) + [F(1)] * n)
    b_eq.append(tstar)
    res = linprog_exact(c, A_eq=A_eq, b_eq=b_eq, bounds=[(F(0), None)] * nv)
    assert res["status"] == "optimal"
    return far, res["x"][:m], res["x"][m : m + n], res["x"][m + n :], res["fun"]


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


CASES = [
    {
        "name": "OBS4 baseline: alpha blow-up but thin row visible, height tiny",
        "v": 0,
        "P": [
            [F(1), F(0), F(0), F(0)],
            [F(10099, 10000), F(0), F(1, 10000), F(-1, 100)],
            [F(0), F(0), F(1), F(0)],
            [F(0), F(0), F(0), F(1)],
        ],
        "expect": {"d": F(1, 100), "W": [1, 2, 3], "hidden": [0], "tops": [0], "A": F(100), "Hv": F(1, 5050), "S4": F(0)},
    },
    {
        "name": "HEIGHT+A attempt: A_min=100 survives, but the new thin row becomes the top",
        "v": 3,
        "P": web_append(1, 2),
        "expect": {"d": F(9859, 400000), "W": [0, 1, 2], "hidden": [3, 4, 5], "tops": [5], "A": F(100), "Hv": F(1, 20), "S4": F(0)},
    },
    {
        "name": "TOP-preserving attempt: v stays top, but A_min collapses to zero",
        "v": 3,
        "P": web_append(4, 0),
        "expect": {"d": F(49, 2000), "W": [0, 1, 2], "hidden": [3, 4, 5], "tops": [3, 4], "A": F(0), "Hv": F(1, 20), "S4": F(0)},
    },
    {
        "name": "SELF-heavy block: P_vv=1 and A_min large, but the thin row is visible",
        "v": 0,
        "P": web_block_self(),
        "expect": {"d": F(49, 2000), "W": [1, 2, 3, 6], "hidden": [0, 4, 5], "tops": [4, 5], "A": F(25625, 256), "Hv": F(50, 100999), "S4": F(0)},
    },
]


def audit(case):
    name, P, v, exp = case["name"], case["P"], case["v"], case["expect"]
    assert matmul(P, P) == P
    assert all(sum(row) == 1 for row in P)
    d, negs, vertices, tstars, W, dists, hidden = visible_data(P)
    H = max(dists)
    tops = [i for i in hidden if dists[i] == H]
    far, lam, alpha, beta, Amin = amin_witness(P, v, d, tstars[v]) if v in hidden else ([], [], [], [], None)
    near_v = [j for j in range(len(P)) if l1(P[j], P[v]) ** 2 < 16 * d]
    deep4 = [j for j in range(len(P)) if dists[j] ** 2 > 16 * d]
    S4 = sum(max(P[v][j], F(0)) for j in near_v if j in deep4)
    Spos = sum(max(P[v][j], F(0)) for j in near_v if dists[j] > 0)
    raw_near = sum(max(P[v][j], F(0)) for j in near_v)

    print(f"\n{name}")
    print(f"v={v}")
    print("P = [")
    for row in P:
        print("  " + qvec(row) + ",")
    print("]")
    print(f"delta={q(d)} row_negs={[q(x) for x in negs]}")
    print(f"vertices={vertices} W={W} hidden={hidden} tops={tops}")
    print(f"dists={[q(x) for x in dists]}")
    print(f"H_global={q(H)} H_global^2/delta={q(H * H / d)}")
    print(f"H_v={q(dists[v])} H_v^2/delta={q(dists[v] * dists[v] / d)}")
    print("tstars={" + ", ".join(f"{i}: {q(tstars[i])}" for i in vertices) + "}")
    print(f"near_v={near_v} deep4={deep4} S4={q(S4)} S_positive_depth={q(Spos)} raw_near_positive={q(raw_near)}")
    if v in hidden:
        print(f"A_min(v)={q(Amin)} far={far}")
        print(f"lambda={qvec(lam)}")
        print(f"alpha={qvec(alpha)}")
        print(f"beta={qvec(beta)}")
    else:
        print("A_min(v)=not computed because v is not hidden")

    assert d == exp["d"]
    assert W == exp["W"]
    assert hidden == exp["hidden"]
    assert tops == exp["tops"]
    assert dists[v] == exp["Hv"]
    assert S4 == exp["S4"]
    if exp["A"] is not None:
        assert Amin == exp["A"]
    print("PASS")


def main():
    for case in CASES:
        audit(case)


if __name__ == "__main__":
    main()
