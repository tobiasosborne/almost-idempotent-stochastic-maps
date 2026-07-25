# Proof Export

## Node 1

**Statement:** Exact amplified Ha adjointness: there is a universal e_adj > 0 such that every H-CB datum with e <= e_adj, every n >= 1, and every Z in M_n tensor S_{P,R} satisfy (Ha^Q_{P,R})_n(Z)^dagger=(Ha^Q_{R,P})_n(Z^dagger).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Let e_cmp>0 be the universal constant from lem-compcb-amplified-compression-identities. Let e_ip>0 be a universal smallness threshold for which the Euclidean sesquilinear forms in def-ha-map and the registered column-hilbert-inner-product-displays are genuine Hilbert inner products (such a threshold exists from their universal 1+/-O(e) norm comparison). Set e_adj=min(e_cmp,e_ip)>0, and fix an arbitrary H-CB datum with e<=e_adj, n>=1, and Z in M_n tensor S_{P,R}. It remains to establish the asserted equality for this arbitrary fixed instance.

**Type:** local_assume

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For any delta-projections A,B in the fixed datum and every a in S_{A,B}, dagger maps S_{A,B} to S_{B,A}, and tilde Q is Hermitian.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Since e<=e_adj<=e_cmp, apply lem-compcb-amplified-compression-identities at n=1. If a is in S_{A,B}=im(Co_{A,B}), then a=Co_{A,B}(a), so a^dagger=Co_{B,A}(a^dagger) and a^dagger is in S_{B,A}; similarly for every corner. Also tilde Q=Co_{Q,Q}(Q) and Q^dagger=Q, hence tilde Q^dagger=Co_{Q,Q}(Q^dagger)=tilde Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Conditional calculation only (and therefore not yet a proof of the reversal assertion in node 1.2): assume the presently unregistered premise that, for compatible a in S_{A,B} and b in S_{B,C}, the compressed product is defined by a dot b := Co_{A,C}(ab). Then lem-compcb-amplified-compression-identities at n=1 and the involution axiom give (a dot b)^dagger = Co_{A,C}(ab)^dagger = Co_{C,A}((ab)^dagger) = Co_{C,A}(b^dagger a^dagger) = b^dagger dot a^dagger; node 1.2.1 supplies the reversed corner memberships. However, neither def-ha-map nor def-hcb-datum nor any registered af definition supplies the assumed formula. Hence the allowed inputs do not currently establish the reversal assertion; the compressed-product definition must first be added to the shard's defs and registered in this workspace.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** The registered definition compressed-product-display supplies the previously missing identity: for delta-projections A,B,C and compatible a in S_{A,B}, b in S_{B,C}, one has a dot b=Co_{A,C}(ab). Together with node 1.2.1 and lem-compcb-amplified-compression-identities at n=1, this gives the exact reversal identity (a dot b)^dagger=b^dagger dot a^dagger. Thus the earlier negative scope assertion and the claimed need for further definition provisioning are withdrawn.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.1

**Statement:** By compressed-product-display, a dot b=Co_{A,C}(ab). Node 1.2.1 gives a^dagger in S_{B,A} and b^dagger in S_{C,B}, so the reversed compressed product is defined and b^dagger dot a^dagger=Co_{C,A}(b^dagger a^dagger).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.3.2

**Statement:** Apply lem-compcb-amplified-compression-identities at n=1 to the ambient element ab and use the involution law: (a dot b)^dagger=Co_{A,C}(ab)^dagger=Co_{C,A}((ab)^dagger)=Co_{C,A}(b^dagger a^dagger)=b^dagger dot a^dagger. No associativity estimate or unregistered premise is used.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** For every z in S_{P,R}, the level-one Ha operators satisfy Ha^Q_{R,P}(z^dagger)=Ha^Q_{P,R}(z)^dagger as bounded operators from S_{P,Q} to S_{R,Q}.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Fix z in S_{P,R} and put T=Ha^Q_{P,R}(z). For arbitrary x in S_{R,Q} and y in S_{P,Q}, def-ha-map gives (y^dagger dot z) dot x + y^dagger dot (z dot x) = 2 <y,T x> tilde Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Take dagger of the equality in node 1.3.1. By node 1.2, tilde Q is Hermitian and every compressed product reverses exactly under dagger. Thus the daggered left side is x^dagger dot (z^dagger dot y) + (x^dagger dot z^dagger) dot y (the two summands may be reordered by commutativity of addition). The daggered scalar is conjugated, and conjugate symmetry plus the definition of the Hilbert-space adjoint give overline(<y,T x>)=<T x,y>=<x,T^dagger y>. Hence, for all x,y, (x^dagger dot z^dagger) dot y + x^dagger dot (z^dagger dot y) = 2 <x,T^dagger y> tilde Q.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Apply def-ha-map with the pair (R,P), symbol z^dagger, input y in S_{P,Q}, and test vector x in S_{R,Q}. It defines Ha^Q_{R,P}(z^dagger)y as the unique element whose coefficient satisfies exactly the identity in node 1.3.2. Therefore Ha^Q_{R,P}(z^dagger)y=T^dagger y for every y, so Ha^Q_{R,P}(z^dagger)=Ha^Q_{P,R}(z)^dagger.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Dependency audit addressing ch-1495f7e9d0bcd506: the validated node 1.2.1, by direct application of lem-compcb-amplified-compression-identities at n=1, supplies both dagger-stability of the compressed corners and tilde Q^dagger=tilde Q. The remaining identity needed in node 1.3.2 is (a dot b)^dagger=b^dagger dot a^dagger. The amplified-compression external gives Co_{A,C}(ab)^dagger=Co_{C,A}(b^dagger a^dagger), but this becomes the required dot-reversal identity only after using a dot b:=Co_{A,C}(ab). As recorded concretely in validated audit node 1.2.2 and pending definition request 1dc4987689164c1b, neither def-ha-map, def-hcb-datum, nor any registered af definition supplies that premise. Therefore node 1.2 cannot presently be validated and no valid replacement dependency on the compression external alone proves node 1.3. The necessary mathematical repair is to add def-compressed-corner to the allowed defs in the shard, register it here, then validate node 1.2 (or a direct reversal child) before node 1.3; until then node 1.3 must remain pending.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.5

**Statement:** Repaired exact product-reversal step, without using pending node 1.2. For compatible a in S_{A,B} and b in S_{B,C}, registered compressed-product-display gives a dot b=Co_{A,C}(ab). Since the fixed threshold is at most e_cmp, lem-compcb-amplified-compression-identities at n=1 gives Co_{A,C}(ab)^dagger=Co_{C,A}((ab)^dagger). The involution axiom gives (ab)^dagger=b^dagger a^dagger. Validated node 1.2.1 gives a^dagger in S_{B,A}, b^dagger in S_{C,B}, and tilde Q^dagger=tilde Q. Applying compressed-product-display to those reversed compatible corners yields Co_{C,A}(b^dagger a^dagger)=b^dagger dot a^dagger. Therefore (a dot b)^dagger=b^dagger dot a^dagger, and tilde Q is Hermitian, using only the registered display, the allowed validated compression external, and node 1.2.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.6

**Statement:** Fix z and T=Ha^Q_{P,R}(z) as in validated node 1.3.1. For arbitrary x in S_{R,Q} and y in S_{P,Q}, dagger its defining equality. Applying node 1.3.5 to each compressed product and to tilde Q gives (x^dagger dot z^dagger) dot y+x^dagger dot (z^dagger dot y)=2*overline(<y,T x>)*tilde Q=2*<x,T^dagger y>*tilde Q, where conjugate symmetry and the Hilbert-space adjoint identity give overline(<y,T x>)=<T x,y>=<x,T^dagger y>. By def-ha-map for the pair (R,P), symbol z^dagger, input y, and test vector x, the left side is also 2*<x,Ha^Q_{R,P}(z^dagger)y>*tilde Q. The defining uniqueness in def-ha-map therefore gives Ha^Q_{R,P}(z^dagger)y=T^dagger y for every y, hence Ha^Q_{R,P}(z^dagger)=Ha^Q_{P,R}(z)^dagger.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Writing the amplification entrywise, the (i,j) block of (Ha^Q_{P,R})_n(Z)^dagger equals the (i,j) block of (Ha^Q_{R,P})_n(Z^dagger); hence the two amplified operators are equal. Since the instance fixed in node 1.1 was arbitrary, this proves node 1 with e_adj as chosen there.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Write Z=[Z_{ij}]. By the standard matrix amplification in the contract, (Ha^Q_{P,R})_n(Z) is the block operator [Ha^Q_{P,R}(Z_{ij})] from the n-fold Hilbert direct sum of S_{R,Q} to that of S_{P,Q}. Therefore its Hilbert-space adjoint has (i,j) block Ha^Q_{P,R}(Z_{ji})^dagger.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** The (i,j) entry of Z^dagger is Z_{ji}^dagger, which lies in S_{R,P} by node 1.2.1. Hence the (i,j) block of (Ha^Q_{R,P})_n(Z^dagger) is Ha^Q_{R,P}(Z_{ji}^dagger). Node 1.3 identifies this with Ha^Q_{P,R}(Z_{ji})^dagger, the (i,j) block found in node 1.4.1. Equality of every block proves the amplified operator equality, and arbitrary n,Z plus node 1.1 gives the universal assertion.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.4.2.1

**Statement:** Conditional on validation of node 1.3, fix i,j and apply node 1.3 with z=Z_{ji}. Since Z_{ji} is in S_{P,R}, node 1.2.1 gives Z_{ji}^dagger in S_{R,P}; hence node 1.3 yields Ha^Q_{R,P}(Z_{ji}^dagger)=Ha^Q_{P,R}(Z_{ji})^dagger. By node 1.4.1 the right-hand side is the (i,j) block of (Ha^Q_{P,R})_n(Z)^dagger, while entrywise amplification and (Z^dagger)_{ij}=Z_{ji}^dagger identify the left-hand side as the (i,j) block of (Ha^Q_{R,P})_n(Z^dagger). Thus all blocks agree. This step is structurally dependent on nodes 1.2.1, 1.3, and 1.4.1 and cannot be accepted before node 1.3 is validated.

**Type:** qed

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.2.1.1

**Statement:** Correction of the stale dependency audit: the registered AF definition compressed-product-display now supplies, for compatible a in S_{A,B} and b in S_{B,C}, a dot b = Co_{A,C}(ab). Together with validated node 1.2.1, the validated external lem-compcb-amplified-compression-identities at n=1, and the involution law, this gives the exact reversal identity (a dot b)^dagger = b^dagger dot a^dagger. Thus the former assertion that this definition was unregistered, and the resulting claimed obstruction to deriving node 1.3, are withdrawn; the product-reversal ingredient required by node 1.3 is available in the current workspace.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

###### Node 1.4.2.1.1.1

**Statement:** Let a be in S_{A,B} and b in S_{B,C}. By validated node 1.2.1, a^dagger is in S_{B,A} and b^dagger is in S_{C,B}, so the reversed compressed product is defined. The registered compressed-product-display and the validated amplified-compression identity at n=1 give (a dot b)^dagger = Co_{A,C}(ab)^dagger = Co_{C,A}((ab)^dagger). The registered involution axiom gives (ab)^dagger=b^dagger a^dagger, and a second use of compressed-product-display gives Co_{C,A}(b^dagger a^dagger)=b^dagger dot a^dagger. Hence (a dot b)^dagger=b^dagger dot a^dagger exactly; no associativity or approximation estimate is used.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

