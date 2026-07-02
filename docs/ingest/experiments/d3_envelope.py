#!/usr/bin/env python3 -u
"""
d3_envelope.py -- ADVERSARIAL envelope-mining for the anchored-circuit cost (HCC).

THE ONE OPEN QUESTION.  For an EXACT signed affine retraction P (P1=1, P^2=P) write
neg(p_i) = sum_j max(-P_ij, 0).  Fix a "hidden height" H and ask for the LOWER
ENVELOPE

    env(H) := min { max_i neg(p_i) :  P exact, some row at dist_1(.,conv W) >= H }

where W = (rho,kappa)-well-exposed row vertices, rho=C*tau, kappa=c*tau, tau=sqrt(delta),
delta = max_i neg(p_i).  The HCC conjecture predicts env(H) >= a*H^2 (a universal).
We MINE this envelope by ADVERSARIALLY minimizing max-row-neg over EXACT idempotents
that realize a "hidden" geometry.

KEY DESIGN DECISIONS (vs the prover-favorable d3_hunt):
 1. ADVERSARIAL R.  d3_hunt used the min-Frobenius completion R=R_from_Lambda(Lam),
    which is PROVER-favorable (it minimizes ||R||, often suppressing negativity in an
    artificial way).  Here we OPTIMIZE over BOTH Lambda and R by EXACT ALTERNATING LPs:
      * fixed Lambda: {R : R Lambda = I_r, R rows sum 1} is an AFFINE set; minimizing
        max_i neg((Lambda R)_i) over it is an exact LP (convex PWL objective).
      * fixed R: {Lambda : R Lambda = I_r, Lambda rows sum 1} is an AFFINE set; the
        neg objective is convex in Lambda -> exact LP.
    Multistart + alternation drives max-row-neg DOWN to the true adversarial minimum
    for each fixed hidden-geometry template.  (Lower max-neg => stronger / harder for
    the conjecture.)
 2. HIDDEN GEOMETRY via fixed combinatorial TEMPLATES + honest verification.
    The geometric constraint "some row at dist_1 >= H from conv W" is NOT smooth (W
    depends on P).  We encode it as explicit LINEAR constraints PINNING the realized
    rows of the hidden cluster to target positions at height ~H arranged so they
    mutually shadow (a thin diamond / circuit).  We DO NOT trust the template; after
    optimization we RECOMPUTE W honestly and the achieved dist_1 and max-neg with the
    robust checker.  Only VERIFIED points enter the envelope.

Templates implemented:
  * thin_diamond(H, w, ...):  m_base "anchor" rows forming a low simplex (intended W)
    + a k-row "diamond/circuit" at height H whose rows mutually shadow (each hidden row
    is a near-affine-combination of its diamond neighbours so its exposedness margin < kappa).
  * staircase(H, ...):  a single far row at height H over a base (control: an ISOLATED
    far row is provably well-exposed, so it should JOIN W -> dist collapses -> not a
    valid hidden point; this is a CONTROL that the pipeline rejects bad templates).

We pin the REALIZED rows of P (= rows of Lambda R) to targets in a chosen ell^1
embedding.  Pinning row i to target t_i is the linear constraint (Lambda R)_i = t_i.
For fixed R that is linear in Lambda[i,:]:  Lambda[i,:] R = t_i.  For fixed Lambda it
is linear in R.  So pinning is compatible with BOTH alternating LPs.

OUTPUT: out/d3_envelope_<family>.json  with the verified envelope table, exponent fit,
dual certificate structure, control results.  Crash-safe checkpoints.
"""
import sys, os, json, time, itertools
import numpy as np

import gurobipy as gp
from gurobipy import GRB

from d1_infra import (check_idempotent, neg_mass, check_factorization,
                      well_exposed_set, dist1_to_conv, exposed_margin,
                      ratio_stats)

np.set_printoptions(precision=5, suppress=True, linewidth=160)

# ----------------------------------------------------------------------
# Gurobi env: silent, presolve handled per-model. We keep numerics tight.
# ----------------------------------------------------------------------
_ENV = gp.Env(empty=True)
_ENV.setParam("OutputFlag", 0)
_ENV.start()

def _newmodel(name=""):
    m = gp.Model(name, env=_ENV)
    m.setParam("OutputFlag", 0)
    m.setParam("FeasibilityTol", 1e-9)
    m.setParam("OptimalityTol", 1e-9)
    m.setParam("Presolve", 1)   # mild; we add anti-degeneracy by margin maximization elsewhere
    return m

# ----------------------------------------------------------------------
# Inner LP A:  fixed Lambda  ->  optimize R.
#   variables: R (r x n).  constraints: R Lambda = I_r ; R rows sum 1 ; rows pinned:
#   for pinned row i with target t_i:  (Lambda R)_i = t_i  i.e. sum_a Lambda[i,a] R[a,:] = t_i.
#   objective: minimize  m  s.t.  for every row i:  sum_j neg_ij <= m ,
#     neg_ij >= -(Lambda R)_ij , neg_ij >= 0 .
#   (Lambda R)_ij = sum_a Lambda[i,a] R[a,j].  Linear in R.
# Returns R, max_neg, and dual multipliers on the binding constraints.
# ----------------------------------------------------------------------
def lp_optimize_R(Lam, pins, R_warm=None, collect_duals=False):
    Lam = np.asarray(Lam, float)
    n, r = Lam.shape
    m = _newmodel("optR")
    R = m.addVars(r, n, lb=-GRB.INFINITY, name="R")
    # neg vars + epigraph
    neg = m.addVars(n, n, lb=0.0, name="neg")
    mneg = m.addVar(lb=0.0, name="mneg")
    # P_ij expression
    def Pij(i, j):
        return gp.quicksum(Lam[i, a] * R[a, j] for a in range(r))
    cons = {}
    # R Lambda = I_r
    for a in range(r):
        for b in range(r):
            cons[("RL", a, b)] = m.addConstr(
                gp.quicksum(R[a, k] * Lam[k, b] for k in range(n)) == (1.0 if a == b else 0.0),
                name=f"RL_{a}_{b}")
    # R rows sum 1
    for a in range(r):
        cons[("Rsum", a)] = m.addConstr(gp.quicksum(R[a, k] for k in range(n)) == 1.0,
                                        name=f"Rsum_{a}")
    # pins: (Lambda R)_i = t_i
    for i, t in pins.items():
        for j in range(n):
            cons[("pin", i, j)] = m.addConstr(Pij(i, j) == float(t[j]), name=f"pin_{i}_{j}")
    # neg constraints + epigraph
    for i in range(n):
        for j in range(n):
            cons[("neg", i, j)] = m.addConstr(neg[i, j] >= -Pij(i, j), name=f"neg_{i}_{j}")
        cons[("epi", i)] = m.addConstr(gp.quicksum(neg[i, j] for j in range(n)) <= mneg,
                                       name=f"epi_{i}")
    m.setObjective(mneg, GRB.MINIMIZE)
    if R_warm is not None:
        for a in range(r):
            for k in range(n):
                R[a, k].Start = float(R_warm[a, k])
    m.optimize()
    if m.Status != GRB.OPTIMAL:
        return None, None, {"status": int(m.Status)}
    Rval = np.array([[R[a, k].X for k in range(n)] for a in range(r)])
    duals = None
    if collect_duals:
        duals = {}
        for key, con in cons.items():
            pi = con.Pi
            if abs(pi) > 1e-7:
                duals[str(key)] = float(pi)
    return Rval, float(mneg.X), {"status": int(m.Status), "duals": duals}

# ----------------------------------------------------------------------
# Inner LP B:  fixed R -> optimize Lambda.
#   variables: Lambda (n x r). constraints: R Lambda = I_r ; Lambda rows sum 1 ;
#   pins (Lambda R)_i = t_i (linear in Lambda[i,:]).
#   objective: minimize max-row-neg as above.
# ----------------------------------------------------------------------
def lp_optimize_Lambda(R, pins, Lam_warm=None, collect_duals=False):
    R = np.asarray(R, float)
    r, n = R.shape
    m = _newmodel("optL")
    Lam = m.addVars(n, r, lb=-GRB.INFINITY, name="Lam")
    neg = m.addVars(n, n, lb=0.0, name="neg")
    mneg = m.addVar(lb=0.0, name="mneg")
    def Pij(i, j):
        return gp.quicksum(Lam[i, a] * R[a, j] for a in range(r))
    cons = {}
    for a in range(r):
        for b in range(r):
            cons[("RL", a, b)] = m.addConstr(
                gp.quicksum(R[a, k] * Lam[k, b] for k in range(n)) == (1.0 if a == b else 0.0),
                name=f"RL_{a}_{b}")
    for i in range(n):
        cons[("Lsum", i)] = m.addConstr(gp.quicksum(Lam[i, a] for a in range(r)) == 1.0,
                                        name=f"Lsum_{i}")
    for i, t in pins.items():
        for j in range(n):
            cons[("pin", i, j)] = m.addConstr(Pij(i, j) == float(t[j]), name=f"pin_{i}_{j}")
    for i in range(n):
        for j in range(n):
            cons[("neg", i, j)] = m.addConstr(neg[i, j] >= -Pij(i, j), name=f"neg_{i}_{j}")
        cons[("epi", i)] = m.addConstr(gp.quicksum(neg[i, j] for j in range(n)) <= mneg,
                                       name=f"epi_{i}")
    m.setObjective(mneg, GRB.MINIMIZE)
    if Lam_warm is not None:
        for i in range(n):
            for a in range(r):
                Lam[i, a].Start = float(Lam_warm[i, a])
    m.optimize()
    if m.Status != GRB.OPTIMAL:
        return None, None, {"status": int(m.Status)}
    Lval = np.array([[Lam[i, a].X for a in range(r)] for i in range(n)])
    duals = None
    if collect_duals:
        duals = {}
        for key, con in cons.items():
            pi = con.Pi
            if abs(pi) > 1e-7:
                duals[str(key)] = float(pi)
    return Lval, float(mneg.X), {"status": int(m.Status), "duals": duals}

# ----------------------------------------------------------------------
# Alternating minimization: minimize max-row-neg over (Lambda,R) with RLambda=I,
# rowsums, and the pins.  Returns best (Lam,R,P,max_neg) + final duals.
# ----------------------------------------------------------------------
def alternating_min(Lam0, R0, pins, rounds=12, tol=1e-9, verbose=False):
    Lam, R = np.asarray(Lam0, float), np.asarray(R0, float)
    best = None
    prev = np.inf
    for it in range(rounds):
        Rn, mn1, infoR = lp_optimize_R(Lam, pins, R_warm=R)
        if Rn is None:
            if verbose: print(f"    [alt {it}] optR status={infoR['status']}", flush=True)
            break
        R = Rn
        Ln, mn2, infoL = lp_optimize_Lambda(R, pins, Lam_warm=Lam)
        if Ln is None:
            if verbose: print(f"    [alt {it}] optL status={infoL['status']}", flush=True)
            # keep R-only result
            P = Lam @ R
            best = (Lam.copy(), R.copy(), P, mn1)
            break
        Lam = Ln
        cur = mn2
        P = Lam @ R
        best = (Lam.copy(), R.copy(), P, cur)
        if verbose:
            print(f"    [alt {it}] mneg(R)={mn1:.6e} mneg(L)={mn2:.6e}", flush=True)
        if abs(prev - cur) < tol * max(1.0, cur):
            break
        prev = cur
    return best

# ----------------------------------------------------------------------
# HONEST VERIFICATION of a candidate P: recompute W, dist1 of hidden rows, max-neg.
# Returns a dict; "verified_hidden" True iff exact idempotent AND some designated
# hidden row genuinely has dist1(.,conv W) >= H_target (recomputed honestly).
# ----------------------------------------------------------------------
def verify(P, hidden_idx, C=4.0, c=0.25, H_target=None, idem_tol=1e-7):
    P = np.asarray(P, float)
    n = P.shape[0]
    chk = check_idempotent(P, tol=idem_tol)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "idem_resid": chk["idem_resid"],
           "row_sum_resid": chk["row_sum_resid"],
           "delta": float(delta), "max_neg": float(delta)}
    if not chk["ok"]:
        out["verified_hidden"] = False
        out["reason"] = "not_idempotent"
        return out
    if delta <= 1e-12:
        # purely stochastic: tau=0, W = all vertices, hidden geometry meaningless
        out["tau"] = 0.0; out["verified_hidden"] = False; out["reason"] = "delta_zero"
        return out
    tau = float(np.sqrt(delta))
    rho, kappa = C * tau, c * tau
    W, info = well_exposed_set(P, rho, kappa)
    # solver-failure flag in exposedness
    solver_fail = any(isinstance(v, dict) and v.get("exposed") is False and
                      isinstance(v.get("margin"), type(None)) for v in info.values())
    dists = {}
    maxhid = -1.0; arghid = -1
    for i in hidden_idx:
        di, _ = dist1_to_conv(P, W, i)
        dists[i] = float(di)
        if di > maxhid:
            maxhid = di; arghid = i
    out.update({"tau": tau, "rho": rho, "kappa": kappa, "nW": len(W),
                "W": list(map(int, W)), "hidden_dists": {int(k): v for k, v in dists.items()},
                "max_hidden_dist": float(maxhid), "argmax_hidden": int(arghid),
                "hidden_in_W": [int(i) for i in hidden_idx if i in W]})
    H = H_target if H_target is not None else maxhid
    # verified hidden: the achieved max hidden dist >= H_target (we record actual dist)
    out["verified_hidden"] = bool(maxhid >= (H if H is not None else 0.0) - 1e-9 and maxhid > 1e-9)
    return out
