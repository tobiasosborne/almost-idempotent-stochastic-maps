# Proof Export

## Node 1

**Statement:** After first fixing one global witness package W_RF supplied by lem-routef-raw-factor-setting-formation, for every input (H,Phi,eta) to which that formation result applies, fix one def-routef-raw-factor-setting datum S over that same W_RF supplied by the same result, writing the fields of (W_RF,S) as the unqualified symbols below: Raw factor-map identities: for 0 <= eta <= rho_id^corr := min{rho_theta, rho_AI, epsilon_E/C_A}, tilde-Delta tilde-Upsilon = tilde-Phi and tilde-Upsilon tilde-Delta = I_B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Formation instantiation and retained identities: invoke lem-routef-raw-factor-setting-formation once to fix its single global scalar header W_RF. For an arbitrary input (H,Phi,eta) to which that result applies (in particular 0 <= eta <= rho_id^corr and the stated cb-defect hypothesis), choose the supplied datum S over this same W_RF. Then, with the notation of def-routef-raw-factor-setting, A=Im(tilde-Phi), u=v^(-1), tilde-Phi^2=tilde-Phi, tilde-Delta=iota_{A subseteq B(H)} o v, and tilde-Upsilon=u o tilde-Phi.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** First raw factor identity: for every datum S fixed by the preceding formation step, tilde-Delta o tilde-Upsilon = tilde-Phi as maps B(H)->B(H).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Pointwise expansion: for each x in B(H), (tilde-Delta o tilde-Upsilon)(x)=iota_{A subseteq B(H)}(v(u(tilde-Phi(x)))), by the two defining composition formulas in def-routef-raw-factor-setting.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Inverse cancellation in the correctly typed space: tilde-Phi(x) lies in A=Im(tilde-Phi), and u=v^(-1) from lem-routef-raw-factor-setting-formation entails v o u=I_A; hence iota_{A subseteq B(H)}(v(u(tilde-Phi(x))))=iota_{A subseteq B(H)}(tilde-Phi(x))=tilde-Phi(x).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** Map extensionality: the equality in the preceding two steps holds for every x in B(H), so tilde-Delta o tilde-Upsilon and tilde-Phi are equal as maps B(H)->B(H).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Second raw factor identity: for every datum S fixed by the preceding formation step, tilde-Upsilon o tilde-Delta = I_B as maps B->B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Pointwise expansion: for each b in B, (tilde-Upsilon o tilde-Delta)(b)=u(tilde-Phi(iota_{A subseteq B(H)}(v(b)))), by the two defining composition formulas in def-routef-raw-factor-setting.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.2

**Statement:** Projection-on-range fact: if a lies in A=Im(tilde-Phi), choose x in B(H) with a=tilde-Phi(x); then tilde-Phi(a)=tilde-Phi(tilde-Phi(x))=tilde-Phi(x)=a by tilde-Phi^2=tilde-Phi from lem-routef-raw-factor-setting-formation. Thus tilde-Phi restricted to A is I_A (with the canonical inclusion into B(H) understood).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.3

**Statement:** Apply the projection-on-range fact to v(b) in A: tilde-Phi(iota_{A subseteq B(H)}(v(b)))=v(b), so the pointwise expression becomes u(v(b))=b because u=v^(-1) from lem-routef-raw-factor-setting-formation entails u o v=I_B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.4

**Statement:** Map extensionality: the equality (tilde-Upsilon o tilde-Delta)(b)=b holds for every b in B, so tilde-Upsilon o tilde-Delta=I_B as maps B->B.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

