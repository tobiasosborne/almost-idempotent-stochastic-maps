#!/usr/bin/env python3
"""HARD independent verification of the H/delta=2.041 candidate instance.
   - P^2=P exact, rowsum exact, delta exact.
   - W membership: for each row, independently certify vertex + exposedness/hiddenness.
   - H = dist(p3, conv{p0,p1,p2}): certify by PRIMAL (explicit convex combo, upper bnd)
     and DUAL (1-Lipschitz affine functional, lower bnd). If they match -> H certified.
   No trust in analyze() for the load-bearing numbers; recompute from scratch."""
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import matmul, l1, delta, is_idempotent, exposed_tstar, is_row_vertex, dist1_to_conv
from exact_lp import linprog_exact

p = F(1,40); rho = F(1,100); x = p/3
C = [[F(1,2)-x, F(1,2)+x+p, -p], [F(1,2)+x, F(1,2)-x+p, -p]]
R2 = [[rho,rho],[rho,rho],[rho,rho]]
P, R, _ = build_from_LambdaC(C, R2)
n = len(P)

print("1) P^2=P exact, P1=1 exact:", is_idempotent(P))
d, negs = delta(P)
print("   delta =", d, "attained rows", [i for i in range(n) if negs[i]==d])

print("\n2) vertex + exposedness for each row (tau=sqrt(delta), rho=4tau, kappa=tau/4):")
for i in range(n):
    vert, verr = is_row_vertex(P, i)
    ts = exposed_tstar(P, i, d)
    if ts is None:
        cls = "EXPOSED(vacuous: no far rows)"
    else:
        exp = (ts >= 0) and (16*ts*ts >= d)   # t* >= kappa <=> 16 t*^2 >= delta
        cls = f"t*={ts}(={float(ts):.5f}) 16t*^2={16*ts*ts} vs delta={d} -> {'EXPOSED' if exp else 'HIDDEN'}"
    print(f"   row {i}: vertex={vert}  {cls}")

# far-set sanity for row 3: which rows are >= rho away? rho^2 = 16 delta
print("\n   far rows (||.||_1^2 >= 16 delta) from row 3:")
for j in range(n):
    if j==3: continue
    dd = l1(P[3],P[j])
    print(f"     row {j}: ||p3-pj||_1={dd}={float(dd):.4f}  far={dd*dd >= 16*d}")

print("\n3) H = dist_1(p3, conv{p0,p1,p2}) -- primal & dual certificates:")
W = [0,1,2]; v = 3
# PRIMAL: solve exact LP, get lambdas, build the point, compute exact l1 distance
dv, lam = dist1_to_conv(P, W, v)
print("   LP optimum (dist) =", dv, "=", float(dv))
pt = [sum(lam[t]*P[W[t]][j] for t in range(len(W))) for j in range(n)]
prim = l1(P[v], pt)
print("   lambdas =", [str(l) for l in lam], " sum=", sum(lam))
print("   PRIMAL upper bound ||p3 - sum lam*p_w||_1 =", prim, "=", float(prim))
print("   lambdas all >=0:", all(l>=0 for l in lam))

# DUAL: find phi(x)=a.x+b, ||a||_inf<=1, phi<=0 on p0,p1,p2, maximize phi(p3).
# = dist_1(p3, conv W) by l1/linf duality. Solve exact LP for the dual value + get a,b.
nv = n + 1  # a(n), b
c = [F(0)]*n + [F(0)]  # maximize a.p3+b => min -(a.p3+b)
c = [-P[v][j] for j in range(n)] + [F(-1)]
A_ub = []; b_ub = []
for w in W:
    row = [P[w][j] for j in range(n)] + [F(1)]   # a.pw + b <= 0
    A_ub.append(row); b_ub.append(F(0))
bounds = [(F(-1),F(1))]*n + [(None,None)]  # ||a||_inf<=1, b free
r = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
dualval = -r["fun"]
a = r["x"][:n]; b = r["x"][n]
print("   DUAL value max phi(p3) =", dualval, "=", float(dualval))
print("   ||a||_inf =", max(abs(ai) for ai in a), " phi(p_w) for w in W:", [str(sum(a[j]*P[w][j] for j in range(n))+b) for w in W])
print("   PRIMAL==DUAL==LP:", prim==dualval==dv, " => H certified =", dv)
print(f"\n   nu_v(row3) = {negs[v]}  H = {dv}  H/nu_v = {dv/negs[v]} = {float(dv/negs[v]):.6f}")
print(f"   H/delta = {dv/d} = {float(dv/d):.6f}")
tau2=float(d)**0.5
print(f"   H/tau = {float(dv)/tau2:.6f}  (B*tau with B=0.536 => H>Btau? {dv*dv > F(536,1000)**2*d})")
