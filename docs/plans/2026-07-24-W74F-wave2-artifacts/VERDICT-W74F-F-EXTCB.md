SHA CHECK: PASS — `sha256sum refs/kitaev-2405.02434/approximate_algebras.tex` returned `e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.

# W74F-F hostile-verifier verdict

I read the pinned source first, in particular `lem_PQR` and `lem_1d_proj`
(`tex:1162-1185`), `lem_merging` and `cor_merge_sum` (`tex:1325-1359`),
`lem_add_dim` (`tex:1363-1369`), `lem_extension` including
`merging0h`--`merging3h` (`tex:1378-1412`), and `lem_approx_ext`
(`tex:1508-1535`). I then checked the prover output against the amended H-CB
contract and recomputed its estimates.

## Per-section verdicts

### Premise ledger — VALID

The proof uses only the amended conditional H-CB clauses, APPROX-CB,
MERGE-CB, and the level-one selection machinery. In particular, it does not
use an unconditional inverse for a general \(h_{P,P}\). Enlarging the three
universal constants to be at least one and absorbing the compressed-unit
estimate into \(C_H\) are legitimate. The APPROX-CB target is the exact
\(C^*\)-algebra \(\mathcal B(H_1)\), and MERGE-CB is invoked with one fixed
two-by-two corner partition.

One nonmathematical sentence is stale: §10(1) says that the registered H-CB
contract “still requires” correction, whereas `argument/lemmas/conj-hcb.md`
already contains the corrected conditional clauses. This does not affect the
proof.

### EXTCB-1 — VALID-WITH-CORRECTIONS

The dimension dichotomy is level-one only and has no \(r\)-dependent norm
estimate. Once the matrix-unit corners \(R_a=v(E_{aa})\) are known to be
one-dimensional and mutually equivalent, `lem_1d_proj` gives
\(\dim\mathcal S_{R_a,Q}\le1\), `lem_PQR` makes these dimensions equal, and
`lem_add_dim` plus \(\mathcal S_{P,Q}\ne0\) gives
\(\dim\mathcal S_{P,Q}=r\).

The correction is that §2 suppresses an exact normalization required by the
printed statement of `lem_add_dim`. That lemma initially gives the corner for
\(\widehat P=v(I_r)\), not literally the externally named \(P\). The proof
must state that
\[
 \|\widehat P-P\|=O(e),\qquad
 \|\operatorname{Co}_{\widehat P,Q}
       -\operatorname{Co}_{P,Q}\|=O(e),
\]
using the unit condition for \(v\), \(u_P=\operatorname{Co}_P(P)\), and
`tex:1054-1064`. For a universal smallness threshold the two compression
operators are idempotents at distance \(<1\); restriction of either to the
other's range is injective in both directions, so their ranges have the same
dimension. The same close-idempotent argument justifies the source's terse
assertion that the \(R_a\) are one-dimensional matrix-unit corners. This is a
level-one, universal-threshold correction and introduces neither \(r\)- nor
amplification-level dependence.

Accordingly, §1.4 must say that \(e_{\rm sel}\) also covers these
close-idempotent range identifications, not only the three named lemmas. No
change to the claimed \(C_{\rm ext}\) is required.

### EXTCB-2 — VALID

For \(T=h_{11}v\), the composition estimate is
\[
 \operatorname{def}(T_m)
 \le (1+C_He)\delta+C_He(1+\delta)^2
 \le4(C_H+1)e.
\]
Its unit defect has the same safe upper coefficient, and involution
preservation is exact. Thus APPROX-CB applies to an extended approximate
homomorphism between exact finite-dimensional \(C^*\)-algebras. Since its
target error is zero, `lem_approx_ext` returns an exact unital
\(*\)-homomorphism \(\mu_{11}\), completely \(\kappa e\)-close to \(T\).

Unitality makes \(\mu_{11}\) nonzero; simplicity of \(M_r\) makes its kernel
zero; and \(\dim H_1=r\) makes domain and codomain both \(r^2\)-dimensional.
It is therefore onto and spatially implemented by one unitary
\(U_1:\mathbb C^r\to H_1\). Its amplifications use \(I_m\otimes U_1\).
Neither this argument nor the norm-one diagonal in \(M_r\) introduces an
\(r\)-dependent constant.

### EXTCB-3 — VALID

The conditional inverse triggers occur in the correct order. First,
\(\|T-\mu_{11}\|\le\kappa e<1\) makes \(T\) bijective by Neumann inversion;
bijectivity of \(v\) then makes \(h_{11}\) bijective. Before H5 is invoked,
the proof establishes
\[
 \inf_{Z\ne0}\frac{\|h_{11}(Z)\|}{\|Z\|}
 \ge\frac{1-\kappa e}{1+\delta}>\frac14.
\]
H4 separately gives level-one Neumann bijectivity and the \(1/4\) lower
modulus for the canonical \(h_{12},h_{21},h_{22}\) corners. Only then are H5
and H6 applied, with \(h_{22}\) anchoring \(h_{12}\) and \(h_{11}\)
anchoring \(h_{21}\). No inverse is used before its conditional hypotheses
are met, and \(h_{jk,m}^{-1}=I_m\otimes h_{jk}^{-1}\) is algebraic rather
than a per-level choice.

### EXTCB-4 — VALID

The deliberate proof change works. Defining
\[
 \gamma_{11}=v,\qquad
 \gamma_{jk}=h_{jk}^{-1}\mu_{jk}\quad((j,k)\ne(1,1))
\]
at level one produces one exact transported spatial corner system at every
amplification. Exact H-CB adjointness gives the exact `merging0` relation.
The three transported corners satisfy \(h_{jk,m}\gamma_{jk,m}=\mu_{jk,m}\)
exactly; only the \(11\) corner has error at most \(\kappa e\).

Recomputing the product comparison gives
\[
 4C_He+\kappa e+(2\kappa+\kappa^2e)e
 \le4(C_H+\kappa)e
\]
before applying \(h_{jl,m}^{-1}\), and hence
\[
 \|\gamma_{jl,m}(XY)
   -\gamma_{jk,m}(X)\mathbin{\cdot}\gamma_{kl,m}(Y)\|
 \le5(C_H+\kappa)e\|X\|\|Y\|.
\]
The unit coefficient \(3(C_H+\kappa)\), lower coefficient
\(C_H+\kappa\), and upper coefficient \(2(C_H+\kappa)\) are all dominated
by the same defect \(\rho=5(C_H+\kappa)e\). Thus all four amplified
`merging0`--`merging3` hypotheses hold. The construction keeps
\(\gamma_{11}=v\) exactly and smuggles in no level-dependent object.

### EXTCB-5 — VALID

MERGE-CB applies with the original projection/complementarity defect
\(\delta\le e\) dominated by the common corner defect \(\rho\). It gives the
claimed extended-inclusion estimate for the single sum map \(v_+\).
Bijectivity is exact, not perturbative: the canonical matrix-corner
decomposition, the direct sum of the four bijective \(\gamma_{jk}\), and
the `lem_alpha` recombination are linear bijections. Hence \(v_+\), and
algebraically every \(I_m\otimes v_+\), is bijective.

### Constant ledger — VALID-WITH-CORRECTIONS

The arithmetic is
\[
\begin{aligned}
A_0&=4(C_H+1),\\
\kappa&=4C_{\rm app}(C_H+1),\\
D_0&=5(C_H+\kappa)
    =5C_H+20C_{\rm app}(C_H+1),\\
C_{\rm ext}
 &=C_{\rm merge}(D_0+1)\\
 &=C_{\rm merge}
   [1+5C_H+20C_{\rm app}(C_H+1)].
\end{aligned}
\]
The threshold (1.8) supplies the H-CB, APPROX-CB, and MERGE-CB admissible
ranges, the two Neumann conditions, and the \(1/4\) trigger. Its only
correction is the EXTCB-1 clarification: redefine \(e_{\rm sel}\) to include
the level-one close-idempotent range identifications described above (or add
their universal threshold as one more term in the minimum). Every ledger
entry remains independent of \(r\), \(m\), \(\dim\mathcal A\), and block
data.

### Hypothesis usage — VALID

\(\|P+Q-I\|\le\delta\) is used in the final MERGE-CB recombination;
\(\dim\mathcal S_Q=1\) is used only at level one for the Hilbert/Ha
construction, selection lemmas, \(H_2\), and \(U_2\); and
\(\mathcal S_{P,Q}\ne0\) is used only to exclude the zero branch in the
dimension dichotomy. No amplification treats \(I_m\otimes Q\) as
one-dimensional.

## Overall verdict

**VALID-WITH-CORRECTIONS.** Conditional on the amended H-CB, APPROX-CB, and
MERGE-CB premises, EXT-CB holds with a universal, dimension-free constant,
and the displayed
\[
C_{\rm ext}
=C_{\rm merge}[1+5C_H+20C_{\rm app}(C_H+1)]
\]
is safe. The transported-corner construction is valid and closes the
single-map/amplification issue left open by the printed source. The prover
must make the level-one close-idempotent normalization in EXTCB-1 explicit
and include it in \(e_{\rm sel}\); this is not an \(r\)-dependent gap.
After that correction, no internal EXT-CB estimate remains open. What
remains outside this result is the non-L0 status of the premise chain
(H-CB/EXT-CB are hostile-verified paper proofs, not `af`-validated) and the
separate unconditional end-to-end \(K,\eta_K\) ledger for Route F.

## Contract-impact note

No semantic amendment to the registered `conj-extcb` contract is required.
The corner-transport formula is a proof construction, not an additional
hypothesis, and the existing contract already requires one level-one
unitary and the same four corner maps at every amplification. When this
result is reflected in the registry, `conj-hcb` must be recorded as a proof
dependency; APPROX-CB and MERGE-CB remain the established source-level
premises. The EXTCB-1 normalization belongs in the proof/provenance note,
not in the theorem statement.

## Checks performed that passed

1. Recomputed the primary-source SHA256 exactly.
2. Read the source's level-one Hilbert, Ha, selection, merging, extension,
   amplified approximation, and amplification passages directly.
3. Checked that every use of one-dimensionality is at level one.
4. Checked the binary `lem_add_dim` decomposition and the absence of an
   \(r\)-dependent norm estimate.
5. Checked the close-idempotent range correction needed to identify
   \(\mathcal S_{v(I_r),Q}\) with \(\mathcal S_{P,Q}\).
6. Recomputed the composition multiplicativity and unit defects for
   \(T=h_{11}v\).
7. Checked that the APPROX-CB domain and target are exact
   finite-dimensional \(C^*\)-algebras and that target error zero forces
   exact multiplicativity.
8. Checked injectivity, surjectivity, and spatiality of \(\mu_{11}\).
9. Checked that \(U_1,U_2\) and all spatial corner maps are selected once
   and only algebraically amplified.
10. Verified Neumann bijectivity and the \(1/4\) lower-modulus trigger for
    \(h_{11}\) before H5 is used.
11. Verified the H4 trigger for \(h_{22}\) and the correct anchors for both
    applications of H6.
12. Checked \(h_{jk,m}^{-1}=I_m\otimes h_{jk}^{-1}\).
13. Checked exact adjointness of every transported corner.
14. Recomputed the full product-error expansion, including the possible
    \(11\)-corner errors in the output and both factors.
15. Recomputed the unit and two-sided norm bounds for every corner.
16. Checked all four amplified `merging0`--`merging3` hypotheses with the
    common defect \(D_0e\).
17. Checked exact level-one and amplified bijectivity of the combined map.
18. Recomputed (0.1), every entry of (1.8), and all smallness uses.
19. Traced the uses of complementarity, one-dimensionality, nonzero
    cross-corner, finite dimension, and extendedness.
20. Searched the construction for per-level choices and for dependence on
    \(r\), the amplification level, ambient dimension, or block data; none
    occurs after the stated EXTCB-1 correction.
