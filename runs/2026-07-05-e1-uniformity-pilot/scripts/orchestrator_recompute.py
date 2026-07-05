# Orchestrator independent recomputation for E1b headline points, from the PRINTED matrices
# in ANSWER-B.md only (not the worker's script). Checks the WITNESS side: eta(Q), ||Q-E||,
# r^2, E stochastic idempotent. The minimality claims remain worker-certified.
from fractions import Fraction as F

def mat(rows): return [[F(x) for x in r] for r in rows]
def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]
def inf_norm(A): return max(sum(abs(x) for x in row) for row in A)
def sub(A,B): return [[a-b for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def eta(Q): return inf_norm(sub(mm(Q,Q),Q))
def check_stoch_idem(E):
    assert all(x>=0 for r in E for x in r)
    assert all(sum(r)==1 for r in E)
    assert mm(E,E)==E

# 1) Hume-positive-part anchor s=1/16
Q1 = mat([["15/256","3615/4096","241/4096"],["16/257","241/257","0"],["0","0","1"]])
E1 = mat([["15/256","241/256","0"],["15/256","241/256","0"],["0","0","1"]])
check_stoch_idem(E1)
assert all(sum(r)==1 for r in Q1) and all(x>=0 for r in Q1 for x in r)
assert eta(Q1)==F("241/32896"), eta(Q1)
d1=inf_norm(sub(Q1,E1)); assert d1==F("241/2048"), d1
assert d1*d1/eta(Q1)==F("61937/32768")

# 2) level-coupled n=6 (printed verbatim)
Q2 = mat([["1","0","0","0","0","0"],
          ["71/72","1/72","0","0","0","0"],
          ["35/36","1/72","1/72","0","0","0"],
          ["23/24","1/72","1/72","1/72","0","0"],
          ["17/18","1/72","1/72","1/72","1/72","0"],
          ["67/72","1/72","1/72","1/72","1/72","1/72"]])
E2 = [[F(1) if j==0 else F(0) for j in range(6)] for _ in range(6)]
check_stoch_idem(E2)
assert all(sum(r)==1 for r in Q2)
assert eta(Q2)==F("115/864"), eta(Q2)
d2=inf_norm(sub(Q2,E2)); assert d2==F("5/36"), d2
assert d2*d2/eta(Q2)==F("10/69")

# 3) block sum Hume s=1/5 + lazy-cycle a=1/10 (printed verbatim)
Q3 = mat([["4/25","84/125","21/125","0","0","0"],
          ["5/26","21/26","0","0","0","0"],
          ["0","0","1","0","0","0"],
          ["0","0","0","9/10","1/10","0"],
          ["0","0","0","0","9/10","1/10"],
          ["0","0","0","1/10","0","9/10"]])
E3 = mat([["4/25","21/25","0","0","0","0"],
          ["4/25","21/25","0","0","0","0"],
          ["0","0","1","0","0","0"],
          ["0","0","0","1","0","0"],
          ["0","0","0","0","1","0"],
          ["0","0","0","0","0","1"]])
check_stoch_idem(E3)
assert eta(Q3)==F("9/50"), eta(Q3)
d3=inf_norm(sub(Q3,E3)); assert d3==F("42/125"), d3
assert d3*d3/eta(Q3)==F("392/625")

print("orchestrator recompute OK: 3 headline points (anchor s=1/16, coupled n=6, block sum) from printed matrices")
