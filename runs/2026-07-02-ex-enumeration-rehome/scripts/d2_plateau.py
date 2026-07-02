#!/usr/bin/env python3 -u
"""
d2_plateau.py -- The REAL hand-designed plateau test (Task 2).

GEOMETRIC PICTURE (established in d2_coupling).
  All n rows of P=Lambda R live in the (r-1)-flat = affine span of the r archetype
  rows R_1..R_r.  Via the affine iso  lambda -> lambda R  (rows of R aff. indep.),
  the ell^1 geometry of the rows equals the geometry of the ABSTRACT POINTS
  lambda_i in the simplex-plane {sum=1}, with metric ||(lambda_i-lambda_j)R||_1.
  R Lambda = I_r is biorthogonality: signed measures mu_a=R[a,:] satisfy
  <mu_a, phi_b> = delta_{ab}, phi_b = Lambda[:,b].

  P-row i = sum_a Lambda[i,a] R_a.  neg-mass(p_i) depends on R AND the signs of
  Lambda[i,:].

THE PLATEAU.  We want a group G of rows whose abstract points lie OUTSIDE
conv{abstract points of W} (so dist_1>0 after R), are NOT well-exposed, yet the
whole thing is an EXACT idempotent with small delta.  Since abstract points sum
to 1, being outside a sub-face conv(W) means some barycentric coordinate is <0
or >1 => SIGNED Lambda rows => negativity in P (unless R is chosen to hide it).

We make W a proper face: let r archetypes be A0..A_{r-1}. Let W = {A0,...,A_{m-1}}
(m<r exposed low vertices). The remaining archetypes A_m..A_{r-1} are 'pillars'
that are NOT exposed (hidden behind) and carry plateau height H. Plateau rows hang
off the pillars.

We sweep delta down and watch ratio(delta)=max_i dist1(p_i,convW)/tau.
A counterexample: ratio grows / stays >>1 as delta->0. Conjecture-consistent:
ratio = O(tau) or O(delta) (-> 0).

Crucially we let an OPTIMIZER (over R with rows-sum-1 and the biorthogonality
R Lambda=I, minimizing P's delta) find the BEST (lowest-delta) realization of a
given abstract plateau geometry, then read the ratio. This isolates: for a fixed
'far' abstract geometry, how small can delta be?
"""
import sys, json
import numpy as np
from scipy.optimize import linprog
from d1_infra import (check_idempotent, neg_mass, ratio_stats, check_factorization,
                      dist1_to_conv, well_exposed_set)

OUT="out/d2_plateau.json"
res={"runs":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

# ---------- given abstract Lambda, find R (rows sum1, R Lambda=I) minimizing P's delta ----------
def solve_R_min_P_delta(Lambda, w_neg=1.0):
    """Minimize the total negative mass of P = Lambda R over R subject to
       R Lambda = I_r and R rows sum to 1.  LP:
         vars: R flattened (r*n), and pos/neg split of P entries.
       P[i,j] = sum_a Lambda[i,a] R[a,j].  P entries are LINEAR in R. Good.
       Objective: minimize sum over (i,j) of negative part of P[i,j]
                  (== sum_i neg_mass(p_i) == total neg mass). We minimize the TOTAL;
                  to target the MAX neg mass per row we then re-solve minimizing max.
    """
    Lam=np.asarray(Lambda,float); n,r=Lam.shape
    # Unknowns: vec(R) length r*n  (R[a,j] -> index a*n+j), but R rows-sum-1 & RLambda=I.
    # Plus s[i,j] >= max(-P[i,j],0): s>=0, s>=-P[i,j]  -> P[i,j]+s[i,j]>=0.
    nR=r*n; nS=n*n; nv=nR+nS
    def Ridx(a,j): return a*n+j
    def Sidx(i,j): return nR + i*n + j
    # P[i,j] = sum_a Lam[i,a] R[a,j]  -> coefficients on R.
    c=np.zeros(nv); c[nR:]=1.0  # minimize sum of s (>= neg parts)
    A_ub=[]; b_ub=[]
    # P[i,j] + s[i,j] >= 0  -> -(P+s) <= 0
    for i in range(n):
        for j in range(n):
            row=np.zeros(nv)
            for a in range(r):
                row[Ridx(a,j)] -= Lam[i,a]   # -P coeff
            row[Sidx(i,j)] -= 1.0            # -s
            A_ub.append(row); b_ub.append(0.0)
    A_eq=[]; b_eq=[]
    # R Lambda = I:  sum_j R[a,j] Lam[j,b] = delta_{ab}
    for a in range(r):
        for b in range(r):
            row=np.zeros(nv)
            for j in range(n):
                row[Ridx(a,j)] += Lam[j,b]
            A_eq.append(row); b_eq.append(1.0 if a==b else 0.0)
    # R rows sum to 1: sum_j R[a,j] = 1
    for a in range(r):
        row=np.zeros(nv)
        for j in range(n): row[Ridx(a,j)]=1.0
        A_eq.append(row); b_eq.append(1.0)
    bounds=[(None,None)]*nR + [(0,None)]*nS
    rr=linprog(c,A_ub=np.array(A_ub),b_ub=np.array(b_ub),
               A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=bounds,method="highs")
    if not rr.success:
        return None
    R=rr.x[:nR].reshape(r,n)
    return R

# ---------- a parametric abstract plateau geometry ----------
def abstract_plateau(r=3, m=2, nplat=3, nlow=2, H=1.0, push=0.3, seed=0):
    """Build abstract Lambda (rows sum 1).
       Archetypes A0..A_{r-1} present as rows (Lambda row = e_a).
       W intended = {A0..A_{m-1}} (low exposed). Pillars A_m..A_{r-1} high.
       Plateau rows: poke OUT past the pillars using signed coords:
         coord on a pillar = 1+push, compensating negative on a low archetype.
       Low 'host' rows to receive negative mass: just the low archetypes.
    """
    rows=[]
    for a in range(r):
        e=[0.0]*r; e[a]=1.0; rows.append(e)   # archetypes as rows
    # plateau rows hang off pillar archetype index p=r-1, pushed outward
    p=r-1; low=0
    for k in range(nplat):
        e=[0.0]*r
        amt=push*(1+0.0*k)
        e[p]=1.0+amt
        e[low]=-amt
        rows.append(e)
    Lam=np.array(rows,float)
    return Lam

def run_case(r,m,nplat,H,push,delta_target=None,label=""):
    Lam=abstract_plateau(r=r,m=m,nplat=nplat,push=push)
    R=solve_R_min_P_delta(Lam)
    if R is None:
        print(f"[{label}] R solve FAILED", flush=True); return None
    P=Lam@R
    fact=check_factorization(Lam,R)
    chk=check_idempotent(P)
    nm,delta=neg_mass(P)
    info={"label":label,"r":r,"m":m,"nplat":nplat,"push":push,
          "fact_ok":fact["ok"],"idem_ok":chk["ok"],"delta":float(delta),
          "RLambda_err":fact["RLambda_minus_I"]}
    if delta>1e-9 and chk["ok"]:
        rs=ratio_stats(P,C=4.0,c=0.25,label=label)
        info["max_ratio"]=rs["max_ratio"]; info["nW"]=rs["nW"]; info["W"]=rs["W"]
        info["max_dist"]=rs["max_dist"]; info["tau"]=rs["tau"]
    else:
        info["note"]="delta=0 (degenerate: plateau collapses / R hides negativity)"
    print(f"[{label}] delta={delta:.4e} fact_ok={fact['ok']} idem_ok={chk['ok']} "
          f"ratio={info.get('max_ratio','NA')} nW={info.get('nW','NA')}", flush=True)
    res["runs"].append(info); save()
    return info, Lam, R, P

if __name__=="__main__":
    print("="*70); print("d2_plateau: forced negativity of a poking-out plateau"); print("="*70, flush=True)
    # min-delta realization of various plateau geometries
    for push in [0.1,0.3,0.6,1.0]:
        run_case(r=3,m=2,nplat=3,H=1.0,push=push,label=f"r3_push{push}")
    for push in [0.3,0.6]:
        run_case(r=4,m=2,nplat=4,H=1.0,push=push,label=f"r4_push{push}")
        run_case(r=4,m=3,nplat=4,H=1.0,push=push,label=f"r4m3_push{push}")
    for push in [0.3,0.6]:
        run_case(r=5,m=3,nplat=5,H=1.0,push=push,label=f"r5_push{push}")
    print("d2_plateau done. saved", OUT, flush=True)
