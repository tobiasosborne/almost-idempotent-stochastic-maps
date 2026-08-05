#!/usr/bin/env python3
"""Land/regenerate the LEDGER-DOMAINS family: 16 rows (14 reserved + D2/D3) + the formation row.

HISTORY OF THIS SCRIPT (it is the retained, reproducible generator of the family's shards):
  v1 (2026-08-03, commit 5f08f22c): landed the 16 rows verbatim from
    docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md sect-2
    (audit AUDIT-LEDGER-DOMAINS-v2.md, LAND-14, two exact corrections folded in;
    W78-ratified; user-ratified 2026-07-30; 8 provenance-locus typos fixed by the
    independent transcription audit, commit ec663dee).
  v2 (2026-08-05, THIS VERSION): the SETTING RE-SCOPE. First af elevations of rows 1/3
    surfaced a family-wide contract under-specification (fresh-verifier challenges
    ch-fe50a1d4/ch-d2d3e5c9/ch-dd2ab7c3/ch-782c366f): the contracts used the tilde-map
    vocabulary and scalar ledger without binding the ambient finite-dimensional UCP/cb
    setting. Repair per
    docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md
    (hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md: LAND-WITH-EXACT-CORRECTIONS;
    corrections 1 [rows 6/9 X-binders] and finding-8 [row-3 body sentence] folded in
    here), user-ratified 2026-08-05:
      - NEW formation row lem-routef-raw-factor-setting-formation (global-W_RF-first);
      - every row's contract gains an ambient binding prefix; rows 1-13 + D2/D3 keep
        their landed mathematical suffix BYTE-IDENTICAL;
      - row 14 is the SOLE suffix revision: the F2/F3/PRH prose is replaced by the
        literal scalar inequalities of DESIGN-LEDGER-DOMAINS-v2.md sect-3.5 (v1 audit
        finding 5); F2/F3/PRH application moves to the future strengthened K-ledger;
      - defs: lines drop def-almost-idempotent (row-stochastic picture) and import
        def-routef-raw-factor-setting (+ def-ucp-map where CP/UCP maps are produced);
      - deps: lines add the formation row and the v1-audit finding-4 direct edges.
    status: stated / af per current registry -- landing/rescoping promotes NOTHING;
    the af elevation queue adjudicates the mathematics.

Re-running this script rewrites the 17 argument shards to the corrected state
(idempotent). It does NOT touch definitions/, proofs/, or any other file.
"""
import pathlib, sys

REPO = pathlib.Path("/home/tobiasosborne/Projects/almost-idempotent-stochastic-maps")
OUT = REPO / "argument" / "lemmas"

DESIGN = "DESIGN-LEDGER-DOMAINS-v2.md"
AUDIT = "AUDIT-LEDGER-DOMAINS-v2.md"
RDESIGN = "DESIGN-LEDGER-SETTING-RESCOPE-V2.md"
RAUDIT = "AUDIT-LEDGER-SETTING-RESCOPE-V2.md"

# The shared ambient binding prefix (v2 rescope design sect-3.1/3.2). Rows extend it
# with producer-chain clauses and binders as designed.
P_BASE = (
    "After first fixing one global witness package W_RF supplied by "
    "lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that "
    "formation result applies, fix one def-routef-raw-factor-setting datum S over that "
    "same W_RF supplied by the same result"
)
P_WRITE = "writing the fields of (W_RF,S) as the unqualified symbols below: "
# Producer-chain clauses (v2 design sect-3.3--3.5).
P_DP = "for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness"
P_DN = "every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness"
P_UP = "every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness"
P_UN = "every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness"

BODY = """
**Status.** Landed from the hostile-audited designs; `stated` (transcribed, unchecked
in-repo). Landing promotes NOTHING -- the mathematics is adjudicated by the af
elevation queue (fresh prover, separate fresh verifier), not by this transcription.

**Numbered equations.** `(1.1)`--`(1.8)` are the closed scalar-ledger equations of
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md` sect-1, with audit
correction 1 (`rho_id^corr`) applied; they are carried as derived notation of the scalar
header `W_RF` by [[def-routef-raw-factor-setting]]. The ledger is serial: every coefficient
and radius is a finite max/min/sum/product of quantities produced by declared dependencies,
and `AUDIT-LEDGER-DOMAINS-v2.md` sects-4--5 independently recomputed it as finite, positive,
noncircular, and dimension-free.

**Ambient binding (2026-08-05 rescope).** The contract's prefix binds the ambient
finite-dimensional UCP/cb setting through [[def-routef-raw-factor-setting]] (data/notation
only) and [[lem-routef-raw-factor-setting-formation]] (existence, global-W_RF-first). The
mathematical suffix is byte-identical to the 2026-08-03 landing{suffixnote}.

**Elevation note.** The projected af budget for this row is {budget} (nodes / rounds), per the
design's sect-2 table. Rows that import [[lem-thmainext-conditional]] consume it AT CONTRACT LEVEL
as a black-box producer of `C_E, epsilon_E`; under the linker's status-propagation rule their L0
closure is capped by that row's own elevation.
"""

ROWS = [
    dict(
        id="lem-routef-raw-factor-norms",
        prefix=P_BASE + "; for every integer n >= 1 and every X in M_n(S.B), " + P_WRITE,
        suffix=(
            "Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every "
            "amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| "
            "and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
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
        prefix=P_BASE + ", " + P_WRITE,
        suffix=(
            "Raw factor-map units: for 0 <= eta <= rho_unit := rho_T, "
            "max{||tilde-Delta(I)-I||, ||tilde-Upsilon(I)-I||} <= C_T*eta."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2754-2757; LEDGER-W74F-G-K.md:169-181; AUDIT-LEDGER-DOMAINS.md:187",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-raw-factor-identities",
        prefix=P_BASE + ", " + P_WRITE,
        suffix=(
            "Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, "
            "epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2749-2753; LEDGER-W74F-G-K.md:183-187; AUDIT-LEDGER-DOMAINS.md:188",
        budget="3 / 2",
        extra=(
            "\n**Audit correction 1 (applied).** `AUDIT-LEDGER-DOMAINS-v2.md` sect-0 and sect-7 replace "
            "`rho_id := min{rho_AI, epsilon_E/C_A}` by `rho_id^corr := min{rho_theta, rho_AI, "
            "epsilon_E/C_A}`, exposing the `eta < 1/4` domain of the landed "
            "[[lem-kitaev-almost-idemp-audit]] contract (`rho_theta = 1/8`). Only this row uses "
            "`rho_id^corr`; later rows retain the two-term `rho_id`, and their effective domains are "
            "unchanged because they also descend from `rho_T <= rho_id^corr`.\n"
        ),
    ),
    dict(
        id="lem-routef-raw-product-estimate",
        prefix=P_BASE + "; for every integer n >= 1 and all X, Y in M_n(S.B), " + P_WRITE,
        suffix=(
            "Raw tilde-Delta-product estimate: for 0 <= eta <= rho_prod := rho_T, every amplification "
            "and all X, Y satisfy ||tilde-Phi_n(tilde-Delta_n X tilde-Delta_n Y) - tilde-Delta_n(XY)|| "
            "<= C_T*eta*||X||*||Y||."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
        prov="approximate_algebras.tex:2754-2766; LEDGER-W74F-G-K.md:174-181; AUDIT-LEDGER-DOMAINS.md:189",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-delta-prime-closeness",
        prefix=P_BASE + ", " + P_WRITE,
        suffix=(
            "Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, "
            "rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map "
            "Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta."
        ),
        defs="def-routef-raw-factor-setting; def-fd-cstar-diagonal; def-ucp-map",
        deps="lem-routef-raw-factor-setting-formation; cor-kitaev-diagonal-cpization; lem-routef-functional-calculus-closeness; lem-thmainext-conditional; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate",
        prov="approximate_algebras.tex:2771-2801; LEDGER-W74F-G-K.md:193-226; argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9; AUDIT-LEDGER-DOMAINS.md:190",
        budget="6 / 3",
    ),
    dict(
        id="lem-routef-delta-normalization-closeness",
        prefix=(
            P_BASE + " and " + P_DP + ", and for every X in S.B, " + P_WRITE
        ),
        suffix=(
            "Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, "
            "rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is "
            "invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with "
            "||Delta - tilde-Delta||_cb <= C_Delta*eta."
        ),
        defs="def-routef-raw-factor-setting; def-ucp-map",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-units; lem-routef-delta-prime-closeness",
        prov="approximate_algebras.tex:2797-2801; LEDGER-W74F-G-K.md:246-259,415-448; VERDICT-W74F-G-KLEDGER.md:141-145,287-290",
        budget="5 / 3",
        extra=(
            "\n**Rescope audit correction 1 (applied).** `AUDIT-LEDGER-SETTING-RESCOPE-V2.md` finding 1: "
            "the binder `and for every X in S.B` is inserted in the prefix so the `X` displayed in the "
            "normalization formula is bound. The landed suffix is byte-unchanged.\n"
        ),
    ),
    dict(
        id="lem-routef-degree-two-estimate",
        prefix=(
            P_BASE + ", " + P_DP + ", and " + P_DN
            + "; for every integer n >= 1 and all X, Y in M_n(S.B), " + P_WRITE
        ),
        suffix=(
            "Route F degree-two estimate: with C_2 := C_Delta'+4*C_Delta and rho_2 := min{rho_prod, "
            "rho_Delta', rho_Delta}, for 0 <= eta <= rho_2, every amplification satisfies "
            "||Phi_n(Delta_n X Delta_n Y) - Delta_n(XY)|| <= C_2*eta*||X||*||Y||."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-product-estimate; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness",
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
        prefix=(
            P_BASE + ", " + P_DP + ", and " + P_DN
            + "; for every integer n >= 1 and all X, Y in M_n(S.B), " + P_WRITE
        ),
        suffix=(
            "Normalized Delta product: for rho_DeltaPhi := min{rho_theta, rho_Delta, rho_2} and "
            "0 <= eta <= rho_DeltaPhi, every amplification satisfies "
            "||tilde-Phi_n(Delta_n X Delta_n Y) - tilde-Delta_n(XY)|| "
            "<= (C_2+C_theta+C_Delta)*eta*||X||*||Y||."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate",
        prov="LEDGER-W74F-G-K.md:374-383; approximate_algebras.tex:2803-2812",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-degree-three-estimate",
        prefix=(
            P_BASE + ", " + P_DP + ", and " + P_DN
            + "; for every integer n >= 1 and all X, Y, Z in M_n(S.B), " + P_WRITE
        ),
        suffix=(
            "Route F degree-three estimate: with C_3 := 10+20*C_Delta+12*C_theta+2*C_Delta' and "
            "rho_3 := min{rho_theta, rho_Delta', rho_Delta, rho_2}, for 0 <= eta <= rho_3, every "
            "amplification satisfies ||Phi_n(Delta_n X Delta_n Y Delta_n Z) - Delta_n(XYZ)|| "
            "<= C_3*eta*||X||*||Y||*||Z||."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-kitaev-almost-idemp-audit; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate",
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
        prefix=(
            P_BASE + ", " + P_DP + ", and " + P_DN + ", " + P_WRITE
        ),
        suffix=(
            "Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := "
            "min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', "
            "every Choi multiplicity space used below is nonzero and the componentwise construction "
            "produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta."
        ),
        defs="def-routef-raw-factor-setting; def-ucp-map",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-degree-three-estimate",
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
        prefix=(
            P_BASE + ", " + P_DP + ", " + P_DN + ", and " + P_UP
            + ", and for every X in B(H), " + P_WRITE
        ),
        suffix=(
            "Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := "
            "min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, "
            "b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with "
            "||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta."
        ),
        defs="def-routef-raw-factor-setting; def-ucp-map",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-units; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness",
        prov="approximate_algebras.tex:2895-2899; LEDGER-W74F-G-K.md:246-259,415-448; VERDICT-W74F-G-KLEDGER.md:144-149,291-295",
        budget="5 / 3",
        extra=(
            "\n**Rescope audit correction 1 (applied).** `AUDIT-LEDGER-SETTING-RESCOPE-V2.md` finding 1: "
            "the binder `and for every X in B(H)` is inserted in the prefix so the `X` displayed in the "
            "normalization formula is bound. The landed suffix is byte-unchanged.\n"
        ),
    ),
    dict(
        id="lem-routef-delta-upsilon-telescope",
        prefix=(
            P_BASE + ", " + P_DP + ", " + P_DN + ", " + P_UP + ", and " + P_UN + ", " + P_WRITE
        ),
        suffix=(
            "Delta-Upsilon telescope: for rho_DeltaUpsilon := min{rho_theta, rho_T, rho_id, rho_Delta, "
            "rho_Upsilon} and 0 <= eta <= rho_DeltaUpsilon, ||Delta Upsilon - Phi||_cb "
            "<= (C_theta+C_Delta+2*C_Upsilon)*eta."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness",
        prov="LEDGER-W74F-G-K.md:345-372; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-multiplicative-telescope",
        prefix=(
            P_BASE + ", " + P_DP + ", " + P_DN + ", " + P_UP + ", and " + P_UN
            + "; for every integer n >= 1 and all X, Y in M_n(S.B), " + P_WRITE
        ),
        suffix=(
            "Multiplicative telescope: for rho_mult := min{rho_T, rho_id, rho_DeltaPhi, rho_Upsilon} "
            "and 0 <= eta <= rho_mult, every amplification satisfies "
            "||Upsilon_n(Delta_n X Delta_n Y) - XY|| "
            "<= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-delta-phi-product; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness",
        prov="LEDGER-W74F-G-K.md:345-383; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-upsilon-delta-telescope",
        prefix=(
            P_BASE + ", " + P_DP + ", " + P_DN + ", " + P_UP + ", and " + P_UN + ", " + P_WRITE
        ),
        suffix=(
            "Upsilon-Delta telescope: for rho_UpsilonDelta := min{rho_T, rho_id, rho_Delta, "
            "rho_Upsilon} and 0 <= eta <= rho_UpsilonDelta, ||Upsilon Delta - I_B||_cb "
            "<= (C_Upsilon+2*C_Delta)*eta."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness",
        prov="LEDGER-W74F-G-K.md:345-372; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="3 / 2",
    ),
    dict(
        id="lem-routef-k-finiteness",
        prefix=(
            P_BASE + ", " + P_DP + ", " + P_DN + ", " + P_UP + ", and " + P_UN + ", " + P_WRITE
        ),
        suffix=(
            "Route F common coefficient/domain: K in (1.6) is finite and universal, and rho_fac in "
            "(1.7) is positive and is a common domain for the degree-two estimate and the three "
            "Route-F factorization estimates."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope",
        prov="LEDGER-W74F-G-K.md:385-397; VERDICT-W74F-G-KLEDGER.md:96-117",
        budget="4 / 2",
    ),
    dict(
        id="lem-routef-threshold-minimum",
        prefix=(
            P_BASE + ", " + P_DP + ", " + P_DN + ", " + P_UP + ", and " + P_UN + ", " + P_WRITE
        ),
        suffix=(
            "Route F scalar threshold: let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and "
            "every 0 <= eta <= eta_K satisfies eta <= rho_fac, 0 <= eta <= min{(24*K)^(-1),1}, "
            "3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2."
        ),
        defs="def-routef-raw-factor-setting",
        deps="lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-k-finiteness",
        prov="AUDIT-LEDGER-DOMAINS.md:273-317; DESIGN-LEDGER-DOMAINS-v2.md sect-3.5",
        budget="5 / 2",
        suffixnote=(
            " EXCEPT this row: the SOLE suffix revision of the rescope (v1 rescope audit finding 5)"
        ),
        extra=(
            "\n**Row-14 revision (2026-08-05 rescope).** The landed 'threshold minimum' contract "
            "asserted F2/F3 smallness and PRH admissibility, which are not exported scalar interfaces "
            "of [[lem-routef-f2-positive-unital-compression]], [[lem-routef-f3-retract-defect]], or "
            "[[lem-routef-prh-finish]] (AUDIT-LEDGER-SETTING-RESCOPE.md finding 5). The revised "
            "contract asserts exactly the scalar inequalities proved in "
            "`DESIGN-LEDGER-DOMAINS-v2.md` sect-3.5: the common factor domain, the F2 threshold "
            "entry, positivity of the F3 denominator via `3*K*eta <= 1/8`, and the rational retract "
            "bound `3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6`. Actual F2/F3/PRH application (where the "
            "map data are bound) belongs to the future strengthened [[lem-routef-k-ledger]]; those "
            "three rows, `def-stochastic`, `def-positive-approximate-retract`, and "
            "[[lem-thmainext-conditional]] accordingly leave this row's imports "
            "(DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-3.5).\n"
        ),
    ),
]

FORMATION = dict(
    id="lem-routef-raw-factor-setting-formation",
    contract=(
        "Route F raw-factor setting formation: there exists one choice W_RF of the scalar header of "
        "def-routef-raw-factor-setting, independent of H, Phi, eta, dimension, amplification level, "
        "and block data, with C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, eta_A>0 and (C_A,eta_A) "
        "the fixed witnesses of lem-routef-ai-defect-linearization, C_E<infinity and epsilon_E>0 the "
        "fixed witnesses of lem-thmainext-conditional, rho_theta:=1/8, rho_AI:=eta_A, and all "
        "remaining named scalar quantities defined by (1.1)-(1.8), such that for every nonzero "
        "finite-dimensional Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta with "
        "0 <= eta <= rho_id^corr and ||Phi^2-Phi||_cb <= eta, there exist a finite-dimensional unital "
        "C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and a "
        "def-routef-raw-factor-setting datum S over this same W_RF whose fields are the displayed "
        "H,Phi,eta,B,v,u=v^(-1) and the canonical tilde-Phi,A,star,epsilon_AI(eta),tilde-Delta,"
        "tilde-Upsilon notation, with tilde-Phi^2=tilde-Phi, A an extended epsilon_AI(eta)-C*-algebra, "
        "and 0 <= epsilon_AI(eta) <= C_A*eta <= epsilon_E."
    ),
    defs="def-routef-raw-factor-setting; def-ucp-map; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion",
    deps="lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional",
    body="""
**Status.** `stated` (transcribed from the ratified rescope design, unchecked in-repo).
Landing promotes no definition, provider, or ledger result.

**Quantifier discipline.** The existential choice of `W_RF` precedes every input quantifier.
The same `eta_A, C_A, C_E, epsilon_E`, hence the same entire derived scalar ledger, is used
for every datum `S`. The input-specific existential contains `B, v, S` only; it cannot
reselect the global witnesses.

**Derivation obligation.** Fix the AI witnesses once and the MAIN witnesses once. For an
input in the displayed domain, `rho_id^corr` gives `eta <= rho_theta = 1/8 < 1/4`,
`eta <= rho_AI = eta_A`, and `C_A*eta <= epsilon_E`. Apply [[lem-kitaev-almost-idemp-audit]]
for exact idempotence, [[lem-routef-ai-defect-linearization]] for the extended
`epsilon_AI(eta)` structure and linear estimate, and [[lem-thmainext-conditional]] to that
same finite-dimensional range `A` for one `B, v`. Package these particular outputs as `S`;
no analytic conclusion may be inferred from [[def-routef-raw-factor-setting]] alone.

**Projected af budget (binding design target).** Target 10 live nodes / 3 verification
rounds / hard cap 14: root; one global-witness selection node; one scalar-header assembly
node; one radius extraction node; one Kitaev application; one AI application; one
finite-dimensional-range node; one MAIN application; one same-output `S` packaging node;
one quantifier/universality assembly node. Hitting 14 is a factoring stop, not permission
to enlarge the cap (AUDIT-LEDGER-SETTING-RESCOPE-V2.md finding 3: this workspace gets its
own seed/provision/elevate/bank phase BEFORE either live family continuation).
""",
)

SHARD = """---
id: {id}
kind: lemma
contract: {contract}
defs: {defs}
deps: {deps}
status: stated
af: {af}
provenance: {provenance}
owner: A
workspace: proofs/{id}
---
{body}{extra}"""

PROV_ROW = (
    "{design} sect-2 row {row} (landed verbatim 2026-08-03, LaTeX flattened to registry ASCII); "
    "{audit} LAND-14 with two exact corrections, both folded in; W78-ratified package front 3; "
    "user-ratified 2026-07-30, ledger front re-selected by the user 2026-08-03; RE-SCOPED 2026-08-05: "
    "ambient binding prefix + defs/deps repair per {rdesign} sect-3 (hostile re-audit {raudit} "
    "LAND-WITH-EXACT-CORRECTIONS, corrections folded in), user-ratified 2026-08-05; source {prov}"
)

PROV_FORMATION = (
    "{rdesign} sect-2 (formation repair required by AUDIT-LEDGER-SETTING-RESCOPE.md findings 1-3); "
    "hostile re-audit {raudit} verdict LAND-WITH-EXACT-CORRECTIONS (formation cleared, elevation "
    "phase mandated by its finding 3); user-ratified 2026-08-05; scalar ledger source "
    "DESIGN-LEDGER-DOMAINS-v2.md sect-1"
)

# af: field values are read from the CURRENT shards when present (rows 1 and 3 are
# mid-elevation with af: seeded); default none.
def current_af(path):
    if path.exists():
        for ln in path.read_text().splitlines():
            if ln.strip().startswith("af:"):
                return ln.split(":", 1)[1].strip()
    return "none"


def main():
    if not OUT.is_dir():
        sys.exit(f"missing {OUT}")
    labels = ["1", "2", "3", "4", "5", "6", "D2", "7", "D3", "8", "9", "10", "11", "12", "13", "14"]
    assert len(labels) == len(ROWS), (len(labels), len(ROWS))
    written = []
    for label, r in zip(labels, ROWS):
        path = OUT / f"{r['id']}.md"
        prov = PROV_ROW.format(design=DESIGN, audit=AUDIT, rdesign=RDESIGN, raudit=RAUDIT,
                               row=label, prov=r["prov"])
        text = SHARD.format(
            id=r["id"], contract=r["prefix"] + r["suffix"], defs=r["defs"], deps=r["deps"],
            af=current_af(path), provenance=prov,
            body=BODY.format(budget=r["budget"], suffixnote=r.get("suffixnote", "")),
            extra=r.get("extra", ""),
        )
        path.write_text(text)
        written.append(r["id"])
    f = FORMATION
    path = OUT / f"{f['id']}.md"
    text = SHARD.format(
        id=f["id"], contract=f["contract"], defs=f["defs"], deps=f["deps"],
        af=current_af(path),
        provenance=PROV_FORMATION.format(rdesign=RDESIGN, raudit=RAUDIT),
        body=f["body"], extra="",
    )
    path.write_text(text)
    written.append(f["id"])
    print(f"landed/rewrote {len(written)} shards:")
    for w in written:
        print("  ", w)


if __name__ == "__main__":
    main()
