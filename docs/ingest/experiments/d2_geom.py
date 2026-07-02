#!/usr/bin/env python3 -u
"""
d2_geom.py -- The PURE GEOMETRIC core (ignore exactness for a moment).

Question stripped of idempotence: for a finite point set X in R^d with the ell^1
metric, let W = well-exposed vertices (rho,kappa). Can some point of X be FAR
(>> rho-scale) from conv W?

This decouples the two pressures:
  (G) GEOMETRY: can a far-from-convW point exist at all (any point set)?
  (E) EXACTNESS: does P^2=P (R Lambda=I) then ALLOW such a geometry as P's rows?

If (G) is impossible for ALL point sets at the (rho,kappa)=(C tau, c tau) scaling,
the conjecture is true for trivial reasons (no idempotence needed). If (G) is
possible, we then must realize that geometry as an exact idempotent (E).

We test (G): build point sets where a target point is the centroid of a cloud
none of whose members is well-exposed.  A point is NON-exposed if no affine h
in [0,1] with h(point)=0 lifts all rho-far points to >=kappa.  The killer
configuration (from infra): a point that is an affine average of two far points
on OPPOSITE sides cannot be exposed.  Iterating: a far cloud where every point is
in the affine hull-interior of OTHER far points -> none exposed -> W loses them ->
W shrinks to the LOW vertices only -> the high cloud is far from conv W.

We build a 'far cap': a cloud of points high above a low base such that the cap
points mutually shadow.  The cap is a full-dimensional cloud (so its extreme
points ARE vertices) -- the issue is whether those extreme cap vertices are
EXPOSED.  An extreme point of the cap is exposed by a functional separating it
from the rest; but to be in W it must ALSO lift all OTHER far points (incl. the
low base which is far from it) to >=kappa while being 0 at the cap vertex.  If the
low base is on the 'wrong side', that fails.  THAT is the real mechanism: a cap
vertex's exposer would have to put the FAR LOW BASE above kappa while being 0 at
the cap -- but the base is on the opposite side, forcing base below 0.  CONTRADICT
=> cap vertices NOT well-exposed => W = base only => cap far from conv(base).

Let's test this directly: low base simplex at 'height 0', a far cap simplex at
'height H'.  Is any cap vertex (rho,kappa)-well-exposed?  Sweep H, kappa, rho.
"""
import sys, json
import numpy as np
from d1_infra import well_exposed_set, dist1_to_conv, exposed_margin, is_row_vertex

OUT="out/d2_geom.json"
res={"runs":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

def base_and_cap(d_base=2, H=0.4, base_r=0.5, cap_r=0.2, seed=0):
    """
    Points in R^n (n = enough coords). Low base = simplex of d_base+1 points at
    height 0 (last coord 0). Far cap = simplex of d_base+1 points at height H>0
    in a fresh 'up' coordinate, small radius cap_r, centered above base centroid.
    We keep rows summing to 1 (so they are bona fide P-rows) by reserving a
    'slack' coordinate.
    Coordinates: base uses coords 0..d_base; 'up' = coord (d_base+1); slack last.
    """
    rng=np.random.default_rng(seed)
    nb=d_base+1
    ncap=d_base+1
    ncoord=d_base+2+1  # base coords (d_base+1) + up + slack
    up=d_base+1; slack=d_base+2
    pts=[]
    # base simplex vertices: e_a scaled into [0,1], height 0
    base_dirs=rng.standard_normal((nb,d_base));
    for a in range(nb):
        p=np.zeros(ncoord)
        # base vertex on simplex of first d_base+1 coords
        p[a if a<d_base+1 else 0]= base_r
        pts.append(p)
    # better: explicit base = base_r * e_a for a=0..d_base (height 0)
    pts=[]
    for a in range(nb):
        p=np.zeros(ncoord); p[a]=base_r; pts.append(p)
    bcen=np.mean(pts,axis=0)
    # cap: above base centroid by H in 'up', small simplex radius
    cap_dirs=rng.standard_normal((ncap,d_base)); cap_dirs-=cap_dirs.mean(0)
    for k in range(ncap):
        p=bcen.copy(); p[up]+=H
        p[:d_base]+=cap_r*cap_dirs[k]
        pts.append(p)
    pts=np.array(pts)
    # fix slack so each row sums to 1
    s=pts.sum(axis=1)
    pts[:,slack]=1.0-s
    return pts, nb, ncap

def run(d_base=2,H=0.4,base_r=0.5,cap_r=0.2,rho=0.3,kappa=0.075,label="",verbose=False):
    pts,nb,ncap=base_and_cap(d_base,H,base_r,cap_r)
    n=pts.shape[0]
    W,info=well_exposed_set(pts,rho,kappa,verbose=False)
    # distances of cap points to conv W
    cap_idx=list(range(nb,nb+ncap))
    maxd=0; details=[]
    for i in cap_idx:
        di,_=dist1_to_conv(pts,W,i); maxd=max(maxd,di)
        details.append((i,round(di,3)))
    cap_in_W=[i for i in cap_idx if i in W]
    info_out={"label":label,"d_base":d_base,"H":H,"rho":rho,"kappa":kappa,
              "n":n,"nW":len(W),"W":list(map(int,W)),"cap_idx":cap_idx,
              "cap_in_W":cap_in_W,"max_cap_dist":float(maxd),"cap_dists":details}
    print(f"[{label}] H={H} rho={rho} kappa={kappa} |W|={len(W)} "
          f"cap_in_W={cap_in_W} max_cap_dist={maxd:.3f}", flush=True)
    res["runs"].append(info_out); save()
    return info_out, pts, W

if __name__=="__main__":
    print("="*70); print("d2_geom: PURE geometric core -- can a far cap escape conv W?"); print("="*70, flush=True)
    # sweep height vs (rho,kappa). The CONJECTURE-scaling is rho=C tau, kappa=c tau
    # but here we test pure geometry: does a tall cap have non-exposed vertices?
    for H in [0.2,0.5,1.0,2.0]:
        for kappa in [0.05,0.15,0.3]:
            run(d_base=2,H=H,base_r=0.5,cap_r=0.2,rho=0.4,kappa=kappa,
                label=f"H{H}_k{kappa}")
    print("\nInterpretation: if cap vertices are NEVER in W (cap_in_W empty) and",flush=True)
    print("max_cap_dist grows with H, the GEOMETRY admits a far plateau; then",flush=True)
    print("exactness is the only remaining gate. If cap vertices ALWAYS land in W,",flush=True)
    print("exposedness alone kills the plateau (conjecture true geometrically).",flush=True)
    print("d2_geom done.",flush=True)
