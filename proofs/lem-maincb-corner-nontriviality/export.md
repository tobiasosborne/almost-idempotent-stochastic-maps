# Proof Export

## Node 1

**Statement:** Fix the def-maincb-witness-ledger datum W supplied by lem-maincb-reset-constant-ledger; if A is a finite-dimensional extended epsilon-C*-algebra, 0 <= epsilon <= W.epsilon_MAIN, w:C^m->A is an extended W.c0_cb*epsilon-inclusion, and e_j is any projection-basis element of C^m, then P_j=w(e_j) is a W.c0_cb*epsilon-projection satisfying | ||P_j||-1 | <= W.c0_cb*epsilon and hence is nonvanishing, while S_{P_j} contains a nonzero element and therefore dim S_{P_j} >= 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Same-instance ledger alignment: in the construction of the exact fixed W supplied by lem-maincb-reset-constant-ledger, let L^0,e_env^0 denote the particular lem-maincb-direct-corner-envelope witnesses selected before W. The cited reset-ledger result gives W.L>=L^0 and W.e_env<=e_env^0, with no existential reselection. For the root scale 0<=epsilon<=W.epsilon_MAIN, lem-maincb-structural-domain-ledger gives epsilon<=W.e_env and W.L*epsilon<=W.K_call*epsilon<=W.r_reset. Consequently epsilon<=W.e_env<=e_env^0 and 0<=L^0*epsilon<=W.L*epsilon<=W.K_call*epsilon<=W.r_reset.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Set d:=W.c0_cb*epsilon and P_j:=w(e_j). By def-projection-basis, the coordinate projection-basis element e_j of C^m is a nonzero self-adjoint idempotent; as a nonzero projection in the exact C*-algebra C^m it has norm one. At amplification n=1, def-extended-delta-inclusion says that the supplied extended d-inclusion w is a d-homomorphism with the star and product clauses and two-sided (1+-d) norm bounds. Therefore P_j^dagger=P_j, ||P_j^2-P_j||=||w(e_j)w(e_j)-w(e_j^2)||<=d, and 1-d<=||P_j||<=1+d. Hence P_j is a d-projection by def-delta-projection and | ||P_j||-1 |<=d; this explicit second alternative makes P_j nonvanishing.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Let d:=W.c0_cb*epsilon and specialize the extended d-inclusion w at amplification n=1. By def-extended-delta-inclusion, w is then a d-inclusion. GT-kitaev-def-delta-homomorphism defines a d-inclusion to be a d-homomorphism satisfying the two-sided norm bounds, and defines a d-homomorphism in the star-algebra setting to preserve the involution exactly and to satisfy ||w(XY)-w(X)w(Y)|| <= d||X||||Y||. Since def-projection-basis gives e_j^dagger=e_j and e_j^2=e_j, and the nonzero projection e_j in C^m has ||e_j||=1, these clauses yield w(e_j)^dagger=w(e_j), ||w(e_j)^2-w(e_j)||=||w(e_j)w(e_j)-w(e_j^2)|| <= d, and 1-d <= ||w(e_j)|| <= 1+d. Thus, for P_j=w(e_j), def-delta-projection applies and | ||P_j||-1 | <= d; this is precisely the explicit nonvanishing alternative used by the parent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** After node 1.1 is validated, epsilon<=e_env^0 for the same witnesses frozen before W. The singleton U={j} is nonempty, the root supplies the same finite-dimensional extended epsilon-C*-algebra A and the same extended W.c0_cb*epsilon-inclusion w, and W.c0_cb is the c0 witness used for lem-maincb-direct-corner-envelope in lem-maincb-reset-constant-ledger. Applying lem-maincb-direct-corner-envelope to U={j} gives P_U=w(e_j)=P_j and makes the exact vector space A_U=S^A_{P_U}=S^A_{P_j} an extended L^0*epsilon-C*-algebra. Denote the unit furnished on this exact space by I_{S_{P_j}}; by the algebra typing, I_{S_{P_j}} is an element of S_{P_j}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** After nodes 1.1 and 1.3 are validated, I_{S_{P_j}} is the unit of the extended L^0*epsilon-C*-algebra on the exact space S_{P_j}, and 0<=L^0*epsilon<=W.r_reset. By lem-maincb-witness-arithmetic as instantiated in lem-maincb-reset-constant-ledger, W.r_reset is the minimum of listed positive thresholds including [2*(1+K_disp)*D_*]^{-1}, where K_disp>0 and D_*=max{1,D_0,D_1,D_2,D_3}>=1. Thus L^0*epsilon<=W.r_reset<1/2. The n=1 approximate-unit axiom in def-epsilon-cstar-algebra, inherited through def-extended-epsilon-cstar-algebra, gives | ||I_{S_{P_j}}||-1 |<=L^0*epsilon<1/2. Hence ||I_{S_{P_j}}||>1/2, so this element of S_{P_j} is nonzero.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** After node 1.4 is validated, the exact vector space S_{P_j} contains its explicitly typed nonzero element I_{S_{P_j}}. Since S_{P_j} is a linear subspace of the finite-dimensional space A, it is finite-dimensional; the elementary dimension theorem for finite-dimensional vector spaces then gives dim S_{P_j}>=1. Combining this with node 1.2 yields every conclusion of the root contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

