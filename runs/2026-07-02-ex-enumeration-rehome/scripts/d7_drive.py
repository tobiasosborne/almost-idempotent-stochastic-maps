#!/usr/bin/env python3 -u
"""
d7_drive.py -- the FTI-2 decider driver.

For each template cell (r, n, helpers, mu, H_target) it:
  1. builds an explicit ell^1 target geometry (d7_template.build_targets);
  2. seeds a VALID exact idempotent with the canonical frame R0=[I_r|0] (R0 Lambda0 = I_r
     automatically; ALWAYS feasible) AND a perturbed/random valid seed (multistart);
  3. minimizes max-row-neg by EXACT alternating LPs over arbitrary (Lambda, R) subject to
     - anchors + L1,L2 FULLY pinned (the intended W & shadow carriers);
     - v1,v2 (+ free helpers) constrained ONLY by the height functional and the mutual-
       shadow equations (||e_j||_1 <= 4 tau);  (this is the blind-spot freedom);
  4. VERIFIES robustly (d7_fti2.verify_fti2): idempotence, robust W, dist_1(v_j,conv W)>=H,
     both v_j fail (4tau,tau/4)-exposedness;
  5. keeps the MIN verified delta/H^2 per cell; flags any refutation candidate (delta/H^2
     driving to 0) and STOPS to report it.

OBSERVABILITY: python3 -u, flushed progress, crash-safe JSON checkpoints to out/.
"""
import sys, os, json, time, itertools
import numpy as np

from d7_template import build_targets, height_functional
from d7_fti2 import alternating_min, verify_fti2

OUTDIR = "out"
os.makedirs(OUTDIR, exist_ok=True)


def canonical_seed(n, r, T, rng, jitter=0.0):
    """Valid idempotent seed that EXACTLY realizes the template targets T.
       R0=[I_r|0]; Lambda0 top r x r = I_r (the frame archetypes); for every other row i,
       Lambda0[i] = T[i][:r] (its frame coordinates).  Since the targets are supported on
       the first r axes, (Lambda0 R0)_i = Lambda0[i] padded = T[i] EXACTLY, and
       R0 Lambda0 = I_r.  Optional jitter randomizes the FREE (non-pinned) directions for
       multistart without breaking feasibility (jitter only the off-frame columns r..n-1
       of R0, which do not affect the realized rows since Lambda's last n-r cols are 0...
       actually we jitter R0's free columns to give the alternation diverse basins)."""
    R0 = np.zeros((r, n)); R0[:, :r] = np.eye(r)
    if jitter > 0:
        R0[:, r:] += jitter * rng.normal(size=(r, n - r))
        # keep R rows summing to 1: subtract the added mass back on the frame block
        R0[:, :r] -= (R0[:, r:].sum(axis=1, keepdims=True)) * (np.ones((1, r)) / r)
    Lam0 = np.zeros((n, r))
    Lam0[:r, :r] = np.eye(r)
    for i in range(r, n):
        Lam0[i] = T[i][:r]
    return Lam0, R0


def make_pins(T, idx, tau):
    """full pins for anchors + L1 + L2; lin_pins height functional for v1,v2,helpers;
       shadow equations for the mutual-shadow pair (and helper shadows if present)."""
    n = T.shape[0]
    full_pins = {}
    # the frame archetype rows e_a are NOT pinned (the canonical seed already places
    # them; pinning the whole archetype block over-constrains R Lambda = I and is
    # redundant -- the seed's I_r block already realizes them).  We DO pin the anchor
    # rows (the intended W simplex C), L1, L2 (shadow carriers).
    for a in idx["anchors"]:
        full_pins[a] = T[a].copy()
    full_pins[idx["L1"]] = T[idx["L1"]].copy()
    full_pins[idx["L2"]] = T[idx["L2"]].copy()
    wH = height_functional(idx, n)
    Hgt_v1 = float(wH @ T[idx["v1"]])
    Hgt_v2 = float(wH @ T[idx["v2"]])
    lin_pins = [(idx["v1"], wH, Hgt_v1), (idx["v2"], wH, Hgt_v2)]
    # mutual shadow equations: v1 = mu1 v2 + (1-mu1) L1 + e1 ; v2 = mu2 v1 + (1-mu2) L2 + e2
    ebar = 4.0 * tau
    shadows = [
        (idx["v1"], idx["v2"], idx["L1"], MU[0], ebar),
        (idx["v2"], idx["v1"], idx["L2"], MU[1], ebar),
    ]
    return full_pins, lin_pins, shadows


MU = (0.99, 0.99)   # set per cell before make_pins


def run_cell(ma, nh, H, mu, w, n_starts=50, verbose=False, tau_hint=None):
    """Decide one template cell. Returns the best verified record (min delta/H^2)."""
    global MU
    MU = (mu, mu)
    # tau for the shadow error budget: self-consistent loop. Start from a hint (or H/2,
    # since canonical gives delta>=H/2 -> tau~sqrt(H/2)), refine after first solve.
    best = None
    best_unverified = None
    seen = []
    for start in range(n_starts):
        rng = np.random.default_rng(1000 * start + int(1000 * H) + ma + nh)
        T, idx = build_targets(ma=ma, nh=nh, H=H, mu1=mu, mu2=mu, w=w, seed=start)
        n = T.shape[0]
        anchors = idx["anchors"]
        r = idx["r"]            # template prepends r identity archetype rows (frame)
        # self-consistent tau loop (2 passes): use tau_hint then refine
        tau = tau_hint if tau_hint is not None else np.sqrt(max(H / 2.0, 1e-3))
        for tau_pass in range(2):
            full_pins, lin_pins, shadows = make_pins(T, idx, tau)
            Lam0, R0 = canonical_seed(n, r, T, rng,
                                      jitter=(0.0 if start == 0 else 0.15))
            res = alternating_min(Lam0, R0, n, full_pins, lin_pins, shadows,
                                  rounds=14, verbose=False)
            if res is None:
                break
            Lam, R, P, mneg, duals = res
            tau_new = np.sqrt(max(mneg, 1e-12))
            if abs(tau_new - tau) < 1e-4 * max(1.0, tau):
                tau = tau_new
                break
            tau = tau_new
        if res is None:
            continue
        Lam, R, P, mneg, duals = res
        v = verify_fti2(P, anchors, idx["v1"], idx["v2"], H_target=H)
        v["start"] = start; v["ma"] = ma; v["nh"] = nh; v["H_target"] = H
        v["mu"] = mu; v["w"] = w; v["r"] = r; v["n"] = n; v["mneg_lp"] = float(mneg)
        v["duals"] = duals
        seen.append({k: v.get(k) for k in
                     ("start", "pass", "delta", "tau", "H_real", "delta_over_H2",
                      "v1_fails_exposed", "v2_fails_exposed", "nW", "dist_v1", "dist_v2")})
        if v["pass"] and v.get("delta_over_H2") is not None:
            if best is None or v["delta_over_H2"] < best["delta_over_H2"]:
                best = dict(v)
                best["P"] = P.tolist()
        else:
            if v.get("delta_over_H2") is not None:
                if best_unverified is None or v["delta_over_H2"] < best_unverified["delta_over_H2"]:
                    best_unverified = {k: v.get(k) for k in
                        ("start", "pass", "delta", "tau", "H_real", "delta_over_H2",
                         "v1_fails_exposed", "v2_fails_exposed", "v1_vertex", "v2_vertex",
                         "distinct_v", "nW", "dist_v1", "dist_v2", "reason")}
        if verbose and start % 10 == 0:
            bo = best["delta_over_H2"] if best else None
            print(f"    [cell ma={ma} nh={nh} H={H} mu={mu}] start {start}: "
                  f"pass={v['pass']} d/H2={v.get('delta_over_H2')} best={bo}", flush=True)
    return {"ma": ma, "nh": nh, "H": H, "mu": mu, "w": w, "n_starts": n_starts,
            "best_verified": best, "best_unverified": best_unverified,
            "n_seen": len(seen)}


def main():
    t0 = time.time()
    cells = []
    MAS = [3, 4, 5]          # ma anchors (-> r ~ ma+2..)
    NHS = [0, 2, 4]          # helpers
    MUS = [0.9, 0.99, 0.999]
    HS = [0.1, 0.2, 0.4]
    W = 0.05
    NSTART = 50
    results = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "C": 4.0, "c": 0.25, "normalization": "delta=max-row-neg (d3 units)",
                        "n_starts": NSTART, "w": W},
               "cells": [], "refutation_candidate": None}
    OUT = os.path.join(OUTDIR, "d7_floor.json")

    def save():
        with open(OUT, "w") as f:
            json.dump(results, f, indent=2, default=float)

    # DEPTH over breadth: focus on the 2-helper template per the task, but cover the grid.
    combos = list(itertools.product(MAS, NHS, MUS, HS))
    print(f"[d7] {len(combos)} cells x {NSTART} starts. normalization=delta(max-neg).",
          flush=True)
    for ci, (ma, nh, mu, H) in enumerate(combos):
        print(f"[d7] cell {ci+1}/{len(combos)}: ma={ma} nh={nh} mu={mu} H={H}", flush=True)
        rec = run_cell(ma, nh, H, mu, W, n_starts=NSTART, verbose=True)
        bv = rec["best_verified"]
        if bv:
            print(f"    -> VERIFIED min delta/H^2 = {bv['delta_over_H2']:.4f} "
                  f"(delta={bv['delta']:.4e} H={bv['H_real']:.4f} nW={bv['nW']})", flush=True)
            if bv["delta_over_H2"] < 0.5:   # well below the d3 floor ~2.4: candidate refutation
                print(f"    !!! LOW delta/H^2 = {bv['delta_over_H2']:.4f} -- candidate "
                      f"refutation; saving matrix and flagging.", flush=True)
                results["refutation_candidate"] = bv
        else:
            print(f"    -> NO verified instance (best_unverified="
                  f"{rec['best_unverified']})", flush=True)
        # strip P from stored cells except refutation candidate to keep json small
        rec_store = dict(rec)
        if rec_store.get("best_verified"):
            rec_store["best_verified"] = {k: v for k, v in rec_store["best_verified"].items()
                                          if k != "P"}
        results["cells"].append(rec_store)
        save()
        if results["refutation_candidate"] is not None:
            print("[d7] STOPPING: refutation candidate found. See out/d7_floor.json.",
                  flush=True)
            # save the full matrix
            with open(os.path.join(OUTDIR, "d7_refutation.json"), "w") as f:
                json.dump(bv, f, indent=2, default=float)
            break
    results["meta"]["elapsed_s"] = time.time() - t0
    save()
    # global floor
    verified = [c["best_verified"] for c in results["cells"] if c["best_verified"]]
    if verified:
        gmin = min(verified, key=lambda b: b["delta_over_H2"])
        print(f"\n[d7] GLOBAL min verified delta/H^2 = {gmin['delta_over_H2']:.4f} "
              f"at ma={gmin['ma']} nh={gmin['nh']} mu={gmin['mu']} H={gmin['H_real']:.4f}",
              flush=True)
        results["global_floor"] = gmin
        save()
    print(f"[d7] done in {results['meta']['elapsed_s']:.1f}s", flush=True)


if __name__ == "__main__":
    main()
