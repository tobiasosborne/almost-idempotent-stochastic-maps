#!/usr/bin/env python3 -u
"""
d3_seed.py -- build a FEASIBLE seed (Lambda0, R0) with R0 Lambda0 = I_r, rowsums 1,
that realizes a given target row set P0 = targets (exactly), to warm-start the
alternating LP.

Construction (archetype = a chosen affinely-independent subset of the target rows):
  pick r target rows as archetypes A (r x n), affinely independent, each summing to 1.
  R0 = A.   Lambda0[i,:] = barycentric coords of targets[i] w.r.t. A (lam.A=t_i, lam.1=1).
  Then R0 Lambda0 = A * bary(A) ; bary(archetype_a)=e_a so the archetype block is I_r;
  for non-archetype rows the column-block need not be e_a, BUT R0 Lambda0 picks the
  archetype columns of Lambda0, which ARE e_a -> R0 Lambda0 = I_r exactly.  (Because
  (R0 Lambda0)[a,b] = sum_k A[a,k] Lambda0[k? ...]) -- we VERIFY numerically.

We must choose r = rank of the affine span of the targets (so A is a basis of the
flat).  The archetypes should include the ANCHOR rows (they are the intended W) so the
idempotent's range is the anchor flat + the hidden directions.  We greedily pick a
maximal affinely-independent subset, preferring anchors first then hidden rows.
"""
import numpy as np


def affine_rank(pts, tol=1e-9):
    pts = np.asarray(pts, float)
    if len(pts) == 0:
        return 0
    M = pts - pts[0]
    return np.linalg.matrix_rank(M, tol=tol) + 1


def bary(t, A):
    """barycentric coords lam: lam @ A = t, lam.sum=1 (least squares; exact if t in flat)."""
    r = A.shape[0]
    M = np.vstack([A.T, np.ones(r)])     # (n+1) x r
    b = np.concatenate([t, [1.0]])
    lam, *_ = np.linalg.lstsq(M, b, rcond=None)
    resid = float(np.abs(M @ lam - b).max())
    return lam, resid


def pick_archetypes(targets, prefer_first, tol=1e-7):
    """Greedily select a maximal affinely-independent set of row indices, preferring
       the indices in prefer_first (anchors) first."""
    targets = np.asarray(targets, float)
    n = targets.shape[0]
    order = list(prefer_first) + [i for i in range(n) if i not in prefer_first]
    chosen = []
    for i in order:
        trial = chosen + [i]
        if affine_rank(targets[trial], tol=tol) == len(trial):
            chosen.append(i)
    return chosen


def seed_from_targets(targets, anchor_idx, tol=1e-7):
    """Return Lam0 (n x r), R0 (r x n), info. R0 = archetype rows; Lam0 = bary coords.
       Verifies R0 Lam0 = I_r and rowsums."""
    targets = np.asarray(targets, float)
    n = targets.shape[0]
    arch = pick_archetypes(targets, anchor_idx, tol=tol)
    r = len(arch)
    A = targets[arch]                      # r x n
    R0 = A.copy()
    Lam0 = np.zeros((n, r))
    max_resid = 0.0
    for i in range(n):
        lam, resid = bary(targets[i], A)
        Lam0[i] = lam
        max_resid = max(max_resid, resid)
    RL = R0 @ Lam0
    rl_err = float(np.abs(RL - np.eye(r)).max())
    P0 = Lam0 @ R0
    realize_err = float(np.abs(P0 - targets).max())
    info = {"r": r, "arch": arch, "bary_resid": max_resid,
            "RLambda_err": rl_err, "realize_err": realize_err,
            "R_rowsum_err": float(np.abs(R0.sum(1) - 1).max()),
            "Lam_rowsum_err": float(np.abs(Lam0.sum(1) - 1).max())}
    return Lam0, R0, info
