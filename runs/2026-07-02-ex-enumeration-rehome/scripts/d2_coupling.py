#!/usr/bin/env python3 -u
"""
d2_coupling.py -- Understand the R Lambda = I_r coupling for a plateau (Task 2).

Setup. P = Lambda R,  R: r x n (archetype rows, rows sum 1),
       Lambda: n x r (signed bary coords, rows sum 1),  R Lambda = I_r  => P^2=P.

The rows of P are p_i = Lambda_i . R  (a signed combination of the r archetype
rows of R).  So EVERY row of P lives in the affine span (an (r-1)-flat) of the
r archetype rows.  K = conv{rows} sits inside that flat.

Crucial structural facts to nail down symbolically:

 (i) What does R Lambda = I_r say in coordinates?  For each archetype a and
     coordinate b:  sum_i R[a,i] Lambda[i,b] = delta_{ab}.
     Equivalently: the r columns of Lambda are a *dual basis* to the rows of R
     under the pairing <R_a, Lambda^{(b)}> = sum_i R[a,i] Lambda[i,b].
     BUT note the pairing sums over the ROW index i, mixing archetypes with the
     barycentric coordinate functions evaluated at every row.

 (ii) Reparametrize in archetype coordinates.  Let phi_a(i) = Lambda[i,a] be the
      a-th barycentric coordinate of row i.  Row i is at "abstract point"
      lambda_i = (phi_1(i),...,phi_r(i)) in the affine simplex-plane sum=1.
      The map to R^n is x = (lambda) -> lambda R, an affine injection (R rows
      affinely independent => injective).  So ALL the ell^1 geometry of the
      rows is the geometry of the abstract points {lambda_i} pushed through R,
      with the ell^1 metric ||lambda_i R - lambda_j R||_1.

 (iii) The constraint R Lambda = I_r in abstract coords:  if we let the r
       archetypes correspond to r distinguished abstract points e_1..e_r
       (the standard basis of the abstract coordinate, i.e. archetype a is the
       point lambda=e_a), then R Lambda = I_r becomes:
         sum_i R[a,i] phi_b(i) = delta_{ab}.
       Think of R[a,:] as a SIGNED measure mu_a on rows (sum_i R[a,i]=1).
       Then  mu_a(phi_b) = delta_{ab}.  I.e. the signed measure mu_a integrates
       the b-th barycentric coordinate to delta_{ab}.
       Since sum_b phi_b(i)=1 for every i (Lambda rows sum to 1), summing over b:
         sum_b mu_a(phi_b) = mu_a(1) = sum_i R[a,i] = 1 = sum_b delta_{ab}. consistent.

 THE PLATEAU QUESTION.  A plateau = a group G of rows at abstract points
 lambda_i (i in G) that are FAR (>= D tau in ell^1 after R) from conv W, where
 W = well-exposed vertices.  We want the plateau points to be NON-exposed
 (hidden) yet far from conv W.  The abstract points of W and of G live in the
 same (r-1)-simplex-plane.  conv(all rows) is a polytope there.

 We test, symbolically and numerically, the SIMPLEST nontrivial plateau:
   r=3 archetypes A,B,C forming a triangle (the abstract simplex vertices e1,e2,e3).
   Put W = {A,B,C} at height 0 (a low face) -- but with r=3 these ARE the simplex
   vertices, conv W = whole simplex, so EVERY row is in conv W, dist=0. Useless.
 => Need MORE archetypes than W-vertices, or W not spanning. The plateau must
    stick OUT of conv W, so conv W must be a proper sub-face => some archetypes
    are NOT in W and carry the plateau height.

 So the minimal interesting case: r=3, but conv W is a SEGMENT (2 exposed
 vertices) and the plateau pokes out in the 3rd archetype direction.

 We build it and watch which constraint binds.
"""
import sys, json
import numpy as np
import sympy as sp

OUT="out/d2_coupling.json"
res={}
def save():
    import json
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=str)

print("="*70); print("d2_coupling: the R Lambda = I_r structure"); print("="*70, flush=True)

# ----------------------------------------------------------------------
# Symbolic minimal plateau, r=3.
# Abstract points live in plane {x+y+z=1}.  Archetypes at e1,e2,e3.
# Push to R^n via R (3 x n).  Choose R so that the three archetype rows are
# n-vectors summing to 1.  The ell^1 geometry is set by R.
#
# Design: archetypes A and B are the WELL-EXPOSED low vertices; archetype C is a
# "high" direction. Plateau rows sit near C (abstract coord close to e3) but we
# will see RLambda=I_3 forces relations among ALL rows' coordinates.
#
# Let the rows be: the 3 archetypes themselves (rows 0,1,2 with Lambda=e1,e2,e3)
# PLUS plateau rows. For an archetype-as-a-row we need Lambda row = e_a, and then
# p_a = R_a exactly. Good: realized rows include the archetypes.
#
# R Lambda = I_3 with archetype rows present:
#   columns of Lambda for the 3 archetype rows are e1,e2,e3 (a 3x3 identity block).
#   So R Lambda = R[:, arch] * I + R[:, plateau] * Lambda[plateau,:]
#              = R_arch + R_plat @ Lambda_plat   where R_arch is the 3x3 submatrix
#   of R on the archetype columns, R_plat is 3 x |G|, Lambda_plat is |G| x 3.
#   Wait indices: R is 3 x n. Columns indexed by rows? NO. R[a,i] is archetype a,
#   coordinate i in R^n. Lambda[i,b] is row i, coord b. (R Lambda)[a,b]=sum_i R[a,i]Lambda[i,b].
#   The sum is over the n COORDINATES i, not over rows. Let me recompute: R is r x n
#   (n coordinates), Lambda is n x r. So (R Lambda) sums over the n coordinates.
#   The "rows present as archetypes" trick concerns the n x r Lambda whose ROWS are
#   the rows of P's bary coords; that's a different index set (n rows of P) from the
#   n coordinates. CAUTION: only if #rows == n. In P=Lambda R, Lambda is n x r and R
#   is r x n, so P is n x n: there are n rows AND n coordinates, both size n. They are
#   the SAME index set only by accident of P being square. They are NOT the same role.
# ----------------------------------------------------------------------
print("""
KEY CLARIFICATION of indices:
  P = Lambda R is n x n.  Lambda is n x r (n ROWS of P, r abstract coords).
  R is r x n (r archetypes, n COORDINATES of R^n).
  (R Lambda)[a,b] = sum_{i=1..n} R[a,i] Lambda[i,b]  -- the sum runs over the
  shared index 1..n which is simultaneously 'coordinate of R^n' (for R) and
  'row of P' (for Lambda).  This identification IS the coupling: archetype a's
  COORDINATE profile R[a,:] is paired against barycentric-coordinate-b-as-a-
  function-of-row Lambda[:,b].
""", flush=True)
res["index_note"] = ("(R Lambda)[a,b]=sum_i R[a,i] Lambda[i,b]; the index i is both "
  "'coordinate of R^n' for R and 'row of P' for Lambda -- THIS shared index is the coupling.")
save()

# ----------------------------------------------------------------------
# So: define signed measures on the n-element index set:
#   mu_a = R[a,:]  (archetype a's coordinate profile; sum_i mu_a(i)=1)
#   phi_b = Lambda[:,b] (b-th bary coordinate as a function of the index; for each
#                        index i, sum_b phi_b(i)=1)
#   Constraint: <mu_a, phi_b> = sum_i mu_a(i) phi_b(i) = delta_{ab}.
# Both families are 'partitions of unity' (mu over i sums to 1 per a; phi over b
# sums to 1 per i). They are biorthogonal.
#
# This is exactly an OBLIQUE PROJECTION decomposition:  P = Lambda R is the
# oblique projector onto span(rows of R) along ker(R)=null... Actually P=Lambda R
# with R Lambda=I is the standard rank-r idempotent: columns of Lambda span range,
# rows of R span the complementary coimage. Biorthogonality <mu_a,phi_b>=delta.
# ----------------------------------------------------------------------

# Numerical experiment: try to BUILD a plateau and see what RLambda=I forces.
# We parametrize freely R (r x n) and Lambda (n x r) then PROJECT onto the
# constraint manifold {R Lambda=I, rowsums=1} and read off the negativity needed.
print("Building a concrete r=3 plateau attempt and inspecting forced negativity...", flush=True)

def make_simplex_R(r, n, spread, rng):
    """r archetype rows in R^n, rows sum to 1, pairwise ell1-far by ~spread."""
    R = np.zeros((r,n))
    # put archetype a mass near coordinate block a
    for a in range(r):
        R[a, a] = 1.0
    # add a high 'C' archetype far out: handled by caller
    return R

# We instead directly search: given a target geometry of abstract points, solve
# for R, Lambda meeting R Lambda=I with minimal max-neg-mass, via the explicit
# biorthogonal construction:
#   Choose Lambda (n x r), rows sum 1 (the abstract points). Need R (r x n),
#   rows sum 1, with R Lambda = I_r.  R has r*n unknowns; constraints: r*r (=I)
#   + r (rowsums). For n>r this is underdetermined => choose R of MINIMAL negativity.
# Given Lambda full column rank, the constraint R Lambda = I_r is r linear systems
# (one per archetype row R[a,:]): R[a,:] Lambda = e_a^T, i.e. Lambda^T R[a,:]^T = e_a.
# Plus sum_i R[a,i]=1, i.e. 1^T R[a,:]^T = 1. Note 1 = Lambda 1_r (rows sum 1) so
# Lambda^T R[a,:]^T = e_a already implies 1^T... let's just solve each row as an
# LP minimizing neg mass.
from scipy.optimize import linprog
def solve_R_min_neg(Lambda):
    """For given Lambda (n x r, rows sum 1), find R (r x n) rows-sum-1 with
       R Lambda = I_r minimizing the max over archetypes of neg-mass(R[a,:]).
       Returns R or None. (Note: neg mass of R rows is NOT delta of P; delta is
       neg mass of P's rows. But R's negativity is a proxy/driver. We also then
       compute P and its true delta.)"""
    Lam = np.asarray(Lambda, float)
    n, r = Lam.shape
    R = np.zeros((r,n))
    for a in range(r):
        # variables x in R^n (=R[a,:]), split x = xp - xn, xp,xn>=0
        # constraints: Lam^T x = e_a  (r eqs);  minimize sum xn (total neg mass)
        # vars: xp(n), xn(n)
        nv = 2*n
        c = np.concatenate([np.zeros(n), np.ones(n)])
        A_eq = []; b_eq=[]
        for b in range(r):
            row = np.concatenate([Lam[:,b], -Lam[:,b]])
            A_eq.append(row); b_eq.append(1.0 if b==a else 0.0)
        bounds=[(0,None)]*nv
        rr=linprog(c, A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds, method="highs")
        if not rr.success:
            return None, None
        x = rr.x[:n]-rr.x[n:]
        R[a,:]=x
    return R, None

# Try plateau geometry: r=3, abstract points:
#  archetypes A=e1, B=e2 (the two W vertices), C=e3 (high direction).
#  W rows: A,B. Plateau rows: several near e3 but pulled slightly toward A,B with
#  SIGNED coords (poking out). Plus we MUST realize A,B,C as rows (Lambda row=e_a)
#  so the archetypes are actual rows -> C is a row too; is C exposed? we'll see.
#  Also need some 'low' rows to host negative weight.
def build_attempt(eps=0.1, D=3.0, tau=0.1, nplat=3, seed=0):
    # abstract coords (Lambda), each row sums to 1
    rng=np.random.default_rng(seed)
    rows=[]
    rows.append([1,0,0])  # A archetype
    rows.append([0,1,0])  # B archetype
    rows.append([0,0,1])  # C archetype (high)
    # plateau rows: mostly C, slight signed pull. They sit 'above' segment AB.
    for k in range(nplat):
        # signed: weight on C ~ 1+something, negative on a low row to hold height
        a = -eps*(k+1)*0.0
        rows.append([a, a, 1-2*a])
    Lam=np.array(rows,float)
    n=Lam.shape[0]
    R,_=solve_R_min_neg(Lam)
    if R is None: return None
    P=Lam@R
    return Lam,R,P

out=build_attempt()
if out:
    Lam,R,P=out
    from d1_infra import check_idempotent, neg_mass, ratio_stats, check_factorization
    print("Lambda=\n",Lam, flush=True)
    print("R=\n",R, flush=True)
    print("fact check:", check_factorization(Lam,R), flush=True)
    print("idem:", check_idempotent(P), flush=True)
    nm,delta=neg_mass(P); print("P neg mass per row:",nm," delta=",delta, flush=True)
    res["attempt1"]={"Lambda":Lam.tolist(),"R":R.tolist(),"P":P.tolist(),
                     "delta":delta,"fact":check_factorization(Lam,R)}
    save()
print("d2_coupling first pass done", flush=True)
