SHA CHECK: PASS — `sha256sum refs/kitaev-2405.02434/approximate_algebras.tex` returned `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.

# W74F-H hostile-verifier verdict

I read the pinned TeX before the G-verdict and the target. The fresh
nontrivial-projection/\(\mathbb C^2\)-split packet is dimension-free, including
the load-bearing isolation step at `tex:943`. Two bookkeeping corrections are
required: the old compressed side of the Stage-1 merge does not live in the
fresh split corner and must retain its own ambient-defect variable, and the
finite constant ledger should explicitly include the final
isolation-to-nonvanishing shrink. Neither correction changes
\(C_{\rm main}\), \(C_{\rm pre}\), \(K\), or the displayed
\(\eta_K^{\rm corr}\).

## Per-section verdicts

### Packet statement §0 — VALID-WITH-CORRECTIONS

Items 1 and 2 are valid. There are universal \(C_{\rm split}\geq1\) and
\(e_{\rm split}>0\) for the fresh construction in the split corner
\(\mathcal X=\mathcal S_{P_m}\): the two complementary Hermitian elements have
all four projection/cross defects \(O(\varepsilon_X)\), remain nonvanishing,
and define one extended \(O(\varepsilon_X)\)-inclusion
\(\mathbb C^2\to\mathcal X\).

Item 3, as parameterized, is not literally the Stage-1 situation.
\(v_{\rm comm}^{(1)}\) takes values in
\(\mathcal S_{P_{[1,m-1]}}\), whereas the fresh map takes values in
\(\mathcal S_{P_m}\). The preceding maximal commutative map is reset relative
to the Stage-1 ambient algebra, not relative to the exact defect
\(\varepsilon_X\) of \(\mathcal S_{P_m}\). No inequality in the source forces
the former defect to be bounded by the latter.

The exact correction is:

> Let \(\varepsilon_0\) be the Stage-1 ambient-algebra defect and let
> \(\varepsilon_S\) be the defect of the fresh split corner
> \(\mathcal S_{P_m}\). Then COMP-CB gives
> \[
> \operatorname{def}_{\rm ext}(v_{\rm comm}^{(1)})
> \le C_{\rm co}(1+c_0^{\rm cb})\varepsilon_0,
> \]
> while the fresh packet gives
> \[
> \operatorname{def}_{\rm ext}(v_{\rm comm}^{(2)})
> \le C_{\rm split}\varepsilon_S.
> \]
> In MAIN-CB, \(\varepsilon_S\le
> C_{\rm co}(1+c_0^{\rm cb})\varepsilon_0\).

Equivalently, one may use a declared common upper envelope for the two local
defects, but one must not call that envelope “the defect of
\(\mathcal S_{P_m}\).” When \(m=1\), the old side is absent as stated.

### Construction §1, exact-unit rectification — VALID

`prop_unit` is sufficient. Its inverse-function and Neumann estimates are in
operator norm on the underlying Banach space. After a universal shrink they
give a rectified exact unit \(J\), a product differing from the original one by
\(O(\varepsilon_X)\), and a rectified \(O(\varepsilon_X)\)-\(C^*\) defect.
No Euclidean norm comparison or dimension-dependent inverse bound is used.

The fixed-point construction then gives
\(\|U^\dagger-U\|=O(\varepsilon_X)\). Expanding
\[
P_0=\tfrac14(2J+U+U^\dagger)
\]
uses a fixed number of products and the relations
\(U^\dagger\boldsymbol\cdot U=J\),
\(U\boldsymbol\cdot U^\dagger=J+O(\varepsilon_X)\); hence
\(\|P_0\boldsymbol\cdot P_0-P_0\|=O(\varepsilon_X)\) with a universal
coefficient.

### Construction §1, the `tex:943` uniform-isolation expansion — VALID

This was the principal attack target. It does not hide a dimension factor.
In the exact-unit \(J\)-chart, the source's `der_gr_inverse` formula and the
transition estimate at `tex:728-762`, `790-892` give, uniformly for
\(\|U-J\|\le r\),
\[
D(\sigma-\operatorname{id})=-2I+E,\qquad
\|E\|\le C(r+\varepsilon_X),
\]
where \(C\) is independent of the Banach-space dimension. Indeed,
\(L_U,R_U\) are \(O(r)\)-close to the identity, their Neumann inverses have
fixed norm, and the tangential/Hermitian projections have norm at most one.
Choose a universal \(r_{\rm iso}\) inside the fixed polar neighborhood, then
shrink \(\varepsilon_X\) so \(\|E\|<1\). The quantitative inverse-function
lemma makes \(J\) the unique fixed point in that ball. Scalar equivariance of
the polar map gives the identical conclusion at \(-J\).

The quotient is legitimate. The vertical tangent line is
\(i\mathbb R J\), it is invariant under \(D\sigma\), and the induced error on
\(i\mathcal H/i\mathbb R J\), equipped with the quotient norm, is no larger
than the original operator-norm error. Thus
\[
D\breve\sigma(\breve e)=-I+O(\varepsilon_X)
\]
with the same dimension-free control. In fact, no quotient chart radius is
needed for the quantitative conclusion: topology supplies a non-scalar fixed
class; scalar equivariance lifts it to two genuine fixed points of \(\sigma\).
Neither lift can lie in the two uniform isolation balls, since otherwise it
would equal \(\pm J\) and represent the scalar class.

### Construction §1, topological inputs — VALID

The use at `tex:945-1049` is sufficient. The quotient is a connected,
positive-dimensional, compact orientable \(C^1\) manifold and hence has finite
CW type. The left-inversion \(H\)-space argument gives
\(\operatorname{Tr}\breve\sigma^{*k}=(-1)^k\dim H^k\), so the Lefschetz
number is the sum of the Betti numbers. Degree zero and top degree contribute
at least two, while the nondegenerate scalar fixed point has index \(+1\).
Consequently it cannot be the only fixed point. These inputs produce existence
only; they introduce no analytic coefficient or metric conversion.

### Construction §1, exact-unit transfer — VALID

The transfer back to the original corner is correct. Put
\[
P'=P_0,\qquad P''=I_{\mathcal X}-P_0.
\]
Product closeness and \(\|J-I_{\mathcal X}\|=O(\varepsilon_X)\) transfer the
two rectified projection defects and both norm alternatives. The original
approximate unit laws give
\[
\|P'P''\|,\|P''P'\|=O(\varepsilon_X).
\]
Only a fixed number of terms occurs. The projection used by Stage 1 therefore
belongs to the original corner packet, not merely to the rectified algebra.

### Construction §1, fresh all-level inclusion — VALID

Identity (1.14) is exact in \(M_n\otimes\mathcal X\) and has four terms,
independent of \(n\). The operator-space identity at `tex:1475` gives
\(\|T\otimes z\|=\|T\|\|z\|\), so the multiplicativity defect is at most
\(4d\|x\|\|y\|\) without an entrywise sum.

Multiplication by \(I_n\otimes q_i\) gives a uniform preliminary lower modulus
\(1/4\). Applying `prop_delta_hominc`, `tex:1194-1222`, to
\[
v_n:M_n(\mathbb C^2)\longrightarrow M_n\otimes\mathcal X
\]
then yields \(1\pm O(\varepsilon_X)\) norm bounds with the same universal
coefficient at every \(n\). The proposition's proof uses only the \(C^*\)
inequality and scalar quadratic estimates, so no amplification dimension is
hidden. The unit and involution are preserved exactly.

### Construction §1, old side SPLIT-C — VALID-WITH-CORRECTIONS

The structural argument is valid: this is one restriction followed by one
amplified compression, not a sum over \(m-1\) basis projections, so there is
no \(m\)-factor. Its producing estimate must, however, use the old ambient
defect \(\varepsilon_0\), as in the correction to §0, rather than the fresh
corner's exact defect \(\varepsilon_X\). SPLIT-C remains part of COMP-CB; it is
not part of the new analytic split coefficient.

### Constant ledger §2 — VALID-WITH-CORRECTIONS

All fresh analytic coefficients and radii are finite universal maxima/minima.
One final shrink used in the prose should be visible in (2.1). If
\(C_{\rm small}\) bounds the small alternative in `P_alternatives` and
\(C_{\rm sep}\) bounds the \(O(\varepsilon_X)\) terms in (1.8), define
\[
e_{\rm nv}:=
\min\left\{e_{\rm iso},
\frac{r_{\rm iso}}{2(2C_{\rm small}+C_{\rm sep})}\right\}.
\]
Replace \(e_{\rm iso}\) by \(e_{\rm nv}\) in \(e_{\rm np}\), or explicitly
shrink \(e_{\rm iso}\) by this amount. Then a fixed point outside the isolation
balls cannot fall into the small projection alternative.

Also keep \(C_{\rm old},e_{\rm old}\) under the existing COMP-CB packet, or
state them against \(\varepsilon_0\). They need not be included in the
definition of the fresh \(C_{\rm split},e_{\rm split}\). Including their
numerical maxima is harmless only after a common upper-envelope variable has
been declared. With these two corrections, the table's independence claims
are valid.

### Corrected reset chain §3 — VALID-WITH-CORRECTIONS

The displayed constants are correct:
\[
C_{\rm main}=\max\{C_{\rm co},C_{\rm split}\},\qquad
L=C_{\rm main}(1+c_0^{\rm cb}),\qquad
C_{\rm pre}=2L^2\max\{1,C_{\rm ext},C_{\rm merge}\}.
\]
The proof must distinguish the ambient defect of each call from the fresh
split-corner defect. Write \(\varepsilon_Y\) for the ambient defect of the
particular extension or merge. The uniform corner construction gives
\(\varepsilon_Y\le L\varepsilon\).

The complete stage walk is then:

1. In Stage 1, COMP-CB gives the old-side defect at most
   \(C_{\rm co}(1+c_0^{\rm cb})\varepsilon\le L^2\varepsilon\).
   The split corner has defect \(\varepsilon_S\le L\varepsilon\), so the fresh
   side has defect at most
   \(C_{\rm split}\varepsilon_S\le L^2\varepsilon\).
   Their binary merge has ambient defect \(\varepsilon\le L\varepsilon\).
2. In Stage 2, each reset is relative to its current corner. There is exactly
   one compression before EXT-CB, giving a raw packet at most
   \(L\varepsilon_Y\le L^2\varepsilon\), followed immediately by IMPROVE-CB.
3. In Stage 3, each binary MERGE-CB call uses already-reset maps and is
   followed immediately by IMPROVE-CB. Every sum corner again has defect at
   most \(L\varepsilon\).

Thus, for every call,
\[
\delta_{\rm raw}\le L^2\varepsilon,\qquad
e_{\rm raw}:=\delta_{\rm raw}+\varepsilon_Y
\le(L^2+L)\varepsilon\le2L^2\varepsilon.
\]
The output estimates (3.8) are therefore bounded by
\(C_{\rm pre}\varepsilon\). There is no stage-count, block-count,
block-dimension, or amplification factor. This is the same numerical chain as
the target; only the local-defect notation is corrected.

The radius
\[
\varepsilon_E^{\rm corr}=
\min\left\{
\frac{\delta_{\max}^{\rm cb}}{C_{\rm pre}},
\frac{e_H}{C_{\rm pre}},
\frac{e_{\rm ext}}{C_{\rm pre}},
\frac{e_{\rm sel}}{C_{\rm pre}},
\frac{e_{\rm split}}{C_{\rm pre}}
\right\}
\]
then puts every raw output and every local input in range. Since
\(C_{\rm pre}\ge L\), the split invocation is noncircular.

### Corrected \(\eta_K\) delta §4 — VALID

The new guard
\[
\boxed{\frac{e_{\rm split}}{C_{\rm pre}C_A}}
\]
is exactly the required one. From
\(\varepsilon_{\rm AI}(\eta)\le C_A\eta\), it gives
\[
C_{\rm pre}\varepsilon_{\rm AI}(\eta)\le e_{\rm split},
\]
which dominates every split-corner defect by the corrected reset chain before
`lem_nontriv_projection` is invoked. It has no circular dependence on
\(C_{\rm split}\): all quantities are first fixed universal constants, and
only then is \(\eta_K^{\rm corr}\) chosen. The remaining entries of (4.2)
retain the roles and positivity checked in the G-verdict.

### Scope and finish §§5-6 — VALID

The repair changes only the admissible MAIN-CB radius. It does not change
\(C_E=c_0^{\rm cb}\) after the final reset, so no factor-map coefficient
changes. The formula
\[
K=\max\{1,\,
C_\theta+C_\Delta+2C_\Upsilon,\,
C_\Upsilon+2(C_2+C_\theta+C_\Delta),\,
C_\Upsilon+2C_\Delta\}
\]
is untouched. PRH, H-CB, EXT-CB, the factor-map telescopes, and the final
\((K+4\sqrt{2K})\sqrt\eta\) bound are also untouched.

The hypothesis-hygiene list is correct after replacing the single
\(\varepsilon_X\) in its old-side discussion by the local variables above.
Finite dimensionality is used topologically but not as an analytic
coefficient; extended structure is used only for the all-level transfer.

### Honesty §7 and defect register §8 — VALID

The two required honesty sentences have the correct conditional content and
match the G-verdict's demand. After the corrections in this verdict are
incorporated as binding bookkeeping, the condition “survives separate fresh
hostile verification” is met at the `proved-mod-audit` rung only. Nothing here
is `af`-validated, Lean-formalized, or a byte-verbatim import of the repaired
chain.

## Overall verdict

**VALID-WITH-CORRECTIONS.** Yes: with the old/fresh corner defects separated
as above and the final nonvanishing shrink made explicit, the Route F relative
\(K/\eta_K\) ledger is **CLOSED at `proved-mod-audit`**. The `tex:943`
isolation radius is dimension-free; the quotient is legitimate; the
topological step adds no analytic coefficient; exact-unit transfer recovers
the original corner; and the all-level split uses one four-term identity with
no \(n\)-sum. The G-verdict's sole mathematical omission is discharged. The
only remaining open work is L0 closure of the repaired Route F chain
(`af`/Lean or another repository-approved rigorous route); in particular PRH
and the large MAIN-CB/H-CB/EXT-CB chain remain below T0. The two corrections
above are necessary wording/ledger corrections, not new conjectures or
unnamed coefficients.

## Registry-impact note

The G-verdict's codification plan is confirmed. Codify a separate ledger node
at `proved-mod-audit`, with dependencies on
`lem-thmainext-conditional`, `cor-kitaev-diagonal-cpization`,
`lem-kitaev-almost-idemp-audit`, and `lem-prh`. I endorse this exact contract:

> Relative Route F factorization ledger: there are universal
> \(K\ge1\) and \(\eta_K>0\), independent of Hilbert-space dimension,
> amplification level, simple-block count, and block dimensions, such that for
> every \(0\le\eta\le\eta_K\) the repaired Kitaev factorization supplies UCP
> maps \(\Delta,\Upsilon\) with the three estimates bounded by \(K\eta\), and
> the associated stochastic map admits a stochastic idempotent \(E\) satisfying
> \(\|Q-E\|_{\infty\to\infty}\le
> (K+4\sqrt{2K})\sqrt\eta\); the constants and threshold are the explicit
> relative finite expressions in the hostile-verified ledger.

The historical `lem-thmainext-conditional` id may remain stable and should be
restated at `proved-mod-audit`. I endorse this exact contract:

> Extended `th_main_ext` assembly: there are universal
> \(C_E<\infty\) and \(\varepsilon_E>0\) such that every finite-dimensional
> extended \(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\), for
> \(0\le\varepsilon\le\varepsilon_E\), is carried by one extended
> \(C_E\varepsilon\)-isomorphism \(v:\mathcal B\to\mathcal A\) from a
> finite-dimensional \(C^*\)-algebra; the assembly uses the corrected squared
> COL-HILB estimate and the hostile-verified H-CB, EXT-CB, and Stage-1 reset
> packets, with constants independent of dimension, amplification level, and
> block data.

In both codifications, the body should record the correction that
\(C_{\rm split},e_{\rm split}\) govern the fresh
\(\mathbb C^2\)-inclusion, while the old Stage-1 side remains governed by
COMP-CB against its own ambient defect.

## Checks performed that passed

1. Recomputed the primary-source SHA256 exactly.
2. Read `lem_nontriv_projection` and its complete proof at `tex:915-969`.
3. Read the exact-unit rectification and its inverse-function input at
   `tex:663-687`.
4. Read the unitary charts, polar map, group operations, and inversion
   derivative at `tex:690-914`.
5. Derived the fixed \(J\)-chart estimate
   \(D(\sigma-\mathrm{id})=-2I+O(r+\varepsilon_X)\) in operator norm.
6. Checked that the isolation radius and all Neumann/IFT margins are
   independent of \(\dim\mathcal X\).
7. Checked scalar equivariance, invariance of the vertical tangent line, and
   the induced quotient derivative in the quotient norm.
8. Checked the Lefschetz-Hopf index calculation and the Hopf/augmentation
   trace calculation at `tex:945-1049`.
9. Checked compactness, orientability, positive dimension, finite-CW type,
   and the two nonzero cohomology degrees used in the contradiction.
10. Checked that a non-scalar quotient fixed point lifts to two genuine fixed
    points and that isolation gives their fixed separation from \(\pm J\).
11. Expanded the rectified projection defect and checked both nonvanishing
    alternatives.
12. Transferred both projection defects, both norm estimates, and both cross
    products back to the original approximate unit/product.
13. Recomputed the four-term amplified multiplicativity identity (1.14).
14. Applied the `tex:1475` elementary-tensor isometry without an entrywise
    matrix estimate.
15. Recomputed the uniform preliminary lower modulus for the fresh
    \(\mathbb C^2\)-map.
16. Read and applied `prop_delta_hominc`, `tex:1194-1222`, uniformly to every
    amplification.
17. Read the Stage-1 split and merge at `tex:1414-1426`.
18. Walked the Stage-2 compression/extension/reset at `tex:1428-1441`.
19. Walked every Stage-3 binary merge/immediate reset at `tex:1443`.
20. Rechecked the error-reduction and binary-merge source statements at
    `tex:1316-1359`.
21. Verified that the old Stage-1 side is one restriction plus one
    compression and therefore has no \(m\)-factor.
22. Recomputed \(C_{\rm main}\), \(L\), \(C_{\rm pre}\), all raw/output
    inequalities, and \(C_{\rm pre}\ge L\).
23. Verified that the corrected reset proof works with per-corner ambient
    defects and has no step-count, block-count, block-dimension, or
    amplification factor.
24. Verified that \(e_{\rm split}/(C_{\rm pre}C_A)\) is sufficient,
    positive, and noncircular.
25. Swept the remaining Route F ledger entries and found no additional
    unnamed coefficient beyond the already defined finite universal
    normalizations.
26. Confirmed that the artifact does not alter \(K\), PRH, H-CB, EXT-CB, or
    their previously verified thresholds and formulas.
27. Compared both honesty sentences with the G-verdict's required scope and
    confirmed the `proved-mod-audit`/L0 distinction.
