#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt


OUT = "runs/2026-07-05-e1-uniformity-pilot/data/pilot-full-report.md"


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def row_l1(row):
    return sum(abs(x) for x in row)


def inf_norm(A):
    return max(row_l1(r) for r in A)


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eta(Q):
    return inf_norm(mat_sub(matmul(Q, Q), Q))


def dist(Q, E):
    return inf_norm(mat_sub(Q, E))


def assert_row_stochastic(Q):
    for row in Q:
        assert all(x >= 0 for x in row), Q
        assert sum(row) == 1, row


def assert_idempotent_stochastic(E):
    assert_row_stochastic(E)
    E2 = matmul(E, E)
    assert E2 == E, E


def frac(s):
    return F(s)


def fmt(x):
    x = F(x)
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def matrix_md(M):
    return "\n".join("- [" + ", ".join(fmt(x) for x in row) + "]" for row in M)


def square_root_expr(q):
    q = F(q)
    if q < 0:
        raise ValueError(q)
    rn = isqrt(q.numerator)
    rd = isqrt(q.denominator)
    if rn * rn == q.numerator and rd * rd == q.denominator:
        return fmt(F(rn, rd))
    return f"sqrt({fmt(q)})"


def ratio_data(Q, E):
    e = eta(Q)
    d = dist(Q, E)
    assert e > 0
    r2 = d * d / e
    return {"eta": e, "dist": d, "r2": r2, "rexpr": square_root_expr(r2)}


def solve_square(A, b):
    n = len(b)
    M = [[F(A[i][j]) for j in range(n)] + [F(b[i])] for i in range(n)]
    for col in range(n):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r == col:
                continue
            f = M[r][col]
            if f:
                M[r] = [x - f * y for x, y in zip(M[r], M[col])]
    return [M[i][n] for i in range(n)]


def lp_minimize_t(num_vars, constraints):
    """Minimize the last variable t subject to exact rational linear inequalities.

    constraints are pairs (coefficients, rhs), interpreted as coeff*x <= rhs.
    This tiny vertex enumerator is intentionally only used for n=3 pilot LPs.
    """
    best = None
    best_active = None
    for active in combinations(range(len(constraints)), num_vars):
        A = [constraints[i][0] for i in active]
        b = [constraints[i][1] for i in active]
        x = solve_square(A, b)
        if x is None:
            continue
        if all(dot(c, x) <= rhs for c, rhs in constraints):
            if best is None or x[-1] < best[-1]:
                best = x
                best_active = active
    assert best is not None, "LP has no enumerated optimum"
    return best, best_active


def eval_affine(expr, params):
    const, coeff = expr
    return const + dot(coeff, params)


def solve_structured_type(Q, name, param_count, param_constraints, row_exprs):
    n = len(Q)
    constraints = []
    for coeff, rhs in param_constraints:
        constraints.append((coeff + [F(0)], rhs))
    constraints.append(([F(0)] * param_count + [F(-1)], F(0)))  # t >= 0
    for i in range(n):
        for signs in product([F(-1), F(1)], repeat=n):
            coeff = [F(0)] * param_count
            const = F(0)
            for j in range(n):
                c, a = row_exprs[i][j]
                const += signs[j] * (c - Q[i][j])
                for k in range(param_count):
                    coeff[k] += signs[j] * a[k]
            constraints.append((coeff + [F(-1)], -const))
    sol, active = lp_minimize_t(param_count + 1, constraints)
    params = sol[:-1]
    E = [[eval_affine(row_exprs[i][j], params) for j in range(n)] for i in range(n)]
    assert_idempotent_stochastic(E)
    assert dist(Q, E) == sol[-1]
    return {"name": name, "E": E, "dist": sol[-1], "params": params, "active": active}


def const_expr(x, k):
    return (F(x), [F(0)] * k)


def var_expr(idx, k, const=F(0), scale=F(1)):
    coeff = [F(0)] * k
    coeff[idx] = scale
    return (F(const), coeff)


def one_minus_var_expr(idx, k):
    coeff = [F(0)] * k
    coeff[idx] = F(-1)
    return (F(1), coeff)


def n3_min_stochastic_idempotent(Q):
    n = len(Q)
    assert n == 3
    types = []

    # Identity.
    E_id = [[const_expr(F(1) if i == j else F(0), 0) for j in range(3)] for i in range(3)]
    types.append(solve_structured_type(Q, "I_3", 0, [], E_id))

    # Rank-one: all rows equal p=(p0,p1,1-p0-p1).
    k = 2
    p = [var_expr(0, k), var_expr(1, k), (F(1), [F(-1), F(-1)])]
    rows = [p, p, p]
    cons = [([F(-1), F(0)], F(0)), ([F(0), F(-1)], F(0)), ([F(1), F(1)], F(1))]
    types.append(solve_structured_type(Q, "rank-one all rows equal p", k, cons, rows))

    # One singleton recurrent class and one two-state recurrent class.
    for a in range(3):
        pair = [j for j in range(3) if j != a]
        b, c = pair
        k = 1
        rows = []
        for i in range(3):
            row = [const_expr(0, k) for _ in range(3)]
            if i == a:
                row[a] = const_expr(1, k)
            else:
                row[b] = var_expr(0, k)
                row[c] = one_minus_var_expr(0, k)
            rows.append(row)
        cons = [([F(-1)], F(0)), ([F(1)], F(1))]
        types.append(solve_structured_type(Q, f"singleton {a} plus recurrent pair {b,c}", k, cons, rows))

    # Two singleton recurrent classes and one transient row mixing between them.
    for a, b in combinations(range(3), 2):
        c = ({0, 1, 2} - {a, b}).pop()
        k = 1
        rows = []
        for i in range(3):
            row = [const_expr(0, k) for _ in range(3)]
            if i == a:
                row[a] = const_expr(1, k)
            elif i == b:
                row[b] = const_expr(1, k)
            else:
                row[a] = var_expr(0, k)
                row[b] = one_minus_var_expr(0, k)
            rows.append(row)
        cons = [([F(-1)], F(0)), ([F(1)], F(1))]
        types.append(solve_structured_type(Q, f"singletons {a,b}; transient {c}", k, cons, rows))

    best = min(types, key=lambda item: item["dist"])
    return best, types


def hume_signed(s):
    v = [F(1), -F(1) + s, -s]
    u = [F(1) - s + s * s, -s, F(0)]
    I = eye(3)
    P = [[I[i][j] - u[i] * v[j] for j in range(3)] for i in range(3)]
    assert matmul(P, P) == P
    assert all(sum(row) == 1 for row in P)
    return P


def positive_row_normalize(P):
    Q = []
    for row in P:
        pos = [x if x > 0 else F(0) for x in row]
        total = sum(pos)
        assert total > 0
        Q.append([x / total for x in pos])
    assert_row_stochastic(Q)
    return Q


def hume_stochastic_anchor(s):
    return positive_row_normalize(hume_signed(s))


def lazy_cycle(a):
    C = [[F(0), F(1), F(0)], [F(0), F(0), F(1)], [F(1), F(0), F(0)]]
    I = eye(3)
    Q = [[(F(1) - a) * I[i][j] + a * C[i][j] for j in range(3)] for i in range(3)]
    assert_row_stochastic(Q)
    return Q


def uniform_cycle(a):
    C = [[F(0), F(1), F(0)], [F(0), F(0), F(1)], [F(1), F(0), F(0)]]
    J = [[F(1, 3) for _ in range(3)] for _ in range(3)]
    Q = [[(F(1) - a) * J[i][j] + a * C[i][j] for j in range(3)] for i in range(3)]
    assert_row_stochastic(Q)
    return Q


def clone_matrix(M, idx, weights):
    n = len(M)
    assert sum(weights) == 1
    old_of = []
    col_weight = []
    for i in range(n):
        if i == idx:
            for w in weights:
                old_of.append(i)
                col_weight.append(w)
        else:
            old_of.append(i)
            col_weight.append(F(1))
    N = len(old_of)
    C = [[col_weight[b] * M[old_of[a]][old_of[b]] for b in range(N)] for a in range(N)]
    return C


def block_sum(A, B):
    n, m = len(A), len(B)
    Z = [[F(0) for _ in range(n + m)] for _ in range(n + m)]
    for i in range(n):
        for j in range(n):
            Z[i][j] = A[i][j]
    for i in range(m):
        for j in range(m):
            Z[n + i][n + j] = B[i][j]
    return Z


def level_coupled_family(n):
    """A stochastic averaging chain with real cross-level coupling.

    The candidate idempotent collapses every level to state 0.  Level i places
    most mass on 0 and a decreasing tail on all lower levels; changing n changes
    every high-level row, so this is not a clone/direct-sum construction.
    """
    eps = F(1, 12 * n)
    Q = []
    for i in range(n):
        row = [F(0) for _ in range(n)]
        if i == 0:
            row[0] = F(1)
        else:
            tail_total = i * eps
            row[0] = F(1) - tail_total
            for j in range(1, i + 1):
                row[j] = eps
        Q.append(row)
    E = [[F(1)] + [F(0) for _ in range(n - 1)] for _ in range(n)]
    assert_row_stochastic(Q)
    assert_idempotent_stochastic(E)
    return Q, E


def assert_ratio_from_matrices(Q, E, expected_eta, expected_dist, expected_r2):
    assert_row_stochastic(Q)
    assert_idempotent_stochastic(E)
    got_eta = eta(Q)
    got_dist = dist(Q, E)
    got_r2 = got_dist * got_dist / got_eta
    assert got_eta == expected_eta, (got_eta, expected_eta)
    assert got_dist == expected_dist, (got_dist, expected_dist)
    assert got_r2 == expected_r2, (got_r2, expected_r2)


def main():
    lines = []
    all_records = []
    asserts = []

    anchor_s = [F(1, 3), F(1, 5), F(1, 8), F(1, 16)]
    anchor_rows = []
    for s in anchor_s:
        Q = hume_stochastic_anchor(s)
        best, _ = n3_min_stochastic_idempotent(Q)
        E = best["E"]
        data = ratio_data(Q, E)
        assert data["eta"] < F(1, 4)
        assert_ratio_from_matrices(Q, E, data["eta"], data["dist"], data["r2"])
        all_records.append(("Hume-positive-part s=" + fmt(s), Q, E, data))
        anchor_rows.append((s, Q, E, best, data))
        asserts.append(f"Hume-positive-part s={fmt(s)}: eta={fmt(data['eta'])}, dist={fmt(data['dist'])}, r^2={fmt(data['r2'])}")

    perturbed = [
        ("lazy-cycle a=1/10", lazy_cycle(F(1, 10))),
        ("uniform-cycle a=1/10", uniform_cycle(F(1, 10))),
    ]
    pert_rows = []
    for name, Q in perturbed:
        best, _ = n3_min_stochastic_idempotent(Q)
        E = best["E"]
        data = ratio_data(Q, E)
        assert data["eta"] < F(1, 4)
        assert_ratio_from_matrices(Q, E, data["eta"], data["dist"], data["r2"])
        all_records.append((name, Q, E, data))
        pert_rows.append((name, Q, E, best, data))
        asserts.append(f"{name}: eta={fmt(data['eta'])}, dist={fmt(data['dist'])}, r^2={fmt(data['r2'])}")

    # Invariance checks.
    Q0 = hume_stochastic_anchor(F(1, 3))
    E0 = n3_min_stochastic_idempotent(Q0)[0]["E"]
    Qc = clone_matrix(Q0, 2, [F(2, 5), F(3, 5)])
    Ec = clone_matrix(E0, 2, [F(2, 5), F(3, 5)])
    assert eta(Qc) == eta(Q0)
    assert dist(Qc, Ec) == dist(Q0, E0)
    assert_idempotent_stochastic(Ec)
    clone_data = ratio_data(Qc, Ec)
    assert clone_data["eta"] < F(1, 4)
    assert_ratio_from_matrices(Qc, Ec, clone_data["eta"], clone_data["dist"], clone_data["r2"])
    asserts.append(f"clone of Hume-positive-part s=1/3: eta={fmt(clone_data['eta'])}, dist={fmt(clone_data['dist'])}, r^2={fmt(clone_data['r2'])}")

    Q1 = hume_stochastic_anchor(F(1, 5))
    E1 = n3_min_stochastic_idempotent(Q1)[0]["E"]
    Q2 = lazy_cycle(F(1, 10))
    E2 = n3_min_stochastic_idempotent(Q2)[0]["E"]
    Qb = block_sum(Q1, Q2)
    Eb = block_sum(E1, E2)
    assert eta(Qb) == max(eta(Q1), eta(Q2))
    assert dist(Qb, Eb) == max(dist(Q1, E1), dist(Q2, E2))
    block_data = ratio_data(Qb, Eb)
    assert block_data["eta"] < F(1, 4)
    assert_ratio_from_matrices(Qb, Eb, block_data["eta"], block_data["dist"], block_data["r2"])
    asserts.append(f"block sum Hume s=1/5 with lazy-cycle a=1/10: eta={fmt(block_data['eta'])}, dist={fmt(block_data['dist'])}, r^2={fmt(block_data['r2'])}")

    coupled_rows = []
    for n in range(4, 13):
        Q, E = level_coupled_family(n)
        data = ratio_data(Q, E)
        assert data["eta"] < F(1, 4)
        assert_ratio_from_matrices(Q, E, data["eta"], data["dist"], data["r2"])
        coupled_rows.append((n, Q, E, data))
        all_records.append((f"level-coupled n={n}", Q, E, data))
        asserts.append(f"level-coupled n={n}: eta={fmt(data['eta'])}, dist={fmt(data['dist'])}, r^2={fmt(data['r2'])}")
    assert all(coupled_rows[i][3]["r2"] <= coupled_rows[i + 1][3]["r2"] for i in range(len(coupled_rows) - 1))

    largest = max(all_records, key=lambda rec: rec[3]["r2"])
    largest_label, largest_Q, largest_E, largest_data = largest

    lines.append(f"Largest certified ratio seen: `{largest_data['rexpr']}` (`r^2={fmt(largest_data['r2'])}`), at `{largest_label}` with `eta={fmt(largest_data['eta'])}` and `||Q-E||={fmt(largest_data['dist'])}`.")
    lines.append(f"The `n=4..12` coupled stochastic averaging family has bounded monotone drift only: `r^2` goes from `{fmt(coupled_rows[0][3]['r2'])}` to `{fmt(coupled_rows[-1][3]['r2'])}`; this is a bounded pilot, not evidence of a uniform theorem.")
    lines.append("")

    lines.append("## Protocol and tier tags")
    lines.append("")
    lines.append("[T0] means directly recomputed by the script from the printed rational matrices. [T1] means a short derivation from `E^2=E` or block/clone algebra, checked on examples. [T2] means pilot interpretation. [T3] means suggested next work.")
    lines.append("")
    lines.append("Rerun command:")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 runs/2026-07-05-e1-uniformity-pilot/scripts/e1_worker_b_pilot.py")
    lines.append("```")
    lines.append("")

    lines.append("## Task 1 -- anchors from `ex-hume`")
    lines.append("")
    lines.append("[T1] Locus used: `argument/lemmas/ex-hume.md` gives the signed exact family `P_s=I-u_s v_s^T`, with `v_s=(1,-1+s,-s)` and `u_s=(1-s+s^2,-s,0)^T`; its status is `proved-mod-audit`, so I use it only as a calibration source, not as a rigorous theorem.")
    lines.append("")
    lines.append("[T1] Stochastic conversion used here: rowwise positive-part normalization of that signed `P_s`. Since `P_s` has a single negative entry `-s^2`, this changes `P_s` by order `s^2`; all reported `eta`, distances, and ratios below are recomputed from the resulting nonnegative row-stochastic `Q_s` alone.")
    lines.append("")
    lines.append("| s | true n=3 min type | eta(Q) | min_E ||Q-E|| | r^2 | r |")
    lines.append("|---|---|---:|---:|---:|---:|")
    for s, Q, E, best, data in anchor_rows:
        lines.append(f"| `{fmt(s)}` | `{best['name']}` | `{fmt(data['eta'])}` | `{fmt(data['dist'])}` | `{fmt(data['r2'])}` | `{data['rexpr']}` |")
    lines.append("")
    lines.append("[T0] Anchor headline matrices:")
    for s, Q, E, best, data in anchor_rows:
        lines.append("")
        lines.append(f"### Hume-positive-part anchor s={fmt(s)}")
        lines.append("")
        lines.append(f"`eta={fmt(data['eta'])}`, `min_E ||Q-E||={fmt(data['dist'])}`, `r^2={fmt(data['r2'])}`, `r={data['rexpr']}`.")
        lines.append("")
        lines.append("Q:")
        lines.append(matrix_md(Q))
        lines.append("")
        lines.append("Certified minimizing E among all 3x3 stochastic idempotents:")
        lines.append(matrix_md(E))
    lines.append("")

    lines.append("## Task 2 -- exact minimum at n=3")
    lines.append("")
    lines.append("[T1] Structure derived from `E^2=E`: each row `e_i` is stationary for `E` because `e_iE=e_i`. Recurrent communicating classes are closed; inside one recurrent class all rows must be the same stationary distribution on that class, while every transient row is a convex mixture of those recurrent-class stationary rows. For `n=3`, this leaves only: identity; one rank-one class; one singleton plus one two-state recurrent class; or two singleton classes plus one transient row.")
    lines.append("")
    lines.append("[T0] The script enumerates exactly those `n=3` structures. The rank-one case is a 2-variable exact LP. The other nontrivial cases are 1-variable exact LPs. The objective is `max_i ||Q_i-E_i||_1`, encoded by all `2^3` sign inequalities per row and solved by exact rational vertex enumeration.")
    lines.append("")
    lines.append("Additional exact-minimum instances:")
    lines.append("")
    lines.append("| instance | true n=3 min type | eta(Q) | min_E ||Q-E|| | r^2 | r |")
    lines.append("|---|---|---:|---:|---:|---:|")
    for name, Q, E, best, data in pert_rows:
        lines.append(f"| `{name}` | `{best['name']}` | `{fmt(data['eta'])}` | `{fmt(data['dist'])}` | `{fmt(data['r2'])}` | `{data['rexpr']}` |")
    for name, Q, E, best, data in pert_rows:
        lines.append("")
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"`eta={fmt(data['eta'])}`, `min_E ||Q-E||={fmt(data['dist'])}`, `r^2={fmt(data['r2'])}`, `r={data['rexpr']}`.")
        lines.append("")
        lines.append("Q:")
        lines.append(matrix_md(Q))
        lines.append("")
        lines.append("Certified minimizing E among all 3x3 stochastic idempotents:")
        lines.append(matrix_md(E))
    lines.append("")

    lines.append("## Task 3 -- clone and block invariance sanity checks")
    lines.append("")
    lines.append("[T1] Cloning one state with split weights `alpha_b` replaces every cloned column entry by `alpha_b` times the old entry and duplicates the cloned row pattern. Matrix multiplication commutes with this split operation, so `Q^2-Q` clones exactly and its max row `l1` norm is unchanged. Cloning an idempotent candidate `E` gives an idempotent candidate with exactly the same distance.")
    lines.append("")
    lines.append("[T0] Clone example: state 2 of the `s=1/3` Hume-positive-part anchor is split with weights `2/5,3/5`.")
    lines.append("")
    lines.append(f"`eta={fmt(clone_data['eta'])}`, `||Q_clone-E_clone||={fmt(clone_data['dist'])}`, `r^2={fmt(clone_data['r2'])}`, `r={clone_data['rexpr']}`.")
    lines.append("")
    lines.append("Q_clone:")
    lines.append(matrix_md(Qc))
    lines.append("")
    lines.append("E_clone:")
    lines.append(matrix_md(Ec))
    lines.append("")
    lines.append("[T1] For block direct sums, `(Q_1⊕Q_2)^2-(Q_1⊕Q_2)` is the block sum of the two defects, so `eta` is the maximum of the block etas. A block-sum candidate `E_1⊕E_2` is idempotent stochastic and its distance is the maximum of the two block distances. This gives a no-growth construction; it is not a proof about arbitrary cross-block idempotents.")
    lines.append("")
    lines.append("[T0] Block example: `Hume s=1/5` block-summed with `lazy-cycle a=1/10`.")
    lines.append("")
    lines.append(f"`eta={fmt(block_data['eta'])}`, `||Q_block-E_block||={fmt(block_data['dist'])}`, `r^2={fmt(block_data['r2'])}`, `r={block_data['rexpr']}`.")
    lines.append("")
    lines.append("Q_block:")
    lines.append(matrix_md(Qb))
    lines.append("")
    lines.append("E_block:")
    lines.append(matrix_md(Eb))
    lines.append("")

    lines.append("## Task 4 -- one coupled n-growing stochastic family")
    lines.append("")
    lines.append("[T1] Family: levels `0,...,n-1`, state 0 absorbing; for `i>0`, row `i` puts `1-i/(12n)` on state 0 and `1/(12n)` on each level `1,...,i`. This is not a clone or direct sum: increasing `n` changes the coupling pattern of every high-level row and all high levels send mass through a shared lower-level chain. Candidate `E_n` collapses every row to state 0.")
    lines.append("")
    lines.append("[T2] These are constructed-candidate ratios only. They do not lower-bound the true error-bound constant; a larger value could mean the construction is bad, and a bounded value only says this family did not visibly break uniformity.")
    lines.append("")
    lines.append("| n | eta(Q_n) | ||Q_n-E_n|| | r^2 | r |")
    lines.append("|---:|---:|---:|---:|---:|")
    for n, Q, E, data in coupled_rows:
        lines.append(f"| {n} | `{fmt(data['eta'])}` | `{fmt(data['dist'])}` | `{fmt(data['r2'])}` | `{data['rexpr']}` |")
    lines.append("")
    lines.append("[T0] Coupled-family matrices for every reported `n`:")
    for n, Q, E, data in coupled_rows:
        lines.append("")
        lines.append(f"### level-coupled n={n}")
        lines.append("")
        lines.append(f"`eta={fmt(data['eta'])}`, `||Q-E||={fmt(data['dist'])}`, `r^2={fmt(data['r2'])}`, `r={data['rexpr']}`.")
        lines.append("")
        lines.append("Q:")
        lines.append(matrix_md(Q))
        lines.append("")
        lines.append("E:")
        lines.append(matrix_md(E))
    lines.append("")

    lines.append("## Assert list")
    lines.append("")
    lines.append("[T0] The script exits nonzero unless every item below is recomputed from the printed matrices/candidates:")
    lines.append("")
    for item in asserts:
        lines.append(f"- {item}")
    lines.append("")

    lines.append("## Task 5 -- protocol for wave 2")
    lines.append("")
    lines.append("[T2] This pilot saw no obvious dimension blowup. The largest exact ratio came from the stochasticized `ex-hume` anchor, not from the `n`-growing coupled chain. That is consistent with the known sharp `sqrt` mechanism but does not address uniformity.")
    lines.append("")
    lines.append("[T3] A decision-grade kill wave should not spend time on clones or direct sums. It should search genuinely coupled, quotient-many-class families: the `FINDINGS.md` 2026-07-02 web-regime entry says the plausible wall is dimension-many genuine outside quotient classes, and `argument/lemmas/obs-fwr-gap.md` says common-pattern web rigidity cannot give a dimension-free shallow-class count.")
    lines.append("")
    lines.append("[T3] Concrete wave-2 computation: generate exact signed idempotents with `build_from_LambdaC`-style rank-growing webs, convert to stochastic almost-idempotents by a fixed audited projection rule, and for each `n<=8` compute a certified two-sided bracket on `min_E ||Q-E||` using an exact LP/MILP over stochastic-idempotent support structures. For `n=9..12`, keep constructed candidates but add independent lower bounds from quotient/lumping certificates.")
    lines.append("")
    lines.append("[T3] Decision-grade support would be: all quotient-web families tested have true or tightly bracketed ratios bounded by a small constant, with the worst cases collapsing to Hume-like local obstructions. Decision-grade kill would be: a coupled rank-growing family with exact matrices, `eta -> 0`, and certified lower bounds on `min_E ||Q-E||/sqrt(eta)` increasing with `n`, not just a poor constructed `E`.")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
