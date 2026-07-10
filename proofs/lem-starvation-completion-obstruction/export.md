# Proof Export

## Node 1

**Statement:** Bounded-slab starvation completion obstruction (K-free): for every finite I, every real A in [4,6], every real tau in (0,1/256], and t := tau^2, a := tau/(1+tau), there is no rank-three exact signed idempotent P (P^2 = P, P*1 = 1, rank P = 3) with row negative mass nu_i <= t for every i in I having five distinct full row-point fibers represented by v,w,f,z,o such that, with D := p_z - p_v and E := p_o - p_v linearly independent, ||D||_1 = tau, p_f - p_v = -A*D + t*E, p_w - p_v = a*(p_f - p_v), top-row fiber masses c_v = 1 - tau, c_w = tau + t, c_f = -t, and c_Q = 0 for every other full row-point fiber Q, every full row-point fiber Q has unique reals x_Q, y_Q with p_Q = p_v + x_Q*D + y_Q*E, and every nonactor support fiber Q satisfies either p_Q in conv{p_v,p_w,p_f,p_z,p_o} or 0 <= y_Q <= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Proof by contradiction with explicit fiber notation. Fix arbitrary finite I, A, tau, t, a and a putative matrix P satisfying every hypothesis of node 1. For each full row-point fiber Q (an equivalence class for i~j iff p_i=p_j), let p_Q be its common row and define c_Q:=sum_{j in Q} P_{vj}, d_Q:=sum_{j in Q}(P_{zj}-P_{vj}), and e_Q:=sum_{j in Q}(P_{oj}-P_{vj}); thus the contract's top-row mass is c_Q. Call Q a support fiber exactly when (c_Q,d_Q,e_Q)!=(0,0,0), and call the five fibers of v,w,f,z,o actors. Put P_i(S):=sum_{j in S}P_{ij}, x_j:=x_[j], y_j:=y_[j], H:=conv{p_v,p_w,p_f,p_z,p_o}, and Ext:={Q: Q is a support fiber and p_Q is not in H}. The child calculations derive the exact identity sum_Q x_Q d_Q=1 but an absolute upper bound strictly below 1 for the same sum. This contradiction discharges the arbitrary supposition and proves node 1.

**Type:** claim

**Inference:** contradiction

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Signed-row subset ledger. For every row i and every subset S of I, -t <= P_i(S) <= 1+t and ||p_i||_1 <= 1+2t. Indeed, set P_{ij}^+:=max(P_{ij},0) and P_{ij}^-:=max(-P_{ij},0). The registered exact-signed-idempotent definition gives sum_j P_{ij}=1, while the registered negative-mass definition and the root hypothesis give sum_j P_{ij}^-=nu_i<=t. Hence sum_j P_{ij}^+=1+nu_i. Therefore -nu_i <= -sum_{j in S}P_{ij}^- <= P_i(S) <= sum_{j in S}P_{ij}^+ <= 1+nu_i, proving the subset bounds; also ||p_i||_1=sum_j(P_{ij}^++P_{ij}^-)=1+2nu_i<=1+2t.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Idempotence gives the exact unit reproduction moment, and the actor hull has bounded x-coordinate. Since P^2=P, subtracting the v-row identity p_v P=p_v from the z-row identity p_z P=p_z yields D P=D. Since both p_z and p_v have row sum one, sum_j D_j=0. For each j, the root's unique fiber coordinates give p_j=p_v+x_j D+y_j E. Thus D=sum_j D_j p_j=(sum_j D_j)p_v+(sum_j x_jD_j)D+(sum_j y_jD_j)E. Linear independence of D,E forces sum_j x_jD_j=1. Grouping the finite sum by full fibers and using d_Q=sum_{j in Q}D_j gives sum_Q x_Q d_Q=1. The actor relations give (x_v,y_v)=(0,0), (x_z,y_z)=(1,0), (x_o,y_o)=(0,1), (x_f,y_f)=(-A,t), and (x_w,y_w)=(-Aa,ta). Because 0<a<1 and A>=4, every convex combination in H has x-coordinate in [-A,1], hence |x_Q|<=A whenever p_Q is in H.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** Canonical-slab exterior lever bound. For every Q in Ext, |x_Q| tau <= 2+4t. Indeed, Q cannot be an actor because each actor row point is a generator of H. Hence Q is a nonactor support fiber outside H, so the root's disjunction forces 0<=y_Q<=1. Writing X:=x_Q and Y:=y_Q, the coordinate identities p_Q=p_v+XD+YE and p_o=p_v+E give XD=p_Q-(1-Y)p_v-Yp_o. Taking l1 norms, using Y in [0,1], ||D||_1=tau, and the row norm bound from node 1.1.1 for the representative row p_Q and for p_v,p_o, gives |X|tau <= ||p_Q||_1+(1-Y)||p_v||_1+Y||p_o||_1 <= (1+2t)+(1-Y)(1+2t)+Y(1+2t)=2+4t.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.1.4

**Statement:** One global exterior coefficient budget. The exterior fibers satisfy sum_{Q in Ext}|d_Q| <= t(1+(2+t)/A). Every Q in Ext is nonactor, hence c_Q=0 by the root's zero-top hypothesis. From d_Q,e_Q and p_f=p_v-A(p_z-p_v)+t(p_o-p_v), for every fiber Q one has P_z(Q)=c_Q+d_Q, P_o(Q)=c_Q+e_Q, and P_f(Q)=c_Q-Ad_Q+te_Q. Split Ext into Ext_-:={Q:d_Q<0} and Ext_+:={Q:d_Q>=0}, and let S_-,S_+ be the corresponding unions of original coordinate indices. On S_-, c_Q=0 and the row-z lower subset bound from node 1.1.1 gives -sum_{Ext_-}|d_Q|=P_z(S_-)>=-t, hence sum_{Ext_-}|d_Q|<=t. Put D_+:=sum_{Ext_+}d_Q>=0 and E_+:=sum_{Ext_+}e_Q. On S_+, the row-f lower and row-o upper subset bounds give -AD_++tE_+=P_f(S_+)>=-t and E_+=P_o(S_+)<=1+t. Therefore AD_+<=t(E_++1)<=t(2+t), so sum_{Ext_+}|d_Q|=D_+<=t(2+t)/A. Adding the two sign-union bounds proves the displayed budget; no factor depending on the number of fibers occurs.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

#### Node 1.1.5

**Statement:** The unit moment cannot be financed, giving the contradiction. Let Hin:={Q: Q is a support fiber and p_Q is in H}. Nonsupport fibers have d_Q=0 by definition, while every support fiber lies in exactly one of Hin and Ext. For Q in Hin, node 1.1.2 gives |x_Q|<=A, and grouping the original coordinates by full fibers gives sum_{Q in Hin}|d_Q| <= sum_Q |sum_{j in Q}D_j| <= sum_j|D_j|=||D||_1=tau. Hence |sum_{Hin}x_Qd_Q|<=A tau. Nodes 1.1.3 and 1.1.4, together with t=tau^2 and tau>0, give |sum_{Ext}x_Qd_Q| <= ((2+4t)/tau) sum_{Ext}|d_Q| <= tau(2+4t)(1+(2+t)/A). Applying these two bounds to the exact moment sum_Q x_Qd_Q=1 from node 1.1.2 yields 1 <= tau[A+(2+4t)(1+(2+t)/A)]. But 0<tau<=1/256 implies t=tau^2<1/4 and t<1; therefore 2+4t<3, (2+t)/A<=(2+t)/4<3/4, and A<=6. The right side is thus strictly less than (1/256)[6+3(1+3/4)]=45/1024<1, contradicting the preceding necessary inequality.

**Type:** qed

**Inference:** contradiction

**Status:** validated

**Taint:** clean

