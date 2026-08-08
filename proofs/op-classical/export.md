# Proof Export

## Node 1

**Statement:** Classical projection stability: there are universal eta_0,C>0 (n-free) such that every row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta_0 admits a stochastic idempotent E with ||Q-E||_{inf->inf} <= C sqrt(eta) (the commutative case of op-npps).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** External invocation: lem-routef-f0-assembly supplies universal eta_0,C>0 independent of n such that for every n>=1, every row-stochastic Q:l_inf^n->l_inf^n, and every 0<=eta<=eta_0 with ||Q^2-Q||_{infinity->infinity}<=eta, the same Q admits a stochastic idempotent E satisfying ||Q-E||_{infinity->infinity}<=C*sqrt(eta).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Vocabulary match: by def-stochastic and def-almost-idempotent, a row-stochastic matrix Q is the same object as the row-stochastic map Q:l_inf^n->l_inf^n used in lem-routef-f0-assembly, a stochastic idempotent means row-stochastic E with E^2=E, and ||.||_{inf->inf} is the same induced operator norm denoted ||.||_{infinity->infinity}; independent of n is exactly n-free. Hence the external conclusion has precisely the hypotheses and conclusion of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By def-stochastic and def-almost-idempotent, a row-stochastic matrix Q is equivalently the row-stochastic map Q:l_inf^n->l_inf^n used by lem-routef-f0-assembly, a stochastic idempotent is row-stochastic E with E^2=E, and the inf->inf and infinity->infinity symbols denote the same induced operator norm; independent of n means n-free.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** By def-near-positive-projection, near-positive-projection stability has as its commutative stochastic specialization exactly approximation by a stochastic idempotent with a square-root bound, so the parenthetical phrase the commutative case of op-npps is descriptive and adds no further hypothesis or conclusion to node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

