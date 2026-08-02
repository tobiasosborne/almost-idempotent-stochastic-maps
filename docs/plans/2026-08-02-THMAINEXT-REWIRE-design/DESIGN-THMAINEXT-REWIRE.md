# DESIGN — `lem-thmainext-conditional` dependency rewire

**Status:** design only; proposed for a fresh hostile audit before verbatim
landing. This document changes no registry row, definition, proof workspace,
or status. In particular, `lem-thmainext-conditional` remains
`proved-mod-audit`, `af: none`, and `op-classical` remains OPEN.

## 1. Final dependency decision

Retain the user-ratified v5 §10 step 15 line **verbatim**:

```yaml
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

No repaired provider dropped an input used by the W74F record. On the
contrary, the repaired M28 contract now exports exactly the stronger final
interface required by the repair hand-off: the isomorphism into the original
ambient algebra, its unit estimate, and finite positive universal witnesses.

The line is sufficient but is deliberately not a transitive reduction of the
current DAG. All six other proposed imports are currently ancestors of M28;
several are also ancestors of one another. They are retained as direct imports
because v5 ratified an explicit seven-input audit/ future-`af` interface, and
because the unchanged target contract itself records the corrected COL-HILB,
H-CB, EXT-CB, and Stage-1 reset inputs rather than merely asserting M28's
conclusion. Removing a direct edge solely because today's M28 implementation
reaches it would silently replace that ratified interface by an
implementation-dependent transitive one.

There is one correction to the **v5 rationale**, but not to its deps line.
V5 said that the reset constant ledger was available transitively through
M19-R. The current M19-R shard instead quantifies over every suitable `W` and
has only `lem-maincb-improvement-iteration` and
`lem-maincb-error-improvement` as deps. The current M28 shard directly imports
`lem-maincb-reset-constant-ledger`; therefore the ledger is available through
M28, not through M19-R.

## 2. Coverage against the current contracts

Every quotation below is from the current `contract:` line of the named shard,
not from a design paraphrase. All seven providers are presently `status:
proved`, `af: validated`, including the two ids whose names retain the
historical `conj-` prefix.

| Analytic input used by the W74F record | Direct provider | Exact clause below |
|---|---|---|
| Corrected squared COL-HILB estimate | `lem-hcb-column-hilbert-squared` | Q1 |
| H-CB at every amplification, including the corrected inverse hypotheses | `conj-hcb` | Q2 |
| EXT-CB with one level-one construction controlling every amplification | `conj-extcb` | Q3 |
| Fixed-map four-corner merge at the total defect scale | `lem-extcb-four-corner-merge` | Q4 |
| Complete error improvement, with bijectivity retained | `lem-maincb-error-improvement` | Q5 |
| Reset after an explicit Stage-1/raw call, including the unit clause and type preservation | `lem-maincb-reset-invariant-preservation` | Q6 |
| Completion of the Stage-1/reset packet inside the full finite assembly | `lem-maincb-structural-assembly` | Q7; its current dependency closure contains the repaired Stage-1 producers, reset rows, and finite recombination rows. |
| Final dimension-free assembly and universal constants | `lem-maincb-structural-assembly` | Q8 |

The exact current-shard quotations referenced by the table are:

**Q1 — `lem-hcb-column-hilbert-squared`:**

```text
every H-CB datum with e <= e_col, every n >= 1, and every X in M_{n,1} tensor S_{P,Q} satisfy abs(<X,X>_n-||X||_{n,1}^2) <= C_col*e*||X||_{n,1}^2.
```

**Q2 — `conj-hcb`:**

```text
the maps 1_{M_n} tensor Ha^Q_{P,R}, under the COL-HILB identification with operators on C^n tensor S_{R,Q} and C^n tensor S_{P,Q}, satisfy for every n the adjoint equality, product defect at most C_H*e*||Z||||W||, and the uniform unit, upper-norm, homomorphism, and canonical-identity closeness estimates required by lem_extension; moreover, if the level-one lower modulus of Ha^Q_{P,P} is at least 1/4, then every amplification has lower modulus at least 1-C_H*e, and if Ha^Q_{P,P} is also bijective at level one then every amplification is bijective with inverse norm at most 1+C_H*e; the analogous off-diagonal inverse bound for Ha^Q_{P,R} is asserted only when Ha^Q_{P,R} is bijective at level one and Ha^Q_{R,R} satisfies that diagonal lower-modulus hypothesis
```

**Q3 — `conj-extcb`:**

```text
there is one map v_+:M_{r+1}->A whose every amplification is a C_ext*e-isomorphism; the same level-one unitary and the same four corner maps carry all amplification levels, with constants independent of r, n, and dim A.
```

**Q4 — `lem-extcb-four-corner-merge`:**

```text
four fixed bijective level-one corner maps satisfying def-four-corner-merging-datum with common defect rho and rho+epsilon <= a_merge combine into one extended C_merge*(rho+epsilon)-isomorphism.
```

**Q5 — `lem-maincb-error-improvement`:**

```text
every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.
```

**Q6 — `lem-maincb-reset-invariant-preservation`:**

```text
every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R satisfying d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, preserving bijectivity when u_R is bijective and leaving the source, target corner, and amplification form unchanged.
```

**Q7 — `lem-maincb-structural-assembly`:**

```text
every finite-dimensional extended epsilon-C*-algebra A with 0 <= epsilon <= W.epsilon_MAIN admits a finite-dimensional C*-algebra B=oplus_C M_{|C|} and an extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A satisfying ||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon
```

**Q8 — `lem-maincb-structural-assembly`:**

```text
hence C_struct=W.c0_cb*W.K_call and e_struct=W.epsilon_MAIN are finite positive universal witnesses.
```

Thus M28 supplies the actual final map consumed by the target. Nothing in the
target requires an intermediate compressed-corner map or a pre-repair
unit-free interface. The additional M28 estimate
`||v(I_B)-I_A|| <= W.c0_cb*W.K_call*epsilon` is compatible with, and makes
explicit, the unit part of the exported extended isomorphism; it is not a new
premise that the target must prove.

## 3. W-ledger coherence and elevation readiness

**Verdict: coherent without changing the target contract.** Fix once the
universal `def-maincb-witness-ledger` datum `W` supplied by
`lem-maincb-reset-constant-ledger`, exactly as M28 requires. For the target's
existential constants choose `C_E := W.c0_cb*W.K_call` and
`epsilon_E := W.epsilon_MAIN`.

M28's current contract states that these are finite positive universal
witnesses and exports, for every eligible `A`, one map with exactly the target
source and codomain. Existentially hiding the already-fixed `W` therefore
produces the target's `C_E, epsilon_E` binders; the target need not expose `W`.

This use obeys both 2026-07-28 typed-witness laws:

1. The final `v:B->A` is M28's very same typed witness, including its source,
   target, bijectivity, amplification, and unit data. No map from M19-R or an
   intermediate corner is identified with it by notation.
2. The proof fixes the provider datum `W` first and only then defines the two
   receiving constants. It does not choose an unbounded receiving coefficient
   and later call it universal. If a future root proof invokes M19-R directly,
   it must instantiate M19-R's universal `W` parameter with this same fixed
   datum rather than select a second ledger witness.

No future contract rewording is mathematically required. One future workspace
construction requirement is flagged: an `af` elevation must explicitly unpack
one ledger witness (or consume M28 as the final typed external) before defining
`C_E` and `epsilon_E`. If the proof language cannot elaborate that
existential-elimination step directly, the remedy is a small typed
witness-instantiation child under the unchanged root contract, not a root
contract amendment and not a reopening of M28.

## 4. DAG and linker check

The current DAG was checked using `argument/INDEX.md` and
`python3 scripts/argument.py --show` for the target and each proposed import.
An in-memory substitution of the proposed line into the parsed registry gave
no parse, import, acyclicity, or status-propagation errors.

The shortest current M28 ancestry paths relevant here are:

```text
M28 -> lem-maincb-one-class-extension -> lem-maincb-stage2-raw-extension -> conj-extcb -> conj-hcb -> lem-hcb-column-hilbert-squared
M28 -> lem-maincb-structural-domain-ledger -> lem-maincb-error-improvement
M28 -> lem-maincb-one-class-extension -> lem-maincb-reset-invariant-preservation
M28 -> lem-maincb-reset-constant-ledger -> lem-maincb-stage3-raw-merge -> lem-extcb-four-corner-merge
```

Consequently, in strict reachability terms M28 makes the other six imports
redundant. Further redundancy exists because `conj-extcb` reaches `conj-hcb`
and `lem-extcb-four-corner-merge`, `conj-hcb` reaches the COL-HILB row, and
M19-R reaches error improvement. This is recorded rather than hidden; §1
explains why the explicit ratified audit interface is retained.

No proposed provider has `lem-thmainext-conditional` in its ancestor closure,
so adding these edges cannot create a cycle. M28 currently has no dependency on
the target. The current target's downstream `lem-routef-k-ledger` edge is also
unaffected.

There is no mixed-rigour problem in the proposed line: all seven current rows
are T0 (`proved`/`validated`). The consumer remains non-rigorous
(`proved-mod-audit`, `af: none`), and the linker permits such a row to import
validated results; importing them does not promote the consumer. The
historical `conj-` prefixes have no status semantics.

## 5. No-T0-invalidation boundary

| Object | Landing disposition | T0 consequence |
|---|---|---|
| `argument/lemmas/lem-thmainext-conditional.md` `deps:` | Replace the current two-id value by the seven-id line in §1. | Consumer stays `proved-mod-audit`; no promotion. |
| Same shard's `provenance:` | Append only the sentence in §6 after the hostile audit exists and approves the design. | Records design/audit authority; no mathematical status change. |
| Same shard's `contract:`, `defs:`, `status:`, `af:`, body | Byte-unchanged. | No contract, definition, or proof claim is disturbed. |
| Seven provider shards and all other registry shards | Untouched. | No T0 contract or dependency closure is invalidated. |
| Locked definitions | Untouched. | No definition ripple. |
| Validated workspaces and exports | Untouched. | No `af` ledger, external, metadata, or export changes. |
| Generated `argument/INDEX.md` and `argument/DAG.md` | Regenerate mechanically after the authoritative shard edit, as required by the repository gates. | Derived views only; then run the linker and full gate. |

`proofs/lem-thmainext-conditional/` exists but is presently empty: it has no
`meta.json`, ledger, externals, export, or seed to preserve. That matches the
shard's `af: none`. The deps-only landing requires no workspace action now;
seeding or importing externals belongs only to a separately authorized future
elevation.

## 6. Exact landing package

After `AUDIT-THMAINEXT-REWIRE.md` exists and approves this design, the only
authoritative registry mutation is the target shard's deps field plus its
provenance note.

Replace the deps field with exactly:

```yaml
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-reset-invariant-preservation; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

Append exactly this sentence to the existing `provenance:` value:

> Dependency-only amendment prescribed by DESIGN-MAIN-STRUCTURE-v5.md sect-10 step 15, re-validated against the repaired current contracts by DESIGN-THMAINEXT-REWIRE.md, and approved by AUDIT-THMAINEXT-REWIRE.md; contract byte-UNCHANGED, status unchanged at proved-mod-audit, and af unchanged at none.

Do not land that sentence before the named hostile audit actually exists and
has the stated verdict. After landing, regenerate the argument index/DAG and
run the repository gates; those mechanical generated-file refreshes do not
broaden the authoritative deps-only amendment.

## 7. Hostile-audit risk register

The auditor should attack these in order:

1. **Witness identity / binder capture.** Check that one supplied `W` is fixed
   before `C_E` and `epsilon_E`, and that the final map is M28's map into the
   original `A`. Reject any proof that identifies it with an M19-R or corner
   map merely by reusing a symbol.
2. **False ledger path.** Reject the old claim that current M19-R imports the
   reset constant ledger. Verify instead that M28 directly imports
   `lem-maincb-reset-constant-ledger` and that no use requires an inaccessible
   second witness.
3. **Direct-edge redundancy disguised as minimality.** Confirm that the seven
   edges are intentionally an audit interface, not a graph-theoretic
   transitive reduction. If repository policy has changed to prohibit
   redundant edges, stop and re-escalate rather than silently deleting ids.
4. **Stage-1 packet coverage.** Recompute M28's closure and ensure it still
   contains the repaired Stage-1 producers, reset invariant, and final finite
   recombination. A future refactor of M28 could invalidate the present
   transitive coverage even while leaving its conclusion unchanged.
5. **Unit/codomain regression.** Inspect M28's current export for the final
   ambient-unit estimate, not merely a local compressed-unit estimate. The
   hand-off forbids reopening the MAIN package or substituting an intermediate
   codomain.
6. **Old analytic clauses.** Check the squared COL-HILB right-hand side, the
   conditional H-CB inverse clauses, and EXT-CB's same-map/all-amplifications
   clause. For four-corner merge, check smallness of `rho+epsilon`, not `rho`
   alone.
7. **Status leakage.** Confirm that a deps edit does not change `status:
   proved-mod-audit`, `af: none`, or imply that the root is T0. T0 providers do
   not automatically validate their consumer, and `op-classical` stays OPEN.
8. **Workspace drift between design and landing.** Recheck that the target
   workspace is still unseeded before landing. If it has acquired a ledger or
   externals, stop and audit preservation requirements rather than applying
   this no-workspace-action disposition mechanically.
9. **Stale explanatory prose in provider shards.** Where body prose and current
   frontmatter/export status disagree, use the current frontmatter plus the
   validated export as the registry authority; do not import an obsolete body
   description as a contract.

Subject to those attacks, the v5 deps line remains the correct deps-only
landing package after the MAINCB repair.
