# Proof Export

## Node 1

**Statement:** Every point of a finite polyhedron lies in a maximal simplex of its defining finite simplicial complex; therefore every point of every finite fixed set does.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let K be the defining finite simplicial complex and let x lie in its polyhedron |K|. By the definition of geometric realization, x lies in some simplex sigma of K. The set of simplices of K containing sigma is a nonempty finite partially ordered set under inclusion, so it has a maximal element tau. If tau were properly contained in a simplex of K, that simplex would also contain sigma, contradicting maximality in this set; hence tau is a maximal simplex of K, and x lies in tau.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let F be any finite fixed set contained in that finite polyhedron. Apply the preceding pointwise conclusion separately to each x in F: for every x in F there exists a maximal simplex tau_x of the defining complex with x in tau_x. The simplex may depend on x, which is exactly the assertion that every point of every finite fixed set lies in a maximal simplex.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

