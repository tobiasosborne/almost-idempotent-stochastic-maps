#!/usr/bin/env python3 -u
"""
d3_drive.py -- ENVELOPE DRIVER.  Mines env(H) over EXACT idempotents realizing a
hidden-geometry template, with ADVERSARIAL optimization over BOTH Lambda and R.

CLEAN STRUCTURAL FACT (the canonical embedding).  Take archetypes R = [I_r | 0]
(r x n): the constraint R Lambda = I_r FORCES the top r x r block of Lambda to equal
I_r, leaving the bottom (n-r) rows of Lambda FREE (each summing to 1).  Then:
  * rows 0..r-1 of P are e_0..e_{r-1}  (clean probability vertices, natural W),
  * row i>=r of P is p_i = (Lambda[i,:], 0,...,0): a SIGNED AFFINE COMBINATION of the
    archetypes with barycentric coords Lambda[i,:], and neg(p_i)=sum_a max(-Lambda[i,a],0).
So in this embedding a row is "hidden/far" exactly when its barycentric coords sit far
OUTSIDE the probability simplex -- the negativity IS the distance-outside-simplex.
This embedding is NOT prover-favorable; it is the canonical simplex picture.

ADVERSARIAL R.  A GENERAL R (archetypes not the standard basis) re-coordinatizes the
flat and can, in principle, lower max-row-neg for the SAME ell^1 geometry.  We probe
this by alternating exact LPs (lp_optimize_R / lp_optimize_Lambda from d3_envelope)
starting from a FEASIBLE idempotent seed, with the hidden rows PINNED to thin-diamond
targets.  We report whether adversarial R beats the canonical R=I_r value (it should
NOT drop below the HCC floor if the conjecture holds).

PIPELINE per (template, H):
  1. build targets, anchors, hidden (d3_templates).
  2. build a FEASIBLE exact-idempotent seed realizing the hidden geometry:
     R0 = [I_r|0] with r = (#anchors) + (#hidden) chosen so the hidden rows ARE
     archetypes (their realized position = their target exactly), anchors are the rest.
     Then Lambda top block = I_r (forced), and we are already idempotent & realize the
     hidden targets EXACTLY.  This is the canonical-R feasible point.
  3. canonical value: max-row-neg of the seed (closed form from targets).
  4. adversarial: alternate optimize R then Lambda (hidden rows pinned) to push
     max-row-neg DOWN.  Collect duals at the optimum.
  5. VERIFY honestly (recompute W, hidden dist, max-neg).  Record only verified points.
Crash-safe JSON checkpoints; flushed progress.
"""
import sys, os, json, time
import numpy as np

from d1_infra import check_idempotent, neg_mass, check_factorization
from d3_envelope import (alternating_min, lp_optimize_R, lp_optimize_Lambda, verify,
                         well_exposed_set, dist1_to_conv)
import d3_templates as T


# ----------------------------------------------------------------------
# Feasible idempotent seed realizing the hidden geometry EXACTLY.
# We make EVERY row an archetype is overkill; instead make the hidden rows + anchors
# all archetypes so r = n and R0 = identity-like realizing targets:
#   set R0 = targets (n x n) ... but then r=n and R0 Lambda=I_n forces Lambda=R0^{-1}.
# Simpler & canonical: choose r = n, R0 = targets, Lambda0 = inv(targets) IF invertible.
# Then P0 = Lambda0 R0 = I_n -> trivial (every row = e_i), NOT our geometry.  No good.
#
# Correct canonical seed: r = (#distinct flat dims). Put archetypes = a maximal affinely
# independent subset of the targets; set R0 to THOSE rows; Lambda0 from R0 Lambda=I.
# With R0 = chosen target rows, R0 Lambda=I forces Lambda[arch]=... we solve the affine
# system exactly and READ the realized rows (they need NOT equal non-archetype targets).
# So we accept the realized geometry and verify it.  To make hidden rows land where we
# want, we INCLUDE all hidden rows in the archetype set (then their realized row ==
# their target exactly, since archetype a -> P row = e_a @ R0 = R0[a] = target).
# ----------------------------------------------------------------------
def canonical_seed(targets, anchor_idx, hidden_idx):
    """R0 = the rows {hidden_idx + as many anchors as keep affine independence}.
       Archetypes include ALL hidden rows so they are realized exactly.
       Returns Lam0 (n x r), R0 (r x n), arch (list), info."""
    targets = np.asarray(targets, float)
    n = targets.shape[0]
    # archetype order: hidden first (must be realized exactly), then anchors, then rest
    prefer = list(hidden_idx) + list(anchor_idx) + [i for i in range(n)
                                                    if i not in hidden_idx and i not in anchor_idx]
    chosen = []
    for i in prefer:
        trial = chosen + [i]
        M = targets[trial] - targets[trial][0]
        if np.linalg.matrix_rank(M, tol=1e-9) + 1 == len(trial):
            chosen.append(i)
    r = len(chosen)
    R0 = targets[chosen].copy()                 # r x n
    # Lambda0: for each row solve bary coords wrt R0 (exact, rows in flat)
    A = np.vstack([R0.T, np.ones(r)])           # (n+1) x r
    Lam0 = np.zeros((n, r))
    bres = 0.0
    for i in range(n):
        b = np.concatenate([targets[i], [1.0]])
        lam, *_ = np.linalg.lstsq(A, b, rcond=None)
        Lam0[i] = lam
        bres = max(bres, float(np.abs(A @ lam - b).max()))
    P0 = Lam0 @ R0
    RL = R0 @ Lam0
    info = {"r": r, "arch": chosen, "bary_resid": bres,
            "RLambda_err": float(np.abs(RL - np.eye(r)).max()),
            "realize_err": float(np.abs(P0 - targets).max()),
            "idem_resid": float(np.abs(P0 @ P0 - P0).max())}
    return Lam0, R0, chosen, info


def mine_point(template_fn, params, C=4.0, c=0.25, adversarial_rounds=10,
               pin_hidden=True, verbose=False):
    """Mine one envelope point. Returns a record dict."""
    targets, anchor_idx, hidden_idx, meta = template_fn(**params)
    H = meta["H"]
    Lam0, R0, arch, sinfo = canonical_seed(targets, anchor_idx, hidden_idx)
    rec = {"meta": meta, "params": {k: v for k, v in params.items()},
           "anchor_idx": anchor_idx, "hidden_idx": hidden_idx,
           "seed_info": {k: (round(v, 6) if isinstance(v, float) else v)
                         for k, v in sinfo.items()}}
    P0 = Lam0 @ R0
    chk0 = check_idempotent(P0, tol=1e-6)
    if not chk0["ok"]:
        rec["seed_idem_ok"] = False
        rec["status"] = "seed_not_idempotent"
        return rec
    # canonical (seed) verified value
    v0 = verify(P0, hidden_idx, C=C, c=c, H_target=H)
    rec["canonical"] = v0
    # adversarial: pin hidden rows to their realized (target) positions; alternate.
    pins = {i: P0[i].copy() for i in hidden_idx} if pin_hidden else {}
    best = alternating_min(Lam0, R0, pins, rounds=adversarial_rounds, verbose=verbose)
    if best is None:
        rec["adversarial"] = {"status": "alt_failed"}
        rec["env_maxneg"] = v0["max_neg"]; rec["env_dist"] = v0["max_hidden_dist"]
        rec["verified"] = v0["verified_hidden"]
        return rec
    Lamb, Rb, Pb, mnb = best
    vb = verify(Pb, hidden_idx, C=C, c=c, H_target=H)
    # collect duals at the adversarial optimum (final optR + optL)
    _, _, infoR = lp_optimize_R(Lamb, pins, R_warm=Rb, collect_duals=True)
    _, _, infoL = lp_optimize_Lambda(Rb, pins, Lam_warm=Lamb, collect_duals=True)
    vb["duals_R"] = infoR.get("duals")
    vb["duals_L"] = infoL.get("duals")
    rec["adversarial"] = vb
    # envelope value = the MIN verified max-neg among canonical & adversarial that are
    # still genuinely hidden (verified_hidden True).
    cands = []
    if v0.get("verified_hidden"):
        cands.append(("canonical", v0["max_neg"], v0["max_hidden_dist"]))
    if vb.get("verified_hidden"):
        cands.append(("adversarial", vb["max_neg"], vb["max_hidden_dist"]))
    if cands:
        cands.sort(key=lambda x: x[1])
        rec["env_source"], rec["env_maxneg"], rec["env_dist"] = cands[0]
        rec["verified"] = True
    else:
        rec["verified"] = False
        rec["env_maxneg"] = min(v0["max_neg"], vb["max_neg"])
        rec["env_dist"] = max(v0.get("max_hidden_dist", 0), vb.get("max_hidden_dist", 0))
    return rec


def fit_exponent(Hs, envs):
    """Fit log env = p log H + b on positive verified points; return p, b, r2, n."""
    Hs = np.asarray(Hs, float); envs = np.asarray(envs, float)
    m = (Hs > 0) & (envs > 1e-12)
    if m.sum() < 2:
        return {"p": None, "b": None, "r2": None, "n": int(m.sum())}
    x = np.log(Hs[m]); y = np.log(envs[m])
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    p, b = coef
    yhat = A @ coef
    ss_res = float(((y - yhat) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 1.0
    return {"p": float(p), "b": float(b), "r2": float(r2), "n": int(m.sum())}


if __name__ == "__main__":
    print("d3_drive smoke test on one thin_diamond point", flush=True)
    rec = mine_point(T.thin_diamond, dict(H=0.3, k=4, mb=3, base_r=0.5, w=0.05),
                     verbose=True)
    import pprint
    pprint.pprint({k: rec[k] for k in ("seed_info", "env_source", "env_maxneg",
                                       "env_dist", "verified") if k in rec})
    print("canonical:", {k: rec["canonical"].get(k) for k in
                         ("delta", "tau", "nW", "max_hidden_dist", "hidden_in_W",
                          "verified_hidden")})
    if "adversarial" in rec and "delta" in rec["adversarial"]:
        print("adversarial:", {k: rec["adversarial"].get(k) for k in
                              ("delta", "tau", "nW", "max_hidden_dist", "hidden_in_W",
                               "verified_hidden")})
