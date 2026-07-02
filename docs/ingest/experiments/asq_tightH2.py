#!/usr/bin/env python3
r"""
Find configs where H=dist_1(v,conv W) is LARGE relative to 2*neg(v) -- i.e. the vertex is
far from conv W not (only) because it pokes out, but because conv W is SMALL/low (W lost
some archetypes). That is the regime where delta/H^2 could approach its true infimum and
potentially REFUTE ASQ (if delta/H^2 -> 0).

Mechanism for H >> 2 neg(v): if some archetypes are NOT in W (e.g. an archetype is itself
shadowed/non-vertex), conv W shrinks and v can be far from it even with small neg. We try
to engineer this: a low face that does NOT span the simplex, with the high vertices far
from that small low face.

But: archetypes e_a are unit vectors; an archetype is a vertex and is isolated (dist to
hull of others is large) => it EXPOSES => it's in W. Hard to evict an archetype from W. The
only way conv W misses simplex directions is if NO row points that way. Then 'far from conv
W' in that direction is cheap. Test: put both high vertices far in a direction the low face
doesn't cover, with small neg.
"""
import numpy as np
from scipy.optimize import linprog
from asq_model import l1, dist_to_hull_l1, exposed_margin, is_vertex, compute_W

def neg_row(r): return np.maximum(-np.array(r),0).sum()

def evaluate_full(rows,C=4.0,cc=0.25):
    nm=[neg_row(r) for r in rows]; delta=max(nm)
    if delta<=1e-12: return None
    tau=np.sqrt(delta); rho=C*tau; kappa=cc*tau
    W=compute_W(rows,rho,kappa); convW=[rows[i] for i in W]
    if not convW: return None
    # designate the two highest-neg vertices as the 'high pair'
    order=np.argsort(nm)[::-1]
    hi=[i for i in order if is_vertex(rows,i)][:2]
    if len(hi)<2: return None
    i1,i2=hi
    d1=dist_to_hull_l1(rows[i1],convW); d2=dist_to_hull_l1(rows[i2],convW)
    m1=exposed_margin(rows,i1,rho); m2=exposed_margin(rows,i2,rho)
    f1=(m1 is None) or (m1<kappa-1e-9); f2=(m2 is None) or (m2<kappa-1e-9)
    H=min(d1,d2)
    both=f1 and f2 and np.isfinite(H) and H>1e-9 and i1 not in W and i2 not in W
    return dict(delta=delta,H=H,both=both,W=W,d1=d1,d2=d2,m1=m1,m2=m2,kappa=kappa,rho=rho,
                nm=nm,hi=hi,negH=max(nm[i1],nm[i2]),neg2H=2*max(nm[i1],nm[i2]))

rng=np.random.default_rng(99)
print("Broad random search (any-dim canonical bary rows) for SMALL delta/H^2 with both-failing.")
print("Goal: drive delta/H^2 below the ~3.8 floor => would refute ASQ. Track the worst.")
worst=None; nfound=0
for trial in range(20000):
    r=rng.integers(3,5)         # simplex dim r-1
    nrows=rng.integers(r+2, r+6)
    rows=[np.eye(r)[a] for a in range(r)]   # archetypes
    # extra rows: bary vectors, mostly low (small neg), a couple high (the pair)
    for _ in range(nrows-r-2):
        x=rng.dirichlet(np.ones(r))         # interior, neg 0
        rows.append(x)
    # two high vertices: poke out a bit
    for _ in range(2):
        x=rng.dirichlet(np.ones(r))
        a=rng.integers(r); p=rng.uniform(0.01,0.12)
        x=x.copy(); x[a]-=p;
        # renormalize others up to keep sum 1
        idx=[j for j in range(r) if j!=a]; x[idx]+= p/len(idx)
        rows.append(x)
    res=evaluate_full(rows)
    if res and res['both']:
        nfound+=1
        ratio=res['delta']/res['H']**2
        if worst is None or ratio<worst[0]:
            worst=(ratio,res['delta'],res['H'],res['negH'],res['W'],res['m1'],res['m2'],res['kappa'])
print(f"both-failing configs found: {nfound}")
if worst:
    print(f"MIN delta/H^2 = {worst[0]:.3f}  (delta={worst[1]:.4f} H={worst[2]:.4f} neg_highpair={worst[3]:.4f})")
    print(f"   W={worst[4]} m1={worst[5]} m2={worst[6]} kappa={worst[7]:.4f}")
    print(f"   note: H vs 2*neg = {worst[2]:.4f} vs {2*worst[3]:.4f}  (if H>2neg, conv W lost coverage)")
else:
    print("no both-failing config found in random search")
