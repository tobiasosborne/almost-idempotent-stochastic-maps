# Proof Export

## Node 1

**Statement:** Mass split: for an exact signed idempotent P and any row index v, writing a_j = P_{vj}, a_j^+ = max(a_j, 0), a_j^- = max(-a_j, 0), and nu_v = sum_j a_j^-, one has sum_j a_j^+ = 1 + nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** By def-signed-idempotent, P 1 = 1; therefore for the chosen row index v, sum_j P_{vj} = 1, and since a_j = P_{vj}, sum_j a_j = 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For each index j, the definitions a_j^+ = max(a_j,0) and a_j^- = max(-a_j,0) imply a_j = a_j^+ - a_j^-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** For a fixed j with a_j >= 0, max(a_j,0)=a_j and max(-a_j,0)=0, so a_j^+ - a_j^- = a_j - 0 = a_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** For a fixed j with a_j < 0, max(a_j,0)=0 and max(-a_j,0)=-a_j, so a_j^+ - a_j^- = 0 - (-a_j) = a_j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Every real number a_j satisfies exactly one of a_j >= 0 or a_j < 0; hence the identity a_j = a_j^+ - a_j^- holds for every index j.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Summing the pointwise identity from child 1.2 over the finite index set gives sum_j a_j = sum_j a_j^+ - sum_j a_j^-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** By the definition of nu_v in the root statement, nu_v = sum_j a_j^-.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Combining child 1.1 with child 1.3 and child 1.4 gives 1 = sum_j a_j^+ - nu_v; adding nu_v to both sides gives sum_j a_j^+ = 1 + nu_v.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

