#!/usr/bin/env python3
r"""
Verify the QUANTITATIVE steps of the proposed ASQ proof (the 'height cap' argument).

PROOF SKELETON (to verify numerically step by step):

Notation: rho=C tau, kappa=c tau, C=4, c=1/4. diam_1(K)=:D <= 2+4delta. 'far' = ell1 dist >= rho.

Step 1 (lone-far-row, PROVED in d2): if dist_1(v, conv(rows\{v})) >= rho then v is
   (rho, rho/D)-well-exposed, hence in W (since rho/D = 4tau/(2+4delta) >= tau/4 = kappa
   for delta<=1/2... check: 4tau/(2+4*0.5)=4tau/4=tau >= tau/4. yes). CONTRAPOSITIVE:
   v failing (rho,kappa)-exposedness => dist_1(v, conv(rows\{v})) < rho  (a rho-shadow).

Step 2 (the height functional): Let g be the affine functional on K with ||g||_lip(ell1)<=1
   (i.e. g(x)=w.x, ||w||_inf<=1/... we use the ell1/ell-inf duality: any w with
   ||w||_inf<=1 gives |g(x)-g(y)|<=||x-y||_1). For v_j far from conv W by H:
        g(v_j) - sup_{conv W} g  <=  ||proj||... we instead DEFINE H via the BEST such g:
        H = dist_1(v_j, conv W) = max over ||w||_inf<=1 of [w.v_j - sup_{conv W} w.x].
   So there EXISTS g_j, ||g_j||_inf<=1, with g_j(v_j) - sup_{conv W} g_j = H_j >= H.

Step 3 (shadow has the OTHER high vertex with weight near 1): v_j has rho-shadow:
        v_j = sum_{i!=j} mu_i p_i + e_j, mu>=0 sum 1, ||e_j||_1 < rho.
   Apply g_j: H + sup_{cW}g_j <= g_j(v_j) = sum mu_i g_j(p_i) + g_j(e_j).
   Rows split into HIGH (the other high vertex v_k; g_j(v_k) <= g_j(v_j)) and the rest R
   (anchors/low/side) which are 'g_j-low': we will REQUIRE the anchored hypothesis to give
        g_j(p_i) <= sup_{conv W} g_j + rho   for every NON-high row p_i.        (ANCHOR)
   [Anchoring hypothesis A subset conv W ∪ low rows: the anchors are at g_j-height <= that of
    conv W up to the shadow scale rho. This is what 'anchored' must mean to be usable.]
   Let s_j = mu_{v_k} (weight on the other high vertex), m_lo=1-s_j on R-rows. Then
        g_j(v_j) <= s_j g_j(v_k) + (1-s_j)(sup_{cW}g_j + rho) + ||e_j||_1.
   Using g_j(v_j) >= H+sup g_j, g_j(v_k) <= sup_{cW}g_j + H_k' where H_k'=g_j(v_k)-sup g_j:
        H + S <= s_j(S+H_k') + (1-s_j)(S+rho) + rho       (S:=sup_{cW}g_j)
        H <= s_j H_k' + (1-s_j) rho + rho
   If both high vertices have the SAME height bound H (H_k' <= Hmax for the pair), and we
   look at the vertex achieving Hmax: H=Hmax, and g_j(v_k)<=Hmax too:
        Hmax <= s_j Hmax + (1-s_j)rho + rho
        Hmax(1-s_j) <= (2-s_j) rho  =>  Hmax <= (2-s_j)/(1-s_j) * rho.
   This BOUNDS Hmax by O(rho/(1-s_j)) -- but only if 1-s_j is bounded below. It is NOT
   (s_j can be ~1). So a SINGLE height pass does not cap H. NEED the SECOND vertex's relation
   to bound s_j away from 1, OR negativity. This is the crux the tautology exposed.

   *** The resolution (verified by numerics): the cap on Hmax comes from NEGATIVITY via the
   shadow direction. We verify the EMPIRICAL law Hmax <= K * tau (K~0.55 in d3, ~ but in the
   skinny pair with anchors we measure the constant) and hence delta=tau^2 >= (Hmax/K)^2.
   The clean provable surrogate: the two high vertices, each within rho of conv(others) and
   mutually shadowing, are within rho of EACH OTHER's side, so the pair is an O(rho)=O(tau)
   diameter cluster; its distance to the low face is bounded by its OWN neg mass (a vertex at
   ell1-distance d below the simplex has neg >= d/2). Combine: H=dist to low face, and
   neg >= H/2 gives delta >= H/2 => RATE H not H^2.  *** So which is it: H or H^2?
"""
import numpy as np
from scipy.optimize import linprog
from asq_model import l1, dist_to_hull_l1, exposed_margin, is_vertex, compute_W

# CRITICAL TEST: in the both-far-both-failing window, is delta ~ H or delta ~ H^2?
# Measure the EXPONENT p in delta ~ H^p along the failure boundary (largest depth that fails).
def neg_row(r): return np.maximum(-np.array(r),0).sum()
def make(depth, gap, anchors, side=0.0):
    rows=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
    for a in anchors: rows.append(np.array(a,float))
    v1=np.array([0.5+side, 0.5-side+depth, -depth])
    v2=np.array([0.5+side+gap, 0.5-side-gap+depth, -depth])
    rows.append(v1); rows.append(v2)
    return rows
def both_fail_far(rows,C=4.0,cc=0.25):
    nm=[neg_row(r) for r in rows]; delta=max(nm)
    if delta<=0: return None
    tau=np.sqrt(delta); rho=C*tau; kappa=cc*tau
    W=compute_W(rows,rho,kappa); convW=[rows[i] for i in W]
    i1,i2=len(rows)-2,len(rows)-1
    if not convW: return None
    d1=dist_to_hull_l1(rows[i1],convW); d2=dist_to_hull_l1(rows[i2],convW)
    m1=exposed_margin(rows,i1,rho); m2=exposed_margin(rows,i2,rho)
    f1=(m1 is None) or (m1<kappa-1e-9); f2=(m2 is None) or (m2<kappa-1e-9)
    v1,v2=is_vertex(rows,i1),is_vertex(rows,i2)
    H=min(d1,d2)
    ok = f1 and f2 and v1 and v2 and np.isfinite(H) and H>1e-9
    return dict(delta=delta,H=H,tau=tau,ok=ok,kappa=kappa,m1=m1,m2=m2)

anchors=[[1/3,1/3,1/3],[0.45,0.45,0.1],[0.2,0.6,0.2],[0.6,0.2,0.2]]
print("Boundary: largest depth at which BOTH still fail, per (effective) scale. Measure delta vs H.")
pts=[]
# the FAILURE boundary is depth ~ kappa scale. find max depth with ok=True, fine grid.
for target in np.linspace(0.01,0.1,40):
    rows=make(target, 0.05*target, anchors)
    r=both_fail_far(rows)
    if r and r['ok']:
        pts.append((r['H'],r['delta'],r['tau'],target))
import numpy as np
pts=np.array([(h,d,t,g) for (h,d,t,g) in pts])
if len(pts)>3:
    H=pts[:,0]; D=pts[:,1]
    # fit log D = p log H + b
    p,b=np.polyfit(np.log(H),np.log(D),1)
    print(f"fitted delta ~ H^p : p={p:.3f}  (p=1 => rate H; p=2 => rate H^2/ASQ)")
    print("sample (H, delta, delta/H^2, delta/H):")
    for h,d,t,g in pts[::max(1,len(pts)//8)]:
        print(f"  H={h:.4f} delta={d:.4f} delta/H^2={d/h**2:.2f} delta/H={d/h:.3f}")
