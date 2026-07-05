# Orchestrator-independent recomputation of the wave-15 Gamma-emptiness refuter.
# Input: ONLY the P matrix derived from the worker's L,B (re-multiplied here); everything re-derived.
import itertools
from fractions import Fraction as F

L = [[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)],
     [F(2,25),F(-3,50),F(49,50)],[F(1,25),F(197,200),F(-1,40)],[F(-1,100),F(51,100),F(1,2)]]
Bl = [[F(1),F(0),F(0),F(0),F(0),F(0)],
      [F(-1,50),F(203,400),F(1,80),F(0),F(1,2),F(0)],
      [F(-55319,1000000),F(7269,1000000),F(5599,20000),F(7,10),F(0),F(681,10000)]]
n = 6
P = [[sum(L[i][t]*Bl[t][j] for t in range(3)) for j in range(n)] for i in range(n)]
assert all(sum(row) == 1 for row in P)
P2 = [[sum(P[i][k]*P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
assert P2 == P
delta = max(sum(max(-x,0) for x in row) for row in P)
assert delta == F(55319,1000000) and delta <= F(1,4)

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def coords(chart):
    M = [L[c] for c in chart]
    d = det3(M)
    assert d != 0
    out = []
    for i in range(n):
        a = []
        for t in range(3):
            Mt = [r[:] for r in M]
            for rr in range(3): Mt[t] = Mt[t]  # placeholder
        # solve a·M = L[i] via Cramer on M^T
        MT = [[M[r][c] for r in range(3)] for c in range(3)]
        dT = det3(MT)
        for t in range(3):
            Mt = [row[:] for row in MT]
            for rr in range(3): Mt[rr][t] = L[i][rr]
            a.append(det3(Mt)/dT)
        assert all(sum(a[t]*M[t][c] for t in range(3)) == L[i][c] for c in range(3))
        out.append(a)
    return out

def phis(chart, A):
    out = []
    for r in range(3):
        tot = F(0)
        for i in range(n):
            beta = P[chart[r]][i]
            if beta > 0:
                mu = sum(max(-A[i][t],0) for t in range(3) if t != r)
                E = max(mu - (1 - A[i][r]), F(0))
                tot += beta*E
        out.append(tot)
    return out

vols = {}
for ch in itertools.combinations(range(n),3):
    M = [L[c] for c in ch]
    vols[ch] = abs(det3(M))
vmax = max(vols.values())
theta = [c for c,v in vols.items() if 2*v >= vmax]
res = {c: phis(c, coords(c)) for c in theta}
best = min(max(v) for v in res.values())
argmins = [c for c in theta if max(res[c]) == best]
assert argmins == [(0,2,4)], argmins
U = (0,2,4); A = coords(U)
PhiU = res[U]
M0 = PhiU[2]
assert M0 == F(219870541,7880000000) and max(PhiU) == M0   # s=2 maximal
# clean block at j=1: V_j replaces u_s = chart row index 2 (= actual row 4) by row 1
j = 1
c = A[j][2]
mU = vols[U]/vmax
assert abs(c)*mU >= F(1,2), (c, mU)
Vj = (0,2,1)
Aj = coords(Vj)
# Psi_j = Phi at pivot position of the NEW chart row (row j sits where u_s was)... compute all three
PhiV = phis(Vj, Aj)
# In V_j=(0,2,1): position 2 holds row 1 (the new pivot row) -> Psi_j = PhiV[2]; Gamma_j = max over the other positions
Psi, Gamma = PhiV[2], max(PhiV[0], PhiV[1])
assert Psi == F(1,200) and Gamma == F(7,250), (Psi, Gamma)
assert Psi < M0 <= Gamma
# B-lemma data at (r=1 position? transverse chart positions 0,1 hold rows 0,2)
Brs = sum(max(P[U[1]][i],0)*max(-A[i][2],0) for i in range(n))
print("delta =", delta, "| argmin:", U, "| M =", M0)
print("Psi =", Psi, "< M <= Gamma =", Gamma, "| margins:", M0-Psi, Gamma-M0)
print("B_{1,2} =", Brs, "| B/delta =", float(Brs/delta))
print("ORCH-INDEPENDENT-VERIFY: CLEAN CAPPED GAMMA-BLOCK CONFIRMED (conj-gamma-emptiness REFUTED)")
