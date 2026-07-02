#!/usr/bin/env python3
"""exp8: scan the wave-1 twin family, cranking the TAIL (self+twin) mass rho.
   Tests the self-mass route to sigma~ -> 1.  Family (build_from_LambdaC):
     C  = [[1/2-x, 1/2+x+p, -p],[1/2+x, 1/2-x+p, -p]], x=p/3
     R2 = [[r,r],[r,r],[r,r]]         (tail block; r = self/twin mass knob)
   As r grows, does sigma~ -> 1 while staying hidden and delta small?
   Everything exact (Fraction)."""
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import analyze, is_idempotent, delta

def run(p, r, verbose=False):
    x = p/3
    C = [[F(1,2)-x, F(1,2)+x+p, -p],[F(1,2)+x, F(1,2)-x+p, -p]]
    R2 = [[r,r],[r,r],[r,r]]
    P,_,_ = build_from_LambdaC(C, R2)
    ok,_,_ = is_idempotent(P)
    assert ok
    res = analyze(P, verbose=False)
    d = res["delta"]
    if d==0:
        return None
    tau2 = float(d)**0.5
    hid = res["hidden"]
    out = {"p":p,"r":r,"delta":d,"H":res["H"],"W":res["W"],"hidden":hid,
           "sigt":res["sigma_tilde"],"argmaxH":res["argmaxH"]}
    return out

print(f"{'p':>8} {'r':>8} {'delta':>10} {'H/tau':>8} {'|W|':>4} {'#hid':>5} "
      f"{'max sigt/tau(hid)':>18} {'1-sigt(minhid)':>14}")
p = F(1,40)
for rnum in [1,2,4,8,16,32,64,80,90,95,99,120,150,200,300,400,490]:
    r = F(rnum,1000)
    out = run(p, r)
    if out is None:
        print(f"{float(p):8.4f} {float(r):8.4f}  delta=0"); continue
    d=out["delta"]; tau2=float(d)**0.5
    hid=out["hidden"]; sigt=out["sigt"]
    if hid:
        sighid = [sigt[v] for v in hid]
        maxsig = max(sighid)
        # min (1-sigt) over hidden vertices that are actually top (dist>0)
        minoneminus = min(F(1)-sigt[v] for v in hid)
        print(f"{float(p):8.4f} {float(r):8.4f} {float(d):10.5f} {float(out['H'])/tau2:8.4f} "
              f"{len(out['W']):4d} {len(hid):5d} {float(maxsig)/tau2:18.4f} "
              f"{float(minoneminus):14.6f}  [1-sigt/tau={float(minoneminus)/tau2:.4f}]")
    else:
        print(f"{float(p):8.4f} {float(r):8.4f} {float(d):10.5f} {float(out['H'])/tau2:8.4f} "
              f"{len(out['W']):4d} {len(hid):5d}  (no hidden vertices)")
