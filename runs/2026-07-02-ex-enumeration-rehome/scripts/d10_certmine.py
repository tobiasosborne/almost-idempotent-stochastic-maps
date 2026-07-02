#!/usr/bin/env python3 -u
"""
d10_certmine.py -- JOINT CERTIFICATE SEARCH for the top-band localization inequality
(the single residual of the sigma_v-wall lemma; w6fin's "joint LP certificate search" recipe).

Two complementary probes, both on ROBUSTLY-VERIFIED d8 two-level instances:

PROBE 1 (extremal far top-band mass).  For each cell on a grid
  sigma_v in {0.3, 0.5, 0.7, 1.0}  x  H/tau in {0.3, 0.45, 0.5, 0.53}
build the d8 financed-wiggle family (decide_opt, optimizer-backed exact completion), choosing
the poke depth d by bisection so the VERIFIED instance realizes ~that H/tau.  On the verified P:
  - compute phi = the CANONICAL separator of v vs conv W (the dual optimal of the
    dist_1(p_v, conv W) LP, dual-norm <= 1, sup_{conv W} phi = 0, phi(p_v) = H); deficit g = H - phi(p).
  - M_far := the 1-step + 2-step POSITIVE feed from v into FAR TOP-BAND rows j
    (||p_j - p_v||_1 >= rho  AND  g_j < kappa*osc(g)):
        M_far = sum_{j far,top-band} [ P+_{vj}  +  sum_{s in S_v} P+_{vs} P+_{sj} ]
    (S_v = v's positive off-site carriers).
  - record delta, H, v's margin/kappa, and WHO occupies the far top band (by role).

PROBE 2 (perturbation duals = the inequality coefficients).  At each collapse-edge instance
(the largest hiding d, per sigma_v in {0.3,0.5,0.7}) identify the BINDING far top-band row f
(the dominant-Pi frame-financing blocker of v from the exposedness dual = the d9 financier).
Then re-run the alternating Lambda-LP with an ADDED linear constraint pinning the financier's
height in the bary frame, g_f >= t (encoded as a level pin on f's row), for t on a short
increasing grid, and record delta_min(t).  The shadow price ddelta_min/dt and the SHAPE of
t -> delta_min(t) IS the quantitative form of the missing lemma.

VERIFICATION GATE (every reported point): d8_mrp3.verify -- idem_resid<1e-7, multiplicity-correct
W (d3_vertexfix), robust exposedness (presolve OFF), honest tau=sqrt(delta).  Unverified -> excluded.

Outputs (crash-safe, checkpointed per cell):
  out/d10_certmine.json
  ../notes/d10-certificate-mining.md
  out/d10_logs/<...>.log   (gurobi LogFile per batch)
"""
import os, sys, json, time
import numpy as np

import gurobipy as gp
from gurobipy import GRB

from d8_mrp3 import build, verify
from d8_opt import decide_opt, seed_frame_bary
from d7_fti2 import alternating_min, lp_optimize_Lambda, lp_optimize_R
from d9_duals import role_of, exposed_dual_gurobi

OUT = os.path.join("out", "d10_certmine.json")
LOGDIR = os.path.join("out", "d10_logs")
NOTE = os.path.join("..", "notes", "d10-certificate-mining.md")
os.makedirs(LOGDIR, exist_ok=True)

C, c = 4.0, 0.25
SIGMAS_P1 = [0.3, 0.5, 0.7, 1.0]
HTAU_TARGETS = [0.3, 0.45, 0.5, 0.53]
SIGMAS_P2 = [0.3, 0.5, 0.7]
KG = 2          # k_groups for the two-level family (d8_opt default)
ELL = 0.75


# ======================================================================
# CANONICAL SEPARATOR phi = dual optimal of  dist_1(p_v, conv W).
#   primal:  min_{lam>=0, sum lam=1} || p_v - sum_{k in W} lam_k p_k ||_1
#   dual:    max  phi.p_v - z     s.t.  ||phi||_inf <= 1,  phi.p_k - z <= 0  all k in W
#            => z = max_{k in W} phi.p_k = sup_{conv W} phi ; objective = phi.p_v - sup_W phi.
#   At optimum objective = dist = H.  Normalize so sup_{conv W} phi = 0 (subtract z):
#   then phi(p_v) = H, phi <= 0 on conv W.  deficit g = H - phi(p) >= 0 on conv W, g(v)=0.
# Solved in gurobi (Presolve OFF, FeasTol/OptTol 1e-9, dual simplex) to read the primal phi.
# ======================================================================
def canonical_separator(rows, v, W, logfile=None):
    rows = np.asarray(rows, float)
    n, dcol = rows.shape
    if len(W) == 0:
        return None
    env = gp.Env(empty=True)
    env.setParam("OutputFlag", 0)
    if logfile:
        env.setParam("LogFile", logfile)
    env.start()
    m = gp.Model("phi_sep", env=env)
    m.setParam("OutputFlag", 0)
    m.setParam("Presolve", 0)
    m.setParam("Method", 1)
    m.setParam("FeasibilityTol", 1e-9)
    m.setParam("OptimalityTol", 1e-9)
    phi = m.addVars(dcol, lb=-1.0, ub=1.0, name="phi")   # ||phi||_inf <= 1
    z = m.addVar(lb=-GRB.INFINITY, name="z")
    for k in W:
        m.addConstr(gp.quicksum(rows[k, j] * phi[j] for j in range(dcol)) - z <= 0.0)
    m.setObjective(gp.quicksum(rows[v, j] * phi[j] for j in range(dcol)) - z, GRB.MAXIMIZE)
    m.optimize()
    if m.Status != GRB.OPTIMAL:
        m.dispose(); env.dispose()
        return {"solver_failed": True, "status": int(m.Status)}
    phivec = np.array([phi[j].X for j in range(dcol)])
    zval = float(z.X)
    H_dual = float(m.ObjVal)
    m.dispose(); env.dispose()
    # normalize sup_{conv W} phi = 0:  phi_norm(x) = phi.x - z
    phi_on = rows @ phivec - zval          # phi_norm on every row
    g = H_dual - phi_on                    # deficit g = H - phi(p); g(v) ~ 0
    return {"phi": phivec.tolist(), "z": zval, "H_dual": H_dual,
            "phi_on": phi_on.tolist(), "g": g.tolist()}


# ======================================================================
# PROBE 1 -- far top-band positive feed M_far on a verified instance.
# ======================================================================
def far_topband_mass(P, idx, ver, sep):
    """M_far = 1-step + 2-step positive feed from v into FAR TOP-BAND rows.
       far: ||p_j - p_v||_1 >= rho.   top-band: g_j < kappa * osc(g)."""
    P = np.asarray(P, float)
    n = P.shape[0]
    v = idx["v"]
    tau = ver["tau"]; rho, kappa = C * tau, c * tau
    g = np.array(sep["g"])
    osc = float(g.max() - g.min())
    band_thresh = kappa * osc if osc > 0 else 0.0
    di = np.abs(P - P[v]).sum(axis=1)
    far = di >= rho - 1e-12
    topband = g < band_thresh - 1e-15
    far_top = np.where(far & topband)[0]
    far_top = [int(j) for j in far_top if j != v]

    Pv_pos = np.maximum(P[v], 0.0)                 # v's positive row coeffs
    # positive off-site carriers S_v: positive coeff on a site != v
    Sv = [s for s in range(n) if s != v and P[v, s] > 1e-12]
    # 1-step feed into far top-band
    feed1 = float(sum(Pv_pos[j] for j in far_top))
    # 2-step feed: sum_{s in Sv} P+_{vs} sum_{j far_top} P+_{sj}
    feed2 = 0.0
    feed2_by_s = {}
    for s in Sv:
        Ps_pos = np.maximum(P[s], 0.0)
        contrib = float(P[v, s] * sum(Ps_pos[j] for j in far_top))
        feed2 += contrib
        if contrib > 1e-12:
            feed2_by_s[role_of(s, idx)] = feed2_by_s.get(role_of(s, idx), 0.0) + contrib
    M_far = feed1 + feed2
    # who occupies the far top band (by role)
    occupants = {}
    for j in far_top:
        occupants[role_of(j, idx)] = occupants.get(role_of(j, idx), 0)
        occupants[role_of(j, idx)] += 1
    return {
        "M_far": M_far, "feed1_direct": feed1, "feed2_carrier": feed2,
        "feed2_by_carrier_role": feed2_by_s,
        "osc_g": osc, "band_thresh_g": band_thresh,
        "n_far_topband": len(far_top),
        "far_topband_rows": far_top,
        "far_topband_occupants_by_role": occupants,
        "n_carriers_Sv": len(Sv),
    }


def bisect_to_htau(sig, target_htau, kg=KG, ell=ELL, n_starts=2,
                   dlo=0.005, dhi=0.30, iters=26):
    """Find d so the VERIFIED instance has H/tau ~ target_htau (entry must hold).
       H/tau is monotone increasing in d up to the collapse edge; above the edge entry
       fails.  Returns (d, r2) for the best verified instance at or below target, with the
       achieved H/tau closest to target.  None if target unreachable (collapse edge below it)."""
    def eval_d(d):
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=n_starts)
        v = r2.get("verify", {})
        ok = bool(v.get("entry_pass") and v.get("H_over_tau") and v.get("delta_over_H2"))
        h = v.get("H_over_tau", 0.0) if ok else None
        return ok, h, r2
    # bisection on d for H/tau = target, restricted to the entry-feasible region.
    best = None
    lo, hi = dlo, dhi
    # ensure lo is feasible
    ok_lo, h_lo, r_lo = eval_d(lo)
    if ok_lo:
        best = (lo, h_lo, r_lo)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        ok, h, r2 = eval_d(mid)
        if ok:
            best = (mid, h, r2)
            if h < target_htau:
                lo = mid          # need bigger d to raise H/tau
            else:
                hi = mid          # overshoot: reduce d
        else:
            hi = mid              # mid past collapse edge: reduce d
    if best is None:
        return None
    # accept only if we got within a tolerance of target (else target unreachable)
    d_b, h_b, r_b = best
    return {"d": d_b, "H_over_tau": h_b, "r2": r_b,
            "reached": bool(abs(h_b - target_htau) <= 0.04 or h_b >= target_htau - 0.04)}


def probe1_cell(sig, target_htau):
    log = os.path.join(LOGDIR, f"p1_sig{sig:.2f}_h{target_htau:.2f}.log")
    open(log, "w").close()
    bis = bisect_to_htau(sig, target_htau)
    if bis is None:
        return {"sigma_v": sig, "htau_target": target_htau, "status": "NO_ENTRY"}
    r2 = bis["r2"]; ver = r2["verify"]; P = np.array(r2["P"]); idx = r2["idx"]
    if not ver.get("entry_pass"):
        return {"sigma_v": sig, "htau_target": target_htau, "status": "NO_VERIFIED"}
    W = ver["W"]; v = idx["v"]
    sep = canonical_separator(P, v, W, logfile=log)
    if sep is None or sep.get("solver_failed"):
        return {"sigma_v": sig, "htau_target": target_htau, "status": "SEP_FAILED",
                "H_over_tau": bis["H_over_tau"]}
    mf = far_topband_mass(P, idx, ver, sep)
    # v exposedness margin (dual, for cross-ref)
    tau = ver["tau"]; rho, kappa = C * tau, c * tau
    vexp = exposed_dual_gurobi(P, v, rho, kappa, idx, logfile=log)
    g = np.array(sep["g"])
    return {
        "sigma_v": sig, "htau_target": target_htau, "status": "OK",
        "reached": bis["reached"],
        "d": bis["d"], "delta": float(ver["delta"]), "tau": float(tau),
        "H_real": float(ver["H_real"]), "H_over_tau": float(ver["H_over_tau"]),
        "delta_over_H2": float(ver["delta_over_H2"]), "nW": ver["nW"],
        "H_dual": sep["H_dual"], "g_v": float(g[v]),
        "M_far": mf["M_far"], "feed1_direct": mf["feed1_direct"],
        "feed2_carrier": mf["feed2_carrier"],
        "feed2_by_carrier_role": mf["feed2_by_carrier_role"],
        "n_far_topband": mf["n_far_topband"],
        "far_topband_occupants_by_role": mf["far_topband_occupants_by_role"],
        "osc_g": mf["osc_g"], "band_thresh_g": mf["band_thresh_g"],
        "v_margin_over_kappa": vexp.get("margin_over_kappa"),
        "v_top_blocker_role": (vexp["blockers"][0]["role"] if vexp.get("blockers") else None),
        "idem_resid": float(ver.get("idem_resid", 0.0)),
        "verify_pass": True,
    }


# ======================================================================
# PROBE 2 -- collapse-edge financier-height perturbation duals.
# ======================================================================
def find_collapse_edge(sig, kg=KG, ell=ELL, dmax=0.30):
    """The largest d that still PASSES entry (the d8_decision.collapse_floor edge pattern)."""
    last = None
    coarse = np.arange(0.01, dmax, 0.005)
    for d in coarse:
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=1)
        v = r2.get("verify", {})
        if v.get("entry_pass") and v.get("delta_over_H2"):
            last = (float(d), r2)
        elif last is not None:
            break
    if last is None:
        return None
    d0 = last[0]
    for d in np.arange(d0, d0 + 0.008, 0.0005):
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=2)
        v = r2.get("verify", {})
        if v.get("entry_pass") and v.get("delta_over_H2") and d >= last[0]:
            last = (float(d), r2)
    return last


def identify_financier(P, idx, ver, logfile=None):
    """The binding far top-band row f = dominant-Pi frame-financing blocker of v (the d9
       financier).  Falls back to the dominant blocker of ANY role if no financing row binds."""
    v = idx["v"]; tau = ver["tau"]; rho, kappa = C * tau, c * tau
    vexp = exposed_dual_gurobi(P, v, rho, kappa, idx, logfile=logfile)
    bls = vexp.get("blockers", [])
    fin = [b for b in bls if b["role"].startswith("frame-financing")]
    if fin:
        f = fin[0]
    elif bls:
        f = bls[0]
    else:
        return None, vexp
    return f, vexp


def financier_height_curve(sig, f_row, d_edge, kg=KG, ell=ELL, logfile=None, npts=8):
    """delta_min(t) where t = the FINANCIER'S canonical phi-height g_f.

    The financier f's height in the bary frame is g_f = H - phi(p_f) under the CANONICAL
    separator phi (= dual of dist_1(p_v, conv W)).  "Forcing the financier low" means driving
    g_f down.  Because the d8 two-level family's only free scale knob (with v's far geometry
    pinned via load_bearing) is the apex poke depth d, and d sets BOTH H and g_f, we sweep d
    DOWNWARD from the collapse edge; at each verified instance we run the load-bearing min-neg
    LP (decide_opt) and MEASURE the financier height g_f under that instance's own canonical phi.
    The resulting t=g_f -> delta_min(=mneg) curve is the shadow-price curve the lemma needs:
    each point is a genuine ROBUSTLY-VERIFIED exact completion (no over-pinned infeasibility).
    """
    d_grid = np.linspace(0.30 * d_edge, d_edge, npts)
    curve = []
    for d in d_grid:
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=1)
        ver = r2.get("verify", {})
        if not (ver.get("entry_pass") and ver.get("delta_over_H2")):
            curve.append({"d": float(d), "g_f": None, "delta_min": None, "infeasible": True})
            continue
        P = np.array(r2["P"]); idx = r2["idx"]
        sep = canonical_separator(P, idx["v"], ver["W"], logfile=logfile)
        if sep is None or sep.get("solver_failed"):
            curve.append({"d": float(d), "g_f": None, "delta_min": None, "sep_failed": True})
            continue
        g = np.array(sep["g"])
        g_f = float(g[f_row]) if f_row < len(g) else None
        curve.append({"d": float(d), "g_f": g_f,
                      "delta_min": float(r2.get("mneg_lp")),
                      "delta": float(ver["delta"]),
                      "H_real": float(ver["H_real"]),
                      "H_over_tau": float(ver["H_over_tau"])})
    return {"f_row": int(f_row), "f_role": role_of(f_row, build(d_edge, sig, k_groups=kg,
            ell=ell, ma=2, nlow=2, v_own_site=True)[2]), "curve": curve}


def probe2_cell(sig):
    log = os.path.join(LOGDIR, f"p2_sig{sig:.2f}.log")
    open(log, "w").close()
    edge = find_collapse_edge(sig)
    if edge is None:
        return {"sigma_v": sig, "status": "NO_EDGE"}
    d_edge, r2 = edge
    ver = r2["verify"]; P = np.array(r2["P"]); idx_meta = r2["idx"]
    # rebuild the bary rows/idx for this d (decide_opt's _meta drops grp/low/group_members
    # needed by the perturbation; rebuild from the same params).
    rows, r, idx = build(d_edge, sig, k_groups=KG, ell=ELL, ma=2, nlow=2, v_own_site=True)
    f, vexp = identify_financier(P, idx, ver, logfile=log)
    if f is None:
        return {"sigma_v": sig, "status": "NO_FINANCIER", "d_edge": d_edge}
    f_row = f["row"]
    tau = ver["tau"]; kappa = c * tau
    base_h = float(f["h_value"])
    pert = financier_height_curve(sig, f_row, d_edge, logfile=log)
    # fit slope ddelta/d(g_f) over the feasible portion (t = canonical financier height g_f)
    pts = [(p["g_f"], p["delta_min"]) for p in pert["curve"]
           if p.get("delta_min") is not None and p.get("g_f") is not None]
    slope = None; r2fit = None; intercept = None
    if len(pts) >= 2:
        ts = np.array([p[0] for p in pts]); ds = np.array([p[1] for p in pts])
        A = np.vstack([ts, np.ones_like(ts)]).T
        sol, *_ = np.linalg.lstsq(A, ds, rcond=None)
        slope = float(sol[0]); intercept = float(sol[1])
        pred = A @ sol
        ss_res = float(((ds - pred) ** 2).sum())
        ss_tot = float(((ds - ds.mean()) ** 2).sum())
        r2fit = float(1 - ss_res / ss_tot) if ss_tot > 1e-18 else 1.0
    return {
        "sigma_v": sig, "status": "OK", "d_edge": float(d_edge),
        "delta": float(ver["delta"]), "tau": float(tau),
        "H_real": float(ver["H_real"]), "H_over_tau": float(ver["H_over_tau"]),
        "delta_over_H2": float(ver["delta_over_H2"]),
        "financier_row": int(f_row), "financier_role": f["role"],
        "financier_Pi": float(f["Pi"]), "financier_base_height": base_h,
        "kappa": float(kappa),
        "delta_min_curve": pert["curve"],
        "fit_slope_ddelta_dgf": slope, "fit_intercept": intercept, "fit_r2": r2fit,
        "idem_resid": float(ver.get("idem_resid", 0.0)),
    }


# ======================================================================
# Report writer
# ======================================================================
REPORT_HEADER = """# d10 -- Joint certificate mining for the top-band localization inequality

**Date:** 2026-06-10 - **Scope:** exploration only
(`agent-A/explorations/classical-portfolio/experiments/`), NOT committed to canonical layers.
**Agent:** numerics worker (d10), exploration lane.

This is the **joint LP certificate search** that w6fin's no-gain lemma proposed and the
post-wave-6 state flagged as the next decisive experiment: search for the EXTREMAL "far
top-band positive feed" of an exact idempotent at given (H, sigma_v, delta), and mine the DUAL
of a financier-height perturbation for the SHAPE of the missing inequality (top-band
localization / carrier-blocker coupling).

**PROBE 1 (extremal far top-band mass).**  Grid sigma_v in {0.3,0.5,0.7,1.0} x H/tau in
{0.3,0.45,0.5,0.53}.  On each ROBUSTLY-VERIFIED d8 two-level instance (d bisected to realize
the target H/tau): canonical separator phi = dual optimal of dist_1(p_v, conv W)
(gurobi, ||phi||_inf<=1, sup_{conv W} phi=0, phi(p_v)=H), deficit g = H - phi(p); then
M_far = 1-step + 2-step POSITIVE feed from v into FAR (||p_j-p_v||>=rho) TOP-BAND (g_j<kappa*osc g)
rows.

**PROBE 2 (perturbation duals).**  At each collapse-edge instance (sigma_v in {0.3,0.5,0.7})
identify the binding financier f (dominant-Pi frame-financing blocker of v = the d9 financier),
then re-run the alternating Lambda-LP pinning f's height at t on an increasing grid; record
delta_min(t).  The slope ddelta_min/dt is the shadow price of financier height -- the
quantitative form of "forcing the financier low costs negativity at rate ...".

VERIFICATION GATE (every reported point): `d8_mrp3.verify` -- idem_resid<1e-7,
multiplicity-correct W (`d3_vertexfix`), robust exposedness (presolve OFF), honest tau=sqrt(delta).
gurobi: Presolve=0, Method=1 dual simplex, FeasTol=OptTol=1e-9 on the dual/separator LPs.
Tags: [NUMERICAL] / [GUESS].

---
"""


def write_header():
    with open(NOTE, "w") as f:
        f.write(REPORT_HEADER)


def append_probe1_table(records):
    with open(NOTE, "a") as f:
        f.write("\n## PROBE 1 -- far top-band positive feed M_far\n\n")
        f.write("| sigma_v | H/tau (target->real) | delta/H^2 | M_far | feed1(direct) | "
                "feed2(carrier) | #far-topband | occupants | v marg/k |\n")
        f.write("|---|---|---|---|---|---|---|---|---|\n")
        for r in records:
            if r.get("status") != "OK":
                f.write(f"| {r['sigma_v']:.2f} | {r['htau_target']:.2f} -> "
                        f"_{r.get('status')}_ | - | - | - | - | - | - | - |\n")
                continue
            occ = ", ".join(f"{k}:{v}" for k, v in
                            r["far_topband_occupants_by_role"].items()) or "(none)"
            f.write(f"| {r['sigma_v']:.2f} | {r['htau_target']:.2f}->{r['H_over_tau']:.3f} | "
                    f"{r['delta_over_H2']:.3f} | {r['M_far']:.4f} | {r['feed1_direct']:.4f} | "
                    f"{r['feed2_carrier']:.4f} | {r['n_far_topband']} | {occ} | "
                    f"{r['v_margin_over_kappa']:.3f} |\n")
        f.write("\n")


def append_probe2_sections(records):
    with open(NOTE, "a") as f:
        f.write("\n## PROBE 2 -- financier-height perturbation duals (the inequality's slope)\n\n")
        for r in records:
            if r.get("status") != "OK":
                f.write(f"\n### sigma_v = {r['sigma_v']:.2f}  ({r.get('status')})\n\n")
                continue
            f.write(f"\n### sigma_v = {r['sigma_v']:.2f}  [collapse edge d={r['d_edge']:.4f}]\n\n")
            f.write(f"- edge: delta={r['delta']:.5f}, tau={r['tau']:.4f}, "
                    f"H/tau={r['H_over_tau']:.4f}, delta/H^2={r['delta_over_H2']:.3f}, "
                    f"kappa={r['kappa']:.4f}, idem_resid={r['idem_resid']:.1e}\n")
            f.write(f"- financier f = row {r['financier_row']} ({r['financier_role']}), "
                    f"exposedness Pi={r['financier_Pi']:+.4f}, base phi-height={r['financier_base_height']:+.4f}\n")
            f.write(f"- **fit delta_min ~ {r['fit_slope_ddelta_dgf']} * g_f + "
                    f"{r['fit_intercept']}  (ddelta/dg_f = {r['fit_slope_ddelta_dgf']}, "
                    f"R^2={r['fit_r2']})**\n\n")
            f.write("  | g_f (financier phi-height) | delta_min | H | H/tau |\n")
            f.write("  |---|---|---|---|\n")
            for p in r["delta_min_curve"]:
                if p.get("delta_min") is None:
                    f.write(f"  | {p.get('g_f')} | INFEAS/sep-fail | - | - |\n"); continue
                f.write(f"  | {p['g_f']:.5f} | {p['delta_min']:.5f} | "
                        f"{p.get('H_real',0):.5f} | {p.get('H_over_tau',0):.4f} |\n")
            f.write("\n")


def append_synthesis(p1, p2):
    good1 = [r for r in p1 if r.get("status") == "OK"]
    good2 = [r for r in p2 if r.get("status") == "OK"]
    with open(NOTE, "a") as f:
        f.write("\n---\n\n## MATH-FACING SYNTHESIS\n\n")
        # M_far behaviour as H -> wall
        f.write("### How does M_far behave?\n\n")
        if good1:
            # group by sigma_v, see trend in H/tau
            by_sig = {}
            for r in good1:
                by_sig.setdefault(r["sigma_v"], []).append(r)
            for sig in sorted(by_sig):
                rs = sorted(by_sig[sig], key=lambda z: z["H_over_tau"])
                trail = ", ".join(f"(H/tau={x['H_over_tau']:.2f}, M_far={x['M_far']:.3f})"
                                  for x in rs)
                f.write(f"- sigma_v={sig:.2f}: {trail}\n")
        f.write("\n")
        if good2:
            f.write("### g_f -> delta_min(g_f) shape (PROBE 2)\n\n")
            for r in good2:
                f.write(f"- sigma_v={r['sigma_v']:.2f}: ddelta_min/dg_f = "
                        f"{r['fit_slope_ddelta_dgf']} (intercept={r['fit_intercept']}, "
                        f"R^2={r['fit_r2']}), edge H/tau={r['H_over_tau']:.3f}, "
                        f"kappa={r['kappa']:.4f}\n")
            f.write("\n")
        f.write(SYNTH_TAIL)


SYNTH_TAIL = """### The conjectured quantitative inequality (filled by the runner's final synthesis)

The slope ddelta_min/dt is the shadow price of forcing the financier's height; if it is
negative and bounded away from 0 as H -> wall, then driving the financier DOWN (to hide it in
the far top band) costs negativity at that rate -- the quantitative core of top-band
localization.  See the runner's closing message for the fitted constants and the
[NUMERICAL]/[GUESS] tags on the conjectured  delta >= c1 * t_deficit * H + c2 * H^2  form.
"""


# ======================================================================
def main():
    t0 = time.time()
    print("[d10] joint certificate mining: PROBE 1 (M_far grid) + PROBE 2 (financier duals)",
          flush=True)
    write_header()
    res = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": C, "c": c,
                    "sigmas_p1": SIGMAS_P1, "htau_targets": HTAU_TARGETS,
                    "sigmas_p2": SIGMAS_P2, "k_groups": KG, "ell": ELL,
                    "gurobi": "Presolve=0, Method=1, FeasTol=OptTol=1e-9 (sep/exposedness LPs)",
                    "normalization": "delta=max-row-neg, tau=sqrt(delta)"},
           "probe1": [], "probe2": []}

    # ---------- PROBE 1 ----------
    print("\n[d10] PROBE 1 -- far top-band mass grid", flush=True)
    p1 = []
    for sig in SIGMAS_P1:
        for ht in HTAU_TARGETS:
            print(f"  cell sigma_v={sig:.2f} H/tau~{ht:.2f} ...", flush=True)
            try:
                rec = probe1_cell(sig, ht)
            except Exception as e:
                import traceback; traceback.print_exc()
                rec = {"sigma_v": sig, "htau_target": ht, "status": "ERROR", "error": str(e)}
            p1.append(rec); res["probe1"] = p1
            with open(OUT, "w") as f:
                json.dump(res, f, indent=2, default=float)
            if rec.get("status") == "OK":
                print(f"    -> H/tau={rec['H_over_tau']:.3f} d/H2={rec['delta_over_H2']:.3f} "
                      f"M_far={rec['M_far']:.4f} (f1={rec['feed1_direct']:.4f}, "
                      f"f2={rec['feed2_carrier']:.4f}) #ftb={rec['n_far_topband']} "
                      f"occ={rec['far_topband_occupants_by_role']}", flush=True)
            else:
                print(f"    -> {rec.get('status')}", flush=True)

    # ---------- PROBE 2 ----------
    print("\n[d10] PROBE 2 -- financier-height perturbation duals", flush=True)
    p2 = []
    for sig in SIGMAS_P2:
        print(f"  collapse-edge sigma_v={sig:.2f} ...", flush=True)
        try:
            rec = probe2_cell(sig)
        except Exception as e:
            import traceback; traceback.print_exc()
            rec = {"sigma_v": sig, "status": "ERROR", "error": str(e)}
        p2.append(rec); res["probe2"] = p2
        with open(OUT, "w") as f:
            json.dump(res, f, indent=2, default=float)
        if rec.get("status") == "OK":
            print(f"    -> edge d={rec['d_edge']:.4f} financier={rec['financier_role']} "
                  f"slope ddelta/dg_f={rec['fit_slope_ddelta_dgf']} (R2={rec['fit_r2']})", flush=True)
        else:
            print(f"    -> {rec.get('status')}", flush=True)

    # ---------- report ----------
    append_probe1_table(p1)
    append_probe2_sections(p2)
    append_synthesis(p1, p2)
    res["meta"]["elapsed_s"] = time.time() - t0
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d10] DONE ({res['meta']['elapsed_s']:.1f}s). Wrote {OUT} and {NOTE}", flush=True)


if __name__ == "__main__":
    main()
