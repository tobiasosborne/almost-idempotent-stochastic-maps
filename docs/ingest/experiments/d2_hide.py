#!/usr/bin/env python3 -u
"""
d2_hide.py -- Can a row be FAR from conv W while NON-exposed, at the
conjecture scaling rho=C tau, kappa=c tau (tau small)?  Pure geometry, then note
the exactness gate.

Two hiding mechanisms to test honestly:
 (M1) NON-VERTEX far point. A point strictly inside conv(other points) is not a
   vertex (excluded from W by definition). For it to be FAR from conv W it must be
   inside conv(NON-exposed points) yet outside conv W. So we need a far region
   whose own vertices are NON-exposed. By the cap test, cap vertices are exposed
   at small kappa. So M1 needs the cap vertices themselves non-exposed.
 (M2) Make cap vertices non-exposed by SURROUNDING them: place far points on all
   affine sides of each cap vertex so the exposer (h(v)=0, others>=kappa) is
   impossible. The cleanest: a far point that is the affine centroid of a far
   simplex whose vertices are pushed out -> centroid is interior, non-vertex,
   far. But then conv W still must exclude that whole region.

We directly OPTIMIZE (pure geometry, ell^1, rows sum to 1): find a point set and a
marked row p* maximizing dist1(p*, conv W)/tau subject to: tau fixed scale,
rho=C tau, kappa=c tau. We do a structured search over 'cap-with-skirt'
configurations and also a random multistart, in the SMALL-kappa (true-scaling)
regime.

To emulate true scaling we set tau as a small parameter and place geometry at
ell^1-scale ~ tau (so rho, kappa, and inter-point distances are all ~tau).
THE KEY: at scale tau with kappa=c tau, an affine h with slope ~1 changes by
~ (ell1 distance) which is ~tau, so lifting far points to kappa=c tau ~ needs
slope ~ c -- generically feasible. Hiding requires CURVATURE the affine h lacks
across MANY points => need >= d+2 far points in 'convex-cap' position so no single
affine functional lifts all while vanishing at the marked vertex.
"""
import sys, json
import numpy as np
from scipy.optimize import minimize
from d1_infra import well_exposed_set, dist1_to_conv, exposed_margin

OUT="out/d2_hide.json"
res={"runs":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

def ratio_for_points(pts, C=4.0, c=0.25, tau=1.0):
    rho=C*tau; kappa=c*tau
    W,_=well_exposed_set(pts,rho,kappa)
    n=pts.shape[0]
    maxr=0.0; argi=-1
    for i in range(n):
        d,_=dist1_to_conv(pts,W,i)
        if d/tau>maxr: maxr=d/tau; argi=i
    return maxr, W, argi

# ---- structured: a 'circuit' of far points so each is non-exposed ----
def circuit_config(K=5, R=1.0, tau=1.0, base_m=2, base_r=0.5):
    """
    base_m low base vertices (exposed) at height 0.
    K far points arranged as a CONVEX POLYGON (circuit) high up; each polygon
    vertex is extreme, but its exposer must lift the OTHER polygon vertices AND
    the base. We test whether the circuit hides itself + admits a far interior
    centroid point.
    Coordinates: 2 'circle' coords (x,y) for the polygon + 1 'up' coord + base
    coords + slack.
    """
    ncoord = 2 + 1 + base_m + 1
    cx,cy,up,slack = 0,1,2, ncoord-1
    pts=[]
    # base vertices: at up=0, distinct base coords
    for a in range(base_m):
        p=np.zeros(ncoord); p[3+a]=base_r; pts.append(p)
    bcen=np.mean(pts,axis=0)
    # circuit: regular K-gon at height H=R (up), radius R in (x,y)
    H=R
    for k in range(K):
        th=2*np.pi*k/K
        p=bcen.copy(); p[up]+=H; p[cx]+=R*np.cos(th); p[cy]+=R*np.sin(th)
        pts.append(p)
    # interior centroid of the circuit (far, non-vertex)
    circ=np.array(pts[base_m:])
    pc=circ.mean(axis=0); pts.append(pc)
    pts=np.array(pts)
    s=pts.sum(axis=1); pts[:,slack]=1.0-s
    return pts, base_m, K

if __name__=="__main__":
    print("="*70); print("d2_hide: far+nonexposed at true scaling rho=C tau,kappa=c tau"); print("="*70, flush=True)
    tau=1.0  # pure geometry; ratios are scale-free here
    # sweep circuit size & radius (relative to rho=C tau=4, kappa=c tau=0.25)
    for K in [3,4,5,6,8]:
        for R in [0.5,1.0,2.0,4.0]:
            pts,bm,Kk=circuit_config(K=K,R=R,tau=tau,base_m=2,base_r=0.5)
            maxr,W,argi=ratio_for_points(pts,C=4.0,c=0.25,tau=tau)
            ncirc=Kk; cen_idx=pts.shape[0]-1
            cen_d,_=dist1_to_conv(pts,W,cen_idx)
            entry={"K":K,"R":R,"n":int(pts.shape[0]),"nW":len(W),"W":list(map(int,W)),
                   "max_ratio":float(maxr),"argmax":int(argi),
                   "centroid_dist":float(cen_d),"centroid_in_W":bool(cen_idx in W)}
            print(f"[K{K}_R{R}] |W|={len(W)} max_ratio={maxr:.3f} argmax={argi} "
                  f"centroid_dist={cen_d:.3f}", flush=True)
            res["runs"].append(entry); save()
    print("\nNote: rho=C tau=4.0 here. Points at radius R<<4 are NOT rho-far from",flush=True)
    print("each other, so the kappa constraint is vacuous among them -> easy to expose.",flush=True)
    print("That vacuity (rho too large vs geometry scale) is itself the codex's point.",flush=True)
    print("d2_hide done.",flush=True)
