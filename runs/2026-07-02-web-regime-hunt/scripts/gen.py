#!/usr/bin/env python3
"""
gen.py -- exact generators of exact signed idempotents P (P^2=P, P1=1), via the
factorization P=Lambda R with R Lambda = I_k (guarantees idempotence + row sums).

R-first / C-solve builder (n = 2k):
  - R (k x 2k): archetype rows, each summing to 1.  Columns split R=[R1|R2],
    R1,R2 are k x k; R2 must be invertible.
  - C = R2^{-1} (I_k - R1)  (the (n-k) hidden-row barycentric coords; rows sum to 1 auto).
  - P rows: r_1..r_k (archetypes = visible candidates), then p_{k+i}=sum_s C[i,s] r_s.
This lets us place archetypes near distinct corners while pushing hidden rows out by
negative C-coordinates -- the 'dilution' handle: coordinate-negativity (drives H) vs
entry-negativity (drives delta).

All arithmetic exact (Fraction).  matrix inverse via exact Gaussian elimination.
"""
from fractions import Fraction as F
from pipeline import matmul, as_F, analyze


def mat_inv(A):
    """Exact inverse of square Fraction matrix via Gauss-Jordan. Returns None if singular."""
    n = len(A)
    M = [[F(A[i][j]) for j in range(n)] + [F(1) if j == i else F(0) for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = None
        for r in range(col, n):
            if M[r][col] != 0:
                piv = r; break
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [[M[i][j + n] for j in range(n)] for i in range(n)]


def build_from_R(R):
    """R: k x (2k) exact, rows sum to 1.  Returns P (2k x 2k) exact or None if R2 singular."""
    k = len(R)
    n = 2 * k
    R = as_F(R)
    R1 = [[R[s][t] for t in range(k)] for s in range(k)]
    R2 = [[R[s][k + t] for t in range(k)] for s in range(k)]
    R2inv = mat_inv(R2)
    if R2inv is None:
        return None
    # C = R2inv (I - R1)
    ImR1 = [[(F(1) if s == t else F(0)) - R1[s][t] for t in range(k)] for s in range(k)]
    C = matmul(R2inv, ImR1)   # k x k ; C[i][s] = coord of hidden row i on archetype s
    # rows of P
    P = [R[s][:] for s in range(k)]
    for i in range(k):
        row = [sum(C[i][s] * R[s][j] for s in range(k)) for j in range(n)]
        P.append(row)
    return P, C


def build_from_LambdaC(C, R2):
    """FULLY GENERAL exact builder. Guarantees P^2=P, P1=1.
       C  : (n-k) x k  hidden-row barycentric coords (rows sum to 1; may be signed).
       R2 : k x (n-k)  archetype values on the 'tail' coords (free dilution knob).
       Sets R1 = I_k - R2 C, R = [R1|R2], Lambda = [I_k ; C], P = Lambda R.
       Rows 1..k of P are the archetypes r_s; rows k+1..n are sum_s C[i,s] r_s.
       n = k + (n-k) = k + len(C).  Requires each row of C to sum to 1."""
    C = as_F(C); R2 = as_F(R2)
    m = len(C)              # n-k hidden rows
    k = len(C[0])           # rank
    assert len(R2) == k and len(R2[0]) == m, "R2 must be k x (n-k)"
    for i in range(m):
        assert sum(C[i]) == 1, f"C row {i} does not sum to 1"
    R2C = matmul(R2, C)     # k x k
    R1 = [[(F(1) if s == t else F(0)) - R2C[s][t] for t in range(k)] for s in range(k)]
    R = [R1[s] + R2[s] for s in range(k)]     # k x (k + m) = k x n
    n = k + m
    # P rows
    P = [R[s][:] for s in range(k)]
    for i in range(m):
        row = [sum(C[i][s] * R[s][j] for s in range(k)) for j in range(n)]
        P.append(row)
    return P, R, C


def build_from_R_general(R, C):
    """More general: choose archetypes R (k x n, rows sum 1) AND hidden coords C
       ((n-k) x k, rows sum 1) freely, provided R1 + R2 C = I_k where R=[R1|R2] with
       R1=R[:,:k], R2=R[:,k:] is k x (n-k), C is (n-k) x k.  Verifies the constraint
       exactly; returns (P, ok)."""
    R = as_F(R); C = as_F(C)
    k = len(R); n = len(R[0])
    R1 = [[R[s][t] for t in range(k)] for s in range(k)]
    R2 = [[R[s][k + t] for t in range(n - k)] for s in range(k)]
    RC = matmul(R2, C)  # k x k
    ok = all(R1[s][t] + RC[s][t] == (F(1) if s == t else F(0)) for s in range(k) for t in range(k))
    P = [R[s][:] for s in range(k)]
    for i in range(n - k):
        row = [sum(C[i][s] * R[s][j] for s in range(k)) for j in range(n)]
        P.append(row)
    return P, ok
