#!/usr/bin/env python3 -u
"""
d2_fixR.py -- Pin the archetype geometry R (so the plateau's realized ell^1
position is FIXED and cannot be re-coordinatized away), then solve for Lambda
(n x r, rows sum 1) with R Lambda = I_r minimizing delta = max-row-neg-mass(P),
P = Lambda R.  This is the correct way to force the plateau to be 'far'.

Why this is the right lever (from d2_plateau & d2_direct):
  - Negativity is NOT forced by signed ABSTRACT coords (R can hide it).
  - It IS forced when the realized rows must lie at prescribed ell^1 positions
    AND reproduce the idempotent structure R Lambda = I.
  So we FIX R = the realized archetype rows (their ell^1 geometry) and ask:
  can every row be a small-neg combination, or does some row's required position
  (far from conv W) force negativity?

Construction of R (r archetypes as honest probability rows in R^n, n>=r):
  - W archetypes (m of them): clean basis-like low vertices e_0..e_{m-1}.
  - 'pillar' archetypes (r-m): probability rows that are CONVEX-FAR from the W
    vertices (e.g. supported on fresh coordinates), so anything that must equal a
    pillar (or beyond it) is genuinely far in ell^1.
  Then we DEMAND plateau rows whose abstract Lambda coords push beyond the pillar
  (coord >1 on a pillar, negative elsewhere) so the realized row pokes out.

But here's the subtlety we proved: if we let Lambda be free with only R Lambda=I,
the optimizer may choose plateau rows to coincide with a pillar (abstract e_pillar,
neg-free). To force 'far + poking out + non-exposed' we must additionally PIN the
realized plateau rows p_i to TARGET positions t_i (chosen far from conv W). Then:
   p_i = Lambda[i,:] R = t_i  =>  Lambda[i,:] = t_i R^+ (on row space) and R Lambda=I.
This is now a LINEAR feasibility: given targets t_i in the flat span(R), solve.
The neg mass of p_i = neg mass of t_i (since p_i=t_i pinned!). So delta is just
max neg mass of the chosen targets. The question becomes: can targets t_i be
   (i) far from conv W (>= D tau), (ii) low neg mass (<= delta), (iii) in span(R),
   (iv) NON-well-exposed, AND (v) consistent with R Lambda=I for SOME completion?
The binding piece is R Lambda = I_r: the abstract coords Lambda[i,:]=t_i (R restricted)
of ALL rows must satisfy the biorthogonality with R. THIS couples the plateau to W.

We implement: choose R; choose target rows (W vertices + plateau targets + hosts);
the abstract coords are forced (Lambda[i,:] = barycentric coords of t_i wrt R,
unique since R rows aff. indep.); CHECK whether R Lambda = I_r holds; if not,
we must ADD/adjust rows. We measure the residual ||R Lambda - I|| -- the OBSTRUCTION.
"""
import sys, json
import numpy as np
from scipy.optimize import linprog
from d1_infra import check_idempotent, neg_mass, ratio_stats, check_factorization

OUT="out/d2_fixR.json"
res={"runs":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

def barycentric(t, R):
    """abstract coords lam s.t. lam R = t and lam.1=1 (unique since R rows aff indep,
       and t in affine span). Solve [R^T ; 1] lam = [t;1] least squares -> exact if in flat."""
    r,n=R.shape
    A=np.vstack([R.T, np.ones(r)])      # (n+1) x r
    b=np.concatenate([t,[1.0]])
    lam,*_=np.linalg.lstsq(A,b,rcond=None)
    resid=np.abs(A@lam-b).max()
    return lam, resid

def make_R(m_w, n_pillar, dim, seed=0):
    """r=m_w+n_pillar archetypes in R^dim. W archetypes = distinct basis vectors;
       pillars = distinct basis vectors on FRESH coords (so far in ell^1)."""
    r=m_w+n_pillar
    R=np.zeros((r,dim))
    for a in range(r):
        R[a,a]=1.0      # archetype a = e_a (clean prob vertex). all pairwise ell1 dist=2.
    return R

def attempt(m_w=2, n_pillar=1, plateau_targets=None, host_targets=None,
            label="", D=0.3):
    """
    R has r=m_w+n_pillar archetypes = e_0..e_{r-1} in R^dim, dim>=needed.
    Rows of P (targets t_i): the r archetypes themselves (so they're realized rows)
    + plateau targets + host targets. Abstract coords Lambda[i,:]=bary(t_i).
    W = {archetype rows 0..m_w-1}. Plateau pokes 'beyond' the pillar archetype.
    Then build Lambda from all targets and TEST R Lambda = I_r.
    """
    r=m_w+n_pillar
    nplat=len(plateau_targets or [D])
    n = r + nplat              # total rows = archetypes + plateau rows
    R=make_R(m_w,n_pillar,n)   # R is r x n  (each archetype = e_a in R^n)
    # base rows = the r archetypes
    targets=[R[a].copy() for a in range(r)]
    # plateau targets: poke beyond pillar (last archetype, index r-1).
    # 'beyond pillar' in the flat: lam = e_{r-1} + s*(e_{r-1}-e_0) = (-s,0..,1+s)
    #   => t = (1+s) R_{r-1} - s R_0. With R clean basis: t has -s on coord 0,
    #      1+s on coord r-1. neg mass = s. This is the FORCED negativity if pinned.
    plats=[]
    for s in (plateau_targets or [D]):
        lam=np.zeros(r); lam[r-1]=1+s; lam[0]=-s
        t=lam@R
        targets.append(t); plats.append(len(targets)-1)
    Lam=np.array([barycentric(t,R)[0] for t in targets])
    P=Lam@R
    fact=check_factorization(Lam,R)
    chk=check_idempotent(P)
    nm,delta=neg_mass(P)
    info={"label":label,"r":r,"n":n,"plats":plats,
          "RLambda_err":fact["RLambda_minus_I"],"fact_ok":fact["ok"],
          "idem_ok":chk["ok"],"delta":float(delta),"idem_resid":chk["idem_resid"]}
    if chk["ok"] and delta>1e-9:
        rs=ratio_stats(P,label=label); info.update(
            {"max_ratio":rs["max_ratio"],"tau":rs["tau"],"nW":rs["nW"],"W":rs["W"]})
    print(f"[{label}] RLam_err={fact['RLambda_minus_I']:.3e} idem_ok={chk['ok']} "
          f"idem_resid={chk['idem_resid']:.3e} delta={delta:.4e} "
          f"ratio={info.get('max_ratio','NA')}", flush=True)
    res["runs"].append(info); save()
    return info, Lam, R, P

if __name__=="__main__":
    print("="*70); print("d2_fixR: pin R, force plateau target, test R Lambda=I obstruction"); print("="*70, flush=True)
    for s in [0.1,0.3,0.6,1.0]:
        attempt(m_w=2,n_pillar=1,plateau_targets=[s],label=f"r3_s{s}")
    for s in [0.3,0.6]:
        attempt(m_w=3,n_pillar=1,plateau_targets=[s],label=f"r4_s{s}")
        attempt(m_w=2,n_pillar=2,plateau_targets=[s],label=f"r4p2_s{s}")
    print("\nKEY: read RLam_err. If !=0, the pinned plateau is INCONSISTENT with",flush=True)
    print("R Lambda=I unless we add rows -> that's the coupling/obstruction.",flush=True)
    print("d2_fixR done. saved",OUT,flush=True)
