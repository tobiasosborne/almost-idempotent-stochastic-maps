#!/usr/bin/env python3
"""exp9b: coarse EXACT 2D scan of the symmetric twin family -> exact small-delta
   frontier (max sigt/tau subject to hiddenness).  Confirms the float search."""
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import analyze, is_idempotent, delta

def evalpr(p, r):
    x = p/3
    C = [[F(1,2)-x, F(1,2)+x+p, -p],[F(1,2)+x, F(1,2)-x+p, -p]]
    R2 = [[r,r],[r,r],[r,r]]
    P,_,_ = build_from_LambdaC(C, R2)
    if not is_idempotent(P)[0]: return None
    d,_ = delta(P)
    if d==0 or d>F(1,4): return None
    res = analyze(P, verbose=False)
    tops=[v for v in res["hidden"] if res["dists"][v] and res["dists"][v]>0]
    if not tops: return None
    tau=float(d)**0.5
    v=max(tops,key=lambda i:res["sigma_tilde"][i])
    s=res["sigma_tilde"][v]; dv=res["dists"][v]
    return dict(delta=d,St=float(s)/tau,Ht=float(dv)/tau,oneminus=float(F(1)-s)/tau,nhid=len(tops))

best_St=None
rows=[]
for pn in [2,4,8,12,16,24,32,44,56]:
    p=F(pn,200)
    for rn in [1,2,4,8,16,24,32,40,50,63]:
        r=F(rn,2000)
        res=evalpr(p,r)
        if res is None: continue
        if best_St is None or res["St"]>best_St["St"]:
            best_St=dict(res,p=p,r=r)
print("EXACT symmetric-twin frontier scan (small delta):")
print(f"MAX sigt/tau : p={best_St['p']} r={best_St['r']} delta={float(best_St['delta']):.5f} "
      f"sigt/tau={best_St['St']:.4f} H/tau={best_St['Ht']:.4f} (1-s)/tau={best_St['oneminus']:.4f}")
