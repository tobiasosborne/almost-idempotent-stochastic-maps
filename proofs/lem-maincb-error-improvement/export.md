# Proof Export

## Node 1

**Statement:** Complete error improvement: there are universal epsilon_max^cb>0, delta_max^cb>0 and c_0^cb<infinity such that every extended delta-inclusion v:B->A from a finite-dimensional C*-algebra B into an extended epsilon-C*-algebra A with 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb can be replaced by an extended c_0^cb*epsilon-inclusion v_tilde:B->A that is bijective whenever v is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Fix universal constants e_it>0, K_disp<infinity, and K_floor<infinity supplied by lem-maincb-improvement-iteration, and set epsilon_max^cb:=e_it/2, delta_max^cb:=min(e_it/2, 1/(2*(1+|K_disp|))), and c_0^cb:=K_floor; then epsilon_max^cb and delta_max^cb are positive and c_0^cb is finite.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For any 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb, one has delta+epsilon<=e_it and 1-delta-|K_disp|*delta>=1/2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Under the hypotheses of node 1, lem-maincb-improvement-iteration applied with d=delta yields a linear map v_tilde:B->A that is an extended c_0^cb*epsilon-inclusion and satisfies ||v_tilde-v||<=K_disp*delta<=|K_disp|*delta at level one.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** By node 1.2, d:=delta satisfies d+epsilon<=e_it; the remaining assumptions that B is a finite-dimensional C*-algebra, A is an extended epsilon-C*-algebra, and v:B->A is an extended d-inclusion are exactly the hypotheses of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.3.1.1

**Statement:** Validated node 1.1 fixes epsilon_max^cb=e_it/2 and delta_max^cb=min(e_it/2,1/(2*(1+|K_disp|))); validated node 1.2 consequently establishes, for the present bounds 0<=epsilon<=epsilon_max^cb and 0<=delta<=delta_max^cb, the required inequality delta+epsilon<=e_it.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

##### Node 1.3.1.2

**Statement:** Set d:=delta. The preceding child gives d+epsilon<=e_it. For the arbitrary instance under node 1, B is a finite-dimensional C*-algebra, A is an extended epsilon-C*-algebra, and v:B->A is an extended delta-inclusion, hence an extended d-inclusion by the equality d=delta. These are exactly all hypotheses of lem-maincb-improvement-iteration.

**Type:** claim

**Inference:** universal_instantiation

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Applying lem-maincb-improvement-iteration with d=delta therefore gives a linear dagger-preserving v_tilde:B->A which is an extended K_floor*epsilon-inclusion and obeys sup_n ||I_n tensor v_tilde-I_n tensor v||<=K_disp*delta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Since c_0^cb=K_floor, the inclusion conclusion is the required extended c_0^cb*epsilon-inclusion; taking n=1 in the supremum gives ||v_tilde-v||<=K_disp*delta, and K_disp*delta<=|K_disp|*delta because delta>=0.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** If v is bijective, then the map v_tilde furnished above is injective: for every x in B, the level-one lower norm bound for the extended delta-inclusion v and the displacement estimate give ||v_tilde(x)|| >= ||v(x)||-||(v_tilde-v)(x)|| >= (1-delta-|K_disp|*delta)||x|| >= (1/2)||x||.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Because v is an extended delta-inclusion, its n=1 amplification satisfies the lower norm bound ||v(x)||>=(1-delta)||x|| for every x in B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** The level-one displacement bound in node 1.3 implies ||(v_tilde-v)(x)||<=|K_disp|*delta*||x|| for every x in B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.3

**Statement:** The reverse triangle inequality and the preceding two bounds give ||v_tilde(x)||>=||v(x)||-||(v_tilde-v)(x)||>=(1-delta-|K_disp|*delta)||x||; node 1.2 makes the last coefficient at least 1/2, so v_tilde(x)=0 forces x=0 and v_tilde is injective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** If v is bijective, then A and B have the same finite dimension; hence the linear injective map v_tilde:B->A is also surjective and therefore bijective. Together with the preceding nodes this proves node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.1

**Statement:** If v:B->A is bijective and B is finite-dimensional, then v is a linear vector-space isomorphism, so A is finite-dimensional and dim(A)=dim(B).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.2

**Statement:** By node 1.4, v_tilde:B->A is injective; an injective linear map between finite-dimensional vector spaces of equal dimension is surjective, hence v_tilde is bijective.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.5.3

**Statement:** Nodes 1.1--1.3 provide universal positive thresholds, a finite c_0^cb, and the required extended c_0^cb*epsilon-inclusion for every admissible v; the preceding child supplies the additional bijectivity whenever v is bijective, which is precisely the conclusion of node 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

