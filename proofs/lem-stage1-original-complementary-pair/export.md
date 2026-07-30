# Proof Export

## Node 1

**Statement:** There are universal C_np<infinity and e_np>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_np and 1<dim_C calX<infinity contains nonvanishing C_np*epsilon_X-projections P' and P'' for the original product such that P'+P''=I_X and ||P'P''||,||P''P'||<=C_np*epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Dependency instantiation and constants: let C_np:=C_proj and e_np:=e_proj, where C_proj<infinity and e_proj>0 are the universal constants from the validated external lem-stage1-rectified-nontrivial-projection. Fix any finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_np and 1<dim_C calX<infinity. That external, applied with epsilon_X, supplies an element P_0 that is a nontrivial delta-projection for the original product and original unit I_X with delta=C_proj*epsilon_X=C_np*epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Complementary choice: for the P_0 supplied in node 1.1, define P_prime:=P_0 and P_doubleprime:=I_X-P_0. Since I_X is the two-sided unit for the original multiplication, direct vector-space cancellation gives P_prime+P_doubleprime=I_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Projection and nonvanishing transfer with coefficient enlargement: let C_base:=C_proj (the coefficient called C_np in node 1.1). The definition def-delta-projection supplies a universal complement-error coefficient, so there is a universal finite C_cmp>=0 for which the complement of a delta-projection in an epsilon_X-C*-algebra is a (delta+C_cmp*epsilon_X)-projection (the definition's delta+O(epsilon_X) clause). Set C_bar:=max{C_base,C_base+C_cmp}. Then the P_prime and P_doubleprime of node 1.2 are both nonvanishing C_bar*epsilon_X-projections for the original product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Complement-defect bookkeeping: node 1.1 gives P_0=P_prime as a delta-projection with delta=C_base*epsilon_X. The general-unit complement clause in def-delta-projection states that I_X-P_0=P_doubleprime is a delta_prime-projection with delta_prime=delta+O(epsilon_X). Unpacking this fixed definitional O-term, choose its universal finite coefficient C_cmp>=0, so delta_prime<=delta+C_cmp*epsilon_X=(C_base+C_cmp)*epsilon_X<=C_bar*epsilon_X. Also delta<=C_bar*epsilon_X; hence both elements are C_bar*epsilon_X-projections.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Nonvanishing bookkeeping: node 1.1 supplies P_0 as nontrivial for the original unit I_X. By def-delta-projection, nontrivial means exactly that both P_0 and I_X-P_0 satisfy the nonvanishing norm alternative. With the identifications in node 1.2 and the defect bounds of child 1.3.1, P_prime and P_doubleprime are therefore nonvanishing C_bar*epsilon_X-projections for the original product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Cross-product bounds: bilinearity of the original multiplication and the two-sided unit identities P_0 I_X=I_X P_0=P_0 give P_prime P_doubleprime=P_0(I_X-P_0)=P_0-P_0^2 and P_doubleprime P_prime=(I_X-P_0)P_0=P_0-P_0^2. Since node 1.1 gives ||P_0^2-P_0||<=delta=C_np*epsilon_X, norm symmetry under multiplication by -1 yields ||P_prime P_doubleprime||,||P_doubleprime P_prime||<=C_np*epsilon_X.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Quantified assembly with one enlargement: retain e_np:=e_proj>0 from node 1.1 and take the root coefficient C_np:=C_bar=max{C_proj,C_proj+C_cmp}<infinity from node 1.3. For every algebra in the root range, nodes 1.1-1.2 construct P_prime,P_doubleprime; node 1.3 proves both are nonvanishing C_np*epsilon_X-projections; node 1.2 gives P_prime+P_doubleprime=I_X; and node 1.4 gives each cross norm at most C_proj*epsilon_X<=C_np*epsilon_X. Universality and positivity/finiteness of the constants follow from the validated external and the fixed universal complement coefficient in def-delta-projection. Thus the witnesses establish the root contract, also at epsilon_X=0 because all bounds are non-strict.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Validated-dependency discharge: once nodes 1.1, 1.2, 1.3 (through 1.3.1-1.3.2), and 1.4 are validated, choose e_np=e_proj and choose the root's C_np to be the enlarged C_bar from node 1.3. Their conjunction gives, for every admissible algebra, witnesses P_prime,P_doubleprime that are nonvanishing C_np*epsilon_X-projections for the original product, sum exactly to I_X, and obey both cross-product bounds (the node-1.4 coefficient is no larger than C_np). Existential generalization in the witnesses and universal generalization in the arbitrary admissible algebra prove node 1.5 and hence root node 1.

**Type:** qed

**Inference:** local_discharge

**Status:** validated

**Taint:** clean

