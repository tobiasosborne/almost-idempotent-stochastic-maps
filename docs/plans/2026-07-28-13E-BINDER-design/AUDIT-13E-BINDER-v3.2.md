# Hostile audit of `DESIGN-13E-BINDER-v3.2.md`

1. **Location:** v3.1 §1 line 6 versus v3.2 line 16, complete contract
   token stream.  
   **Defect:** none. A token diff using
   `[[:alnum:]_]+|[^[:space:][:alnum:]_]` has 724 tokens in v3.1 and 771
   in v3.2. The 47 added tokens are exactly the two prescribed repair
   groups: (i) the graph predicate changes `such that g_V(A^par) is` to
   `such that, for every V in calU and every A^par in
   B_{2delta}^{icalH}(0), g_V(A^par) is`; and (ii) the inverse
   characterization appends `for every X in S_delta` to the first identity
   and `for every (U,H) in calU x B_delta^{calH}(J)` to the second. There
   is no deletion, reordering, or other substitution. As a stronger check,
   applying exactly those replacements to the v3.1 character stream gives
   the v3.2 stream byte-for-byte (both have SHA256
   `089a9c437c28c2272bb1c8ba633349e73a66083ae3b68fabea203d1b7298e513`
   when the contract line is hashed without its terminal newline).  
   **Severity:** NONE.  
   **Prescribed repair:** none.

2. **Location:** v3.2 line 16, every binder, displayed definition, and
   definite noun phrase.  
   **Defect:** none. The opening universal binders cover the
   finite-dimensional exact-unit `epsilon_r`-C*-algebra datum, including
   its reserved `calU`, `calH`, `icalH`, `J`, `bold-dot`, and `dagger`
   notation, and `delta`. The family declaration binds `g` and its indexed
   maps; the new pointwise universal explicitly binds `V` and `A^par`;
   `the unique A^perp` binds the unique witness; and the displayed
   definition `f_V(A)=...` binds its argument `A`. The displayed
   `chi_V(A^par)=...` family definition and
   `calA_delta={chi_V}_{V in calU}` bind the chart arguments and index, and
   `every smooth embedded-manifold structure calM_delta` binds the smooth
   structure. Consequently “this displayed calA_delta,” “every displayed
   g_V and chi_V,” and their point values and differentials all have local
   antecedents.

   The displayed source, image target, and formula for `Pi_delta` bind
   `Pi_delta`, `S_delta`, and the formal arguments `(U,H)`. The typed map
   declaration binds `(u_delta,h_delta)`; the two new postfix universals
   explicitly scope the inverse identities over `X in S_delta` and
   `(U,H) in calU x B_delta^{calH}(J)`. The group-input premise explicitly
   scopes `U,V`, while the two displayed differential lambdas bind their
   own `(U,H)` and `X`. Thus “the open set,” “the displayed inverse,”
   “same displayed point values,” and “their displayed C^1 differentials”
   all refer to locally typed objects.

   Finally, the three `writing` clauses display and type
   `alpha_C1`, `mu_C1`, and `sigma_C1`, with their formal arguments bound
   by the displayed function definitions; the existential quantifier binds
   the smooth `alpha`, `mu`, and `sigma`; and the terminal explicit
   universal over `U,V in calU` and `c,d in U(1)` scopes the entire
   coordinated list introduced by “satisfy,” including the pointwise and
   covariance identities. The derivative identities are equalities of the
   already-bound maps. The remaining notation (`B`, `C^1`, `C^infinity`,
   `D`, `U(1)`, and `conj`) is standard typed notation, not a free
   variable. No occurrence depends on implicit universal closure, and no
   same-named object is imported across an opaque boundary without its
   contract-local typed witness.  
   **Severity:** NONE.  
   **Prescribed repair:** none.

3. **Location:** v3.2 lines 17–18 and its inherited v3.1 external list and
   12/18 elevation cap.  
   **Defect:** none. The two definitions still supply exactly the ambient
   algebra and approximate-unitary vocabulary. The five dependencies retain
   distinct appropriate roles:
   `lem-stage1-explicit-group-domain-membership` supplies the two typed
   inputs in `S_delta`; `lem-stage1-unitary-graph-control` supplies the
   displayed graph family and charts; `lem-stage1-polar-retraction`
   supplies the displayed diffeomorphism and its two-component inverse;
   `lem-stage1-smooth-unitary-atlas` supplies the smooth structure on those
   same graphs and charts; and `lem-stage1-smooth-polar-inverse` supplies
   the smooth upgrade of that same `Pi_delta` and inverse. The inherited
   external-registration list is exactly those two `defs:` followed by
   those five `deps:`; the inserted quantifiers introduce no new term or
   provider. They also add no proof branch or estimate, so the prior
   restriction/corestriction, composition, injectivity, covariance, and
   derivative-identification proof shape is unchanged. The target/hard
   live-node cap therefore remains appropriately 12/18.  
   **Severity:** NONE.  
   **Prescribed repair:** none.

VERDICT: LAND
