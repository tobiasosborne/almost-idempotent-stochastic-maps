#!/usr/bin/env python3 -u
"""
d2_direct.py -- Direct construction of a signed exact idempotent realizing the
scalar plateau equations from d0-codex-vacuity-plateau.md, and the structural
diagnosis of WHY delta>0 is hard to keep while staying far from conv W.

LESSON from d2_plateau: minimizing P's delta over the archetype geometry R gives
delta=0 for ANY abstract plateau -- signed ABSTRACT coordinates do NOT force
negativity, because R can re-coordinatize 'outside' abstract points into honest
nonnegative vertices (which are then well-exposed; ratio collapses to 0).

So negativity must be FORCED by fixing the realized geometry, not chosen away.
We now build P DIRECTLY from the scalar plateau ansatz and check P^2=P exactly,
then measure delta and the ratio. We use the block picture:

  States (coordinates = rows, n total):
    - PLATEAU rows  B = {b_1..b_g} : the long-lived far group, at 'height' h.
    - an EXIT/low row  L0 (height 0).
    - a NEGATIVE-host row  Lm (height -1) that receives the negative weight.
  The codex ansatz for a bad (plateau) row i:
    p_i = (1-eps+eta) * (avg over plateau rows) + eps * e_{L0} - eta * e_{Lm}.
  with eta = eps*h/(1+h). For P^2=P EXACTLY we need consistent rows for L0,Lm and
  for the plateau's internal stochastic block to be idempotent on its own (a
  recurrent class), which forces the plateau rows to be IDENTICAL (a single
  absorbing law) OR genuinely multi-state with its own idempotent block.

  THE EXACTNESS TENSION: P^2=P on the plateau block A (rows&cols B) reads
    A^2 + U V = A,  U = B->outside,  V = outside->B.
  If plateau rows are identical (rank-1 A, = 1 mu^T), A^2 = (mu^T 1) A. For a
  signed mu with mu^T 1 = 1-eps+eta (NOT 1, because exit+neg), A^2=(1-eps+eta)A,
  so A-A^2 = (eps-eta) A, supplied by U V. U V must reproduce (eps-eta) * 1 mu^T,
  an order-(eps) rank-1 feedback INTO the plateau. That feedback comes from
  outside rows V. The codex's pressure point: V cannot come from W (well-exposed)
  rows (those send <= delta/kappa = O(tau) into far rows), so it must come from
  OTHER non-exposed rows -> a self-feeding shell.

We test the smallest closed realization and read delta and ratio, sweeping the
plateau height h ~ D*tau and delta down.
"""
import sys, json
import numpy as np
from d1_infra import check_idempotent, neg_mass, ratio_stats

OUT="out/d2_direct.json"
res={"runs":[]}
def save():
    with open(OUT,"w") as f: json.dump(res,f,indent=2,default=float)

def build_single_plateau(h, eps, g=3, seed=0, extra_low=0):
    """
    Smallest closed signed idempotent with a single absorbing plateau law.
    Coordinates / rows (n = g + 2 + extra_low):
      0..g-1   : plateau rows (group B)
      g        : exit/low row L0 (height 0)   -- absorbing? must be idempotent.
      g+1      : neg-host row Lm (height -1)
    We must define ALL rows so P^2=P EXACTLY. Strategy: make L0 and Lm ABSORBING
    (rows = e_{L0}, e_{Lm}); plateau rows convex+signed combos of {plateau avg,
    L0, Lm}. For P^2=P we need plateau-row^2 = plateau-row.
    Let m = plateau row (same for all, rank-1 block). m = (1-eps+eta)/g on each
    plateau coord + eps on L0 - eta on Lm.  Row sum = (1-eps+eta) + eps - eta = 1. ok
    P^2 row (plateau) = m P. Since L0,Lm absorbing: contributions
      from plateau mass (1-eps+eta): (1-eps+eta)*m   [each plateau row = m]
      from L0 mass eps: eps * e_{L0}
      from Lm mass -eta: -eta * e_{Lm}
    => (P^2)_plateau = (1-eps+eta) m + eps e_{L0} - eta e_{Lm}.
    For this to equal m = (1-eps+eta)*uniform_plateau + eps e_{L0} - eta e_{Lm}:
      need (1-eps+eta) m  restricted to plateau coords == (1-eps+eta)*uniform/g...
      m on plateau coords = (1-eps+eta)/g each; (1-eps+eta)*m on plateau coords
      = (1-eps+eta)^2/g each. Need == (1-eps+eta)/g => (1-eps+eta)^2=(1-eps+eta)
      => 1-eps+eta in {0,1} => eps=eta. But eta=eps*h/(1+h)<eps for h<inf. CONTRADICT.
    => a SELF-CONTAINED single absorbing plateau law is NOT idempotent unless eps=eta
       (i.e. h=infinity). THIS IS THE BINDING OBSTRUCTION (rank-1 version):
       the exit mass (eps-eta) must be RETURNED. With L0,Lm absorbing it's lost.
    Fix: route returned mass back. Make L0 feed back into plateau: L0 row not e_{L0}
    but sends mass back. But L0 must ALSO be idempotent-consistent. This is the
    'feedback' the codex flagged. We solve it exactly below in build_feedback.
    """
    raise NotImplementedError("see build_feedback")

def build_feedback(h, eps, g=1, verbose=False):
    """
    Exact rank-1 plateau WITH return feedback, smallest case g=1 (single plateau
    state b), plus L0 (height 0) and Lm (height -1). n=3.
    Unknowns: the 3x3 stochastic-ish (signed) P with P1=1, P^2=P, and a target
    'height' functional f=(f_b,f_0,f_m)=(h,0,-1) that is HARMONIC enough to make
    b a far non-exposed plateau. Let's just PARAMETRIZE all rank-1-return P with
    P^2=P and minimize delta for a given separation, exactly.
    A 3x3 idempotent of rank 2 (P^2=P, trace=2) with P1=1. Rows sum 1.
    Parametrize rank-2 idempotent: P = I - w z^T with z^T w=1, z^T 1=0 (so P1=1).
    (This is exactly the Hume rank-one COMPLEMENT: P=I-wz^T is idempotent iff
    z^T w=1; P1=1 iff z^T1=0.) rank(P)=n-1=2.
    Then neg entries come from -w z^T. We want a 'plateau' coordinate b sitting
    far from the others yet hidden. Sweep.
    """
    # We'll handle this family generally in d2_humefamily.
    raise NotImplementedError

# ---- Direct general construction: rank-(n-1) idempotent P = I - w z^T ----
# P1=1  <=> z.1=0 ; P^2=P <=> z.w=1. neg mass tunable by w,z magnitudes... but
# z.w=1 pins magnitude (the rank-one rigidity again). Let's instead allow rank n-k
# and BUILD a genuine multi-row plateau directly, solving exactness as linear
# constraints and minimizing the MAX neg mass for a PRESCRIBED far geometry that
# CANNOT be re-coordinatized away (we pin the realized rows, not the abstract).

def build_pinned(h, g=3, eps=0.2, low_neg_height=1.0, verbose=False):
    """
    Pin the REALIZED rows directly in a coordinate system that is the height/
    geometry we care about, so the optimizer cannot relocate the plateau.
    Coordinates are abstract 'feature' axes we control:
      We work in R^n with explicit rows; we DEMAND P^2=P exactly by least-squares-
      free *construction*: choose P's rows as the codex ansatz then PROJECT onto
      the exact idempotent variety is nonlinear. Instead we VERIFY a closed ansatz.

    Closed ansatz (n = g+2): plateau states 0..g-1, L0=g, Lm=g+1.
      Plateau rows i<g:  P[i] = a * U + eps * e_{L0} - eta * e_{Lm} + c * (return)
      We let L0 NOT be absorbing but RETURN to plateau to fix idempotence:
        P[L0] = beta * U + (1-beta) e_{L0}   (sends beta back to plateau uniformly)
      Lm absorbing: P[Lm]=e_{Lm}.
      U = uniform over plateau coords (1/g each).
      a = 1-eps+eta on plateau mass; eta=eps*h/(1+h).
    Solve beta and self-consistency for EXACT P^2=P.
    """
    eta = eps*h/(1+h)
    a = 1 - eps + eta
    n = g+2
    L0=g; Lm=g+1
    U=np.zeros(n); U[:g]=1.0/g
    P=np.zeros((n,n))
    for i in range(g):
        P[i]= a*U
        P[i,L0]+=eps
        P[i,Lm]-=eta
    P[Lm,Lm]=1.0
    # P[L0]= beta*U + (1-beta) e_{L0} ; choose beta to make P^2=P exact.
    # Compute P^2 - P as function of beta and solve (it's linear in beta).
    def resid(beta):
        Q=P.copy(); Q[L0]=0; Q[L0,:g]=beta/g; Q[L0,L0]=1-beta
        return (Q@Q - Q), Q
    # try to solve: residual should vanish for the right beta IF the ansatz closes.
    import numpy as _np
    betas=_np.linspace(-2,2,4001)
    best=None
    for beta in betas:
        D,Q=resid(beta)
        err=_np.abs(D).max()
        if best is None or err<best[0]: best=(err,beta,Q)
    err,beta,Q=best
    return Q, beta, err, eta, a

if __name__=="__main__":
    print("="*70); print("d2_direct: exact plateau ansatz, binding obstruction"); print("="*70, flush=True)
    print("Diagnosis (rank-1 absorbing plateau): exit mass (eps-eta) MUST be returned;")
    print("with L0,Lm absorbing it is lost => P^2=P fails unless eps=eta (h=inf).")
    print("=> exactness FORCES return feedback into the plateau. Testing closed ansatz with feedback.\n", flush=True)
    for h in [0.3,0.1,0.03]:
        for eps in [0.3,0.1]:
            Q,beta,err,eta,a=build_pinned(h=h,g=3,eps=eps)
            chk=check_idempotent(Q,tol=1e-6)
            nm,delta=neg_mass(Q)
            print(f"h={h} eps={eps}: best beta={beta:.4f} idem_resid={err:.3e} "
                  f"delta={delta:.4e} eta={eta:.4f}", flush=True)
            entry={"h":h,"eps":eps,"beta":beta,"idem_resid":float(err),
                   "delta":float(delta),"eta":eta,"a":a,"exact":bool(err<1e-9)}
            if err<1e-6:
                rs=ratio_stats(Q,label=f"direct_h{h}_eps{eps}")
                entry["max_ratio"]=rs["max_ratio"]; entry["tau"]=rs["tau"]; entry["nW"]=rs["nW"]
            res["runs"].append(entry); save()
    print("\nd2_direct done. saved", OUT, flush=True)
