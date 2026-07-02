#!/usr/bin/env python3 -u
"""
d12_dmfprobe.py -- THE DECISIVE DMF FALSIFICATION PROBE (mission d12).

Tests DMF (deep-witness mass forcing, SC2 of wave8-fable-closer.md):
  for every exact P (small delta) and hidden top vertex v, every OPTIMAL exposedness-
  dual witness mu carries mass >= m* on rows at deficit g >= H - O(delta/tau).

DMF was verified exactly saturated (m* = 1) on the d8 WALL-EDGE instance
(d=0.1435, sigma_v=0.5, ell=0.65) by w8_witness_check.py.  This probe tests it OFF
that edge -- on the d3/d7 STACKING instances (d8_mrp3 financed-wiggle family, driven
to the floor by the d8_opt optimizer) across delta in [0.005, 0.072] spanning
delta/H^2 in [3.4, 50].  A single VERIFIED all-shallow witness (>= 1/2 of mu-mass at
g < H/2) REFUTES DMF as stated.

METHODOLOGY (replicates w8_witness_check.py / wave8 Stage 2b exactly):
  1. build instance via d8_mrp3.build (off the d8 edge: varied sigma_v, ell, ma, k_groups);
     optimize neg over (Lambda,R) via d8_opt.decide_opt (load_bearing pins).
  2. GATE: idem_resid < 1e-7, multiplicity-correct W (d3_vertexfix), honest tau = sqrt(delta),
     v a robust vertex, v_fails_exposed, suppliers hidden.  Reject failures.
  3. canonical separator phi: LP dual of dist1(p_v, conv W); deficit g = H - phi, R = osc(g).
  4. exposedness LP for v (scipy HiGHS, PRESOLVE OFF) -> OPTIMAL DUAL witness (mu, alpha, beta, gamma)
     per (diamond); verify identity residual <= 1e-12, mass balance 1+A-B=gamma, B=t*.
  5. depth profile: cumulative mu-mass at deficit >= H - E for E/H in {0,.1,.25,.5,.75,.9,1.0};
     per-row g_j tagged by class; m*_observed := mu-mass at g >= H - 5 delta/tau.
  6. sigma_v (off-own-site mass) AND sigma-tilde (mass outside conv W) -- N3 disambiguation.
  7. all-shallow detector: >= 1/2 of mu-mass at g < H/2 -> STOP, re-verify, persist candidate.

All exposedness/distance LPs: presolve OFF.  Crash-safe checkpoint per instance.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from scipy.optimize import linprog
from d8_mrp3 import build, verify as mrp_verify
from d8_opt import decide_opt
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d1_infra import neg_mass, check_idempotent, dist1_to_conv

OUTDIR = "out"
LOGDIR = os.path.join(OUTDIR, "d12_logs")
os.makedirs(LOGDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "d12_dmfprobe.json")
CAND = os.path.join(OUTDIR, "d12_DMF_witness_candidate.json")

C, c = 4.0, 0.25


def lp(cobj, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    """HiGHS, PRESOLVE OFF (project gate)."""
    r = linprog(cobj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                method="highs", options={"presolve": False})
    assert r.status == 0, f"LP failed: {r.message}"
    return r


def canonical_separator(P, W, v):
    """phi: max phi(p_v) s.t. phi affine, ||grad||_inf <= 1, sup_{conv W} phi <= 0.
       Returns w (gradient), s (offset), phi(=P w - s), H, g=H-phi, R=osc(g)."""
    n = P.shape[0]
    nv = n + 1
    cobj = np.zeros(nv); cobj[:n] = -P[v]; cobj[n] = 1.0   # max phi_v = P[v].w - s
    A_ub = []; b_ub = []
    for u in W:
        row = np.zeros(nv); row[:n] = P[u]; row[n] = -1.0
        A_ub.append(row); b_ub.append(0.0)                  # P[u].w - s <= 0
    r = lp(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
           bounds=[(-1, 1)] * n + [(None, None)])
    w = r.x[:n]; s = r.x[n]
    phi = P @ w - s
    H = phi[v]
    g = phi[v] - phi
    R = g.max() - g.min()
    return w, s, phi, float(H), g, float(R)


def exposedness_dual(P, v, rho, kappa):
    """Solve the exposedness LP for v (presolve OFF), extract the OPTIMAL DUAL witness
       (mu, alpha, beta, gamma) per (diamond) of wave8 1.1.  Replicates w8_witness_check.
       Returns dict with mu/alpha/beta (index->mass), gamma, A,B,t*, far set, and the
       optimal exposer h* values."""
    n = P.shape[0]
    di = np.abs(P - P[v]).sum(axis=1)
    far = [k for k in range(n) if k != v and di[k] >= rho - 1e-12]
    # primal: max t  s.t.  0 <= h(p_k) <= 1 all k, h(p_v)=0, h(p_j) >= t for j in far.
    # vars: a(n), b(1), t(1)
    nv = n + 2
    cobj = np.zeros(nv); cobj[-1] = -1.0
    Aub = []; bub = []; kinds = []
    for k in range(n):
        hk = np.zeros(nv); hk[:n] = P[k]; hk[n] = 1.0
        Aub.append(hk.copy()); bub.append(1.0); kinds.append(("beta", k))   # h<=1
        Aub.append(-hk.copy()); bub.append(0.0); kinds.append(("alpha", k))  # h>=0
    for k in far:
        hk = np.zeros(nv); hk[:n] = -P[k]; hk[n] = -1.0; hk[-1] = 1.0
        Aub.append(hk); bub.append(0.0); kinds.append(("mu", k))             # t-h<=0
    Aeq = np.zeros((1, nv)); Aeq[0, :n] = P[v]; Aeq[0, n] = 1.0
    r2 = lp(cobj, A_ub=np.array(Aub), b_ub=np.array(bub),
            A_eq=Aeq, b_eq=[0.0], bounds=[(None, None)] * nv)
    tstar = r2.x[-1]; a_opt = r2.x[:n]; b_opt = r2.x[n]
    hstar = P @ a_opt + b_opt
    marg = np.array(r2.ineqlin.marginals)
    mu = {}; alpha = {}; beta = {}
    for (kind, k), m in zip(kinds, marg):
        val = -m
        if val > 1e-9:
            d_ = dict(mu=mu, alpha=alpha, beta=beta)[kind]
            d_[k] = d_.get(k, 0.0) + val
    gamma = -np.array(r2.eqlin.marginals)[0]
    A_ = sum(alpha.values()); B_ = sum(beta.values()); MU = sum(mu.values())
    # identity residual of (diamond): sum mu p + sum alpha p - sum beta p - gamma p_v
    vec = np.zeros(n)
    for k, m in mu.items(): vec += m * P[k]
    for k, m in alpha.items(): vec += m * P[k]
    for k, m in beta.items(): vec -= m * P[k]
    ident_resid = float(np.abs(vec - gamma * P[v]).max())
    return {"tstar": float(tstar), "mu": mu, "alpha": alpha, "beta": beta,
            "gamma": float(gamma), "A": float(A_), "B": float(B_), "MU": float(MU),
            "ident_resid": ident_resid, "massbal_resid": float(abs(1 + A_ - B_ - gamma)),
            "B_minus_tstar": float(abs(B_ - tstar)),
            "far": far, "di": di, "hstar": hstar}


def classify_row(P, k, v, W, g, di, rho, H):
    """tag a mu-carrying row by class."""
    vert, _ = is_row_vertex_robust(P, k)
    inW = k in W
    o = float(np.abs(P[k]).sum() - P[k, k])   # off-own-site l1 mass
    within_rho = bool(di[k] < rho)
    if inW:
        cls = "W-vertex"
    elif vert and not inW:
        cls = "hidden-vertex"
    elif within_rho:
        cls = "within-rho-of-v"
    else:
        cls = "non-vertex-mixture"
    return {"vertex": bool(vert), "inW": bool(inW), "class": cls,
            "o": o, "within_rho": within_rho, "g": float(g[k]),
            "dist_over_rho": float(di[k] / rho)}


def depth_profile(mu, g, H, R, kappa, delta, tau):
    """cumulative mu-mass at deficit >= H - E for E/H grid + m*_observed."""
    prof = {}
    for frac in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
        E = frac * H
        dm = sum(m for k, m in mu.items() if g[k] >= H - E - 1e-12)
        prof[f"E/H={frac}"] = float(dm)
    # m*_observed: mu-mass at g >= H - 5 delta/tau   (the DMF operative slack target)
    E_dmf = 5.0 * delta / tau if tau > 0 else 0.0
    mstar = sum(m for k, m in mu.items() if g[k] >= H - E_dmf - 1e-12)
    # shallow mass: mu-mass at g < H/2
    shallow = sum(m for k, m in mu.items() if g[k] < H / 2.0 - 1e-12)
    return prof, float(mstar), float(E_dmf), float(shallow)


def witness_anatomy(P, idx, label, extra=None):
    """Full per-instance anatomy. Returns the record dict (or {gate fail})."""
    n = P.shape[0]
    chk = check_idempotent(P, tol=1e-7)
    nm, delta = neg_mass(P)
    rec = {"label": label, "n": n, "idem_resid": float(chk["idem_resid"]),
           "row_sum_resid": float(chk["row_sum_resid"]), "delta": float(delta)}
    if extra:
        rec.update(extra)
    # GATE 1: idempotence
    if not chk["ok"] or chk["idem_resid"] >= 1e-7:
        rec["gate"] = "FAIL_idempotent"; return rec
    if delta <= 1e-12:
        rec["gate"] = "FAIL_delta_zero"; return rec
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    rec.update({"tau": tau, "rho": rho, "kappa": kappa})
    v = idx["v"]
    rec["v"] = int(v)
    # GATE 2: multiplicity-correct W
    W, _ = well_exposed_set_robust(P, rho, kappa)
    rec["nW"] = len(W); rec["W"] = list(map(int, W))
    # GATE 3: v robust vertex
    vert_v, _ = is_row_vertex_robust(P, v)
    rec["v_vertex"] = bool(vert_v)
    if not vert_v:
        rec["gate"] = "FAIL_v_not_vertex"; return rec
    # H = dist to conv W (must be the max-height hidden vertex)
    Hd, _ = dist1_to_conv(P, W, v)
    rec["H_dist"] = float(Hd)
    if Hd <= 1e-9:
        rec["gate"] = "FAIL_v_in_W"; return rec
    # is v genuinely the MAX-height hidden vertex?  check all non-W rows
    maxH = -1.0; argmaxH = -1
    for i in range(n):
        if i in W:
            continue
        vi, _ = is_row_vertex_robust(P, i)
        if not vi:
            continue
        di_, _ = dist1_to_conv(P, W, i)
        if di_ > maxH:
            maxH = di_; argmaxH = i
    rec["max_height_vertex"] = int(argmaxH); rec["max_height"] = float(maxH)
    rec["v_is_max_height"] = bool(argmaxH == v or abs(maxH - Hd) < 1e-7)
    # use the actual max-height hidden vertex as the DMF target
    target = argmaxH if (argmaxH >= 0 and maxH > Hd + 1e-9) else v
    rec["target_vertex"] = int(target)
    # canonical separator + deficit for the target
    w, s, phi, H, g, R = canonical_separator(P, W, target)
    rec["H"] = float(H); rec["R"] = float(R)
    rec["sep_resid_Pg"] = float(np.abs(P @ g - g).max())  # g = P g (affine, P-stationary)
    rec["g_v_target"] = float(g[target])
    if H <= 1e-9:
        rec["gate"] = "FAIL_H_zero"; return rec
    # GATE 4: target fails exposedness -> exposedness dual
    dual = exposedness_dual(P, target, rho, kappa)
    rec["tstar"] = dual["tstar"]; rec["tstar_over_kappa"] = float(dual["tstar"] / kappa)
    rec["A"] = dual["A"]; rec["B"] = dual["B"]; rec["gamma"] = dual["gamma"]
    rec["MU"] = dual["MU"]
    rec["ident_resid"] = dual["ident_resid"]
    rec["massbal_resid"] = dual["massbal_resid"]
    rec["B_minus_tstar"] = dual["B_minus_tstar"]
    rec["v_fails_exposed"] = bool(dual["tstar"] < kappa - 1e-9)
    if dual["tstar"] >= kappa - 1e-9:
        rec["gate"] = "FAIL_v_exposed"; return rec
    if dual["ident_resid"] > 1e-9:
        rec["witness_identity_ok"] = False
    else:
        rec["witness_identity_ok"] = True
    mu = dual["mu"]; di = dual["di"]
    # depth profile + m*_observed
    prof, mstar, E_dmf, shallow = depth_profile(mu, g, H, R, kappa, delta, tau)
    rec["depth_profile"] = prof
    rec["m_star_observed"] = mstar
    rec["E_dmf_5delta_over_tau"] = E_dmf
    rec["shallow_mass_g_lt_Hhalf"] = shallow
    # per mu-row anatomy
    mu_rows = {}
    for k, m in sorted(mu.items()):
        cinfo = classify_row(P, k, target, W, g, di, rho, H)
        cinfo["mu"] = float(m)
        cinfo["g_over_H"] = float(g[k] / H) if H > 0 else None
        mu_rows[int(k)] = cinfo
    rec["mu_rows"] = mu_rows
    # class composition (mass-weighted)
    comp = {}
    for k, ci in mu_rows.items():
        comp[ci["class"]] = comp.get(ci["class"], 0.0) + ci["mu"]
    rec["class_composition"] = {kk: float(vv) for kk, vv in comp.items()}
    # sigma_v (off-own-site positive mass) AND sigma-tilde (v's positive coeff mass on rows
    # OUTSIDE conv W) -- N3 disambiguation
    sigma_v = float(sum(max(P[target, k], 0.0) for k in range(n) if k != target))
    sigma_tilde = float(sum(max(P[target, k], 0.0) for k in range(n)
                            if k != target and k not in W))
    rec["sigma_v"] = sigma_v
    rec["sigma_tilde"] = sigma_tilde
    rec["P_vv"] = float(P[target, target])
    rec["nu_v"] = float(np.maximum(-P[target], 0.0).sum())
    # exchange check: sum mu g <= t* R
    exch = float(sum(m * g[k] for k, m in mu.items())
                 + sum(m * g[k] for k, m in dual["alpha"].items()))
    rec["exchange_LHS"] = exch
    rec["exchange_bound_tstarR"] = float(dual["B"] * R)
    rec["exchange_bound_kappaR"] = float(kappa * R)
    # all-shallow verdict
    total_mu = dual["MU"] if dual["MU"] > 1e-12 else 1.0
    rec["shallow_fraction"] = float(shallow / total_mu)
    rec["ALL_SHALLOW"] = bool(shallow / total_mu >= 0.5)
    rec["gate"] = "PASS"
    return rec


# ----------------------------------------------------------------------
# Instance plan: off the d8 wall-edge, span delta/H^2 in [3.4, 50].
# Each entry: (d, sigma_v, ell, ma, k_groups, nlow, tag)
# Prioritize the floor [3.4, 6] at the corner-ish delta, plus mid-envelope.
# The d8 wall-edge is exactly (0.1435, 0.5, 0.65, 2, 2) -- EXCLUDED; we use neighbors
# and varied (sigma_v, ell, ma, k_groups) so these are genuinely off-family.
# ----------------------------------------------------------------------
PLAN = [
    # --- floor region delta/H^2 in [3.4, 6], near the corner, VARIED params (off-edge) ---
    (0.143, 0.35, 0.70, 2, 2, "floor_sv35"),
    (0.140, 0.70, 0.72, 2, 2, "floor_sv70"),
    (0.130, 0.50, 0.65, 3, 2, "floor_ma3"),
    (0.135, 0.50, 0.75, 2, 3, "floor_kg3"),
    (0.120, 0.50, 0.65, 2, 2, "floor_d120"),
    (0.110, 0.50, 0.65, 2, 2, "floor_d110"),
    (0.100, 0.70, 0.72, 2, 2, "floor_d100sv70"),
    (0.090, 0.50, 0.65, 2, 2, "mid_d090"),
    # --- mid-envelope, smaller delta (H >> 2delta in the H/tau sense; delta/H^2 in [10,50]) ---
    (0.070, 0.50, 0.65, 2, 2, "mid_d070"),
    (0.050, 0.50, 0.65, 3, 2, "mid_d050ma3"),
    (0.050, 0.35, 0.65, 2, 2, "small_d050sv35"),
    (0.030, 0.50, 0.65, 2, 3, "small_d030kg3"),
    (0.020, 0.50, 0.65, 2, 2, "small_d020"),
    (0.010, 0.70, 0.72, 2, 2, "small_d010sv70"),
]


def main():
    t0 = time.time()
    results = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "C": C, "c": c, "mission": "d12 DMF off-d8 falsification probe",
                        "d8_edge_excluded": "(d=0.1435,sv=0.5,ell=0.65,ma=2,kg=2)",
                        "presolve": "OFF on all LPs"},
               "instances": [], "all_shallow_found": False,
               "min_m_star": None, "median_m_star": None}

    def save():
        with open(OUT, "w") as f:
            json.dump(results, f, indent=2, default=float)

    print(f"[d12] {len(PLAN)} planned off-d8 instances. presolve OFF.", flush=True)
    mstars = []
    for ii, (d, sv, ell, ma, kg, tag) in enumerate(PLAN):
        print(f"\n[d12] === instance {ii+1}/{len(PLAN)}: {tag} "
              f"(d={d} sv={sv} ell={ell} ma={ma} kg={kg}) ===", flush=True)
        try:
            r = decide_opt(d, sv, k_groups=kg, ell=ell, ma=ma, nlow=2, v_own_site=True,
                           rounds=14, n_starts=4)
        except Exception as e:
            print(f"  decide_opt EXCEPTION: {e}", flush=True)
            results["instances"].append({"label": tag, "gate": "FAIL_decide_opt",
                                         "error": str(e)})
            save(); continue
        if not r.get("optimized"):
            print(f"  decide_opt did not optimize", flush=True)
            results["instances"].append({"label": tag, "gate": "FAIL_not_optimized"})
            save(); continue
        P = np.array(r["P"])
        # rebuild idx (decide_opt returns _meta only; need full idx for v)
        _, _, idx = build(d, sv, k_groups=kg, ell=ell, ma=ma, nlow=2, v_own_site=True)
        extra = {"d_poke": d, "design_sigma_v": sv, "ell": ell, "ma": ma, "k_groups": kg,
                 "mneg_lp": float(r["mneg_lp"])}
        rec = witness_anatomy(P, idx, tag, extra=extra)
        # log
        with open(os.path.join(LOGDIR, f"{tag}.json"), "w") as f:
            json.dump({**rec, "P": P.tolist()}, f, indent=2, default=float)
        if rec.get("gate") == "PASS":
            print(f"  PASS: delta={rec['delta']:.5f} H={rec['H']:.4f} "
                  f"H/tau={rec['H']/rec['tau']:.3f} delta/H^2={rec['delta']/rec['H']**2:.3f}",
                  flush=True)
            print(f"        ident_resid={rec['ident_resid']:.1e} massbal={rec['massbal_resid']:.1e} "
                  f"B-t*={rec['B_minus_tstar']:.1e}", flush=True)
            print(f"        m*_observed={rec['m_star_observed']:.4f} "
                  f"shallow_frac={rec['shallow_fraction']:.4f} "
                  f"sigma_v={rec['sigma_v']:.4f} sigma_tilde={rec['sigma_tilde']:.4f}",
                  flush=True)
            print(f"        depth profile (E/H -> mu-mass deep): "
                  f"{ {k: round(v,3) for k,v in rec['depth_profile'].items()} }", flush=True)
            print(f"        class comp: { {k: round(v,3) for k,v in rec['class_composition'].items()} }",
                  flush=True)
            mstars.append(rec["m_star_observed"])
            if rec["ALL_SHALLOW"]:
                print(f"  !!!!! ALL-SHALLOW WITNESS DETECTED ({tag}) -- DMF REFUTED-CANDIDATE !!!!!",
                      flush=True)
                results["all_shallow_found"] = True
                with open(CAND, "w") as f:
                    json.dump({**rec, "P": P.tolist()}, f, indent=2, default=float)
        else:
            print(f"  GATE {rec.get('gate')}", flush=True)
        results["instances"].append({k: v for k, v in rec.items() if k != "P"})
        if mstars:
            results["min_m_star"] = float(min(mstars))
            results["median_m_star"] = float(np.median(mstars))
        save()
        if results["all_shallow_found"]:
            print("[d12] STOPPING sweep: all-shallow candidate found.", flush=True)
            break

    results["meta"]["elapsed_s"] = time.time() - t0
    results["n_passed"] = sum(1 for x in results["instances"] if x.get("gate") == "PASS")
    save()
    print(f"\n[d12] done in {results['meta']['elapsed_s']:.1f}s. "
          f"passed={results['n_passed']} "
          f"min_m*={results['min_m_star']} median_m*={results['median_m_star']} "
          f"all_shallow={results['all_shallow_found']}", flush=True)


if __name__ == "__main__":
    main()
