#!/usr/bin/env python3
"""Hardest adversarial probe: maximize the number of POSITIVE-beta OVERSHOOT rows
(beta>0 AND lambda<0) and push lambda toward the box edge +3 / -1, hunting for any
S* > 2 Phi + 6 delta.  This targets exactly the failure mode of the w38 refutation
(overshoot at theta=1/2) but now against the FACTORIZATION (not the SF<=S* step).

Also explicitly drive lambda to the box extremes a_s=-2 (lambda=3) and a_s=2 (lambda=-1)
by choosing actual-row charts whose Cramer coords sit at the +/-2 edge.
"""
import sys, itertools, random
sys.path.insert(0,'.')
import sympy as sp
from fractions import Fraction as F
from falsify import (rstoch_idem, is_idem_rstoch, delta_of, coeff_matrix,
                     metrics_for_pivot, all_theta_half_charts)

def per_step_check(P,L):
    """Return min slack of (S*<=2Phi+6d) and worst max|a| over all theta-half charts/pivots,
    plus count of overshoot rows in the worst chart."""
    d=delta_of(P)
    if d==0: return None
    charts=all_theta_half_charts(L)
    worst=None
    for basis in charts:
        A=coeff_matrix(L,basis); r=A.cols
        maxa=max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))
        for s in range(r):
            u=basis[s]
            Phi=Splus=Vpos=sp.Integer(0); novr=0; lam_max=sp.Integer(-10); lam_min=sp.Integer(10)
            for j in range(P.cols):
                beta=sp.nsimplify(P[u,j]); bp=sp.Max(beta,0)
                a_s=A[j,s]; lam=1-a_s
                lam_max=sp.Max(lam_max,lam); lam_min=sp.Min(lam_min,lam)
                sigma=sum(sp.Max(A[j,t],0) for t in range(r) if t!=s)
                E=sp.Max(sigma-2*lam,0)
                Phi+=bp*E; Splus+=bp*sigma; Vpos+=bp*sp.Max(-lam,0)
                if bp>0 and lam<0: novr+=1
            Sstar=Splus+2*Vpos
            sl=sp.simplify(2*Phi+6*d-Sstar)
            slack=F(str(sl)) if sl.is_rational else F(str(sp.Rational(round(float(sl)*10**9),10**9)))
            if worst is None or slack<worst[0]:
                worst=(slack,basis,s,novr,str(maxa),str(lam_max),str(lam_min),str(d),str(Phi),str(Sstar))
    return worst

# Generator A: "windmill" - r clusters of points arranged so charts force overshoot
def windmill(r, spread, npc):
    rows=[]
    # r vertices
    for i in range(r):
        rows.append([sp.Integer(1) if k==i else sp.Integer(0) for k in range(r)])
    # extra points pushed outside each edge
    for i in range(r):
        for _ in range(npc):
            v=[ -spread if k==i else (spread*sp.Rational(1,r-1)) for k in range(r)]
            # renormalize row sum to 1
            sgn=sum(v); v=[x + (1-sgn)*sp.Rational(1,r) for x in v]
            rows.append(v)
    L=sp.Matrix(rows)
    n=L.rows
    # left inverse on the r vertices
    sub=L[list(range(r)),:]
    if sub.det()==0: return None,None
    Binv=sub.inv(); B=sp.zeros(r,n)
    for c in range(r):
        for a in range(r): B[a,c]=Binv[a,c]
    return L,B

print("=== Overshoot windmill probe ===")
worstall=None
for r in [2,3]:
    for spread in [sp.Rational(1,4),sp.Rational(1,2),1,sp.Rational(3,2),2,3]:
        for npc in [1,2]:
            L,B=windmill(r,spread,npc)
            if L is None: continue
            P=rstoch_idem(L,B)
            if not is_idem_rstoch(P): continue
            res=per_step_check(P,L)
            if res is None: continue
            tag="VIOLATION" if res[0]<0 else "ok"
            if res[0]<0 or res[3]>=2:
                print(f"  r={r} spread={spread} npc={npc}: slack={res[0]} overshoot_rows={res[3]} "
                      f"max|a|={res[4]} lam_max={res[5]} lam_min={res[6]} d={res[7]} {tag}")
            if worstall is None or res[0]<worstall[0]:
                worstall=res

# Generator B: random heavy-overshoot search inside delta<=1/4
rng=random.Random(2024)
print("\n=== Random heavy-overshoot search (report min slack + any violation) ===")
minslack=None; viol=0; n_inside=0
for it in range(1500):
    r=rng.choice([2,3]); n=r+rng.choice([2,3])
    rows=[]
    for i in range(n):
        if i<r: rows.append([sp.Integer(1) if k==i else sp.Integer(0) for k in range(r)])
        else:
            w=[sp.Rational(rng.randint(-4,4),rng.randint(1,3)) for _ in range(r-1)]; w.append(1-sum(w))
            rows.append(w)
    L=sp.Matrix(rows)
    sub=L[list(range(r)),:]
    if sub.det()==0: continue
    Binv=sub.inv(); B=sp.zeros(r,n)
    for c in range(r):
        for a in range(r): B[a,c]=Binv[a,c]
    P=rstoch_idem(L,B)
    if not is_idem_rstoch(P): continue
    if not all(sp.nsimplify(x).is_rational for x in list(P)): continue
    res=per_step_check(P,L)
    if res is None: continue
    if F(res[7])<=F(1,4): n_inside+=1
    if res[0]<0:
        viol+=1; print("  VIOLATION:",res)
    if minslack is None or res[0]<minslack[0]: minslack=res
print(f"random search: violations={viol}, inside-delta instances={n_inside}")
print(f"global min slack: {minslack[0]} (overshoot_rows={minslack[3]}, max|a|={minslack[4]}, "
      f"lam range=[{minslack[6]},{minslack[5]}], d={minslack[7]})")
print(f"windmill min slack: {worstall[0]} (max|a|={worstall[4]}, lam_max={worstall[5]})")
