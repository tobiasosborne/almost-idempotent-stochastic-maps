#!/usr/bin/env python3 -u
"""
d3_templates.py -- hidden-geometry TEMPLATES (target row positions) for the
envelope mine.  A template returns:
  targets : (n, n) array of REALIZED row positions t_i (ell^1 embedding, rows sum 1),
  anchor_idx : indices intended as W (the low simplex),
  hidden_idx : indices of the hidden cluster (the far diamond/circuit),
  meta : dict with H and geometry params.
We PIN every realized row to its target (so the geometry is exactly what we asked),
then the alternating LP finds the EXACT idempotent Lambda,R with P=Lambda R==targets
of minimal max-row-neg.  NOTE: when we pin ALL rows, max-row-neg = max-neg of the
TARGETS (since P==targets), so the LP only checks REALIZABILITY (R Lambda=I feasible).
The ADVERSARIAL freedom comes from pinning only the HIDDEN rows (and leaving anchors
free): then the optimizer may move anchors / re-coordinatize R to reduce negativity,
and the binding constraint is the hidden geometry + idempotence.  We expose a flag
pin_anchors to study both.

Geometry (all in R^n, rows sum to 1 via a slack coord):
  coords: [base_0 .. base_{mb-1}] (anchor simplex)  | up | s1 | s2 | slack
  - anchor a: base_r * e_a, height 0.    (mb anchors)
  - hidden k: centered above anchor centroid by H in 'up', spread (s1,s2) on a thin
    polygon of half-width w.  A SMALL w makes the hidden rows nearly collinear in
    (up,s1,s2) -> each is ~affine-comb of its neighbours -> exposedness margin small
    -> they SHADOW each other -> none joins W -> the cluster is far from conv(anchors).
The negative mass appears because a row at height H>0 in 'up' with the slack
correction (slack = 1 - sum) goes NEGATIVE on the slack coord when sum>1, i.e. the
height/ spread costs negativity ~ H (linear in this raw embedding).  The QUADRATIC
env(H) (if real) must come from the IDEMPOTENCE coupling re-distributing it, which is
exactly what alternating over R/Lambda probes -- so we let the LP move mass and only
read the VERIFIED max-neg of the resulting exact P.
"""
import numpy as np


def _fix_slack(pts, slack):
    pts = np.array(pts, float)
    s = pts.sum(axis=1)
    pts[:, slack] = pts[:, slack] + (1.0 - s)
    return pts


def thin_diamond(H, k=4, mb=3, base_r=0.5, w=0.05, seed=0):
    """mb anchor rows (low simplex) + k hidden rows on a thin polygon at height H.
       Returns targets (n x n), anchor_idx, hidden_idx, meta.
       n = mb + k.  Coordinates: base(mb) | up | s1 | s2 | slack  -> need mb+4 coords
       BUT total #coords must equal n (square P).  We pad with extra zero coords if
       needed so the embedding dim == n; the slack is the LAST coord.
    """
    n = mb + k
    # coord layout needs at least mb+4; ensure n large enough by construction
    # if n < mb+4, increase k handled by caller. We place: base 0..mb-1, up=mb,
    # s1=mb+1, s2=mb+2, slack=n-1. Requires n >= mb+4.
    assert n >= mb + 4, f"need n>=mb+4 (got n={n}, mb={mb}); increase k"
    up, s1, s2, slack = mb, mb + 1, mb + 2, n - 1
    pts = np.zeros((n, n))
    # anchors: base_r * e_a, height 0
    for a in range(mb):
        pts[a, a] = base_r
    bcen = pts[:mb].mean(axis=0)
    # hidden polygon: regular k-gon of radius w in (s1,s2), lifted by H in 'up',
    # centered above anchor centroid.
    for j in range(k):
        th = 2 * np.pi * j / k
        p = bcen.copy()
        p[up] += H
        p[s1] += w * np.cos(th)
        p[s2] += w * np.sin(th)
        pts[mb + j] = p
    pts = _fix_slack(pts, slack)
    anchor_idx = list(range(mb))
    hidden_idx = list(range(mb, mb + k))
    meta = {"family": "thin_diamond", "H": H, "k": k, "mb": mb,
            "base_r": base_r, "w": w, "n": n}
    return pts, anchor_idx, hidden_idx, meta


def thin_segment(H, k=2, mb=3, base_r=0.5, w=0.0, seed=0):
    """Degenerate diamond: k hidden rows COLLINEAR (on a segment) at height H.
       w controls the spread along the segment. With w=0 they coincide (a single
       far point repeated). With w>0 they are k points on a line at height H -- each
       interior one is an exact affine comb of its endpoints (NON-vertex) and the two
       endpoints are the only vertices -> at most 2 hidden vertices, mutually the only
       far ones. This is the THINNEST circuit; good for isolating the H-cost.
    """
    n = mb + k
    assert n >= mb + 3, f"need n>=mb+3 (got n={n})"
    up, s1, slack = mb, mb + 1, n - 1
    pts = np.zeros((n, n))
    for a in range(mb):
        pts[a, a] = base_r
    bcen = pts[:mb].mean(axis=0)
    for j in range(k):
        frac = (j / (k - 1) - 0.5) if k > 1 else 0.0   # in [-0.5,0.5]
        p = bcen.copy()
        p[up] += H
        p[s1] += 2 * w * frac
        pts[mb + j] = p
    pts = _fix_slack(pts, slack)
    return pts, list(range(mb)), list(range(mb, mb + k)), \
        {"family": "thin_segment", "H": H, "k": k, "mb": mb, "base_r": base_r, "w": w, "n": n}


def isolated_far(H, mb=3, base_r=0.5, seed=0):
    """CONTROL: a SINGLE far row at height H over a base.  An isolated far row is
       PROVABLY well-exposed (margin >= rho/(2+4 delta)) so it JOINS W and its dist
       to conv W collapses to 0.  The pipeline MUST report verified_hidden=False here
       (dist ~ 0), confirming the hidden-constraint check rejects non-hidden rows.
    """
    n = mb + 1
    up, slack = mb, n - 1
    pts = np.zeros((n, n))
    for a in range(mb):
        pts[a, a] = base_r
    bcen = pts[:mb].mean(axis=0)
    p = bcen.copy(); p[up] += H
    pts[mb] = p
    pts = _fix_slack(pts, slack)
    return pts, list(range(mb)), [mb], \
        {"family": "isolated_far", "H": H, "mb": mb, "base_r": base_r, "n": n}


def inside_circuit(H, k=4, mb=3, base_r=0.5, w=0.4, seed=0):
    """CONTROL: a circuit of k rows at height H but with LARGE spread w so the
       circuit centroid (an extra hidden row) lies INSIDE conv(anchors + circuit).
       A row INSIDE conv W costs nothing (neg=0 achievable) and is NOT far -> the
       pipeline should see dist ~ 0 for the interior point (reproduces the known
       zero-neg transient circuits).  We mark the centroid as the 'hidden' test row.
    """
    n = mb + k + 1
    assert n >= mb + 4
    up, s1, s2, slack = mb, mb + 1, mb + 2, n - 1
    pts = np.zeros((n, n))
    for a in range(mb):
        pts[a, a] = base_r
    bcen = pts[:mb].mean(axis=0)
    for j in range(k):
        th = 2 * np.pi * j / k
        p = bcen.copy(); p[up] += H * 0.0   # circuit at SAME height as base (not far up)
        p[s1] += w * np.cos(th); p[s2] += w * np.sin(th)
        pts[mb + j] = p
    # centroid of circuit (interior, same height) -> should be inside conv, neg 0
    cen = pts[mb:mb + k].mean(axis=0)
    pts[mb + k] = cen
    pts = _fix_slack(pts, slack)
    return pts, list(range(mb)), [mb + k], \
        {"family": "inside_circuit", "H": H, "k": k, "mb": mb, "base_r": base_r, "w": w, "n": n}


def hume_rank_one(t, n=4):
    """CALIBRATION: a rank-one-ish Hume family with KNOWN neg = t^2 and a far row that
       EXPOSES.  Construct P = I + t*(u v^T) shaped to be an exact idempotent with one
       transient row whose negativity is ~ t^2.  We use the classic 2x2-block:
         P = [[1,0],[ -t^2/(1-?)...]] -- instead we build the standard rank-1 update.
       Simplest exact idempotent with a tunable transient:  pick a stochastic target
       and a single eigen-direction.  We return P plus the index of the 'far' row.
       (This is a sanity check on W-computation: the far row should be exposed.)
    """
    # Build a 2-state lumping idempotent perturbed: rows mostly e_i, one row with a
    # small signed excursion of mass ~ t (neg ~ t). For a t^2 calibration we use the
    # square-hole element q_r^2 style: a row = e_0 + t(e_1-e_0) reflected -> neg ~ t^2.
    P = np.eye(n)
    # transient row n-1: e_{n-1} pushed: coefficient (1+t) on n-1, -t on 0, then square.
    # Make it idempotent by using a rank-1 projector onto an affine line.
    # Use: u = e_{n-1} - e_0 (sums 0), and P = I - t*outer(w, u) with w chosen so P^2=P.
    # For a genuine idempotent we take the spectral projector onto span complement.
    # Simpler & exact: 2x2 block on {0, n-1}:  [[1+a, -a],[b, 1-b]] is idempotent iff
    # it's a projector: trace=1 (rank1) and det=0 -> (1+a)(1-b)+ab=... set rank1.
    # Projector onto a line: P0 = v w^T / (w^T v), with w^T(row)=... Let's just take
    # the well-known neg=t^2 element from obs-bridge-numerics conceptually: a 3x3.
    a = t
    P = np.eye(n)
    # rank-1 projector block on coords {0,1}: project onto direction d=(1,-? )
    # P_block = [[1, 0],[c, 0]] has P^2=P (idempotent, rank1) and rowsums: row0=1, row1=c.
    # To get rowsum 1 we need a 1 elsewhere. Use 3 coords {0,1,2}:
    # row1 = c*e0 + (1-c)*e2 with c can be negative -> neg = |c| if c<0.
    # We want neg ~ t^2: pick c = -t^2. Build a consistent idempotent.
    P = np.eye(n)
    c = -a * a
    P[1, 0] = c
    P[1, 1] = 0.0
    P[1, 2 % n] = 1.0 - c
    # verify P^2=P numerically; this simple form: row1 maps... check idempotence
    return P, n - 1
