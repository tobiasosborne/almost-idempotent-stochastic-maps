# DESIGN — KITAEV-PAIR af elevation

**Status:** unaudited design only. This file proves nothing, seeds no
workspace, changes no registry row, and promotes no result. Both targets
remain `proved-mod-audit` / `af: none`. A separate fresh hostile audit and
then explicit user ratification are required before any seeding or metadata
change.

## 1. Verdict and order

**Both frozen contracts are dischargeable as written.** The repair has two
logically independent branches: a source-provenance branch followed by an
explicit counterexample, and a constructive branch using finite generalized
Pauli diagonals inside each matrix block followed by independent sign
averaging across blocks. The CP-ization corollary then follows entrywise at
every matrix level from the repaired diagonal's exact centrality.

The order is binding:

1. hostile-audit and user-ratify this package;
2. seed, validate, export, oracle-check, bank, and promote
   `lem-kitaev-diagonal-repair`;
3. only after step 2 is complete, seed
   `cor-kitaev-diagonal-cpization` with the validated workspace import
   `proofs/lem-kitaev-diagonal-repair`;
4. validate and bank the corollary separately.

The corollary has one L2 metadata prerequisite. Its frozen contract uses the
canonical term `UCP`, but its present registry `defs:` line lists only
`def-fd-cstar-diagonal`. The ratified pre-seed landing should add
`def-ucp-map` to that `defs:` line, without changing one byte of the contract.
This design makes no such edit.

The source payload used below is
`refs/kitaev-2405.02434/approximate_algebras.tex`, SHA256
`e7eb512a2ec2438d139c581fe48c017a6ffdc87c37f6fa7492159b757a9a9acb`.
The two externals containing the false printed formula are
**provenance-only**: they establish what text the paper prints, not that the
printed mathematical assertion is true.

## 2. Repair lemma: complete af tree skeleton

Tree shape (12 nodes):

```text
KDR-ROOT
|- KDR-REFUTATION
|  |- KDR-PRINT-LOCUS
|  `- KDR-C2-COUNTEREXAMPLE
`- KDR-CONSTRUCTION
   |- KDR-BLOCK-UNITARIES
   |- KDR-BLOCK-EXPANSION
   |- KDR-BLOCK-DIAGONAL
   |- KDR-PHASE-FAMILY
   |- KDR-PHASE-CANCELLATION
   |- KDR-WHOLE-DIAGONAL
   `- KDR-NORM-AND-UNIVERSALITY
```

### Node `1` — `KDR-ROOT`

Parent: none. Children: `1.1`, `1.2`.

**Exact statement (byte-verbatim frozen contract):**

```text
Kitaev diagonal repair: the direct-sum diagonal formula printed at approximate_algebras.tex:1254 and :2780-2783 is false (already for B=C direct-sum C), but every finite-dimensional C*-algebra B=direct-sum_{r=1}^m M_{d_r} has a finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t with unitary W_t, q_t >= 0, sum_t q_t=1, ZD=DZ for every Z in B, pi(D)=I_B, and projective norm ||D||_pi=sum_t q_t||W_t^dagger||||W_t||=1, independently of block count and block dimensions.
```

Definitions: `def-fd-cstar-diagonal`. Externals: none directly; the two
children establish the two conjuncts.

### Node `1.1` — `KDR-REFUTATION`

Parent: `1`. Children: `1.1.1`, `1.1.2`.

**Exact statement:**

```text
The provenance-only externals GT-kitaev-printed-direct-sum-formula-1254 and GT-kitaev-printed-direct-sum-formula-2780-2783 print the same Cartesian-product/direct-sum prescription. Applied to B=C direct-sum C with the one-point unitary design {1} in each block, that prescription gives D_print=I_B tensor I_B; node 1.1.2 shows that D_print violates the centrality clause of def-fd-cstar-diagonal. Therefore the formula printed at both named loci is false, already for B=C direct-sum C.
```

Definitions: `def-fd-cstar-diagonal`. Externals: the two printed-text GT
entries.

### Node `1.1.1` — `KDR-PRINT-LOCUS`

Parent: `1.1`. Children: none.

**Exact statement:**

```text
GT-kitaev-printed-direct-sum-formula-1254 byte-records the source prescription p_{j_1,...,j_m}=p_{1j_1}...p_{mj_m} and U_{j_1,...,j_m}=U_{1j_1} direct-sum ... direct-sum U_{mj_m}; GT-kitaev-printed-direct-sum-formula-2780-2783 byte-records its repetition with indices s_1,...,s_m. These externals are used only to identify the two printed formulas and make no assertion that either formula is mathematically a diagonal.
```

Definitions: none beyond the parent vocabulary. Externals: both printed-text
GT entries.

### Node `1.1.2` — `KDR-C2-COUNTEREXAMPLE`

Parent: `1.1`. Children: none.

**Exact statement:**

```text
Let B=C direct-sum C with e_1=(1,0), e_2=(0,1), and I_B=e_1+e_2. The one-point design in each block has weight 1 and unitary 1, so either printed prescription has one joint unitary I_B and gives D_print=I_B tensor I_B. Under the bimodule actions in def-fd-cstar-diagonal, e_1 D_print=e_1 tensor I_B=e_1 tensor e_1+e_1 tensor e_2, whereas D_print e_1=I_B tensor e_1=e_1 tensor e_1+e_2 tensor e_1. The four tensors e_r tensor e_s are the coordinate basis of B tensor B, so these two elements are unequal. Thus D_print is not central and is not a diagonal, although pi(D_print)=I_B.
```

Definitions: `def-fd-cstar-diagonal`. Externals: none; this is a direct
finite-dimensional calculation.

### Node `1.2` — `KDR-CONSTRUCTION`

Parent: `1`. Children: `1.2.1` through `1.2.7`.

**Exact statement:**

```text
Fix an arbitrary finite-dimensional C*-algebra B=direct-sum_{r=1}^m M_{d_r}. For each block use nodes 1.2.1-1.2.3 to obtain a finite convex unitary diagonal D_r. Form the independently signed whole-algebra unitaries and weights of node 1.2.4. Nodes 1.2.5-1.2.7 show that their finite sum D is phase-balanced, satisfies ZD=DZ and pi(D)=I_B, has coefficient sum and projective norm exactly 1, and has bounds independent of m and every d_r. This proves the constructive half of KDR-ROOT.
```

Definitions: `def-fd-cstar-diagonal`. Externals: only
`GT-kitaev-projective-tensor-norm` is used downstream for the norm
definition; the block construction itself is proved by finite sums.

### Node `1.2.1` — `KDR-BLOCK-UNITARIES`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
For d>=1 let omega=exp(2*pi*i/d), let (e_a)_{a=0}^{d-1} be the standard basis of C^d, and for 0<=j,k<d define S_{jk} e_a=omega^{ka} e_{a+j mod d}. Each S_{jk} is unitary because it is a diagonal phase followed by a cyclic basis permutation. Therefore D_d:=d^{-2} sum_{j,k=0}^{d-1} S_{jk}^dagger tensor S_{jk} is a finite convex combination of U^dagger tensor U: all coefficients are d^{-2}>=0 and their sum is 1.
```

Definitions: standard matrix-algebra vocabulary. Externals: none. This is
the finite Pauli construction displayed in the source, but its required
properties are checked internally rather than imported.

### Node `1.2.2` — `KDR-BLOCK-EXPANSION`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
Let E_{ab} be the standard matrix units of M_d. Expanding S_{jk}=sum_a omega^{ka} E_{a+j,a} and S_{jk}^dagger=sum_a omega^{-ka} E_{a,a+j}, and using sum_{k=0}^{d-1} omega^{k(b-a)}=d when a=b mod d and 0 otherwise, gives the exact identity D_d=d^{-1} sum_{a,b=0}^{d-1} E_{ab} tensor E_{ba}.
```

Definitions: standard matrix-algebra vocabulary. Externals: none.

### Node `1.2.3` — `KDR-BLOCK-DIAGONAL`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
For D_d=d^{-1} sum_{a,b} E_{ab} tensor E_{ba} and a matrix unit E_{uv}, direct multiplication gives E_{uv}D_d=d^{-1} sum_b E_{ub} tensor E_{bv}=D_d E_{uv}. By linearity, X D_d=D_d X for every X in M_d. Also pi(D_d)=d^{-1} sum_{a,b} E_{ab}E_{ba}=d^{-1} sum_{a,b} E_{aa}=I_d. Hence D_d is a diagonal in the sense of def-fd-cstar-diagonal, with the finite convex unitary representation from node 1.2.1.
```

Definitions: `def-fd-cstar-diagonal`. Externals: none.

### Node `1.2.4` — `KDR-PHASE-FAMILY`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
For each r write the block diagonal from nodes 1.2.1-1.2.3 as D_r=sum_{alpha_r in S_r} p_{r,alpha_r} U_{r,alpha_r}^dagger tensor U_{r,alpha_r}, where S_r is finite, p_{r,alpha_r}>=0, sum_{alpha_r}p_{r,alpha_r}=1, and every U_{r,alpha_r} is unitary. For alpha=(alpha_1,...,alpha_m) and sigma=(sigma_1,...,sigma_m) in {+1,-1}^m define W_{alpha,sigma}:=direct-sum_r sigma_r U_{r,alpha_r} and q_{alpha,sigma}:=2^{-m} product_r p_{r,alpha_r}. The family is finite, every W_{alpha,sigma} is unitary in B, every q_{alpha,sigma}>=0, and sum_{alpha,sigma}q_{alpha,sigma}=2^{-m}2^m product_r sum_{alpha_r}p_{r,alpha_r}=1.
```

Definitions: standard direct-sum C*-algebra vocabulary. Externals: none.

### Node `1.2.5` — `KDR-PHASE-CANCELLATION`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
Let iota_r:M_{d_r}->B be the r-th block inclusion and set D=sum_{alpha,sigma}q_{alpha,sigma} W_{alpha,sigma}^dagger tensor W_{alpha,sigma}. For every r,s, 2^{-m} sum_{sigma in {+1,-1}^m} sigma_r sigma_s equals 1 if r=s and 0 if r!=s. Expanding both direct sums and then using this sign moment gives D=sum_{r,s}(2^{-m}sum_sigma sigma_r sigma_s) sum_alpha(product_l p_{l,alpha_l}) iota_r(U_{r,alpha_r}^dagger) tensor iota_s(U_{s,alpha_s})=sum_r (iota_r tensor iota_r)(D_r). Thus all cross-block tensors vanish exactly for arbitrary m and arbitrary block sizes d_r; this exact sign cancellation is the asserted phase balance.
```

Definitions: standard finite-sum vocabulary. Externals: none.

### Node `1.2.6` — `KDR-WHOLE-DIAGONAL`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
For Z=direct-sum_r Z_r in B and D=sum_r(iota_r tensor iota_r)(D_r), blockwise centrality gives ZD=sum_r(iota_r tensor iota_r)(Z_rD_r)=sum_r(iota_r tensor iota_r)(D_rZ_r)=DZ. Likewise pi(D)=direct-sum_r pi(D_r)=direct-sum_r I_{d_r}=I_B. Therefore D is a diagonal in the sense of def-fd-cstar-diagonal.
```

Definitions: `def-fd-cstar-diagonal`. Externals: none.

### Node `1.2.7` — `KDR-NORM-AND-UNIVERSALITY`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
The representation in node 1.2.5 and unitarity give sum_{alpha,sigma}q_{alpha,sigma}||W_{alpha,sigma}^dagger||||W_{alpha,sigma}||=sum_{alpha,sigma}q_{alpha,sigma}=1. By GT-kitaev-projective-tensor-norm, this representation implies ||D||_pi<=1. For every algebraic representation C=sum_j A_j tensor B_j, ||pi(C)||=||sum_j A_jB_j||<=sum_j||A_j||||B_j||; taking the defining infimum shows ||pi(C)||<=||C||_pi. Applying this to pi(D)=I_B gives 1=||I_B||<=||D||_pi, hence ||D||_pi=1. The numerical bound and coefficient sum are exactly 1 for every m and every d_r; only the finite number of terms may depend on the block data.
```

Definitions: `def-fd-cstar-diagonal`. External:
`GT-kitaev-projective-tensor-norm`.

## 3. Repair lemma: exact seeding package

### Root and definition

Preflight must first show an empty/new workspace and no duplicate definition
name. Seed node 1 with the exact `KDR-ROOT` text above. The sole registry
definition needed is:

```bash
af def-add def-fd-cstar-diagonal --file definitions/def-fd-cstar-diagonal.md -d proofs/lem-kitaev-diagonal-repair
```

No other definition shard is needed. Finite-dimensional C*-algebra, matrix
units, unitaries, finite direct sums, and roots of unity are standard
operator-algebra/linear-algebra vocabulary. The one less-basic item actually
used by the proof, the projective tensor norm, is provisioned byte-verbatim as
the first GT external below. `phase-balanced` is not introduced as a second
definition: it is a descriptive label witnessed by the explicit sign-moment
identity in node `1.2.5`.

### Exact `af add-external` entries

Register each name exactly once. For each entry below, the displayed
`source:` value is the complete string to pass as the single `--source`
argument.

#### `GT-kitaev-projective-tensor-norm`

```text
name: GT-kitaev-projective-tensor-norm
source: refs/kitaev-2405.02434/approximate_algebras.tex:1228-1232 VERBATIM: "The proof involves the concept of a diagonal. Let us give its general definition for completeness, and then specialize to the finite-dimensional case. For arbitrary Banach algebras $\calA$ and $\calB$, the projective tensor product $\calA\hotimes\calB$ is also a Banach algebra. In more detail, $\calA\hotimes\calB$ is the completion of $\calA\otimes\calB$ endowed with the projective tensor norm,
\begin{equation}
\|C\|=\inf\biggl\{\sum_{j}\|A_j\|\ts\|B_j\|:\,
\sum_{j}A_j\otimes B_j=C\biggr\}\qquad (A_j\in\calA,\,\: B_j\in\calB),
\end{equation}"
```

Invocation shape:

```text
af add-external --name "GT-kitaev-projective-tensor-norm" --source <the exact source string above> -d proofs/lem-kitaev-diagonal-repair
```

#### `GT-kitaev-printed-direct-sum-formula-1254`

```text
name: GT-kitaev-printed-direct-sum-formula-1254
source: refs/kitaev-2405.02434/approximate_algebras.tex:1254 VERBATIM: "where $\braket{e_l}{S_{jk}e_m}$ are the matrix elements of $S_{jk}$ in some orthonormal basis $\{e_0,\dots,e_{d-1}\}$. The diagonal of $\bigoplus_{l=1}^{m}\Bo(\CC^{d_l})$ is obtained by combining the component diagonals $D_l=\sum_j p_{lj}\ts U_{lj}^\dag\otimes U_{lj}$ into a sum over $j=(j_1,\dots,j_m)$ with $p_{j_1,\dots,j_m}=p_{1j_1}\cdots p_{mj_m}$ and $U_{j_1,\dots,j_m}=U_{1j_1}\oplus\cdots\oplus U_{mj_m}$." [PROVENANCE-ONLY: records the printed prescription; does not assert that it is a diagonal.]
```

Invocation shape:

```text
af add-external --name "GT-kitaev-printed-direct-sum-formula-1254" --source <the exact source string above> -d proofs/lem-kitaev-diagonal-repair
```

#### `GT-kitaev-printed-direct-sum-formula-2780-2783`

```text
name: GT-kitaev-printed-direct-sum-formula-2780-2783
source: refs/kitaev-2405.02434/approximate_algebras.tex:2780-2783 VERBATIM: "(See \eqref{Pauli_diag} for an explicit example.) The diagonal of the entire algebra $\calB$ is $D=\sum_{s}p_{s}\ts U_{s}^\dag\otimes U_{s}$, where $s=(s_1,\dots,s_m)$,
\begin{equation}
p_{s_1,\dots,s_m}=p_{1s_1}\cdots p_{ms_m},\qquad
U_{s_1,\dots,s_m}=U_{1s_1}\oplus\cdots\oplus U_{ms_m}.
\end{equation}" [PROVENANCE-ONLY: records the printed prescription; does not assert that it is a diagonal.]
```

Invocation shape:

```text
af add-external --name "GT-kitaev-printed-direct-sum-formula-2780-2783" --source <the exact source string above> -d proofs/lem-kitaev-diagonal-repair
```

Do **not** register the existing broad
`GT-kitaev-standard-diagonal` source string from another workspace: that
string extends through line 1254 and therefore bundles the false direct-sum
clause into a mathematical external. The finite Pauli-block proof above makes
that import unnecessary.

## 4. CP-ization corollary: complete af tree skeleton

Tree shape (7 nodes):

```text
KCP-ROOT
|- KCP-LINEARITY
|- KCP-MATRIX-POSITIVITY
|  |- KCP-SQUARE-IDENTITY
|  |  `- KCP-ENTRYWISE-CENTRALITY
|  `- KCP-POSITIVE-SUM
`- KCP-METHOD-SCOPE
```

### Node `1` — `KCP-ROOT`

Parent: none. Children: `1.1`, `1.2`, `1.3`.

**Exact statement (byte-verbatim frozen contract):**

```text
Entrywise CP-ization from the repaired diagonal: for the finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t supplied by lem-kitaev-diagonal-repair, every involution-preserving linear map tilde-Delta:B->B(H) and every UCP map Phi define a completely positive map Delta'(X)=sum_t q_t Phi(tilde-Delta(X W_t^dagger) tilde-Delta(W_t)); complete positivity uses exact centrality of D and does not require exact multiplicativity of tilde-Delta.
```

Definitions: `def-fd-cstar-diagonal`, `def-ucp-map`. External:
`lem-kitaev-diagonal-repair` only.

### Node `1.1` — `KCP-LINEARITY`

Parent: `1`. Children: none.

**Exact statement:**

```text
For fixed t, X maps linearly to X W_t^dagger, then linearly under tilde-Delta, then linearly after right multiplication by the fixed operator tilde-Delta(W_t), and then linearly under Phi. The finite q_t-weighted sum is therefore a linear map Delta':B->B(H).
```

Definitions: standard linear-map vocabulary. Externals: none.

### Node `1.2` — `KCP-MATRIX-POSITIVITY`

Parent: `1`. Children: `1.2.1`, `1.2.2`.

**Exact statement:**

```text
Fix n>=1 and Y in M_n(B), and define Z_t:=tilde-Delta_n((I_n tensor W_t)Y). Node 1.2.1 gives the exact identity Delta'_n(Y^dagger Y)=sum_t q_t Phi_n(Z_t^dagger Z_t), and node 1.2.2 makes its right side positive. Every positive X in the finite-dimensional C*-algebra M_n(B) has X=Y^dagger Y for Y=X^{1/2}; hence Delta'_n is positive for every n. Together with node 1.1, this proves that Delta' is completely positive in the sense recorded by def-ucp-map.
```

Definitions: `def-ucp-map`. External: `lem-kitaev-diagonal-repair` for
the finite family, nonnegative weights, and exact centrality.

### Node `1.2.1` — `KCP-SQUARE-IDENTITY`

Parent: `1.2`. Child: `1.2.1.1`.

**Exact statement:**

```text
For every n>=1 and Y in M_n(B), with Z_t:=tilde-Delta_n((I_n tensor W_t)Y), exact centrality of D and involution preservation of tilde-Delta give the exact matrix identity Delta'_n(Y^dagger Y)=sum_t q_t Phi_n(Z_t^dagger Z_t).
```

Definitions: `def-fd-cstar-diagonal`. External:
`lem-kitaev-diagonal-repair`.

### Node `1.2.1.1` — `KCP-ENTRYWISE-CENTRALITY`

Parent: `1.2.1`. Children: none.

**Exact statement:**

```text
For matrix entries Y_{bc} in B, (Y^dagger Y)_{ac}=sum_b Y_{ba}^dagger Y_{bc}. Exact centrality of D=sum_t q_t W_t^dagger tensor W_t, first with Z=Y_{bc} and then after left multiplication by Y_{ba}^dagger in the first tensor factor, gives sum_t q_t Y_{ba}^dagger Y_{bc}W_t^dagger tensor W_t=sum_t q_t Y_{ba}^dagger W_t^dagger tensor W_tY_{bc}. The map a tensor b maps to Phi(tilde-Delta(a)tilde-Delta(b)) is bilinear because tilde-Delta and Phi are linear. Applying it to this equality and using tilde-Delta(Y_{ba}^dagger W_t^dagger)=tilde-Delta(W_tY_{ba})^dagger gives the (a,c)-entry sum_{b,t}q_t Phi(tilde-Delta(W_tY_{ba})^dagger tilde-Delta(W_tY_{bc})), which is exactly the (a,c)-entry of sum_tq_t Phi_n(Z_t^dagger Z_t). This proves the identity in node 1.2.1 without any multiplicativity identity for tilde-Delta.
```

Definitions: `def-fd-cstar-diagonal`. External:
`lem-kitaev-diagonal-repair`.

### Node `1.2.2` — `KCP-POSITIVE-SUM`

Parent: `1.2`. Children: none.

**Exact statement:**

```text
For every t, Z_t^dagger Z_t is positive in M_n(B(H)). Since Phi is UCP, def-ucp-map gives that Phi_n is positive, so Phi_n(Z_t^dagger Z_t)>=0. The repair external gives q_t>=0 and a finite index set. Therefore sum_t q_t Phi_n(Z_t^dagger Z_t)>=0.
```

Definitions: `def-ucp-map`. External: `lem-kitaev-diagonal-repair` for
the finite nonnegative weights.

### Node `1.3` — `KCP-METHOD-SCOPE`

Parent: `1`. Children: none.

**Exact statement:**

```text
In nodes 1.2-1.2.2 the only diagonal identity used is exact centrality ZD=DZ; neither pi(D)=I_B nor ||D||_pi=1 is invoked. The other explicit inputs are q_t>=0, linearity and involution preservation of tilde-Delta, and complete positivity of Phi. No step replaces tilde-Delta(AB) by tilde-Delta(A)tilde-Delta(B), exactly or approximately. Thus the complete-positivity proof uses exact centrality of D and does not require exact multiplicativity of tilde-Delta.
```

Definitions: `def-fd-cstar-diagonal`, `def-ucp-map`. External:
`lem-kitaev-diagonal-repair` only.

## 5. CP-ization corollary: exact seeding package

### Launch precondition and definitions

Do not create this workspace until `proofs/lem-kitaev-diagonal-repair` has a
clean validated root, has been exported and oracle-checked, and its registry
row has been mechanically banked. Then check definition-name uniqueness and
register exactly:

```bash
af def-add def-fd-cstar-diagonal --file definitions/def-fd-cstar-diagonal.md -d proofs/cor-kitaev-diagonal-cpization
af def-add def-ucp-map --file definitions/def-ucp-map.md -d proofs/cor-kitaev-diagonal-cpization
```

`def-ucp-map` supplies both CP and UCP, including positivity of every matrix
amplification. No operator-space or approximate-algebra definition is used.
The displayed formula type-forces `Phi` to be a UCP map whose domain contains
the operator products in `B(H)` and whose codomain is `B(H)`; in the intended
Route-F use this is `Phi:B(H)->B(H)`. The hostile audit should reject any
attempt to use an untyped `Phi` with an incompatible domain.

### Exact `af add-external` entry

Register exactly one external, with the literal workspace path and the
byte-verbatim repair contract:

```text
name: lem-kitaev-diagonal-repair
source: imports validated registry lemma proofs/lem-kitaev-diagonal-repair — Kitaev diagonal repair: the direct-sum diagonal formula printed at approximate_algebras.tex:1254 and :2780-2783 is false (already for B=C direct-sum C), but every finite-dimensional C*-algebra B=direct-sum_{r=1}^m M_{d_r} has a finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t with unitary W_t, q_t >= 0, sum_t q_t=1, ZD=DZ for every Z in B, pi(D)=I_B, and projective norm ||D||_pi=sum_t q_t||W_t^dagger||||W_t||=1, independently of block count and block dimensions.
```

Invocation shape:

```text
af add-external --name "lem-kitaev-diagonal-repair" --source <the exact source string above> -d proofs/cor-kitaev-diagonal-cpization
```

There are no GT source externals in the corollary workspace. Its only theorem
input is the previously validated repair workspace.

## 6. Projected af budgets

The projections include the observed 1.5x-3x expansion of fresh builds over
clean paper skeletons. A cap hit is a stop-and-classify event, not permission
to raise the cap.

| target | designed nodes | honest live expectation | max rounds | hard node cap | launch tier |
|---|---:|---:|---:|---:|---|
| `lem-kitaev-diagonal-repair` | 12 | 18-25 | 7 | 26 | routine |
| `cor-kitaev-diagonal-cpization` | 7 | 11-18 | 6 | 22 | routine |

For the repair, growth to 26 should be inspected first for duplicated Pauli
calculations, re-proving the projective-norm definition, or attempts to prove
the paper's false prescription rather than refute it. A genuine need beyond
26 means the block-diagonal or projective-norm branch must be factored into a
separate registry lemma and returned for user ratification.

For the corollary, growth beyond 22 almost certainly means the prover has
started importing approximate multiplicativity, norm estimates,
unitalization, Choi-Effros structure, or the downstream closeness argument.
All of those are outside the frozen local contract and must be pruned.

## 7. Ranked hostile-audit risks

1. **Centrality-only CP and factor order.** Recompute the `(a,c)` entry and
   attack every order of `Y_{ba}`, `Y_{bc}`, `W_t`, and `W_t^dagger`. The
   decisive equality must come from applying the bilinear map to
   `Y_{ba}^dagger(ZD=DZ)`; no hidden multiplicativity of `tilde-Delta` may
   enter. Also interpret “only” honestly: centrality is the only *diagonal
   identity* used, while nonnegative weights, star preservation, and CP of
   `Phi` remain explicit hypotheses.

2. **All-level positivity/Choi scope.** Verify linearity of `Delta'`, verify
   the square-root factorization for every positive element of `M_n(B)`, and
   verify that `Phi_n`, not merely `Phi`, is positive. Positivity at `n=1`
   or a Choi-matrix check at one dimension does not prove CP for arbitrary
   finite-dimensional `B` unless the missing equivalence is separately
   supplied. The proposed tree avoids that shortcut and proves every level.

3. **The refutation requires its own counterexample node.** Yes: the
   provenance externals establish only what was printed. They do not prove
   falsity. Node `1.1.2` must independently compute
   `e_1(I_B tensor I_B)` and `(I_B tensor I_B)e_1` in
   `(C direct-sum C) tensor (C direct-sum C)`. Reject a tree that cites the
   paper-proof or hostile verdict as the counterexample.

4. **Phase balance for arbitrary block sizes.** Check the sign moment for
   all `r,s`, including `m=1`, and check that direct-summing
   `sigma_r U_{r,alpha_r}` is unitary without requiring equal `d_r`. The
   cancellation is over block labels, so dimensions never enter it.

5. **L2 and typing closure.** Confirm `def-ucp-map` is registered exactly
   once in the corollary workspace and added to the corollary registry
   `defs:` metadata before seeding, subject to audit and ratification. Confirm
   the displayed expression type-forces an appropriate UCP map `Phi` on the
   ambient operator algebra. A prover may not silently change the frozen root
   to repair typing.

6. **Projective norm equality, not only an upper bound.** The convex unitary
   representation gives `||D||_pi<=1`; it does not by itself give equality.
   The reverse inequality must explicitly use `pi(D)=I_B` and the direct
   proof that multiplication is contractive for the projective norm.

7. **No poisoned GT import.** The broad existing
   `GT-kitaev-standard-diagonal` external includes line 1254 and therefore
   includes the false direct-sum assertion. The repair seed must use only the
   three exact GT entries listed here; the false formulas are
   provenance-only, and the actual block diagonal is established by the
   internal finite Pauli calculation.

8. **Finite and dimension-free mean different things.** The family has
   finitely many terms, but its cardinality grows with `m` and the `d_r`.
   What is independent of the block data is the coefficient sum and
   projective norm, both exactly 1. Reject any node claiming a uniform bound
   on the number of terms.

9. **No downstream overreach.** The corollary proves CP only. It does not
   prove closeness to `tilde-Delta`, invertibility of `Delta'(I)`, UCP
   unitalization, or the Route-F factorization. Those belong to later ledger
   rows and must not be added to this tree.

10. **Root and order drift.** Compare each node `1` byte-for-byte with its
    current shard and with this design. The corollary must not launch against
    a merely seeded or unbanked repair workspace, and neither status may move
    before separate fresh verification, export/oracle checks, gates, and user
    ratification of the audited package.
