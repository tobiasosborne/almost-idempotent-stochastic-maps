# AUDIT — hostile audit of Route-F F0/root assembly

Date: 2026-07-27

Role: fresh independent hostile auditor

Status: **NON-RIGOROUS AUDIT / DESIGN ONLY / DO NOT SHARD, SEED, REWIRE,
PROMOTE, OR TREAT AS LOCAL-REF GROUND TRUTH**

## 0. Final disposition

**LAND (WITH CORRECTIONS).**

The numerical Route-F seam is sound: one input defect \(\eta\), one universal
\(K\), and one terminal threshold \(\eta_K\) pass through F2, F3, and PRH with
the advertised constant \(K+4\sqrt{2K}\). No dimension-dependent coefficient
or hidden \(\eta\mapsto\varepsilon_{\rm AI}\) substitution occurs at F0.

Four defects prevent the design from landing verbatim:

1. The proposed `lem-routef-k-ledger` text is **not merely a binder/closure
   correction**. It strengthens the exact hostile-endorsed contract by adding
   a universal \(Q\)-quantifier, the stochastic defect antecedent, a fixed
   \(\Phi=JQD\), a finite-dimensional algebra, three literal estimates (one at
   every amplification), and a same-\(Q\) conclusion. Compare the endorsed
   text at
   `docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-H-STAGE1.md:292-307`
   with the replacement at
   `docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:79-107`.
   The strengthened statement is supported by the proposed new imports and the
   audited component rows, but it is a **new parent proof obligation** and must
   be reviewed/elevated as such.
2. The exact root wiring in §3 is false if the literal compound
   `op-classical` contract is retained. Its empty unconditional `deps:` leaves
   the legacy route without `ex-hume`; §4 repairs only the Route-F branch.
   Sharpness must either leave the root contract, or `ex-hume` must be an
   unconditional dependency shared by both routes
   (`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:188-206,219-223`;
   `argument/lemmas/op-classical.md:4-6`;
   `argument/lemmas/ex-hume.md:4-8`).
3. The lift contracts mix the real stochastic convention
   \(\ell^\infty_n=\mathbb R^n\) with complex \(M_n\) without binding the
   canonical complex-linear extension of \(Q\), and they use the acronym UCP
   without a canonical definition/import. The exhaustive definition index has
   no UCP entry (`definitions/INDEX.md:2-42`), while the stochastic shard is
   explicitly real (`definitions/def-stochastic.md:13-16`).
4. The prose landing order does not explicitly place elevation of
   `lem-thmainext-conditional` and the other non-T0 transitive ledger inputs
   before their consumers; if sharpness remains in the root, it also omits
   elevation of seeded `ex-hume`
   (`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:237-260`;
   `argument/lemmas/lem-thmainext-conditional.md:4-9`;
   `argument/lemmas/cor-kitaev-diagonal-cpization.md:4-9`;
   `argument/lemmas/ex-hume.md:4-8`).

These are contract/factoring/wiring corrections, not a mathematical
Route-F alarm.

## 1. Verdict per proposed row

### 1.1 `lem-routef-f0-ucp-lift` — VALID-WITH-CORRECTIONS

The mathematics is valid. A row-stochastic map is positive and unital; a
positive map out of a commutative complex \(C^*\)-algebra is completely
positive; and \(D,J\) are UCP, so their composition is UCP
(`docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md:434-444`).
Empty mathematical deps and the proposed 3-node/depth-2 budget are honest.
The local paper proof supports only `proved-mod-audit`, exactly as the design
says
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:46-55`).

Exact corrections before landing:

- replace \(Q\) in the operator-algebraic composition by its canonical
  complex-linear extension \(Q_{\mathbb C}:\mathbb C^n\to\mathbb C^n\), and
  write \(\Phi=JQ_{\mathbb C}D\);
- expand and canonically provision/import “unital completely positive map”
  (or obtain an explicit user-ratified L2 textbook exemption). The present
  `defs: def-stochastic` does not define UCP
  (`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:40-49`;
  `definitions/def-stochastic.md:13-16`;
  `definitions/INDEX.md:2-42`).

### 1.2 `lem-routef-f0-defect-identity` — VALID-WITH-CORRECTIONS

The equality, including the lower bound, is correct. Put
\(L=Q_{\mathbb C}^2-Q_{\mathbb C}\). Since \(DJ=I\),
\[
\Phi^2-\Phi=JLD.
\]
At every matrix level, contractivity of \(D_r\) and isometry of \(J_r\) give
\(\|(JLD)_r\|\le\|L_r\|\). Conversely, on a norm-attaining diagonal input
\(J_rX\),
\[
\|(JLD)_rJ_rX\|=\|J_rL_rX\|=\|L_rX\|,
\]
because \(D_rJ_r=I\). Also
\(\|L_r\|=\max_i\sum_j|l_{ij}|=\|L\|_{\infty\to\infty}\), by the explicit
sign/phase test. This is the missing reverse direction, and it is present in
the cited audit
(`docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md:446-496`).

Apply the same \(Q_{\mathbb C}\) correction as in §1.1. Subject to that
typing correction, empty deps and the 5-node/depth-3 budget are honest
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:57-75`).

### 1.3 corrected `lem-routef-k-ledger` — VALID-WITH-CORRECTIONS

The proposed explicit packet is mathematically supported:

- the audited design produces UCP \(\Delta,\Upsilon\) in its normalization
  rows
  (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:186-192`);
- its three telescope contracts give exactly
  \(\Delta\Upsilon-\Phi\), amplified
  \(\Upsilon_r(\Delta_rX\Delta_rY)-XY\), and
  \(\Upsilon\Delta-I_{\mathcal B}\), in the required orientation and
  normalization
  (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:193-196`);
- the original ledger displays the same all-level middle estimate and the
  two cb estimates
  (`docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md:345-383`);
- F2/F3/PRH then produce an \(E\) for the same input \(Q\)
  (`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4-9`;
  `argument/lemmas/lem-routef-f3-retract-defect.md:4-9`;
  `argument/lemmas/lem-routef-prh-finish.md:4-9`).

But the design must replace “correction only supplies missing binders” by:

> **This is a strengthened replacement contract and a new parent proof
> obligation.** Its new F0 imports specialize the hostile-verified generic
> factorization packet to every row-stochastic \(Q\), and F2/F3/PRH prove the
> same-\(Q\) conclusion. It must receive a fresh proof/review; it is not
> inherited verbatim from the W74F-H verdict.

That correction is forced because the W74F-H verifier endorsed only “for every
\(\eta\)” and “the associated stochastic map,” not the new closed
\(\forall n\,\forall Q\,\forall\eta\) interface
(`docs/plans/2026-07-24-W74F-wave2-artifacts/VERDICT-W74F-H-STAGE1.md:299-307`).
The old proof's finish starts only with
“for \(\eta\le\eta_K\)” and never binds the original \(Q\)
(`docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md:457-477`).

Also use \(Q_{\mathbb C}\) in \(\Phi\), add `def-almost-idempotent` to the
corrected ledger's `defs`, and resolve the UCP definition/import. The audited
\(\rho_{\rm id}^{\rm corr}\) correction must be incorporated in the landed
local row. Its claimed non-effect on the terminal minimum is correct because
\(\rho_T\le\rho_{\rm id}^{\rm corr}\) and the added
\(\rho_\theta\) was already primitive
(`docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS-v2.md:26-44,236-252,303-320`).

The ten direct imports are acyclic in the proposed order and the projected
parent remains within the stated envelope, but its node budget must be
remeasured against the strengthened contract rather than described as a
mechanical binder edit
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:109-133`).

### 1.4 `lem-routef-f0-assembly` — VALID

Once the strengthened K-ledger contract has actually been proved, this row is
pure specialization: take
\[
\eta_0=\eta_K,\qquad C=K+4\sqrt{2K}.
\]
Both are positive and universal by the parent. Therefore the sole direct dep
`lem-routef-k-ledger` is sufficient; the two lift rows and F2/F3/PRH must not
be duplicated here. The 2-node/depth-2 estimate is honest
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:135-158`).

## 2. Recomputed seam table

| seam | verdict | hostile recomputation |
|---|---|---|
| Stochastic defect \(\to\) UCP input | **VALID-WITH-CORRECTIONS** | UCP and the constant-1 defect equality are valid, but use \(Q_{\mathbb C}\) and close the UCP vocabulary (§§1.1-1.2; `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md:434-496`). |
| Ledger algebra/UCP data \(\to\) F2 | **VALID-WITH-CORRECTIONS** | Rows 6 and 9 produce UCP maps and the MAIN black box produces finite-dimensional \(\mathcal B\); the strengthened parent must bind them literally (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:66-86,186-192`; `argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`). |
| Ledger first estimate \(\to\) F2 | **VALID** | Both are \(\|\Delta\Upsilon-\Phi\|_{\rm cb}\le K\eta\), for the same bound \(\Phi\) (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:193`; `argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`). |
| Ledger second estimate \(\to\) F2 | **VALID** | Both are \(\|\Upsilon\Delta-I_{\mathcal B}\|_{\rm cb}\le K\eta\) (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:195`; `argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`). |
| Ledger multiplicativity \(\to\) F2 | **VALID** | The ledger has \(\|\Upsilon_r(\Delta_rX\,\Delta_rY)-XY\|\le K\eta\|X\|\|Y\|\) for every amplification; \(r=1\) is exactly F2's all-\(x,y\in\mathcal B\) hypothesis, with identical orientation and no norm conversion (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:194`; `argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`). |
| One coefficient \(K\) | **VALID** | Row 13 takes the maximum of \(1\) and the three telescope coefficients (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:149-164,383-403`). |
| One domain \(\eta_K\) | **VALID-WITH-CORRECTIONS** | Use the audited \(\rho_{\rm id}^{\rm corr}\); it does not alter the effective terminal minimum. Then \(\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}>0\) (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS-v2.md:38-44,238-262`; `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:405-423`). |
| Location of \(\eta\mapsto\varepsilon_{\rm AI}(\eta)\) | **VALID** | No conversion occurs at F0: equality transfers the same stochastic \(\eta\) to \(\Phi\). Inside the ledger, AI gives \(\varepsilon_{\rm AI}(\eta)\le C_A\eta\), MAIN consumes that defect, and all later coefficients remain multiples of the original \(\eta\) (`argument/lemmas/lem-routef-ai-defect-linearization.md:4-9`; `docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:58-86`). |
| F2 threshold | **VALID** | \(\eta\le\eta_K\le(24K)^{-1}\) and \(\eta_K\le1\) are exactly F2's guards (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:168-170,405-419`; `argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`). |
| F2 \(\to\) F3 | **VALID** | Positive unital \(A,M\), the \(K\eta\) and \(2K\eta\) estimates, and the lower bound for **every** \(x\) match literally (`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`; `argument/lemmas/lem-routef-f3-retract-defect.md:4`). |
| F3 strict guard | **VALID** | \(3K\eta\le1/8<1\), so the denominator is strictly positive (`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:405-417`). |
| F2+F3 \(\to\) PRH finish | **VALID** | F2 supplies positive unital \(A,M\) and \(\|Q-AM\|\le K\eta\); F3 supplies the exact retract defect; these are PRH finish's complete hypotheses (`argument/lemmas/lem-routef-prh-finish.md:4-6`). |
| Norm discipline | **VALID** | The three upstream estimates are cb/all-level where required; after F2 all displayed map norms are the \(\ell_\infty\to\ell_\infty\) norm. The spelling `inf`/`infinity` is cosmetic (`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`; `argument/lemmas/lem-routef-f3-retract-defect.md:4`; `argument/lemmas/lem-routef-prh-finish.md:4`). |
| PRH \(\to\) root upper bound | **VALID** | PRH returns a same-\(Q\) stochastic idempotent with \((K+4\sqrt{2K})\sqrt\eta\), exactly the upper-bound part of the root (`argument/lemmas/lem-routef-prh-finish.md:4`; `argument/lemmas/op-classical.md:4`). |

## 3. Wiring and double-counting — VALID-WITH-CORRECTIONS

The OR-route mechanism exists and has exactly the proposed conjunctive-group /
disjunctive-group semantics (`argument/README.md:29,45-61,71-79`), so using
`routes:` is valid. The current legacy route really is the conjunction
`thm-classical-factorization; prop-approx-simplex`
(`argument/lemmas/op-classical.md:6,14-20`).

For an **upper-bound-only** corrected root contract, the design's block is
valid:

```yaml
deps:
routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]
```

For the **literal current compound contract**, the exact valid block is instead:

```yaml
deps: ex-hume
routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]
```

Making `ex-hume` unconditional is the clean encoding because sharpness is
common to both upper-bound routes. The design's §3 block is therefore
**REFUTED as written under the retain-sharpness option**. Its §4 alternative
`[lem-routef-f0-assembly; ex-hume]` repairs only one branch
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:191-206,219-223`).

There is no F2/F3/PRH double counting: each is a direct dependency only of the
strengthened K-ledger; assembly depends only on that ledger, and the root
depends only on assembly on its Route-F branch
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:109-123,151-152,182-203`).
Both DO-NOT-REWIRE guards remain explicit
(`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:5-6,125-127,262-263`).

## 4. Sharpness and equivalence — VALID-WITH-CORRECTIONS

Changing `op-classical` is a result-contract change, not a definition-shard
change, but it is still contract drift and therefore requires the user
ratification already demanded by the design. Moving sharpness out produces the
cleanest atomic upper-bound contract.

If the compound contract is retained, `[lem-routef-f0-assembly; ex-hume]` is
sufficient at the literal contract level because `ex-hume` itself concludes
that no exponent \(\beta>1/2\) can hold for `op-classical`
(`argument/lemmas/ex-hume.md:4`). It is not yet an available rigorous import:
it is `proved-mod-audit`, `af: seeded`
(`argument/lemmas/ex-hume.md:7-8`). That elevation must
precede root discharge. `lem-classical-equiv` is not a construction dependency
of F0; if it is needed to prove the signed-family-to-stochastic sharpness
sentence during `ex-hume` elevation, it belongs on `ex-hume`, not on
`lem-routef-f0-assembly` (`argument/lemmas/lem-classical-equiv.md:4-9`).

## 5. Dimension-freeness — VALID

The corrected ledger exports universal \(K,\eta_K\), independent of dimension,
amplification, and block data
(`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:45-48,149-170`;
`docs/plans/2026-07-26-LEDGER-DOMAINS-design/AUDIT-LEDGER-DOMAINS-v2.md:254-262,285-299`).
F0 contributes an exact
constant-1 lift. F2's contract contributes only \(2,3,24\), F3 only the fixed
rational denominator, and PRH finish only \(4\sqrt2\)
(`argument/lemmas/lem-routef-f2-positive-unital-compression.md:4`;
`argument/lemmas/lem-routef-f3-retract-defect.md:4`;
`argument/lemmas/lem-routef-prh-finish.md:4`). Thus
\[
\eta_0=\eta_K,\qquad C=K+4\sqrt{2K}
\]
are \(n\)-free. No Route-F alarm is present.

## 6. Landing order — VALID-WITH-CORRECTIONS

F2 and F3 are correctly reclassified as non-T0:
`status: proved-mod-audit`, `af: none`
(`argument/lemmas/lem-routef-f2-positive-unital-compression.md:7-8`;
`argument/lemmas/lem-routef-f3-retract-defect.md:7-8`). PRH finish is already
validated (`argument/lemmas/lem-routef-prh-finish.md:7-17`).

Use this well-founded order:

1. user-ratify the complexification/UCP vocabulary correction, both lift
   contracts, the strengthened-ledger classification, the sharpness choice,
   and the eventual OR wiring;
2. land/elevate both lift rows and F2/F3;
3. land/elevate every non-T0 transitive ledger input, explicitly including
   the repaired MAIN/polar producers needed to elevate
   `lem-thmainext-conditional`, the diagonal/CP-ization chain, D2/D3, and all
   fourteen ledger-domain rows;
4. prove/review/elevate the **strengthened replacement**
   `lem-routef-k-ledger`;
5. elevate `lem-routef-f0-assembly`;
6. if sharpness remains in the root, elevate `ex-hume`;
7. only then replace `op-classical`'s legacy `deps:` by the ratified
   `deps`/`routes` block.

The direct-dependency decoupling claim is correct: F0 has no MAIN or polar
import, and the ledger-domain design consumes MAIN through the public
`lem-thmainext-conditional` black box
(`docs/plans/2026-07-26-LEDGER-DOMAINS-design/DESIGN-LEDGER-DOMAINS-v2.md:66-86,180-197`;
`argument/lemmas/lem-thmainext-conditional.md:4-9`;
`docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md:256-260`).
MAIN and polar are nevertheless mandatory
transitive **elevation** work before that black box can serve an L0 ledger;
the corrected serial order must say so explicitly.
