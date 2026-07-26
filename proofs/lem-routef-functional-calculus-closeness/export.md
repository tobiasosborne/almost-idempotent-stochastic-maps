# Proof Export

## Node 1

**Statement:** Functional-calculus closeness: for 0 <= eta <= 1/8, the exact functional-calculus projector satisfies ||tilde-Phi-Phi||_cb <= C_theta*eta, where C_theta=12*(sqrt(2)-1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Under the root hypotheses, with Delta:=Phi-Phi^2 and T:=2Phi-I in the unital Banach algebra CB(B(H)) (product = composition), the formula for tilde-Phi supplied by lem-kitaev-almost-idemp-audit satisfies ||tilde-Phi-Phi||_cb <= (3/2)*((1-4*eta)^(-1/2)-1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** If Phi:B(H)->B(H) is UCP, then ||Phi||_cb=1; consequently, for T=2Phi-I, the triangle inequality gives ||T||_cb <= 2||Phi||_cb+||I||_cb=3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.1.1

**Statement:** For every amplification m and every X, complete positivity and unitality give the Kadison-Schwarz estimate Phi_m(X)^*Phi_m(X) <= Phi_m(X^*X): indeed [[X^*X,X^*],[X,I]]=[X^*;I][X,I] is positive, applying the positive unital map Phi_(2m) gives [[Phi_m(X^*X),Phi_m(X)^*],[Phi_m(X),I]] >= 0, and its Schur complement is the displayed estimate. Since 0 <= X^*X <= ||X||^2 I, positivity and unitality then give Phi_m(X^*X) <= ||X||^2 I, hence ||Phi_m(X)|| <= ||X||. Thus ||Phi||_cb <= 1, while Phi(I)=I gives equality; also ||I||_cb=1, so ||2Phi-I||_cb <= 3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** Using exactly the projector formula from lem-kitaev-almost-idemp-audit and Phi=(I+T)/2, one has the algebraic identity tilde-Phi-Phi=(1/2)*T*((I-4Delta)^(-1/2)-I), where Delta=Phi-Phi^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.3

**Statement:** If ||Delta||_cb <= eta <= 1/8, then the inverse square root in that formula obeys ||(I-4Delta)^(-1/2)-I||_cb <= (1-4eta)^(-1/2)-1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.1.3.1

**Statement:** In the unital Banach algebra CB(B(H)), ||4Delta||_cb <= 4eta <= 1/2 < 1. Therefore the holomorphic inverse-square-root branch at I agrees with the absolutely norm-convergent binomial series (I-4Delta)^(-1/2)=sum_(n>=0) c_n(4Delta)^n, where c_n=binom(2n,n)/4^n >= 0 and sum_(n>=0)c_n x^n=(1-x)^(-1/2) for |x|<1. Subtracting I and using the triangle inequality and submultiplicativity gives ||(I-4Delta)^(-1/2)-I||_cb <= sum_(n>=1)c_n(4||Delta||_cb)^n <= sum_(n>=1)c_n(4eta)^n=(1-4eta)^(-1/2)-1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** For every real eta with 0 <= eta <= 1/8, (3/2)*((1-4*eta)^(-1/2)-1) <= 12*(sqrt(2)-1)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Put t:=4eta. For 0 <= t <= 1/2 one has (1-t)^(-1/2)-1 <= 2*(sqrt(2)-1)*t.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

##### Node 1.2.1.1

**Statement:** At t=0 the inequality is equality. If 0<t<=1/2 and s:=sqrt(1-t), then s>=1/sqrt(2) and rationalization gives ((1-t)^(-1/2)-1)/t=1/(s*(1+s)) <= 1/((1/sqrt(2))*(1+1/sqrt(2)))=2/(sqrt(2)+1)=2*(sqrt(2)-1); multiplying by t proves the claim.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** Substituting t=4eta into the preceding inequality and multiplying by 3/2 yields (3/2)*((1-4eta)^(-1/2)-1) <= 12*(sqrt(2)-1)*eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

