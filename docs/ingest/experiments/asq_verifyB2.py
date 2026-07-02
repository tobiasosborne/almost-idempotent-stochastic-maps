#!/usr/bin/env python3
"""
Part 2: verify the EXPOSING MARGIN claim and the COLLAPSE claim numerically.

The exposedness definition (from the task): vertex v is (rho,kappa)-well-exposed
if EXISTS affine h:K->[0,1], h(v)=0, h >= kappa on rows rho-FAR from v.

Agent-B's certificate for p0 is y=(0,1,b,b): h(p0)=0, and on the OTHER rows the
values are y1=1, y2=b, y3=b.  The "rho-far" qualifier only DROPS constraints
(rows within rho of p0 need not satisfy h>=kappa). So the margin delivered is

   e_{p0}(rho) >= min over rows that are rho-far of h(p_i)
              >= min(1, b, b) restricted to far rows  >= b   (worst case all far)

So the claim e_{p0}>=b is: the value vector achieves min OTHER-row value = b
(if p2,p3 are far). We confirm min(y1,y2,y3) over the named cert = b. Good.

BUT: is h:K->[0,1] genuinely valued in [0,1] on ALL of K (the full hull),
not just at the four rows? An affine h on conv(rows) is determined by its values
at the rows; on the hull it's a convex combination so stays in
[min row value, max row value] = [0,1]. YES (affine = linear interpolation on a
polytope; values in [0,1] at all vertices => in [0,1] on hull). Confirmed.

Now the COLLAPSE bound and a full NUMERICAL exposedness LP to cross-check margins.
We build explicit P_t-style instances and measure the true LP exposedness margin
vs agent-B's closed-form lower bound.
"""
import numpy as np
from scipy.optimize import linprog

def make_P(a, cc, u):
    # v=(a, 1-a, -cc, -(1-cc)); u given (4-vector) but rescale so v^T u = 1
    v = np.array([a, 1-a, -cc, -(1-cc)], float)
    u = np.array(u, float)
    s = v @ u
    assert abs(s) > 1e-12
    u = u / s
    P = np.eye(4) - np.outer(u, v)
    return P, u, v

def neg_mass(P):
    return np.array([np.sum(np.maximum(-P[i], 0)) for i in range(P.shape[0])])

def l1(x,y): return np.sum(np.abs(x-y))

def dist_to_hull_l1(p, pts):
    # min_{lambda>=0, sum=1} ||p - sum lambda_k pts_k||_1
    pts = np.array(pts); m,n = pts.shape
    # vars: lambda (m), t (n) for |p - P^T lambda|
    nv = m + n
    c = np.concatenate([np.zeros(m), np.ones(n)])
    A_ub=[]; b_ub=[]
    for j in range(n):
        row=np.zeros(nv); row[:m]= -pts[:,j]; row[m+j]=-1; A_ub.append(row); b_ub.append(-p[j])
        row=np.zeros(nv); row[:m]=  pts[:,j]; row[m+j]=-1; A_ub.append(row); b_ub.append( p[j])
    A_eq=[np.concatenate([np.ones(m), np.zeros(n)])]; b_eq=[1.0]
    bnds=[(0,None)]*m+[(0,None)]*n
    r=linprog(c,A_ub=np.array(A_ub),b_ub=np.array(b_ub),A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=bnds,method='highs')
    return r.fun

def exposedness_margin(P, vidx, rho):
    # max t s.t. affine h(x)=w.x+w0, h(p_v)=0, 0<=h(p_i)<=1, h(p_i)>=t for far rows
    n=P.shape[1]; rows=[P[i] for i in range(P.shape[0])]
    pv=rows[vidx]
    far=[i for i in range(len(rows)) if i!=vidx and l1(rows[i],pv)>=rho]
    # vars: w (n), w0 (1), t(1)
    nv=n+2; ti=n+1
    c=np.zeros(nv); c[ti]=-1.0  # maximize t
    A_ub=[]; b_ub=[]
    # cap t<=1 (h in [0,1] => margin <=1 meaningful)
    rowT=np.zeros(nv); rowT[ti]=1; A_ub.append(rowT); b_ub.append(1.0)
    # h(p_i)<=1, -h(p_i)<=0 for all rows; for far rows -h(p_i)+t<=0
    for i,r in enumerate(rows):
        rowU=np.zeros(nv); rowU[:n]=r; rowU[n]=1; A_ub.append(rowU); b_ub.append(1.0)
        rowL=np.zeros(nv); rowL[:n]=-r; rowL[n]=-1; A_ub.append(rowL); b_ub.append(0.0)
    for i in far:
        r=rows[i]; rowF=np.zeros(nv); rowF[:n]=-r; rowF[n]=-1; rowF[ti]=1; A_ub.append(rowF); b_ub.append(0.0)
    # h(p_v)=0
    A_eq=[np.concatenate([pv,[1.0,0.0]])]; b_eq=[0.0]
    bnds=[(None,None)]*n+[(None,None),(None,None)]
    r=linprog(c,A_ub=np.array(A_ub),b_ub=np.array(b_ub),A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=bnds,method='highs')
    if not r.success: return None, far
    return -r.fun, far

print("=== test instances: agent-B P_t family + variants (genuinely small delta) ===")
# P_t: v=(1-t^2,t^2,-1+t^2,-t^2), u=(1,0,-t^2/(1-t^2),0). delta=t^2.
# generalized: v=(a,b,-c,-d) with a+b=c+d=1; choose u so neg is small. The P_t trick:
# put u mass only on a couple rows aligned to make neg(row)= small.
trials=[]
for t in [0.05,0.1,0.15,0.2,0.25]:
    a=1-t**2; cc=1-t**2
    u=np.array([1.0,0.0,-t**2/(1-t**2),0.0])
    trials.append((a,cc,u,t,'Pt'))
# asymmetric variant: a != c
for t in [0.1,0.2]:
    a=1-t**2; cc=1-2*t**2
    u=np.array([1.0,0.0,-t**2/(1-cc),0.0])
    trials.append((a,cc,u,t,'asym'))
for trial,(a,cc,u,t,tag) in enumerate(trials):
    P,u,v = make_P(a,cc,u)
    nm = neg_mass(P)
    delta=nm.max(); tau=np.sqrt(delta) if delta>0 else 0
    print(f"\ntrial {trial} [{tag} t={t}]: a={a:.4f} b={1-a:.4f} c={cc:.4f} d={1-cc:.4f}  maxneg(delta)={delta:.5f} tau={tau:.4f}")
    rows=[P[i] for i in range(4)]
    D=max(l1(rows[i],rows[j]) for i in range(4) for j in range(4))
    # agent-B closed-form margins:
    bcf = {'p0':1-a,'p1':a,'p2':1-cc,'p3':cc}
    rho = 4*tau if tau>0 else 0.0
    for vi,name in enumerate(['p0','p1','p2','p3']):
        m,far = exposedness_margin(P, vi, rho)
        mm = -1 if m is None else m
        print(f"  {name}: agentB lb={bcf[name]:.4f}  LP margin(rho=4tau)={mm:.4f}  #far={len(far)}")
    # collapse: dist(p0, conv{p2,p3}) vs (b/a) D
    d0=dist_to_hull_l1(rows[0],[rows[2],rows[3]]); print(f"  collapse: dist(p0,conv(p2,p3))={d0:.5f}  (b/a)*D={(1-a)/a*D:.5f}  D={D:.4f}")
