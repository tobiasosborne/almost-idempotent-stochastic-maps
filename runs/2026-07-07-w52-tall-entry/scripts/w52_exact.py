#!/usr/bin/env python3
"""W52/BH exact rational perturbation audit.

Self-contained Fraction arithmetic: rank-3 WEB(a) families, exact vertex-enumerated
LPs, whole-face T/O ranges, and FP1 gap/reach instrumentation.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations


def q(x):
    if x is None:
        return "None"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qv(v):
    return "[" + ", ".join(q(x) for x in v) + "]"


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def neg_mass(row):
    return sum(-x for x in row if x < 0)


def delta(P):
    negs = [neg_mass(r) for r in P]
    return max(negs), negs


def pos(x):
    return x if x > 0 else F(0)


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
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [a - fac * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r


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
        dct = {}
        const = F(0)
        for i, a in enumerate(row):
            if a == 0:
                continue
            terms, base = transforms[i]
            const += a * base
            for idx, co in terms:
                dct[idx] = dct.get(idx, F(0)) + a * co
        return dct, const

    cons = []
    for r, rhs in zip(A_ub, b_ub):
        dct, const = expand(r)
        cons.append((dct, rhs - const, "<="))
    for r, rhs in zip(A_eq, b_eq):
        dct, const = expand(r)
        cons.append((dct, rhs - const, "="))
    for iy, cap in extra:
        cons.append(({iy: F(1)}, cap, "<="))

    nnew = len(new_c)
    nslack = sum(1 for _, _, s in cons if s == "<=")
    total = nnew + nslack
    A = []
    b = []
    sp = nnew
    for dct, rhs, sense in cons:
        row = [F(0)] * total
        for idx, co in dct.items():
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


def solve_unique(rows, rhs, n):
    A = [list(row) + [val] for row, val in zip(rows, rhs)]
    r = 0
    pivots = []
    for c in range(n):
        piv = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                fac = A[i][c]
                A[i] = [a - fac * b for a, b in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == len(A):
            break
    for i in range(r, len(A)):
        if all(A[i][c] == 0 for c in range(n)) and A[i][-1] != 0:
            return None
    if len(pivots) != n:
        return None
    x = [F(0)] * n
    for row_idx, col in enumerate(pivots):
        x[col] = A[row_idx][-1]
    return x


def eq_rank(eqs, n):
    return rank_matrix([row[:] for row, _ in eqs])


def feasible_point(n, eqs, ineqs):
    need = n - eq_rank(eqs, n)
    if need < 0 or need > len(ineqs):
        return None
    erows = [r for r, _ in eqs]
    erhs = [b for _, b in eqs]
    for combo in combinations(range(len(ineqs)), need):
        x = solve_unique(erows + [ineqs[i][0] for i in combo], erhs + [ineqs[i][1] for i in combo], n)
        if x is None:
            continue
        if all(dot(row, x) == b for row, b in eqs) and all(dot(row, x) <= b for row, b in ineqs):
            return x
    return None


def optimize(n, eqs, ineqs, obj, maximize=True):
    need = n - eq_rank(eqs, n)
    if need < 0 or need > len(ineqs):
        raise RuntimeError(f"bad LP dimensions n={n} need={need} ineqs={len(ineqs)}")
    erows = [r for r, _ in eqs]
    erhs = [b for _, b in eqs]
    best_val = None
    best_x = None
    seen = set()
    for combo in combinations(range(len(ineqs)), need):
        x = solve_unique(erows + [ineqs[i][0] for i in combo], erhs + [ineqs[i][1] for i in combo], n)
        if x is None:
            continue
        key = tuple(x)
        if key in seen:
            continue
        seen.add(key)
        if not all(dot(row, x) == b for row, b in eqs):
            continue
        if not all(dot(row, x) <= b for row, b in ineqs):
            continue
        val = dot(obj, x)
        if best_val is None or (val > best_val if maximize else val < best_val):
            best_val = val
            best_x = x
    if best_x is None:
        raise RuntimeError("LP has no enumerated vertex")
    return best_val, best_x


def convex_membership(P, i, others):
    m = len(others)
    n = len(P)
    res = linprog_exact(
        [F(0)] * m,
        A_eq=[[P[k][c] for k in others] for c in range(n)] + [[F(1)] * m],
        b_eq=[P[i][c] for c in range(n)] + [F(1)],
        bounds=[(F(0), None)] * m,
    )
    return res["status"] == "optimal"


def row_vertices(P):
    out = []
    for i in range(len(P)):
        others = [k for k in range(len(P)) if k != i and P[k] != P[i]]
        if not others or not convex_membership(P, i, others):
            out.append(i)
    return out


def h_eqs(P, u, include_u=True):
    n = len(P)
    eqs = []
    for i in range(n):
        row = [P[i][j] for j in range(n)]
        row[i] -= F(1)
        eqs.append((row, F(0)))
    if include_u:
        row = [F(0)] * n
        row[u] = F(1)
        eqs.append((row, F(0)))
    return eqs


def far_set(P, u, d):
    return [k for k in range(len(P)) if k != u and l1(P[k], P[u]) ** 2 >= 16 * d]


def tstar(P, u, d):
    far = far_set(P, u, d)
    if not far:
        return None, far, None
    n = len(P)
    A_eq = [row + [F(0)] for row, _ in h_eqs(P, u)]
    b_eq = [rhs for _, rhs in h_eqs(P, u)]
    A_ub = []
    b_ub = []
    for i in range(n):
        row = [F(0)] * (n + 1)
        row[i] = F(1)
        A_ub.append(row)
        b_ub.append(F(1))
        row = [F(0)] * (n + 1)
        row[i] = F(-1)
        A_ub.append(row)
        b_ub.append(F(0))
    for f in far:
        row = [F(0)] * (n + 1)
        row[n] = F(1)
        row[f] = F(-1)
        A_ub.append(row)
        b_ub.append(F(0))
    row = [F(0)] * (n + 1)
    row[n] = F(-1)
    A_ub.append(row)
    b_ub.append(F(0))
    row = [F(0)] * (n + 1)
    row[n] = F(1)
    A_ub.append(row)
    b_ub.append(F(1))
    obj = [F(0)] * n + [F(-1)]
    res = linprog_exact(obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(None, None)] * (n + 1))
    assert res["status"] == "optimal"
    return -res["fun"], far, res["x"]


def face_ranges(P, u, d, ts):
    n = len(P)
    far = far_set(P, u, d)
    eqs = h_eqs(P, u)
    ineqs = []
    for i in range(n):
        row = [F(0)] * n
        row[i] = F(1)
        ineqs.append((row, F(1)))
        row = [F(0)] * n
        row[i] = F(-1)
        ineqs.append((row, F(0)))
    for f in far:
        row = [F(0)] * n
        row[f] = F(-1)
        ineqs.append((row, -ts))
    ranges = {}
    for k in range(n):
        obj = [F(0)] * n
        obj[k] = F(1)
        mn, _ = optimize(n, eqs, ineqs, obj, maximize=False)
        mx, _ = optimize(n, eqs, ineqs, obj, maximize=True)
        ranges[k] = (mn, mx)
    T = [f for f in far if ranges[f] == (ts, ts)]
    O = [k for k in range(n) if ranges[k] == (F(1), F(1))]
    return far, T, O, ranges


def hull_intersection(P, u, T, O, ts):
    if not T or not O:
        return False, None
    n = len(P)
    m = len(T) + len(O)
    eqs = []
    for c in range(n):
        row = []
        for f in T:
            row.append(P[f][c] - P[u][c])
        for o in O:
            row.append(-ts * (P[o][c] - P[u][c]))
        eqs.append((row, F(0)))
    eqs.append(([F(1)] * len(T) + [F(0)] * len(O), F(1)))
    eqs.append(([F(0)] * len(T) + [F(1)] * len(O), F(1)))
    ineqs = []
    for j in range(m):
        row = [F(0)] * m
        row[j] = F(-1)
        ineqs.append((row, F(0)))
    x = feasible_point(m, eqs, ineqs)
    return x is not None, x


def dist_to_conv_l1_dual(P, W, i):
    n = len(P)
    # variables phi_0..phi_{n-1}, eta; ||phi||_inf <= 1 and eta >= phi(p_w)
    eqs = []
    ineqs = []
    B = F(10)
    for j in range(n):
        row = [F(0)] * (n + 1)
        row[j] = F(1)
        ineqs.append((row, F(1)))
        row = [F(0)] * (n + 1)
        row[j] = F(-1)
        ineqs.append((row, F(1)))
    for w in W:
        ineqs.append((P[w][:] + [F(-1)], F(0)))
    row = [F(0)] * (n + 1)
    row[-1] = F(1)
    ineqs.append((row, B))
    row = [F(0)] * (n + 1)
    row[-1] = F(-1)
    ineqs.append((row, B))
    obj = P[i][:] + [F(-1)]
    A_ub = [r for r, _ in ineqs]
    b_ub = [b for _, b in ineqs]
    res = linprog_exact([-x for x in obj], A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * (n + 1))
    assert res["status"] == "optimal"
    return -res["fun"]


def support_functional(P, W, v):
    n = len(P)
    eqs = []
    ineqs = []
    B = F(10)
    for j in range(n):
        row = [F(0)] * (n + 1)
        row[j] = F(1)
        ineqs.append((row, F(1)))
        row = [F(0)] * (n + 1)
        row[j] = F(-1)
        ineqs.append((row, F(1)))
    for w in W:
        ineqs.append((P[w][:] + [F(-1)], F(0)))
    row = [F(0)] * (n + 1)
    row[-1] = F(1)
    ineqs.append((row, B))
    row = [F(0)] * (n + 1)
    row[-1] = F(-1)
    ineqs.append((row, B))
    obj = P[v][:] + [F(-1)]
    A_ub = [r for r, _ in ineqs]
    b_ub = [b for _, b in ineqs]
    res = linprog_exact([-x for x in obj], A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * (n + 1))
    assert res["status"] == "optimal"
    return res["x"][:n], res["x"][-1], -res["fun"]


def visible_data(P):
    d, negs = delta(P)
    verts = row_vertices(P)
    ts = {}
    for i in verts:
        val, _, _ = tstar(P, i, d)
        ts[i] = val
    W = []
    for i in verts:
        val = ts[i]
        if val is None or (val >= 0 and 16 * val * val >= d):
            W.append(i)
    dists = [dist_to_conv_l1_dual(P, W, i) for i in range(len(P))]
    hidden = [i for i in verts if i not in W]
    H = max(dists) if dists else F(0)
    tops = [i for i in hidden if dists[i] == H]
    return d, negs, verts, ts, W, dists, hidden, H, tops


def two_d_coords(P, u):
    n = len(P)
    qs = [[P[j][c] - P[u][c] for c in range(n)] for j in range(n)]
    b1 = None
    b2 = None
    for j in range(n):
        if any(qs[j]):
            b1 = qs[j]
            break
    assert b1 is not None
    for j in range(n):
        w = qs[j]
        indep = False
        for c1 in range(n):
            for c2 in range(c1 + 1, n):
                if b1[c1] * w[c2] - b1[c2] * w[c1] != 0:
                    indep = True
                    break
            if indep:
                break
        if indep:
            b2 = w
            break
    assert b2 is not None
    coords = []
    for j in range(n):
        sol = None
        for c1 in range(n):
            for c2 in range(c1 + 1, n):
                det = b1[c1] * b2[c2] - b1[c2] * b2[c1]
                if det != 0:
                    x = (qs[j][c1] * b2[c2] - qs[j][c2] * b2[c1]) / det
                    y = (b1[c1] * qs[j][c2] - b1[c2] * qs[j][c1]) / det
                    sol = (x, y)
                    break
            if sol is not None:
                break
        assert sol is not None
        x, y = sol
        assert all(x * b1[c] + y * b2[c] == qs[j][c] for c in range(n))
        coords.append(sol)
    return qs, coords, (b1, b2)


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def cone_extreme_rays(coords):
    pts = [(j, c) for j, c in enumerate(coords) if c != (F(0), F(0))]
    r1 = None
    r2 = None
    for j, c in pts:
        if all(cross(c, w) >= 0 for _, w in pts):
            r1 = (j, c)
        if all(cross(w, c) >= 0 for _, w in pts):
            r2 = (j, c)
    assert r1 is not None and r2 is not None
    c1 = r1[1]
    c2 = r2[1]
    gens1 = [j for j, c in pts if cross(c1, c) == 0 and c[0] * c1[0] + c[1] * c1[1] > 0]
    gens2 = [j for j, c in pts if cross(c, c2) == 0 and c[0] * c2[0] + c[1] * c2[1] > 0]
    return c1, c2, gens1, gens2


def chi_norm_l1_subspace(basis, coeff):
    b1, b2 = basis
    n = len(b1)
    # variables s,t,w_0..w_{n-1}; maximize coeff[0]s + coeff[1]t under ||s*b1+t*b2||_1 <= 1.
    def solve(sign):
        nv = 2 + n
        A_ub = []
        b_ub = []
        for c in range(n):
            row = [F(0)] * nv
            row[0] = b1[c]
            row[1] = b2[c]
            row[2 + c] = F(-1)
            A_ub.append(row)
            b_ub.append(F(0))
            row = [F(0)] * nv
            row[0] = -b1[c]
            row[1] = -b2[c]
            row[2 + c] = F(-1)
            A_ub.append(row)
            b_ub.append(F(0))
        row = [F(0)] * nv
        for c in range(n):
            row[2 + c] = F(1)
        A_ub.append(row)
        b_ub.append(F(1))
        obj = [sign * coeff[0], sign * coeff[1]] + [F(0)] * n
        res = linprog_exact([-x for x in obj], A_ub=A_ub, b_ub=b_ub, bounds=[(None, None), (None, None)] + [(F(0), None)] * n)
        assert res["status"] == "optimal"
        return -res["fun"]
    return max(solve(F(1)), solve(F(-1)))


def row_gap_reach(P, d, W, H, top, u):
    ts, far, _ = tstar(P, u, d)
    if ts is None or ts <= 0:
        return None
    far2, T, O, ranges = face_ranges(P, u, d, ts)
    assert far == far2
    intersects, weights = hull_intersection(P, u, T, O, ts)
    Z = [k for k in range(len(P)) if k != u and ranges[k] == (F(0), F(0)) and P[k] != P[u]]
    vec, eta, val = support_functional(P, W, top)
    assert val == H
    phi = [dot(vec, P[j]) - eta for j in range(len(P))]
    depth_profile = [(z, phi[z] - phi[u]) for z in Z]
    qs, coords, basis = two_d_coords(P, u)
    c1, c2, gens1, gens2 = cone_extreme_rays(coords)
    chi1 = [cross(c1, coords[j]) for j in range(len(P))]
    chi2 = [cross(coords[j], c2) for j in range(len(P))]
    assert all(x >= 0 for x in chi1)
    assert all(x >= 0 for x in chi2)
    if Z and all(chi1[z] == 0 for z in Z):
        tv = chi2
        tvname = "chi2"
        norm = chi_norm_l1_subspace(basis, (-c2[1], c2[0]))
    elif Z and all(chi2[z] == 0 for z in Z):
        tv = chi1
        tvname = "chi1"
        norm = chi_norm_l1_subspace(basis, (-c1[1], c1[0]))
    else:
        tv = chi2
        tvname = "chi2"
        norm = chi_norm_l1_subspace(basis, (-c2[1], c2[0]))
    if T and O:
        gap = ts * min(tv[i] for i in O) - max(tv[f] for f in T)
    else:
        gap = None
    reach = max([tv[z] for z in Z] or [F(0)])
    Amin = gap / reach if gap is not None and gap > 0 and reach > 0 else F(0)
    return {
        "u": u,
        "tstar": ts,
        "far": far,
        "T": T,
        "O": O,
        "Z": Z,
        "intersects": intersects,
        "gap": gap,
        "reach": reach,
        "norm": norm,
        "gap_hat": gap / norm if gap is not None else None,
        "reach_hat": reach / norm if norm else None,
        "Amin": Amin,
        "tv": tvname,
        "phi": phi,
        "depth_profile": depth_profile,
        "ranges": ranges,
        "weights": weights,
    }


def web(a):
    return [
        [1 - a, -a - 5 * a * a, 5 * a * a, a, a],
        [-a, 1 - a - 5 * a * a, 5 * a * a, a, a],
        [-a, -a - 5 * a * a, 1 + 5 * a * a, a, a],
        [F(1, 2) - F(11, 6) * a, F(1, 2) + F(7, 3) * a - 5 * a * a, -F(5, 2) * a + 5 * a * a, a, a],
        [F(1, 2) - F(1, 6) * a, F(1, 2) + F(2, 3) * a - 5 * a * a, -F(5, 2) * a + 5 * a * a, a, a],
    ]


def append_stationary(P0, r):
    return [row + [F(0)] for row in P0] + [r + [F(0)]]


def web_append_a(a, y, z, eps=F(1, 100), t=F(1, 100), v=3):
    P0 = web(a)
    r = [P0[v][k] + eps * (t * (P0[z][k] - P0[v][k]) - (P0[y][k] - P0[v][k])) for k in range(len(P0))]
    return append_stationary(P0, r)


def height_row(a=F(1, 100), eps=F(1, 100), t=F(1, 100)):
    return web_append_a(a, 1, 2, eps=eps, t=t)[-1]


def top_pres_row(a=F(1, 100), eps=F(1, 100), t=F(1, 100)):
    return web_append_a(a, 4, 0, eps=eps, t=t)[-1]


def height_to_top_interp(s):
    P0 = web(F(1, 100))
    h = height_row()
    tp = top_pres_row()
    r = [(1 - s) * h[k] + s * tp[k] for k in range(6)]
    # remove the appended zero column before append_stationary
    return append_stationary(P0, r[:5])


def clone_lift(P, clone_rows, weights=None):
    # Duplicate selected rows as zero-column append rows. This preserves idempotence because
    # every clone row is stationary against P, with zero mass to all new columns.
    out = [row[:] + [F(0)] * len(clone_rows) for row in P]
    for idx, r in enumerate(clone_rows):
        out.append(P[r][:] + [F(0)] * len(clone_rows))
    return out


def top_cluster(P, d, dists, hidden, top):
    near = [j for j in range(len(P)) if l1(P[j], P[top]) ** 2 < 16 * d]
    G4 = [j for j, dj in enumerate(dists) if dj * dj > 16 * d]
    C4 = [j for j in near if j in G4]
    pos_total = sum(pos(P[top][j]) for j in range(len(P)))
    mass = sum(pos(P[top][j]) for j in C4)
    shipping = sum(pos(P[top][j]) for j in range(len(P)) if j not in C4)
    hidden_C4 = [j for j in C4 if j in hidden]
    return {
        "near": near,
        "G4": G4,
        "C4": C4,
        "hidden_C4": hidden_C4,
        "mass": mass,
        "pos_total": pos_total,
        "frac": mass / pos_total if pos_total else None,
        "shipping": shipping,
    }


def analyze(P, name, rows=None):
    assert matmul(P, P) == P, name
    assert all(sum(r) == 1 for r in P), name
    d, negs, verts, ts, W, dists, hidden, H, tops = visible_data(P)
    clusters = {top: top_cluster(P, d, dists, hidden, top) for top in tops}
    reports = []
    if rows is None:
        rows = sorted(set(u for top in tops for u in clusters[top]["near"] if u in hidden and P[top][u] > 0))
    for top in tops:
        for u in rows:
            if u in hidden and P[top][u] > 0 and l1(P[u], P[top]) ** 2 < 16 * d:
                rr = row_gap_reach(P, d, W, H, top, u)
                if rr is not None:
                    reports.append((top, rr))
    return {
        "name": name,
        "P": P,
        "rank": rank_matrix(P),
        "delta": d,
        "negs": negs,
        "verts": verts,
        "tstars": ts,
        "W": W,
        "dists": dists,
        "hidden": hidden,
        "H": H,
        "H2_delta": H * H / d if d else None,
        "tops": tops,
        "clusters": clusters,
        "reports": reports,
        "tall": H * H > 16 * d if d else False,
        "delta_ok": d <= F(1, 4),
    }


def one_line(rec):
    return (
        f"{rec['name']} | delta={q(rec['delta'])} H={q(rec['H'])} "
        f"H2/d={q(rec['H2_delta'])} tall={rec['tall']} W={rec['W']} "
        f"hidden={rec['hidden']} tops={rec['tops']}"
    )


def print_matrix(P):
    print("[")
    for row in P:
        print("  " + qv(row) + ",")
    print("]")


def print_rec(rec):
    print("\n" + one_line(rec))
    print(f"  dists={qv(rec['dists'])}")
    for top in rec["tops"]:
        c = rec["clusters"][top]
        print(
            f"  top {top}: near={c['near']} G4={c['G4']} C4={c['C4']} "
            f"hidden_C4={c['hidden_C4']} mass={q(c['mass'])} frac={q(c['frac'])} shipping={q(c['shipping'])}"
        )
    for top, rr in rec["reports"]:
        tau_cmp_num = None
        if rr["reach_hat"] is not None:
            tau_cmp_num = rr["reach_hat"] * rr["reach_hat"] / (((F(1, 2) + rec["delta"]) ** 2) * rec["delta"])
        print(
            f"  top {top} u={rr['u']}: t*={q(rr['tstar'])} T={rr['T']} O={rr['O']} Z={rr['Z']} "
            f"intersects={rr['intersects']} gap_hat={q(rr['gap_hat'])} reach_hat={q(rr['reach_hat'])} "
            f"A_min={q(rr['Amin'])} reach_vs_base_sq={q(tau_cmp_num)}"
        )
        print("    depth phi(z)-phi(u)=" + str([(z, q(v)) for z, v in rr["depth_profile"]]))


def run_named_cases():
    cases = [
        ("W41 HEIGHT+A", web_append_a(F(1, 100), 1, 2, F(1, 100), F(1, 100))),
        ("W41 TOP-preserving", web_append_a(F(1, 100), 4, 0, F(1, 100), F(1, 100))),
        ("W29-scale HEIGHT append", web_append_a(F(1, 200), 1, 2, F(1, 100), F(1, 100))),
        ("W41 H->TOP interp s=1/2", height_to_top_interp(F(1, 2))),
    ]
    for name, P in cases:
        print_rec(analyze(P, name))


def family_records():
    fams = []
    for t in [F(1, 400), F(1, 200), F(1, 100), F(1, 50), F(1, 25), F(1, 10)]:
        fams.append(("HA_t", t, analyze(web_append_a(F(1, 100), 1, 2, F(1, 100), t), f"HA_t t={q(t)}")))
    for eps in [F(1, 400), F(1, 200), F(1, 100), F(1, 50), F(1, 25)]:
        fams.append(("HA_eps", eps, analyze(web_append_a(F(1, 100), 1, 2, eps, F(1, 100)), f"HA_eps eps={q(eps)}")))
    for a in [F(1, 200), F(1, 100), F(1, 50), F(1, 25), F(1, 10), F(1, 8), F(1, 7)]:
        fams.append(("HA_base_a", a, analyze(web_append_a(a, 1, 2, F(1, 100), F(1, 100)), f"HA_base a={q(a)}")))
    for s in [F(0), F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        fams.append(("H_to_TOP", s, analyze(height_to_top_interp(s), f"H_to_TOP s={q(s)}")))
    return fams


def scan_grid():
    vals_a = [F(1, 200), F(1, 100), F(1, 50), F(1, 25), F(1, 10), F(1, 8), F(1, 7)]
    vals_e = [F(1, 200), F(1, 100), F(1, 50), F(1, 25), F(1, 10)]
    vals_t = [F(1, 400), F(1, 100), F(1, 50), F(1, 25), F(1, 10), F(1, 2), F(1)]
    best_ratio = None
    best_c4 = None
    best_disjoint = None
    entered = []
    count = 0
    for a in vals_a:
        for eps in vals_e:
            for t in vals_t:
                for y, z in [(1, 2), (4, 0), (3, 1), (0, 2), (1, 0), (4, 2)]:
                    try:
                        rec = analyze(web_append_a(a, y, z, eps, t), f"grid a={q(a)} y={y} z={z} eps={q(eps)} t={q(t)}")
                    except Exception:
                        continue
                    count += 1
                    if rec["delta"] <= 0 or rec["delta"] > F(1, 4):
                        continue
                    if best_ratio is None or rec["H2_delta"] > best_ratio["H2_delta"]:
                        best_ratio = rec
                    c4_mass = max([c["mass"] for c in rec["clusters"].values()] or [F(0)])
                    if best_c4 is None or c4_mass > max([c["mass"] for c in best_c4["clusters"].values()] or [F(0)]):
                        best_c4 = rec
                    has_disjoint = any(not rr["intersects"] for _, rr in rec["reports"])
                    if has_disjoint and (best_disjoint is None or rec["H2_delta"] > best_disjoint["H2_delta"]):
                        best_disjoint = rec
                    if rec["tall"] and any(c["C4"] for c in rec["clusters"].values()):
                        entered.append(rec)
    return count, best_ratio, best_c4, best_disjoint, entered


def main():
    print("W52 exact audit")
    run_named_cases()
    print("\n## family trace")
    for _, _, rec in family_records():
        print_rec(rec)
    count, best_ratio, best_c4, best_disjoint, entered = scan_grid()
    print(f"\n## grid count={count} entered={len(entered)}")
    if best_ratio:
        print("\n## best ratio")
        print_rec(best_ratio)
    if best_c4:
        print("\n## best C4 mass")
        print_rec(best_c4)
    if best_disjoint:
        print("\n## best disjoint")
        print_rec(best_disjoint)
    if entered:
        print("\n## entered records")
        for rec in entered[:20]:
            print_rec(rec)


if __name__ == "__main__":
    main()
