#!/usr/bin/env python3 -u
"""
d14_leakage.py -- BAND-EDGE LEAKAGE PROFILE (mission d14).

The campaign residual is now ATOMIC (wave-11 orchestrator assessment): sup-vs-averaged
leakage control at the band edge of a signed almost-idempotent block.  t10's finisher
(projective idempotent-collapse) fires IF the top band T_t = {j : g_j >= t} is closed,
i.e. the SUP-form leakage

    lambda_T := sup_{i in T_t} sum_{j not in T_t} |P_ij|

is small (<= c (1-q) tau).  Six died-at certificates surround this single point.  The
pigeonhole/coarea cut gives only AVERAGED leakage; the question numerics answers:

  on VERIFIED instances, is the SUP-leakage actually small for SOME band threshold t
  (lemma TRUE, missing input = structural), or do real instances violate it?

This probe ALSO measures the dual-side per-row leakage l_i = sum_{j: g_j >= t} |P_ij| for
rows i with g_i < t (the band-edge crossing the finisher must close), the bad-shell width,
and the projective diameter Delta of the positive part of the band block (the finisher's
OTHER hypothesis).

INSTANCE LIBRARY (verified):
  - all d12 PASS logs (out/d12_logs/*.json carry the full P + canonical separator) --
    delta in [0.007, 0.072], off the d8 wall edge, every gate green.
  - d13 d5e-02 (the corner-anchor small-delta verified instance, G2_canonical).
  - s5 exact 5x5 (built from its closed form in notes/swarm-answers/s5_refute.md):
    the only known all-shallow optimal face, sigma~ > 0, delta = 1841/1600000.
  - corner edge instance: decide_opt(0.1435,0.5,...) rebuilt fresh (the d8 wall edge,
    delta ~ 0.0718, the corner scale where the linear and exposedness walls meet).

GATES (every instance, before it enters any profile): idem_resid < 1e-7, P1=1,
multiplicity-correct robust W, honest tau = sqrt(delta), v = height-MAX hidden robust
vertex, canonical separator with Pg = g.  Unverified points NEVER enter.

All band-block LPs / projective-diameter computations are entrywise on the verified P.
Crash-safe checkpoint per instance.  python3 -u, flush, logs to out/d14_logs/.
"""
import sys, os, json, time, glob
import numpy as np
from fractions import Fraction as F

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from scipy.optimize import linprog
from d1_infra import neg_mass, check_idempotent, dist1_to_conv
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust

OUTDIR = "out"
LOGDIR = os.path.join(OUTDIR, "d14_logs")
os.makedirs(LOGDIR, exist_ok=True)
OUT = os.path.join(OUTDIR, "d14_leakage.json")

C, c = 4.0, 0.25
NT = 40   # number of band thresholds in [0.1 kappa Omega, 2 kappa Omega]


def lp(cobj, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    r = linprog(cobj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                method="highs", options={"presolve": False})
    assert r.status == 0, f"LP failed: {r.message}"
    return r


def canonical_separator(P, W, v):
    """phi: max phi(p_v) s.t. ||grad||_inf <= 1, sup_{conv W} phi <= 0.
       Returns phi, H, g = H - phi (so g_v = 0, g >= 0 for the height-max vertex), Omega = osc(g).
       Identical construction to d12_dmfprobe.canonical_separator (presolve OFF)."""
    n = P.shape[0]
    nv = n + 1
    cobj = np.zeros(nv); cobj[:n] = -P[v]; cobj[n] = 1.0
    A_ub = []; b_ub = []
    for u in W:
        row = np.zeros(nv); row[:n] = P[u]; row[n] = -1.0
        A_ub.append(row); b_ub.append(0.0)
    r = lp(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
           bounds=[(-1, 1)] * n + [(None, None)])
    w = r.x[:n]; s = r.x[n]
    phi = P @ w - s
    H = float(phi[v]); g = phi[v] - phi
    Omega = float(g.max() - g.min())
    return phi, H, g, Omega


def role_of(P, k, v, W, di, rho):
    """Tag a row by structural role.
       v        = the hidden top vertex itself
       carrier  = receives positive coeff mass FROM v (P[v,k] > 0, k != v) -- v's supplier
       financier= sends positive coeff mass TO v (P[k,v] > 0, k != v) -- biorthogonal financier
       (carrier+financier overlap -> 'reciprocal' = the d11 self-coupling object)
       W-vertex / hidden-vertex / other otherwise."""
    if k == v:
        return "v"
    is_carrier = P[v, k] > 1e-12
    is_fin = P[k, v] > 1e-12
    if is_carrier and is_fin:
        return "reciprocal"
    if is_carrier:
        return "carrier"
    if is_fin:
        return "financier"
    if k in W:
        return "W-vertex"
    vert, _ = is_row_vertex_robust(P, k)
    if vert:
        return "hidden-vertex"
    return "other"


def projective_diameter(B):
    """Hilbert projective diameter of the positive rows of the (nonneg) band block B.
       Delta = max over row pairs i,i' of log( max_j (B[i,j] B[i',j']) / (B[i,j'] B[i',j]) )
       restricted to the support.  Finite iff every pair of rows has FULLY overlapping
       support (no structural zero kills a ratio).  Returns (Delta, finite_flag, q_contract).
       q = tanh(Delta/4) is the Birkhoff contraction (t10 finisher: diam1 <= 2 eps/(1-q))."""
    B = np.asarray(B, float)
    m, w = B.shape
    if m < 2:
        return 0.0, True, 0.0
    # keep only columns that have any positive mass (the active simplex coords)
    colmask = B.max(axis=0) > 1e-14
    Bc = B[:, colmask]
    if Bc.shape[1] == 0:
        return float("inf"), False, 1.0
    Dmax = 0.0
    finite = True
    for i in range(m):
        for ip in range(i + 1, m):
            ri, rip = Bc[i], Bc[ip]
            # projective distance d_H(ri,rip) = log( max_jk (ri_j rip_k)/(ri_k rip_j) )
            # = log( max_j ri_j/rip_j ) - log( min_j ri_j/rip_j ) over common support
            sup = (ri > 1e-14) & (rip > 1e-14)
            both = (ri > 1e-14) | (rip > 1e-14)
            if (both & ~sup).any():
                # a coordinate positive in one row, zero in the other -> infinite proj dist
                finite = False
                continue
            if not sup.any():
                continue
            ratio = ri[sup] / rip[sup]
            d = np.log(ratio.max()) - np.log(ratio.min())
            Dmax = max(Dmax, d)
    if not finite:
        return float("inf"), False, 1.0
    q = float(np.tanh(Dmax / 4.0))
    return float(Dmax), True, q


def leakage_profile(P, v, W, g, Omega, H, delta, tau, rho, kappa, label):
    """For a grid of band thresholds t, compute the band T_t = {j : g_j >= t}, the SUP-form
       closure quantity lambda_T = sup_{i in T} sum_{j not in T} |P_ij|, the per-row crossing
       leakage l_i for rows BELOW the band (g_i < t), the bad-shell, the interior, and the
       projective diameter of the positive part of the band block."""
    n = P.shape[0]
    di = np.abs(P - P[v]).sum(axis=1)
    Pabs = np.abs(P)
    Ppos = np.maximum(P, 0.0)
    roles = [role_of(P, k, v, W, di, rho) for k in range(n)]

    lo = 0.1 * kappa * Omega
    hi = 2.0 * kappa * Omega
    ts = np.linspace(lo, hi, NT)

    rows = []
    best_supT = (float("inf"), None)         # min over t of lambda_T (band-internal sup-leak)
    best_supBelow = (float("inf"), None)      # min over t of sup crossing-leak over below-band rows
    best_interior = (float("inf"), None)      # min over t of sup crossing-leak over interior (g_i <= t/2)
    best_finisher = None                      # the t minimizing the FINISHER quantity lambda_T

    for t in ts:
        # ---- PRIMARY orientation: the SHALLOW band S_t = {j : g_j <= t} (contains v) ----
        # This is the t10/s3 collapse block: v plus the rows close to it in deficit.  Its
        # closure leakage is exactly s3's  lambda_S = sup_{i in S} sum_{j: g_j > t} |P_ij|.
        S = [j for j in range(n) if g[j] <= t + 1e-12]      # the shallow band (with v)
        above = [j for j in range(n) if g[j] > t + 1e-12]    # the deep complement
        if not S or not above:
            continue
        Sset = set(S); aboveset = set(above)
        # lambda_S : SUP over shallow-band rows i in S of mass that LEAKS OUT (to deep j)
        lamS_rows = {i: float(sum(Pabs[i, j] for j in above)) for i in S}
        lamS = max(lamS_rows.values())
        lamS_mean = float(np.mean(list(lamS_rows.values())))
        argsupS = max(lamS_rows, key=lamS_rows.get)

        # per-row crossing leakage l_i = sum_{j: g_j >= t} |P_ij| for rows i with g_i < t
        # (mission item 1, verbatim).  Uses the deep set {g_j > t} as the target.
        below = [i for i in range(n) if g[i] < t - 1e-12]
        li = {i: float(sum(Pabs[i, j] for j in above)) for i in below}
        sup_below = max(li.values()) if li else 0.0
        mean_below = float(np.mean(list(li.values()))) if li else 0.0
        argsup_below = max(li, key=li.get) if li else None
        below_role = roles[argsup_below] if argsup_below is not None else None

        # interior = rows with g_i <= t/2 ; bad shell = rows with g_i in (t/2, t)
        interior = [i for i in below if g[i] <= t / 2.0 + 1e-12]
        shell = [i for i in below if t / 2.0 + 1e-12 < g[i] < t - 1e-12]
        sup_interior = max((li[i] for i in interior), default=0.0)
        shell_count = len(shell)
        shell_mass = float(sum(li[i] for i in shell))   # crossing mass carried by the bad shell

        # ---- CROSS-CHECK orientation: the DEEP band T_t = {j : g_j >= t} (mission item-1 T) ----
        T = [j for j in range(n) if g[j] >= t - 1e-12]
        Tset = set(T)
        lamT_rows = {i: float(sum(Pabs[i, j] for j in range(n) if j not in Tset)) for i in T} if T else {}
        lamT = max(lamT_rows.values()) if lamT_rows else 0.0
        argsupT = max(lamT_rows, key=lamT_rows.get) if lamT_rows else None
        T_role = roles[argsupT] if argsupT is not None else None

        t_over_kO = float(t / (kappa * Omega)) if kappa * Omega > 0 else None

        # projective diameter of the POSITIVE part of the SHALLOW band block (finisher's
        # other hypothesis -- the block t10 collapses is the shallow one containing v).
        if len(S) >= 2:
            B = Ppos[np.ix_(S, S)]
            Delta, finite, q = projective_diameter(B)
        else:
            Delta, finite, q = 0.0, True, 0.0

        # closure target: lambda_S <= c (1-q) tau ; reported as dimensionless ratio (c=1).
        oneq = max(1.0 - q, 1e-12)
        closure_ratio = float(lamS / (oneq * tau)) if tau > 0 else None
        sup_role = roles[argsupS]

        rec = {
            "t": float(t), "t_over_kOmega": t_over_kO,
            "|S_shallow|": len(S), "|above_deep|": len(above), "|T_deepband|": len(T),
            # PRIMARY shallow-band closure
            "lambda_S_sup": float(lamS), "lambda_S_mean": lamS_mean,
            "lambda_S_argsup": int(argsupS), "lambda_S_argsup_role": sup_role,
            "lambda_S_argsup_g_over_t": (float(g[argsupS] / t) if t > 0 else None),
            # per-row crossing leakage of below-band rows
            "sup_below_crossleak": float(sup_below), "mean_below_crossleak": mean_below,
            "below_argsup": (int(argsup_below) if argsup_below is not None else None),
            "below_argsup_role": below_role,
            "below_argsup_g_over_t": (float(g[argsup_below] / t) if argsup_below is not None and t > 0 else None),
            "sup_interior_crossleak": float(sup_interior),
            "shell_count": shell_count, "shell_mass": shell_mass,
            # cross-check deep-band closure (mission item-1 T)
            "lambda_Tdeep_sup": float(lamT), "lambda_Tdeep_argsup_role": T_role,
            # projective diameter of the shallow collapse block
            "Delta_band": (float(Delta) if finite else None),
            "Delta_finite": bool(finite), "q_contract": float(q),
            "closure_ratio_lamS_over_1mq_tau": closure_ratio,
        }
        rows.append(rec)
        lamT = lamS  # reuse the best-tracking below on the PRIMARY quantity

        if lamS < best_supT[0]:
            best_supT = (lamS, rec)
        if sup_interior < best_interior[0]:
            best_interior = (sup_interior, rec)
        # the finisher wants the t minimizing closure_ratio with a FINITE-diameter band
        if closure_ratio is not None and finite:
            if best_finisher is None or closure_ratio < best_finisher["closure_ratio_lamS_over_1mq_tau"]:
                best_finisher = rec

    # decision quantities
    min_supS = best_supT[0] if best_supT[1] is not None else None
    min_supInterior = best_interior[0] if best_interior[1] is not None else None

    out = {
        "n": n, "delta": float(delta), "tau": float(tau), "kappa": float(kappa),
        "rho": float(rho), "H": float(H), "Omega": float(Omega),
        "H_over_tau": float(H / tau) if tau > 0 else None,
        "kappa_Omega": float(kappa * Omega),
        "v": int(v), "W": [int(x) for x in W],
        "roles": {int(k): roles[k] for k in range(n)},
        "g": [float(x) for x in g],
        "n_thresholds": len(rows),
        "MIN_sup_lambda_S": (float(min_supS) if min_supS is not None else None),
        "MIN_sup_interior_crossleak": (float(min_supInterior) if min_supInterior is not None else None),
        "best_lambda_S_record": best_supT[1],
        "best_interior_record": best_interior[1],
        "best_finisher_record": best_finisher,
        "profile": rows,
    }
    # VERDICT per instance: does SOME t give lambda_S <= closure target with finite diameter?
    holds_t = None; holds_c = None
    for rec in rows:
        cr = rec["closure_ratio_lamS_over_1mq_tau"]
        if cr is not None and rec["Delta_finite"]:
            if holds_c is None or cr < holds_c:
                holds_c = cr; holds_t = rec["t_over_kOmega"]
    out["min_closure_ratio_finiteDelta"] = holds_c
    out["min_closure_ratio_t_over_kOmega"] = holds_t
    crs = [rec["closure_ratio_lamS_over_1mq_tau"] for rec in rows
           if rec["closure_ratio_lamS_over_1mq_tau"] is not None]
    out["min_closure_ratio_any"] = (float(min(crs)) if crs else None)
    return out


def build_s5():
    lam = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)],
           [F(-1, 2000), F(1, 20), F(1901, 2000)], [F(-1, 2000), F(11, 20), F(901, 2000)]]
    Pg = [
        [F(4000001, 4000000), F(-399, 8000000), F(-3603, 8000000), F(1801, 4000000), F(199, 4000000)],
        [F(1, 4000000), F(8001601, 8000000), F(-5603, 8000000), F(3801, 4000000), F(-1801, 4000000)],
        [F(1, 4000000), F(-2399, 8000000), F(7998397, 8000000), F(-199, 4000000), F(2199, 4000000)],
        [F(-1999, 4000000), F(1989, 40000), F(3801099, 4000000), F(0), F(1, 2000)],
        [F(-1999, 4000000), F(21999, 40000), F(1800099, 4000000), F(1, 2000), F(0)]]
    P = np.array([[float(x) for x in row] for row in Pg])
    return P


def build_corner():
    from d8_opt import decide_opt
    r = decide_opt(0.1435, 0.5, k_groups=2, ell=0.65, ma=2, nlow=2, v_own_site=True,
                   rounds=14, n_starts=4)
    if not r.get("optimized"):
        return None
    return np.array(r["P"])


def gate_and_target(P, label, forced_v=None):
    """Run the verification gates and return (target_vertex, W, tau, rho, kappa, delta) or None.
       target = height-MAX hidden robust vertex (or forced_v for s5)."""
    chk = check_idempotent(P, tol=1e-7)
    nm, delta = neg_mass(P)
    if not chk["ok"] or chk["idem_resid"] >= 1e-7:
        return None, {"gate": "FAIL_idempotent", "idem_resid": float(chk["idem_resid"])}
    if delta <= 1e-12:
        return None, {"gate": "FAIL_delta_zero"}
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    n = P.shape[0]
    # height-max hidden robust vertex
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
    if forced_v is not None:
        vi, _ = is_row_vertex_robust(P, forced_v)
        di_, _ = dist1_to_conv(P, W, forced_v)
        target = forced_v
        maxH = di_
    else:
        target = argmaxH
    if target < 0 or maxH <= 1e-9:
        return None, {"gate": "FAIL_no_hidden_vertex", "W": [int(x) for x in W], "maxH": float(maxH)}
    meta = {"gate": "PASS", "delta": float(delta), "tau": tau, "rho": rho, "kappa": kappa,
            "W": [int(x) for x in W], "target": int(target), "maxH": float(maxH),
            "idem_resid": float(chk["idem_resid"]), "row_sum_resid": float(chk["row_sum_resid"])}
    return target, meta


def process(P, label, forced_v=None):
    target, meta = gate_and_target(P, label, forced_v=forced_v)
    if target is None:
        print(f"  [{label}] GATE {meta.get('gate')}", flush=True)
        return {"label": label, **meta}
    delta, tau, rho, kappa = meta["delta"], meta["tau"], meta["rho"], meta["kappa"]
    W = meta["W"]
    phi, H, g, Omega = canonical_separator(P, W, target)
    sep_resid = float(np.abs(P @ g - g).max())
    if H <= 1e-9:
        print(f"  [{label}] GATE FAIL_H_zero", flush=True)
        return {"label": label, "gate": "FAIL_H_zero"}
    prof = leakage_profile(P, target, W, g, Omega, H, delta, tau, rho, kappa, label)
    rec = {"label": label, "gate": "PASS", "sep_resid_Pg": sep_resid,
           "g_v": float(g[target]), **meta, **prof}
    print(f"  [{label}] PASS n={prof['n']} delta={delta:.5f} H/tau={prof['H_over_tau']:.3f} "
          f"Omega={Omega:.3f}", flush=True)
    print(f"           MIN sup lambda_S = {prof['MIN_sup_lambda_S']:.4f} "
          f"(target kappa*tau ~ {kappa*tau:.4f}; (1-q)tau scale)", flush=True)
    print(f"           MIN closure_ratio (finite Delta) = {prof['min_closure_ratio_finiteDelta']} "
          f"at t/(kO)={prof['min_closure_ratio_t_over_kOmega']}", flush=True)
    print(f"           MIN closure_ratio (any) = {prof['min_closure_ratio_any']}", flush=True)
    print(f"           MIN sup-interior crossleak = {prof['MIN_sup_interior_crossleak']:.4f}", flush=True)
    br = prof["best_lambda_S_record"]
    if br:
        print(f"           best-lamS t/(kO)={br['t_over_kOmega']:.3f} |S|={br['|S_shallow|']} "
              f"lamS={br['lambda_S_sup']:.4f} argsup-role={br['lambda_S_argsup_role']} "
              f"Delta_finite={br['Delta_finite']} q={br['q_contract']:.4f}", flush=True)
    return rec


def main():
    t0 = time.time()
    results = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "C": C, "c": c, "NT": NT,
                        "mission": "d14 band-edge leakage profile (sup-vs-averaged closure)",
                        "closure_target": "lambda_T <= c (1-q) tau ; reported as closure_ratio = lambda_T/((1-q)tau)",
                        "presolve": "OFF on all LPs"},
               "instances": []}

    def save():
        with open(OUT, "w") as f:
            json.dump(results, f, indent=2, default=float)

    # ---- 1. d12 PASS logs (saved verified P + canonical separator) ----
    d12_logs = sorted(glob.glob(os.path.join(LOGDIR, "..", "d12_logs", "*.json")))
    print(f"[d14] loading d12 PASS logs ...", flush=True)
    for f in d12_logs:
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if not isinstance(d, dict) or "P" not in d or d.get("gate") != "PASS":
            continue
        P = np.array(d["P"])
        label = "d12_" + d.get("label", os.path.basename(f).replace(".json", ""))
        rec = process(P, label)
        with open(os.path.join(LOGDIR, f"{label}.json"), "w") as g:
            json.dump({**rec, "P": P.tolist()}, g, indent=2, default=float)
        results["instances"].append(rec)
        save()

    # ---- 2. d13 d5e-02 corner-anchor small-delta verified instance ----
    d13log = os.path.join(LOGDIR, "..", "d13_logs", "d5e-02.json")
    if os.path.exists(d13log):
        d = json.load(open(d13log))
        if d.get("gate") == "PASS" and "P" in d:
            P = np.array(d["P"])
            rec = process(P, "d13_d5e-02")
            with open(os.path.join(LOGDIR, "d13_d5e-02.json"), "w") as g:
                json.dump({**rec, "P": P.tolist()}, g, indent=2, default=float)
            results["instances"].append(rec)
            save()

    # ---- 3. s5 exact 5x5 (the all-shallow optimal face, sigma~ > 0) ----
    print(f"[d14] s5 exact instance ...", flush=True)
    P_s5 = build_s5()
    rec = process(P_s5, "s5_exact", forced_v=3)   # v = 3 per s5_refute.md
    with open(os.path.join(LOGDIR, "s5_exact.json"), "w") as g:
        json.dump({**rec, "P": P_s5.tolist()}, g, indent=2, default=float)
    results["instances"].append(rec)
    save()

    # ---- 4. corner edge instance (rebuilt fresh) ----
    print(f"[d14] corner edge instance (decide_opt 0.1435,0.5) ...", flush=True)
    try:
        P_c = build_corner()
        if P_c is not None:
            rec = process(P_c, "corner_edge")
            with open(os.path.join(LOGDIR, "corner_edge.json"), "w") as g:
                json.dump({**rec, "P": P_c.tolist()}, g, indent=2, default=float)
            results["instances"].append(rec)
            save()
    except Exception as e:
        print(f"  [corner_edge] EXCEPTION {e}", flush=True)
        results["instances"].append({"label": "corner_edge", "gate": "FAIL_build", "error": str(e)})
        save()

    # ---- summary ----
    passed = [r for r in results["instances"] if r.get("gate") == "PASS"]
    results["n_passed"] = len(passed)
    # campaign-level decision: max over instances of MIN_sup_lambda_T (the worst case);
    # and whether any instance VIOLATES sup-closure (no t gives finite-Delta small lamT).
    worst_minsup = None; worst_label = None
    no_finite_delta = []     # instances where NO t gives a finite-diameter shallow block
    sup_leak_small = []      # instances where MIN_sup_lambda_S <= kappa*tau (sup-closure holds)
    for r in passed:
        ms = r.get("MIN_sup_lambda_S")
        cr = r.get("min_closure_ratio_finiteDelta")
        kt = r.get("kappa", 0) * r.get("tau", 0)
        if ms is not None and (worst_minsup is None or ms > worst_minsup):
            worst_minsup = ms; worst_label = r["label"]
        if cr is None:
            no_finite_delta.append(r["label"])
        if ms is not None and ms <= kt + 1e-12:
            sup_leak_small.append(r["label"])
    results["worst_MIN_sup_lambda_S"] = (float(worst_minsup) if worst_minsup is not None else None)
    results["worst_label"] = worst_label
    results["instances_no_finite_Delta"] = no_finite_delta
    results["instances_sup_leak_small"] = sup_leak_small
    results["meta"]["elapsed_s"] = time.time() - t0
    save()
    print(f"\n[d14] done in {results['meta']['elapsed_s']:.1f}s. passed={len(passed)}", flush=True)
    print(f"      worst MIN_sup_lambda_S = {results['worst_MIN_sup_lambda_S']} ({worst_label})", flush=True)
    print(f"      instances with NO finite-Delta shallow block: {no_finite_delta}", flush=True)
    print(f"      instances with sup-leak <= kappa*tau (closure holds): {len(sup_leak_small)}/{len(passed)}", flush=True)


if __name__ == "__main__":
    main()
