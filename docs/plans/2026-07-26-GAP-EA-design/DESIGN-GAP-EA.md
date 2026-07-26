# DESIGN-GAP-EA — exact-target correction factoring

**Date:** 2026-07-26  
**Bead:** `aism-fbh8`  
**Disposition:** design decision only; no proof, registry mutation, status
promotion, or workspace authorization is made here.

## 1. Recommendation

Choose **(a)**.

Bank the general defect-hypothesis theorem from validated `conj-extcb` node
`1.2` as its own result, and retain
`lem-extcb-exact-target-approximation` as a separate interface lemma for the
extended-\(\alpha\)-homomorphism vocabulary. This preserves the strongest
validated theorem, keeps the design-facing interface stable, and prevents
each consumer from hiding the conversion between “extended
\(\alpha\)-homomorphism” and the two explicit amplified defect inequalities.

The consumer split matters:

```text
lem-extcb-exact-target-correction
├── lem-extcb-exact-target-approximation
│   └── lem-extcb2-exact-representation
└── lem-maincb-error-improvement
    └── the MAIN-CB/reset rows and lem-thmainext-conditional
```

The first consumer has domain \(M_r\), so the design-facing bridge is its
right interface. IMPROVE-CB ranges over an arbitrary finite-dimensional
\(C^*\)-algebra, so it needs the more general \(B\)-form directly; the
\(M_r\)-only bridge is too narrow.

Option (b) would force both consumers to unpack the explicit defect
hypotheses internally. In particular, it would either hide the conversion in
`lem-extcb2-exact-representation` or make IMPROVE-CB appear to depend on an
\(M_r\)-only result that does not cover its source algebra.

### Ledger basis

The decision uses the following validated, taint-clean facts.

- Node `1.2` gives a single level-one \(\mu:B\to B(H)\) whose fixed
  amplifications are uniformly close to \(T_n\), for arbitrary
  finite-dimensional \(B\), not just \(M_r\).
- Nodes `1.2.1`--`1.2.3` contain the norm-one diagonal, exact
  unitalization, normalized Newton step, and convergence argument.
- The actually load-bearing endpoint/dependency repair continues below the
  advertised three children through `1.2.3.1` and `1.2.3.1.1`. Omitting
  those nodes would reintroduce the \(a=0\) and recursive-dependency gaps.
- Node `1.3.1` derives the amplified defects of the particular map
  \(T=h_{11}v\) from `def-extended-delta-inclusion` and `conj-hcb`.
  Therefore it demonstrates that the EXT-CB consumer can enter node `1.2`;
  it is not itself a standalone generic bridge.
- The challenge below `1.3.1` required a separate \(e=0\) branch. The
  proposed generic bridge does not inherit that problem because node `1.2`
  already has the non-strict range \(0\le a\le a_{\rm corr}\).

## 2. Exact registry proposals

Every displayed `contract:` value below is one mathematical statement. No
proof provenance, “hence” clause, or corollary gloss belongs in the
frontmatter.

### 2.1 New factored row: `lem-extcb-exact-target-correction`

```yaml
id: lem-extcb-exact-target-correction
kind: lemma
contract: There are universal a_corr>0 and C_corr<infinity with the following property: if B is a finite-dimensional C*-algebra, H a finite-dimensional Hilbert space, and T:B->B(H) is linear, dagger-preserving, has ||T_n(XY)-T_n(X)T_n(Y)||<=a||X||||Y|| and ||T_n(I)-I||<=a at every n, where 0<=a<=a_corr, then one unital dagger-homomorphism mu:B->B(H) satisfies ||mu_n-T_n||<=C_corr*a at every n.
defs: def-fd-cstar-diagonal; def-extended-epsilon-cstar-algebra
deps:
status: proved
af: none
```

The contract is the central theorem sentence of validated node `1.2`
verbatim. The node's heading is not part of the theorem, and its final
sentence describing which children prove it is forbidden registry
meta-commentary. The separate sentence “The same level-one mu is used at
every amplification” is not repeated: the displayed conclusion already
uses the amplifications \(\mu_n\) of the single quantified map \(\mu\).

`C_corr=57` belongs in the proof body/export, because it is established in
validated node `1.2.3`; the validated root contract quantifies `C_corr` and
does not state the numerical value. Adding `57` to the registry contract
before a standalone root validates that stronger wording would violate the
verbatim-banking precedent.

The proposed pre-elevation state `proved; af: none` records that the exact
mathematical assertion is already validated inside `proofs/conj-extcb`, but
does not pretend that a standalone workspace exists. Only the standalone
workspace may move this row to `af: validated`.

### 2.2 Existing row becomes the bridge:
`lem-extcb-exact-target-approximation`

The v4.1 mathematical contract remains unchanged.

```yaml
id: lem-extcb-exact-target-approximation
kind: lemma
contract: Exact-target complete approximation: there are universal C_app<infinity and a_app>0 such that every extended alpha-homomorphism T:M_r->B(H) with alpha<=a_app is completely C_app*alpha-close to one exact unital *-homomorphism mu:M_r->B(H).
defs: def-extended-epsilon-cstar-algebra
deps: lem-extcb-exact-target-correction
status: stated
af: none
```

This row does not need `def-extended-delta-inclusion`: its hypothesis is an
extended homomorphism, not an inclusion or a two-sided norm bound.
`def-extended-epsilon-cstar-algebra` already contains the cited definition
of an extended \(\delta\)-homomorphism and its amplifications. The proposed
but currently absent `def-operator-space` must not be left as a dangling
frontmatter id.

The bridge proof should only unpack the extended-homomorphism definition,
specialize \(B=M_r\), and identify a unital dagger-homomorphism with a
unital \(*\)-homomorphism. It must not import `conj-hcb`,
`def-extcb-datum`, or the \(h_{11}v\) notation from node `1.3.1`.

### 2.3 Repair `lem-maincb-error-improvement`

The v4.1 dependency

```yaml
deps: lem-extcb-exact-target-approximation
```

should be replaced by

```yaml
deps: lem-extcb-exact-target-correction
```

because IMPROVE-CB consumes an arbitrary finite-dimensional source algebra,
whereas the bridge is deliberately \(M_r\)-specific.

The contract also needs a design-review narrowing before seeding. The
current v4.1 text suppresses two literal hypotheses of
`approximate_algebras.tex:1317-1319`: the source algebra is
finite-dimensional and the ambient defect is below a universal
\(\varepsilon_{\max}\). The consumers need only that narrower form.

```yaml
id: lem-maincb-error-improvement
kind: lemma
contract: Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.
defs: def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-extcb-exact-target-correction
status: stated
af: none
```

This narrowing is not a proof change or a promotion. It prevents the future
workspace from being seeded with a statement stronger than both the pinned
source and the MAIN consumers require.

### 2.4 Downstream wiring

- `lem-extcb2-exact-representation` keeps
  `deps: conj-hcb; lem-extcb-exact-target-approximation`.
- The MAIN-CB/reset rows keep depending on
  `lem-maincb-error-improvement`; none should import either exact-target row
  directly.
- The §3.3 direct dependency list of `lem-thmainext-conditional` is
  unchanged.

Thus closing the two GAP-EA rows removes the exact-target blocker, but it
does not promote or automatically prove IMPROVE-CB or any MAIN row.

## 3. Seeding plan

No node cap increase is justified.

### 3.1 General correction workspace

Seed `proofs/lem-extcb-exact-target-correction` with the contract in §2.1
exactly. The expected tree is **6 live nodes with at most 3 descendant
edges**:

| standalone node | transcribe from `proofs/conj-extcb` |
|---|---|
| `1` | mathematical assertion of `1.2` |
| `1.1` | `1.2.1` — cb control, exact unitalization, norm-one diagonal |
| `1.2` | `1.2.2` — normalized Newton correction |
| `1.3` | `1.2.3` — convergence and \(C_{\rm corr}=57\) |
| `1.3.1` | `1.2.3.1` — validated dependency and induction bridge |
| `1.3.1.1` | `1.2.3.1.1` — degenerate-safe geometric estimate |

The prover should transcribe the final statements and arguments, not the
historical superseded amendments. It must recreate explicit dependency
edges in the new ledger rather than relying on the old nodes' ambient
placement.

Expected budget is 6; a hostile repair may bring it to 8. If the live tree
approaches 12 nodes or exceeds depth 3 relative to the root, stop and
factor the diagonal or normalized-Newton step. R12 applies literally:
ballooning is a factoring signal, never permission to raise the cap.

Workspace provisioning:

- `af def-add`: full local text of `def-fd-cstar-diagonal`,
  `def-epsilon-cstar-algebra`, and
  `def-extended-epsilon-cstar-algebra`;
- `af def-add`: the same byte-matched operator-space matrix-norm axioms
  from `approximate_algebras.tex:1454-1463` used in `conj-extcb`;
- `af add-external`: **none**. The parent subtree claimed no external
  theorem, and the standalone proof should establish the diagonal/Newton
  chain internally.

### 3.2 Bridge workspace

After the general correction row validates and is banked, seed
`proofs/lem-extcb-exact-target-approximation`.

- Expected budget: **2 nodes** (root plus one definition-unpacking
  application); 3 only if the verifier requests a separate terminology
  bridge for dagger-homomorphism versus \(*\)-homomorphism.
- `af def-add`: `def-extended-epsilon-cstar-algebra`.
- `af add-external`: the full validated contract from
  `proofs/lem-extcb-exact-target-correction`.
- Do not transcribe node `1.3.1`; its `conj-hcb`, \(h_{11}\), \(v\), and
  \(A_0e\) calculation belong to `lem-extcb2-exact-representation`.

At banking, the registry contract must equal the newly validated standalone
root verbatim. If a prover or verifier materially expands either root,
reconcile this design and the consumer contracts before banking; do not
silently paraphrase the validated statement.

### 3.3 IMPROVE-CB comes afterward

Only after §3.1 validates may `lem-maincb-error-improvement` seed with the
repaired contract in §2.3. Its proof must treat an approximate target and
stop Newton iteration at an \(O(\varepsilon)\) floor, following
`approximate_algebras.tex:1256-1319`. The exact-target subtree alone does
not prove that statement. Remeasure its plan independently; this note does
not authorize absorbing a second Newton chain by raising the node cap.

## 4. Hostile transfer audit

1. **The advertised three-child subtree is not the complete active proof.**
   The endpoint and recursive-use repairs at `1.2.3.1` and `1.2.3.1.1`
   are essential. A four-node transcription of only `1.2`--`1.2.3` is not
   faithful to the validated ledger.

2. **Node `1.3.1` is ambient.** It refers to `conj-hcb`,
   `def-extended-delta-inclusion`, \(h_{11}\), \(v\), \(C_H\), and
   \(e=\delta+\varepsilon\). None of those belongs in the generic bridge.
   Its transferable content is the consumer pattern “derive explicit
   amplified defects, then apply the correction lemma.”

3. **The \(e=0\) challenge is real.** The original positive-parameter
   application below `1.3.1` failed at \(e=0\) and required
   `1.3.1.1` plus dependency-gated descendants. A later
   `lem-extcb2-exact-representation` transcription must include that
   endpoint logic or use the non-strict generic bridge directly.

4. **The diagonal definition is not an existence theorem.**
   `def-fd-cstar-diagonal` defines a diagonal but does not by itself prove
   the norm-one Haar diagonal exists. Node `1.2.1` invokes normalized Haar
   measure, compactness, and a finite convex representation. A fresh
   verifier may demand those standard facts be expanded or separately
   sourced; that is a legitimate factoring trigger.

5. **State cb-norm is implicit.** Exact unitalization chooses a state
   \(\phi\) on \(B\) and uses that states have cb norm one and respect the
   involution. This was accepted in the parent tree but is not supplied by
   a named external or registry definition. The standalone prover must say
   enough for a hostile verifier to check it.

6. **Do not over-bank the constant.** The subtree proves the usable
   numerical value \(C_{\rm corr}=57\), but the validated node-`1.2` root
   only asserts existence of a universal \(C_{\rm corr}\). The registry
   contract must retain that scope unless the standalone root itself is
   validated with `57`.

7. **Exact correction does not imply IMPROVE-CB.** The former has exact
   target \(B(H)\); the latter has an extended
   \(\varepsilon\)-\(C^*\)-algebra target and needs the
   \(O(\varepsilon)\)-floor Newton argument plus lower-norm/bijectivity
   control. GAP-EA closure is a prerequisite, not an IMPROVE-CB proof.

8. **The old IMPROVE-CB contract was overbroad.** Without
   finite-dimensional \(B\) and \(\varepsilon\le\varepsilon_{\max}^{\rm
   cb}\), it exceeds the pinned source. Seeding it unchanged would repeat
   the local-domain failure pattern that v4.1 quarantines elsewhere.

9. **Faithfulness versus injectivity is consumer-owned.** Node `1.2`
   produces a unital homomorphism, not an injective one. The EXT-CB
   consumer obtains injectivity from simplicity of \(M_r\), and
   IMPROVE-CB must obtain its two-sided norm and bijectivity conclusions
   separately. Neither conclusion may be appended to the correction
   contract as a gloss.

10. **Finite-dimensional \(H\) must be checked at use sites.** In the
    EXT-CB consumer, \(H=S_{P,Q}\) becomes \(r\)-dimensional through the
    validated dimension nodes before correction is applied. A future
    consumer cannot invoke the factored lemma on an arbitrary
    infinite-dimensional Hilbert space.

## 5. Decision summary

Adopt (a) with two rows: the general defect-form correction and the
design-facing \(M_r\) bridge. Wire EXT-CB through the bridge and IMPROVE-CB
through the general result. Before IMPROVE-CB seeds, narrow its contract to
the finite-dimensional, small-\(\varepsilon\) source statement. Transcribe
all six active nodes of the correction subtree, keep the bridge tiny, and
trip R12 instead of increasing the node cap.
