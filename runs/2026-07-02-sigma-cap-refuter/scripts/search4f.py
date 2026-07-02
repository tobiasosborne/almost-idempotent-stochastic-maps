#!/usr/bin/env python3
"""search4f: FAST float hill-climb (fastpipe) mapping the JOINT frontier of a
   HIDDEN TOP vertex (delta, sigt/tau, H/tau, (1-sigt)/tau).  Winners must be
   re-certified EXACTLY.  obj in {St, Ht, joint, oneminus}.
   Usage: python3 search4f.py OBJ SEED ITERS"""
import sys, random, os
import numpy as np
KCH=[int(x) for x in os.environ.get("KCH","2,3,3,4,4,5").split(",")]
MCH=[int(x) for x in os.environ.get("MCH","1,2,2,3,3,4").split(",")]
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import is_idempotent, delta as delta_exact
import fastpipe as fp

OBJ  = sys.argv[1] if len(sys.argv)>1 else "St"
seed = int(sys.argv[2]) if len(sys.argv)>2 else 0
ITERS= int(sys.argv[3]) if len(sys.argv)>3 else 3000
random.seed(seed)

def evalP(C,R2):
    try:
        P,_,_ = build_from_LambdaC(C,R2)
    except Exception:
        return None
    d,_ = delta_exact(P)
    if d==0 or d>F(1,4): return None
    Pf=[[float(x) for x in row] for row in P]
    res=fp.analyze_f(Pf)
    if res is None or not res["hidden"]: return None
    tops=[v for v in res["hidden"] if res["dists"][v]>1e-8]
    if not tops: return None
    tau=float(d)**0.5
    if OBJ=="Sg":
        v=max(tops,key=lambda i:res["sigt_g"][i])
    else:
        v=max(tops,key=lambda i:res["sigt"][i])
    s=res["sigt"][v]; sg=res["sigt_g"][v]; dv=res["dists"][v]
    return dict(delta=float(d),v=v,H=res["H"],distv=dv,sigt=s,sigt_g=sg,tau=tau,
               Ht=dv/tau,St=s/tau,Sg=sg/tau,oneminus=(1.0-s)/tau,onemg=(1.0-sg)/tau,
               sig_gt_tau=(s>tau),H_gt_Btau=(dv>0.536*tau),
               C=C,R2=R2,nW=len(res["W"]),dexact=d)

def score(r):
    if OBJ=="Ht": return r["Ht"]
    if OBJ=="St": return r["St"]
    if OBJ=="Sg": return r["Sg"]          # genuine-recipient invisible mass (dist>=tau/4)
    if OBJ=="oneminus": return -r["oneminus"]
    if OBJ=="joint": return r["St"]+min(r["Ht"],1.5)
    return r["St"]

DEN=[2,3,4,6,8,12,20,40,60,100]
def rq(a,b):
    dd=random.choice(DEN); return F(random.randint(int(a*dd),int(b*dd)),dd)

def rand_start():
    k=random.choice(KCH); m=random.choice(MCH)
    base=[F(0)]*k; home=random.randrange(k)
    for t in range(k):
        if t!=home: base[t]=random.choice([F(0),rq(-1,1)*F(1,random.choice([1,2,4,8]))])
    base[home]=F(1)-sum(base)
    C=[]
    for i in range(m):
        row=base[:]
        if k>=2:
            a,b=random.sample(range(k),2)
            e=F(random.choice([-1,1])*(i+1),random.choice([10,20,40,100,200]))
            row[a]+=e; row[b]-=e
        C.append(row)
    R2=[[rq(-1,1)*F(1,random.choice([2,4,8,20,50,100])) for _ in range(m)] for _ in range(k)]
    return C,R2

def perturb(C,R2,step):
    C=[r[:] for r in C]; R2=[r[:] for r in R2]
    if random.random()<0.5 and C:
        i=random.randrange(len(C)); j=random.randrange(len(C[0]))
        home=max(range(len(C[0])),key=lambda t:C[i][t])
        if j==home: return C,R2
        dd=F(random.choice([-1,1]),step); C[i][j]+=dd; C[i][home]-=dd
    else:
        i=random.randrange(len(R2)); j=random.randrange(len(R2[0]))
        R2[i][j]+=F(random.choice([-1,1]),step)
    return C,R2

pareto=[]
def offer(r):
    global pareto
    for q in pareto:
        if q["St"]>=r["St"]-1e-9 and q["Ht"]>=r["Ht"]-1e-9 and q["delta"]<=r["delta"]+1e-12:
            return
    pareto=[q for q in pareto if not (r["St"]>=q["St"]-1e-9 and r["Ht"]>=q["Ht"]-1e-9 and r["delta"]<=q["delta"]+1e-12)]
    pareto.append(r)

best=None
for it in range(ITERS):
    C,R2=rand_start(); cur=evalP(C,R2)
    if cur is None: continue
    offer(cur)
    for _ in range(30):
        nxt=evalP(*perturb(cur["C"],cur["R2"],random.choice([2,4,8,16,40,100,200])))
        if nxt and score(nxt)>score(cur): cur=nxt; offer(cur)
    if best is None or score(cur)>score(best): best=cur

print(f"OBJ={OBJ} seed={seed} iters={ITERS}: pareto {len(pareto)}")
if best:
    r=best
    print(f"BEST: d={r['delta']:.5f} St={r['St']:.4f} Ht={r['Ht']:.4f} "
          f"(1-s)/t={r['oneminus']:.4f} s>t={r['sig_gt_tau']} H>Bt={r['H_gt_Btau']} nW={r['nW']}")
    print(f"  C={[[str(x) for x in row] for row in r['C']]}")
    print(f"  R2={[[str(x) for x in row] for row in r['R2']]}")
pareto.sort(key=lambda r:-r["St"])
print(f"\n{'delta':>9} {'sigt/tau':>9} {'sigt_g/tau':>10} {'H/tau':>7} {'(1-s)/tau':>10} {'s>t':>4} {'H>Bt':>5} {'nW':>3}")
for r in pareto[:20]:
    print(f"{r['delta']:9.5f} {r['St']:9.4f} {r['Sg']:10.4f} {r['Ht']:7.4f} {r['oneminus']:10.4f} "
          f"{str(r['sig_gt_tau']):>4} {str(r['H_gt_Btau']):>5} {r['nW']:3d}")
# best genuine-recipient invisible mass (the halo-robust cap target)
bg=max(pareto,key=lambda r:r["Sg"])
print(f"\nMAX genuine sigt_g/tau (recipients dist>=tau/4): d={bg['delta']:.5f} sigt_g/tau={bg['Sg']:.4f} "
      f"sigt/tau={bg['St']:.4f} H/tau={bg['Ht']:.4f} (1-sigt_g)/tau={bg['onemg']:.4f}")
print(f"  C={[[str(x) for x in row] for row in bg['C']]}")
print(f"  R2={[[str(x) for x in row] for row in bg['R2']]}")
jt=[r for r in pareto if r["sig_gt_tau"]]
if jt:
    jt.sort(key=lambda r:-r["Ht"]); r=jt[0]
    print(f"\nBEST JOINT (s>t,maxH): d={r['delta']:.5f} St={r['St']:.4f} Ht={r['Ht']:.4f} (1-s)/t={r['oneminus']:.4f}")
    print(f"  C={[[str(x) for x in row] for row in r['C']]}")
    print(f"  R2={[[str(x) for x in row] for row in r['R2']]}")
