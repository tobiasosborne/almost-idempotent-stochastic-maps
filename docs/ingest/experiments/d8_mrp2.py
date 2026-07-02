#!/usr/bin/env python3 -u
"""
d8_mrp2.py -- MRP decider, BARYCENTRIC-FRAME form (built on the PROVEN d7 shell mechanism).

Lesson from the first encoder attempt (d8_mrp.py): pinning v with a direct -H poke makes
neg(v) = H ~ 0.5 tau, which BLOWS UP the realized delta (honest tau ~ sqrt(H)) and destroys
the rho-scale -- the conjecture floor needs delta ~ tau^2 ~ 3.49 H^2, i.e. neg ~ H^2, NOT
neg ~ H.  A naive far poke costs neg = H.  HLC says you CANNOT make a NON-EXPOSED far vertex
cheaper than O(H^2); the d7 hunt confirmed the only mechanism (ring shell) collapses H to ~0
so delta/H^2 -> 300..8600.  The MRP question is precisely whether the TWO-LEVEL web breaks
that collapse.

So we build directly in barycentric coordinates over a frame R0 = [I_r | 0] (d3_main.bary_to_P):
rows of P = the bary coefficient vectors (length r), padded.  THEN neg(p_i) = neg part of
the bary coefficients -- directly controllable.  v is hidden NOT by a poke but by being a
near-affine combination of the SUPPLIER rows (the MI: a hidden vertex is a delta-almost-convex
combination of others, fable Lemma SS).  The suppliers/blockers form the surrounding web.

ARCHITECTURE in bary coords (frame dirs e_0..e_{r-1} are the exposed base vertices = W):
  v   : bary = (1+s) * (group-supplier combo) - s * (anchor)   -- a hidden vertex at "height"
        controlled by s; external mass sigma_v = s on the group dirs; neg(v) = s * (anchor mass).
  v'' : analogous on a second pillar, height ~ 2 sigma_v, external mass sigma_vpp ~ rho/2.2.
  blockers: rho-far rows at v's height that surround v (zero-sum rho-wiggles) so v fails
            exposedness -- the d7 shell, at the CORRECT bary scale.
  supplier groups: k_groups rho-split pairs at "level" ell, feeding v's external mass.
  low rows: sub-C financing rows (extra exposed frame vertices used as anchors of the splits).

We then run the alternating (Lambda,R) LP (d7_fti2) to MINIMIZE max-row-neg over realization
freedom, pinning the load-bearing linear data, and VERIFY robustly post-hoc.  The decision:
sweep sigma_v; does any verified instance reach delta/H^2 < 3 (refutation), or does the entry
gate / neg objective block it everywhere (then mine certificates)?
"""
import sys, os, json, time, itertools
import numpy as np

from d1_infra import check_idempotent, neg_mass, dist1_to_conv, exposed_margin
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_main import bary_to_P

np.set_printoptions(precision=5, suppress=True, linewidth=160)
C, c = 4.0, 0.25


# ======================================================================
# BARY-FRAME MRP family.
# ======================================================================
def build_mrp_bary(sigma_v, H, k_groups=2, ell=None, group_sep=None, ma=3, nlow=3,
                   nb=2, coincident_groups=False, seed=0):
    """Return (bary_rows [list of len-r vectors incl. r archetype rows], r, idx).

    Coordinates of the frame (exposed base vertices = candidate W):
      anchors  : ma dirs (the simplex C base)            indices 0..ma-1
      group    : k_groups dirs (private supplier sites)  ma .. ma+k_groups-1
      low      : nlow dirs (sub-C financing vertices)    ma+k_groups .. r-1
    r = ma + k_groups + nlow.

    H        : the "height" handle = how far v is pushed out of conv(frame) by the negative
               anchor coefficient (neg(v) ~ s where s sets external mass).  We DECOUPLE the
               external mass sigma_v (on group dirs) from the negativity by routing v's
               positive mass through suppliers (so v is a near-convex combo of suppliers,
               paying neg only s = the small overshoot, NOT H).
    sigma_v  : external coefficient mass at v on the group dirs.
    ell      : supplier level handle.
    group_sep: rho-separation of the groups.
    """
    rng = np.random.default_rng(seed)
    if ell is None:
        ell = 0.3
    tau_guess = None
    base = list(range(ma))
    grp = list(range(ma, ma + k_groups))
    low = list(range(ma + k_groups, ma + k_groups + nlow))
    r = ma + k_groups + nlow
    if group_sep is None:
        group_sep = 0.2

    def vz():
        return np.zeros(r)

    # archetype rows (the frame): e_0..e_{r-1}  -- exposed vertices
    rows = [np.eye(r)[a].copy() for a in range(r)]
    idx = {"r": r, "ma": ma, "base": base, "grp": grp, "low": low,
           "sigma_v": sigma_v, "H": H, "ell": ell, "group_sep": group_sep,
           "k_groups": k_groups, "coincident_groups": bool(coincident_groups),
           "archetypes": list(range(r)), "anchors": list(base)}

    # SUPPLIER GROUPS: each a rho-split pair.  Each member lives mostly on its group dir
    # (so it can feed v's external mass there) but is pushed to "level" ell by mixing in a
    # low (financing) dir, and rho-split by a zero-sum wiggle between two low dirs.
    suppliers = []; group_members = []
    for q in range(k_groups):
        site = grp[q] if not coincident_groups else grp[0]
        gmem = []
        for sgn in (+1.0, -1.0):
            sup = vz()
            sup[site] = 1.0 - ell
            sup[low[(2 * q) % nlow]] = ell
            # rho-split zero-sum wiggle
            if nlow >= 2:
                sup[low[(2 * q) % nlow]] += sgn * group_sep / 2.0
                sup[low[(2 * q + 1) % nlow]] -= sgn * group_sep / 2.0
            suppliers.append(len(rows)); gmem.append(len(rows)); rows.append(sup)
        group_members.append(gmem)
    idx["suppliers"] = suppliers; idx["group_members"] = group_members

    # TOP vertex v: a near-convex combination of suppliers (external mass sigma_v spread on
    # them) plus (1 - sigma_v) on its OWN private direction... but v has no private frame dir;
    # instead we PUSH v out by a small negative anchor coefficient s (the height handle).
    #   v = (1 + s) * (supplier-mix) - s * anchor0
    # neg(v) = s * (anchor0 mass) ~ s.   The external (off-anchor) mass = sigma_v := the
    # weight on the suppliers' group dirs.  "Height" H ~ distance of v from conv(W); we set s
    # so that the realized height matches the target (verified post-hoc).
    sup_mix = np.zeros(r)
    w_each = sigma_v / len(suppliers)
    for sidx in suppliers:
        sup_mix += w_each * rows[sidx]
    # remaining mass (1 - sigma_v) on anchor0's direction (v's "own site" surrogate)
    sup_mix[base[0]] += (1.0 - sigma_v)
    s = H                                  # height handle = the overshoot/negativity
    vrow = (1.0 + s) * sup_mix.copy()
    vrow[base[1 % ma]] -= s                # negative anchor coefficient => pushes v out
    # renormalize to rowsum 1 (the (1+s)*mix - s*anchor already sums to 1 if sup_mix sums 1)
    idx["v"] = len(rows); rows.append(vrow)

    # BLOCKERS: at v's height, rho-far, surrounding v (zero-sum group_sep-wiggles so no affine
    # functional separates v).  Built as v + a zero-sum wiggle in group/low dirs.
    blockers = []
    for j in range(nb):
        b = vrow.copy()
        if k_groups >= 1 and nlow >= 1:
            b[grp[j % k_groups]] += group_sep / 2.0
            b[low[j % nlow]] -= group_sep / 2.0
        blockers.append(len(rows)); rows.append(b)
    idx["blockers"] = blockers

    # v'' psi-max vertex: analogous, second pillar (anchor2), height ~2 sigma_v, big external
    sigma_vpp = min(0.45, 4.0 * 0.25)      # placeholder; rho/2.2 in honest-tau set post-hoc
    vpp_mix = np.zeros(r)
    for sidx in suppliers:
        vpp_mix += (sigma_v / len(suppliers)) * rows[sidx]
    vpp_mix[base[2 % ma]] += (1.0 - sigma_v)
    s2 = min(2.0 * sigma_v + H, 0.9)
    vpp = (1.0 + s2) * vpp_mix.copy()
    vpp[base[(2 + 1) % ma]] -= s2
    idx["vpp"] = len(rows); rows.append(vpp)
    idx["s_v"] = s; idx["s_vpp"] = s2

    return rows, r, idx


def realize_and_verify(bary_rows, r, idx):
    """Build P = bary_to_P, verify robustly (honest tau from instance delta)."""
    P = bary_to_P(bary_rows, r)
    return P, verify_bary(P, idx)


def verify_bary(P, idx, idem_tol=1e-7):
    P = np.asarray(P, float); n = P.shape[0]
    chk = check_idempotent(P, tol=idem_tol)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "idem_resid": float(chk["idem_resid"]),
           "delta": float(delta), "max_neg": float(delta), "n": n}
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
    vert_vpp, _ = is_row_vertex_robust(P, vpp)
    out["v_vertex"] = bool(vert_v); out["vpp_vertex"] = bool(vert_vpp)
    dv, _ = dist1_to_conv(P, W, v); dvpp, _ = dist1_to_conv(P, W, vpp)
    out["dist_v"] = float(dv); out["dist_vpp"] = float(dvpp)
    H = dv; out["H_real"] = float(H)
    okv, mv, _ = exposed_margin(P, v, rho, kappa)
    okvpp, mvpp, _ = exposed_margin(P, vpp, rho, kappa)
    out["v_margin"] = (None if mv is None else float(mv))
    out["vpp_margin"] = (None if mvpp is None else float(mvpp))
    out["v_fails_exposed"] = bool(not okv)
    out["vpp_fails_exposed"] = bool(not okvpp)
    out["neg_v"] = float(np.maximum(-P[v], 0).sum())
    out["neg_vpp"] = float(np.maximum(-P[vpp], 0).sum())
    out["all_anchors_in_W"] = bool(all(a in W for a in idx["anchors"]))
    if H > 1e-9:
        out["delta_over_H2"] = float(delta / (H * H))
        out["H_over_tau"] = float(H / tau)
    else:
        out["delta_over_H2"] = None; out["H_over_tau"] = 0.0
    out["entry_pass"] = bool(chk["ok"] and vert_v and (not okv) and H > 1e-9)
    out["pass"] = out["entry_pass"]
    return out


if __name__ == "__main__":
    print("d8_mrp2 self-test", flush=True)
    rows, r, idx = build_mrp_bary(sigma_v=0.1, H=0.05, k_groups=2, ell=0.3, ma=3, nlow=4, nb=4)
    P, ver = realize_and_verify(rows, r, idx)
    print("delta=%.4f tau=%.4f rho=%.4f H_real=%.4f v_fails=%s v_margin=%.4f nW=%d d/H2=%s"
          % (ver["delta"], ver["tau"], ver["rho"], ver["H_real"], ver["v_fails_exposed"],
             ver.get("v_margin") or 0, ver["nW"], ver.get("delta_over_H2")), flush=True)
    v = idx["v"]
    print("blockers dist to v:", [round(float(np.abs(P[v]-P[b]).sum()),4) for b in idx["blockers"]], flush=True)
