#!/usr/bin/env python3
"""exp8b: instrument the twin-family exposure transition.
   Track ||p3-p4||_1 / rho (mutual-shield window), t*(3), self-mass P33,
   tail mass, and whether hidden, as tail knob r grows.  Explains WHY
   the self-mass route exposes."""
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import (analyze, is_idempotent, delta, l1, exposed_tstar,
                      is_row_vertex, visible_set)

p = F(1,40); x = p/3
print(f"{'r':>7} {'delta':>9} {'||p3-p4||/rho':>13} {'P33(self)':>10} "
      f"{'tailmass3':>10} {'t*(3)':>9} {'kappa':>9} {'hidden?':>8} {'H/tau':>7}")
for rnum in [1,4,8,16,24,32,40,48,56,60,63,64,66,70,80]:
    r = F(rnum,1000)
    C = [[F(1,2)-x, F(1,2)+x+p, -p],[F(1,2)+x, F(1,2)-x+p, -p]]
    R2 = [[r,r],[r,r],[r,r]]
    P,_,_ = build_from_LambdaC(C, R2)
    d,_ = delta(P)
    tau2 = float(d)**0.5
    rho2 = 16*d  # rho^2
    sep = l1(P[3],P[4])
    P33 = P[3][3]
    tail3 = P[3][3]+P[3][4]
    ts = exposed_tstar(P, 3, d)
    kappa = tau2/4
    W,info = visible_set(P, d)
    hid = 3 not in W and info.get(3,{}).get("vertex",False)
    res = analyze(P, verbose=False)
    Hstr = f"{float(res['H'])/tau2:.4f}" if res['H'] else "0"
    tsstr = f"{float(ts):.4f}" if ts is not None else "+inf"
    print(f"{float(r):7.3f} {float(d):9.5f} {float(sep)/(4*tau2):13.4f} "
          f"{float(P33):10.4f} {float(tail3):10.4f} {tsstr:>9} {kappa:9.4f} "
          f"{str(hid):>8} {Hstr:>7}")
