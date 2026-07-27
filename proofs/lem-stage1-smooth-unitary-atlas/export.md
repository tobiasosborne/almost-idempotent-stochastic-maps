# Proof Export

## Node 1

**Statement:** Smooth graph-atlas upgrade: for every finite-dimensional exact-unit epsilon_r-C*-algebra, if calU is covered by the unique C^1 graph functions g_V of lem-stage1-unitary-graph-control and D_{A^perp} f_V is invertible at every graph point, then those same g_V are C^infinity, and the same graph charts make calU a smooth embedded manifold; no point or first derivative of a graph or chart is changed.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For each graph-chart center V, the defining map Phi_V:iH x H -> H, Phi_V(P,Q)=f_V(P+Q), is C^infinity: with the displayed parenthesization it is a real polynomial of degree at most two.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By def-epsilon-cstar-algebra, bold-dot is complex-bilinear and dagger is conjugate-linear, hence bold-dot is real-bilinear and dagger is real-linear; therefore A=P+Q maps through the fixed-parenthesized expression defining f_V by sums and compositions of real-linear and real-bilinear maps, so Phi_V is a real polynomial of degree at most two and is C^infinity in finite dimension.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Writing B=V bold-dot (J+P+Q), the exact involution axioms of def-epsilon-cstar-algebra give B^dagger=(J+(P+Q)^dagger) bold-dot V^dagger and (B^dagger bold-dot B)^dagger=B^dagger bold-dot B without any reassociation; since J^dagger=J, Phi_V(P,Q)=(B^dagger bold-dot B-J)/2 belongs to H.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** At every graph point (P,g_V(P)), the invertibility hypothesis and GT-lee-2ed-thm-C.40 produce a neighborhood on which the zero set Phi_V^{-1}(0) is the graph of a C^infinity function F.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** The finite-dimensional real spaces iH and H can be linearly identified with R^n and R^k; the bilinear-product and real-linear-involution calculation from def-epsilon-cstar-algebra makes Phi_V smooth on the open ambient product, and lem-stage1-unitary-graph-control gives Phi_V(P,g_V(P))=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** At (P,g_V(P)), the derivative of Q mapsto Phi_V(P,Q) is exactly D_{A^perp}f_V(P+g_V(P)), which is invertible by the hypothesis of node 1; applying GT-lee-2ed-thm-C.40 with c=0 yields neighborhoods O_P,O_Q and a C^infinity F:O_P->O_Q such that Phi_V(P',Q')=0 in O_P x O_Q if and only if Q'=F(P').

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The local implicit function F equals the already-given g_V after shrinking its neighborhood; consequently each unchanged g_V is C^infinity on its full graph domain, and its points and first derivative are unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By lem-stage1-unitary-graph-control, g_V is C^1 (hence continuous), takes values in the permitted H-ball, satisfies Phi_V(P',g_V(P'))=0, and is the unique such graph branch there; shrink O_P and O_Q around (P,g_V(P)) so continuity keeps g_V(O_P) inside O_Q, then the implicit zero-set equivalence forces g_V=F on O_P. Doing this at every P proves g_V is C^infinity everywhere on its original domain; equality with the original C^1 function is pointwise, so uniqueness of derivatives leaves its existing first derivative unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The unchanged graph parametrizations and their unchanged coordinate inverses are smooth and compatible; because they cover calU and realize it locally as graphs of smooth maps, they make calU a smooth embedded manifold without changing any graph or chart.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** In each graph coordinate supplied by lem-stage1-unitary-graph-control, the parametrization P mapsto (P,g_V(P)) is smooth and its inverse on the graph is the real-linear projection to iH; after the already-supplied affine-linear chart-coordinate transport (notation phi_V from def-approximate-unitary-space), the parametrization and inverse remain smooth, so each chart realizes calU locally as an embedded smooth graph.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** On an overlap, the transition map is the unchanged target-chart coordinate projection composed with the unchanged source graph parametrization; the coordinate transports and projections are affine-linear and the graph parametrizations are smooth, hence transitions are smooth. The cover is the same cover asserted by lem-stage1-unitary-graph-control, and every set, function, and coordinate map used is literally the old one, so the resulting embedded smooth atlas changes neither points nor charts (and node 1.3 preserves their first derivatives).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Self-contained smoothness bridge (independent of node 1.3): fix V and P in the original graph domain and put Phi_V(P_prime,Q_prime)=f_V(P_prime+Q_prime). By def-epsilon-cstar-algebra, bold-dot is real-bilinear and dagger is real-linear, so the fixed-parenthesized Phi_V is a smooth real polynomial. At (P,g_V(P)) it vanishes by lem-stage1-unitary-graph-control, and its Q-derivative is D_{A^perp}f_V(P+g_V(P)), invertible by the hypothesis of node 1. GT-lee-2ed-thm-C.40 therefore gives product neighborhoods O_P x O_Q and a smooth F:O_P->O_Q whose graph is exactly the local zero set. The original g_V is C^1, hence continuous, so after shrinking O_P it has g_V(O_P) subset O_Q; it satisfies Phi_V(P_prime,g_V(P_prime))=0, hence the zero-set equivalence gives g_V=F on O_P. Repeating at every P proves that the same original g_V is smooth on its full original domain. Because this is equality with the pre-existing C^1 function, its points and its first derivative are literally unchanged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.2

**Statement:** For overlapping original charts centered at V and W, write Psi_V for the unchanged source graph parametrization after its affine-linear coordinate transport and write pi_W for the unchanged target anti-Hermitian coordinate projection after the inverse affine-linear transport. On the original overlap the transition is pi_W composed with Psi_V. Its domain is open because the already-supplied C^1 graph charts are charts, and it is smooth because Psi_V uses the now-proved-smooth unchanged g_V while all transports and projections are affine-linear; interchanging V and W gives the smooth inverse. Thus the original cover and the original chart maps form a smooth compatible atlas. No underlying point, graph function, chart map, or first derivative has been replaced: the preceding child identifies each smooth graph function with the original C^1 function, and the remaining maps are exactly the old affine-linear ones.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

