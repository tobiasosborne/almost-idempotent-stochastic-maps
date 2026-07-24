# DESIGN v2 — repaired aism-fudw Route F decomposition

Date: 2026-07-24  
Role: fresh repair architect  
Scope: design only; no registry, definition, proof, report, reference, tracker,
frontier, or Git changes

## 0. Disposition table

The finding ids below are local to
`VERDICT-FUDW-DECOMP.md`. “Closed in design” means only that v2 supplies a
closed proposed contract and DAG placement. It is not a proof, a review, or an
L0 promotion.

| finding | severity | v2 disposition | location |
|---|---|---|---|
| 1.1 Missing COMP-CB subtree | BLOCKER | Closed in design: adds the five verdict-specified COMP-CB rows and all four H-CB plus one Stage-1 dependency replacements. | §§2.1, 3.1 |
| 1.2 MAIN-CB structural assembly absent | BLOCKER | Closed as an explicit five-node `stated` subtree: Stage-1 maximality, equivalence-class partition, Stage-2 walk, Stage-3 recombination, and final structural assembly. Each node is projected separately inside the envelope. | §§2.4, 3.3 |
| 1.3 Stochastic-retract interface absent | BLOCKER | Not invented. Two Phase-5 ids are reserved, but no seedable contract is asserted because the permitted packets do not contain a safe closed F2/F3 hypothesis block. Ledger rewiring is blocked. | §§2.6, 3.4, R25–R26 |
| 2.1 Top-cohomology boundary error | MAJOR | Uses the verdict’s exact “without boundary” replacement. | §2.4 |
| 2.2 Quotient positive dimension missing | MAJOR | Adds \(1<\dim\mathcal X<\infty\); finite-CW type is a separate result. | §2.4 |
| 2.3 Four missing smallness/admissibility clauses | MAJOR | Applies all four exact verdict replacements, including \(e_{\rm np},e_{\rm old},\delta_{\max}^{\rm cb},\varepsilon_E^{\rm corr}\). | §§2.4, 3.3 |
| 2.4 Ledger common small-\(\eta\) range missing | MAJOR | Names \(\eta_A\) and adds \(0\le\eta\le\eta_A\) to the product and three telescope contracts. | §2.5 |
| 2.5 PRH hypotheses incomplete | BLOCKER | Uses the exact replacement with positive-unital \(A,M\). | §2.5 |
| 3.1 Compound/circular Stage-1 packet | BLOCKER | Deletes `lem-stage1-two-side-packet`; replaces only its nonduplicate clause by atomic `lem-maincb-split-corner-defect`. | §§2.4, 3.3 |
| 3.2 EXT-CB parent shorthand | MAJOR | Adds `def-extcb-datum`; every child is self-contained and no child mentions `conj-extcb`. | §§2.2, 4.1 |
| 3.3 Two compound packets | MAJOR | `lem-extcb4-complete-merging-datum` refers to its datum definition; the quotient classification and finite-CW consequence are separate rows. | §§2.2, 2.4 |
| 3.4 Threshold symbol dump | MAJOR | Replaces the minimum assertion by the common-guard interface, adds an atomic degree-three producer, and retains the explicit minimum only in the future shard body. | §2.5 |
| 4.1 Hidden EXT-CB cycle | BLOCKER | Closed in design through `def-extcb-datum` and downward-only deps. | §§2.2, 3.2 |
| 4.2 Hidden Stage-1/MAIN-CB cycle | BLOCKER | Deleted circular wrapper; split-corner comparison flows from COMP-CB and IMPROVE-CB into MAIN-CB. | §§2.4, 3.3 |
| 4.3 H-CB dangling imports | BLOCKER | Closed by the five COMP-CB rows and exact replacement deps. | §§2.1, 3.1 |
| 5.1 Parent projections count imports only | BLOCKER | H-CB and EXT-CB remain 10/2 and 9/2 after externalizing inputs; MAIN-CB is factored; ledger is explicitly `BLOCKED`, not assigned a fictitious projection. | §3 |
| 5.2 Three optimistic near-envelope leaves | MAJOR | Stage-1 isolation and left-inversion trace are factored below 10/3. Exact-target approximation remains a loud pre-seeding factoring GAP because no safe finer contract is present in the permitted packets. | §§2.2, 2.4, R9 |
| 6.1 Polar/IFT results hidden in a definition | BLOCKER | Restricts `def-approximate-unitary-space` to notation and adds separate quantitative-IFT, polar-chart, inversion-derivative, and isolation result rows. | §§2.4, 4.1 |
| 6.2 Composite cited definitions | MAJOR | Retags merging datum as `original/draft`; deletes the composite canonical system and replaces it by two `original/draft` definitions. | §4.1 |
| 6.3 Ledger vocabulary lacks producer | MAJOR | `lem-routef-ai-defect-linearization` names \(C_A,\eta_A\); `lem-routef-degree-three-estimate` produces \(C_3\); the threshold contract names only the guard interface. | §2.5 |
| 7.1 Glue promoted to `proved-mod-audit` | BLOCKER | Deletes the offending wrapper. All newly phrased MAIN-CB structural glue is `stated`; verified atomic comparisons retain `proved-mod-audit`. | §2.4 |
| 8.1 False closure claims | BLOCKER | Replaced by the honest non-seedability statement in §7 and explicit GAP rows/risks. | §§2.6, 6, 7 |
| F2/F3 closed hypothesis block | GAP | Two reserved ids, no invented contract; Phase 5 must extract and freshly review them before ledger rewiring. | §§2.6, 3.4 |
| Stage-1 polar/IFT factoring | GAP | Closed at design granularity by four separate rows, but the generic IFT leaf remains `stated` and all four contracts require the next hostile architecture review before seeding. | §2.4 |
| MAIN-CB assembly factoring | GAP | Replaced by five explicit `stated` contracts; their own prover/verifier passes remain mandatory. | §2.4 |
| Exact-target APPROX factoring | GAP | Still open and loud: no credible ≤12/3 projection can be supported from the permitted packets without another faithful factoring pass. | §2.2 |
| MINOR findings | MINOR | The verdict contains no MINOR-labelled finding. | — |

## 1. Status, counts, and notation

This standalone proposal contains **84 contracted result rows**:

- 19 COMP-CB / H-CB rows;
- 12 EXT-CB rows;
- 7 contingent topology leaves;
- 27 Stage-1 / MAIN-CB rows;
- 19 Route F ledger/finish rows.

It also reserves **two uncontracted Phase-5 GAP ids**. They are not registry
rows yet and are excluded from the count. Of the 84 contracted rows, 65 are
`proved-mod-audit`, 12 are `stated`, and 7 are `cited candidate`. No row is
proposed above `proved-mod-audit`.

`P:def-*` means a definition proposed in §4; unprefixed ids already exist.
Each projection counts the workspace root and treats validated/cited imports as
external leaves. `REFACTOR BEFORE SEEDING` is a blocker, not permission to
raise a node cap. Existing parent contracts remain byte-for-byte unchanged.
There are no `routes:` proposals.

## 2. Proposal table

### 2.1 Phase 2 — COMP-CB and corrected H-CB

| proposed id | kind / status | one-line `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-compcb-amplified-compression` | lemma / `proved-mod-audit` | Amplified compression identity: for every pair of \(\delta\)-projections \(P,Q\) in an extended \(\varepsilon\)-\(C^*\)-algebra and every \(n\ge1\), \(1_{M_n}\otimes Co_{P,Q}=Co_{I_n\otimes P,I_n\otimes Q}\) and \(M_n\otimes S_{P,Q}=S_{I_n\otimes P,I_n\otimes Q}\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | — | `DECOMP-W74F-C-THMAINEXT.md:152-183` | 4 / 2 |
| `lem-compcb-rectangular-product` | lemma / `proved-mod-audit` | Uniform rectangular compressed-product estimate: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{co}}\), every compatible amplified rectangular pair satisfies \(\lVert A\mathbin{\cdot}B-AB\rVert\le C_{\mathrm{co}}e\lVert A\rVert\lVert B\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression` | DECOMP COMP-CB; H-CB proof (1.1) | 4 / 2 |
| `lem-compcb-compressed-unit-action` | lemma / `proved-mod-audit` | Uniform compressed-unit action: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{co}}\), every compatible amplified rectangular corner satisfies \(\lVert u_T\mathbin{\cdot}A-A\rVert\le C_{\mathrm{co}}e\lVert A\rVert\) and \(\lVert A\mathbin{\cdot}u_R-A\rVert\le C_{\mathrm{co}}e\lVert A\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression`; `lem-compcb-rectangular-product` | H-CB proof (1.1); H-CB verdict HCB-3 correction | 4 / 2 |
| `lem-compcb-compressed-unit-norm` | lemma / `proved-mod-audit` | Compressed-unit norm estimate: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{co}}\), every \(\delta\)-projection \(T\) satisfies \(\lVert u_T\rVert\le1+C_{\mathrm{co}}e\), and every nonvanishing \(T\) satisfies \(\lvert\lVert u_T\rVert-1\rvert\le C_{\mathrm{co}}e\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression` | H-CB verdict:72-83 | 3 / 2 |
| `lem-compcb-single-compression-transfer` | lemma / `proved-mod-audit` | Single-compression transfer: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{co}}>0\) such that restricting an extended \(\alpha\)-inclusion to one ideal and following it by one compatible amplified compression produces an extended \(C_{\mathrm{co}}(\alpha+\varepsilon)\)-inclusion whenever \(\alpha+\varepsilon\le e_{\mathrm{co}}\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-amplified-compression`; `lem-compcb-rectangular-product` | DECOMP COMP-CB; Stage-1 proof SPLIT-C; H-verdict SPLIT-C | 6 / 3 |
| `lem-hcb-column-hilbert-squared` | lemma / `proved-mod-audit` | Corrected amplified column-Hilbert estimate: there are universal \(C_{\mathrm{col}}<\infty\) and \(e_{\mathrm{col}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{col}}\), every level-one one-dimensional \(\delta\)-projection \(Q\), every \(\delta\)-projection \(P\), every \(n\ge1\), and every \(X\in M_{n,1}\otimes S_{P,Q}\) satisfy \(\lvert\langle X,X\rangle_n-\lVert X\rVert_{n,1}^2\rvert\le C_{\mathrm{col}}e\lVert X\rVert_{n,1}^2\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-compcb-rectangular-product`; `lem-compcb-compressed-unit-norm` | DECOMP §4; H-CB proof §1.2; H-CB verdict checks 2–3 | 6 / 3 |
| `lem-hcb0-compressed-associator` | lemma / `proved-mod-audit` | Uniform compressed associator: there are universal \(C_{\mathrm{as}}<\infty\) and \(e_{\mathrm{as}}>0\) such that, whenever \(e=\delta+\varepsilon\le e_{\mathrm{as}}\), all compatible amplified rectangular compressed corners satisfy \(\lVert(A\mathbin{\cdot}B)\mathbin{\cdot}C-A\mathbin{\cdot}(B\mathbin{\cdot}C)\rVert\le C_{\mathrm{as}}e\lVert A\rVert\lVert B\rVert\lVert C\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner`; P:`def-compressed-associator` | `lem-compcb-rectangular-product` | H-CB proof §3; verdict HCB-0 | 5 / 2 |
| `lem-hcb1-variational-identity` | lemma / `proved-mod-audit` | Amplified Ha variational identity: for every \(n\ge1\), \(Z\in M_n\otimes S_{P,R}\), \(X\in M_{n,1}\otimes S_{R,Q}\), and \(Y\in M_{n,1}\otimes S_{P,Q}\), one has \(2\langle Y,(Ha^Q_{P,R})_n(Z)X-Z\mathbin{\cdot}X\rangle u_Q=(Y^\dagger\mathbin{\cdot}Z)\mathbin{\cdot}X-Y^\dagger\mathbin{\cdot}(Z\mathbin{\cdot}X)\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | H-CB proof §4; verdict HCB-1a | 4 / 2 |
| `lem-hcb1-column-action` | lemma / `proved-mod-audit` | Uniform Ha column action: there are universal \(C_{\mathrm{act}}<\infty\) and \(e_{\mathrm{act}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{act}}\), every admissible \(P,Q,R,n,Z,X\) satisfies \(q_P((Ha^Q_{P,R})_n(Z)X-Z\mathbin{\cdot}X)\le C_{\mathrm{act}}e\lVert Z\rVert q_R(X)\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner`; P:`def-compressed-associator` | `lem-hcb-column-hilbert-squared`; `lem-hcb0-compressed-associator`; `lem-hcb1-variational-identity` | H-CB proof §5; verdict HCB-1b | 6 / 3 |
| `lem-hcb2-amplified-adjointness` | lemma / `proved-mod-audit` | Exact amplified Ha adjointness: for every \(n\ge1\) and \(Z\in M_n\otimes S_{P,R}\), \((Ha^Q_{P,R})_n(Z)^\dagger=(Ha^Q_{R,P})_n(Z^\dagger)\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | H-CB proof §6.1; verdict HCB-2 | 2 / 1 |
| `lem-hcb2-product-defect` | lemma / `proved-mod-audit` | Uniform amplified Ha product defect: there are universal \(C_{\mathrm{prod}}<\infty\) and \(e_{\mathrm{prod}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{prod}}\), \(\lVert(Ha^Q_{P,R})_n(Z\mathbin{\cdot}W)-(Ha^Q_{P,S})_n(Z)(Ha^Q_{S,R})_n(W)\rVert\le C_{\mathrm{prod}}e\lVert Z\rVert\lVert W\rVert\) at every amplification. | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb0-compressed-associator`; `lem-hcb1-column-action` | H-CB proof §6.2; verdict HCB-2 | 6 / 3 |
| `lem-hcb3-diagonal-unit` | lemma / `proved-mod-audit` | Uniform diagonal Ha unit estimate: there are universal \(C_{\mathrm{unit}}<\infty\) and \(e_{\mathrm{unit}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{unit}}\), \(\lVert(Ha^Q_{P,P})_n(I_n\otimes u_P)-I\rVert\le C_{\mathrm{unit}}e\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb1-column-action`; `lem-compcb-compressed-unit-action` | H-CB proof §7.1; verdict HCB-3 | 4 / 2 |
| `lem-hcb3-diagonal-upper-norm` | lemma / `proved-mod-audit` | Uniform diagonal Ha upper norm: there are universal \(C_{\mathrm{up}}<\infty\) and \(e_{\mathrm{up}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{up}}\), \(\lVert(Ha^Q_{P,P})_n(Z)\rVert\le(1+C_{\mathrm{up}}e)\lVert Z\rVert\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb2-amplified-adjointness`; `lem-hcb2-product-defect` | H-CB proof §7.2; verdict HCB-3 | 5 / 3 |
| `lem-hcb3-diagonal-lower-modulus` | lemma / `proved-mod-audit` | Diagonal Ha lower-modulus propagation: there are universal \(C_{\mathrm{diag}}<\infty\) and \(e_{\mathrm{diag}}>0\) such that, if \(e=\delta+\varepsilon\le e_{\mathrm{diag}}\) and the level-one lower modulus of \(Ha^Q_{P,P}\) is at least \(1/4\), then \(\lVert(Ha^Q_{P,P})_n(Z)\rVert\ge(1-C_{\mathrm{diag}}e)\lVert Z\rVert\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb2-amplified-adjointness`; `lem-hcb2-product-defect` | H-CB proof §7.3; verdict HCB-3 | 8 / 3 |
| `lem-hcb3-diagonal-inverse` | lemma / `proved-mod-audit` | Diagonal Ha inverse propagation: under the hypotheses of `lem-hcb3-diagonal-lower-modulus`, if \(Ha^Q_{P,P}\) is bijective at level one, then every amplification is bijective and \(\lVert((Ha^Q_{P,P})_n)^{-1}\rVert\le1+C_{\mathrm{inv}}e\) for one universal \(C_{\mathrm{inv}}\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-column-hilbert-corner` | `lem-hcb3-diagonal-lower-modulus` | H-CB proof §7.3 (7.10); verdict HCB-3 | 3 / 2 |
| `lem-hcb3-offdiagonal-inverse` | lemma / `proved-mod-audit` | Off-diagonal Ha inverse propagation: there are universal \(C_{\mathrm{rect}}<\infty\) and \(e_{\mathrm{rect}}>0\) such that, when \(e\le e_{\mathrm{rect}}\), \(Ha^Q_{P,R}\) is bijective at level one, and \(Ha^Q_{R,R}\) has level-one lower modulus at least \(1/4\), every amplification of \(Ha^Q_{P,R}\) is bijective with inverse norm at most \(1+C_{\mathrm{rect}}e\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-column-hilbert-corner` | `lem-hcb2-amplified-adjointness`; `lem-hcb2-product-defect`; `lem-hcb3-diagonal-lower-modulus` | H-CB proof §7.4; verdict HCB-3 | 6 / 3 |
| `lem-hcb4-canonical-gram` | lemma / `proved-mod-audit` | Canonical corner Gram estimate: there are universal \(C_J<\infty\) and \(e_J>0\) such that, for \(e=\delta+\varepsilon\le e_J\), the canonical maps \(J_{P,Q,n}\) and \(J_{Q,P,n}\) satisfy \((1-C_Je)\lVert Z\rVert\le\lVert J_n(Z)\rVert\le(1+C_Je)\lVert Z\rVert\) at every amplification. | P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner`; P:`def-canonical-corner-identifications` | `lem-compcb-rectangular-product`; `lem-compcb-compressed-unit-norm` | H-CB proof §8.1–8.2; verdict HCB-4 | 6 / 3 |
| `lem-hcb4-canonical-closeness` | lemma / `proved-mod-audit` | Canonical Ha closeness: there are universal \(C_{\mathrm{sp}}<\infty\) and \(e_{\mathrm{sp}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{sp}}\), \(\max\{\lVert(Ha^Q_{P,Q})_n-J_{P,Q,n}\rVert,\lVert(Ha^Q_{Q,P})_n-J_{Q,P,n}\rVert\}\le C_{\mathrm{sp}}e\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner`; P:`def-canonical-corner-identifications` | `lem-hcb-column-hilbert-squared`; `lem-hcb1-column-action`; `lem-hcb2-amplified-adjointness`; `lem-hcb4-canonical-gram` | H-CB proof §8.3; verdict HCB-4 | 7 / 3 |
| `lem-hcb4-canonical-inverse` | lemma / `proved-mod-audit` | Canonical Ha inverse estimate: there are universal \(C_{\mathrm{sp,inv}}<\infty\) and \(e_{\mathrm{sp,inv}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{sp,inv}}\), the special maps \(Ha^Q_{P,Q}\) and \(Ha^Q_{Q,P}\) are completely bijective and their amplified inverses differ from the corresponding canonical inverses by at most \(C_{\mathrm{sp,inv}}e\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-column-hilbert-corner`; P:`def-canonical-corner-identifications` | `lem-hcb4-canonical-gram`; `lem-hcb4-canonical-closeness` | H-CB proof §8.3; verdict Neumann correction | 5 / 3 |

### 2.2 Phase 3 — EXT-CB

The first five rows remain source-premise targets. They are not promoted from
the printed theorem. No child contract below refers to `conj-extcb`.

| proposed id | kind / status | one-line `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-extcb-one-dimensional-product` | lemma / `stated` | Level-one one-dimensional corner product: there are universal \(C_{PQR}<\infty\) and \(e_{PQR}>0\) such that, for \(e=\delta+\varepsilon\le e_{PQR}\), if \(Q\) is one-dimensional then \(\lvert\lVert X\mathbin{\cdot}Y\rVert-\lVert X\rVert\lVert Y\rVert\rvert\le C_{PQR}e\lVert X\rVert\lVert Y\rVert\) for \(X\in S_{P,Q}\) and \(Y\in S_{Q,R}\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | TeX `lem_PQR`, 1162-1177; EXT-CB §2 | 5 / 3 |
| `lem-extcb-one-dimensional-corner-dimension` | lemma / `stated` | Level-one one-dimensional corner dimension: for sufficiently small universal \(\delta+\varepsilon\), if \(P\) and \(Q\) are one-dimensional \(\delta\)-projections then \(\dim S_{P,Q}\le1\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-extcb-one-dimensional-product` | TeX `lem_1d_proj`, 1179-1185; EXT-CB §2 | 4 / 2 |
| `lem-extcb-corner-dimension-additivity` | lemma / `stated` | Level-one corner-dimension additivity: for two finite-dimensional commutative \(C^*\)-algebras with projection bases and non-unital sufficiently accurate inclusions \(v,w\), the compressed corner \(S_{v(I),w(I)}\) is linearly bijective to \(\bigoplus_{j,k}S_{v(\Pi_j),w(\Sigma_k)}\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner`; P:`def-extended-delta-inclusion`; P:`def-projection-basis` | — | TeX `lem_add_dim`, 1363-1369, with recorded cardinality typo | 8 / 3 |
| `lem-extcb-exact-target-approximation` | lemma / `stated` | Exact-target complete approximation: there are universal \(C_{\mathrm{app}}<\infty\) and \(a_{\mathrm{app}}>0\) such that every extended \(\alpha\)-homomorphism \(T:M_r\to B(H)\) with \(\alpha\le a_{\mathrm{app}}\) is completely \(C_{\mathrm{app}}\alpha\)-close to one exact unital \(*\)-homomorphism \(\mu:M_r\to B(H)\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-operator-space` | — | EXT-CB premise APP; TeX `lem_approx_ext`, 1508-1535 | **REFACTOR BEFORE SEEDING (GAP-EA)** |
| `lem-extcb-four-corner-merge` | lemma / `stated` | Complete four-corner merge: there are universal \(C_{\mathrm{merge}}<\infty\) and \(a_{\mathrm{merge}}>0\) such that four fixed bijective level-one corner maps satisfying `def-four-corner-merging-datum` with common defect \(\rho\le a_{\mathrm{merge}}\) combine into one extended \(C_{\mathrm{merge}}(\rho+\varepsilon)\)-isomorphism. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner`; P:`def-four-corner-merging-datum` | — | EXT-CB premise MERGE; TeX `lem_merging`, 1325-1359 | 8 / 3 |
| `lem-extcb1-close-corner-dimension` | lemma / `proved-mod-audit` | Close-compression range invariance: there is a universal \(e_{\mathrm{close}}>0\) such that, in an EXT-CB datum with \(e=\delta+\varepsilon\le e_{\mathrm{close}}\), the compression ranges \(S_{v(I_r),Q}\) and \(S_{P,Q}\) have the same dimension. | P:`def-extcb-datum`; P:`def-compressed-corner` | — | EXT-CB verdict EXTCB-1 correction | 5 / 3 |
| `lem-extcb1-cross-corner-dimension` | lemma / `proved-mod-audit` | EXT-CB cross-corner dimension: there is a universal \(e_{\mathrm{sel}}>0\) such that every EXT-CB datum with \(e=\delta+\varepsilon\le e_{\mathrm{sel}}\) satisfies \((\dim S_{P,Q},\dim S_{Q,Q})=(r,1)\). | P:`def-extcb-datum`; P:`def-projection-basis` | `lem-extcb-one-dimensional-corner-dimension`; `lem-extcb-corner-dimension-additivity`; `lem-extcb1-close-corner-dimension` | EXT-CB proof §2; verdict correction | 7 / 3 |
| `lem-extcb2-exact-representation` | lemma / `proved-mod-audit` | EXT-CB exact representation: there are universal \(\kappa<\infty\) and \(e_{\mathrm{rep}}>0\) such that every EXT-CB datum with \(e\le e_{\mathrm{rep}}\) admits one exact unital \(*\)-homomorphism \(\mu_{11}:M_r\to B(S_{P,Q})\) satisfying \(\lVert(\mu_{11})_m-(Ha^Q_{P,P})_m v_m\rVert\le\kappa e\) for every \(m\ge1\). | `def-ha-map`; P:`def-extcb-datum`; P:`def-column-hilbert-corner` | `conj-hcb`; `lem-extcb-exact-target-approximation` | EXT-CB proof §3; verdict EXTCB-2 | 7 / 3 |
| `lem-extcb2-spatial-corner-system` | lemma / `proved-mod-audit` | EXT-CB spatial corner system: for the datum and exact representation supplied by `lem-extcb2-exact-representation`, \(\mu_{11}\) is implemented by one level-one unitary \(U_1:\mathbb C^r\to S_{P,Q}\), and together with the normalized \(U_2:\mathbb C\to S_{Q,Q}\) it defines one exact spatial four-corner system \(\mu_{jk}\) whose amplifications use \(I_m\otimes U_j\). | P:`def-extcb-datum`; P:`def-spatial-four-corner-system`; P:`def-column-hilbert-corner` | `lem-extcb1-cross-corner-dimension`; `lem-extcb2-exact-representation` | EXT-CB proof §3 (3.5)-(3.7); verdict EXTCB-2 | 5 / 3 |
| `lem-extcb3-four-ha-inverses` | lemma / `proved-mod-audit` | EXT-CB four Ha inverses: there are universal \(C_{\mathrm{inv}}<\infty\) and \(e_{\mathrm{inv}}>0\) such that every EXT-CB datum with \(e\le e_{\mathrm{inv}}\) has each \(Ha^Q_{P_j,P_k}\) bijective at level one and, for every amplification, \((1-C_{\mathrm{inv}}e)\lVert Z\rVert\le\lVert(Ha^Q_{P_j,P_k})_m(Z)\rVert\le(1+C_{\mathrm{inv}}e)\lVert Z\rVert\) and \(\lVert((Ha^Q_{P_j,P_k})_m)^{-1}\rVert\le1+C_{\mathrm{inv}}e\). | `def-ha-map`; P:`def-extcb-datum`; P:`def-column-hilbert-corner` | `conj-hcb`; `lem-extcb2-exact-representation` | EXT-CB proof §4; verdict EXTCB-3 | 7 / 3 |
| `lem-extcb4-transported-corners` | lemma / `proved-mod-audit` | EXT-CB transported corner comparison: the fixed level-one maps \(\gamma_{11}=v\) and \(\gamma_{jk}=(Ha^Q_{P_j,P_k})^{-1}\mu_{jk}\) for \((j,k)\ne(1,1)\) satisfy \(\lVert(Ha^Q_{P,P})_m\gamma_{11,m}-\mu_{11,m}\rVert\le\kappa e\) and \((Ha^Q_{P_j,P_k})_m\gamma_{jk,m}=\mu_{jk,m}\) in the other three corners for every \(m\). | `def-ha-map`; P:`def-extcb-datum`; P:`def-spatial-four-corner-system`; P:`def-four-corner-merging-datum` | `lem-extcb2-spatial-corner-system`; `lem-extcb3-four-ha-inverses` | EXT-CB proof §5 (5.1)-(5.3); verdict EXTCB-4 | 5 / 3 |
| `lem-extcb4-complete-merging-datum` | lemma / `proved-mod-audit` | EXT-CB complete merging datum: the four fixed transported corner maps of `lem-extcb4-transported-corners` satisfy `def-four-corner-merging-datum` at every amplification with common defect \(5(C_H+\kappa)e\). | `def-ha-map`; P:`def-extcb-datum`; P:`def-four-corner-merging-datum` | `conj-hcb`; `lem-extcb3-four-ha-inverses`; `lem-extcb4-transported-corners` | EXT-CB proof §5.1–5.4; verdict EXTCB-4 | 6 / 3 |

### 2.3 Phase 4A — Stage-1 topology leaves

These are not `cited` until the exact local source is acquired, hashed, and
byte-matched.

| proposed id | kind / status | one-line `contract:` value | defs | deps | candidate source | projected af |
|---|---|---|---|---|---|---|
| `lem-topology-quotient-manifold` | lemma / `cited candidate` | Quotient manifold theorem: if a Lie group acts smoothly, freely, and properly on a smooth manifold \(M\), then \(M/G\) has the unique smooth-manifold structure for which the quotient map is a smooth submersion. | — | — | Lee, *Introduction to Smooth Manifolds*, Thm 21.10 | 1 / 1 external |
| `lem-topology-finite-triangulation` | lemma / `cited candidate` | Finite triangulation of compact \(C^1\) manifolds: every compact \(C^1\) manifold is homeomorphic to a finite simplicial complex. | — | — | Whitehead (1940) or Cairns; exact locus required | 1 / 1 external |
| `lem-topology-lefschetz-hopf` | lemma / `cited candidate` | Lefschetz-Hopf formula: for a self-map of a finite polyhedron with finitely many isolated fixed points, the Lefschetz number is the sum of their fixed-point indices. | P:`def-lefschetz-fixed-point-data` | — | Arkowitz–Brown; exact theorem required | 1 / 1 external |
| `lem-topology-local-index-sign` | lemma / `cited candidate` | Nondegenerate local fixed-point index: if \(x\) is an isolated fixed point of a \(C^1\) self-map and \(\det(I-Df_x)\ne0\), then its local fixed-point index is \(\operatorname{sgn}\det(I-Df_x)\). | P:`def-lefschetz-fixed-point-data` | — | Granas–Dugundji; exact locus required | 1 / 1 external |
| `lem-topology-orientable-top-cohomology` | lemma / `cited candidate` | Top cohomology of a closed orientable manifold: if \(M\) is a connected compact orientable \(d\)-manifold without boundary, then \(H^d(M;\mathbb R)\ne0\). | — | — | Hatcher §3.3; exact theorem required | 1 / 1 external |
| `lem-topology-kunneth-cross-product` | lemma / `cited candidate` | Cohomological Künneth isomorphism over \(\mathbb R\): for finite-CW spaces with finite-dimensional cohomology, the cross product identifies \(H^*(X;\mathbb R)\otimes H^*(Y;\mathbb R)\) with \(H^*(X\times Y;\mathbb R)\). | — | — | Hatcher Thm 3.16 | 1 / 1 external |
| `lem-topology-hopf-structure` | lemma / `cited candidate` | Hopf structure theorem in the form consumed by Stage 1: a finite-dimensional connected graded-commutative bialgebra over a characteristic-zero field is an exterior algebra on odd-degree homogeneous generators. | P:`def-h-space-left-inversion` | — | Hatcher Thm 3C.4; non-coassociative hypothesis match required | 1 / 1 external |

### 2.4 Phase 4B — Stage 1 and MAIN-CB

The old `lem-stage1-two-side-packet` row is deleted. The analytic, trace,
reset, and structural subtrees below are downward-only: no Stage-1 child
imports `lem-thmainext-conditional`, and no EXT-CB child imports `conj-extcb`.

| proposed id | kind / status | one-line `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-stage1-quantitative-inverse-function` | lemma / `stated` | Quantitative inverse-function control: if \(V:X\to Y\) is a Banach-space isomorphism and \(f:B_r(x_0)\to Y\) is \(C^1\) with \(\lVert V^{-1}Df(x)-I\rVert\le c<1\), then \(f\) is injective, \((1-c)\lVert x_1-x_2\rVert\le\lVert V^{-1}(f(x_1)-f(x_2))\rVert\le(1+c)\lVert x_1-x_2\rVert\), and \(f(B_r(x_0))\) contains \(f(x_0)+V(B_{(1-c)r}(0))\). | — | — | pinned TeX 562–592; source theorem premise, not a definition | 5 / 3 |
| `lem-stage1-exact-unit-rectification` | lemma / `proved-mod-audit` | Dimension-free exact-unit rectification: there are universal \(C_{\mathrm{unit}}<\infty\), \(e_{\mathrm{unit}}>0\) such that every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra with \(\varepsilon_X\le e_{\mathrm{unit}}\) admits on the same involutive normed space an exact unit \(J\) and product \(\boldsymbol{\cdot}\) with \(\lVert J-I_X\rVert\le C_{\mathrm{unit}}\varepsilon_X\) and \(\lVert x\boldsymbol{\cdot}y-xy\rVert\le C_{\mathrm{unit}}\varepsilon_X\lVert x\rVert\lVert y\rVert\). | P:`def-epsilon-cstar-algebra` | — | Stage-1 proof §1, (1.1); verdict exact-unit rectification | 7 / 3 |
| `lem-stage1-polar-chart-control` | lemma / `proved-mod-audit` | Uniform Stage-1 polar chart: there are universal \(e_{\mathrm{pol}},r_{\mathrm{pol}}>0\) and \(C_{\mathrm{pol}}<\infty\) such that every finite-dimensional rectified \(\varepsilon_X\)-\(C^*\)-algebra with \(\varepsilon_X\le e_{\mathrm{pol}}\) has the \(C^1\) approximate-unitary space and polar retraction denoted by `def-approximate-unitary-space` on the fixed \(r_{\mathrm{pol}}\)-neighborhood, with polar, group-law, and first-derivative errors at most \(C_{\mathrm{pol}}\varepsilon_X\). | P:`def-epsilon-cstar-algebra`; P:`def-approximate-unitary-space` | `lem-stage1-quantitative-inverse-function`; `lem-stage1-exact-unit-rectification` | Stage-1 proof §1, (1.2)–(1.3); verdict’s required polar/IFT split | 7 / 3 |
| `lem-stage1-inversion-derivative-control` | lemma / `proved-mod-audit` | Uniform inversion derivative: there are universal \(C_{\mathrm{inv}}<\infty\), \(e_{\mathrm{inv}}>0\), and \(r_{\mathrm{inv}}>0\) such that, for \(\varepsilon_X\le e_{\mathrm{inv}}\), the map \(\sigma(U)=u(U^\dagger)\) is \(C^1\) and every radius-\(r\le r_{\mathrm{inv}}\) chart about \(J\) or \(-J\) satisfies \(\lVert D(\sigma-\mathrm{id})+2I\rVert\le C_{\mathrm{inv}}(r+\varepsilon_X)\). | P:`def-epsilon-cstar-algebra`; P:`def-approximate-unitary-space` | `lem-stage1-polar-chart-control` | Stage-1 proof §1, (1.3)–(1.4); verdict’s required derivative split | 5 / 3 |
| `lem-stage1-uniform-inversion-isolation` | lemma / `proved-mod-audit` | Uniform inversion isolation: there are universal \(r_{\mathrm{iso}}>0\) and \(e_{\mathrm{iso}}>0\) such that, in the rectified approximate-unitary manifold of an \(\varepsilon_X\)-\(C^*\)-algebra with \(\varepsilon_X\le e_{\mathrm{iso}}\), the inversion map has no fixed point in either \(r_{\mathrm{iso}}\)-ball about \(J\) or \(-J\) except the center. | P:`def-epsilon-cstar-algebra`; P:`def-approximate-unitary-space` | `lem-stage1-quantitative-inverse-function`; `lem-stage1-inversion-derivative-control` | Stage-1 proof §1, (1.2)–(1.4); verdict isolation section | 5 / 3 |
| `lem-stage1-quotient-manifold-package` | lemma / `proved-mod-audit` | Stage-1 quotient manifold: if \(1<\dim\mathcal X<\infty\) and the Stage-1 analytic construction is in its universal validity range, then \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact positive-dimensional orientable \(C^1\) manifold without boundary. | P:`def-approximate-unitary-space` | `lem-stage1-polar-chart-control`; `lem-topology-quotient-manifold` | Stage-1 proof SPLIT-A; verdict exact replacement | 5 / 3 |
| `lem-stage1-quotient-finite-cw` | lemma / `proved-mod-audit` | Stage-1 quotient finite-CW consequence: if \(1<\dim\mathcal X<\infty\) and the Stage-1 quotient \(\breve{\mathcal U}\) is a compact \(C^1\) manifold, then \(\breve{\mathcal U}\) has finite CW type. | P:`def-approximate-unitary-space` | `lem-stage1-quotient-manifold-package`; `lem-topology-finite-triangulation` | Stage-1 proof SPLIT-A; verdict topological correction | 3 / 2 |
| `lem-stage1-quotient-left-inversion` | lemma / `proved-mod-audit` | Stage-1 quotient H-space: the multiplication and inversion induced on \(\breve{\mathcal U}\) make it a connected H-space with a left inversion map. | P:`def-approximate-unitary-space`; P:`def-h-space-left-inversion` | `lem-stage1-polar-chart-control` | pinned TeX 895–912 and 945–955; Stage-1 proof §1 | 5 / 3 |
| `lem-stage1-exterior-cohomology` | lemma / `proved-mod-audit` | Stage-1 exterior cohomology: if \(M\) is a connected finite-CW H-space with finite-dimensional real cohomology, then \(H^*(M;\mathbb R)\) is an exterior algebra on finitely many odd-degree homogeneous generators. | P:`def-h-space-left-inversion` | `lem-topology-kunneth-cross-product`; `lem-topology-hopf-structure` | pinned TeX 986–1016; Stage-1 proof and verdict | 5 / 3 |
| `lem-stage1-left-inversion-associated-graded` | lemma / `proved-mod-audit` | Left inversion on the associated graded: under the hypotheses of `lem-stage1-exterior-cohomology`, \(\sigma^*\) preserves the augmentation filtration and acts by \((-1)^k\) on every associated-graded component of total cohomological degree \(k\). | P:`def-h-space-left-inversion`; P:`def-augmentation-filtration` | `lem-stage1-exterior-cohomology` | pinned TeX 1023–1049; Stage-1 proof and verdict | 6 / 3 |
| `lem-stage1-left-inversion-trace` | lemma / `proved-mod-audit` | Left-inversion trace: if \(M\) is a connected finite-CW H-space with finite-dimensional real cohomology and left inversion \(\sigma\), then \(\operatorname{Tr}(\sigma^{*k})=(-1)^k\dim H^k(M;\mathbb R)\) for every \(k\). | P:`def-h-space-left-inversion`; P:`def-lefschetz-fixed-point-data`; P:`def-augmentation-filtration` | `lem-stage1-left-inversion-associated-graded` | pinned TeX 971–1050; Stage-1 verdict checks 8–9 | 3 / 2 |
| `lem-stage1-extra-fixed-class` | lemma / `proved-mod-audit` | Extra inversion fixed class: the induced inversion \(\breve{\sigma}\) on the Stage-1 quotient \(\breve{\mathcal U}\) has a fixed point distinct from the scalar class \(\breve e\). | P:`def-approximate-unitary-space`; P:`def-h-space-left-inversion`; P:`def-lefschetz-fixed-point-data` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-finite-cw`; `lem-stage1-quotient-left-inversion`; `lem-stage1-left-inversion-trace`; `lem-topology-lefschetz-hopf`; `lem-topology-local-index-sign`; `lem-topology-orientable-top-cohomology` | Stage-1 proof SPLIT-A; verdict topological sections | 10 / 3 |
| `lem-stage1-rectified-nontrivial-projection` | lemma / `proved-mod-audit` | Rectified nontrivial projection: a non-scalar inversion fixed class outside the two isolation balls yields a Hermitian \(P_0=\frac14(2J+U+U^\dagger)\) with \(\lVert P_0\boldsymbol{\cdot}P_0-P_0\rVert\le C_{\mathrm{proj}}\varepsilon_X\) and with both \(P_0\) and \(J-P_0\) in the nonvanishing norm alternative. | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-approximate-unitary-space` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-extra-fixed-class` | Stage-1 proof §1, (1.5)–(1.9); verdict projection/nonvanishing checks | 7 / 3 |
| `lem-stage1-original-complementary-pair` | lemma / `proved-mod-audit` | Original-product complementary pair: there are universal \(C_{\mathrm{np}}<\infty\) and \(e_{\mathrm{np}}>0\) such that, whenever \(0\le\varepsilon_X\le e_{\mathrm{np}}\), the elements \(P'=P_0\) and \(P''=I_X-P'\) are nonvanishing Hermitian \(C_{\mathrm{np}}\varepsilon_X\)-projections, satisfy \(P'+P''=I_X\), and have both cross-products bounded by \(C_{\mathrm{np}}\varepsilon_X\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection` | `lem-stage1-exact-unit-rectification`; `lem-stage1-rectified-nontrivial-projection` | Stage-1 proof (1.10)–(1.11); verdict exact replacement, including \(e_{\mathrm{nv}}\) shrink | 7 / 3 |
| `lem-stage1-fresh-two-point-inclusion` | lemma / `proved-mod-audit` | Fresh two-point complete inclusion: there are universal \(C_{\mathrm{pair}}<\infty\), \(e_{\mathrm{pair}}>0\) such that \(v_{\mathrm{comm}}^{(2)}:\mathbb C^2\to X\), \((\lambda,\mu)\mapsto\lambda P'+\mu P''\), is an extended \(C_{\mathrm{pair}}\varepsilon_X\)-inclusion whenever \(\varepsilon_X\le e_{\mathrm{pair}}\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-operator-space` | `lem-stage1-original-complementary-pair` | Stage-1 proof SPLIT-B, (1.12)–(1.19); verdict | 8 / 3 |
| `lem-stage1-old-side-compression` | lemma / `proved-mod-audit` | Old-side Stage-1 compression: there are universal \(C_{\mathrm{old}}<\infty\) and \(e_{\mathrm{old}}>0\) such that, whenever \(0\le\varepsilon_0\le e_{\mathrm{old}}\), restricting a reset maximal commutative inclusion and applying the single compatible compression into \(S_{P_{[1,m-1]}}\) produces an extended \(C_{\mathrm{old}}\varepsilon_0\)-inclusion; when \(m=1\) this side is absent. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-compressed-corner`; P:`def-projection-basis` | `lem-compcb-single-compression-transfer`; `lem-maincb-error-improvement` | Stage-1 proof SPLIT-C; verdict exact replacement | 6 / 3 |
| `lem-maincb-error-improvement` | lemma / `stated` | Complete error improvement: there are universal \(\delta_{\max}^{\mathrm{cb}}>0\) and \(c_0^{\mathrm{cb}}<\infty\) such that every extended \(\delta\)-inclusion into an extended \(\varepsilon\)-\(C^*\)-algebra with \(0\le\delta\le\delta_{\max}^{\mathrm{cb}}\) can be replaced by one extended \(c_0^{\mathrm{cb}}\varepsilon\)-inclusion, preserving bijectivity. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-extcb-exact-target-approximation` | DECOMP premise IMPROVE-CB; pinned TeX 1508–1535; not proved by the permitted packets | **REFACTOR BEFORE SEEDING (inherits GAP-EA)** |
| `lem-maincb-split-corner-defect` | lemma / `proved-mod-audit` | MAIN-CB split-corner defect: there are universal \(C_{\mathrm{co}}<\infty\) and \(e_{\mathrm{split}}>0\) such that, if \(\varepsilon_0\le e_{\mathrm{split}}\) is the Stage-1 ambient-algebra defect and \(\varepsilon_S\) is the fresh split-corner defect, then \(\varepsilon_S\le C_{\mathrm{co}}(1+c_0^{\mathrm{cb}})\varepsilon_0\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-compcb-single-compression-transfer`; `lem-maincb-error-improvement` | Stage-1 verdict 187–216 | 4 / 2 |
| `lem-maincb-stage1-raw-reset-bound` | lemma / `proved-mod-audit` | MAIN-CB Stage-1 raw bound: with \(C_{\mathrm{main}}=\max\{C_{\mathrm{co}},C_{\mathrm{split}}\}\), \(L=C_{\mathrm{main}}(1+c_0^{\mathrm{cb}})\), and \(C_{\mathrm{pre}}=2L^2\max\{1,C_{\mathrm{ext}},C_{\mathrm{merge}}\}\), every admissible Stage-1 raw call has \(\delta_{\mathrm{raw}}\le L^2\varepsilon\) and \(e_{\mathrm{raw}}\le C_{\mathrm{pre}}\varepsilon\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner` | `lem-stage1-fresh-two-point-inclusion`; `lem-stage1-old-side-compression`; `lem-maincb-split-corner-defect`; `lem-maincb-error-improvement` | Stage-1 proof §3, (3.1)–(3.4); verdict reset-chain correction | 6 / 3 |
| `lem-maincb-stage2-raw-reset-bound` | lemma / `proved-mod-audit` | MAIN-CB Stage-2 raw bound: with the constants of `lem-maincb-stage1-raw-reset-bound`, every admissible Stage-2 extension call has \(\delta_{\mathrm{raw}}\le L^2\varepsilon\) and \(e_{\mathrm{raw}}\le C_{\mathrm{pre}}\varepsilon\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner` | `lem-maincb-stage1-raw-reset-bound`; `lem-compcb-single-compression-transfer`; `conj-extcb`; `lem-maincb-error-improvement` | Stage-1 proof §3, (3.5)–(3.7); verdict reset-chain correction | 5 / 3 |
| `lem-maincb-stage3-raw-reset-bound` | lemma / `proved-mod-audit` | MAIN-CB Stage-3 raw bound: with the constants of `lem-maincb-stage1-raw-reset-bound`, every admissible binary four-corner merge has \(\delta_{\mathrm{raw}}\le L^2\varepsilon\) and \(e_{\mathrm{raw}}\le C_{\mathrm{pre}}\varepsilon\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-four-corner-merging-datum` | `lem-maincb-stage1-raw-reset-bound`; `lem-extcb-four-corner-merge`; `lem-maincb-error-improvement` | Stage-1 proof §3, (3.8)–(3.10); verdict reset-chain correction | 4 / 2 |
| `lem-maincb-uniform-reset-chain` | lemma / `proved-mod-audit` | MAIN-CB uniform reset invariant: with \(C_{\mathrm{main}}=\max\{C_{\mathrm{co}},C_{\mathrm{split}}\}\), \(L=C_{\mathrm{main}}(1+c_0^{\mathrm{cb}})\), and \(C_{\mathrm{pre}}=2L^2\max\{1,C_{\mathrm{ext}},C_{\mathrm{merge}}\}\), there is a universal \(\varepsilon_E^{\mathrm{corr}}>0\) such that for \(0\le\varepsilon\le\varepsilon_E^{\mathrm{corr}}\) every Stage-1, Stage-2, and Stage-3 raw call satisfies \(\delta_{\mathrm{raw}}\le L^2\varepsilon\) and \(e_{\mathrm{raw}}\le C_{\mathrm{pre}}\varepsilon\), and every extension or merge is followed immediately by an error reset. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner`; P:`def-four-corner-merging-datum` | `lem-maincb-stage1-raw-reset-bound`; `lem-maincb-stage2-raw-reset-bound`; `lem-maincb-stage3-raw-reset-bound` | Stage-1 proof §3; verdict exact replacement | 4 / 2 |
| `lem-maincb-stage1-maximality-termination` | lemma / `stated` | MAIN-CB Stage-1 maximality termination: under the validated split, compression, improvement, and reset interfaces, iterating the Stage-1 split strictly enlarges the selected finite family of nonzero orthogonal corner classes and therefore terminates at a maximal commutative selection while preserving the single-level-one-map and bijectivity invariants. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-projection-basis` | `lem-stage1-fresh-two-point-inclusion`; `lem-stage1-old-side-compression`; `lem-maincb-split-corner-defect`; `lem-maincb-uniform-reset-chain` | DECOMP MAIN-CB 546–568; newly factored structural glue | 7 / 3 |
| `lem-maincb-equivalence-class-partition` | lemma / `stated` | MAIN-CB equivalence-class partition: the maximal Stage-1 one-dimensional corner family is partitioned by nonzero cross-corners into finitely many equivalence classes, and the dimension-additivity interface identifies the matrix-block size attached to each class. | P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-projection-basis` | `lem-extcb-one-dimensional-corner-dimension`; `lem-extcb-corner-dimension-additivity` | DECOMP MAIN-CB 568–574; newly factored structural glue | 4 / 2 |
| `lem-maincb-stage2-extension-walk` | lemma / `stated` | MAIN-CB Stage-2 extension walk: for every equivalence class from `lem-maincb-equivalence-class-partition`, finitely many EXT-CB extension calls construct a bijective level-one matrix-block map on that class while preserving the common raw-defect and immediate-reset invariants. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-projection-basis` | `lem-maincb-equivalence-class-partition`; `conj-extcb`; `lem-compcb-single-compression-transfer`; `lem-maincb-uniform-reset-chain` | DECOMP MAIN-CB 574–581; newly factored structural glue | 6 / 3 |
| `lem-maincb-stage3-binary-recombination` | lemma / `stated` | MAIN-CB Stage-3 binary recombination: the finitely many Stage-2 block maps can be joined by a finite binary sequence of complete four-corner merges to one bijective level-one map, with each merge preserving the single-level-one-map invariant and followed immediately by reset. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-four-corner-merging-datum` | `lem-maincb-stage2-extension-walk`; `lem-extcb-four-corner-merge`; `lem-maincb-uniform-reset-chain` | DECOMP MAIN-CB 581–589; newly factored structural glue | 5 / 3 |
| `lem-maincb-structural-assembly` | lemma / `stated` | MAIN-CB structural assembly: the finite Stage-1 maximal selection, equivalence-class partition, Stage-2 extension walk, and Stage-3 binary recombination yield a bijective level-one map \(v:\mathcal B\to\mathcal A\) from a finite-dimensional \(C^*\)-algebra \(\mathcal B\), and every all-level map used by the construction is the amplification of its single level-one map. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner` | `lem-maincb-stage1-maximality-termination`; `lem-maincb-equivalence-class-partition`; `lem-maincb-stage2-extension-walk`; `lem-maincb-stage3-binary-recombination` | DECOMP MAIN-CB 546–589; newly factored structural glue | 5 / 2 |

### 2.5 Phase 4C — relative Route F ledger and finish

These contracts remain relative to the existing Kitaev/PRH leaves and to the
proposed MAIN-CB subtree. The final parent stays blocked as specified in §3.4.

| proposed id | kind / status | one-line `contract:` value | defs | deps | provenance | projected af |
|---|---|---|---|---|---|---|
| `lem-routef-main-radius-ledger` | lemma / `proved-mod-audit` | Corrected MAIN-CB radius ledger: the constants \(C_{\mathrm{main}},L,C_{\mathrm{pre}}\) from `lem-maincb-uniform-reset-chain` and \(\varepsilon_E^{\mathrm{corr}}=\min\{\delta_{\max}^{\mathrm{cb}},e_H,e_{\mathrm{ext}},e_{\mathrm{sel}},e_{\mathrm{split}}\}/C_{\mathrm{pre}}\) are finite, positive, universal, and independent of dimension, amplification, block data, and stage index. | `def-extended-epsilon-cstar-algebra` | `conj-hcb`; `conj-extcb`; `lem-maincb-uniform-reset-chain`; `lem-thmainext-conditional` | Stage-1 proof §3; Stage-1 verdict corrected radius | 6 / 3 |
| `lem-routef-functional-calculus-closeness` | lemma / `proved-mod-audit` | Functional-calculus closeness: for \(0\le\eta\le1/8\), the exact functional-calculus projector satisfies \(\lVert\widetilde\Phi-\Phi\rVert_{\mathrm{cb}}\le C_\theta\eta\), where \(C_\theta=12(\sqrt2-1)\). | `def-almost-idempotent` | `lem-kitaev-almost-idemp-audit` | G-ledger §1.1; G-verdict checks 3–4 | 4 / 2 |
| `lem-routef-ai-defect-linearization` | lemma / `proved-mod-audit` | Approximate-algebra defect linearization: there are universal \(C_A<\infty\) and \(\eta_A>0\) such that, for \(0\le\eta\le\eta_A\), the image of \(\widetilde\Phi\) is an extended \(\varepsilon_{\mathrm{AI}}(\eta)\)-\(C^*\)-algebra with \(\varepsilon_{\mathrm{AI}}(\eta)\le C_A\eta\), where \(C_A=20+\frac{211}{8}C_\theta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-kitaev-almost-idemp-audit`; `lem-routef-functional-calculus-closeness` | G-ledger §1.1, (1.1); verdict exact replacement | 5 / 3 |
| `lem-routef-raw-factor-norms` | lemma / `proved-mod-audit` | Raw factor-map norm bound: for \(0\le\eta\le\eta_A\), \(\max\{\lVert\widetilde\Delta\rVert_{\mathrm{cb}},\lVert\widetilde\Upsilon\rVert_{\mathrm{cb}}\}\le1+C_T\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | G-ledger §1.3, (1.9); verdict arithmetic | 5 / 3 |
| `lem-routef-raw-factor-units` | lemma / `proved-mod-audit` | Raw factor-map unit bound: for \(0\le\eta\le\eta_A\), \(\max\{\lVert\widetilde\Delta(I)-I\rVert,\lVert\widetilde\Upsilon(I)-I\rVert\}\le C_T\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | G-ledger §1.3, (1.9); verdict arithmetic | 5 / 3 |
| `lem-routef-raw-factor-identities` | lemma / `proved-mod-audit` | Raw factor-map identities: \((\widetilde\Delta\widetilde\Upsilon,\widetilde\Upsilon\widetilde\Delta)=(\widetilde\Phi,I_{\mathcal B})\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-thmainext-conditional` | G-ledger §1.3, (1.10); verdict | 3 / 2 |
| `lem-routef-raw-product-estimate` | lemma / `proved-mod-audit` | Raw factor-map product estimate: for \(0\le\eta\le\eta_A\), \(\lVert\widetilde\Upsilon_n(\widetilde\Delta_n(X)\widetilde\Delta_n(Y))-XY\rVert\le C_T\eta\lVert X\rVert\lVert Y\rVert\) for every amplification \(n\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-routef-raw-factor-norms`; `lem-routef-raw-factor-identities`; `lem-thmainext-conditional` | G-ledger §1.3, (1.9); verdict arithmetic | 6 / 3 |
| `lem-routef-delta-prime-closeness` | lemma / `proved-mod-audit` | Delta-prime CP closeness: for \(0\le\eta\le\eta_A\), the repaired diagonal CP-ization produces a completely positive map \(\Delta'\) with \(\lVert\Delta'-\widetilde\Delta\rVert_{\mathrm{cb}}\le C_{\Delta'}\eta\), where \(C_{\Delta'}=C_T+4C_\theta\). | `def-fd-cstar-diagonal`; `def-extended-epsilon-cstar-algebra` | `cor-kitaev-diagonal-cpization`; `lem-routef-functional-calculus-closeness`; `lem-routef-raw-factor-norms` | G-ledger §1.3, (1.11)–(1.12); verdict | 7 / 3 |
| `lem-routef-delta-normalization-closeness` | lemma / `proved-mod-audit` | Delta UCP normalization: for \(0\le\eta\le\eta_A\), normalizing \(\Delta'\) produces a UCP map \(\Delta\) with \(\lVert\Delta-\widetilde\Delta\rVert_{\mathrm{cb}}\le C_\Delta\eta\), where \(C_\Delta=6C_T+7C_{\Delta'}\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-factor-units`; `lem-routef-delta-prime-closeness` | G-ledger §1.3, (1.11)–(1.12); verdict | 7 / 3 |
| `lem-routef-delta-phi-product` | lemma / `proved-mod-audit` | Normalized Delta product estimate: for \(0\le\eta\le\eta_A\) and every amplification \(n\), \(\lVert\widetilde\Phi_n(\Delta_n(X)\Delta_n(Y))-\widetilde\Delta_n(XY)\rVert\le(C_2+C_\theta+C_\Delta)\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-ai-defect-linearization`; `lem-routef-functional-calculus-closeness`; `lem-routef-delta-normalization-closeness` | G-ledger §3 before (3.3); verdict exact replacement | 6 / 3 |
| `lem-routef-upsilon-prime-closeness` | lemma / `proved-mod-audit` | Upsilon-prime CP closeness: for \(0\le\eta\le\eta_A\), the componentwise CP construction produces a completely positive map \(\Upsilon'\) with \(\lVert\Upsilon'-\widetilde\Upsilon\rVert_{\mathrm{cb}}\le C_{\Upsilon'}\eta\), where \(C_{\Upsilon'}\) is finite, universal, and independent of block count and block dimensions. | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-product-estimate`; `lem-routef-delta-phi-product` | G-ledger §1.3, (1.13); verdict checks 13–14 | 10 / 3, highest-risk ledger leaf |
| `lem-routef-upsilon-normalization-closeness` | lemma / `proved-mod-audit` | Upsilon UCP normalization: for \(0\le\eta\le\eta_A\), normalizing \(\Upsilon'\) produces a UCP map \(\Upsilon\) with \(\lVert\Upsilon-\widetilde\Upsilon\rVert_{\mathrm{cb}}\le C_\Upsilon\eta\), where \(C_\Upsilon=6C_T+7C_{\Upsilon'}\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-factor-units`; `lem-routef-upsilon-prime-closeness` | G-ledger §1.3, (1.14)–(1.15); verdict | 7 / 3 |
| `lem-routef-delta-upsilon-telescope` | lemma / `proved-mod-audit` | Delta-Upsilon telescope: for \(0\le\eta\le\eta_A\), \(\lVert\Delta\Upsilon-\Phi\rVert_{\mathrm{cb}}\le(C_\theta+C_\Delta+2C_\Upsilon)\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-ai-defect-linearization`; `lem-routef-functional-calculus-closeness`; `lem-routef-raw-factor-identities`; `lem-routef-delta-normalization-closeness`; `lem-routef-upsilon-normalization-closeness` | G-ledger §3, first line of (3.2); verdict exact replacement | 6 / 3 |
| `lem-routef-multiplicative-telescope` | lemma / `proved-mod-audit` | Multiplicative telescope: for \(0\le\eta\le\eta_A\) and every amplification \(n\), \(\lVert\Upsilon_n(\Delta_n(X)\Delta_n(Y))-XY\rVert\le[C_\Upsilon+2(C_2+C_\theta+C_\Delta)]\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-ai-defect-linearization`; `lem-routef-raw-factor-norms`; `lem-routef-raw-factor-identities`; `lem-routef-delta-phi-product`; `lem-routef-upsilon-normalization-closeness` | G-ledger §3, second line of (3.2); verdict exact replacement | 7 / 3 |
| `lem-routef-upsilon-delta-telescope` | lemma / `proved-mod-audit` | Upsilon-Delta telescope: for \(0\le\eta\le\eta_A\), \(\lVert\Upsilon\Delta-I_{\mathcal B}\rVert_{\mathrm{cb}}\le(C_\Upsilon+2C_\Delta)\eta\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-ai-defect-linearization`; `lem-routef-raw-factor-identities`; `lem-routef-delta-normalization-closeness`; `lem-routef-upsilon-normalization-closeness` | G-ledger §3, third line of (3.2); verdict exact replacement | 5 / 3 |
| `lem-routef-degree-three-estimate` | lemma / `proved-mod-audit` | Route F degree-three estimate: for \(0\le\eta\le\eta_A\), \(\operatorname{def}_3(\Phi,\Delta)(X,Y,Z)\le C_3\eta\lVert X\rVert\lVert Y\rVert\lVert Z\rVert\), where \(C_3=10+20C_\Delta+12C_\theta+2C_{\Delta'}\) is finite and universal. | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-ai-defect-linearization`; `lem-routef-functional-calculus-closeness`; `lem-routef-delta-prime-closeness`; `lem-routef-delta-normalization-closeness` | G-ledger §1.3, (1.11)–(1.12), pinned TeX 2786–2829 | 6 / 3 |
| `lem-routef-k-finiteness` | lemma / `proved-mod-audit` | Route F common coefficient: \(K=\max\{1,C_\theta+C_\Delta+2C_\Upsilon,C_\Upsilon+2(C_2+C_\theta+C_\Delta),C_\Upsilon+2C_\Delta\}\) is finite and universal. | `def-extended-epsilon-cstar-algebra` | `lem-routef-delta-upsilon-telescope`; `lem-routef-multiplicative-telescope`; `lem-routef-upsilon-delta-telescope` | G-ledger §3, (3.3); verdict | 5 / 2 |
| `lem-routef-threshold-minimum` | lemma / `proved-mod-audit` | Route F common threshold: there is a universal \(\eta_K>0\), equal to the finite minimum of the functional-calculus, MAIN-CB, H-CB, EXT-CB, selection, split, CP-normalization, degree-two/three, and PRH guards produced by its dependencies, such that \(0\le\eta\le\eta_K\) implies every local smallness hypothesis in the Route F factorization. | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-main-radius-ledger`; `lem-routef-ai-defect-linearization`; `lem-routef-delta-normalization-closeness`; `lem-routef-degree-three-estimate`; `lem-routef-upsilon-prime-closeness`; `lem-routef-upsilon-normalization-closeness`; `lem-routef-k-finiteness` | G-ledger §4; Stage-1 verdict corrected minimum; design verdict exact replacement | 8 / 3 |
| `lem-routef-prh-finish` | lemma / `proved-mod-audit` | Route F PRH finish: let \(A:\ell_\infty^k\to\ell_\infty^n\) and \(M:\ell_\infty^n\to\ell_\infty^k\) be positive unital maps and let \(Q\) be row-stochastic; if \(K\ge1\), \(0\le\eta\le\min\{(24K)^{-1},1\}\), \(\lVert Q-AM\rVert_{\infty\to\infty}\le K\eta\), and \(\lVert MA-I\rVert_{\infty\to\infty}\le3K\eta/(1-3K\eta)\), then there is a stochastic idempotent \(E\) with \(\lVert Q-E\rVert_{\infty\to\infty}\le(K+4\sqrt{2K})\sqrt\eta\). | `def-positive-approximate-retract`; `def-stochastic` | `lem-prh`; `lem-routef-threshold-minimum` | G-ledger §5; G-verdict Finish; PRH export | 5 / 3 |

### 2.6 Phase-5 GAP reservations — not result rows

| reserved id | disposition | why no contract is supplied |
|---|---|---|
| `gap-routef-f2-positive-unital-compression-contract` | **GAP / DO NOT SHARD OR SEED** | The permitted F2 material does not expose one reviewed, closed hypothesis block that constructs the positive-unital maps \(A,M\) required by `lem-routef-prh-finish`. |
| `gap-routef-f3-retract-defect-contract` | **GAP / DO NOT SHARD OR SEED** | The permitted F3 material does not expose one reviewed, closed contract producing the bound \(\lVert MA-I\rVert\le3K\eta/(1-3K\eta)\) from the preceding UCP estimates. |

The names reserve review targets only. They have no `contract:`, `status:`,
`defs:`, or `deps:` fields and therefore are not part of the 84-row proposal.

## 3. Assembly wiring

No `routes:` field is proposed. These are conjunctive decompositions. Every
existing parent contract remains byte-for-byte unchanged.

### 3.1 `conj-hcb`

Proposed direct imports:

```yaml
deps: lem-hcb2-amplified-adjointness; lem-hcb2-product-defect; lem-hcb3-diagonal-unit; lem-hcb3-diagonal-upper-norm; lem-hcb3-diagonal-lower-modulus; lem-hcb3-diagonal-inverse; lem-hcb3-offdiagonal-inverse; lem-hcb4-canonical-closeness; lem-hcb4-canonical-inverse
```

Projected parent workspace: root plus nine validated imports, **10 nodes /
depth 2**. COMP-CB, corrected COL-HILB, HCB-0/HCB-1, and the Gram estimate
remain transitive and are not duplicated at the parent.

### 3.2 `conj-extcb`

Proposed direct imports:

```yaml
deps: conj-hcb; lem-extcb1-cross-corner-dimension; lem-extcb2-exact-representation; lem-extcb2-spatial-corner-system; lem-extcb3-four-ha-inverses; lem-extcb4-transported-corners; lem-extcb4-complete-merging-datum; lem-extcb-four-corner-merge
```

Projected parent workspace: root plus eight validated imports, **9 nodes /
depth 2**. The parent is never an import of an EXT-CB child; `def-extcb-datum`
closes each child's hypotheses.

### 3.3 `lem-thmainext-conditional`

Proposed direct imports:

```yaml
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-maincb-error-improvement; lem-maincb-uniform-reset-chain; lem-maincb-structural-assembly; lem-extcb-four-corner-merge
```

Projected parent workspace: root plus seven validated imports, **8 nodes /
depth 2**, but only after all five `stated` structural rows have independent
prover/verifier outcomes and the exact-target approximation gap inherited by
IMPROVE-CB is factored. Until then the operational disposition is:

`REFACTOR: structural assembly not yet af-sized; do not seed the parent.`

The deleted `lem-stage1-two-side-packet` appears nowhere in this wiring.

### 3.4 `lem-routef-k-ledger`

**DO NOT REWIRE OR SEED.** The existing contract stays unchanged. The three
telescopes, \(K\)-finiteness, threshold, and PRH-finish rows do not themselves
construct the positive-unital \(A,M\) or the F3 retract-defect estimate.
Accordingly there is no proposed `deps:` replacement and no projected node
count.

Only after Phase 5 extracts two closed result contracts from the F2/F3
material, gives them honest statuses, and obtains a fresh hostile architecture
review may a later design add those reviewed rows alongside:

```text
lem-routef-delta-upsilon-telescope
lem-routef-multiplicative-telescope
lem-routef-upsilon-delta-telescope
lem-routef-k-finiteness
lem-routef-threshold-minimum
lem-routef-prh-finish
```

Current projection: **REFACTOR / BLOCKED ON F2-F3 STOCHASTIC-RETRACT BRIDGE**.

### 3.5 Existing leaves

`lem-kitaev-diagonal-repair`, `cor-kitaev-diagonal-cpization`,
`lem-kitaev-almost-idemp-audit`, and `lem-prh` receive no contract or
dependency change. No proposal here changes any parent contract or existing
leaf contract.

## 4. Definition and external-input provisioning

### 4.1 Proposed definition shards

Exactly 17 definition shards are proposed. “Cited” remains conditional on a
local byte-match; `consensus` and `original` remain draft until sign-off.

| proposed def id | canonical term | proposed kind/status | source locus or rationale | used by |
|---|---|---|---|---|
| `def-epsilon-cstar-algebra` | \(\varepsilon\)-\(C^*\)-algebra | `cited` / lock after byte-match | pinned TeX 407–440, including approximate unit | Stage 1 and source premises |
| `def-delta-projection` | \(\delta\)-projection and nonvanishing alternative | `cited` / lock after byte-match | pinned TeX 917–929 | COMP/H/EXT/MAIN |
| `def-one-dimensional-delta-projection` | one-dimensional \(\delta\)-projection and equivalence | `cited` / lock after byte-match | pinned TeX 1064–1066, 1187 | H/EXT/MAIN |
| `def-compressed-corner` | \(Co_{P,Q}\), \(S_{P,Q}\), compressed product and unit | `cited` / lock after byte-match | pinned TeX 1054–1082; exclude printed index typo | COMP/H/EXT/MAIN |
| `def-column-hilbert-corner` | level-one and amplified column-Hilbert corner | `cited` / lock after byte-match | pinned TeX 1123–1149, 1546–1550; exclude false unsquared display | COL-HILB and Ha |
| `def-extended-delta-inclusion` | extended \(\delta\)-inclusion/isomorphism | `consensus` / `draft` pending sign-off | harmonizes pinned TeX 443–456 with 1477–1484; no single verbatim source block | COMP/EXT/MAIN/ledger |
| `def-operator-space` | operator space and rectangular matrix norms | `cited` / lock after byte-match | pinned TeX 1453–1475 | amplified contracts |
| `def-four-corner-merging-datum` | amplified four-corner merging datum | `original` / `draft` pending sign-off | project packaging of the four hypotheses at pinned TeX 1325–1345; not a source definition | EXT/MAIN |
| `def-projection-basis` | projection basis of a finite-dimensional commutative \(C^*\)-algebra | `cited` / lock after byte-match | pinned TeX 1361–1364 | EXT/MAIN |
| `def-compressed-associator` | \((A\cdot B)\cdot C-A\cdot(B\cdot C)\) | `original` / `draft` pending sign-off | project name over the source compressed product | HCB-0/HCB-1 |
| `def-canonical-corner-identifications` | canonical \(J_{P,Q,n},J_{Q,P,n}\) identifications | `original` / `draft` pending sign-off | faithful packaging of H-CB §8 notation | HCB-4 |
| `def-spatial-four-corner-system` | \(\mu_{jk}(A)=U_jAU_k^\dagger\) and its fixed amplifications | `original` / `draft` pending sign-off | faithful packaging of EXT-CB §3.6 / pinned TeX 1404 | EXT-CB-2/4 |
| `def-approximate-unitary-space` | notation \(\mathcal U,\mathcal U_e,u,\sigma\) only | `consensus` / `draft` pending sign-off | pinned notation 692–697 and 809–892; excludes existence, differentiability, chart estimates, IFT, and isolation | Stage 1 |
| `def-h-space-left-inversion` | H-space and left inversion | `cited` / lock after byte-match | pinned TeX 895–912, definition only | Stage-1 topology |
| `def-lefschetz-fixed-point-data` | Lefschetz number and local fixed-point index | `cited` / lock after byte-match | pinned TeX 957–967, definitions only | Stage-1 topology |
| `def-extcb-datum` | closed EXT-CB datum | `original` / `draft` pending sign-off | \(\mathcal A,P,Q,v,r,e\) hypothesis package prescribed by the hostile verdict | EXT-CB children |
| `def-augmentation-filtration` | augmentation ideal and its filtration in graded cohomology | `original` / `draft` pending sign-off | project packaging of pinned TeX 1017–1049; carries notation only, not the associated-graded theorem | Stage-1 trace |

The exact proposed `def-extcb-datum` content is: an extended
\(\varepsilon\)-\(C^*\)-algebra \(\mathcal A\); \(\delta\)-projections \(P,Q\)
with \(\lVert P+Q-I\rVert\le\delta\); an extended
\(\delta\)-isomorphism \(v:M_r\to S_P\); \(\dim S_Q=1\); and
\(S_{P,Q}\ne0\), with \(e=\delta+\varepsilon\).

Existing `def-extended-epsilon-cstar-algebra`, `def-ha-map`,
`def-fd-cstar-diagonal`, `def-almost-idempotent`,
`def-positive-approximate-retract`, and `def-stochastic` are reused unchanged.
The v1 composite `def-canonical-corner-system` proposal is deleted.

### 4.2 Stage-1 external-input register

| input actually consumed | proposed row | acquisition / status gate |
|---|---|---|
| Free proper smooth action gives quotient manifold and submersion. | `lem-topology-quotient-manifold` | Lee Thm 21.10; local acquisition and byte-match before `cited`. |
| Compact \(C^1\) manifold has finite triangulation / finite-CW type. | `lem-topology-finite-triangulation` | Whitehead or Cairns; choose an exact \(C^1\), compact statement. |
| Lefschetz-Hopf index sum. | `lem-topology-lefschetz-hopf` | Arkowitz–Brown exact theorem required. |
| Nondegenerate local index is \(\operatorname{sgn}\det(I-Df)\). | `lem-topology-local-index-sign` | Granas–Dugundji exact differentiable statement required. |
| Closed orientable manifold has nonzero top real cohomology. | `lem-topology-orientable-top-cohomology` | Exact source must include connected, compact, orientable, and without boundary. |
| Cohomological Künneth cross product. | `lem-topology-kunneth-cross-product` | Hatcher Thm 3.16 after byte-match. |
| Finite-dimensional Hopf structure is exterior on odd generators. | `lem-topology-hopf-structure` | Hatcher Thm 3C.4 only if the non-coassociative bialgebra hypotheses match exactly. |

The quantitative inverse-function theorem is deliberately a local `stated`
result row, not a cited definition and not hidden inside
`def-approximate-unitary-space`. The polar and derivative contracts likewise
remain results requiring architecture review.

## 5. Phase map and strictly serial seeding order

No `af` workspace is authorized by this design. The order below applies only
after the corresponding definitions, source acquisitions, contracts, and
fresh hostile architecture review have cleared.

### Phase 2 — COMP-CB then H-CB (`aism-niwk`)

1. Provision the algebra/corner definitions.
2. Seed the five COMP-CB rows in dependency order.
3. Seed H-CB by layers: identities/Gram/COL-HILB; associator/action/product;
   diagonal and canonical estimates; inverse propagation.
4. Seed existing parent `conj-hcb` last.

### Phase 3 — EXT-CB (`aism-fgr7`)

1. Provision `def-extcb-datum`, the two separated corner-system definitions,
   and the original merging datum.
2. Resolve and factor **GAP-EA** before seeding the exact-target or
   IMPROVE-CB chains.
3. Prove the five `stated` source-premise rows, then the seven EXT-CB children
   strictly bottom-up.
4. Seed existing parent `conj-extcb` last.

### Phase 4 — Stage 1, MAIN-CB, and the relative ledger

1. Acquire and byte-match all seven topology leaves.
2. Review the quantitative-IFT contract; then seed exact-unit, polar-chart,
   derivative, isolation, quotient, cohomology, trace, and fixed-class rows in
   dependency order.
3. Seed the projection, complementary-pair, fresh-side, old-side, split-corner,
   and error-improvement rows only after GAP-EA closes.
4. Seed the three raw-reset rows, then the uniform reset row.
5. Treat all five structural rows as new `stated` glue; give each its own
   prover and independent verifier, bottom-up.
6. Seed `lem-thmainext-conditional` only after the preceding subtree closes.
7. Seed the 19 relative ledger rows bottom-up. This does **not** authorize the
   ledger parent.

### Phase 5 — stochastic-retract interface (`aism-fudw`)

1. Return to the permitted F2/F3 artifacts and extract minimal, closed,
   self-contained contracts for the two reserved GAPs.
2. Obtain a fresh hostile architecture review of those contracts and factor
   them further if either exceeds the ≤12-node/depth-3 envelope.
3. Only then create result rows, seed them, and prepare a new
   `lem-routef-k-ledger` dependency proposal.
4. F0/root work remains separate and downstream; this design creates no F0
   row and no root theorem claim.

All orchestration is serial. A node that balloons is factored; the node cap is
never raised to absorb missing mathematics.

## 6. Risk register

| id | risk | required control |
|---|---|---|
| R1 | The five EXT-CB source premises, quantitative IFT, and IMPROVE-CB are consumed by campaign artifacts but not proved by the permitted proof packets. | Keep all seven `stated`; never cite the repaired theorem proof as ground truth. |
| R2 | The seven topology leaves are not in local `refs/`. | Acquire, hash, byte-match, and record exact theorem loci before changing `cited candidate` to `cited`. |
| R3 | The Hopf theorem may require stronger associativity/coassociativity hypotheses than the Stage-1 H-space supplies. | Match hypotheses exactly; if they fail, do not seed the exterior-cohomology row. |
| R4 | H-CB inverse propagation is conditional at level one. | Preserve the level-one bijectivity/lower-modulus hypotheses in HCB-3 contracts. |
| R5 | The HCB-4 inverse step needs an explicit small Neumann radius. | Put the shrink in the future shard body; never infer invertibility from closeness without it. |
| R6 | Close idempotents can have different ranks outside the uniform close-compression radius. | Keep `e_close` explicit in `lem-extcb1-close-corner-dimension`. |
| R7 | Spatiality can be accidentally chosen independently at each amplification. | `def-spatial-four-corner-system` fixes one level-one \(U_1\) and amplifies it by \(I_m\otimes U_1\). |
| R8 | Stage-1 old and fresh sides have different defects. | Keep \(\varepsilon_0\) and \(\varepsilon_S\) distinct; use `lem-maincb-split-corner-defect` only for their comparison. |
| R9 | Exact-target approximation still hides a Newton/diagonal chain. | **GAP-EA: REFACTOR BEFORE SEEDING; do not raise the node cap.** |
| R10 | The isolation-to-nonvanishing shrink was prose-only in the prover artifact. | Future complementary-pair body must include the verifier's \(e_{\mathrm{nv}}\) shrink. |
| R11 | The polar-chart contract may still package too much analytic work. | Hostile architecture review before seeding; split again if its af plan exceeds 7/3. |
| R12 | The associated-graded action can hide the augmentation-filtration induction. | Keep exterior structure, associated-graded action, and trace in three distinct rows. |
| R13 | Quotient manifold and finite-CW type were compound. | Keep the two rows separate and retain \(1<\dim\mathcal X<\infty\) plus “without boundary.” |
| R14 | MAIN reset arithmetic and MAIN structural existence are independent obligations. | Keep three raw rows plus uniform reset separate from the five `stated` structural rows. |
| R15 | Structural MAIN wording is new glue, not a verified artifact result. | All five rows start `stated` and receive separate prover/verifier passes. |
| R16 | The Stage-1 maximality claim may not establish strict progress in its present contract. | Prover must identify the finite monotone measure; otherwise refactor or challenge, never weaken silently. |
| R17 | The equivalence relation and block-size assignment may be two proof obligations. | If the 4/2 projection fails, split the row before any orchestration. |
| R18 | `lem-routef-upsilon-prime-closeness` is the longest relative ledger leaf. | Start at the stated 10/3 cap and factor componentwise if it balloons. |
| R19 | The ledger's \(C_3\) formerly had no producer. | Keep `lem-routef-degree-three-estimate` as a direct threshold dependency. |
| R20 | \(C_2\) is still produced inside the repaired Delta chain rather than by a dedicated proposal row. | Link its exact producing inequality in the future Delta shard body; split if a verifier rejects that interface. |
| R21 | Four ledger inequalities formerly omitted their common range. | Preserve \(0\le\eta\le\eta_A\) in Delta-product and all three telescope contracts. |
| R22 | The printed EXT-CB dimension locus contains a cardinality typo. | Record the typo and use only the corrected reviewed statement; do not call the source print byte-correct. |
| R23 | Composite definitions can smuggle theorem content. | Keep polar/IFT facts out of definitions; keep merging and corner-system packages `original/draft`. |
| R24 | Parent projections can conceal transitive mathematics. | Count only genuinely validated/cited imports as external; remeasure after each actual af plan. |
| R25 | No safe closed F2 positive-unital compression contract is present. | Keep the reserved id uncontracted and the ledger parent blocked. |
| R26 | No safe closed F3 retract-defect contract is present. | Keep the reserved id uncontracted and the ledger parent blocked. |
| R27 | PRH cannot be applied from norm bounds alone. | Retain the positive-unital hypotheses on \(A,M\) verbatim in `lem-routef-prh-finish`. |
| R28 | A future architect could mistake the 84-row table for authorization to seed. | Phase gates and §7 explicitly say this design is not globally seedable. |
| R29 | Author review cannot satisfy reviewer ≠ author. | Every substantive row and this architecture require a fresh independent reviewer. |
| R30 | A `proved-mod-audit` label can be misread as rigorous. | No proposal is L0-rigorous; promotion requires the repository's byte-matched/af/Lean and independent-review gates. |

## 7. Honest closure statement

This v2 proposal is **not globally seedable**. It supplies the explicit COMP-CB
subtree, removes the EXT parent/child cycle, and factors the Stage-1 analytic,
trace, reset, and MAIN structural packets into named rows. Those repairs are
architecture only: the quantitative IFT and all newly phrased structural glue
remain `stated`, topology leaves remain unacquired `cited candidate` inputs,
and every substantive row still needs fresh independent review.

Three named contract gaps remain. **GAP-EA** blocks the exact-target
approximation and therefore IMPROVE-CB; the **F2 positive-unital compression**
and **F3 retract-defect** interfaces have no safe contracts in the permitted
artifacts. The last two are deliberately uncontracted, so
`lem-routef-k-ledger` remains **DO NOT REWIRE OR SEED**. No parent is to be
seeded until its inputs have closed contracts, honest statuses, credible
≤12-node/depth-3 projections, and a fresh hostile architecture review.

This document proposes no mathematical proof, no status promotion, no parent
contract change, no route change, and no registry mutation.
