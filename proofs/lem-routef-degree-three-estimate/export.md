# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, and every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness; for every integer n >= 1 and all X, Y, Z in M_n(S.B), writing the fields of (W_RF,S) as the unqualified symbols below: Route F degree-three estimate: with C_3 := 10+20*C_Delta+12*C_theta+2*C_Delta' and rho_3 := min{rho_theta, rho_Delta', rho_Delta, rho_2}, for 0 <= eta <= rho_3, every amplification satisfies ||Phi_n(Delta_n X Delta_n Y Delta_n Z) - Delta_n(XYZ)|| <= C_3*eta*||X||*||Y||*||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Admissibility and the one-factor invariance estimate. Under the root hypotheses and 0 <= eta <= rho_3, all cited estimates below are applicable, Phi and Delta are UCP and hence completely contractive, tilde-Phi_n tilde-Delta_n=tilde-Delta_n, ||tilde-Delta||_cb <= 2, and for every amplification n and T in M_n(B), ||Phi_n(Delta_n T)-Delta_n T|| <= d||T|| with d:=2(C_theta+C_Delta)eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** Radius bookkeeping, map status, and exact range identity. By def-routef-raw-factor-setting, rho_3=min{rho_theta,rho_Delta_prime,rho_Delta,rho_2}, rho_theta=1/8, and rho_Delta_prime<=rho_T. Thus eta<=rho_3 places us simultaneously in the domains of lem-routef-functional-calculus-closeness, lem-routef-raw-factor-norms, lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-degree-two-estimate, and in eta<1/4 for lem-kitaev-almost-idemp-audit. The root choice is licensed by lem-routef-raw-factor-setting-formation; Phi is UCP there, and the chosen Delta is UCP by lem-routef-delta-normalization-closeness, so both are completely contractive. Formation also gives tilde-Phi^2=tilde-Phi and tilde-Delta(B) subset A=Im(tilde-Phi); hence tilde-Phi_n tilde-Delta_n=tilde-Delta_n at every amplification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Uniform raw-map bound. Lem-routef-raw-factor-norms gives ||tilde-Delta||_cb<=1+C_T eta because eta<=rho_3<=rho_Delta_prime<=rho_T. From def-routef-raw-factor-setting, C_T=C_theta+3C_V and rho_T<=1/[4(1+C_theta)] and rho_T<=1/[4(1+C_V)]. Hence C_theta eta<=1/4 and 3C_V eta<=3/4, so C_T eta<=1 and ||tilde-Delta||_cb<=2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** One-factor estimate. Using tilde-Phi_n tilde-Delta_n=tilde-Delta_n, the exact identity Phi_n Delta_n-Delta_n=(Phi_n-tilde-Phi_n)tilde-Delta_n+Phi_n(Delta_n-tilde-Delta_n)+(tilde-Delta_n-Delta_n) holds. Lem-routef-functional-calculus-closeness bounds the first map difference by C_theta eta, lem-routef-delta-normalization-closeness bounds ||Delta-tilde-Delta||_cb by C_Delta eta, Phi is completely contractive, and ||tilde-Delta||_cb<=2. Therefore for every T, ||Phi_n(Delta_n T)-Delta_n T||<=[2C_theta+C_Delta+C_Delta]eta||T||=2(C_theta+C_Delta)eta||T||=d||T||.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** First three-factor replacement. Assuming the one-factor estimate ||Phi_n(Delta_n T)-Delta_n T|| <= d||T|| and complete contractivity of Phi and Delta, put P0:=Phi_n(Delta_n X Delta_n Y Delta_n Z) and P1:=Phi_n(Phi_n(Delta_n X) Phi_n(Delta_n Y) Phi_n(Delta_n Z)); a three-term product telescope gives ||P0-P1|| <= 3d||X||||Y||||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Write D_X=Delta_n X and F_X=Phi_n(D_X), and similarly for Y,Z. The exact product identity D_XD_YD_Z-F_XF_YF_Z=(D_X-F_X)D_YD_Z+F_X(D_Y-F_Y)D_Z+F_XF_Y(D_Z-F_Z), followed by complete contractivity of Delta and Phi and the assumed one-factor estimate, bounds its norm by 3d||X||||Y||||Z||. Applying the contractive outer Phi_n gives ||P0-P1||<=3d||X||||Y||||Z||.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Associativity comparison. Define P1:=Phi_n(Phi_n(Delta_n X) Phi_n(Delta_n Y) Phi_n(Delta_n Z)) and P2:=Phi_n(Phi_n(Phi_n(Delta_n X) Phi_n(Delta_n Y)) Phi_n(Delta_n Z)). Since eta <= rho_3 <= rho_theta=1/8<1/4, the amplified Phi_assoc1 estimate of lem-kitaev-almost-idemp-audit applied to Delta_n X, Delta_n Y, Delta_n Z, together with complete contractivity of Delta, gives ||P1-P2|| <= 10eta||X||||Y||||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** At amplification n, Phi_assoc1 from lem-kitaev-almost-idemp-audit is precisely ||Phi_n(Phi_n(Phi_n(U)Phi_n(V))Phi_n(W))-Phi_n(Phi_n(U)Phi_n(V)Phi_n(W))||<=10eta||U||||V||||W|| whenever eta<1/4. Substitute U=Delta_n X, V=Delta_n Y, W=Delta_n Z. The two displayed terms are P2 and P1 respectively, while UCP contractivity gives ||U||||V||||W||<=||X||||Y||||Z||; symmetry of norm under sign reversal yields the claimed comparison.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Second three-factor replacement. Define P2:=Phi_n(Phi_n(Phi_n(Delta_n X) Phi_n(Delta_n Y)) Phi_n(Delta_n Z)) and P3:=Phi_n(Phi_n(Delta_n X Delta_n Y) Delta_n Z). Assuming ||Phi_n(Delta_n T)-Delta_n T|| <= d||T|| for all T, where d:=2(C_theta+C_Delta)eta, and complete contractivity of Phi and Delta, a two-factor telescope inside the inner Phi_n costs at most 2d||X||||Y|| and replacing the last Phi_n(Delta_n Z) by Delta_n Z costs at most d||Z||, so ||P2-P3|| <= 3d||X||||Y||||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Let A=Phi_n(Phi_n(Delta_n X)Phi_n(Delta_n Y)), B=Phi_n(Delta_n Z), C=Phi_n(Delta_n X Delta_n Y), and D=Delta_n Z, so P2=Phi_n(AB) and P3=Phi_n(CD). Contractivity of the outer Phi_n and AB-CD=(A-C)B+C(B-D) give ||P2-P3||<=||A-C||||B||+||C||||B-D||. The exact two-factor telescope Phi_n(Delta_n X)Phi_n(Delta_n Y)-Delta_n X Delta_n Y=[Phi_n(Delta_n X)-Delta_n X]Phi_n(Delta_n Y)+Delta_n X[Phi_n(Delta_n Y)-Delta_n Y], followed by contractivity, gives ||A-C||<=2d||X||||Y||. Also ||B||<=||Z||, ||C||<=||X||||Y||, and ||B-D||<=d||Z||. Thus ||P2-P3||<=3d||X||||Y||||Z||.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Degree-two finish and coefficient closure. Define P3:=Phi_n(Phi_n(Delta_n X Delta_n Y) Delta_n Z), P4:=Phi_n(Delta_n(XY) Delta_n Z), and P5:=Delta_n(XYZ). Because eta <= rho_3 <= rho_2, two applications of lem-routef-degree-two-estimate, first to X,Y and then to XY,Z, plus complete contractivity, give ||P3-P4|| <= C_2 eta||X||||Y||||Z|| and ||P4-P5|| <= C_2 eta||X||||Y||||Z||. Independently, for d:=2(C_theta+C_Delta)eta and C_2=C_Delta'+4C_Delta, 6d+10eta+2C_2 eta=(10+12C_theta+20C_Delta+2C_Delta')eta=C_3 eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** First degree-two comparison. Contractivity of the outer Phi_n gives ||P3-P4||<=||Phi_n(Delta_n X Delta_n Y)-Delta_n(XY)|| ||Delta_n Z||. Lem-routef-degree-two-estimate applies because eta<=rho_3<=rho_2 and bounds the first factor by C_2 eta||X||||Y||; UCP contractivity of Delta bounds the second by ||Z||. Hence ||P3-P4||<=C_2 eta||X||||Y||||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** Second degree-two comparison. Apply lem-routef-degree-two-estimate at amplification n to the pair XY,Z. Since M_n(B) is an associative C*-algebra, ||XY||<=||X||||Y|| and (XY)Z=XYZ, so ||P4-P5||=||Phi_n(Delta_n(XY)Delta_n Z)-Delta_n((XY)Z)||<=C_2 eta||XY||||Z||<=C_2 eta||X||||Y||||Z||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Coefficient arithmetic. By def-routef-raw-factor-setting, C_2=C_Delta_prime+4C_Delta and C_3=10+20C_Delta+12C_theta+2C_Delta_prime. With d=2(C_theta+C_Delta)eta, 6d+10eta+2C_2 eta=[12C_theta+12C_Delta+10+2C_Delta_prime+8C_Delta]eta=C_3 eta.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

