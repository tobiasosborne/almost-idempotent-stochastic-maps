#!/usr/bin/env python3 -u
"""
d3_drive2.py -- envelope mining on the PROVABLY-VALID canonical family (d3_bary), with
ADVERSARIAL optimization over R (and Lambda).  This is the load-bearing driver.

Build per (template, H):
  r = mb + npil archetypes; k hidden rows; n = r + k.
  R0 = [I_r | 0]   (r x n).
  Lam0 = [[I_r],[bary_hidden]]  (n x r); top block I_r forces R0 Lam0 = I_r (EXACT).
  P0 = Lam0 R0  is the canonical exact idempotent realizing the hidden bary geometry.

Canonical value: max-row-neg(P0) (closed form = max over hidden rows of neg of its bary
coords).  Then ADVERSARIAL: pin the realized hidden rows P[i] (i>=r) to their canonical
positions and alternate exact LPs over R then Lambda to push max-row-neg DOWN, probing
whether a non-trivial R re-coordinatization cheats the cost.  VERIFY honestly; only
verified-hidden points enter env(H).

Outputs out/d3_env_<family>.json crash-safe; flushed progress.
"""
import sys, os, json, time
import numpy as np

from d1_infra import check_idempotent, neg_mass
from d3_envelope import alternating_min, lp_optimize_R, lp_optimize_Lambda, verify
import d3_bary as B


def build_canonical(bary_hidden, r):
    """Return Lam0 (n x r), R0 (r x n), hidden_idx, anchor rows are 0..r-1."""
    bary_hidden = np.asarray(bary_hidden, float)
    k = bary_hidden.shape[0]
    n = r + k
    R0 = np.zeros((r, n))
    R0[:, :r] = np.eye(r)
    Lam0 = np.zeros((n, r))
    Lam0[:r, :] = np.eye(r)
    Lam0[r:, :] = bary_hidden
    hidden_idx = list(range(r, n))
    return Lam0, R0, hidden_idx


def mine(template_fn, params, C=4.0, c=0.25, adversarial_rounds=12,
         do_adversarial=True, verbose=False):
    bary, anchor_arch, pillar_arch, meta = template_fn(**params)
    r = meta["r"]; H = meta["H"]
    Lam0, R0, hidden_idx = build_canonical(bary, r)
    P0 = Lam0 @ R0
    chk = check_idempotent(P0, tol=1e-9)
    rec = {"meta": meta, "params": dict(params), "r": r, "n": Lam0.shape[0],
           "hidden_idx": hidden_idx, "anchor_arch": anchor_arch,
           "pillar_arch": pillar_arch,
           "seed_idem_resid": chk["idem_resid"], "seed_idem_ok": bool(chk["ok"])}
    if not chk["ok"]:
        rec["status"] = "seed_not_idempotent"; return rec
    v0 = verify(P0, hidden_idx, C=C, c=c, H_target=H)
    rec["canonical"] = v0
    # adversarial
    if do_adversarial:
        pins = {i: P0[i].copy() for i in hidden_idx}
        best = alternating_min(Lam0, R0, pins, rounds=adversarial_rounds, verbose=verbose)
        if best is not None:
            Lamb, Rb, Pb, mnb = best
            vb = verify(Pb, hidden_idx, C=C, c=c, H_target=H)
            _, _, iR = lp_optimize_R(Lamb, pins, R_warm=Rb, collect_duals=True)
            _, _, iL = lp_optimize_Lambda(Rb, pins, Lam_warm=Lamb, collect_duals=True)
            vb["duals_R"] = iR.get("duals"); vb["duals_L"] = iL.get("duals")
            rec["adversarial"] = vb
        else:
            rec["adversarial"] = {"status": "alt_failed"}
    # envelope value: min verified-hidden max-neg
    cands = []
    if v0.get("verified_hidden"):
        cands.append(("canonical", v0["max_neg"], v0["max_hidden_dist"]))
    av = rec.get("adversarial", {})
    if av.get("verified_hidden"):
        cands.append(("adversarial", av["max_neg"], av["max_hidden_dist"]))
    if cands:
        cands.sort(key=lambda x: x[1])
        rec["env_source"], rec["env_maxneg"], rec["env_dist"] = cands[0]
        rec["verified"] = True
    else:
        rec["verified"] = False
        rec["env_maxneg"] = v0["max_neg"]
        rec["env_dist"] = v0.get("max_hidden_dist", 0.0)
    return rec


if __name__ == "__main__":
    print("=" * 70, flush=True)
    print("d3_drive2 smoke: thin diamond, single H", flush=True)
    print("=" * 70, flush=True)
    rec = mine(B.diamond_bary, dict(H=0.3, k=4, mb=2, npil=2, w=0.03), verbose=True)
    print("\nseed idem ok:", rec["seed_idem_ok"], "resid", rec["seed_idem_resid"], flush=True)
    c = rec["canonical"]
    print("CANONICAL:", {k: c.get(k) for k in
          ("delta", "tau", "rho", "nW", "W", "max_hidden_dist", "hidden_dists",
           "hidden_in_W", "verified_hidden")}, flush=True)
    if "adversarial" in rec and "delta" in rec["adversarial"]:
        a = rec["adversarial"]
        print("ADVERSARIAL:", {k: a.get(k) for k in
              ("delta", "tau", "nW", "max_hidden_dist", "hidden_in_W",
               "verified_hidden")}, flush=True)
    print("ENV:", {k: rec.get(k) for k in ("env_source", "env_maxneg", "env_dist",
                                           "verified")}, flush=True)
