#!/usr/bin/env python3
r"""
Find the WORST (smallest delta/H^2) over the both-far-both-failing window, by scanning
the boundary where the high vertices are about to join W, across geometry params.
This estimates the universal constant c in delta >= c H^2, i.e. c = min delta/H^2.

Also test the (C,c) baseline sensitivity and a crucial REFUTATION probe: can extra
anchor structure (a third high 'helper', or asymmetric low face) push delta/H^2 below
the observed floor? If yes -> ASQ false; report config.
"""
import numpy as np
from scipy.optimize import linprog
from asq_model import l1, dist_to_hull_l1, exposed_margin, is_vertex, compute_W

def neg_row(r): return np.maximum(-np.array(r),0).sum()

def make(depth, gap, anchors, side=0.0):
    rows=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
    for a in anchors: rows.append(np.array(a,float))
    v1=np.array([0.5+side, 0.5-side+depth, -depth])
    v2=np.array([0.5+side+gap, 0.5-side-gap+depth, -depth])
    rows.append(v1); rows.append(v2)
    return rows

def evaluate(rows, C, cc):
    nm=[neg_row(r) for r in rows]; delta=max(nm)
    if delta<=0: return None
    tau=np.sqrt(delta); rho=C*tau; kappa=cc*tau
    W=compute_W(rows,rho,kappa); convW=[rows[i] for i in W]
    i1,i2=len(rows)-2,len(rows)-1
    d1=dist_to_hull_l1(rows[i1],convW) if convW else np.inf
    d2=dist_to_hull_l1(rows[i2],convW) if convW else np.inf
    m1=exposed_margin(rows,i1,rho); m2=exposed_margin(rows,i2,rho)
    f1=(m1 is None) or (m1<kappa-1e-9); f2=(m2 is None) or (m2<kappa-1e-9)
    v1,v2 = is_vertex(rows,i1), is_vertex(rows,i2)
    H=min(d1,d2)
    return dict(delta=delta,tau=tau,rho=rho,kappa=kappa,H=H,d1=d1,d2=d2,
               m1=m1,m2=m2,fail1=f1,fail2=f2,vert1=v1,vert2=v2,W=W,
               both=f1 and f2 and v1 and v2 and np.isfinite(H) and H>1e-9)

print("=== boundary scan: baseline (C=4,c=1/4) ===")
anchors=[[1/3,1/3,1/3],[0.45,0.45,0.1],[0.2,0.6,0.2],[0.6,0.2,0.2]]
best=None
for depth in np.linspace(0.005,0.12,60):
    for gap in [0.05*depth,0.2*depth,0.5*depth, 0.01,0.03]:
        rows=make(depth,gap,anchors)
        r=evaluate(rows,4.0,0.25)
        if r and r['both']:
            ratio=r['delta']/r['H']**2
            if best is None or ratio<best[0]:
                best=(ratio,depth,gap,r['H'],r['delta'],r['m1'],r['kappa'])
print("min delta/H^2 (baseline):", best)

print("\n=== baseline (C=2,c=1/2) ===")
best2=None
for depth in np.linspace(0.005,0.2,80):
    for gap in [0.05*depth,0.2*depth,0.5*depth,0.01,0.03]:
        rows=make(depth,gap,anchors)
        r=evaluate(rows,2.0,0.5)
        if r and r['both']:
            ratio=r['delta']/r['H']**2
            if best2 is None or ratio<best2[0]:
                best2=(ratio,depth,gap,r['H'],r['delta'],r['m1'],r['kappa'])
print("min delta/H^2 (C=2,c=1/2):", best2)

print("\n=== REFUTATION probe: random anchor faces + asymmetry, baseline ===")
rng=np.random.default_rng(7)
worst=None
for _ in range(4000):
    na=rng.integers(2,6)
    anc=[]
    for _ in range(na):
        a0=rng.uniform(0,1); a2=rng.uniform(0,0.5*(1-a0)); a1=1-a0-a2
        anc.append([a0,a1,a2])
    depth=rng.uniform(0.005,0.1); gap=rng.uniform(0.0,0.06); side=rng.uniform(-0.25,0.25)
    rows=make(depth,gap,anc,side)
    r=evaluate(rows,4.0,0.25)
    if r and r['both']:
        ratio=r['delta']/r['H']**2
        if worst is None or ratio<worst[0]:
            worst=(ratio,depth,gap,side,na,r['H'],r['delta'],r['m1'],r['kappa'])
print("min delta/H^2 over random anchored configs:", worst)
print("(if this floor stays well above 0, ASQ supported; the floor is ~ c in delta>=cH^2)")
