# Proof Export

## Node 1

**Statement:** Finite triangulation of compact smooth manifolds: every compact smooth manifold without boundary is homeomorphic to a finite simplicial complex.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Hypothesis bridge and triangulation existence: if M is a compact smooth manifold without boundary, then its C^∞ atlas is in particular C^1, and GT-munkres-edt-def-1.1-non-bounded identifies empty boundary with M being non-bounded. Thus M is a non-bounded C^1 manifold, so GT-munkres-edt-thm-10.6 supplies a simplicial complex K and a C^1 triangulation f:K→M.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Meaning of triangulation: for any complex K and C^1 triangulation f:K→M supplied above, GT-munkres-edt-def-8.1 makes f a map |K|→M (class C^1 simplexwise), and GT-munkres-edt-def-8.3 says precisely that such a triangulation is a homeomorphism of |K| onto M.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Compactness transfer: if M is compact and f:|K|→M is a homeomorphism, then |K| is compact, since the continuous inverse f^{-1}:M→|K| maps the compact space M onto |K|.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Finite-complex step: if the realization |K| of a simplicial complex is compact, then K is finite. For each vertex v, let St°(v) be the union of the relative interiors of all simplices containing v. These sets are open in the realization topology, and they cover |K| because every point lies in the relative interior of a simplex. A vertex w lies in St°(v) exactly when w=v, since w lies in the relative interior of its zero-simplex alone. Compactness gives a finite subcover, so every vertex is one of its finitely many centers. Thus K has finitely many vertices, and its simplices, being finite subsets of that finite vertex set, are finite in number.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Assembly: let M be any compact smooth manifold without boundary. Node 1.1 supplies a complex K and a C^1 triangulation f:K→M; node 1.2 identifies f as a homeomorphism |K|→M; node 1.3 gives compactness of |K|; and node 1.4 then makes K a finite simplicial complex. Hence M is homeomorphic to the finite simplicial complex K, which is the root conclusion.

**Type:** qed

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

