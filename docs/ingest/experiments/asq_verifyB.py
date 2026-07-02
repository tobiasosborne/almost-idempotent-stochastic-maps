#!/usr/bin/env python3
"""
Independent verification of the agent-B n=4 2|2 circuit dichotomy.

Agent-B claim (agentB-n4-circuit.md):
  P = I - u v^T, sum_i v_i = 0, v^T u = 1, rank-3 corank-one.
  2|2 sign pattern: v = (a,b,-c,-d), a,b,c,d>0, a+b=c+d=1.
  Then circuit:  a p_0 + b p_1 = c p_2 + d p_3   (C)
  Exposing values (satisfy C_h and lie in [0,1]):
     p_0: y=(0,1,b,b) -> e_{p0} >= b
     p_1: y=(1,0,a,a) -> e_{p1} >= a
     p_2: y=(d,d,0,1) -> e_{p2} >= d
     p_3: y=(c,c,1,0) -> e_{p3} >= c
  Collapse: b small -> dist_1(p_0, conv{p_2,p_3}) <= (b/a) D, etc.

We verify:
  (1) P=I-uv^T with the stated constraints is row-stochastic idempotent.
  (2) The affine circuit a p0+b p1 = c p2+d p3 holds (v^T P = 0).
  (3) Each exposing value vector y satisfies the circuit relation C_h
      a y0+b y1 = c y2+d y3, lies in [0,1], and is 0 at the named vertex,
      and gives the claimed lower bound = min over the OTHER rows.
  (4) The collapse bound: solve dist_1(p0, conv{p2,p3}) numerically and
      compare to (b/a) D.
"""
import sympy as sp
import numpy as np
from scipy.optimize import linprog

a,b,c,d = sp.symbols('a b c d', positive=True)
# constraint a+b=1, c+d=1 -> b=1-a, d=1-c
A,C = sp.symbols('A C', positive=True)  # free a=A, c=C in (0,1)
subst = {a:A, b:1-A, c:C, d:1-C}

print("=== (1)(2) symbolic structural check ===")
# v with 2|2 pattern; u free (4 components) with v^T u = 1.
v = sp.Matrix([a,b,-c,-d]).subs(subst)
print("sum v =", sp.simplify(sum(v)))   # should be (1)-(1)=0
u0,u1,u2,u3 = sp.symbols('u0 u1 u2 u3', real=True)
u = sp.Matrix([u0,u1,u2,u3])
# enforce v^T u = 1 by leaving u symbolic; check P 1 = 1 and P^2=P given v^T u=1, sum v=0
P = sp.eye(4) - u*v.T
ones = sp.Matrix([1,1,1,1])
P1 = sp.simplify(P*ones)
print("P*1 - 1 (uses sum v=0):", sp.simplify(P1 - ones))  # should be 0 vector
# P^2 - P = -u v^T + u (v^T u) v^T ... = u(v^T u -1) v^T
vTu = sp.simplify((v.T*u)[0])
P2mP = sp.simplify(P*P - P)
print("P^2-P factored, requires v^T u=1; P^2-P =", sp.simplify(P2mP - u*(vTu-1)*v.T))
print("so P^2=P iff v^T u = 1; vTu =", vTu)

print("\n=== (2) circuit v^T P = 0 => sum_i v_i p_i = 0 ===")
# rows p_i = P[i,:]; sum_i v_i p_i = (v^T P) as a row = should be 0
vTP = sp.simplify(v.T*P)
print("v^T P =", vTP)  # = v^T - (v^T u) v^T = (1 - v^T u) v^T = 0 when vTu=1
print("with v^T u=1 substituted: still symbolic u; v^T P = (1-vTu) v^T")

print("\n=== (3) exposing value vectors satisfy circuit C_h and bounds ===")
# C_h: a y0 + b y1 = c y2 + d y3
def check_Ch(y):
    lhs = a*y[0]+b*y[1]; rhs = c*y[2]+d*y[3]
    return sp.simplify((lhs-rhs).subs(subst))
ys = {
 'p0': [0,1,b,b],
 'p1': [1,0,a,a],
 'p2': [d,d,0,1],
 'p3': [c,c,1,0],
}
for name,y in ys.items():
    ysub=[sp.simplify(sp.S(e).subs(subst)) for e in y]
    print(name, "y=",ysub, " C_h residual=", check_Ch(y), " in[0,1]? (a,c in(0,1))")
