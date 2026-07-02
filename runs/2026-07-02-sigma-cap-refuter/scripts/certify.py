#!/usr/bin/env python3
"""certify.py -- EXACT (Fraction) certification of a (C,R2) candidate.
   Prints all exact invariants + per-recipient breakdown of sigma~ with each
   recipient's exact dist/tau, to decide whether recipients are >= c*tau outside
   (genuine kill) or only epsilon-halo (dist << tau; cap survives morally).
   Usage: edit C,R2 below or import certify()."""
from fractions import Fraction as F
from gen import build_from_LambdaC
from pipeline import (analyze, is_idempotent, delta, l1, exposed_tstar,
                      is_row_vertex, visible_set, dist1_to_conv, matmul)

def certify(C, R2, label=""):
    P,_,_ = build_from_LambdaC(C, R2)
    n=len(P)
    ok,idem,rs = is_idempotent(P)
    d,negs = delta(P)
    print(f"=== {label} ===")
    print(f"  n={n}  P^2=P exact={idem}  P1=1 exact={rs}  delta={d}={float(d):.6f}  attained rows {[i for i in range(n) if negs[i]==d]}")
    if not ok or d==0: print("  ABORT"); return None
    tau2=float(d)**0.5
    W,info=visible_set(P,d)
    print(f"  W (exposed)={W}")
    dists=[dist1_to_conv(P,W,i)[0] for i in range(n)]
    H=max(dd for dd in dists if dd is not None)
    argmaxH=max(range(n),key=lambda i:(dists[i] if dists[i] is not None else F(-1)))
    outside=[j for j in range(n) if dists[j] is not None and dists[j]>0]
    hidden=[i for i in range(n) if info.get(i,{}).get("vertex") and not info.get(i,{}).get("exposed")]
    tops=[v for v in hidden if dists[v] is not None and dists[v]>0]
    print(f"  hidden={hidden}  hidden TOP (dist>0)={tops}  argmaxH={argmaxH}  H={H}={float(H):.6f}  H/tau={float(H)/tau2:.4f}")
    print(f"  outside rows (dist>0): {[(j, str(dists[j]), f'{float(dists[j])/tau2:.4f}tau') for j in outside]}")
    for v in tops:
        s=sum(max(P[v][j],F(0)) for j in outside)
        print(f"\n  --- hidden TOP vertex v={v}: t*={info[v].get('tstar')}, dist_v={dists[v]}={float(dists[v]):.6f} (={float(dists[v])/tau2:.4f} tau) ---")
        print(f"      sigma~_v = {s} = {float(s):.6f}   sigma~/tau={float(s)/tau2:.4f}   1-sigma~={float(F(1)-s):.6f}  (1-s)/tau={float(F(1)-s)/tau2:.4f}")
        print(f"      nu_v(neg mass)={negs[v]}={float(negs[v]):.6f}  nu/tau={float(negs[v])/tau2:.4f}")
        # collapse-bound check: H(1-sigt) <= nu(2+4d)
        lhs=H*(F(1)-s); rhs=negs[v]*(2+4*d)
        print(f"      collapse bound H(1-sigt)={float(lhs):.6f} <= nu(2+4d)={float(rhs):.6f} : {lhs<=rhs}")
        print(f"      per-recipient positive mass of v on OUTSIDE rows (recipient dist/tau):")
        for j in outside:
            if P[v][j]>0:
                print(f"         col {j}: P_vj={P[v][j]}={float(P[v][j]):.5f}  recipient dist={float(dists[j]):.6f}={float(dists[j])/tau2:.4f} tau")
        # halo-robust sigma at thresholds eps = c*tau
        for c in [F(1,4), F(1,2), F(1,1)]:
            eps=c*F(int(tau2*10**6),10**6)  # approx c*tau as rational for threshold
            # exact threshold: dist^2 vs (c^2 * delta) since eps=c*tau => eps^2=c^2 delta
            s_eps=sum(max(P[v][j],F(0)) for j in outside if dists[j]*dists[j] >= c*c*d)
            print(f"      sigma~ restricted to recipients at dist >= {float(c)}*tau : {float(s_eps):.6f}  (sigma_eps/tau={float(s_eps)/tau2:.4f})")
    # clone-invariance sanity
    from pipeline import clone_row
    Pc=clone_row(P,0,[F(1,2),F(1,2)])
    okc,_,_=is_idempotent(Pc); dc,_=delta(Pc)
    print(f"\n  clone-invariance (split row0 x2): idempotent={okc} delta_inv={dc==d}")
    return dict(P=P,delta=d,H=H,W=W,hidden=hidden,tops=tops,dists=dists)

if __name__=="__main__":
    # the sigma~>1 candidate from search4f oneminus seed5 BEST
    C=[[F('28/25'),F('1/200'),F(0),F('-1/8')]]
    R2=[[F('-49/800')],[F('-1/6')],[F('-1/8')],[F('-33/800')]]
    certify(C,R2,"sigma~>1 candidate (d~0.197, single hidden row)")
