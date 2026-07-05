#!/usr/bin/env python3
"""Exact-rational proof-side checker for arm G wave 16.

This script proves no theorem.  It hard-asserts the wave-15 seed certificate,
the direct row-reproduction/FE identity for B_{r,s}, and the seed's clean
Gamma-block anatomy.  All arithmetic is fractions.Fraction.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

import w16_b_restricted as w


ROOT = Path(__file__).resolve().parent
JSON_PATH = ROOT / "identity_certificate.json"
REPORT_PATH = ROOT / "IDENTITY.md"


def fstr(x: F) -> str:
    return w.fstr(x)


def seed_instance() -> tuple[list[list[F]], list[list[F]]]:
    L = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(2, 25), F(-3, 50), F(49, 50)],
        [F(1, 25), F(197, 200), F(-1, 40)],
        [F(-1, 100), F(51, 100), F(1, 2)],
    ]
    B = [
        [F(1), F(0), F(0), F(0), F(0), F(0)],
        [F(-1, 50), F(203, 400), F(1, 80), F(0), F(1, 2), F(0)],
        [F(-55319, 1000000), F(7269, 1000000), F(5599, 20000), F(7, 10), F(0), F(681, 10000)],
    ]
    return L, B


def direct_fe_identity(
    P: list[list[F]],
    coords: tuple[tuple[F, F, F], ...],
    U: tuple[int, int, int],
    r: int,
    s: int,
) -> dict:
    beta = P[U[r]]
    x = [coords[i][s] for i in range(len(P))]
    xpos = [w.pos(v) for v in x]
    wneg = [w.neg(v) for v in x]
    J = [i for i in range(len(P)) if beta[i] > 0 and x[i] < 0]
    assert J, "nonempty carrier set"

    Bmass = sum(beta[i] * wneg[i] for i in J)
    assert Bmass == w.B_mass(P, coords, U, r, s)

    # Row-reproduction in the s-coordinate for every B-carrier:
    # a_s(i) = sum_k P_ik a_s(k).
    for i in J:
        assert x[i] == sum(P[i][k] * x[k] for k in range(len(P)))

    # FE-style exact identity, directly for x=a_s:
    # sum_i W_i (beta_i - A_i^J) = exact signed source.
    A_in = {
        k: sum(beta[i] * w.pos(P[i][k]) for i in J)
        for k in J
    }
    lhs_terms = {
        k: wneg[k] * (beta[k] - A_in[k])
        for k in J
    }
    lhs = sum(lhs_terms.values())

    source_terms = {}
    rhs = F(0)
    for i in J:
        total_i = -w.neg(P[i][i]) * wneg[i]
        pieces = {
            "self_negative": -w.neg(P[i][i]) * wneg[i],
            "internal_negative_transfer": F(0),
            "external_positive_to_negative_coord": F(0),
            "external_negative_to_positive_coord": F(0),
            "external_positive_to_positive_coord": F(0),
            "external_negative_to_negative_coord": F(0),
        }
        for k in range(len(P)):
            if k == i:
                continue
            if k in J:
                term = -w.neg(P[i][k]) * wneg[k]
                pieces["internal_negative_transfer"] += term
                total_i += term
            else:
                t1 = w.pos(P[i][k]) * wneg[k]
                t2 = w.neg(P[i][k]) * xpos[k]
                t3 = -w.pos(P[i][k]) * xpos[k]
                t4 = -w.neg(P[i][k]) * wneg[k]
                pieces["external_positive_to_negative_coord"] += t1
                pieces["external_negative_to_positive_coord"] += t2
                pieces["external_positive_to_positive_coord"] += t3
                pieces["external_negative_to_negative_coord"] += t4
                total_i += t1 + t2 + t3 + t4
        source_terms[i] = {"unweighted": total_i, "weighted": beta[i] * total_i, **pieces}
        rhs += beta[i] * total_i

    assert lhs == rhs
    assert lhs == sum(beta[i] * ((1 - w.pos(P[i][i])) * wneg[i] - sum(w.pos(P[i][k]) * wneg[k] for k in J if k != i)) for i in J)

    transfer_excess = sum(wneg[k] * w.pos(A_in[k] - beta[k]) for k in J)
    signed_self_defect_floor = lhs / Bmass

    return {
        "carriers": J,
        "B": Bmass,
        "A_in": A_in,
        "lhs_terms": lhs_terms,
        "lhs": lhs,
        "rhs": rhs,
        "source_terms": source_terms,
        "transfer_excess": transfer_excess,
        "signed_self_defect_floor": signed_self_defect_floor,
    }


def ci_terms(
    P: list[list[F]],
    coords: tuple[tuple[F, F, F], ...],
    U: tuple[int, int, int],
    s: int,
    r: int,
    j: int,
) -> dict:
    I, terms, c, d_r, d_t = w.ci_import(P, coords, U, s, r, j)
    alpha_B, alpha_A = w.import_reduction_coefficients(c, d_r, d_t)
    Bmass = w.B_mass(P, coords, U, r, s)
    Amass = w.A_mass(P, coords, U, r, s)
    assert I == sum(term for _, _, term in terms)
    assert I <= alpha_B * Bmass + alpha_A * Amass
    return {
        "I": I,
        "terms": terms,
        "c": c,
        "d_r": d_r,
        "d_t": d_t,
        "alpha_B": alpha_B,
        "alpha_A": alpha_A,
        "bound": alpha_B * Bmass + alpha_A * Amass,
    }


def jsonable(obj):
    if isinstance(obj, F):
        return fstr(obj)
    if isinstance(obj, tuple):
        return [jsonable(x) for x in obj]
    if isinstance(obj, list):
        return [jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    return obj


def main() -> None:
    L, Bleft = seed_instance()
    P = w.P_of(L, Bleft)
    delta = w.delta_of(P)
    assert delta == F(55319, 1000000)
    assert delta <= F(1, 4)

    charts = w.chart_data(L, P)
    argmins = w.theta_argmins(charts)
    assert len(argmins) == 1
    cd = argmins[0]
    U = (0, 2, 4)
    s = 2
    r = 1
    j = 1
    assert cd.U == U
    assert cd.m == F(197, 200)
    assert cd.phi == (F(0), F(679, 24625), F(219870541, 7880000000))
    M = cd.phi[s]
    assert M == F(219870541, 7880000000)

    br = w.branch_record(L, P, cd, s, j)
    assert br["a"] == [F(-8, 197), F(5, 197), F(200, 197)]
    assert br["self"] == F(203, 400)
    assert br["theta_pivot"]
    assert br["Psi"] == F(1, 200)
    assert br["Gamma"] == F(7, 250)
    assert br["Psi"] < M <= br["Gamma"]

    Bmass = w.B_mass(P, cd.coords, U, r, s)
    assert Bmass == F(42, 985)
    assert Bmass / delta == F(8400000, 10897843)

    carriers = [
        {
            "i": i,
            "beta": P[U[r]][i],
            "a_s": cd.coords[i][s],
            "contribution": w.pos(P[U[r]][i]) * w.neg(cd.coords[i][s]),
            "pivot_admissible": w.neg(cd.coords[i][s]) * cd.m >= F(1, 2),
            "row_negativity": w.row_neg(P[i]),
            "self": P[i][i],
        }
        for i in range(len(P))
        if P[U[r]][i] > 0 and cd.coords[i][s] < 0
    ]
    assert len(carriers) == 1
    assert carriers[0]["i"] == 3
    assert carriers[0]["contribution"] == Bmass
    assert carriers[0]["pivot_admissible"] is False

    fe = direct_fe_identity(P, cd.coords, U, r, s)
    assert fe["carriers"] == [3]
    assert fe["B"] == Bmass
    assert fe["signed_self_defect_floor"] == F(157, 500)
    assert fe["transfer_excess"] == 0

    ci = ci_terms(P, cd.coords, U, s, r, j)
    assert ci["I"] == F(21, 9850)
    assert ci["c"] == F(200, 197)
    assert ci["d_r"] == F(5, 197)
    assert ci["d_t"] == F(-8, 197)

    cert = {
        "tier": "T0 exact rational certificate; T1 identity interpretation only",
        "delta": delta,
        "U": U,
        "s": s,
        "r": r,
        "clean_block_row": j,
        "Phi": cd.phi,
        "M": M,
        "Psi": br["Psi"],
        "Gamma": br["Gamma"],
        "B": Bmass,
        "B_over_delta": Bmass / delta,
        "carriers": carriers,
        "direct_fe": fe,
        "ci": ci,
    }
    JSON_PATH.write_text(json.dumps(jsonable(cert), indent=2, sort_keys=True) + "\n")

    lines = [
        "# Wave 16 Direct FE Identity Certificate",
        "",
        "Status: T0 exact arithmetic for the seed; T1 algebraic identity; no theorem proof.",
        "",
        f"Seed: `delta={fstr(delta)}`, `U={U}`, `s={s}`, `r={r}`, clean row `j={j}`.",
        f"`Phi(U)=({', '.join(fstr(x) for x in cd.phi)})`, `M={fstr(M)}`, `Psi={fstr(br['Psi'])}`, `Gamma={fstr(br['Gamma'])}`.",
        f"`B_{{1,2}}={fstr(Bmass)}`, `B/delta={fstr(Bmass / delta)}`.",
        "",
        "## B-mass anatomy",
        "",
    ]
    for c in carriers:
        lines.append(
            f"- carrier `i={c['i']}`: `beta={fstr(c['beta'])}`, `a_s={fstr(c['a_s'])}`, "
            f"`contribution={fstr(c['contribution'])}`, `self={fstr(c['self'])}`, "
            f"`nu_i={fstr(c['row_negativity'])}`, `pivot_admissible={c['pivot_admissible']}`."
        )
    lines.extend(
        [
            "",
            "## Direct FE identity",
            "",
            "For `J={i: beta_r(i)>0, a_s(i)<0}` and `W_i=a_s(i)^-`, row reproduction gives",
            "",
            "```text",
            "sum_{i in J} W_i (beta_i - sum_{j in J} beta_j P_ji^+) = exact signed source from P_ik a_s(k).",
            "```",
            "",
            f"Here `J={fe['carriers']}`, `lhs=rhs={fstr(fe['lhs'])}`, and `lhs/B={fstr(fe['signed_self_defect_floor'])}`.",
            f"The internal positive-transfer excess is `{fstr(fe['transfer_excess'])}`.",
            "",
            "## Clean-block import anatomy",
            "",
            f"The Γ-row import has `I={fstr(ci['I'])}` with `c={fstr(ci['c'])}`, `d_r={fstr(ci['d_r'])}`, `d_t={fstr(ci['d_t'])}`.",
            f"The CI reduction bound gives `I <= {fstr(ci['bound'])}`; it is a lower-forcing diagnostic, not an upper charge for `B`.",
            "",
            "Machine-readable certificate: `identity_certificate.json`.",
        ]
    )
    REPORT_PATH.write_text("\n".join(lines) + "\n")

    print(f"seed delta={fstr(delta)} B={fstr(Bmass)} B/delta={fstr(Bmass / delta)}")
    print(f"direct FE lhs=rhs={fstr(fe['lhs'])} lhs/B={fstr(fe['signed_self_defect_floor'])}")
    print(f"clean block Psi={fstr(br['Psi'])} M={fstr(M)} Gamma={fstr(br['Gamma'])}")
    print(f"wrote {JSON_PATH}")
    print(f"wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
