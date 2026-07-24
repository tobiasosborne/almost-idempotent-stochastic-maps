# DESIGN — aism-fudw Route F decomposition into af-sized registry proposals

Date: 2026-07-24  
Role: fresh decomposition architect  
Scope: design only; no registry/definition/proof edits and no new mathematics

## 0. Status and notation

This document factors only the mathematics already present in the four W74F
proof/verdict packets named in `BRIEF-FUDW-DESIGN.md`, using
`DECOMP-W74F-C-THMAINEXT.md` only for the assembly interfaces it records.  It
does not promote a result.  A row marked `proved-mod-audit` is a proposal to
transcribe a hostile-verified artifact section at that same non-L0 rung.

Rows marked `stated` are source-level premises consumed by the verified
artifacts but not proved in one of the four permitted proof packets.  They must
receive their own prover pass before af validation.  Rows marked
`cited candidate` must not be instantiated as `cited` until the named source is
acquired under `refs/`, hashed, and the contract is byte-matched.

Symbols used in the contracts have the meanings in the proposed definition
list in §3.  Existing definitions are written without a `P:` prefix; proposed
ones are written `P:def-...`.  The projected node count includes the workspace
root but treats a future validated/cited import as one external leaf.  It is an
architecture estimate, not an af run.

There are **64 proposed result shards**:

- 14 for the corrected column/H-CB subtree;
- 12 for the EXT-CB subtree, including five deliberately `stated` source
  premises;
- 20 for Stage 1 / MAIN-CB, including seven contingent cited topology leaves
  and one deliberately `stated` improvement premise;
- 18 for the relative Route F ledger and PRH finish.

No new mathematical glue statement is introduced.  No genuine mathematical
gap was found in the supplied hostile-verified packets.  The unresolved work is
formalisation/provisioning: six `stated` premise leaves and seven external
reference acquisitions.

## 1. Proposal table

### 1.1 Phase 2 — corrected COL-HILB and H-CB

| proposed id | kind / status | contract (verbatim proposed one-line `contract:` value) | defs | deps | provenance locus | projected af |
|---|---|---|---|---|---|---|
| `lem-hcb-column-hilbert-squared` | lemma / `proved-mod-audit` | Corrected amplified column-Hilbert estimate: there are universal \(C_{\mathrm{col}}<\infty\) and \(e_{\mathrm{col}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{col}}\), every level-one one-dimensional \(\delta\)-projection \(Q\), every \(\delta\)-projection \(P\), every \(n\ge1\), and every \(X\in M_{n,1}\otimes S_{P,Q}\) satisfy \(\lvert\langle X,X\rangle_n-\lVert X\rVert_{n,1}^2\rvert\le C_{\mathrm{col}}e\lVert X\rVert_{n,1}^2\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | `DECOMP-W74F-C-THMAINEXT.md` §4.1–4.3; `PROOF-W74F-E-HCB.md` §1.2; `VERDICT-W74F-E-HCB.md` checks 2–3 | 6 / 3 |
| `lem-hcb0-compressed-associator` | lemma / `proved-mod-audit` | Uniform compressed associator: there are universal \(C_{\mathrm{as}}<\infty\) and \(e_{\mathrm{as}}>0\) such that, whenever \(e=\delta+\varepsilon\le e_{\mathrm{as}}\), all compatible amplified rectangular compressed corners satisfy \(\lVert(A\mathbin{\cdot}B)\mathbin{\cdot}C-A\mathbin{\cdot}(B\mathbin{\cdot}C)\rVert\le C_{\mathrm{as}}e\lVert A\rVert\lVert B\rVert\lVert C\rVert\). | `def-extended-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner`; P:`def-compressed-associator` | — | `PROOF-W74F-E-HCB.md` §3 (HCB-0); verdict HCB-0 `VALID` | 5 / 2 |
| `lem-hcb1-variational-identity` | lemma / `proved-mod-audit` | Amplified Ha variational identity: for every \(n\ge1\), \(Z\in M_n\otimes S_{P,R}\), \(X\in M_{n,1}\otimes S_{R,Q}\), and \(Y\in M_{n,1}\otimes S_{P,Q}\), one has \(2\langle Y,(Ha^Q_{P,R})_n(Z)X-Z\mathbin{\cdot}X\rangle u_Q=(Y^\dagger\mathbin{\cdot}Z)\mathbin{\cdot}X-Y^\dagger\mathbin{\cdot}(Z\mathbin{\cdot}X)\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | `PROOF-W74F-E-HCB.md` §4 (HCB-1a); verdict HCB-1a `VALID` | 4 / 2 |
| `lem-hcb1-column-action` | lemma / `proved-mod-audit` | Uniform Ha column action: there are universal \(C_{\mathrm{act}}<\infty\) and \(e_{\mathrm{act}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{act}}\), every admissible \(P,Q,R,n,Z,X\) satisfies \(q_P((Ha^Q_{P,R})_n(Z)X-Z\mathbin{\cdot}X)\le C_{\mathrm{act}}e\lVert Z\rVert q_R(X)\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner`; P:`def-compressed-associator` | `lem-hcb-column-hilbert-squared`; `lem-hcb0-compressed-associator`; `lem-hcb1-variational-identity` | `PROOF-W74F-E-HCB.md` §5 (HCB-1b); verdict HCB-1b `VALID` | 6 / 3 |
| `lem-hcb2-amplified-adjointness` | lemma / `proved-mod-audit` | Exact amplified Ha adjointness: for every \(n\ge1\) and \(Z\in M_n\otimes S_{P,R}\), \((Ha^Q_{P,R})_n(Z)^\dagger=(Ha^Q_{R,P})_n(Z^\dagger)\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | `PROOF-W74F-E-HCB.md` §6.1 (HCB-2); verdict HCB-2 `VALID` | 2 / 1 |
| `lem-hcb2-product-defect` | lemma / `proved-mod-audit` | Uniform amplified Ha product defect: there are universal \(C_{\mathrm{prod}}<\infty\) and \(e_{\mathrm{prod}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{prod}}\), \(\lVert(Ha^Q_{P,R})_n(Z\mathbin{\cdot}W)-(Ha^Q_{P,S})_n(Z)(Ha^Q_{S,R})_n(W)\rVert\le C_{\mathrm{prod}}e\lVert Z\rVert\lVert W\rVert\) at every amplification. | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb0-compressed-associator`; `lem-hcb1-column-action` | `PROOF-W74F-E-HCB.md` §6.2 (HCB-2); verdict HCB-2 `VALID` | 6 / 3 |
| `lem-hcb3-diagonal-unit` | lemma / `proved-mod-audit` | Uniform diagonal Ha unit estimate: there are universal \(C_{\mathrm{unit}}<\infty\) and \(e_{\mathrm{unit}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{unit}}\), \(\lVert(Ha^Q_{P,P})_n(I_n\otimes u_P)-I\rVert\le C_{\mathrm{unit}}e\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb1-column-action` | `PROOF-W74F-E-HCB.md` §7.1 (HCB-3); verdict HCB-3 `VALID-WITH-CORRECTIONS` | 4 / 2 |
| `lem-hcb3-diagonal-upper-norm` | lemma / `proved-mod-audit` | Uniform diagonal Ha upper norm: there are universal \(C_{\mathrm{up}}<\infty\) and \(e_{\mathrm{up}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{up}}\), \(\lVert(Ha^Q_{P,P})_n(Z)\rVert\le(1+C_{\mathrm{up}}e)\lVert Z\rVert\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb2-amplified-adjointness`; `lem-hcb2-product-defect` | `PROOF-W74F-E-HCB.md` §7.2 (HCB-3); verdict HCB-3 `VALID-WITH-CORRECTIONS` | 5 / 3 |
| `lem-hcb3-diagonal-lower-modulus` | lemma / `proved-mod-audit` | Diagonal Ha lower-modulus propagation: there are universal \(C_{\mathrm{diag}}<\infty\) and \(e_{\mathrm{diag}}>0\) such that, if \(e=\delta+\varepsilon\le e_{\mathrm{diag}}\) and the level-one lower modulus of \(Ha^Q_{P,P}\) is at least \(1/4\), then \(\lVert(Ha^Q_{P,P})_n(Z)\rVert\ge(1-C_{\mathrm{diag}}e)\lVert Z\rVert\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-hcb2-amplified-adjointness`; `lem-hcb2-product-defect` | `PROOF-W74F-E-HCB.md` §7.3, equations (7.5)–(7.9); verdict HCB-3 `VALID-WITH-CORRECTIONS` | 8 / 3 |
| `lem-hcb3-diagonal-inverse` | lemma / `proved-mod-audit` | Diagonal Ha inverse propagation: under the hypotheses of `lem-hcb3-diagonal-lower-modulus`, if \(Ha^Q_{P,P}\) is bijective at level one, then every amplification is bijective and \(\lVert((Ha^Q_{P,P})_n)^{-1}\rVert\le1+C_{\mathrm{inv}}e\) for one universal \(C_{\mathrm{inv}}\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-column-hilbert-corner` | `lem-hcb3-diagonal-lower-modulus` | `PROOF-W74F-E-HCB.md` §7.3, equation (7.10); verdict HCB-3 `VALID-WITH-CORRECTIONS` | 3 / 2 |
| `lem-hcb3-offdiagonal-inverse` | lemma / `proved-mod-audit` | Off-diagonal Ha inverse propagation: there are universal \(C_{\mathrm{rect}}<\infty\) and \(e_{\mathrm{rect}}>0\) such that, when \(e\le e_{\mathrm{rect}}\), \(Ha^Q_{P,R}\) is bijective at level one, and \(Ha^Q_{R,R}\) has level-one lower modulus at least \(1/4\), every amplification of \(Ha^Q_{P,R}\) is bijective with inverse norm at most \(1+C_{\mathrm{rect}}e\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-column-hilbert-corner` | `lem-hcb2-amplified-adjointness`; `lem-hcb2-product-defect`; `lem-hcb3-diagonal-lower-modulus` | `PROOF-W74F-E-HCB.md` §7.4 (HCB-3); verdict HCB-3 `VALID-WITH-CORRECTIONS` | 6 / 3 |
| `lem-hcb4-canonical-gram` | lemma / `proved-mod-audit` | Canonical corner Gram estimate: there are universal \(C_J<\infty\) and \(e_J>0\) such that, for \(e=\delta+\varepsilon\le e_J\), the canonical maps \(J_{P,Q,n}\) and \(J_{Q,P,n}\) satisfy \((1-C_Je)\lVert Z\rVert\le\lVert J_n(Z)\rVert\le(1+C_Je)\lVert Z\rVert\) at every amplification. | P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner`; P:`def-canonical-corner-system` | — | `PROOF-W74F-E-HCB.md` §8.1–8.2 (HCB-4); verdict HCB-4 `VALID-WITH-CORRECTIONS` | 6 / 3 |
| `lem-hcb4-canonical-closeness` | lemma / `proved-mod-audit` | Canonical Ha closeness: there are universal \(C_{\mathrm{sp}}<\infty\) and \(e_{\mathrm{sp}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{sp}}\), \(\max\{\lVert(Ha^Q_{P,Q})_n-J_{P,Q,n}\rVert,\lVert(Ha^Q_{Q,P})_n-J_{Q,P,n}\rVert\}\le C_{\mathrm{sp}}e\) for every \(n\ge1\). | `def-ha-map`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner`; P:`def-canonical-corner-system` | `lem-hcb-column-hilbert-squared`; `lem-hcb1-column-action`; `lem-hcb2-amplified-adjointness`; `lem-hcb4-canonical-gram` | `PROOF-W74F-E-HCB.md` §8.3 (HCB-4); verdict HCB-4 `VALID-WITH-CORRECTIONS` | 7 / 3 |
| `lem-hcb4-canonical-inverse` | lemma / `proved-mod-audit` | Canonical Ha inverse estimate: there are universal \(C_{\mathrm{sp,inv}}<\infty\) and \(e_{\mathrm{sp,inv}}>0\) such that, for \(e=\delta+\varepsilon\le e_{\mathrm{sp,inv}}\), the special maps \(Ha^Q_{P,Q}\) and \(Ha^Q_{Q,P}\) are completely bijective and their amplified inverses differ from the corresponding canonical inverses by at most \(C_{\mathrm{sp,inv}}e\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-column-hilbert-corner`; P:`def-canonical-corner-system` | `lem-hcb4-canonical-gram`; `lem-hcb4-canonical-closeness` | `PROOF-W74F-E-HCB.md` §8.3, equations (8.12)–(8.13); HCB verdict correction requiring the Neumann condition | 5 / 3 |

### 1.2 Phase 3 — EXT-CB

The first five rows are **not** promoted from the printed paper.  They are
deliberately proposed as `stated` because the EXT-CB packet consumes them as
premises but the permitted hostile-verified artifact does not itself prove
them.

| proposed id | kind / status | contract (verbatim proposed one-line `contract:` value) | defs | deps | provenance locus | projected af |
|---|---|---|---|---|---|---|
| `lem-extcb-one-dimensional-product` | lemma / `stated` | Level-one one-dimensional corner product: there are universal \(C_{PQR}<\infty\) and \(e_{PQR}>0\) such that, for \(e=\delta+\varepsilon\le e_{PQR}\), if \(Q\) is one-dimensional then \(\lvert\lVert X\mathbin{\cdot}Y\rVert-\lVert X\rVert\lVert Y\rVert\rvert\le C_{PQR}e\lVert X\rVert\lVert Y\rVert\) for \(X\in S_{P,Q}\) and \(Y\in S_{Q,R}\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | — | pinned TeX `lem_PQR`, `tex:1162-1177`; consumed in `PROOF-W74F-F-EXTCB.md` §2 and its verdict | 5 / 3, uncertain until prover |
| `lem-extcb-one-dimensional-corner-dimension` | lemma / `stated` | Level-one one-dimensional corner dimension: for sufficiently small universal \(\delta+\varepsilon\), if \(P\) and \(Q\) are one-dimensional \(\delta\)-projections then \(\dim S_{P,Q}\le1\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-extcb-one-dimensional-product` | pinned TeX `lem_1d_proj`, `tex:1179-1185`; consumed in EXT-CB §2 and verdict EXTCB-1 | 4 / 2, uncertain until prover |
| `lem-extcb-corner-dimension-additivity` | lemma / `stated` | Level-one corner-dimension additivity: for two finite-dimensional commutative \(C^*\)-algebras with projection bases and non-unital sufficiently accurate inclusions \(v,w\), the compressed corner \(S_{v(I),w(I)}\) is linearly bijective to \(\bigoplus_{j,k}S_{v(\Pi_j),w(\Sigma_k)}\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-compressed-corner`; P:`def-extended-delta-inclusion`; P:`def-projection-basis` | — | pinned TeX `lem_add_dim`, `tex:1363-1369`, with the printed second-cardinality typo noted in DECOMP defect 7; consumed in EXT-CB §2 | 8 / 3, uncertain until prover |
| `lem-extcb-exact-target-approximation` | lemma / `stated` | Exact-target complete approximation: there are universal \(C_{\mathrm{app}}<\infty\), \(a_{\mathrm{app}}>0\) such that every extended \(\alpha\)-homomorphism \(T:M_r\to B(H)\) with \(\alpha\le a_{\mathrm{app}}\) is completely \(C_{\mathrm{app}}\alpha\)-close to one exact unital \(*\)-homomorphism \(\mu:M_r\to B(H)\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-operator-space` | — | premise `APP` in `PROOF-W74F-F-EXTCB.md` §1.2; pinned TeX `lem_approx_ext`, `tex:1508-1535`; verdict premise ledger `VALID` only conditionally on this premise | 9 / 3, uncertain until prover |
| `lem-extcb-four-corner-merge` | lemma / `stated` | Complete four-corner merge: there are universal \(C_{\mathrm{merge}}<\infty\), \(a_{\mathrm{merge}}>0\) such that four fixed bijective level-one corner maps satisfying the amplified merging datum with common defect \(\rho\le a_{\mathrm{merge}}\) combine into one extended \(C_{\mathrm{merge}}(\rho+\varepsilon)\)-isomorphism. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner`; P:`def-four-corner-merging-datum` | — | premise `MERGE` in `PROOF-W74F-F-EXTCB.md` §1.3; pinned TeX `lem_merging`, `tex:1325-1359`; verdict premise ledger `VALID` only conditionally on this premise | 9 / 3, uncertain until prover |
| `lem-extcb1-close-corner-dimension` | lemma / `proved-mod-audit` | Close-compression range invariance: there is a universal \(e_{\mathrm{close}}>0\) such that, in the EXT-CB setup with \(e=\delta+\varepsilon\le e_{\mathrm{close}}\), the compression ranges \(S_{v(I_r),Q}\) and \(S_{P,Q}\) have the same dimension. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-compressed-corner` | — | EXT-CB verdict EXTCB-1 correction (close idempotents at distance \(<1\)); `PROOF-W74F-F-EXTCB.md` §2 as corrected | 5 / 3 |
| `lem-extcb1-cross-corner-dimension` | lemma / `proved-mod-audit` | EXT-CB cross-corner dimension: under the hypotheses of `conj-extcb` and a universal smallness threshold, \((\dim S_{P,Q},\dim S_{Q,Q})=(r,1)\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-projection-basis` | `lem-extcb-one-dimensional-corner-dimension`; `lem-extcb-corner-dimension-additivity`; `lem-extcb1-close-corner-dimension` | `PROOF-W74F-F-EXTCB.md` §2 (EXTCB-1); verdict EXTCB-1 `VALID-WITH-CORRECTIONS` | 7 / 3 |
| `lem-extcb2-exact-representation` | lemma / `proved-mod-audit` | EXT-CB exact representation: under the hypotheses of `conj-extcb`, there is one exact unital \(*\)-homomorphism \(\mu_{11}:M_r\to B(S_{P,Q})\) such that \(\lVert(\mu_{11})_m-(Ha^Q_{P,P})_m v_m\rVert\le\kappa e\) for every amplification \(m\), with universal \(\kappa\). | `def-extended-epsilon-cstar-algebra`; `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `conj-hcb`; `lem-extcb-exact-target-approximation` | `PROOF-W74F-F-EXTCB.md` §3 (EXTCB-2); verdict EXTCB-2 `VALID` | 7 / 3 |
| `lem-extcb2-spatial-corner-system` | lemma / `proved-mod-audit` | EXT-CB spatial corner system: under the hypotheses of `conj-extcb`, the exact representation \(\mu_{11}\) is implemented by one level-one unitary \(U_1:\mathbb C^r\to S_{P,Q}\), and together with the normalized \(U_2:\mathbb C\to S_{Q,Q}\) it defines one exact spatial four-corner system \(\mu_{jk}\) whose amplifications use \(I_m\otimes U_j\). | P:`def-canonical-corner-system`; P:`def-column-hilbert-corner`; P:`def-compressed-corner`; P:`def-extended-delta-inclusion` | `lem-extcb1-cross-corner-dimension`; `lem-extcb2-exact-representation` | `PROOF-W74F-F-EXTCB.md` §3, equations (3.5)–(3.7); verdict EXTCB-2 `VALID` | 5 / 3 |
| `lem-extcb3-four-ha-inverses` | lemma / `proved-mod-audit` | EXT-CB four Ha inverses: under the hypotheses of `conj-extcb` and a universal smallness threshold, every \(Ha^Q_{P_j,P_k}\) is bijective at level one and all its amplifications have norm and inverse norm between \(1-Ce\) and \(1+Ce\) for one universal \(C\). | `def-ha-map`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-one-dimensional-delta-projection`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `conj-hcb`; `lem-extcb2-exact-representation` | `PROOF-W74F-F-EXTCB.md` §4 (EXTCB-3); verdict EXTCB-3 `VALID` | 7 / 3 |
| `lem-extcb4-transported-corners` | lemma / `proved-mod-audit` | EXT-CB transported corner comparison: the fixed level-one maps \(\gamma_{11}=v\) and \(\gamma_{jk}=(Ha^Q_{P_j,P_k})^{-1}\mu_{jk}\) for \((j,k)\ne(1,1)\) satisfy \(\lVert(Ha^Q_{P,P})_m\gamma_{11,m}-\mu_{11,m}\rVert\le\kappa e\) and \((Ha^Q_{P_j,P_k})_m\gamma_{jk,m}=\mu_{jk,m}\) in the other three corners for every \(m\). | `def-ha-map`; P:`def-canonical-corner-system`; P:`def-four-corner-merging-datum`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `lem-extcb2-spatial-corner-system`; `lem-extcb3-four-ha-inverses` | `PROOF-W74F-F-EXTCB.md` §5, equations (5.1)–(5.3); verdict EXTCB-4 `VALID` | 5 / 3 |
| `lem-extcb4-complete-merging-datum` | lemma / `proved-mod-audit` | EXT-CB complete merging datum: the four fixed transported corner maps of `lem-extcb4-transported-corners` satisfy the adjoint, product, unit, and two-sided norm conditions of the amplified four-corner merging datum with common defect \(5(C_H+\kappa)e\) at every amplification. | `def-ha-map`; P:`def-canonical-corner-system`; P:`def-four-corner-merging-datum`; P:`def-compressed-corner`; P:`def-column-hilbert-corner` | `conj-hcb`; `lem-extcb3-four-ha-inverses`; `lem-extcb4-transported-corners` | `PROOF-W74F-F-EXTCB.md` §5.1–5.4 (EXTCB-4); verdict EXTCB-4 `VALID` | 8 / 3 |

### 1.3 Phase 4A — Stage-1 external cited candidates

These are proposed registry leaves only after acquisition and byte matching.
Until then they are provisioning blockers, not `cited` results.

| proposed id | kind / status | contract (verbatim proposed one-line `contract:` value) | defs | deps | provenance locus | projected af |
|---|---|---|---|---|---|---|
| `lem-topology-quotient-manifold` | lemma / `cited candidate` | Quotient manifold theorem: if a Lie group acts smoothly, freely, and properly on a smooth manifold \(M\), then \(M/G\) has the unique smooth-manifold structure for which the quotient map is a smooth submersion. | — | — | candidate: J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Theorem 21.10, as already cited at pinned TeX `tex:949` | 1 / 1 external |
| `lem-topology-finite-triangulation` | lemma / `cited candidate` | Finite triangulation of compact \(C^1\) manifolds: every compact \(C^1\) manifold is homeomorphic to a finite simplicial complex. | — | — | candidate: J. H. C. Whitehead, “On \(C^1\)-complexes,” *Annals of Mathematics* 41 (1940), or the Cairns triangulation theorem; exact acquisition locus must be selected before sharding | 1 / 1 external |
| `lem-topology-lefschetz-hopf` | lemma / `cited candidate` | Lefschetz-Hopf formula: for a self-map of a finite polyhedron with finitely many isolated fixed points, the Lefschetz number is the sum of their fixed-point indices. | P:`def-lefschetz-fixed-point-data` | — | candidate: M. Arkowitz and R. F. Brown, “The Lefschetz-Hopf theorem and axioms for the Lefschetz number,” Theorem 1.2/normalization theorem | 1 / 1 external |
| `lem-topology-local-index-sign` | lemma / `cited candidate` | Nondegenerate local fixed-point index: if \(x\) is an isolated fixed point of a \(C^1\) self-map and \(\det(I-Df_x)\ne0\), then its local fixed-point index is \(\operatorname{sgn}\det(I-Df_x)\). | P:`def-lefschetz-fixed-point-data` | — | candidate: A. Granas and J. Dugundji, *Fixed Point Theory*, local-index chapter; acquire a source with the exact differentiable statement before sharding | 1 / 1 external |
| `lem-topology-orientable-top-cohomology` | lemma / `cited candidate` | Top cohomology of a closed orientable manifold: if \(M\) is a connected compact orientable \(d\)-manifold, then \(H^d(M;\mathbb R)\ne0\). | — | — | candidate: A. Hatcher, *Algebraic Topology*, §3.3 Poincaré duality; exact theorem locus to be byte-matched after acquisition | 1 / 1 external |
| `lem-topology-kunneth-cross-product` | lemma / `cited candidate` | Cohomological Künneth isomorphism over \(\mathbb R\): for finite-CW spaces with finite-dimensional cohomology, the cross product identifies \(H^*(X;\mathbb R)\otimes H^*(Y;\mathbb R)\) with \(H^*(X\times Y;\mathbb R)\). | — | — | candidate: A. Hatcher, *Algebraic Topology*, Theorem 3.16, cited at pinned TeX `tex:986` | 1 / 1 external |
| `lem-topology-hopf-structure` | lemma / `cited candidate` | Hopf structure theorem in the form consumed by Stage 1: a finite-dimensional connected graded-commutative bialgebra over a characteristic-zero field is an exterior algebra on odd-degree homogeneous generators. | P:`def-h-space-left-inversion` | — | candidate: A. Hatcher, *Algebraic Topology*, Theorem 3C.4, cited at pinned TeX `tex:1014`; hypothesis match must be checked before sharding | 1 / 1 external |

### 1.4 Phase 4B — Stage-1 and MAIN-CB

| proposed id | kind / status | contract (verbatim proposed one-line `contract:` value) | defs | deps | provenance locus | projected af |
|---|---|---|---|---|---|---|
| `lem-stage1-exact-unit-rectification` | lemma / `proved-mod-audit` | Dimension-free exact-unit rectification: there are universal \(C_{\mathrm{unit}}<\infty\), \(e_{\mathrm{unit}}>0\) such that every finite-dimensional \(\varepsilon_X\)-\(C^*\)-algebra with \(\varepsilon_X\le e_{\mathrm{unit}}\) admits on the same involutive normed space an exact unit \(J\) and product \(\boldsymbol{\cdot}\) with \(\lVert J-I_X\rVert\le C_{\mathrm{unit}}\varepsilon_X\) and \(\lVert x\boldsymbol{\cdot}y-xy\rVert\le C_{\mathrm{unit}}\varepsilon_X\lVert x\rVert\lVert y\rVert\). | P:`def-epsilon-cstar-algebra` | — | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A, equation (1.1); Stage-1 verdict “exact-unit rectification — VALID” | 7 / 3 |
| `lem-stage1-uniform-inversion-isolation` | lemma / `proved-mod-audit` | Uniform inversion isolation: there are universal \(r_{\mathrm{iso}}>0\) and \(e_{\mathrm{iso}}>0\) such that, in the rectified approximate-unitary manifold of an \(\varepsilon_X\)-\(C^*\)-algebra with \(\varepsilon_X\le e_{\mathrm{iso}}\), the inversion map has no fixed point in either \(r_{\mathrm{iso}}\)-ball about \(J\) or \(-J\) except the center. | P:`def-epsilon-cstar-algebra`; P:`def-approximate-unitary-space` | `lem-stage1-exact-unit-rectification` | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A, equations (1.2)–(1.4); Stage-1 verdict uniform-isolation section `VALID` | 9 / 3 |
| `lem-stage1-quotient-manifold-package` | lemma / `proved-mod-audit` | Stage-1 quotient manifold package: the quotient \(\breve{\mathcal U}=\mathcal U_e/U(1)\) is a connected compact positive-dimensional orientable \(C^1\) manifold of finite CW type. | P:`def-approximate-unitary-space` | `lem-topology-quotient-manifold`; `lem-topology-finite-triangulation` | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A topological paragraph; Stage-1 verdict “topological inputs — VALID” | 6 / 3 |
| `lem-stage1-quotient-left-inversion` | lemma / `proved-mod-audit` | Stage-1 quotient H-space: the multiplication and inversion induced on \(\breve{\mathcal U}\) make it a connected H-space with a left inversion map. | P:`def-approximate-unitary-space`; P:`def-h-space-left-inversion` | — | pinned construction `tex:895-912`, `945-955`, as consumed in `PROOF-W74F-H-STAGE1.md` §1 and validated by its verdict | 5 / 3 |
| `lem-stage1-left-inversion-trace` | lemma / `proved-mod-audit` | Left-inversion trace: if \(M\) is a connected finite-CW H-space with finite-dimensional real cohomology and left inversion \(\sigma\), then \(\operatorname{Tr}(\sigma^{*k})=(-1)^k\dim H^k(M;\mathbb R)\) for every \(k\). | P:`def-h-space-left-inversion`; P:`def-lefschetz-fixed-point-data` | `lem-topology-kunneth-cross-product`; `lem-topology-hopf-structure` | pinned proof `tex:971-1050`; `PROOF-W74F-H-STAGE1.md` §1 topological paragraph; Stage-1 verdict checks 8–9 | 9 / 3 |
| `lem-stage1-extra-fixed-class` | lemma / `proved-mod-audit` | Extra inversion fixed class: the induced inversion \(\breve{\sigma}\) on the Stage-1 quotient \(\breve{\mathcal U}\) has a fixed point distinct from the scalar class \(\breve e\). | P:`def-approximate-unitary-space`; P:`def-h-space-left-inversion`; P:`def-lefschetz-fixed-point-data` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-quotient-manifold-package`; `lem-stage1-quotient-left-inversion`; `lem-stage1-left-inversion-trace`; `lem-topology-lefschetz-hopf`; `lem-topology-local-index-sign`; `lem-topology-orientable-top-cohomology` | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A topological paragraph; Stage-1 verdict topological sections `VALID` | 10 / 3 |
| `lem-stage1-rectified-nontrivial-projection` | lemma / `proved-mod-audit` | Rectified nontrivial projection: a non-scalar inversion fixed class outside the two isolation balls yields a Hermitian \(P_0=\frac14(2J+U+U^\dagger)\) with \(\lVert P_0\boldsymbol{\cdot}P_0-P_0\rVert\le C_{\mathrm{proj}}\varepsilon_X\) and with both \(P_0\) and \(J-P_0\) in the nonvanishing norm alternative. | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection`; P:`def-approximate-unitary-space` | `lem-stage1-uniform-inversion-isolation`; `lem-stage1-extra-fixed-class` | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A, equations (1.5)–(1.9); Stage-1 verdict projection and nonvanishing checks | 7 / 3 |
| `lem-stage1-original-complementary-pair` | lemma / `proved-mod-audit` | Original-product complementary pair: there are universal \(C_{\mathrm{np}}<\infty\), \(e_{\mathrm{np}}>0\) such that \(P'=P_0\) and \(P''=I_X-P'\) are nonvanishing Hermitian elements with \(P'+P''=I_X\) and with both projection defects and both cross-products bounded by \(C_{\mathrm{np}}\varepsilon_X\). | P:`def-epsilon-cstar-algebra`; P:`def-delta-projection` | `lem-stage1-exact-unit-rectification`; `lem-stage1-rectified-nontrivial-projection` | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-A, equations (1.10)–(1.11); Stage-1 verdict exact-unit transfer `VALID` plus explicit \(e_{\mathrm{nv}}\) correction | 7 / 3 |
| `lem-stage1-fresh-two-point-inclusion` | lemma / `proved-mod-audit` | Fresh two-point complete inclusion: there are universal \(C_{\mathrm{pair}}<\infty\), \(e_{\mathrm{pair}}>0\) such that the map \(v_{\mathrm{comm}}^{(2)}:\mathbb C^2\to X\), \((\lambda,\mu)\mapsto\lambda P'+\mu P''\), is an extended \(C_{\mathrm{pair}}\varepsilon_X\)-inclusion whenever \(\varepsilon_X\le e_{\mathrm{pair}}\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-operator-space` | `lem-stage1-original-complementary-pair` | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-B, equations (1.12)–(1.19); Stage-1 verdict fresh all-level inclusion `VALID` | 8 / 3 |
| `lem-stage1-old-side-compression` | lemma / `proved-mod-audit` | Old-side Stage-1 compression: there are universal \(C_{\mathrm{old}}<\infty\), \(e_{\mathrm{old}}>0\) such that the restriction of a reset maximal commutative inclusion followed by the single compression into \(S_{P_{[1,m-1]}}\) has extended defect at most \(C_{\mathrm{old}}\varepsilon_0\), where \(\varepsilon_0\) is the Stage-1 ambient-algebra defect. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-compressed-corner`; P:`def-projection-basis` | — | `PROOF-W74F-H-STAGE1.md` §1 SPLIT-C, corrected by Stage-1 verdict “old side SPLIT-C — VALID-WITH-CORRECTIONS” | 6 / 3 |
| `lem-stage1-two-side-packet` | lemma / `proved-mod-audit` | Corrected Stage-1 two-side packet: there are universal \(C_{\mathrm{split}}\ge1\), \(e_{\mathrm{split}}>0\) such that the old side has defect at most \(C_{\mathrm{co}}(1+c_0^{\mathrm{cb}})\varepsilon_0\), the fresh side has defect at most \(C_{\mathrm{split}}\varepsilon_S\), and MAIN-CB supplies \(\varepsilon_S\le C_{\mathrm{co}}(1+c_0^{\mathrm{cb}})\varepsilon_0\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-delta-projection`; P:`def-compressed-corner` | `lem-stage1-fresh-two-point-inclusion`; `lem-stage1-old-side-compression` | `PROOF-W74F-H-STAGE1.md` §0 and §2, with the exact two-defect replacement in `VERDICT-W74F-H-STAGE1.md` Packet §0 | 5 / 3 |
| `lem-maincb-error-improvement` | lemma / `stated` | Complete error improvement: there are universal \(\delta_{\max}^{\mathrm{cb}}>0\) and \(c_0^{\mathrm{cb}}<\infty\) such that every admissible extended raw inclusion into an extended \(\varepsilon\)-\(C^*\)-algebra can be replaced by one extended \(c_0^{\mathrm{cb}}\varepsilon\)-inclusion, preserving bijectivity. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-extcb-exact-target-approximation` | premise IMPROVE-CB in `DECOMP-W74F-C-THMAINEXT.md`; pinned TeX `cor_improvement`, `prop_inc_ext`, `lem_approx_ext`; not proved in the four permitted packets | 9 / 3, uncertain until prover |
| `lem-maincb-uniform-reset-chain` | lemma / `proved-mod-audit` | MAIN-CB uniform reset invariant: with \(C_{\mathrm{main}}=\max\{C_{\mathrm{co}},C_{\mathrm{split}}\}\), \(L=C_{\mathrm{main}}(1+c_0^{\mathrm{cb}})\), and \(C_{\mathrm{pre}}=2L^2\max\{1,C_{\mathrm{ext}},C_{\mathrm{merge}}\}\), every Stage-1, Stage-2, and Stage-3 raw call has \(\delta_{\mathrm{raw}}\le L^2\varepsilon\) and \(e_{\mathrm{raw}}\le C_{\mathrm{pre}}\varepsilon\), with every extension or merge followed immediately by an error reset. | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion`; P:`def-compressed-corner`; P:`def-four-corner-merging-datum` | `conj-extcb`; `lem-extcb-four-corner-merge`; `lem-stage1-two-side-packet`; `lem-maincb-error-improvement` | `PROOF-W74F-H-STAGE1.md` §3, equations (3.1)–(3.10); Stage-1 verdict corrected reset chain `VALID-WITH-CORRECTIONS` | 9 / 3 |

### 1.5 Phase 4C — relative Route F ledger

| proposed id | kind / status | contract (verbatim proposed one-line `contract:` value) | defs | deps | provenance locus | projected af |
|---|---|---|---|---|---|---|
| `lem-routef-main-radius-ledger` | lemma / `proved-mod-audit` | Corrected MAIN-CB radius ledger: the constants \(C_{\mathrm{main}},L,C_{\mathrm{pre}}\) from `lem-maincb-uniform-reset-chain` and the minimum \(\varepsilon_E^{\mathrm{corr}}=\min\{\delta_{\max}^{\mathrm{cb}},e_H,e_{\mathrm{ext}},e_{\mathrm{sel}},e_{\mathrm{split}}\}/C_{\mathrm{pre}}\) are finite, positive, universal, and independent of dimension, amplification, block data, and stage index. | `def-extended-epsilon-cstar-algebra` | `conj-hcb`; `conj-extcb`; `lem-maincb-uniform-reset-chain`; `lem-thmainext-conditional` | `PROOF-W74F-H-STAGE1.md` §3; Stage-1 verdict corrected reset chain; replaces the invalid G-ledger §1.3 radius | 6 / 3 |
| `lem-routef-functional-calculus-closeness` | lemma / `proved-mod-audit` | Functional-calculus closeness: for \(0\le\eta\le1/8\), the exact functional-calculus projector satisfies \(\lVert\widetilde\Phi-\Phi\rVert_{\mathrm{cb}}\le C_\theta\eta\), where \(C_\theta=12(\sqrt2-1)\). | `def-almost-idempotent` | `lem-kitaev-almost-idemp-audit` | `LEDGER-W74F-G-K.md` §1.1; G-verdict checks 3–4 | 4 / 2 |
| `lem-routef-ai-defect-linearization` | lemma / `proved-mod-audit` | Approximate-algebra defect linearization: for \(\eta\) below one universal positive threshold, the image of \(\widetilde\Phi\) is an extended \(\varepsilon_{\mathrm{AI}}(\eta)\)-\(C^*\)-algebra with \(\varepsilon_{\mathrm{AI}}(\eta)\le C_A\eta\), where \(C_A=20+\frac{211}{8}C_\theta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-kitaev-almost-idemp-audit`; `lem-routef-functional-calculus-closeness` | `LEDGER-W74F-G-K.md` §1.1, equation (1.1); G-verdict checks 4 and symbol-table arithmetic | 5 / 3 |
| `lem-routef-raw-factor-norms` | lemma / `proved-mod-audit` | Raw factor-map norm bound: for sufficiently small universal \(\eta\), \(\max\{\lVert\widetilde\Delta\rVert_{\mathrm{cb}},\lVert\widetilde\Upsilon\rVert_{\mathrm{cb}}\}\le1+C_T\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | `LEDGER-W74F-G-K.md` §1.3, equation (1.9); G-verdict intermediate arithmetic | 5 / 3 |
| `lem-routef-raw-factor-units` | lemma / `proved-mod-audit` | Raw factor-map unit bound: for sufficiently small universal \(\eta\), \(\max\{\lVert\widetilde\Delta(I)-I\rVert,\lVert\widetilde\Upsilon(I)-I\rVert\}\le C_T\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-routef-ai-defect-linearization`; `lem-thmainext-conditional` | `LEDGER-W74F-G-K.md` §1.3, equation (1.9); G-verdict intermediate arithmetic | 5 / 3 |
| `lem-routef-raw-factor-identities` | lemma / `proved-mod-audit` | Raw factor-map identities: \((\widetilde\Delta\widetilde\Upsilon,\widetilde\Upsilon\widetilde\Delta)=(\widetilde\Phi,I_{\mathcal B})\). | `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-thmainext-conditional` | `LEDGER-W74F-G-K.md` §1.3, equation (1.10); G-verdict checks exact identities | 3 / 2 |
| `lem-routef-raw-product-estimate` | lemma / `proved-mod-audit` | Raw factor-map product estimate: for sufficiently small universal \(\eta\), \(\lVert\widetilde\Upsilon_n(\widetilde\Delta_n(X)\widetilde\Delta_n(Y))-XY\rVert\le C_T\eta\lVert X\rVert\lVert Y\rVert\) for every amplification \(n\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra`; P:`def-extended-delta-inclusion` | `lem-routef-raw-factor-norms`; `lem-routef-raw-factor-identities`; `lem-thmainext-conditional` | `LEDGER-W74F-G-K.md` §1.3, equation (1.9); G-verdict intermediate arithmetic | 6 / 3 |
| `lem-routef-delta-prime-closeness` | lemma / `proved-mod-audit` | Delta-prime CP closeness: the repaired diagonal CP-ization produces a completely positive map \(\Delta'\) with \(\lVert\Delta'-\widetilde\Delta\rVert_{\mathrm{cb}}\le C_{\Delta'}\eta\), where \(C_{\Delta'}=C_T+4C_\theta\). | `def-fd-cstar-diagonal`; `def-extended-epsilon-cstar-algebra` | `cor-kitaev-diagonal-cpization`; `lem-routef-functional-calculus-closeness`; `lem-routef-raw-factor-norms` | `LEDGER-W74F-G-K.md` §1.3, equations (1.11)–(1.12); G-verdict CP-ization arithmetic | 7 / 3 |
| `lem-routef-delta-normalization-closeness` | lemma / `proved-mod-audit` | Delta UCP normalization: for sufficiently small universal \(\eta\), normalizing \(\Delta'\) produces a UCP map \(\Delta\) with \(\lVert\Delta-\widetilde\Delta\rVert_{\mathrm{cb}}\le C_\Delta\eta\), where \(C_\Delta=6C_T+7C_{\Delta'}\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-factor-units`; `lem-routef-delta-prime-closeness` | `LEDGER-W74F-G-K.md` §1.3, equations (1.11)–(1.12); G-verdict normalization arithmetic | 7 / 3 |
| `lem-routef-delta-phi-product` | lemma / `proved-mod-audit` | Normalized Delta product estimate: for every amplification \(n\), \(\lVert\widetilde\Phi_n(\Delta_n(X)\Delta_n(Y))-\widetilde\Delta_n(XY)\rVert\le(C_2+C_\theta+C_\Delta)\eta\lVert X\rVert\lVert Y\rVert\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; `lem-routef-delta-normalization-closeness` | `LEDGER-W74F-G-K.md` §3 immediately before (3.3); G-verdict `K — VALID` | 6 / 3 |
| `lem-routef-upsilon-prime-closeness` | lemma / `proved-mod-audit` | Upsilon-prime CP closeness: the componentwise CP construction produces a completely positive map \(\Upsilon'\) with \(\lVert\Upsilon'-\widetilde\Upsilon\rVert_{\mathrm{cb}}\le C_{\Upsilon'}\eta\), where \(C_{\Upsilon'}\) is one finite universal coefficient independent of block count and block dimensions. | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-product-estimate`; `lem-routef-delta-phi-product` | `LEDGER-W74F-G-K.md` §1.3, equation (1.13); G-verdict checks 13–14 | 10 / 3, highest-risk ledger leaf |
| `lem-routef-upsilon-normalization-closeness` | lemma / `proved-mod-audit` | Upsilon UCP normalization: for sufficiently small universal \(\eta\), normalizing \(\Upsilon'\) produces a UCP map \(\Upsilon\) with \(\lVert\Upsilon-\widetilde\Upsilon\rVert_{\mathrm{cb}}\le C_\Upsilon\eta\), where \(C_\Upsilon=6C_T+7C_{\Upsilon'}\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-factor-units`; `lem-routef-upsilon-prime-closeness` | `LEDGER-W74F-G-K.md` §1.3, equations (1.14)–(1.15); G-verdict normalization check | 7 / 3 |
| `lem-routef-delta-upsilon-telescope` | lemma / `proved-mod-audit` | Delta-Upsilon telescope: \(\lVert\Delta\Upsilon-\Phi\rVert_{\mathrm{cb}}\le(C_\theta+C_\Delta+2C_\Upsilon)\eta\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-functional-calculus-closeness`; `lem-routef-raw-factor-identities`; `lem-routef-delta-normalization-closeness`; `lem-routef-upsilon-normalization-closeness` | `LEDGER-W74F-G-K.md` §3, first line of (3.2); G-verdict `K — VALID` | 6 / 3 |
| `lem-routef-multiplicative-telescope` | lemma / `proved-mod-audit` | Multiplicative telescope: \(\lVert\Upsilon_n(\Delta_n(X)\Delta_n(Y))-XY\rVert\le[C_\Upsilon+2(C_2+C_\theta+C_\Delta)]\eta\lVert X\rVert\lVert Y\rVert\) for every amplification \(n\). | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-factor-norms`; `lem-routef-raw-factor-identities`; `lem-routef-delta-phi-product`; `lem-routef-upsilon-normalization-closeness` | `LEDGER-W74F-G-K.md` §3, second line of (3.2); G-verdict `K — VALID` | 7 / 3 |
| `lem-routef-upsilon-delta-telescope` | lemma / `proved-mod-audit` | Upsilon-Delta telescope: \(\lVert\Upsilon\Delta-I_{\mathcal B}\rVert_{\mathrm{cb}}\le(C_\Upsilon+2C_\Delta)\eta\). | `def-extended-epsilon-cstar-algebra` | `lem-routef-raw-factor-identities`; `lem-routef-delta-normalization-closeness`; `lem-routef-upsilon-normalization-closeness` | `LEDGER-W74F-G-K.md` §3, third line of (3.2); G-verdict `K — VALID` | 5 / 3 |
| `lem-routef-k-finiteness` | lemma / `proved-mod-audit` | Route F common coefficient: \(K=\max\{1,C_\theta+C_\Delta+2C_\Upsilon,C_\Upsilon+2(C_2+C_\theta+C_\Delta),C_\Upsilon+2C_\Delta\}\) is finite and universal. | `def-extended-epsilon-cstar-algebra` | `lem-routef-delta-upsilon-telescope`; `lem-routef-multiplicative-telescope`; `lem-routef-upsilon-delta-telescope` | `LEDGER-W74F-G-K.md` §3, equation (3.3); G-verdict `K — VALID`; Stage-1 verdict says unchanged | 5 / 2 |
| `lem-routef-threshold-minimum` | lemma / `proved-mod-audit` | Route F threshold positivity: \(\eta_K=\min\{\frac18,\eta_A,\frac{\delta_{\max}^{\mathrm{cb}}}{C_{\mathrm{pre}}C_A},\frac{e_H}{C_{\mathrm{pre}}C_A},\frac{e_{\mathrm{ext}}}{C_{\mathrm{pre}}C_A},\frac{e_{\mathrm{sel}}}{C_{\mathrm{pre}}C_A},\frac{e_{\mathrm{split}}}{C_{\mathrm{pre}}C_A},\frac1{4C_\theta},\frac1{4C_EC_A},\frac1{2(C_T+C_{\Delta'})},\frac1{4(1+C_2+C_3+C_{\Upsilon'})},\frac1{2(C_T+C_{\Upsilon'})},\frac1{24K},1\}\) is positive. | `def-almost-idempotent`; `def-extended-epsilon-cstar-algebra` | `lem-routef-main-radius-ledger`; `lem-routef-ai-defect-linearization`; `lem-routef-delta-normalization-closeness`; `lem-routef-upsilon-prime-closeness`; `lem-routef-k-finiteness` | `LEDGER-W74F-G-K.md` §4 plus `PROOF-W74F-H-STAGE1.md` §4; Stage-1 verdict corrected delta `VALID` | 8 / 3 |
| `lem-routef-prh-finish` | lemma / `proved-mod-audit` | Route F PRH finish: if \(K\ge1\), \(0\le\eta\le\min\{(24K)^{-1},1\}\), \(\lVert Q-AM\rVert_{\infty\to\infty}\le K\eta\), and \(\lVert MA-I\rVert_{\infty\to\infty}\le3K\eta/(1-3K\eta)\), then there is a stochastic idempotent \(E\) with \(\lVert Q-E\rVert_{\infty\to\infty}\le(K+4\sqrt{2K})\sqrt\eta\). | `def-positive-approximate-retract`; `def-stochastic` | `lem-prh`; `lem-routef-threshold-minimum` | `LEDGER-W74F-G-K.md` §5; G-verdict Finish `VALID`; Stage-1 verdict Scope and finish `VALID` | 5 / 3 |

## 2. Assembly wiring

No `routes:` field is proposed.  These are conjunctive proof decompositions,
not alternative strategies.

### 2.1 `conj-hcb`

Keep the existing contract byte-for-byte.  Replace its empty direct dependency
list by:

```yaml
deps: lem-hcb2-amplified-adjointness; lem-hcb2-product-defect; lem-hcb3-diagonal-unit; lem-hcb3-diagonal-upper-norm; lem-hcb3-diagonal-lower-modulus; lem-hcb3-diagonal-inverse; lem-hcb3-offdiagonal-inverse; lem-hcb4-canonical-closeness; lem-hcb4-canonical-inverse
```

Projected parent workspace: root plus nine validated imports, **10 nodes /
depth 2**.  The associator, variational identity, column action, corrected
COL-HILB, and Gram estimate remain transitive dependencies of those nine
imports; they must not be duplicated in the parent tree.

### 2.2 `conj-extcb`

Keep the existing contract byte-for-byte.  Its exact proposed direct
dependency list is:

```yaml
deps: conj-hcb; lem-extcb1-cross-corner-dimension; lem-extcb2-exact-representation; lem-extcb2-spatial-corner-system; lem-extcb3-four-ha-inverses; lem-extcb4-transported-corners; lem-extcb4-complete-merging-datum; lem-extcb-four-corner-merge
```

Projected parent workspace: root plus eight validated imports, **9 nodes /
depth 2**.  The conditional H-CB inverse order is represented by the
dependencies of `lem-extcb3-four-ha-inverses`; the parent must not restate or
weaken it.

### 2.3 `lem-thmainext-conditional`

Keep the existing contract byte-for-byte.  Its exact proposed direct
dependency list is:

```yaml
deps: conj-hcb; conj-extcb; lem-hcb-column-hilbert-squared; lem-stage1-two-side-packet; lem-maincb-error-improvement; lem-maincb-uniform-reset-chain; lem-extcb-four-corner-merge
```

Projected parent workspace: root plus seven validated imports, **8 nodes /
depth 2**.  The Stage-1 old/fresh defect distinction is buried nowhere: it is
the literal contract of `lem-stage1-two-side-packet`.

### 2.4 `lem-routef-k-ledger`

Keep the existing contract byte-for-byte.  Replace its current direct
dependency list by:

```yaml
deps: lem-routef-delta-upsilon-telescope; lem-routef-multiplicative-telescope; lem-routef-upsilon-delta-telescope; lem-routef-k-finiteness; lem-routef-threshold-minimum; lem-routef-prh-finish
```

Projected parent workspace: root plus six validated imports, **7 nodes /
depth 2**.  Its current four imports remain transitive:

- `lem-thmainext-conditional` through the raw-factor and main-radius nodes;
- `cor-kitaev-diagonal-cpization` through the Delta-normalization node;
- `lem-kitaev-almost-idemp-audit` through the AI-linearization node;
- `lem-prh` through the PRH-finish node.

### 2.5 Existing non-parent leaves

`lem-kitaev-diagonal-repair`, `cor-kitaev-diagonal-cpization`,
`lem-kitaev-almost-idemp-audit`, and `lem-prh` receive **no contract or
dependency change in this design**.  The first three are future serial
elevation targets; `lem-prh` is already validated.

## 3. Definition provisioning

### 3.1 Proposed definition shards

The table is deliberately limited to vocabulary actually used by the proposed
contracts.  Definitions from the pinned Kitaev TeX are candidates for
byte-matched `cited` shards even though theorem proofs in that source are not
citable as rigorous results.

| proposed def id | canonical term | proposed kind/status | sound source locus / rationale | used by |
|---|---|---|---|---|
| `def-epsilon-cstar-algebra` | \(\varepsilon\)-\(C^*\)-algebra | `cited` / lock after byte-match | pinned TeX `tex:407-440` (the complete definition, including approximate unit) | Stage-1 and source-premise contracts |
| `def-delta-projection` | \(\delta\)-projection; nonvanishing/nontrivial projection | `cited` / lock after byte-match | pinned TeX `tex:917-929` | H-CB, EXT-CB, Stage 1 |
| `def-one-dimensional-delta-projection` | one-dimensional \(\delta\)-projection and equivalence | `cited` / lock after byte-match | pinned TeX `tex:1064-1066`, `1187` | COL-HILB, H-CB, EXT-CB |
| `def-compressed-corner` | compression map \(Co_{P,Q}\), corner \(S_{P,Q}\), and compressed product | `cited` / lock after byte-match | pinned TeX `tex:1054-1082`; the printed `tex:1109` index typo is outside the definition | all H-CB/EXT-CB/MAIN contracts |
| `def-column-hilbert-corner` | level-one and amplified column-Hilbert corner | `cited` / lock after byte-match | pinned TeX sound identity loci `tex:1123-1149`, `1546-1550`; **exclude** the false unsquared display `1551-1553` | corrected COL-HILB and Ha contracts |
| `def-extended-delta-inclusion` | extended \(\delta\)-inclusion and extended \(\delta\)-isomorphism | `consensus` / `draft` pending sign-off | harmonizes pinned TeX base definitions `tex:443-456` with the extended clauses `1477-1484`; not byte-verbatim in one contiguous source passage | EXT-CB, MAIN-CB, inverse contracts |
| `def-operator-space` | operator space and rectangular matrix norms | `cited` / lock after byte-match | pinned TeX `tex:1453-1475` | amplification and tensor contracts |
| `def-four-corner-merging-datum` | amplified four-corner merging datum | `cited` / lock after byte-match | pinned TeX `tex:1325-1345`, using the four hypotheses only | EXT-CB transport and merge |
| `def-projection-basis` | projection basis of a finite-dimensional commutative \(C^*\)-algebra | `cited` / lock after byte-match | pinned TeX `tex:1361-1364` | level-one dimension and Stage-1 old side |
| `def-compressed-associator` | compressed associator | `original` / `draft` pending sign-off | project name for \((A\cdot B)\cdot C-A\cdot(B\cdot C)\); compressed product source `tex:1080-1082`, artifact HCB §3 | HCB-0 and HCB-1 |
| `def-canonical-corner-system` | canonical column/row identifications and exact spatial four-corner system | `cited` / lock after byte-match | pinned TeX `tex:1404` defines \(\mu_{jk}=U_j(\cdot)U_k^\dagger\); artifact EXT-CB §3.6 fixes the all-level notation | HCB-4 and EXT-CB-2/4 |
| `def-approximate-unitary-space` | approximate unitary manifold, polar retraction, and inversion | `cited` / lock after byte-match | pinned TeX `tex:692-697`, `809-892` | Stage-1 analytic/topological nodes |
| `def-h-space-left-inversion` | H-space and left inversion map | `cited` / lock after byte-match | pinned TeX `tex:895-912` (definition only) | Stage-1 topology |
| `def-lefschetz-fixed-point-data` | Lefschetz number and nondegenerate fixed-point index | `cited` / lock after byte-match | pinned TeX `tex:957-967` (definitions only, not the theorem) | Stage-1 topology |

Existing `def-extended-epsilon-cstar-algebra`, `def-ha-map`,
`def-fd-cstar-diagonal`, `def-almost-idempotent`,
`def-positive-approximate-retract`, and `def-stochastic` are reused unchanged.

### 3.2 Stage-1 external-input register

| input actually consumed | proposed registry treatment | candidate source for `refs/` | cited-vs-consensus call |
|---|---|---|---|
| Free proper smooth group action gives a quotient manifold and quotient submersion. | `lem-topology-quotient-manifold` | Lee, *Introduction to Smooth Manifolds*, 2nd ed., Theorem 21.10 (already cited by Kitaev) | **cited leaf** after acquisition/byte-match; not consensus |
| A compact \(C^1\) manifold has finite triangulation / finite CW type. | `lem-topology-finite-triangulation` | Whitehead, “On \(C^1\)-complexes” (1940), or Cairns's triangulation theorem | **cited leaf**; choose one source whose statement exactly covers \(C^1\) and compactness |
| Lefschetz-Hopf index sum for finitely many isolated fixed points. | `lem-topology-lefschetz-hopf` | Arkowitz–Brown, “The Lefschetz-Hopf theorem and axioms for the Lefschetz number” | **cited leaf** after byte-match |
| Local index of a nondegenerate differentiable fixed point is \(\operatorname{sgn}\det(I-Df)\). | `lem-topology-local-index-sign` | Granas–Dugundji, *Fixed Point Theory*, local-index chapter | **cited leaf**; do not fold it silently into the Lefschetz-Hopf leaf unless one acquired source states both |
| Connected compact orientable \(d\)-manifold has nonzero \(H^d(-;\mathbb R)\). | `lem-topology-orientable-top-cohomology` | Hatcher, *Algebraic Topology*, Poincaré-duality section | **cited leaf** after exact-locus selection |
| Cross product is the required cohomological Künneth isomorphism. | `lem-topology-kunneth-cross-product` | Hatcher, Theorem 3.16 (already cited by Kitaev) | **cited leaf** |
| Hopf structure theorem gives an exterior algebra on odd generators in the finite-dimensional case. | `lem-topology-hopf-structure` | Hatcher, Theorem 3C.4 (already cited by Kitaev); Milnor–Moore is a secondary fallback | **cited leaf only if the acquired theorem's hypotheses match the non-coassociative bialgebra form actually used**; otherwise keep the augmentation argument inside `lem-stage1-left-inversion-trace` and cite only the exact theorem it needs |
| Definition of H-space / left inversion, Lefschetz number, and local fixed-point index. | proposed defs in §3.1 | pinned Kitaev TeX definitions are already local | **cited definitions**, not consensus |
| Banach inverse-function estimate, exact-unit rectification, polar retraction, uniform isolation, quotient orientability, and lifting a non-scalar class. | internal Stage-1 proposal nodes | supplied W74F-H artifact and verdict | **not external leaves**; `proved-mod-audit` now, future af proofs |

This register is exhaustive for SPLIT-A/B/C as written.  SPLIT-B additionally
uses only the operator-space tensor isometry and the source-level
homomorphism/inclusion bootstrap already represented by proposed
definitions/results.  SPLIT-C uses COMP-CB against the old ambient defect and
has no new topological input.

## 4. Phase map and bottom-up seeding order

### Phase 2 — H-CB (`aism-niwk`)

Provision the proposed algebra/corner/column definitions first.  Then seed
serially by dependency layers:

1. `lem-hcb-column-hilbert-squared`,
   `lem-hcb0-compressed-associator`,
   `lem-hcb1-variational-identity`,
   `lem-hcb2-amplified-adjointness`,
   `lem-hcb4-canonical-gram`.
2. `lem-hcb1-column-action`.
3. `lem-hcb2-product-defect`, `lem-hcb3-diagonal-unit`,
   `lem-hcb4-canonical-closeness`.
4. `lem-hcb3-diagonal-upper-norm`,
   `lem-hcb3-diagonal-lower-modulus`,
   `lem-hcb4-canonical-inverse`.
5. `lem-hcb3-diagonal-inverse`,
   `lem-hcb3-offdiagonal-inverse`.
6. Existing parent `conj-hcb`.

All orchestrations remain strictly serial even when nodes share a dependency
layer.

### Phase 3 — EXT-CB (`aism-fgr7`)

1. Prove the five `stated` source-premise leaves:
   `lem-extcb-one-dimensional-product`,
   `lem-extcb-one-dimensional-corner-dimension`,
   `lem-extcb-corner-dimension-additivity`,
   `lem-extcb-exact-target-approximation`,
   `lem-extcb-four-corner-merge`.
2. `lem-extcb1-close-corner-dimension`.
3. `lem-extcb1-cross-corner-dimension`;
   `lem-extcb2-exact-representation`.
4. `lem-extcb2-spatial-corner-system`;
   `lem-extcb3-four-ha-inverses`.
5. `lem-extcb4-transported-corners`.
6. `lem-extcb4-complete-merging-datum`.
7. Existing parent `conj-extcb`.

### Phase 4 — Stage 1, MAIN-CB, assembly, ledger (`aism-5byv`)

Reference acquisition may run before orchestration, but af work remains serial.

1. Acquire and byte-match the seven topology leaves.
2. Prove `lem-maincb-error-improvement`, the sole Phase-4 `stated` source
   premise.
3. Stage-1 analytic leaves:
   `lem-stage1-exact-unit-rectification`,
   then `lem-stage1-uniform-inversion-isolation`.
4. Stage-1 topology:
   `lem-stage1-quotient-manifold-package`,
   `lem-stage1-quotient-left-inversion`,
   `lem-stage1-left-inversion-trace`,
   then `lem-stage1-extra-fixed-class`.
5. Projection/split:
   `lem-stage1-rectified-nontrivial-projection`,
   `lem-stage1-original-complementary-pair`,
   `lem-stage1-fresh-two-point-inclusion`,
   and independently `lem-stage1-old-side-compression`,
   then `lem-stage1-two-side-packet`.
6. `lem-maincb-uniform-reset-chain`.
7. Existing parent `lem-thmainext-conditional`.
8. Ledger:
   `lem-routef-main-radius-ledger`,
   `lem-routef-functional-calculus-closeness`,
   `lem-routef-ai-defect-linearization`,
   `lem-routef-raw-factor-norms`,
   `lem-routef-raw-factor-units`,
   `lem-routef-raw-factor-identities`,
   `lem-routef-raw-product-estimate`,
   `lem-routef-delta-prime-closeness`,
   `lem-routef-delta-normalization-closeness`,
   `lem-routef-delta-phi-product`,
   `lem-routef-upsilon-prime-closeness`,
   `lem-routef-upsilon-normalization-closeness`,
   `lem-routef-delta-upsilon-telescope`,
   `lem-routef-multiplicative-telescope`,
   `lem-routef-upsilon-delta-telescope`,
   `lem-routef-k-finiteness`,
   `lem-routef-threshold-minimum`,
   `lem-routef-prh-finish`.
9. Existing parent `lem-routef-k-ledger`.

### Phase 5 — F0/F2/F3 and the `op-classical` root (`aism-y81y`)

This brief supplied no permitted proof artifact for new F0/F2/F3 contracts, so
**no Phase-5 result shard is invented here**.  Phase 4 hands one validated
`lem-routef-k-ledger` import to the separate Phase-5 codification specified in
`2026-07-24-af-elevation-campaign.md`.  The W73 audit/sketch must provide those
contracts in that later pass.  This is a scope boundary, not a mathematical
gap in the four artifacts decomposed here.

## 5. Risk register

| id | risk / judgment | required treatment |
|---|---|---|
| R1 | The six source-premise nodes (`lem-extcb-*` first five plus `lem-maincb-error-improvement`) are consumed by verified artifacts but are not themselves proved in the four permitted proof packets. | Keep them `stated` and prove them before their dependents.  Do not cite the repaired theorem proof. |
| R2 | None of the seven topology theorem candidates is currently in `refs/`. | They are provisioning blockers.  Acquire, hash, byte-match, and only then set `cited`; otherwise no cited shard exists. |
| R3 | Hatcher Theorem 3C.4 may be stated for a stronger Hopf/bialgebra hypothesis than the non-coassociative form used in the artifact. | Check hypotheses exactly.  If they do not match, keep the artifact's augmentation-filtration proof inside `lem-stage1-left-inversion-trace`; never strengthen the input silently. |
| R4 | The H-CB parent contract's unconditional inverse reading is false. | Preserve the current parent contract exactly and keep the lower-modulus and bijectivity triggers in separate dependencies. |
| R5 | HCB-4 bijectivity does not follow from two-sided norm estimates alone in the potentially infinite-dimensional statement. | `lem-hcb4-canonical-inverse` must use the verifier-required Neumann condition. |
| R6 | EXTCB-1 initially identifies \(S_{v(I_r),Q}\) with \(S_{P,Q}\) too tersely. | Keep `lem-extcb1-close-corner-dimension` as a separate prerequisite and include its threshold in selection bookkeeping. |
| R7 | EXT-CB must use one level-one \(U_1\) and the same four maps at every amplification. | The single-map invariant is the entire contract of `lem-extcb2-spatial-corner-system` and `lem-extcb4-transported-corners`; no per-level choices. |
| R8 | Stage-1 old and fresh sides have different ambient defects. | `lem-stage1-two-side-packet` names \(\varepsilon_0\) and \(\varepsilon_S\) separately; never rename a common envelope as the fresh corner defect. |
| R9 | The final isolation-to-nonvanishing shrink was prose-only in the prover artifact. | Include the verifier's explicit \(e_{\mathrm{nv}}\) shrink in the body/provenance of `lem-stage1-original-complementary-pair`. |
| R10 | The G-ledger was hostile-rejected before the Stage-1 repair. | Ledger nodes use the H-verdict corrections, including \(C_{\mathrm{main}}\) and \(e_{\mathrm{split}}/(C_{\mathrm{pre}}C_A)\); never transcribe G §2/§4 without the H delta. |
| R11 | `lem-routef-upsilon-prime-closeness` covers the longest componentwise source chain and has the least certain projection. | Start with node-cap 10; if the prover projects beyond 10 or depth 3, split its componentwise construction before orchestration. |
| R12 | `lem-stage1-uniform-inversion-isolation` and `lem-stage1-left-inversion-trace` are each near the envelope. | They project 9/3.  Any af plan showing a fourth internal level triggers another registry split; do not raise the cap. |
| R13 | The proposed bundled type contracts (`quotient-manifold-package`, four-corner datum) list several defining properties. | They are single classification statements, not “hence” contracts.  If af treats the properties as independent goals and balloons, provision the corresponding definition rather than adding conclusions to the contract. |
| R14 | Proposed definitions can collide with vocabulary embedded in existing `def-extended-epsilon-cstar-algebra` and `def-ha-map`. | Before actual creation, run alias/dedup review against the existing bodies.  The new shards own missing terms only; they do not restate Ha or extended-\(\varepsilon\)-\(C^*\). |
| R15 | The pinned source's unsquared COL-HILB display is false as printed. | The definition shard includes only the sound inner-product identity; the corrected squared estimate remains a `proved-mod-audit` result, never a cited definition. |
| R16 | The pinned source contains invalid theorem-proof steps elsewhere. | Only sound definitions may be cited from it.  All repaired proof claims stay `proved-mod-audit` until af validation. |
| R17 | Parent dependency rewiring changes direct, but not transitive, imports. | Apply exactly the lists in §2 in a later registry pass; regenerate the DAG and confirm no cycle before seeding. |
| R18 | The projections are estimates, not guarantees. | Every workspace retains the repository balloon tripwire.  A projected overflow is a factor signal, not permission to increase node/depth limits. |
| R19 | Phase 5 is not sourced by this brief. | Do not invent F0/F2/F3 contracts here; use the separately pinned W73/phase-5 material. |
| R20 | No reviewer has adjudicated this architecture yet. | This document remains a design proposal for the separate fresh hostile decomposition reviewer named by `BRIEF-FUDW-VERIFY.md`. |

## 6. Closure statement

This design changes no existing contract and proposes no disjunctive route.
Its four parent assemblies project to 10/2, 9/2, 8/2, and 7/2,
respectively.  The supplied hostile-verified mathematics is fully assigned to
atomic proposed shards.  The deliberately unresolved surface is explicit:
six `stated` source-premise prover targets, seven contingent cited topology
leaves, and the ordinary uncertainty of af node projections.  There is no
invented proof, no hidden status promotion, and no claimed L0 closure.
