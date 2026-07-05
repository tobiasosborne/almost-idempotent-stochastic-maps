# Orchestrator-independent recomputation of the DC2 zero-denominator refuter.
# Input: ONLY the P matrix from the certificate. Everything else re-derived here.
import json, itertools
from fractions import Fraction as F

d = json.load(open('runs/2026-07-05-nsc-zero-denominator-refuter/data/nsc_certificates.json'))
cert = next(c for c in d['certificates'] if c['name'] == 'direct-zero-den-refuter')
P = [[F(x) for x in row] for row in cert['P']]
n = len(P)

# 1. exact identities
assert all(sum(row) == 1 for row in P), "row sums"
P2 = [[sum(P[i][k]*P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
assert P2 == P, "P^2 = P"
delta = max(sum(max(-x, 0) for x in row) for row in P)
assert F(0) < delta <= F(1,4), f"delta cap: {delta}"
nu = [sum(max(-x, 0) for x in row) for row in P]

# 2. affine frame: rows in barycentric coords w.r.t. a reference row triple.
def coords_in(chart):
    # solve p_i = sum_t a_t p_{chart[t]} with sum_t a_t = 1, exactly (least: use 3 indep columns)
    rows = [P[c] for c in chart]
    out = []
    for i in range(n):
        # solve [rows^T | constraint] : find a with a.rows = P[i], sum a = 1
        # build 3x3 system from 2 independent column differences + the affine constraint
        for c1, c2 in itertools.combinations(range(n), 2):
            M = [[rows[t][c1] for t in range(3)], [rows[t][c2] for t in range(3)], [F(1)]*3]
            det = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
                   + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
            if det != 0:
                b = [P[i][c1], P[i][c2], F(1)]
                a = []
                for t in range(3):
                    Mt = [r[:] for r in M]
                    for rr in range(3): Mt[rr][t] = b[rr]
                    dt = (Mt[0][0]*(Mt[1][1]*Mt[2][2]-Mt[1][2]*Mt[2][1]) - Mt[0][1]*(Mt[1][0]*Mt[2][2]-Mt[1][2]*Mt[2][0])
                          + Mt[0][2]*(Mt[1][0]*Mt[2][1]-Mt[1][1]*Mt[2][0]))
                    a.append(dt/det)
                break
        # verify reconstruction on ALL columns (this catches rank issues)
        assert all(sum(a[t]*rows[t][j] for t in range(3)) == P[i][j] for j in range(n)), f"coords row {i}"
        out.append(a)
    return out

# find one valid basis chart to serve as frame
frame = None
for chart in itertools.combinations(range(n), 3):
    try:
        C = coords_in(chart); frame = chart; frameC = C; break
    except AssertionError:
        continue
assert frame is not None, "no basis triple found"

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

# 3. chart volumes (relative, frame-independent ratios) + theta-half set + Phi
vols = {}
for chart in itertools.combinations(range(n), 3):
    vols[chart] = abs(det3([frameC[c] for c in chart]))
vmax = max(vols.values())
theta_half = [c for c, v in vols.items() if v*2 >= vmax and v > 0]

def phis(chart):
    A = coords_in(chart)
    out = []
    for r in range(3):
        tot = F(0)
        for i in range(n):
            beta = P[chart[r]][i]
            if beta > 0:
                mu = sum(max(-A[i][t], 0) for t in range(3) if t != r)
                lam = 1 - A[i][r]
                E = max(mu - lam, F(0))
                tot += beta*E
        out.append(tot)
    return out, A

results = {c: phis(c)[0] for c in theta_half}
argmins = [c for c in theta_half if max(results[c]) == min(max(v) for v in results.values())]
assert argmins == [(0, 3, 4)], f"argmin set: {argmins}"
assert results[(0,3,4)] == [F(0)]*3, f"Phi at argmin: {results[(0,3,4)]}"

# 4. the refuting pair at U=(0,3,4), s=0, r=1
U = (0, 3, 4)
_, A = phis(U)
s, r = 0, 1
B_rs = sum(max(P[U[r]][i], 0)*max(-A[i][s], 0) for i in range(n))
carriers = [i for i in range(n) if P[U[r]][i] > 0 and A[i][s] < 0]
SUMc = sum(P[U[r]][i]*nu[i] for i in carriers)
print("delta =", delta)
print("theta-half charts:", len(theta_half), "| unique argmin:", argmins[0], "Phi:", results[(0,3,4)])
print("B_{1,0} =", B_rs, "| carriers:", carriers, "| carrier nu:", [nu[i] for i in carriers])
print("SUM_carriers =", SUMc)
assert B_rs == F(1, 4020000000) and B_rs > 0, "B value"
assert SUMc == 0, "zero denominator"
assert all(x >= 0 for x in P[carriers[0]]), "carrier row entrywise nonnegative"
print("ORCH-INDEPENDENT-VERIFY: REFUTATION CONFIRMED (broad conj-nsc: B > 0, SUM_carriers = 0)")
