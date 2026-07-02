#!/usr/bin/env python3 -u
"""
test_lp_robustness.py -- Regression test for the FALSE-NEGATIVE exposedness bug.

DISCOVERED FAILURE MODE (d1-report.md): on near-coincident / badly scaled rows
(clusters of nearly-identical rows in a low-rank exact idempotent), the default
scipy HiGHS *simplex* solver returns status 4 ('numerical difficulties') for the
exposedness LP. The old code treated 'not success' as 'non-exposed', wrongly
dropping a genuinely well-exposed vertex from W and inflating
  max_i dist1(p_i, conv W)/tau  to a bogus ~69 ('counterexample' spike).

The fix: robust_linprog tries highs-ipm (interior point) first and trusts only
status==2 as genuine infeasibility. This test PINS that the spike instance is
correctly classified (ratio small, the third cluster's vertex IS exposed).

Run: python3 test_lp_robustness.py  (expects out/spike_Lambda.npy present).
"""
import sys, numpy as np
from d3_hunt import R_from_Lambda
from d1_infra import (neg_mass, exposed_margin, well_exposed_set, ratio_stats,
                      robust_linprog)

def main():
    L = np.load("out/spike_Lambda.npy")
    R,_ = R_from_Lambda(L); P = L@R
    nm, delta = neg_mass(P); tau = float(np.sqrt(delta))
    rho, kappa = 4*tau, 0.25*tau

    # (1) the previously-misclassified vertex (cluster-3 representative) IS exposed
    ok2, s2, _ = exposed_margin(P, 2, rho, kappa)
    assert ok2, "REGRESSION: row 2 should be well-exposed (was false-negative)"
    print(f"[ok] row 2 exposed (margin={s2:.4f})", flush=True)

    # (2) the headline ratio is small (conjecture-consistent), NOT the bogus ~69
    rs = ratio_stats(P, C=4.0, c=0.25)
    assert rs["max_ratio"] < 0.5, f"REGRESSION: ratio={rs['max_ratio']} (bogus spike?)"
    print(f"[ok] max_ratio={rs['max_ratio']:.4f} (was bogus 69.0 with buggy LP)", flush=True)

    # (3) robust_linprog actually returns success where bare 'highs' simplex fails:
    #     re-create the exposer LP for row 2 and confirm robust path succeeds.
    from scipy.optimize import linprog
    n, d = P.shape
    di = np.abs(P - P[2]).sum(axis=1)
    far = [k for k in range(n) if di[k] >= rho - 1e-12 and k != 2]
    def hv(k):
        v = np.zeros(d+2); v[:d] = P[k]; v[d] = 1.0; return v
    c = np.zeros(d+2); c[-1] = -1.0
    A_ub=[]; b_ub=[]
    for k in range(n):
        A_ub.append(hv(k)); b_ub.append(1.0)
        A_ub.append(-hv(k)); b_ub.append(0.0)
    for k in far:
        v=-hv(k); v[-1]=1.0; A_ub.append(v); b_ub.append(-kappa)
    A_eq=[hv(2)]; b_eq=[0.0]
    bounds=[(None,None)]*d+[(None,None)]+[(0.0,10.0)]
    bare = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                   A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds, method="highs")
    rob = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds)
    print(f"[info] bare 'highs' success={bare.success} status={bare.status}; "
          f"robust success={rob.success}", flush=True)
    assert rob.success, "REGRESSION: robust_linprog should solve the exposer LP"
    # The bug is real iff bare simplex failed here; if scipy improves and bare also
    # succeeds, the test still passes (we only require robust to succeed).

    # (4) the aggressive-hunt 'counterexamples' (reported ratio inf / 340) were the
    #     SAME degenerate near-duplicate-row class; with the margin-based exposedness
    #     they MUST collapse to ~0.  Pin a few.
    try:
        arts = np.load("out/flagged_artifacts.npy", allow_pickle=True)
    except FileNotFoundError:
        arts = []
    for k, Lk in enumerate(arts):
        Lk = np.asarray(Lk, float)
        Rk,_ = R_from_Lambda(Lk); Pk = Lk@Rk
        rk = ratio_stats(Pk)
        assert rk["max_ratio"] < 0.5, \
            f"REGRESSION: flagged artifact {k} ratio={rk['max_ratio']} (should be ~0)"
        print(f"[ok] flagged artifact {k}: ratio={rk['max_ratio']:.4f} |W|={rk['nW']} "
              f"(was reported inf/340)", flush=True)

    print("\nALL ROBUSTNESS TESTS PASSED", flush=True)

if __name__ == "__main__":
    main()
