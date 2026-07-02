#!/usr/bin/env python3 -u
"""
d8_sweep.py -- the MRP DECISION sweep over sigma_v, k_groups, d, ell, group_sep, ma, nlow.

For each cell: build the financed-wiggle MRP instance, verify robustly (honest tau), record
delta/H^2 when the entry gate passes (v hidden + non-exposed + vertex + idempotent + suppliers
out of W).  Crash-safe JSON checkpoints.  Reports:
  - the floor table over the grid (min verified delta/H^2 per (sigma_v, k_groups))
  - any refutation (delta/H^2 < 3)
  - the entry-gate map: which cells ENTER the hypothesis at all (the design tension)
"""
import os, json, time, itertools
import numpy as np
from d8_mrp3 import run_one

OUT = os.path.join("out", "d8_sweep.json")


def main():
    t0 = time.time()
    sigmas = [0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 1.0]
    kgs = [1, 2, 3]
    ds = [0.002, 0.005, 0.008, 0.01, 0.012, 0.015, 0.02, 0.03]
    ells = [0.45]
    mas = [2, 3]
    nlows = [2]
    res = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": C_(),
                    "normalization": "delta=max-row-neg"},
           "entered": [], "best_per_cell": {}, "refutation": None,
           "all_min_dH2": None, "summary": {}}
    best_global = (np.inf, None)
    count = 0; entered = 0
    combos = list(itertools.product(sigmas, kgs, ds, ells, mas, nlows))
    print(f"[d8-sweep] {len(combos)} cells", flush=True)
    for (sig, kg, d, ell, ma, nlow) in combos:
        try:
            P, idx, ver = run_one(d, sig, k_groups=kg, ell=ell, ma=ma, nlow=nlow)
        except Exception as e:
            count += 1
            continue
        count += 1
        cell = f"sig{sig}_kg{kg}"
        rec = {"sigma_v": sig, "k_groups": kg, "d": d, "ell": ell, "ma": ma, "nlow": nlow,
               "delta": ver.get("delta"), "tau": ver.get("tau"),
               "H_real": ver.get("H_real"), "delta_over_H2": ver.get("delta_over_H2"),
               "H_over_tau": ver.get("H_over_tau"), "v_margin": ver.get("v_margin"),
               "v_fails_exposed": ver.get("v_fails_exposed"),
               "suppliers_all_hidden": ver.get("suppliers_all_hidden"),
               "nW": ver.get("nW"), "entry_pass": ver.get("entry_pass"),
               "idem_ok": ver.get("idem_ok")}
        if ver.get("entry_pass") and ver.get("delta_over_H2") is not None:
            entered += 1
            res["entered"].append(rec)
            dh2 = ver["delta_over_H2"]
            cur = res["best_per_cell"].get(cell)
            if cur is None or dh2 < cur["delta_over_H2"]:
                res["best_per_cell"][cell] = rec
            if dh2 < best_global[0]:
                best_global = (dh2, rec)
            if dh2 < 3.0:
                print(f"  !!! REFUTATION TERRITORY {cell} d={d}: delta/H^2={dh2:.4f}", flush=True)
                res["refutation"] = dict(rec, P=P.tolist())
                with open(os.path.join("out", "d8_refutation.json"), "w") as f:
                    json.dump(res["refutation"], f, indent=2, default=float)
        if count % 30 == 0:
            res["all_min_dH2"] = best_global[1]
            with open(OUT, "w") as f:
                json.dump(res, f, indent=2, default=float)
            print(f"  [{count}/{len(combos)}] entered={entered} "
                  f"min(d/H2)={best_global[0]:.3f}", flush=True)
    res["all_min_dH2"] = best_global[1]
    res["summary"] = {"n_cells": count, "n_entered": entered,
                      "min_delta_over_H2": (None if best_global[1] is None else best_global[0]),
                      "verdict": ("REFUTATION" if res["refutation"] else
                                  ("ENTERED_FLOOR_ABOVE_3" if entered else "NO_ENTRY")),
                      "elapsed_s": time.time() - t0}
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d8-sweep] DONE cells={count} entered={entered} "
          f"min(delta/H^2)={best_global[0]:.4f} verdict={res['summary']['verdict']} "
          f"({res['summary']['elapsed_s']:.1f}s)", flush=True)
    if best_global[1]:
        b = best_global[1]
        print(f"  best: sigma_v={b['sigma_v']} k_groups={b['k_groups']} d={b['d']} "
              f"H/tau={b['H_over_tau']:.3f} delta/H^2={b['delta_over_H2']:.4f}", flush=True)


def C_():
    return 4.0


if __name__ == "__main__":
    main()
