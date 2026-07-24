SHA CHECK: PASS — `sha256sum refs/kitaev-2405.02434/approximate_algebras.tex` returned `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.

# W74F-G hostile-verifier verdict

I read the pinned TeX before the target and checked the cited functional-calculus,
approximate-algebra, MAIN-CB, factor-map, CP-ization, and degree-two/three loci
directly. The ledger has one closure-critical omission in MAIN-CB Stage 1. The
subsequent factor-map arithmetic is sound, but it cannot make the displayed
threshold unconditional.

## Per-section verdicts

### Symbol table — INVALID

The table is not complete for the entire Route F pipeline. The printed MAIN proof
uses `lem_nontriv_projection` at `tex:1419`; that lemma is stated only as producing
a nontrivial \(O(\varepsilon_X)\)-projection at `tex:931-943`. The resulting fresh
projections \(P',P''\) and fresh split inclusion
\(v_{\rm comm}^{(2)}:\mathbb C^2\to\mathcal S_{P_m}\) occur at
`tex:1419-1425` before the Stage-1 merge at `tex:1426`.

Neither the coefficient of this \(O(\varepsilon_X)\) construction nor its positive
input-validity threshold appears in §1. They are not instances of the listed
compression-transfer estimate: `lem_nontriv_projection` is produced by the
approximate-unitary/topological construction at `tex:915-969`. In particular:

- \(C_{\rm co}\) is defined only for compression, compressed units/products,
  corner-algebra errors, one compression transfer, and fixed-corner coefficients;
- \(\delta_{\max}^{\rm cb}\) is defined only as a common
  APPROX/INC/IMPROVE/MERGE radius;
- \(e_{\rm sel}\) covers the three named dimension lemmas and the EXTCB-1
  close-idempotent identifications, not `lem_nontriv_projection`.

An exact repair must introduce a Stage-1 packet, for example universal
\(C_{\rm split}\ge1\) and \(e_{\rm split}>0\), whose producing statement is:
whenever the current corner has defect
\(\varepsilon_X\le e_{\rm split}\) and dimension \(>1\),
`lem_nontriv_projection` and the two induced commutative split inclusions at
`tex:1419-1425` have all raw defects at most
\(C_{\rm split}\varepsilon_X\), with the required nonvanishing conclusions.

### Reset verification — INVALID

The assertion at target (2.2) that every pre-extension/merge packet arises from
the reset map followed by at most one compression is false for Stage 1.
\(v_{\rm comm}^{(2)}\) is newly built from \(P',P''\); it is not a compression of
the preceding maximal commutative inclusion. Thus
\[
 \delta_{\rm raw}\le C_{\rm co}(1+c_0^{\rm cb})\varepsilon_X
\]
does not follow for this packet, and (2.3)--(2.5) do not prove that the Stage-1
merge output is below \(\delta_{\max}^{\rm cb}\).

The claimed structural statement is otherwise correct: Stage 2 has exactly the
printed compression at `tex:1435-1439`, followed by extension and immediate
IMPROVE reset at `tex:1441`; each Stage-3 binary merge is followed by an immediate
reset at `tex:1443`. Those stages acquire no block-count or amplification factor.

A sufficient correction is to set
\[
 C_{\rm main}:=\max\{C_{\rm co},C_{\rm split}\},\qquad
 L:=C_{\rm main}(1+c_0^{\rm cb}),
\]
retain
\[
 C_{\rm pre}:=2L^2\max\{1,C_{\rm ext},C_{\rm merge}\},
\]
and add \(e_{\rm split}/C_{\rm pre}\) to \(\varepsilon_E\). Then
\(\varepsilon_X\le L\varepsilon\le C_{\rm pre}\varepsilon
\le e_{\rm split}\), while both the compression packets and the fresh split
packet are bounded by \(L^2\varepsilon\). This correction must itself be
verified against the complete Stage-1 construction; it cannot be supplied merely
by relabelling \(C_{\rm co}\).

### Normalizations — INVALID

Enlarging a universal coefficient over finitely many specified source estimates
and shrinking to a common positive radius are legitimate operations. The target's
normalization is nevertheless incomplete because its stated finite family omits
the Stage-1 projection/split construction above. Folding that construction into
\(C_{\rm co}\) after the fact would contradict the producing inequality and locus
given for \(C_{\rm co}\), and would still leave its admissibility threshold
unstated.

The other normalization judgments pass:

- replacing \(a_{\rm app},a_{\rm merge}\) in EXT-CB by the smaller common
  \(\delta_{\max}^{\rm cb}\) is sufficient;
- \(e_{\rm sel}\) correctly includes the EXTCB-1 close-idempotent range
  identifications;
- the H-CB common input radius is legitimately absorbed into the normalized
  \(c\);
- the repaired whole-algebra diagonal has coefficient sum/projective norm \(1\),
  so no block-count factor is introduced.

### \(K\) — VALID

The three expressions in (3.1) recompute correctly. With
\(\|\widetilde\Delta\|_{\rm cb},\|\widetilde\Upsilon\|_{\rm cb}\le2\),
\[
\begin{aligned}
\|\Delta\Upsilon-\Phi\|_{\rm cb}
&\le(C_\theta+C_\Delta+2C_\Upsilon)\eta,\\
\|\Upsilon_n(\Delta_n(X)\Delta_n(Y))-XY\|
&\le\bigl[C_\Upsilon+2(C_2+C_\theta+C_\Delta)\bigr]
  \eta\|X\|\|Y\|,\\
\|\Upsilon\Delta-I_{\mathcal B}\|_{\rm cb}
&\le(C_\Upsilon+2C_\Delta)\eta.
\end{aligned}
\]
For the middle estimate,
\(\widetilde\Upsilon\widetilde\Phi=\widetilde\Upsilon\) and
\(\widetilde\Upsilon\widetilde\Delta=I\) are exact, so there is no omitted
composition term. The maximum in (3.3) also dominates the degree-two estimate
needed upstream. Every coefficient in \(K\) is finite and dimension-free. The
Stage-1 defect does not change this formula; it changes the admissible threshold
under which \(C_E=c_0^{\rm cb}\) is reached.

The intermediate arithmetic also passes:
\[
C_{\Delta'}=C_T+4C_\theta,\qquad
C_\Delta=6C_T+7C_{\Delta'},\qquad
C_2=C_{\Delta'}+4C_\Delta,
\]
and the five-step calculation at `tex:2817-2829` gives
\[
C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'}.
\]

### \(\eta_K\) — INVALID

Every displayed entry of (4.2) is defined, positive, noncircular, and sufficient
for its stated local role:

- \(1/8,\eta_A\) guard functional calculus and the finite source
  linearizations;
- the four \(C_{\rm pre}C_A\) denominators guard the listed reset,
  H-CB, EXT-CB, and EXTCB-1 selection ranges;
- \(1/(4C_\theta)\) and \(1/(4C_EC_A)\) give the raw-factor norm/Neumann
  bounds;
- \(1/[2(C_T+C_{\Delta'})]\) is the correct condition for
  \(a=\Delta'(I)\), because
  \(\|a-I\|\le(C_T+C_{\Delta'})\eta\);
- \(1/[2(C_T+C_{\Upsilon'})]\) is analogously the correct condition for
  \(\Upsilon'(I)\);
- the common \(1/[4(1+C_2+C_3+C_{\Upsilon'})]\) range is dimension-free
  and sufficient for the fixed `Delta_norm`/degree-two/degree-three/`lem_RC`
  chain;
- \(1/(24K)\) and \(1\) suffice for the finish.

But the minimum has no term guarding
\(\varepsilon_X\le e_{\rm split}\). With the correction above, (4.2) must
also contain
\[
 \boxed{\frac{e_{\rm split}}{C_{\rm pre}C_A}}.
\]
Equivalently one may redefine a named common MAIN radius to include
\(e_{\rm split}\), but the symbol table must still state the producing
Stage-1 threshold and the reset proof must show how it is consumed. As written,
\(\eta_K>0\) is a positive number but is not sufficient for every Route F step.

### Finish — VALID

Conditional on \(\eta\) lying below a genuinely sufficient corrected
\(\eta_K\), (5.1)--(5.2) are correct. From
\(\eta\le(24K)^{-1}\),
\[
 3K\eta\le\frac18,\qquad
 \frac{3K\eta}{1-3K\eta}\le4K\eta\le\frac16<\frac12.
\]
PRH therefore applies with constant \(2\sqrt2\), and
\[
 2\sqrt{2\varepsilon_{\rm PRH}}
 \le2\sqrt{8K\eta}=4\sqrt{2K\eta}.
\]
Together with the \(K\eta\) factorization error and \(\eta\le1\), this gives
\[
 \|Q-E\|_{\infty\to\infty}
 \le(K+4\sqrt{2K})\sqrt\eta.
\]
There is no wrong coefficient or missing dimension factor in this final
composition.

### Honesty — VALID-WITH-CORRECTIONS

The L0 caveat is accurate: none of MAIN-CB, H-CB, EXT-CB, this ledger, or the
assembled Route F chain is `af`-validated or Lean-formalized, and the repaired
argument is not a byte-verbatim theorem import. The description of the D-audit
also matches its residual register: it checked the diagrammatic identities and
estimates, while retaining the functional-calculus dependency, the canonical
Stinespring dependency, and the printed type/index corrections.

The artifact nevertheless overclaims mathematical closure at §0 and §6(9).
Until the Stage-1 packet is supplied, “unconditional relative
universal-constant ledger” and “No mathematical gap is knowingly left inside
this relative ledger” must be replaced by:

> The factor-map and finish ledgers are closed relative to MAIN-CB, H-CB, and
> EXT-CB, but MAIN-CB still requires a named universal coefficient and positive
> threshold for the `lem_nontriv_projection` Stage-1 split packet.

No absolute numerical constant, `af` validation, or byte-verbatim repaired import
is otherwise claimed.

## Overall verdict

**INVALID.** The relative ledger is **not CLOSED** as written. It has no dangling
factor-map coefficient and no dimension, block-count, block-dimension, or
amplification dependence in the parts that were actually quantified. It does,
however, have one dangling Stage-1 coefficient and one dangling Stage-1
threshold: the \(O(\varepsilon_X)\) nontrivial-projection/split construction at
`tex:1419-1425`. Consequently (2.2)--(2.5) do not cover every raw pre-reset
packet, and the displayed \(\eta_K\) is not sufficient for the complete
MAIN-CB pipeline. Route F still needs exactly this Stage-1 packet to be extracted,
inserted into \(L,C_{\rm pre},\varepsilon_E,\eta_K\), and freshly verified. After
that, the checked \(K\) formula and PRH finish require no further mathematical
change. L0 closure—independent formal or byte-provenanced validation of the
repaired chain—also remains open.

## Registry-impact note

Do **not** codify this artifact as a closed ledger lemma in its present form, and
do not use it to claim an unconditional Route F theorem. The H-CB and EXT-CB
registry contracts need no amendment from this audit.

After the Stage-1 packet is repaired and hostile-verified, codify a separate
ledger node at `proved-mod-audit` (not `proved`/`af: validated`) with dependencies
on `lem-thmainext-conditional`, `cor-kitaev-diagonal-cpization`,
`lem-kitaev-almost-idemp-audit`, and `lem-prh`. A suitable exact contract is:

> Relative Route F factorization ledger: there are universal
> \(K\ge1\) and \(\eta_K>0\), independent of Hilbert-space dimension,
> amplification level, simple-block count, and block dimensions, such that for
> every \(0\le\eta\le\eta_K\) the repaired Kitaev factorization supplies UCP
> maps \(\Delta,\Upsilon\) with the three estimates bounded by \(K\eta\), and
> the associated stochastic map admits a stochastic idempotent \(E\) satisfying
> \(\|Q-E\|_{\infty\to\infty}\le
> (K+4\sqrt{2K})\sqrt\eta\); the constants and threshold are the explicit
> relative finite expressions in the hostile-verified ledger.

The conditional framing of `lem-thmainext-conditional` is stale now that H-CB and
EXT-CB are `proved-mod-audit`, but it should not be restated as an explicit
closed-threshold result until the Stage-1 repair lands. At that point replace its
contract by:

> Extended `th_main_ext` assembly: there are universal
> \(C_E<\infty\) and \(\varepsilon_E>0\) such that every finite-dimensional
> extended \(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\), for
> \(0\le\varepsilon\le\varepsilon_E\), is carried by one extended
> \(C_E\varepsilon\)-isomorphism \(v:\mathcal B\to\mathcal A\) from a
> finite-dimensional \(C^*\)-algebra; the assembly uses the corrected squared
> COL-HILB estimate and the hostile-verified H-CB, EXT-CB, and Stage-1 reset
> packets, with constants independent of dimension, amplification level, and
> block data.

Keep that amended node at `proved-mod-audit`; the historical
`lem-thmainext-conditional` id may remain stable.

## Checks performed that passed

1. Recomputed the primary-source SHA256 exactly.
2. Read `tex:458`, the functional calculus at `tex:2171-2179`, and the
   approximate-algebra construction at `tex:2192-2209`.
3. Recomputed
   \(C_\theta=12(\sqrt2-1)\) from the \(r(\eta)\) bound on
   \(\eta\le1/8\).
4. Checked
   \((1+r)^5-1\le(211/16)r\) for \(0\le r\le1/2\) and the resulting
   \(C_A=20+(211/8)C_\theta\).
5. Checked the source error-reduction, INC-CB, APPROX-CB, fixed four-corner
   MERGE-CB, and their finite universal-radius normalization.
6. Recomputed the hostile-verified H-CB values
   \(C_H=4000c\), \(e_H=(10000c)^{-1}\), including the corrected
   compressed-unit and conditional-inverse clauses.
7. Recomputed
   \(A_0,\kappa,D_0,C_{\rm ext}\) and every displayed EXT-CB threshold;
   confirmed that \(e_{\rm sel}\) includes the EXTCB-1 close-idempotent
   correction.
8. Walked every printed MAIN stage at `tex:1414-1444`; confirmed the
   one-compression/immediate-reset pattern in Stages 2 and 3 and isolated the
   distinct fresh split in Stage 1.
9. Read `lem_nontriv_projection` at `tex:915-969` and confirmed that its
   coefficient/radius is not produced by COMP-CB.
10. Checked that the repaired whole-algebra diagonal has total weight and
    projective norm \(1\), and rechecked complete positivity of \(\Delta'\)
    from exact diagonal centrality.
11. Recomputed the \(\Delta'\) unitalization bound, including the necessary
    unit-defect sum \(C_T+C_{\Delta'}\).
12. Recomputed `Delta_norm`, `PhiDelta1`, degree-two, and degree-three
    constants \(C_2,C_3\) against `tex:2803-2829`.
13. Checked the componentwise \(\Upsilon'\) construction at
    `tex:2840-2895`; probability averaging and the direct-sum maximum norm
    introduce no term count or block-count factor.
14. Recomputed the \(\Upsilon'\) unitalization bound and the necessary
    \(C_T+C_{\Upsilon'}\) inversion condition.
15. Recomputed all three \(K\) telescopes, including exact use of
    \(\widetilde\Upsilon\widetilde\Phi=\widetilde\Upsilon\) and
    \(\widetilde\Upsilon\widetilde\Delta=I\).
16. Checked every displayed \(\eta_K\) entry for definition, positivity,
    local sufficiency, and circularity; all passed except completeness of the
    missing Stage-1 entry.
17. Checked that no surviving constant depends on \(n\),
    \(\dim\mathcal H\), amplification level, simple-block count, or block
    dimension.
18. Recomputed the stochastic-compression denominator, the \(4K\eta\)
    estimate, the strict PRH \(<1/2\) trigger, and the final
    \(K+4\sqrt{2K}\) coefficient.
19. Compared the rigour caveat and D-audit scope statement with
    `AUDIT-W74F-D-ALMOSTIDEMP.md`'s residual register; they agree.
