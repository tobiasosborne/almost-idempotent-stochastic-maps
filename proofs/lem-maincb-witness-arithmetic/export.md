# Proof Export

## Node 1

**Statement:** After first fixing positive finite universal provider witnesses D_0,D_1,D_2,D_3,e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb,e_it,K_disp,K_floor,epsilon_unit,delta_unit,a_unit,L,c0_cb,K_1,K_2,K_3,e_env,e_s2,e_cross,e_sim,e_full with K_2,K_3 >= max{1,L,c0_cb*L}, set D_* = max{1,D_0,D_1,D_2,D_3}; then there is a def-maincb-witness-ledger datum W whose fields satisfy W.r_reset = min{e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*),[2*(1+K_disp)*D_*]^{-1}}, W.K_call = max{1,L+1,c0_cb,K_1,K_2,K_3}, W.epsilon_MAIN = min{e_env,e_1/K_1,e_s2/K_2,e_cross/K_3,W.r_reset/W.K_call,e_sim/W.K_call,e_full/W.K_call,[2*max{1,c0_cb*W.K_call}]^{-1}}, and the remaining fields equal the correspondingly named receiving witnesses; in particular every field is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Since D_0,D_1,D_2,D_3 are positive finite universal scalars, D_* = max{1,D_0,D_1,D_2,D_3} is positive, finite, universal, dimension-independent, and satisfies D_* >= 1. Consequently each of e_0,e_1,e_2,e_3,epsilon_max^cb,delta_max^cb/D_*,e_it/(D_*+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D_*), and [2*(1+K_disp)*D_*]^{-1} is a positive finite universal scalar independent of dimension, amplification, block data, class count, and stage index.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Therefore the finite minimum r_reset of the eleven reset candidates displayed in the contract is positive, finite, universal, independent of dimension, amplification, block data, class count, and stage index, and it has exactly the asserted formula.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Since L,c0_cb,K_1,K_2,K_3 are positive finite universal scalars, K_call = max{1,L+1,c0_cb,K_1,K_2,K_3} is positive, finite, universal, independent of dimension, amplification, block data, class count, and stage index, satisfies K_call >= 1, and has exactly the asserted formula.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Using positivity and finiteness of K_1,K_2,K_3,K_call,r_reset and of e_env,e_1,e_s2,e_cross,e_sim,e_full, every one of e_env,e_1/K_1,e_s2/K_2,e_cross/K_3,r_reset/K_call,e_sim/K_call,e_full/K_call,[2*max{1,c0_cb*K_call}]^{-1} is positive, finite, universal and independent of dimension, amplification, block data, class count, and stage index. Hence their finite minimum epsilon_MAIN is so as well and has exactly the asserted formula.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** Define W to be the def-maincb-witness-ledger tuple (c0_cb,L,K_1,K_2,K_3,K_call,e_env,e_1,e_s2,e_cross,r_reset,epsilon_MAIN). By the definition, these entries are exactly its twelve named fields, so the remaining fields equal the correspondingly named receiving witnesses; combining their inherited properties with the established properties of K_call,r_reset,epsilon_MAIN proves existence of the asserted W and proves that every field is positive, finite, universal, and independent of dimension, amplification, block data, class count, and stage index.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

