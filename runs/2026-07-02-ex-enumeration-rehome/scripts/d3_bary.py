#!/usr/bin/env python3 -u
"""
d3_bary.py -- the PROVABLY-VALID canonical family + barycentric hidden-geometry
templates.

CANONICAL EXACT IDEMPOTENT FAMILY.  Fix archetypes R0 = [I_r | 0] (r x n).  Then for
ANY Lambda (n x r) with  Lambda[0:r, :] = I_r  and every row summing to 1, P = Lambda R0
is an EXACT signed affine retraction (P1=1, P^2=P), with:
  * rows 0..r-1 = e_0..e_{r-1}  (the archetype simplex vertices; the natural W),
  * row i>=r : p_i = (Lambda[i,:], 0,...,0), a SIGNED affine comb of the archetypes
    with barycentric coords lam_i := Lambda[i,:],  neg(p_i) = sum_a max(-lam_i[a], 0).
The whole picture lives in the (r-1)-simplex with vertices e_0..e_{r-1}; ell^1 distance
between rows is the ell^1 distance of their barycentric coords (since rows differ only
on the first r coords).  A row is FAR from conv W exactly when its bary coords lie far
OUTSIDE conv{ e_a : a in W }.  Negativity = ell^1 mass outside the simplex.

THE HIDDEN-GEOMETRY TEMPLATES specify the bary coords lam_i of the hidden rows.  The
"thin diamond / circuit" is a set of k bary points at ell^1-distance ~ H beyond the
anchor face of the simplex, arranged so each is a near-affine-combination of the others
(mutual shadowing) -> none is (rho,kappa)-well-exposed -> they drop from W -> the
cluster is genuinely far from conv W.  We then VERIFY honestly.

A "far beyond a face" bary point: take the anchor vertices a in A (|A|=mb), and push
along the direction (vertex_far - centroid_of_A) by amount controlling H.  Concretely a
bary point lam with sum=1, with NEGATIVE entries on the anchors and POSITIVE > 1 on the
'pillar' archetype(s) pokes outside the simplex; its neg mass = the magnitude pushed.

This file produces bary-coordinate templates; the embedding/idempotent build + adversarial
R search live in d3_drive2.py.
"""
import numpy as np


def diamond_bary(H, k=4, mb=2, npil=2, w=0.05, seed=0):
    """r = mb + npil archetypes:  mb 'anchors' (low, intended W) + npil 'pillars'.
       k hidden bary points poking 'beyond' the pillars by height ~H, spread w on a
       thin polygon so they mutually shadow.

       A hidden bary point: base = pillar centroid pushed outward.  Push direction
       d = (pillar_centroid - anchor_centroid) normalized in bary space.  lam =
       pillar_centroid + H_eff * d, then perturbed by w around a k-gon in the
       pillar-tangent directions.  We rescale so the REALIZED ell^1 distance of the
       hidden row to the anchor face is ~ H.

       Returns:
         bary_hidden : (k, r) bary coords of hidden rows (rows sum to 1),
         anchor_arch : list of anchor archetype indices (0..mb-1),
         pillar_arch : list of pillar archetype indices (mb..mb+npil-1),
         meta.
       The anchor archetypes are the intended W; pillars exist only to give the hidden
       rows somewhere 'far' to be.  (Pillars are themselves rows e_{mb}..e_{r-1}; we
       will check whether THEY end up in W -- if a pillar is well-exposed it joins W and
       can shrink the hidden distance, which is exactly the adversarial pressure.)
    """
    r = mb + npil
    rng = np.random.default_rng(seed)
    anchor_arch = list(range(mb))
    pillar_arch = list(range(mb, r))
    # anchor centroid and pillar centroid in bary space (R^r)
    ca = np.zeros(r); ca[anchor_arch] = 1.0 / mb
    cp = np.zeros(r); cp[pillar_arch] = 1.0 / npil
    d = cp - ca                     # direction from anchors to pillars (sums to 0)
    nd = np.abs(d).sum()
    d = d / nd if nd > 0 else d     # unit ell^1 push direction (still sums to 0)
    bary = []
    for j in range(k):
        # base hidden point: push from anchor centroid by amount 'amp' along d so the
        # ell^1 distance into the simplex-and-beyond is ~ H. ell^1 dist of (ca+amp*d)
        # to ca is amp (since |d|_1=1). To get BEYOND the simplex (negative anchor
        # coords) we push amp>1 worth; choose amp = H so realized far-distance ~ H.
        amp = H
        lam = ca + amp * d
        # thin-polygon perturbation in pillar-tangent (between pillars) directions
        if npil >= 2 and k > 1:
            th = 2 * np.pi * j / k
            # tangent: difference of two pillars (sums to 0), scaled by w
            tdir = np.zeros(r)
            tdir[pillar_arch[0]] = 1.0; tdir[pillar_arch[1]] = -1.0
            tdir = tdir / np.abs(tdir).sum()
            lam = lam + w * np.cos(th) * tdir
            if npil >= 3:
                t2 = np.zeros(r); t2[pillar_arch[0]] = 1.0; t2[pillar_arch[2]] = -1.0
                t2 = t2 / np.abs(t2).sum()
                lam = lam + w * np.sin(th) * t2
        bary.append(lam)
    bary = np.array(bary)
    # ensure rows sum to 1 (they do: ca sums 1, d sums 0, tangents sum 0)
    meta = {"family": "diamond_bary", "H": H, "k": k, "mb": mb, "npil": npil,
            "w": w, "r": r}
    return bary, anchor_arch, pillar_arch, meta


def segment_bary(H, k=2, mb=2, npil=1, w=0.0, seed=0):
    """Thinnest circuit: k hidden bary points pushed 'beyond' a single pillar by H,
       collinear (segment of half-length w). With npil=1 the push is toward e_pillar.
    """
    r = mb + npil
    anchor_arch = list(range(mb)); pillar_arch = list(range(mb, r))
    ca = np.zeros(r); ca[anchor_arch] = 1.0 / mb
    cp = np.zeros(r); cp[pillar_arch] = 1.0 / npil
    d = cp - ca; d = d / np.abs(d).sum()
    bary = []
    for j in range(k):
        frac = (j / (k - 1) - 0.5) if k > 1 else 0.0
        lam = ca + H * d
        if npil == 1:
            # spread along an anchor-difference tangent
            if mb >= 2:
                t = np.zeros(r); t[anchor_arch[0]] = 1.0; t[anchor_arch[1]] = -1.0
                t = t / np.abs(t).sum()
                lam = lam + 2 * w * frac * t
        bary.append(lam)
    return np.array(bary), anchor_arch, pillar_arch, \
        {"family": "segment_bary", "H": H, "k": k, "mb": mb, "npil": npil, "w": w, "r": r}


def isolated_bary(H, mb=2, npil=1, seed=0):
    """CONTROL: a SINGLE hidden bary point pushed beyond a pillar by H. Provably
       well-exposed -> should JOIN W -> verified_hidden False (dist collapses)."""
    r = mb + npil
    anchor_arch = list(range(mb)); pillar_arch = list(range(mb, r))
    ca = np.zeros(r); ca[anchor_arch] = 1.0 / mb
    cp = np.zeros(r); cp[pillar_arch] = 1.0 / npil
    d = cp - ca; d = d / np.abs(d).sum()
    lam = ca + H * d
    return lam[None, :], anchor_arch, pillar_arch, \
        {"family": "isolated_bary", "H": H, "mb": mb, "npil": npil, "r": r}


def inside_bary(H, k=4, mb=3, seed=0):
    """CONTROL: k hidden bary points INSIDE the anchor simplex (a small circuit around
       the centroid). They cost NO negativity and are NOT far -> reproduces the known
       zero-neg transient circuits.  We mark the circuit centroid as the test row."""
    r = mb
    anchor_arch = list(range(mb)); pillar_arch = []
    ca = np.ones(r) / r
    bary = []
    rng = np.random.default_rng(seed)
    for j in range(k):
        th = 2 * np.pi * j / k
        # small perturbation INSIDE the simplex (stay positive): radius 0.1
        pert = np.zeros(r)
        pert[0] = 0.1 * np.cos(th); pert[1 % r] = 0.1 * np.sin(th)
        pert -= pert.mean()
        bary.append(ca + pert)
    bary.append(ca.copy())   # centroid (interior)
    return np.array(bary), anchor_arch, pillar_arch, \
        {"family": "inside_bary", "H": H, "k": k, "mb": mb, "npil": 0, "r": r}
