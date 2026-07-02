#!/usr/bin/env python3
import sys, json
"""wave-8 closer Stage 2b verifier: rebuild the d8 wall-edge instance via d8_opt.decide_opt(0.1435, 0.5, k_groups=2, ell=0.65, v_own_site=True) saving P to /tmp/w8closer/P_edge.npy + idx json, then run this. See notes/wave8-fable-closer.md Stage 2b."""
import numpy as np
sys.path.insert(0, "/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments")
import os
os.chdir("/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments")
from scipy.optimize import linprog
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d1_infra import neg_mass

def lp(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    r = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds,
                method="highs", options={"presolve": False})
    assert r.status == 0, r.message
    return r

P = np.load('/tmp/w8closer/P_edge.npy'); idx = json.load(open('/tmp/w8closer/idx_edge.json'))
n = P.shape[0]; v = idx["v"]
nm, delta = neg_mass(P); tau = float(np.sqrt(delta)); rho, kappa = 4*tau, 0.25*tau
W, _ = well_exposed_set_robust(P, rho, kappa)
print("delta",delta,"tau",tau,"rho",rho,"kappa",kappa,"W",W,"v",v)

# canonical separator
nv = n + 1
c = np.zeros(nv); c[:n] = -P[v]; c[n] = 1.0
A_ub=[];b_ub=[]
for u in W:
    row=np.zeros(nv); row[:n]=P[u]; row[n]=-1.0; A_ub.append(row); b_ub.append(0.0)
r = lp(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=[(-1,1)]*n+[(None,None)])
w=r.x[:n]; s=r.x[n]; phi=P@w-s; H=phi[v]; g=phi[v]-phi; R=g.max()-g.min()
print("H(phi) =",H," min g =",g.min()," R =",R," ||Pg-g|| =",np.abs(P@g-g).max())

di = np.abs(P-P[v]).sum(axis=1)
far=[k for k in range(n) if k!=v and di[k]>=rho-1e-12]
nv2=n+2; c2=np.zeros(nv2); c2[-1]=-1.0
Aub=[];bub=[];kinds=[]
for k in range(n):
    hk=np.zeros(nv2); hk[:n]=P[k]; hk[n]=1.0
    Aub.append(hk.copy()); bub.append(1.0); kinds.append(("beta",k))
    Aub.append(-hk.copy()); bub.append(0.0); kinds.append(("alpha",k))
for k in far:
    hk=np.zeros(nv2); hk[:n]=-P[k]; hk[n]=-1.0; hk[-1]=1.0
    Aub.append(hk); bub.append(0.0); kinds.append(("mu",k))
Aeq=np.zeros((1,nv2)); Aeq[0,:n]=P[v]; Aeq[0,n]=1.0
r2=lp(c2,A_ub=np.array(Aub),b_ub=np.array(bub),A_eq=Aeq,b_eq=[0.0],
      bounds=[(None,None)]*(n+2))
tstar=r2.x[-1]; a_opt=r2.x[:n]; b_opt=r2.x[n]; hstar=P@a_opt+b_opt
print("t* =",tstar," t*/kappa =",tstar/kappa)
marg=np.array(r2.ineqlin.marginals)
mu={};alpha={};beta={}
for (kind,k),m in zip(kinds,marg):
    val=-m
    if val>1e-9:
        d_=dict(mu=mu,alpha=alpha,beta=beta)[kind]; d_[k]=d_.get(k,0)+val
gamma=-np.array(r2.eqlin.marginals)[0]
A_=sum(alpha.values()); B_=sum(beta.values()); MU=sum(mu.values())
print("sum mu =",MU," A =",A_," B =",B_," gamma(eq-marg) =",gamma," 1+A-B =",1+A_-B_)
vec=np.zeros(n)
for k,m in mu.items(): vec+=m*P[k]
for k,m in alpha.items(): vec+=m*P[k]
for k,m in beta.items(): vec-=m*P[k]
print("identity residual with gamma=1+A-B:", np.abs(vec-(1+A_-B_)*P[v]).max())
print("B vs t*:",B_,tstar)
alpha_far=sum(m for k,m in alpha.items() if k in far)
print("alpha on far:",alpha_far)
print("alpha rows (k,a,dist/rho,h*,g):",[(k,round(m,4),round(di[k]/rho,3),round(hstar[k],4),round(g[k],4)) for k,m in sorted(alpha.items())])
print("beta rows (k,b,h*):",[(k,round(m,4),round(hstar[k],4)) for k,m in sorted(beta.items())])
print("mu rows (k,mu,h*,g,dist/rho):",[(k,round(m,4),round(hstar[k],4),round(g[k],4),round(di[k]/rho,2)) for k,m in sorted(mu.items())])
exch_l=sum(m*g[k] for k,m in mu.items())+sum(m*g[k] for k,m in alpha.items())
exch_r=sum(m*g[k] for k,m in beta.items())
print("exchange LHS =",exch_l," =RHS",exch_r," bound B*R =",B_*R," kR =",kappa*R)
S=np.where(P[v]>1e-12)[0]; pS=P[:,S].sum(axis=1); nu_v=np.maximum(-P[v],0).sum()
print("S =",list(S)," p_v(S) =",pS[v]," 1+nu_v =",1+nu_v)
sf=sum(m*pS[k] for k,m in mu.items())
print("SF: mu.p(S) =",sf," bound =",1-A_*delta-B_*(1+2*delta))
smin=rho/(2+4*delta)-2*delta
print("FC smin =",smin," far P_kv max =",max(P[k,v] for k in far)," cap =",1-smin)
Aset=[k for k in range(n) if k!=v and P[v,k]>1e-12]; pA=P[:,Aset].sum(axis=1)
print("CPL: mu.p(A) =",sum(m*pA[k] for k,m in mu.items())," vs s_min-leak =",smin-A_*delta-kappa*(1+2*delta)-delta)
lhs_rf=sum(max(P[v,k],0)*max(P[k,v],0) for k in range(n) if k!=v)
Pvv=P[v,v]; sig=sum(max(P[v,k],0) for k in range(n) if k!=v)
print("RF:",lhs_rf," P_vv(1-P_vv) =",Pvv*(1-Pvv)," sigma_v =",sig," bound =",sig*(1-sig)-3.1*delta)
t0=rho/2-kappa*(1+2*delta)-2*delta
print("ND' t0 =",t0,"  (H-5delta)/3 =",(H-5*delta)/3)
for x in range(n):
    o=np.abs(P[x]).sum()-P[x,x]; pred=H-3*o-5*delta
    flag="  <-- VIOL" if (o<=t0 and g[x]<pred-1e-9) else ""
    print(f"   row {x}: o={o:.4f} g={g[x]:.4f} bound={pred:.4f} applies={o<=t0}{flag}")
lam={k:P[v,k]/sig for k in Aset}
theta_far=sum(lam[k] for k in Aset if di[k]>=rho-1e-12)
print("MC theta_far =",theta_far," cap delta/(sig*theta_far) =",(delta/(sig*theta_far) if theta_far>0 else float('inf'))," t* =",tstar)
print("witness classes:")
for k,m in sorted(mu.items()):
    vert,_=is_row_vertex_robust(P,k)
    print(f"   row {k}: mu={m:.4f} vertex={vert} inW={k in W} g={g[k]:.4f} o={np.abs(P[k]).sum()-P[k,k]:.4f} pS={pS[k]:.4f} pA={pA[k]:.4f} P_kv={P[k,v]:.4f} P_vk={P[v,k]:.4f}")
for E in [0.0,kappa,2*kappa,kappa*R,H/2,H]:
    dm=sum(m for k,m in mu.items() if g[k]>=H-E-1e-12)
    print(f"   deep mu-mass at E={E:.4f}: {dm:.4f}")
# d11 M (lambda-weighted coupling, P+_{jb}: carriers leaning on blockers)
Pp=np.maximum(P,0)
M=sum(m*sum(lam[j]*Pp[j,k] for j in Aset) for k,m in mu.items())
print("d11-style M =",M," M/tau =",M/tau)
