#!/usr/bin/env python3
"""KILL TEST (L3 scratch, orchestrator arithmetic): on every certified instance,
at its certified theta-half Phi-argmin U and maximal pivot s, compute the
cross-pivot masses B_{r,s} and C_{r,s} for each transverse r and compare with
the pivot-s unified budget G_class^- + S_-^mu + SIGMA (FanRes = 0 on all these
instances per the wave records). Question: is B+C bounded by a small multiple
of the budget across capped certified argmins, or does it dwarf it somewhere?
"""
from fractions import Fraction as F
from itertools import combinations

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def solve3(A,b):
    n=len(b)
    for cols in combinations(range(n),3):
        M=[[A[t][c] for t in range(3)] for c in cols]
        d=det3(M)
        if d!=0:
            rhs=[b[c] for c in cols]; xs=[]
            for k in range(3):
                Mk=[r[:] for r in M]
                for i in range(3): Mk[i][k]=rhs[i]
                xs.append(det3(Mk)/d)
            for c in range(n):
                assert sum(xs[t]*A[t][c] for t in range(3))==b[c]
            return xs
    raise ValueError

def P_of(Lr,Br):
    L=[[F(x) for x in r] for r in Lr]; B=[[F(x) for x in r] for r in Br]
    assert matmul(B,L)==[[1,0,0],[0,1,0],[0,0,1]]
    P=matmul(L,B); assert matmul(P,P)==P and all(sum(r)==1 for r in P)
    return P

KNOWN = {}  # name -> (delta, budget_total)
RESULTS = []

def analyze(name, P, U, s):
    n=len(P); basis=[P[i] for i in U]
    co=lambda i: solve3(basis,P[i])
    delta=max(sum(max(-x,0) for x in r) for r in P)
    # budget at pivot s
    Gc=sum(max(-P[U[s]][u],0) for u in U)
    Bset=[i for i in range(n) if i not in U]
    Smu=sum(max(-P[U[s]][i],0)*sum(max(-co(i)[q],0) for q in range(3) if q!=s) for i in Bset)
    SIG=sum(P[U[s]][i]*sum(max(-x,0) for x in P[i]) for i in Bset if P[U[s]][i]>0)
    bud=Gc+Smu+SIG
    if name in KNOWN:
        kd, kb = KNOWN[name]
        assert delta == kd and bud == kb, f"{name}: known-value mismatch delta={delta} bud={bud}"
    print(f"{name}: delta={delta} capped={delta<=F(1,4)}  budget: G={Gc} Smu={Smu} SIGMA={SIG} total={bud}")
    for r in range(3):
        if r==s: continue
        Brs=sum(max(P[U[r]][i],0)*max(-co(i)[s],0) for i in range(n))
        Crs=sum(max(-P[U[r]][i],0)*max(co(i)[s],0) for i in range(n))
        tot=Brs+Crs
        ratio = "inf" if bud==0 and tot>0 else (str(tot/bud) + f" (~{float(tot/bud):.3f})" if bud>0 else "0/0")
        print(f"   r={r}: B_(r,s)={Brs}  C_(r,s)={Crs}  B+C={tot}  (B+C)/budget={ratio}")
        RESULTS.append((name, r, Brs, Crs, tot, bud))

KNOWN.update({
    "G5 h=1/10": (F(7,30), F(13,60)),
    "G5 h=1/100": (F(637,2550), F(172,1275)),
    "G9-(V)": (F(1,4), F(4427,16640)),
    "G9-(P)": (F(1,4), F(451,1440)),
    "G10-witness (UNCAPPED)": (F(49,60), F(4897,10000)),
    "G11-nearmiss": (F(1,4), F(71,200)),
})

# 1-2. G5 two-orphan family at h=1/10 and h=1/100 (certified argmin (0,1,2), s=2)
for h in (F(1,10), F(1,100)):
    p,e,q = F(1,2)+h, F(1,2)-h, 1-2*h
    L=[[1,0,0],[0,1,0],[0,0,1],[p,-e,q],[-e,p,q]]
    B=[[1-p/4-e*e/(4*p), e/2, -h*q/(2*p), F(1,4), -e/(4*p)],
       [e/2, 1-p/4-e*e/(4*p), -h*q/(2*p), -e/(4*p), F(1,4)],
       [-h/2, -h/2, p, F(1,4), F(1,4)]]
    analyze(f"G5 h={h}", P_of(L,B), (0,1,2), 2)

# 3. G9 (V) instance (certified argmin (0,1,2), s=2)
analyze("G9-(V)", P_of(
 [[1,0,0],[0,1,0],[0,0,1],[F(2,3),F(-1,10),F(13,30)]],
 [[F(8,13),F(3,52),F(-1,4),F(15,26)],
  [F(1,6),F(39,40),F(13,120),F(-1,4)],
  [F(-1,4),F(3,80),F(67,80),F(3,8)]]), (0,1,2), 2)

# 4. G9 (P) instance
analyze("G9-(P)", P_of(
 [[1,0,0],[0,1,0],[0,0,1],[F(3,5),F(-2,5),F(4,5)]],
 [[F(13,16),F(1,8),F(-1,4),F(5,16)],
  [F(3,20),F(9,10),F(1,5),F(-1,4)],
  [F(-1,4),F(1,6),F(2,3),F(5,12)]]), (0,1,2), 2)

# 5. G10 witness (UNCAPPED delta=49/60; certified argmin (0,1,2), s=2)
analyze("G10-witness (UNCAPPED)", P_of(
 [[1,0,0],[0,1,0],[0,0,1],[F(3,5),F(-2,5),F(4,5)],[F(-1,5),F(4,5),F(2,5)]],
 [[F(2,5),F(13,30),F(-23,30),F(59,60),F(-1,20)],
  [F(23,100),F(12,25),F(-3,50),F(-1,5),F(11,20)],
  [F(-3,20),F(-1,5),F(1,2),F(2,5),F(9,20)]]), (0,1,2), 2)

# 6. G11 near miss (capped, certified argmin (0,1,2), s=2)
analyze("G11-nearmiss", P_of(
 [[1,0,0],[0,1,0],[0,0,1],[F(3,5),F(-2,5),F(4,5)],[F(-1,5),F(4,5),F(2,5)]],
 [[F(169,200),F(7,100),F(-6,25),F(11,40),F(1,20)],
  [F(9,40),F(1,2),F(-1,20),F(-1,5),F(21,40)],
  [F(-1,4),0,F(1,2),F(1,2),F(1,4)]]), (0,1,2), 2)

assert len(RESULTS) == 12, len(RESULTS)
assert all(B == 0 for _,_,B,_,_,_ in RESULTS), "headline finding violated: some B_(r,s) != 0"
worst = max((tot/bud, n, r) for n, r, B, C, tot, bud in RESULTS)
print(f"\nINVARIANT PASS: 12 (instance, r) pairs; known delta/budget values reproduced;")
print(f"B_(r,s) = 0 everywhere; worst (B+C)/budget = {worst[0]} (~{float(worst[0]):.3f}) at {worst[1]} r={worst[2]}")
