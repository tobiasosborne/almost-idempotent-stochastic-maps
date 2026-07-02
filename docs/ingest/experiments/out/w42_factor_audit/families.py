#!/usr/bin/env python3
"""Run the campaign's named families through INDEPENDENT factorization metrics, and
verify EACH intermediate inequality of the w41 proof on real instances:
   (i)   S* = sum beta_+ g       (g = sigma + 2(-lam)_+)
   (ii)  S* <= Phi + 2 Dpos      (pointwise g <= E + 2 lam_+)
   (iii) Dpos = V + Dneg         (DEF identity)
   (iv)  V <= Phi/2
   (v)   Dneg <= 3 delta
   (vi)  S* <= 2 Phi + 6 delta
We import ONLY the family CONSTRUCTORS from w39 harness; all metric code is ours.
"""
import sys, itertools
sys.path.insert(0, '../w39_opus_repair')
import sympy as sp
from fractions import Fraction as F
from harness import (transverse_pair, dense_pair_k7, staircase,
                     perturbed_staircase, no_center_path)

def delta_of(P):
    n=P.rows; d=sp.Integer(0)
    for i in range(n):
        d=sp.Max(d, sum(sp.Max(-P[i,j],0) for j in range(P.cols)))
    return sp.nsimplify(d)

def theta_half(L):
    n,r=L.rows,L.cols; vols={}
    for b in itertools.combinations(range(n),r):
        dd=L[list(b),:].det()
        if dd!=0: vols[b]=abs(dd)
    vmax=max(vols.values())
    return [b for b,v in vols.items() if 2*v>=vmax]

def audit_family(name, L, B):
    P=sp.simplify(L*B)
    n=P.rows
    # idempotent + stochastic
    if sp.simplify(P*P-P)!=sp.zeros(n,n):
        print(f"[{name}] NOT idempotent -- skip"); return
    d=delta_of(P)
    charts=theta_half(L)
    worst=None; fails=[]
    for basis in charts:
        A=sp.simplify(L*L[list(basis),:].inv())
        r=A.cols
        for s in range(r):
            u=basis[s]
            Phi=Splus=Vpos=Dpos=Dneg=Sstar_g=sp.Integer(0)
            DEFsum=sp.Integer(0)
            for j in range(P.cols):
                beta=sp.nsimplify(P[u,j]); bp=sp.Max(beta,0); bm=sp.Max(-beta,0)
                a_s=A[j,s]; lam=1-a_s
                sigma=sum(sp.Max(A[j,t],0) for t in range(r) if t!=s)
                E=sp.Max(sigma-2*lam,0)
                g=sigma+2*sp.Max(-lam,0)
                lam_p=sp.Max(lam,0); lam_m=sp.Max(-lam,0)
                Phi+=bp*E; Splus+=bp*sigma; Vpos+=bp*lam_m
                Dpos+=bp*lam_p; Dneg+=bm*lam; Sstar_g+=bp*g
                DEFsum+=beta*lam
            Sstar=Splus+2*Vpos
            # checks
            c_i  = sp.nsimplify(Sstar - Sstar_g)            # ==0
            c_def= sp.nsimplify(DEFsum)                      # ==0
            c_iii= sp.nsimplify(Dpos-(Vpos+Dneg))           # ==0
            c_iv = sp.nsimplify(Phi/2 - Vpos)               # >=0
            c_v  = sp.nsimplify(3*d - Dneg)                 # >=0
            c_vi = sp.nsimplify(2*Phi+6*d-Sstar)            # >=0
            def ge0(x):
                x=sp.simplify(x)
                return bool(x>=0) or x.is_nonnegative is True
            def eq0(x):
                return sp.simplify(x)==0
            for nm,val,kind in [('S*=Σβ+g',c_i,'eq'),('DEF=0',c_def,'eq'),
                                ('Dpos=V+Dneg',c_iii,'eq'),('V<=Phi/2',c_iv,'ge'),
                                ('Dneg<=3d',c_v,'ge'),('S*<=2Phi+6d',c_vi,'ge')]:
                bad = (not eq0(val)) if kind=='eq' else (not ge0(val))
                if bad: fails.append((basis,s,nm,str(val)))
            cv=sp.simplify(c_vi)
            wv = float(cv) if cv.is_number else 0.0
            if worst is None or wv<worst[0]:
                worst=(wv,basis,s,str(Phi),str(Sstar),str(d))
    status = "ALL STEPS OK" if not fails else f"FAILURES={len(fails)}"
    print(f"[{name}] delta={d} charts={len(charts)} min_slack(S*<=2Phi+6d)={worst[0]} {status}")
    for f in fails[:5]:
        print("    FAIL", f)

print("=== Campaign families through independent factorization audit ===")
for a in [sp.Rational(1,8), sp.Rational(1,4), sp.Rational(1,2), 1]:
    audit_family(f"transverse_pair a={a}", *transverse_pair(a))
for m in [1,2,3]:
    audit_family(f"staircase m={m}", *staircase(m))
for m,eps in [(1,sp.Rational(1,1000)),(2,sp.Rational(1,1000)),(5,sp.Rational(1,1000)),(2,sp.Rational(1,10))]:
    audit_family(f"perturbed_staircase m={m} eps={eps}", *perturbed_staircase(m,eps))
audit_family("dense_pair_k7", *dense_pair_k7())
for k in [4,5,6]:
    res=no_center_path(k)
    if res: audit_family(f"no_center_path k={k}", *res)
