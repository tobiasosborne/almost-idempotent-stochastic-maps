#!/usr/bin/env python3
"""Targeted: BELOW the corner scale (delta < (2-sqrt3)^2 = 0.0718), what is the max H/tau
   over hidden vertices WITH sigma~ > tau? (the exact dangerous-regime question).
   Also: verify best H/delta instance from exp6. Exact throughout."""
import sys, random
from fractions import Fraction as F
from pipeline import analyze, delta, is_idempotent
from gen import build_from_LambdaC

CORNER = F(2,1)  # placeholder
# delta* = (2-sqrt3)^2 = 7 - 4 sqrt3 approx 0.0718; use rational bound delta < 7/97 ~ 0.0722
DSTAR = F(7,100)  # conservative: strictly below 0.0718 use <= 0.07

def one(C, R2):
    try:
        P,_,_ = build_from_LambdaC(C,R2)
    except Exception:
        return None
    if not is_idempotent(P)[0]:
        return None
    d,negs = delta(P)
    if d==0 or d > DSTAR:   # BELOW corner scale only
        return None
    res = analyze(P,verbose=False)
    if "note" in res or not res["hidden"]:
        return None
    out=[]
    tau=float(d)**0.5
    for v in res["hidden"]:
        s=res["sigma_tilde"][v]; dv=res["dists"][v]
        if dv==0: continue
        out.append(dict(d=d,v=v,so=float(s)/tau,Ht=float(dv)/tau,Hd=float(dv)/float(d),
                        sig_gt_tau=(s*s>d), H_gt_Btau=(dv*dv>F(536,1000)**2*d),
                        C=C,R2=R2))
    return out

random.seed(99)
DEN=[2,3,4,6,8,10,16,20,40,80]
def rq(a,b):
    dd=random.choice(DEN); return F(random.randint(a*dd,b*dd),dd)
best_joint=None; best_sig=None; n_sig_gt=0; n_kept=0
for it in range(9000):
    k=random.choice([2,3,3,4])
    m=random.choice([1,2,2,3])
    C=[]
    for _ in range(m):
        home=random.randrange(k); row=[F(0)]*k
        for t in range(k):
            if t!=home and random.random()<0.6:
                row[t]=rq(-1,1)*F(1,random.choice([2,3,4,8]))
        row[home]=F(1)-sum(row)
        C.append(row)
    R2=[[rq(-1,1)*F(1,random.choice([4,8,20,50])) for _ in range(m)] for _ in range(k)]
    r=one(C,R2)
    if not r: continue
    n_kept+=1
    for rec in r:
        if rec["sig_gt_tau"]:
            n_sig_gt+=1
            if best_joint is None or rec["Ht"]>best_joint["Ht"]:
                best_joint=rec
        if best_sig is None or rec["so"]>best_sig["so"]:
            best_sig=rec
print(f"BELOW corner (delta<={float(DSTAR)}): kept={n_kept} hidden-verts-with-sig>tau={n_sig_gt}")
def show(t,r):
    if r is None: print(f"  {t}: NONE"); return
    print(f"  {t}: delta={float(r['d']):.5f} H/tau={r['Ht']:.4f} sig/tau={r['so']:.4f} "
          f"H/delta={r['Hd']:.4f} sig>tau={r['sig_gt_tau']} H>Btau={r['H_gt_Btau']}")
show("max H/tau WITH sig>tau (below corner)", best_joint)
show("max sig/tau (below corner)", best_sig)

print("\n--- verify exp6 seed5 best H/delta instance ---")
C=[[F(1,2),F(337,600),F(-7,150),F(-3,200)]]
R2=[[F(1,200)],[F(29,600)],[F(-29,800)],[F(0)]]
P,_,_=build_from_LambdaC(C,R2)
print("  idempotent:",is_idempotent(P)[0])
d,negs=delta(P); res=analyze(P,verbose=False)
v=max(res["hidden"],key=lambda i:res["dists"][i]) if res["hidden"] else None
if v is not None:
    dv=res["dists"][v]
    print(f"  delta={d}={float(d):.5f} H={dv}={float(dv):.5f} H/delta={dv/d}={float(dv/d):.4f} "
          f"H/tau={float(dv)/float(d)**0.5:.4f} hidden={res['hidden']} W={res['W']}")
