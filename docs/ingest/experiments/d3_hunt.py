#!/usr/bin/env python3 -u
"""
d3_hunt.py -- OPTIMIZATION HUNT (Task 3).

We optimize over EXACT idempotents P=Lambda R (R Lambda=I_r, rows sum 1) to
MAXIMIZE the REAL tau-scaled ratio  max_i dist1(p_i, conv W)/tau,  with tau=sqrt(delta)
where delta = max-row-neg-mass(P).  A counterexample signature: ratio grows as
delta shrinks, or ratio >> 1 robustly.  O(tau)/O(delta) ratios (ratio->0) are
conjecture-consistent.

Approach:
  - Free variables: Lambda (n x r) and R (r x n).
  - Hard constraints: R Lambda = I_r ; R rows sum 1 ; Lambda rows sum 1.
    We enforce by an augmented-Lagrangian / penalty inside a smooth objective, OR
    we PARAMETRIZE the constraint manifold:
       Given Lambda (n x r) full col rank with rows summing to 1, the MINIMAL-norm
       R with R Lambda=I and rows-sum-1 is  R = (Lambda^+ ) adjusted; but we want
       R free too. We instead use penalty on (R Lambda - I), rowsum residuals.
  - The objective (ratio) is itself an LP-defined max over rows of an LP value;
    nonsmooth. We use a SURROGATE: pick a target row index t and maximize
    dist1(p_t, conv W)/tau via finite-difference / Nelder-Mead from many
    structured starts, recomputing W (an LP) each eval. Expensive but robust.

Because the inner W computation is discrete (set membership), we use a black-box
optimizer (scipy differential_evolution / Nelder-Mead) on a modest parametrization
and just SCAN; the goal is to find the BEST achievable ratio vs delta and report
the scaling, not a slick solver.

We multistart from:
  (s1) staircase heights 2^-m D tau,
  (s2) near-circuit configs (from d2_hide) realized as exact idempotents,
  (s3) perturbed Baake-Sumner idempotents with transient rows pushed off-hull.
and record ratio(delta) for delta in {1e-1,1e-2,1e-3,1e-4} via rescaling.
"""
import sys, json, time
import numpy as np
from scipy.optimize import linprog, minimize
from d1_infra import (check_idempotent, neg_mass, ratio_stats, check_factorization,
                      well_exposed_set, dist1_to_conv)

OUT="out/d3_hunt.json"
res={"scaling":[], "best":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

# ---------- exact-idempotent projector: given free Lambda, get R via min-norm ----------
def R_from_Lambda(Lam):
    """Min-Frobenius R with R Lambda=I_r and R rows sum 1.
       R Lambda=I: R = A Lambda^+ + N where rows of N in left-null(Lambda).
       Simplest valid: R = pinv(Lambda^T)... we want R (r x n), R Lambda=I_r.
       That's R = (Lambda^+), the Moore-Penrose pinv of Lambda (since Lambda^+ Lambda=I
       for full col rank). And does R have rows summing to 1?  R 1_n = Lambda^+ 1_n,
       not generally 1_r. We fix rowsum by adding a correction in the null space:
       any R0+C with C Lambda=0 keeps idempotence; choose C to fix rowsums.
       Left null space of Lambda: vectors x (1 x n) with x Lambda=0. We solve a
       small LS to set rowsums to 1 while keeping C Lambda=0. For simplicity, we
       accept that exactness (R Lambda=I) is the load-bearing constraint and FIX
       P1=1 separately by noting: P1=Lambda R 1. If R rows sum to 1 then R1=1_r and
       P1=Lambda 1_r=1 (Lambda rows sum 1). So we DO need R rowsum=1.
    """
    Lam=np.asarray(Lam,float); n,r=Lam.shape
    Rp=np.linalg.pinv(Lam)            # r x n, Rp Lambda = I_r (full col rank)
    # fix rowsums: want (Rp+C)1 = 1_r with C Lambda=0.
    # Basis for left-null(Lambda): rows orthogonal to range(Lambda). Project.
    # We solve: find C (r x n) minimal with C Lambda=0 and (Rp+C)1=1.
    # Parametrize C = D (I - Lambda Lambda^+)  for D (r x n): then C Lambda = D(Lambda-Lambda)=0. good.
    Proj = np.eye(n) - Lam@np.linalg.pinv(Lam)   # projects onto left-null cols
    one=np.ones(n)
    # want (Rp + D Proj) 1 = 1_r  -> D Proj 1 = 1_r - Rp 1
    b = 1.0 - Rp@one                  # r-vector
    pv = Proj@one                     # n-vector
    denom = pv@pv
    if denom<1e-12:
        # cannot fix rowsum in null space; return Rp (rowsum may be off)
        return Rp, float(np.abs(Rp@one-1).max())
    D = np.outer(b, pv)/denom         # r x n
    R = Rp + D@Proj
    return R, 0.0

def eval_ratio(Lam, C=4.0, c=0.25):
    Lam=np.asarray(Lam,float); n,r=Lam.shape
    R,_=R_from_Lambda(Lam)
    P=Lam@R
    chk=check_idempotent(P,tol=1e-7)
    if not chk["ok"]:
        return None
    nm,delta=neg_mass(P)
    if delta<1e-12:
        return {"delta":0.0,"ratio":0.0,"P":P}
    rs=ratio_stats(P,C=C,c=c)
    return {"delta":float(delta),"tau":rs["tau"],"ratio":rs["max_ratio"],
            "nW":rs["nW"],"P":P}

# ---------- structured starts ----------
def start_staircase(r=4, levels=3, n_extra=4, scale=0.3, seed=0):
    rng=np.random.default_rng(seed)
    rows=[]
    for a in range(r):
        e=[0.0]*r; e[a]=1.0; rows.append(e)
    # staircase plateau rows: signed coords with 2^-m heights
    for m in range(levels):
        h=scale*2.0**(-m)
        e=[0.0]*r; e[r-1]=1+h; e[0]=-h; rows.append(e)
    for _ in range(n_extra):
        e=rng.standard_normal(r); e-= (e.sum()-1)/r; rows.append(list(e))
    return np.array(rows,float)

def start_circuit(r=3, K=6, scale=0.3, seed=0):
    rng=np.random.default_rng(seed)
    rows=[]
    for a in range(r):
        e=[0.0]*r; e[a]=1.0; rows.append(e)
    for k in range(K):
        th=2*np.pi*k/K
        e=np.zeros(r); e[r-1]=1+scale
        e[0]= -scale*0.5*(1+np.cos(th));
        if r>2: e[1]= -scale*0.5*(1+np.sin(th))
        e -= (e.sum()-1)/r
        rows.append(list(e))
    return np.array(rows,float)

def hunt(start_fn, name, scales, C=4.0, c=0.25, maxiter=200):
    best=None
    for sc in scales:
        Lam0=start_fn(scale=sc)
        n,r=Lam0.shape
        # black-box over Lambda entries (keep rows summing to 1 by projection)
        def project_rows(x):
            L=x.reshape(n,r).copy()
            L -= (L.sum(axis=1,keepdims=True)-1)/r
            return L
        def negobj(x):
            L=project_rows(x)
            out=eval_ratio(L,C=C,c=c)
            if out is None: return 1.0   # infeasible idempotent -> penalize
            return -out["ratio"]
        x0=Lam0.flatten()
        r0=eval_ratio(project_rows(x0),C=C,c=c)
        try:
            rr=minimize(negobj,x0,method="Nelder-Mead",
                        options={"maxiter":maxiter,"xatol":1e-4,"fatol":1e-4})
            Lbest=project_rows(rr.x); ob=eval_ratio(Lbest,C=C,c=c)
        except Exception as e:
            ob=r0; Lbest=project_rows(x0)
        cand = ob if ob else r0
        if cand and (best is None or cand["ratio"]>best["ratio"]):
            best={"name":name,"scale":sc,"delta":cand["delta"],
                  "ratio":cand["ratio"],"tau":cand.get("tau"),
                  "Lambda":Lbest.tolist()}
        print(f"[{name} sc={sc}] start_ratio={r0['ratio'] if r0 else None:.4f} "
              f"opt_ratio={cand['ratio']:.4f} delta={cand['delta']:.3e}", flush=True)
    res["best"].append(best); save()
    return best

if __name__=="__main__":
    print("="*70); print("d3_hunt: optimization hunt for high tau-scaled ratio"); print("="*70, flush=True)
    hunt(lambda scale,seed=0: start_staircase(r=4,levels=3,n_extra=4,scale=scale,seed=seed),
         "staircase", scales=[0.1,0.2,0.4,0.8])
    hunt(lambda scale,seed=0: start_circuit(r=3,K=6,scale=scale,seed=seed),
         "circuit3", scales=[0.1,0.2,0.4,0.8])
    hunt(lambda scale,seed=0: start_circuit(r=4,K=8,scale=scale,seed=seed),
         "circuit4", scales=[0.1,0.2,0.4,0.8])
    print("\nBEST overall:", flush=True)
    for b in res["best"]:
        if b: print(f"  {b['name']}: ratio={b['ratio']:.4f} delta={b['delta']:.3e}", flush=True)
    save()
    print("d3_hunt done.",flush=True)
