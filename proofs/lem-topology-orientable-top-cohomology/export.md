# Proof Export

## Node 1

**Statement:** Top cohomology of a closed orientable manifold: if M is a connected compact orientable d-manifold without boundary, then H^d(M;R) != 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the hypotheses of node 1, H_d(M; R) is isomorphic to R (here R denotes the real coefficient field).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Compact without boundary is exactly 'closed' in the manifold terminology used by GT-hatcher-AT-thm-3.26; hence the root hypotheses make M a closed connected d-manifold.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Under the hypotheses of node 1, M is R-orientable for the real coefficient field R. This is proved without any change-of-coefficients assertion: GT-hatcher-AT-cor-3.39 over R supplies nonzero top cohomology, GT-hatcher-AT-field-UCT then forces H_d(M;R) to be nonzero, and GT-hatcher-AT-thm-3.26(b) rules out failure of R-orientability because {r in R : 2r=0}={0}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.1

**Statement:** Apply GT-hatcher-AT-cor-3.39 in its field-coefficient form with the field R, k=0, and the nonzero unit class 1 in H^0(M;R). Since M is closed, connected, and orientable, the corollary gives a class beta in H^d(M;R) such that 1 cup beta is a generator of H^d(M;R) (equivalently, of its one-dimensional top-degree R-space). In particular H^d(M;R) is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.2

**Statement:** By GT-hatcher-AT-field-UCT, H^d(M;R) is isomorphic to Hom_R(H_d(M;R),R). If H_d(M;R) were zero, this Hom-space would be zero, contrary to node 1.1.2.1. Hence H_d(M;R) is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.2.3

**Statement:** If M were not R-orientable, GT-hatcher-AT-thm-3.26(b) would give an injective map H_d(M;R) -> H_d(M||x;R) ≅ R whose image is {r in R : 2r=0}. Since R is the real field, this image is {0}; injectivity would force H_d(M;R)=0, contradicting node 1.1.2.2. Therefore M is R-orientable.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Applying GT-hatcher-AT-thm-3.26(a) with n=d and coefficient ring R to this closed connected R-orientable manifold gives H_d(M; R) ≅ R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** By GT-hatcher-AT-field-UCT with X=M, F=R (the real field), and n=d, H^d(M; R) is isomorphic to Hom_R(H_d(M; R), R).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** If H_d(M; R) is isomorphic to the real field R, then Hom_R(H_d(M; R), R) is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Assume an R-linear isomorphism phi: H_d(M; R) -> R, as supplied by the antecedent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** The isomorphism phi is an element of Hom_R(H_d(M; R), R) and is not the zero map, since its image is all of R and 1 in R is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Therefore Hom_R(H_d(M; R), R) contains a nonzero element and is a nonzero vector space.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** An isomorphism H^d(M; R) ≅ Hom_R(H_d(M; R), R) to a nonzero vector space implies H^d(M; R) != 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

