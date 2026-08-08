Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE — pending fresh hostile audit and user ratification.

# DESIGN — strengthened `lem-routef-k-ledger` replacement and F0 assembly landing

Date: 2026-08-08  
Role: fresh independent design worker  
Disposition: LANDING TEXT COMPLETE; 15-DEpendency INTERFACE CLOSES; PARENT CAP NEEDS HOSTILE BUDGET ATTACK

Nothing in this file is a proof, registry edit, status promotion, guard release, seed, or root rewire.
The proposed rows remain non-rigorous until separately landed, proved, and hostile-verified under the
repository protocol. `op-classical` remains open.

## 1. Dependency decision: retain the binding 15-row block

The strengthened parent needs **15**, not 16, direct dependencies. In particular it does **not** need
`lem-routef-upsilon-prime-component-construction` directly.

The current byte-frozen contract of `lem-routef-upsilon-prime-closeness` already concludes that, for the
same `(W_RF,S,Delta',Delta)`, “the componentwise construction produces CP Upsilon'” together with
`||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta`. The current row-9 contract then quantifies “every
Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness” and produces the UCP map
`Upsilon`. The strengthened parent consumes only that exported `Upsilon'`, the resulting `Upsilon`, and
the three telescope estimates. It never opens the Choi/twirl package
`(m,(L_j,E_j,W_j,Sigma_j,U_js,p_js,C_j,xi_j,Lambda_j,Upsilon'_j),F,V,Upsilon')`.

Thus the component-construction and left-inverse rows remain genuine T0 transitive dependencies of row
8, but neither is a direct dependency of the parent. Adding the component row would duplicate an
implementation dependency without supplying any datum used by the parent contract or proof skeleton.
If a future proof worker opens the component package rather than treating row 8 as a black box, that is
a same-interface failure and must stop for a fresh dependency audit; it is not authorization to add a
sixteenth edge during seeding.

## 2. Complete replacement shard: `lem-routef-k-ledger.md`

The following is the complete proposed replacement text. The contract is a strengthened replacement and
a new proof obligation, not a binder edit. Its status therefore starts at `stated`, not at the superseded
paper ledger's `proved-mod-audit` rung.

```markdown
---
id: lem-routef-k-ledger
kind: lemma
contract: Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish
status: stated
af: none
provenance: Strengthened replacement required by docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect-1.3 and corrected by AUDIT-F0-ASSEMBLY.md findings 1 and 3 (new fully quantified parent proof obligation, canonical Q_C typing); dependency/application rescope fixed by docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-6.2 and hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md; row-8 factoring interface from docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md and its landed T0 rows; exact landing package proposed by DESIGN-KLEDGER-STRENGTHENED.md, pending its required fresh hostile audit and user ratification. Supersedes the narrower W74F proved-mod-audit paper-ledger contract recorded in docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md, PROOF-W74F-H-STAGE1.md, VERDICT-W74F-G-KLEDGER.md, and VERDICT-W74F-H-STAGE1.md; that historical verdict does not transfer status to this strengthened statement.
owner: A
workspace: proofs/lem-routef-k-ledger
---

**Status.** `stated`, `af: none`. This fully quantified statement is a strengthened
replacement and a new proof obligation. It is not a wording repair of the W74F paper
ledger, and no part of the old `proved-mod-audit` status is inherited. Landing this shard
promotes no mathematics.

**Closed input seam.** For each `n,Q,eta`, the contract defines the complex matrix-algebra
typing explicitly: `D:M_n->C^n`, `J:C^n->M_n`, the canonical complex-linear extension
`Q_C:C^n->C^n`, and `Phi:=J Q_C D`. The two F0 rows give UCP and the exact defect identity
for this same `Phi`. The one outer `W_RF` is selected before all inputs; its `K`, `rho_fac`,
and `eta_K` are exactly the scalars (1.6)--(1.8) of
[[def-routef-raw-factor-setting]], certified by [[lem-routef-k-finiteness]] and
[[lem-routef-threshold-minimum]].

**Same-datum application order.** Apply the dependencies in the following order, without
reselecting any datum:

```text
F0 UCP lift + F0 defect identity
  -> eta <= eta_K <= rho_fac <= rho_T <= rho_id^corr
  -> formation for H=C^n and the same Phi,eta
  -> row 5 (Delta') -> row 6 (Delta)
  -> row 8 (Upsilon') -> row 9 (Upsilon)
  -> rows 10,11,12 -> row 13 -> row 14
  -> F2 -> F3 -> PRH.
```

Row 8's public contract exports the `Upsilon'` consumed by row 9. The parent does not use
the internal componentwise package, so the two ROW8-FACTOR lemmas stay transitive rather
than direct imports.

**What the statement proves if validated.** The first ten applications produce one
finite-dimensional `B` and one UCP pair `Delta,Upsilon` for the F0 lift of the input `Q`.
The three telescope coefficients are bounded by the same `K` from (1.6). Row 14 supplies
the terminal threshold and strict denominator guard. F2 then gives positive unital
`A,M`, F3 gives the retract defect, and PRH returns `E` for the same `Q` with constant
`K+4*sqrt(2*K)`.

**Superseded paper-ledger history.** Before this replacement, the shard carried the W74F
contract beginning “Relative Route F factorization ledger: there are universal K ... for
every 0 <= eta <= eta_K” and ending with “the associated stochastic map”. Fresh hostile
review had repaired and endorsed that narrower paper ledger at `proved-mod-audit`, after
rejecting its first version for a missing Stage-1 packet. It did not quantify the original
`n,Q`, did not bind the stochastic defect antecedent or `Q_C`, and did not prove this
closed same-`Q` statement. That evidence remains part of the historical provenance only.

**Sharpness boundary.** This row proves only the Route-F upper bound. It neither states nor
proves sharpness of exponent `1/2`; `ex-hume` remains the separate obstruction. No signed
to stochastic crossing occurs here.

**Guard.** Landing this exact strengthened replacement releases the DO-NOT-REWIRE guard on
`lem-routef-k-ledger` itself. It does not edit, rewire, discharge, or change the status of
`op-classical`; the root rewire remains a separate LAST step after F0 assembly is T0.

**Designed af budget.** Binding target: 17 designed nodes, at most 4 rounds, hard cap 22.
The cap is not raised. Section 6 records the required hostile expansion assessment and the
factoring contingency.
```

## 3. Complete new shard: `lem-routef-f0-assembly.md`

The following is the complete proposed new shard. Its only dependency is the strengthened parent; F2,
F3, PRH, formation, and the packet rows must not be duplicated here.

```markdown
---
id: lem-routef-f0-assembly
kind: lemma
contract: Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).
defs: def-stochastic; def-almost-idempotent
deps: lem-routef-k-ledger
status: stated
af: none
provenance: docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect-1.4 (assembly row and no-double-counting rule), with the canonical complexification typing correction required by AUDIT-F0-ASSEMBLY.md; strengthened-parent interface and exact constants from DESIGN-KLEDGER-STRENGTHENED.md, pending its required fresh hostile audit and user ratification. This is an upper-bound assembly only; no sharpness claim is imported or promoted.
owner: A
workspace: proofs/lem-routef-f0-assembly
---

**Status.** `stated`, `af: none`. This is a proposed one-step specialization of the
strengthened [[lem-routef-k-ledger]] and promotes nothing at landing.

**Specialization.** Take `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)` from the parent. The parent
states that `eta_K>0`, `K>=1`, both are universal and dimension-free, and for every
admissible `n,Q,eta` returns the required stochastic idempotent for the same `Q`.

**No double counting.** Registry `deps:` is exactly `lem-routef-k-ledger`. The parent
already consumes both F0 seam rows, formation, the factor-map packet, F2, F3, and PRH.
Repeating any of those edges here would misstate the module boundary.

**Sharpness and root guard.** This row proves only the upper-bound statement displayed in
its contract. It does not consume `ex-hume`, does not claim sharpness, and does not edit or
rewire `op-classical`. Root rewire remains the separate LAST step after this row is T0.

**Designed af budget.** Target 2 nodes / depth 2 / at most 2 rounds / hard cap 6.
```

## 4. Re-run seam table against the current frozen contracts

`EXACT-MATCH` means the current dependency exports exactly the datum or inequality consumed, modulo
specializing an explicit universal quantifier and the registry's cosmetic `inf`/`infinity` spelling.
`MATCH-STRONGER` means the dependency exports a strictly stronger quantified statement or guard. Any
`MISMATCH` would stop this package. There are no mismatches in this re-run.

| order | producer / current frozen text consumed | consumer requirement and same-datum check | verdict |
|---:|---|---|---|
| 1 | `lem-routef-f0-ucp-lift`: for `D:M_n->C^n`, `J:C^n->M_n`, row-stochastic `Q`, and “the canonical complex-linear extension” `Q_C`, `Phi := J Q_C D` is UCP. | The parent binds byte-compatible `D,J,Q,Q_C,Phi`; formation requires UCP on `B(H)` with `H=C^n`. | **EXACT-MATCH** |
| 2 | `lem-routef-f0-defect-identity`: for the same typing, `||Phi^2-Phi||_cb = ||Q^2-Q||_{infinity->infinity}`. | The parent antecedent bounds the right side by the same `eta`, so formation receives `||Phi^2-Phi||_cb<=eta` with no defect conversion. | **EXACT-MATCH** |
| 3 | `def-routef-raw-factor-setting` (1.1),(1.2),(1.7),(1.8) and rows 13--14: `eta_K<=rho_fac`, `rho_fac<=rho_2`, `rho_2<=rho_prod=rho_T`, and `rho_T<=rho_id^corr`. | Required chain is `eta <= eta_K <= rho_fac <= rho_T <= rho_id^corr`; the displayed finer chain supplies it. | **EXACT-MATCH** |
| 4 | `lem-routef-raw-factor-setting-formation`: one global `W_RF`, then for every finite-dimensional nonzero `H`, UCP `Phi`, and admissible `eta`, one `B,v,S` over the same header. | Use `H=C^n`, the exact F0 `Phi`, and the same stochastic `eta`; `n>=1` gives nonzero finite-dimensional `H`. No witness is reselected downstream. | **EXACT-MATCH** |
| 5 | `lem-routef-delta-prime-closeness`: at `eta<=rho_Delta'`, produces CP `Delta'` for the fixed `(W_RF,S)`. | `eta<=eta_K<=rho_fac<=rho_2<=rho_Delta'`; parent fixes this output for the same datum. | **EXACT-MATCH** |
| 6 | `lem-routef-delta-normalization-closeness`: for every such `Delta'`, at `eta<=rho_Delta`, produces UCP `Delta` and its cb closeness. | `eta<=eta_K<=rho_fac<=rho_2<=rho_Delta`; the parent uses this same `Delta`. | **EXACT-MATCH** |
| 7 | `lem-routef-upsilon-prime-closeness`: for the same `Delta',Delta`, at `eta<=rho_Upsilon'`, “the componentwise construction produces CP Upsilon'” with cb closeness. | `eta<=eta_K<=rho_fac<=rho_DeltaUpsilon<=rho_Upsilon<=rho_Upsilon'`; this public output, not its internal component package, is all the parent needs. | **EXACT-MATCH** |
| 8 | `lem-routef-upsilon-normalization-closeness`: for every `Upsilon'` supplied by row 8, at `eta<=rho_Upsilon`, produces UCP `Upsilon` with cb closeness. | `eta<=eta_K<=rho_fac<=rho_DeltaUpsilon<=rho_Upsilon`; the producer wording forces the same row-8 output and the same `Delta',Delta`. | **EXACT-MATCH** |
| 9 | `lem-routef-delta-upsilon-telescope`: on the explicitly threaded packet, at `eta<=rho_DeltaUpsilon`, `||Delta Upsilon-Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta`. | `rho_fac<=rho_DeltaUpsilon`; (1.6) makes this coefficient `<=K`. | **EXACT-MATCH** |
| 10 | `lem-routef-multiplicative-telescope`: for every amplification and all `X,Y`, at `eta<=rho_mult`, the error is `[C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||`. | `rho_fac<=rho_mult`; (1.6) bounds the coefficient by `K`. F2 needs only amplification `r=1`. | **MATCH-STRONGER** |
| 11 | `lem-routef-upsilon-delta-telescope`: at `eta<=rho_UpsilonDelta`, `||Upsilon Delta-I_B||_cb <= (C_Upsilon+2*C_Delta)*eta`. | `rho_fac<=rho_UpsilonDelta`; (1.6) bounds the coefficient by `K`. | **EXACT-MATCH** |
| 12 | `lem-routef-k-finiteness`: `K` in (1.6) is finite and universal, and `rho_fac` is positive and common to the degree-two and three factorization estimates. | Together with the definition `K=max{1,...}`, this gives the parent's one dimension-free `K>=1` and one common factor domain. | **EXACT-MATCH** |
| 13 | `lem-routef-threshold-minimum`: `eta_K:=min{rho_fac,(24*K)^(-1),1}>0`, with `eta<=rho_fac`, the exact F2 window, `3Keta<=1/8<1`, and `3Keta/(1-3Keta)<=4Keta<=1/6`. | These are exactly the terminal constants and all scalar guards used by F2, F3, and PRH. | **EXACT-MATCH** |
| 14 | The three telescope rows plus (1.6) yield the two cb bounds and the all-amplification multiplicativity bound with coefficient `K`. | `lem-routef-f2-positive-unital-compression` assumes the same `Q,D,J,Q_C,Phi,B,Delta,Upsilon`, the same threshold, both cb bounds, and the multiplicativity bound for all `x,y in B`. | **MATCH-STRONGER** (all amplifications specialize to level one) |
| 15 | F2 concludes positive unital `A,M` with `||Q-AM||<=Keta`, `||QA-A||<=2Keta`, and `||Ax||>=(1-3Keta)||x||` for every `x`. | `lem-routef-f3-retract-defect` has exactly these hypotheses for the same `n,k,Q,K,eta,A,M`. | **EXACT-MATCH** |
| 16 | Row 14 gives `3Keta<=1/8<1`. | F3 requires the strict guard `3Keta<1`. | **MATCH-STRONGER** |
| 17 | F3 concludes `||MA-I_k||<=3Keta/(1-3Keta)`; F2 already supplied positive unital `A,M` and `||Q-AM||<=Keta`. | `lem-routef-prh-finish` has exactly these hypotheses and the same threshold for the same `Q`. | **EXACT-MATCH** |
| 18 | PRH returns a stochastic idempotent `E` with `||Q-E|| <= (K+4*sqrt(2*K))*sqrt(eta)`. | This is the strengthened parent's same-`Q` conclusion and specializes to F0 assembly with `eta_0=eta_K`, `C=K+4*sqrt(2*K)`. | **EXACT-MATCH** |

**Global seam verdict: ALL 18 CHECKS PASS; 15 EXACT-MATCH and 3 MATCH-STRONGER; 0 MISMATCH.**

## 5. Complete af tree skeletons

These are design skeletons only. Node statements deliberately repeat the same-datum clauses so a proof
worker cannot satisfy the root by independently choosing incompatible packets.

### 5.1 Strengthened `lem-routef-k-ledger` — 17 designed nodes

- **Node 1 — Root.** Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
- **Node 1.1 — F0 UCP seam.** Under the root's arbitrary `n>=1`, row-stochastic `Q`, `D`, `J`, canonical complex-linear extension `Q_C`, and `Phi:=J Q_C D`, the map `Phi:M_n->M_n` is UCP.
- **Node 1.2 — F0 defect seam.** Under the same root datum, `||Phi^2-Phi||_cb = ||Q^2-Q||_{infinity->infinity} <= eta`.
- **Node 1.3 — Common domain chain.** For the single `W_RF` furnished by formation, its scalars satisfy `eta <= eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr`; in particular formation applies to `(H:=C^n,Phi,eta)`, rows 5 and 6 apply, and every later factorization domain required below contains `eta`.
- **Node 1.4 — Same-input formation.** For the one outer `W_RF` and the root's same `(H:=C^n,Phi,eta)`, there exist one finite-dimensional unital C*-algebra `B`, one extended isomorphism `v`, and one `def-routef-raw-factor-setting` datum `S` over that `W_RF`, with all fields and conclusions exported by `lem-routef-raw-factor-setting-formation`; fix this one `(B,v,S)` for every remaining node.
- **Node 1.5 — Delta-prime construction.** For the fixed `(W_RF,S)` of node 1.4 and the same `eta`, `lem-routef-delta-prime-closeness` supplies one CP map `Delta'` with `||Delta'-tilde-Delta||_cb <= C_Delta'*eta`; fix this `Delta'`.
- **Node 1.6 — Delta normalization.** From the same `(W_RF,S,Delta')`, `lem-routef-delta-normalization-closeness` supplies one UCP map `Delta:B->M_n` with `||Delta-tilde-Delta||_cb <= C_Delta*eta`; fix this `Delta`.
- **Node 1.7 — Upsilon-prime construction.** From the same `(W_RF,S,Delta',Delta)`, `lem-routef-upsilon-prime-closeness` supplies one CP map `Upsilon':M_n->B` with `||Upsilon'-tilde-Upsilon||_cb <= C_Upsilon'*eta`; fix this public row-8 output without opening its internal component package.
- **Node 1.8 — Upsilon normalization.** From the same `(W_RF,S,Delta',Delta,Upsilon')`, `lem-routef-upsilon-normalization-closeness` supplies one UCP map `Upsilon:M_n->B` with `||Upsilon-tilde-Upsilon||_cb <= C_Upsilon*eta`; fix this `Upsilon`.
- **Node 1.9 — Delta-Upsilon estimate.** For the fixed packet of nodes 1.4--1.8, `||Delta Upsilon-Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta`.
- **Node 1.10 — Multiplicativity estimate.** For the same fixed packet, every integer `r>=1`, and all `X,Y in M_r(B)`, `||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||`.
- **Node 1.11 — Upsilon-Delta estimate.** For the same fixed packet, `||Upsilon Delta-I_B||_cb <= (C_Upsilon+2*C_Delta)*eta`.
- **Node 1.12 — One universal coefficient.** For this one `W_RF`, `K=max{1,C_theta+C_Delta+2*C_Upsilon,C_Upsilon+2*(C_2+C_theta+C_Delta),C_Upsilon+2*C_Delta}` is finite, universal, dimension-free, and at least `1`; nodes 1.9--1.11 therefore imply the root's three factorization estimates with the common coefficient `K`.
- **Node 1.13 — One terminal threshold.** For this same `W_RF` and `K`, `eta_K=min{rho_fac,(24*K)^(-1),1}>0`; every root input `0<=eta<=eta_K` satisfies `eta<=rho_fac`, `eta<=min{(24*K)^(-1),1}`, `3*K*eta<=1/8<1`, and `3*K*eta/(1-3*K*eta)<=4*K*eta<=1/6<1/2`.
- **Node 1.14 — F2 specialization.** Applying `lem-routef-f2-positive-unital-compression` to the root's same `Q,D,J,Q_C,Phi`, the fixed `B,Delta,Upsilon`, nodes 1.9--1.13, and the level-one specialization of node 1.10 gives `k>=1` and positive unital maps `A:l_inf^k->l_inf^n`, `M:l_inf^n->l_inf^k` satisfying `||Q-AM||_{inf->inf}<=K*eta`, `||QA-A||_{inf->inf}<=2*K*eta`, and `||Ax||_inf >= (1-3*K*eta)*||x||_inf` for every `x in l_inf^k`.
- **Node 1.15 — F3 specialization.** Since node 1.13 gives `3*K*eta<1`, applying `lem-routef-f3-retract-defect` to the same `Q,K,eta,A,M` from node 1.14 yields `||MA-I_k||_{inf->inf} <= 3*K*eta/(1-3*K*eta)`.
- **Node 1.16 — PRH finish and quantifier assembly.** Applying `lem-routef-prh-finish` to the same `Q,K,eta,A,M` from nodes 1.13--1.15 gives a stochastic idempotent `E` with `||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta)`; because `W_RF,K,eta_K` were fixed before the arbitrary `n,Q,eta`, assembling the quantifiers proves node 1.

Designed count: **17** including the root. Maximum rounds: **4**. Hard cap: **22**.

### 5.2 `lem-routef-f0-assembly` — 2 designed nodes, depth 2

- **Node 1 — Root.** Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).
- **Node 1.1 — Specialization.** Take the universal `K>=1` and `eta_K>0` of `lem-routef-k-ledger`, define `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)>0`, and specialize that lemma to the root's arbitrary `n,Q,eta,D,J,Q_C,Phi`; its same-`Q` stochastic idempotent is the required `E`, and its displayed bound is exactly `C*sqrt(eta)`.

Designed count: **2**. Depth: **2**. Maximum rounds: **2**. Hard cap: **6**.

## 6. Budget re-audit and mandatory factoring contingency

### 6.1 Honest expansion assessment

The 2-node F0 assembly is credible under the observed `1.5x--3x` fresh-build expansion: that range is
3--6 live nodes, exactly within cap 6.

The 17-node strengthened parent is **not robustly credible under that empirical multiplier**. A literal
application predicts 26--51 live nodes, already above cap 22 at the low end. The skeleton is unusually
external-heavy—15 mathematical steps are direct applications of already T0 contracts—so a disciplined
fresh prover may stay close to 17, but the observed family history does not justify assuming that. The
correct design verdict is therefore:

> Landability of the statement is closed, but monolithic elevation under cap 22 is a hostile-audit
> risk. Cap 22 is binding and must not be raised. If the fresh auditor cannot defend an at-most-22 build,
> or if the live build reaches the cap, stop and factor before further rounds.

### 6.2 Proposed factoring if cap 22 cannot be defended

Do not enact this contingency without a separate hostile audit and user ratification, because it would
change the binding 15-edge public parent. The natural split is two private registry helpers, followed by
the unchanged public strengthened contract:

1. `lem-routef-factor-map-packet`: F0 lift/defect, the scalar domain chain, formation, rows 5/6, and rows
   8/9; exports one same-input `(W_RF,S,B,Delta',Delta,Upsilon',Upsilon)` packet. Combine each adjacent
   producer pair into one proof node. Target 6 designed nodes, cap 18.
2. `lem-routef-factor-estimate-packet`: consumes the first helper, rows 10/11/12, row 13, and row 14;
   exports the same `K,eta_K,B,Delta,Upsilon` and the three `K*eta` estimates. Target 6 designed nodes,
   cap 18.
3. The public `lem-routef-k-ledger` then consumes the second helper plus F2, F3, and PRH and keeps the
   exact contract in section 2. Target 5 designed nodes, cap 15.

Each proposed count remains at most 18 even under `3x` expansion. This is a factoring proposal only, not
an alternate deps line in the land-ready shard. The hostile auditor must choose between (i) defending the
17/22 external-heavy monolith or (ii) escalating this two-helper split for user ratification. Inflating
cap 22 is not an option.

## 7. Seeding packages

No command in this section is authorized by this design. Before every future `def-add` or
`add-external`, preflight the workspace for duplicate names; if any root bytes or registry dependency
bytes differ from the strings below, stop and re-audit rather than seeding stale text.

### 7.1 Strengthened parent: `def-add` list

Add the complete bytes of these existing definition shards, exactly once, in this order:

1. `def-routef-raw-factor-setting` <- `definitions/def-routef-raw-factor-setting.md`
2. `def-stochastic` <- `definitions/def-stochastic.md`
3. `def-almost-idempotent` <- `definitions/def-almost-idempotent.md`
4. `def-ucp-map` <- `definitions/def-ucp-map.md`
5. `def-extended-epsilon-cstar-algebra` <- `definitions/def-extended-epsilon-cstar-algebra.md`
6. `def-extended-delta-inclusion` <- `definitions/def-extended-delta-inclusion.md`

The first four are the root's declared vocabulary. The last two close the vocabulary appearing in the
formation external. No new definition is proposed. Neither
`GT-kitaev-fd-cstar-structure` nor `GT-kitaev-canonical-stinespring` is needed: all structure and
Stinespring work is sealed behind T0 row 8 and F2 contracts rather than re-derived in this workspace.

### 7.2 Strengthened parent: exact `add-external` list

Add these 15 externals in dependency/application order. Each source string follows the literal
`proofs/<dep-id>` path plus byte-verbatim registry-contract convention.

**E1 — `lem-routef-f0-ucp-lift`**

```text
imports validated registry lemma proofs/lem-routef-f0-ucp-lift — Route F F0 UCP lift: let n >= 1, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C) and J: C^n -> M_n the diagonal inclusion, let Q: l_inf^n -> l_inf^n be row-stochastic, and let Q_C: C^n -> C^n be the canonical complex-linear extension of Q; then Phi := J Q_C D: M_n -> M_n is a unital completely positive map.
```

**E2 — `lem-routef-f0-defect-identity`**

```text
imports validated registry lemma proofs/lem-routef-f0-defect-identity — Route F F0 defect identity: let n >= 1, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C) and J: C^n -> M_n the diagonal inclusion, let Q: l_inf^n -> l_inf^n be row-stochastic with canonical complex-linear extension Q_C: C^n -> C^n, and put Phi := J Q_C D; then ||Phi^2 - Phi||_cb = ||Q^2 - Q||_{infinity->infinity}.
```

**E3 — `lem-routef-raw-factor-setting-formation`**

```text
imports validated registry lemma proofs/lem-routef-raw-factor-setting-formation — Route F raw-factor setting formation: there exists one choice W_RF of the scalar header of def-routef-raw-factor-setting, independent of H, Phi, eta, dimension, amplification level, and block data, with C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, eta_A>0 and (C_A,eta_A) the fixed witnesses of lem-routef-ai-defect-linearization, C_E<infinity and epsilon_E>0 the fixed witnesses of lem-thmainext-conditional, rho_theta:=1/8, rho_AI:=eta_A, and all remaining named scalar quantities defined by (1.1)-(1.8), such that for every nonzero finite-dimensional Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta with 0 <= eta <= rho_id^corr and ||Phi^2-Phi||_cb <= eta, there exist a finite-dimensional unital C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and a def-routef-raw-factor-setting datum S over this same W_RF whose fields are the displayed H,Phi,eta,B,v,u=v^(-1) and the canonical tilde-Phi,A,star,epsilon_AI(eta),tilde-Delta,tilde-Upsilon notation, with tilde-Phi^2=tilde-Phi, A an extended epsilon_AI(eta)-C*-algebra, and 0 <= epsilon_AI(eta) <= C_A*eta <= epsilon_E.
```

**E4 — `lem-routef-delta-prime-closeness`**

```text
imports validated registry lemma proofs/lem-routef-delta-prime-closeness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta.
```

**E5 — `lem-routef-delta-normalization-closeness`**

```text
imports validated registry lemma proofs/lem-routef-delta-normalization-closeness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result and for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and for every X in S.B, writing the fields of (W_RF,S) as the unqualified symbols below: Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with ||Delta - tilde-Delta||_cb <= C_Delta*eta.
```

**E6 — `lem-routef-upsilon-prime-closeness`**

```text
imports validated registry lemma proofs/lem-routef-upsilon-prime-closeness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every Choi multiplicity space used below is nonzero and the componentwise construction produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta.
```

**E7 — `lem-routef-upsilon-normalization-closeness`**

```text
imports validated registry lemma proofs/lem-routef-upsilon-normalization-closeness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and for every X in B(H), writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon UCP normalization: with C_Upsilon := 6*C_T+7*C_Upsilon' and rho_Upsilon := min{rho_unit, rho_Upsilon', [2*(C_T+C_Upsilon')]^(-1)}, for 0 <= eta <= rho_Upsilon, b = Upsilon'(I) is invertible and Upsilon(X) = b^(-1/2)*Upsilon'(X)*b^(-1/2) is UCP with ||Upsilon - tilde-Upsilon||_cb <= C_Upsilon*eta.
```

**E8 — `lem-routef-delta-upsilon-telescope`**

```text
imports validated registry lemma proofs/lem-routef-delta-upsilon-telescope — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-Upsilon telescope: for rho_DeltaUpsilon := min{rho_theta, rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_DeltaUpsilon, ||Delta Upsilon - Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta.
```

**E9 — `lem-routef-multiplicative-telescope`**

```text
imports validated registry lemma proofs/lem-routef-multiplicative-telescope — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Multiplicative telescope: for rho_mult := min{rho_T, rho_id, rho_DeltaPhi, rho_Upsilon} and 0 <= eta <= rho_mult, every amplification satisfies ||Upsilon_n(Delta_n X Delta_n Y) - XY|| <= [C_Upsilon+2*(C_2+C_theta+C_Delta)]*eta*||X||*||Y||.
```

**E10 — `lem-routef-upsilon-delta-telescope`**

```text
imports validated registry lemma proofs/lem-routef-upsilon-delta-telescope — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-Delta telescope: for rho_UpsilonDelta := min{rho_T, rho_id, rho_Delta, rho_Upsilon} and 0 <= eta <= rho_UpsilonDelta, ||Upsilon Delta - I_B||_cb <= (C_Upsilon+2*C_Delta)*eta.
```

**E11 — `lem-routef-k-finiteness`**

```text
imports validated registry lemma proofs/lem-routef-k-finiteness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F common coefficient/domain: K in (1.6) is finite and universal, and rho_fac in (1.7) is positive and is a common domain for the degree-two estimate and the three Route-F factorization estimates.
```

**E12 — `lem-routef-threshold-minimum`**

```text
imports validated registry lemma proofs/lem-routef-threshold-minimum — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F scalar threshold: let eta_K := min{rho_fac, (24*K)^(-1), 1}; then eta_K > 0, and every 0 <= eta <= eta_K satisfies eta <= rho_fac, 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
```

**E13 — `lem-routef-f2-positive-unital-compression`**

```text
imports validated registry lemma proofs/lem-routef-f2-positive-unital-compression — Route F F2 positive-unital compression: let K >= 1 be a dimension-independent constant, n >= 1, Q: l_inf^n -> l_inf^n row-stochastic, D: M_n -> C^n diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), J: C^n -> M_n diagonal inclusion, Q_C: C^n -> C^n the canonical complex-linear extension of Q, and Phi = J Q_C D, B a finite-dimensional unital C*-algebra, and Delta: B -> M_n, Upsilon: M_n -> B UCP maps; if 0 <= eta <= min{(24K)^{-1},1}, ||Delta Upsilon - Phi||_cb <= K*eta, ||Upsilon Delta - I_B||_cb <= K*eta, and ||Upsilon(Delta x Delta y) - xy|| <= K*eta*||x||*||y|| for all x,y in B, then B is commutative and there are k >= 1 and a unital *-isomorphism iota_C: C^k = l_inf^k(C) -> B such that D Delta iota_C maps R^k into R^n, iota_C^{-1} Upsilon J maps R^n into R^k, and the resulting restrictions and corestrictions A := (D Delta iota_C)|_{R^k}: l_inf^k -> l_inf^n and M := (iota_C^{-1} Upsilon J)|_{R^n}: l_inf^n -> l_inf^k are positive unital maps satisfying ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k.
```

**E14 — `lem-routef-f3-retract-defect`**

```text
imports validated registry lemma proofs/lem-routef-f3-retract-defect — Route F F3 retract defect: let K >= 1 be a dimension-independent constant, n,k >= 1, A: l_inf^k -> l_inf^n and M: l_inf^n -> l_inf^k positive unital maps, Q: l_inf^n -> l_inf^n row-stochastic, and eta >= 0 with 3K*eta < 1; if ||Q - AM||_{inf->inf} <= K*eta, ||QA - A||_{inf->inf} <= 2K*eta, and ||Ax||_inf >= (1-3K*eta)*||x||_inf for every x in l_inf^k, then ||MA - I_k||_{inf->inf} <= 3K*eta/(1-3K*eta).
```

**E15 — `lem-routef-prh-finish`**

```text
imports validated registry lemma proofs/lem-routef-prh-finish — Route F PRH finish: let A:l-infinity(k)->l-infinity(n) and M:l-infinity(n)->l-infinity(k) be positive unital maps and let Q be row-stochastic; if K >= 1, 0 <= eta <= min{(24*K)^(-1),1}, ||Q-AM||_{infinity->infinity} <= K*eta, and ||MA-I||_{infinity->infinity} <= 3*K*eta/(1-3*K*eta), then there is a stochastic idempotent E with ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
```

The candidate ROW8-FACTOR externals are intentionally absent. E6 is the public row-8 interface; E7
consumes exactly its `Upsilon'` output.

### 7.3 F0 assembly: `def-add` and exact `add-external`

Add these definitions exactly once:

1. `def-stochastic` <- `definitions/def-stochastic.md`
2. `def-almost-idempotent` <- `definitions/def-almost-idempotent.md`
3. `def-routef-raw-factor-setting` <- `definitions/def-routef-raw-factor-setting.md`
4. `def-ucp-map` <- `definitions/def-ucp-map.md`

The last two close vocabulary in the sole external. Add exactly one external after the strengthened
parent is T0:

```text
imports validated registry lemma proofs/lem-routef-k-ledger — Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
```

## 8. Landing manifest

This is the complete authorized surface for the future **landing** session after a fresh hostile audit
and explicit user ratification. It does not include the later proof workspaces or root rewire.

### 8.1 Registry and report sources

1. Replace `argument/lemmas/lem-routef-k-ledger.md` with section 2 verbatim.
2. Add `argument/lemmas/lem-routef-f0-assembly.md` from section 3 verbatim.
3. Add `lem-routef-f0-assembly` to `report/UNWIRED.md`; retain the existing
   `lem-routef-k-ledger` entry. Neither proposed `stated` row belongs on the paper track yet.
4. Reconcile stale K-ledger status prose in these existing report shards, without reproducing either
   proposed row as a theorem:
   - `report/sections/02_prh.tex`
   - `report/sections/36_routef_prh_finish.tex`
   - `report/sections/42_routef_f0_seam.tex`
   - `report/sections/43_routef_ai_ledger.tex`
   - `report/sections/44_routef_f2_f3.tex`

   The truthful landing-time phrase is “strengthened replacement `status: stated`, `af: none`; all 15
   direct inputs T0; pending its own af elevation.” Do not say `proved-mod-audit`, and do not say the
   Route-F chain or `op-classical` is closed.
5. Check `report/SHARD_CATALOG.md` and `report/PROVENANCE.md`. Their rows need no byte change if the five
   report shard headers/claim anchors remain unchanged; if the report gate reports drift, update them in
   the same atomic landing rather than deferring it.

### 8.2 Generated projections

Run the canonical generators and commit every changed generated byte:

```text
python3 scripts/check-defs.py --generate-index
python3 scripts/argument.py --generate
python3 scripts/gen-report-defs.py --generate --dag-anchors
python3 scripts/gen-report-dag.py --generate
python3 scripts/gen-report-stats.py --extract
```

Expected files are:

- `definitions/INDEX.md` (expected byte-identical because no definition changes; generator/check still
  mandatory);
- `argument/INDEX.md` and `argument/DAG.md`;
- `report/generated/defs/MANIFEST.md`, `_all.tex`, and the three `layer-*.tex` files (commit only if the
  DAG-anchor regeneration changes bytes);
- all six `report/generated/dag/*.tex` files;
- `report/generated/stats/README.md`, `body.tex`, `campaign-extract.json`, `headline.tex`, and
  `preamble.tex`.

The registry count rises by one. T0 remains 190. The strengthened parent moves from
`proved-mod-audit/none` to `stated/none`, and the new assembly row is `stated/none`; generated statistics
must reflect both facts without promotion.

### 8.3 Live strategy and session record

1. Add a new dated top-down proof sketch (do not edit v48) recording: the 15-dep decision; landing of the
   strengthened replacement and F0 assembly; guard release limited to the K-ledger; parent and assembly
   still non-T0; root rewire still LAST; and the cap-22 audit/factoring decision.
2. Run `python3 scripts/gen-current-pointer.py`, updating `docs/plans/CURRENT.md` to that new sketch.
3. Rewrite `HANDOFF.md` so the next action is strengthened-parent elevation or its ratified factoring,
   followed by F0-assembly elevation, with root rewire LAST.
4. Append the landing entry to `docs/worklog.md`.
5. Log the landing wave with `fr`; update `.frontier/log.jsonl` and, if the FRONTIER text changes,
   `.frontier/portfolio.json`. Banking language is forbidden at this stage because neither row is T0.
6. Update the governing bead state through `bd`; do not create a Markdown TODO.

No `op-classical` shard, root route, `proofs/` workspace, definition shard, old dated design/audit, or
historical sketch is edited by the landing. The only guard released is the K-ledger's DO-NOT-REWIRE
guard; root rewire remains separately forbidden until `lem-routef-f0-assembly` is T0.

### 8.4 Landing gates

After the exact landing edits, run:

```text
python3 scripts/argument.py --check
python3 scripts/check-provenance.py --check
sh scripts/check-all.sh
cd report && make
```

Then obtain reviewer-not-author sign-off and follow the repository's atomic commit/push protocol. This
design worker performs none of those mutations.

## 9. Elevation order and budgets

1. **Strengthened parent first.** Only after the landing is ratified, seed
   `proofs/lem-routef-k-ledger` at the exact section-2 contract and provision section 7.1--7.2 exactly
   once. Use target **17 nodes / 4 rounds / hard cap 22**. Before launch, the fresh hostile auditor must
   explicitly resolve section 6: defend the external-heavy build under cap 22 or ratify the proposed
   factoring. Any cap hit stops the run; it does not increase the cap.
2. **F0 assembly second.** Only after `lem-routef-k-ledger` is af-validated, exported, oracle-verified,
   mechanically banked T0, regenerated, gated, committed, and present at the checkout used for the new
   worktree, seed `proofs/lem-routef-f0-assembly`. Use target **2 nodes / depth 2 / 2 rounds / hard cap 6**.
3. **Root rewire last.** Only after F0 assembly is itself af-validated and banked may a separate,
   user-ratified session consider `op-classical`. This package does not specify or authorize that rewire.

Every elevation uses a fresh prover and separate fresh hostile verifier(s), bottom-up. Never resume an af
run across a registry ratification; recreate the worktree at the new HEAD.

## 10. Ranked hostile-audit attack list

1. **Packet existence versus telescope imports.** Verify that formation plus rows 5/6/8/9 really exports
   one existing packet before rows 10--14 are specialized. Reject any proof that treats a telescope's
   universal implication as packet existence.
2. **Same-datum drift across all 15 deps.** Track one outer `W_RF`, one root `(n,Q,eta,D,J,Q_C,Phi)`, one
   formation output `(B,v,S)`, and one serial `Delta',Delta,Upsilon',Upsilon`; attack every implicit
   reselection.
3. **Scalar-domain chain.** Recompute
   `eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr`, plus the separate inclusions into
   `rho_Delta'`, `rho_Delta`, `rho_Upsilon'`, `rho_Upsilon`, and all three telescope radii.
4. **Complexification seam.** Check the real stochastic `Q`, its canonical complex-linear extension
   `Q_C`, and `Phi=J Q_C D` are typed exactly as in both T0 F0 rows and F2. Attack any silent replacement
   of `Q_C` by `Q` on `C^n` or any change of `Phi` between formation and F2.
5. **15-versus-16 dependency decision.** Confirm the parent uses only row 8's public `Upsilon'` output
   and never needs the Choi/twirl component package. If it opens that package, stop and require a new
   direct-edge audit rather than silently citing a transitive lemma.
6. **Coefficient orientation and norm level.** Verify the two cb estimates have the correct compositions,
   the amplified multiplicativity estimate has `Upsilon_r(Delta_r X Delta_r Y)-XY`, and F2 consumes its
   `r=1` specialization with no norm or dimension factor.
7. **F2/F3/PRH identity threading.** Ensure F2's `A,M`, F3's `A,M`, and PRH's `A,M` are literally the
   same maps, and that the stochastic idempotent repairs the same input `Q`.
8. **Parent budget realism.** Attack the 17/22 monolith using the observed 1.5--3x family expansion.
   Either defend why 15 T0 external applications stay at most 22, or require the two-helper factoring in
   section 6.2. Never inflate cap 22.
9. **Sharpness overclaim.** Neither proposed contract asserts sharpness. Reject any argument that treats
   the Route-F upper bound as proving `ex-hume` or rewires the compound root without the separate
   sharpness discipline.
10. **Status laundering.** The W74F paper ledger was `proved-mod-audit`; this stronger contract was not.
    Verify both proposed shards land as `stated`, `af: none`, and that historical hostile verdicts are
    recorded only as superseded provenance.
11. **Guard-release scope.** Landing releases only the K-ledger's DO-NOT-REWIRE guard. Reject any edit to
    `op-classical`, any root route, or any claim that the guard release itself proves the replacement.
12. **Landing completeness.** Re-run the report/status/projection manifest. In particular, add F0
    assembly to `report/UNWIRED.md`, remove stale `proved-mod-audit` prose for K-ledger, refresh stats,
    supersede the live sketch, and leave no Rule-9 artifact stale.
