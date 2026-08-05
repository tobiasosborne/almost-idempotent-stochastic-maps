# Proof Export

## Node 1

**Statement:** Entrywise CP-ization from the repaired diagonal: for the finite phase-balanced diagonal D=sum_t q_t W_t^dagger tensor W_t supplied by lem-kitaev-diagonal-repair, every involution-preserving linear map tilde-Delta:B->B(H) and every UCP map Phi define a completely positive map Delta'(X)=sum_t q_t Phi(tilde-Delta(X W_t^dagger) tilde-Delta(W_t)); complete positivity uses exact centrality of D and does not require exact multiplicativity of tilde-Delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The displayed formula for Delta' is linear in X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For each fixed t, the map X mapsto X W_t^dagger is linear, tilde-Delta is linear, right multiplication by the fixed operator tilde-Delta(W_t) is linear, and Phi is linear; hence X mapsto Phi(tilde-Delta(X W_t^dagger) tilde-Delta(W_t)) is linear.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** A finite scalar-weighted sum of linear maps is linear, so Delta' is linear.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every n at least 1 and every Y in M_n(B), if Z_t=tilde-Delta_n((I_n tensor W_t)Y), then the exact identity Delta'_n(Y^dagger Y)=sum_t q_t Phi_n(Z_t^dagger Z_t) holds.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By lem-kitaev-diagonal-repair, D=sum_t q_t W_t^dagger tensor W_t is exactly central. Thus for every pair of entries Y_ca,Y_cb, multiplying the equality Y_cb D=D Y_cb on the first tensor factor by Y_ca^dagger gives sum_t q_t Y_ca^dagger Y_cb W_t^dagger tensor W_t = sum_t q_t Y_ca^dagger W_t^dagger tensor W_t Y_cb.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** The rule beta(A tensor B)=tilde-Delta(A) tilde-Delta(B) is induced by a bilinear map and hence is linear on the algebraic tensor product; applying beta to the tensor equality gives sum_t q_t tilde-Delta(Y_ca^dagger Y_cb W_t^dagger) tilde-Delta(W_t) = sum_t q_t tilde-Delta(Y_ca^dagger W_t^dagger) tilde-Delta(W_t Y_cb).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Because B is finite-dimensional, the linear map tilde-Delta is bounded; operator multiplication is bounded, so (A,B) mapsto tilde-Delta(A)tilde-Delta(B) is a bounded bilinear map and therefore induces a continuous linear map beta on the projective tensor product B hat-tensor B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.2

**Statement:** Applying this beta to the equality in node 1.2.1 and evaluating beta(A tensor B)=tilde-Delta(A)tilde-Delta(B) gives sum_t q_t tilde-Delta(Y_ca^dagger Y_cb W_t^dagger) tilde-Delta(W_t) = sum_t q_t tilde-Delta(Y_ca^dagger W_t^dagger) tilde-Delta(W_t Y_cb).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Involution preservation gives tilde-Delta(Y_ca^dagger W_t^dagger)=tilde-Delta((W_t Y_ca)^dagger)=tilde-Delta(W_t Y_ca)^dagger, so the right side is sum_t q_t tilde-Delta(W_t Y_ca)^dagger tilde-Delta(W_t Y_cb).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Summing the entry identity over c and using linearity of Delta' and Phi shows entry by entry that Delta'_n(Y^dagger Y)=sum_t q_t Phi_n(Z_t^dagger Z_t), where Z_t has entries tilde-Delta(W_t Y_ab), equivalently Z_t=tilde-Delta_n((I_n tensor W_t)Y).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every n at least 1 and every Y in M_n(B), the operator sum_t q_t Phi_n(Z_t^dagger Z_t) is positive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For every t, Z_t^dagger Z_t is positive in M_n(B(H)).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Because Phi is UCP, def-ucp-map says Phi is completely positive; therefore its nth amplification Phi_n is positive and Phi_n(Z_t^dagger Z_t) is positive for every t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** By lem-kitaev-diagonal-repair every q_t is nonnegative, so the finite sum sum_t q_t Phi_n(Z_t^dagger Z_t) is positive because the positive cone is closed under nonnegative finite linear combinations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The preceding matrix-level identity and positivity prove that Delta' is completely positive, and the derivation uses no multiplicativity of tilde-Delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Every positive A in M_n(B) has a positive square root Y=A^(1/2), hence A=Y^dagger Y.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Applying the identity of node 1.2 and the positivity of node 1.3 to this square root gives Delta'_n(A) positive for every positive A in M_n(B).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** Since n was arbitrary, every amplification Delta'_n is positive; together with linearity from node 1.1, def-ucp-map's definition of complete positivity yields that Delta' is completely positive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.4

**Statement:** The algebraic derivation used only exact centrality from lem-kitaev-diagonal-repair, linearity and involution preservation of tilde-Delta, and linearity and complete positivity of Phi; it nowhere replaced tilde-Delta(AB) by tilde-Delta(A)tilde-Delta(B), so exact multiplicativity of tilde-Delta is not required.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.4.1

**Statement:** Correction to the exhaustive wording of node 1.4.4: the derivation also uses the phase-balanced coefficient data supplied by lem-kitaev-diagonal-repair, namely that the index set is finite and every q_t is nonnegative (indeed sum_t q_t=1). Thus, after the matrix-level identity is established using exact centrality together with linearity and involution preservation of tilde-Delta, complete positivity of Phi makes each Phi_n(Z_t^dagger Z_t) positive, and finiteness plus q_t>=0 makes their weighted sum positive. No step in either the identity or this positivity argument replaces tilde-Delta(AB) by tilde-Delta(A)tilde-Delta(B); hence exact multiplicativity of tilde-Delta is not required. The phrase used only in node 1.4.4 must be read with this coefficient hypothesis added.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Typing clarification forced by the displayed definition and fixed by the registry shard: throughout this corollary, the quantifier over Phi ranges over UCP maps Phi:B(H)->B(H). Indeed tilde-Delta(X W_t^dagger) and tilde-Delta(W_t) lie in B(H), hence their product lies in B(H), while the asserted codomain of Delta prime is B(H); thus the displayed formula is a well-typed definition precisely with this stated Phi type. Consequently Phi_n has domain M_n(B(H)) and codomain M_n(B(H)), as used in nodes 1.2.4 and 1.3.2. For H=C^2, id_C:C->C is not an element of this typed quantifier and therefore is not a counterexample. This is an explicit type annotation for the frozen formula, not an additional multiplicativity assumption on tilde-Delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

