# Proof Export

## Node 1

**Statement:** Zero-sum triangle bound: let w and v be vectors in R^d with v having coordinate sum zero (sum_l v(l) = 0); write n(x) = sum_l max(-x(l), 0); then n(w - v) <= n(w) + n(v).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** For every coordinate l, max(-(w(l)-v(l)),0) <= max(-w(l),0) + max(v(l),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** For any real numbers a and b, max(a+b,0) <= max(a,0) + max(b,0). Indeed, max(a,0)+max(b,0) is nonnegative and is at least a+b, so it bounds the maximum of a+b and 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** For a fixed coordinate l, take a=-w(l) and b=v(l); since -(w(l)-v(l)) = -w(l)+v(l), the previous real inequality gives max(-(w(l)-v(l)),0) <= max(-w(l),0)+max(v(l),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Summing the coordinate inequalities over l gives n(w-v) <= n(w) + sum_l max(v(l),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Because sum_l v(l)=0, sum_l max(v(l),0) = n(v).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** For each coordinate l, v(l) = max(v(l),0) - max(-v(l),0), by the two cases v(l) >= 0 and v(l) < 0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Summing the preceding coordinate identity gives sum_l v(l) = sum_l max(v(l),0) - sum_l max(-v(l),0).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Since sum_l v(l)=0 and n(v)=sum_l max(-v(l),0), the equality sum_l max(v(l),0)=n(v) follows.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Combining the preceding two conclusions gives n(w-v) <= n(w) + n(v).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

