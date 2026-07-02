#!/usr/bin/env python3 -u
"""
d3_hunt_robust.py -- broad ADVERSARIAL hunt for ANY genuinely hidden row, using the
multiplicity-correct robust verifier (d3_vertexfix).  After the coincident-row vertex
artifact was fixed, the structured families (F1/F2) produce NO hidden rows.  Here we
hunt widely (random exact idempotents in the canonical R=[I_r|0] family + the general-R
alternation) to find the MAX honest dist_1(row, conv W)/tau over many random P.  A large
robust dist/tau would be a real counterexample signal; dist/tau ~ 0 across the board is
strong evidence HCC holds (nothing hides at the (C tau, c tau) scaling).

We sample random bottom-blocks Lambda (n x r, top=I_r, rows sum 1) with controlled
negativity, build P, and compute the robust max dist/tau over ALL rows (not just a
designated hidden set).  Crash-safe checkpoints; flushed.
"""
import sys, os, json, time
import numpy as np
from d1_infra import neg_mass, dist1_to_conv
from d3_vertexfix import well_exposed_set_robust, verify_robust
from d3_main import bary_to_P

OUT = "out/d3_hunt_robust.json"
RES = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S")},
       "samples": [], "worst": None}


def save():
    with open(OUT, "w") as f:
        json.dump(RES, f, indent=2, default=float)


def random_canonical(r, n_extra, neg_scale, rng):
    """random P=Lam R0, R0=[I_r|0], top block I_r, extra rows = random signed bary
       coords (rows sum 1) with negativity ~ neg_scale."""
    n = r + n_extra
    rows = [np.eye(r)[a] for a in range(r)]
    for _ in range(n_extra):
        x = rng.standard_normal(r) * neg_scale
        x -= (x.sum() - 1) / r        # rows sum to 1
        rows.append(x)
    return bary_to_P(rows, r), list(range(r, n))


def max_robust_ratio(P, C=4.0, c=0.25):
    nm, delta = neg_mass(P)
    if delta <= 1e-12:
        return 0.0, 0.0, None, 0
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, info = well_exposed_set_robust(P, rho, kappa)
    n = P.shape[0]
    worst = 0.0; argi = -1
    for i in range(n):
        di, _ = dist1_to_conv(P, W, i)
        if di / tau > worst:
            worst = di / tau; argi = i
    return float(worst), tau, W, argi


def hunt(n_samples=400, seed=0):
    rng = np.random.default_rng(seed)
    worst_overall = {"ratio": 0.0}
    configs = [(r, ne) for r in (3, 4, 5, 6) for ne in (1, 2, 3, 5, 8)]
    t0 = time.time()
    cnt = 0
    for s in range(n_samples):
        r, ne = configs[rng.integers(len(configs))]
        neg_scale = float(rng.uniform(0.05, 1.5))
        P, extra = random_canonical(r, ne, neg_scale, rng)
        ratio, tau, W, argi = max_robust_ratio(P)
        cnt += 1
        rec = {"r": r, "n_extra": ne, "neg_scale": neg_scale,
               "tau": tau, "max_ratio": ratio, "argmax": argi,
               "nW": len(W) if W is not None else 0}
        RES["samples"].append(rec)
        if ratio > worst_overall["ratio"]:
            worst_overall = {"ratio": ratio, "r": r, "n_extra": ne,
                             "neg_scale": neg_scale, "tau": tau, "P": P.tolist(),
                             "W": list(map(int, W)) if W is not None else [], "argmax": argi}
            RES["worst"] = worst_overall
            print(f"  [s={s}] NEW WORST robust dist/tau={ratio:.4f} (r={r} ne={ne} "
                  f"neg_scale={neg_scale:.3f} tau={tau:.4f})", flush=True)
        if s % 50 == 0:
            print(f"  ... {s}/{n_samples} done, worst so far={worst_overall['ratio']:.4f} "
                  f"({time.time()-t0:.1f}s)", flush=True)
            save()
    RES["meta"]["n_samples"] = cnt
    RES["meta"]["worst_ratio"] = worst_overall["ratio"]
    save()
    return worst_overall


if __name__ == "__main__":
    print("=" * 70, flush=True)
    print("d3_hunt_robust: broad hunt for ANY hidden row (robust W)", flush=True)
    print("=" * 70, flush=True)
    w = hunt(n_samples=600, seed=1)
    print(f"\nWORST robust dist/tau over all samples: {w['ratio']:.4f}", flush=True)
    if w["ratio"] < 0.5:
        print("=> No row hides: robust dist/tau ~ 0 across the board. HCC-consistent "
              "(nothing far-from-conv-W exists at the (C tau,c tau) scaling).", flush=True)
    else:
        print("=> POTENTIAL hidden row found; AUDIT the worst P (saved) carefully for "
              "coincidence/solver artifacts before claiming a counterexample.", flush=True)
    print("saved", OUT, flush=True)
