Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE — pending fresh hostile re-audit and user ratification.

# DESIGN v2 — cap-compliant strengthened `lem-routef-k-ledger` and F0 assembly

Date: 2026-08-08
Role: fresh independent design worker
Disposition: THREE-HELPER FACTORING DESIGNED; ALL TARGETS STRICTLY BELOW CAP AT 3x; FRESH RE-AUDIT REQUIRED

Nothing in this file is a proof, registry edit, status promotion, guard release, seed, or root rewire.
Every proposed row remains `stated`, `af: none` until separately landed, proved, and hostile-verified under
the repository protocol. `op-classical` remains open. This file supersedes the rejected v1 design as a
design proposal only; it does not alter the historical v1 design or its hostile audit.

## 1. Cleared material carried forward from v1

The hostile audit cleared the public contract seams, the original 15-dependency block, the scalar-domain
chain, packet existence, the 15-versus-16 decision, same-datum threading, dimension-freeness, F0-assembly
minimality, status honesty, historical provenance, and guard-release scope. Those items are frozen below.
The only public-interface change proposed by v2 is to append three helper ids to the parent's `deps:` line;
the original 15 ids remain byte-identical and in the same order.

### 1.1 Dependency decision: retain the binding 15-row block

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

### 1.2 Byte-frozen public contracts and original dependency block

The strengthened parent contract is carried forward byte-for-byte from v1:

```text
contract: Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
```

The cleared 15-id block is also carried forward byte-for-byte:

```text
deps: lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish
```

The F0-assembly contract is carried forward byte-for-byte from v1:

```text
contract: Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).
```

No cleared public contract text changes in v2. The original 15-dependency substring is unchanged; only
three auditable module edges are appended after it. The F0 `deps:` line remains exactly
`deps: lem-routef-k-ledger`.

## Repair of audit finding 1

> **FATAL — the parent has no credible cap-compliant elevation package (mandatory attack 9; design risk 8).** At `DESIGN-KLEDGER-STRENGTHENED.md` §6.1 lines 219–227 and §9 lines 471–475 the design itself computes an empirical 26–51-node build against hard cap 22 and does not defend an at-most-22 monolith, while the purported remedy at §6.2 lines 229–247 supplies no exact helper contracts, `defs:`, `deps:`, seeding strings, or same-datum quantifiers that can be audited and places both 6-node helpers exactly at cap 18 under the stipulated 3x expansion rather than below it; **consequence:** ratifying this package would authorize a strengthened parent whose prescribed proof is expected to trip the binding cap, with no verified fallback that could be landed without another design/audit/ratification cycle.

**Repair.** V2 makes the factoring primary and land-ready. It introduces three first-class registry rows:

1. `lem-routef-scalar-header-positivity` isolates the pre-input scalar logic;
2. `lem-routef-factor-map-packet` constructs one serial same-input map packet; and
3. `lem-routef-factor-estimate-packet` turns that exact packet into the three common-`K` estimates and
   the terminal threshold facts.

Their complete shards, exact roots, definitions, dependencies, external strings, and seeding packages
appear below. The factored parent consumes those three rows plus F2/F3/PRH. Its six-node design has an
honest `9--18` live expectation and hard cap `21`. The helpers have `6--12/14`, `8--15/18`, and
`8--15/18` expected/cap pairs. F0 assembly has `3--6/8`. Thus **every target's 3x endpoint is strictly
below its cap**, and every cap is at most 22. A cap hit remains a mandatory stop and classification; no
cap increase is authorized.

## Repair of audit finding 2

> **HIGH — the 17-node skeleton hoists packet-conditional scalar facts across the outer quantifiers (mandatory attacks 3 and 5; design risks 2 and 3).** The root requires `K >= 1` and `eta_K > 0` before `for every n,Q,eta` (`DESIGN-KLEDGER-STRENGTHENED.md` §2 line 43), but nodes 1.12–1.13 obtain those facts only after fixing the arbitrary input and the full packet (lines 188–200), exactly as the frozen row-13 and row-14 contracts require at `argument/lemmas/lem-routef-k-finiteness.md:4` and `argument/lemmas/lem-routef-threshold-minimum.md:4`, and line 201 then invalidly cites only the earlier choice of `W_RF` to hoist them; **consequence:** unless a separate pre-`forall` scalar-positivity proof (or an independently admissible dummy packet) is added, the skeleton proves the scalar claims only conditional on the existence of an admissible input and therefore does not discharge the displayed root or its advertised 17-node budget.

**Choice: option (a), pre-forall scalar positivity from the header alone.** This is the correct option.
In `def-routef-raw-factor-setting`, equations (1.1)--(1.8) define every scalar used by `K`, `rho_fac`,
and `eta_K` solely from the four real header fields and the fixed derived formulas. No setting datum `S`,
input Hilbert space, map, dimension, or packet occurs in those formulas. The formation contract supplies
one global `W_RF` before its `for every H,Phi,eta`, with `eta_A>0`, `epsilon_E>0`, finite `C_E`, and the
explicit finite positive `C_theta,C_A`. Elementary finite min/max/reciprocal arithmetic therefore proves
`K>=1`, `rho_fac>0`, and `eta_K>0` for that `W_RF` before any input is fixed.

The new scalar helper exposes exactly that pre-forall statement and the coordinate domain inclusions.
Rows 13/14 are not hoisted: they remain inside `lem-routef-factor-estimate-packet`, after the same packet
has been fixed, where their frozen quantifier prefixes apply literally. The public parent first chooses
the scalar helper's `W_RF,K,eta_K`, then opens `for every n,Q,eta`, then invokes the packet and estimate
helpers. The F0 specialization is unchanged: it receives the parent's genuinely pre-forall
`K>=1,eta_K>0`, so `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)` remain valid with no contract delta.

## Repair of audit finding 3

> **HIGH — the seeding package does not perform the mandated textbook-theorem inventory (mandatory attack 10).** `DESIGN-KLEDGER-STRENGTHENED.md` §7.1 lines 257–269 lists definitions and rules out only the two large structure/Stinespring externals, but the skeleton silently uses positivity and coordinate inequalities for finite minima/maxima and reciprocals (lines 188, 197–200), the canonical identifications `M_1(B)=B`, `Delta_1=Delta`, and `Upsilon_1=Upsilon` in the level-one specialization (line 199), and positivity of `sqrt(eta)` and `K+4*sqrt(2*K)` (lines 201, 208) without enumerating them or saying which are definitional/textbook-local; **consequence:** the exact provisioning audit demanded after the documented 37-node Wedderburn/Stinespring balloon has not occurred, so a fresh prover can again spend the hard-cap budget re-deriving undeclared facts.

**Repair.** Section 6 gives a 30-item census of every textbook, logical, order-arithmetic,
level-one, typing, and structural fact used by the five skeletons. Each item is classified and assigned
one of: L2 BSc/MSc common knowledge with no provisioning, an explicit in-skeleton node, a `def-add`, or a
validated registry external. In particular, the scalar min/max/reciprocal facts live explicitly in the
four-node scalar helper; the level-one identifications live explicitly in estimate-packet node 1.4; and
the square-root positivity facts live explicitly in the F0 specialization node. The finite-dimensional
C*-structure and Stinespring theorems are not re-derived: the construction is sealed behind the T0 row-8
and F2 public contracts. No new ground-truth external is required by this factoring.

## Repair of audit finding 4

> **HIGH — the landing manifest knowingly leaves live status prose stale (mandatory attack 12; design risk 12).** The report manifest at `DESIGN-KLEDGER-STRENGTHENED.md` §8.1 lines 390–409 names five shards but omits `report/sections/41_status_outlook.tex:97–111`, which still says `lem-thmainext-conditional` is `proved-mod-audit/none` and the MAIN/K-ledger rows are quarantined, and its directions do not explicitly repair the same already-false `lem-thmainext-conditional` status in the included `report/sections/36_routef_prh_finish.tex:124–127` and `report/sections/44_routef_f2_f3.tex:199–203`; **consequence:** the claimed “complete authorized surface” would violate Rule 9 even before considering the new K-ledger status change.

**Repair.** Section 7 enumerates every targeted stale prose locus found by the required repo-wide grep,
including the three named loci and six additional section loci, the stale `UNWIRED` status comment, the
status-outlook shard metadata/catalog row, and every generated projection class that must be regenerated.
The landing-time truth is explicit: `lem-thmainext-conditional` is `proved/validated` T0;
`lem-routef-k-ledger`, the three helpers, and F0 assembly are `stated/none`; the 15 original parent inputs
are T0; and neither the new rows nor `op-classical` is closed.

## 2. Land-ready registry shards

### 2.1 New helper: `lem-routef-scalar-header-positivity.md`

```markdown
---
id: lem-routef-scalar-header-positivity
kind: lemma
contract: Route F scalar-header positivity: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K is finite with K >= 1, rho_fac > 0, and eta_K > 0, these scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions, and eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr, rho_2 <= rho_Delta', rho_2 <= rho_Delta, rho_fac <= rho_DeltaUpsilon <= rho_Upsilon <= rho_Upsilon', rho_fac <= rho_mult, and rho_fac <= rho_UpsilonDelta.
defs: def-routef-raw-factor-setting
deps: lem-routef-raw-factor-setting-formation
status: stated
af: none
provenance: definitions/def-routef-raw-factor-setting.md equations (1.1)-(1.8) and the global scalar-header witness exported by lem-routef-raw-factor-setting-formation; factoring and pre-forall quantifier repair designed in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile audit and user ratification.
owner: A
workspace: proofs/lem-routef-scalar-header-positivity
---

**Status.** `stated`, `af: none`. This is a new elementary scalar-header proof obligation.
It promotes no part of the former paper ledger.

**Quantifier scope.** Select the global `W_RF` from
[[lem-routef-raw-factor-setting-formation]] and stop before entering that lemma's
`for every H,Phi,eta`. Equations (1.1)--(1.8) of
[[def-routef-raw-factor-setting]] contain no setting datum or input variable. Hence all
conclusions here are genuinely pre-input and apply to the same `W_RF` later used by the
packet family.

**Scalar route.** The formation header gives positive finite primitive data. Finite
sums, products, reciprocals, minima, and maxima then give positivity and finiteness of
all derived coefficients and radii. The coordinate inequalities of the displayed minima
give the domain chain. In particular `K` is a finite maximum containing `1`,
`rho_fac` is a positive finite minimum, and `eta_K` is a positive finite minimum.

**Designed af budget.** Four designed nodes; honest live expectation 6--12 under the
observed 1.5--3x expansion; at most 3 rounds; hard cap 14. The 3x endpoint 12 is strictly
below 14.
```

### 2.2 New helper: `lem-routef-factor-map-packet.md`

```markdown
---
id: lem-routef-factor-map-packet
kind: lemma
contract: Relative Route F factor-map packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then Phi is UCP with ||Phi^2-Phi||_cb <= eta, and there exist a finite-dimensional unital C*-algebra B, one def-routef-raw-factor-setting datum S over this same W_RF supplied by lem-routef-raw-factor-setting-formation for the same (H:=C^n,Phi,eta) whose B-field is B, CP maps Delta':B->M_n and Upsilon':M_n->B, and UCP maps Delta:B->M_n and Upsilon:M_n->B such that Delta' is supplied for (W_RF,S) by lem-routef-delta-prime-closeness, Delta is supplied from that same Delta' by lem-routef-delta-normalization-closeness, Upsilon' is supplied from that same (Delta',Delta) by lem-routef-upsilon-prime-closeness, and Upsilon is supplied from that same (Delta',Delta,Upsilon') by lem-routef-upsilon-normalization-closeness.
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-scalar-header-positivity; lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness
status: stated
af: none
provenance: The byte-frozen F0, formation, and rows 5/6/8/9 interfaces audited in AUDIT-KLEDGER-STRENGTHENED.md findings 5-9; first-class cap factoring designed in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile audit and user ratification.
owner: A
workspace: proofs/lem-routef-factor-map-packet
---

**Status.** `stated`, `af: none`. This helper only packages existing T0 interfaces and
promotes nothing at landing.

**Same-datum prefix.** The scalar helper selects one `W_RF` before every input. For one
arbitrary `n,Q,eta`, the F0 rows produce the exact same `Phi`; formation is instantiated
once at `H=C^n`; rows 5, 6, 8, and 9 are then applied serially. Every witness is explicitly
qualified by its provider, so no map or packet may be reselected.

**15-versus-16 boundary.** Row 8's public contract supplies the CP `Upsilon'` consumed by
row 9. This helper never opens the component package and has no dependency on
`lem-routef-upsilon-prime-component-construction`.

**Designed af budget.** Five designed nodes; honest live expectation 8--15 under the
observed 1.5--3x expansion; at most 4 rounds; hard cap 18. The 3x endpoint 15 is strictly
below 18.
```

### 2.3 New helper: `lem-routef-factor-estimate-packet.md`

```markdown
---
id: lem-routef-factor-estimate-packet
kind: lemma
contract: Relative Route F factor-estimate packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; for every same-datum packet (B,S,Delta',Delta,Upsilon',Upsilon) supplied for this (W_RF,n,Q,eta,D,J,Q_C,Phi) by lem-routef-factor-map-packet, ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||; moreover 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-scalar-header-positivity; lem-routef-factor-map-packet; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum
status: stated
af: none
provenance: The byte-frozen telescope and rows 13/14 interfaces audited in AUDIT-KLEDGER-STRENGTHENED.md findings 5-9; first-class cap factoring and same-packet projection designed in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile audit and user ratification.
owner: A
workspace: proofs/lem-routef-factor-estimate-packet
---

**Status.** `stated`, `af: none`. This helper projects the three telescope estimates and
the terminal arithmetic for one packet; it promotes nothing at landing.

**Packet-conditional rows stay packet-conditional.** Rows 13 and 14 are invoked only
after `lem-routef-factor-map-packet` has fixed the exact serial packet required by their
frozen prefixes. Their conclusions are not used to establish the earlier pre-forall
positivity; that role belongs solely to [[lem-routef-scalar-header-positivity]].

**Coefficient and level-one boundary.** The three telescope coefficients are coordinate
entries of the maximum defining `K`. The amplified multiplicativity conclusion is kept
in full. Its later F2 use is the explicit definitional specialization
`M_1(B)=B`, `Delta_1=Delta`, and `Upsilon_1=Upsilon` recorded in the skeleton and census.

**Designed af budget.** Five designed nodes; honest live expectation 8--15 under the
observed 1.5--3x expansion; at most 4 rounds; hard cap 18. The 3x endpoint 15 is strictly
below 18.
```

### 2.4 Complete replacement: `lem-routef-k-ledger.md`

The contract, `defs:`, status, owner, and workspace below are byte-identical to v1. The `deps:` line
retains the cleared 15-id substring byte-for-byte and appends the three helper ids. The provenance keeps
all cleared historical text verbatim and adds the mandatory v1-rejection/v2-repair record; this is an
administrative history correction, not a contract change. The body is updated only to describe the
repaired proof boundary and cap.

```markdown
---
id: lem-routef-k-ledger
kind: lemma
contract: Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
defs: def-routef-raw-factor-setting; def-stochastic; def-almost-idempotent; def-ucp-map
deps: lem-routef-f0-ucp-lift; lem-routef-f0-defect-identity; lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-upsilon-prime-closeness; lem-routef-upsilon-normalization-closeness; lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum; lem-routef-f2-positive-unital-compression; lem-routef-f3-retract-defect; lem-routef-prh-finish; lem-routef-scalar-header-positivity; lem-routef-factor-map-packet; lem-routef-factor-estimate-packet
status: stated
af: none
provenance: Strengthened replacement required by docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect-1.3 and corrected by AUDIT-F0-ASSEMBLY.md findings 1 and 3 (new fully quantified parent proof obligation, canonical Q_C typing); dependency/application rescope fixed by docs/plans/2026-08-05-LEDGER-SETTING-RESCOPE/DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-6.2 and hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md; row-8 factoring interface from docs/plans/2026-08-08-ROW8-FACTOR/DESIGN-ROW8-FACTOR.md and its landed T0 rows; exact landing package proposed by DESIGN-KLEDGER-STRENGTHENED.md, pending its required fresh hostile audit and user ratification. That v1 package was REJECTED by AUDIT-KLEDGER-STRENGTHENED.md findings 1-4; its cleared findings 5-14 and exact public contract are retained, while cap factoring, quantifier scope, provisioning census, and report manifest are repaired by DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile re-audit and user ratification. Supersedes the narrower W74F proved-mod-audit paper-ledger contract recorded in docs/plans/2026-07-24-W74F-wave2-artifacts/LEDGER-W74F-G-K.md, PROOF-W74F-H-STAGE1.md, VERDICT-W74F-G-KLEDGER.md, and VERDICT-W74F-H-STAGE1.md; that historical verdict does not transfer status to this strengthened statement.
owner: A
workspace: proofs/lem-routef-k-ledger
---

**Status.** `stated`, `af: none`. This fully quantified statement is a strengthened
replacement and a new proof obligation. It is not a wording repair of the W74F paper
ledger, and no part of the old `proved-mod-audit` status is inherited. Landing this shard
promotes no mathematics.

**Closed input seam.** The public contract retains the exact F0 typing and all 15 original
T0 dependencies. The three appended helpers are proof modules, not new mathematical
assumptions: the scalar helper fixes the formation witness and its universal positive
scalars before every input; the map-packet helper fixes one serial packet for each input;
and the estimate-packet helper exports the three common-`K` estimates for that same packet.

**Same-datum application order.** Apply the dependencies in the following order, without
reselecting any datum:

```text
scalar-header positivity (choose W_RF,K,rho_fac,eta_K before all inputs)
  -> for arbitrary n,Q,eta: factor-map packet (F0 -> formation -> rows 5/6/8/9)
  -> factor-estimate packet (rows 10/11/12 -> rows 13/14)
  -> level-one specialization -> F2 -> F3 -> PRH.
```

Row 8's public contract exports the `Upsilon'` consumed by row 9. The parent and helpers
do not use the internal componentwise package, so the two ROW8-FACTOR lemmas stay
transitive rather than direct imports.

**What the statement proves if validated.** The scalar helper supplies one universal
`K>=1` and `eta_K>0` before all inputs. For each admissible input the two packet helpers
produce one finite-dimensional `B`, one UCP pair `Delta,Upsilon`, and all three estimates.
F2 gives positive unital `A,M`, F3 gives the retract defect, and PRH returns `E` for the
same `Q` with constant `K+4*sqrt(2*K)`.

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

**Designed af budget.** Six designed nodes; honest live expectation 9--18 under the
observed 1.5--3x expansion; at most 4 rounds; hard cap 21. The 3x endpoint 18 is strictly
below 21. A proof worker must use the helper interfaces rather than reopening their
internals; a cap hit stops the run.
```

### 2.5 Complete new shard: `lem-routef-f0-assembly.md`

The following retains the complete v1 mathematical interface, with its public contract and sole
dependency unchanged. Its provenance preserves the cleared source history and appends the v1-rejection/
v2-repair record. The designed cap sentence is raised from 6 to 8 so the 3x expectation is strictly below,
rather than equal to, the cap.

```markdown
---
id: lem-routef-f0-assembly
kind: lemma
contract: Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).
defs: def-stochastic; def-almost-idempotent
deps: lem-routef-k-ledger
status: stated
af: none
provenance: docs/plans/2026-07-27-F0-ASSEMBLY-design/DESIGN-F0-ASSEMBLY.md sect-1.4 (assembly row and no-double-counting rule), with the canonical complexification typing correction required by AUDIT-F0-ASSEMBLY.md; strengthened-parent interface and exact constants from DESIGN-KLEDGER-STRENGTHENED.md, pending its required fresh hostile audit and user ratification. That v1 package was REJECTED by AUDIT-KLEDGER-STRENGTHENED.md findings 1-4; the byte-identical F0 contract and cleared minimality finding are retained in DESIGN-KLEDGER-STRENGTHENED-V2.md, pending fresh hostile re-audit and user ratification. This is an upper-bound assembly only; no sharpness claim is imported or promoted.
owner: A
workspace: proofs/lem-routef-f0-assembly
---

**Status.** `stated`, `af: none`. This is a proposed one-step specialization of the
strengthened [[lem-routef-k-ledger]] and promotes nothing at landing.

**Specialization.** Take `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)` from the parent. The parent
states that `eta_K>0`, `K>=1`, both are universal and dimension-free, and for every
admissible `n,Q,eta` returns the required stochastic idempotent for the same `Q`.
Elementary square-root positivity gives `C>0`.

**No double counting.** Registry `deps:` is exactly `lem-routef-k-ledger`. The parent
already consumes both F0 seam rows, formation, the factor-map packet, F2, F3, and PRH.
Repeating any of those edges here would misstate the module boundary.

**Sharpness and root guard.** This row proves only the upper-bound statement displayed in
its contract. It does not consume `ex-hume`, does not claim sharpness, and does not edit or
rewire `op-classical`. Root rewire remains the separate LAST step after this row is T0.

**Designed af budget.** Two designed nodes; honest live expectation 3--6 under the
observed 1.5--3x expansion; depth 2; at most 2 rounds; hard cap 8. The 3x endpoint 6 is
strictly below 8.
```

## 3. Contract identity and complete seam re-run

Neither cleared public contract changed. The parent contract in sections 1.2 and 2.4 is byte-identical
to the v1 contract; the F0 contract in sections 1.2 and 2.5 is byte-identical to the v1 contract. The
original 15-dependency substring is byte-identical; the only dependency delta is the append-only suffix

```text
; lem-routef-scalar-header-positivity; lem-routef-factor-map-packet; lem-routef-factor-estimate-packet
```

The v1 18-check seam table is therefore carried forward verbatim below. The helper projection column
records where each already-cleared seam now lives; it changes no producer or consumer contract.

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

The helper projection is exact:

| helper | cleared seam rows projected | exported boundary |
|---|---|---|
| `lem-routef-scalar-header-positivity` | scalar-header clauses of formation plus definitional parts of checks 3, 12, 13 | one pre-forall `W_RF,K,rho_fac,eta_K`, positivity, universality, domain inclusions |
| `lem-routef-factor-map-packet` | checks 1--8 | one same-input serial `(B,S,Delta',Delta,Upsilon',Upsilon)` packet |
| `lem-routef-factor-estimate-packet` | checks 9--13 | the three common-`K` estimates and terminal scalar guards for that same packet |
| factored parent | checks 14--18 | F2/F3/PRH on the same `Q,A,M` |

No helper weakens, strengthens, or rewrites a cleared dependency contract. Each helper is a new projection
lemma whose own statement must pass fresh hostile audit and af validation.

## 4. Complete af tree skeletons and budgets

Every statement below is the proposed node statement. Each root is exactly the corresponding registry
contract in section 2. Same-datum phrases are repeated deliberately.

### 4.1 `lem-routef-scalar-header-positivity` — 4 designed nodes

- **Node 1 — Root.** Route F scalar-header positivity: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K is finite with K >= 1, rho_fac > 0, and eta_K > 0, these scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions, and eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr, rho_2 <= rho_Delta', rho_2 <= rho_Delta, rho_fac <= rho_DeltaUpsilon <= rho_Upsilon <= rho_Upsilon', rho_fac <= rho_mult, and rho_fac <= rho_UpsilonDelta.
- **Node 1.1 — Pre-forall header selection and primitive positivity.** Select the one `W_RF` whose existence is asserted before the input quantifiers by `lem-routef-raw-factor-setting-formation`; do not instantiate its `for every H,Phi,eta` clause. For this header, `C_theta=12*(sqrt(2)-1)>0`, `C_A=20+(211/8)*C_theta>0`, `eta_A>0`, `epsilon_E>0`, `C_E` is finite, `bar-C_E=max{1,C_E}>=1`, `rho_theta=1/8>0`, and `rho_AI=eta_A>0`, and all are finite and universal.
- **Node 1.2 — Derived coefficient/radius induction and coordinate inclusions.** Reading (1.1)--(1.5) in displayed order, finite sums/products of the positive finite coefficients are positive and finite, reciprocals of their positive denominators are positive and finite, and every finite minimum of the displayed positive radii is positive and no larger than each coordinate. Consequently every coefficient through `C_Upsilon` and every radius through `rho_UpsilonDelta` is finite and positive, and `rho_2<=rho_T<=rho_id^corr`, `rho_2<=rho_Delta'`, `rho_2<=rho_Delta`, `rho_DeltaUpsilon<=rho_Upsilon<=rho_Upsilon'` hold.
- **Node 1.3 — K, rho_fac, eta_K, and quantifier assembly.** By (1.6), `K` is a finite maximum and `K>=1`; by (1.7), `rho_fac>0` and is no larger than `rho_2,rho_DeltaUpsilon,rho_mult,rho_UpsilonDelta`; by (1.8), `(24*K)^(-1)>0` and hence `eta_K>0` with `eta_K<=rho_fac`. These formula-derived scalars inherit universality and independence from the single header, so nodes 1.1--1.3 prove node 1 before any input is chosen.

Designed count: **4**. Honest live expectation: **6--12**. Maximum rounds: **3**. Hard cap:
**14**, with `12<14` at 3x.

### 4.2 `lem-routef-factor-map-packet` — 5 designed nodes

- **Node 1 — Root.** Relative Route F factor-map packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then Phi is UCP with ||Phi^2-Phi||_cb <= eta, and there exist a finite-dimensional unital C*-algebra B, one def-routef-raw-factor-setting datum S over this same W_RF supplied by lem-routef-raw-factor-setting-formation for the same (H:=C^n,Phi,eta) whose B-field is B, CP maps Delta':B->M_n and Upsilon':M_n->B, and UCP maps Delta:B->M_n and Upsilon:M_n->B such that Delta' is supplied for (W_RF,S) by lem-routef-delta-prime-closeness, Delta is supplied from that same Delta' by lem-routef-delta-normalization-closeness, Upsilon' is supplied from that same (Delta',Delta) by lem-routef-upsilon-prime-closeness, and Upsilon is supplied from that same (Delta',Delta,Upsilon') by lem-routef-upsilon-normalization-closeness.
- **Node 1.1 — F0 and admissible domain.** Fix the scalar helper's one `W_RF` before the arbitrary root input. For the root's exact `D,J,Q,Q_C,Phi`, the two F0 rows give that `Phi:M_n->M_n=B(C^n)->B(C^n)` is UCP and `||Phi^2-Phi||_cb=||Q^2-Q||<=eta`; `n>=1` makes `C^n` nonzero and finite-dimensional. The scalar helper gives `eta<=eta_K<=rho_fac<=rho_2<=rho_T<=rho_id^corr` and every construction radius needed below.
- **Node 1.2 — Same-input formation.** Apply formation once to `(H:=C^n,Phi,eta)` under the exact header fixed above. Obtain one finite-dimensional unital `B` and one datum `S` over this same `W_RF`; fix this `B,S` for all remaining nodes.
- **Node 1.3 — Delta pair.** Apply `lem-routef-delta-prime-closeness` to the fixed `(W_RF,S)` and then `lem-routef-delta-normalization-closeness` to the resulting same `Delta'`; fix the exported CP `Delta'` and UCP `Delta`.
- **Node 1.4 — Upsilon pair and packet assembly.** Apply `lem-routef-upsilon-prime-closeness` to the same `(W_RF,S,Delta',Delta)` and then `lem-routef-upsilon-normalization-closeness` to its public `Upsilon'` output; fix the exported CP `Upsilon'` and UCP `Upsilon`. Assemble exactly `(B,S,Delta',Delta,Upsilon',Upsilon)` without opening or reselecting any component witness.

Designed count: **5**. Honest live expectation: **8--15**. Maximum rounds: **4**. Hard cap:
**18**, with `15<18` at 3x.

### 4.3 `lem-routef-factor-estimate-packet` — 5 designed nodes

- **Node 1 — Root.** Relative Route F factor-estimate packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; for every same-datum packet (B,S,Delta',Delta,Upsilon',Upsilon) supplied for this (W_RF,n,Q,eta,D,J,Q_C,Phi) by lem-routef-factor-map-packet, ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||; moreover 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
- **Node 1.1 — Delta-Upsilon telescope on the fixed packet.** The scalar helper gives `eta<=rho_fac<=rho_DeltaUpsilon`; applying `lem-routef-delta-upsilon-telescope` to the exact packet gives `||Delta Upsilon-Phi||_cb <= (C_theta+C_Delta+2*C_Upsilon)*eta`.
- **Node 1.2 — Amplified multiplicative telescope on the fixed packet.** The scalar helper gives `eta<=rho_fac<=rho_mult`; applying `lem-routef-multiplicative-telescope` to the exact packet gives the stated estimate at every integer `r>=1` with coefficient `C_Upsilon+2*(C_2+C_theta+C_Delta)`.
- **Node 1.3 — Upsilon-Delta telescope on the fixed packet.** The scalar helper gives `eta<=rho_fac<=rho_UpsilonDelta`; applying `lem-routef-upsilon-delta-telescope` to the exact packet gives `||Upsilon Delta-I_B||_cb <= (C_Upsilon+2*C_Delta)*eta`.
- **Node 1.4 — Common K, terminal threshold, and assembly.** Now, and only now, apply the packet-conditional frozen rows `lem-routef-k-finiteness` and `lem-routef-threshold-minimum` to this same packet. Coordinate inequalities for the maximum (1.6), multiplied by `eta>=0`, turn nodes 1.1--1.3 into the three `K*eta` bounds. Row 14 supplies the displayed threshold and denominator guards. Record for the provisioning audit—but do not pretend the helper contract needs to export—the definitional level-one identities `M_1(B)=B`, `Delta_1=Delta`, `Upsilon_1=Upsilon`, `I_{M_1(B)}=I_B`, and the base norm/product identifications; the parent will use these locally.

Designed count: **5**. Honest live expectation: **8--15**. Maximum rounds: **4**. Hard cap:
**18**, with `15<18` at 3x.

### 4.4 Factored `lem-routef-k-ledger` — 6 designed nodes

- **Node 1 — Root.** Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
- **Node 1.1 — Pre-forall scalar witness.** Invoke `lem-routef-scalar-header-positivity` once and fix its `W_RF,K,rho_fac,eta_K` before the root's `for every n,Q,eta`. This gives exactly the root's universal, dimension-free `K>=1` and `eta_K>0` without using a packet-conditional row.
- **Node 1.2 — Same-input packet and estimates.** For the arbitrary root input, take one packet from `lem-routef-factor-map-packet` and apply `lem-routef-factor-estimate-packet` to that exact packet. Fix its `B,Delta,Upsilon`; this supplies the root's two cb estimates, full amplified multiplicativity estimate, F2 window, and F3/PRH scalar guards.
- **Node 1.3 — Explicit level-one F2 specialization.** Use the census-listed definitional level-one identities to specialize the estimate-packet root's amplified conclusion at `r=1`, with no change of maps, algebra, product, identity, or norm. These identities are local common knowledge, not an undeclared export from the helper. Apply `lem-routef-f2-positive-unital-compression` to the same `Q,D,J,Q_C,Phi,B,Delta,Upsilon,K,eta`, obtaining one `k>=1` and positive unital `A,M` with all three F2 estimates; fix these exact maps.
- **Node 1.4 — F3 on the same maps.** Since the estimate helper gives `3*K*eta<=1/8<1`, apply `lem-routef-f3-retract-defect` to the same `Q,K,eta,A,M`, obtaining `||MA-I_k||<=3*K*eta/(1-3*K*eta)`.
- **Node 1.5 — PRH and quantifier assembly.** Apply `lem-routef-prh-finish` to the same `Q,K,eta,A,M`; it returns a stochastic idempotent `E` for that same `Q` with the exact displayed bound. Assemble the arbitrary-input quantifiers under the `W_RF,K,eta_K` already fixed in node 1.1, proving node 1.

Designed count: **6**. Honest live expectation: **9--18**. Maximum rounds: **4**. Hard cap:
**21**, with `18<21` at 3x.

### 4.5 `lem-routef-f0-assembly` — 2 designed nodes

- **Node 1 — Root.** Route F F0 assembly: there are universal eta_0,C > 0, independent of n, such that for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_0 with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= C*sqrt(eta); for the universal K and eta_K supplied by lem-routef-k-ledger, one may take eta_0 := eta_K and C := K+4*sqrt(2*K).
- **Node 1.1 — Positive universal specialization.** Take the universal `K>=1` and `eta_K>0` of `lem-routef-k-ledger`, define `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)`. Since `K>=1`, `2*K>0`, `sqrt(2*K)>0`, and hence `C>0`; the formula preserves universality and dimension-independence. Specialize the parent to the root's arbitrary `n,Q,eta,D,J,Q_C,Phi`; its same-`Q` stochastic idempotent is the required `E` and its displayed bound is exactly `C*sqrt(eta)`.

Designed count: **2**. Honest live expectation: **3--6**. Depth: **2**. Maximum rounds: **2**.
Hard cap: **8**, with `6<8` at 3x.

### 4.6 Budget table and stop rule

| target | designed nodes | honest 1.5--3x live expectation | max rounds | hard cap | 3x strictly below cap? |
|---|---:|---:|---:|---:|---|
| `lem-routef-scalar-header-positivity` | 4 | 6--12 | 3 | 14 | yes, `12<14` |
| `lem-routef-factor-map-packet` | 5 | 8--15 | 4 | 18 | yes, `15<18` |
| `lem-routef-factor-estimate-packet` | 5 | 8--15 | 4 | 18 | yes, `15<18` |
| `lem-routef-k-ledger` | 6 | 9--18 | 4 | 21 | yes, `18<21` |
| `lem-routef-f0-assembly` | 2 | 3--6 | 2 | 8 | yes, `6<8` |

All hard caps are at most 22. No target is parked exactly at its cap under 3x. A live cap hit is not a
request for more headroom: stop and classify it as `MISSING fact`, `DAG dep`, or `genuine gap`. If the
parent begins reopening helper internals, that is a `DAG dep`/worker-discipline failure and requires a
fresh clean seed, not a monolithic continuation.

## 5. Exact seeding packages

No command in this section is authorized by this design. Before every future `def-add` or
`add-external`, preflight the clean workspace for duplicate names. If the seeded root bytes, definition
bytes, dependency bytes, or literal registry paths differ from this section, stop and re-audit. Never
resume a workspace across a registry ratification.

### 5.1 Exact `def-add` lists

Add the complete bytes of the listed existing definition shards exactly once, in the displayed order.

**Scalar-header helper**

1. `def-routef-raw-factor-setting` <- `definitions/def-routef-raw-factor-setting.md`
2. `def-ucp-map` <- `definitions/def-ucp-map.md`
3. `def-extended-epsilon-cstar-algebra` <- `definitions/def-extended-epsilon-cstar-algebra.md`
4. `def-extended-delta-inclusion` <- `definitions/def-extended-delta-inclusion.md`

The last three close vocabulary in the formation external; the helper contract itself declares only the
first definition.

**Map-packet helper, estimate-packet helper, and strengthened parent**

1. `def-routef-raw-factor-setting` <- `definitions/def-routef-raw-factor-setting.md`
2. `def-stochastic` <- `definitions/def-stochastic.md`
3. `def-almost-idempotent` <- `definitions/def-almost-idempotent.md`
4. `def-ucp-map` <- `definitions/def-ucp-map.md`
5. `def-extended-epsilon-cstar-algebra` <- `definitions/def-extended-epsilon-cstar-algebra.md`
6. `def-extended-delta-inclusion` <- `definitions/def-extended-delta-inclusion.md`

**F0 assembly**

1. `def-stochastic` <- `definitions/def-stochastic.md`
2. `def-almost-idempotent` <- `definitions/def-almost-idempotent.md`
3. `def-routef-raw-factor-setting` <- `definitions/def-routef-raw-factor-setting.md`
4. `def-ucp-map` <- `definitions/def-ucp-map.md`

No new definition is proposed. The two large facts implicated in the 37-node ROW8 balloon are not local
inputs here: finite-dimensional C*-structure and Stinespring construction remain sealed behind already
validated public rows, as itemized in the census.

### 5.2 Exact external-string dictionary: frozen original inputs

The following 15 strings are carried forward byte-for-byte from v1. Each uses the literal
`proofs/<dep-id>` path and the dependency's byte-verbatim current contract.

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

### 5.3 Exact external-string dictionary: new helper interfaces

These strings must be generated only after the corresponding helper is af-validated and banked. The
text after the em dash is the exact contract from section 2.

**H1 — `lem-routef-scalar-header-positivity`**

```text
imports validated registry lemma proofs/lem-routef-scalar-header-positivity — Route F scalar-header positivity: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K is finite with K >= 1, rho_fac > 0, and eta_K > 0, these scalars are universal and independent of H, Phi, eta, n, amplification level, simple-block count, and block dimensions, and eta_K <= rho_fac <= rho_2 <= rho_T <= rho_id^corr, rho_2 <= rho_Delta', rho_2 <= rho_Delta, rho_fac <= rho_DeltaUpsilon <= rho_Upsilon <= rho_Upsilon', rho_fac <= rho_mult, and rho_fac <= rho_UpsilonDelta.
```

**H2 — `lem-routef-factor-map-packet`**

```text
imports validated registry lemma proofs/lem-routef-factor-map-packet — Relative Route F factor-map packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then Phi is UCP with ||Phi^2-Phi||_cb <= eta, and there exist a finite-dimensional unital C*-algebra B, one def-routef-raw-factor-setting datum S over this same W_RF supplied by lem-routef-raw-factor-setting-formation for the same (H:=C^n,Phi,eta) whose B-field is B, CP maps Delta':B->M_n and Upsilon':M_n->B, and UCP maps Delta:B->M_n and Upsilon:M_n->B such that Delta' is supplied for (W_RF,S) by lem-routef-delta-prime-closeness, Delta is supplied from that same Delta' by lem-routef-delta-normalization-closeness, Upsilon' is supplied from that same (Delta',Delta) by lem-routef-upsilon-prime-closeness, and Upsilon is supplied from that same (Delta',Delta,Upsilon') by lem-routef-upsilon-normalization-closeness.
```

**H3 — `lem-routef-factor-estimate-packet`**

```text
imports validated registry lemma proofs/lem-routef-factor-estimate-packet — Relative Route F factor-estimate packet: after first fixing one global witness package W_RF supplied by lem-routef-scalar-header-positivity from lem-routef-raw-factor-setting-formation, writing K, rho_fac, and eta_K for its scalars (1.6)-(1.8), for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; for every same-datum packet (B,S,Delta',Delta,Upsilon',Upsilon) supplied for this (W_RF,n,Q,eta,D,J,Q_C,Phi) by lem-routef-factor-map-packet, ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||; moreover 0 <= eta <= min{(24*K)^(-1),1}, 3*K*eta <= 1/8 < 1, and 3*K*eta/(1-3*K*eta) <= 4*K*eta <= 1/6 < 1/2.
```

**P — strengthened `lem-routef-k-ledger`**

```text
imports validated registry lemma proofs/lem-routef-k-ledger — Relative Route F factorization-and-finish ledger: there exists one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation such that, writing K for its scalar (1.6), rho_fac for its scalar (1.7), and eta_K := min{rho_fac, (24*K)^(-1), 1} for its scalar (1.8), K >= 1 and eta_K > 0 are universal and independent of n, amplification level, simple-block count, and block dimensions, and for every n >= 1, every row-stochastic Q: l_inf^n -> l_inf^n, and every 0 <= eta <= eta_K with ||Q^2-Q||_{infinity->infinity} <= eta, let D: M_n -> C^n be diagonal extraction onto the complex diagonal algebra C^n = l_inf^n(C), let J: C^n -> M_n be the diagonal inclusion, let Q_C: C^n -> C^n be the canonical complex-linear extension of Q, and put Phi := J Q_C D; then there exist a finite-dimensional unital C*-algebra B and UCP maps Delta: B -> M_n and Upsilon: M_n -> B such that ||Delta Upsilon-Phi||_cb <= K*eta, ||Upsilon Delta-I_B||_cb <= K*eta, and for every integer r >= 1 and all X,Y in M_r(B), ||Upsilon_r(Delta_r X Delta_r Y)-XY|| <= K*eta*||X||*||Y||, and the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity} <= (K+4*sqrt(2*K))*sqrt(eta).
```

### 5.4 Exact per-target `add-external` lists

Add only the strings named below, in the displayed order, after every referenced helper target is T0.
The declared dependency list of each shard and its registry-external list must agree exactly; the parent
therefore retains all original imports even though its designed proof is intentionally routed through the
helpers.

- `lem-routef-scalar-header-positivity`: **E3**.
- `lem-routef-factor-map-packet`: **H1, E1, E2, E3, E4, E5, E6, E7**.
- `lem-routef-factor-estimate-packet`: **H1, H2, E8, E9, E10, E11, E12**.
- `lem-routef-k-ledger`: **E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12,
  E13, E14, E15, H1, H2, H3**. This is exactly the 15 cleared ids followed by the three appended ids.
- `lem-routef-f0-assembly`: **P**.

No target receives `lem-routef-upsilon-prime-component-construction` or
`lem-routef-upsilon-prime-left-inverse` directly. E6 is the public row-8 interface. No target receives
`GT-kitaev-fd-cstar-structure` or `GT-kitaev-canonical-stinespring`: those theorems are sealed behind E6
and E13 and are not opened by any designed node.

## 6. Textbook/definitional fact census — 30 items

This census is part of the seeding package. “L2 exemption” means BSc/MSc common knowledge under
`CLAUDE.md` L2 and therefore no definition shard or ground-truth external is added. “In-skeleton” means
the fact is named explicitly in the indicated node so a fresh prover is not invited to create an
undeclared theorem branch. “Validated external” means the fact is consumed only through the exact public
contract listed in section 5; its proof is not reopened.

| # | fact used by the skeleton | classification | exact provisioning decision |
|---:|---|---|---|
| 1 | Existential elimination: select the `W_RF` exported before formation's input quantifiers. | elementary first-order logic, L2 exemption | No external; explicit in scalar node 1.1. |
| 2 | Provider-qualified serial choice preserves witness identity: after fixing `S`, choose the particular `Delta'`, then its `Delta`, then their `Upsilon'`, then its `Upsilon`. | elementary logic, L2 exemption | No external; explicit in map-packet nodes 1.2--1.4. |
| 3 | Universal instantiation and final quantifier assembly do not move an input-dependent witness outside its scope. | elementary logic, L2 exemption | No external; explicit in scalar node 1.3 and parent nodes 1.1/1.5. |
| 4 | `n>=1` implies `C^n` is a nonzero finite-dimensional complex Hilbert space. | BSc linear algebra, L2 exemption | No external; explicit in map-packet node 1.1. |
| 5 | The canonical identification `B(C^n)=M_n` used to instantiate formation at `H=C^n`. | BSc finite-dimensional operator theory, L2 exemption | No external; explicit in map-packet node 1.1. |
| 6 | Equality substitution and order transitivity: the F0 defect identity plus the stochastic antecedent yields `||Phi^2-Phi||_cb<=eta`; chains may be concatenated. | elementary logic/order, L2 exemption | No external; explicit in map-packet node 1.1. Cosmetic `inf`/`infinity` spelling is the registry convention, not a theorem. |
| 7 | `sqrt(2)>1`, positive rational constants remain positive, and hence the explicit `C_theta,C_A,rho_theta` are positive finite reals. | BSc real analysis/arithmetic, L2 exemption | No external; explicit in scalar node 1.1. |
| 8 | Finite sums and products of finite real scalars are finite. | BSc real arithmetic, L2 exemption | No external; explicit in scalar node 1.2. |
| 9 | A sum or product of positive real scalars is positive. | BSc ordered-field arithmetic, L2 exemption | No external; explicit in scalar node 1.2. |
| 10 | The reciprocal of a positive finite real scalar is positive and finite. | BSc ordered-field arithmetic, L2 exemption | No external; explicit in scalar nodes 1.2/1.3. |
| 11 | A finite minimum of positive real scalars is positive. | BSc real analysis, L2 exemption | No external; explicit in scalar nodes 1.2/1.3. |
| 12 | A finite minimum is no larger than each of its coordinates. | BSc order theory, L2 exemption | No external; explicit in scalar node 1.2 and the exported scalar-helper contract. |
| 13 | A finite maximum of finite real scalars is finite. | BSc real analysis, L2 exemption | No external; explicit in scalar node 1.3. |
| 14 | A finite maximum is at least every coordinate; because `1` is a coordinate of (1.6), `K>=1`, and each telescope coefficient is `<=K`. | BSc order theory, L2 exemption | No external; explicit in scalar node 1.3 and estimate node 1.4. |
| 15 | Recursive substitution through displayed definitions (1.1)--(1.8) is legitimate in their stated order. | definitional unfolding | `def-add def-routef-raw-factor-setting`; explicit induction in scalar node 1.2. |
| 16 | Finite formulas in universal header scalars remain universal and independent of all excluded dimensions/data. | elementary dependency bookkeeping, L2 exemption | No external; explicit in scalar node 1.3. |
| 17 | From `eta<=eta_K` and the exported coordinate chain, `eta` lies in every formation/construction/telescope radius actually invoked. | elementary order transitivity, L2 exemption | No external; explicit in map node 1.1 and estimate nodes 1.1--1.3. |
| 18 | If `a<=b` and `eta>=0`, then `a*eta<=b*eta`; this changes each telescope coefficient to `K`. | BSc ordered-field arithmetic, L2 exemption | No external; explicit in estimate node 1.4. |
| 19 | The rational inequalities `1/8<1` and `1/6<1/2` are exact. | elementary arithmetic, L2 exemption | No external; the full chain is also supplied verbatim by E12 and repeated in estimate node 1.4. |
| 20 | `3*K*eta<=1/8<1` implies `1-3*K*eta>0`, so the displayed reciprocal denominator is legal. | BSc ordered-field arithmetic, L2 exemption | No external; the conclusion and stronger quotient estimate are supplied by E12; the strict guard is explicitly passed in parent node 1.4. |
| 21 | Canonical level-one identification `M_1(B)=B`. | definitional matrix-amplification convention | No new definition/external; explicit in estimate node 1.4 and parent node 1.3. |
| 22 | At level one, `Delta_1=Delta`, `Upsilon_1=Upsilon`, and `I_{M_1(B)}=I_B`. | definitional amplification convention in `def-routef-raw-factor-setting` | `def-add def-routef-raw-factor-setting`; explicit in estimate node 1.4. |
| 23 | The level-one matrix norm, product, and elements agree with the base norm, product, and elements of `B`. | definitional matrix-algebra convention | No new external; explicit in estimate node 1.4. |
| 24 | A statement quantified over every integer `r>=1` may be specialized at `r=1`. | elementary logic, L2 exemption | No external; explicit in parent node 1.3. |
| 25 | For `eta>=0`, `sqrt(eta)` exists and is nonnegative. | BSc real analysis, L2 exemption | No external; used locally in the parent conclusion already supplied by E15 and recorded in F0 node 1.1. |
| 26 | From `K>=1`, `2*K>0`, `sqrt(2*K)>0`, and `K+4*sqrt(2*K)>0`. | BSc real analysis/arithmetic, L2 exemption | No external; explicit in F0 node 1.1. |
| 27 | Defining `eta_0:=eta_K` and `C:=K+4*sqrt(2*K)` preserves universality and dimension-independence. | elementary dependency bookkeeping, L2 exemption | No external; explicit in F0 node 1.1. |
| 28 | The F0 map is UCP, its cb defect equals the stochastic defect, formation returns a finite-dimensional `B,S`, and rows 5/6/8/9 return actual CP/UCP maps of the displayed types. | nontrivial mathematical interfaces | Provisioned only by validated externals E1--E7 plus the listed `def-add`s; map-packet nodes invoke them as black boxes. |
| 29 | Finite-dimensional C*-algebra decomposition, Choi/Stinespring realization, nonzero multiplicity repair, and component CP construction underlying row 8. | nontrivial theorems; not L2-local for this workspace | **Do not provision or rederive here.** They are sealed behind validated E6; `GT-kitaev-fd-cstar-structure` and `GT-kitaev-canonical-stinespring` are intentionally absent. Opening them is a cap-stop/interface violation. |
| 30 | F2's commutativity/coordinate construction, F3's lower-modulus calculation, and PRH's stochastic-idempotent/square-root conclusion. | nontrivial theorems | Provisioned only by validated externals E13, E14, E15. The parent passes exact hypotheses and never re-proves their internals. |

**Census verdict.** Thirty facts/classes are accounted for: 23 elementary L2 facts, 4 definitional
facts, and 3 nontrivial interface/theorem classes, with overlaps resolved by the provisioning
column. There is no silently invoked theorem and no new source acquisition. A verifier who finds an
unlisted non-elementary fact must reject the package as `MISSING fact`, not allow an in-tree re-derivation.

## 7. Corrected complete landing manifest

This is the complete authorized surface for a future landing session **only after** fresh hostile re-audit
and explicit user ratification. It includes no `proofs/` mutations and no root rewire.

### 7.1 Registry landing

1. Add `argument/lemmas/lem-routef-scalar-header-positivity.md` from section 2.1 verbatim.
2. Add `argument/lemmas/lem-routef-factor-map-packet.md` from section 2.2 verbatim.
3. Add `argument/lemmas/lem-routef-factor-estimate-packet.md` from section 2.3 verbatim.
4. Replace `argument/lemmas/lem-routef-k-ledger.md` with section 2.4 verbatim. Verify that its contract is
   byte-identical to v1 and its original 15-id dependency substring is byte-identical; only the three
   helper ids are appended.
5. Add `argument/lemmas/lem-routef-f0-assembly.md` from section 2.5 verbatim.
6. Add all four new ids to `report/UNWIRED.md`; retain the existing `lem-routef-k-ledger` entry. None of
   these five `stated/none` rows belongs on the paper track.

The registry row count rises from 367 to **371**. T0 remains **190**. The old parent moves from
`proved-mod-audit/none` to `stated/none`; the three helpers and F0 assembly are new `stated/none` rows.
No definition changes, proof workspaces, status promotions, or mathematical banking occur at landing.

### 7.2 Exhaustive stale-report prose repair

The required sweep used case-insensitive matches for `thmainext`, `k-ledger`/`k ledger`,
`proved-mod-audit`, `af: none`, and `quarantin` across `report/**/*.tex` and `report/**/*.md`. The following
are every live prose/metadata locus whose statement is stale now or would become stale at this landing:

| locus | stale statement | required landing-time statement |
|---|---|---|
| `report/sections/00_overview.tex:118-119` | `lem-thmainext-conditional` is `proved-mod-audit/none`; assembly quarantined | Say it is `proved/validated` T0 and not reproduced here; identify the strengthened K-ledger plus its three helpers and F0 assembly as `stated/none`; route/root remain open. |
| `report/sections/02_prh.tex:123` | Calls both `lem-routef-prh-finish` and `lem-routef-k-ledger` non-rigorous | Say PRH finish is `proved/validated` T0 while the strengthened K-ledger is `stated/none`. |
| `report/sections/16_compcb_single_compression_transfer.tex:105-106` | `lem-thmainext-conditional` remains `proved-mod-audit/none` and has no registry consumers | Say it is `proved/validated` T0; re-check and state its current consumer relation rather than retaining “no consumers.” |
| `report/sections/35_extcb.tex:201-203` | Assembly carrier is `proved-mod-audit/none`, open, not reproduced | Say `lem-thmainext-conditional` is T0 and not reproduced; the remaining Route-F gap is the new stated K-ledger/helper/F0 package, not MAIN quarantine. |
| `report/sections/36_routef_prh_finish.tex:124-127` | **Named audit locus:** K-ledger and `lem-thmainext-conditional` are both `proved-mod-audit/none` | Say `lem-thmainext-conditional` is T0 and the strengthened K-ledger is `stated/none`; preserve the open-root warning. |
| `report/sections/41_status_outlook.tex:3-5` and corresponding `report/SHARD_CATALOG.md:425` | Shard metadata says the live route stops at a quarantined assembly interface | Update the summary/keywords and catalog projection to the T0 MAIN state and the stated K-ledger/helper/F0 frontier. |
| `report/sections/41_status_outlook.tex:97-111` | **Named audit locus:** `lem-thmainext-conditional` is `proved-mod-audit/none`; MAIN/K-ledger rows quarantined | Rewrite the whole paragraph: MAIN and `lem-thmainext-conditional` are T0; all 15 original K-ledger inputs are T0; the strengthened parent, three helpers, and F0 assembly are `stated/none`; `op-classical` remains open. |
| `report/sections/42_routef_f0_seam.tex:143-145` | K-ledger is `proved-mod-audit/none` | Say strengthened replacement `stated/none`, all 15 original inputs T0, three helper projections also stated pending elevation. |
| `report/sections/43_routef_ai_ledger.tex:256-258` | K-ledger is `proved-mod-audit/none` | Same truthful strengthened-parent/helper status; no unconditional bound yet. |
| `report/sections/44_routef_f2_f3.tex:199-203` | **Named audit locus:** K-ledger is `proved-mod-audit/none`; `lem-thmainext-conditional` grouped with the open gap | Say MAIN carrier T0 and strengthened K-ledger/helpers/F0 `stated/none`; preserve the conclusion that Route F and `op-classical` are open. |
| `report/UNWIRED.md:335-336` | Comment says the ledger-domain rows remain `stated/none` until elevation | Replace with a historical/current comment reflecting that the queue is T0; keep off-paper whitelist entries as appropriate and add the four new stated ids. |

The sweep also found generated status projections that must not be hand-edited:

- `report/generated/dag/index.tex` (K-ledger status row),
- `report/generated/dag/overview.tex` and `phases.tex` (K-ledger glyph/status),
- `report/generated/dag/legend.tex:38-39` (live route annotations sourced from the current sketch), and
- `report/generated/stats/body.tex` (status/T0 counts and the T0 row for `lem-thmainext-conditional`).

Regenerate all of them under section 7.3 after the registry, prose, and live-sketch edits. Generic
rigour-ladder prose in `report/RESCOPE-NOTE.md:20`, `report/SHARD_CATALOG.md:410`,
`report/sections/00_overview.tex:92`, and the generated legend's definitions of `proved-mod-audit` is not
stale and must not be rewritten. Unrelated uses of “quarantined” for signed negativity or numerical work
are also out of scope. Legitimate `proved-mod-audit` rows in the generated DAG/index remain generated
truth and are not blanket-replaced.

Synchronize `report/SHARD_CATALOG.md` byte-for-byte with every changed shard header (the status-outlook
row must change). Check `report/README.md` and `report/PROVENANCE.md` in the same landing: no report shard
is added and no proposed non-rigorous row is reproduced, so both are expected to remain byte-identical;
if either report gate detects a changed order, anchor, source, or status projection, reconcile it in the
same atomic landing rather than deferring it.

### 7.3 Generated projections

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
- all six `report/generated/dag/*.tex` files; and
- `report/generated/stats/README.md`, `body.tex`, `campaign-extract.json`, `headline.tex`, and
  `preamble.tex`.

The generated statistics must show 371 registry rows, T0 still 190, the strengthened parent at
`stated/none`, and the four new rows at `stated/none`.

### 7.4 Live strategy, session record, and guard scope

1. Add a new dated top-down proof sketch (do not edit the previous dated sketch) recording: the retained
   15-versus-16 decision; the three-helper factoring; option (a) pre-forall scalar repair; the exact
   budgets; landing of five non-T0 rows; and the elevation order in section 8.
2. Run `python3 scripts/gen-current-pointer.py`, updating `docs/plans/CURRENT.md` to that new sketch before
   generating the report DAG annotations.
3. Rewrite `HANDOFF.md` so the next action is scalar-helper elevation, then map packet, estimate packet,
   strengthened parent, and F0 assembly, with root rewire LAST.
4. Append the landing entry to `docs/worklog.md`.
5. Log the landing wave with `fr`; update `.frontier/log.jsonl` and, only if the FRONTIER changes,
   `.frontier/portfolio.json`. Banking language is forbidden because no new row is T0.
6. Update the governing bead through `bd`; create no Markdown TODO.

No `op-classical` shard, root route, `proofs/` workspace, definition shard, old dated design/audit, or
historical sketch is edited by landing. The only guard released is the K-ledger's landing guard. Root
rewire remains forbidden until `lem-routef-f0-assembly` is T0.

### 7.5 Landing gates

After the exact future landing edits, run:

```text
python3 scripts/argument.py --check
python3 scripts/check-provenance.py --check
sh scripts/check-all.sh
cd report && make
```

Then obtain reviewer-not-author sign-off and follow the repository's atomic commit/push protocol. This
design worker performs none of those mutations.

## 8. Elevation order

Every stage uses a fresh prover and separate fresh hostile verifier(s), bottom-up. Every helper must be
af-validated, oracle-verified, mechanically banked, regenerated, gated, committed, and present at the
checkout used to seed its consumer. Never resume across a registry ratification.

1. **Scalar header first.** Seed `lem-routef-scalar-header-positivity` with section 5.1 and E3. Use
   **4 designed / 6--12 expected / 3 rounds / cap 14**.
2. **Map packet second.** Only after stage 1 is T0, seed `lem-routef-factor-map-packet` with H1 and
   E1--E7 in the exact section-5.4 order. Use **5 / 8--15 / 4 rounds / cap 18**.
3. **Estimate packet third.** Only after stage 2 is T0, seed
   `lem-routef-factor-estimate-packet` with H1, H2, and E8--E12. Use
   **5 / 8--15 / 4 rounds / cap 18**.
4. **Strengthened parent fourth.** Only after all helpers are T0, cleanly seed
   `lem-routef-k-ledger` at the byte-frozen public contract, attach all 18 declared externals, and direct
   the prover to use H1/H2/H3 plus E13--E15 without reopening helper internals. Use
   **6 / 9--18 / 4 rounds / cap 21**.
5. **F0 assembly fifth.** Only after the parent is T0, seed `lem-routef-f0-assembly` with P. Use
   **2 / 3--6 / 2 rounds / cap 8**.
6. **Root rewire LAST.** Only after F0 assembly is T0 may a separate user-ratified package consider
   `op-classical`. This design specifies and authorizes no root edit.

Any target that reaches its cap stops immediately. Repeated bookkeeping/ordering thrash on an otherwise
small design calls for a fresh-prover clean reseed; a missing theorem calls for exact provisioning; a
helper-internal branch in the parent calls for factoring discipline. None authorizes a cap increase.

## 9. Ranked risks for fresh hostile re-audit

1. **NEW — scalar-helper existential projection.** Attack whether formation's syntax truly permits
   selecting `W_RF` and proving its header formulas before instantiating `H,Phi,eta`. Reject any proof
   that uses rows 13/14 or an implicit dummy packet to recover pre-forall positivity.
2. **NEW — helper-provider contract semantics.** Check that “supplied by
   `lem-routef-scalar-header-positivity` from formation” fixes literally the same `W_RF` accepted by every
   family row, and that the map/estimate packet tuple is a sufficiently typed public interface rather
   than documentary shorthand.
3. **Primitive scalar signs.** Recompute every step of (1.1)--(1.8), especially that no sign assumption
   on `C_E` is needed because `bar-C_E=max{1,C_E}`, every reciprocal denominator is positive, and all
   minima used in the exported chain contain only positive finite coordinates.
4. **Parent dependency redundancy.** The public parent keeps all 15 cleared edges and appends three
   helpers. Verify the DAG is acyclic, status propagation is legal, and the exact seeding attaches all 18
   declared dependencies even though the proof uses the helper projections. Reject deletion or reordering
   of the cleared 15-id substring.
5. **Cap discipline under redundant imports.** A fresh parent prover may ignore helpers and reopen 15
   externals. The prompt and hostile review must enforce the six-node module-level skeleton. The
   `9--18/21` budget assumes interface use, not monolithic reconstruction.
6. **Map-packet existence and same-datum identity.** Verify F0 plus formation plus rows 5/6/8/9 actually
   produces the exact serial packet, with no telescope treated as an existence theorem and no map
   reselected.
7. **15-versus-16 boundary.** Confirm no helper opens the Choi/twirl component package. If it does, stop;
   do not silently add the component-construction row.
8. **Estimate-packet scope.** Rows 13/14 must be invoked only after the map packet is fixed. Check each
   telescope radius, coefficient orientation, cb norm, amplification quantifier, and the explicit
   level-one identities.
9. **F2/F3/PRH threading.** Track one `Q,D,J,Q_C,Phi,B,Delta,Upsilon`, then one `A,M`, through the three
   validated finish rows. Reject any new witness or a change between real and complex pictures.
10. **Textbook census completeness.** Re-run the 30-item table against the actual worker tree. Any new
    Wedderburn, Stinespring, CP, square-root, min/max, or amplification subtheorem is a missing-provision
    finding, not harmless elaboration.
11. **Status and history.** All five landed targets must be `stated/none`; W74F remains superseded
    `proved-mod-audit` history only. No audit verdict or T0 dependency status transfers to a helper or
    parent.
12. **Report sweep completeness.** Verify all eleven live prose/metadata rows in section 7.2, the named
    audit loci, generated projections, and current-sketch-derived DAG annotations. Reject a landing that
    leaves `lem-thmainext-conditional` described as non-T0 or the K-ledger described as
    `proved-mod-audit`.
13. **Guard and sharpness scope.** Landing and all five elevations prove only the Route-F upper-bound
    package. They neither import `ex-hume` nor authorize `op-classical` edits. Root composition and
    sharpness remain separate.

**Fresh-audit decision requested.** Ratify only if the auditor confirms: (i) option (a) is a valid
pre-forall projection of formation's scalar header; (ii) all three helper contracts are adequately typed
and same-datum; (iii) each 3x endpoint is strictly below its declared cap; (iv) the 30-item census is
complete; and (v) the report manifest exhausts every stale status locus. Otherwise reject and return an
exact contract, dependency, provisioning, or locus correction; do not authorize partial landing.
