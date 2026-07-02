#!/usr/bin/env python3 -u
"""
d2_cluster.py -- Build a HIDDEN plateau CLUSTER (Task 2, the real attempt).

Findings so far:
  - Pushing a SINGLE row far out makes it an extreme vertex that is itself
    well-exposed (joins W) => dist=0. (d2_fixR)
  - Letting the optimizer choose R drives delta->0 (relocates). (d2_plateau)
So a counterexample needs a GROUP of plateau rows that are FAR from conv W but
each NON-well-exposed because the others shadow it (the affine-midpoint
non-exposure: a row that is an affine combo of two far rows can't be lifted to
>=kappa by an affine h while h(v)=0).

GOAL geometry (abstract, in the (r-1)-flat):
  - W = m well-exposed low vertices (a low face), realized as clean prob rows.
  - A plateau CLUSTER of g rows sitting far 'above' conv W, arranged so that
    every cluster row lies in the relative interior of the convex hull of the
    OTHER cluster rows' affine shadow -> non-exposed. Classic: cluster points on
    a small sphere/regular simplex whose CENTROID is far, each point a vertex but
    mutually shadowing? Actually mutual shadowing needs a point to be an affine
    average of others. A regular simplex's vertices are all extreme & exposed.
  - To hide, use a cluster where some rows are STRICTLY INSIDE the cluster hull
    (non-vertices) -> automatically dist measured to conv W; but non-vertices are
    excluded from W by definition, and we want them FAR from conv W.

KEY TARGET: a far row p* that is the AFFINE MIDPOINT of two far rows p_a,p_b which
are themselves far from conv W. Then p* is not exposed (proved by infra test).
If p_a,p_b are ALSO not exposed (shadowed by yet others), the whole cluster is
hidden and far. The minimal closed instance: a far SEGMENT [p_a,p_b] none of
whose points (incl. endpoints) is well-exposed, with the segment >= D tau from
conv W. Endpoints p_a,p_b ARE vertices; to make them non-exposed we need MORE far
rows beyond them on both sides (so each endpoint is shadowed). This is a far
'staircase'/circuit. We try a far cluster forming a small regular polygon (cycle)
whose every vertex is shadowed by the convex position of the others + extra rows.

Concretely we PIN realized rows (fixed R = clean basis e_a) and place a cluster
of g rows as a small simplex centered at a far point, PLUS we add for each cluster
vertex a 'mirror' row just outside it so the vertex is the midpoint of (mirror,
interior) => non-exposed. Then test exactness via R Lambda = I and read delta+ratio.

Because pinning rows forces Lambda = bary(targets), R Lambda=I may FAIL; we
report the residual (the obstruction) AND, when we add the necessary extra rows
to satisfy it, whether THOSE extra rows are themselves well-exposed & near (which
would re-expose the cluster). That tension is the crux.
"""
import sys, json, itertools
import numpy as np
from d1_infra import (check_idempotent, neg_mass, ratio_stats, check_factorization,
                      well_exposed_set, dist1_to_conv, exposed_margin, is_row_vertex)

OUT="out/d2_cluster.json"
res={"runs":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

def bary(t,R):
    r,n=R.shape
    A=np.vstack([R.T,np.ones(r)]); b=np.concatenate([t,[1.0]])
    lam,*_=np.linalg.lstsq(A,b,rcond=None)
    return lam, float(np.abs(A@lam-b).max())

def attempt_cluster(m_w=2, g=3, height=0.4, radius=0.15, mirror=0.1, label="", verbose=False):
    """
    r = m_w + 1 pillar (the 'up' direction). n = rows.
    Rows:
      0..m_w-1 : W archetypes (clean prob vertices e_a). These define conv W.
      pillar archetype index P = m_w (e_{m_w}) -- realized but maybe not in W.
      cluster of g rows near abstract centroid 'high' = e_P pushed up by 'height'
        along (e_P - centroid_W); arranged in a small simplex of 'radius'.
      mirror rows: for each cluster vertex, one row just beyond it so it is the
        midpoint of (mirror, cluster-centroid) -> shadowed/non-exposed.
    R = clean basis (r x n). Lambda = bary(targets). Test R Lambda = I.
    """
    r=m_w+1; P_idx=m_w
    cluster=[]; mirrors=[]
    # We'll lay out targets directly in R^n later; first count rows.
    # rows: r archetypes + g cluster + g mirrors
    nrows=r + g + g
    n=nrows
    R=np.zeros((r,n))
    for a in range(r): R[a,a]=1.0
    targets=[R[a].copy() for a in range(r)]
    # abstract 'up' direction: from W-centroid to pillar
    wcen=np.zeros(r); wcen[:m_w]=1.0/m_w
    up=np.zeros(r); up[P_idx]=1.0; up=up-wcen
    cen=wcen+ (1+height)*up   # cluster centroid abstract coord, pushed beyond pillar
    # small simplex of g cluster points around cen, in a 2-plane of the flat
    # use random small offsets summing to zero (stay on the sum=1 flat)
    rng=np.random.default_rng(0)
    offs=rng.standard_normal((g,r)); offs-=offs.mean(axis=1,keepdims=True)
    offs/=np.abs(offs).max(); offs*=radius
    cluster_lams=[]
    for k in range(g):
        lam=cen+offs[k]
        cluster_lams.append(lam)
        targets.append(lam@R)
    # mirrors: push each cluster vertex further out from centroid (so vertex is
    # between centroid and mirror)
    for k in range(g):
        lam=cen + (offs[k])* (1+ mirror/max(radius,1e-9))  # beyond cluster vertex
        # ensure it's strictly beyond: scale offset up
        lam=cen + offs[k]*(1.0+mirror)
        targets.append(lam@R)
    Lam=np.array([bary(t,R)[0] for t in targets])
    Pm=Lam@R
    fact=check_factorization(Lam,R)
    chk=check_idempotent(Pm)
    nm,delta=neg_mass(Pm)
    info={"label":label,"r":r,"n":n,"g":g,"height":height,"radius":radius,"mirror":mirror,
          "RLambda_err":fact["RLambda_minus_I"],"idem_ok":chk["ok"],
          "idem_resid":chk["idem_resid"],"delta":float(delta)}
    if chk["ok"] and delta>1e-9:
        rs=ratio_stats(Pm,label=label)
        info.update({"max_ratio":rs["max_ratio"],"tau":rs["tau"],"nW":rs["nW"],"W":rs["W"]})
        # which rows are far AND non-exposed?
        tau=rs["tau"]; W=rs["W"]
        far_hidden=[]
        for i in range(n):
            d,_=dist1_to_conv(Pm,W,i)
            if d/tau>1.0 and i not in W:
                far_hidden.append((i,round(d/tau,3)))
        info["far_hidden_rows"]=far_hidden
    print(f"[{label}] RLam_err={fact['RLambda_minus_I']:.2e} idem_ok={chk['ok']} "
          f"idem_resid={chk['idem_resid']:.2e} delta={delta:.3e} "
          f"ratio={info.get('max_ratio','NA')} far_hidden={info.get('far_hidden_rows','NA')}",
          flush=True)
    res["runs"].append(info); save()
    return info, Lam, R, Pm

if __name__=="__main__":
    print("="*70); print("d2_cluster: hidden far plateau cluster"); print("="*70, flush=True)
    for g in [2,3,4]:
        for height in [0.2,0.4,0.8]:
            for radius in [0.1,0.3]:
                attempt_cluster(m_w=2,g=g,height=height,radius=radius,mirror=0.1,
                                label=f"g{g}_h{height}_r{radius}")
    print("\nd2_cluster done. saved",OUT,flush=True)
