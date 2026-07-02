#!/usr/bin/env python3
"""[check] halo-robust collapse bound.  Refine the af-validated export node 1.2:
   split v's positive outside mass into GENUINE (dist>=eps) and HALO (dist<eps).
   dist(q,C_W) <= S^{-1}( sigt_g*H + (sigt-sigt_g)*eps ), S=1+nu>=1, giving

       H*(1 - sigt_g)  <=  (sigt - sigt_g)*eps  +  nu*(2+4 delta).

   With eps = tau/4 this bounds H by O(tau) provided sigt_g is bounded away from 1.
   Verify the inequality holds EXACTLY on the certified instances (a red->green
   style invariant: it must hold; then check it is non-vacuous, i.e. 1-sigt_g>0)."""
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import (is_idempotent, delta, visible_set, dist1_to_conv)

INSTANCES = {
 "A_maxSg":   ([[F('-3/80'),F('23/400'),F('5/12'),F('-1/200'),F('341/600')]],
               [[F('3/80')],[F('1/100')],[F('1/16')],[F('1/96')],[F('7/80')]]),
 "B_maxH":    ([[F('1/2'),F('-1/20'),F('11/20')],[F('257/400'),F('-7/200'),F('157/400')]],
               [[F('9/200'),F('1/80')],[F('1/200'),F('1/200')],[F('11/160'),F('1/100')]]),
 "C_selfmass":([[F('28/25'),F('1/200'),F(0),F('-1/8')]],
               [[F('-49/800')],[F('-1/6')],[F('-1/8')],[F('-33/800')]]),
}

def check(name, C, R2):
    P,_,_ = build_from_LambdaC(C,R2)
    n=len(P); d,negs=delta(P)
    W,info=visible_set(P,d)
    dists=[dist1_to_conv(P,W,i)[0] for i in range(n)]
    H=max(dd for dd in dists if dd is not None)
    outside=[j for j in range(n) if dists[j] is not None and dists[j]>0]
    tops=[v for v in range(n) if info.get(v,{}).get("vertex") and not info.get(v,{}).get("exposed")
          and dists[v] is not None and dists[v]>0]
    for v in tops:
        nu=negs[v]
        sigt=sum(max(P[v][j],F(0)) for j in outside)
        # eps = tau/4 -> eps^2 = delta/16 ; genuine: dist^2 >= delta/16
        gen=[j for j in outside if dists[j]*dists[j] >= d/16]
        sigt_g=sum(max(P[v][j],F(0)) for j in gen)
        halo=sigt - sigt_g
        # eps as exact upper rational bound on tau/4: eps >= tau/4 iff eps^2>=delta/16
        # use eps^2 = delta/16 exactly -> we need eps; bound halo*eps <= halo*sqrt(delta)/4.
        # verify H(1-sigt_g) <= halo*tau/4 + nu(2+4d) by squaring is messy; use float w/ exact inputs:
        import math
        tau=math.sqrt(float(d)); eps=tau/4
        lhs=float(H)*(1-float(sigt_g))
        rhs=float(halo)*eps + float(nu)*(2+4*float(d))
        print(f"[{name}] v={v} delta={float(d):.5f} H/tau={float(H)/tau:.4f} "
              f"sigt/tau={float(sigt)/tau:.4f} sigt_g/tau={float(sigt_g)/tau:.4f} "
              f"1-sigt_g={float(1-float(sigt_g)):.4f}")
        print(f"     halo-robust bound  H(1-sigt_g)={lhs:.6f} <= halo*tau/4+nu(2+4d)={rhs:.6f}  : {lhs<=rhs+1e-12}")
        print(f"     (non-vacuous: 1-sigt_g>0 ? {1-float(sigt_g)>0})  => H <= {rhs/max(1-float(sigt_g),1e-9):.5f} = {rhs/max(1-float(sigt_g),1e-9)/tau:.4f} tau")

for name,(C,R2) in INSTANCES.items():
    check(name,C,R2)
