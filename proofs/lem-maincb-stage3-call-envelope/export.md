# Proof Export

## Node 1

**Statement:** After first choosing a universal c0 witness for which lem-maincb-error-improvement remains valid, fixing the corresponding L^0,e_env^0 witnesses of lem-maincb-direct-corner-envelope, and fixing the C_cross^0,e_cross^0 witnesses of lem-maincb-cross-class-merging-datum, there is a universal K_3^0 >= 1 with every Stage-3 prerequisite absorbed such that for every def-maincb-witness-ledger datum W with W.c0_cb = c0, W.L >= L^0, W.K3 >= max{K_3^0,1,W.L,W.c0_cb*W.L}, and W.e_cross <= e_cross^0, if A is a finite-dimensional extended epsilon-C*-algebra, w:C^m->A is an extended W.c0_cb*epsilon-inclusion satisfying ||w(I_{C^m})-I_A|| <= W.c0_cb*epsilon with one-dimensional atomic images, a supplied MAIN partition state for A,w has disjoint nonempty unions U,V sharing no class and R=U union V, 0 <= epsilon <= W.e_cross/W.K3, and supplied current reset isomorphisms v_U:B_U->A_U and v_V:B_V->A_V have recorded ambient fields epsilon_U,epsilon_V <= W.L*epsilon and satisfy d_U <= W.c0_cb*epsilon_U, d_V <= W.c0_cb*epsilon_V, ||v_U(I_{B_U})-u_{A_U}|| <= W.c0_cb*epsilon_U, and ||v_V(I_{B_V})-u_{A_V}|| <= W.c0_cb*epsilon_V, then lem-maincb-direct-corner-envelope certifies A_R with the Stage-3 raw-call target ambient record epsilon_R := W.L*epsilon, and t_3=W.K3*epsilon dominates epsilon_U,epsilon_V,d_U,d_V,epsilon_R, both displayed unit norms, and every other datum error, so lem-maincb-cross-class-merging-datum furnishes the explicit Stage-3 four-corner raw-call datum with rho <= C_cross^0*t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Choose the universal witnesses in the contract in their mandated order and set K_3^0 := max{1,L^0,c0*L^0,e_cross^0/e_env^0}; then K_3^0 is universal, K_3^0 >= 1, and e_cross^0/K_3^0 <= e_env^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** By lem-maincb-error-improvement, choose the universal valid coefficient c0 required by the root prefix. Next apply lem-maincb-direct-corner-envelope for this c0, initially obtaining universal witnesses L_*,e_env^0 with L_*>=1 and e_env^0>0, and normalize the coefficient witness to L^0:=max{L_*,c0,1}. Enlarging an error-tolerance coefficient preserves every conclusion of that external: each upper defect bound only weakens, and in each defining lower norm inequality the new lower bound is no larger; hence L^0,e_env^0 are corresponding valid witnesses and L^0>=max{c0,1}. Finally bind the already-fixed C_cross^0,e_cross^0 witnesses named in the root prefix. This makes no new existence inference: by lem-maincb-cross-class-merging-datum, calling them witnesses of that result means its prerequisite corner-unit witness pair was fixed first and the same admissible instance is used here. Thus all chosen constants are universal, and no unlisted dependency is being proved or invoked.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** The quantifier bookkeeping is as follows. The permitted cross-class external has the conditional witness-selection form: after c0, the direct-corner witnesses, and a corner-unit witness pair are fixed, it supplies universal C_cross^0,e_cross^0. The root does not assert existence of the omitted corner-unit pair; its opening phrase fixes C_cross^0,e_cross^0 specifically as witnesses of that external. Hence the theorem is evaluated only in an admissible instance of the external, and unpacking the phrase witnesses of the external carries its prerequisite fixed pair. If such an admissible instance has not been fixed, the root prefix has not been instantiated. Therefore binding the cross constants here is valid without adding the corner-unit comparison as a dependency or proving it anew.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

#### Node 1.1.2

**Statement:** Since e_env^0>0 and e_cross^0>0, K_3^0=max{1,L^0,c0*L^0,e_cross^0/e_env^0} is a finite universal constant at least 1, and K_3^0 >= e_cross^0/e_env^0 implies e_cross^0/K_3^0 <= e_env^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Under the hypotheses of node 1, lem-maincb-direct-corner-envelope applies to A,w and certifies the corner A_R with the admissible recorded ambient tolerance epsilon_R := W.L*epsilon, while all its projection, subordination, and complementarity errors are at most W.L*epsilon.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** The scalar assumptions imply 0 <= epsilon <= e_env^0: indeed W.K3 >= K_3^0 >= 1 and W.e_cross <= e_cross^0 give epsilon <= W.e_cross/W.K3 <= e_cross^0/K_3^0 <= e_env^0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Apply lem-maincb-direct-corner-envelope with c0=W.c0_cb to the nonempty set R=U union V, using node 1.2.1 for epsilon<=e_env^0. With the normalized witnesses fixed in node 1.1.1, it gives P_R a c0*epsilon-projection bound, gives A_R an extended L^0*epsilon-C*-algebra structure, and bounds every subordination and complementarity error by L^0*epsilon. Since epsilon>=0 and c0<=L^0<=W.L, all these errors are at most W.L*epsilon. The same tolerance monotonicity used in choosing L^0 lets the certified L^0*epsilon ambient structure be recorded at the weaker Stage-3 tolerance epsilon_R:=W.L*epsilon. Therefore the direct-corner external certifies precisely the ambient record and error bounds claimed in node 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** At the ordered witness-selection stage, after c0 has been fixed, take any witnesses L_*,e_env^0 supplied by lem-maincb-direct-corner-envelope and define L^0:=max{L_*,c0,1}. This enlarged L^0 is still a valid witness with the same e_env^0: every extended-(L_* epsilon)-C*-algebra defining inequality remains true with the larger tolerance L^0 epsilon (upper-error bounds weaken, and the C*-lower bound 1-L^0 epsilon is no larger than 1-L_* epsilon), and every L_* epsilon subordination or complementarity bound is at most L^0 epsilon. Thus the witnesses fixed in node 1 may and do satisfy L^0>=c0; this is the normalization already recorded in node 1.1.1, not an additional hypothesis on W.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

##### Node 1.2.2.2

**Statement:** With the normalized witnesses, lem-maincb-direct-corner-envelope gives P_R a c0*epsilon-projection bound, gives A_R an extended L^0*epsilon-C*-algebra structure, and gives each subordination and complementarity error a bound L^0*epsilon. Since epsilon>=0 and c0<=L^0<=W.L, all of these bounds are at most W.L*epsilon. The same monotonicity of the defining extended-C*-algebra inequalities lets the L^0*epsilon structure be recorded at epsilon_R:=W.L*epsilon. Hence the conclusion of node 1.2.2 follows without asserting that the external lemma itself originally supplied max{c0,L^0}=L^0.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

### Node 1.3

**Statement:** With t_3 := W.K3*epsilon, every hypothesis of lem-maincb-cross-class-merging-datum holds; t_3 dominates all quantities and datum errors listed in node 1, and that external lemma yields the explicit Stage-3 amplified four-corner raw-call datum in A_R with rho <= C_cross^0*t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** The assumptions W.K3 >= max{1,W.L,W.c0_cb*W.L}, epsilon >= 0, and epsilon <= W.e_cross/W.K3 imply epsilon <= t_3, W.L*epsilon <= t_3, W.c0_cb*W.L*epsilon <= t_3, and t_3 <= W.e_cross. Also W.L >= L^0 >= c0=W.c0_cb, so W.c0_cb*epsilon <= W.L*epsilon <= t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Consequently epsilon_U,epsilon_V,epsilon_R <= t_3; d_U,d_V and both displayed reset-unit norms are at most W.c0_cb*W.L*epsilon <= t_3; the non-unital inclusion defect and displayed ambient-unit error of w are at most W.c0_cb*epsilon <= t_3; and every projection, subordination, and complementarity error certified by lem-maincb-direct-corner-envelope is at most W.L*epsilon <= t_3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** All analytic hypotheses of lem-maincb-cross-class-merging-datum now hold. The root gives W.c0_cb=c0, W.e_cross<=e_cross^0, the required partition and reset-isomorphism data, and the inequalities d_U<=W.c0_cb*epsilon_U and d_V<=W.c0_cb*epsilon_V. Nodes 1.3.1-1.3.2 give epsilon,epsilon_U,epsilon_V,d_U,d_V and both reset-unit errors <=t_3<=W.e_cross; they also give W.c0_cb*epsilon<=t_3, so tolerance monotonicity turns the supplied extended W.c0_cb*epsilon-inclusion w into the required non-unital extended t_3-inclusion, while preserving its one-dimensional images. Hence lem-maincb-cross-class-merging-datum supplies in A_R its explicit Stage-3 amplified four-corner datum with common defect rho<=C_cross^0*t_3. To package the literal raw call, take the named finite-dimensional C*-algebra B_R:=B_U direct-sum B_V with complementary central projections q_U=(I_{B_U},0), q_V=(0,I_{B_V}). Write phi_UU,phi_VV for the datum's diagonal nested-corner and outer-compression maps and phi_UV=phi_VU=0 for its zero-cross-corner maps. Define v_R:B_R->A_R by v_R(b_U,b_V)=phi_UU(b_U)+phi_VV(b_V). The cross source corners q_U B_R q_V and q_V B_R q_U are zero, so v_R restricts to precisely all four supplied corner maps. At every n, I_n tensor v_R is the corresponding sum of the fixed amplifications of phi_UU and phi_VV, hence this is one fixed amplification family. Record the def-maincb-raw-call fields: Stage-3 tag; the two input reset states; source B_R; target A_R; base scale t_3; post-helper scale rho; output v_R with that amplification family; epsilon_R from node 1.2; and d_raw:=rho. This is exactly the asserted Stage-3 four-corner raw-call datum, with d_raw=rho<=C_cross^0*t_3, and it asserts no unproved inclusion or isomorphism property of v_R.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.3.1

**Statement:** Make the packaging explicit as follows. Let B_R:=B_U direct-sum B_V, a named finite-dimensional C*-algebra, with complementary central projections q_U=(I_{B_U},0) and q_V=(0,I_{B_V}). Denote by phi_UU and phi_VV the two diagonal level-one maps produced by the nested-corner and outer-compression parts of the explicit Stage-3 four-corner datum, and by phi_UV=0 and phi_VU=0 its zero-cross-corner maps; their domains are the four q_i B_R q_j corners. Define the single level-one output map v_R:B_R->A_R by v_R(b_U,b_V):=phi_UU(b_U)+phi_VV(b_V). Because q_U B_R q_V=q_V B_R q_U={0}, v_R restricts on all four source corners to exactly phi_UU,phi_UV,phi_VU,phi_VV. Moreover, for every n and (x_U,x_V) in M_n(B_U) direct-sum M_n(B_V), (I_n tensor v_R)(x_U,x_V)=(I_n tensor phi_UU)(x_U)+(I_n tensor phi_VV)(x_V); hence these maps give one fixed amplification family of v_R, not four unrelated level-one maps. Now record the def-maincb-raw-call fields: Stage-3 tag; input reset states (v_U,v_V); source B_R; target A_R; base scale t_3; post-helper datum scale rho; output v_R and the displayed amplification family; target ambient defect epsilon_R; and raw-defect number d_raw:=rho. This is a Stage-3 raw-call datum by definition, and the external bound gives d_raw=rho<=C_cross^0*t_3. No extended-inclusion or isomorphism property of v_R is asserted here, consistently with def-maincb-raw-call.

**Type:** claim

**Inference:** assumption

**Status:** archived

**Taint:** clean

