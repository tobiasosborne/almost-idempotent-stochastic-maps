#!/usr/bin/env python3 -u
"""
d3_envlp.py -- DIRECT envelope LP on the canonical family R=[I_r|0].

In this family every row i>=r is its barycentric coordinate vector lam_i in R^r (rows
0..r-1 are the simplex vertices e_0..e_{r-1}).  neg(row i)=sum_a max(-lam_i[a],0).
ell^1 distance between rows = ell^1 distance of bary coords (rows differ only on first r
coords).  So the WHOLE problem is bary geometry in R^r with ell^1.

DIRECT ENVELOPE.  Fix the W-candidate set to the anchor vertices A (a subset of
0..r-1) by template.  Minimize  m = max-row-neg  over the FREE bary coords {lam_i}_{i>=r}
subject to:
   (rowsum)  sum_a lam_i[a] = 1
   (FAR)     dist_1( lam_t , conv{e_a : a in A} ) >= H     for the designated hidden row t
   (neg/epi) m >= sum_a max(-lam_i[a],0)  for all i.
This is an LP (the FAR constraint: dist_1(x, conv A) >= H.  dist_1 to conv of simplex
vertices A = sum_{a not in A} max(x_a,0)+... actually for x a bary vector, the ell^1
distance to conv{e_a:a in A} equals the ell^1 mass of x OUTSIDE the face A =
sum_{b not in A} |x_b| + (correction).  We compute it EXACTLY as an inner LP variable,
but to keep ONE LP we use the lower bound: dist_1(x,conv A) >= sum_{b notin A} |x_b|
is NOT linear as >= (abs).  Instead we use the SUPPORTING-HYPERPLANE form: there is a
1-Lipschitz (ell^infty<=1) affine functional g with g=0 on conv A and g(lam_t) = dist.
We pick the natural separator g(x) = sum_{b notin A} x_b (=0 on A-face, coeffs in {0,1}
so ell^infty<=1, hence g(x) <= dist_1(x,conv A)).  Requiring g(lam_t) >= H FORCES
dist >= H.  (Conservative: real dist may be larger; we VERIFY actual dist post-hoc.)

Then we ALSO run the ADVERSARIAL general-R alternation (d3_envelope) from the LP optimum
to check no general-R re-coordinatization undercuts the cost.

Crucially this LP lets the optimizer make the hidden row a NON-VERTEX (interior to other
far rows) for free, and choose the cheapest way (min neg) to be far -- exactly the
adversarial envelope.  We then VERIFY honestly (recompute W; the hidden row must really
be >=H from conv W, where W is recomputed, NOT assumed = anchors).
"""
import sys, os, json, time
import numpy as np
import gurobipy as gp
from gurobipy import GRB

from d1_infra import (check_idempotent, neg_mass, well_exposed_set, dist1_to_conv)
from d3_envelope import _newmodel, alternating_min, lp_optimize_R, lp_optimize_Lambda, verify


def envelope_lp(r, A, H, n_hidden=1, extra_far=0, far_template="single", w=0.0,
                collect_duals=True):
    """Minimize max-row-neg over bary coords of hidden rows in the R=[I_r|0] family.
       r        : #archetypes (simplex dim r-1).
       A        : anchor indices (subset of 0..r-1) = W-candidates; conv A is the face.
       H        : required ell^1 far-distance of the designated hidden row to conv A.
       n_hidden : #hidden rows (>=1). row 0 of the hidden block is the FAR target;
                  the rest are 'shadow' rows we also require far (to force non-vertex).
       far_template:
         'single'  : only the target row is forced far.
         'circuit' : ALL hidden rows forced far by H, arranged so target is interior
                     (target = centroid of the others, forced) -> non-vertex.
       Returns Lam (n x r), R0, P, max_neg, duals, hidden_idx.
    """
    nonA = [b for b in range(r) if b not in A]
    n = r + n_hidden
    m = _newmodel("envlp")
    # bary coords of hidden rows: lam[h, a], h=0..n_hidden-1
    lam = m.addVars(n_hidden, r, lb=-GRB.INFINITY, name="lam")
    neg = m.addVars(n_hidden, r, lb=0.0, name="neg")     # neg mass of hidden rows
    mneg = m.addVar(lb=0.0, name="mneg")
    cons = {}
    for h in range(n_hidden):
        cons[("rowsum", h)] = m.addConstr(gp.quicksum(lam[h, a] for a in range(r)) == 1.0)
        for a in range(r):
            cons[("neg", h, a)] = m.addConstr(neg[h, a] >= -lam[h, a])
        cons[("epi", h)] = m.addConstr(gp.quicksum(neg[h, a] for a in range(r)) <= mneg)
    # FAR constraint via separator g(x)=sum_{b notin A} x_b >= H (forces dist>=H).
    targets = [0] if far_template == "single" else list(range(n_hidden))
    for h in targets:
        cons[("far", h)] = m.addConstr(gp.quicksum(lam[h, b] for b in nonA) >= H)
    if far_template == "circuit" and n_hidden >= 3:
        # force the LAST hidden row to be the centroid of the others -> interior, non-vertex
        for a in range(r):
            cons[("cen", a)] = m.addConstr(
                (n_hidden - 1) * lam[n_hidden - 1, a]
                == gp.quicksum(lam[h, a] for h in range(n_hidden - 1)))
    m.setObjective(mneg, GRB.MINIMIZE)
    m.optimize()
    if m.Status != GRB.OPTIMAL:
        return None
    Lamh = np.array([[lam[h, a].X for a in range(r)] for h in range(n_hidden)])
    Lam = np.zeros((n, r)); Lam[:r] = np.eye(r); Lam[r:] = Lamh
    R0 = np.zeros((r, n)); R0[:, :r] = np.eye(r)
    P = Lam @ R0
    duals = None
    if collect_duals:
        duals = {}
        for key, con in cons.items():
            try:
                pi = con.Pi
            except Exception:
                continue
            if abs(pi) > 1e-7:
                duals[str(key)] = float(pi)
    return {"Lam": Lam, "R0": R0, "P": P, "max_neg": float(mneg.X),
            "duals": duals, "hidden_idx": list(range(r, n)), "A": A, "r": r, "H": H}


def mine_lp(r, A, H, n_hidden=1, far_template="single", C=4.0, c=0.25,
            do_adversarial=True, adversarial_rounds=10):
    out = envelope_lp(r, A, H, n_hidden=n_hidden, far_template=far_template)
    if out is None:
        return {"status": "lp_infeasible", "H": H, "r": r, "A": A,
                "far_template": far_template, "n_hidden": n_hidden}
    P = out["P"]; hidden_idx = out["hidden_idx"]
    v = verify(P, hidden_idx, C=C, c=c, H_target=H)
    rec = {"H": H, "r": r, "A": A, "n_hidden": n_hidden, "far_template": far_template,
           "lp_max_neg": out["max_neg"], "lp_duals": out["duals"],
           "canonical": v}
    if do_adversarial and v.get("idem_ok"):
        pins = {i: P[i].copy() for i in hidden_idx}
        best = alternating_min(out["Lam"], out["R0"], pins, rounds=adversarial_rounds)
        if best is not None:
            Lamb, Rb, Pb, mnb = best
            vb = verify(Pb, hidden_idx, C=C, c=c, H_target=H)
            _, _, iR = lp_optimize_R(Lamb, pins, R_warm=Rb, collect_duals=True)
            vb["duals_R"] = iR.get("duals")
            rec["adversarial"] = vb
    # envelope value: min verified-hidden max-neg
    cands = []
    if v.get("verified_hidden"):
        cands.append(("canonical", v["max_neg"], v["max_hidden_dist"]))
    av = rec.get("adversarial", {})
    if av.get("verified_hidden"):
        cands.append(("adversarial", av["max_neg"], av["max_hidden_dist"]))
    if cands:
        cands.sort(key=lambda x: x[1])
        rec["env_source"], rec["env_maxneg"], rec["env_dist"] = cands[0]
        rec["verified"] = True
    else:
        rec["verified"] = False
        rec["env_maxneg"] = v["max_neg"]; rec["env_dist"] = v.get("max_hidden_dist", 0.0)
    return rec


if __name__ == "__main__":
    print("d3_envlp smoke: r=4, anchors A={0,1}, sweep H, single far row", flush=True)
    for H in [0.1, 0.3, 0.6, 1.0, 1.5, 2.0]:
        rec = mine_lp(r=4, A=[0, 1], H=H, n_hidden=1, far_template="single")
        c = rec.get("canonical", {})
        print(f"H={H}: lp_maxneg={rec.get('lp_max_neg'):.4f} "
              f"delta={c.get('delta')} tau={c.get('tau')} |W|={c.get('nW')} "
              f"hid_dist={c.get('max_hidden_dist')} hid_in_W={c.get('hidden_in_W')} "
              f"verified={rec.get('verified')} env={rec.get('env_maxneg'):.4f}", flush=True)
