#!/usr/bin/env python3 -u
"""
d8_opt.py -- OPTIMIZER-backed MRP decider: take the MRP bary geometry, pin the LOAD-BEARING
linear data (anchors as frame, v's far position, supplier group-site feed), and run the
alternating (Lambda,R) LP (d7_fti2) to MINIMIZE max-row-neg over the realization + (Lambda,R)
freedom.  Then verify robustly.  This is the proper blind-spot-exploiting decider: it asks
whether a CHEAPER exact completion of the SAME hidden geometry exists than the hand-built one
(the d3/d7 floor of 3.49 was only found this way).

If the optimizer drives delta/H^2 below the hand-built ~10 floor toward (or below) 3.49 we are
in refutation territory; if it stalls above 3.49 the architecture is blocked and we mine the
certificate (active constraints / duals) as a function of sigma_v.
"""
import os, json, time, itertools
import numpy as np

from d3_main import bary_to_P
from d7_fti2 import alternating_min, lp_optimize_R, lp_optimize_Lambda
from d8_mrp3 import build, verify
from d1_infra import neg_mass

OUT = os.path.join("out", "d8_opt.json")


def seed_frame_bary(bary_rows, r):
    """Seed (Lam0,R0) from bary rows: R0 = [I_r | 0] padded to n, Lam0 = bary coords (n x r).
       R0 Lam0 = I_r exactly (R0 picks the first r columns of Lam0, which are e_a for the
       archetype rows)."""
    Lam0 = np.asarray(bary_rows, float)        # n x r  (each row already len r... pad to n)
    n = Lam0.shape[0]
    if Lam0.shape[1] < n:
        Lam0 = np.hstack([Lam0, np.zeros((n, n - Lam0.shape[1]))])
    # but R must be r x n with R0=[I_r|0]; Lam must be n x r.  Use first r cols as the frame.
    Lam = Lam0[:, :r].copy()
    R0 = np.zeros((r, n)); R0[:, :r] = np.eye(r)
    return Lam, R0


def decide_opt(d, sigma_v, k_groups=2, ell=0.65, ma=2, nlow=2, v_own_site=True,
               rounds=16, n_starts=4, pin_level="load_bearing", seed=0, collect_duals=True):
    rows, r, idx = build(d, sigma_v, k_groups=k_groups, ell=ell, ma=ma, nlow=nlow,
                         v_own_site=v_own_site)
    n = len(rows)
    targets = np.array([np.concatenate([row, np.zeros(n - r)]) for row in rows])  # n x n
    Lam0, R0 = seed_frame_bary(rows, r)
    P0 = Lam0 @ R0
    seed_err = float(np.abs(P0 - targets).max())
    rl0 = float(np.abs(R0 @ Lam0 - np.eye(r)).max())

    # build pins (in P_ij coordinates; targets are n x n)
    full_pins = {}; lin_pins = []
    arche = idx["archetypes"]; anchors = idx["anchors"]
    for i in arche:
        full_pins[i] = targets[i]
    if pin_level == "load_bearing":
        # pin v FULLY (fix the far hidden geometry => entry preserved) + supplier group-site
        # feed; leave the FRAME (R) and the financing realization free to minimize neg.
        full_pins[idx["v"]] = targets[idx["v"]]
        for q, gmem in enumerate(idx["group_members"]):
            site = idx["grp"][q]
            for s in gmem:
                w = np.zeros(n); w[site] = 1.0
                lin_pins.append((s, w, float(targets[s][site])))
    elif pin_level == "full":
        for i in range(n):
            full_pins[i] = targets[i]
    elif pin_level == "v_only":
        full_pins[idx["v"]] = targets[idx["v"]]

    best = None
    for st in range(n_starts):
        if st == 0:
            Ls, Rs = Lam0, R0
        else:
            rng = np.random.default_rng(1000 * seed + st)
            Ls = Lam0 + 0.02 * rng.standard_normal(Lam0.shape)
            Ls = Ls - (Ls.sum(1, keepdims=True) - 1.0) / Ls.shape[1]
            Rs = R0.copy()
        res = alternating_min(Ls, Rs, n, full_pins, lin_pins, [], rounds=rounds)
        if res is None:
            continue
        Lam, R, P, mneg, duals = res
        if best is None or mneg < best[3]:
            best = (Lam, R, P, mneg, duals)
    if best is None:
        return {"seed_err": seed_err, "rl0": rl0, "optimized": False, "idx": _meta(idx)}
    Lam, R, P, mneg, duals = best
    ver = verify(P, idx)
    return {"seed_err": seed_err, "rl0": rl0, "optimized": True, "mneg_lp": float(mneg),
            "duals": duals, "verify": ver, "idx": _meta(idx), "P": P.tolist()}


def _meta(idx):
    return {k: idx[k] for k in ["r", "ma", "n", "d", "sigma_v", "k_groups", "ell",
                                "group_sep", "v", "suppliers", "anchors", "blockers"]}


if __name__ == "__main__":
    print("d8_opt self-test: optimize one MRP instance (sig=1.0, d=0.02) vs hand-built ~12.5",
          flush=True)
    # hand-built reference
    rows, r, idx = build(0.02, 1.0, k_groups=2, ell=0.75, ma=2, nlow=2, v_own_site=True)
    Phand = bary_to_P(rows, r); vh = verify(Phand, idx)
    print("  HAND: delta=%.4f H=%.4f d/H2=%s entry=%s"
          % (vh["delta"], vh["H_real"], vh.get("delta_over_H2"), vh["entry_pass"]), flush=True)
    r2 = decide_opt(0.02, 1.0, k_groups=2, ell=0.75, ma=2, nlow=2, pin_level="load_bearing")
    if r2.get("optimized"):
        v = r2["verify"]
        print("  OPT(load_bearing): seed_err=%.2e mneg=%.4f delta=%.4f H=%.4f d/H2=%s entry=%s"
              % (r2["seed_err"], r2["mneg_lp"], v["delta"], v["H_real"],
                 v.get("delta_over_H2"), v["entry_pass"]), flush=True)
    else:
        print("  OPT failed:", {k: r2[k] for k in r2 if k != "idx"}, flush=True)
