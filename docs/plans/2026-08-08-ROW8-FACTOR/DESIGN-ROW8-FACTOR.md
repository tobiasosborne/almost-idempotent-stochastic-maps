Status: DESIGN ONLY / NON-RIGOROUS / DO NOT SHARD, SEED, OR PROMOTE — pending fresh hostile audit and user ratification.

# DESIGN — factor ledger row 8 after the 2026-08-08 balloon abort

Date: 2026-08-08
Role: fresh factoring designer
Disposition: NATURAL TWO-ROW SPLIT FITS THE BUDGETS; NO DEVIATION PROPOSED

This design factors the aborted row at the exact natural branch boundaries prescribed by
`BRIEF-ROW8-FACTOR.md`.  The finite-dimensional Choi/twirl, nonzero-multiplicity repair,
and CP construction (old branches 1.2--1.4) become one row.  The amplification-uniform
approximate-left-inverse estimate (old branch 1.5) becomes a second row.  Ambient fixing
(old branch 1.1) and the final cb telescope (old branch 1.6) remain in the frozen main row.
The source mathematics is still only a design until fresh hostile audit, user ratification,
separate af proofs, and fresh adversarial verification.

## 1. New registry shard 1 — component construction

The following is the complete proposed shard, ready to land verbatim only after the guard
at the head of this file is released.

```markdown
---
id: lem-routef-upsilon-prime-component-construction
kind: lemma
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, with C_N, C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon' there exist an integer m >= 1, nonzero finite-dimensional Hilbert spaces L_j and E_j for 1 <= j <= m, a finite-dimensional Hilbert space F, operators W_j:H->L_j tensor E_j, an isometry V:H->H tensor F, nonempty finite index sets Sigma_j, unitaries U_js on L_j and weights p_js for s in Sigma_j, positive contractions C_j on E_j, unit vectors xi_j in E_j, contractions Lambda_j:L_j->H tensor F, CP maps Upsilon'_j:B(H)->B(L_j), and a CP map Upsilon':B(H)->B such that B=direct-sum_{j=1}^m B(L_j), sum_j W_j^*W_j=I_H, Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B, Phi(T)=V^*(T tensor I_F)V for every T in B(H), p_js >= 0, sum_{s in Sigma_j}p_js=1, sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/dim(L_j)) for every Z in B(L_j tensor E_j), where Tr_Lj denotes the unnormalized partial trace over L_j, R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej)=I_Lj tensor C_j, 0 <= C_j <= I_Ej, ||C_j|| >= 1-C_R*eta, 1-<xi_j,C_j^*C_j xi_j> <= 2*C_R*eta, if hat-U_js denotes U_js in the j-th block of B and zero in every other block and iota_js(z):=U_js z tensor xi_j then Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js, Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j, Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m, and ||Upsilon'||_cb <= 1.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-raw-factor-norms; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 8 (TeX 2831-2895; K-ledger 228-245; audit 181-209); DESIGN-ROW8-FACTOR.md sects-1,4-6 (natural branch 1.2-1.4 factoring, 2026-08-08); TREE-ROW8-ABORTED.md balloon-abort classification (2026-08-08: 28 live nodes exceeded NODE_SOFT_CAP 26)
owner: A
workspace: proofs/lem-routef-upsilon-prime-component-construction
---

**Status.** `stated` design transcription only.  This shard promotes nothing and may not
be seeded before fresh hostile audit and user ratification.

**Ambient binding.** The contract repeats the family's complete global-W_RF-first and
per-input-S binding.  `Delta'` and `Delta` are quantified from their declared providers;
all remaining scalar and map notation is carried by
[[def-routef-raw-factor-setting]] or defined in the contract itself.

**Factoring role.** This row contains exactly old branches 1.2--1.4: finite-dimensional
Stinespring/Choi data, an explicit Weyl twirl, the `(2*C_R)^(-1)` nonvanishing repair, and
the componentwise CP construction.  It exports the actual witness package consumed by
[[lem-routef-upsilon-prime-left-inverse]] and the frozen main row.

**Designed af budget.** Seven nodes; honest live expectation 11--21 nodes under the
observed 1.5--3x expansion; at most 5 rounds; hard cap 26.  A cap hit is a new factoring
stop, not permission to enlarge the cap.
```

## 2. New registry shard 2 — uniform approximate left inverse

The following is the complete proposed shard, ready to land verbatim only after the guard
at the head of this file is released and shard 1 is T0.

```markdown
---
id: lem-routef-upsilon-prime-left-inverse
kind: lemma
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every componentwise package (m,(L_j,E_j,W_j,Sigma_j,U_js,p_js,C_j,xi_j,Lambda_j,Upsilon'_j)_{j=1}^m,F,V,Upsilon') supplied for (W_RF,S,Delta',Delta) by lem-routef-upsilon-prime-component-construction, with C_L:=C_2+C_3+2*C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every integer q >= 1, and every Y=(Y_1,...,Y_m) in M_q(B)=direct-sum_{j=1}^m M_q(B(L_j)), ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= C_L*eta*||Y|| for every j, and consequently ||(Upsilon' Delta-I_B)_q(Y)|| <= C_L*eta*||Y|| and ||Upsilon' Delta-I_B||_cb <= C_L*eta.
defs: def-routef-raw-factor-setting; def-ucp-map
deps: lem-routef-raw-factor-setting-formation; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-degree-three-estimate; lem-routef-upsilon-prime-component-construction
status: stated
af: none
provenance: DESIGN-LEDGER-DOMAINS-v2.md sect-2 row 8 (TeX 2831-2895; K-ledger 228-245; audit 181-209); DESIGN-ROW8-FACTOR.md sects-2,4-6 (natural branch 1.5 factoring, 2026-08-08); TREE-ROW8-ABORTED.md balloon-abort classification (2026-08-08: 28 live nodes exceeded NODE_SOFT_CAP 26)
owner: A
workspace: proofs/lem-routef-upsilon-prime-left-inverse
---

**Status.** `stated` design transcription only.  This shard promotes nothing and may not
be seeded before fresh hostile audit, user ratification, and af validation of
[[lem-routef-upsilon-prime-component-construction]].

**Ambient binding.** The contract repeats the family's complete global-W_RF-first and
per-input-S binding, then quantifies `Delta'`, `Delta`, and every component package from
their declared providers.  Thus no amplification, block, or construction symbol relies on
the design preamble.

**Factoring role.** This row contains exactly old branch 1.5.  It exports both the
component estimate and the cb estimate so the frozen main row can use it as a black box.
Probability weights and the direct-sum maximum norm introduce no multiplicity, block-count,
or amplification factor.

**Designed af budget.** Five nodes; honest live expectation 8--15 nodes under the observed
1.5--3x expansion; at most 4 rounds; hard cap 20.  A cap hit is a new factoring stop, not
permission to enlarge the cap.
```

## 3. Frozen main row — contract unchanged, dependencies extended

The main contract below is copied byte-for-byte from the current registry shard.  It must
not be edited during landing:

```text
contract: After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every Choi multiplicity space used below is nonzero and the componentwise construction produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta.
```

Only the following `deps:` line is proposed.  It preserves every current dependency in
the same order and adds the two new ids at the end:

```text
deps: lem-routef-raw-factor-setting-formation; lem-routef-functional-calculus-closeness; lem-routef-raw-factor-norms; lem-routef-raw-factor-identities; lem-routef-delta-prime-closeness; lem-routef-delta-normalization-closeness; lem-routef-degree-two-estimate; lem-routef-degree-three-estimate; lem-routef-upsilon-prime-component-construction; lem-routef-upsilon-prime-left-inverse
```

No `defs:` change is needed.  The pre-existing aborted workspace must be cleanly re-seeded
after ratification; updating it with duplicate `def-add` entries is forbidden because name
lookup can retain stale copies.

## 4. Complete af tree skeletons

Every statement below is the exact proposed node statement.  The numbering is local to
each target.  Sibling statements may cite earlier validated siblings in the same workspace,
as in the aborted tree.

### 4.1 `lem-routef-upsilon-prime-component-construction` — 7 designed nodes

- **Node 1 — Root.** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, with C_N, C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon' there exist an integer m >= 1, nonzero finite-dimensional Hilbert spaces L_j and E_j for 1 <= j <= m, a finite-dimensional Hilbert space F, operators W_j:H->L_j tensor E_j, an isometry V:H->H tensor F, nonempty finite index sets Sigma_j, unitaries U_js on L_j and weights p_js for s in Sigma_j, positive contractions C_j on E_j, unit vectors xi_j in E_j, contractions Lambda_j:L_j->H tensor F, CP maps Upsilon'_j:B(H)->B(L_j), and a CP map Upsilon':B(H)->B such that B=direct-sum_{j=1}^m B(L_j), sum_j W_j^*W_j=I_H, Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B, Phi(T)=V^*(T tensor I_F)V for every T in B(H), p_js >= 0, sum_{s in Sigma_j}p_js=1, sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/dim(L_j)) for every Z in B(L_j tensor E_j), where Tr_Lj denotes the unnormalized partial trace over L_j, R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej)=I_Lj tensor C_j, 0 <= C_j <= I_Ej, ||C_j|| >= 1-C_R*eta, 1-<xi_j,C_j^*C_j xi_j> <= 2*C_R*eta, if hat-U_js denotes U_js in the j-th block of B and zero in every other block and iota_js(z):=U_js z tensor xi_j then Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js, Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j, Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m, and ||Upsilon'||_cb <= 1.
- **Node 1.1 — Finite-dimensional Choi data.** Under the root hypotheses there are m >= 1 and nonzero finite-dimensional Hilbert spaces L_j such that B=direct-sum_{j=1}^m B(L_j); complete positivity of the UCP map Delta gives finite-dimensional Hilbert spaces E_j, provisionally allowed to be zero, and operators W_j:H->L_j tensor E_j satisfying sum_j W_j^*W_j=I_H and Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B; complete positivity and unitality of Phi give a finite-dimensional Hilbert space F and an isometry V:H->H tensor F satisfying Phi(T)=V^*(T tensor I_F)V for every T in B(H).
- **Node 1.2 — Explicit Weyl twirl.** For every j, let d_j:=dim(L_j), fix an orthonormal basis (e_j[k])_{0 <= k < d_j}, put Sigma_j:={0,...,d_j-1}^2, and for s=(a,b) in Sigma_j define U_js e_j[k]:=exp(2*pi*i*a*k/d_j)e_j[(k+b) mod d_j] and p_js:=d_j^(-2); then every U_js is unitary, p_js >= 0, sum_{s in Sigma_j}p_js=1, and for every Z in B(L_j tensor E_j), sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/d_j), where Tr_Lj denotes the unnormalized partial trace over L_j; this twirl is a positive order-preserving contraction onto I_Lj tensor B(E_j).
- **Node 1.3 — Twirl contraction and lower bound.** For every j define R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej); then R_j=I_Lj tensor C_j for a positive contraction C_j on E_j, and, writing hat-U_js for U_js in the j-th block of B and zero elsewhere, W_j^*R_jW_j=sum_{s in Sigma_j}p_js*Delta(hat-U_js^*)Delta(hat-U_js), so lem-routef-degree-two-estimate, lem-routef-raw-factor-norms, and lem-routef-delta-normalization-closeness give ||C_j|| >= 1-(C_V+C_Delta+C_2)*eta=1-C_R*eta.
- **Node 1.4 — Nonzero multiplicity and selected vector.** Since eta <= (2*C_R)^(-1), node 1.3 gives ||C_j|| >= 1/2, so E_j is nonzero; finite-dimensional norm attainment gives a unit vector xi_j in E_j with ||C_j xi_j||=||C_j||, and positivity of C_j gives 0 <= 1-<xi_j,C_j^*C_j xi_j>=1-||C_j||^2 <= 2*C_R*eta.
- **Node 1.5 — Component contractions.** For every j and s in Sigma_j define iota_js:L_j->L_j tensor E_j by iota_js(z):=U_js z tensor xi_j and define Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js; each iota_js and V is an isometry, Delta is UCP, ||W_j|| <= 1, and the p_js form a probability distribution, hence ||Lambda_j|| <= 1.
- **Node 1.6 — CP direct-sum construction.** Define Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j and Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m; tensoring the CP map Phi with I_F, compression by Lambda_j, and finite direct sums preserve complete positivity, so every Upsilon'_j and Upsilon' are CP, and at every amplification the direct-sum maximum norm and ||Lambda_j|| <= 1 give ||Upsilon'||_cb <= 1 with no block-count or amplification factor.

Designed count: 7.  Honest live expectation: 11--21.  Maximum rounds: 5.
Hard cap: 26.

### 4.2 `lem-routef-upsilon-prime-left-inverse` — 5 designed nodes

- **Node 1 — Root.** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every componentwise package (m,(L_j,E_j,W_j,Sigma_j,U_js,p_js,C_j,xi_j,Lambda_j,Upsilon'_j)_{j=1}^m,F,V,Upsilon') supplied for (W_RF,S,Delta',Delta) by lem-routef-upsilon-prime-component-construction, with C_L:=C_2+C_3+2*C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every integer q >= 1, and every Y=(Y_1,...,Y_m) in M_q(B)=direct-sum_{j=1}^m M_q(B(L_j)), ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= C_L*eta*||Y|| for every j, and consequently ||(Upsilon' Delta-I_B)_q(Y)|| <= C_L*eta*||Y|| and ||Upsilon' Delta-I_B||_cb <= C_L*eta.
- **Node 1.1 — Degree-two replacement.** For every q >= 1 and Y in M_q(B), unitality gives Delta_q(I)=I; applying lem-routef-degree-two-estimate to (Y,I) gives ||Phi_q(Delta_q(Y))-Delta_q(Y)|| <= C_2*eta*||Y||, and compression by the contraction Lambda_j shows that replacing Phi_q(Delta_q(Y)) by Delta_q(Y) inside (Upsilon'_j)_q(Delta_q(Y)) costs at most C_2*eta*||Y||.
- **Node 1.2 — Double-average degree-three replacement.** Put A_js:=(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js, so Lambda_j=sum_{s in Sigma_j}p_js*A_js; after node 1.1 the amplified expression is sum_{s,t in Sigma_j}p_js*p_jt*(A_js)_q^*(Delta_q(Y) tensor I_F)(A_jt)_q, and the Stinespring identity for Phi rewrites it as the same double average of compressions of Phi_q(Delta_q(hat-U_js)Delta_q(Y)Delta_q(hat-U_jt^*)); lem-routef-degree-three-estimate replaces these middle terms by Delta_q(hat-U_js Y hat-U_jt^*) with total averaged error at most C_3*eta*||Y||.
- **Node 1.3 — Exact twirl identity.** The Choi formula for Delta, the fact that hat-U_js Y hat-U_jt^* has only j-th block U_js Y_j U_jt^*, and iota_js=(U_js tensor I_Ej)J_xi_j transform the replaced double average exactly into (I_q tensor J_xi_j)^*(I_q tensor R_j)(Y_j tensor I_Ej)(I_q tensor R_j)(I_q tensor J_xi_j)=alpha_j Y_j, where J_xi_j(z):=z tensor xi_j and alpha_j:=<xi_j,C_j^*C_j xi_j>.
- **Node 1.4 — Component and cb assembly.** Nodes 1.1--1.3 give ||(Upsilon'_j)_q(Delta_q(Y))-alpha_j Y_j|| <= (C_2+C_3)*eta*||Y||, while the component-construction contract gives 0 <= 1-alpha_j <= 2*C_R*eta; hence ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= (C_2+C_3+2*C_R)*eta*||Y||=C_L*eta*||Y||, and taking the direct-sum maximum followed by the suprema over nonzero Y and q gives ||Upsilon' Delta-I_B||_cb <= C_L*eta with no multiplicity, block-count, or amplification factor.

Designed count: 5.  Honest live expectation: 8--15.  Maximum rounds: 4.
Hard cap: 20.

### 4.3 Slimmed `lem-routef-upsilon-prime-closeness` — 4 designed nodes

- **Node 1 — Root.** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Upsilon-prime CP closeness: with C_N, C_R, C_L, C_Upsilon' from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every Choi multiplicity space used below is nonzero and the componentwise construction produces CP Upsilon' with ||Upsilon' - tilde-Upsilon||_cb <= C_Upsilon'*eta.
- **Node 1.1 — Ambient fixing and imported branch outputs.** Invoke lem-routef-raw-factor-setting-formation to fix W_RF once and then S, take Delta' and Delta from their providers, take a component package from lem-routef-upsilon-prime-component-construction, and apply lem-routef-upsilon-prime-left-inverse to that same package; for 0 <= eta <= rho_Upsilon', all named dependencies are applicable, every E_j is nonzero, Upsilon' is CP with ||Upsilon'||_cb <= 1, ||Upsilon' Delta-I_B||_cb <= C_L*eta, lem-routef-raw-factor-norms and the two rho_T guards give ||tilde-Upsilon||_cb <= 1+C_T*eta <= 2, and lem-routef-raw-factor-identities gives tilde-Phi=tilde-Delta tilde-Upsilon.
- **Node 1.2 — Idempotence comparison.** For every q >= 1, T in M_q(B(H)), and component j, the construction formula gives (Upsilon'_j)_q(Phi_q(T))-(Upsilon'_j)_q(T)=(Lambda_j)_q^*(((Phi_q^2-Phi_q)(T)) tensor I_F)(Lambda_j)_q; the formation input bound, ||Lambda_j|| <= 1, and the direct-sum maximum therefore give ||Upsilon' Phi-Upsilon'||_cb <= eta.
- **Node 1.3 — Final cb telescope.** Apply the cb triangle inequality along Upsilon' -> Upsilon' Phi -> Upsilon' tilde-Phi = Upsilon' tilde-Delta tilde-Upsilon -> Upsilon' Delta tilde-Upsilon -> tilde-Upsilon; node 1.2 costs eta, lem-routef-functional-calculus-closeness and ||Upsilon'||_cb <= 1 cost C_theta*eta, lem-routef-raw-factor-identities gives the equality, lem-routef-delta-normalization-closeness and ||tilde-Upsilon||_cb <= 2 cost 2*C_Delta*eta, and lem-routef-upsilon-prime-left-inverse with the same raw bound costs 2*C_L*eta, so ||Upsilon'-tilde-Upsilon||_cb <= (1+C_theta+2*C_Delta+2*C_L)*eta=C_Upsilon'*eta.

Designed count: 4.  Honest live expectation: 6--12.  Maximum rounds: 4.
Hard cap: 18.

## 5. Seeding packages

No command in this section is authorized by this design.  It records the exact future
inputs so a hostile auditor can check for omissions and byte drift.

### 5.1 Shared `def-add` list

For each of the three targets, add the complete bytes of these files under the displayed
names, in this order:

1. `def-routef-raw-factor-setting` <- `definitions/def-routef-raw-factor-setting.md`
2. `def-ucp-map` <- `definitions/def-ucp-map.md`
3. `def-extended-epsilon-cstar-algebra` <- `definitions/def-extended-epsilon-cstar-algebra.md`
4. `def-extended-delta-inclusion` <- `definitions/def-extended-delta-inclusion.md`
5. `def-epsilon-cstar-algebra` <- `definitions/def-epsilon-cstar-algebra.md`
6. `def-operator-space` <- `definitions/def-operator-space.md`

This is the same vocabulary package used by the aborted row-8 workspace.  No new
definition is proposed.

### 5.2 Exact `add-external` source-string dictionary

The following dictionary is authoritative for the per-target lists in sect-5.3.  Each
registry source is the literal path-plus-em-dash convention followed by the dependency's
byte-verbatim contract.

**E0 — `GT-kitaev-def-delta-homomorphism`**

```text
approximate_algebras.tex:443-456 (verbatim): \begin{Definition}
A \emph{$\delta$-homomorphism} from an $\eps'$-Banach algebra $\calA'$ to an $\eps''$-Banach algebra $\calA''$ is a bounded linear map $v\colon \calA'\to\calA''$ that almost preserves the unit and the multiplication:
\begin{align}
\label{hom_unit}
\|v(I)-I\|&\le \delta,\\[2pt]
\label{hom_mult}
\|v(XY)-v(X)v(Y)\|&\le \delta\ts\|X\|\ts\|Y\|\qquad (X,Y\in \calA').
\end{align}
A \emph{non-unital $\delta$-homomorphism} is defined by imposing only condition \eqref{hom_mult}. In the $*$-algebra setting, it is also required that $v(X^\dag)=v(X)^\dag$. A \emph{$\delta$-inclusion} is a $\delta$-homomorphism such that
\begin{equation}
(1-\delta)\ts\|X\|\le \|v(X)\|\le (1+\delta)\ts\|X\|\qquad (X\in \calA').
\end{equation}
A \emph{$\delta$-isomorphism} is a bijective $\delta$-inclusion.
\end{Definition}
```

**E1 — `lem-routef-raw-factor-setting-formation`**

```text
imports validated registry lemma proofs/lem-routef-raw-factor-setting-formation — Route F raw-factor setting formation: there exists one choice W_RF of the scalar header of def-routef-raw-factor-setting, independent of H, Phi, eta, dimension, amplification level, and block data, with C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, eta_A>0 and (C_A,eta_A) the fixed witnesses of lem-routef-ai-defect-linearization, C_E<infinity and epsilon_E>0 the fixed witnesses of lem-thmainext-conditional, rho_theta:=1/8, rho_AI:=eta_A, and all remaining named scalar quantities defined by (1.1)-(1.8), such that for every nonzero finite-dimensional Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta with 0 <= eta <= rho_id^corr and ||Phi^2-Phi||_cb <= eta, there exist a finite-dimensional unital C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and a def-routef-raw-factor-setting datum S over this same W_RF whose fields are the displayed H,Phi,eta,B,v,u=v^(-1) and the canonical tilde-Phi,A,star,epsilon_AI(eta),tilde-Delta,tilde-Upsilon notation, with tilde-Phi^2=tilde-Phi, A an extended epsilon_AI(eta)-C*-algebra, and 0 <= epsilon_AI(eta) <= C_A*eta <= epsilon_E.
```

**E2 — `lem-routef-functional-calculus-closeness`**

```text
imports validated registry lemma proofs/lem-routef-functional-calculus-closeness — Functional-calculus closeness: for 0 <= eta <= 1/8, the exact functional-calculus projector satisfies ||tilde-Phi-Phi||_cb <= C_theta*eta, where C_theta=12*(sqrt(2)-1).
```

**E3 — `lem-routef-raw-factor-norms`**

```text
imports validated registry lemma proofs/lem-routef-raw-factor-norms — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result; for every integer n >= 1 and every X in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map norms: with C_V, C_T, rho_T from (1.1), for 0 <= eta <= rho_T, every amplification satisfies (1-C_V*eta)*||X|| <= ||tilde-Delta_n X|| <= (1+C_V*eta)*||X|| and max{||tilde-Delta||_cb, ||tilde-Upsilon||_cb} <= 1+C_T*eta.
```

**E4 — `lem-routef-raw-factor-identities`**

```text
imports validated registry lemma proofs/lem-routef-raw-factor-identities — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B.
```

**E5 — `lem-routef-delta-prime-closeness`**

```text
imports validated registry lemma proofs/lem-routef-delta-prime-closeness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Delta-prime CP closeness: with C_Delta' := C_T+4*C_theta and rho_Delta' := min{rho_T, rho_prod}, for 0 <= eta <= rho_Delta', the repaired norm-one diagonal produces a CP map Delta' with ||Delta' - tilde-Delta||_cb <= C_Delta'*eta.
```

**E6 — `lem-routef-delta-normalization-closeness`**

```text
imports validated registry lemma proofs/lem-routef-delta-normalization-closeness — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result and for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and for every X in S.B, writing the fields of (W_RF,S) as the unqualified symbols below: Delta UCP normalization: with C_Delta := 6*C_T+7*C_Delta' and rho_Delta := min{rho_unit, rho_Delta', [2*(C_T+C_Delta')]^(-1)}, for 0 <= eta <= rho_Delta, a = Delta'(I) is invertible and Delta(X) = a^(-1/2)*Delta'(X)*a^(-1/2) is UCP with ||Delta - tilde-Delta||_cb <= C_Delta*eta.
```

**E7 — `lem-routef-degree-two-estimate`**

```text
imports validated registry lemma proofs/lem-routef-degree-two-estimate — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Route F degree-two estimate: with C_2 := C_Delta'+4*C_Delta and rho_2 := min{rho_prod, rho_Delta', rho_Delta}, for 0 <= eta <= rho_2, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y) - Delta_n(XY)|| <= C_2*eta*||X||*||Y||.
```

**E8 — `lem-routef-degree-three-estimate`**

```text
imports validated registry lemma proofs/lem-routef-degree-three-estimate — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y, Z in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Route F degree-three estimate: with C_3 := 10+20*C_Delta+12*C_theta+2*C_Delta' and rho_3 := min{rho_theta, rho_Delta', rho_Delta, rho_2}, for 0 <= eta <= rho_3, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y Delta_n Z) - Delta_n(XYZ)|| <= C_3*eta*||X||*||Y||*||Z||.
```

**E9 — `lem-routef-upsilon-prime-component-construction`**

```text
imports validated registry lemma proofs/lem-routef-upsilon-prime-component-construction — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, with C_N, C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon' there exist an integer m >= 1, nonzero finite-dimensional Hilbert spaces L_j and E_j for 1 <= j <= m, a finite-dimensional Hilbert space F, operators W_j:H->L_j tensor E_j, an isometry V:H->H tensor F, nonempty finite index sets Sigma_j, unitaries U_js on L_j and weights p_js for s in Sigma_j, positive contractions C_j on E_j, unit vectors xi_j in E_j, contractions Lambda_j:L_j->H tensor F, CP maps Upsilon'_j:B(H)->B(L_j), and a CP map Upsilon':B(H)->B such that B=direct-sum_{j=1}^m B(L_j), sum_j W_j^*W_j=I_H, Delta(X)=sum_j W_j^*(X_j tensor I_Ej)W_j for every X=(X_1,...,X_m) in B, Phi(T)=V^*(T tensor I_F)V for every T in B(H), p_js >= 0, sum_{s in Sigma_j}p_js=1, sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)Z(U_js tensor I_Ej)=I_Lj tensor (Tr_Lj(Z)/dim(L_j)) for every Z in B(L_j tensor E_j), where Tr_Lj denotes the unnormalized partial trace over L_j, R_j:=sum_{s in Sigma_j}p_js*(U_js^* tensor I_Ej)W_jW_j^*(U_js tensor I_Ej)=I_Lj tensor C_j, 0 <= C_j <= I_Ej, ||C_j|| >= 1-C_R*eta, 1-<xi_j,C_j^*C_j xi_j> <= 2*C_R*eta, if hat-U_js denotes U_js in the j-th block of B and zero in every other block and iota_js(z):=U_js z tensor xi_j then Lambda_j:=sum_{s in Sigma_j}p_js*(Delta(hat-U_js^*) tensor I_F)V W_j^*iota_js, Upsilon'_j(T):=Lambda_j^*(Phi(T) tensor I_F)Lambda_j, Upsilon'(T):=(Upsilon'_j(T))_{j=1}^m, and ||Upsilon'||_cb <= 1.
```

**E10 — `lem-routef-upsilon-prime-left-inverse`**

```text
imports validated registry lemma proofs/lem-routef-upsilon-prime-left-inverse — After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, and every componentwise package (m,(L_j,E_j,W_j,Sigma_j,U_js,p_js,C_j,xi_j,Lambda_j,Upsilon'_j)_{j=1}^m,F,V,Upsilon') supplied for (W_RF,S,Delta',Delta) by lem-routef-upsilon-prime-component-construction, with C_L:=C_2+C_3+2*C_R from (1.3) and rho_Upsilon' := min{rho_T, rho_id, rho_Delta, rho_2, rho_3, (2*C_R)^(-1)}, for 0 <= eta <= rho_Upsilon', every integer q >= 1, and every Y=(Y_1,...,Y_m) in M_q(B)=direct-sum_{j=1}^m M_q(B(L_j)), ||(Upsilon'_j)_q(Delta_q(Y))-Y_j|| <= C_L*eta*||Y|| for every j, and consequently ||(Upsilon' Delta-I_B)_q(Y)|| <= C_L*eta*||Y|| and ||Upsilon' Delta-I_B||_cb <= C_L*eta.
```

### 5.3 Exact per-target lists

- `lem-routef-upsilon-prime-component-construction`: add E0, E1, E3, E5,
  E6, E7, in that order.  E1/E3/E5/E6/E7 are exactly its declared deps.
- `lem-routef-upsilon-prime-left-inverse`: add E0, E1, E5, E6, E7, E8,
  E9, in that order.  Seed only after E9's workspace is validated and clean.
- `lem-routef-upsilon-prime-closeness`: add E0, E1, E2, E3, E4, E5, E6,
  E7, E8, E9, E10, in that order.  These are exactly the frozen row's ten
  revised deps plus the shared ground-truth external E0.

## 6. Elevation order and budgets

1. After hostile audit and user ratification, land and seed
   `lem-routef-upsilon-prime-component-construction`; use 7 designed nodes,
   expect 11--21 live nodes, allow at most 5 rounds, and enforce hard cap 26.
2. Only after target 1 is af-validated and banked T0, land and seed
   `lem-routef-upsilon-prime-left-inverse`; use 5 designed nodes, expect 8--15
   live nodes, allow at most 4 rounds, and enforce hard cap 20.
3. Only after both sub-lemmas are af-validated and banked T0, append their ids
   to the main row's `deps:`, discard/rebuild the aborted seed cleanly, and
   elevate the byte-frozen main contract; use 4 designed nodes, expect 6--12
   live nodes, allow at most 4 rounds, and enforce hard cap 18.

Every target uses a fresh prover and separate fresh hostile verifier(s), bottom-up.  Any
hard-cap hit is classified as `MISSING fact`, `DAG dep`, or `genuine gap`; no cap is raised.

## 7. Ranked hostile-audit attack list

1. **Ambient quantifiers and witness identity.** Check that the exact required prefix is
   present in both new contracts and that `Delta'`, `Delta`, and the component package are
   quantified from the same `(W_RF,S)` rather than silently reselected.
2. **Type correctness of the component package.** Check every domain/codomain in the Choi
   formulas, especially `W_j^*iota_js`, `V`, `Lambda_j`, and the two tensor identities.
3. **The double-average algebra.** Recompute adjoint order in `A_js`, the two Weyl indices,
   and the conversion to the degree-three expression; a swapped star would invalidate the
   exact `alpha_j Y_j` identity.
4. **Amplification uniformity.** Verify every operation in nodes 4.2.1--4.2.4 commutes with
   amplification and that no hidden factor depending on `q` is introduced.
5. **Nonzero-multiplicity repair.** Attack the inference `||C_j|| >= 1/2 => E_j != 0`, the
   finite-dimensional norm-attaining choice of `xi_j`, and the scalar inequality
   `1-||C_j||^2 <= 2*C_R*eta`.
6. **CP and cb-norm assembly.** Check that `T |-> Phi(T) tensor I_F`, compression, and the
   finite direct sum are CP at every level, and that the direct-sum norm is a maximum rather
   than a sum.
7. **Dependency sufficiency and T0 order.** Check that shard 1 really needs no D3 or raw
   identity edge, shard 2 needs no undeclared raw edge, and no target is seeded before every
   declared dependency is T0.
8. **Final telescope constants.** Recompute the five costs as
   `1, C_theta, 0, 2*C_Delta, 2*C_L` and check the exact identity
   `C_Upsilon'=1+C_theta+2*C_Delta+2*C_L` from (1.3).
9. **Contract/source fidelity.** Compare TeX 2831--2895, K-ledger 228--245, audit 181--209,
   the aborted tree, both proposed contracts, and E9/E10 byte-for-byte; reject documentary
   shorthand that changes the mathematical interface.
10. **Budget realism.** Treat any proof-worker split beyond 21/15/12 expected live nodes as
    an early brittleness warning, and enforce the declared 26/20/18 caps without exception.
