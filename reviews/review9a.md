# Review 9a - §38 and §39 after the rewrite, and the remark of §31 on a recursive type without positivity

Reader: fresh, independent, had not seen the page. Written 2026-11-10 (PST).

Read: `out/reading-copy.txt` (the copy of 21:18 PST, 4134 lines; unchanged while this review ran): lines 1-1175 (front, contents, §1 to §13), §23 limits 2 to 4, §31 from the lemma "No predecessor into F(R), for an F that is not monotone" to the remark after it, the lemma "Head steps commute with other steps" of §36, §37 in full, §38 and §39 in full and twice, the status section and the list of sources; `rules-research.md`, `rules-writing.md`; `src/classical.html` for the frames and subscripts of the definitions and of the theorem; the Uses entries in `plan.py` and the table of registered mentions in `build.py`. Sources (pdftotext output, read as data): `pdf/L7/vanbakel-sn-lambdamu.txt` (all), `pdf/L7/nour-saber-completeness-lambdamu.txt` (1-420), `pdf/L7/nour-realizability-lambdamu.txt` (1-1420), `pdf/L7/matthes-stabilization.txt` (1-140, 296-312, 396-410, 520-545, 762-812, 862-890, 1015-1025, 1380-1445, and the two entries for Parigot), `pdf/L7/david-nour-short-sn.txt` (1-200), `pdf/L7/irif-classicalded.txt` (1-60, 600-836), `pdf/L11/appel-mcallester-tr629.txt` (1-470). `reviews/review8a.md` was read after my own view of the two sections was formed, and then `review8a-scratch/sec38-39.txt` (the form of the two sections that review 8a read) to see what is new.

Quotations from the page are verbatim, except that typographic quotation marks and apostrophes are written in ASCII. Quotations from the sources are verbatim, with words that the text files break across lines joined and the spacing inside formulas normalised. "Line" with a file name means a line of that file.

Method. Everything marked "here, unreviewed" in §38 and §39 was re-derived by hand, line by line, and so was the first paragraph of the remark of §31. Claims about particular terms, the identities of Lemma R, the item names, the two claims of the proof that T1 is closed under steps, and the recipe of "closed terms fail" were also run by program, as extra evidence. My scripts are in `/home/lew/agent/tt-papers/review9a-scratch/` (`r9_common.py`, `r9_sec38.py`, `r9_sec39.py`, `r9_t1.py`, `r9_sound.py`); they use the writer's evaluator `scratch-L7c/lmu.py` for steps, and their own code for appending a list in one pass, for the replacement of §39, for putting a name for a free name, and for the enumerations. Nothing under `page-L7` was touched except this file.

## Summary

All results of §38 and §39 that carry "here, unreviewed" are correct as stated. Their proofs are correct, with one clause missing in the case of the rule μ (A1); the theorem is not affected. The new proof that T1 is closed under steps is correct; I could not break it by hand or by program. The proof of "closed terms fail" in its new wording is correct, and so is its worked instance. The first paragraph of the remark of §31 is correct; it is limit 2 of §23 with a second set (C7).

What is wrong is around the results: three sentences outside §39 still make the claim that review 8a had removed from §39 (A2); one sentence of the report of Appel and McAllester says something the report does not (A3); one credit is wrong (A4); one sentence of §38 is false as it stands (A5). The status section has no record of the eighth review (B1).

Review 8a: of its 35 findings, 25 are applied (four of them with a small slip that Parts A to C list), 9 are applied in part, and 1 is left out by a choice that the page names; none is applied wrongly in substance. The table is near the end.

Counts: Part A 5, Part B 10, Part C 13.

## Verdicts, one line per re-derived result

§38.

- Definition of appending in one pass, with its clauses and the μ step: well defined; the conventions on bound names are enough; correct.
- Note on appending a list: correct under its hypothesis (α not free in v1). The sentence after it, "Without that condition the two differ", is false as it stands (A5). The note is stated for two terms and used for n (B6).
- Lemma R, steps kept, both halves, for appending and for substitution: correct as stated and proved. Each of the four identities holds under the hypothesis stated, by induction on c, which I went through case by case. The hypotheses are used in the case [α]r of the first (x not free in u), in the case [α]r of the second (γ not free in u), in the cases x and y of the third, and in the case x of the fourth (γ not free in u). They are needed: the first fails for c = μδ.[α]x, w = y, u = x; the second fails if γ is free in u.
- Lemma R, names: correct as stated and proved. The converse holds as well (C3).
- Lemma R, R1 and R2, under μ, R3 of either sort: correct as stated and proved. For the μ head step the only redex that is not inside t, u or an argument is the head redex, so the case analysis of the proof is complete.
- Example "Three runs": correct.

§39.

- Definition "Replacing variables and names at once": well defined; one pass is needed, as the note says (a member or a test may have a name of Δ free). Correct.
- Definition of a true judgment: correct; every case of the soundness proof uses it as stated.
- Example "One judgment, with its replacement": correct; the replacement is μγ.[α](u v⃗).
- Lemma "What carries over": operations, tests, against a test: correct as stated and proved (n = 0 included).
- Lemma on the μ condition, tests suffice: correct.
- Lemma on the μ condition, not the smallest: correct. T0 is cl(Base), every type set contains it, and μα.[α]x passes every test and is not in it.
- Lemma on the μ condition, not only tests: correct as stated and proved. T1 is a type set, has the μ condition, is closed under steps and is not test-defined.
- Lemma on the μ condition, operations: correct.
- Lemma "Closed λμ-terms fail a test", both items, and the worked instance: correct as stated and proved.
- Example "Peirce's law" and example "The proof of Peirce's law fails a test": correct.
- Theorem, soundness: true. The five rules of §13 are proved as written. The case of the rule μ is correct once α′ is also kept apart from the names of Δ (A1).
- Theorem, C1 (strong normalization): correct.
- Theorem, C2 (consistency): correct; the lemma it uses now stands before it.
- Theorem, not over all type sets: correct.
- Paragraph on μα.I: correct.

§31.

- Remark, first paragraph (no type sets R and T with R = R ⇒ T): correct. Both inclusions are used: R ⊆ R ⇒ T gives u u ∈ T, and R ⇒ T ⊆ R gives δ ∈ R.
- Remark, second paragraph: the quotation is verbatim; the report is right except for one sentence (A3) and one imprecision (C7).

How I tried to break the proof that T1 is closed under steps. (i) A step inside the argument of a head redex whose argument is thrown away: then s′ is s, and "zero or more steps" covers it. (ii) The same with the argument copied: s reaches s′ by one step in each copy. (iii) A μ head step with the other step inside the body, inside the argument, inside a later argument: the term after the head step of t′ is reached from s by the item steps kept, in one step, in zero or more steps, in one step. (iv) A step t → t′ that is not the head step and gives the same term as the head step, as in I (I y): the proof splits by the term ("t′ is s"), not by the step, so the case is covered. (v) A term whose head steps end at a μ-abstraction that a later step turns into something else: with β and μ only, every step of μα.[β]b is inside b, so the form stays; this is the place where the rule that removes a μ would break the proof, and the page leaves that rule out. (vi) The induction: the terms on the way from s to s′ are reducts of s, so their longest runs are shorter than that of t; the induction hypothesis applies to each. By program: no failure of either claim on all 6,259 steps of the 35,878 terms with at most 7 symbols, nor on 18,356 steps of 6,000 random strongly normalizing terms with 8 to 16 symbols that have a head step (12,252 cases of the first claim; the head step is a μ step in 5,814 of them; the other step is inside the argument of the head redex in 6,160, and the argument is thrown away in 2,036 of those).

---

## Part A - errors

### A1. §39, soundness, the rule μ: the new name α′ has to be kept apart from the names of Δ as well

Quoted (proof): "Choose a name α′ that is not free in t, in the terms put in, or in the terms of v⃗; write t′ for t with α′ put for every free α, and β′ for β, or for α′ if β is α. Then (μα.[β]t)* is m = μα′.([β′]t′)*".

Quoted (note on the rules): "A name context may list names that are not free in the term, as a context may list variables that are not."

Why it is a gap. The three conditions on α′ allow a name of Δ′ that is not free in t. For such a choice the formula for m is wrong: the replacement written * appends the test of that name at [α′] inside the named term [β′]t′, where the name α′ is free, while in (μα.[β]t)* the name is bound and nothing is appended.

Instance. Above the line: y : X ⊢ y : X | α:X, γ:Y, by the variable rule. Below it, with β the name α: y : X ⊢ μα.[α]y : X | γ:Y. Send X to SN and Y to the set of the terms that pass the one-term test z; give y the member y, give γ the test z, and let v⃗ be the empty test. The name γ is not free in t = y, in the terms put in, or in v⃗, so the sentence allows α′ = γ. Then μα′.([β′]t′)* is μγ.[γ](y z), and (μα.[α]y)* is μα.[α]y. The next step fails with it: r′ is y z and r is y, and r is not r′ with α put for γ (`r9_sound.py`, last check).

Fix. One clause: "Choose a name α′ that is not a name of Δ and is not free in t, in the terms put in, or in the terms of v⃗". With it the case is correct: I followed it for β different from α (r′ is t′*[α′⇐v⃗] followed by the test of β) and for β = α (r′ is t′*[α′⇐v⃗] v⃗), and in both r is r′ with α put for every free α′. Twenty instances agree, among them instances with the name α free in the member, in the test, and in both (`r9_sound.py`). See also C2 for the one equality that the proof asserts and does not show.

### A2. Three sentences outside §39 still say that the rule needs the sets defined by tests, or that only they can do it

Review 8a (its A5) had "what a set must have" and "turns out to need a fourth" changed, in §39 and in §23, to what is proved: the μ condition is enough. §39 now says "Whether a weaker fourth condition would do was not examined", and its item not only tests gives a type set with the μ condition that is not test-defined. Three sentences elsewhere were not changed with them.

(a) §37, remark "What tests are for": "§39 is where sets given by tests do something that other type sets cannot: for the terms of Parigot's λμ-calculus a name stands for a test, the rule that makes a μ-abstraction is false over all type sets, and it is true over the sets defined by tests." The first clause is false as it stands: T1 is a type set that is not given by tests, it is a member of MU, and the rule is true over MU.
Fix: "§39 is where the choice of the collection matters: for the terms of Parigot's λμ-calculus a name stands for a test, the rule that makes a μ-abstraction is false over all type sets, and it is true over the sets defined by tests, and over the larger collection of the type sets with the μ condition."

(b) Front of the page, the list "I want to learn": "Classical logic: Peirce's law, and the condition it asks of a set". Nothing shows that the rule asks the μ condition of a set.
Fix: "Classical logic: Peirce's law, and a condition on sets that makes its rule true".

(c) §37, opening: "§38 and §39 then take the step to classical logic, where the sets of this section are needed, or sets close to them." What is proved is that all type sets are too many and that these are enough.
Fix: "... where the rule for the new terms is false over all type sets and true over the sets of this section."

### A3. §31, remark, second paragraph: Appel and McAllester derive no type expression for the looping term

Quoted: "They derive, by the two rules for the recursive type, a type expression for a term that runs forever, in the empty type."

The source. appel-mcallester-tr629 lines 260-264: "let Ω be the term (λx.xx)(λx.xx). The derivation in figure 3 shows how to use the type lemmas in figure 2 to derive |=Ω : ⊥. By lemma 3 we then have that Ω is safe." Line 153: "⊥ ≡ {}". Lines 86-90: "The semantic approach avoids formalizing syntactic type expressions. Instead, one formalizes a type as a set of semantic values."

Why it is wrong. There are no type expressions in that report, and it says so; what Figure 3 derives is that Ω belongs to the empty type. As written, the sentence also reads as if the derivation took place inside the empty type. The two "rules" are the two lemmas for μ of their Figure 2, which is what the page's "such rules are true" already means.

Fix: "By the two lemmas for the recursive type, taken for the function that sends a set α to α → ⊥, they derive that δ δ, which runs forever, belongs to the empty set of pairs, their ⊥ (their Figure 3)."

The rest of the paragraph agrees with the source: the quotation "in any computation running for no more than k steps" is verbatim (line 60); a type is a set of pairs of a number and a value, closed under smaller numbers (their Definition 1, lines 131-133); the arrow at k looks at smaller numbers (line 157: the clause for σ → τ has "∀ j < k"); every function built from the constants, × and → is "either well founded or the identity", so that the lemmas for μ hold for it (lines 421-425); "any well typed closed expression is safe" (line 425), with nothing about normalization. One imprecision is in C7.

### A4. §39, note under the lemma on the μ condition: the three readers did not find that T0 is the smallest type set

Quoted: "The items tests suffice and not the smallest were found by three readers of the papers named in the remark "What is in the literature, and what was left out", each without knowing of the others."

The item not the smallest now has two halves: that T0 is the smallest type set of λμ-terms, and that it does not have the μ condition. The form of the section that review 8a read said of the first half: "that it is the smallest type set of λμ-terms was not checked and is not used" (`review8a-scratch/sec38-39.txt`, line 194). The proof of that half is from review 8a (its C2).

Fix: "The item tests suffice, and the half of the item not the smallest that says that T0 does not have the μ condition, were found by three readers ...; that T0 is the smallest type set is from the reader who reviewed this section."

### A5. §38, definition of appending: "Without that condition the two differ" is false as it stands

Quoted: "If α is not free in v1, appending one term after another is appending the list: t[α⇐v1][α⇐v2] = t[α⇐v1,v2], because the second pass then finds nothing to do inside the copies of v1. Without that condition the two differ."

For t = x both sides are x, whatever v1 is. The two differ exactly if α is free in v1 and some named term [α]w of t has this α free in t: then the first has v1[α⇐v2] where the second has v1.

Fix: "Without that condition the two can differ: for t = μδ.[α]x, v1 = με.[α]y and v2 = z the first is μδ.[α](x (με.[α](y z)) z) and the second is μδ.[α](x (με.[α]y) z)." (Checked by `r9_sec38.py`; among 60,000 random triples none differs under the hypothesis.)

---

## Part B - rule violations

B1 (research rule 12; the review process of the page). The status section has no record of the eighth review. Its list "Errors found by review and fixed" begins "The seventh review, by two readers, ...", and nothing in it concerns §38, §39 or the lemma of §37 that review 8b read. The errors that review 8a found and the page corrected are of the kind that this list reports for the earlier reviews: a report that R2 (variable applied) and the Base condition fail with the mirror image of μ, which the paper does not say and a theorem it quotes excludes for typed terms; "what was proved from them stays true" for lemmas that were not read again, one of which fails; a proposition of van Bakel, Barbanera and de'Liguoro reported with two things it does not state; "must have" for a condition shown to be enough; a step skipped in the case of the rule μ; a source that was read and not named. The paragraph on §38 and §39 under "Worked out for this page, and not reviewed" says "each of these papers had one reader, and the writer checked the mathematics by hand and the claims about particular terms by program"; it does not say that an independent reader re-derived the five results once, that the two sections were rewritten after that, or which parts are new since (the item names, the item not only tests with its set and proof, the first half of the item not the smallest, the definition of the replacement, the case of the rule μ). The two sections say some of this in their notes ("the item names was added by the reader who reviewed them"); the status section is where the page keeps the account. It claims nothing as reviewed that is not: the five headers carry "here, unreviewed", and neither the front of the page nor the list of re-derived results names any result of §38 or §39.

B2 (rule 18; research rule 12). One question under two headings, and one question in one list only. §39, closing remark: "Not on this page. Which set ∀X.X names if ∀ ranges over MU; ... Whether a condition weaker than the μ condition makes the rule true." Status section: "Open on this page. ... Whether a condition weaker than the μ condition of §39 makes the rule for μ true." The first question of §39's list is in neither list of the status section. Review 8a found the same for another question (its B15 iv); that question is gone, and this one took its place.

B3 (rules 11 and 3). The closing remark of §39 opens "Quoted, each from the paper named", and three of its sentences are not quoted. (i) "With the mirror image of μ a variable applied to arguments can have a step at its head, so the proof of R2 (variable applied) no longer applies and a member of Base need not stay in Base": this is the page's own observation, from review 8a; the paper says only that its condition (C4) "proves to be trivial due to the fact that we have omitted the µ′-reduction" (nour-realizability, line 1212). (ii) "a reader for this page found one lemma of that proof false as printed, at one rule, and has a repair": a finding of the page, and a pointer with no name. The lemma is their Lemma 2.17, the Replacement Lemma, at the rule (abs) with ω for κ. I confirmed it by hand: (ax) and (abs) with κ = ω give ⊢ λx.x : (ω→ν)×ω→ν |; by their Definition 2.11 the stack δ, δ is in the set of (ω→ν)×ω, because the set of ω→ν is SN; and (λx.x) δ δ is not in SN. The repair is not on the page, and the digest that has it marks it as read by no one else; the sentence should say both. (iii) "Their theorem is the counterpart of §21" is the page's comparison. Mark the three as the page's.

B4 (rules 3 and 4, names and not positions).
- §38, proof of steps kept: "by the first identity", "by the second identity", "In this second identity the case that matters", "The other two are the same", "with the other two identities". The four identities are introduced with words that could be their names: appending passes through a substitution; appending at two names in either order; substitution at two variables; substitution passes through appending.
- §38, closing remark: "which is the theorem of the first of those papers". Write "of the paper of van Bakel, Barbanera and de'Liguoro".
- §39, closing remark: "found the proofs by translations of the second sort to fail". Write "by translations that pass to every term what is waiting for it".
- §39, closing remark: "and C2 would need another proof": a bare label; §13 writes "C2 (consistency)". The status section has "with C1 and C2".
- §39, example on one judgment: "the theorem of this section"; §38, note under Lemma R: "of the example", for the example "Three runs".

B5 (rules 7 and 8). The operation "t with α put for every free α′" is defined inside the item names of Lemma R ("let t° be t with α put for every free α′"), and is then used twice more in the proof of the theorem under other letters ("write t′ for t with α′ put for every free α"; "The term r is r′ with α put for every free α′"). It recurs: define it once in §38, in a line of its own, with one notation. The replacement of §39 has a frame of its own since review 8a (its B8) and still no notation; the proof introduces t* and t** for it.

B6 (rules 7, 11, 14 and 6). Two facts with their proofs stand in notes of definition frames and carry no status. (i) §38, "Appending at a name": the identity for a list. It is used in the proof of the item against a test for a test of n terms and is stated for two. For n terms the hypothesis is that α is not free in any term of the list but the last. (ii) §39, "The μ condition, and two sets": "A type set is test-defined exactly if every term that passes every test of the set is a member". It is correct, and it is a lemma of two lines. Also without a status: the first sentence of §38, "Classical logic has proofs that System F has not." Review 8a listed all three (its B11); the remark "What changed, and what did not" has its status now, these have not.

B7 (rule 1). §39, closing remark, on van Bakel, Barbanera and de'Liguoro: "a type expression for terms stands for the terms that are in SN with every stack of such a set appended". On this page "appended" is the operation at a name, defined in §38. Here the term is applied to the terms of the stack: their clause is { M | M L ∈ SN for every stack L of the set }. Write "the terms t with t v⃗ ∈ SN for every stack v⃗ of such a set".

B8 (rule 1, against rule 2). "name" now has two meanings as a noun. §10 is called "Type expressions are names", and the page says throughout that a type expression names a set. §38 calls the second sort of variables "the names", which is Parigot's word. In §39 the two meet: "tests are given for the names of Δ′" and "the set that ∀X.X names" in one proof, "a name stands for a test" in the title, "the name of a set" on the front. Rule 2 asks for the standard word and rule 1 for one meaning. The cheapest way to keep both is one sentence in the definition of λμ-terms: "The word is Parigot's; it has nothing to do with a type expression being the name of a set in §10", next to the sentence there that already says this of the letter μ.

B9 (rules 9 and 15). No example follows the definition of the μ condition; the sets that have it and the set that has not are inside the lemma. Review 8a asked for one (its B14); the example for a true judgment was added, this one was not. Two lines would do: SN has it, because a μ-abstraction that passes the empty test is in SN; T0 has not, because of μα.[α]x.

B10 (rule 1). "fail" is used for "does not pass" in the title of the lemma "Closed λμ-terms fail a test", in the name of its item, and in the title of the example on Peirce's law; §37 defines "passes" only. One sentence in §37, "A term fails a test if it does not pass it", would cover both sections. And "form" has two senses in §38 and §39: the five forms of a term, and a presentation of the calculus ("the other form of terms, in which μα may stand in front of any term", "the form of terms chosen in §38"). For the second, "syntax" with a word of explanation, or "the calculus in which μα may stand in front of any term".

On the Uses lines of §38 and §39: nothing to report; the mentions of §3, §7, §21 and §36 are passing mentions that the lint table registers.

---

## Part C - correct, and could be said more simply or more precisely

C1. §39, proof that T1 is closed under steps: the first claim is the lemma "Head steps commute with other steps" of §36, and its second statement makes the induction unnecessary. The first statement of that lemma reads word for word for λμ-terms, with the μ head step added and the item steps kept of §38 for the terms after the head step; "safe" comes for free in SN. Its second statement then gives the claim in three lines: let t ∈ SN reach r by head steps, with r having no head step, and let t → t′; then t′ reaches by head steps a term r′ that r reaches by steps; every step of a term with no head step is inside it and keeps its form, so r′ has the form of r and no head step; so the head steps of t′ end at r′. I would put "commuting" as a fourth item into the lemma "What carries over" and use it here. That also keeps one statement of the fact on the page (research rule 2).

C2. §39, the rule μ: "the two are built in the same way, r from t and r′ from t′". The step behind it is one equality, and it is the reason the name α′ was introduced: t′*[α′⇐v⃗] is the replacement of t′ with v⃗ added for α′, because α′ is not free in the terms put in, so that appending at α′ finds nothing to do inside them. With that sentence, r′ and r are two replacements, of t′ and of t, followed by the same test, and "r is r′ with α put for every free α′" can be read off.

C3. §38, item names: the literature has it, and it holds in both directions. Battyányi and Nour, Lemma 4.2 (nour-realizability, lines 1103-1104): "Let M ∈ T and α, β ∈ Vµ. Then M →R N iff M[α := β] →R N[α := β]", for their larger set of rules, proved "By induction on M". Nour and Saber state their lemma of correctness for every renaming of the free names at once, for the same purpose (their Definition 3.6). By research rule 6 the note under Lemma R should name the first, beside "the item names was added by the reader who reviewed them". For β and μ the converse is true as well, because a redex of t° is a redex of t; the page needs one direction only.

C4. §38, clauses of appending: "with the bound variables and bound names of t chosen different from α and not free in u". A variable cannot be α. Write "with the bound names of t chosen different from α, and the bound variables and bound names of t not free in u".

C5. §38, remark "What changed, and what did not": "These lines of it hold for λμ-terms, by this section: Lemma R, a head step that survives one more argument, the β head step of an abstraction, and the three facts about Base." The list of §13 has one more line, "that a member of cl(S) reaches S by safe head steps". It holds by the definition of cl(S), for either sort of head step, and the item not the smallest of §39 uses it for S = Base. The remark is silent about it; one clause closes the list.

C6. §23, limit 4: "There Lemma R gets three more lines". Review 8a counted three for the form it read: steps and appending, named, and the new sort of head step in R3. With the item names there are four by that count. If the three new items are meant (steps kept, names, under μ), say "three new items, and a second sort of head step in R3".

C7. §31, remark. (i) The first paragraph is limit 2 of §23 with a second set: there T = T ⇒ T, here R = R ⇒ T, and the argument is the same line for line. Say so, "by the argument of limit 2 of §23, with T on the right", and the paragraph is one sentence shorter and no longer reads as a new result that waits for a review. (ii) "a rule that folds and unfolds a type expression for it cannot be true here": there are two rules, and each alone can be true: the rule that unfolds if the type expression names Min, because Min ⊆ Min ⇒ T, and the rule that folds if it names SN. What cannot be is that both are true, whatever type set the type expression names. (iii) "the arrow at k looks at arguments at smaller numbers only, and that makes every such F have a fixed point": the clause for pairs looks at smaller numbers too, and that is what covers an F built from pairs alone; and the function that returns its argument is treated apart in the report (their Lemma 21). Write "the arrow and the pair at k look at smaller numbers only".

C8. Front of the page: "that rule is false over the largest collection and true over the smallest". By §39's own account the chain of §36 and §37 was not read again for λμ-terms ("Not read again, and so not claimed: the lemmas of §7 and of §36, and the rest of §37"), so "the smallest" is not claimed there. Write "false over all type sets and true over the sets defined by tests".

C9. §39, lemma "What carries over", proof of operations: the list of four facts leaves out that a variable is in Base, which the SN condition of the arrow lemma uses ("A variable x is in T, because Base ⊆ T"). The remark of §38 has it among "the three facts about Base". Write "that a variable is in Base and a member of Base applied to a member of SN is in Base".

C10. §39, theorem. "Let the collection that ∀ ranges over be TT or MU" stands over all four items, and the item not over all type sets is about a third collection. Move the sentence into the item soundness, or begin the fourth item "For the collection of all type sets of λμ-terms". In the proof of C1 (strong normalization), "t ∈ ⟦A⟧ρ" needs an assignment: "for any assignment ρ into the collection, which is not empty".

C11. §39, example on Peirce's law: "it is in Rozière's lecture notes, with this derivation". The term is there (irif-classicalded, line 721, with δ for γ). The derivation there has three lines, in rules that name a term and bind a name in two separate steps. Write "with a derivation in his rules".

C12. §39, closing remark: "In both papers a name with a type expression is replaced by a finite list taken from the orthogonal of the set of that type expression". In Battyányi and Nour it is an initial part of such a list (their Theorem 3.15). Review 8a had this (its C9 ii); the half about the names in the lists of Nour and Saber was taken up, this half was not.

C13. §39, T1: it is the smallest type set that contains every strongly normalizing μ-abstraction, that is, cl of Base together with those. Said that way, "has the μ condition" needs no argument, and the reader sees why it is the natural witness: a set with the μ condition has to contain the μ-abstractions that pass its tests, and T1 contains all that are in SN.

---

## The findings of review 8a, one by one

"Applied" means applied correctly. The numbers A1 to C13 in this table are those of review 8a.

| 8a | What it asked | State in the reading copy of 21:18 PST | Verdict |
|---|---|---|---|
| A1 | Close the gap at the bound name in the rule μ; define appending in one pass | Item names added to Lemma R and used; appending defined in one pass with no side condition; the list identity keeps its hypothesis; the replacement has its own definition; the case of the rule μ is rewritten with α′, r and r′ | Applied; one clause missing in the new proof (my A1), and one overstatement in the new note (my A5) |
| A2 | Correct the report of Battyányi and Nour on R2 and the Base condition | The sentence now says that the proof of R2 no longer applies, reports "trivial only because that rule is left out", and quotes the theorem for typed terms | Applied; the first clause is the page's and stands under "Quoted" (my B3) |
| A3 | Opening of §39 claims more than was checked | Opening names the lemma "What carries over"; "Not read again, and so not claimed"; §38 says where the lemmas of §7 and §36 stop | Applied |
| A4 | Report of Proposition 2.10 | "R3 for both sorts of head step, and the "if" halves of R2 and of the item under μ" | Applied; agrees with lines 308-312 of the paper |
| A5 | "must have", "turns out to need" | Changed in the opening of §39 and in limit 4 of §23 | Applied in part: three sentences of the same kind remain, in §37 twice and on the front (my A2) |
| A6 | R3 named where the closure condition is used | The proof of operations now reads as 8a proposed | Applied |
| A7 | Rozière's notes and Parigot's paper of 1993 not named | Both in the list of sources; the example carries "Quoted"; the status section has "five papers and one set of lecture notes" | Applied |
| B1 | Lemma used before it is stated | The lemma "Closed λμ-terms fail a test" stands before the theorem and is named in the proof of C2 | Applied |
| B2 | Parts of lemmas named by position | All the places listed are changed | Applied; new places of the same kind (my B4) |
| B3 | "The two rules that §38 left out" | "If α is not free in v, the rule that renames and the rule that removes, both left out in §38" | Applied |
| B4 | "item" in two meanings; "named" | "prefix"; "under μ" | Applied |
| B5 | "free", "bound", "closed" for names | Defined in the frame "λμ-terms" of §38 | Applied |
| B6 | "part", "hands to", "takes hold of", "fails" | "subterm" and "append" in the proofs; "takes hold of" stays in the two informal descriptions; "fail" stays in titles | Applied in part (my B10) |
| B7 | TT, the judgment sign, "a test of A" | TT redefined in a frame; the judgment written with ⊢ now "says that it is" derivable, as in §13; "a test of the set of A" | Applied |
| B8 | Definitions outside frames; the replacement | T0, T1, MU and TT are in frames; the replacement has a frame | Applied in part: no notation for the replacement (my B5) |
| B9 | Four hypotheses left out | All four are stated | Applied |
| B10 | Jargon in the closing remark | Replaced or explained at first use | Applied |
| B11 | Claims with no status | The remark of §38 has one | Applied in part: the two notes and the first sentence of §38 have none (my B6) |
| B12 | "narrow point" | The word is gone | Applied |
| B13 | "the words of §8" | "the words of §4" | Applied |
| B14 | No example after two definitions | Example "One judgment, with its replacement" added; none for the μ condition | Applied in part (my B9) |
| B15 | Status section | Examples and carried sentences listed; "notes and remarks"; the open question removed; "five papers and one set of lecture notes" | Applied in part: no record of the review itself (my B1), and another question under two headings (my B2) |
| C1 | T2 answers the open question | T1 is now that set; the proof of closure under steps is on the page | Applied; the proof is correct |
| C2 | T0 is the smallest type set | In the item not the smallest, with its proof | Applied; the credit in the note is wrong (my A4); the remark of §38 is silent on the line about cl(S) (my C5) |
| C3 | The smallest member of MU | Not taken up; the closing remark of §39 names the question as not on the page and proves that the set is strictly inside the one over TT | Left out, by a choice that the page names |
| C4 | Both halves of steps kept for both operations | Stated so | Applied |
| C5 | "safe" matters only if α does not occur | Stated so | Applied |
| C6 | C1 not needed for a normal form | "is a normal form" | Applied |
| C7 | "classical logic is the first rule" | "the rule μ is the first rule on this page that is true over a smaller collection of sets and false over the largest" | Applied |
| C8 | "one more line" in §23 | "three more lines" | Applied; the count is one short since the item names (my C6) |
| C9 | Three precisions on the reports | (i) and (iii) taken up; of (ii) the half on names | Applied in part (my C12) |
| C10 | Lemma 2.17 of van Bakel, Barbanera and de'Liguoro | "quoted here without its proof having been checked; ... one lemma of that proof false as printed, at one rule, and has a repair" | Applied; the lemma is not named, and "has a repair" is not from 8a (my B3) |
| C11 | Front of the page | The front names §39 and says that the choice is not free for its rule | Applied (see my C8) |
| C12 | Names that the term does not use | Sentence added under the rules | Applied |
| C13 | An instance of the last case | Added, with the numbers of 8a | Applied; correct |

Totals: applied 25 (A3, A4, A6, A7, B1, B3, B4, B5, B7, B9, B10, B12, B13, C1, C4, C5, C6, C7, C11, C12, C13, and A2, B2, C2, C10 with a small slip that is listed above); applied in part or one short 9 (A1, A5, B6, B8, B11, B14, B15, C8, C9); left out 1 (C3).

---

## The reports of sources in §38 and §39, one by one

- "the form given here, in which a μ is always followed by a name, is taken from the paper of van Bakel, Barbanera and de'Liguoro"; "structural substitution": right (their Definitions 1.1 to 1.3; β and μ are their only rules).
- The rules left out (one that renames, one that removes, the mirror image): right as described (Battyányi and Nour, Definition 2.5, items 3 to 5; Rozière has the rule that renames and the rule that removes).
- R3 and the "if" halves, "stated without proof as one proposition": right (Proposition 2.10, introduced by "The following is straightforward:"). "David and Nour prove the like of R3 for another presentation": right (their Lemma 3.3, with one sort of variable and no named terms).
- "Parigot proved strong normalization ... in papers of 1993 and 1997": right as far as the sources say (Matthes, line 36 and his bibliography; David and Nour: "for the types of Girard's system F").
- The rule μ "in the form in which van Bakel, Barbanera and de'Liguoro give his system for arrows": right (their Definition 3.1, two rules there, one here). "Rozière's lecture notes say the same of the second-order system": right (line 678: "les règles sur la quantification ne sont pas interprétées au niveau des termes").
- The term for Peirce's law: right (Rozière, line 721); see C11.
- Nour and Saber, the quotation: verbatim (lines 70-72). "Battyányi and Nour describe his proof in the same way": right in substance (lines 584-586, "relying on the notion of orthogonality", and lines 903-908, "every element S within M can be represented as" the set of the terms that pass an orthogonal).
- Lists from the orthogonal; names in the lists of Nour and Saber; the other form of terms in both papers: right, with C12.
- Van Bakel, Barbanera and de'Liguoro: the sets of stacks, the theorem, the rule of subtyping, the leftmost step: right, with B7 for the word "appended" and B3 for the lemma that is false as printed.
- Matthes, all four sentences: right (abstract; Definitions 1 and 6; Remark 3; section 5.3, lines 1389-1397).
- Battyányi and Nour on the rules left out: right (Corollary 4.16; line 1212; lines 553-556; Theorem 2.8; the term of lines 1336-1339), with B3 for the first clause.
- No quotation in §38 or §39 departs from its source.

Not checked, because nothing on disk allows it: that three readers found the items independently; the repair of Lemma 2.17; anything about Parigot's own papers.

## Program checks (extra evidence; all agree with the page)

- `r9_sec38.py`: the three runs; the list identity on 60,000 random triples (no failure under the hypothesis; 10,384 differ without it); steps kept on 4,223 steps of t and 4,218 steps of u; the four identities on 40,000 random triples each under its hypothesis, and a failure of the first and of the second without it; the item names on all 1,201 steps of the terms with at most 6 symbols over one free variable and two free names.
- `r9_sec39.py`: the two claims of the proof for T1 on all terms with at most 7 symbols; the recipe of "closed terms fail" on all 1,259,303 closed normal forms with at most 10 symbols, by the run that the proof describes (under the μ prefixes, head step by head step): every one reaches a repeating term; the last case occurs 22,549 times; the worked instance with its four terms; the example on Peirce's law with its run and its test; the example of a replacement; the item against a test on 3,000 random decided cases; μα.[γ]I and μα.[α]x against 300 random tests.
- `r9_t1.py`: the two claims for T1 on 6,000 random larger terms (numbers above).
- `r9_sound.py`: twenty instances of the case of the rule μ, among them instances with the name free in a member, in a test, and in both: in each, r is r′ with α put for α′, and r, r′ and m applied to the test are in SN; the instance of A1.
