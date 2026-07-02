#!/usr/bin/env python3
r"""
EXACT k=2-with-anchors algebra (the mechanism), symbolic.

Coordinate model (the task's "heights as one coordinate, rest the simplex flat"):
We separate one affine functional g = "height". Anchors and low rows have g <= g_lo ~ 0.
The two high vertices v1,v2 have g(v_j) = H. W lives among low rows, so conv W has
g <= g_lo. "v_j is H-far from conv W" we will MODEL by g(v_j) - max_{conv W} g >= H
(height is a 1-Lipschitz-in-ell1 functional witnessing a lower bound on ell1 distance:
if ||g||_{lip,ell1} <= 1 then dist_1(v_j,conv W) >= g(v_j)-sup_{conv W} g).

FAILED (rho,kappa)-EXPOSEDNESS, dual form. v_j fails: for the family of admissible
exposers, none lifts all rho-far rows to >= kappa. By LP duality (Farkas on the
exposedness LP), failure produces a 'pull-in' certificate: there exist convex weights
mu^j on the rho-far rows with
        || v_j - sum_i mu^j_i p_i ||  controlled, AND
        the height defect  g(v_j) - sum_i mu^j_i g(p_i)  <=  kappa * (something).
More usable (and what we make exact): failing exposedness at margin kappa means v_j is
NOT (rho,kappa)-exposed; combined with v_j being a vertex with a rho-shadow (PROVED
recursion input), the cleanest extractable fact is a NEAR-AFFINE RELATION:

   (R_j)   v_j = sum_{i != j} mu^j_i p_i + e_j,   mu^j_i >= 0, sum mu^j_i = 1,
           ||e_j||_1 <= shadow := rho     (the rho-shadow: v_j within rho of conv(others))

PLUS the failed-exposedness REFINEMENT: the pulling mass mu^j cannot avoid the OTHER
high vertex. Concretely (skinny + anchored): the only rows with height ~ H are v1,v2;
all others (anchors/low/side) have height <= g_lo. Write mu^j's mass on the other high
vertex as t_j := mu^j_{(other high)} and the rest (mass 1-t_j) on LOW rows. Apply g:

   H = g(v_j) = sum_i mu^j_i g(p_i) + g(e_j)
     = t_j * H  + (1-t_j)*g_lo' + g(e_j),     g_lo' <= g_lo (avg height of low mass)

  => H (1 - t_j) = (1-t_j) g_lo' + g(e_j)
  => (1-t_j)(H - g_lo') = g(e_j) <= ||g||_lip * ||e_j||_1 <= rho     (since ||g||_lip<=1)

  => 1 - t_j <= rho / (H - g_lo').                                   (HEIGHT-LEAN)

So each high vertex's pull-in leans on the OTHER high vertex with weight
   t_j >= 1 - rho/(H-g_lo)  ->  near 1 when H >> rho.

Now COMPOSE the two relations (R_1),(R_2). This is the core. Substitute (R_2) into (R_1):
   v_1 = t_1 v_2 + (1-t_1) L_1 + e_1                 (L_1 = low-row convex combo)
   v_2 = t_2 v_1 + (1-t_2) L_2 + e_2
=> v_1 = t_1(t_2 v_1 + (1-t_2)L_2 + e_2) + (1-t_1)L_1 + e_1
=> v_1(1 - t_1 t_2) = t_1(1-t_2)L_2 + (1-t_1)L_1 + t_1 e_2 + e_1
=> v_1 = [t_1(1-t_2)L_2 + (1-t_1)L_1]/(1-t_1 t_2)  + [t_1 e_2 + e_1]/(1-t_1 t_2)
The first bracket is a CONVEX combo of LOW rows (coeffs nonneg, sum to
 (t_1(1-t_2)+(1-t_1))/(1-t_1 t_2) = (1 - t_1 t_2)/(1-t_1 t_2) = 1). Call it Lbar (low).
The second bracket is the ERROR:  E1 = (t_1 e_2 + e_1)/(1 - t_1 t_2).

  => v_1 = Lbar + E1,   Lbar in conv(LOW rows),   ||E1||_1 <= (t_1||e_2||+||e_1||)/(1-t_1 t_2)
                                                            <= (1+1)*rho/(1-t_1 t_2)? no: <= (t_1+1) rho/(1-t1t2)

APPLY g once more to v_1 = Lbar + E1:
   H = g(v_1) = g(Lbar) + g(E1) <= g_lo + ||E1||_1
  => H - g_lo <= ||E1||_1 <= (1+t_1) rho / (1 - t_1 t_2).

This is the HEIGHT DEFECT INEQUALITY. Now bound 1 - t_1 t_2 from HEIGHT-LEAN:
 t_j >= 1 - rho/(H-g_lo) =: 1 - r,  r := rho/(H-g_lo).
 => t_1 t_2 >= (1-r)^2  => 1 - t_1 t_2 <= 1-(1-r)^2 = 2r - r^2 <= 2r.
 So:  H - g_lo <= (1+t_1) rho / (1 - t_1 t_2).  This goes the WRONG way (upper bounds
 H-g_lo by something, but 1-t1t2 small makes RHS big -> vacuous). NEED THE OTHER DIRECTION.

The cost must come from NEGATIVITY, not from this consistency. Where does neg enter?
=> Lbar in conv(LOW rows) but LOW rows are ROWS of P with neg mass. The relation
   v_1 = Lbar + E1 says a HIGH point (height H) equals a low-hull point + small error.
   That's only an INCONSISTENCY if the low rows are honest (neg 0): a convex combo of
   height<=g_lo points has height <= g_lo < H, contradiction unless ||E1|| >= H-g_lo.
   The convex-combo bound g(Lbar)<=g_lo USED nonnegativity of the mu-weights. With
   honest low rows there is NO negativity and NO contradiction-with-cost: E1 just has
   to be big (>= H-g_lo), and ||E1|| big requires... the shadows e_j big? e_j <= rho.
   So if H - g_lo > (1+t_1) rho/(1-t_1 t_2) is VIOLATED, the config is INFEASIBLE
   (no such pull-ins exist) => v_j was actually EXPOSED => contradiction with failing.

CONCLUSION OF THIS BLOCK (the honest finding): the pure height/convex bookkeeping gives a
FEASIBILITY constraint  H - g_lo <= (1+t_1) rho/(1-t_1 t_2), NOT a cost lower bound. The
H^2 cost is NOT forced by convex geometry of one configuration -- matching the task's
warning. The cost must come from EXACTNESS coupling the shadows e_j to NEGATIVITY:
e_j is not free; e_j = v_j - (convex combo of rows), and ||e_j||_1 <= rho is the shadow,
but the DIRECTION/height of e_j is constrained because the SAME rows expand via P.
We make that precise numerically next (asq_search did: delta/H^2 stayed >= ~5*2? in
max-neg units; here we instead pin the symbolic relation between rho, H, and neg).
"""
import sympy as sp

H,glo,rho,t1,t2,r = sp.symbols('H glo rho t1 t2 r', positive=True)

# HEIGHT-LEAN: 1 - t_j <= r where r = rho/(H-glo)
# Composed error bound: H - glo <= (1+t1) rho/(1 - t1 t2)
# Substitute t1=t2=1-r (the tight symmetric case):
expr = (1+(1-r))*rho/(1-(1-r)**2)
expr_s = sp.simplify(expr)
print("composed error bound RHS at t1=t2=1-r:", expr_s)
# = (2-r) rho /(2r - r^2) = (2-r)rho/(r(2-r)) = rho/r = H-glo.  TAUTOLOGY.
print("simplify (2-r)*rho/(r*(2-r)) =", sp.simplify((2-r)*rho/(r*(2-r))))
print("=> the convex bookkeeping is a TAUTOLOGY (H-glo <= H-glo). No cost from geometry alone.")
print()
print("So the H^2 cost requires an EXACTNESS-driven relation between the shadow e_j and neg.")
print("Proceed to pin that numerically (asq_exact.py): does ||e_j|| (the rho-shadow) being")
print("realized by EXACT idempotent rows force neg >= c H^2 even though geometry alone does not?")
