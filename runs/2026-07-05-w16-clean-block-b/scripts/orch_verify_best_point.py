# Orchestrator-independent verification of the wave-16 headline (best clean-block point):
# rebuilds P from L,B in data/certified_points.json; re-derives coordinates, volumes, theta-half
# census, argmin, maximal pivot, the clean Gamma-block, and B/delta with independent code.
import json, itertools, pathlib
from fractions import Fraction as F
here = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(here/'data/certified_points.json'))
best = max(d['certified_points'], key=lambda c: F(c['B_over_delta']))
L = [[F(x) for x in row] for row in best['L']]
Bl = [[F(x) for x in row] for row in best['B']]
n = len(L)
P = [[sum(L[i][t]*Bl[t][j] for t in range(3)) for j in range(n)] for i in range(n)]
assert all(sum(r) == 1 for r in P)
assert [[sum(P[i][k]*P[k][j] for k in range(n)) for j in range(n)] for i in range(n)] == P
delta = max(sum(max(-x,0) for x in r) for r in P)
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def coords(ch):
    M = [L[c] for c in ch]; MT = [[M[r][c] for r in range(3)] for c in range(3)]; dT = det3(MT)
    assert dT != 0
    out = []
    for i in range(n):
        a = []
        for t in range(3):
            Mt = [row[:] for row in MT]
            for rr in range(3): Mt[rr][t] = L[i][rr]
            a.append(det3(Mt)/dT)
        assert all(sum(a[t]*M[t][c] for t in range(3)) == L[i][c] for c in range(3))
        out.append(a)
    return out
def phis(ch, A):
    out = []
    for r in range(3):
        tot = F(0)
        for i in range(n):
            b = P[ch[r]][i]
            if b > 0:
                mu = sum(max(-A[i][t],0) for t in range(3) if t != r)
                tot += b*max(mu - (1 - A[i][r]), F(0))
        out.append(tot)
    return out
vols = {ch: abs(det3([L[c] for c in ch])) for ch in itertools.combinations(range(n),3)}
vmax = max(vols.values())
theta = [c for c,v in vols.items() if 2*v >= vmax]
res = {c: phis(c, coords(c)) for c in theta}
mbest = min(max(v) for v in res.values())
argmins = [c for c in theta if max(res[c]) == mbest]
# argmin may be a TIE (the wave-13 record has {(0,1,3),(0,2,4)}); search every tied argmin
found = None
for U in argmins:
    A = coords(U); PhiU = res[U]; s = PhiU.index(max(PhiU)); M0 = PhiU[s]
    for j in range(n):
        if j in U: continue
        c = A[j][s]
        if c == 0 or abs(c)*vols[U]/vmax < F(1,2): continue
        Vj = tuple(U[t] if t != s else j for t in range(3))
        try: Aj = coords(Vj)
        except AssertionError: continue
        PhiV = phis(Vj, Aj)
        Psi, Gam = PhiV[s], max(PhiV[t] for t in range(3) if t != s)
        if Psi < M0 <= Gam: found = (U, s, j, Psi, M0, Gam); break
    if found: break
assert found, "no clean block on any tied argmin"
U, s, j, Psi, M0, Gam = found
A = coords(U)
Brs = max(sum(max(P[U[r]][i],0)*max(-A[i][s],0) for i in range(n)) for r in range(3) if r != s)
assert Brs == F(best['B_mass']) and delta == F(best['delta']) and Brs/delta < 1
print("ORCH-INDEPENDENT-VERIFY: best clean-block point CONFIRMED (B/delta = %.12f < 1)" % float(Brs/delta))
