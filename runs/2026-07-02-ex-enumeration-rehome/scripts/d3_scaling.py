#!/usr/bin/env python3 -u
"""
d3_scaling.py -- The decisive SCALING experiment (Task 3 core).

For a FIXED structural family (a plateau/circuit shape), scale the configuration
by a parameter and track BOTH delta(scale) and the REAL tau-scaled ratio
  ratio(scale) = max_i dist1(p_i, conv W)/tau,  tau=sqrt(delta).
We build EXACT idempotents P = Lambda R with R = R_from_Lambda(Lambda) (R Lambda=I).

Counterexample signature: ratio grows (or stays >> 1) as delta -> 0.
Conjecture-consistent: ratio = O(tau) or O(delta) -> 0, or bounded by a small const.

We also do a large RANDOM multistart hunt over exact idempotents at each delta
band to find the empirical MAX ratio, to be sure we are not missing a region.
"""
import sys, json, time
import numpy as np
from d3_hunt import R_from_Lambda, eval_ratio
from d1_infra import neg_mass, ratio_stats, check_idempotent

OUT="out/d3_scaling.json"
res={"families":{}, "random_hunt":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

def family_staircase(scale, r=4, levels=3, n_extra=3, seed=0):
    rng=np.random.default_rng(seed)
    rows=[]
    for a in range(r):
        e=[0.0]*r; e[a]=1.0; rows.append(e)
    for m in range(levels):
        h=scale*2.0**(-m)
        e=[0.0]*r; e[r-1]=1+h; e[0]=-h; rows.append(e)
    for k in range(n_extra):
        e=[0.0]*r; e[r-1]=1+scale*0.5; e[k%(r-1)]=-scale*0.5; rows.append(e)
    return np.array(rows,float)

def family_circuit(scale, r=4, K=8, seed=0):
    rows=[]
    for a in range(r):
        e=[0.0]*r; e[a]=1.0; rows.append(e)
    for k in range(K):
        th=2*np.pi*k/K
        e=np.zeros(r); e[r-1]=1+scale
        e[0]=-scale*0.5*(1+np.cos(th))
        if r>2: e[1]=-scale*0.5*(1+np.sin(th))
        e-=(e.sum()-1)/r
        rows.append(list(e))
    return np.array(rows,float)

def scan_family(fam_fn, name, scales):
    rows_out=[]
    for sc in scales:
        Lam=fam_fn(sc)
        out=eval_ratio(Lam)
        if out is None:
            print(f"[{name} sc={sc}] idempotent infeasible", flush=True); continue
        rec={"scale":sc,"delta":out["delta"],"tau":out.get("tau",0.0),
             "ratio":out["ratio"],"nW":out.get("nW")}
        rows_out.append(rec)
        print(f"[{name} sc={sc:.4f}] delta={out['delta']:.3e} tau={out.get('tau',0):.3e} "
              f"ratio={out['ratio']:.4f} nW={out.get('nW')}", flush=True)
    res["families"][name]=rows_out; save()

def random_hunt(n_per_band=400, r_choices=(3,4,5,6), n_extra=(2,4,6), seed=0):
    rng=np.random.default_rng(seed)
    # bands by delta magnitude
    bands={"1e-1":[], "1e-2":[], "1e-3":[], "1e-4":[], "other":[]}
    best_overall={"ratio":-1}
    t0=time.time()
    for trial in range(n_per_band):
        r=int(rng.choice(r_choices)); ne=int(rng.choice(n_extra))
        n=r+ne
        # random signed Lambda rows summing to 1, magnitude controlled by 'amp'
        amp=10**rng.uniform(-3,0)   # spread of negativity
        L=np.zeros((n,r))
        for a in range(r): L[a,a]=1.0
        for i in range(r,n):
            v=rng.standard_normal(r)*amp
            v[rng.integers(r)] += 1.0
            v-= (v.sum()-1)/r
            L[i]=v
        out=eval_ratio(L)
        if out is None or out["delta"]<1e-9: continue
        d=out["delta"]
        rec={"delta":d,"ratio":out["ratio"],"tau":out.get("tau"),"r":r,"n":n,
             "Lambda":L.tolist()}
        if d<3e-4: bands["1e-4"].append(rec)
        elif d<3e-3: bands["1e-3"].append(rec)
        elif d<3e-2: bands["1e-2"].append(rec)
        elif d<3e-1: bands["1e-1"].append(rec)
        else: bands["other"].append(rec)
        if out["ratio"]>best_overall["ratio"]:
            best_overall={"ratio":out["ratio"],"delta":d,"r":r,"n":n,"Lambda":L.tolist()}
        if trial%100==0:
            print(f"  hunt trial {trial} best_ratio={best_overall['ratio']:.4f} "
                  f"(delta={best_overall.get('delta',0):.2e}) t={time.time()-t0:.0f}s", flush=True)
    # report max ratio per band
    summary={}
    for k,v in bands.items():
        if v:
            mr=max(v,key=lambda z:z["ratio"])
            summary[k]={"count":len(v),"max_ratio":mr["ratio"],"delta":mr["delta"]}
            print(f"  band {k}: n={len(v)} max_ratio={mr['ratio']:.4f} at delta={mr['delta']:.2e}", flush=True)
    res["random_hunt"]=summary
    res["random_best"]=best_overall
    save()
    return best_overall

if __name__=="__main__":
    print("="*70); print("d3_scaling: ratio vs delta scaling (the decisive test)"); print("="*70, flush=True)
    scales=[0.8,0.4,0.2,0.1,0.05,0.02,0.01,0.005,0.002,0.001]
    scan_family(lambda s: family_staircase(s), "staircase", scales)
    scan_family(lambda s: family_circuit(s,r=4,K=8), "circuit_r4K8", scales)
    scan_family(lambda s: family_circuit(s,r=6,K=12), "circuit_r6K12", scales)
    print("\nRANDOM HUNT over exact idempotents (max ratio per delta band):", flush=True)
    random_hunt(n_per_band=1200)
    print("d3_scaling done. saved",OUT,flush=True)
