# Proof Export

## Node 1

**Statement:** There are universal D_1 < infinity and e_1 > 0 such that, if an explicit Stage-1 raw-call datum supplies complementary target t-projections, an old extended t-inclusion C^{m-1}->S_{P_old} when m > 1, a fresh extended t-inclusion C^2->S_{P_fresh}, fixed amplification families, and every projection, complementarity, map, and target-ambient defect is at most t <= e_1, then their sum map is an extended D_1*t-inclusion C^{m+1}->A; when m = 1, the old side is absent and the conclusion is the supplied fresh inclusion.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Defect-parameter monotonicity: if 0 <= delta <= Delta and a linear map with its fixed amplification family is an extended delta-inclusion, then it is an extended Delta-inclusion, because every defining delta-homomorphism defect upper bound and the two-sided (1 +/- delta) norm bounds in def-extended-delta-inclusion only weaken when delta is enlarged.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Choose the universal constants from lem-maincb-direct-sum-inclusion-merge: if C_dir < infinity and e_dir > 0 are its witnesses, set D_1 := max(1,C_dir) and e_1 := e_dir; then D_1 < infinity and e_1 > 0 are universal.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Case m = 1: the final clause of the root contract explicitly replaces the preceding merged-map conclusion by the supplied fresh inclusion. The old side is absent, and the hypothesis already supplies v_fresh:C^2->S_{P_fresh} as an extended t-inclusion with its fixed amplification family. Since C^2=C^{m+1}, this is exactly the conclusion stipulated for m=1. No change of codomain from S_{P_fresh} to A is asserted, and neither defect-parameter monotonicity nor a corner-to-ambient transfer is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Case m > 1: apply lem-maincb-direct-sum-inclusion-merge with B_1=C^{m-1}, B_2=C^2, P_1=P_old, P_2=P_fresh, v_1=v_old, and v_2=v_fresh. All of its hypotheses are exactly among the raw-call hypotheses and t <= e_1=e_dir. It yields the sum map as an extended C_dir*t-inclusion on C^{m-1} direct-sum C^2 = C^{m+1}; since C_dir*t <= D_1*t, defect-parameter monotonicity gives the required extended D_1*t-inclusion into A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

