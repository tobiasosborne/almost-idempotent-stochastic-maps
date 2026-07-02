#!/usr/bin/env python3 -u
"""
d7_fti2.py -- NUMERICAL DECIDER for FTI-2 (the crux of op-exposed-hull).

FTI-2 conjecture (d6-codex-frame-transfer.md, Fallback Deciding Configuration C):
  P exact (P1=1, P^2=P, max row neg <= delta), tau=sqrt(delta).
  A subset W (the (4tau, tau/4)-well-exposed row vertices), C = conv A.
  v1,v2 DISTINCT row vertices with dist_1(v_j, C) >= H, BOTH failing
  (4tau, tau/4)-exposedness, with mutual shadows:
     v1 = mu1 v2 + (1-mu1) L1 + e1,
     v2 = mu2 v1 + (1-mu2) L2 + e2,
  L_j in C, ||e_j||_1 <= 4tau, mu_j -> 1 (skinny regime).
  CLAIM: max_i neg(p_i) >= a * H^2.

DECIDER: minimize delta/H^2 over EXACT completions of this template with ARBITRARY
(Lambda, R), R Lambda = I_r -- NOT only canonical/min-norm frames (the known blind spot).
A verified instance with delta/H^2 -> 0 REFUTES FTI-2; a stable positive floor ~ a
SUPPORTS it.

NORMALIZATION.  delta = max_i neg(p_i) = max_i sum_j max(-P_ij, 0).  This is the SAME
"max-neg units" as the d3 envelope (a in [2.4,3.5] there: env(H)=delta >= a H^2).  So our
delta/H^2 is directly comparable to the d3 a.  (tau = sqrt(delta).)

DESIGN -- exploiting the blind spot.
  The blind spot is that FULLY PINNING the realized hidden rows makes R inert and recovers
  the canonical/bary geometry where delta ~ a H^2 holds.  To attack the conjecture we must
  give the optimizer the freedom the conjecture forbids it to keep: we pin only the
  LOAD-BEARING LINEAR DATA (heights, the mutual-shadow relations, anchor positions) and let
  the alternating LP choose the rest of each hidden row's realization AND the full (Lambda,R).
  We then VERIFY honestly post-hoc (robust W, distances, failed exposedness).

We encode the template in an explicit ell^1 coordinate embedding R^n.  Anchors are pinned
fully (they are the intended W and must stay exposed).  v1, v2 (and helpers) are constrained
only by:
  (i) a HEIGHT functional h(.) with h(v_j) >= H and h(anchor) = 0  (separation from C);
  (ii) the mutual-shadow EQUATIONS as linear constraints in the realized rows, with a free
       error row e_j bounded ||e_j||_1 <= 4 tau (tau a parameter, swept; we also self-
       consistently re-solve tau = sqrt(delta) at the end).
The optimizer minimizes max-row-neg (= delta).  Failed exposedness of v1,v2 is NOT encoded;
it is VERIFIED post-hoc and only instances where both fail are kept.

Verification gate (every reported point), all via the validated robust infra:
  - exact idempotence (idem_resid, row_sum_resid <= 1e-9 target, 1e-7 gate)
  - W recomputed with the MULTIPLICITY-CORRECT vertex test (d3_vertexfix) + robust margins
  - dist_1(v_j, conv W) >= H re-verified (conv W, not conv A!)
  - both v_j genuinely failing (4tau, tau/4)-exposedness (robust exposed_margin < tau/4)
Unverified points are reported separately, never mixed into the floor.
"""
import sys, os, json, time, itertools
import numpy as np

import gurobipy as gp
from gurobipy import GRB

from d1_infra import (check_idempotent, neg_mass, check_factorization,
                      dist1_to_conv, exposed_margin)
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_seed import seed_from_targets

np.set_printoptions(precision=5, suppress=True, linewidth=160)

# ----------------------------------------------------------------------
_ENV = gp.Env(empty=True)
_ENV.setParam("OutputFlag", 0)
_ENV.start()

def _newmodel(name=""):
    m = gp.Model(name, env=_ENV)
    m.setParam("OutputFlag", 0)
    m.setParam("FeasibilityTol", 1e-9)
    m.setParam("OptimalityTol", 1e-9)
    m.setParam("Presolve", 1)
    return m


# ======================================================================
# GENERAL inner LPs supporting:
#   - full row pins:        (Lambda R)_i = t_i                 (dict full_pins: i -> t)
#   - linear functional pins on a row:  <w, (LR)_i> = val      (list lin_pins: (i,w,val))
#   - shadow equations across rows with a bounded error:
#        (LR)_a = mu (LR)_b + (1-mu) (LR)_c + e,  ||e||_1 <= ebar
#     encoded as: introduce slack abs vars for e = (LR)_a - mu (LR)_b - (1-mu)(LR)_c,
#     sum |e_j| <= ebar.   (list shadows: (a,b,c,mu,ebar))
# Objective: minimize max-row-neg.
# Two variants (fixed Lambda -> opt R; fixed R -> opt Lambda); both share constraint code
# via a small builder over the P_ij linear expression.
# ======================================================================
def _build_common(m, Pij, n, full_pins, lin_pins, shadows):
    cons = {}
    # full pins
    for i, t in (full_pins or {}).items():
        for j in range(n):
            cons[("pin", i, j)] = m.addConstr(Pij(i, j) == float(t[j]))
    # linear functional pins
    for k, (i, w, val) in enumerate(lin_pins or []):
        cons[("lin", k)] = m.addConstr(
            gp.quicksum(float(w[j]) * Pij(i, j) for j in range(n)) == float(val))
    # shadow equations with bounded l1 error
    eabs_all = []
    for s, (a, b, c, mu, ebar) in enumerate(shadows or []):
        eabs = m.addVars(n, lb=0.0, name=f"eabs_{s}")
        for j in range(n):
            expr = Pij(a, j) - mu * Pij(b, j) - (1.0 - mu) * Pij(c, j)
            m.addConstr(eabs[j] >= expr)
            m.addConstr(eabs[j] >= -expr)
        cons[("ebar", s)] = m.addConstr(
            gp.quicksum(eabs[j] for j in range(n)) <= float(ebar))
        eabs_all.append(eabs)
    return cons


def lp_optimize_R(Lam, n, full_pins, lin_pins, shadows, R_warm=None, collect_duals=False):
    Lam = np.asarray(Lam, float)
    nn, r = Lam.shape
    assert nn == n
    m = _newmodel("optR")
    R = m.addVars(r, n, lb=-GRB.INFINITY, name="R")
    neg = m.addVars(n, n, lb=0.0, name="neg")
    mneg = m.addVar(lb=0.0, name="mneg")
    def Pij(i, j):
        return gp.quicksum(Lam[i, a] * R[a, j] for a in range(r))
    cons = {}
    for a in range(r):
        for b in range(r):
            cons[("RL", a, b)] = m.addConstr(
                gp.quicksum(R[a, k] * Lam[k, b] for k in range(n)) == (1.0 if a == b else 0.0))
    for a in range(r):
        cons[("Rsum", a)] = m.addConstr(gp.quicksum(R[a, k] for k in range(n)) == 1.0)
    cons.update(_build_common(m, Pij, n, full_pins, lin_pins, shadows))
    for i in range(n):
        for j in range(n):
            cons[("neg", i, j)] = m.addConstr(neg[i, j] >= -Pij(i, j))
        cons[("epi", i)] = m.addConstr(gp.quicksum(neg[i, j] for j in range(n)) <= mneg)
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
        duals = {str(key): float(con.Pi) for key, con in cons.items()
                 if hasattr(con, "Pi") and abs(con.Pi) > 1e-7}
    return Rval, float(mneg.X), {"status": int(m.Status), "duals": duals}


def lp_optimize_Lambda(R, n, full_pins, lin_pins, shadows, Lam_warm=None, collect_duals=False):
    R = np.asarray(R, float)
    r, nn = R.shape
    assert nn == n
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
                gp.quicksum(R[a, k] * Lam[k, b] for k in range(n)) == (1.0 if a == b else 0.0))
    for i in range(n):
        cons[("Lsum", i)] = m.addConstr(gp.quicksum(Lam[i, a] for a in range(r)) == 1.0)
    cons.update(_build_common(m, Pij, n, full_pins, lin_pins, shadows))
    for i in range(n):
        for j in range(n):
            cons[("neg", i, j)] = m.addConstr(neg[i, j] >= -Pij(i, j))
        cons[("epi", i)] = m.addConstr(gp.quicksum(neg[i, j] for j in range(n)) <= mneg)
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
        duals = {str(key): float(con.Pi) for key, con in cons.items()
                 if hasattr(con, "Pi") and abs(con.Pi) > 1e-7}
    return Lval, float(mneg.X), {"status": int(m.Status), "duals": duals}


def alternating_min(Lam0, R0, n, full_pins, lin_pins, shadows, rounds=14, tol=1e-10,
                    verbose=False):
    Lam, R = np.asarray(Lam0, float), np.asarray(R0, float)
    best = None
    prev = np.inf
    last_duals = None
    for it in range(rounds):
        Rn, mn1, infoR = lp_optimize_R(Lam, n, full_pins, lin_pins, shadows, R_warm=R)
        if Rn is None:
            if verbose: print(f"    [alt {it}] optR status={infoR['status']}", flush=True)
            break
        R = Rn
        Ln, mn2, infoL = lp_optimize_Lambda(R, n, full_pins, lin_pins, shadows, Lam_warm=Lam,
                                             collect_duals=True)
        if Ln is None:
            if verbose: print(f"    [alt {it}] optL status={infoL['status']}", flush=True)
            P = Lam @ R
            best = (Lam.copy(), R.copy(), P, mn1, last_duals)
            break
        Lam = Ln
        cur = mn2
        last_duals = infoL.get("duals")
        P = Lam @ R
        best = (Lam.copy(), R.copy(), P, cur, last_duals)
        if verbose:
            print(f"    [alt {it}] mneg(R)={mn1:.6e} mneg(L)={mn2:.6e}", flush=True)
        if abs(prev - cur) < tol * max(1.0, cur):
            break
        prev = cur
    return best


# ======================================================================
# VERIFICATION  (robust, multiplicity-correct)
# ======================================================================
def verify_fti2(P, anchor_idx, v1, v2, C=4.0, c=0.25, H_target=None, idem_tol=1e-7):
    """Full FTI-2 verification gate.  Returns dict with all gate flags."""
    P = np.asarray(P, float)
    n = P.shape[0]
    chk = check_idempotent(P, tol=idem_tol)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "idem_resid": chk["idem_resid"],
           "row_sum_resid": chk["row_sum_resid"], "delta": float(delta),
           "max_neg": float(delta)}
    if not chk["ok"]:
        out["pass"] = False; out["reason"] = "not_idempotent"; return out
    if delta <= 1e-12:
        out["tau"] = 0.0; out["pass"] = False; out["reason"] = "delta_zero"; return out
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    out["tau"] = tau; out["rho"] = rho; out["kappa"] = kappa
    # robust W (multiplicity-correct)
    W, info = well_exposed_set_robust(P, rho, kappa)
    out["nW"] = len(W); out["W"] = list(map(int, W))
    # v1, v2 must be DISTINCT
    out["distinct_v"] = bool(np.abs(P[v1] - P[v2]).sum() > 1e-7)
    # v1, v2 must be VERTICES (robust)
    vert1, _ = is_row_vertex_robust(P, v1)
    vert2, _ = is_row_vertex_robust(P, v2)
    out["v1_vertex"] = bool(vert1); out["v2_vertex"] = bool(vert2)
    # dist_1 to conv W (conv W, NOT conv anchors)
    d1, _ = dist1_to_conv(P, W, v1)
    d2, _ = dist1_to_conv(P, W, v2)
    out["dist_v1"] = float(d1); out["dist_v2"] = float(d2)
    H = min(d1, d2)
    out["H_real"] = float(H)
    out["dist_ge_H"] = bool((H_target is None) or (H >= H_target - 1e-9))
    # both v_j FAIL (4tau, tau/4)-exposedness: robust margin < kappa
    ok1, marg1, _ = exposed_margin(P, v1, rho, kappa)
    ok2, marg2, _ = exposed_margin(P, v2, rho, kappa)
    out["v1_margin"] = (None if marg1 is None else float(marg1))
    out["v2_margin"] = (None if marg2 is None else float(marg2))
    out["v1_fails_exposed"] = bool(not ok1)
    out["v2_fails_exposed"] = bool(not ok2)
    # anchors should be IN W (sanity: C = conv A subset conv W)
    out["anchors_in_W"] = [int(a) for a in anchor_idx if a in W]
    out["all_anchors_in_W"] = bool(all(a in W for a in anchor_idx))
    # the headline ratio
    if H > 1e-9:
        out["delta_over_H2"] = float(delta / (H * H))
    else:
        out["delta_over_H2"] = None
    # FULL GATE
    out["pass"] = bool(
        chk["ok"] and out["distinct_v"] and vert1 and vert2 and
        (not ok1) and (not ok2) and H > 1e-9 and
        ((H_target is None) or H >= H_target - 1e-9))
    return out
