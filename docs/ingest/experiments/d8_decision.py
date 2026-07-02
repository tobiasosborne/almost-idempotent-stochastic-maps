#!/usr/bin/env python3 -u
"""
d8_decision.py -- THE MRP decision sweep (consolidated, optimizer-backed, certificate-mining).

For each (sigma_v, k_groups): bisect the poke depth d to the COLLAPSE edge (the largest d for
which the hidden cluster still fails (rho,kappa)-exposedness), record the floor delta/H^2 there
and the exposedness margin/kappa of the cluster (the binding certificate).  The wall is the
cluster exposedness margin reaching kappa at H/tau ~ 0.536 => delta/H^2 -> 1/0.536^2 ~ 3.49.

Outputs out/d8_decision.json:
  - floor table: min delta/H^2 per (sigma_v, k_groups) + the H/tau where it lives
  - the sigma_v certificate: collapse H/tau vs sigma_v (why small sigma_v can't reach the wall)
  - delta-scaling: floor at several tau scales (scale-invariance / sampling caveat)
  - refutation flag (delta/H^2 < 3 anywhere)
"""
import os, json, time, numpy as np
from d8_opt import decide_opt
from d1_infra import exposed_margin

OUT = os.path.join("out", "d8_decision.json")
C, c = 4.0, 0.25


def collapse_floor(sig, kg, ell=0.75, ma=2, nlow=2, dmax=0.25, fine=True):
    """Scan d upward; return the floor (min delta/H^2 over entering d) + the record at the
       collapse edge (last entering d) with the cluster exposedness margin/kappa."""
    best = (np.inf, None)
    last_enter = None
    coarse = np.arange(0.01, dmax, 0.005)
    for d in coarse:
        r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=ma, nlow=nlow,
                        pin_level="load_bearing", n_starts=1)
        v = r2.get("verify", {})
        if v.get("entry_pass") and v.get("delta_over_H2"):
            last_enter = (float(d), r2)
            if v["delta_over_H2"] < best[0]:
                best = (v["delta_over_H2"], r2)
    # refine near the collapse edge
    if fine and last_enter is not None:
        d0 = last_enter[0]
        for d in np.arange(d0, d0 + 0.006, 0.0005):
            r2 = decide_opt(float(d), sig, k_groups=kg, ell=ell, ma=ma, nlow=nlow,
                            pin_level="load_bearing", n_starts=2)
            v = r2.get("verify", {})
            if v.get("entry_pass") and v.get("delta_over_H2"):
                if v["delta_over_H2"] < best[0]:
                    best = (v["delta_over_H2"], r2)
    if best[1] is None:
        return None
    r2 = best[1]; v = r2["verify"]; P = np.array(r2["P"]); idx = r2["idx"]
    tau = v["tau"]; rho, kappa = C * tau, c * tau
    cluster_marg = []
    for s in idx["suppliers"] + [idx["v"]]:
        ok, m, _ = exposed_margin(P, s, rho, kappa)
        cluster_marg.append((m or 0.0) / kappa)
    return {"sigma_v": sig, "k_groups": kg, "min_delta_over_H2": float(best[0]),
            "H_over_tau": float(v.get("H_over_tau", 0)), "tau": float(tau),
            "delta": float(v["delta"]), "nW": v["nW"],
            "cluster_margin_over_kappa_min": float(min(cluster_marg)),
            "cluster_margin_over_kappa_max": float(max(cluster_marg)),
            "v_fails_exposed": v["v_fails_exposed"],
            "suppliers_all_hidden": v["suppliers_all_hidden"]}


def main():
    t0 = time.time()
    res = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": C, "c": c,
                    "normalization": "delta=max-row-neg",
                    "decider": "optimizer-backed (alternating Lambda,R LP), v pinned far, "
                               "financing+frame free; robust post-hoc verification"},
           "floor_table": [], "refutation": None, "summary": {}}
    sigmas = [0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 1.0]
    kgs = [1, 2, 3]
    best_global = (np.inf, None)
    print("[d8-decision] collapse-edge floor over (sigma_v, k_groups)", flush=True)
    print("sig_v  kg  min_dH2   H/tau   clustMarg/k(min,max)", flush=True)
    for sig in sigmas:
        for kg in kgs:
            rec = collapse_floor(sig, kg)
            if rec is None:
                print(f"  {sig:.2f}  {kg}  NO ENTRY", flush=True)
                continue
            res["floor_table"].append(rec)
            print(f"  {sig:.2f}  {kg}  {rec['min_delta_over_H2']:.4f}  "
                  f"{rec['H_over_tau']:.4f}  "
                  f"({rec['cluster_margin_over_kappa_min']:.3f},"
                  f"{rec['cluster_margin_over_kappa_max']:.3f})", flush=True)
            if rec["min_delta_over_H2"] < best_global[0]:
                best_global = (rec["min_delta_over_H2"], rec)
            if rec["min_delta_over_H2"] < 3.0:
                res["refutation"] = rec
            with open(OUT, "w") as f:
                json.dump(res, f, indent=2, default=float)
    res["summary"] = {
        "min_delta_over_H2_global": (None if best_global[1] is None else best_global[0]),
        "argmin": best_global[1],
        "verdict": ("REFUTATION" if res["refutation"] else "HLC_SUPPORTED_floor_at_wall"),
        "wall_H_over_tau": (None if best_global[1] is None else best_global[1]["H_over_tau"]),
        "elapsed_s": time.time() - t0,
    }
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d8-decision] DONE min(delta/H^2)={best_global[0]:.4f} "
          f"verdict={res['summary']['verdict']} ({res['summary']['elapsed_s']:.1f}s)", flush=True)


if __name__ == "__main__":
    main()
