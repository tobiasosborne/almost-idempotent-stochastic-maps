#!/usr/bin/env python3 -u
"""
d7_template.py -- explicit ell^1 target geometry for the FTI-2 skinny-pair template,
plus partial-pin specification for the d7 decider.

GEOMETRY (in R^n, ell^1).  Coordinates are split into:
  * a "base" block carrying the anchor simplex C = conv A (the intended W);
  * a "height" direction along which v1, v2 are pushed out by ~H;
  * "helper" rows L1, L2 in C (shadow targets) and 0..nh free auxiliary helper rows
    (where a refutation would hide).

We place:
  anchors a_0..a_{ma-1} : the simplex C, at height 0.   a_t = e_{base_t} (unit base coords).
  L1, L2  in C          : convex combinations of anchors (interior of C), height 0.
  v1, v2                : DISTINCT, at height >= H, mutually shadowing:
        v1 ~ mu1 v2 + (1-mu1) L1 ,  v2 ~ mu2 v1 + (1-mu2) L2  (skinny: mu_j -> 1).
        Solving the linear system for the v's positions (ignoring errors e):
          v1 = mu1 v2 + (1-mu1) L1
          v2 = mu2 v1 + (1-mu2) L2
        => v1 = [ (1-mu1)L1 + mu1(1-mu2)L2 ] / (1 - mu1 mu2)   (+ height component).
  We add an explicit HEIGHT component along a fresh axis so v1,v2 sit at height H, and a
  SMALL transverse split so v1 != v2 (skinny diamond width w).

This base target is FULLY REALIZABLE (a stochastic config -> delta could be 0 if we did
not also demand failed exposedness; the optimizer adds the negativity needed to push the
v's beyond conv W).  The decider does NOT pin v1,v2 fully -- it pins only:
  - all anchors + L1,L2 FULLY (they are the intended W / shadow carriers);
  - v1,v2 (and free helpers) via the HEIGHT functional and the SHADOW equations only,
    leaving their detailed realization + (Lambda,R) free.
"""
import numpy as np


def build_targets(ma=3, nh=0, H=0.2, mu1=0.99, mu2=0.99, w=0.05, seed=0):
    """Return (targets [n x n], idx) for the skinny-pair template.
       idx: dict with anchors, L1, L2, v1, v2, helpers, height_axis.
    """
    rng = np.random.default_rng(seed)
    # layout of coordinate axes:
    #  base block: ma axes (anchor simplex)  -> indices 0..ma-1
    #  height axis: 1 axis                    -> index ma
    #  split axis : 1 axis                    -> index ma+1
    #  helper axes: nh axes                   -> ma+2 .. ma+2+nh-1
    # The COORDINATE FRAME has r = ma + 2 + (nh helper axes) directions e_0..e_{r-1}.
    # We PREPEND r identity "archetype" rows e_a so the canonical seed R0=[I_r|0],
    # Lambda0 top-block=I_r is valid AND every template row (anchors, L1, L2, v's,
    # helpers) is a NON-archetype row (index >= r) realized as an affine combo of the
    # frame.  This keeps R Lambda = I feasible jointly with the pins.
    r = ma + 2 + nh
    n_axes = r
    # rows: r archetype identity rows, then ma anchors, L1, L2, v1, v2, nh helpers
    nrows = r + ma + 2 + 2 + nh
    n = max(n_axes, nrows)
    base = list(range(ma))
    ax_h = ma
    ax_s = ma + 1
    hel_ax = list(range(ma + 2, ma + 2 + nh))

    def vec():
        return np.zeros(n)

    rows = []
    idx = {}
    # r archetype identity rows e_0..e_{r-1} (the coordinate frame; genuine exposed
    # vertices of the simplex).  These are the canonical archetypes.
    arche = []
    for a in range(r):
        v = vec(); v[a] = 1.0
        arche.append(len(rows)); rows.append(v)
    idx["archetypes"] = arche
    idx["r"] = r
    # anchors: the simplex C = conv A. Use the first ma archetype directions but as
    # SEPARATE rows (so C is a sub-simplex of the frame; anchors are e_0..e_{ma-1}).
    anchors = []
    for t in range(ma):
        v = vec(); v[base[t]] = 1.0
        anchors.append(len(rows)); rows.append(v)
    idx["anchors"] = anchors
    # L1, L2 in C : interior convex combos of anchors (height 0, on base block)
    cL1 = rng.dirichlet(np.ones(ma))
    cL2 = rng.dirichlet(np.ones(ma))
    L1 = vec();
    for t in range(ma): L1[base[t]] = cL1[t]
    L2 = vec()
    for t in range(ma): L2[base[t]] = cL2[t]
    idx["L1"] = len(rows); rows.append(L1)
    idx["L2"] = len(rows); rows.append(L2)
    # solve the (errorless) mutual-shadow system for the base/height parts of v1,v2.
    #   v1 = mu1 v2 + (1-mu1) L1
    #   v2 = mu2 v1 + (1-mu2) L2
    # componentwise linear; solve 2x2 per coordinate.
    M = np.array([[1.0, -mu1], [-mu2, 1.0]])
    Minv = np.linalg.inv(M)
    v1 = vec(); v2 = vec()
    for j in range(n):
        rhs = np.array([(1 - mu1) * L1[j], (1 - mu2) * L2[j]])
        sol = Minv @ rhs
        v1[j] = sol[0]; v2[j] = sol[1]
    # POKE the v's genuinely OUT of the anchor simplex along a pillar anchor, by an amount
    # >= H, compensating with NEGATIVE coordinate mass on a DISTINCT anchor (this is the
    # only mechanism that creates real distance from conv C and costs negativity).  v1
    # pokes pillar via anchor0, v2 via anchor1 -> distinct; a thin transverse split (w) on
    # ax_s makes them mutually-shadowing rather than coincident.
    pillar = base[ma - 1]    # poke beyond this anchor
    a1, a2 = base[0], base[1 % ma]
    g = H                    # excursion magnitude ~ H (sets dist beyond the simplex)
    v1[:] = 0.0; v2[:] = 0.0
    v1[pillar] = 1.0 + g; v1[a1] = -g
    v2[pillar] = 1.0 + g; v2[a2] = -g
    v1[ax_s] += w / 2.0; v1[pillar] -= w / 2.0
    v2[ax_s] -= w / 2.0; v2[pillar] += w / 2.0
    # height functional now reads the pillar-excursion (g) -- redefine height axis = pillar
    ax_h = pillar
    idx["v1"] = len(rows); rows.append(v1)
    idx["v2"] = len(rows); rows.append(v2)
    # free helper rows: start as copies of midpoint(v1,v2) on a helper axis (the optimizer
    # is free to move them; they are the "where a refutation hides" rows).
    helpers = []
    for hh in range(nh):
        v = (v1 + v2) / 2.0 + 0.0
        if hel_ax:
            v[hel_ax[hh]] += 0.0
        helpers.append(len(rows)); rows.append(v)
    idx["helpers"] = helpers
    idx["height_axis"] = ax_h
    idx["split_axis"] = ax_s
    targets = np.array(rows)
    # pad rows so it's square n x n (extra rows = duplicate anchors? no -- we set n=max,
    # if nrows<n we need filler rows that are anchors to keep it square & exact).  Add
    # copies of anchor 0 as filler (they coincide -> harmless, treated as one vertex by
    # the robust W).
    while targets.shape[0] < n:
        targets = np.vstack([targets, anchors_row(anchors, rows)])
    return targets, idx


def anchors_row(anchors, rows):
    return rows[anchors[0]].copy()


def height_functional(idx, n):
    """linear functional w with <w, row> = height of row (its ax_h coordinate)."""
    w = np.zeros(n); w[idx["height_axis"]] = 1.0
    return w
