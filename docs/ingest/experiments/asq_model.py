#!/usr/bin/env python3
"""
ASQ embedded model — does failed exposedness of BOTH high vertices force
max_i neg(p_i) >= c H^2 ?

We DIRECTLY MINIMIZE max-row-neg over exact retractions P whose rows realize an
anchored skinny quadrilateral with both high vertices H-far from conv W and both
failing (rho,kappa)-exposedness. If the minimum stays >= c H^2 with c>0 in the
small-tau regime, ASQ is supported; if we find a config with max-neg << H^2 and
genuine failed exposedness of both, ASQ is REFUTED (and we report the config).

Strategy: build a 2D barycentric-geometry instance (the canonical R=[I_r|0] family
makes rows = barycentric coords; ell1 row-distance = ell1 bary-distance; neg(row)=
ell1 mass outside simplex). Place:
  - r=3 archetypes e0,e1,e2 (a triangle); height = coordinate that is "up".
  Actually use a cleaner explicit 2D layout with an extra "height" archetype.

We instead use a CONCRETE small LP over exact P=Lambda R, R Lambda = I, with rows
pinned to a chosen geometry, minimizing max-row-neg, exactly as d3 did. Reuse d3
infra if importable; else self-contained.

Here: self-contained 'pinned-rows' minimization. Given target rows X (m x n), find
min over exact idempotents P with rows = X of max_i neg(p_i)? That's not well posed
(P's rows ARE X). Instead: the rows X themselves have fixed neg mass. The real
question is whether a geometry with both-failed-both-far can have SMALL neg AT ALL
while being realizable as rows of an exact idempotent.

So the actual experiment: search over exact idempotents P (any n), compute its rows,
its W, find configs where two row-vertices are H-far from conv W AND each fails
(rho,kappa)-exposedness, and record (H, max-neg). Look for max-neg << H^2.
This is the d3 hunt specialized to the 2-high-vertex anchored case. Reuse d3 bary
templates.
"""
import numpy as np
from scipy.optimize import linprog
import itertools, json

def neg_mass(P):
    return np.array([np.sum(np.maximum(-P[i],0)) for i in range(P.shape[0])])
def l1(x,y): return np.sum(np.abs(x-y))

def is_idempotent(P,tol=1e-7):
    return np.max(np.abs(P@P-P))<tol and np.max(np.abs(P.sum(1)-1))<tol

def dist_to_hull_l1(p, pts):
    pts=np.array(pts); m,n=pts.shape; nv=m+n
    c=np.concatenate([np.zeros(m),np.ones(n)])
    A_ub=[];b_ub=[]
    for j in range(n):
        r=np.zeros(nv); r[:m]=-pts[:,j]; r[m+j]=-1; A_ub.append(r); b_ub.append(-p[j])
        r=np.zeros(nv); r[:m]= pts[:,j]; r[m+j]=-1; A_ub.append(r); b_ub.append( p[j])
    A_eq=[np.concatenate([np.ones(m),np.zeros(n)])]; b_eq=[1.0]
    bnds=[(0,None)]*m+[(0,None)]*n
    r=linprog(c,A_ub=np.array(A_ub),b_ub=np.array(b_ub),A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=bnds,method='highs')
    return r.fun if r.success else np.inf

def exposed_margin(rows, vidx, rho):
    n=len(rows[0]); pv=rows[vidx]
    far=[i for i in range(len(rows)) if i!=vidx and l1(rows[i],pv)>=rho]
    if not far: return None
    nv=n+2; ti=n+1
    c=np.zeros(nv); c[ti]=-1.0
    A_ub=[];b_ub=[]
    A_ub.append(np.eye(nv)[ti]); b_ub.append(1.0)  # t<=1
    for r in rows:
        u=np.zeros(nv); u[:n]=r; u[n]=1; A_ub.append(u); b_ub.append(1.0)
        u=np.zeros(nv); u[:n]=-np.array(r); u[n]=-1; A_ub.append(u); b_ub.append(0.0)
    for i in far:
        u=np.zeros(nv); u[:n]=-np.array(rows[i]); u[n]=-1; u[ti]=1; A_ub.append(u); b_ub.append(0.0)
    A_eq=[np.concatenate([pv,[1.0,0.0]])]; b_eq=[0.0]
    bnds=[(None,None)]*(n)+[(None,None),(None,None)]
    r=linprog(c,A_ub=np.array(A_ub),b_ub=np.array(b_ub),A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=bnds,method='highs')
    return (-r.fun) if r.success else None

def is_vertex(rows, idx, tol=1e-7):
    # row idx is a vertex if it is NOT in conv of the geometrically-distinct OTHER rows
    others=[rows[j] for j in range(len(rows)) if j!=idx and l1(rows[j],rows[idx])>tol]
    if not others: return True
    return dist_to_hull_l1(rows[idx], others) > tol

def compute_W(rows, rho, kappa):
    W=[]
    for i in range(len(rows)):
        if not is_vertex(rows,i): continue
        m=exposed_margin(rows,i,rho)
        if m is not None and m>=kappa-1e-9: W.append(i)
    return W

# ---- Build embedded anchored skinny quadrilateral as canonical bary rows ----
# Archetypes: 3 of them -> 2-simplex (triangle). bary coords = points in triangle.
# Use coordinates in R^3 (bary), neg = mass below 0 in any coordinate.
# "height" = how far a vertex pokes outside the triangle (a negative coordinate)
# Low/anchor rows: inside triangle (neg 0). High vertices v1,v2: poke out by amount
# making them H-far from conv(W).
def bary_row(coords):  # coords sum to 1, can be negative
    return np.array(coords,float)

def build_instance(H, gap, side):
    """
    Triangle archetypes e0=(1,0,0),e1=(0,1,0),e2=(0,0,1).
    Anchor/low rows: a few interior points (neg 0) forming a low face W.
    High vertices: push outside edge e0-e1 in the -e2 direction-ish by amount ~H.
    Make them skinny (close together, separated by 'gap') and shadow each other.
    """
    rows=[]
    # archetypes (these are rows of identity block; neg 0)
    rows.append(bary_row([1,0,0]))
    rows.append(bary_row([1e-9,1,0]) if False else bary_row([0,1,0]))
    rows.append(bary_row([0,0,1]))
    # low anchors interior
    rows.append(bary_row([1/3,1/3,1/3]))
    rows.append(bary_row([0.4,0.4,0.2]))
    # two high vertices: poke out past edge (e0,e1) by making coord-2 negative ~ -H/2,
    # excess split into coords 0,1. height ~ |neg coord| controls distance.
    # v1, v2 close in (0,1) split, separated by gap.
    s=side
    v1=bary_row([0.5+s, 0.5+H/2-s, -H/2])
    v2=bary_row([0.5+s+gap, 0.5+H/2-s-gap, -H/2])
    rows.append(v1); rows.append(v2)
    return rows

if __name__=="__main__":
    print("=== sanity: a built instance, its neg, W, exposedness, distances ===")
    H=0.2; rows=build_instance(H, gap=0.02, side=0.0)
    P=None
    nm=np.array([np.sum(np.maximum(-r,0)) for r in rows])
    print("rows:");
    for i,r in enumerate(rows): print(f"  {i}: {np.round(r,4)}  neg={nm[i]:.4f}")
    delta=nm.max(); tau=np.sqrt(delta); rho=4*tau; kappa=tau/4
    print(f"delta={delta:.4f} tau={tau:.4f} rho={rho:.4f} kappa={kappa:.4f}")
    W=compute_W(rows,rho,kappa)
    print("W=",W)
    convW=[rows[i] for i in W] if W else None
    vi1, vi2 = 5,6
    for vi in (vi1,vi2):
        dW=dist_to_hull_l1(rows[vi],convW) if convW else np.inf
        m=exposed_margin(rows,vi,rho)
        print(f"  v{vi}: dist_to_convW={dW:.4f}  H?={dW:.4f}  margin={m}  fails(kappa={kappa:.4f})? {m is None or m<kappa}")
