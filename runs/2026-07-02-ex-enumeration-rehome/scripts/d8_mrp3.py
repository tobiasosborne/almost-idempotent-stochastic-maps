#!/usr/bin/env python3 -u
"""
d8_mrp3.py -- MRP DECIDER, working financed-wiggle bary family + optimizer + sweep.

WORKING MECHANISM (found empirically, d8_mrp2 exploration):
  Build in barycentric coords over a frame R0=[I_r|0] (rows of P = bary coeff vectors).
  Suppliers = a rho-split PAIR, each financed POSITIVELY (the split wiggle paid by positive
  mass on low "financing" dirs, NOT by negativity), pushed out of conv(anchors) by a small
  negative anchor coefficient d.  Because the split makes the pair hard to expose, the
  suppliers stay OUT of W (margin < kappa), so conv W = anchors only.  v sits on the
  suppliers (near-convex combo, ~zero extra neg) => v is far from conv W and non-exposed.

KEY EMPIRICAL SCALING of the single-level family:
  H ~ 2d,  delta ~ d   =>  delta/H^2 ~ 1/(4d), MINIMIZED at the largest d before the
  structure collapses (suppliers expose, H->0) ~ d~0.012 => floor delta/H^2 ~ 25 >> 3.49.
  To beat 3.49 we would need H ~ sqrt(delta) (so delta/H^2 = const); a single poke gives
  H ~ delta.  The MRP TWO-LEVEL / k_groups / STACKING question: can stacking amplify H to
  the sqrt(delta) scale?  This decider sweeps sigma_v, k_groups, stacking depth, financing
  level ell, group separation, d, r, n and reports delta/H^2 with robust verification.

DECISION:
  (a) any verified instance with delta/H^2 < 3  => REFUTATION TERRITORY (push, save, stop).
  (b) else the floor stays bounded away below; mine certificates (active/infeasible
      constraints, exposedness margins) as a function of sigma_v.
"""
import sys, os, json, time, itertools
import numpy as np

from d1_infra import check_idempotent, neg_mass, dist1_to_conv, exposed_margin
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_main import bary_to_P

OUTDIR = "out"; os.makedirs(OUTDIR, exist_ok=True)
C, c = 4.0, 0.25
np.set_printoptions(precision=5, suppress=True, linewidth=160)


# ======================================================================
# The MRP bary family (financed-wiggle, two-level capable).
# ======================================================================
def build(d, sigma_v, k_groups=1, ell=0.45, group_sep=None, ma=2, nlow=2, nb=0,
          stack=1, tau_for_sep=None, seed=0, v_own_site=False):
    """Return (bary_rows, r, idx).

    Frame dirs: ma anchors (0..ma-1), k_groups group dirs, then financing low dirs.
      We need >= 2 low dirs PER group to finance that group's split positively.
    d        : poke depth (neg anchor coefficient) of the suppliers -> sets delta ~ d.
    sigma_v  : external coeff mass v draws from the suppliers (the rest on anchor0).
    k_groups : number of supplier groups (each a rho-split pair).
    ell      : financing level (positive low mass per supplier, must exceed group_sep/2).
    group_sep: the split size (~rho); default tau_for_sep*4 with tau_for_sep=sqrt(d).
    stack    : >1 => stack levels (v on suppliers on sub-suppliers ...), the amplification test.
    """
    if tau_for_sep is None:
        tau_for_sep = float(np.sqrt(max(d, 1e-12)))
    if group_sep is None:
        group_sep = 4.0 * tau_for_sep
    nlow_eff = max(nlow, 2 * k_groups + 2)
    base = list(range(ma))
    grp = list(range(ma, ma + k_groups))
    low = list(range(ma + k_groups, ma + k_groups + nlow_eff))
    n_own = 1 if v_own_site else 0
    ax_own = ma + k_groups + nlow_eff if v_own_site else None
    r = ma + k_groups + nlow_eff + n_own
    rows = [np.eye(r)[a].copy() for a in range(r)]
    idx_own = ax_own
    idx = {"r": r, "ma": ma, "base": base, "grp": grp, "low": low, "d": d,
           "sigma_v": sigma_v, "k_groups": k_groups, "ell": ell, "group_sep": group_sep,
           "stack": stack, "archetypes": list(range(r)), "anchors": list(base)}

    # financing level must exceed half the split to keep wiggles positive
    Lfin = max(ell, group_sep / 2.0 + 0.05)

    suppliers = []; group_members = []
    for q in range(k_groups):
        gdir = grp[q]
        la = low[(2 * q) % nlow_eff]
        lb = low[(2 * q + 1) % nlow_eff]
        gmem = []
        for sgn in (+1.0, -1.0):
            s = np.zeros(r)
            s[gdir] = 1.0 - Lfin - d
            s[la] = Lfin / 2.0 + sgn * group_sep / 2.0
            s[lb] = Lfin / 2.0 - sgn * group_sep / 2.0
            s[base[0]] = -d                     # poke out (the only negativity)
            s[gdir] += 2.0 * d                  # keep rowsum 1 (=> excursion ~2d beyond frame)
            suppliers.append(len(rows)); gmem.append(len(rows)); rows.append(s)
        group_members.append(gmem)
    idx["suppliers"] = suppliers; idx["group_members"] = group_members

    # TOP vertex v: convex combo of ALL suppliers (weight sigma_v total) + (1-sigma_v) anchor0,
    # plus a small APEX poke beyond the supplier segment so v is a genuine VERTEX (extreme).
    # The apex pokes along the suppliers' group dir (further out) financed by the low dirs so
    # neg stays ~d.  apex magnitude = d (same scale as the supplier poke).
    sup_mix = np.zeros(r)
    w_each = 1.0 / len(suppliers)
    for sidx in suppliers:
        sup_mix += w_each * rows[sidx]
    # v's "own site": a private frame dir (exposed) if v_own_site, else anchor0.
    own_dir = idx_own if v_own_site else base[0]
    vrow = sigma_v * sup_mix + (1.0 - sigma_v) * np.eye(r)[own_dir]
    # apex: push v beyond the supplier midpoint along group0, financed by pulling equally from
    # the two financing low dirs (zero-sum among positives => stays a vertex, no extra neg).
    apex = d
    g0 = grp[0]
    la0 = low[0]; lb0 = low[1 % nlow_eff]
    if vrow[la0] >= apex / 2.0 and vrow[lb0] >= apex / 2.0:
        vrow[g0] += apex
        vrow[la0] -= apex / 2.0
        vrow[lb0] -= apex / 2.0
    idx["v"] = len(rows); rows.append(vrow)
    idx["apex"] = apex

    # v'' psi-max vertex: a SECOND combo skewed to one group (carries larger external mass),
    # on anchor1 pillar, at higher level.
    sigma_vpp = min(0.9, sigma_v + group_sep)
    vpp_mix = np.zeros(r)
    for sidx in suppliers:
        vpp_mix += w_each * rows[sidx]
    vpp = sigma_vpp * vpp_mix + (1.0 - sigma_vpp) * np.eye(r)[base[min(1, ma - 1)]]
    idx["vpp"] = len(rows); rows.append(vpp)
    idx["sigma_vpp"] = sigma_vpp

    # optional blockers (extra rho-far rows surrounding v) -- not needed if suppliers already
    # de-expose v, but available for the surround test.
    blockers = []
    for j in range(nb):
        b = vrow.copy()
        if k_groups >= 1 and nlow_eff >= 2:
            b[grp[j % k_groups]] += group_sep / 2.0
            b[low[j % nlow_eff]] -= group_sep / 2.0
        blockers.append(len(rows)); rows.append(b)
    idx["blockers"] = blockers
    idx["n"] = len(rows)
    return rows, r, idx


def verify(P, idx, idem_tol=1e-7):
    P = np.asarray(P, float); n = P.shape[0]
    chk = check_idempotent(P, tol=idem_tol)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "idem_resid": float(chk["idem_resid"]),
           "delta": float(delta), "n": n}
    if not chk["ok"]:
        out["pass"] = False; out["reason"] = "not_idempotent"; return out
    if delta <= 1e-12:
        out["tau"] = 0.0; out["pass"] = False; out["reason"] = "delta_zero"; return out
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    out.update({"tau": tau, "rho": rho, "kappa": kappa})
    W, _ = well_exposed_set_robust(P, rho, kappa)
    out["nW"] = len(W); out["W"] = list(map(int, W))
    v = idx["v"]; vpp = idx["vpp"]
    vert_v, _ = is_row_vertex_robust(P, v)
    out["v_vertex"] = bool(vert_v)
    dv, _ = dist1_to_conv(P, W, v)
    out["dist_v"] = float(dv); out["H_real"] = float(dv)
    okv, mv, _ = exposed_margin(P, v, rho, kappa)
    out["v_margin"] = (None if mv is None else float(mv))
    out["v_fails_exposed"] = bool(not okv)
    # supplier exposedness (they must be OUT of W for the mechanism)
    sup_in_W = [int(s) for s in idx["suppliers"] if s in W]
    out["suppliers_in_W"] = sup_in_W
    out["suppliers_all_hidden"] = bool(len(sup_in_W) == 0)
    out["neg_v"] = float(np.maximum(-P[v], 0).sum())
    out["all_anchors_in_W"] = bool(all(a in W for a in idx["anchors"]))
    H = dv
    if H > 1e-9:
        out["delta_over_H2"] = float(delta / (H * H))
        out["H_over_tau"] = float(H / tau)
    else:
        out["delta_over_H2"] = None; out["H_over_tau"] = 0.0
    out["entry_pass"] = bool(chk["ok"] and vert_v and (not okv) and H > 1e-9)
    out["pass"] = out["entry_pass"]
    return out


def run_one(d, sigma_v, **kw):
    rows, r, idx = build(d, sigma_v, **kw)
    P = bary_to_P(rows, r)
    ver = verify(P, idx)
    return P, idx, ver


if __name__ == "__main__":
    print("d8_mrp3 self-test (working financed-wiggle instance)", flush=True)
    P, idx, ver = run_one(0.01, 0.9, k_groups=1, ell=0.45)
    keys = ["delta", "tau", "rho", "H_real", "v_fails_exposed", "v_margin",
            "suppliers_all_hidden", "nW", "delta_over_H2", "H_over_tau", "entry_pass"]
    print({k: (round(ver[k], 4) if isinstance(ver.get(k), float) else ver.get(k)) for k in keys}, flush=True)
