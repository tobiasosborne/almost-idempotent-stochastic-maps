#!/usr/bin/env python3
"""Land the LAND-14 ledger-domains package (14 reserved rows + D2/D3 reconnections).

Source of truth: docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md
  sect-2 table (contracts, defs, deps, provenance) + sect-6.1 (corrected D2/D3 dep lists).
Audit:          docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS-v2.md
  disposition LAND-14 with two exact corrections (sect-7), BOTH folded in here:
    C1  rho_id := min{rho_AI, epsilon_E/C_A}  ->  rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}
        (row 3 contract; no other radius formula or primitive-minimum entry changes)
    C2  "the MAIN contract supplies the unital extended isomorphism" -> "... supplies the extended
        isomorphism, whose unit defect is at most C_V*eta" (design prose sect-3.1; no arithmetic change,
        no contract text carries the old wording, recorded in the body note of row 1)
Ratification:   docs/plans/2026-07-27-W78-ratification-package.md front 3; user ratified in-session
  2026-07-30 ("proceed as you recommend on all decisions D1-4"); user re-selected the ledger front
  2026-08-03.

Contracts are the design's one-line contracts with LaTeX flattened to registry ASCII per the
established convention (commit a7ab84c7, the MAIN landing). status: stated / af: none -- landing
promotes NOTHING; the af elevation queue adjudicates the mathematics.
"""
import pathlib, sys

REPO = pathlib.Path("/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps")
OUT = REPO / "argument" / "lemmas"

DESIGN = "DESIGN-LEDGER-DOMAINS-v2.md"
AUDIT = "AUDIT-LEDGER-DOMAINS-v2.md"

# Shared body note: what the numbered equations mean, and the status boundary.
BODY = """
**Status.** Landed verbatim from the hostile-audited design; `stated` (transcribed, unchecked
in-repo) and `af: none`. Landing promotes NOTHING -- the mathematics is adjudicated by the af
elevation queue (fresh prover, separate fresh verifier), not by this transcription.

**Numbered equations.** `(1.1)`--`(1.8)` are the closed scalar-ledger equations of
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md` sect-1, with audit
correction 1 (`rho_id^corr`) applied. The ledger is serial: every coefficient and radius is a
finite max/min/sum/product of quantities produced by declared dependencies, and
`AUDIT-LEDGER-DOMAINS-v2.md` sects-4--5 independently recomputed it as finite, positive,
noncircular, and dimension-free.

**Elevation note.** The projected af budget for this row is {budget} (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.
"""

ROWS = [
    dict(
        id="lem-routef-raw-factor-norms",
        contract=(
            "Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every "
            "amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| "
            "and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion",
        deps="lem-routef-functional-calculus-closeness; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2749-2753; LEDGER-W74F-G-K.md:154-190",
        budget="8 / 3",
        extra=(
            "\n**Audit correction 2 (wording, applied).** The design's sect-3.1 prose is read as "
            "\"the MAIN contract supplies the extended isomorphism, whose unit defect is at most "
            "C_V*eta\" -- NOT as a unital extended isomorphism. No arithmetic changes; the unit "
            "defect is carried explicitly by [[lem-routef-raw-factor-units]].\n"
        ),
    ),
    dict(
        id="lem-routef-raw-factor-units",
        contract=(
            "Raw factor-map units: for 0 <= eta <= rho_unit := rho_T, "
            "max{||tilde-Delta(I)-I||, ||tilde-Upsilon(I)-I||} <= C_T*eta."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion",
        deps="lem-routef-raw-factor-norms; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2754-2757; LEDGER-W74F-G-K.md:169-181; AUDIT-LEDGER-DOMAINS.md:187",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-raw-factor-identities",
        contract=(
            "Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, "
            "epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion",
        deps="lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2749-2753; LEDGER-W74F-G-K.md:183-187; AUDIT-LEDGER-DOMAINS.md:188",
        budget="3 / 2",
        extra=(
            "\n**Audit correction 1 (applied).** `AUDIT-LEDGER-DOMAINS-v2.md` sect-0 and sect-7 replace "
            "`rho_id := min{rho_AI, epsilon_E/C_A}` by `rho_id^corr := min{rho_theta, rho_AI, "
            "epsilon_E/C_A}`, exposing the `eta < 1/4` domain of the landed "
            "[[lem-kitaev-almost-idemp-audit]] contract (`rho_theta = 1/8`). No downstream radius or "
            "primitive-minimum entry changes; later rows referring to `rho_id` denote the corrected "
            "value.\n"
        ),
    ),
    dict(
        id="lem-routef-raw-product-estimate",
        contract=(
            "Raw tilde-Delta-product estimate: for 0 <= eta <= rho_prod := rho_T, every amplification "
            "and all X, Y satisfy ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) - tilde-Delta_n(XY)|| "
            "<= C_T*eta*||X||*||Y||."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion",
        deps="lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2754-2766; LEDGER-W74F-G-K.md:174-181; AUDIT-LEDGER-DOMAINS.md:189",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-delta-prime-closeness",
        contract=(
            "Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, "
            "rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map "
            "Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta."
        ),
        defs="def-fd-cstar-diagonal; def-extended-epsilon-cstar-algebra",
        deps="cor-kitaev-diagonal-cpization; lem-routef-functional-calculus-closeness; lem-thmainext-conditional; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate",
        prov="approximate_algebras.tex:2771-2801; LEDGER-W74F-G-K.md:193-226; argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9; AUDIT-LEDGER-DOMAINS.md:190",
        budget="6 / 3",
    ),
    dict(
        id="lem-routef-delta-normalization-closeness",
        contract=(
            "Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, "
            "rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is "
            "invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with "
            "||Delta - tilde-Delta||_cb <= C_Delta*eta."
        ),
        defs="def-extended-epsilon-cstar-algebra",
        deps="lem-routef-raw-factor-units; lem-routef-delta-prime-closeness",
        prov="approximate_algebras.tex:2797-2801; LEDGER-W74F-G-K.md:246-259,415-448; VERDICT-W74F-G-KLEDGER.md:141-145,287-290",
        budget="5 / 3",
    ),
    dict(
        id="lem-routef-degree-two-estimate",
        contract=(
            "Route F degree-two estimate: with C_2 := C_Delta'+4*C_Delta and rho_2 := min{rho_prod, "
            "rho_Delta', rho_Delta}, for 0 <= eta <= rho_2, every amplification satisfies "
            "||Phi_n(Delta_n X Delta_n Y) - Delta_n(XY)|| <= C_2*eta*||X||*||Y||."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra",
        deps="lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness",
        prov="approximate_algebras.tex:2803-2812; LEDGER-W74F-G-K.md:193-226; VERDICT-W74F-G-KLEDGER.md:119-128; AUDIT-LEDGER-DOMAINS.md:234-249",
        budget="5 / 3",
        extra=(
            "\n**Reconnection row (D2).** Not one of the fourteen reservations: a degree-row "
            "reconnection whose dependency list is the audit-prescribed corrected list of the design's "
            "sect-6.1 (adding the direct [[lem-routef-functional-calculus-closeness]] import the first "
            "audit found missing). It carries no forward edge.\n"
        ),
    ),
    dict(
        id="lem-routef-delta-phi-product",
        contract=(
            "Normalized Delta product: for rho_DeltaPhi := min{rho_theta, rho_Delta, rho_2} and "
            "0 <= eta <= rho_DeltaPhi, every amplification satisfies "
            "||tilde-Phi_n(Delta_n X Delta_n Y) - tilde-Delta_n(XY)|| "
            "<= (C_2+C_theta+C_Delta)*eta*||X||*||Y||."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra",
        deps="lem-routef-functional-calculus-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate",
        prov="LEDGER-W74F-G-K.md:374-383; approximate_algebras.tex:2803-2812",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-degree-three-estimate",
        contract=(
            "Route F degree-three estimate: with C_3 := 10+20*C_Delta+12*C_theta+2*C_Delta' and "
            "rho_3 := min{rho_theta, rho_Delta', rho_Delta, rho_2}, for 0 <= eta <= rho_3, every "
            "amplification satisfies ||Phi_n(Delta_n X Delta_n Y Delta_n Z) - Delta_n(XYZ)|| "
            "<= C_3*eta*||X||*||Y||*||Z||."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra",
        deps="lem-kitaev-almost-idemp-audit; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate",
        prov="approximate_algebras.tex:2813-2829; LEDGER-W74F-G-K.md:193-226; VERDICT-W74F-G-KLEDGER.md:119-128; AUDIT-LEDGER-DOMAINS.md:251-264",
        budget="7 / 3",
        extra=(
            "\n**Reconnection row (D3).** Not one of the fourteen reservations: a degree-row "
            "reconnection whose dependency list is the audit-prescribed corrected list of the design's "
            "sect-6.1. It carries no forward edge.\n"
        ),
    ),
    dict(
        id="lem-routef-upsilon-prime-closeness",
        contract=(
            "Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := "
            "min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', "
            "every Choi multiplicity space used below is nonzero and the componentwise construction "
            "produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta."
        ),
        defs="def-extended-epsilon-cstar-algebra",
        deps="lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-degree-three-estimate",
        prov="approximate_algebras.tex:2831-2895; LEDGER-W74F-G-K.md:228-245; AUDIT-LEDGER-DOMAINS.md:181-230",
        budget="11 / 3",
        extra=(
            "\n**The load-bearing repair.** The `(2*C_R)^(-1)` entry of `rho_Upsilon'` is the first "
            "audit's exact repair, re-confirmed in place by `AUDIT-LEDGER-DOMAINS-v2.md` sect-4: on "
            "that radius `||C_j|| >= 1/2`, hence every Choi multiplicity space from which the "
            "construction chooses a unit vector is PROVED nonzero before the choice is made.\n"
        ),
    ),
    dict(
        id="lem-routef-upsilon-normalization-closeness",
        contract=(
            "Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := "
            "min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, "
            "b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with "
            "||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta."
        ),
        defs="def-extended-epsilon-cstar-algebra",
        deps="lem-routef-raw-factor-units; lem-routef-upsilon-prime-closeness",
        prov="approximate_algebras.tex:2895-2899; LEDGER-W74F-G-K.md:246-259,415-448; VERDICT-W74F-G-KLEDGER.md:144-149,291-295",
        budget="5 / 3",
    ),
    dict(
        id="lem-routef-delta-upsilon-telescope",
        contract=(
            "Delta-Upsilon telescope: for rho_DeltaUpsilon := min{rho_theta, rho_T, rho_id, rho_Delta, "
            "rho_Upsilon} and 0 <= eta <= rho_DeltaUpsilon, ||Delta Upsilon - Phi||_cb "
            "<= (C_theta+C_Delta+2*C_Upsilon)*eta."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra",
        deps="lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-normalization-closeness; lem-routef-upsilon-normalization-closeness",
        prov="LEDGER-W74F-G-K.md:345-372; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-multiplicative-telescope",
        contract=(
            "Multiplicative telescope: for rho_mult := min{rho_T, rho_id, rho_DeltaPhi, rho_Upsilon} "
            "and 0 <= eta <= rho_mult, every amplification satisfies "
            "||Upsilon_n(Delta_n X Delta_n Y) - XY|| "
            "<= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra",
        deps="lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-phi-product; lem-routef-upsilon-normalization-closeness",
        prov="LEDGER-W74F-G-K.md:345-383; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-upsilon-delta-telescope",
        contract=(
            "Upsilon-Delta telescope: for rho_UpsilonDelta := min{rho_T, rho_id, rho_Delta, "
            "rho_Upsilon} and 0 <= eta <= rho_UpsilonDelta, ||Upsilon Delta - I_B||_cb "
            "<= (C_Upsilon+2*C_Delta)*eta."
        ),
        defs="def-extended-epsilon-cstar-algebra",
        deps="lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-normalization-closeness; lem-routef-upsilon-normalization-closeness",
        prov="LEDGER-W74F-G-K.md:345-372; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="3 / 2",
    ),
    dict(
        id="lem-routef-k-finiteness",
        contract=(
            "Route F common coefficient/domain: K in (1.6) is finite and universal, and rho_fac in "
            "(1.7) is positive and is a common domain for the degree-two estimate and the three "
            "Route-F factorization estimates."
        ),
        defs="def-extended-epsilon-cstar-algebra",
        deps="lem-routef-degree-two-estimate; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope",
        prov="LEDGER-W74F-G-K.md:385-397; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-threshold-minimum",
        contract=(
            "Route F threshold minimum: importing the black-box constants C_E, epsilon_E used in rows "
            "1-4, let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and for 0 <= eta <= eta_K "
            "the three factorization estimates have common coefficient K, the F2 and F3 smallness "
            "conditions hold, and the PRH finish is admissible."
        ),
        defs="def-almost-idempotent; def-extended-epsilon-cstar-algebra; def-stochastic; def-positive-approximate-retract",
        deps="lem-thmainext-conditional; lem-routef-k-finiteness; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish",
        prov="AUDIT-LEDGER-DOMAINS.md:273-317; argument/lemmas/lem-thmainext-conditional.md:4-9; lem-routef-f2-positive-unital-compression / lem-routef-f3-retract-defect / lem-routef-prh-finish shards:4-9",
        budget="5 / 2",
        extra=(
            "\n**Terminal-row note (design sect-2).** This row consumes [[lem-thmainext-conditional]] AT "
            "CONTRACT LEVEL as the black-box producer of `C_E, epsilon_E`. That producer remains "
            "`proved-mod-audit`; using its contract here promotes it not at all, and under the linker's "
            "status-propagation rule this row's own af elevation inherits its status restriction. The "
            "first audit's claim that the terminal threshold was a GAP was REFUTED by "
            "`AUDIT-LEDGER-DOMAINS-v2.md` sect-0 and sect-5: the ten-entry expanded minimum is finite, "
            "positive, noncircular, and dimension-free.\n"
        ),
    ),
]

SHARD = """---
id: {id}
kind: lemma
contract: {contract}
defs: {defs}
deps: {deps}
status: stated
af: none
provenance: {design} sect-2 row {row} (landed verbatim, LaTeX flattened to registry ASCII); {audit} LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; source {prov}
owner: A
workspace: proofs/{id}
---
{body}{extra}"""


def main():
    if not OUT.is_dir():
        sys.exit(f"missing {OUT}")
    labels = ["1", "2", "3", "4", "5", "6", "D2", "7", "D3", "8", "9", "10", "11", "12", "13", "14"]
    assert len(labels) == len(ROWS), (len(labels), len(ROWS))
    written = []
    for label, r in zip(labels, ROWS):
        path = OUT / f"{r['id']}.md"
        if path.exists():
            sys.exit(f"REFUSING to overwrite existing shard: {path}")
        text = SHARD.format(
            id=r["id"], contract=r["contract"], defs=r["defs"], deps=r["deps"],
            design=DESIGN, audit=AUDIT, row=label, prov=r["prov"],
            body=BODY.format(budget=r["budget"]), extra=r.get("extra", ""),
        )
        path.write_text(text)
        written.append(r["id"])
    print(f"landed {len(written)} shards:")
    for w in written:
        print("  ", w)


if __name__ == "__main__":
    main()
