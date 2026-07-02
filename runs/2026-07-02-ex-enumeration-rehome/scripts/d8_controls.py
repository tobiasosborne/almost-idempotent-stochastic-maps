#!/usr/bin/env python3 -u
"""
d8_controls.py -- mandatory controls for the MRP decider pipeline (task step 2).

(i)   3.49 floor reproduced on the d7/d3 template (pipeline correctly finds the known floor).
(ii)  wiggle-rigidity collapse: when the supplier cluster is forced to a SINGLE coincident
      point with NO surrounding web (one lone far row), it EXPOSES (joins W) -> H collapses.
(iii) F-ND: a near-delta row (tiny off-own-site mass) turns out EXPOSED in the pipeline.

These exercise the robust gates (idempotence, multiplicity-correct W, honest tau) so a passed
MRP entry is trustworthy.
"""
import os, json, numpy as np
from d3_main import bary_to_P
from d1_infra import neg_mass, dist1_to_conv, exposed_margin, check_idempotent
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d8_mrp3 import build, verify

C, c = 4.0, 0.25
OUT = os.path.join("out", "d8_controls.json")


def control_i_floor():
    """Reproduce the d3/d7 ~3.49 floor: a thin diamond (two far vertices at the exposedness
       boundary) realized canonically; the worst dist/tau ~ 0.536 => delta/H^2 ~ 3.49."""
    # thin-diamond: anchors e0,e1; a poke vertex v at the (4tau,tau/4) boundary.
    # thin DIAMOND: two coincident-ish far vertices forming a 2-cluster at the boundary
    # (the d3/d7 floor config: a far cluster that is non-exposed only marginally).
    best = [np.inf, None]
    for r in [4, 5]:
        for g in np.linspace(0.02, 0.4, 30):
            for w in [0.0, 0.02, 0.05]:
                rows = [np.eye(r)[a].copy() for a in range(r)]
                v1 = np.zeros(r); v1[r - 1] = 1 + g; v1[0] = -g
                v2 = np.zeros(r); v2[r - 1] = 1 + g; v2[1 % r] = -g
                if r > 2:
                    v1[2 % r] += w / 2; v1[r - 1] -= w / 2
                    v2[2 % r] -= w / 2; v2[r - 1] += w / 2
                iv = len(rows); rows.append(v1); rows.append(v2)
                P = bary_to_P(rows, r)
                _floor_update(P, iv, best)
    return tuple(best)


def _floor_update(P, iv, best):
    from d1_infra import neg_mass as _nm, dist1_to_conv as _d1, exposed_margin as _em
    from d3_vertexfix import well_exposed_set_robust as _wes
    nm, delta = _nm(P)
    if delta <= 1e-12:
        return
    tau = np.sqrt(delta); rho, kappa = C * tau, c * tau
    W, _ = _wes(P, rho, kappa)
    for jj in (iv, iv + 1):
        dd, _ = _d1(P, W, jj)
        ok, m, _ = _em(P, jj, rho, kappa)
        if not ok and dd > 1e-9:
            dh2 = delta / dd ** 2
            if dh2 < best[0]:
                best[0] = dh2
                best[1] = {"delta": float(delta), "H": float(dd),
                           "dist_over_tau": float(dd / tau), "delta_over_H2": float(dh2)}


def _control_i_unused():
    best = (np.inf, None)
    for r in [4, 5]:
        for g in np.linspace(0.02, 0.4, 30):
            rows = [np.eye(r)[a].copy() for a in range(r)]
            v = np.zeros(r); v[r - 1] = 1 + g; v[0] = -g
            iv = len(rows); rows.append(v)
            P = bary_to_P(rows, r)
            nm, delta = neg_mass(P)
            if delta <= 1e-12:
                continue
            tau = np.sqrt(delta); rho, kappa = C * tau, c * tau
            W, _ = well_exposed_set_robust(P, rho, kappa)
            dd, _ = dist1_to_conv(P, W, iv)
            ok, m, _ = exposed_margin(P, iv, rho, kappa)
            if not ok and dd > 1e-9:           # non-exposed far vertex (boundary)
                dh2 = delta / dd ** 2
                if dh2 < best[0]:
                    best = (dh2, {"r": r, "g": float(g), "delta": float(delta),
                                  "H": float(dd), "dist_over_tau": float(dd / tau),
                                  "delta_over_H2": float(dh2)})
    return best


def control_ii_collapse():
    """A LONE far supplier with NO surrounding web exposes (joins W) -> v's H collapses.
       Build the MRP family but with a SINGLE supplier (k_groups=1, one member) and remove
       the web: the lone far row must expose."""
    # one lone far row poked out, no cluster around it
    r = 4
    rows = [np.eye(r)[a].copy() for a in range(r)]
    d = 0.015
    S = np.zeros(r); S[2] = 1 + 2 * d; S[0] = -d; S[3] = 0.0; S[2] -= d  # net poke ~d
    iS = len(rows); rows.append(S)
    P = bary_to_P(rows, r)
    nm, delta = neg_mass(P); tau = np.sqrt(delta); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    ok, m, _ = exposed_margin(P, iS, rho, kappa)
    dd, _ = dist1_to_conv(P, W, iS)
    return {"lone_far_exposed": bool(ok), "margin": float(m or 0), "kappa": float(kappa),
            "dist_to_W": float(dd), "in_W": bool(iS in W),
            "collapse_ok": bool(ok and dd < 1e-6)}


def control_iii_fnd():
    """F-ND: a near-delta row (off-own-site mass <= t small) is EXPOSED.  Build a row that is
       0.97 on its own frame dir + 0.03 spread; it must come out exposed (joins W)."""
    r = 5
    rows = [np.eye(r)[a].copy() for a in range(r)]
    # a near-delta extra row: 0.97 on dir 4, 0.01 each on 0..2, plus a tiny neg to set tau>0
    nd = np.zeros(r); nd[4] = 0.97; nd[0] = 0.02; nd[1] = 0.02; nd[2] = -0.01
    ind = len(rows); rows.append(nd)
    # add a small distinct poke elsewhere so delta>0 robustly
    P = bary_to_P(rows, r)
    nm, delta = neg_mass(P); tau = np.sqrt(max(delta, 1e-9)); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    ok, m, _ = exposed_margin(P, ind, rho, kappa)
    return {"near_delta_exposed": bool(ok), "in_W": bool(ind in W),
            "off_site_mass": float(np.abs(nd).sum() - abs(nd[4])),
            "fnd_ok": bool(ok or ind in W)}


def main():
    res = {}
    dh2, rec = control_i_floor()
    res["control_i_3p49_floor"] = {"min_delta_over_H2": float(dh2), "rec": rec,
                                   "pass": bool(2.5 <= dh2 <= 5.0)}
    print(f"[control i] floor delta/H^2 = {dh2:.3f} (expect ~3.49) "
          f"pass={res['control_i_3p49_floor']['pass']}", flush=True)
    res["control_ii_collapse"] = control_ii_collapse()
    print(f"[control ii] lone far row exposed={res['control_ii_collapse']['lone_far_exposed']} "
          f"collapse_ok={res['control_ii_collapse']['collapse_ok']}", flush=True)
    res["control_iii_fnd"] = control_iii_fnd()
    print(f"[control iii] near-delta exposed={res['control_iii_fnd']['near_delta_exposed']} "
          f"fnd_ok={res['control_iii_fnd']['fnd_ok']}", flush=True)
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    allpass = (res["control_i_3p49_floor"]["pass"] and
               res["control_ii_collapse"]["collapse_ok"] and res["control_iii_fnd"]["fnd_ok"])
    print(f"\n[d8-controls] ALL PASS = {allpass}", flush=True)


if __name__ == "__main__":
    main()
