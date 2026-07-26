# DESIGN v2 — GAP-LEDGER-DOMAINS repaired local-domain DAG

Date: 2026-07-26
Role: fresh repair designer
Status: **DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, REWIRE, OR PROMOTE**

## 0. Disposition

**DESIGN-CLOSABLE, SUBJECT TO A NEW HOSTILE PASS.** All fourteen reserved
rows close at design level after applying the binding audit corrections. The
two degree rows reconnect without a forward edge, and the proposed
`lem-routef-k-ledger` wiring remains guarded.

The three substantive repairs are:

1. the componentwise \(\Upsilon'\) radius now contains
   \((2C_R)^{-1}\), where \(C_R=C_V+C_\Delta+C_2\), so every Choi
   multiplicity space from which the construction chooses a unit vector is
   proved nonzero;
2. the five dependency-list corrections from the audit are applied
   verbatim; and
3. the terminal threshold is
   \[
   \eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}>0,
   \]
   using the landed `lem-thmainext-conditional` contract as the black-box
   producer of \(C_E,\varepsilon_E\). It does not import the unlanded
   internal MAIN reset package.

This document supplies designs, not proofs. It does not change a registry
contract or status and does not certify any row as rigorous.

## 1. Sources, notation, and closed scalar ledger

The binding repair is
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS.md:1-337`.
The underlying source and architecture loci are:

- `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:230-275,348-364,596-610`;
- `docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP-V3.md:69-102`;
- `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md:154-259,345-455`;
- `docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-G-KLEDGER.md:96-160,287-304`; and
- `refs/kitaev-2405.02434/approximate_algebras.tex:2749-2899`.

All proposed contracts are restricted to the finite Route-F setting
\(\mathcal H=\mathbb C^n\). Every constant below is required to be
independent of \(n\), amplification level, the number and sizes of simple
blocks, and any MAIN stage index.

The existing dependencies produce
\[
\rho_\theta:=\frac18,\qquad
C_\theta:=12(\sqrt2-1),
\]
by `lem-routef-functional-calculus-closeness`
(`argument/lemmas/lem-routef-functional-calculus-closeness.md:4-9`), and
\[
\rho_{\rm AI}:=\eta_A>0,\qquad
C_A:=20+\frac{211}{8}C_\theta
\]
by `lem-routef-ai-defect-linearization`
(`argument/lemmas/lem-routef-ai-defect-linearization.md:4-9`).
The notation \(\rho_{\rm AI}=\eta_A\) is used **only** to invoke that
AI-defect row.

The landed `lem-thmainext-conditional` contract produces universal
\(C_E<\infty\) and \(\varepsilon_E>0\), independent of dimension,
amplification, and block data
(`argument/lemmas/lem-thmainext-conditional.md:4-9`). Put
\[
\bar C_E:=\max\{1,C_E\},\qquad
C_V:=\bar C_EC_A,\qquad
C_T:=C_\theta+3C_V,
\]
and
\[
\boxed{\rho_T:=
\min\left\{
\rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)}
\right\}.}
\tag{1.1}
\]
Thus \(C_\theta\eta,C_V\eta\le1/4\) on \(\rho_T\), while
\(C_A\eta\le\varepsilon_E\) puts the AI algebra inside the black-box MAIN
contract's domain.

For later rows define, in this order,
\[
\begin{aligned}
\rho_{\rm unit}&:=\rho_T,\\
\rho_{\rm id}&:=\min\{\rho_{\rm AI},\varepsilon_E/C_A\},\\
\rho_{\rm prod}&:=\rho_T,\\
C_{\Delta'}&:=C_T+4C_\theta,\\
\rho_{\Delta'}&:=\min\{\rho_T,\rho_{\rm prod}\},\\
C_\Delta&:=6C_T+7C_{\Delta'},\\
\rho_\Delta&:=\min\left\{
\rho_{\rm unit},\rho_{\Delta'},
\frac1{2(C_T+C_{\Delta'})}
\right\},\\
C_2&:=C_{\Delta'}+4C_\Delta,\\
\rho_2&:=\min\{\rho_{\rm prod},\rho_{\Delta'},\rho_\Delta\},\\
\rho_{\Delta\Phi}&:=\min\{\rho_\theta,\rho_\Delta,\rho_2\},\\
C_3&:=10+20C_\Delta+12C_\theta+2C_{\Delta'},\\
\rho_3&:=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}.
\end{aligned}
\tag{1.2}
\]

For the audited componentwise repair, put
\[
\begin{aligned}
C_N&:=C_V+C_\Delta,\\
C_R&:=C_N+C_2=C_V+C_\Delta+C_2,\\
C_L&:=C_2+C_3+2C_R,\\
C_{\Upsilon'}&:=1+C_\theta+2C_\Delta+2C_L,
\end{aligned}
\tag{1.3}
\]
and use the **corrected** radius
\[
\boxed{\rho_{\Upsilon'}:=
\min\left\{
\rho_T,\rho_{\rm id},\rho_\Delta,\rho_2,\rho_3,
\frac1{2C_R}
\right\}.}
\tag{1.4}
\]
The added last entry is the exact audit repair
(`AUDIT-LEDGER-DOMAINS.md:86-90,153-157,181-209`).

Continue serially with
\[
\begin{aligned}
C_\Upsilon&:=6C_T+7C_{\Upsilon'},\\
\rho_\Upsilon&:=\min\left\{
\rho_{\rm unit},\rho_{\Upsilon'},
\frac1{2(C_T+C_{\Upsilon'})}
\right\},\\
\rho_{\Delta\Upsilon}&:=\min\{
\rho_\theta,\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\},\\
\rho_{\rm mult}&:=\min\{
\rho_T,\rho_{\rm id},\rho_{\Delta\Phi},\rho_\Upsilon\},\\
\rho_{\Upsilon\Delta}&:=\min\{
\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}.
\end{aligned}
\tag{1.5}
\]
Finally,
\[
\boxed{
K:=\max\left\{
1,\ C_\theta+C_\Delta+2C_\Upsilon,\
C_\Upsilon+2(C_2+C_\theta+C_\Delta),\
C_\Upsilon+2C_\Delta
\right\},
}
\tag{1.6}
\]
\[
\boxed{\rho_{\rm fac}:=
\min\{\rho_2,\rho_{\Delta\Upsilon},
\rho_{\rm mult},\rho_{\Upsilon\Delta}\},}
\tag{1.7}
\]
and
\[
\boxed{\eta_K:=
\min\left\{\rho_{\rm fac},\frac1{24K},1\right\}.}
\tag{1.8}
\]

## 2. Full corrected serial DAG

Rows D2 and D3 are the two design-only reconnections, not members of the
fourteen reservations. They are interleaved at the first points where their
outputs are available. “Row \(r\)” in a dependency cell means the reserved
id displayed in row \(r\).

| order | proposed id | closed one-line `contract:` (design only) | defs | deps | provenance | projected af |
|---:|---|---|---|---|---|---|
| 1 | `lem-routef-raw-factor-norms` | Raw factor-map norms: with \(C_V,C_T,\rho_T\) from (1.1), for \(0\le\eta\le\rho_T\), every amplification satisfies \((1-C_V\eta)\lVert X\rVert\le\lVert\widetilde\Delta_nX\rVert\le(1+C_V\eta)\lVert X\rVert\) and \(\max\{\lVert\widetilde\Delta\rVert_{\rm cb},\lVert\widetilde\Upsilon\rVert_{\rm cb}\}\le1+C_T\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-routef-functional-calculus-closeness`; `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | TeX 2749-2753; K-ledger 154-190 | 8 / 3 |
| 2 | `lem-routef-raw-factor-units` | Raw factor-map units: for \(0\le\eta\le\rho_{\rm unit}:=\rho_T\), \(\max\{\lVert\widetilde\Delta(I)-I\rVert,\lVert\widetilde\Upsilon(I)-I\rVert\}\le C_T\eta\). | same as row 1 | row 1; **`lem-routef-ai-defect-linearization`**; `lem-thmainext-conditional` | TeX 2754-2757; K-ledger 169-181; audit 160-162 | 4 / 2 |
| 3 | `lem-routef-raw-factor-identities` | Raw factor-map identities: for \(0\le\eta\le\rho_{\rm id}:=\min\{\rho_{\rm AI},\varepsilon_E/C_A\}\), \(\widetilde\Delta\widetilde\Upsilon=\widetilde\Phi\) and \(\widetilde\Upsilon\widetilde\Delta=I_{\mathcal B}\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | **`lem-kitaev-almost-idemp-audit`**; `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | TeX 2749-2753; K-ledger 183-187; audit 163-165 | 3 / 2 |
| 4 | `lem-routef-raw-product-estimate` | Raw \(\widetilde\Delta\)-product estimate: for \(0\le\eta\le\rho_{\rm prod}:=\rho_T\), every amplification and all \(X,Y\) satisfy \(\lVert\widetilde\Phi_n(\widetilde\Delta_nX\,\widetilde\Delta_nY)-\widetilde\Delta_n(XY)\rVert\le C_T\eta\lVert X\rVert\lVert Y\rVert\). | same as row 1 | row 1; row 3; **`lem-routef-ai-defect-linearization`**; `lem-thmainext-conditional` | TeX 2754-2766; K-ledger 174-181; audit 166-168 | 4 / 2 |
| 5 | `lem-routef-delta-prime-closeness` | Delta-prime CP closeness: with \(C_{\Delta'}:=C_T+4C_\theta\) and \(\rho_{\Delta'}:=\min\{\rho_T,\rho_{\rm prod}\}\), for \(0\le\eta\le\rho_{\Delta'}\), the repaired norm-one diagonal produces a CP map \(\Delta'\) with \(\lVert\Delta'-\widetilde\Delta\rVert_{\rm cb}\le C_{\Delta'}\eta\). | `def-fd-cstar-diagonal`; `def-extended-epsilon-cstar-algebra` | `cor-kitaev-diagonal-cpization`; `lem-routef-functional-calculus-closeness`; **`lem-thmainext-conditional`**; rows 1 and 4 | TeX 2771-2801; K-ledger 193-226; `argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9`; audit 169-171 | 6 / 3 |
| 6 | `lem-routef-delta-normalization-closeness` | Delta UCP normalization: with \(C_\Delta:=6C_T+7C_{\Delta'}\) and \(\rho_\Delta:=\min\{\rho_{\rm unit},\rho_{\Delta'},[2(C_T+C_{\Delta'})]^{-1}\}\), for \(0\le\eta\le\rho_\Delta\), \(a=\Delta'(I)\) is invertible and \(\Delta(X)=a^{-1/2}\Delta'(X)a^{-1/2}\) is UCP with \(\lVert\Delta-\widetilde\Delta\rVert_{\rm cb}\le C_\Delta\eta\). | `def-extended-epsilon-cstar-algebra` | rows 2 and 5 | TeX 2797-2801; K-ledger 246-259,415-448; G-verdict 141-145,287-290 | 5 / 3 |
| D2 | `lem-routef-degree-two-estimate` | Route F degree-two estimate: with \(C_2:=C_{\Delta'}+4C_\Delta\) and \(\rho_2:=\min\{\rho_{\rm prod},\rho_{\Delta'},\rho_\Delta\}\), for \(0\le\eta\le\rho_2\), every amplification satisfies \(\lVert\Phi_n(\Delta_nX\,\Delta_nY)-\Delta_n(XY)\rVert\le C_2\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | **`lem-routef-functional-calculus-closeness`**; rows 1, 4, 5, and 6 | TeX 2803-2812; K-ledger 193-226; G-verdict 119-128; audit 217-227 | 5 / 3 |
| 7 | `lem-routef-delta-phi-product` | Normalized Delta product: for \(\rho_{\Delta\Phi}:=\min\{\rho_\theta,\rho_\Delta,\rho_2\}\) and \(0\le\eta\le\rho_{\Delta\Phi}\), every amplification satisfies \(\lVert\widetilde\Phi_n(\Delta_nX\,\Delta_nY)-\widetilde\Delta_n(XY)\rVert\le(C_2+C_\theta+C_\Delta)\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; row 6; D2 | K-ledger 374-383; TeX 2803-2812 | 4 / 2 |
| D3 | `lem-routef-degree-three-estimate` | Route F degree-three estimate: with \(C_3:=10+20C_\Delta+12C_\theta+2C_{\Delta'}\) and \(\rho_3:=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}\), for \(0\le\eta\le\rho_3\), every amplification satisfies \(\lVert\Phi_n(\Delta_nX\,\Delta_nY\,\Delta_nZ)-\Delta_n(XYZ)\rVert\le C_3\eta\lVert X\rVert\lVert Y\rVert\lVert Z\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-kitaev-almost-idemp-audit`; `lem-routef-functional-calculus-closeness`; rows 1, 5, and 6; D2 | TeX 2813-2829; K-ledger 193-226; G-verdict 119-128; audit 229-242 | 7 / 3 |
| 8 | `lem-routef-upsilon-prime-closeness` | Upsilon-prime CP closeness: with \(C_N,C_R,C_L,C_{\Upsilon'}\) from (1.3) and \(\rho_{\Upsilon'}:=\min\{\rho_T,\rho_{\rm id},\rho_\Delta,\rho_2,\rho_3,(2C_R)^{-1}\}\), for \(0\le\eta\le\rho_{\Upsilon'}\), every Choi multiplicity space used below is nonzero and the componentwise construction produces CP \(\Upsilon'\) with \(\lVert\Upsilon'-\widetilde\Upsilon\rVert_{\rm cb}\le C_{\Upsilon'}\eta\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; rows 1, 3, and 6; D2 and D3 | TeX 2831-2895; K-ledger 228-245; audit 181-209 | 11 / 3 |
| 9 | `lem-routef-upsilon-normalization-closeness` | Upsilon UCP normalization: with \(C_\Upsilon:=6C_T+7C_{\Upsilon'}\) and \(\rho_\Upsilon:=\min\{\rho_{\rm unit},\rho_{\Upsilon'},[2(C_T+C_{\Upsilon'})]^{-1}\}\), for \(0\le\eta\le\rho_\Upsilon\), \(b=\Upsilon'(I)\) is invertible and \(\Upsilon(X)=b^{-1/2}\Upsilon'(X)b^{-1/2}\) is UCP with \(\lVert\Upsilon-\widetilde\Upsilon\rVert_{\rm cb}\le C_\Upsilon\eta\). | `def-extended-epsilon-cstar-algebra` | rows 2 and 8 | TeX 2895-2899; K-ledger 246-259,415-448; G-verdict 144-149,291-295 | 5 / 3 |
| 10 | `lem-routef-delta-upsilon-telescope` | Delta-Upsilon telescope: for \(\rho_{\Delta\Upsilon}:=\min\{\rho_\theta,\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}\) and \(0\le\eta\le\rho_{\Delta\Upsilon}\), \(\lVert\Delta\Upsilon-\Phi\rVert_{\rm cb}\le(C_\theta+C_\Delta+2C_\Upsilon)\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; rows 1, 3, 6, and 9 | K-ledger 345-372; G-verdict 96-117 | 4 / 2 |
| 11 | `lem-routef-multiplicative-telescope` | Multiplicative telescope: for \(\rho_{\rm mult}:=\min\{\rho_T,\rho_{\rm id},\rho_{\Delta\Phi},\rho_\Upsilon\}\) and \(0\le\eta\le\rho_{\rm mult}\), every amplification satisfies \(\lVert\Upsilon_n(\Delta_nX\,\Delta_nY)-XY\rVert\le[C_\Upsilon+2(C_2+C_\theta+C_\Delta)]\eta\lVert X\rVert\lVert Y\rVert\). | same as row 10 | rows 1, 3, 7, and 9 | K-ledger 345-383; G-verdict 96-117 | 4 / 2 |
| 12 | `lem-routef-upsilon-delta-telescope` | Upsilon-Delta telescope: for \(\rho_{\Upsilon\Delta}:=\min\{\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}\) and \(0\le\eta\le\rho_{\Upsilon\Delta}\), \(\lVert\Upsilon\Delta-I_{\mathcal B}\rVert_{\rm cb}\le(C_\Upsilon+2C_\Delta)\eta\). | `def-extended-epsilon-cstar-algebra` | rows 1, 3, 6, and 9 | K-ledger 345-372; G-verdict 96-117 | 3 / 2 |
| 13 | `lem-routef-k-finiteness` | Route F common coefficient/domain: \(K\) in (1.6) is finite and universal, and \(\rho_{\rm fac}\) in (1.7) is positive and is a common domain for the degree-two estimate and the three Route-F factorization estimates. | `def-extended-epsilon-cstar-algebra` | D2; rows 10, 11, and 12 | K-ledger 385-397; G-verdict 96-117 | 4 / 2 |
| 14 | `lem-routef-threshold-minimum` | Route F threshold minimum: importing the black-box constants \(C_E,\varepsilon_E\) used in rows 1-4, let \(\eta_K:=\min\{\rho_{\rm fac},(24K)^{-1},1\}\); then \(\eta_K>0\), and for \(0\le\eta\le\eta_K\) the three factorization estimates have common coefficient \(K\), the F2 and F3 smallness conditions hold, and the PRH finish is admissible. | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; `def-stochastic`; `def-positive-approximate-retract` | **`lem-thmainext-conditional`**; row 13; `lem-routef-f2-positive-unital-compression`; `lem-routef-f3-retract-defect`; `lem-routef-prh-finish` | audit 262-301; `argument/lemmas/lem-thmainext-conditional.md:4-9`; F2/F3/PRH shards:4-9 | 5 / 2 |

### Terminal-row status note

Row 14 consumes `lem-thmainext-conditional` **at its contract level** as the
producer of \(C_E,\varepsilon_E\). That producer remains
`proved-mod-audit`, design-blocked for eventual L0 closure; using its
contract in this design does not promote it. Any eventual af elevation of
`lem-routef-threshold-minimum` must list it as a dependency and therefore
inherits its status restriction under the linker rules.

Two audit facts remain true on the separate MAIN front:

1. there is no landed
   `argument/lemmas/lem-maincb-reset-constant-ledger.md`; and
2. the v4.1 proposed reset at
   `DESIGN-FUDW-DECOMP-v4.1.md:216` omits the
   \(\varepsilon_{\max}^{\rm cb}\) hypothesis now present in
   `argument/lemmas/lem-maincb-error-improvement.md:4,13-19`.

Those are W76 / GAP-MAIN-STRUCTURE findings. They are cross-referenced here
but are **not** blockers for this relative-ledger design, because the
existing `lem-thmainext-conditional` interface already packages a positive
admissible \(\varepsilon_E\).

## 3. Per-row radius derivation

### 3.1 Raw rows 1-4

On
\(\eta\le\min\{\rho_{\rm AI},\varepsilon_E/C_A\}\), the AI algebra has
defect at most \(C_A\eta\le\varepsilon_E\), so the black-box MAIN contract
gives an extended \(C_EC_A\eta\)-isomorphism \(v\). Enlarging its
coefficient to \(C_V\) gives
\[
(1-C_V\eta)\|X\|\le\|v_nX\|\le(1+C_V\eta)\|X\|.
\]
With \(\widetilde\Delta=v\) and
\(\widetilde\Upsilon=v^{-1}\widetilde\Phi\), (1.1) gives
\[
\frac{1+C_\theta\eta}{1-C_V\eta}
\le1+(C_\theta+3C_V)\eta=1+C_T\eta.
\]
This proves row 1 on \(\rho_T\).

For row 2, the AI row identifies the exact functional-calculus projector
and its unit, while the MAIN contract supplies the unital extended
isomorphism. Hence
\[
\|\widetilde\Upsilon(I)-I\|
\le\frac{C_V\eta}{1-C_V\eta}
\le3C_V\eta\le C_T\eta.
\]
The direct AI import is retained because row 1 exports norm bounds, not the
unit identity.

For row 3, `lem-kitaev-almost-idemp-audit` supplies
\(\widetilde\Phi^2=\widetilde\Phi\); the AI row supplies its range
\(\mathcal A\); and the MAIN map is onto \(\mathcal A\). Therefore
\(\widetilde\Delta\widetilde\Upsilon=\widetilde\Phi\) and
\(\widetilde\Upsilon\widetilde\Delta=I_{\mathcal B}\) on
\(\rho_{\rm id}\). The direct Kitaev import is necessary because neither
of the other displayed contracts exports idempotence.

For row 4, the AI row supplies the Choi-Effros product and the MAIN
extended-isomorphism estimate gives
\[
\|\widetilde\Phi_n(v_nX\,v_nY)-v_n(XY)\|
\le C_EC_A\eta\|X\|\|Y\|
\le C_T\eta\|X\|\|Y\|.
\]
The direct AI import is necessary because rows 1 and 3 do not export that
product structure.

### 3.2 Delta rows, D2, row 7, and D3

For row 5, the repaired whole-algebra diagonal is a probability average of
projective norm one. Row 4 costs \(C_T\eta\), and replacing
\(\widetilde\Phi\) by \(\Phi\) on two raw factors of cb norm at most \(2\)
costs \(4C_\theta\eta\). Thus
\[
C_{\Delta'}=C_T+4C_\theta.
\]
The direct MAIN import supplies involution preservation of
\(\widetilde\Delta\), which the CP-ization contract consumes and rows 1 and
4 do not export.

Rows 2 and 5 imply
\[
\|\Delta'(I)-I\|\le(C_T+C_{\Delta'})\eta.
\]
The explicit guard in \(\rho_\Delta\) makes this at most \(1/2\). The
uniform inverse-square-root calculation then gives
\[
6(C_T+C_{\Delta'})+C_{\Delta'}
=6C_T+7C_{\Delta'}=C_\Delta,
\]
which closes row 6.

For D2, the four fixed comparisons give
\[
C_2=C_{\Delta'}+4C_\Delta
\]
on the intersection \(\rho_2\). The direct functional-calculus import
supplies the comparison \(\widetilde\Phi\to\Phi\); none of rows 1, 4, 5, or
6 exports it.

For row 7, insert \(\Phi\) and \(\Delta\):
\[
\begin{aligned}
\|\widetilde\Phi(\Delta X\Delta Y)-\widetilde\Delta(XY)\|
&\le\|(\widetilde\Phi-\Phi)(\Delta X\Delta Y)\|\\
&\quad+\|\Phi(\Delta X\Delta Y)-\Delta(XY)\|\\
&\quad+\|(\Delta-\widetilde\Delta)(XY)\|.
\end{aligned}
\]
UCP contractivity of \(\Delta\) yields the coefficient
\(C_\theta+C_2+C_\Delta\) on \(\rho_{\Delta\Phi}\).

For D3, the Kitaev audit gives the \(10\eta\) associativity input on
\(\rho_\theta=1/8<1/4\). The five comparisons at TeX 2817-2829 yield
\[
C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'}
\]
on \(\rho_3\). No \(\Upsilon\)-row is used in D2 or D3.

### 3.3 Corrected componentwise \(\Upsilon'\) row

Rows 1 and 6 give, at every amplification,
\[
\|\Delta_nX\|
\ge(1-C_V\eta-C_\Delta\eta)\|X\|
=(1-C_N\eta)\|X\|.
\tag{3.1}
\]
For the \(j\)-th Choi block, TeX 2840-2857 and D2 then give
\[
R_j=I_{\mathcal L_j}\otimes C_j,\qquad
0\le C_j\le I,\qquad
\|C_j\|\ge1-(C_N+C_2)\eta=1-C_R\eta.
\tag{3.2}
\]
The new guard \(\eta\le(2C_R)^{-1}\) makes
\(\|C_j\|\ge1/2\). Therefore \(C_j\ne0\), hence its multiplicity space
\(\mathcal E_j\ne\{0\}\). Since the space is finite-dimensional, there is
a unit vector \(\xi_j\in\mathcal E_j\) attaining \(\|C_j\|\). For that
vector,
\[
\begin{aligned}
1-\langle\xi_j,C_j^*C_j\xi_j\rangle
&=1-\|C_j\|^2\\
&\le1-(1-C_R\eta)^2
\le2C_R\eta.
\end{aligned}
\tag{3.3}
\]
This is the missing logical step in the first design.

The middle component comparison costs \(C_2+C_3+2C_R=C_L\), so
\[
\|\Upsilon'\Delta-I_{\mathcal B}\|_{\rm cb}\le C_L\eta.
\tag{3.4}
\]
The final five comparisons cost
\(1,C_\theta,0,2C_\Delta,2C_L\), giving
\[
C_{\Upsilon'}=1+C_\theta+2C_\Delta+2C_L.
\]
Probability averages contribute no term count, and the direct-sum target
uses the maximum norm. Thus the new guard proves existence of the chosen
vectors without introducing a dimension-dependent coefficient.

### 3.4 Row 9, telescopes, and row 13

Rows 2 and 8 give
\[
\|\Upsilon'(I)-I\|\le(C_T+C_{\Upsilon'})\eta.
\]
The guard in \(\rho_\Upsilon\) makes this at most \(1/2\), and the same
normalization arithmetic as for \(\Delta\) gives
\[
C_\Upsilon
=6(C_T+C_{\Upsilon'})+C_{\Upsilon'}
=6C_T+7C_{\Upsilon'}.
\]

Using the exact row-3 identities, the three fixed telescopes give,
respectively,
\[
\begin{aligned}
K_{\Delta\Upsilon}&=C_\theta+C_\Delta+2C_\Upsilon,\\
K_{\rm mult}&=C_\Upsilon+2(C_2+C_\theta+C_\Delta),\\
K_{\Upsilon\Delta}&=C_\Upsilon+2C_\Delta.
\end{aligned}
\tag{3.5}
\]
Their domains are exactly the intersections in (1.5). Row 13 takes the
maximum of \(1\) and these three coefficients and the minimum of the four
named factor domains. The new \((2C_R)^{-1}\) guard propagates through
\[
\rho_{\Upsilon'}
\longrightarrow\rho_\Upsilon
\longrightarrow
\rho_{\Delta\Upsilon},\rho_{\rm mult},\rho_{\Upsilon\Delta}
\longrightarrow\rho_{\rm fac};
\]
hence it composes through all telescopes and \(K\)-finiteness.

### 3.5 Terminal threshold

The row-13 output gives all three factorization estimates with common
coefficient \(K\) on \(\rho_{\rm fac}\). The additional condition
\(\eta\le(24K)^{-1}\) is exactly the F2 threshold. It also gives
\[
3K\eta\le\frac18<1,
\]
so F3's denominator is positive, and
\[
\frac{3K\eta}{1-3K\eta}
\le4K\eta\le\frac16<\frac12,
\]
which is the bound consumed by the PRH finish. The entry \(1\) is the
remaining explicit F2/PRH guard. Thus (1.8) closes row 14.

The MAIN smallness is already upstream: \(\rho_T\le\varepsilon_E/C_A\),
and \(\rho_{\rm fac}\le\rho_T\) by the expansion in §4. No reset constant
is needed at this abstraction boundary.

## 4. Independent acyclicity and finite-minimum audit

### 4.1 Acyclicity

Deleting external registry leaves, the corrected internal edges are
\[
\begin{array}{rcl}
2&\leftarrow&1,\\
4&\leftarrow&1,3,\\
5&\leftarrow&1,4,\\
6&\leftarrow&2,5,\\
\mathrm{D2}&\leftarrow&1,4,5,6,\\
7&\leftarrow&6,\mathrm{D2},\\
\mathrm{D3}&\leftarrow&1,5,6,\mathrm{D2},\\
8&\leftarrow&1,3,6,\mathrm{D2},\mathrm{D3},\\
9&\leftarrow&2,8,\\
10&\leftarrow&1,3,6,9,\\
11&\leftarrow&1,3,7,9,\\
12&\leftarrow&1,3,6,9,\\
13&\leftarrow&\mathrm{D2},10,11,12,\\
14&\leftarrow&13.
\end{array}
\]
Therefore
\[
1,2,3,4,5,6,\mathrm{D2},7,\mathrm{D3},8,9,10,11,12,13,14
\]
is a topological order. Every added import is an external leaf or points to
an earlier row. There is no forward, dangling, or circular radius edge.
`lem-routef-k-finiteness` and `lem-routef-threshold-minimum` remain the last
two reserved rows.

### 4.2 Fully expanded finite minimum

Recursively expanding \(\rho_{\rm fac}\) gives precisely the following
primitive guard family:
\[
\mathfrak G_{\rm fac}=
\left\{
\rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)},
\frac1{2(C_T+C_{\Delta'})},
\frac1{2C_R},
\frac1{2(C_T+C_{\Upsilon'})}
\right\}.
\tag{4.1}
\]
In particular, the corrected Choi guard \((2C_R)^{-1}\) is not lost in a
downstream telescope. Consequently,
\[
\eta_K=\min\left(
\mathfrak G_{\rm fac}\cup
\left\{\frac1{24K},1\right\}
\right).
\tag{4.2}
\]

This audit is:

1. **finite:** (4.2) contains ten entries;
2. **produced:** functional calculus produces
   \(\rho_\theta,C_\theta\); AI produces \(\rho_{\rm AI},C_A\); the
   black-box MAIN contract produces \(C_E,\varepsilon_E\); rows 1, 5, 6,
   D2, D3, 8, 9, and 13 produce the remaining displayed coefficients and
   aggregators;
3. **non-circular:** \(C_R\) uses only \(C_V,C_\Delta,C_2\), all produced
   before row 8; \(C_{\Upsilon'}\) is computed before row 9; \(K\) uses
   only telescope coefficients and does not depend on \(\eta_K\);
4. **nonempty:** it is a minimum of ten entries; and
5. **positive:** \(\rho_\theta,\rho_{\rm AI},\varepsilon_E\) are positive,
   \(C_A,C_V,C_T,C_{\Delta'},C_\Delta,C_2,C_3,C_R,C_{\Upsilon'},K\) are
   finite with \(C_A,C_R,K>0\), and every denominator in (4.2) is strictly
   positive.

No reset-ledger output, unnamed \(O(\eta)\) radius, or future \(\eta_K\)
occurs in (4.1).

## 5. Independent dimension-freeness audit

| rows | dimension-freeness check |
|---|---|
| 1-4 | \(C_\theta,C_A\) are amplification-uniform. The `lem-thmainext-conditional` contract explicitly makes \(C_E,\varepsilon_E\) independent of dimension, amplification, and block data. Scalar sums, products, maxima, and minima preserve that property. |
| 5 | The repaired diagonal is a probability average of projective norm one. Neither the number of diagonal terms nor the number or sizes of simple blocks appears. |
| 6 | The inverse-square-root estimate is uniform on the fixed \(1/2\)-ball. |
| D2, 7, D3 | These are fixed-length amplified/cb telescopes. The associativity coefficient \(10\) is uniform at every amplification. |
| 8 | The new guard proves \(\mathcal E_j\ne0\) uniformly. Finite-dimensional norm attainment chooses a vector but contributes no coefficient. Probability averages and the direct-sum maximum norm introduce no term count, block count, block dimension, or amplification factor. |
| 9 | The same scalar \(1/2\)-ball normalization is taken in the direct-sum maximum norm. |
| 10-12 | Each is a fixed two- or three-term cb telescope. |
| 13 | A maximum and minimum of finitely many universal quantities cannot introduce data dependence. |
| 14 | \(\eta_K\) is a minimum of the universal \(\rho_{\rm fac}\), \((24K)^{-1}\), and \(1\); the F2, F3, and PRH contracts introduce variables \(n,k\) but no \(n\)- or \(k\)-dependent constant. |

**ROUTE-LEVEL ALARM CHECK: NONE.** No corrected coefficient or radius
depends on \(n\), amplification level, number of simple summands, block
dimension, or MAIN stage index.

## 6. Reconnection map

### 6.1 Degree rows

The audit-prescribed corrected lists are:

```text
lem-routef-degree-two-estimate:
  deps:
    lem-routef-functional-calculus-closeness
    lem-routef-raw-factor-norms
    lem-routef-raw-product-estimate
    lem-routef-delta-prime-closeness
    lem-routef-delta-normalization-closeness
```

```text
lem-routef-degree-three-estimate:
  deps:
    lem-kitaev-almost-idemp-audit
    lem-routef-functional-calculus-closeness
    lem-routef-raw-factor-norms
    lem-routef-delta-prime-closeness
    lem-routef-delta-normalization-closeness
    lem-routef-degree-two-estimate
```

These are **DESIGN ONLY / DO NOT TRANSCRIBE** pending a fresh hostile pass
and user authorization.

### 6.2 Proposed parent wiring

After and only after all fourteen rows pass hostile review and are
authorized to land, the proposed complete replacement dependency list for
`lem-routef-k-ledger` is:

```text
lem-routef-k-ledger:
  deps:
    lem-routef-delta-upsilon-telescope
    lem-routef-multiplicative-telescope
    lem-routef-upsilon-delta-telescope
    lem-routef-k-finiteness
    lem-routef-threshold-minimum
    lem-routef-f2-positive-unital-compression
    lem-routef-f3-retract-defect
    lem-routef-prh-finish
```

**DO NOT REWIRE OR SEED.** This is proposed wiring only. The current parent
contract and registry remain unchanged.

## 7. Disposition of binding audit findings

| audit finding | disposition | clearing locus |
|---|---|---|
| Row 8 did not prove \(\mathcal E_j\ne0\) before choosing \(\xi_j\). | **CLEARED-BY** | (1.3)-(1.4), table row 8, and §3.3: \(\eta\le(2C_R)^{-1}\) gives \(\|C_j\|\ge1/2\), hence \(\mathcal E_j\ne0\). |
| Row 2 omitted direct `lem-routef-ai-defect-linearization`. | **CLEARED-BY** | Table row 2 and §3.1; import added verbatim. |
| Row 3 omitted direct `lem-kitaev-almost-idemp-audit`. | **CLEARED-BY** | Table row 3 and §3.1; import added verbatim. |
| Row 4 omitted direct `lem-routef-ai-defect-linearization`. | **CLEARED-BY** | Table row 4 and §3.1; import added verbatim. |
| Row 5 omitted direct `lem-thmainext-conditional`. | **CLEARED-BY** | Table row 5 and §3.2; import added verbatim. |
| D2 omitted direct `lem-routef-functional-calculus-closeness`. | **CLEARED-BY** | Table D2 and §§3.2, 6.1; import added verbatim. |
| The terminal GAP was overstated. | **CLEARED-BY** | (1.8), table row 14, §§3.5 and 4.2: \(\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}>0\). |
| The threshold must consume `lem-thmainext-conditional` at contract level without promotion. | **CLEARED-BY** | Table row 14 direct dependency and the terminal-row status note. |
| Reset-shard absence and the omitted \(\varepsilon_{\max}^{\rm cb}\) guard remain real MAIN findings, not ledger blockers. | **CLEARED-BY / CROSS-REFERENCED** | Terminal-row status note; retained for W76 / GAP-MAIN-STRUCTURE and excluded from \(\eta_K\). |
| Recheck serial well-foundedness and finite minima. | **CLEARED-BY** | §4 gives an explicit topological order and the ten-entry primitive minimum. |
| Recheck dimension-freeness, especially the \(\Upsilon'\) selection. | **CLEARED-BY** | §§3.3 and 5; no route-level alarm. |

No binding finding is refuted or escalated. A fresh hostile audit is still
required before any landing decision.

## 8. Design landing decision

- All fourteen reserved rows: **CLOSED AS A DESIGN**, with no status
  promotion.
- D2 and D3: dependency lists corrected and acyclic, still design-only.
- `lem-routef-k-ledger`: complete parent wiring proposed, not enacted.
- Entire family: **DO NOT SHARD, SEED, REWIRE, OR PROMOTE UNTIL A FRESH
  HOSTILE AUDIT PASSES AND THE USER AUTHORIZES LANDING.**
