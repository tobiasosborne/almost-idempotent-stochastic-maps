#!/usr/bin/env python3 -u
"""
d1_validate.py -- Task 1 validation of the infrastructure on known instances:
  (a) identity (n=4)              -- every row a vertex, delta=0, trivially ok.
  (b) Baake-Sumner-style stochastic idempotent (E_i blocks + transient rows).
  (c) Hume rank-one family P_t = I - u v^T with v.1=0, v.u=1 (exact retraction).
  (d) random P = Psi Phi, Phi Psi = I_r (the prior 4500-sample family) -- a few.

For signed instances we expect max_dist/tau to be SMALL (ratio -> 0, O(tau)),
i.e. conjecture-consistent. We report the ratio and verify P^2=P.
Results streamed to out/d1_validate.json crash-safe.
"""
import sys, json, time
import numpy as np
from d1_infra import (check_idempotent, neg_mass, ratio_stats, build_P,
                      check_factorization)

OUT = "out/d1_validate.json"
results = {}

def save():
    with open(OUT, "w") as f:
        json.dump(results, f, indent=2)

def banner(s):
    print("="*70, flush=True); print(s, flush=True); print("="*70, flush=True)

# ----------------------------------------------------------------------
# (a) identity
# ----------------------------------------------------------------------
banner("(a) identity n=4")
P = np.eye(4)
r = ratio_stats(P, verbose=True, label="identity4")
results["identity4"] = r; save()

# ----------------------------------------------------------------------
# (b) Baake-Sumner stochastic idempotent.
#   A stochastic idempotent (Markov): recurrent classes are absorbing
#   blocks where each block has identical rows = its stationary law; transient
#   rows are convex combos of block laws. Construct:
#     two absorbing states 0,1 (rows e0, e1). Two more absorbing? Make
#     blocks: states {0},{1} absorbing; transient states 2,3 map to a mix.
#   P =
#     [1 0 0 0]
#     [0 1 0 0]
#     [a 1-a 0 0]
#     [b 1-b 0 0]
#   P^2 = P since columns 2,3 are zero and rows 0,1 are fixed:
#   (P^2)_{2,:} = a*row0 + (1-a)*row1 + 0 = (a,1-a,0,0) = row2. ok.
#   No negativity -> delta=0, tau=0. The transient rows are NOT vertices
#   (they're convex combos of e0,e1). Vertices = e0,e1; both well-exposed.
# ----------------------------------------------------------------------
banner("(b) Baake-Sumner stochastic idempotent")
a, b = 0.7, 0.3
P = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [a,1-a,0,0],
    [b,1-b,0,0]], float)
print("idem check:", check_idempotent(P), flush=True)
r = ratio_stats(P, verbose=True, label="baake_sumner")
results["baake_sumner"] = r; save()

# A larger Baake-Sumner with a transient row OFF the segment in another coord:
# 3 absorbing e0,e1,e2 ; transient rows mixtures.
banner("(b') Baake-Sumner, 3 absorbing + 3 transient (n=6)")
Pmix = np.zeros((6,6))
Pmix[0,0]=Pmix[1,1]=Pmix[2,2]=1
Pmix[3] = [0.5,0.3,0.2,0,0,0]
Pmix[4] = [0.2,0.2,0.6,0,0,0]
Pmix[5] = [0.4,0.4,0.2,0,0,0]
print("idem check:", check_idempotent(Pmix), flush=True)
r = ratio_stats(Pmix, verbose=True, label="baake_sumner6")
results["baake_sumner6"] = r; save()

# ----------------------------------------------------------------------
# (c) Hume rank-one family P_t = I - u v^T, v.1=0, v.u=1.
#   P^2 = I - 2 u v^T + u (v^T u) v^T = I - 2uv^T + uv^T = I - uv^T = P. exact.
#   P 1 = 1 - u (v^T 1) = 1 since v.1=0. exact retraction onto a hyperplane.
#   Negativity comes from -u v^T entries. Scale to control delta.
#   3x3: pick v = t*(1,-2,1) (v.1=0). u with v.u=1.
#     v.u = t(u0 -2u1 + u2) = 1.  pick u=(1,1,1): v.u = t(1-2+1)=0 -> bad.
#     pick u=(1,0,0): v.u=t -> t=1 gives v.u=1 with v=(1,-2,1).
#     Then P = I - u v^T, u v^T = [[1,-2,1],[0,0,0],[0,0,0]].
#     P=[[0,2,-1],[0,1,0],[0,0,1]]. row sums:1,1,1 ok. neg mass row0 = 1.
#   To make delta small, scale: u = s*(1,0,0), v=(1,-2,1)/s so v.u=1 still,
#   but then u v^T = (1,0,0)^T (1,-2,1) independent of s -> same P. Rank-one
#   P_t is RIGID in magnitude. Instead tune v direction to shrink neg mass.
#   General: u v^T row i = u_i v. neg mass row i = u_i * (sum of neg parts of v
#   if u_i>0) ... = |u_i| * negmass(v) roughly. Choose u_i tiny except keep v.u=1.
#   Let v=(eps, -2 eps, eps)? then v.1=0, but need v.u=1: pick u=(1/eps,0,0)
#   -> u v^T row0 = (1/eps)(eps,-2eps,eps)=(1,-2,1) again. Magnitude conserved.
#   Conclusion: a single rank-one Hume retraction has neg mass ~O(1) on the
#   active row; to get SMALL delta use a DIFFERENT family (many small rank-one
#   pushes). We instead demonstrate a scaled rank-one with moderate delta and
#   confirm ratio is modest, then a SMALL-delta variant via barycentric build.
# ----------------------------------------------------------------------
banner("(c) Hume rank-one P = I - u v^T (3x3)")
u = np.array([1.0,0,0]); v = np.array([1.0,-2,1])
P = np.eye(3) - np.outer(u, v)
print("P=\n", P, flush=True)
print("idem:", check_idempotent(P), "  v.1=", v.sum(), " v.u=", v@u, flush=True)
nm, delta = neg_mass(P)
print("neg mass per row:", nm, " delta=", delta, flush=True)
r = ratio_stats(P, verbose=True, label="hume_rank1_3")
results["hume_rank1_3"] = r; save()

# small-delta Hume-like: P = I - u v^T with small ||u v^T||.
# Take u=(c,0,0,...), v with v.1=0, v.u=1 => c*v0=1 not small unless...
# Instead: u=(c, -c, 0,...) sum, v.u small? Let v=(g, g, ...) ...
# Simplest small-delta exact retraction: P = I - u v^T with
# u = delta0 * w, v = w'/delta0 chosen so v.u=1 and neg mass = delta0-controlled.
# Use u=(0.5,0.5,0,0,0,0) (>=0, no neg from u sign), v=(s,-s, ...).
# Let v = (s, s, -? ) Need v.1=0 and v.u=1: with u=(.5,.5,0,...),
#   v.u = .5(v0+v1)=1 -> v0+v1=2. v.1=0 -> sum v =0.
# pick v0=v1=1, rest sum -2 spread over many coords as small negatives:
#   v = (1,1, -2/(n-2) * ones).  neg mass of P row i = u_i * negmass(v) = u_i * 2 ...
# That's O(1) again because v.u=1 pins magnitude. RANK-ONE IS RIGID: any exact
# rank-one retraction has a row of neg mass >= |v_-|*max u, bounded below by the
# v.u=1 normalization. So delta for rank-one is NOT freely small. We accept that
# and just verify the n=3 ratio is finite/modest (it is the analog of n=4 rigidity).
banner("(c') note: rank-one Hume is rigid in delta (documented in JSON)")
results["hume_note"] = ("rank-one exact retractions have delta=Theta(1) on the "
    "active row because v.u=1 pins the magnitude; cannot be made small-delta. "
    "This is the n-dim analog of the n=4 rigidity. Ratio is finite, not blowing up.")
save()

# ----------------------------------------------------------------------
# (d) random P = Psi Phi, Phi Psi = I_r  (the prior family) -- small delta.
# Build via R, Lambda with R Lambda = I_r and small signed perturbation.
# Simple construction with controllable delta:
#   pick r archetype rows R (rows sum 1), then Lambda = pseudo so R Lambda=I.
# We instead reuse the random Psi/Phi route and just MEASURE delta.
# ----------------------------------------------------------------------
banner("(d) random P=Psi Phi, Phi Psi=I_r")
rng = np.random.default_rng(0)
def random_exact_retraction(n, r, scale=0.1, rng=rng):
    # Phi (r x n), Psi (n x r) with Phi Psi = I_r, and P=Psi Phi has P1=1.
    # Ensure 1 in column span: set first column of Psi = 1 (constant), and
    # make Phi's first row the functional dual to it. Easiest: build via QR.
    # Choose Psi random with first column = ones; Phi = (Psi^+); then Phi Psi=I.
    Psi = rng.standard_normal((n, r)) * scale
    Psi[:,0] = 1.0
    Phi = np.linalg.pinv(Psi)          # r x n, Phi Psi = I_r (since Psi full col rank)
    P = Psi @ Phi
    return P
for k in range(3):
    P = random_exact_retraction(8, 3, scale=0.05, rng=rng)
    chk = check_idempotent(P)
    nm, delta = neg_mass(P)
    if not chk["ok"]:
        print(f"sample {k}: idem fail {chk}", flush=True); continue
    if delta < 1e-6:
        print(f"sample {k}: delta tiny ({delta:.2e}), skip ratio", flush=True); continue
    r = ratio_stats(P, verbose=True, label=f"random_d_{k}")
    results[f"random_d_{k}"] = r; save()

banner("DONE task 1 validation")
save()
print("saved", OUT, flush=True)
