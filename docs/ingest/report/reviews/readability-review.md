I read only `report/main.tex` and `report/sections/*.tex`, in order. I did not read project notes.

1. `report/main.tex:110`: compiled abstract is still a TODO: “Abstract stub.”  
Fix: replace with the real abstract or remove the duplicate document-level abstract.

2. `01:109-130`, `09:103-139`, `10:7-30`, `11:31-36`: the report depends on external ledger/notes/scripts while claiming self-containment.  
Fix: include exact statements, certificates, data tables, and proof sketches in the report, or mark them as external assumptions.

3. `02:24-27` vs `06:16-18`, `10:16-18`, `99:35`: canonical separator is inconsistent: first `sup_{C_W} phi=0`, later “vanishes on `C_W`” / “zero on `C_W`.”  
Fix: use the supporting-functional definition everywhere: `phi <= 0` on `C_W`, `sup_{C_W} phi=0`, `phi(p_v)=H`.

4. `01:109-130`, `04:31-42`: imported equivalence and cluster theorem are not self-contained: no hypotheses, constants, norm, threshold, or proof route.  
Fix: state precise black-box theorem forms with all constants/norms used by later reductions.

5. `03:39-45`, `04:44-57`, `99:127`: `op-exposed-hull` is never defined beyond “global exposed-hull problem.”  
Fix: add a formal problem statement before using it in the chain.

6. `04:48-55`: “verified two-family assembly,” “large-height threshold,” and `A_HLC` appear without definition.  
Fix: define the assembly theorem and threshold constant, or delete the constant formula.

7. `02:80-86`, `07:19-45`: LP dual variables are introduced without deriving the primal/dual or explaining `alpha,beta,gamma` operationally.  
Fix: add the primal LP in standard form and one dual derivation.

8. `04:111-114`, `08:74-75`: `Omega_g <= 2+4delta` is used as a load-bearing estimate without proof or citation.  
Fix: prove it once immediately after defining `g`, or cite a numbered lemma.

9. `03:106-110`, `02:146-157`, `04:161-168`, `10:114-120`, `99:167`: pushed-witness cleanup has conflicting statuses: mod-audit, refuted, proved dead end, downgraded.  
Fix: choose one status label and use it consistently.

10. `03:98-105`, `07:167-172`, `08:132-139`, `10:79-86`, `99:95`: all-shallow faces are mod-audit/downgraded/open depending on section.  
Fix: split “existence certificate” from “general exclusion” and assign statuses separately.

11. `02:139-141`: the report starts with state set `{1,...,n}` but the example uses `W={0,1,2}`, hidden vertices `3,4`.  
Fix: use one-based indices or explicitly switch conventions.

12. `07:109-113`, `99:49`: bare `sigma'` / `sigma` violates the report’s own sigma audit.  
Fix: write `sigma_T` for generic carrier mass and `sigma_v^{off}` or `tilde sigma_v` for branch variables.

13. `08:80-86`: “not the older index-based `sigma_v^{off}`” conflates two different wrong quantities.  
Fix: distinguish formal off-own-site mass, index-not-in-`W` proxy, and geometric non-`C_W` mass.

14. `10:63-68`: “`R`-handling bug” reintroduces the forbidden bare `R` language.  
Fix: say `Omega_g`-handling bug.

15. `05:22-40`: finite corner theorem assumes “corner family laws recorded in campaign notes.”  
Fix: define the family and prove or state the family laws inside the section.

16. `05:78-103`, `09:58-98`: numerical campaign rows use unexplained terms: “MRP,” “frame-financing,” “pin/neg/epi,” “financier law.”  
Fix: add a compact campaign glossary before the table or remove nicknames.

17. `09:103-139`: reproducibility table points into `notes/...` and says artifacts may not be report inputs.  
Fix: include the relevant artifact hashes/tables/certificates in an appendix.

18. `08:123-129`: “two-site mutual carrying,” “two-ball cycles,” “return-mass inequality,” and “skinny spread-mass” are not defined.  
Fix: give formal definitions before the proposition.

19. `00:27-37`, `08:180-185`, `99:128`: quantitative Baake--Sumner stability remains circular: “desired signed stability excluding shallow hidden webs.”  
Fix: state the exact `delta=0` theorem and the desired perturbative theorem.

20. `99:118`: glossary says “height collapse” is `H <= delta Omega_g/(1-s)`, conflicting with the repeated proved cap `H <= 2(1+2delta) max(sigtilde,nu_v)`.  
Fix: reconcile or delete the obsolete formula.

21. `06:29-83`, `06:104-145`: day-1/fable tables list many named lemmas without hypotheses or proofs.  
Fix: either state each lemma formally or demote the section to “historical inventory.”

22. `07:53-124`: abbreviations `RF`, `ND'`, `SF`, `FC`, `CPL`, `MC`, `RW`, `WL` are hostile to a new reader.  
Fix: expand each acronym in the lemma title and glossary.

23. `06:16-19`, `10:16-19`, `99:35`: “canonical separator” is repeatedly stronger than what convex separation gives.  
Fix: audit every separator sentence after fixing item 3.

24. `00:68-75`: roadmap promises consumed main-project inputs justify the signed model, but Section 01 only asserts them.  
Fix: make the roadmap say these are black-box assumptions unless their proofs are included.

25. `00:99-115`: roadmap promises the “audited belt” and “wave-5--9” machinery, but Sections 06-07 mostly deliver ledger summaries.  
Fix: relabel these as inventories or add full arguments.

Overall verdict: the report is useful as an internal campaign map, but it is not self-contained for the advertised reader. A basic linear-algebra/Markov-chain reader can follow the broad narrative: stochastic problem -> signed idempotents -> exposed hull -> HLC -> DMF/web residual. They cannot reliably verify the chain, constants, statuses, or final obstruction without external notes and project lore. My estimate: `P(reader can follow the main chain as mathematics, not just a story) = 0.25`.