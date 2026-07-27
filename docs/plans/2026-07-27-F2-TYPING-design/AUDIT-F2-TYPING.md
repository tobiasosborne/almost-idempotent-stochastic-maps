VERDICT: LAND-WITH-CORRECTIONS

# Hostile audit — F2 typing correction and elevation provisioning

The proposed one-line F2 contract may land **verbatim**: its mathematical
changes are exactly the necessary real/complex typing repair, and its real
output still supplies F3 and PRH without loss. The provisioning plan needs the
following exact corrections before re-seeding.

## Required exact corrections

1. Replace the two dependency bullets at
   `DESIGN-F2-TYPING.md:190-194` with this exact text:

   > - Make the \(10K\eta\) commutator node depend explicitly on approximate
   >   invariance and on the typed diagonal-range node. It must not mention
   >   unvalidated siblings.
   > - Make the commutativity-forcing node bind \(K,\eta\) and
   >   \(0\le\eta\le(24K)^{-1}\) in its own statement and rederive
   >   \(10K\eta\le5/12<2\) locally. It must not use an undeclared threshold
   >   sibling.
   > - Make the coordinate-isomorphism node depend explicitly on both the
   >   validated commutativity node and the byte-verbatim projection-basis
   >   external.
   > - Make the \(QA-A\) node depend explicitly on approximate invariance (or
   >   rederive the two-line telescope locally); do not rely on a pending
   >   sibling.

   This closes the two inputs that `ch-3af3f2702d6348b0` says were still
   undeclared: threshold arithmetic from old node 1.1.1 and the commutative
   coordinate theorem
   (`proofs/lem-routef-f2-positive-unital-compression/ledger/000113.json:1`).

2. Replace `DESIGN-F2-TYPING.md:218-221` with this exact text:

   > This is at the requested envelope and below the executable af soft cap
   > `NODE_SOFT_CAP = 26`. The repository's prose still says that \(>12\)
   > nodes is the brittleness threshold, while `scripts/af_constants.py`
   > records that value as historical drift and declares 26 the shared
   > linker/orchestrator source of truth. That process-documentation drift
   > must be reconciled separately. For this design, retain the stricter hard
   > stop at 25 live nodes: first try the byte-matched external plus a
   > carefully dependency-declared re-seed, do not raise the cap, and factor
   > the atomic registry sublemmas below if the projected or live tree exceeds
   > 25.

   The table does sum to 25 and is honest against both the brief and the
   executable cap (`scripts/af_constants.py:1-19`). The contradictory 12-node
   prose is real repository drift (`AGENTS.md:90-91`;
   `argument/README.md:80-81`), but it is not a defect in this task-specific
   25-node budget.

3. Insert after `DESIGN-F2-TYPING.md:132`:

   > **Repository-hygiene guard.** The frontmatter of
   > `def-projection-basis` says `status: locked`, but its body still says
   > “Draft transcription; ratification is required before locking.” Resolve
   > that pre-existing metadata/body drift before provisioning the af
   > external. It does not alter the byte-verbatim source anchor.

   The conflict is literal
   (`definitions/def-projection-basis.md:6,19`). It does not invalidate the
   source bytes, but the design currently calls the shard cleanly “locked”
   without recording the stale body status.

## (a) Contract surgery: PASS

The landed contract quantifies \(K,n,Q,D,J,\Phi,\mathcal B,\Delta,\Upsilon\),
the same threshold, and the same three hypotheses, and concludes
commutativity, \(k\), \(A,M\), and the same three estimates
(`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`). The
candidate preserves all of these literally
(`DESIGN-F2-TYPING.md:39-41`):

- \(K\ge1\), \(n\ge1\), and
  \(0\le\eta\le\min\{(24K)^{-1},1\}\) are unchanged;
- the errors remain \(K\eta,K\eta,K\eta\), and the outputs remain
  \(K\eta,2K\eta,(1-3K\eta)\);
- all \(x,y\in\mathcal B\) and every real
  \(x\in\ell_\infty^k\) retain their quantifiers;
- commutativity remains a conclusion, not a hypothesis.

The only new binders are the uniquely determined complexification \(Q_{\mathbb
C}\) and the corrected complex domains of \(D,J,\iota_{\mathbb C}\). The two
real-preservation clauses are conclusions, not assumptions, and follow from
positivity. Thus there is no silent strengthening or weakening.

The \(\Phi\)-typing matches both T0 seam contracts exactly:
\(D:M_n\to\mathbb C^n\), \(J:\mathbb C^n\to M_n\),
\(Q_{\mathbb C}:\mathbb C^n\to\mathbb C^n\), and
\(\Phi=JQ_{\mathbb C}D\)
(`argument/lemmas/lem-routef-f0-ucp-lift.md:4`;
`argument/lemmas/lem-routef-f0-defect-identity.md:4`).

## (b) Real/complex interface: PASS

The repository fixes \(\ell_\infty^m=\mathbb R^m\)
(`definitions/def-stochastic.md:13-16`), while UCP maps are complex-linear
positive maps of unital \(C^*\)-algebras
(`definitions/def-ucp-map.md:13-20`). The design's interface is well posed:

- a positive complex-linear map takes a self-adjoint \(h=h_+-h_-\) to the
  difference of two positive, hence self-adjoint, elements;
- a unital \(*\)-isomorphism built from a projection basis satisfies
  \(\iota_{\mathbb C}(\mathbb R^k)=\mathcal B_{\rm sa}\): the projections are
  self-adjoint and form a complex vector-space basis
  (`definitions/def-projection-basis.md:13-17`);
- a self-adjoint matrix has real diagonal, so
  \(D\Delta\iota_{\mathbb C}(\mathbb R^k)\subseteq\mathbb R^n\);
- \(J(\mathbb R^n)\) is self-adjoint, so
  \(\iota_{\mathbb C}^{-1}\Upsilon J(\mathbb R^n)\subseteq\mathbb R^k\).

The restricted maps are real positive and unital because the real cones are
the self-adjoint positive cones. For the estimates, the precise comparison is
\[
\|T|_{\mathbb R^a}\|_{\infty\to\infty}
\le \|T\|_{\mathbb C^a\to\mathbb C^b}
\le \|T\|_{\rm cb}.
\]
Corestricting an already real-valued output changes no vector norm. Therefore
the restriction step introduces neither a constant nor a dimension factor.
This justifies, more precisely, the claim at
`DESIGN-F2-TYPING.md:83-90`.

## (c) Factorization identities: PASS

On the complex spaces, \(DJ=I_{\mathbb C^n}\) and
\(D\Phi=Q_{\mathbb C}D\). Hence
\[
A_{\mathbb C}M_{\mathbb C}-Q_{\mathbb C}
   =D(\Delta\Upsilon-\Phi)J,
\qquad
Q_{\mathbb C}A_{\mathbb C}-A_{\mathbb C}
   =D(\Phi\Delta-\Delta)\iota_{\mathbb C}.
\]
Restricting to \(\mathbb R^n\) and \(\mathbb R^k\) gives exactly the two
identities claimed in the design (`DESIGN-F2-TYPING.md:77-89`). These are the
correctly typed versions of the original bridge calculations
(`docs/plans/2026-07-24-fudw-decomposition-artifacts/PROOF-F2F3-BRIDGE.md:122-140`).
The first identity is written as \(AM-Q\)
while the conclusion bounds \(Q-AM\); norm symmetry makes this harmless.

## (d) Commutativity conclusion: PASS

“\(\mathcal B\) is commutative” was already in the landed conclusion
(`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`) and in the
hostile-endorsed exact contract
(`docs/plans/2026-07-24-fudw-decomposition-artifacts/VERDICT-F2F3-BRIDGE.md:212-214`).
F3 and PRH do not consume commutativity; they consume only the resulting real
positive unital \(A,M\) and estimates
(`argument/lemmas/lem-routef-f3-retract-defect.md:4`;
`argument/lemmas/lem-routef-prh-finish.md:4`). Retaining it is neither new nor
consumer-visible strengthening.

## (e) Provisioning: PASS mathematically; CORRECTIONS REQUIRED procedurally

The proposed projection-basis external can be byte-verbatim. The exact local
sentence says that a finite-dimensional commutative \(C^*\)-algebra is
described by a projection basis and prints the adjoint, orthogonality, and
unit-sum relations
(`refs/kitaev-2405.02434/approximate_algebras.tex:1361`). The definition shard
reproduces that sentence verbatim
(`definitions/def-projection-basis.md:13-17`). Defining
\(\iota_{\mathbb C}(\lambda)=\sum_j\lambda_j\Pi_j\) then gives a unital
\(*\)-isomorphism using only those relations and the word “basis”; it does not
upgrade the external to a Wedderburn theorem.

The local source registry contains no operator-algebra classification source
beyond the Kitaev payload (`refs/manifest/SOURCES.md:20-31`), and an exhaustive
text search of the local payloads found no byte-matchable direct-sum-of-matrix
classification theorem. The design is therefore correct to mark that broader
statement **NOT IN LOCAL REFS** and prove the noncommutative norm-\(2\)
commutator witness in-tree (`DESIGN-F2-TYPING.md:150-158`).

The complete-contractivity derivation at
`DESIGN-F2-TYPING.md:160-179` is correct. For every \(r\),
\(T_r=\operatorname{id}_{M_r}\otimes T\) is UCP and hence 2-positive; applying
\(\operatorname{id}_{M_2}\otimes T_r\) to
\(\bigl[\begin{smallmatrix}z^*z&z^*\\z&1\end{smallmatrix}\bigr]\ge0\) yields
\(T_r(z)^*T_r(z)\le T_r(z^*z)\). Positivity and unitality then give
\(\|T_r(z)\|\le\|z\|\); taking \(\sup_r\) gives
\(\|T\|_{\rm cb}\le1\), while the unit gives equality.

The design recognizes all eight raised challenge classes:
typing
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000080.json:1`),
UCP contractivity (`proofs/lem-routef-f2-positive-unital-compression/ledger/000046.json:1`),
noncommutative classification
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000048.json:1`),
commutator dependencies
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000050.json:1`),
\(QA-A\) dependencies
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000091.json:1`),
root/lower-modulus assembly
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000094.json:1`),
commutative coordinates
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000113.json:1`), and
\(\varepsilon\)-scope
(`proofs/lem-routef-f2-positive-unital-compression/ledger/000127.json:1`).
Its only remaining dependency defect is that it does not explicitly close the
threshold and external edges also named in the `000113.json:1` challenge;
correction 1 does so.

The 25-node table at `DESIGN-F2-TYPING.md:204-216` adds correctly and sits one
node below the executable soft cap. Correction 2 records, without hiding, the
separate process-documentation drift between that executable cap and the
older 12-node prose.

## (f) Future strengthened \(k\)-ledger: PASS, subject to its already-required typing correction

The raw future-parent text still writes the old schematic \(\Phi=JQD\)
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:85-97`), so it
is not literally composable as printed. The F0 hostile audit already required
that parent to use \(Q_{\mathbb C}\)
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/AUDIT-F0-ASSEMBLY.md:144-145`), and
the F2 design explicitly carries that correction forward
(`DESIGN-F2-TYPING.md:270-285`). After that already-ratified correction, the
F0 lift, F0 defect identity, strengthened ledger, and corrected F2 contract
all use the same map \(\Phi=JQ_{\mathbb C}D:M_n\to M_n\). No extra conversion
or hypothesis is introduced.

## (g) Definition imports and naked symbols: PASS, with recorded shard drift

Registry imports must name every definition used
(`argument/README.md:9-16,43-46`). The current F2 shard imports only
`def-stochastic` (`argument/lemmas/lem-routef-f2-positive-unital-compression.md:5`),
so adding `def-ucp-map` is required because the contract says “UCP maps.”
Adding `def-projection-basis` is also correct if the proof body/external uses
that project term. The proposed line
`def-stochastic; def-ucp-map; def-projection-basis`
(`DESIGN-F2-TYPING.md:93-103`) is adequate.

\(M_n,\mathbb C^n\), self-adjoint part, complexification, operator norm, and
unital \(*\)-isomorphism are standard finite-dimensional operator-algebra
notation; the contract defines \(\mathbb C^n=\ell_\infty^n(\mathbb C)\) inline
and uses the same \(Q_{\mathbb C}\) vocabulary as the T0 seams. No additional
project-specific definition import is missing. The stale status sentence in
`def-projection-basis` is the separate documentation drift addressed by
correction 3.
