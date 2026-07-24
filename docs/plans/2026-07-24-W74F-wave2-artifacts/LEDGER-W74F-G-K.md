STATUS: UNVERIFIED PROVER OUTPUT

# W74F-G — unconditional relative \(K/\eta_K\) ledger for Route F

Date: 2026-07-24  
Role: fresh prover; this document is not a verifier verdict  
Primary source: `refs/kitaev-2405.02434/approximate_algebras.tex`  
Checked SHA256:
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`

## 0. Outcome and normalization policy

The two gaps isolated by `DECOMP-W74F-C-THMAINEXT.md` are now inputs with
hostile-verifier verdicts:

- H-CB is available in its corrected conditional-inverse form with
  \[
  C_H=4000c,\qquad e_H=(10000c)^{-1};
  \]
- EXT-CB is available with
  \[
  C_{\rm ext}
  =C_{\rm merge}[1+5C_H+20C_{\rm app}(C_H+1)]
  \]
  and the corrected threshold below.

Consequently the MAIN-CB induction and the factorization post-processing
have an unconditional **relative** universal-constant ledger: every
constant and threshold below is defined in terms of fixed universal
source/artifact constants. “Unconditional” here means that H-CB and
EXT-CB are no longer hypotheses or dangling gap nodes. It does **not**
mean L0-rigorous: the whole chain remains `proved-mod-audit`.

Throughout, an unnamed universal coefficient may be enlarged and an
unnamed positive universal threshold may be shrunk. This is legitimate
because the source declares at `tex:458` that each big-\(O\) denotes a
concrete function independent of all additional data. Normalize
\[
C_{\rm app},C_{\rm inc},C_{\rm co},C_{\rm col},C_{\rm merge}\ge1.
\tag{0.1}
\]
Here \(C_{\rm co}\) is enlarged once to dominate all fixed COMP-CB
product, compressed-unit, corner-algebra, one-compression transfer, and
level-one fixed-corner coefficients used by MAIN-CB. It also, together
with \(C_{\rm col}\), dominates the reciprocal of their common input
validity radius. This packages finitely many unnamed source coefficients;
it does not introduce dependence on a dimension or on the number of
steps.

## 1. Symbol table

Every coefficient or threshold used later is defined in this section.
The final column records dependence on \(n\), Hilbert-space dimension,
matrix size, number of simple blocks, and block dimensions; in every row
it is absent.

### 1.1 Functional calculus and the approximate algebra

| symbol | definition and producing inequality | source/artifact locus | data dependence |
|---|---|---|---|
| \(C_\theta\) | \(C_\theta:=12(\sqrt2-1)\). For \(\eta\le1/8\), the D-audit bound \(r(\eta)=\frac32((1-4\eta)^{-1/2}-1)\) gives \(\|\widetilde\Phi-\Phi\|_{\rm cb}\le C_\theta\eta\). | `tex:2171-2179`; D-audit (E8) | none |
| \(C_A\) | \(C_A:=20+\frac{211}{8}C_\theta\). If \(r\le1/2\), then \((1+r)^5-1\le\frac{211}{16}r\); hence D-audit (E9) gives \(\varepsilon_{\rm AI}(\eta)\le C_A\eta\). | `tex:2192-2209`; D-audit (E9) | none |
| \(\eta_A\) | A fixed positive common source-linearization radius, chosen no larger than \(\min\{1/8,(2C_\theta)^{-1}\}\), and small enough that the finitely many source \(O(\eta)\) bounds in `tex:2749-2899` admit the coefficients named below. Positivity follows from the source convention at `tex:458`. | `tex:458`, `2171-2209`, `2749-2899` | none |

Indeed, for \(\eta\le(2C_\theta)^{-1}\), \(r\le1/2\), and
\[
\begin{aligned}
\varepsilon_{\rm AI}(\eta)
&=\max\{r,\ 20\eta+2((1+r)^5-1),\ 3r-r^2\}\\
&\le C_A\eta.
\end{aligned}
\tag{1.1}
\]
This makes the approximate-algebra input explicit rather than leaving
\(\varepsilon_{\rm AI}=O(\eta)\).

### 1.2 Error reduction and tensor-extension constants

| symbol | definition and producing inequality | source/artifact locus | data dependence |
|---|---|---|---|
| \(C_{\rm app}\) | A common coefficient for APPROX-CB: an extended raw \(\delta\)-homomorphism is changed by at most \(C_{\rm app}\delta\) in cb norm and the corrected map has extended homomorphism defect at most \(C_{\rm app}\varepsilon\). | `tex:1224-1313`, `1508-1535`; repaired norm-one diagonal | none |
| \(C_{\rm inc}\) | A common coefficient for INC-CB: once the level-one lower modulus is bounded away from \(0\), every amplification has inclusion/norm error at most \(C_{\rm inc}(\alpha+\varepsilon)\) for homomorphism defect \(\alpha\). | `tex:1483-1505` | none |
| \(\delta_{\max}^{\rm cb}\) | A positive common admissible radius, obtained by shrinking the source's error-reduction radius so APPROX-CB, INC-CB, IMPROVE-CB, and the fixed four-corner MERGE-CB all apply whenever their ambient and raw defects are at most \(\delta_{\max}^{\rm cb}\). | `tex:1316-1319`, `1325-1359`, `1508-1535` | none |
| \(c_0^{\rm cb}\) | \(c_0^{\rm cb}:=1+C_{\rm app}+C_{\rm inc}(C_{\rm app}+1)\). IMPROVE-CB therefore replaces any admissible raw inclusion in an extended \(\varepsilon\)-\(C^*\)-algebra by one extended \(c_0^{\rm cb}\varepsilon\)-inclusion; bijectivity is preserved. | `tex:1316-1319`, `1483-1535`; DECOMP IMPROVE-CB | none |
| \(C_{\rm co}\) | The normalized common coefficient described in §0 for COMP-CB, corner-algebra errors, compressed products/units, and a single compression transfer. | `tex:1054-1115`, `1542-1544`; DECOMP COMP-CB | none |
| \(C_{\rm col}\) | The coefficient in \(\bigl|q_T(X)^2-\|X\|^2\bigr|\le C_{\rm col}e\|X\|^2\), after the corrected squared-norm reading. | `tex:1547-1555`; DECOMP (4.1); H-CB (1.2) | none |
| \(c\) | \(c:=\max\{1,C_{\rm co},C_{\rm col}\}\). The normalization in §0 makes \(e\le(10000c)^{-1}\) lie inside the sanctioned COMP-CB/COL-HILB input range. | H-CB (0.1), with the hostile verifier's compressed-unit correction | none |
| \(C_H,e_H\) | \(C_H:=4000c\), \(e_H:=(10000c)^{-1}\). These dominate the corrected H-CB adjoint, product, unit, norm, canonical-corner, and conditional inverse estimates. | H-CB (0.1), (6.3), (7.1)-(7.12), (8.10)-(8.13); H-CB verdict | none |
| \(C_{\rm merge}\) | If four fixed corner maps have common defect \(\rho\) in an ambient extended \(\varepsilon\)-algebra, MERGE-CB returns defect at most \(C_{\rm merge}(\rho+\varepsilon)\). | `tex:1325-1359`; EXT-CB (MERGE) | none |
| \(e_{\rm sel}\) | A positive common level-one threshold for `lem_PQR`, `lem_1d_proj`, `lem_add_dim`, and the close-idempotent range identifications \(\mathcal S_{v(I_r),Q}\cong\mathcal S_{P,Q}\) required by the EXTCB-1 verifier correction. | `tex:1162-1185`, `1363-1369`, `1378-1391`; EXT-CB verdict, EXTCB-1 | none |

For EXT-CB define
\[
\begin{aligned}
A_0&:=4(C_H+1),\\
\kappa&:=4C_{\rm app}(C_H+1),\\
D_0&:=5(C_H+\kappa),
\end{aligned}
\tag{1.2}
\]
and
\[
\boxed{
e_{\rm ext}:=\min\left\{
e_H,\ e_{\rm sel},\
\frac{\delta_{\max}^{\rm cb}}{A_0},\
\frac{\delta_{\max}^{\rm cb}}{D_0+1},\
\frac1{4(C_H+1)},\
\frac1{4(\kappa+1)}
\right\}.}
\tag{1.3}
\]
This is EXT-CB (1.8), with the APPROX/MERGE admissible radii replaced by
the smaller common radius \(\delta_{\max}^{\rm cb}\), and with
\(e_{\rm sel}\) carrying the hostile verifier's close-idempotent
correction. Every entry is positive. Define
\[
\boxed{
C_{\rm ext}:=C_{\rm merge}(D_0+1)
=C_{\rm merge}[1+5C_H+20C_{\rm app}(C_H+1)].
}
\tag{1.4}
\]
This is EXT-CB (6.2)-(6.3). The construction selects one level-one
unitary and one four-corner system and algebraically amplifies them; no
coefficient depends on \(r\) or on the amplification level.

### 1.3 MAIN-CB, the raw factor maps, and CP-ization

Put
\[
\begin{aligned}
L&:=C_{\rm co}(1+c_0^{\rm cb}),\\
C_{\rm pre}
&:=2L^2\max\{1,C_{\rm ext},C_{\rm merge}\},\\
C_E&:=c_0^{\rm cb},\\
\varepsilon_E
&:=\min\left\{
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}},
\frac{e_H}{C_{\rm pre}},
\frac{e_{\rm ext}}{C_{\rm pre}},
\frac{e_{\rm sel}}{C_{\rm pre}}
\right\}.
\end{aligned}
\tag{1.5}
\]
Section 2 proves the producing MAIN-CB inequalities
\[
\operatorname{def}(v)\le C_E\varepsilon,\qquad
0<\varepsilon\le\varepsilon_E.
\tag{1.6}
\]

Let
\[
C_V:=C_EC_A,\qquad
C_T:=C_\theta+3C_V.
\tag{1.7}
\]
For
\[
\eta\le\min\{(4C_\theta)^{-1},(4C_V)^{-1}\},
\tag{1.8}
\]
the maps
\(\widetilde\Delta=v\) and
\(\widetilde\Upsilon=v^{-1}\widetilde\Phi\) satisfy
\[
\begin{gathered}
\|\widetilde\Delta\|_{\rm cb},
\|\widetilde\Upsilon\|_{\rm cb}\le1+C_T\eta,\\
\|\widetilde\Delta(I)-I\|,
\|\widetilde\Upsilon(I)-I\|\le C_T\eta,\\
\|\widetilde\Phi_n(\widetilde\Delta_n(X)
\widetilde\Delta_n(Y))-\widetilde\Delta_n(XY)\|
\le C_T\eta\|X\|\|Y\|,\\
\|\widetilde\Upsilon_n(\widetilde\Delta_n(X)
\widetilde\Delta_n(Y))-XY\|
\le C_T\eta\|X\|\|Y\|.
\end{gathered}
\tag{1.9}
\]
The exact identities are
\[
\widetilde\Delta\widetilde\Upsilon=\widetilde\Phi,\qquad
\widetilde\Upsilon\widetilde\Delta=I_{\mathcal B}.
\tag{1.10}
\]
Equations (1.9)-(1.10) are the explicit \(C_T\) version of
`tex:2749-2766`. The factor \(3C_V\) covers the inverse norm and the one
composition cross-term under (1.8).

The repaired whole-algebra diagonal has coefficient sum and projective
norm exactly \(1\). With \(\|\widetilde\Delta\|_{\rm cb}\le2\), define
\[
\begin{aligned}
C_{\Delta'}&:=C_T+4C_\theta,\\
C_\Delta&:=6C_T+7C_{\Delta'},\\
C_2&:=C_{\Delta'}+4C_\Delta,\\
C_3&:=10+20C_\Delta+12C_\theta+2C_{\Delta'}.
\end{aligned}
\tag{1.11}
\]
Their producing inequalities are:
\[
\begin{aligned}
\|\Delta'-\widetilde\Delta\|_{\rm cb}
&\le C_{\Delta'}\eta,\\
\|\Delta-\widetilde\Delta\|_{\rm cb}
&\le C_\Delta\eta,\\
\bigl|\|\Delta_n(X)\|-\|X\|\bigr|,
\quad\|\Phi\Delta-\Delta\|_{\rm cb},
\quad\operatorname{def}_2(\Phi,\Delta)
&\le C_2\eta\quad\text{with the matching norm factors},\\
\operatorname{def}_3(\Phi,\Delta)
&\le C_3\eta\quad\text{with }\|X\|\|Y\|\|Z\|.
\end{aligned}
\tag{1.12}
\]
Here \(C_{\Delta'}\) is the diagonal artifact's
\(K_0=c_2+c_\Phi A^2\) with \(c_2\le C_T\),
\(c_\Phi=C_\theta\), and \(A=2\);
\(C_\Delta=6c_1+7K_0\) with \(c_1\le C_T\).
The formulas for \(C_2,C_3\) are the explicit fixed telescoping ledger in
the diagonal artifact §4.2, using the D-audit associativity coefficient
\(10\). The relevant source loci are `tex:2786-2829`.

Define \(C_{\Upsilon'}\ge1\) to be one fixed universal coefficient
dominating the finite componentwise chain at `tex:2840-2895`:
\[
\|\Upsilon'\Phi-\Upsilon'\|_{\rm cb},
\quad\|\Upsilon'\Delta-I_{\mathcal B}\|_{\rm cb},
\quad\|\Upsilon'-\widetilde\Upsilon\|_{\rm cb}
\le C_{\Upsilon'}\eta.
\tag{1.13}
\]
This is a definition by the producing inequalities, not a dangling
big-\(O\): \(\eta_A\) was chosen as a common linearization radius, and
\(C_{\Upsilon'}\) is the maximum of the finitely many concrete universal
coefficients in `lem_RC` and the five comparisons at `tex:2871-2895`.
The output direct sum has the maximum norm, so the maximum of the
component coefficients introduces no block-count factor. The source does
not print those coefficients separately, so no honest decimal or shorter
polynomial can be extracted without a new audit.

Finally define
\[
\boxed{C_\Upsilon:=6C_T+7C_{\Upsilon'}.}
\tag{1.14}
\]
Indeed,
\(\|\Upsilon'(I)-I\|\le(C_T+C_{\Upsilon'})\eta\); the same
inverse-square-root calculation used for \(\Delta\) gives
\[
\|\Upsilon-\widetilde\Upsilon\|_{\rm cb}
\le C_\Upsilon\eta
\tag{1.15}
\]
when \((C_T+C_{\Upsilon'})\eta\le1/2\).

## 2. MAIN-CB reset verification

Let \(\varepsilon\) be the defect of the original extended approximate
algebra. The induction invariant after every IMPROVE-CB call is:

> in the current corner algebra \(\mathcal A_X\), whose defect is
> \(\varepsilon_X\), the same level-one map and all its amplifications
> form an extended \(c_0^{\rm cb}\varepsilon_X\)-inclusion.

The source uses at most one compression transfer between a reset and the
next binary extension or merge (`tex:1417-1443`). By the normalization of
\(C_{\rm co}\):

1. every corner algebra used in MAIN-CB is a corner of the original
   algebra cut out by a reset \(c_0^{\rm cb}\varepsilon\)-projection, so
   \[
   \varepsilon_X\le
   C_{\rm co}(1+c_0^{\rm cb})\varepsilon
   =L\varepsilon;
   \tag{2.1}
   \]
2. after reset, the map defect is at most
   \(c_0^{\rm cb}\varepsilon_X\);
3. after the one possible compression transfer, the complete raw packet
   satisfies
   \[
   \delta_{\rm raw}
   \le C_{\rm co}(1+c_0^{\rm cb})\varepsilon_X
   \le L^2\varepsilon.
   \tag{2.2}
   \]

Therefore every EXT-CB or MERGE-CB call sees the single common bound
\[
\boxed{
e_{\rm raw}:=\delta_{\rm raw}+\varepsilon_X
\le(L^2+L)\varepsilon
\le2L^2\varepsilon
\le C_{\rm pre}\varepsilon.
}
\tag{2.3}
\]
The corresponding pre-reset output is bounded by
\[
\begin{aligned}
\delta_{\rm ext,out}
&\le C_{\rm ext}e_{\rm raw}
\le C_{\rm pre}\varepsilon,\\
\delta_{\rm merge,out}
&\le C_{\rm merge}e_{\rm raw}
\le C_{\rm pre}\varepsilon.
\end{aligned}
\tag{2.4}
\]
These inequalities cover:

- the hypothetical binary refinement in Stage 1;
- every compression-plus-extension in Stage 2;
- every binary merge in Stage 3.

There is no iteration factor: (2.4) is followed immediately by a reset.
If \(\varepsilon\le\varepsilon_E\), then simultaneously
\[
C_{\rm pre}\varepsilon
\le\delta_{\max}^{\rm cb},\quad
C_{\rm pre}\varepsilon\le e_H,\quad
C_{\rm pre}\varepsilon\le e_{\rm ext},\quad
C_{\rm pre}\varepsilon\le e_{\rm sel}.
\tag{2.5}
\]
Thus every raw inclusion is admissible for IMPROVE-CB, every H-CB/EXT-CB
use is in range, and every selection/range-identification step is in
range. IMPROVE-CB then restores the invariant. At the final merge the
ambient corner is the original algebra itself, so the final reset gives
\[
\boxed{\operatorname{def}(v)\le c_0^{\rm cb}\varepsilon
=C_E\varepsilon.}
\tag{2.6}
\]
This closes DECOMP defect 10. The threshold ordering does not fail; the
necessary correction is to put the *raw-output* factor
\(C_{\rm pre}\), rather than merely the reset coefficient
\(c_0^{\rm cb}\), beneath the common admissible thresholds.

## 3. Evaluation of \(K\)

The UCP maps \(\Delta,\Upsilon\) have cb norm \(1\), whereas (1.8) gives
\(\|\widetilde\Delta\|_{\rm cb},
\|\widetilde\Upsilon\|_{\rm cb}\le2\).
Using (1.10), (1.12), and (1.15), define
\[
\begin{aligned}
K_{\Delta\Upsilon}
&:=C_\theta+C_\Delta+2C_\Upsilon,\\
K_{\rm mult}
&:=C_\Upsilon+2(C_2+C_\theta+C_\Delta),\\
K_{\Upsilon\Delta}
&:=C_\Upsilon+2C_\Delta.
\end{aligned}
\tag{3.1}
\]
Then
\[
\begin{aligned}
\|\Delta\Upsilon-\Phi\|_{\rm cb}
&\le K_{\Delta\Upsilon}\eta,\\
\|\Upsilon_n(\Delta_n(X)\Delta_n(Y))-XY\|
&\le K_{\rm mult}\eta\|X\|\|Y\|,\\
\|\Upsilon\Delta-I_{\mathcal B}\|_{\rm cb}
&\le K_{\Upsilon\Delta}\eta.
\end{aligned}
\tag{3.2}
\]
For the middle line, insert
\(\widetilde\Upsilon\widetilde\Phi=\widetilde\Upsilon\),
\(\widetilde\Upsilon\widetilde\Delta=I\), and use
\[
\|\widetilde\Phi_n(\Delta_n(X)\Delta_n(Y))
-\widetilde\Delta_n(XY)\|
\le(C_2+C_\theta+C_\Delta)\eta\|X\|\|Y\|.
\]
No new operator estimate is being asserted here; this is fixed-length
telescoping of the named inequalities.

The unconditional relative evaluation of DECOMP (5.1) is therefore
\[
\boxed{
K:=\max\{
1,\,
C_\theta+C_\Delta+2C_\Upsilon,\,
C_\Upsilon+2(C_2+C_\theta+C_\Delta),\,
C_\Upsilon+2C_\Delta
\}.
}
\tag{3.3}
\]
Every symbol on the right was defined in §1 and is finite and universal.

## 4. Evaluation of \(\eta_K\)

The MAIN-CB contribution expands as
\[
\frac{\varepsilon_E}{C_A}
=\min\left\{
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}C_A},
\frac{e_H}{C_{\rm pre}C_A},
\frac{e_{\rm ext}}{C_{\rm pre}C_A},
\frac{e_{\rm sel}}{C_{\rm pre}C_A}
\right\}.
\tag{4.1}
\]
In particular, the hostile-verifier correction absorbed into
\(e_{\rm sel}\) is an explicit entry, not hidden inside prose.

Replace DECOMP's unspecified \(\min\mathfrak T\), and its insufficient
standalone normalization conditions
\((2C_{\Delta'})^{-1},(2C_{\Upsilon'})^{-1}\), by the actual unit-defect
sums. Define
\[
\boxed{
\begin{aligned}
\eta_K:=\min\biggl\{&
\frac18,\ \eta_A,\
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}C_A},\
\frac{e_H}{C_{\rm pre}C_A},\
\frac{e_{\rm ext}}{C_{\rm pre}C_A},\
\frac{e_{\rm sel}}{C_{\rm pre}C_A},\\
&\frac1{4C_\theta},\
\frac1{4C_EC_A},\
\frac1{2(C_T+C_{\Delta'})},\
\frac1{4(1+C_2+C_3+C_{\Upsilon'})},\
\frac1{2(C_T+C_{\Upsilon'})},\\
&\frac1{24K},\ 1
\biggr\}.
\end{aligned}}
\tag{4.2}
\]
The entries have the following roles, in order:

1. functional-calculus convergence/uniform linearization and the common
   source-linearization radius;
2. the four expanded MAIN-CB reset, H-CB, EXT-CB, and corrected selection
   thresholds;
3. the two raw-factor-map Neumann/norm bounds;
4. invertibility of \(\Delta'(I)\);
5. a common explicit small range for the fixed
   `Delta_norm`/degree-two/degree-three/`lem_RC` chain;
6. invertibility of \(\Upsilon'(I)\);
7. the stochastic-compression/PRH denominator and \(\eta\le1\).

All entries are positive: every coefficient is finite and at least one,
while \(\eta_A,\delta_{\max}^{\rm cb},e_H,e_{\rm ext},e_{\rm sel}\)
are positive by construction. Thus \(\eta_K>0\). No entry depends on
\(n\), \(\dim\mathcal H\), \(\dim\mathcal A\), the matrix size \(r\), a
block count, or a block dimension.

## 5. Route F finish at the honest rung

For \(\eta\le\eta_K\), (3.2) supplies the factorization input with common
constant \(K\). The already hostile-checked stochastic compression gives
\[
\varepsilon_{\rm PRH}:=\|MA-I_k\|_{\infty\to\infty}
\le\frac{3K\eta}{1-3K\eta}
\le4K\eta<\frac12,
\tag{5.1}
\]
where \(\eta_K\le(24K)^{-1}\). PRH then supplies a stochastic idempotent
\(E\) and
\[
\begin{aligned}
\|Q-E\|_{\infty\to\infty}
&\le K\eta+4\sqrt{2K\eta}\\
&\le\boxed{(K+4\sqrt{2K})\sqrt\eta},
\end{aligned}
\tag{5.2}
\]
using \(\eta_K\le1\).

This is now unconditional **in the former H-CB/EXT-CB/ledger gaps**, and
it rests on the following named artifact set:

- `PROOF-W74F-B-DIAGONAL.md` and the wave-1 batch verdict;
- `DECOMP-W74F-C-THMAINEXT.md` and the wave-1 batch verdict;
- `AUDIT-W74F-D-ALMOSTIDEMP.md` and the wave-1 batch verdict;
- `PROOF-W74F-E-HCB.md` plus `VERDICT-W74F-E-HCB.md`;
- `PROOF-W74F-F-EXTCB.md` plus `VERDICT-W74F-F-EXTCB.md`;
- `PROOF-W74F-A-PRH.md` plus `VERDICT-W74F-BATCH.md`.

**Rigour caveat.** The conclusion is `proved-mod-audit`, not rigorous in
the repository's L0 sense. None of MAIN-CB, H-CB, EXT-CB, this ledger, or
the assembled Route F chain is `af`-validated or Lean-formalized. The
local TeX is a pinned primary source, but its printed proof required the
recorded diagonal, squared-norm, type/index, H-CB, and EXT-CB repairs, so
the repaired chain is not a byte-verbatim theorem import.

In particular, the D-audit checked the long diagrammatic blocks
`tex:2239-2723` at the identity/estimate level and extracted the
dimension-free coefficient \(10\eta\); it was not a formal line-by-line
reproof. Its own residual register says that exact idempotence of the
functional-calculus projector still rests on the earlier source
construction, the canonical Stinespring commuting proposition
`tex:1621-1687` was used but not reconstructed from first principles,
and the literal operator-domain annotations and the \(V_1\) index at
`tex:2665` require correction.

## 6. Defect and judgment register

1. **No absolute decimal ledger is available.** The source does not print
   numerical values for \(C_{\rm app},C_{\rm inc},C_{\rm co},
   C_{\rm col},C_{\rm merge}\), their original admissible radii, or the
   componentwise coefficient \(C_{\Upsilon'}\). This forces the relative
   symbolic ledger above. No number was invented.

2. **\(C_{\Upsilon'}\) is symbolic but not dangling.** It is defined by
   the three producing inequalities (1.13) on the positive common radius
   \(\eta_A\). Extracting a shorter polynomial from `tex:2840-2895` would
   be a separate detailed constant audit, forbidden by this brief's
   no-new-mathematics rule.

3. **Normalization judgment.** \(C_{\rm co}\) was enlarged once to
   dominate all finitely many fixed compression/corner/selection
   coefficients in MAIN-CB, and \(\delta_{\max}^{\rm cb}\) was shrunk to
   a common APPROX/INC/IMPROVE/MERGE admissible radius. These changes are
   coefficient-neutral existential normalizations, but a fresh verifier
   should check that every source use fits the packet stated in §0.

4. **The reset bound is deliberately coarse.** The \(L^2\) in (2.2)
   pays for one compression after a reset, and the factor \(2\) in (2.3)
   pays for \(\delta_{\rm raw}+\varepsilon_X\). No claim of optimality is
   made. Its purpose is to close the common-threshold defect without a
   block-count factor.

5. **Normalization thresholds were corrected.** It is not enough to ask
   \(C_{\Delta'}\eta<1/2\) or
   \(C_{\Upsilon'}\eta<1/2\): the unnormalized unit also carries the raw
   unit defects \(C_T\eta\). Equation (4.2) therefore uses
   \(C_T+C_{\Delta'}\) and \(C_T+C_{\Upsilon'}\).

6. **H-CB inverse wording remains conditional where it must.** The exact
   \(\mathbb C\oplus\mathbb C\) example kills an unconditional inverse
   for arbitrary \(h_{P,P}\). EXT-CB establishes the required level-one
   lower modulus and bijectivity before invoking the corrected inverse
   clauses; this ledger does not restore the false wording.

7. **EXTCB-1 uses the verifier correction.** The level-one
   close-idempotent range identifications are included in \(e_{\rm sel}\).
   Omitting them would leave a threshold gap even though it would not
   change \(C_{\rm ext}\).

8. **The repaired diagonal is essential.** The formulas at `tex:1254`
   and `tex:2780-2783` are false for direct sums. The phase-balanced
   whole-algebra diagonal has exact projective norm and coefficient sum
   \(1\), which is why neither APPROX-CB nor \(C_{\Delta'}\) contains a
   block-count factor.

9. **No mathematical gap is knowingly left inside this relative
   ledger.** What remains is external hostile verification and eventual
   L0 closure. This document must not be described as self-verified,
   `af`-validated, or rigorous.
