#!/usr/bin/env python3
"""Exact L3 decider for the five W65 D-cap creative leaves.

This is constructive/numerical evidence, never a proof.  Every numerical
quantity is a fractions.Fraction and every advertised identity is asserted.
The tested D-routed plateau is a near-miss: it gives a definition-level C0
cell, but it is short and is not an I-base datum.  The W55 calculation is a
separate rejection regression for the all-row negativity gate.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Any, Iterable, Sequence

Z, O = F(0), F(1)
CM = F(1, 4)
B_SMALL = CM / 128                 # 1/512
KB = CM * B_SMALL / 64             # 1/131072
ONE_80 = F(1, 80)


def dot(a: Sequence[F], b: Sequence[F]) -> F:
    return sum((x * y for x, y in zip(a, b)), Z)


def add(a: Sequence[F], b: Sequence[F]) -> list[F]:
    return [x + y for x, y in zip(a, b)]


def sub(a: Sequence[F], b: Sequence[F]) -> list[F]:
    return [x - y for x, y in zip(a, b)]


def scale(t: F, a: Sequence[F]) -> list[F]:
    return [t * x for x in a]


def l1(a: Sequence[F], b: Sequence[F] | None = None) -> F:
    if b is None:
        return sum((abs(x) for x in a), Z)
    return sum((abs(x - y) for x, y in zip(a, b)), Z)


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> list[list[F]]:
    bt = list(zip(*b))
    return [[dot(row, col) for col in bt] for row in a]


def convex(weights: Sequence[F], points: Sequence[Sequence[F]]) -> list[F]:
    assert weights and len(weights) == len(points) and sum(weights, Z) == O
    return [sum((weights[i] * points[i][j] for i in range(len(points))), Z)
            for j in range(len(points[0]))]


def neg(row: Sequence[F]) -> F:
    return sum((-x for x in row if x < Z), Z)


def positive(row: Sequence[F]) -> list[F]:
    return [max(x, Z) for x in row]


def delta_of(p: Sequence[Sequence[F]]) -> F:
    return max(neg(row) for row in p)


def identity(n: int) -> list[list[F]]:
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def assert_factorization(L: Sequence[Sequence[F]], Bt: Sequence[Sequence[F]],
                         p: Sequence[Sequence[F]], delta: F | None = None) -> None:
    assert matmul(Bt, L) == identity(len(Bt))
    assert matmul(L, Bt) == [list(row) for row in p]
    assert matmul(p, p) == [list(row) for row in p]
    assert all(sum(row, Z) == O for row in p)
    if delta is not None:
        assert delta_of(p) == delta
        assert all(neg(row) <= delta for row in p)


def qstr(x: Any) -> Any:
    if isinstance(x, F):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, dict):
        return {k: qstr(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [qstr(v) for v in x]
    return x


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def pf(ok: bool) -> str:
    return "PASS" if ok else "FAIL"


def solve_square(a: Sequence[Sequence[F]], b: Sequence[F]) -> list[F] | None:
    """Exact Gaussian elimination; None means singular."""
    n = len(a)
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != Z), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        d = aug[col][col]
        aug[col] = [x / d for x in aug[col]]
        for r in range(n):
            if r == col or aug[r][col] == Z:
                continue
            t = aug[r][col]
            aug[r] = [aug[r][j] - t * aug[col][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def exposedness_margin(coords: Sequence[tuple[F, F]], u: int,
                       far: Iterable[int]) -> F:
    """Solve the 2D affine exposedness LP exactly by vertex enumeration."""
    far_set = set(far)
    if not far_set:
        raise ValueError("the +infinity far-empty edge is not used by this fixture")
    xu, yu = coords[u]
    # Variables are (beta, gamma, margin); h_i=beta*dx+gamma*dy.
    inequalities: list[tuple[list[F], F]] = []
    for i, (x, y) in enumerate(coords):
        dx, dy = x - xu, y - yu
        inequalities.append(([-dx, -dy, Z], Z))       # h_i >= 0
        inequalities.append(([dx, dy, Z], O))         # h_i <= 1
        if i in far_set:
            inequalities.append(([-dx, -dy, O], Z))   # margin <= h_i
    feasible: list[list[F]] = []
    for chosen in itertools.combinations(inequalities, 3):
        sol = solve_square([row for row, _ in chosen], [rhs for _, rhs in chosen])
        if sol is None:
            continue
        if all(dot(row, sol) <= rhs for row, rhs in inequalities):
            feasible.append(sol)
    assert feasible
    return max(sol[2] for sol in feasible)


def cross(o: tuple[F, F], a: tuple[F, F], b: tuple[F, F]) -> F:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull_indices(coords: Sequence[tuple[F, F]]) -> list[int]:
    """Exact strict-vertex convex hull in two dimensions."""
    pts = sorted((p[0], p[1], i) for i, p in enumerate(coords))

    def half(seq: Sequence[tuple[F, F, int]]) -> list[tuple[F, F, int]]:
        out: list[tuple[F, F, int]] = []
        for item in seq:
            while len(out) >= 2 and cross((out[-2][0], out[-2][1]),
                                           (out[-1][0], out[-1][1]),
                                           (item[0], item[1])) <= Z:
                out.pop()
            out.append(item)
        return out

    lower = half(pts)
    upper = half(list(reversed(pts)))
    return [item[2] for item in lower[:-1] + upper[:-1]]


def sup_overflow(mu: Sequence[F], nu: Sequence[F]) -> F:
    """sup_{0<=g<=1} (mu-nu)(g), coordinatewise on singleton fibers."""
    return sum((max(x - y, Z) for x, y in zip(mu, nu)), Z)


def branch_package(mass: F, g: F, A: F, ell: F, tau: F) -> dict[str, Any]:
    """Fix the display first, then apply the exact R1 boundary ownership."""
    cells = {name: Z for name in ("N", "G<4", "C0", "A-esc", "T-esc")}
    if g < tau:
        cell = "N"
    elif A < 4:
        cell = "G<4"
    elif ell < tau / 2:
        cell = "C0"
    else:
        # This fixture never reaches the starvation window.  Residual/tail
        # classification is deliberately not invented.
        raise AssertionError("plateau unexpectedly reached the A/T window")
    cells[cell] = mass
    priority = next(name for name in ("N", "G<4", "C0", "A-esc", "T-esc")
                    if cells[name] >= ONE_80)
    assert priority == cell
    return {"masses": cells, "priority": priority}


def plateau(k: int) -> dict[str, Any]:
    """W63 transient diagonal plateau, now measured in the W65 R1 cells."""
    tau = F(1, k)
    delta = tau * tau
    t0 = tau / 8
    e = 2 * tau
    D0 = 2 + 4 * delta
    e_delta = 2 * delta * (O + delta)
    delta_rt = min(F(1, 2**16), (CM / 4) ** 2, (CM * B_SMALL / 120) ** 2)

    # Exact rank-three factorization.  Coordinates use the basis (u,o,a).
    L = [
        [O, Z, Z],
        [O + delta * (O - t0), delta * t0, -delta],
        [Z, O, Z],
        [Z, Z, O],
        [Z, delta, O - delta],
        [Z, -delta, O + delta],
        [O - e, -e * delta, e * (O + delta)],
    ]
    Bt = [
        [O, Z, Z, Z, Z, Z, Z],
        [Z, Z, O, Z, Z, Z, Z],
        [Z, Z, Z, F(1, 2), F(1, 4), F(1, 4), Z],
    ]
    p = matmul(L, Bt)
    assert_factorization(L, Bt, p, delta)
    labels = ["u", "z", "o", "a", "x", "y", "f_transient"]
    u, zrow, orow, arow, xrow, yrow, frow = range(7)

    coords = [(row[1], row[2]) for row in L]
    vertices = hull_indices(coords)
    assert set(vertices) == {u, zrow, orow, yrow}
    rho, kappa = 4 * tau, tau / 4
    margins: dict[int, F] = {}
    for i in vertices:
        far = [j for j in range(len(p)) if l1(p[j], p[i]) >= rho]
        margins[i] = exposedness_margin(coords, i, far)

    # The canonical optimal exposer at u and its transiently lowered margin.
    hstar = t0 - delta * (O - t0)
    hvals = [Z, Z, O, t0, delta + (O - delta) * t0, hstar, e * hstar]
    assert [dot(row, hvals) for row in p] == hvals
    assert margins[u] == e * hstar < kappa
    visible = [i for i in vertices if margins[i] >= kappa]
    assert set(visible) == {zrow, orow, yrow}
    far_u = [i for i in range(len(p)) if l1(p[i], p[u]) >= rho]
    assert frow in far_u
    assert [i for i in far_u if hvals[i] == e * hstar] == [frow]
    assert [i for i in range(len(p)) if hvals[i] == O] == [orow]
    assert [i for i in range(len(p)) if hvals[i] == Z] == [u, zrow]

    # Exact height certificate: closest point on [z,y] plus a dual support.
    alpha = (O + delta) / (O + 2 * delta)
    closest = convex([alpha, O - alpha], [p[zrow], p[yrow]])
    H = l1(p[u], closest)
    r = (O - 2 * delta * t0) / (O + 2 * delta)
    dual = [O, Z, -O, r, r, r, Z]
    constant = -dot(dual, p[zrow])
    phi = [dot(dual, row) + constant for row in p]
    assert max(abs(x) for x in dual) == O
    assert phi[u] == H and all(phi[i] <= Z for i in visible)
    # a and x are in conv{o,y}; f is on [u,y], so u is the top.
    assert p[arow] == convex([delta / (O + delta), O / (O + delta)],
                             [p[orow], p[yrow]])
    assert p[xrow] == convex([delta, O - delta], [p[orow], p[arow]])
    assert p[frow] == convex([O - e, e], [p[u], p[yrow]])
    assert H < tau / 4 and H < 16 * tau

    # Attempted I-base selection A={u}: S and q_A are exact, but the selected
    # row is not rho-far.  This gives a defined true ray diagnostic without
    # pretending that the I-base selection is legal.
    selected_A = [u]
    S = p[u][u]
    qA = p[u]
    assert S == O and l1(p[u], p[u]) < rho
    G_mass = Z                         # P_u^+ is supported only at u, not G_v
    shallow_ext_sup = Z               # H-8*tau<0, hence Sh_v is empty
    all_center_floor = tau * S / 16
    assert H - 8 * tau < Z
    assert shallow_ext_sup < all_center_floor
    assert G_mass < all_center_floor
    theta = Z                          # d_u=H is above the rim's upper edge
    assert theta < tau / D0

    # True ray value via lem-l5-top-face-ray-formula.  q_A=p_u makes the
    # dual objective identically zero; Lambda=0 attains the ray minimum.
    ray_lambda = Z
    ray_obj = l1(sub(p[u], qA))
    ray_dual = Z
    assert ray_obj == ray_dual == Z

    # Definition-level selected D corner at f*.  B_N retains (u,u).
    assert l1(p[frow], p[u]) == 4 * tau * (O + delta) >= rho
    z_f = H - phi[frow]
    score = 2 * z_f / D0
    assert Z <= z_f < 4 * tau and score <= 12 * tau / 13
    eta_mass = O - e
    MX = MI = Z
    MD = eta_mass
    assert MX <= F(1, 8) and MI < F(1, 16) and MD > F(1, 16)

    # Fixed reduced optimal display.  The algebra above forces T={f}, O={o},
    # Z={z} on the whole optimal face; no display is selected after routing.
    kT = sub(p[frow], p[u])
    kO = scale(e * hstar, sub(p[orow], p[u]))
    A = e * (O + delta) / delta
    q = p[zrow]
    ell = l1(q, p[u])
    g = l1(kT, kO)
    assert add(kT, scale(A, sub(q, p[u]))) == kO
    assert ell == 2 * delta
    assert g == A * ell == 4 * tau * (O + delta)
    r1 = branch_package(eta_mass, g, A, ell, tau)
    assert r1["priority"] == "C0"

    # R0 receiver cap at f*: Pi_D*=eta(u)P_u^+.
    Pi_root = scale(eta_mass, positive(p[u]))
    Pf_plus = positive(p[frow])
    r0_overflow = sup_overflow(Pi_root, Pf_plus)
    assert r0_overflow == Z <= e_delta

    # Mandatory tall packet diagnostics.  P_u^+ is the point mass at u.
    Pv_L = O
    ell_T = delta + (4 * tau / 63) * (D0 + tau / 4)
    assert not (Pv_L < ell_T)
    assert ell_T < 2 * tau / 15
    Pv_E = Z
    assert l1(p[u], p[frow]) < F(1, 2)
    exterior_floor = tau * S / 8
    assert Pv_E < exterior_floor

    # A definition-level BD overlay is fixed independently: beta_D=delta_u.
    # It has the corrected intrinsic U_D lift and exactly the D_gap label.
    beta_mass = O
    Pi_overlay = positive(p[u])
    overlay_overflow = sup_overflow(Pi_overlay, positive(p[u]))
    b5_error = (2 + delta) * e_delta
    outer_overlap = Z                  # d_u=H<tau/4
    x_far = x_near = i_far = i_near = d_near = Z
    d_gap = O
    tx = CM / 1024
    tid = CM / 3072
    label_truth = {
        "X_gap": x_far >= tx,
        "X_near": x_far < tx and x_near > tx,
        "I_far": i_far >= tid,
        "I_near": i_far < tid and i_near > tid,
        "D_gap": d_gap >= tid,
        "D_near": d_gap < tid and d_near > tid,
    }
    active_labels = [name for name, truth in label_truth.items() if truth]
    assert active_labels == ["D_gap"]
    assert beta_mass > CM / 768 and overlay_overflow <= b5_error
    assert not (outer_overlap > CM / 1024)

    leaf_deficit = ray_obj - CM * tau / 64 + (CM / 16) * Pv_L
    assert leaf_deficit > Z

    gate = {
        "P=LB_and_BL=I": True,
        "delta=tau^2_and_all_row_negativity<=delta": True,
        "nonempty_visible_set": bool(visible),
        "hidden_top": margins[u] < kappa,
        "tall_H>16tau": H > 16 * tau,
        "selected_A_is_far_and_deep": False,
        "S>=1/4": S >= CM,
        "all_center_shallow": shallow_ext_sup < all_center_floor,
        "all_center_far_G": G_mass >= all_center_floor,
        "omega_nonempty": False,
        "ultra_drift": False,
        "ultra_width": False,
        "theta<tau/D0": theta < tau / D0,
        "delta<=delta_rt": delta <= delta_rt,
        "fixed_D_certificate": MD > F(1, 16) and MX <= F(1, 8) and MI < F(1, 16),
        "Z/tau_to_zero_diagnostic": ray_obj / tau == Z,
        "leaf_deficit<0": leaf_deficit < Z,
    }
    genuine = all(gate.values())
    assert not genuine

    panel = {
        "m_D_star": MD,
        "m_D_star_threshold": F(1, 16),
        "m_D_star_pass": MD > F(1, 16),
        "R0_sup_overflow": r0_overflow,
        "R0_e_delta": e_delta,
        "R0_pass": r0_overflow <= e_delta,
        "P_v_plus_L_v": Pv_L,
        "ell_T": ell_T,
        "two_tau_over_15": 2 * tau / 15,
        "shallow_chain_pass": Pv_L < ell_T < 2 * tau / 15,
        "P_v_plus_E_star": Pv_E,
        "tau_S_over_8": exterior_floor,
        "exterior_pass": Pv_E >= exterior_floor,
        "B5_route": "BD-definition-level; theorem antecedent fails",
        "B5_1_beta_mass": beta_mass,
        "B5_1_beta_threshold": CM / 768,
        "B5_1_overflow": overlay_overflow,
        "B5_1_error": b5_error,
        "B5_1_pass": beta_mass > CM / 768 and overlay_overflow <= b5_error,
        "B5_2_outer_overlap": outer_overlap,
        "B5_2_threshold": CM / 1024,
        "B5_2_pass": outer_overlap > CM / 1024,
        "B5_3_X_far_mass": x_far,
        "B5_3_X_near_mass": x_near,
        "B5_3_X_threshold": tx,
        "B5_3_I_far_mass": i_far,
        "B5_3_I_near_mass": i_near,
        "B5_3_D_gap_mass": d_gap,
        "B5_3_D_near_mass": d_near,
        "B5_3_ID_threshold": tid,
        "B5_label_truth": label_truth,
        "B5_active_label": active_labels[0],
        "B5_exactly_one": len(active_labels) == 1,
        "Z_v_q_A": ray_obj,
        "Z_over_tau": ray_obj / tau,
        "leaf_deficit": leaf_deficit,
        "leaf_deficit_negative": leaf_deficit < Z,
    }

    return {
        "id": f"w63_diagonal_plateau_k{k}",
        "classification": "definition-level C0 by-catch; rejected before genuine D-cap",
        "warning": "L3 evidence only; this is not a proof or a genuine I-base datum",
        "labels": labels,
        "L": L,
        "B_left_inverse": Bt,
        "matrix": p,
        "parameters": {"k": k, "tau": tau, "delta": delta, "c_m": CM,
                       "b": B_SMALL, "k_b": KB, "D0": D0,
                       "delta_rt": delta_rt, "e_delta": e_delta},
        "row_negative_masses": [neg(row) for row in p],
        "geometry": {
            "factor_coordinates_xy": coords,
            "vertex_indices": vertices,
            "visible_indices": visible,
            "visible_labels": [labels[i] for i in visible],
            "exposedness_margins": {labels[i]: margins[i] for i in vertices},
            "hidden_top": "u", "H": H, "H_over_tau": H / tau,
            "H_minus_16tau": H - 16 * tau, "closest": closest,
            "top_dual": dual, "top_constant": constant, "phi_values": phi,
        },
        "attempted_I_base": {
            "selected_A": [labels[i] for i in selected_A], "S": S, "q_A": qA,
            "selected_far_failure_distance": l1(p[u], p[u]), "rho": rho,
            "all_center_shallow_sup": shallow_ext_sup,
            "all_center_far_G_inf": G_mass,
            "all_center_threshold": all_center_floor,
            "omega_mass": G_mass, "r_omega": None, "Omega": None,
            "theta": theta, "theta_threshold": tau / D0,
        },
        "ray": {"Z": ray_obj, "Z_over_tau": ray_obj / tau,
                "Lambda": ray_lambda, "dual_lower": ray_dual,
                "formula_note": "q_A=p_u, so Lambda=0 and the dual objective are both exactly zero"},
        "fixed_local_D_certificate": {
            "phi": phi, "h_values": [Z] * len(p), "f_star": labels[frow],
            "eta": {"(u,u)": eta_mass}, "M_X": MX, "M_I": MI, "M_D": MD,
            "public_extraction_available": False,
            "failure": "H>16*tau and the I-base antecedent fail",
        },
        "fixed_reduced_display": {
            "fixed_before_classification": True,
            "T": [labels[frow]], "O": [labels[orow]], "Z": [labels[zrow]],
            "t_star": e * hstar, "h_values": hvals,
            "k_T": kT, "k_O": kO, "A": A, "q": q, "ell": ell, "g": g,
            "g_over_tau": g / tau, "ell_over_tau": ell / tau,
            "display_residual": sub(add(kT, scale(A, sub(q, p[u]))), kO),
        },
        "R1": r1,
        "gate": gate,
        "genuine_candidate": genuine,
        "panel": panel,
    }


def w55_unit() -> dict[str, Any]:
    """Canonical W55 A0=5 completion: exact rejection by finance negativity."""
    tau, target_delta, A = F(1, 256), F(1, 65536), F(5)
    a = tau / (O + tau)
    L = [
        [O, Z, Z],
        [O + A * a - a * target_delta, -A * a, a * target_delta],
        [O + A - target_delta, -A, target_delta],
        [Z, O, Z],
        [Z, Z, O],
    ]
    Bt = [
        [O - tau, tau + target_delta, -target_delta, Z, Z],
        [Z, Z, Z, O, Z],
        [Z, Z, Z, Z, O],
    ]
    p = matmul(L, Bt)
    assert_factorization(L, Bt, p)
    nus = [neg(row) for row in p]
    finance = A + (O + A - target_delta) * target_delta
    assert nus[2] == finance == delta_of(p)
    assert finance == F(21475229695, 4294967296)
    assert finance > target_delta

    # Exact local T-escape-shaped scaffold, deliberately not classified as a
    # D-cap candidate because delta(P) is finance, not target_delta=tau^2.
    v, w, frow, zrow, orow = range(5)
    dz = sub(p[zrow], p[v])
    df = sub(p[frow], p[v])
    do = sub(p[orow], p[v])
    assert add(df, scale(A, dz)) == scale(target_delta, do)
    ell = l1(dz)
    g = A * ell
    assert ell > 2 * tau
    qtilde = add(p[v], scale(2 * tau / ell, dz))
    Atilde = A * ell / (2 * tau)
    assert scale(Atilde, sub(qtilde, p[v])) == scale(A, dz)
    actor_residual = l1(add(df, scale(Atilde, sub(qtilde, p[v]))))
    assert actor_residual == target_delta * l1(do) <= 3 * target_delta
    signs = [F(1 if x > 0 else -1 if x < 0 else 0) for x in dz]
    chi = [dot(signs, sub(row, p[v])) / (2 * tau) for row in p]
    tail = sum((max(p[v][j], Z) for j in range(len(p)) if abs(chi[j]) > O), Z)
    assert tail > target_delta

    return {
        "id": "w55_A0_5_finance_negativity_unit",
        "labels": ["v", "w", "f", "z", "o"],
        "L": L, "B_left_inverse": Bt, "matrix": p,
        "parameters": {"tau": tau, "target_delta=tau^2": target_delta, "A0": A},
        "row_negative_masses": nus, "actual_delta": finance,
        "finance_nu": finance, "excess_over_tau2": finance - target_delta,
        "local_T_escape_shape_only": {
            "ell": ell, "g": g, "q_tilde": qtilde, "A_tilde": Atilde,
            "actor_residual": actor_residual, "3delta_target": 3 * target_delta,
            "chi_values": chi, "Tail_1": tail, "Tail_1_minus_delta_target": tail - target_delta,
        },
        "classification": "REJECTED: actual delta is order one, not tau^2",
    }


def print_panel(c: dict[str, Any]) -> None:
    p = c["panel"]
    display = c["fixed_reduced_display"]
    masses = c["R1"]["masses"]
    print(f"PANEL {c['id']}")
    print(f"  m_D*={fstr(p['m_D_star'])} > 1/16: {pf(p['m_D_star_pass'])}")
    print("  sup(Pi_D*-P_f*+)="
          f"{fstr(p['R0_sup_overflow'])} <= e_delta={fstr(p['R0_e_delta'])}: {pf(p['R0_pass'])}")
    print("  P_v+(L_v)="
          f"{fstr(p['P_v_plus_L_v'])} < ell_T={fstr(p['ell_T'])} < "
          f"2tau/15={fstr(p['two_tau_over_15'])}: {pf(p['shallow_chain_pass'])}")
    print("  P_v+(E*)="
          f"{fstr(p['P_v_plus_E_star'])} >= tau*S/8={fstr(p['tau_S_over_8'])}: "
          f"{pf(p['exterior_pass'])}")
    print(f"  B5 route={p['B5_route']}")
    print("  B5.1 beta_D(1)="
          f"{fstr(p['B5_1_beta_mass'])} > {fstr(p['B5_1_beta_threshold'])}; "
          f"overflow={fstr(p['B5_1_overflow'])} <= {fstr(p['B5_1_error'])}: {pf(p['B5_1_pass'])}")
    print("  B5.2 outer-overlap="
          f"{fstr(p['B5_2_outer_overlap'])} > {fstr(p['B5_2_threshold'])}: {pf(p['B5_2_pass'])}")
    print("  B5.3 X_gap: far="
          f"{fstr(p['B5_3_X_far_mass'])} >= {fstr(p['B5_3_X_threshold'])}: "
          f"{pf(p['B5_label_truth']['X_gap'])}")
    print("  B5.3 X_near: far<"
          f"{fstr(p['B5_3_X_threshold'])}, near={fstr(p['B5_3_X_near_mass'])}>"
          f"{fstr(p['B5_3_X_threshold'])}: {pf(p['B5_label_truth']['X_near'])}")
    print("  B5.3 I_far: far="
          f"{fstr(p['B5_3_I_far_mass'])} >= {fstr(p['B5_3_ID_threshold'])}: "
          f"{pf(p['B5_label_truth']['I_far'])}")
    print("  B5.3 I_near: far<"
          f"{fstr(p['B5_3_ID_threshold'])}, near={fstr(p['B5_3_I_near_mass'])}>"
          f"{fstr(p['B5_3_ID_threshold'])}: {pf(p['B5_label_truth']['I_near'])}")
    print("  B5.3 D_gap: gap="
          f"{fstr(p['B5_3_D_gap_mass'])} >= c_m/3072={fstr(p['B5_3_ID_threshold'])}: "
          f"{pf(p['B5_label_truth']['D_gap'])}")
    print("  B5.3 D_near: gap<"
          f"c_m/3072={fstr(p['B5_3_ID_threshold'])}, near={fstr(p['B5_3_D_near_mass'])}>"
          f"{fstr(p['B5_3_ID_threshold'])}: {pf(p['B5_label_truth']['D_near'])}")
    print(f"  B5 active={p['B5_active_label']}; exactly one: {pf(p['B5_exactly_one'])}")
    print("  fixed display: g/tau="
          f"{fstr(display['g_over_tau'])}, A={fstr(display['A'])}, "
          f"ell/tau={fstr(display['ell_over_tau'])}")
    print("  R1 masses: N="
          f"{fstr(masses['N'])}, G<4={fstr(masses['G<4'])}, C0={fstr(masses['C0'])}, "
          f"A-esc={fstr(masses['A-esc'])}, T-esc={fstr(masses['T-esc'])}; "
          f"priority={c['R1']['priority']}")
    print("  D_leaf=Z-c_m*tau/64+(c_m/16)P_v+(L_v)="
          f"{fstr(p['leaf_deficit'])} < 0: {pf(p['leaf_deficit_negative'])}")


def build() -> dict[str, Any]:
    # These samples lie below the pinned routine ceiling and form an exact
    # parametric tau=1/k calibration.  None is a genuine candidate.
    ks = [262144, 524288, 1048576]
    candidates = [plateau(k) for k in ks]
    assert all(c["parameters"]["delta"] <= c["parameters"]["delta_rt"] for c in candidates)
    assert all(not c["genuine_candidate"] for c in candidates)

    # Mandatory regressions.
    w63 = plateau(2048)
    assert w63["fixed_local_D_certificate"]["M_I"] == Z
    assert w63["fixed_local_D_certificate"]["M_D"] == F(1023, 1024)
    assert w63["R1"]["priority"] == "C0"
    assert not w63["gate"]["tall_H>16tau"]
    w55 = w55_unit()

    best_id = candidates[-1]["id"]
    leaves = {
        "N": {
            "verdict": "BLOCKED", "best_near_miss": best_id,
            "binding": "eta_D*(N)=0; g-tau=3*tau+4*tau^3>0, and H-16*tau<0",
        },
        "G<4": {
            "verdict": "BLOCKED", "best_near_miss": best_id,
            "binding": "eta_D*(G<4)=0; A-4=2/tau+2*tau-4>0, and H-16*tau<0",
        },
        "C0": {
            "verdict": "PARTIAL", "best_near_miss": best_id,
            "binding": "local C0 mass is 1-2*tau, but selected A is not far, omega is empty, and H-16*tau<0",
        },
        "A-esc": {
            "verdict": "BLOCKED", "best_near_miss": best_id,
            "binding": "ell-tau/2=2*tau^2-tau/2<0, so the tested D mass routes earlier to C0; no growing-rank tall completion",
        },
        "T-esc": {
            "verdict": "BLOCKED", "best_near_miss": best_id,
            "binding": "plateau routes to C0; W55 has residual<=3*tau^2 and Tail_1>tau^2 only at finance negativity nu_f>>tau^2",
            "auxiliary": w55["id"],
        },
    }

    return {
        "schema": "w66-dcap-five-leaf-exact-l3-v1",
        "arithmetic": "fractions.Fraction; JSON rationals are exact numerator/denominator strings",
        "warning": "L3 constructive/numerical evidence only; never a proof",
        "constants": {"c_m": CM, "b": B_SMALL, "k_b": KB},
        "candidate_family": {
            "description": "W63 transient diagonal plateau at tau=1/k",
            "parametric_distribution": {
                "mass": "1-2*tau", "g/tau": "4*(1+tau^2)",
                "A": "2*(1+tau^2)/tau", "ell/tau": "2*tau",
                "R1_cell": "C0",
            },
            "members": candidates,
        },
        "leaves": leaves,
        "unit_tests": {"W63_diagonal_plateau": w63, "W55_A0_5": w55},
        "genuine_I_base_count": 0,
        "genuine_refuter_count": 0,
        "bycatch": "definition-level C0 entrant on mass 1-2*tau; not a leaf-hypothesis entrant",
    }


def main() -> None:
    data = build()
    Path("certificates.json").write_text(json.dumps(qstr(data), indent=2) + "\n")
    for candidate in data["candidate_family"]["members"]:
        print_panel(candidate)
    w63 = data["unit_tests"]["W63_diagonal_plateau"]
    print("UNIT W63 diagonal plateau: PASS — corner routes to D with M_I="
          f"{fstr(w63['fixed_local_D_certificate']['M_I'])}, M_D="
          f"{fstr(w63['fixed_local_D_certificate']['M_D'])}; W65 R1=C0; H>16tau=FAIL(expected).")
    w55 = data["unit_tests"]["W55_A0_5"]
    print("UNIT W55 A0=5: PASS — nu_f="
          f"{fstr(w55['finance_nu'])} > tau^2={fstr(w55['parameters']['target_delta=tau^2'])}; "
          "rejected, not a refuter.")
    print("N: BLOCKED — N mass is 0; the tested D plateau has g/tau=4*(1+tau^2) and is short.")
    print("G<4: BLOCKED — low-gauge mass is 0; A=2*(1+tau^2)/tau>4 and tallness fails.")
    print("C0: PARTIAL — exact local C0 mass 1-2*tau is realized, but no I-base datum or tall top is realized.")
    print("A-esc: BLOCKED — the tested mass has ell/tau=2*tau<1/2 and routes to C0; no tall growing-rank completion was found.")
    print("T-esc: BLOCKED — W55 has the residual/tail shape only with order-one finance negativity; the legal plateau routes to C0.")
    print("SUMMARY: exact checks passed; 0 genuine I-base data and 0 genuine refuters; L3 evidence only, never a proof.")


if __name__ == "__main__":
    main()
