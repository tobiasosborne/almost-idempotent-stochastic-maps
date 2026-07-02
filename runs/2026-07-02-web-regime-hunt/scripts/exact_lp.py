#!/usr/bin/env python3
"""
exact_lp.py -- exact two-phase simplex over Fractions (Bland's rule, no cycling).

Solves:   min c.x  s.t.  A_ub x <= b_ub,  A_eq x = b_eq,  lb_i <= x_i <= ub_i
with lb/ub each possibly None (i.e. -inf / +inf).  All data Fraction.

Returns dict: {status: 'optimal'|'infeasible'|'unbounded', fun: Fraction, x: [Fraction]}.

Everything is exact rational.  Used to certify:
  - dist_1(p_i, conv W)      (min ell^1 distance to a convex hull)
  - exposedness margin t*(v) (max separating-margin LP)
  - vertex test              (min ell^1 reconstruction error)
"""
from fractions import Fraction as F


def _simplex_standard(c, A, b, nvar, verbose=False):
    """min c.x s.t. A x = b, x >= 0, all Fraction, b >= 0 assumed.
       Two-phase, Bland's rule.  Returns (status, fun, x)."""
    m = len(A)
    # ensure b >= 0
    A = [row[:] for row in A]
    b = b[:]
    c = c[:]
    for i in range(m):
        if b[i] < 0:
            b[i] = -b[i]
            A[i] = [-v for v in A[i]]
    # Phase I: add artificials
    total = nvar + m
    # tableau rows: A | I_art | b
    T = []
    for i in range(m):
        row = A[i][:] + [F(0)] * m + [b[i]]
        row[nvar + i] = F(1)
        T.append(row)
    basis = [nvar + i for i in range(m)]
    # phase I cost: minimize sum artificials
    def run(cost):
        # cost: list length total
        # reduced-cost objective row maintained explicitly
        while True:
            # compute reduced costs: c_j - c_B B^{-1} A_j; tableau already in canonical form
            # objective row z_j - c_j via current basis
            cB = [cost[basis[i]] for i in range(m)]
            # reduced cost for each nonbasic column j: cost[j] - sum_i cB[i]*T[i][j]
            entering = -1
            for j in range(total):
                if j in basis:
                    continue
                rc = cost[j]
                for i in range(m):
                    rc -= cB[i] * T[i][j]
                if rc < 0:
                    entering = j  # Bland: first improving
                    break
            if entering == -1:
                return  # optimal
            # ratio test
            leave = -1
            best = None
            for i in range(m):
                aij = T[i][entering]
                if aij > 0:
                    ratio = T[i][-1] / aij
                    if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                        best = ratio
                        leave = i
            if leave == -1:
                raise RuntimeError("unbounded (should not happen in phase I)")
            # pivot
            piv = T[leave][entering]
            T[leave] = [v / piv for v in T[leave]]
            for i in range(m):
                if i == leave:
                    continue
                f = T[i][entering]
                if f != 0:
                    T[i] = [a - f * bb for a, bb in zip(T[i], T[leave])]
            basis[leave] = entering

    phase1_cost = [F(0)] * total
    for j in range(nvar, total):
        phase1_cost[j] = F(1)
    run(phase1_cost)
    # phase I objective value
    art_val = F(0)
    for i in range(m):
        if basis[i] >= nvar:
            art_val += T[i][-1]
    if art_val > 0:
        return ("infeasible", None, None)
    # drive artificials out of basis if any remain at zero level
    for i in range(m):
        if basis[i] >= nvar:
            # try pivot on a nonbasic structural col with nonzero entry
            done = False
            for j in range(nvar):
                if j not in basis and T[i][j] != 0:
                    piv = T[i][j]
                    T[i] = [v / piv for v in T[i]]
                    for r in range(m):
                        if r == i:
                            continue
                        f = T[r][j]
                        if f != 0:
                            T[r] = [a - f * bb for a, bb in zip(T[r], T[i])]
                    basis[i] = j
                    done = True
                    break
            # if not done, row is redundant; leave artificial in basis at 0
    # Phase II
    cost = c[:] + [F(0)] * m
    # unbounded check inside run: adapt run to detect unboundedness
    while True:
        cB = [cost[basis[i]] for i in range(m)]
        entering = -1
        for j in range(total):
            if j in basis:
                continue
            # never re-enter artificial
            if j >= nvar:
                continue
            rc = cost[j]
            for i in range(m):
                rc -= cB[i] * T[i][j]
            if rc < 0:
                entering = j
                break
        if entering == -1:
            break
        leave = -1
        best = None
        for i in range(m):
            aij = T[i][entering]
            if aij > 0:
                ratio = T[i][-1] / aij
                if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                    best = ratio
                    leave = i
        if leave == -1:
            return ("unbounded", None, None)
        piv = T[leave][entering]
        T[leave] = [v / piv for v in T[leave]]
        for i in range(m):
            if i == leave:
                continue
            f = T[i][entering]
            if f != 0:
                T[i] = [a - f * bb for a, bb in zip(T[i], T[leave])]
        basis[leave] = entering
    # extract solution
    x = [F(0)] * nvar
    for i in range(m):
        if basis[i] < nvar:
            x[basis[i]] = T[i][-1]
    fun = sum(c[j] * x[j] for j in range(nvar))
    return ("optimal", fun, x)


def linprog_exact(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    """Exact LP.  c: list of Fraction (length nx).  bounds: list of (lb,ub) each None-able.
       Returns {status, fun, x}."""
    nx = len(c)
    c = [F(v) for v in c]
    if bounds is None:
        bounds = [(F(0), None)] * nx
    A_ub = [] if A_ub is None else [[F(v) for v in row] for row in A_ub]
    b_ub = [] if b_ub is None else [F(v) for v in b_ub]
    A_eq = [] if A_eq is None else [[F(v) for v in row] for row in A_eq]
    b_eq = [] if b_eq is None else [F(v) for v in b_eq]

    # Map each original var to standard nonneg vars via substitution.
    # x_i = shift_i + s_i * y_i  (+ possibly minus another var for free)
    # We'll build: for each original var, an affine map to new vars.
    # Represent x_i = base_i + sum over (newvar_index, coeff).
    new_c = []
    # each original var expands; keep transform: list of (list of (idx,coeff), const)
    transforms = []
    extra_ub_rows = []  # standard-form-friendly upper bound constraints handled as <= via slack later
    extra_ub_b = []

    def add_var(coef_in_obj):
        new_c.append(coef_in_obj)
        return len(new_c) - 1

    for i in range(nx):
        lb, ub = bounds[i]
        if lb is not None:
            lb = F(lb)
        if ub is not None:
            ub = F(ub)
        if lb is None and ub is None:
            # free: x = xp - xn
            ip = add_var(c[i])
            inn = add_var(-c[i])
            transforms.append(([(ip, F(1)), (inn, F(-1))], F(0)))
        elif lb is not None and ub is None:
            # x = lb + y, y>=0
            iy = add_var(c[i])
            transforms.append(([(iy, F(1))], lb))
        elif lb is None and ub is not None:
            # x = ub - y, y>=0
            iy = add_var(-c[i])
            transforms.append(([(iy, F(-1))], ub))
        else:
            # both finite: x = lb + y, 0<=y<=ub-lb ; add y <= (ub-lb)
            iy = add_var(c[i])
            transforms.append(([(iy, F(1))], lb))
            extra_ub_rows.append((iy, ub - lb))

    nnew = len(new_c)

    # Build equality/inequality constraints in new vars, then add slacks for inequalities.
    rows = []   # each: (coeffs list length grows, rhs)
    # We'll first collect all constraints as (coeff_dict over new vars, rhs, sense) sense in {'<=','='}
    cons = []

    def expand_row(orig_row):
        # returns dict newvar->coeff, and constant contribution to LHS
        d = {}
        const = F(0)
        for i in range(nx):
            a = orig_row[i]
            if a == 0:
                continue
            terms, base = transforms[i]
            const += a * base
            for (idx, co) in terms:
                d[idx] = d.get(idx, F(0)) + a * co
        return d, const

    for r in range(len(A_ub)):
        d, const = expand_row(A_ub[r])
        cons.append((d, b_ub[r] - const, '<='))
    for r in range(len(A_eq)):
        d, const = expand_row(A_eq[r])
        cons.append((d, b_eq[r] - const, '='))
    for (iy, cap) in extra_ub_rows:
        cons.append(({iy: F(1)}, cap, '<='))

    # add slack vars for <= constraints
    nslack = sum(1 for _, _, s in cons if s == '<=')
    total_vars = nnew + nslack
    A = []
    b = []
    slack_ptr = nnew
    for (d, rhs, sense) in cons:
        row = [F(0)] * total_vars
        for idx, co in d.items():
            row[idx] = co
        if sense == '<=':
            row[slack_ptr] = F(1)
            slack_ptr += 1
        A.append(row)
        b.append(rhs)

    cost = new_c + [F(0)] * nslack
    if not A:
        # no constraints: unbounded unless c>=0 componentwise etc. Handle trivially.
        # minimize cost with x>=0 -> if any cost<0 unbounded else 0.
        if any(v < 0 for v in cost):
            return {"status": "unbounded", "fun": None, "x": None}
        xnew = [F(0)] * total_vars
    else:
        status, fun, xnew = _simplex_standard(cost, A, b, total_vars)
        if status != "optimal":
            return {"status": status, "fun": None, "x": None}

    # reconstruct original x
    x = []
    for i in range(nx):
        terms, base = transforms[i]
        val = base
        for (idx, co) in terms:
            val += co * xnew[idx]
        x.append(val)
    fun = sum(c[i] * x[i] for i in range(nx))
    return {"status": "optimal", "fun": fun, "x": x}


if __name__ == "__main__":
    import numpy as np
    from scipy.optimize import linprog as sp_lp
    import random
    random.seed(0)
    # random test vs scipy
    ntest = 300
    maxerr = 0.0
    fails = 0
    for _ in range(ntest):
        n = random.randint(2, 5)
        mub = random.randint(1, 4)
        c = [F(random.randint(-5, 5)) for _ in range(n)]
        A_ub = [[F(random.randint(-3, 3)) for _ in range(n)] for _ in range(mub)]
        b_ub = [F(random.randint(0, 8)) for _ in range(mub)]
        bounds = [(F(0), F(6)) for _ in range(n)]
        r = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
        rs = sp_lp([float(v) for v in c],
                   A_ub=[[float(v) for v in row] for row in A_ub],
                   b_ub=[float(v) for v in b_ub],
                   bounds=[(0, 6)] * n, method="highs")
        if r["status"] == "optimal" and rs.status == 0:
            err = abs(float(r["fun"]) - rs.fun)
            maxerr = max(maxerr, err)
            if err > 1e-6:
                fails += 1
                print("MISMATCH", float(r["fun"]), rs.fun)
        elif (r["status"] == "optimal") != (rs.status == 0):
            # allow unbounded/infeasible mismatch reporting
            print("STATUS DIFF", r["status"], rs.status)
            fails += 1
    print(f"random LP test done: maxerr={maxerr:.2e} fails={fails}/{ntest}")
