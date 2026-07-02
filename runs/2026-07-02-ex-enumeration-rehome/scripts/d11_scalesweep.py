#!/usr/bin/env python3 -u
"""
d11_scalesweep.py -- DISAMBIGUATE the d10 scale degeneracy + run the wave-7 M-minimization.

d10 PROBE 2 found delta_min = (1/2) g_f (R^2=1) and reported g_f = H -- but PROBED ONLY at the
default family scale, where the collapse edge sits at delta ~ 0.0718 and H = 2*delta EXACTLY,
making "g_f = H" and "g_f = 2*delta" numerically INDISTINGUISHABLE.

TASK A (disambiguation, PRIORITY 1).  Replicate d10's financier-law mining at family scales
spanning >= 2 decades of delta by sweeping the collapse edge over a sigma_v ladder
(sigma_v in {0.05,0.10,0.15,0.20,0.30,0.40,0.50}).  Lower sigma_v collapses earlier (smaller
edge delta) AND in the BUDGET regime (H/tau < 0.536), so H/tau VARIES across the ladder
(0.045 .. 0.533).  At EACH edge record SEPARATELY g_f, H, delta, tau, kappa*osc, and the ratios
g_f/H, g_f/(2 delta), g_f/(kappa*osc); plus the forced-height curve t->delta_min(t) and its slope.
Every point passes d8_mrp3.verify (idem_resid<1e-7, multiplicity-correct W, robust exposedness
presolve OFF, honest tau=sqrt(delta)).

DECISION OUTPUT (TASK A): which reading survives -- g_f tracks H, or g_f tracks 2*delta, or
neither/crossover; does the slope 1/2 persist across scales.

TASK B (the wave-7 aggregate-coupling minimization, PRIORITY 2).  Minimize
    M := sum_b mu_b sum_{j in A_v} lambda_j P+_{jb}
where lambda_j = P+_{vj}/sigma_v (v's normalized positive carrier measure) and mu is a C10
failed-exposedness witness measure on rho-far top-band blocker rows b (the exposedness-LP dual
multipliers, presolve OFF).  We MEASURE M on the verified hidden edge instance at the default
scale and one small scale (sigma_v ~ 0.30, delta ~ 0.026), and also over the financier-height
sweep (the family's remaining realization freedom).  DECISION: min M = 0 (coupling lemma FALSE
as stated) vs min M >= c*tau (record c + the binding dual).

Outputs (crash-safe):
  out/d11_scalesweep.json
  ../notes/d11-scale-disambiguation.md
  out/d11_logs/<...>.log
"""
import os, sys, json, time
import numpy as np

import gurobipy as gp
from gurobipy import GRB

from d8_mrp3 import build, verify
from d8_opt import decide_opt
from d9_duals import role_of, exposed_dual_gurobi
from d10_certmine import canonical_separator

OUT = os.path.join("out", "d11_scalesweep.json")
LOGDIR = os.path.join("out", "d11_logs")
NOTE = os.path.join("..", "notes", "d11-scale-disambiguation.md")
os.makedirs(LOGDIR, exist_ok=True)
os.makedirs("out", exist_ok=True)

C, c = 4.0, 0.25
# sigma_v ladder: spans the budget regime so the collapse edge delta spans >= 2 decades
# (d10 catch: at the wall edge sigma_v>=0.5 delta is LOCKED ~0.07; lower sigma_v collapses
#  earlier => smaller edge delta AND H/tau<0.536 so H != 2delta is testable separately).
SIGMA_LADDER = [0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]
KG = 2
ELL = 0.75
TASKB_SIGMAS = [0.50, 0.30]   # default-scale + one small scale


# ======================================================================
# Collapse-edge finder (largest hiding d that still verifies).  Honest:
# every accepted instance passes d8_mrp3.verify entry gate.
# ======================================================================
def find_edge(sig, kg=KG, ell=ELL, dlo=0.008, dhi=0.40, dstep=0.004, n_starts=1):
    last = None
    d = dlo
    while d < dhi:
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=n_starts)
        v = r2.get("verify", {})
        if v.get("entry_pass") and v.get("delta_over_H2"):
            last = (float(d), r2)
        elif last is not None:
            break
        d += dstep
    if last is None:
        return None
    # refine upward with more starts to push d to the largest hiding value
    d0 = last[0]
    d = d0
    while d < d0 + 0.006:
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=2)
        v = r2.get("verify", {})
        if v.get("entry_pass") and v.get("delta_over_H2") and d >= last[0]:
            last = (float(d), r2)
        d += 0.0005
    return last


def identify_financier(P, idx, ver, logfile=None):
    """Binding far top-band financier f = dominant-Pi frame-financing blocker of v (d9/d10)."""
    v = idx["v"]; tau = ver["tau"]; rho, kappa = C * tau, c * tau
    vexp = exposed_dual_gurobi(P, v, rho, kappa, idx, logfile=logfile)
    bls = vexp.get("blockers", [])
    fin = [b for b in bls if b["role"].startswith("frame-financing")]
    if fin:
        return fin[0], vexp
    if bls:
        return bls[0], vexp
    return None, vexp


# ======================================================================
# TASK A -- per-scale financier-law record + forced-height curve.
# ======================================================================
def financier_height_curve(sig, f_row, d_edge, kg=KG, ell=ELL, logfile=None, npts=8):
    """Sweep d DOWN from the collapse edge; at each VERIFIED instance measure the canonical
       financier height g_f and delta_min (= the load-bearing min-neg LP value).  Returns the
       (g_f -> delta_min) curve with H and 2*delta alongside so the readings are separable."""
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
        delta = float(ver["delta"]); H = float(ver["H_real"])
        curve.append({"d": float(d), "g_f": g_f,
                      "delta_min": float(r2.get("mneg_lp")),
                      "delta": delta, "two_delta": 2.0 * delta, "H": H,
                      "H_over_tau": float(ver["H_over_tau"]),
                      "idem_resid": float(ver.get("idem_resid", 0.0))})
    return curve


def fit_slope(curve):
    pts = [(p["g_f"], p["delta_min"]) for p in curve
           if p.get("delta_min") is not None and p.get("g_f") is not None]
    if len(pts) < 2:
        return None, None, None
    ts = np.array([p[0] for p in pts]); ds = np.array([p[1] for p in pts])
    A = np.vstack([ts, np.ones_like(ts)]).T
    sol, *_ = np.linalg.lstsq(A, ds, rcond=None)
    pred = A @ sol
    ss_res = float(((ds - pred) ** 2).sum())
    ss_tot = float(((ds - ds.mean()) ** 2).sum())
    r2 = float(1 - ss_res / ss_tot) if ss_tot > 1e-18 else 1.0
    return float(sol[0]), float(sol[1]), r2


def taskA_cell(sig):
    log = os.path.join(LOGDIR, f"A_sig{sig:.2f}.log")
    open(log, "w").close()
    edge = find_edge(sig)
    if edge is None:
        return {"sigma_v": sig, "status": "UNREACHABLE",
                "note": "no verified hidden instance at any d for this sigma_v"}
    d_edge, r2 = edge
    ver = r2["verify"]; P = np.array(r2["P"]); idx = r2["idx"]
    tau = ver["tau"]; rho, kappa = C * tau, c * tau
    # canonical separator + deficit g at the EDGE instance
    sep = canonical_separator(P, idx["v"], ver["W"], logfile=log)
    if sep is None or sep.get("solver_failed"):
        return {"sigma_v": sig, "status": "SEP_FAILED", "d_edge": d_edge}
    g = np.array(sep["g"])
    osc = float(g.max() - g.min())
    kappa_osc = kappa * osc
    f, vexp = identify_financier(P, idx, ver, logfile=log)
    if f is None:
        return {"sigma_v": sig, "status": "NO_FINANCIER", "d_edge": d_edge}
    f_row = f["row"]
    g_f = float(g[f_row])
    H = float(ver["H_real"]); delta = float(ver["delta"])
    # the three readings, resolved
    rec = {
        "sigma_v": sig, "status": "OK", "d_edge": float(d_edge),
        "delta": delta, "tau": float(tau), "kappa": float(kappa),
        "H": H, "two_delta": 2.0 * delta, "H_over_tau": float(ver["H_over_tau"]),
        "delta_over_H2": float(ver["delta_over_H2"]),
        "g_f": g_f, "osc_g": osc, "kappa_osc": kappa_osc,
        "financier_row": int(f_row), "financier_role": f["role"],
        "financier_Pi": float(f["Pi"]),
        # ratios (the disambiguation):
        "ratio_gf_over_H": (g_f / H) if H > 1e-12 else None,
        "ratio_gf_over_2delta": (g_f / (2 * delta)) if delta > 1e-12 else None,
        "ratio_gf_over_kappaosc": (g_f / kappa_osc) if kappa_osc > 1e-12 else None,
        "ratio_H_over_2delta": (H / (2 * delta)) if delta > 1e-12 else None,
        "idem_resid": float(ver.get("idem_resid", 0.0)),
        "nW": ver["nW"], "verify_pass": True,
    }
    # forced-height curve + slope
    curve = financier_height_curve(sig, f_row, d_edge, logfile=log)
    slope, intercept, r2fit = fit_slope(curve)
    rec["curve"] = curve
    rec["fit_slope_ddelta_dgf"] = slope
    rec["fit_intercept"] = intercept
    rec["fit_r2"] = r2fit
    return rec


# ======================================================================
# TASK B -- aggregate-coupling M = sum_b mu_b sum_{j in A_v} lambda_j P+_{jb}.
#   lambda_j = P+_{vj}/sigma_v  (v's normalized positive off-site carrier measure)
#   mu       = C10 witness on rho-far top-band blocker rows b (exposedness-LP duals, normalized)
# ======================================================================
def carrier_measure(P, v, sigma_v):
    """lambda_j = P+_{vj}/sigma_v over off-site positive carriers A_v = {j != v : P_vj > 0}.
       sigma_v here is the ACTUAL positive off-site mass (re-measured, honest)."""
    Pv = np.asarray(P[v], float)
    A_v = [j for j in range(P.shape[0]) if j != v and Pv[j] > 1e-12]
    mass = float(sum(Pv[j] for j in A_v))
    lam = {j: float(Pv[j] / mass) for j in A_v} if mass > 1e-15 else {}
    return A_v, lam, mass


def c10_witness_measure(P, idx, ver, logfile=None):
    """mu on rho-far TOP-BAND blocker rows b: the binding far-row exposedness duals |Pi|,
       restricted to rows that are BOTH rho-far AND in the top band (g_b < kappa*osc), then
       normalized to a probability measure.  (The C10 failed-exposedness witness lives on the
       far blockers; we keep only the top-band ones, the loiterers the lemma is about.)"""
    P = np.asarray(P, float)
    v = idx["v"]; tau = ver["tau"]; rho, kappa = C * tau, c * tau
    vexp = exposed_dual_gurobi(P, v, rho, kappa, idx, logfile=logfile)
    bls = vexp.get("blockers", [])
    sep = canonical_separator(P, v, ver["W"], logfile=logfile)
    g = np.array(sep["g"]); osc = float(g.max() - g.min())
    band = kappa * osc
    di = np.abs(P - P[v]).sum(axis=1)
    raw = {}
    for b in bls:
        bb = b["row"]
        if di[bb] >= rho - 1e-12 and g[bb] < band - 1e-15:
            raw[bb] = raw.get(bb, 0.0) + abs(b["Pi"])
    tot = float(sum(raw.values()))
    mu = {b: w / tot for b, w in raw.items()} if tot > 1e-15 else {}
    return mu, raw, band, osc, vexp


def aggregate_coupling_M(P, idx, ver, logfile=None):
    """M = sum_b mu_b sum_{j in A_v} lambda_j P+_{jb}, in raw units and in units of tau."""
    P = np.asarray(P, float)
    v = idx["v"]; tau = ver["tau"]
    A_v, lam, vmass = carrier_measure(P, v, ver.get("sigma_v", 1.0))
    mu, mu_raw, band, osc, vexp = c10_witness_measure(P, idx, ver, logfile=logfile)
    if not mu or not lam:
        return {"M": None, "M_over_tau": None, "n_blockers_topband": len(mu),
                "n_carriers": len(A_v), "note": "empty mu or lambda",
                "mu_blockers": {role_of(b, idx): float(w) for b, w in mu.items()}}
    M = 0.0
    contrib = {}
    for b, mub in mu.items():
        inner = 0.0
        for j, lamj in lam.items():
            pjb = max(P[j, b], 0.0)
            inner += lamj * pjb
        M += mub * inner
        contrib[role_of(b, idx)] = contrib.get(role_of(b, idx), 0.0) + mub * inner
    return {
        "M": float(M), "M_over_tau": float(M / tau) if tau > 0 else None,
        "tau": float(tau), "n_blockers_topband": len(mu),
        "n_carriers": len(A_v),
        "carrier_roles": {role_of(j, idx): float(w) for j, w in lam.items()},
        "mu_blockers": {role_of(b, idx): float(w) for b, w in mu.items()},
        "M_contrib_by_blocker_role": contrib,
        "band_thresh_g": float(band), "osc_g": float(osc),
    }


def taskB_cell(sig):
    log = os.path.join(LOGDIR, f"B_sig{sig:.2f}.log")
    open(log, "w").close()
    edge = find_edge(sig)
    if edge is None:
        return {"sigma_v": sig, "status": "UNREACHABLE"}
    d_edge, r2 = edge
    ver = r2["verify"]; P = np.array(r2["P"]); idx = r2["idx"]
    # M at the edge instance
    M_edge = aggregate_coupling_M(P, idx, ver, logfile=log)
    # M over the family's realization freedom: sweep d down from the edge (the only free
    # scale knob with v's far geometry pinned), take the MINIMUM verified M.
    d_grid = np.linspace(0.40 * d_edge, d_edge, 6)
    sweep = []
    M_min = M_edge.get("M_over_tau")
    for d in d_grid:
        r3 = decide_opt(float(d), sig, k_groups=KG, ell=ELL, ma=2, nlow=2,
                        pin_level="load_bearing", n_starts=1)
        v3 = r3.get("verify", {})
        if not (v3.get("entry_pass") and v3.get("delta_over_H2")):
            continue
        P3 = np.array(r3["P"]); idx3 = r3["idx"]
        Mr = aggregate_coupling_M(P3, idx3, v3, logfile=log)
        if Mr.get("M_over_tau") is not None:
            sweep.append({"d": float(d), "delta": float(v3["delta"]),
                          "M": Mr["M"], "M_over_tau": Mr["M_over_tau"],
                          "n_blockers_topband": Mr["n_blockers_topband"]})
            if M_min is None or Mr["M_over_tau"] < M_min:
                M_min = Mr["M_over_tau"]
    return {
        "sigma_v": sig, "status": "OK", "d_edge": float(d_edge),
        "delta_edge": float(ver["delta"]), "tau_edge": float(ver["tau"]),
        "M_edge": M_edge, "M_sweep": sweep,
        "M_over_tau_min": M_min,
        "idem_resid": float(ver.get("idem_resid", 0.0)),
    }


# ======================================================================
# Report writer (incremental).
# ======================================================================
HEADER = """# d11 -- Scale disambiguation of the d10 financier law + wave-7 M-minimization

**Date:** 2026-06-10/11 - **Scope:** exploration only
(`agent-A/explorations/classical-portfolio/experiments/`), NOT committed to canonical layers.
**Agent:** numerics worker (d11), exploration lane.

Mission: resolve the d10 PROBE-2 scale degeneracy (it probed only the default scale where the
collapse edge has delta ~ 0.0718 and H = 2*delta EXACTLY, so "g_f = H" and "g_f = 2*delta" were
indistinguishable) by sweeping the collapse edge across >= 2 decades of delta; and run the
wave-7 aggregate-coupling minimization M = sum_b mu_b sum_{j in A_v} lambda_j P+_{jb}.

VERIFICATION GATE (every reported point): d8_mrp3.verify -- idem_resid<1e-7, multiplicity-correct
W (d3_vertexfix), robust exposedness (presolve OFF), honest tau=sqrt(delta).  gurobi separator/
exposedness LPs: Presolve=0, Method=1 (dual simplex), FeasTol=OptTol=1e-9.  Tags: [NUMERICAL]/[GUESS].

---
"""


def write_header():
    with open(NOTE, "w") as f:
        f.write(HEADER)


def append_taskA(records):
    with open(NOTE, "a") as f:
        f.write("\n## TASK A -- delta-scale sweep of the financier law (the disambiguation)\n\n")
        f.write("Collapse edge swept over a sigma_v ladder (budget regime: lower sigma_v "
                "collapses earlier, so the edge delta spans decades AND H/tau varies, breaking "
                "the H=2delta degeneracy *if* the family allows it).\n\n")
        f.write("| sigma_v | d_edge | delta | H | 2delta | H/tau | kappa*osc | g_f | "
                "g_f/H | g_f/2delta | g_f/(k*osc) | H/2delta | slope | R^2 |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for r in records:
            if r.get("status") != "OK":
                f.write(f"| {r['sigma_v']:.2f} | _{r.get('status')}_ | - | - | - | - | - | - "
                        f"| - | - | - | - | - | - |\n")
                continue
            def fmt(x, p=5):
                return f"{x:.{p}f}" if isinstance(x, (int, float)) and x is not None else "-"
            f.write(f"| {r['sigma_v']:.2f} | {fmt(r['d_edge'])} | {fmt(r['delta'])} | "
                    f"{fmt(r['H'])} | {fmt(r['two_delta'])} | {fmt(r['H_over_tau'],4)} | "
                    f"{fmt(r['kappa_osc'])} | {fmt(r['g_f'])} | "
                    f"{fmt(r['ratio_gf_over_H'],4)} | {fmt(r['ratio_gf_over_2delta'],4)} | "
                    f"{fmt(r['ratio_gf_over_kappaosc'],4)} | {fmt(r['ratio_H_over_2delta'],4)} | "
                    f"{fmt(r['fit_slope_ddelta_dgf'],4)} | {fmt(r['fit_r2'],4)} |\n")
        f.write("\n")
        # per-cell forced-height curves
        for r in records:
            if r.get("status") != "OK":
                continue
            f.write(f"\n### sigma_v = {r['sigma_v']:.2f}  forced-height curve "
                    f"(edge d={r['d_edge']:.4f}, financier={r['financier_role']})\n\n")
            f.write("| g_f | delta_min | H | 2delta | H/tau |\n|---|---|---|---|---|\n")
            for p in r["curve"]:
                if p.get("delta_min") is None:
                    f.write(f"| {p.get('g_f')} | INFEAS/sep-fail | - | - | - |\n"); continue
                f.write(f"| {p['g_f']:.5f} | {p['delta_min']:.5f} | {p['H']:.5f} | "
                        f"{p['two_delta']:.5f} | {p['H_over_tau']:.4f} |\n")
            f.write(f"\n- fit: delta_min = {r['fit_slope_ddelta_dgf']} * g_f + "
                    f"{r['fit_intercept']}  (R^2={r['fit_r2']})\n")


def append_taskB(records):
    with open(NOTE, "a") as f:
        f.write("\n## TASK B -- wave-7 aggregate-coupling minimization M\n\n")
        f.write("M := sum_b mu_b sum_{j in A_v} lambda_j P+_{jb};  "
                "lambda = v's normalized positive carrier measure, "
                "mu = C10 exposedness-dual witness on rho-far TOP-BAND blockers (normalized).\n\n")
        f.write("| sigma_v | delta_edge | M (edge) | M/tau (edge) | min M/tau (sweep) | "
                "#topband blockers | mu blocker roles |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for r in records:
            if r.get("status") != "OK":
                f.write(f"| {r['sigma_v']:.2f} | _{r.get('status')}_ | - | - | - | - | - |\n")
                continue
            me = r["M_edge"]
            roles = ", ".join(f"{k}:{v:.2f}" for k, v in
                              me.get("mu_blockers", {}).items()) or "(none)"
            Mv = me.get("M"); Mt = me.get("M_over_tau"); Mm = r.get("M_over_tau_min")
            f.write(f"| {r['sigma_v']:.2f} | {r['delta_edge']:.5f} | "
                    f"{Mv if Mv is None else f'{Mv:.5f}'} | "
                    f"{Mt if Mt is None else f'{Mt:.4f}'} | "
                    f"{Mm if Mm is None else f'{Mm:.4f}'} | "
                    f"{me.get('n_blockers_topband')} | {roles} |\n")
        f.write("\n")


def main():
    t0 = time.time()
    print("[d11] scale disambiguation (TASK A) + M-minimization (TASK B)", flush=True)
    write_header()
    res = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": C, "c": c,
                    "sigma_ladder": SIGMA_LADDER, "taskB_sigmas": TASKB_SIGMAS,
                    "k_groups": KG, "ell": ELL,
                    "gurobi": "Presolve=0, Method=1, FeasTol=OptTol=1e-9 (sep/exposedness LPs)",
                    "normalization": "delta=max-row-neg, tau=sqrt(delta)"},
           "taskA": [], "taskB": []}

    # ---------- TASK A ----------
    print("\n[d11] TASK A -- delta-scale sweep of the financier law", flush=True)
    A = []
    for sig in SIGMA_LADDER:
        print(f"  edge sigma_v={sig:.2f} ...", flush=True)
        try:
            rec = taskA_cell(sig)
        except Exception as e:
            import traceback; traceback.print_exc()
            rec = {"sigma_v": sig, "status": "ERROR", "error": str(e)}
        A.append(rec); res["taskA"] = A
        with open(OUT, "w") as f:
            json.dump(res, f, indent=2, default=float)
        if rec.get("status") == "OK":
            print(f"    -> delta={rec['delta']:.5f} H={rec['H']:.5f} 2d={rec['two_delta']:.5f} "
                  f"g_f={rec['g_f']:.5f} | g_f/H={rec['ratio_gf_over_H']:.3f} "
                  f"g_f/2d={rec['ratio_gf_over_2delta']:.3f} H/2d={rec['ratio_H_over_2delta']:.3f} "
                  f"slope={rec['fit_slope_ddelta_dgf']} R2={rec['fit_r2']}", flush=True)
        else:
            print(f"    -> {rec.get('status')}", flush=True)

    # ---------- TASK B ----------
    print("\n[d11] TASK B -- aggregate-coupling minimization M", flush=True)
    B = []
    for sig in TASKB_SIGMAS:
        print(f"  M-min sigma_v={sig:.2f} ...", flush=True)
        try:
            rec = taskB_cell(sig)
        except Exception as e:
            import traceback; traceback.print_exc()
            rec = {"sigma_v": sig, "status": "ERROR", "error": str(e)}
        B.append(rec); res["taskB"] = B
        with open(OUT, "w") as f:
            json.dump(res, f, indent=2, default=float)
        if rec.get("status") == "OK":
            me = rec["M_edge"]
            print(f"    -> M(edge)={me.get('M')} M/tau(edge)={me.get('M_over_tau')} "
                  f"min M/tau={rec.get('M_over_tau_min')} "
                  f"#tb-blockers={me.get('n_blockers_topband')}", flush=True)
        else:
            print(f"    -> {rec.get('status')}", flush=True)

    # ---------- report ----------
    append_taskA(A)
    append_taskB(B)
    res["meta"]["elapsed_s"] = time.time() - t0
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d11] DONE ({res['meta']['elapsed_s']:.1f}s). Wrote {OUT} and {NOTE}", flush=True)


if __name__ == "__main__":
    main()
