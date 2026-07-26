# DESIGN — GAP-LEDGER-DOMAINS local-domain DAG

Date: 2026-07-26  
Role: fresh hostile design mathematician  
Status: **DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, REWIRE, OR PROMOTE**

## 0. Hostile verdict

**PARTIAL CLOSE, WITH ONE TERMINAL GAP.** Thirteen of the fourteen reserved
rows, together with the two degree-estimate consumers, admit a serial
dependency-produced local-domain design from the registry contracts that
actually exist. The fourteenth row,
`lem-routef-threshold-minimum`, is a **GAP**.

The GAP has two independently checkable causes.

1. The brief calls `lem-maincb-reset-constant-ledger` a landed shard, but
   there is no `argument/lemmas/lem-maincb-reset-constant-ledger.md` and no
   such row in `argument/INDEX.md`. The only occurrence under
   `argument/lemmas/` is a prospective-consumer mention in
   `argument/lemmas/lem-maincb-error-improvement.md:34-37`. Thus the
   dependency required by v4.1 R27/R36 is **NOT IN THE LOCAL REGISTRY**.
2. Even the unlanded v4.1 proposal is no longer a closed reset package. It
   defines
   \[
   \varepsilon_E^{\rm corr}
   =\frac{\min\{\delta_{\max}^{\rm cb},e_H,e_{\rm ext},
                      e_{\rm sel},e_{\rm split}\}}{C_{\rm pre}}
   \]
   at
   `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:216`,
   but the now-ratified landed IMPROVE-CB contract also requires the ambient
   defect to satisfy
   \(\varepsilon\le\varepsilon_{\max}^{\rm cb}\)
   (`argument/lemmas/lem-maincb-error-improvement.md:4,13-19`).
   The proposed reset minimum does not pay for that guard.

Finding this is a successful outcome under the brief. No radius is supplied
for the terminal row, and the parent remains blocked. There is **no
dimension-freeness alarm** in the thirteen rows that do close.

## 1. Scope, source discipline, and notation

The binding domain warning is
`docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-FUDW-DECOMP-V3.md:69-102`:
the source needs separate MAIN, normalization, degree, and terminal guards;
the AI-linearization radius is not a global source radius. The reservations
and reconnection guard are at
`docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md:230-275`,
the parent wiring at the same file's lines 348-364, and R24-R28/R36-R38 at
lines 596-610.

For compact exact citations below:

- **TeX** means
  `refs/kitaev-2405.02434/approximate_algebras.tex`;
- **K-ledger** means
  `docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md`;
- **G-verdict** means
  `docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-G-KLEDGER.md`;
- **v4.1** means
  `docs/plans/2026-07-24-fudw-decomposition-artifacts/DESIGN-FUDW-DECOMP-v4.1.md`.

Every number following one of these names is a one-indexed line or line
range in that exact file.

All contracts below are restricted to the finite Route-F setting
\(\mathcal H=\mathbb C^n\). Constants must be independent of \(n\). This
restriction is enough for the stochastic theorem and ensures that the
finite-dimensional norm selection in the componentwise \(\Upsilon'\)
construction is literal.

Use the following outputs of existing dependencies.

- \(C_\theta=12(\sqrt2-1)\) and
  \(\rho_\theta:=1/8\) come from
  `lem-routef-functional-calculus-closeness`
  (`argument/lemmas/lem-routef-functional-calculus-closeness.md:4-9`).
- Write \(\rho_{\rm AI}\) for the positive radius called \(\eta_A\) in
  `lem-routef-ai-defect-linearization`, and retain its
  \(C_A=20+\frac{211}{8}C_\theta\)
  (`argument/lemmas/lem-routef-ai-defect-linearization.md:4-9`).
  **This is the only identification with \(\eta_A\).** Downstream rows use
  \(\rho_{\rm AI}\) only to invoke that dependency; it is never used to
  certify an unrelated source \(O(\eta)\).
- \(C_E<\infty\) and \(\varepsilon_E>0\) are the dimension-free outputs of
  the existing `lem-thmainext-conditional`
  (`argument/lemmas/lem-thmainext-conditional.md:4-9`). Normalize
  \[
  \bar C_E:=\max\{1,C_E\},\qquad
  C_V:=\bar C_E C_A,\qquad
  C_T:=C_\theta+3C_V.
  \]
  This enlargement is arithmetic, not a new estimate.
- Define the first genuinely local Route-F radius
  \[
  \boxed{\rho_T:=
  \min\left\{\rho_\theta,\rho_{\rm AI},
       \frac{\varepsilon_E}{C_A},
       \frac1{4(1+C_\theta)},
       \frac1{4(1+C_V)}\right\}.}
  \tag{1.1}
  \]
  Every entry is positive and dependency-produced. In particular,
  \(C_\theta\eta\le1/4\) and \(C_V\eta\le1/4\) on this radius.

The existing `lem-thmainext-conditional` is used only to close the local
factor-map rows from the registry as it stands. This does not substitute it
for the missing reset package in the terminal minimum.

## 2. Serial local-domain DAG

Rows D2 and D3 are the two design-only consumer reconnections, not members
of the fourteen reservations. They are interleaved because
`lem-routef-delta-phi-product` needs D2 and the componentwise
\(\Upsilon'\) construction needs both D2 and D3. Every dependency is an
existing registry id or an earlier row in this table. The sole exception is
the terminal GAP, where the absent dependency is shown explicitly rather
than hidden.

| order | proposed id | closed one-line `contract:` (design only) | defs | deps | provenance | projected af |
|---:|---|---|---|---|---|---|
| 1 | `lem-routef-raw-factor-norms` | Raw factor-map norms: with \(C_V,C_T,\rho_T\) from (1.1), for \(0\le\eta\le\rho_T\), every amplification satisfies \((1-C_V\eta)\lVert X\rVert\le\lVert\widetilde\Delta_nX\rVert\le(1+C_V\eta)\lVert X\rVert\) and \(\max\{\lVert\widetilde\Delta\rVert_{\rm cb},\lVert\widetilde\Upsilon\rVert_{\rm cb}\}\le1+C_T\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-routef-functional-calculus-closeness`; `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | TeX 2749-2753; K-ledger 154-190 | 8 / 3 |
| 2 | `lem-routef-raw-factor-units` | Raw factor-map units: for \(\rho_{\rm unit}:=\rho_T\) and \(0\le\eta\le\rho_{\rm unit}\), \(\max\{\lVert\widetilde\Delta(I)-I\rVert,\lVert\widetilde\Upsilon(I)-I\rVert\}\le C_T\eta\). | same as row 1 | row 1; `lem-thmainext-conditional` | TeX 2754-2757; K-ledger 169-181 | 4 / 2 |
| 3 | `lem-routef-raw-factor-identities` | Raw factor-map identities: for \(\rho_{\rm id}:=\min\{\rho_{\rm AI},\varepsilon_E/C_A\}\) and \(0\le\eta\le\rho_{\rm id}\), \(\widetilde\Delta\widetilde\Upsilon=\widetilde\Phi\) and \(\widetilde\Upsilon\widetilde\Delta=I_{\mathcal B}\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; `def-extended-delta-inclusion` | `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | TeX 2749-2753; K-ledger 183-187 | 3 / 2 |
| 4 | `lem-routef-raw-product-estimate` | Raw \(\widetilde\Delta\)-product estimate: for \(\rho_{\rm prod}:=\rho_T\), \(0\le\eta\le\rho_{\rm prod}\), every amplification, and all \(X,Y\), \(\lVert\widetilde\Phi_n(\widetilde\Delta_nX\,\widetilde\Delta_nY)-\widetilde\Delta_n(XY)\rVert\le C_T\eta\lVert X\rVert\lVert Y\rVert\). | same as row 1 | row 1; row 3; `lem-thmainext-conditional` | TeX 2754-2766; K-ledger 174-181 | 4 / 2 |
| 5 | `lem-routef-delta-prime-closeness` | Delta-prime CP closeness: set \(C_{\Delta'}:=C_T+4C_\theta\) and \(\rho_{\Delta'}:=\min\{\rho_T,\rho_{\rm prod}\}\); for \(0\le\eta\le\rho_{\Delta'}\), the repaired norm-one diagonal produces a CP map \(\Delta'\) with \(\lVert\Delta'-\widetilde\Delta\rVert_{\rm cb}\le C_{\Delta'}\eta\). | `def-fd-cstar-diagonal`; `def-extended-epsilon-cstar-algebra` | `cor-kitaev-diagonal-cpization`; `lem-routef-functional-calculus-closeness`; rows 1 and 4 | TeX 2771-2801; K-ledger 193-226; `cor-kitaev-diagonal-cpization.md:4-9` | 6 / 3 |
| 6 | `lem-routef-delta-normalization-closeness` | Delta UCP normalization: set \(C_\Delta:=6C_T+7C_{\Delta'}\) and \(\rho_\Delta:=\min\{\rho_{\rm unit},\rho_{\Delta'},[2(C_T+C_{\Delta'})]^{-1}\}\); for \(0\le\eta\le\rho_\Delta\), \(a=\Delta'(I)\) is invertible and \(\Delta(X)=a^{-1/2}\Delta'(X)a^{-1/2}\) is UCP with \(\lVert\Delta-\widetilde\Delta\rVert_{\rm cb}\le C_\Delta\eta\). | `def-extended-epsilon-cstar-algebra` | rows 2 and 5 | TeX 2797-2801; K-ledger 246-259, 415-448; G-verdict 141-145,287-295 | 5 / 3 |
| D2 | `lem-routef-degree-two-estimate` | Route F degree-two estimate: set \(C_2:=C_{\Delta'}+4C_\Delta\) and \(\rho_2:=\min\{\rho_{\rm prod},\rho_{\Delta'},\rho_\Delta\}\); for \(0\le\eta\le\rho_2\), every amplification satisfies \(\lVert\Phi_n(\Delta_nX\,\Delta_nY)-\Delta_n(XY)\rVert\le C_2\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | rows 1, 4, 5, and 6 | TeX 2803-2812; K-ledger 193-226; G-verdict 119-128 | 5 / 3 |
| 7 | `lem-routef-delta-phi-product` | Normalized Delta product: for \(\rho_{\Delta\Phi}:=\min\{\rho_\theta,\rho_\Delta,\rho_2\}\) and \(0\le\eta\le\rho_{\Delta\Phi}\), every amplification satisfies \(\lVert\widetilde\Phi_n(\Delta_nX\,\Delta_nY)-\widetilde\Delta_n(XY)\rVert\le(C_2+C_\theta+C_\Delta)\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; row 6; D2 | K-ledger 374-383; TeX 2803-2812 | 4 / 2 |
| D3 | `lem-routef-degree-three-estimate` | Route F degree-three estimate: set \(C_3:=10+20C_\Delta+12C_\theta+2C_{\Delta'}\) and \(\rho_3:=\min\{\rho_\theta,\rho_{\Delta'},\rho_\Delta,\rho_2\}\); for \(0\le\eta\le\rho_3\), every amplification satisfies \(\lVert\Phi_n(\Delta_nX\,\Delta_nY\,\Delta_nZ)-\Delta_n(XYZ)\rVert\le C_3\eta\lVert X\rVert\lVert Y\rVert\lVert Z\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-kitaev-almost-idemp-audit`; `lem-routef-functional-calculus-closeness`; rows 1, 5, and 6; D2 | TeX 2813-2829; K-ledger 193-226; G-verdict 119-128 | 7 / 3 |
| 8 | `lem-routef-upsilon-prime-closeness` | Upsilon-prime CP closeness: put \(C_N:=C_V+C_\Delta\), \(C_R:=C_N+C_2\), \(C_L:=C_2+C_3+2C_R\), \(C_{\Upsilon'}:=1+C_\theta+2C_\Delta+2C_L\), and \(\rho_{\Upsilon'}:=\min\{\rho_T,\rho_{\rm id},\rho_\Delta,\rho_2,\rho_3\}\); for \(0\le\eta\le\rho_{\Upsilon'}\), the componentwise construction produces CP \(\Upsilon'\) with \(\lVert\Upsilon'-\widetilde\Upsilon\rVert_{\rm cb}\le C_{\Upsilon'}\eta\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; rows 1, 3, and 6; D2 and D3 | TeX 2831-2895; K-ledger 228-245; G-verdict 291-295 | 11 / 3 |
| 9 | `lem-routef-upsilon-normalization-closeness` | Upsilon UCP normalization: set \(C_\Upsilon:=6C_T+7C_{\Upsilon'}\) and \(\rho_\Upsilon:=\min\{\rho_{\rm unit},\rho_{\Upsilon'},[2(C_T+C_{\Upsilon'})]^{-1}\}\); for \(0\le\eta\le\rho_\Upsilon\), \(b=\Upsilon'(I)\) is invertible and \(\Upsilon(X)=b^{-1/2}\Upsilon'(X)b^{-1/2}\) is UCP with \(\lVert\Upsilon-\widetilde\Upsilon\rVert_{\rm cb}\le C_\Upsilon\eta\). | `def-extended-epsilon-cstar-algebra` | rows 2 and 8 | TeX 2895-2899; K-ledger 246-259,415-448; G-verdict 144-149,294-295 | 5 / 3 |
| 10 | `lem-routef-delta-upsilon-telescope` | Delta-Upsilon telescope: for \(\rho_{\Delta\Upsilon}:=\min\{\rho_\theta,\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}\) and \(0\le\eta\le\rho_{\Delta\Upsilon}\), \(\lVert\Delta\Upsilon-\Phi\rVert_{\rm cb}\le(C_\theta+C_\Delta+2C_\Upsilon)\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; rows 1, 3, 6, and 9 | K-ledger 345-372; G-verdict 96-117 | 4 / 2 |
| 11 | `lem-routef-multiplicative-telescope` | Multiplicative telescope: for \(\rho_{\rm mult}:=\min\{\rho_T,\rho_{\rm id},\rho_{\Delta\Phi},\rho_\Upsilon\}\) and \(0\le\eta\le\rho_{\rm mult}\), every amplification satisfies \(\lVert\Upsilon_n(\Delta_nX\,\Delta_nY)-XY\rVert\le[C_\Upsilon+2(C_2+C_\theta+C_\Delta)]\eta\lVert X\rVert\lVert Y\rVert\). | same as row 10 | rows 1, 3, 7, and 9 | K-ledger 345-383; G-verdict 96-117 | 4 / 2 |
| 12 | `lem-routef-upsilon-delta-telescope` | Upsilon-Delta telescope: for \(\rho_{\Upsilon\Delta}:=\min\{\rho_T,\rho_{\rm id},\rho_\Delta,\rho_\Upsilon\}\) and \(0\le\eta\le\rho_{\Upsilon\Delta}\), \(\lVert\Upsilon\Delta-I_{\mathcal B}\rVert_{\rm cb}\le(C_\Upsilon+2C_\Delta)\eta\). | `def-extended-epsilon-cstar-algebra` | rows 1, 3, 6, and 9 | K-ledger 345-372; G-verdict 96-117 | 3 / 2 |
| 13 | `lem-routef-k-finiteness` | Route F common coefficient/domain: \(K:=\max\{1,C_\theta+C_\Delta+2C_\Upsilon,C_\Upsilon+2(C_2+C_\theta+C_\Delta),C_\Upsilon+2C_\Delta\}\) is finite and universal, and \(\rho_{\rm fac}:=\min\{\rho_2,\rho_{\Delta\Upsilon},\rho_{\rm mult},\rho_{\Upsilon\Delta}\}>0\) is the common domain of its three factorization estimates. | `def-extended-epsilon-cstar-algebra` | D2; rows 10, 11, and 12 | K-ledger 385-397; G-verdict 96-117 | 4 / 2 |
| 14 | `lem-routef-threshold-minimum` | **GAP — NO CLOSED CONTRACT.** After the missing reset package is landed and its omitted ambient guard is repaired, the candidate contract is: \(\eta_K:=\min\{\rho_{\rm fac},\rho_{\rm reset},(24K)^{-1},1\}>0\), where \(\rho_{\rm reset}\) is the dependency-produced corrected MAIN radius in (3.4), and \(0\le\eta\le\eta_K\) implies every local Route-F and PRH smallness hypothesis. | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional`; rows 1, 6, 9, and 13; **MISSING** `lem-maincb-reset-constant-ledger`; `lem-maincb-error-improvement` | v4.1 216,250-275,596-610; `argument/lemmas/lem-maincb-error-improvement.md:4,13-19` | **N/A while GAP; candidate 5 / 2 after repair** |

### Contract hygiene note

The replacement for `lem-routef-raw-product-estimate` deliberately states
the \(\widetilde\Phi\)-\(\widetilde\Delta\) product estimate, not only the
\(\widetilde\Upsilon\)-valued consequence in the withdrawn v3 row. The former
is exactly what the \(\Delta'\) comparison consumes. Stating only the latter
would either leave row 5 dangling or enlarge \(C_{\Delta'}\) by an
unrecorded composition. This is one product mechanism, not a compound
contract.

## 3. Per-row radius derivations

### 3.1 Raw factor rows

**Row 1.** On
\(\eta\le\min\{\rho_{\rm AI},\varepsilon_E/C_A\}\), the AI algebra has
defect at most \(C_A\eta\), so `lem-thmainext-conditional` supplies an
extended \(C_EC_A\eta\)-isomorphism \(v\). Enlarging to \(C_V\) gives
\[
(1-C_V\eta)\|X\|\le\|v_nX\|\le(1+C_V\eta)\|X\|.
\]
Set \(\widetilde\Delta=v\) and
\(\widetilde\Upsilon=v^{-1}\widetilde\Phi\).
For \(a=C_\theta\eta\), \(b=C_V\eta\), (1.1) gives
\(a,b\le1/4\), and
\[
\frac{1+a}{1-b}\le1+a+3b=1+C_T\eta.
\]
This proves the two cb-norm bounds. This is the explicit local replacement
for the unsafe use of the AI radius in K-ledger lines 160-181.

**Row 2.** Extended isomorphism unitality gives
\(\|\widetilde\Delta(I)-I\|\le C_V\eta\).
Since \(\widetilde\Phi(I)=I\),
\[
\|\widetilde\Upsilon(I)-I\|
\le \|v^{-1}\|\,\|I-v(I)\|
\le\frac{C_V\eta}{1-C_V\eta}
\le 3C_V\eta\le C_T\eta.
\]
No new radius is used.

**Row 3.** The range of the exact idempotent \(\widetilde\Phi\) is
\(\mathcal A\), \(v\) is onto \(\mathcal A\), and
\(\widetilde\Phi|_{\mathcal A}=I_{\mathcal A}\). Thus the two identities
are algebraic once the AI and MAIN constructions exist. Their radius is
exactly the minimum of those two existence radii; no Neumann guard is
needed.

**Row 4.** The extended-isomorphism product defect says
\[
\|\widetilde\Phi_n(v_nX\,v_nY)-v_n(XY)\|
\le C_EC_A\eta\|X\|\|Y\|
\le C_T\eta\|X\|\|Y\|.
\]
This is valid on \(\rho_T\). It does not invoke an unnamed source
linearization radius.

### 3.2 Delta repair, normalization, and degree rows

**Row 5.** The repaired diagonal has positive weights summing to one and
projective norm one
(`cor-kitaev-diagonal-cpization.md:4-9`; TeX 2771-2796). On \(\rho_T\),
\(C_T\eta\le C_\theta\eta+3C_V\eta\le1\), so
\(\|\widetilde\Delta\|_{\rm cb}\le2\). Comparing each averaged summand:

- row 4 costs \(C_T\eta\);
- replacing \(\widetilde\Phi\) by \(\Phi\) costs at most
  \(C_\theta\eta\cdot2\cdot2=4C_\theta\eta\).

The convex average introduces no term-count factor. Hence
\(C_{\Delta'}=C_T+4C_\theta\) on
\(\rho_{\Delta'}=\min\{\rho_T,\rho_{\rm prod}\}\).

**Row 6.** Rows 2 and 5 give
\[
\|\Delta'(I)-I\|\le(C_T+C_{\Delta'})\eta.
\]
The explicit radius
\([2(C_T+C_{\Delta'})]^{-1}\) makes this at most \(1/2\).
The hostile-checked inverse-square-root calculation then costs at most six
times the unit defect; adding the original
\(C_{\Delta'}\eta\) comparison yields
\[
6(C_T+C_{\Delta'})+C_{\Delta'}
=6C_T+7C_{\Delta'}=C_\Delta.
\]
This is precisely the R25 guard, not the unsafe
\((2C_{\Delta'})^{-1}\).

**D2.** On the intersection of the raw-product, \(\Delta'\), and normalized
\(\Delta\) domains, the fixed-length comparison verified at
`VERDICT-W74F-G-KLEDGER.md:119-128` gives
\[
C_2=C_{\Delta'}+4C_\Delta.
\]
No downstream \(\Upsilon'\) constant enters \(\rho_2\); hence there is no
forward edge or circular “common degree range.”

**Row 7.** Insert \(\Phi\) and \(\Delta\):
\[
\begin{aligned}
\|\widetilde\Phi(\Delta X\Delta Y)-\widetilde\Delta(XY)\|
&\le\|(\widetilde\Phi-\Phi)(\Delta X\Delta Y)\|\\
&\quad+\|\Phi(\Delta X\Delta Y)-\Delta(XY)\|\\
&\quad+\|(\Delta-\widetilde\Delta)(XY)\|.
\end{aligned}
\]
Because \(\Delta\) is UCP, the three coefficients are respectively
\(C_\theta,C_2,C_\Delta\). The radius is the minimum of the three producer
domains.

**D3.** The \(10\eta\) associativity input is supplied by
`lem-kitaev-almost-idemp-audit`
(`argument/lemmas/lem-kitaev-almost-idemp-audit.md:4-9`), and
\(\rho_\theta=1/8<1/4\) lies in its displayed defect range. The five
fixed comparisons at TeX 2817-2829, hostile-recomputed at
`VERDICT-W74F-G-KLEDGER.md:119-128`, give
\[
C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'}.
\]
All inputs are earlier rows; \(\rho_3\) is their finite minimum.

### 3.3 Componentwise Upsilon repair

**Row 8.** This is the longest leaf, but its constants can be exposed
without reusing \(\rho_{\rm AI}\) as a source-wide radius.

First, row 1 and row 6 imply the lower norm estimate
\[
\|\Delta_nX\|\ge
\bigl(1-(C_V+C_\Delta)\eta\bigr)\|X\|
=(1-C_N\eta)\|X\|.
\tag{3.1}
\]
For the Choi block \(j\), TeX 2840-2857 gives
\(R_j=I_{\mathcal L_j}\otimes C_j\), \(0\le C_j\le I\). Applying D2 to
the unitary average and then (3.1) to the block identity gives
\[
\|C_j\|\ge1-(C_N+C_2)\eta=1-C_R\eta.
\tag{3.2}
\]
Since the Route-F Hilbert space is finite-dimensional, choose a unit
\(\xi_j\) attaining \(\|C_j\|\). The final scalar in TeX 2888-2892 then
differs from one by at most \(2C_R\eta\).

The middle comparison at TeX 2874-2892 uses:

- \(\|\Phi\Delta-\Delta\|_{\rm cb}\le C_2\eta\), obtained from D2 by
  setting its second input to \(I\);
- the D3 estimate, costing \(C_3\eta\);
- the final scalar error \(2C_R\eta\).

Thus
\[
\|\Upsilon'\Delta-I_{\mathcal B}\|_{\rm cb}
\le C_L\eta,\qquad C_L=C_2+C_3+2C_R.
\tag{3.3}
\]
Each component map is CP and contractive. Probability averages introduce
no term-count factor, and the direct-sum target has the maximum norm, so
(3.3) is uniform in the number and sizes of blocks.

Finally use the exact row-3 identities in the source chain at TeX 2895:
\[
\Upsilon'\to\Upsilon'\Phi\to\Upsilon'\widetilde\Phi
=\Upsilon'\widetilde\Delta\widetilde\Upsilon
\to\Upsilon'\Delta\widetilde\Upsilon\to\widetilde\Upsilon.
\]
The five costs are \(1,C_\theta,0,2C_\Delta,2C_L\), since row 1 gives
\(\|\widetilde\Upsilon\|_{\rm cb}\le2\). This yields the displayed
\[
C_{\Upsilon'}=1+C_\theta+2C_\Delta+2C_L
\]
on the minimum of the named producer radii. No hidden block-count,
amplification, or source-\(O\) radius remains.

**Row 9.** Rows 2 and 8 give
\[
\|\Upsilon'(I)-I\|\le(C_T+C_{\Upsilon'})\eta.
\]
The explicit R25 guard
\([2(C_T+C_{\Upsilon'})]^{-1}\) makes the unit invertible. The same
hostile-checked normalization arithmetic as in row 6 gives
\[
C_\Upsilon=6(C_T+C_{\Upsilon'})+C_{\Upsilon'}
=6C_T+7C_{\Upsilon'}.
\]

### 3.4 Telescopes and \(K\)

**Row 10.** Insert the exact row-3 identity
\(\widetilde\Delta\widetilde\Upsilon=\widetilde\Phi\):
\[
\|\Delta\Upsilon-\Phi\|_{\rm cb}
\le C_\Delta\eta+2C_\Upsilon\eta+C_\theta\eta.
\]
The factor two is row 1's bound for \(\widetilde\Delta\).

**Row 11.** Since
\(\widetilde\Upsilon\widetilde\Phi=\widetilde\Upsilon\) and
\(\widetilde\Upsilon\widetilde\Delta=I\), row 7 gives
\[
\|\Upsilon(\Delta X\Delta Y)-XY\|
\le C_\Upsilon\eta\|X\|\|Y\|
+2(C_2+C_\theta+C_\Delta)\eta\|X\|\|Y\|.
\]

**Row 12.** The exact identity
\(\widetilde\Upsilon\widetilde\Delta=I\) gives
\[
\|\Upsilon\Delta-I\|_{\rm cb}
\le C_\Upsilon\eta+2C_\Delta\eta.
\]

**Row 13.** The maximum defining \(K\) is over four already-produced
finite universal numbers. The minimum defining \(\rho_{\rm fac}\) is over
four already-produced positive radii. Neither expression contains \(K\)'s
domain or the future \(\eta_K\), so there is no arithmetic cycle.

### 3.5 Terminal row — GAP

**Row 14 cannot be derived from the named dependencies in the current
repository.** The required reset-package dependency is absent. Moreover,
landing the v4.1 text verbatim would not close the new
\(\varepsilon_{\max}^{\rm cb}\) hypothesis.

The smallest sufficient repair to the reset interface is to produce
\(C_{\rm pre}>0\) and \(\varepsilon_E^{\rm corr}>0\) and then expose
\[
\boxed{\rho_{\rm reset}:=
\min\left\{
  \frac{\varepsilon_E^{\rm corr}}{C_A},
  \frac{\varepsilon_{\max}^{\rm cb}}{C_{\rm pre}C_A}
\right\}.}
\tag{3.4}
\]
Equivalently, the upstream package may redefine
\[
\varepsilon_E^{\rm corr,new}:=
\frac{\min\{\varepsilon_{\max}^{\rm cb},
             \delta_{\max}^{\rm cb},e_H,e_{\rm ext},
             e_{\rm sel},e_{\rm split}\}}{C_{\rm pre}}.
\]
That is an upstream contract change and is not authorized here. Until a
landed producer exposes one of these equivalent interfaces, row 14 stays
GAP.

## 4. Finite-minimum audit (R27)

Conditional on the repair in §3.5, the terminal candidate is
\[
\boxed{\eta_K=
\min\left\{\rho_{\rm fac},\rho_{\rm reset},
            \frac1{24K},1\right\}.}
\tag{4.1}
\]

Expanding the recursively named radii produces the following finite
primitive guard set:
\[
\left\{
\rho_\theta,\rho_{\rm AI},\frac{\varepsilon_E}{C_A},
\frac1{4(1+C_\theta)},\frac1{4(1+C_V)},
\frac1{2(C_T+C_{\Delta'})},
\frac1{2(C_T+C_{\Upsilon'})},
\frac{\varepsilon_E^{\rm corr}}{C_A},
\frac{\varepsilon_{\max}^{\rm cb}}{C_{\rm pre}C_A},
\frac1{24K},1
\right\}.
\tag{4.2}
\]

Audit:

1. **Finite:** (4.2) has eleven named entries.
2. **Named producers:** functional calculus produces
   \(\rho_\theta,C_\theta\); AI produces \(\rho_{\rm AI},C_A\);
   `lem-thmainext-conditional` produces \(C_E,\varepsilon_E\);
   rows 1, 5, 6, 8, 9, and 13 produce
   \(C_V,C_T,C_{\Delta'},C_\Delta,C_{\Upsilon'},C_\Upsilon,K\) and their
   local radii; IMPROVE-CB produces
   \(\varepsilon_{\max}^{\rm cb}\); the missing reset package is required
   to produce \(C_{\rm pre},\varepsilon_E^{\rm corr}\).
   Row 14's proposed dependency list imports each of these primitive guard
   producers directly; D2, D3, row 8, and the three telescopes introduce
   only finite minima of those primitive guards and are imported through
   the row-13 \(\rho_{\rm fac}\) aggregator.
3. **Non-circular:** every entry other than the missing reset outputs is
   produced strictly before row 14. \(K\) depends on the telescopes, not on
   \(\eta_K\). The reset constants are MAIN-CB constants and do not depend
   on any Route-F telescope or on \(K\).
4. **Nonempty and positive after repair:** all eleven entries are positive.
   In particular, \(C_A>0\), \(K\ge1\),
   \(C_T+C_{\Delta'}>0\), and \(C_T+C_{\Upsilon'}>0\).
5. **Current verdict:** because two named reset outputs do not presently
   have a landed producer, this positivity argument is conditional and
   cannot support a registry contract now.

The coarse original entry
\([4(1+C_2+C_3+C_{\Upsilon'})]^{-1}\) is not needed in this replacement
DAG: D2, D3, and row 8 now have explicit predecessor radii and row 8's
component arithmetic is exposed. Reintroducing that term would be safe but
redundant; treating it as a substitute for a missing producer would not be
safe.

## 5. Dimension-freeness audit

| row | audit |
|---|---|
| 1-4 | \(C_\theta,C_A\) are amplification-uniform; \(C_E,\varepsilon_E\) are declared independent of dimension, amplification, and block data by `lem-thmainext-conditional`. Fixed scalar arithmetic introduces no index. |
| 5 | The repaired diagonal has weights summing to one and projective norm one. No number of diagonal terms, simple blocks, or block dimensions appears. |
| 6 | Inverse-square-root functional calculus is scalar and uniform on the fixed \(1/2\)-ball. |
| D2, 7, D3 | Each is a fixed-length telescope of cb/amplified estimates. The \(10\) associativity coefficient is dimension-free at every amplification. |
| 8 | Each \(j\)-component uses probability averages; the target direct sum uses the maximum norm. The same \(C_R,C_L,C_{\Upsilon'}\) applies to every block. There is no sum over \(j\), no block-size coefficient, and no amplification coefficient. |
| 9 | Same scalar \(1/2\)-ball normalization in the direct-sum maximum norm. |
| 10-12 | Fixed two- or three-term cb telescopes; no data-dependent count. |
| 13 | A maximum/minimum of four universal quantities; no dimension or stage input. |
| 14 | The candidate formula is dimension-free if the reset producer is repaired as specified, but the row is GAP for dependency closure, not for dimension leakage. |

**ROUTE-LEVEL ALARM CHECK:** none of the closed formulas depends on
\(n\), amplification level, number of simple blocks, block dimensions, or
MAIN stage index. No route-level dimension alarm was found.

## 6. Reconnection map

### 6.1 Degree rows

The corrected design-only dependencies are:

```text
lem-routef-degree-two-estimate:
  deps:
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

These rows remain **DESIGN-ONLY / DO NOT TRANSCRIBE** until the preceding
replacement rows pass a separate hostile audit and the user authorizes
landing.

### 6.2 Proposed parent wiring

Per v4.1 §3.4, after and only after all fourteen rows close, the proposed
complete replacement dependency list for `lem-routef-k-ledger` is:

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

**DO NOT REWIRE OR SEED.** The current threshold row is GAP, so this parent
wiring is only a proposal and the v4.1 guard remains fully in force.

## 7. Landing decision

- Rows 1-13 and D2/D3: mathematically closed **as a design** relative to
  the existing registry contracts and the displayed source mechanisms;
  still non-rigorous and subject to a separate hostile audit.
- Row 14: **GAP / DO NOT SHARD OR SEED**.
- Entire fourteen-row family: **NOT LANDING-READY**.
- Required upstream action before a renewed audit: land a genuine
  `lem-maincb-reset-constant-ledger` producer and include the
  \(\varepsilon_{\max}^{\rm cb}\) ambient guard either in that package or
  in an equivalent explicitly imported reset-radius producer.
