#!/usr/bin/env python3
"""fastpipe.py -- FLOAT (scipy) mirror of pipeline.py for FAST search only.
   NOT a certificate: every reported result must be re-verified exactly with
   pipeline.py.  Same operational defs (delta, (rho,kappa)-exposedness t*, W,
   dist_1(.,convW), height H, invisible mass sigma~), tol-based decisions."""
import numpy as np
from scipy.optimize import linprog

TOL = 1e-9

def delta_f(P):
    return float(np.max(np.sum(np.maximum(-P,0.0),axis=1)))

def l1(a,b):
    return float(np.sum(np.abs(a-b)))

def is_row_vertex(P,i):
    n=len(P); v=P[i]
    others=[k for k in range(n) if k!=i and l1(P[k],v)>1e-12]
    if not others: return True
    m=len(others); d=n
    # min sum t s.t. sum lam_k A_k - v = r, -t<=r<=t, lam>=0 sum=1
    nv=m+d
    c=np.zeros(nv); c[m:]=1.0
    A_ub=[]; b_ub=[]
    for j in range(d):
        rp=np.zeros(nv)
        for kk in range(m): rp[kk]=P[others[kk]][j]
        rp[m+j]=-1.0; A_ub.append(rp); b_ub.append(v[j])
        rn=np.zeros(nv)
        for kk in range(m): rn[kk]=-P[others[kk]][j]
        rn[m+j]=-1.0; A_ub.append(rn); b_ub.append(-v[j])
    A_eq=[np.concatenate([np.ones(m),np.zeros(d)])]; b_eq=[1.0]
    bounds=[(0,None)]*m+[(0,None)]*d
    try:
        r=linprog(c,A_ub=np.array(A_ub),b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=bounds,method="highs")
    except Exception:
        return True
    if not r.success: return True
    return r.fun>1e-7

def exposed_tstar(P,i,dval):
    n=len(P); d=n
    di=np.array([l1(P[k],P[i]) for k in range(n)])
    rho=4.0*np.sqrt(dval)
    far=[k for k in range(n) if k!=i and di[k]>=rho-1e-12]
    if not far: return None
    nv=d+1+1
    c=np.zeros(nv); c[-1]=-1.0
    A_ub=[]; b_ub=[]
    def hvec(k):
        row=np.zeros(nv); row[:d]=P[k]; row[d]=1.0; return row
    for k in range(n):
        hk=hvec(k); A_ub.append(hk.copy()); b_ub.append(1.0)
        A_ub.append(-hk); b_ub.append(0.0)
    for k in far:
        row=-hvec(k); row[-1]=1.0; A_ub.append(row); b_ub.append(0.0)
    A_eq=[hvec(i)]; b_eq=[0.0]
    bounds=[(None,None)]*(d+1)+[(None,1.0)]
    try:
        r=linprog(c,A_ub=np.array(A_ub),b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=bounds,method="highs")
    except Exception:
        return 0.0
    if not r.success: return 0.0
    return -r.fun

def visible_set(P,dval):
    n=len(P); W=[]; info={}
    kappa=np.sqrt(dval)/4.0
    for i in range(n):
        if not is_row_vertex(P,i):
            info[i]={"vertex":False}; continue
        ts=exposed_tstar(P,i,dval)
        if ts is None:
            info[i]={"vertex":True,"tstar":None,"exposed":True}; W.append(i)
        else:
            exp=ts>=kappa-1e-12
            info[i]={"vertex":True,"tstar":ts,"exposed":exp}
            if exp: W.append(i)
    return W,info

def dist1_to_conv(P,W,i):
    n=len(P); d=n
    if not W: return None
    v=P[i]; m=len(W); nv=m+d
    c=np.zeros(nv); c[m:]=1.0
    A_ub=[]; b_ub=[]
    for j in range(d):
        rp=np.zeros(nv)
        for kk in range(m): rp[kk]=P[W[kk]][j]
        rp[m+j]=-1.0; A_ub.append(rp); b_ub.append(v[j])
        rn=np.zeros(nv)
        for kk in range(m): rn[kk]=-P[W[kk]][j]
        rn[m+j]=-1.0; A_ub.append(rn); b_ub.append(-v[j])
    A_eq=[np.concatenate([np.ones(m),np.zeros(d)])]; b_eq=[1.0]
    bounds=[(0,None)]*m+[(0,None)]*d
    try:
        r=linprog(c,A_ub=np.array(A_ub),b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=bounds,method="highs")
    except Exception:
        return None
    if not r.success: return None
    return r.fun

def analyze_f(P):
    P=np.array(P,dtype=float); n=len(P)
    dval=delta_f(P)
    if dval<1e-12: return None
    W,info=visible_set(P,dval)
    if not W: return None
    dists=[dist1_to_conv(P,W,i) for i in range(n)]
    dists=[dd if dd is not None else 0.0 for dd in dists]
    H=max(dists)
    outside=[j for j in range(n) if dists[j]>1e-9]
    sigt=[float(np.sum(np.maximum(P[v][outside],0.0))) if outside else 0.0 for v in range(n)]
    # genuine-recipient invisible mass: recipients at dist >= tau/4 (halo-robust, self excluded when close)
    tau=np.sqrt(dval); thr=tau/4.0
    genuine=[j for j in range(n) if dists[j]>=thr-1e-12]
    sigt_g=[float(np.sum(np.maximum(P[v][genuine],0.0))) if genuine else 0.0 for v in range(n)]
    hidden=[i for i in range(n) if info.get(i,{}).get("vertex") and not info.get(i,{}).get("exposed")]
    return dict(delta=dval,W=W,dists=dists,H=H,sigt=sigt,sigt_g=sigt_g,hidden=hidden,info=info)
