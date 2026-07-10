#!/usr/bin/env python3
"""Exact-rational W61 leak-financing search/certificate generator.

This is an L3 construction script, not a proof.  It builds a dyadic family of
exact signed idempotents by deforming the banked thin-zero-face fixture with a
signed clone split and a transient hull row.  All asserted identities use
fractions.Fraction; floats are emitted only as human-readable diagnostics.

Default rerun:
    PYTHONDONTWRITEBYTECODE=1 python3 search.py
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parent
CERTIFICATE_PATH = ROOT / "certificates.json"
LABELS = ("a0", "a1", "z", "c", "d", "x")
POINTS = ("A", "Z", "C", "D", "X")
CORNER_FLOOR = F(58079731, 109051904)


def qstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qfloat(x: F) -> float:
    return float(x)


def qrecord(x: F) -> Dict[str, object]:
    return {"exact": qstr(x), "decimal": qfloat(x)}


def dot(a: Sequence[F], b: Sequence[F]) -> F:
    assert len(a) == len(b)
    return sum((x * y for x, y in zip(a, b)), F(0))


def add(*vectors: Sequence[F]) -> Tuple[F, ...]:
    assert vectors
    n = len(vectors[0])
    assert all(len(v) == n for v in vectors)
    return tuple(sum((v[j] for v in vectors), F(0)) for j in range(n))


def scale(a: F, v: Sequence[F]) -> Tuple[F, ...]:
    return tuple(a * x for x in v)


def sub(a: Sequence[F], b: Sequence[F]) -> Tuple[F, ...]:
    return tuple(x - y for x, y in zip(a, b))


def l1(v: Sequence[F]) -> F:
    return sum((abs(x) for x in v), F(0))


def dist(a: Sequence[F], b: Sequence[F]) -> F:
    return l1(sub(a, b))


def matmul(a: Sequence[Sequence[F]], b: Sequence[Sequence[F]]) -> List[List[F]]:
    assert a and b and len(a[0]) == len(b)
    bt = list(zip(*b))
    return [[dot(row, col) for col in bt] for row in a]


def neg_mass(row: Sequence[F]) -> F:
    return sum((-x for x in row if x < 0), F(0))


def pos_mass(row: Sequence[F], indices: Iterable[int] | None = None) -> F:
    js = range(len(row)) if indices is None else indices
    return sum((max(row[j], F(0)) for j in js), F(0))


def affine(coeff: Sequence[F], constant: F, point: Sequence[F]) -> F:
    return dot(coeff, point) + constant


def full_fibers(p: Sequence[Sequence[F]]) -> List[Tuple[int, ...]]:
    buckets: Dict[Tuple[F, ...], List[int]] = {}
    for j, row in enumerate(p):
        buckets.setdefault(tuple(row), []).append(j)
    return [tuple(js) for js in buckets.values()]


def point_name(row: Sequence[F], representatives: Mapping[str, Sequence[F]]) -> str:
    matches = [name for name, value in representatives.items() if tuple(row) == tuple(value)]
    assert len(matches) == 1, matches
    return matches[0]


def ledger_entry(
    actual: F,
    cap: F,
    relation: str,
    *,
    applicable: bool = True,
    note: str = "",
) -> Dict[str, object]:
    if relation == "<=":
        assert actual <= cap
        slack = cap - actual
    elif relation == ">=":
        assert actual >= cap
        slack = actual - cap
    elif relation == "=":
        assert actual == cap
        slack = F(0)
    elif relation == "<":
        assert actual < cap
        slack = cap - actual
    else:
        raise AssertionError(relation)
    return {
        "applicable": applicable,
        "actual": qstr(actual),
        "relation": relation,
        "bound": qstr(cap),
        "slack": qstr(slack),
        "note": note,
    }


def eval_values(
    coeff: Sequence[F], constant: F, representatives: Mapping[str, Sequence[F]]
) -> Dict[str, F]:
    return {name: affine(coeff, constant, row) for name, row in representatives.items()}


def build_candidate(k: int) -> Dict[str, object]:
    """Build and completely audit the tau=2^-k member of the family."""

    assert k >= 8
    tau = F(1, 2**k)
    delta = tau * tau
    eps = delta / 2
    t = tau / 8
    kappa = tau / 4
    rho = 4 * tau
    diameter = 2 + 4 * delta

    # Thin-zero-face fixture parameters, followed by a signed split of the A
    # column.  q=eps/K makes row Z's two negative entries total exactly delta.
    K = 1 + eps * (1 - t)
    q = eps / K
    w = 1 + q
    theta = tau / (4 * (1 + q))

    zero = F(0)
    one = F(1)
    A = (w, -q, zero, zero, zero, zero)
    Z = (K * w, -K * q, zero, t * eps, -eps, zero)
    C = (zero, zero, zero, one, zero, zero)
    D = (zero, zero, zero, zero, one, zero)
    X = ((1 - theta) * w, -(1 - theta) * q, zero, theta, zero, zero)
    P: List[List[F]] = [list(A), list(A), list(Z), list(C), list(D), list(X)]
    reps: Dict[str, Tuple[F, ...]] = {"A": A, "Z": Z, "C": C, "D": D, "X": X}

    # Core signed-idempotent and factorization identities.
    assert all(sum(row, F(0)) == 1 for row in P)
    assert matmul(P, P) == P
    assert tuple(Z) == add(scale(K, A), scale(t * eps, C), scale(-eps, D))
    assert tuple(X) == add(scale(1 - theta, A), scale(theta, C))
    nus = [neg_mass(row) for row in P]
    assert nus == [q, q, delta, F(0), F(0), (1 - theta) * q]
    assert max(nus) == delta
    assert delta <= F(1, 2**16)
    assert tau * tau == delta

    fibers = full_fibers(P)
    assert fibers == [(0, 1), (2,), (3,), (4,), (5,)]
    fiber_names = [point_name(P[js[0]], reps) for js in fibers]
    assert fiber_names == ["A", "Z", "C", "D", "X"]

    # The A vertex is hidden.  The displayed primal exposer and dual witness
    # meet at t*=t; the witness is the exact small-beta banked form.
    h_coeff = (zero, zero, zero, one, t, zero)
    h_values = eval_values(h_coeff, zero, reps)
    assert h_values == {"A": 0, "Z": 0, "C": 1, "D": t, "X": theta}
    assert all(0 <= value <= 1 for value in h_values.values())

    far_A = {name for name, row in reps.items() if dist(row, A) >= rho}
    assert far_A == {"C", "D"}
    assert min(h_values[name] for name in far_A) == t

    witness_balance = add(sub(D, A), scale(1 / eps, sub(Z, A)))
    witness_rhs = scale(t, sub(C, A))
    assert witness_balance == witness_rhs
    assert t < kappa

    # Exact visible-set audit.  Strict admissible exposers show Z,C,D are
    # vertices and visible.  X is a strict A/C hull point.  A is a vertex via
    # the top support below and is hidden by the primal/dual equality above.
    exposers: Dict[str, Dict[str, F]] = {
        "Z": {
            "A": (1 - t) * q,
            "Z": 0,
            "C": 1,
            "D": 1,
            "X": (1 - theta) * (1 - t) * q + theta,
        },
        "C": {"A": 1, "Z": 1 - t * eps, "C": 0, "D": 1, "X": 1 - theta},
        "D": {
            "A": (1 - t * eps) / K,
            "Z": 1,
            "C": 1,
            "D": 0,
            "X": (1 - theta) * (1 - t * eps) / K + theta,
        },
    }
    visible_margins: Dict[str, F] = {}
    for base, values in exposers.items():
        assert values[base] == 0
        assert all(0 <= value <= 1 for value in values.values())
        assert all(values[name] > 0 for name in POINTS if name != base)
        # Affine compatibility with the two defining row relations.  Since
        # A,C,D are affinely independent, these checks certify that the value
        # table is induced by an affine functional on the whole row hull.
        assert values["Z"] == K * values["A"] + t * eps * values["C"] - eps * values["D"]
        assert values["X"] == (1 - theta) * values["A"] + theta * values["C"]
        far = {name for name, row in reps.items() if dist(row, reps[base]) >= rho}
        assert far
        margin = min(values[name] for name in far)
        assert margin >= kappa
        visible_margins[base] = margin
    assert 0 < theta < 1

    # Top support at A relative to W={Z,C,D}.  The closest point is on ZD;
    # the coefficient infinity norm is exactly one, certifying the distance.
    H = 2 * t * q
    phi_coeff = (one, 1 - 2 * t, zero, -one, one, zero)
    phi_constant = -one
    assert max(abs(x) for x in phi_coeff) == 1
    phi_values = eval_values(phi_coeff, phi_constant, reps)
    assert phi_values == {
        "A": H,
        "Z": 0,
        "C": -2,
        "D": 0,
        "X": (1 - theta) * H - 2 * theta,
    }
    assert all(phi_values[name] <= 0 for name in ("Z", "C", "D"))

    closest = add(scale(1 / K, Z), scale(1 - 1 / K, D))
    assert dist(A, closest) == H
    assert affine(phi_coeff, phi_constant, A) - affine(phi_coeff, phi_constant, closest) == H

    x_weights = {
        "Z": (1 - theta) / K,
        "C": theta - (1 - theta) * t * q,
        "D": (1 - theta) * q,
    }
    assert all(value >= 0 for value in x_weights.values())
    assert sum(x_weights.values(), F(0)) == 1
    assert X == add(*(scale(x_weights[name], reps[name]) for name in ("Z", "C", "D")))
    assert phi_values["X"] <= 0
    visible_set = ("Z", "C", "D")
    hidden_set = ("A",)

    # Top deficits and selected-corner local geometry.
    z_values = {name: H - value for name, value in phi_values.items()}
    assert all(value >= 0 for value in z_values.values())
    assert z_values["C"] == H + 2
    assert z_values["X"] == theta * (H + 2)
    assert z_values["X"] < 4 * tau
    assert h_values["X"] < 4 * tau
    assert H < 4 * tau

    # The N5(ii) pair: carrier u=A=v and freight x=X.
    r, s = 5, 0
    separation = dist(P[r], P[s])
    assert separation == tau / 2
    assert tau / 4 < separation <= 8 * tau
    assert dist(A, A) < rho
    assert X != A

    # Exact financing-floor instantiation.  Because A is a two-index full
    # fiber, l_chi=2*theta is strictly smaller than the ambient separation.
    pair_difference = sub(P[r], P[s])
    psi_coeff = tuple(F(0) if value == 0 else F(1 if value > 0 else -1, 1) / separation
                      for value in pair_difference)
    psi_constant = -dot(psi_coeff, P[s])
    psi_values = eval_values(psi_coeff, psi_constant, reps)
    assert psi_values["A"] == 0
    assert psi_values["X"] == 1
    assert psi_values["C"] == 1 / theta
    assert abs(psi_values["Z"]) < 1
    assert 0 < psi_values["D"] < psi_values["C"]
    assert psi_values["X"] - psi_values["A"] == 1

    d_by_fiber: Dict[str, F] = {}
    for name, js in zip(fiber_names, fibers):
        d_by_fiber[name] = sum((P[r][j] - P[s][j] for j in js), F(0))
    assert d_by_fiber == {"A": -theta, "Z": 0, "C": theta, "D": 0, "X": 0}
    l_chi = sum((abs(value) for value in d_by_fiber.values()), F(0))
    assert l_chi == 2 * theta
    assert l_chi < separation

    N = ("A", "Z", "X")
    high = ("C", "D")
    A_parameter = F(1)
    Lambda = 1 / theta
    assert max(abs(psi_values[name]) for name in N) == A_parameter
    assert max(abs(psi_values[name]) for name in high) == Lambda

    actual_high_r = sum(
        pos_mass(P[r], fibers[fiber_names.index(name)]) for name in high
    )
    actual_high_s = sum(
        pos_mass(P[s], fibers[fiber_names.index(name)]) for name in high
    )
    assert actual_high_r == theta
    assert actual_high_s == 0
    actual_high = actual_high_r + actual_high_s
    demand = (1 - A_parameter * l_chi) / Lambda - nus[r] - nus[s]
    assert demand == theta * (1 - 2 * theta) - (2 - theta) * q
    assert demand > 0
    assert actual_high >= demand
    assert actual_high - demand == 2 * theta * theta + (2 - theta) * q

    # Both high observables detect exactly C at threshold 4*tau, and every
    # unit of pair financing is the X-row's positive C coefficient.
    z_high = tuple(name for name in POINTS if z_values[name] >= 4 * tau)
    h_high = tuple(name for name in POINTS if h_values[name] >= 4 * tau)
    assert z_high == ("C",)
    assert h_high == ("C",)
    assert actual_high == P[r][3] == theta

    # Corner-row f=D: all its positive mass stays in the numerical corner.
    # The actual corner-ledger contract is NOT applicable because H<16*tau;
    # this audit records both that failed hypothesis and the conclusion's
    # numerical slack without claiming an invocation.
    f = 4
    f_score = 2 * z_values["D"] / diameter + h_values["D"]
    assert dist(D, A) >= rho
    assert F(0) > H - 4 * tau  # d_f=0 since D is visible.
    assert f_score <= 12 * tau / 13

    # Legal vertex kernel: Dirac on A,Z,C,D; X=(1-theta)A+theta*C.
    xi: Dict[str, Dict[str, F]] = {
        "A": {"A": 1},
        "Z": {"Z": 1},
        "C": {"C": 1},
        "D": {"D": 1},
        "X": {"A": 1 - theta, "C": theta},
    }
    for name, weights in xi.items():
        assert sum(weights.values(), F(0)) == 1
        assert reps[name] == add(*(scale(value, reps[vertex]) for vertex, value in weights.items()))

    corner_points = tuple(
        name for name in POINTS if z_values[name] < 4 * tau and h_values[name] < 4 * tau
    )
    assert corner_points == ("A", "Z", "D", "X")
    gamma: Dict[Tuple[str, str], F] = {}
    for name, js in zip(fiber_names, fibers):
        pfx = pos_mass(P[f], js)
        for vertex, weight in xi[name].items():
            gamma[(name, vertex)] = pfx * weight
    gamma_total = sum(gamma.values(), F(0))
    gamma_corner = sum(
        value for (name, vertex), value in gamma.items()
        if name in corner_points and vertex in corner_points
    )
    assert gamma_total == 1 + nus[f] == 1
    assert gamma_corner == 1
    gamma_BF = sum(
        value for (name, vertex), value in gamma.items()
        if name in corner_points and vertex in corner_points and dist(reps[vertex], A) >= rho
    )
    gamma_BN = gamma_corner - gamma_BF
    gamma_MX_BF = sum(
        value for (name, vertex), value in gamma.items()
        if name in corner_points and vertex in corner_points
        and dist(reps[vertex], A) >= rho and reps[name] != reps[vertex]
    )
    gamma_MX_BN = sum(
        value for (name, vertex), value in gamma.items()
        if name in corner_points and vertex in corner_points
        and dist(reps[vertex], A) < rho and reps[name] != reps[vertex]
    )
    assert gamma_BF == 1
    assert gamma_BN == 0
    assert gamma_MX_BF == gamma_MX_BN == 0
    assert ("X", "A") in gamma and gamma[("X", "A")] == 0

    # Per-ledger accounting.  Exact top-deficit and h-leak masses at v=A are
    # zero, while their caps are strictly positive because nu_v=q>0.
    v_z_weighted = sum(
        max(P[s][j], F(0)) * z_values[point_name(P[j], reps)] for j in range(len(P))
    )
    v_z_high_mass = sum(
        max(P[s][j], F(0)) for j in range(len(P))
        if point_name(P[j], reps) in z_high
    )
    v_h_high_mass = sum(
        max(P[s][j], F(0)) for j in range(len(P))
        if point_name(P[j], reps) in h_high
    )
    assert v_z_weighted == v_z_high_mass == v_h_high_mass == 0

    # Capacity at the two h-zero rows A and Z.
    def row_high_mass(row_index: int, threshold: F) -> F:
        return sum(
            max(P[row_index][j], F(0)) for j in range(len(P))
            if h_values[point_name(P[j], reps)] >= threshold
        )

    cap_A_kappa_mass = row_high_mass(s, kappa)
    cap_Z_kappa_mass = row_high_mass(2, kappa)
    cap_Z_4tau_mass = row_high_mass(2, 4 * tau)
    assert cap_A_kappa_mass == 0
    assert cap_Z_kappa_mass == cap_Z_4tau_mass == t * eps

    ledgers: Dict[str, Dict[str, object]] = {
        "engine_financing_floor": ledger_entry(
            actual_high, demand, ">=",
            note="All actual high-lever mass is P_x^+(C)=theta; P_u^+(F)=0.",
        ),
        "top_deficit_weighted_at_v": ledger_entry(
            v_z_weighted, nus[s] * diameter, "<=",
            note="Sharp banked cap nu_v*(2+4delta).",
        ),
        "z_leak_at_4tau_sharp": ledger_entry(
            v_z_high_mass, nus[s] * diameter / (4 * tau), "<=",
            note="Threshold consequence using nu_v, stronger than the advertised delta cap.",
        ),
        "z_leak_at_4tau_advertised": ledger_entry(
            v_z_high_mass, delta * diameter / (4 * tau), "<=",
            note="The N5 sketch's delta*(2+4delta)/(4tau) allowance.",
        ),
        "h_leak_at_4tau_v": ledger_entry(
            v_h_high_mass, nus[s] / (4 * tau), "<=",
            note="h-reproduction/sign-split cap; strictly slack because nu_v=q>0.",
        ),
        "zero_face_capacity_A_kappa": ledger_entry(
            kappa * cap_A_kappa_mass, nus[s], "<=",
            note="Charged form kappa*m <= nu_A for the h-zero carrier/top.",
        ),
        "zero_face_capacity_Z_kappa": ledger_entry(
            kappa * cap_Z_kappa_mass, nus[2], "<=",
            note="Charged form at the nonclone h-zero blocker Z.",
        ),
        "zero_face_capacity_Z_4tau": ledger_entry(
            4 * tau * cap_Z_4tau_mass, nus[2], "<=",
            note="Generic affine-exposer capacity at threshold 4tau.",
        ),
        "hiddenness_small_beta": ledger_entry(
            t, kappa, "<",
            note="Exact witness lambda_D=1, alpha_Z=1/eps, beta_C=t.",
        ),
        "corner_mass_numerical_conclusion": ledger_entry(
            gamma_corner, CORNER_FLOOR, ">=", applicable=False,
            note="Conclusion holds numerically, but lem-sl1a-corner-ledger is not applicable: H>16tau fails.",
        ),
        "corner_exterior_coarse": ledger_entry(
            gamma_total - gamma_corner, F(1, 2) + nus[f], "<=", applicable=False,
            note="Numerical outside-corner accounting; same tallness failure prevents invoking the lemma.",
        ),
        "corner_exterior_from_exact_floor": ledger_entry(
            gamma_total - gamma_corner, gamma_total - CORNER_FLOOR, "<=", applicable=False,
            note="Numerical consequence of the printed floor, recorded without claiming its hypotheses.",
        ),
    }
    for row_index, name in ((s, "A"), (r, "X"), (f, "D"), (2, "Z")):
        ledgers[f"mass_split_{name}"] = ledger_entry(
            pos_mass(P[row_index]), 1 + nus[row_index], "=",
            note="sum P_i^+ = 1 + nu_i.",
        )

    # Clauses which are deliberately NOT claimed.  This is a local financing
    # witness, not a refutation of either selected-corner conjecture.
    selected_corner_clauses = {
        "delta_at_most_2^-16": True,
        "visible_set_nonempty_and_exactly_Z_C_D": True,
        "v_is_hidden_top": True,
        "H_gt_16tau": False,
        "top_support_phi": True,
        "admissible_exposer_h_at_v": True,
        "corner_row_f_D_is_rho_far": True,
        "corner_row_f_D_is_co_top": True,
        "corner_score_at_f_D": True,
        "legal_vertex_kernel": True,
        "pair_X_A_lies_geometrically_in_Cf_and_BN": True,
        "Gamma_f_assigns_positive_mass_to_pair_X_A": False,
        "Gamma_f_BN_at_least_1/4": False,
        "M_X_gamma_BN_gt_1/8": False,
        "N6_far_carrier_geometry_for_financing_pair": False,
    }
    assert not selected_corner_clauses["H_gt_16tau"]

    return {
        "id": f"dyadic_k{k}",
        "status": "FINANCING_INSTANCE_LOCAL_N5II",
        "rigour_scope": "L3 exact construction; not a proof and not a selected-corner counterexample",
        "parameters": {
            "k": k,
            "tau": qstr(tau),
            "delta": qstr(delta),
            "eps": qstr(eps),
            "t_star_A": qstr(t),
            "kappa": qstr(kappa),
            "rho": qstr(rho),
            "K": qstr(K),
            "q": qstr(q),
            "theta": qstr(theta),
            "D": qstr(diameter),
            "H": qstr(H),
        },
        "labels": list(LABELS),
        "matrix": [[qstr(value) for value in row] for row in P],
        "row_point_fibers": [
            {"point": name, "indices": list(js)} for name, js in zip(fiber_names, fibers)
        ],
        "negative_masses": {LABELS[i]: qstr(nus[i]) for i in range(len(P))},
        "visible_set": list(visible_set),
        "hidden_vertices": list(hidden_set),
        "visible_margin_lower_bounds": {name: qstr(value) for name, value in visible_margins.items()},
        "top_geometry": {
            "v": "A",
            "height": qstr(H),
            "H_over_tau": qstr(H / tau),
            "phi_coefficients": [qstr(value) for value in phi_coeff],
            "phi_constant": qstr(phi_constant),
            "phi_values": {name: qstr(value) for name, value in phi_values.items()},
            "z_values": {name: qstr(value) for name, value in z_values.items()},
            "h_coefficients": [qstr(value) for value in h_coeff],
            "h_values": {name: qstr(value) for name, value in h_values.items()},
            "closest_point_to_A_in_convW": [qstr(value) for value in closest],
            "X_convW_weights": {name: qstr(value) for name, value in x_weights.items()},
        },
        "hiddenness_witness_A": {
            "far_set": sorted(far_A),
            "lambda": {"D": "1"},
            "alpha": {"Z": qstr(1 / eps)},
            "beta": {"C": qstr(t)},
            "sum_beta": qstr(t),
            "balance_verified": True,
            "always_tight_support": {"T": ["D"], "O": ["C"], "Z": ["Z"]},
        },
        "pair": {
            "freight_row": "X",
            "carrier_row": "A",
            "carrier_equals_top_v": True,
            "carrier_distance_to_v": "0",
            "separation_l": qstr(separation),
            "band_lower_tau/4": qstr(tau / 4),
            "band_upper_8tau": qstr(8 * tau),
            "l_chi_full_fiber_variation": qstr(l_chi),
        },
        "engine": {
            "psi_coefficients": [qstr(value) for value in psi_coeff],
            "psi_constant": qstr(psi_constant),
            "psi_values": {name: qstr(value) for name, value in psi_values.items()},
            "N": list(N),
            "F": list(high),
            "A": qstr(A_parameter),
            "Lambda": qstr(Lambda),
            "d_by_full_fiber": {name: qstr(value) for name, value in d_by_fiber.items()},
            "demand": qstr(demand),
            "actual_joint_positive_mass_F": qstr(actual_high),
            "from_freight_X": qstr(actual_high_r),
            "from_carrier_A": qstr(actual_high_s),
            "slack": qstr(actual_high - demand),
            "financing_fiber": "C",
            "financing_fiber_z": qstr(z_values["C"]),
            "financing_fiber_h": qstr(h_values["C"]),
        },
        "corner_audit": {
            "f": "D",
            "score": qstr(f_score),
            "score_cap": qstr(12 * tau / 13),
            "corner_points": list(corner_points),
            "Gamma_total": qstr(gamma_total),
            "Gamma_Cf": qstr(gamma_corner),
            "Gamma_BF": qstr(gamma_BF),
            "Gamma_BN": qstr(gamma_BN),
            "M_X_gamma_BF": qstr(gamma_MX_BF),
            "M_X_gamma_BN": qstr(gamma_MX_BN),
            "Gamma_X_A": qstr(gamma[("X", "A")]),
        },
        "ledger_table": ledgers,
        "selected_corner_clauses": selected_corner_clauses,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-k", type=int, default=8, help="smallest k in tau=2^-k")
    parser.add_argument("--max-k", type=int, default=16, help="largest k in tau=2^-k")
    parser.add_argument(
        "--certificate", type=Path, default=CERTIFICATE_PATH,
        help="output JSON path (default: certificates.json beside this script)",
    )
    args = parser.parse_args()
    assert 8 <= args.min_k <= args.max_k

    candidates = [build_candidate(k) for k in range(args.min_k, args.max_k + 1)]
    payload = {
        "schema": "w61-leak-financing-exact-v1",
        "arithmetic": "All exact fields are rational strings; decimals are omitted from invariants.",
        "verdict": "FINANCING INSTANCE FOUND (local N5(ii) geometry; not a selected-corner counterexample)",
        "family": {
            "parameter": "tau=2^-k, delta=tau^2, k>=8",
            "construction": "thin-zero-face fixture + signed A-fiber split + transient X=(1-theta)A+theta*C",
            "tested_k_range": [args.min_k, args.max_k],
            "delta_tends_to_zero": True,
        },
        "candidates": candidates,
    }
    args.certificate.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print("W61 exact leak-financing audit: PASS")
    print(f"tested k={args.min_k}..{args.max_k}; wrote {args.certificate}")
    for candidate in candidates:
        p = candidate["parameters"]
        e = candidate["engine"]
        print(
            f"{candidate['id']}: delta={p['delta']} tau={p['tau']} "
            f"l={candidate['pair']['separation_l']} demand={e['demand']} "
            f"actual={e['actual_joint_positive_mass_F']} slack={e['slack']}"
        )
    print("Scope: L3 exact construction only; H>16tau and Gamma freight-mass clauses are false.")


if __name__ == "__main__":
    main()
