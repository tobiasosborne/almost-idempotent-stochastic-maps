#!/usr/bin/env python3
"""Audit the COMPOSITION / quantifier step.

Factorization (proved per-s, per-chart):  for all U, for all s:
        S*_s(U) <= 2 Phi_s(U) + 6 delta.                              (F)

(EX):   there exists U0 in theta-1/2 class with  max_s Phi_s(U0) <= C0 delta.   (EX)

argmin selection: U* := argmin_{U in class} [ max_s Phi_s(U) ].
   By (EX), max_s Phi_s(U*) <= max_s Phi_s(U0) <= C0 delta.            (A)

Want:   max_s S*_s(U*) <= (2 C0 + 6) delta.                            (GOAL)

Derivation:
   max_s S*_s(U*)
      = S*_{s0}(U*)             for some maximizing s0
      <= 2 Phi_{s0}(U*) + 6 delta          by (F) at U=U*, s=s0
      <= 2 (max_s Phi_s(U*)) + 6 delta     since Phi_{s0} <= max_s Phi_s
      <= 2 C0 delta + 6 delta              by (A)
      = (2 C0 + 6) delta.
   => C_sf = 2 C0 + 6.   NO quantifier slip: (F) is universal in s, so it applies to
   whichever s0 maximizes S*; then we relax Phi_{s0} up to max_s Phi_s. CLEAN.
"""
import sys, itertools, random
sys.path.insert(0,'.')
import sympy as sp
from fractions import Fraction as F
from falsify import (rstoch_idem, is_idem_rstoch, delta_of, coeff_matrix,
                     metrics_for_pivot, all_theta_half_charts)

print(__doc__)
print("=== Empirical check: does  max_s S*_s(U*) <= 2 max_s Phi_s(U*) + 6 delta  hold")
print("    where U* = argmin over charts of max_s Phi_s? (the SELECTED-chart contract) ===")

def rand_inst(rng, n, r, outside):
    L=sp.zeros(n,r)
    for i in range(n):
        if i<r:
            for k in range(r): L[i,k]=sp.Integer(1) if k==i else 0
        else:
            sp_=5 if outside else 3
            w=[sp.Rational(rng.randint(-sp_,sp_),rng.randint(1,4)) for _ in range(r-1)]
            w.append(1-sum(w))
            for k in range(r): L[i,k]=w[k]
    for _ in range(15):
        sub=tuple(sorted(rng.sample(range(n),r)))
        if L[list(sub),:].det()!=0:
            Binv=L[list(sub),:].inv(); B=sp.zeros(r,n)
            for c,row in enumerate(sub):
                for a in range(r): B[a,row]=Binv[a,c]
            return L,B
    return None,None

rng=random.Random(99)
viol=0; tested=0; worst_ratio=None
for it in range(500):
    outside = it%4!=0
    n=rng.choice([3,4,5]); r=rng.choice([2,3])
    if r>=n: continue
    L,B=rand_inst(rng,n,r,outside)
    if L is None: continue
    P=rstoch_idem(L,B)
    if not is_idem_rstoch(P): continue
    d=delta_of(P)
    if d==0: continue
    charts=all_theta_half_charts(L)
    # compute per-chart max_s Phi and max_s S*
    chart_data=[]
    for basis in charts:
        A=coeff_matrix(L,basis)
        phis=[]; sstars=[]
        for s in range(r):
            Phi,Sstar=metrics_for_pivot(P,A,basis,s)
            phis.append(F(str(Phi))); sstars.append(F(str(Sstar)))
        chart_data.append((max(phis),max(sstars),basis))
    # argmin chart by max_s Phi
    Ustar=min(chart_data,key=lambda t:t[0])
    maxPhi, maxSstar, basis = Ustar
    lhs=maxSstar; rhs=2*maxPhi+6*F(str(d))
    tested+=1
    if lhs>rhs:
        viol+=1
        print("  CONTRACT VIOLATION at argmin chart:",basis,"maxS*=",lhs,"2maxPhi+6d=",rhs,"d=",d)
    ratio=(lhs)/F(str(d))
    if worst_ratio is None or ratio>worst_ratio[0]:
        worst_ratio=(ratio,maxPhi/F(str(d)),basis,str(d))
print(f"\ntested {tested} nontrivial instances; CONTRACT violations = {viol}")
print(f"worst maxS*/delta = {worst_ratio[0]}  (maxPhi/delta there = {worst_ratio[1]})")
print("Note: contract = max_s S*_s(U*) <= 2 max_s Phi_s(U*) + 6 delta. This is what")
print("(F)+argmin give; it is WEAKER than per-s but is exactly C_sf=2C0+6 once (EX) caps maxPhi.")
