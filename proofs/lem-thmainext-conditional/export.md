# Proof Export

## Node 1

**Statement:** Extended th_main_ext assembly: there are universal C_E < infinity and epsilon_E > 0 such that every finite-dimensional extended epsilon-C*-algebra A, for 0 <= epsilon <= epsilon_E, is carried by one extended C_E*epsilon-isomorphism v:B->A from a finite-dimensional C*-algebra, with constants independent of dimension, amplification level, and block data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Invoke lem-maincb-structural-assembly and fix its universal MAIN-CB witness-ledger datum W. Define C_E := W.c0_cb*W.K_call and epsilon_E := W.epsilon_MAIN. The final clause of lem-maincb-structural-assembly states that these two quantities are finite positive universal witnesses; therefore C_E < infinity and epsilon_E > 0, with neither depending on dimension, amplification level, block count, or block dimensions.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Let A be an arbitrary finite-dimensional extended epsilon-C*-algebra and let 0 <= epsilon <= epsilon_E. Using epsilon_E = W.epsilon_MAIN from node 1.1, lem-maincb-structural-assembly supplies a finite-dimensional C*-algebra B = direct_sum_C M_{|C|} and one extended W.c0_cb*W.K_call*epsilon-isomorphism v:B->A (indeed also satisfying its unused unit estimate). Substituting C_E = W.c0_cb*W.K_call, this is one extended C_E*epsilon-isomorphism v:B->A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** By the registered definition def-extended-delta-inclusion, an extended C_E*epsilon-isomorphism is a single bijective linear map v whose every amplification 1_{M_n} tensor v is a C_E*epsilon-inclusion. Thus the map in node 1.2 carries A at all amplification levels with the same constant; node 1.1 makes that constant and epsilon_E universal and independent of all dimension and block data. Since A and epsilon in node 1.2 were arbitrary, the asserted universal conclusion follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

