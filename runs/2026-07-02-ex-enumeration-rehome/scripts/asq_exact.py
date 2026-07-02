#!/usr/bin/env python3
r"""
Where does H^2 come from? Pin the relation between H=dist_1(v,conv W), the shadow rho,
and neg mass, using the EXACT canonical bary family. Two competing scalings:
  (a) H ~ neg          => delta ~ H, NOT H^2  (would REFUTE the H^2 form; rate would be H)
  (b) H ~ sqrt(neg)=tau => delta ~ H^2        (ASQ form)
The d3 report claims (b): dist/tau <= ~0.54 i.e. H <= 0.54 tau i.e. delta=tau^2 >= (H/0.54)^2.
So d3 says H is bounded by O(tau), i.e. you CANNOT get H much bigger than tau. The H^2 is
because the FAR distance H is itself capped at O(tau), and tau^2=delta. That is: it is not
that 'a height-H config costs H^2'; it is that 'you cannot make a row H-far from conv W
without delta >= (H/0.54)^2', BECAUSE far vertices EXPOSE (join W) unless dragged back by neg.

The single high vertex story: a vertex poking out by depth p has neg ~ p, dist to the
LOW face ~ p, BUT it is (rho,kappa)-EXPOSED (lone-far-row lemma) as soon as its shadow
> rho = 4 tau. So to keep it OUT of W (far from conv W) while far, you need shadow <= rho,
i.e. it must be within rho=4 tau of conv(other rows). A vertex poking out by p that is also
within 4 tau of the hull of the OTHERS: the others must also poke out ~ p (to shadow it),
so they ALSO have neg ~ p... and they ALSO expose unless shadowed. The skinny pair shadow
EACH OTHER: v1,v2 both poke out by ~p, within gap of each other (gap <= rho), so each is
rho-shadowed by the other. Now: are they far from conv W? conv W = low face (the anchors +
archetypes). dist_1(v_j, low face) ~ p = H. And neg(v_j) ~ p = H. So delta ~ H => RATE H,
not H^2 !?  Let's MEASURE precisely whether neg(v) == H or H is something else.
"""
import numpy as np
from scipy.optimize import linprog
from asq_model import l1, dist_to_hull_l1, exposed_margin, is_vertex, compute_W

def neg_row(r): return np.maximum(-np.array(r),0).sum()

def make_pair(depth, gap, anchors):
    rows=[np.array([1.,0,0]),np.array([0.,1,0]),np.array([0.,0,1])]
    for a in anchors: rows.append(np.array(a,float))
    # two high vertices poking below edge e0-e1 by 'depth' in coord2
    v1=np.array([0.5, 0.5+depth, -depth])
    v2=np.array([0.5+gap, 0.5-gap+depth, -depth])
    rows.append(v1); rows.append(v2)
    return rows

print("Measure: depth p -> neg(v), dist_1(v,low face), dist_1(v,conv W), exposedness, W")
print("anchors = interior low face; gap small so the pair shadow each other")
anchors=[[1/3,1/3,1/3],[0.45,0.45,0.1],[0.2,0.6,0.2],[0.6,0.2,0.2]]
lowface=anchors+[[1,0,0],[0,1,0],[0,0,1]]
for depth in [0.02,0.05,0.1,0.15,0.2,0.3]:
    gap=0.3*depth  # keep them shadowing: gap proportional
    rows=make_pair(depth,gap,anchors)
    nm=[neg_row(r) for r in rows]
    delta=max(nm); tau=np.sqrt(delta); rho=4*tau; kappa=tau/4
    v1,v2=rows[-2],rows[-1]
    d_low=dist_to_hull_l1(v1,[np.array(x,float) for x in lowface])
    shadow1=dist_to_hull_l1(v1,[rows[i] for i in range(len(rows)-2)]+[v2]) # dist to conv(all others)
    W=compute_W(rows,rho,kappa)
    convW=[rows[i] for i in W]
    dW=dist_to_hull_l1(v1,convW) if convW else np.inf
    m1=exposed_margin(rows,len(rows)-2,rho); m2=exposed_margin(rows,len(rows)-1,rho)
    print(f"depth={depth:.3f}: neg(v)={nm[-2]:.4f} delta={delta:.4f} tau={tau:.4f} rho={rho:.3f} "
          f"d_low={d_low:.4f} shadow={shadow1:.4f} dist_convW={dW:.4f} "
          f"m1={None if m1 is None else round(m1,4)} m2={None if m2 is None else round(m2,4)} "
          f"W={W} | dist/tau={dW/tau if tau>0 and np.isfinite(dW) else float('nan'):.3f} "
          f"delta/dist^2={delta/dW**2 if np.isfinite(dW) and dW>0 else float('nan'):.2f}")
