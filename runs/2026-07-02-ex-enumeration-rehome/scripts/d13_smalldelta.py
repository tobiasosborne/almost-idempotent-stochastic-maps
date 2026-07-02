#!/usr/bin/env python3 -u
"""
d13_smalldelta.py -- THE DECISIVE SMALL-DELTA PROBE (mission d13).

The sigma~-height-collapse lemma (wave-9) proves: any hidden top VERTEX v with H >> delta
has sigma~_v >= 1 - delta R / H ~ 1 (its positive mass is almost entirely OUTSIDE conv W),
so the corner witness mechanism cannot operate at small delta.  d12's "DMF SUPPORTED"
verdict was measured ONLY at the corner scale (H ~ 2 delta) -- it says nothing about the
flat floor (H ~ 0.536 sqrt(delta) >> delta).

THE question: do VERIFIED hidden-top-VERTEX instances with H ~ 0.536 sqrt(delta) actually
EXIST at small delta?  Targets delta in {3e-3, 1e-3, 3e-4} (plus 1e-2 bridge), with
delta/H^2 in [3.4, 8] i.e. H ~ (0.35-0.54) sqrt(delta) >> 10 delta.

Three outcomes (all major):
  (a) instances verify + witnesses DEEP  -> DMF stands, new mechanism to find.
  (b) instances verify + witnesses SHALLOW -> DMF refuted as stated (persist candidate).
  (c) instances FAIL verification at small delta -> the flat floor is a corner extrapolation
      and the true small-delta law may be LINEAR.  Report exactly what fails per delta.

METHODOLOGY:
  STAGE 1 (entry hunt): per target delta, intensively maximize the HONEST ratio
      H/tau := max_i dist1(p_i, conv W_robust) / tau,  tau = sqrt(delta)
    over exact idempotents P = Lam R0 (R0=[I_r|0]) using THREE generators borrowed verbatim:
      G1 rand_P_fixed_tau  (d3_envtrue: undistorted geometry, EXACT delta = tau^2 control)
      G2 random_canonical  (d3_hunt_robust: signed bary rows, neg_scale control)
      G3 build_shell        (d7_hunt: two distinct poke vertices + shadow shell)
    delta is rescaled to the EXACT target by the affine negativity dial (G1 is exact; G2/G3
    are post-rescaled by shrinking the off-archetype displacement to hit delta=target).
    Record the best instance per delta (max ratio AND, separately, max ratio among instances
    whose argmax row is a robust VERTEX -- the lemma's object).
  STAGE 2 (gate + anatomy): every instance clearing the entry gate (ratio >= RATIO_GATE and
    a hidden robust vertex) gets the FULL d12 witness_anatomy: idem_resid<1e-7, mult-correct W
    (presolve OFF), honest tau, v_fails_exposed, canonical separator, exposedness dual witness
    (residual<=1e-12), depth profile, sigma~ measurement, all-shallow detector.
  HONEST: if NO instance clears the entry gate at a given delta after a genuine hunt, that is
    OUTCOME (c) for that delta -- record max ratio achieved + WHY it fails (no vertex hides /
    ratio collapses / only non-vertices reach the floor).

All LPs presolve OFF.  Crash-safe checkpoint per (delta, generator).  Reuses d3/d7/d12 code
by import; modifies nothing.
"""
import sys, os, json, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from d1_infra import neg_mass, dist1_to_conv, check_idempotent
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_main import bary_to_P
from d3_envtrue import rand_P_fixed_tau
from d3_hunt_robust import random_canonical
from d7_hunt import build_shell
# d12 witness anatomy -- the canonical depth-profile / sigma~ / exposedness-dual machinery
from d12_dmfprobe import witness_anatomy

OUTDIR = "out"
LOGDIR = os.path.join(OUTDIR, "d13_logs")
os.makedirs(LOGDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "d13_smalldelta.json")
CAND = os.path.join(OUTDIR, "d13_DMF_refutation_candidate.json")

C, c = 4.0, 0.25
RATIO_GATE = 0.30          # H/tau >= 0.30 ==> delta/H^2 <= 11.1 ; the floor band is [0.35,0.54]
# 5e-2 is a VALIDATION ANCHOR (the floor H/tau~0.5 is realized there -> proves the pipeline can
# find the floor when it exists); 1e-2 bridges from d12's corner; the 3 small targets are the probe.
TARGETS = [5e-2, 1e-2, 3e-3, 1e-3, 3e-4]


def rescale_to_delta(P, target, r=None):
    """Given an exact canonical idempotent P = Lam R0 (R0=[I_r|0]), rescale the
       off-archetype displacement so that max-row-neg == target, PRESERVING exactness and
       geometry direction.  Works because for P=Lam R0 with archetype top block I_r, shrinking
       (Lam_extra - centroid) by factor s scales every row's negativity; neg is piecewise
       linear & monotone in s, so we bisect s to hit the target.  Re-forms P exactly."""
    P = np.asarray(P, float)
    n = P.shape[0]
    # infer r from the leading identity block (archetype rows)
    if r is None:
        r = 0
        while r < n and abs(P[r, r] - 1.0) < 1e-9 and np.abs(P[r]).sum() - 1.0 < 1e-9 \
                and np.abs(P[r, :r]).sum() < 1e-12 and np.abs(P[r, r + 1:]).sum() < 1e-12:
            r += 1
        if r == 0:
            r = n  # fallback: treat all as bary
    Lam = P[:, :r].copy()              # n x r barycentric coords (R0=[I_r|0] => P[:, :r]=Lam)
    cen = np.ones(r) / r
    disp = Lam - cen                   # displacement from centroid

    def build(s):
        rows = cen + s * disp
        # keep archetypes EXACT identity rows (don't perturb the I_r block)
        for a in range(min(r, n)):
            if a < n:
                rows[a] = np.eye(r)[a]
        return bary_to_P([rows[i] for i in range(n)], r)

    def negof(s):
        Q = build(s)
        _, d = neg_mass(Q)
        return d

    # bisect s in [0, s_hi] for negof(s)=target (negof monotone nondecreasing in s>=0)
    s_lo, s_hi = 0.0, 1.0
    nhi = negof(s_hi)
    tries = 0
    while nhi < target and tries < 60:
        s_hi *= 1.6; nhi = negof(s_hi); tries += 1
    if nhi < target:
        return None  # cannot reach target by scaling (geometry caps it)
    for _ in range(80):
        s_mid = 0.5 * (s_lo + s_hi)
        if negof(s_mid) < target:
            s_lo = s_mid
        else:
            s_hi = s_mid
    return build(s_hi)


def honest_ratio(P):
    """max_i dist1(p_i, conv W_robust)/tau and the argmax row + whether it is a robust vertex."""
    nm, delta = neg_mass(P)
    if delta <= 1e-15:
        return 0.0, delta, 0.0, -1, False, []
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    n = P.shape[0]
    best = 0.0; argi = -1
    for i in range(n):
        if i in W:
            continue
        di, _ = dist1_to_conv(P, W, i)
        if np.isfinite(di) and di / tau > best:
            best = di / tau; argi = i
    is_vert = False
    if argi >= 0:
        is_vert, _ = is_row_vertex_robust(P, argi)
    return float(best), float(delta), float(tau), int(argi), bool(is_vert), list(map(int, W))


def gen_one(kind, target, rng):
    """Produce one exact idempotent at delta=target via generator `kind`, return (P, argi-hint
       dict) or None.  For G1 we build at tau=sqrt(target) directly (exact).  G2/G3 build at a
       free scale then rescale_to_delta."""
    if kind == "G1_fixed_tau":
        r = int(rng.integers(3, 7)); ne = int(rng.integers(1, 6))
        tau = float(np.sqrt(target))
        P = rand_P_fixed_tau(r, ne, tau, rng)
        # rand_P_fixed_tau's analytic tail can over/undershoot delta; rescale to the EXACT
        # target so the achieved delta lands in band (the band gate would reject it otherwise).
        _, d0 = neg_mass(P)
        if not (0.5 * target <= d0 <= 2.0 * target):
            P2 = rescale_to_delta(P, target, r=r)
            P = P2 if P2 is not None else P
        return P
    if kind == "G2_canonical":
        r = int(rng.integers(3, 7)); ne = int(rng.integers(1, 7))
        neg_scale = float(rng.uniform(0.05, 1.5))
        P, _ = random_canonical(r, ne, neg_scale, rng)
        return rescale_to_delta(P, target, r=r)
    if kind == "G3_shell":
        r = int(rng.choice([4, 5, 6])); ma = int(rng.choice([3, 4]))
        if ma > r:
            ma = r - 1
        g = float(rng.choice([0.05, 0.1, 0.2, 0.35]))
        w = float(rng.choice([0.0, 0.01, 0.05]))
        nh = int(rng.choice([0, 2, 4]))
        shell = "none" if nh == 0 else str(rng.choice(["coincident_v", "between", "ring", "shadow"]))
        rad = float(rng.choice([0.02, 0.1, 0.3]))
        P, _, _, _ = build_shell(r, ma, g, w, nh, shell, rad, rng)
        return rescale_to_delta(P, target, r=r)
    return None


def hunt_delta(target, budget_s, seed=0):
    """Intensive entry hunt at one target delta.  Returns the best record + per-generator stats."""
    rng = np.random.default_rng(seed)
    gens = ["G1_fixed_tau", "G2_canonical", "G3_shell"]
    best = {"ratio": -1.0}
    best_vertex = {"ratio": -1.0}     # best among instances whose argmax is a robust VERTEX
    stats = {g: {"n": 0, "max_ratio": 0.0, "max_ratio_vertex": 0.0,
                 "n_vertex_hidden": 0, "n_idem_fail": 0, "n_rescale_fail": 0,
                 "n_delta_off": 0}
             for g in gens}
    # delta-band gate: the achieved delta must land within [target/2, 2*target].  G1's
    # analytic-tail builder can OVERSHOOT delta massively (breakpoint crossings) -> a huge-delta
    # degenerate instance (nW=1, ratio blows up); those are NOT small-delta floor instances and
    # are honestly rejected here.  W must be non-trivial (>=2) for dist-to-conv-W to be meaningful.
    DLO, DHI = target / 1.5, target * 1.5
    t0 = time.time(); trial = 0
    while time.time() - t0 < budget_s:
        kind = gens[trial % len(gens)]; trial += 1
        try:
            P = gen_one(kind, target, rng)
        except Exception:
            P = None
        if P is None:
            stats[kind]["n_rescale_fail"] += 1; continue
        chk = check_idempotent(P, tol=1e-7)
        if not chk["ok"]:
            stats[kind]["n_idem_fail"] += 1; continue
        ratio, delta, tau, argi, is_vert, W = honest_ratio(P)
        if not (DLO <= delta <= DHI):
            stats[kind]["n_delta_off"] += 1; continue
        if len(W) < 2:
            stats[kind]["n_delta_off"] += 1; continue
        stats[kind]["n"] += 1
        if ratio > stats[kind]["max_ratio"]:
            stats[kind]["max_ratio"] = ratio
        if is_vert and argi >= 0 and ratio > 1e-9:
            stats[kind]["n_vertex_hidden"] += 1
            if ratio > stats[kind]["max_ratio_vertex"]:
                stats[kind]["max_ratio_vertex"] = ratio
            if ratio > best_vertex["ratio"]:
                best_vertex = {"ratio": ratio, "delta": delta, "tau": tau, "argi": argi,
                               "gen": kind, "W": W, "P": P.tolist(),
                               "idem_resid": float(chk["idem_resid"]),
                               "delta_over_H2": float(delta / (ratio * tau) ** 2)}
        if ratio > best["ratio"]:
            best = {"ratio": ratio, "delta": delta, "tau": tau, "argi": argi,
                    "gen": kind, "is_vertex": is_vert, "W": W, "P": P.tolist(),
                    "idem_resid": float(chk["idem_resid"]),
                    "delta_over_H2": float(delta / (ratio * tau) ** 2) if ratio > 1e-9 else None}
    return best, best_vertex, stats, trial, time.time() - t0


def main():
    t0 = time.time()
    results = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": C, "c": c,
                        "mission": "d13 small-delta flat-floor probe",
                        "targets": TARGETS, "ratio_gate": RATIO_GATE,
                        "floor_target_ratio": "H/tau in [0.35,0.54] (delta/H^2 in [3.4,8])",
                        "presolve": "OFF on all LPs"},
               "per_delta": [], "verified_instances": [], "all_shallow_found": False}

    def save():
        with open(OUT, "w") as f:
            json.dump(results, f, indent=2, default=float)

    # budget: split across targets; smaller delta is harder so give it more
    total_budget = float(os.environ.get("D13_BUDGET_S", 3600))
    weights = {5e-2: 0.10, 1e-2: 0.16, 3e-3: 0.22, 1e-3: 0.26, 3e-4: 0.26}
    print(f"[d13] entry hunt over {TARGETS}; total budget {total_budget:.0f}s; "
          f"ratio_gate={RATIO_GATE}; floor band H/tau in [0.35,0.54]. presolve OFF.", flush=True)

    for ti, target in enumerate(TARGETS):
        bud = total_budget * weights.get(target, 1.0 / len(TARGETS))
        print(f"\n[d13] ===== target delta = {target:.1e} (budget {bud:.0f}s) =====", flush=True)
        best, best_vertex, stats, ntrial, el = hunt_delta(target, bud, seed=100 + ti)
        floor_ratio = 0.536 / 1.0   # the empirical wall constant
        H_floor = floor_ratio * np.sqrt(target)
        rec = {"target_delta": target, "sqrt_delta": float(np.sqrt(target)),
               "H_floor_if_realized": float(H_floor),
               "n_trials": ntrial, "elapsed_s": el,
               "best_ratio_any": best["ratio"], "best_is_vertex": best.get("is_vertex"),
               "best_delta_over_H2": best.get("delta_over_H2"),
               "best_vertex_ratio": best_vertex["ratio"],
               "best_vertex_delta_over_H2": best_vertex.get("delta_over_H2"),
               "gen_stats": stats}
        print(f"  best ratio (any row)    H/tau = {best['ratio']:.4f}  "
              f"(vertex? {best.get('is_vertex')}, gen {best.get('gen')})", flush=True)
        print(f"  best ratio (VERTEX row) H/tau = {best_vertex['ratio']:.4f}  "
              f"(gen {best_vertex.get('gen')}, delta/H^2={best_vertex.get('delta_over_H2')})",
              flush=True)
        for g, s in stats.items():
            print(f"    {g}: n={s['n']} max_ratio={s['max_ratio']:.4f} "
                  f"max_ratio_vertex={s['max_ratio_vertex']:.4f} "
                  f"n_vertex_hidden={s['n_vertex_hidden']}", flush=True)

        # ENTRY GATE: a hidden robust VERTEX at ratio >= RATIO_GATE
        cleared = (best_vertex["ratio"] >= RATIO_GATE)
        rec["entry_gate_cleared"] = bool(cleared)
        if not cleared:
            rec["outcome"] = "c_no_floor_vertex"
            # diagnose: did ANY row (vertex or not) reach the floor, or did everything collapse?
            if best["ratio"] >= RATIO_GATE and not best.get("is_vertex"):
                rec["failure_reason"] = ("ratio reaches floor but ONLY via a NON-vertex hidden "
                                         "row (coincident/interior); no hidden VERTEX -- the "
                                         "lemma's object is absent")
            elif best["ratio"] < RATIO_GATE:
                rec["failure_reason"] = (f"ratio COLLAPSES: max H/tau over all rows = "
                                         f"{best['ratio']:.4f} << {RATIO_GATE}; nothing hides "
                                         f"near the floor at this delta (entry gate not enterable)")
            else:
                rec["failure_reason"] = "vertex hides but below ratio gate"
            print(f"  -> OUTCOME (c) at delta={target:.1e}: {rec['failure_reason']}", flush=True)
        else:
            # STAGE 2: full witness anatomy on the best hidden-vertex instance
            P = np.array(best_vertex["P"]); argi = best_vertex["argi"]
            idx = {"v": argi}
            extra = {"target_delta": target, "generator": best_vertex["gen"],
                     "entry_ratio": best_vertex["ratio"]}
            anat = witness_anatomy(P, idx, f"d13_d{target:.0e}", extra=extra)
            with open(os.path.join(LOGDIR, f"d{target:.0e}.json"), "w") as f:
                json.dump({**anat, "P": P.tolist()}, f, indent=2, default=float)
            rec["anatomy_gate"] = anat.get("gate")
            if anat.get("gate") == "PASS":
                rec["outcome"] = "ab_verified"
                rec.update({"H": anat["H"], "H_over_tau": float(anat["H"] / anat["tau"]),
                            "delta_over_H2": float(anat["delta"] / anat["H"] ** 2),
                            "sigma_v": anat["sigma_v"], "sigma_tilde": anat["sigma_tilde"],
                            "m_star_observed": anat["m_star_observed"],
                            "E_dmf_5delta_over_tau": anat["E_dmf_5delta_over_tau"],
                            "shallow_fraction": anat["shallow_fraction"],
                            "ALL_SHALLOW": anat["ALL_SHALLOW"],
                            "class_composition": anat["class_composition"],
                            "depth_profile": anat["depth_profile"],
                            "sigma_tilde_lemma_bound": float(1 - anat["delta"] * anat["R"] / anat["H"])})
                results["verified_instances"].append({k: v for k, v in anat.items() if k != "P"})
                print(f"  -> VERIFIED instance: H/tau={rec['H_over_tau']:.3f} "
                      f"delta/H^2={rec['delta_over_H2']:.3f} sigma~={anat['sigma_tilde']:.4f} "
                      f"m*={anat['m_star_observed']:.4f} shallow_frac={anat['shallow_fraction']:.4f}",
                      flush=True)
                if anat["ALL_SHALLOW"]:
                    print(f"  !!!!! ALL-SHALLOW WITNESS (DMF REFUTED-CANDIDATE) at delta={target:.1e}",
                          flush=True)
                    results["all_shallow_found"] = True
                    with open(CAND, "w") as f:
                        json.dump({**anat, "P": P.tolist()}, f, indent=2, default=float)
                    rec["outcome"] = "b_dmf_refuted_candidate"
                else:
                    rec["outcome"] = "a_verified_deep" if rec["shallow_fraction"] < 0.5 else "b_refuted"
            else:
                rec["outcome"] = "c_anatomy_gate_fail"
                rec["anatomy_failure"] = anat.get("gate")
                print(f"  -> anatomy GATE {anat.get('gate')} (entry cleared but full gate fails)",
                      flush=True)
        results["per_delta"].append(rec)
        save()

    results["meta"]["elapsed_s"] = time.time() - t0
    # overall verdict -- based on the SMALL-DELTA PROBE targets ONLY (delta <= 1e-2).
    # delta >= 5e-2 is a VALIDATION ANCHOR proving the pipeline can find the floor when it
    # exists; it must NOT count toward the small-delta verdict.
    ANCHOR_DELTA = 5e-2
    probe = [r for r in results["per_delta"] if r["target_delta"] < ANCHOR_DELTA - 1e-12]
    anchor = [r for r in results["per_delta"] if r["target_delta"] >= ANCHOR_DELTA - 1e-12]
    verified = [r for r in probe if r.get("outcome", "").startswith(("a_", "b_"))]
    cfail = [r for r in probe if r.get("outcome", "").startswith("c")]
    anchor_ok = any(a.get("entry_gate_cleared") for a in anchor)
    if results["all_shallow_found"]:
        verdict = "b_DMF_REFUTED"
    elif verified:
        verdict = "a_DMF_STANDS_new_mechanism" if all(not r.get("ALL_SHALLOW") for r in verified) else "b_DMF_REFUTED"
    else:
        verdict = "c_FLAT_FLOOR_IS_CORNER_EXTRAPOLATION"
    results["VERDICT"] = verdict
    results["verdict_basis"] = ("small-delta probe targets only (delta<1e-2); "
                                "delta>=5e-2 is the validation anchor")
    results["validation_anchor_found_floor"] = bool(anchor_ok)
    results["n_targets_floor_verified"] = len(verified)
    results["n_targets_outcome_c"] = len(cfail)
    save()
    print(f"\n[d13] DONE in {results['meta']['elapsed_s']:.1f}s. VERDICT = {verdict}", flush=True)
    print(f"      floor-verified targets: {len(verified)} ; outcome-(c) targets: {len(cfail)}",
          flush=True)


if __name__ == "__main__":
    main()
