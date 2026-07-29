# Proof Export

## Node 1

**Statement:** For every finite-dimensional exact-unit epsilon_r-C*-algebra, if breve-calU = calU_e/U(1) is a compact smooth manifold without boundary, then breve-calU is homeomorphic to a finite simplicial complex and hence has finite CW type.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Antecedent instantiation (including its Stage-1 source): fix a finite-dimensional exact-unit epsilon_r-C*-algebra and write M = breve-calU = calU_e/U(1). Under the root antecedent, M is by hypothesis a compact smooth manifold without boundary. In the intended small-error range this hypothesis is also supplied as follows: if 1 < N = dim_C calX < infinity and 0 <= epsilon_r <= e_quot^r, lem-stage1-quotient-manifold-package gives exactly that M is a connected compact orientable smooth manifold without boundary (with extra conclusions not needed here); if N=1, exact unitality gives calX = C J, (zJ)^dagger = conjugate(z)J, and (zJ)·(wJ)=zwJ, hence calU=calU_e={zJ:|z|=1} and its scalar U(1)-quotient M is one point, a compact smooth 0-manifold without boundary. The proof below uses only the root antecedent that M has the stated manifold properties.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Finite triangulation: for M fixed in node 1.1, the compact-smooth-without-boundary hypothesis and the validated external lem-topology-finite-triangulation imply that there exist a finite simplicial complex K and a homeomorphism h:|K|→M. Equivalently, M is homeomorphic to a finite simplicial complex.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Finite-CW transfer and assembly: the geometric realization |K| of a finite simplicial complex K is a finite CW complex, with one open cell for the relative interior of each simplex and the usual face-attachment maps. Thus the homeomorphism h:|K|→M from node 1.2 either transports that finite CW structure to M or, more weakly, exhibits M as homotopy equivalent to the finite CW complex |K|. Hence M has finite CW type. Together with node 1.2 this proves both conclusions of the root conditional for the arbitrary algebra fixed in node 1.1.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

