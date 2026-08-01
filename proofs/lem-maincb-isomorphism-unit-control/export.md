# Proof Export

## Node 1

**Statement:** There are universal C_iso_unit < infinity and e_iso_unit > 0 such that if B is a finite-dimensional C*-algebra, A is a finite-dimensional extended epsilon-C*-algebra, and v:B->A is an extended delta-isomorphism with 0 <= delta+epsilon <= e_iso_unit, then ||v(I_B)-I_A|| <= C_iso_unit*(delta+epsilon); the witnesses are independent of dimension, amplification, block data, and the particular source and target.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose the numerical witnesses C_iso_unit:=1 and e_iso_unit:=1; these are finite and positive universal constants.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Fix B,A,v,delta,epsilon satisfying the hypotheses. By def-extended-delta-inclusion, an extended delta-isomorphism is an extended delta-inclusion, so every amplification is a delta-inclusion; specializing to n=1 says that v itself is a delta-inclusion and hence a delta-homomorphism.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** By the unit clause in the delta-homomorphism definition incorporated by def-extended-delta-inclusion, the level-one map satisfies ||v(I_B)-I_A|| <= delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** By def-extended-epsilon-cstar-algebra at amplification n=1 and def-epsilon-cstar-algebra, the target unit obeys | ||I_A||-1 | <= epsilon; since the left side is nonnegative, epsilon >= 0, and therefore delta <= delta+epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Combining the preceding two inequalities yields ||v(I_B)-I_A|| <= delta+epsilon = C_iso_unit*(delta+epsilon); because C_iso_unit=e_iso_unit=1 were fixed numerical constants, the witnesses are independent of dimension, amplification, block data, and the particular B,A,v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

