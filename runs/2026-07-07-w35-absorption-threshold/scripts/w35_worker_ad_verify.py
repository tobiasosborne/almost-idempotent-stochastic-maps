#!/usr/bin/env python3
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
    assert W, "empty W in audited certificate"
    dists = [dist1_to_conv(P, W, i) for i in range(len(P))]
    hidden = [i for i in vertices if i not in W]
    return d, negs, vertices, tstars, W, dists, hidden


def audit(name, P, expected=None):
    n = len(P)
    assert matmul(P, P) == P
    assert all(sum(r) == 1 for r in P)
    d, negs, vertices, tstars, W, dists, hidden = visible_data(P)
    H = max(dists)
    print(f"\n== {name} ==")
    print(f"delta={q(d)} tau^2={q(d)} H={q(H)} H^2/delta={q(H*H/d) if d else 'inf'}")
    print(f"vertices={vertices} W={W} hidden={hidden}")
    print("dists=[" + ", ".join(q(x) for x in dists) + "]")
    print("tstars={" + ", ".join(f"{i}: {q(tstars[i])}" for i in vertices) + "}")
    for a in [F(4), F(1), F(1, 4)]:
        G = [j for j, x in enumerate(dists) if x * x > a * a * d]
        R = {v: sum(max(P[v][j], F(0)) for j in G) for v in hidden}
        label = "sigma_4" if a == 4 else f"R_{q(a)}"
        print(f"a={q(a)} G={G} {label}={{{', '.join(str(k)+': '+q(v) for k, v in R.items())}}}")
    print("matrix:")
    for i, row in enumerate(P):
        print(f"  r{i}: {qvec(row)}  nu={q(negs[i])}")
    if expected:
        assert d == expected.get("delta", d)
        assert W == expected.get("W", W)
        assert hidden == expected.get("hidden", hidden)
        assert H == expected.get("H", H)
    print("PASS")


TRUE_HIDDEN_W29 = [
    [F(199, 200), F(-41, 8000), F(1, 8000), F(1, 200), F(1, 200)],
    [F(-1, 200), F(7959, 8000), F(1, 8000), F(1, 200), F(1, 200)],
    [F(-1, 200), F(-41, 8000), F(8001, 8000), F(1, 200), F(1, 200)],
    [F(589, 1200), F(12277, 24000), F(-99, 8000), F(1, 200), F(1, 200)],
    [F(599, 1200), F(12077, 24000), F(-99, 8000), F(1, 200), F(1, 200)],
]

LOW_HALO_RANK5_S1403_1000 = [
    [F(6412627, 6400000), F(-96807, 32000000), F(-1403, 64000), F(4209, 16000000), F(-478423, 16000000), F(4209, 80000)],
    [F(4209, 8000000), F(39967731, 40000000), F(-1403, 240000), F(1403, 20000000), F(-478423, 60000000), F(1403, 100000)],
    [F(4209, 1280000), F(-32269, 6400000), F(36997, 38400), F(1403, 3200000), F(-478423, 9600000), F(1403, 16000)],
    [F(1403, 2560000), F(-32269, 38400000), F(-1403, 230400), F(19201403, 19200000), F(-478423, 57600000), F(1403, 96000)],
    [F(29463, 6400000), F(-225883, 32000000), F(-9821, 192000), F(9821, 16000000), F(44651039, 48000000), F(9821, 80000)],
    [F(-214783881, 6400000000), F(1646676421, 32000000000), F(71594627, 192000000), F(-71594627, 16000000000), F(24413767807, 48000000000), F(8405373, 80000000)],
]

ABSORBED_RANK5_S351_250 = [
    [F(1603159, 1600000), F(-24219, 8000000), F(-351, 16000), F(1053, 4000000), F(-119691, 4000000), F(1053, 20000)],
    [F(1053, 2000000), F(9991927, 10000000), F(-117, 20000), F(351, 5000000), F(-39897, 5000000), F(351, 25000)],
    [F(1053, 320000), F(-8073, 1600000), F(3083, 3200), F(351, 800000), F(-39897, 800000), F(351, 4000)],
    [F(351, 640000), F(-2691, 3200000), F(-39, 6400), F(1600117, 1600000), F(-13299, 1600000), F(117, 8000)],
    [F(7371, 1600000), F(-56511, 8000000), F(-819, 16000), F(2457, 4000000), F(3720721, 4000000), F(2457, 20000)],
    [F(-53691477, 1600000000), F(411634657, 8000000000), F(17897159, 48000000), F(-17897159, 4000000000), F(6102931219, 12000000000), F(2102841, 20000000)],
]

LP_HIGH_MASS_ABSORBED = [
    [F(-495, 3224), F(0), F(5, 124), F(92325, 99944), F(18465, 99944), F(469, 99944)],
    [F(749, 3224), F(0), F(25, 124), F(-18751, 99944), F(76205, 99944), F(-879, 99944)],
    [F(-99, 3224), F(0), F(125, 124), F(2345, 99944), F(469, 99944), F(-551, 99944)],
    [F(-1, 4), F(0), F(0), F(149, 124), F(5, 124), F(1, 124)],
    [F(31, 104), F(0), F(0), F(-25, 104), F(99, 104), F(-1, 104)],
    [F(0), F(0), F(5, 4), F(-25, 124), F(-5, 124), F(-1, 124)],
]


def main():
    audit("true-hidden W29 frontier (deep widths empty)", TRUE_HIDDEN_W29, {"delta": F(99, 8000), "W": [0, 1, 2], "hidden": [3, 4], "H": F(1, 40)})
    audit("low-halo rank5 scaled record s=1403/1000", LOW_HALO_RANK5_S1403_1000, {"delta": F(5588149, 96000000), "W": [0, 1, 2, 3, 4], "hidden": [5]})
    audit("rank5 scale s=351/250 absorbed comparison", ABSORBED_RANK5_S351_250, {"W": [0, 1, 2, 3, 4, 5], "hidden": [], "H": F(0)})
    audit("LP high-mass absorbed comparison", LP_HIGH_MASS_ABSORBED, {"delta": F(1, 4), "W": [3, 4, 5], "hidden": [], "H": F(0)})


if __name__ == "__main__":
    main()
