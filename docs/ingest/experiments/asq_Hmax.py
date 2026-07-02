#!/usr/bin/env python3
r"""
Pin H_max: the largest H=dist_1(v,conv W) achievable with BOTH high vertices failing
(rho,kappa)-exposedness, as a function of the geometry. Since delta=H/2 (measured), the
constant in ASQ is c = inf delta/H^2 = inf (H/2)/H^2 = 1/(2 H_max). ASQ TRUE iff H_max
is universally bounded. We must determine: is H_max bounded by an ABSOLUTE constant, or
does it scale with tau (=sqrt(delta)=sqrt(H/2)) so that the bound is self-referential?

Self-referential check: delta=H/2, tau=sqrt(H/2). 'far' threshold rho=4tau=4 sqrt(H/2).
For the high vertex to be FAR from conv W by H, need H to be a real ell1 distance; for it
to FAIL exposedness need shadow<rho i.e. mutual shadow gap<rho=4sqrt(H/2). As H grows,
rho=4sqrt(H/2) grows like sqrt(H) -- SLOWER than H. At some point H exceeds what the
mutual-shadow + anchored geometry can hide, and the vertex EXPOSES (joins W). Find that H.

Also: when the high vertices join W, is it because the FAR set empties (rho > diam) -- the
vacuous large-tau regime d3 warned about -- or a genuine exposedness? Distinguish.
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
def probe(rows,C=4.0,cc=0.25):
    nm=[neg_row(r) for r in rows]; delta=max(nm)
    tau=np.sqrt(delta); rho=C*tau; kappa=cc*tau
    W=compute_W(rows,rho,kappa); convW=[rows[i] for i in W]
    i1,i2=len(rows)-2,len(rows)-1
    d1=dist_to_hull_l1(rows[i1],convW) if convW else np.inf
    d2=dist_to_hull_l1(rows[i2],convW) if convW else np.inf
    m1=exposed_margin(rows,i1,rho); m2=exposed_margin(rows,i2,rho)
    f1=(m1 is None) or (m1<kappa-1e-9); f2=(m2 is None) or (m2<kappa-1e-9)
    # is far set empty (vacuous)?
    pv=rows[i1]; nfar=sum(1 for i in range(len(rows)) if i!=i1 and l1(rows[i],pv)>=rho)
    diam=max(l1(rows[a],rows[b]) for a in range(len(rows)) for b in range(len(rows)))
    return dict(delta=delta,tau=tau,rho=rho,kappa=kappa,d1=d1,d2=d2,m1=m1,m2=m2,
                f1=f1,f2=f2,W=W,nfar=nfar,diam=diam,
                both=f1 and f2 and is_vertex(rows,i1) and is_vertex(rows,i2)
                     and np.isfinite(min(d1,d2)) and min(d1,d2)>1e-9)

# many anchor geometries; for each, binary-search the max depth with both-failing.
rng=np.random.default_rng(3)
print("Per geometry: H_max (largest min-dist with both-failing), delta there, rho vs diam (vacuity).")
records=[]
for trial in range(12):
    na=rng.integers(3,6); anc=[]
    for _ in range(na):
        a0=rng.uniform(0.1,0.9); a2=rng.uniform(0,0.4*(1-a0)); anc.append([a0,1-a0-a2,a2])
    gapfac=rng.uniform(0.02,0.5); side=rng.uniform(-0.15,0.15)
    lo,hi=0.005,0.6; bestok=None
    # find largest depth with both-failing by scan (non-monotone safe)
    for depth in np.linspace(0.005,0.6,120):
        r=probe(make(depth,gapfac*depth,anc,side))
        if r['both']:
            if bestok is None or depth>bestok[0]:
                bestok=(depth,r)
    if bestok:
        depth,r=bestok
        Hm=min(r['d1'],r['d2'])
        vac = r['rho']>=r['diam']  # far set could be empty/vacuous
        records.append((Hm,r['delta'],r['delta']/Hm**2,depth,r['rho'],r['diam'],vac,r['nfar']))
        print(f"trial {trial}: H_max={Hm:.4f} delta={r['delta']:.4f} delta/H^2={r['delta']/Hm**2:.2f} "
              f"depth={depth:.3f} rho={r['rho']:.3f} diam={r['diam']:.3f} rho>=diam?{vac} nfar={r['nfar']}")
    else:
        print(f"trial {trial}: no both-failing config")
if records:
    rec=np.array([(a,b,c) for (a,b,c,*_ ) in records])
    print(f"\nMIN delta/H^2 across geometries = {rec[:,2].min():.3f}  (= c, the ASQ constant in max-neg units)")
    print(f"MAX H_max = {rec[:,0].max():.4f}; corresponding tau range; is H_max/tau bounded?")
    for (Hm,d,r,*_) in records:
        print(f"   H_max={Hm:.4f} tau={np.sqrt(d):.4f} H_max/tau={Hm/np.sqrt(d):.3f}")
