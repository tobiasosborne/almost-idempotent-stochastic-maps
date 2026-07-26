---
id: lem-routef-ai-defect-linearization
kind: lemma
contract: Approximate-algebra defect linearization: set C_theta=12*(sqrt(2)-1). There are universal C_A < infinity and eta_A > 0, with C_A=20+(211/8)*C_theta, such that for every nonzero Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta satisfying 0 <= eta <= eta_A and ||Phi^2-Phi||_cb <= eta, if tilde-Phi=(1/2)*(I+(2*Phi-I)*(I-4*(Phi-Phi^2))^(-1/2)), A=Im(tilde-Phi), X star Y=tilde-Phi(XY), r=(3/2)*((1-4*eta)^(-1/2)-1), and epsilon_AI(eta)=max{r,20*eta+2*((1+r)^5-1),3*r-r^2}, then the inherited operator-space norms, involution, and unit together with star make A an extended epsilon_AI(eta)-C*-algebra and epsilon_AI(eta) <= C_A*eta.
defs: def-almost-idempotent; def-extended-epsilon-cstar-algebra
deps: lem-kitaev-almost-idemp-audit; lem-routef-functional-calculus-closeness
status: proved
af: validated
provenance: LEDGER-W74F-G-K.md §1.1 (1.1); VERDICT-W74F-G-KLEDGER.md Symbol table and checks 2-4; DESIGN-FUDW-DECOMP-v3.md §2.5; VERDICT-FUDW-DECOMP-V3.md §D
owner: A
workspace: proofs/lem-routef-ai-defect-linearization
---

**Status.** af-VALIDATED in-repo (2026-07-26): 13-node tree, taint clean,
fresh-codex prover/verifier protocol (§6). BANKING NOTE (user-ratified option
2026-07-26): the prover expanded the seeded one-line contract into a
self-contained root statement (inlining C_theta's value and the tilde-Phi
formula from its imported deps); the fresh verifiers validated THAT statement,
so the registry contract was mechanically replaced by the validated root
VERBATIM at banking — no orchestrator judgment of equivalence was exercised;
the linker/oracle contract-match refusals that forced this reconciliation are
the 8d0a5061 banking-time precedent. Export in
`proofs/lem-routef-ai-defect-linearization/export.md`; oracle registered.
L0-rigorous.

**Provenance.** `LEDGER-W74F-G-K.md` §1.1 and
`VERDICT-W74F-G-KLEDGER.md` symbol-table audit; detached-leaf authorization
in `VERDICT-FUDW-DECOMP-V3.md` §D.
