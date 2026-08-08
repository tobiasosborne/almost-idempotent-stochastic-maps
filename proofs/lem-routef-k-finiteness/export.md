# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, for every Delta' supplied for (W_RF,S) by lem-routef-delta-prime-closeness, every Delta supplied from that same Delta' by lem-routef-delta-normalization-closeness, every Upsilon' supplied from that same pair by lem-routef-upsilon-prime-closeness, and every Upsilon supplied from that same triple by lem-routef-upsilon-normalization-closeness, writing the fields of (W_RF,S) as the unqualified symbols below: Route F common coefficient/domain: K in (1.6) is finite and universal, and rho_fac in (1.7) is positive and is a common domain for the degree-two estimate and the three Route-F factorization estimates.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** The prefix of node 1 is a nested conditional binding, not an assertion that Delta', Delta, Upsilon', and Upsilon exist for every formation-applicable eta. The formation lemma supplies one global W_RF and, for each formation-applicable input, a datum S; node 1 then quantifies successively over any Delta', Delta, Upsilon', and Upsilon supplied on the respective provider domains, with the displayed dependency relations and unqualified notation. Moreover, on the common domain 0 <= eta <= rho_fac where the four estimates are invoked, all four providers are applicable in sequence.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** The contract prefix literally has the nested form: after fixing W_RF and S, for every Delta prime supplied by the first provider, every Delta supplied from that Delta prime by the second provider, every Upsilon prime supplied from that same pair by the third provider, and every Upsilon supplied from that same triple by the fourth provider. Therefore it binds any such supplied maps conditionally and makes no unconditional existence claim for eta outside the providers respective radius hypotheses.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** If 0 <= eta <= rho_fac, then (1.7) gives eta <= rho_2 and eta <= rho_DeltaUpsilon. From (1.2), rho_2 <= rho_Delta prime and rho_2 <= rho_Delta, so the Delta-prime and Delta providers apply successively. From (1.5), rho_DeltaUpsilon <= rho_Upsilon, and the definition of rho_Upsilon in (1.5) gives rho_Upsilon <= rho_Upsilon prime; hence the Upsilon-prime and Upsilon providers also apply successively. Thus all four maps exist with the required dependency relations on the common domain, while outside that domain node 1 asserts only the nested conditional quantification.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For the globally fixed header W_RF, every coefficient entering K is a finite positive real scalar independent of H, Phi, eta, dimension, amplification level, and block data, and each radius entering rho_fac is positive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** By lem-routef-raw-factor-setting-formation and (1.1) of def-routef-raw-factor-setting, C_theta, C_A, bar_C_E, C_V, and C_T are finite positive real scalars; rho_theta, rho_AI, epsilon_E/C_A, [4(1+C_theta)]^(-1), and [4(1+C_V)]^(-1) are positive, so their finite minimum rho_T is positive. All these scalars are independent of the input data because W_RF is one globally fixed independent header and the displayed operations use only its fields and numerical constants.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Starting from the positive finite scalars of (1.1), the serial definitions in (1.2) make C_Delta', C_Delta, C_2, and C_3 finite positive, and make rho_unit, rho_id, rho_prod, rho_Delta', rho_Delta, rho_2, rho_DeltaPhi, and rho_3 positive: sums and positive integer multiples preserve finite positivity, reciprocals have strictly positive denominators, and every displayed minimum has finitely many positive entries. These derived scalars remain independent of all input data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.2.1

**Statement:** Directly expanding (1.1)-(1.2) of def-routef-raw-factor-setting and using lem-routef-raw-factor-setting-formation: C_theta=12*(sqrt(2)-1)>0, C_A=20+(211/8)*C_theta>0, bar_C_E=max{1,C_E}>=1, hence C_V=bar_C_E*C_A>0 and C_T=C_theta+3*C_V>0, all finite; eta_A, epsilon_E, rho_theta, and rho_AI are positive, so every entry of rho_T is positive. Substitution into (1.2) then proves, in displayed order, the asserted coefficient finiteness/positivity and radius positivity, because each operation is a finite sum, positive multiple, reciprocal of a positive scalar, or finite minimum of positive scalars. Global-header independence is preserved under these scalar operations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Using the positive finite quantities already produced by (1.1)-(1.2), (1.3) makes C_N, C_R, C_L, and C_Upsilon' finite positive; since C_R>0, (2*C_R)^(-1)>0, and therefore (1.4) makes rho_Upsilon' a finite minimum of positive radii and hence positive. These derived scalars remain independent of all input data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** Direct expansion from the formation data through (1.1)-(1.3) of def-routef-raw-factor-setting gives finite positive C_V, C_T, C_Delta', C_Delta, C_2, and C_3; therefore the four sums defining C_N, C_R, C_L, and C_Upsilon' are finite positive. Direct expansion of the radius formulas through (1.2) gives positive rho_T, rho_id, rho_Delta, rho_2, and rho_3, while C_R>0 gives (2*C_R)^(-1)>0; their minimum rho_Upsilon' in (1.4) is thus positive. Every value uses only the fixed input-independent header and numerical scalar operations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.4

**Statement:** Using the positive finite quantities produced by (1.1)-(1.4), (1.5) makes C_Upsilon finite positive and makes rho_Upsilon, rho_DeltaUpsilon, rho_mult, and rho_UpsilonDelta positive: both new reciprocal denominators are strictly positive and every displayed minimum has only positive entries. These derived scalars remain independent of H, Phi, eta, dimension, amplification level, and block data.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.4.1

**Statement:** Direct expansion from lem-routef-raw-factor-setting-formation through (1.1)-(1.4) of def-routef-raw-factor-setting yields finite positive C_T and C_Upsilon' and positive rho_unit, rho_Upsilon', rho_theta, rho_T, rho_id, rho_Delta, and rho_DeltaPhi. Hence C_Upsilon=6*C_T+7*C_Upsilon' is finite positive, [2*(C_T+C_Upsilon')]^(-1)>0, and each minimum defining rho_Upsilon, rho_DeltaUpsilon, rho_mult, and rho_UpsilonDelta in (1.5) is positive. These quantities depend only on the globally fixed input-independent header and numerical scalar operations.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** The scalar K defined by (1.6) is finite and universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By lem-routef-raw-factor-setting-formation, the fields of W_RF are one fixed package independent of H, Phi, eta, dimension, amplification level, and block data. Direct serial expansion of (1.1)-(1.5) in def-routef-raw-factor-setting uses only finite real sums, products, maxima, minima, and reciprocals with positive denominators, so C_theta, C_Delta, C_Upsilon, and C_2 are finite and input-independent. Consequently all four entries in the maximum (1.6) are finite and input-independent, and their finite maximum K is finite and universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** The scalar rho_fac defined by (1.7) is positive.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** From lem-routef-raw-factor-setting-formation, eta_A>0 and epsilon_E>0, while C_theta=12*(sqrt(2)-1)>0, C_A=20+(211/8)*C_theta>0, rho_theta=1/8>0, and bar_C_E=max{1,C_E}>=1. Expanding (1.1)-(1.5) of def-routef-raw-factor-setting in displayed order, every coefficient used as a reciprocal denominator is positive and every radius is a finite minimum of positive quantities; in particular rho_2, rho_DeltaUpsilon, rho_mult, and rho_UpsilonDelta are positive. Equation (1.7) defines rho_fac as the minimum of exactly these four positive numbers, hence rho_fac>0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Every eta with 0 <= eta <= rho_fac lies simultaneously in the domains of lem-routef-degree-two-estimate, lem-routef-delta-upsilon-telescope, lem-routef-multiplicative-telescope, and lem-routef-upsilon-delta-telescope; hence rho_fac is a common domain for the degree-two estimate and the three Route-F factorization estimates.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** Equation (1.7) of def-routef-raw-factor-setting gives rho_fac<=rho_2, rho_fac<=rho_DeltaUpsilon, rho_fac<=rho_mult, and rho_fac<=rho_UpsilonDelta. Thus 0<=eta<=rho_fac implies each corresponding radius hypothesis. In the ambient package supplied respectively by lem-routef-raw-factor-setting-formation, lem-routef-delta-prime-closeness, lem-routef-delta-normalization-closeness, lem-routef-upsilon-prime-closeness, and lem-routef-upsilon-normalization-closeness, exact application of lem-routef-degree-two-estimate at rho_2, lem-routef-delta-upsilon-telescope at rho_DeltaUpsilon, lem-routef-multiplicative-telescope at rho_mult, and lem-routef-upsilon-delta-telescope at rho_UpsilonDelta yields all four estimates on 0<=eta<=rho_fac. Therefore rho_fac is their common domain.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

