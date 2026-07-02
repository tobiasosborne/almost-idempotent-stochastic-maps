#!/usr/bin/env python3
r"""
The COUPLED 2x2 shadow algebra, done exactly, to close (or expose the gap in) the CAP.

Setup (embedded, anchored). Rows = {v1, v2} U A, where A = anchor/low rows with
dist_1(a, conv W) <= eta for all a in A   (ANCHORING, eta = O(rho); for A subset conv W, eta=0).
W contains enough of A's hull that conv W approximates conv A.

Each high vertex fails (rho,kappa)-exposedness => d2 contrapositive => rho-shadow:
   v1 = mu1*v2 + (1-mu1)*L1 + e1,   L1 in conv A,  ||e1||_1 < rho,  mu1 in [0,1]
   v2 = mu2*v1 + (1-mu2)*L2 + e2,   L2 in conv A,  ||e2||_1 < rho,  mu2 in [0,1]
(the shadow of v1 is a convex combo of the OTHER rows = v2 and A-rows; group A-mass into L1.)

Goal: bound dist_1(v1, conv A) =: H1 (and H = dist to conv W <= H1 + eta).
From the two relations, eliminate v2:
   v1 = mu1(mu2 v1 + (1-mu2)L2 + e2) + (1-mu1)L1 + e1
   v1(1-mu1 mu2) = mu1(1-mu2)L2 + (1-mu1)L1 + mu1 e2 + e1
   v1 = [mu1(1-mu2)L2+(1-mu1)L1]/(1-mu1mu2) + [mu1 e2+e1]/(1-mu1mu2)
First bracket: convex combo of A-rows (coeffs sum to 1). Call it Lbar in conv A.
   => v1 = Lbar + Ebar,  Ebar=[mu1 e2+e1]/(1-mu1mu2),  ||Ebar||_1 <= (mu1+1)rho/(1-mu1mu2).
   => H1 = dist_1(v1,conv A) <= ||v1-Lbar||_1 = ||Ebar||_1 <= (1+mu1)rho/(1-mu1mu2).   (*)

PROBLEM: if mu1,mu2 -> 1, (1-mu1mu2)->0 and (*) is VACUOUS (RHS->inf). So the pure shadow
algebra does NOT cap H1 -- EXACTLY the tautology found before. The cap must come from
elsewhere. Candidates to break the mu->1 degeneracy:
  (G) GEOMETRY/NEG: mu1->1 means v1 ~ v2 (v1 is ~ a copy of v2 up to e1<rho). Then v1,v2
      coincide within rho => they are NOT two distinct vertices at the (rho,kappa) scale =>
      the 'skinny quadrilateral' degenerates to a near-segment; one of them is non-vertex /
      they merge in W-computation. So the regime mu->1 is the COINCIDENT-ROW degeneracy d3
      warned about; excluding it (distinct vertices, ||v1-v2||>= some gap g) bounds mu away
      from 1:  ||v1 - v2||_1 >= g  and v1 = mu1 v2 + (1-mu1)L1 + e1 =>
         ||v1-v2|| = ||(mu1-1)v2+(1-mu1)L1+e1|| <= (1-mu1)||v2-L1|| + rho
         => g <= (1-mu1) D + rho  => 1-mu1 >= (g-rho)/D.   (needs g>rho to be useful!)
      But skinny means g SMALL (the quadrilateral is thin) -- g<rho is the whole point. So
      this does NOT save it either: skinny + both-failing => mu->1 => (*) vacuous.

CONCLUSION (honest): the CAP via shadow-composition is GENUINELY not closed by convex algebra;
the H^2 cost in the canonical numerics comes from INEQ A (frame: H<=2 neg), which is
FRAME-SPECIFIC. In an arbitrary module without the simplex-frame, the shadow route leaves a
real gap precisely in the skinny/mutual-shadow degenerate regime. This is the SAME gap the
d4 note calls 'dual-localization' (the alpha-mass on the high zero-face).

So ASQ is: PROVED in the canonical simplex-frame (INEQ A, even gives rate H, hence c=1/2 and
the H^2 form a fortiori, with H capped by the exposedness window). NOT proved transferably
(the mutual-shadow degeneracy is the open dual-localization gap). We verify the dividing line:
measure mu1 at the optimum and confirm it -> 1 (degenerate) exactly where (*) goes vacuous.
"""
import numpy as np
from scipy.optimize import linprog
from asq_model import l1, dist_to_hull_l1

def neg_row(r): return np.maximum(-np.array(r),0).sum()
def make(depth, gap, anchors):
    rows=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
    for a in anchors: rows.append(np.array(a,float))
    rows.append(np.array([0.5, 0.5+depth, -depth]))
    rows.append(np.array([0.5+gap, 0.5-gap+depth, -depth]))
    return rows

def shadow_decomp(v, others):
    # find convex combo of 'others' closest to v in ell1; return weights and residual norm
    others=np.array(others); m,n=others.shape; nv=m+n
    c=np.concatenate([np.zeros(m),np.ones(n)])
    A_ub=[];b_ub=[]
    for j in range(n):
        r=np.zeros(nv); r[:m]=-others[:,j]; r[m+j]=-1; A_ub.append(r); b_ub.append(-v[j])
        r=np.zeros(nv); r[:m]= others[:,j]; r[m+j]=-1; A_ub.append(r); b_ub.append( v[j])
    A_eq=[np.concatenate([np.ones(m),np.zeros(n)])]; b_eq=[1.0]
    res=linprog(c,A_ub=np.array(A_ub),b_ub=np.array(b_ub),A_eq=np.array(A_eq),b_eq=np.array(b_eq),
                bounds=[(0,None)]*m+[(0,None)]*n,method='highs')
    w=res.x[:m]; return w, res.fun

anchors=[[1/3,1/3,1/3],[0.45,0.45,0.1],[0.2,0.6,0.2],[0.6,0.2,0.2]]
print("Measure mu1 = weight on v2 in v1's shadow decomposition (does it -> 1 = degenerate?):")
for depth,gap in [(0.02,0.001),(0.04,0.002),(0.06,0.003),(0.06,0.03),(0.06,0.1)]:
    rows=make(depth,gap,anchors)
    i1,i2=len(rows)-2,len(rows)-1
    others=[rows[j] for j in range(len(rows)) if j!=i1]
    w,resid=shadow_decomp(rows[i1],others)
    mu_on_v2 = w[i2-1] if i2>i1 else w[i2]  # index of v2 within 'others'
    # 'others' list excludes i1; v2 is last element
    mu_on_v2 = w[-1]
    gapdist=l1(rows[i1],rows[i2])
    print(f"  depth={depth} gap={gap}: ||v1-v2||={gapdist:.4f} mu_on_v2={mu_on_v2:.4f} "
          f"shadow_resid={resid:.5f}  (mu->1 & gap small => degenerate, (*) vacuous)")
