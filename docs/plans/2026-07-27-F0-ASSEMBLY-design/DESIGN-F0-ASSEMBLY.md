# DESIGN — Route-F F0/root assembly

Date: 2026-07-27  
Role: fresh independent design mathematician  
Status: **DESIGN ONLY / NON-RIGOROUS / ESCALATED FOR USER RATIFICATION /
DO NOT SHARD, SEED, REWIRE, OR PROMOTE**

## 0. Verdict

**DESIGNED-CLOSABLE WITH CONTRACT CORRECTIONS; NOT ELEVATION-READY.**

The numerical interfaces compose with one universal \(K\) and one threshold:
the three factorization estimates feed F2 literally, F2 feeds F3 literally,
and F2+F3 feed PRH literally. No new estimate or constant is needed.

There are, however, three authoritative-registry mismatches:

1. `lem-routef-k-ledger` does not quantify the input \(Q\), does not state
   \(\lVert Q^2-Q\rVert_{\infty\to\infty}\le\eta\), and abbreviates rather
   than states the three estimates. Its phrase “associated stochastic map”
   does not close the input/output interface to `op-classical`.
2. `op-classical` includes “sharp exponent \(1/2\)” in its authoritative
   one-line contract. The Route-F upper-bound assembly does not prove
   sharpness. That parenthetical must be moved to the body/a separate
   obstruction statement, or `ex-hume` must be an actual dependency.
3. The brief calls F2 and F3 T0, but their authoritative frontmatter says
   `status: proved-mod-audit`, `af: none`. They must be elevated before an
   af-validated ledger or root can consume them.

Items 1–2 are **contract corrections**, not new mathematical gaps. Item 3 is
an **elevation gate**. The independently audited F0 cb-lift is also absent
from the registry and, to avoid a compound contract, needs two atomic rows.

## 1. Proposed rows

### 1.1 `lem-routef-f0-ucp-lift`

Proposed one-line contract:

> Route F F0 UCP lift: let \(n\ge1\), let
> \(D:M_n\to\ell_\infty^n\) be diagonal extraction and
> \(J:\ell_\infty^n\to M_n\) diagonal inclusion, and let
> \(Q:\ell_\infty^n\to\ell_\infty^n\) be row-stochastic; then
> \(\Phi:=JQD\) is UCP.

- `kind`: lemma
- initial honest status: `proved-mod-audit`
- `defs`: `def-stochastic`
- `deps`: none
- provenance:
  `docs/plans/2026-07-22-W73-artifacts/AUDIT-W73B-ROUTE-F.md` Q4
  (fresh hostile audit, verdict VALID); this is a local paper proof, not a
  published byte-matched theorem
- projected af: **3 nodes / depth 2** (positivity/complete positivity,
  unitality, root)

### 1.2 `lem-routef-f0-defect-identity`

Proposed one-line contract:

> Route F F0 defect identity: let \(n\ge1\), let
> \(D:M_n\to\ell_\infty^n\) be diagonal extraction and
> \(J:\ell_\infty^n\to M_n\) diagonal inclusion, let
> \(Q:\ell_\infty^n\to\ell_\infty^n\) be row-stochastic, and put
> \(\Phi:=JQD\); then
> \(\lVert\Phi^2-\Phi\rVert_{\rm cb}
> =\lVert Q^2-Q\rVert_{\infty\to\infty}\).

- `kind`: lemma
- initial honest status: `proved-mod-audit`
- `defs`: `def-stochastic; def-almost-idempotent`
- `deps`: none
- provenance: the same W73B Q4 hostile audit
- projected af: **5 nodes / depth 3** (\(DJ=I\), squaring, cb upper bound,
  cb lower bound, root)

The contract's sole mathematical conclusion is the norm identity.

### 1.3 Required correction to `lem-routef-k-ledger`

This is a correction to the existing row, not a third new row. Before F0 can
depend on it, its contract must bind the seam explicitly. Proposed corrected
one-line contract:

> Relative Route F factorization-and-finish ledger: there are universal
> \(K\ge1\) and \(\eta_K>0\), independent of \(n\), amplification level,
> simple-block count, and block dimensions, such that for every \(n\ge1\),
> every row-stochastic \(Q:\ell_\infty^n\to\ell_\infty^n\), and every
> \(0\le\eta\le\eta_K\) with
> \(\lVert Q^2-Q\rVert_{\infty\to\infty}\le\eta\), putting
> \(\Phi=JQD\), the repaired Kitaev factorization supplies a
> finite-dimensional unital \(C^*\)-algebra \(\mathcal B\) and UCP maps
> \(\Delta:\mathcal B\to M_n\), \(\Upsilon:M_n\to\mathcal B\) satisfying
> \(\lVert\Delta\Upsilon-\Phi\rVert_{\rm cb}\le K\eta\),
> \(\lVert\Upsilon\Delta-I_{\mathcal B}\rVert_{\rm cb}\le K\eta\), and
> \(\lVert\Upsilon_r(\Delta_rX\,\Delta_rY)-XY\rVert
> \le K\eta\lVert X\rVert\lVert Y\rVert\) for every amplification \(r\)
> and all \(X,Y\in M_r(\mathcal B)\), and the same \(Q\) admits a stochastic
> idempotent \(E\) with
> \(\lVert Q-E\rVert_{\infty\to\infty}
> \le(K+4\sqrt{2K})\sqrt\eta\).

No constant is new: \(K\) and
\(\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}\) are exported by the audited
ledger design. The correction only supplies missing binders, identifies the
same \(\Phi,\Delta,\Upsilon\) throughout, expands the three estimates, and
states that the output \(E\) repairs the input \(Q\).

The future direct deps should be the audited v2 §6.2 list plus the missing
lift:

```text
lem-routef-f0-ucp-lift
lem-routef-f0-defect-identity
lem-routef-delta-upsilon-telescope
lem-routef-multiplicative-telescope
lem-routef-upsilon-delta-telescope
lem-routef-k-finiteness
lem-routef-threshold-minimum
lem-routef-f2-positive-unital-compression
lem-routef-f3-retract-defect
lem-routef-prh-finish
```

Projected parent af workspace: **11 nodes / depth 2** (root plus ten
imports), within the linker envelope. The DO-NOT-REWIRE-OR-SEED guard remains
active.

Before landing, the telescope contracts must also quantify a common
\((\mathcal B,\Phi,\Delta,\Upsilon,\eta)\) datum rather than rely on the
design document's ambient notation. This is a **contract-closure correction**:
the v2 serial construction clearly intends the same maps, but the future
registry contracts must say so.

### 1.4 `lem-routef-f0-assembly`

Proposed one-line contract:

> Route F F0 assembly: there are universal \(\eta_0,C>0\), independent of
> \(n\), such that every \(n\ge1\), every row-stochastic
> \(Q:\ell_\infty^n\to\ell_\infty^n\), and every \(0\le\eta\le\eta_0\)
> with \(\lVert Q^2-Q\rVert_{\infty\to\infty}\le\eta\) admit a stochastic
> idempotent \(E\) satisfying
> \(\lVert Q-E\rVert_{\infty\to\infty}\le C\sqrt\eta\); for the universal
> \(K,\eta_K\) supplied by `lem-routef-k-ledger`, one may take
> \(\eta_0=\eta_K\) and \(C=K+4\sqrt{2K}\).

- `kind`: lemma
- initial honest status after paper review: at most `proved-mod-audit`
- `defs`: `def-stochastic; def-almost-idempotent`
- `deps`: `lem-routef-k-ledger`
- provenance: the corrected K-ledger contract; F2, F3, and PRH authoritative
  shards; `DESIGN-LEDGER-DOMAINS-v2.md` §§3.5, 6.2 and
  `AUDIT-LEDGER-DOMAINS-v2.md` §§3, 6
- projected af: **2 nodes / depth 2** (ledger import plus existential
  specialization)

No other glue row is needed.

## 2. Single-\(K\), single-threshold audit

| seam | literal check | disposition |
|---|---|---|
| Stochastic defect \(\to\) Kitaev input | The two proposed lift rows give the same \(\Phi=JQD\), first UCP and then with exact equality \(\|\Phi^2-\Phi\|_{\rm cb}=\|Q^2-Q\|_{\infty\to\infty}\). | **MATCH after adding both lift rows.** No \(\eta\mapsto\varepsilon_{\rm AI}(\eta)\) conversion occurs at this seam. |
| Ledger \(\to\) F2, first estimate | Ledger telescope: \(\|\Delta\Upsilon-\Phi\|_{\rm cb}\le K\eta\). F2 asks exactly this estimate for the same \(\Phi=JQD\). | **EXACT MATCH**, once the corrected parent binds the same objects. |
| Ledger \(\to\) F2, second estimate | Ledger telescope: \(\|\Upsilon\Delta-I_{\mathcal B}\|_{\rm cb}\le K\eta\). | **EXACT MATCH.** |
| Ledger \(\to\) F2, multiplicativity | Ledger row 11 gives the estimate at every amplification and for all matrix-level \(X,Y\). F2 needs only level one, for all \(x,y\in\mathcal B\), with the same product orientation. | **MATCH; ledger is stronger.** No norm conversion is needed. |
| Common coefficient | Row 13 defines \(K\) as the maximum of \(1\) and the three telescope coefficients. | **ONE \(K\)** dominates all three estimates; no re-enlargement downstream. |
| Common domain | Corrected audit leaves \(\eta_K=\min\{\rho_{\rm fac},(24K)^{-1},1\}>0\). The row-3 repair adds \(\rho_\theta=1/8\) only inside \(\rho_{\rm id}\) and does not change the effective terminal minimum. | **ONE \(\eta_K\).** It also lies below \(1/4\), matching `def-almost-idempotent`. |
| F2 threshold | F2 asks \(0\le\eta\le\min\{(24K)^{-1},1\}\). | **EXACTLY PROVIDED** by \(\eta\le\eta_K\). |
| F2 \(\to\) F3 | F2 produces positive unital \(A,M\), \(\|Q-AM\|\le K\eta\), \(\|QA-A\|\le2K\eta\), and \(\|Ax\|\ge(1-3K\eta)\|x\|\) for every \(x\). F3 asks exactly these data. | **EXACT MATCH**, including the universal quantifier on \(x\). |
| F3 strict denominator guard | \(\eta\le(24K)^{-1}\) gives \(3K\eta\le1/8<1\). | **MATCH.** |
| F3 \(\to\) PRH | F3 gives \(\|MA-I_k\|\le3K\eta/(1-3K\eta)\). F2 already gives positive unital \(A,M\) and \(\|Q-AM\|\le K\eta\). | **EXACT MATCH** to `lem-routef-prh-finish`. |
| Norm discipline | The three factor estimates are cb/amplified norms because F2 requires them there. From F2 onward every displayed norm is the \(\ell_\infty\to\ell_\infty\) norm. `inf->inf` versus `infinity->infinity` is notation only. | **NO NORM GAP**, but normalize spelling when contracts are ratified. |
| PRH \(\to\) root | PRH returns a stochastic idempotent for the same \(Q\), with \((K+4\sqrt{2K})\sqrt\eta\). | **EXACT UPPER-BOUND MATCH.** |

The current K-ledger contract's omitted \(Q\)-binder, defect antecedent, and
exact estimate block are therefore the only substantive seam mismatch.
Classification: **contract correction needed**, not a new glue estimate and
not a genuine mathematical gap.

## 3. Root wiring and double-counting

F2, F3, and PRH are consumed **inside `lem-routef-k-ledger`**. Consequently
`lem-routef-f0-assembly` consumes only `lem-routef-k-ledger`; it must not list
F2, F3, or PRH again.

The existing signed-geometry route is independent and should not silently
become an AND-premise of Route F. The exact proposed root import block is:

```yaml
deps:
routes: [lem-routef-f0-assembly] | [thm-classical-factorization; prop-approx-simplex]
```

Thus each Route-F direct edge occurs once:

```text
F2, F3, PRH, two lift rows, telescopes, K-finiteness, threshold
    -> lem-routef-k-ledger
    -> lem-routef-f0-assembly
    -> op-classical
```

This preserves the legacy route as an alternative. Merely appending F0 to
the current `deps:` would incorrectly require both independent proofs.

## 4. Sharpness and signed-equivalence side check

Route F proves only the displayed \(O(\sqrt\eta)\) upper bound, with
\(C=K+4\sqrt{2K}\). It neither improves nor worsens the exponent.

- `ex-hume` is the separate sharpness obstruction. It is not used in the
  construction of \(E\) and must not be a Route-F dependency.
- `lem-classical-equiv` is the signed/stochastic bridge. Route F begins with
  a row-stochastic \(Q\) and ends with a stochastic idempotent \(E\), so it
  never crosses that bridge.

The current `op-classical` contract nevertheless contains the sharpness
claim. Recommended ratified correction: make the contract the upper
stability theorem only and keep sharpness in the body/`ex-hume`. If the
literal compound contract is retained, then the Route-F root route must be
`[lem-routef-f0-assembly; ex-hume]`; omitting `ex-hume` would be overclaiming.

## 5. Dimension-freeness

\(K\) and \(\eta_K\) are universal outputs of the corrected ledger. The
defect lift is an exact complete-norm identity with constant \(1\). F2 and F3 introduce
only \(2,3,24\); PRH introduces only \(4\) and \(\sqrt2\). Existential
specialization introduces nothing. Hence
\[
\eta_0=\eta_K,\qquad C=K+4\sqrt{2K}
\]
are independent of \(n\). No amplification level, block count, block
dimension, Choi multiplicity, or MAIN stage index reaches F0.

## 6. Feasibility and serial landing order

| row | feasibility | gates before elevation |
|---|---|---|
| `lem-routef-f0-ucp-lift` | **ELEVATION-READY AFTER RATIFICATION** | Land the closed contract; fresh reviewer; af seed/prover/verifier. It is independent of MAIN, polar, and the ledger rows. |
| `lem-routef-f0-defect-identity` | **ELEVATION-READY AFTER RATIFICATION** | Land the closed contract; fresh reviewer; af seed/prover/verifier. It is independent of MAIN, polar, the UCP-lift proof, and the ledger rows. |
| corrected `lem-routef-k-ledger` | **CLOSABLE, NOT READY** | Apply the two ledger-v2 audit corrections; close common-datum binders; user-ratify all ledger rows and wiring; land/elevate the fourteen rows and D2/D3; elevate F2 and F3; validate every imported parent, including `lem-thmainext-conditional`. |
| `lem-routef-f0-assembly` | **READY ONLY AFTER THE LEDGER** | User-ratify the root/ledger contract corrections; validate the corrected ledger; then a two-node assembly pass. |
| `op-classical` wiring | **LAST** | Resolve the sharpness-contract split; use OR-routes; rewire only after the Route-F assembly is validated. |

Serial order:

1. ratify the two new row contracts, the K-ledger binder correction, the
   root sharpness split, and the proposed OR-route wiring;
2. land/elevate the two independent lift rows and F2/F3;
3. land/elevate the corrected ledger-domain DAG and its parent;
4. elevate `lem-routef-f0-assembly`;
5. rewire and discharge the Route-F route of `op-classical`.

At the design/paper interface, the ledger remains decoupled from the
unlanded MAIN reset internals: it consumes only the public
`lem-thmainext-conditional` black-box constants \(C_E,\varepsilon_E\).
For eventual L0 closure, MAIN and polar matter only transitively through
validation of that black box. F0 has no direct MAIN or polar dependency.

No registry, definition, proof workspace, status, or guard is changed by
this design.
