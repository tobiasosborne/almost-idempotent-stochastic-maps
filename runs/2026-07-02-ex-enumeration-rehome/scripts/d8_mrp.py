#!/usr/bin/env python3 -u
"""
d8_mrp.py -- ENCODER + DECIDER for the MRP (middle-regime pinch) two-level architecture,
the LAST open parameter region of HLC (fable-hlc-attack.md Stage 4.4 / Stage 6.2).

ARCHITECTURE (deficit coordinate g; g(v)=0 at the top, g >= H at/below conv W).
The two-level evasion that survives every proved wall in the fable pass:

  * TOP vertex v at g ~ 0, height H above conv W.  External (off-own-site) coefficient
    mass sigma_v in (~3 delta, tau/2).  This is the row whose hidden-ness we want.
  * BLOCKER(s) for v's S-pattern: rho-far rows with S-mass ~ 1, financing the exposer
    failure.  By F-BC they carry <= kappa + 2delta external mass; the split burden falls
    on v (and on v'').
  * The psi-max vertex v'' at level g <= 2 sigma_v carrying forced external mass
    sigma_{v''} ~ rho/2.2 ~ 1.8 tau (the wiggle-rigidity F-WR cost of a rho-split cluster).
  * SUPPLIER GROUPS (k_groups of them) at g-level ell ~ 2.2 delta / sigma feeding the
    external mass.  Pairwise >= rho-separated OR coincident (coincident => wiggle-rigidity
    collapse, a PROVED fact the instance must dodge -- the design tension).
  * Supplier-group splits + surrounds financed by sub-C rows (g < 0 in the affine exposer
    sense; here realized as ordinary low-level rows that carry NO exposedness obligation
    and NO negativity cost).

We REALIZE this in an explicit ell^1 coordinate embedding R^n.  We pin the LOAD-BEARING
linear data only (heights/levels via a height functional, the master fixed-point relations
that DEFINE the architecture, anchor positions) and let the alternating (Lambda,R) LP
choose the rest + minimize max-row-neg.  We then VERIFY honestly post-hoc with the robust,
multiplicity-correct gates (d3_vertexfix): v at dist >= H from conv W, v genuinely failing
(rho,kappa)-exposedness, idempotence < 1e-12.

The g-deficit and the height H:  in this realized geometry the "height" of a row is its
excursion BEYOND conv(anchors) along a poke pillar (exactly as in d7_template).  conv W is
recomputed post-hoc; H = dist_1(v, conv W).  We DO NOT trust the design-time H; only the
post-hoc robust H counts.
"""
import sys, os, json, time, itertools
import numpy as np

import gurobipy as gp
from gurobipy import GRB

from d1_infra import (check_idempotent, neg_mass, check_factorization,
                      dist1_to_conv, exposed_margin)
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_seed import seed_from_targets
from d7_fti2 import lp_optimize_R, lp_optimize_Lambda, alternating_min

np.set_printoptions(precision=5, suppress=True, linewidth=160)


# ======================================================================
# GEOMETRY of the two-level MRP family (explicit ell^1 targets in R^n).
# ======================================================================
#
# Coordinate axes (the frame directions e_a):
#   base block  : ma axes  -> the anchor simplex C = conv A (intended W), level g = H.
#   poke pillar : 1 axis   -> the direction the TOP vertex v is poked OUT of conv C.
#   v''-pillar  : 1 axis   -> the direction v'' (psi-max) is poked out (distinct from v).
#   group axes  : k_groups axes -> private supplier-group sites (rho-separated splits).
#   low axes    : nlow axes -> sub-C financing rows (obligation-free).
#
# Rows (each realized as a row of P = Lambda R, i.e. a signed affine combo of the frame):
#   r archetype identity rows e_0..e_{r-1}     (the frame; canonical exposed vertices)
#   ma anchors  a_t = e_{base_t}               (the simplex C, the intended W)
#   1  top vertex v                            (poked +H along pillar, external mass sigma_v)
#   nb blockers  for v                         (rho-far, S-mass ~ 1; finance exposer failure)
#   1  v'' psi-max vertex                      (poked along v''-pillar to level ~2 sigma_v)
#   per group: 2 supplier rows (a rho-split pair)  + optional surround
#   nlow low financing rows                    (sub-C; carry the supplier splits)
#
# The DEFINING relations we pin as linear constraints (the architecture's "master
# identity" content), all linear in P_ij once the combinatorics are fixed:
#   (H1)  height(v)   = H          (poke pillar coordinate of v)
#   (H2)  height(v'') = h_vpp       (= 2 sigma_v / tau scale, design level of v'')
#   anchors fully pinned (e_{base_t}); archetypes fully pinned (e_a).
# Everything else (blocker realizations, supplier/low realizations, the (Lambda,R) factor)
# is FREE -> the optimizer minimizes max-row-neg.  Failed exposedness of v is VERIFIED
# post-hoc, never encoded.


def build_mrp_targets(sigma_v=0.1, tau=0.1, k_groups=2, ell_supplier=None,
                      group_sep=None, ma=3, nlow=3, nb=2, H=None, seed=0,
                      coincident_groups=False):
    """Construct the explicit ell^1 target rows for one MRP instance.

    sigma_v   : intended external (off-site) coefficient mass at the top vertex v.
    tau       : sqrt(delta) scale used to set rho = 4 tau, kappa = tau/4 design geometry.
    k_groups  : number of supplier groups (each a rho-split pair).
    ell_supplier : design g-level of suppliers (default the budget 2.2*delta/sigma_v with
                   delta=tau^2; capped).
    group_sep : ell^1 separation between groups (default rho = 4 tau; coincident if flagged).
    ma        : number of anchors (the simplex C).
    nlow      : number of sub-C financing rows.
    nb        : number of blockers for v's S-pattern.
    H         : design height of v above conv C (default 0.5*tau -- near the hard wall).
    coincident_groups : force groups coincident (control: wiggle-rigidity collapse).

    Returns (targets [n x n], idx).  targets are square (n x n), rows realizable as
    signed affine combos of the r frame directions.
    """
    rng = np.random.default_rng(seed)
    delta = tau * tau
    rho = 4.0 * tau
    kappa = tau / 4.0
    if H is None:
        H = 0.5 * tau                      # near the empirical hard wall H <= 0.54 tau
    if group_sep is None:
        group_sep = rho                    # rho-separated (else coincident -> collapse)
    if ell_supplier is None:
        ell_supplier = min(2.2 * delta / max(sigma_v, 1e-9), 2.0)  # g-budget level

    # axis layout
    base = list(range(ma))
    ax_pillar = ma                          # v poke pillar
    ax_vpp = ma + 1                         # v'' poke pillar
    grp_ax = list(range(ma + 2, ma + 2 + k_groups))   # group private sites
    low_ax = list(range(ma + 2 + k_groups, ma + 2 + k_groups + nlow))
    r = ma + 2 + k_groups + nlow            # frame dimension

    def vec():
        return np.zeros(r)

    rows = []
    idx = {"r": r, "ma": ma, "tau": tau, "delta": delta, "rho": rho, "kappa": kappa,
           "sigma_v": sigma_v, "H_design": H, "ell_supplier": ell_supplier,
           "group_sep": group_sep, "k_groups": k_groups, "coincident_groups": bool(coincident_groups)}

    # r archetype identity rows (the frame)
    arche = []
    for a in range(r):
        v = vec(); v[a] = 1.0
        arche.append(len(rows)); rows.append(v)
    idx["archetypes"] = arche

    # anchors: simplex C = conv A (the intended W), at level g = H (height 0 above THEM,
    # i.e. the base of the deficit).  a_t = e_{base_t}.
    anchors = []
    for t in range(ma):
        v = vec(); v[base[t]] = 1.0
        anchors.append(len(rows)); rows.append(v)
    idx["anchors"] = anchors

    # The S-pattern site for v: we let v's "own site" be the poke pillar (a private site,
    # so the blocker has to REPLICATE the pillar pattern to block the indicator exposer).
    # TOP vertex v: poked +H beyond anchor0 along the pillar, with external mass sigma_v
    # placed (as design intent) on the supplier groups; negativity compensates the poke.
    #   realized vector (design): mostly on pillar (own site), -H on anchor0 (the poke),
    #   and sigma_v spread on the group sites (external mass).
    vrow = vec()
    vrow[ax_pillar] = 1.0 + H - sigma_v
    vrow[base[0]] = -H
    # external mass sigma_v onto the group sites (this is what the suppliers feed):
    for q in range(k_groups):
        vrow[grp_ax[q]] = sigma_v / k_groups
    idx["v"] = len(rows); rows.append(vrow)

    # BLOCKERS for v: rho-far rows that REPLICATE v's pillar (S=pillar) pattern with
    # S-mass ~ 1 but wiggle by ~rho in the OTHER coordinates (so they are rho-far yet
    # carry the pattern, defeating the S-indicator exposer).  By F-BC their external mass
    # is small.  We place blocker b_j ~ pillar + a rho-wiggle in a low axis.
    # CORRECT blocker geometry: b sits at the SAME height as v (same pillar excursion, same
    # S=pillar pattern, S-mass ~ 1) but is rho-separated from v by a ZERO-SUM wiggle in the
    # low/group axes.  This makes v one of a rho-cluster of equal-height rows so no affine
    # functional in [0,1] vanishing at v lifts every rho-far row above kappa => v fails
    # exposedness, WITHOUT lowering the blockers below v (the prior bug).  Blockers are
    # arranged to SURROUND v: their wiggles point in different low-axis directions.
    blockers = []
    for j in range(nb):
        b = vrow.copy()                       # start from v's exact vector (same height)
        # zero-sum rho-wiggle in two low axes (or base axes if no low axes)
        if low_ax and nlow >= 2:
            wa = low_ax[j % nlow]
            wb = low_ax[(j + 1) % nlow]
            b[wa] += rho / 2.0
            b[wb] -= rho / 2.0
        elif low_ax:
            b[low_ax[0]] += rho / 2.0
            b[ax_pillar] -= rho / 2.0
        else:
            b[base[(j + 1) % ma]] += rho / 2.0
            b[base[(j + 2) % ma]] -= rho / 2.0
        blockers.append(len(rows)); rows.append(b)
    idx["blockers"] = blockers

    # v'' psi-max vertex: poked along its OWN pillar to level ~2 sigma_v, carrying the
    # FORCED large external mass sigma_vpp ~ rho/2.2 ~ 1.8 tau on the group sites.
    sigma_vpp = rho / 2.2
    h_vpp = min(2.0 * sigma_v, 0.9)         # design level of v'' (<= 2 sigma_v)
    vpp = vec()
    vpp[ax_vpp] = 1.0 + h_vpp - sigma_vpp
    vpp[base[0]] = -h_vpp
    for q in range(k_groups):
        vpp[grp_ax[q]] = sigma_vpp / k_groups
    idx["vpp"] = len(rows); rows.append(vpp)
    idx["sigma_vpp"] = sigma_vpp
    idx["h_vpp"] = h_vpp

    # SUPPLIER GROUPS: each a rho-split pair sitting at g-level ell_supplier.  The split is
    # what F-WR taxes: the two rows of a group differ by ~rho.  They live mostly on their
    # private group site (so they CAN feed v's external mass at that site) plus a level
    # component (ell_supplier worth of "below" mass) financed by low rows.
    suppliers = []
    group_members = []
    # ell_supplier is a g-LEVEL (deficit), not a coordinate mass; we realize the supplier's
    # "below" level by an excursion frac (capped so rows stay sane).  level_frac in [0,1).
    level_frac = float(np.clip(ell_supplier, 0.0, 0.9))
    for q in range(k_groups):
        gmem = []
        # the group's center site:
        site = grp_ax[q] if not coincident_groups else grp_ax[0]
        for s in range(2):                  # a rho-split pair
            sup = vec()
            split_sign = (1.0 if s == 0 else -1.0)
            # base: (1-level_frac) on the group site (the external feed v draws),
            #       level_frac on a low financing axis.  rowsum so far = 1.
            low0 = low_ax[(2 * q) % nlow] if low_ax else base[(q + 1) % ma]
            sup[site] = 1.0 - level_frac
            sup[low0] = level_frac
            # zero-sum rho-split wiggle: +/- group_sep/2 between two low axes (rowsum kept 1)
            if low_ax and nlow >= 2:
                wa = low_ax[(2 * q + s) % nlow]
                wb = low_ax[(2 * q + s + 1) % nlow]
                sup[wa] += split_sign * (group_sep / 2.0)
                sup[wb] -= split_sign * (group_sep / 2.0)
            suppliers.append(len(rows)); gmem.append(len(rows)); rows.append(sup)
        group_members.append(gmem)
    idx["suppliers"] = suppliers
    idx["group_members"] = group_members

    # LOW financing rows (sub-C, obligation-free): plain points low on the frame, used to
    # finance the supplier splits.  Placed at the group/low sites mixtures.
    lows = []
    for k in range(nlow):
        lw = vec()
        if low_ax:
            lw[low_ax[k % nlow]] = 1.0
        else:
            lw[base[k % ma]] = 1.0
        lows.append(len(rows)); rows.append(lw)
    idx["lows"] = lows

    idx["ax_pillar"] = ax_pillar
    idx["ax_vpp"] = ax_vpp
    idx["grp_ax"] = grp_ax
    idx["low_ax"] = low_ax

    # square up
    targets = np.array(rows)
    nrows = targets.shape[0]
    n = max(r, nrows)
    if targets.shape[1] < n:
        targets = np.hstack([targets, np.zeros((targets.shape[0], n - targets.shape[1]))])
    while targets.shape[0] < n:
        targets = np.vstack([targets, targets[anchors[0]].copy()])
    idx["n"] = targets.shape[0]
    return targets, idx


def height_functional_pillar(idx, n, axis_key="ax_pillar"):
    w = np.zeros(n); w[idx[axis_key]] = 1.0
    return w


# ======================================================================
# DECIDER: alternating (Lambda,R) LP minimizing max-row-neg subject to the
# architecture's pinned linear data; multistart; robust post-hoc verification.
# ======================================================================
def decide_mrp(sigma_v=0.1, tau=0.1, k_groups=2, ell_supplier=None, group_sep=None,
               ma=3, nlow=3, nb=2, H=None, seed=0, coincident_groups=False,
               pin_mode="anchors_heights", rounds=14, n_starts=3, verbose=False):
    """Build one MRP instance, optimize over (Lambda,R), verify robustly.

    pin_mode:
      "anchors_heights" : pin archetypes + anchors fully; pin height(v), height(v'')
                          via linear functionals; everything else free.  (the intended
                          blind-spot-exploiting mode -- gives the optimizer maximal freedom)
      "full"            : pin ALL design rows fully (control: recovers the design geometry).
    """
    targets, idx = build_mrp_targets(sigma_v=sigma_v, tau=tau, k_groups=k_groups,
                                     ell_supplier=ell_supplier, group_sep=group_sep,
                                     ma=ma, nlow=nlow, nb=nb, H=H, seed=seed,
                                     coincident_groups=coincident_groups)
    n = idx["n"]
    anchor_idx = idx["anchors"]
    arche = idx["archetypes"]

    # build pin spec
    full_pins = {}
    lin_pins = []
    # always pin archetypes + anchors fully (they are the frame + intended W)
    for i in arche:
        full_pins[i] = targets[i]
    for i in anchor_idx:
        full_pins[i] = targets[i]
    if pin_mode == "full":
        for i in range(n):
            full_pins[i] = targets[i]
    elif pin_mode == "anchors_heights":
        # pin v and v'' heights via the pillar functionals (separation from C)
        wv = height_functional_pillar(idx, n, "ax_pillar")
        wvpp = height_functional_pillar(idx, n, "ax_vpp")
        lin_pins.append((idx["v"], wv, float(targets[idx["v"]][idx["ax_pillar"]])))
        lin_pins.append((idx["vpp"], wvpp, float(targets[idx["vpp"]][idx["ax_vpp"]])))
        # ALSO pin the external-mass design at v (its group-site coords) so sigma_v is real:
        for q in range(k_groups):
            wgq = np.zeros(n); wgq[idx["grp_ax"][q]] = 1.0
            lin_pins.append((idx["v"], wgq, float(targets[idx["v"]][idx["grp_ax"][q]])))
    elif pin_mode == "pin_vfull":
        # pin v and v'' FULLY (genuine far geometry => entry guaranteed), pin supplier
        # group-site mass (the external feed), leave blockers/lows + (Lambda,R) FREE so the
        # optimizer minimizes max-row-neg over the realization freedom.  THE decider mode.
        full_pins[idx["v"]] = targets[idx["v"]]
        full_pins[idx["vpp"]] = targets[idx["vpp"]]
        for q, gmem in enumerate(idx["group_members"]):
            site = idx["grp_ax"][q] if not coincident_groups else idx["grp_ax"][0]
            for s in gmem:
                wgs = np.zeros(n); wgs[site] = 1.0
                lin_pins.append((s, wgs, float(targets[s][site])))
    else:
        raise ValueError(pin_mode)

    # seed: use the EXPLICIT frame archetype rows as R0 (guarantees R0 Lambda0 = I_r since
    # bary(e_a) = e_a).  seed_from_targets re-picks archetypes by affine rank, which can
    # differ from our frame and break R0 Lambda0 = I -- so seed directly here.
    Lam0, R0, sinfo = seed_frame(targets, arche)
    if sinfo["realize_err"] > 1e-6 or sinfo["RLambda_err"] > 1e-6:
        return {"ok_seed": False, "seed": sinfo, "idx_meta": _meta(idx)}

    best = None
    for st in range(n_starts):
        if st == 0:
            Ls, Rs = Lam0, R0
        else:
            rng = np.random.default_rng(1000 * seed + st)
            Ls = Lam0 + 0.01 * rng.standard_normal(Lam0.shape)
            # renormalize rowsums to 1
            Ls = Ls - (Ls.sum(1, keepdims=True) - 1.0) / Ls.shape[1]
            Rs = R0.copy()
        res = alternating_min(Ls, Rs, n, full_pins, lin_pins, [], rounds=rounds,
                              verbose=verbose)
        if res is None:
            continue
        Lam, R, P, mneg, duals = res
        if best is None or mneg < best[3]:
            best = (Lam, R, P, mneg, duals)
    if best is None:
        return {"ok_seed": True, "optimized": False, "seed": sinfo, "idx_meta": _meta(idx)}
    Lam, R, P, mneg, duals = best

    # robust verification
    ver = verify_mrp(P, idx)
    out = {"ok_seed": True, "optimized": True, "mneg_lp": float(mneg),
           "seed": {k: sinfo[k] for k in ["r", "RLambda_err", "realize_err"]},
           "idx_meta": _meta(idx), "duals": duals, "verify": ver}
    out["P"] = P.tolist()
    return out


def seed_frame(targets, arche):
    """Seed (Lam0, R0) with R0 = the explicit frame archetype rows (R0 Lambda0 = I_r
       guaranteed since bary(frame_a) = e_a).  Lambda0[i] = bary coords of targets[i]."""
    from d3_seed import bary
    targets = np.asarray(targets, float)
    n = targets.shape[0]
    r = len(arche)
    A = targets[arche]                       # r x n
    R0 = A.copy()
    Lam0 = np.zeros((n, r)); maxres = 0.0
    for i in range(n):
        lam, res = bary(targets[i], A); Lam0[i] = lam; maxres = max(maxres, res)
    RL = R0 @ Lam0
    info = {"r": r, "RLambda_err": float(np.abs(RL - np.eye(r)).max()),
            "realize_err": float(np.abs(Lam0 @ R0 - targets).max()),
            "bary_resid": float(maxres)}
    return Lam0, R0, info


def _meta(idx):
    return {k: idx[k] for k in ["r", "ma", "n", "tau", "delta", "rho", "kappa",
                                "sigma_v", "sigma_vpp", "h_vpp", "H_design",
                                "ell_supplier", "group_sep", "k_groups",
                                "coincident_groups", "v", "vpp", "anchors",
                                "blockers", "suppliers", "lows", "group_members"]}


def verify_mrp(P, idx, C=4.0, c=0.25, idem_tol=1e-7):
    """Robust, multiplicity-correct verification of one MRP instance.

    HONEST tau:  tau = sqrt(delta) from the INSTANCE's own delta = max-row-neg.  rho,kappa
    recomputed from that honest tau (NOT the design tau).  W recomputed robustly.  v's
    hidden-ness = dist_1(v, conv W) and its failure of (rho,kappa)-exposedness.
    """
    P = np.asarray(P, float)
    n = P.shape[0]
    chk = check_idempotent(P, tol=idem_tol)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "idem_resid": float(chk["idem_resid"]),
           "row_sum_resid": float(chk["row_sum_resid"]),
           "delta": float(delta), "max_neg": float(delta)}
    if not chk["ok"]:
        out["pass"] = False; out["reason"] = "not_idempotent"; return out
    if delta <= 1e-12:
        out["tau"] = 0.0; out["pass"] = False; out["reason"] = "delta_zero"; return out
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    out["tau"] = tau; out["rho"] = rho; out["kappa"] = kappa
    W, info = well_exposed_set_robust(P, rho, kappa)
    out["nW"] = len(W); out["W"] = list(map(int, W))

    v = idx["v"]; vpp = idx["vpp"]
    # v a vertex?
    vert_v, _ = is_row_vertex_robust(P, v)
    vert_vpp, _ = is_row_vertex_robust(P, vpp)
    out["v_vertex"] = bool(vert_v); out["vpp_vertex"] = bool(vert_vpp)
    # dist to conv W
    dv, _ = dist1_to_conv(P, W, v)
    dvpp, _ = dist1_to_conv(P, W, vpp)
    out["dist_v"] = float(dv); out["dist_vpp"] = float(dvpp)
    H = dv
    out["H_real"] = float(H)
    # v fails exposedness?
    okv, margv, _ = exposed_margin(P, v, rho, kappa)
    okvpp, margvpp, _ = exposed_margin(P, vpp, rho, kappa)
    out["v_margin"] = (None if margv is None else float(margv))
    out["vpp_margin"] = (None if margvpp is None else float(margvpp))
    out["v_fails_exposed"] = bool(not okv)
    out["vpp_fails_exposed"] = bool(not okvpp)
    out["all_anchors_in_W"] = bool(all(a in W for a in idx["anchors"]))

    # the actual external (off-own-site) coefficient mass at v, measured on P (column = coeff)
    # v's own site = the pillar axis; its self-coefficient row:
    rowv = P[v]
    # "external" = negative-mass + off-dominant-support; report neg(v) and total |off-pillar|
    out["neg_v"] = float(np.maximum(-rowv, 0.0).sum())
    out["neg_vpp"] = float(np.maximum(-P[vpp], 0.0).sum())

    # headline ratios
    if H > 1e-9:
        out["delta_over_H2"] = float(delta / (H * H))
        out["H_over_tau"] = float(H / tau)
    else:
        out["delta_over_H2"] = None
        out["H_over_tau"] = 0.0

    # ENTRY GATE for a verified MRP instance: v genuinely hidden (dist>=H>0) AND
    # genuinely failing exposedness AND a vertex AND idempotent.
    out["entry_pass"] = bool(chk["ok"] and vert_v and (not okv) and H > 1e-9)
    out["pass"] = out["entry_pass"]
    return out


if __name__ == "__main__":
    print("d8_mrp self-test: one mid-regime instance (sigma_v=0.1*tau? use sigma_v=tau*0.1)", flush=True)
    tau = 0.1
    r = decide_mrp(sigma_v=0.1 * tau, tau=tau, k_groups=2, seed=0, n_starts=2, verbose=True)
    print(json.dumps({k: r[k] for k in r if k != "P"}, indent=2, default=str)[:2000], flush=True)
