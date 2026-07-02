#!/usr/bin/env python3
"""
ASQ envelope search in the canonical bary family.

Goal: among exact idempotents (canonical R=[I_r|0] family, so ANY bary rows are legal),
find configurations where TWO row-vertices v1,v2 are H-far from conv W and BOTH fail
(rho,kappa)-exposedness, and measure (H, delta=max-neg). Test whether delta/H^2 has a
positive lower bound (ASQ) or can be driven to 0 (refutation).

We parametrize a skinny quadrilateral at height H with small neg and OPTIMIZE the
free geometry (anchor positions, side rows, the split) to MINIMIZE delta subject to
'both far by >= H' and 'both fail exposedness'. Since W and exposedness are themselves
LP/combinatorial, we do a randomized + local search over geometry, evaluating the true
H, delta, and failure flags for each candidate, and track the frontier delta vs H.

Key regime: H ~ tau ~ sqrt(delta). We sweep target heights and for each measure the
minimal achievable delta with both-far-both-failing.
"""
import numpy as np
from scipy.optimize import linprog
import itertools, json
from asq_model import (neg_mass, l1, dist_to_hull_l1, exposed_margin, is_vertex, compute_W)

rng=np.random.default_rng(12345)

def eval_config(rows, C=4.0, cc=0.25):
    """Return dict with delta, tau, rho, kappa, W, and for the two designated high
    vertices (last two rows) their dist-to-convW and exposedness margin/fail."""
    nm=np.array([np.maximum(-np.array(r),0).sum() for r in rows])
    delta=nm.max(); tau=np.sqrt(delta) if delta>0 else 0.0
    rho=C*tau; kappa=cc*tau
    W=compute_W(rows,rho,kappa)
    convW=[rows[i] for i in W]
    res={'delta':delta,'tau':tau,'rho':rho,'kappa':kappa,'W':W,'nm':nm.tolist()}
    info=[]
    for vi in (len(rows)-2,len(rows)-1):
        if convW:
            dW=dist_to_hull_l1(np.array(rows[vi]),convW)
        else:
            dW=np.inf
        m=exposed_margin(rows,vi,rho)
        isv=is_vertex(rows,vi)
        fails = (m is None) or (m < kappa - 1e-9)
        info.append({'vi':vi,'dist_convW':dW,'margin':(None if m is None else float(m)),
                     'is_vertex':bool(isv),'fails_exp':bool(fails),
                     'in_W': vi in W})
    res['high']=info
    return res

def build(H, gap, s, anchor_spread, n_anchors, extra_high_split=0.0):
    """Triangle e0,e1,e2; anchors interior; two high vertices poking below edge e0-e1
    by depth H/2 (coord2 = -H/2 each), split between coords 0,1, separated by gap.
    extra side rows can be added by caller. Returns rows (bary, dim 3)."""
    rows=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
    for k in range(n_anchors):
        # interior points biased low (small coord2) to form a low face
        a0=0.5+anchor_spread*(rng.random()-0.5)
        a2=anchor_spread*rng.random()
        a1=1-a0-a2
        rows.append(np.array([a0,a1,a2]))
    # high vertices
    depth=H/2
    base0=0.5+s
    v1=np.array([base0, 1-base0+depth - depth, -depth]) # coord1 = 1-base0 - (-depth)?? fix below
    # ensure rowsum 1: coords sum to 1. choose coord2=-depth, coord0=base0, coord1=1-base0+depth.
    v1=np.array([base0, 1-base0+depth, -depth])
    v2=np.array([base0+gap, 1-base0-gap+depth, -depth])
    rows.append(v1); rows.append(v2)
    return rows

if __name__=="__main__":
    print("Sweep: for several target H (relative to expected tau), minimize delta over geometry")
    # We expect delta ~ H (since neg of a high vertex ~ depth = H/2). So delta~H, tau~sqrt(H),
    # and H/tau ~ sqrt(H) -> 0 as H->0. So far/H>=H0*tau means H>=H0*sqrt(H) i.e. sqrt(H)>=H0,
    # H>=H0^2: the FAR condition is only nontrivial for H above a floor. Let's just MEASURE.
    frontier=[]
    for H in [0.05,0.1,0.15,0.2,0.3,0.4,0.5]:
        best=None
        for trial in range(300):
            gap=rng.uniform(0.005,0.15)
            s=rng.uniform(-0.2,0.2)
            spread=rng.uniform(0.05,0.6)
            na=rng.integers(2,5)
            rows=build(H,gap,s,spread,na)
            r=eval_config(rows)
            hv=r['high']
            both_far = all(h['dist_convW']>=H-1e-9 for h in hv)
            both_fail= all(h['fails_exp'] for h in hv)
            both_vert= all(h['is_vertex'] for h in hv)
            if both_far and both_fail and both_vert:
                key=r['delta']
                if best is None or key<best['delta']:
                    best={'delta':r['delta'],'tau':r['tau'],'H':H,
                          'dists':[h['dist_convW'] for h in hv],
                          'margins':[h['margin'] for h in hv],'kappa':r['kappa'],
                          'W':r['W']}
        if best:
            best['delta_over_H2']=best['delta']/H**2
            frontier.append(best)
            print(f"H={H}: min delta={best['delta']:.4f} tau={best['tau']:.4f} "
                  f"delta/H^2={best['delta_over_H2']:.3f} dists={np.round(best['dists'],3)} "
                  f"margins={best['margins']} kappa={best['kappa']:.4f}")
        else:
            print(f"H={H}: NO config with both-far + both-fail + both-vertex found (out of 300)")
