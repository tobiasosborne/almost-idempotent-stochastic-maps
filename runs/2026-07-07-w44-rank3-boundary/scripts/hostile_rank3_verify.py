#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations


def q(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qv(v):
    return "[" + ", ".join(q(x) for x in v) + "]"


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, x):
    return [dot(row, x) for row in A]


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
    if need < 0:
        return None
    if need > len(ineqs):
        return None
    erows = [r for r, _ in eqs]
    erhs = [b for _, b in eqs]
    for combo in combinations(range(len(ineqs)), need):
        rows = erows + [ineqs[i][0] for i in combo]
        rhs = erhs + [ineqs[i][1] for i in combo]
        x = solve_unique(rows, rhs, n)
        if x is None:
            continue
        if all(dot(row, x) == b for row, b in eqs) and all(dot(row, x) <= b for row, b in ineqs):
            return x
    return None


def optimize(n, eqs, ineqs, obj, maximize=True):
    need = n - eq_rank(eqs, n)
    if need < 0 or need > len(ineqs):
        raise RuntimeError("bad LP dimensions")
    erows = [r for r, _ in eqs]
    erhs = [b for _, b in eqs]
    best_val = None
    best_x = None
    seen = set()
    for combo in combinations(range(len(ineqs)), need):
        rows = erows + [ineqs[i][0] for i in combo]
        rhs = erhs + [ineqs[i][1] for i in combo]
        x = solve_unique(rows, rhs, n)
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


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def neg_mass(row):
    return sum(-x for x in row if x < 0)


def delta(P):
    ns = [neg_mass(row) for row in P]
    return max(ns), ns


def convex_membership(P, i, others):
    m = len(others)
    n = len(P)
    eqs = []
    for c in range(n):
        eqs.append(([P[k][c] for k in others], P[i][c]))
    eqs.append(([F(1)] * m, F(1)))
    ineqs = []
    for j in range(m):
        row = [F(0)] * m
        row[j] = F(-1)
        ineqs.append((row, F(0)))
    return feasible_point(m, eqs, ineqs) is not None


def row_vertices(P):
    out = []
    for i in range(len(P)):
        others = [k for k in range(len(P)) if k != i]
        if not convex_membership(P, i, others):
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
    eqs = []
    for row, rhs in h_eqs(P, u):
        eqs.append((row + [F(0)], rhs))
    ineqs = []
    for i in range(n):
        row = [F(0)] * (n + 1)
        row[i] = F(1)
        ineqs.append((row, F(1)))
        row = [F(0)] * (n + 1)
        row[i] = F(-1)
        ineqs.append((row, F(0)))
    for f in far:
        row = [F(0)] * (n + 1)
        row[n] = F(1)
        row[f] = F(-1)
        ineqs.append((row, F(0)))
    row = [F(0)] * (n + 1)
    row[n] = F(-1)
    ineqs.append((row, F(0)))
    row = [F(0)] * (n + 1)
    row[n] = F(1)
    ineqs.append((row, F(1)))
    obj = [F(0)] * n + [F(1)]
    val, x = optimize(n + 1, eqs, ineqs, obj, maximize=True)
    return val, far, x


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
    H = max(dists)
    tops = [i for i in hidden if dists[i] == H]
    return d, negs, verts, ts, W, dists, hidden, H, tops


def dist_to_conv_l1_dual(P, W, i):
    n = len(P)
    # variables are phi_0..phi_{n-1}, eta; eta >= phi(p_w)
    B = F(10)
    eqs = []
    ineqs = []
    for j in range(n):
        row = [F(0)] * (n + 1)
        row[j] = F(1)
        ineqs.append((row, F(1)))
        row = [F(0)] * (n + 1)
        row[j] = F(-1)
        ineqs.append((row, F(1)))
    for w in W:
        row = P[w][:] + [F(-1)]
        ineqs.append((row, F(0)))
    row = [F(0)] * (n + 1)
    row[-1] = F(1)
    ineqs.append((row, B))
    row = [F(0)] * (n + 1)
    row[-1] = F(-1)
    ineqs.append((row, B))
    obj = P[i][:] + [F(-1)]
    val, _ = optimize(n + 1, eqs, ineqs, obj, maximize=True)
    return val


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


def displacement_identity(P, u, lhs, rhs_scale, rhs):
    n = len(P)
    left = [F(0)] * n
    right = [F(0)] * n
    for idx, wt in lhs:
        for c in range(n):
            left[c] += wt * (P[idx][c] - P[u][c])
    for idx, wt in rhs:
        for c in range(n):
            right[c] += rhs_scale * wt * (P[idx][c] - P[u][c])
    return left, right, [a - b for a, b in zip(left, right)]


def exact_case_summary(name, P, claimed_delta=None):
    d, negs, verts, ts, W, dists, hidden, H, tops = visible_data(P)
    print(f"\n== {name} ==")
    print(f"rank={rank_matrix(P)} idempotent={matmul(P, P) == P} row_sums={all(sum(r) == 1 for r in P)}")
    print(f"delta={q(d)} row_negs={[q(x) for x in negs]}")
    if claimed_delta is not None:
        print(f"claimed_delta_ok={d == claimed_delta}")
    print(f"vertices={verts} W={W} hidden={hidden} tops={tops}")
    print(f"dists={[q(x) for x in dists]}")
    print(f"H={q(H)} H^2/delta={q(H * H / d)}")
    print("tstars={" + ", ".join(f"{i}: {q(ts[i]) if ts[i] is not None else 'None'}" for i in verts) + "}")
    return d, negs, verts, ts, W, dists, hidden, H, tops


def audit_row(P, d, u):
    ts, far, _ = tstar(P, u, d)
    far2, T, O, ranges = face_ranges(P, u, d, ts)
    ok, weights = hull_intersection(P, u, T, O, ts)
    assert far == far2
    print(f"row {u}: t*={q(ts)} far={far} T={T} O={O} intersection={ok}")
    print("  face_ranges={" + ", ".join(f"{k}:({q(a)},{q(b)})" for k, (a, b) in ranges.items()) + "}")
    if ok:
        print(f"  hull_weights_T={qv(weights[:len(T)])} hull_weights_O={qv(weights[len(T):])}")
    return ts, T, O, ok, weights, ranges


W41_HEIGHT_A = [
    [F(99, 100), F(-21, 2000), F(1, 2000), F(1, 100), F(1, 100), F(0)],
    [F(-1, 100), F(1979, 2000), F(1, 2000), F(1, 100), F(1, 100), F(0)],
    [F(-1, 100), F(-21, 2000), F(2001, 2000), F(1, 100), F(1, 100), F(0)],
    [F(289, 600), F(3137, 6000), F(-49, 2000), F(1, 100), F(1, 100), F(0)],
    [F(299, 600), F(3037, 6000), F(-49, 2000), F(1, 100), F(1, 100), F(0)],
    [F(583841, 1200000), F(77717, 150000), F(-9859, 400000), F(1, 100), F(1, 100), F(0)],
]


W41_TOP_PRESERVING = [
    [F(99, 100), F(-21, 2000), F(1, 2000), F(1, 100), F(1, 100), F(0)],
    [F(-1, 100), F(1979, 2000), F(1, 2000), F(1, 100), F(1, 100), F(0)],
    [F(-1, 100), F(-21, 2000), F(2001, 2000), F(1, 100), F(1, 100), F(0)],
    [F(289, 600), F(3137, 6000), F(-49, 2000), F(1, 100), F(1, 100), F(0)],
    [F(299, 600), F(3037, 6000), F(-49, 2000), F(1, 100), F(1, 100), F(0)],
    [F(577861, 1200000), F(39221, 75000), F(-9799, 400000), F(1, 100), F(1, 100), F(0)],
]


W29_FRONTIER = [
    [F(199, 200), F(-41, 8000), F(1, 8000), F(1, 200), F(1, 200)],
    [F(-1, 200), F(7959, 8000), F(1, 8000), F(1, 200), F(1, 200)],
    [F(-1, 200), F(-41, 8000), F(8001, 8000), F(1, 200), F(1, 200)],
    [F(589, 1200), F(12277, 24000), F(-99, 8000), F(1, 200), F(1, 200)],
    [F(599, 1200), F(12077, 24000), F(-99, 8000), F(1, 200), F(1, 200)],
]


def positive_mass_near_hidden(P, d, top, hidden):
    return [
        u for u in hidden
        if P[top][u] > 0 and l1(P[u], P[top]) ** 2 < 16 * d
    ]


def main():
    d, _, _, _, W, dists, hidden, H, tops = exact_case_summary("W41 HEIGHT+A", W41_HEIGHT_A, F(9859, 400000))
    assert d == F(9859, 400000)
    assert W == [0, 1, 2] and hidden == [3, 4, 5] and tops == [5]
    assert H == F(10059, 200000)
    print(f"top 5 near positive hidden rows={positive_mass_near_hidden(W41_HEIGHT_A, d, 5, hidden)}")
    print(f"P_5,3={q(W41_HEIGHT_A[5][3])} P_5,4={q(W41_HEIGHT_A[5][4])}")
    print(f"G4={[i for i, dist in enumerate(dists) if dist * dist > 16 * d]}")
    print(f"H<4tau={H * H < 16 * d}")
    r3 = audit_row(W41_HEIGHT_A, d, 3)
    r4 = audit_row(W41_HEIGHT_A, d, 4)
    assert r3[0] == F(1, 100) and r3[1] == [1] and r3[2] == [2] and not r3[3]
    assert r4[0] == F(5339, 292059) and r4[1] == [0] and r4[2] == [2] and not r4[3]

    d, _, _, _, W, dists, hidden, H, tops = exact_case_summary("W41 TOP-preserving", W41_TOP_PRESERVING, F(49, 2000))
    assert d == F(49, 2000)
    assert W == [0, 1, 2] and hidden == [3, 4, 5] and tops == [3, 4]
    for top in tops:
        print(f"top {top} near positive hidden rows={positive_mass_near_hidden(W41_TOP_PRESERVING, d, top, hidden)}")
    rt3 = audit_row(W41_TOP_PRESERVING, d, 3)
    rt4 = audit_row(W41_TOP_PRESERVING, d, 4)
    assert rt3[0] == F(1, 41) and rt3[1] == [0, 1] and rt3[2] == [2] and rt3[3]
    assert rt4[0] == F(1, 41) and rt4[1] == [0, 1] and rt4[2] == [2] and rt4[3]
    left, right, residual = displacement_identity(
        W41_TOP_PRESERVING, 3, [(0, F(59, 123)), (1, F(64, 123))], F(1, 41), [(2, F(1))]
    )
    print(f"u=3 claimed identity residual={qv(residual)} weights_sum={q(F(59,123)+F(64,123))}")
    assert residual == [F(0)] * len(W41_TOP_PRESERVING)
    left, right, residual = displacement_identity(
        W41_TOP_PRESERVING, 4, [(0, F(61, 123)), (1, F(62, 123))], F(1, 41), [(2, F(1))]
    )
    print(f"u=4 claimed identity residual={qv(residual)} weights_sum={q(F(61,123)+F(62,123))}")
    assert residual == [F(0)] * len(W41_TOP_PRESERVING)

    d, _, _, _, W, dists, hidden, H, tops = exact_case_summary("W29 frontier B", W29_FRONTIER, F(99, 8000))
    assert d == F(99, 8000)
    assert W == [0, 1, 2] and hidden == [3, 4] and tops == [3, 4]
    print(f"G4={[i for i, dist in enumerate(dists) if dist * dist > 16 * d]}")
    for top in tops:
        print(f"top {top} near positive hidden rows={positive_mass_near_hidden(W29_FRONTIER, d, top, hidden)}")
    rf3 = audit_row(W29_FRONTIER, d, 3)
    rf4 = audit_row(W29_FRONTIER, d, 4)
    assert rf3[0] == F(1, 81) and rf3[3]
    assert rf4[0] == F(1, 81) and rf4[3]
    print("\nALL ASSERTIONS PASSED")


if __name__ == "__main__":
    main()
