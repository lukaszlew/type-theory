# Review 7 - the results marked "here, unreviewed", the rewritten lemmas of §43 and §36, the reports of sources, and the status section

Reader: fresh, independent, had not seen the page. Read: `out/reading-copy.txt` (front, §1-§13, §22, §23, §31, §36, §37, §39, §43, §45, status, in full; the rest skimmed where a claim pointed there), `rules-research.md`, `rules-writing.md`, `reviews/review6.md`. Sources read for the checks: `vanbakel-survey.txt` (820-960, 1005-1255), `abd-cs0011039.txt` (55-108, 705-812, 843-856, 940-1002, 1250-1330), `abel-coquand.txt` (whole), `matthes.txt` (1536-1550, 5380-5420, 6615-6672, 6762-6780, 7478-7532, 7584-7765, 10610-10630, 10756-10764, and greps), `riba-values.txt` (26-60, 100-200, 270-326, 336-376, 428-447, 664-680, references), `geuvers94.txt` (606-640).

Method. Every result in the task list was re-derived by hand. The claims about particular terms were also run through `lam.py`; the script is `/tmp/claude-1000/-home-lew/6534068f-6359-5a93-aa5d-b162dbed9d2f/scratchpad/r7/chk.py` (outside the repo). It confirms: ω (in ω) with P = out is back at itself after 6 head steps; the predecessor of Mendler recursion reaches n after 9 head steps for three different n; the encoding of ∃ reaches t after 4 head steps; both runs of the iterator; (λb.u b) w_n is not in SN and (λc.I) (λb.u b) is in SN for n = 0, 1, 2. Nothing under `/home/lew/type-theory` was changed except this file.

Summary. All re-derived proofs are correct in their mathematics, with one exception of statement: the definition "a rule that keeps the term" in §45 does not fix the context, and with it the item "not derivable" is false as stated (A1). The other errors are overstatements around correct lemmas (A2-A5), a proof that uses more quoted facts than it lists (A6), reports of sources that say slightly more or less than the source (A7-A12), and a status section with one lemma in two lists and one claim under two statuses (A13). Counts: Part A 14, Part B 12, Part C 9.

---

## Part A - errors

### A1. §45, definition "A rule that keeps the term": the context is not fixed, and with that definition the item "not derivable" is false

Quoted: "A rule keeps the term if it concludes a judgment about a term from one or more judgments about the same term." and "Take the rules "variable", "→ in" and "→ out", and with them any rules that keep the term and are true ... Then no judgment Γ ⊢ (λc.I) (λb.x b) : F is derivable in which Γ gives x the type expression X."

Why it is wrong. The definition lets a rule change the context. The proof's fact about derivations, "If Γ ⊢ s v : F is derivable by the rules named, then Γ ⊢ v : A is derivable for some A", is proved by "if the last rule keeps the term, a judgment about s v is above it, and the induction applies". The induction then gives Γ′ ⊢ v : A for the context Γ′ of the judgment above, and the last paragraph needs "x : X in Γ".

Counterexample to the statement. The rule "from x : Z → Z′ ⊢ t : W → W conclude x : X ⊢ t : W → W, for t = (λc.I) (λb.x b)" concludes a judgment about a term from one judgment about the same term; it is true, because its conclusion is true by the item "true"; and its premise is derivable in System D (the lemma's own text: "typable in System D ... with x : Z → Z′"). So the judgment of the lemma is derivable. A natural true rule of the same kind, which does no damage to the conclusion but breaks the fact as stated: "from Γ, x:B ⊢ t : A conclude Γ ⊢ t : A" (true by the Base condition: x is replaced by itself).

Fix. "A rule keeps the term if it concludes a judgment Γ ⊢ t : B from one or more judgments Γ ⊢ t : A1, ..., Γ ⊢ t : An, with the same context and the same term." Every rule the page lists as keeping the term has that form, and the proof is then correct as written.

### A2. §45, both remarks: System D with subtyping is not complete for the simple semantics as the page defines it

Quoted (first remark): "Dezani, Honsell and Alessi show that ω is not needed for completeness: System D with a rule of subtyping ... is complete for the simple semantics too, over structures that need not be models of the whole λ-calculus." Quoted (closing remark): "The comparison can even be made with one system of rules: System D with the rule of subtyping is complete for the simple semantics, by the theorem of Dezani, Honsell and Alessi quoted in the first remark, and it is not complete for type sets, by the lemma."

Why it says more than the source. The page defined the simple semantics two sentences earlier over models "in which every term has a meaning and convertible terms have the same meaning", with "true if it holds in every model". For that semantics System D with subtyping is not complete: y : A ⊨ (λx.y) (δ δ) : A holds in every such model, and δ δ has no type expression without ω. The source's theorem (5.16) is relative to another class: Definition 5.7 takes "all ▽-good simple interpretation domains ... which moreover agree with Σ▽", and the paper says after the theorem that "the strict theories, which induce λv-models and λ-I-N-models, are complete for the corresponding classes of models", while only "natural theories, which induce λ-models, are ... complete also for the class of λ-models". A strict theory is one without Ω. So without ω completeness is bought by a wider class of structures, in which a step that discards its argument need not keep the meaning. That is the page's own point about ω, and the two sentences hide it.

Fix. First remark: "... is complete for the simple semantics taken over a wider class of structures, in which a step that discards an argument need not keep the meaning; over the models of the whole λ-calculus it is not, because (λx.y) Ω has there every type expression that y has." Closing remark: drop "The comparison can even be made with one system of rules ...", or say "complete for that wider class of structures, and not complete for type sets".

### A3. §45, opening and closing remark: "in any context", "in every context that declares the free variable"

Quoted: "System D is not such a system, in any context"; "it is there ... in every context that declares the free variable".

The lemma proves the failure for contexts that give x the type expression X, a variable. In the context x : Z → Z′ the judgment is derivable, as the lemma's text says. Fix: "even for a judgment whose context declares every free variable of the term"; "in a context that declares the free variable".

### A4. §31, table, row Predecessor: "or by recursion in Rec(F), for any F"

The lemma on Mendler recursion proves a predecessor only "For the F of the example "Mendler-style natural numbers"". For any F it is false: the proof of "No predecessor into F(R)" uses of the constructor only that it is in F(R) ⇒ R and that P applied to it gives the argument back, so it applies to in+ and R = Rec(F) with F(C) = C ⇒ T. Fix: "or by recursion in Rec(F), for the numbers; recursion itself for any F".

### A5. §39: "The derivation is the counterexample of Abel and Coquand, with the annotations erased"

The term is theirs erased; the derivation is not. Theirs: δ z = z ⊤ z : ⊤; ω h A = cast ⊤ A (h ⊤ A) δ, so δ is cast to a variable A and generalized, ω h : ⊥; then Ω h = δ (ω h), the uncast δ : ⊥ → ⊥ applied to the cast δ : ⊥. The page casts δ once to ⊤ → ⊥ (line 5) and applies the cast δ to the uncast one (line 6). Both are correct and erase to δ δ. Fix: "The term is that of the counterexample of Abel and Coquand with the annotations and the cast erased; the derivation is shorter than theirs, which casts δ to a variable, generalizes to ⊥ and applies δ to the result."

### A6. §45, lemma "Complete, for expansion-closed sets": the proof uses two facts beyond the three it lists as quoted

Quoted: "from three facts that the survey proves"; status section: "checked by the writer against the three facts of the survey that it uses".

The three facts are transcribed correctly (Lemma 4.4, lines four and five; Lemma 4.6; Theorem 4.10), and so are the grammar, ≤ and the four rules (Definitions 4.1, 4.3). The proof also uses:

1. Weakening (Lemma 4.5 with Γ′ ≤ Γ; the survey: "if Γ ⊆ Γ′, then Γ′ ≤ Γ"). Four places: the case ∧ of "every S′ names C(S′)" (n derivations over n finite parts of Γ∞ have to be put over one part before "∧ in"); "a member of C(S′ → A) sends C(S′) into C(A), by "→ out"" (two finite parts); "a finite part of Γ∞ that contains z:S′ derives s z : A" (the part that derives it need not contain z); and the end, where "a part of Γ" has to become Γ.
2. Lemma 4.2, line two (ω ≤ σ only if σ is ω), with an induction on the derivation, for "a variable with ω can only be given ω, which it has without being declared; so it can be removed too". "Parts" does not give this: the variable is free in the term.

Both are easy; neither is a hole in the mathematics. Fix: list them among the quoted facts ("Weakening", "ω alone") and write "five facts" in the lemma's note and in the status section.

### A7. §23, limit 4: "the set that every saturated set contains gets one more clause"

Geuvers's Definition 5.2 adds two clauses to the base terms: "5. If M ∈ B, then π1 M ∈ B and π2 M ∈ B" and "6. If M, N ∈ SN, the[n] Σv:M.N ∈ B". The page reports the first. The sixth review found the same under-report in §42 (its A8); this is its sibling in §23. Fix: "gets a clause for projections, a projection of one of its members is a member, and one for the new form of type expression, which is a term in his setting".

### A8. §36: "that is the head-closed collection in other words"

Quoted: "A footnote of his names a paper of McAllester, Kucan and Otth in which membership of a term is decided at the term its head steps end at; that is the head-closed collection in other words, and the paper was not read for this page."

Matthes's footnote 6 says: "instead of checking whether a term is in the predicate one checks whether its weak head normal form is in the predicate. The price to pay is that in some sense one has to calculate with equivalence classes modulo weak head reduction." That is one property. An identification with the collection HC (inside SN, containing Base, the closure condition) is a claim about a paper that was not read. Fix: "which, from the footnote alone, looks like the head-closed collection".

### A9. §36: "Riba proves that a reducibility candidate is determined by its values"; "hereditarily neutral"

The paper states it as "Lemma 3.7 ([16])", citing another paper of Riba's for the proof; the page says the same of Lemma 3.9 in §37 ("with a reference to another paper of his for the proof") and should say it here. The paper's name is "hereditary neutral terms"; the page writes "hereditarily neutral" as if quoting ("He calls the members ... the hereditarily neutral terms"), and the status section repeats it.

### A10. §22, item Encoding: "The statement is Riba's"

Riba calls the encoding usual ("the existential quantification is usually encoded as ∀Y.(∀X.T ⇒ Y) ⇒ Y") and proves that it and his ∃ (the closure of the union) have closed members both ways, with terms that use his let ("λy.λx.(let x = y in xz)"). The page's two terms, λx.λk. k x and λe. e I, and the count of four head steps are not his. Fix: "The encoding is the usual one. That it and the union have terms both ways is a statement of Riba's, for candidates and biorthogonals with his let; the two terms here and the proof for type sets were worked out here."

### A11. §31, note of the definition of the Mendler algebra: "the translation into System F"

Matthes translates his system MeIT−rec into "system eF", which is "F [extended] by the types 0, 1, pairs and ..." (his 2.2); eF is then embedded in F (his 2.2.6). The clause for μ and the constructor use only ∀ and →, as the page says. Fix: "into his system eF, an extension of System F that he embeds in System F".

### A12. §31, note of "The inductive part, at any fixed point": "where the same holds for the set he defines by its eliminations"

The quotation "µE(Φ) := any fixed point of ΨE" and the open problem are exact. But his ΨE is the operator of recursion (ME(M) has "(P → M) → (P → N) → Φ(P) → N"), which is the page's Ψ of the lemma on Mendler recursion, not G. So what "the same" is true of in the thesis is Rec(F), where the page takes "the least fixed point μΨ" and could take any. Fix: say so in the note ("for his operator, which is the Ψ of the lemma on Mendler recursion; the same holds there, and Rec(F) could be any fixed point of Ψ"), and add to the lemma on Mendler recursion that only Rec(F) = Ψ(Rec(F)) is used.

### A13. Status section: one lemma in two lists, one claim under two statuses, two stale phrases

1. "The lemma of §37 that test-defined sets are not closed under union, and the example after it; the six claims of its proof about particular terms were checked by a program." stands in the paragraph "Worked out for this page, and not reviewed", and the same lemma stands in the paragraph of re-derived results ("Re-derived by the reader of the sixth review ... the lemma of §37 that test-defined sets are not closed under union, with the example after it"). Its header says "here, reviewed". Remove the sentence from the unreviewed paragraph. "six claims": the proof now says "The four claims ... so was the fact, not used".
2. The example "What replaces the union" in §37 was extended after the sixth review (the report of Riba, and "What serves over TT ... is the encoding of §22: ... it is test-defined if the sets F(C) are"). The reviewed list still says "with the example after it". The new sentences are correct (E is built from ⇒ and ⋂ over TT, and the item arrow and intersection applies; the way into E does not use the union), but they are unreviewed and listed nowhere except under "The corrections made ... after that review".
3. "The two claims about subject reduction in §23" is under "From general knowledge, and not checked against sources", and "The example in §23 of a step that loses a type expression, from Riba's paper" is under "From the listed sources". The second of the two claims is now quoted, with Riba's Example 2.1 reproduced exactly. Say "The claim in §23 that subject reduction holds for System F".
4. The errata paragraph on the sixth review is accurate in every item it lists (checked against A1-A10, A13, A14 and B1 of `review6.md`). It leaves out two findings of that review: A11 (two departures from Matthews's guide in §37) and A12 (the qualification on subject reduction in §42). If they were fixed, list them; if not, they are open.

### A14. Front, "What here is not in the textbooks": the characterization of candidates

Quoted: "Worked out for the page ... the characterization of Girard's candidates as the type sets closed under steps". Matthes states it: "Girard's candidates are nothing but saturated sets which are closed under reduction" (footnote 8; "It is possible to show", no proof). The status section credits "the sentence on candidates in §35" to him. The front should say "the proof of" the characterization, as it says "a two-line proof of Riba's theorem".

### Quotations and reports checked and found accurate

Van Bakel: Definition 4.1 (grammar, ω as the empty intersection, the three clauses of ≤), Definition 4.3 (four rules, n ≥ 0), Lemma 4.4, Lemma 4.6, Theorem 4.10; the quotation "is used to type those sub-terms that disappear during reduction, and that cannot be typed from the current context" (line 587); Property 3.15; "the mere introduction of a relation ... with contra-variance in the arrow would have done the trick"; the three readings of the arrow (Definition 3.13). Dezani, Honsell and Alessi: Proposition 5.11 with the example x : (A → B) ∩ (A → C); the three semantics by functionality set; Hindley and the simple types (section 6 and the introduction). Abel and Coquand: the cast and its step; "Consistency and canonicity is not at stake"; equality reflection; the second term with tautext; strict propositions, Gilbert's result for the predicative case and open problem (1); Girard's J in §18. Matthes: line 1543 on van Raamsdonk and Severi and Loader; the clause (µ) and (µ-I), whose erasure is the term that in u reaches by one head step; the names elimination-based and introduction-based, the extracted type, the encoded constructor as the proof of the inclusion, the open question on embeddings; "any fixed point of ΨE", MI⊇ and the least fixed point; Lemma 9.44, whose term s (λy.y) (λx. x E s) t is in+ after two head steps; the argument with π = µα.α → 1, ω = λx.P x x; the open problem quoted; footnote 9; "extended induction ... motivates primitive recursion" (line 331); "upper monotonization" (line 424). Riba: the three kinds of reducibility families and [13] Parigot; orthogonal and biorthogonal for contexts; Lemma 3.9; "their lattice is not distributive"; ∃ as the closure of the union, (∃ I) valid in every family, "We only know that it is validated by reducibility families which are closed under unions", "closure under unions is not possible for all rewrite relations", the let; Example 2.1 from [18] Tatsuta, reproduced exactly in §23; values and elimination contexts in limit 4. Geuvers: Definition 5.2 clause 5, the key redex under a projection, Definition 5.3.

---

## Part B - rule violations (new or changed text)

1. Rule 1. `t` is a term everywhere and a term variable in the proof of the item cast in §39 ("Let Γ be h : X ≐ Y, t : X ... replace t by I"). Use x.
2. Rule 1. `ω` is the type expression of §19 and §45 and a term in §31 ("Let ω = λx. P x x"). Rename the term.
3. Rule 1. `F` is a function from type sets to type sets on the whole page, a variable of kind ∗ → ∗ in §39 ("∀F:∗→∗. F A → F B"), and a type expression in §45 ("Γ ⊢ s v : F"). Rename the last two.
4. Rule 1. In §31 the lemma on the iterator writes "it z s (λz.λs.z) reaches z": the same letters are the free variables of A and B and the bound variables of the numeral.
5. Rule 3. "So nothing in the two lemmas before this one uses ..." (§31); "by the first paragraph of the proof" (§45, closing remark; the helper has no name: give it one, for instance "applied to a variable, converse"); "quoted in the first remark" (§45); "The head steps are one for λz and the two of in" (§31, Mendler recursion: the constructor there is in+).
6. Rule 7. §45, the frame "Expansion-closed set, and the essential system" holds two definitions, a grammar, a relation and three claims ("The empty set and the set of all terms are expansion-closed, and no type set is ..."). The lemma after it defines truth for the new reading inside its statement ("call a judgment true as in §12, with members put for the variables of the context").
7. Rule 6. §45, lemma on expansion-closed sets: not said whether the term may have free variables outside the context (it may; the proof handles them by ω), and not said that an assignment may send a variable to the empty set (the remark before says it for the other semantics). §45, definition of a rule that keeps the term: the context (A1). §31, "No predecessor": x not free in P.
8. Rule 6 and 11. §22: "For monotone F:" governs "t ∈ μF if and only if t ∈ F(μF)" and extended induction, and not "Induction: if F(C) ⊆ C then μF ⊆ C", which holds for every F and which the lemma on the iterator and the item greatest use in that generality. The sixth review said this (its B12); it is still so.
9. Rule 11. §22, item Greatest carries no status in its text; the status section lists it as unreviewed. §45, lemma on expansion-closed sets: "from three facts" (A6).
10. Rule 13. §45 uses "convertible" for terms in the fact Conversion, and "System D", without §19 or §30 being named at the place (§30 is in the Uses line; §19 only through §21).
11. Rule 12. §45, "True implies derivable": "Under it every S′ names C(S′), by induction on S′" skips the case of a variable (by the choice of ρ) and the uses of weakening (A6).
12. Rule 18. The departures from review 6 that the errata does not list (A13, point 4).

---

## Part C - correct, and could be simpler or more precise

1. §45, "no true part". The split into a variable and an arrow needs "C1 ∧ C2 true implies C1 true" only; say that ∧ names ∩ in System D. The count "n is the number of arrows in B" works; "at most m arrows" in the induction is for every m at once (the induction is on A′, with m universally quantified). Say so.
2. §45, helper. "replacing a variable by a variable neither creates nor removes a redex" is also right if b is free in s; one clause would stop the reader from checking.
3. §45, closing remark. The rule "from Γ ⊢ t : A conclude Γ ⊢ λb.t b : ∃Z.Z" is true and derives the judgment (c : ∃Z.Z ⊢ I : W → W, "→ in", "→ out"). It leaves the type expressions of System D; say so, since the lemma is stated "for the type expressions of System D".
4. §31, "the greatest". "contains Min, which is inside every type set" uses that G(Min) is a type set; the item type set of the lemma for any F gives it. One reference.
5. §31, iterator. "The term it z s n reaches it by three safe head steps, so it z s n ∈ C, and abstract, three times" - abstract alone gives the claim from n A B B ∈ C; the head steps are not needed. And the proof should say where it uses that F is monotone: only for μF to be a fixed point, which the item member does not use; "μF ⊆ X" needs F(X) ⊆ X alone.
6. §31, Mendler recursion, item fixed point: "because a larger input set gives a smaller arrow, and so Ψ(M) ⊆ Ψ(M′), for the same reason" - three inclusions, two reversals; write the three lines.
7. §39, item cast and SN. A reader may ask why line 4 is allowed: "∀ out twice" at X := ⊤ and Y := ⊤ → ⊥. Say it. The conclusion "no semantics that proves C1 can make the cast true" needs "and the rules of Fω true"; add it, as §30 does for β with φ.
8. §22, item Greatest: "every type set C with C ⊆ F(C) is inside νF" holds for every F, by the definition; the sentence reads as if it needed monotone.
9. §43. The rewritten lemma is correct. In the case "∀ in" the remark "holds for Γ° if it holds for Γ" is the direction needed; the other direction fails (a family variable can be free in Γ only inside the A of a ∀x:A.B, which the reading drops), and a clause saying so would explain why the sentence is one-directional.

---

## Verdicts on the re-derived results

1. §45, "Complete, for expansion-closed sets". Correct as stated. The system and the three facts are transcribed correctly from the survey. Both directions hold; the infinite context is handled correctly (every S given to infinitely many variables, finite parts), variables outside the context are handled correctly (ω in Γ∞, removed at the end), and ω is the set of all terms in both the n = 0 cases. The proof uses weakening and "ω ≤ σ only if σ is ω" without listing them (A6).
2. §45, "True, and not derivable by rules that keep the term". Items true and no true part: correct as stated and proved; the helper is correct; w_m and u check by hand and by program. Item not derivable: false as stated, because the definition of a rule that keeps the term does not fix the context (A1); correct, with the proof given, once it does. The closing remark's rule is true and derives the judgment. The remark "Where completeness holds" is accurate except A2; the two "in every context" phrases overstate (A3).
3. §31. "The inductive part, at any fixed point": both items correct; the split of the open question is exact. "No predecessor into F(R)": correct; six head steps with P = out confirmed. "Mendler recursion, for any F": all four items correct; three and nine head steps confirmed by hand and by program. "An iterator over the least fixed point": both items correct; X is a type set, F(X) ⊆ X holds with D = E ⇒ C, and μF ⊆ X needs nothing more. "The inductive part, for any F" with the strengthened in: correct. The table overstates the predecessor (A4).
4. §39, "Equality of type expressions, and the cast". All four items correct; the six lines are a derivation. It is not Abel and Coquand's derivation (A5).
5. §22. Item Encoding: correct, four head steps confirmed; attribution A10. Item Greatest: correct. Extended induction: correct.
6. §43, the forgetful reading and the lemma. Correct after the rewrite: four facts, every rule case, the corollaries, "not the equality" and "what is forgotten". No error introduced.
7. §36, "The arrow generated by abstractions" and the lemma. Correct after the restructuring: all four items, and the example I ∈ SN ⇒ U, I ∉ SN ⇒I U.

Status section: lists every result that is marked unreviewed in a header, and the closing remark of §45. It lists one reviewed lemma also as unreviewed, has one claim under two statuses, and its errata for the sixth review omit two findings (A13). It claims nothing as reviewed that I found wrong, except that the extended example of §37 is covered by "with the example after it" (A13, point 2).

No restructuring is proposed.
