#!/usr/bin/env python3 -u
"""
d1_infra.py  --  Infrastructure for op-exposed-hull counterexample hunt.

Object P (n x n real):  P 1 = 1,  P^2 = P EXACTLY.
Row negative mass neg(p_i) = sum_j max(-P_ij, 0) <= delta.   tau = sqrt(delta).
Rows p_i in R^n (ell^1 geometry).  K = conv{rows}.

A row VERTEX v of K is (rho,kappa)-well-exposed if there is an affine h: K->[0,1]
with h(v)=0 and h(p_i) >= kappa for every row with ||p_i - v||_1 >= rho.
Take rho = C*tau, kappa = c*tau.
W = set of well-exposed row vertices.

CONJECTURE (op-exposed-hull): every row satisfies dist_1(p_i, conv W) <= C' tau,
C' universal (independent of n AND delta).

This module provides:
  - check_idempotent(P): verify P 1 = 1 and P^2 = P (returns residuals).
  - neg_mass(P): per-row negative mass, delta = max.
  - is_row_vertex(rows, i): LP test whether row i is a vertex of conv(rows).
  - exposed_margin(rows, i, rho, kappa): feasibility LP for well-exposedness of row i.
  - well_exposed_set(...): the set W.
  - dist1_to_conv(rows, W_idx, i): LP for dist_1(p_i, conv{rows[W]}).
  - ratio_stats(P, C, c): the headline ratio max_i dist_1(p_i, conv W)/tau.

All LPs use scipy.optimize.linprog (HiGHS).  Crash-safe progress prints.
"""
import sys, json, time
import numpy as np
from scipy.optimize import linprog

np.set_printoptions(precision=6, suppress=True, linewidth=160)

# ----------------------------------------------------------------------
# Robust LP wrapper.  The default HiGHS simplex can return status 4
# ("numerical difficulties") -- NOT genuine infeasibility -- on near-coincident
# or badly scaled rows (this caused a FALSE ratio=69 'counterexample' spike in
# the d3 hunt, see d1-report.md).  We try interior-point + both simplex variants
# and only trust status==2 as truly infeasible.
# ----------------------------------------------------------------------
def robust_linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    last = None
    for meth in ("highs-ipm", "highs", "highs-ds"):
        r = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                    bounds=bounds, method=meth)
        if r.success:
            return r
        last = r
        if getattr(r, "status", None) == 2:   # genuinely infeasible: trust it
            return r
    return last

# ----------------------------------------------------------------------
# Basic algebra
# ----------------------------------------------------------------------
def check_idempotent(P, tol=1e-9):
    P = np.asarray(P, float)
    n = P.shape[0]
    row1 = np.abs(P @ np.ones(n) - 1.0).max()
    idem = np.abs(P @ P - P).max()
    return {"row_sum_resid": float(row1), "idem_resid": float(idem),
            "ok": bool(row1 < tol and idem < tol)}

def neg_mass(P):
    P = np.asarray(P, float)
    nm = np.maximum(-P, 0.0).sum(axis=1)
    return nm, float(nm.max())

# ----------------------------------------------------------------------
# Vertex test:  is row i NOT a convex combination of the others?
#   Solve feasibility: exists lambda >= 0, sum=1, supported off i, with
#       sum_k lambda_k rows[k] = rows[i].
#   If infeasible -> i is a vertex (extreme).  We test via an LP that
#   minimizes ell1 reconstruction error; >tol => vertex.
# ----------------------------------------------------------------------
def is_row_vertex(rows, i, tol=1e-7):
    rows = np.asarray(rows, float)
    n, d = rows.shape
    others = [k for k in range(n) if k != i]
    if not others:
        return True, 0.0
    A = rows[others].T            # d x (n-1)
    b = rows[i]
    m = len(others)
    # variables: lambda (m) >=0, t_j (d) for |residual_j|
    # min sum t  s.t.  A lam - b <= t,  -(A lam - b) <= t,  sum lam = 1
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    # inequality rows
    A_ub = []
    b_ub = []
    for j in range(d):
        row_pos = np.zeros(nv); row_pos[:m] = A[j]; row_pos[m+j] = -1.0
        A_ub.append(row_pos); b_ub.append(b[j])
        row_neg = np.zeros(nv); row_neg[:m] = -A[j]; row_neg[m+j] = -1.0
        A_ub.append(row_neg); b_ub.append(-b[j])
    A_eq = np.zeros((1, nv)); A_eq[0, :m] = 1.0
    b_eq = [1.0]
    bounds = [(0, None)]*m + [(0, None)]*d
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if res is None or not res.success:
        return True, np.inf
    err = res.fun
    return bool(err > tol), float(err)

# ----------------------------------------------------------------------
# Well-exposedness feasibility LP.
#   affine h(x) = a.x + b.   Variables a in R^d, b in R.
#   Constraints:
#     0 <= h(p_k) <= 1   for all rows k         (h: K -> [0,1])
#     h(p_i) = 0                                 (the exposed vertex)
#     h(p_k) >= kappa    for all k with ||p_k - p_i||_1 >= rho
#   Feasible <=> i is (rho,kappa)-well-exposed.
#   We solve a feasibility LP (maximize a slack s>=0 on the kappa-far rows:
#     h(p_k) >= kappa + s) so the returned margin tells how exposed it is.
# ----------------------------------------------------------------------
def exposed_margin(rows, i, rho, kappa):
    """(rho,kappa)-well-exposedness of row i.

    ROBUST FORMULATION (margin-maximizing).  Instead of a *fixed*-kappa feasibility
    LP (which scipy HiGHS misreports as status-4 on near-coincident / badly-scaled
    rows -- this produced FALSE non-exposed verdicts and a bogus ratio=69..inf spike,
    see d1-report.md), we compute the MAXIMUM achievable margin

        t* = max over affine h with h(p_i)=0, 0<=h<=1, of  min_{k far} h(p_k).

    Then row i is (rho,kappa)-well-exposed  <=>  t* >= kappa.  Returning t* makes
    the classification a numeric comparison (robust to a measure-zero noise twin
    sitting exactly at margin 0) rather than a brittle feasible/infeasible flag.
    We solve with interior-point AND presolve OFF (presolve was the culprit on the
    degenerate near-duplicate-row clusters).
    """
    rows = np.asarray(rows, float)
    n, d = rows.shape
    di = np.abs(rows - rows[i]).sum(axis=1)        # ell1 distances to row i
    far = [k for k in range(n) if di[k] >= rho - 1e-12 and k != i]
    if not far:
        # no far rows: vacuously exposable with unbounded margin
        return True, float("inf"), {"far": 0}
    # variables: a(d), b(1), t(1) = min_{far} h ; maximize t (min -t)
    nv = d + 1 + 1
    c = np.zeros(nv); c[-1] = -1.0
    A_ub = []; b_ub = []
    def hvec(k):
        v = np.zeros(nv); v[:d] = rows[k]; v[d] = 1.0; return v
    for k in range(n):
        hk = hvec(k)
        A_ub.append(hk.copy()); b_ub.append(1.0)        # h(p_k) <= 1
        A_ub.append(-hk.copy()); b_ub.append(0.0)       # h(p_k) >= 0
    for k in far:
        hk = hvec(k); v = -hk; v[-1] = 1.0
        A_ub.append(v); b_ub.append(0.0)                # h(p_k) >= t
    A_eq = [hvec(i)]; b_eq = [0.0]                       # h(p_i) = 0
    # bounds: a,b free; t free (can be 0 or tiny positive). t bounded above by 1.
    bounds = [(None, None)]*d + [(None, None)] + [(None, 1.0)]
    res = None
    for meth, presolve in (("highs-ipm", False), ("highs", False),
                           ("highs-ipm", True), ("highs-ds", False)):
        r = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                    A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                    bounds=bounds, method=meth, options={"presolve": presolve})
        if r.success:
            res = r; break
    if res is None:
        # could not solve numerically at all: report unknown as NOT exposed,
        # but flag it so callers can see this is a solver failure, not geometry.
        return False, None, {"far": len(far), "solver_failed": True}
    tstar = -res.fun
    ok = bool(tstar >= kappa - 1e-9)
    return ok, float(tstar), {"far": len(far), "tstar": float(tstar),
                              "a": res.x[:d].tolist(), "b": float(res.x[d])}

def well_exposed_set(rows, rho, kappa, require_vertex=True, vtol=1e-7, verbose=False):
    rows = np.asarray(rows, float)
    n = rows.shape[0]
    W = []
    info = {}
    for i in range(n):
        if require_vertex:
            vert, verr = is_row_vertex(rows, i, tol=vtol)
            if not vert:
                info[i] = {"vertex": False, "verr": verr}
                continue
        else:
            vert = True
        ok, s, ex = exposed_margin(rows, i, rho, kappa)
        info[i] = {"vertex": vert, "exposed": ok, "margin": s}
        if ok:
            W.append(i)
        if verbose:
            print(f"  row {i}: vertex={vert} exposed={ok} margin={s}", flush=True)
    return W, info

# ----------------------------------------------------------------------
# dist_1(p_i, conv{rows[W]})  via LP.
#   min ||p_i - sum_{k in W} lam_k rows[k]||_1  s.t. lam>=0, sum=1.
# ----------------------------------------------------------------------
def dist1_to_conv(rows, W_idx, i):
    rows = np.asarray(rows, float)
    n, d = rows.shape
    if len(W_idx) == 0:
        return np.inf, None
    A = rows[W_idx].T             # d x |W|
    b = rows[i]
    m = len(W_idx)
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    A_ub = []; b_ub = []
    for j in range(d):
        rp = np.zeros(nv); rp[:m] = A[j]; rp[m+j] = -1.0
        A_ub.append(rp); b_ub.append(b[j])
        rn = np.zeros(nv); rn[:m] = -A[j]; rn[m+j] = -1.0
        A_ub.append(rn); b_ub.append(-b[j])
    A_eq = np.zeros((1, nv)); A_eq[0, :m] = 1.0
    b_eq = [1.0]
    bounds = [(0, None)]*m + [(0, None)]*d
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if res is None or not res.success:
        return np.inf, None
    return float(res.fun), res.x[:m]

# ----------------------------------------------------------------------
# Headline ratio.
# ----------------------------------------------------------------------
def ratio_stats(P, C=4.0, c=0.25, require_vertex=True, verbose=False, label=""):
    P = np.asarray(P, float)
    n = P.shape[0]
    chk = check_idempotent(P)
    nm, delta = neg_mass(P)
    if delta <= 0:
        # purely stochastic idempotent: no negativity. tau=0; conjecture trivial.
        tau = 0.0
    else:
        tau = float(np.sqrt(delta))
    rho = C*tau; kappa = c*tau
    rows = P  # rows of P are the rows p_i
    W, info = well_exposed_set(rows, rho, kappa, require_vertex=require_vertex, verbose=verbose)
    dists = []
    for i in range(n):
        di, _ = dist1_to_conv(rows, W, i)
        dists.append(di)
    dists = np.array(dists)
    if tau > 0:
        ratios = dists / tau
        maxr = float(np.nanmax(ratios))
    else:
        ratios = dists
        maxr = float(np.nanmax(dists))
    out = {"label": label, "n": n, "delta": delta, "tau": tau,
           "C": C, "c": c, "rho": rho, "kappa": kappa,
           "idem": chk, "nW": len(W), "W": list(map(int, W)),
           "max_dist": float(np.nanmax(dists)),
           "max_ratio": maxr,
           "dists": dists.tolist(),
           "ratios": (dists/tau).tolist() if tau>0 else dists.tolist()}
    if verbose:
        print(f"[{label}] n={n} delta={delta:.3e} tau={tau:.4e} "
              f"|W|={len(W)} max_dist={out['max_dist']:.4e} "
              f"max_ratio={maxr:.4f} idem_ok={chk['ok']}", flush=True)
    return out

# ----------------------------------------------------------------------
# Builders for the parametrization P = Lambda R with R Lambda = I_r.
#   R: r x n  (archetype rows, rows sum to 1)
#   Lambda: n x r (signed barycentric coords, rows sum to 1)
#   If R Lambda = I_r then P=Lambda R satisfies P^2=P and P1=1.
# ----------------------------------------------------------------------
def build_P(Lambda, R):
    Lambda = np.asarray(Lambda, float); R = np.asarray(R, float)
    return Lambda @ R

def check_factorization(Lambda, R, tol=1e-9):
    Lambda = np.asarray(Lambda, float); R = np.asarray(R, float)
    r = R.shape[0]
    RL = R @ Lambda
    res = {
        "RLambda_minus_I": float(np.abs(RL - np.eye(r)).max()),
        "R_rowsum": float(np.abs(R.sum(axis=1) - 1).max()),
        "Lambda_rowsum": float(np.abs(Lambda.sum(axis=1) - 1).max()),
    }
    res["ok"] = bool(res["RLambda_minus_I"] < tol and res["R_rowsum"] < tol
                     and res["Lambda_rowsum"] < tol)
    return res

if __name__ == "__main__":
    print("d1_infra module self-test", flush=True)
    P = np.eye(4)
    print(ratio_stats(P, verbose=True, label="identity4"))
