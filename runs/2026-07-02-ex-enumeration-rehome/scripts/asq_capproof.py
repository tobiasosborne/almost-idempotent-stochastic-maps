#!/usr/bin/env python3
r"""
RIGOROUS CAP CHAIN for ASQ. Verify each inequality numerically; mark PROVED/SKETCH.

The honest mechanism (revised after measuring delta=H/2, H<=0.5 tau):

LEMMA CAP (the real engine):  H = dist_1(v_j, conv W) <= rho = C tau.
Proof attempt: v_j fails (rho,kappa)-exposedness. We want to show H<=rho directly.
Suppose H = dist_1(v_j, conv W) > rho. We derive that v_j IS (rho,kappa)-exposed,
contradiction. By the d2 lone-far-row construction applied to the SET conv W (a convex
set, not a single row): if dist_1(v_j, conv W) = H, there is g, ||g||_inf<=1, with
   g(v_j) - sup_{conv W} g >= H.
Define h(x) = (g(v_j)-g(x))/(M-m) where M=g(v_j), m=min_K g. Then h(v_j)=0, h:K->[0,1],
and for any row p_i in conv W: h(p_i) >= (g(v_j)-sup_{cW}g)/(M-m) >= H/(M-m) >= H/D.
BUT exposedness needs h>=kappa on all rho-FAR rows, not just rows in conv W. A far row NOT
in conv W could have small h. So this exposes v_j against conv-W rows but maybe not against
the OTHER high vertex v_k (which is far and NOT in conv W).
=> The exposedness can only FAIL because of v_k (and possibly low rows not in conv W within
the rho-far set). For the ANCHORED skinny pair: the only non-conv-W far rows are v_k (high)
and any low rows excluded from W. If anchoring puts all low rows in conv W, the ONLY
obstruction to exposing v_j is v_k. Then 'v_j fails' <=> h(v_k) < kappa for EVERY valid h,
in particular for the h above => h(v_k) < kappa.

Now h(v_k) < kappa means g(v_k) > g(v_j) - kappa(M-m) >= g(v_j) - kappa D. So v_k is nearly
as g-high as v_j: g(v_j)-g(v_k) < kappa D = (c tau)(<=2+4delta) = O(tau). The two high
vertices are g-close. SYMMETRICALLY (failing v_k) gives the same. So the pair is an
O(tau)-tall, mutually-g-close cluster sitting H above conv W.

THE COST: v_j is a vertex (extreme), at g-height >= sup_{cW} g + H, with v_k the only other
row near that height. v_j's rho-shadow writes v_j = mu_k v_k + (1-mu_k) L + e, L in conv(low),
||e||<rho. Apply g: g(v_j) = mu_k g(v_k) + (1-mu_k) g(L) + g(e).
g(L) <= sup_{cW} g (L is low). g(v_k) <= g(v_j). g(e)<=||e||<rho. So
  g(v_j) <= mu_k g(v_j) + (1-mu_k) sup_{cW}g + rho
  (1-mu_k)(g(v_j)-sup g) <= rho  => (1-mu_k) H <= rho  => mu_k >= 1 - rho/H.   (LEAN, exact)
So v_j leans on v_k with weight >= 1-rho/H. If H>rho this is positive.

Now the NEGATIVITY. v_j and v_k are rows. Consider the affine functional that is NEGATIVE
mass detector. KEY EXACTNESS INPUT: in the canonical frame the archetypes e_0..e_{r-1} are
rows in W (they are isolated unit vectors, trivially exposed). v_j's bary coords have a
NEGATIVE entry (that's its neg mass). The ell1 distance from v_j to the simplex (= conv of
archetypes subset of conv W) equals 2*neg(v_j) (a point with neg coordinate -p and the rest
summing to 1+p has ell1 distance 2p to the simplex). So
   dist_1(v_j, conv W) <= dist_1(v_j, simplex) = 2 neg(v_j) <= 2 delta.    (NEG-DIST)
Wait that gives H <= 2 delta, i.e. delta >= H/2. RATE H again, the trivial bound.
Combined with the CAP H<=rho=4tau=4 sqrt(delta):  H<=4 sqrt(delta) => delta >= H^2/16.
*** THAT IS ASQ: delta >= H^2/16, c=1/16 (max-neg units). ***
The cap H<=rho is the exposedness fact; NEG-DIST H<=2delta is the geometry fact; the BINDING
one for small H is the cap (H^2/16), giving the H^2 rate. Both hold; ASQ uses the cap.

Let me verify: (i) NEG-DIST: dist_1(v,simplex)=2 neg(v) for a vertex with one neg coord.
(ii) CAP: H = dist_1(v_j,conv W) <= rho whenever v_j fails (rho,kappa)-exposedness AND the
only far non-W rows are the other high vertex / handled. Test the cap empirically: is
H <= rho ALWAYS in the both-failing window?  (we measured H~0.1, rho~0.9: YES H<<rho.)
"""
import numpy as np
from scipy.optimize import linprog
from asq_model import l1, dist_to_hull_l1, exposed_margin, is_vertex, compute_W

def neg_row(r): return np.maximum(-np.array(r),0).sum()
def make(depth, gap, anchors, side=0.0):
    rows=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
    for a in anchors: rows.append(np.array(a,float))
    v1=np.array([0.5+side, 0.5-side+depth, -depth]); v2=np.array([0.5+side+gap, 0.5-side-gap+depth, -depth])
    rows.append(v1); rows.append(v2); return rows

print("=== (i) NEG-DIST: dist_1(v, simplex) vs 2*neg(v) ===")
simplex=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
for depth in [0.05,0.1,0.2,0.3]:
    v=np.array([0.5,0.5+depth,-depth])
    d=dist_to_hull_l1(v,simplex); n=neg_row(v)
    print(f"  depth={depth}: dist_1(v,simplex)={d:.4f}  2*neg(v)={2*n:.4f}  equal? {abs(d-2*n)<1e-6}")

print("\n=== (ii) CAP: in both-failing window, is H <= rho? and H <= 2 delta? ===")
anchors=[[1/3,1/3,1/3],[0.45,0.45,0.1],[0.2,0.6,0.2],[0.6,0.2,0.2]]
for depth in [0.02,0.04,0.06,0.08,0.1,0.12]:
    rows=make(depth,0.05*depth,anchors)
    nm=[neg_row(r) for r in rows]; delta=max(nm); tau=np.sqrt(delta); rho=4*tau; kappa=tau/4
    W=compute_W(rows,rho,kappa); convW=[rows[i] for i in W]
    i1=len(rows)-2; d1=dist_to_hull_l1(rows[i1],convW) if convW else np.inf
    m1=exposed_margin(rows,i1,rho)
    fails=(m1 is None) or (m1<kappa-1e-9)
    print(f"  depth={depth}: H={d1:.4f} rho={rho:.4f} 2delta={2*delta:.4f} fails={fails} "
          f"H<=rho?{d1<=rho+1e-9} H<=2delta?{d1<=2*delta+1e-9} delta/H^2={delta/d1**2 if d1>0 else float('nan'):.2f}")

print("\n=== combined bound: delta >= H^2/16 (cap) and delta>=H/2 (negdist). check both hold ===")
for depth in [0.02,0.04,0.06,0.08,0.1,0.12]:
    rows=make(depth,0.05*depth,anchors)
    nm=[neg_row(r) for r in rows]; delta=max(nm); tau=np.sqrt(delta); rho=4*tau; kappa=tau/4
    W=compute_W(rows,rho,kappa); convW=[rows[i] for i in W]
    i1=len(rows)-2; H=dist_to_hull_l1(rows[i1],convW) if convW else np.inf
    if np.isfinite(H) and H>0:
        print(f"  depth={depth}: delta={delta:.4f}  H^2/16={H**2/16:.5f}  H/2={H/2:.4f}  "
              f"delta>=H^2/16?{delta>=H**2/16-1e-9}  delta>=H/2?{delta>=H/2-1e-9}")
