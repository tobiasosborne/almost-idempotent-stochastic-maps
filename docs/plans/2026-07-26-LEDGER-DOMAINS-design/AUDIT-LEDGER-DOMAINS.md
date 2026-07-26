# AUDIT — hostile verification of the LEDGER-DOMAINS design

Date: 2026-07-26  
Role: fresh independent hostile auditor  
Status: **NON-RIGOROUS AUDIT / DESIGN ONLY / DO NOT SHARD, SEED, REWIRE, OR PROMOTE**

## 0. Disposition

**REDESIGN.**

The proposed disposition `LAND-13-HOLD-1` does not survive audit.

1. One of the thirteen claimed-closable rows has an insufficient radius.
   In `lem-routef-upsilon-prime-closeness`, the proof chooses a unit vector
   \(\xi_j\in\mathcal E_j\), but the proposed radius does not ensure that the
   Choi multiplicity space \(\mathcal E_j\) is nonzero. The exact local repair
   is to add \((2C_R)^{-1}\) to \(\rho_{\Upsilon'}\), where
   \(C_R=C_V+C_\Delta+C_2\).
2. Four raw/Delta rows and the degree-two reconnection omit direct imports
   used by their displayed derivations. These are exact dependency-list
   corrections, not new mathematical estimates.
3. Conversely, the claimed terminal GAP is **overstated**. The design uses
   the landed `lem-thmainext-conditional` contract as a black box in rows
   1--4. That contract already produces \(C_E,\varepsilon_E\), and row 1
   already places \(\varepsilon_E/C_A\) in \(\rho_T\). Consequently, after
   correcting row 8, the terminal row closes as
   \[
   \eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}>0
   \]
   without importing the internal MAIN reset package.

The reset shard really is absent, and the v4.1 reset formula really omits the
new \(\varepsilon_{\max}^{\rm cb}\) guard. Those two facts do **not** imply
that the relative Route-F threshold is unproducible from the registry
interfaces the design itself chose. There is no dimension-freeness alarm.

## 1. Sources and binding checks

Abbreviations below:

- **Design**:
  `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS.md`.
- **v4.1**:
  `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`.
- **v3 verdict**:
  `docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP-V3.md`.
- **K-ledger**:
  `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md`.
- **G-verdict**:
  `docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-G-KLEDGER.md`.
- **TeX**: `refs/kitaev-2405.02434/approximate_algebras.tex`.

The binding warning is exactly as represented: the fourteen rows were
withdrawn because \(\eta_A\) was used outside AI linearization and separate
MAIN, normalization, degree, and terminal domains were missing
(v3 verdict:69-102). The reservations and the two normalization guards are
at v4.1:250-275 and v4.1:596-600. The degree mechanisms and constants are
confirmed at TeX:2803-2829 and G-verdict:119-128.

The current registry facts are:

- `lem-routef-functional-calculus-closeness` gives
  \(C_\theta=12(\sqrt2-1)\) on \(0\le\eta\le1/8\)
  (`argument/lemmas/lem-routef-functional-calculus-closeness.md:4-9`).
- `lem-routef-ai-defect-linearization` gives \(C_A\), \(\eta_A>0\), and
  \(\varepsilon_{\rm AI}(\eta)\le C_A\eta\)
  (`argument/lemmas/lem-routef-ai-defect-linearization.md:4-9`).
- `lem-thmainext-conditional` gives universal \(C_E<\infty\) and
  \(\varepsilon_E>0\), independent of dimension, amplification, and block
  data (`argument/lemmas/lem-thmainext-conditional.md:4-9`).
- `lem-maincb-error-improvement` now requires both a finite-dimensional
  source and \(\varepsilon\le\varepsilon_{\max}^{\rm cb}\)
  (`argument/lemmas/lem-maincb-error-improvement.md:4,13-19`).
- `lem-maincb-reset-constant-ledger` has no shard and no registry row:
  the only lemma-shard occurrence is the prospective-consumer note at
  `argument/lemmas/lem-maincb-error-improvement.md:34-37`; the generated
  index contains `lem-maincb-error-improvement` at `argument/INDEX.md:175`
  and no reset-ledger row.

## 2. Independent radius recomputation

Write
\[
\rho_\theta=\frac18,\qquad
\rho_{\rm AI}=\eta_A,\qquad
\bar C_E=\max\{1,C_E\},\qquad
C_V=\bar C_EC_A,\qquad C_T=C_\theta+3C_V .
\]
The first common factor radius recomputes to
\[
\rho_T=\min\left\{
\rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)}
\right\}.
\tag{2.1}
\]
Indeed, the last two entries imply \(C_\theta\eta,C_V\eta\le1/4\).
The extended-isomorphism norm lower bound and
\[
\frac{1+C_\theta\eta}{1-C_V\eta}
\le1+(C_\theta+3C_V)\eta
\]
then give the raw cb bounds. This is a legitimate local replacement for
K-ledger:154-190 and respects R24.

The remaining recomputed constants and radii are
\[
\begin{aligned}
\rho_{\rm unit}&=\rho_T,\\
\rho_{\rm id}&=\min\{\rho_{\rm AI},\varepsilon_E/C_A\},\\
\rho_{\rm prod}&=\rho_T,\\
C_{\Delta'}&=C_T+4C_\theta,&
\rho_{\Delta'}&=\min\{\rho_T,\rho_{\rm prod}\},\\
C_\Delta&=6C_T+7C_{\Delta'},&
\rho_\Delta&=\min\left\{\rho_{\rm unit},\rho_{\Delta'},
\frac1{2(C_T+C_{\Delta'})}\right\},\\
C_2&=C_{\Delta'}+4C_\Delta,&
\rho_2&=\min\{\rho_{\rm prod},\rho_{\Delta'},\rho_\Delta\},\\
\rho_{\Delta\Phi}&=\min\{\rho_\theta,\rho_\Delta,\rho_2\},\\
C_3&=10+20C_\Delta+12C_\theta+2C_{\Delta'},&
\rho_3&=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}.
\end{aligned}
\tag{2.2}
\]
The \(4C_\theta\) in \(C_{\Delta'}\) is the cost of replacing
\(\widetilde\Phi\) by \(\Phi\) on two raw factors of cb norm at most \(2\)
(TeX:2786-2801; K-ledger:193-226). The two normalization guards are exactly
the unit-defect sums demanded by G-verdict:130-149, not the withdrawn
\((2C_{\Delta'})^{-1}\) and \((2C_{\Upsilon'})^{-1}\) guards. The formulas
for \(C_2,C_3\) agree with the hostile recomputation
(G-verdict:119-128; TeX:2803-2829).

For the componentwise row, put
\[
C_N=C_V+C_\Delta,\qquad
C_R=C_N+C_2,\qquad
C_L=C_2+C_3+2C_R,
\]
\[
C_{\Upsilon'}=1+C_\theta+2C_\Delta+2C_L.
\tag{2.3}
\]
The **corrected**, dependency-produced radius is
\[
\boxed{\rho_{\Upsilon'}^{\,\rm corr}
=\min\left\{\rho_T,\rho_{\rm id},\rho_\Delta,\rho_2,\rho_3,
\frac1{2C_R}\right\}.}
\tag{2.4}
\]
Then continue with
\[
\begin{aligned}
C_\Upsilon&=6C_T+7C_{\Upsilon'},\\
\rho_\Upsilon&=\min\left\{\rho_{\rm unit},
\rho_{\Upsilon'}^{\,\rm corr},
\frac1{2(C_T+C_{\Upsilon'})}\right\},\\
\rho_{\Delta\Upsilon}
&=\min\{\rho_\theta,\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\},\\
\rho_{\rm mult}
&=\min\{\rho_T,\rho_{\rm id},\rho_{\Delta\Phi},\rho_\Upsilon\},\\
\rho_{\Upsilon\Delta}
&=\min\{\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}.
\end{aligned}
\tag{2.5}
\]
Finally,
\[
\begin{aligned}
K=\max\{&1,\ C_\theta+C_\Delta+2C_\Upsilon,\\
&C_\Upsilon+2(C_2+C_\theta+C_\Delta),\
C_\Upsilon+2C_\Delta\},\\
\rho_{\rm fac}
&=\min\{\rho_2,\rho_{\Delta\Upsilon},
\rho_{\rm mult},\rho_{\Upsilon\Delta}\}.
\end{aligned}
\tag{2.6}
\]
These are finite expressions in named earlier constants. The three
telescope coefficients agree with K-ledger:345-397 and
G-verdict:96-117.

## 3. Verdict on every reserved row

| row | id | verdict | recomputation / exact correction |
|---:|---|---|---|
| 1 | `lem-routef-raw-factor-norms` | **VALID** | Radius (2.1). The two \(1/[4(1+C)]\) guards are slightly stronger than the raw \(1/(4C)\) guards and are safe. |
| 2 | `lem-routef-raw-factor-units` | **VALID-WITH-CORRECTIONS** | \(\rho_{\rm unit}=\rho_T\) is correct. Add direct dep `lem-routef-ai-defect-linearization`, used to identify \(\widetilde\Phi\) and obtain \(\widetilde\Phi(I)=I\); row 1's contract exports only norm bounds. |
| 3 | `lem-routef-raw-factor-identities` | **VALID-WITH-CORRECTIONS** | \(\rho_{\rm id}\) is correct. Add direct dep `lem-kitaev-almost-idemp-audit`, whose contract actually exports \(\widetilde\Phi^2=\widetilde\Phi\) (`argument/lemmas/lem-kitaev-almost-idemp-audit.md:4-9`). |
| 4 | `lem-routef-raw-product-estimate` | **VALID-WITH-CORRECTIONS** | \(\rho_{\rm prod}=\rho_T\), coefficient \(C_T\) are safe. Add direct dep `lem-routef-ai-defect-linearization`, whose conclusion supplies the Choi--Effros product used with the extended isomorphism. |
| 5 | `lem-routef-delta-prime-closeness` | **VALID-WITH-CORRECTIONS** | \(C_{\Delta'}\), \(\rho_{\Delta'}\) recompute. Add direct dep `lem-thmainext-conditional`: CP-ization requires \(\widetilde\Delta\) to preserve the involution (`argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9`), a fact not exported by rows 1 or 4. |
| 6 | `lem-routef-delta-normalization-closeness` | **VALID** | The guard makes \(\|\Delta'(I)-I\|\le1/2\); \(6(C_T+C_{\Delta'})+C_{\Delta'}=C_\Delta\). This is exactly G-verdict:141-145,287-290. |
| 7 | `lem-routef-delta-phi-product` | **VALID** | The three costs are \(C_\theta,C_2,C_\Delta\) on \(\rho_{\Delta\Phi}\). Valid after the D2 dep correction below. |
| 8 | `lem-routef-upsilon-prime-closeness` | **VALID-WITH-CORRECTIONS** | Replace the displayed radius by (2.4). The design's radius is insufficient; detailed defect below. Constants (2.3) recompute correctly. |
| 9 | `lem-routef-upsilon-normalization-closeness` | **VALID** | On corrected row 8, the guard gives \(\|\Upsilon'(I)-I\|\le1/2\) and \(C_\Upsilon=6C_T+7C_{\Upsilon'}\), matching G-verdict:144-149,291-295. |
| 10 | `lem-routef-delta-upsilon-telescope` | **VALID** | Coefficient \(C_\theta+C_\Delta+2C_\Upsilon\) and radius in (2.5) recompute from the exact raw identity and cb norm \(2\). |
| 11 | `lem-routef-multiplicative-telescope` | **VALID** | Coefficient \(C_\Upsilon+2(C_2+C_\theta+C_\Delta)\) and radius in (2.5) recompute. |
| 12 | `lem-routef-upsilon-delta-telescope` | **VALID** | Coefficient \(C_\Upsilon+2C_\Delta\) and radius in (2.5) recompute. |
| 13 | `lem-routef-k-finiteness` | **VALID** | \(K\) and \(\rho_{\rm fac}\) are finite, positive, universal, and depend only on earlier rows. |
| 14 | `lem-routef-threshold-minimum` | **REFUTED AS A GAP** | It closes from the design's own black-box MAIN interface with \(\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}\). No reset constant occurs. |

### The row-8 defect

TeX:2831-2837 represents \(\Delta\) by multiplicity spaces
\(\mathcal E_j\). TeX:2840-2857 proves
\[
\|C_j\|\ge1-(C_V+C_\Delta+C_2)\eta=1-C_R\eta .
\]
The design then chooses a unit vector \(\xi_j\in\mathcal E_j\)
(Design:275-284; TeX:2859-2869). But its proposed
\(\rho_{\Upsilon'}\) contains no guard forcing \(C_R\eta<1\).
The normalization radius only controls
\((C_T+C_{\Delta'})\eta\); since
\[
C_R=C_V+C_{\Delta'}+5C_\Delta,
\]
that does not force \(1-C_R\eta>0\). Thus the displayed lower bound can be
vacuous, \(\Delta\) need not be shown faithful on the \(j\)-th simple
summand, and \(\mathcal E_j\) may be zero. Norm attainment in a zero space
is impossible.

Adding \((2C_R)^{-1}\) proves \(\|C_j\|\ge1/2\), hence
\(\mathcal E_j\ne0\), and allows the required unit vector. For that vector,
\[
1-\langle\xi_j,C_j^*C_j\xi_j\rangle
\le1-(1-C_R\eta)^2\le2C_R\eta.
\]
The remaining middle costs are \(C_2+C_3\), so
\(C_L=C_2+C_3+2C_R\). The five final comparisons cost
\(1,C_\theta,0,2C_\Delta,2C_L\), yielding (2.3). This gives an exact,
dimension-free repair; it is not licensed to land here.

## 4. Degree rows and serial well-foundedness

The corrected degree dependencies are:

```text
lem-routef-degree-two-estimate:
  deps:
    lem-routef-functional-calculus-closeness
    lem-routef-raw-factor-norms
    lem-routef-raw-product-estimate
    lem-routef-delta-prime-closeness
    lem-routef-delta-normalization-closeness
```

The added functional-calculus dep is essential: the D2 telescope replaces
\(\widetilde\Phi\) by \(\Phi\), and none of the four proposed row contracts
exports that comparison. Its coefficient is still
\(C_2=C_{\Delta'}+4C_\Delta\) on \(\rho_2\).

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

This D3 list is correct. The \(10\eta\) associativity term is supplied on
\(\rho_\theta=1/8<1/4\), and the five comparisons give the displayed
\(C_3\) (TeX:2817-2829; G-verdict:119-128).

After the direct-import corrections and (2.4), the order is acyclic:
raw rows \(\to\Delta\) repair \(\to\) D2 \(\to\Delta\Phi\) and D3
\(\to\Upsilon'\to\Upsilon\to\) telescopes \(\to K\to\eta_K\).
The new guard uses only \(C_R\), produced before row 8. K-finiteness and
threshold-minimum remain the final two reserved rows. There is no forward,
dangling, or circular radius.

## 5. Audit of both alleged GAP causes

### Cause 1 — missing reset-ledger registry row: **VALID FACT, INVALID AS A CAUSE OF THIS GAP**

The shard and index row are absent, exactly as Design:17-22 claims. This
blocks any design that chooses to expose the internal MAIN reset arithmetic.
It does not block the present thirteen-row design, which invokes the landed
`lem-thmainext-conditional` contract and consumes only its outputs
\(C_E,\varepsilon_E\).

### Cause 2 — omitted \(\varepsilon_{\max}^{\rm cb}\): **VALID FACT, INVALID AS A CAUSE OF THIS GAP**

The v4.1 proposal defines
\[
\varepsilon_E^{\rm corr}
=\min\{\delta_{\max}^{\rm cb},e_H,e_{\rm ext},e_{\rm sel},e_{\rm split}\}
/C_{\rm pre}
\]
at v4.1:216, whereas the landed IMPROVE-CB row additionally requires
\(\varepsilon\le\varepsilon_{\max}^{\rm cb}\)
(`argument/lemmas/lem-maincb-error-improvement.md:4,13-19`).
Therefore the proposed internal reset package is indeed incomplete.

But the black-box `lem-thmainext-conditional` contract already asserts a
positive admissible \(\varepsilon_E\). Row 1 includes
\(\varepsilon_E/C_A\) in \(\rho_T\); rows 10--12 inherit \(\rho_T\); and
row 13 puts their domains into \(\rho_{\rm fac}\). Hence
\[
\boxed{\eta_K^{\rm corr}
=\min\{\rho_{\rm fac},(24K)^{-1},1\}>0}
\tag{5.1}
\]
simultaneously invokes `th_main_ext`, the three factorization estimates,
F2/F3, and PRH. The F2 and PRH thresholds are explicit at
`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4-9` and
`argument/lemmas/lem-routef-prh-finish.md:4-9`; \(3K\eta<1\) for F3 follows
from \(\eta\le(24K)^{-1}\).

Thus the two alleged causes expose a real defect in the *internal reset
proposal*, but the conclusion “row 14 cannot be derived from the current
registry” is false. If R27 is intended as a non-negotiable architectural
requirement to unpack MAIN rather than consume `lem-thmainext-conditional`,
then the design must say so and redesign rows 1--4 consistently. It cannot
use the black box to close thirteen rows and reject the same abstraction
only at the terminal minimum.

## 6. Dimension-freeness and reconnection

There is **no ROUTE-LEVEL ALARM**. All corrected radii are finite
sum/product/minimum expressions in universal registry constants. In row 8,
finite-dimensionality is used only for norm attainment. Once (2.4) proves
\(\mathcal E_j\ne0\), choosing a maximizing unit vector introduces no
dimension-dependent coefficient. Probability averages and the direct-sum
maximum norm introduce neither a term count nor a block count
(TeX:2840-2895; G-verdict:291-295).

The proposed parent wiring at Design:494-513 matches v4.1:348-364:
the three telescopes, K-finiteness, threshold-minimum, F2, F3, and PRH.
The guard remains:

**DO NOT REWIRE OR SEED.**

The family requires a corrected design and a new hostile pass before any
landing decision. Nothing in this audit promotes a claim or certifies a
proof as rigorous.
