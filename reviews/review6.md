# Review 6 - the five unreviewed lemmas, the new remarks, and the reports of four sources

Reader: fresh, independent, had not seen the page. Read in full: `out/reading-copy.txt` (3376 lines), `rules-research.md`, `rules-writing.md`. Read for the source checks: `geuvers94.txt` (whole paper), `matthes.txt` (lines 290-370, 455-600, 2686-2700, 4930-5175, 5335-5350, 6600-6790, 7570-7680), `vanbakel-survey.txt` (60-120, 575-600, 790-980), `abd-cs0011039.txt` (1-470, 680-1020, 1240-1340), Matthews's guide `p.txt` (362-690, 946-1500, and the places where coherence is used).

Method. Every result marked "here, unreviewed" was re-derived by hand, line by line. Every claim about a particular term being or not being strongly normalizing was also run through the evaluator `lam.py`; my scripts are in `/home/lew/agent/type-theory-review6/fresh-reader/` (`check37.py`, `check45.py`, `check45b.py`, `check_misc.py`), none in the repo. Nothing under `/home/lew/type-theory` was changed except this file.

Summary. The five unreviewed lemmas are correct as stated and proved. What is wrong is around them: the lemma of §45 does not show what the section, §21 and the front matter say it shows (its judgment is false in every context that declares z, and trivially underivable in every other one); §43 says "the theorem" where only the two corollaries are meant; one report of Matthes's thesis credits Mendler's system with a property Matthes says it did not have; and the status section has become ambiguous in three places. Counts: Part A 14, Part B 15, Part C 12.

Notation in this report: `I = λx.x`, `δ = λx.x x`, `Ω = δ δ`, as on the page. "The page" is the reading copy; line numbers are its lines.

---

## Part A - errors

### A1. §45: the judgment is true only while z is outside the context, so "derivable in no context" is not evidence of a new incompleteness

Quoted (line 3237): "In System D, the judgment Δ ⊢ λx.y (x z) : X → Y is derivable for no context Δ."
Quoted (line 3265): "It shows that the incompleteness of §14 is not an accident of System F, of the empty context or of missing inclusions".
Quoted (§21, line 1568): "And this is not a matter of a missing context or a missing inclusion: §45 gives a judgment of System D that is true and derivable in no context."
Quoted (§45 intro, line 3217): "The lemma 'True and not derivable' is repaired by giving its variable a place in the context".

The item is literally true, and its proof is correct. But split the contexts in two:

- Δ does not declare z (or does not declare y). Then no judgment about this term is derivable in System D at all, for the reason §14 gives for `(λz.I) y`: a free variable enters a derivation only through the variable rule. The three facts are not needed.
- Δ declares z : A, for any type expression A of System D. Then the judgment `Δ ⊨ λx.y (x z) : X → Y` is false, so it is underivable by the soundness theorem, and again the three facts are not needed. Counter-instance: let n be the number of arrows in A; send every variable of type expressions to SN; write `w_m` for `λv1. ... λvm.I` (m abstractions in front of I); replace z by `w = w_n` and every other variable of Δ by itself; take `u = λa. a I...I δ δ` with n copies of I.
  - For every m ≥ 0 and every A′ of System D with at most m arrows, `w_m ∈ ⟦A′⟧ρ`. By induction on A′: a variable names SN, and w_m is a normal form; ∧ is immediate; if `B → C` has at most m arrows, then m ≥ 1 and C has at most m - 1, and for b ∈ ⟦B⟧ρ the head step `w_m b →h w_{m-1}` is safe, its result is in ⟦C⟧ρ by induction, and the closure condition applies. So w ∈ ⟦A⟧ρ.
  - u is a normal form, so u ∈ SN = ρ(X).
  - `(λx.y (x w)) u → y (u w) → y (w I...I δ δ) → ... → y (I δ δ) → y Ω`, which is not in SN, so not in ρ(Y).
  - Checked by program for n = 0..3 (`check45b.py`).

So in every context the judgment is either underivable for the reason of §14 or false. The lemma shows no incompleteness that is not "a free variable that the context does not declare". Giving z "a place in the context", the repair the intro names, does not make the judgment derivable because it makes it false; the two examples are not parallel. The sentence of the remark, "the Base condition lets that fact be used, by wrapping the term under a variable", is the same thing seen from inside: the wrapping variable must be one that no context declares.

What the three facts and the item "no true part" do prove is something the page does not state: the judgment stays underivable if System D is given the rule "Γ ⊢ y : A, for every variable y that is not in Γ and every A". That rule is true by the Base condition, and it is the repair of §14's lemma written as a rule.

Fix, two ways.

- Smallest patch. State the rule just named, say that it is true and that it repairs the lemma of §14; state "not derivable" for System D with that rule and the empty context (the three facts hold unchanged, "variable" being about the declared x); replace "derivable in no context" by "in a context that declares z the judgment is false", with the counter-instance above; drop "of the empty context" from the remark and "a missing context" from §21.
- Better, and not larger: change the example to one whose free variables are all declared. Take `x : X ⊨ (λc.I) (λb. x b) : W → W`.
  - True: for u ∈ ρ(X), u ∈ SN, so `u b ∈ SN` by the helper of this proof, so `λb.u b ∈ SN`, so `(λc.I)(λb.u b) →h I` is a safe head step, and I ∈ ρ(W) ⇒ ρ(W); the closure condition gives the claim. (648 instances checked by program.)
  - No true part: for no C of System D is `x : X ⊨ λb.x b : C` true. C is built by ∧ from variables and arrows; refute one of them. A variable: send everything to Min and replace x by itself; `λb.x b` is an abstraction, so it is not in Min. An arrow `B → C′` with n arrows in B: send everything to SN, and with w and u as above, `(λb.u b) w → u w → ... → Ω`.
  - Not derivable: by the fact "application" alone, a derivation of `Γ, x:X ⊢ (λc.I)(λb.x b) : F` contains one of `Γ, x:X ⊢ λb.x b : A`, which would be true by the soundness theorem, against "no true part". The facts "abstraction" and "variable" are not needed.
  - This version needs no undeclared variable, holds in every context that extends x : X, and its reason is the SN condition with the word "safe" of the closure condition (a discarded argument has only to be in SN; a rule can only ask it to be typable), which is the gap §21 already names in "The discarded argument has to be typable" and which ω fills in the system of Barendregt, Coppo and Dezani. The Base condition is not used. If this version is taken, the sentences that name "the SN condition together with the Base condition" as the reason (lines 3217, 3227, 3265, and the row of §46) change accordingly.

### A2. §45, §21, front matter: "missing inclusions", "no repair", "the answer is no" claim more than is proved

Quoted (line 3217): "is there a system of rules, for the sets of this page, that derives every true judgment? ... For the type sets of this page the answer is no already for System D".
Quoted (line 3241): "The item no true part says why no repair of the kind tried so far can help".
Quoted (line 15): "why no repair of the usual sort makes the rules derive every true judgment".
Quoted (line 3265): "... or of missing inclusions".

- The question asked is whether some system of rules is complete. What is proved is that System D is not. The closing remark says so itself: "It does not show that no rule could be added ... Whether some finite list of rules of that sort derives every true judgment of System D was not looked at." The intro and the front matter contradict that remark.
- "Missing inclusions": the three facts are proved for the five rules of System D. With a rule of subtyping, "abstraction" and "variable" are false as stated (a variable x : X then has every F with X ≤ F; an abstraction of X → Y need not come from a derivation under x : X). The page gives no argument for the system with inclusions. For the inclusions of §20 and §22 I expect the claim to hold, but the argument needs the generation lemma for a system with ≤ (Dezani, Honsell and Alessi, Theorem 2.14) and two facts about ≤ (an intersection of arrows is below X → Y only through arrows whose inputs are above X; a variable is below no arrow), none of which the page proves or quotes.

Fix. With the second example of A1 the claim becomes provable in one line and for every true rule that keeps the term: the fact "application" survives any such rule (∧ in, ∧ out, a rule of subtyping for any relation ≤ that is true of the named sets), because the induction hypothesis applies to the judgment above it; then soundness and "no true part" finish. With the page's example, either add the inversion lemma as a quoted fact or delete "or of missing inclusions" in §45 and "or a missing inclusion" in §21. In every case reword the intro, and the front matter with it, to what is proved. With the second example: "System D is not such a system, in any context and with any true rule that keeps the term; whether rules of another shape make one is open." With the page's example: "System D is not such a system, even with the rule that a variable outside the context has every type expression; whether further rules make one is open."

### A3. §43, §44, front matter: "the theorem" does not follow from System F with ∧; only its two corollaries do

Quoted (line 3107): "The theorem and its two corollaries did not: for the rules of §26, §27, §28 and §29 they follow from System F with ∧ alone, by forgetting every term inside a type expression."
Quoted (lemma title): "THE THEOREM DOES NOT NEED THE FAMILIES".
Quoted (line 3158): "The theorem is on one side, and it is the theorem of §19."
Quoted (§44, line 3198): "For the theorem alone the third feature costs nothing at all".
Quoted (line 15): "what the theorem needs of dependent types, which is nothing beyond System F with ∧".

On this page "the theorem" is the soundness theorem (§13; §26: "The theorem and both corollaries hold with the five rules of the table added"). The soundness theorem of §26 says that a derivable judgment is true of the sets named with their families. It cannot be stated without the families, and it does not follow from the forgetful reading: the lemma's own fourth item gives a consequence of it, "no closed term t has ⊢ t : I ≡ K", "that the forgetful reading cannot show". What the lemma proves is its second item: C1 and C2. So the intro contradicts the lemma it introduces, and the word "theorem" has two meanings (rule 1).

Fix. Line 3107: "The two corollaries did not: strong normalization and consistency for the rules of §26, §27, §28 and §29 follow from System F with ∧ alone ... The soundness theorem itself, that every derivable judgment is true of the sets with their families, is among the things that needed them." Title: "Strong normalization and consistency do not need the families". Line 3158: "The two corollaries are on one side, and they are those of §19." §44: "For strong normalization and consistency alone ...". Front matter: "what strong normalization needs of dependent types".

### A4. §31: Matthes does not say that Mendler's system has no condition of positivity; he says Mendler imposed one and that it can be dropped

Quoted (line 2239): "Quoted from his thesis: the rules that Mendler gave for an inductive type are the rules of the least fixed point of F⊇, and not of F; that is why they ask nothing of F, and why his system is strongly normalizing with no condition of positivity."

The thesis, opening of chapter 6: "three mysterious facts on Mendler's system: That I succeeded in proving strong normalization without having to restrict to positive inductive types as Mendler did." Its list of central points: "Mendler's system proved to be strongly normalizing without any restriction to forming inductive types." Its footnote 14 calls the version with positivity "the original system of Mendler". And the system whose rules are matched with lfp⊇ is MeIT, "a variant of Mendler's [Men87a] system" (MeIT has an iterator, which "Mendler's original system ... does not have"). So: Mendler asked for positivity; the reading through the upper monotonization is Matthes's explanation of why it is not needed; the theorem without positivity is Matthes's, for his variant. As written, "they ask nothing of F" and "his system ... with no condition of positivity" say the opposite about Mendler.

Fix. "Quoted from his thesis: the rules of Mendler's system, in the variant the thesis studies, are the rules of the least fixed point of F⊇, and not of F. That is why they need nothing of F: Mendler restricted his system to positive F, and Matthes proves strong normalization without the restriction."

### A5. §37: sets of the form P⊥ in Krivine's realizability are not saturated sets

Quoted (line 2853): "closure under steps, CR2, is not inherited there, because a pole need not be closed under evaluation, so in that generality the sets are saturated sets and not candidates."

By §5, "saturated sets" is the standard name for type sets: SN condition, Base condition, closure condition. The sets of that semantics have only the third. The next sentence of the page says so: "Nothing is asked about termination ... a formula may name the set of all terms"; and terms there are closed, so there is no Base. One word with two meanings, and false with the page's meaning.

Fix. "... so in that generality the sets have the closure condition of §5 and not CR2; they are neither saturated sets nor candidates, because nothing bounds them by SN."

### A6. Status section: three statements are no longer accurate

- Quoted (line 3324): "Both lemmas of §31, with the counts of head steps." and "Both lemmas of §37." §31 now has three lemmas and §37 has three; one of each is unreviewed. As written the reviewed list can be read as covering them, which is the one thing the section must not allow. Fix: "The lemmas of §31 on the Mendler fixed point and on the inductive part for monotone F, with the counts of head steps." and "The lemmas of §37 that one term passes every test and every closed term fails one, and that test-defined sets form a fourth collection."
- Quoted (line 3326): "the accounts of the four sources in the remarks of §43, §42 and §45". Those three remarks report three sources (Geuvers; van Bakel; Dezani, Honsell and Alessi). The accounts of Matthes are in §22, §31, §35 and §36; further accounts of Geuvers are in §34 and §44; the sentence on Dezani, Honsell and Alessi in §20, the row in §46, and the last paragraph of the remark in §40 (Matthews) are new accounts too. None of these is listed as checked by its writer only. Fix: list the sections.
- Not listed as unreviewed although worked out for the page and new: the closing remark of §45 with its claim "A rule for exactly this case would be true" (it is true, see the verdicts, but it has no proof and no status); the three "Measured against this page" paragraphs of §42, §43 and §45; the sentences added elsewhere on the strength of the unreviewed lemmas (§21 third bullet, §22 CAUTION, §44, the front-matter paragraph "The reading answers questions ...", the changed rows of the table of §31).
- "Open on this page" lacks the question that §45 leaves open in so many words: whether a finite list of true rules derives every true judgment of System D.

### A7. §36: the example of two arrows that differ is Matthes's example, and the inclusion is his Lemma 9.9; the page lists both as derived by its writer

Quoted (line 2687): "It can be strictly smaller: for T = SN and U = Gen({ I u : u ∈ SN }), the term I is in T ⇒ U and not in T ⇒I U."
Quoted (status, line 3326): "the lemma of §36 on the arrow into a head-closed type set, with its example of two arrows that differ".

Thesis, section 9.1.2, after Lemma 9.9 (transcribed; the thesis tells its two sets N apart by typeface, written N and N0 here): "It is possible that M →I N ≠ M →E N": take both types to be α → α, M := SN at that type, N := the saturated closure of N0, with N0 := {(λz.z) t | t ∈ SN}; then r := λz.z is in M →E N and not in M →I N, and the proof is the page's proof (an abstraction in a closure is in the generating set; take t := λx.x). The page's example is this one with the types removed. The remark does say that Matthes "gives an example where they differ", but not that it is the example of the lemma, and the status section claims it for the page. Rule 6 of the research rules.

Fix. In the item: "... as in Matthes's example, read for untyped terms". In the status section: "the lemma of §36 on the arrow into a head-closed type set; its item not so for SAT, with the example, is Matthes's Lemma 9.9 and his example, transcribed for untyped terms". The items head-closed, values and generated are the page's.

### A8. §42: the base terms of Geuvers's paper are under-reported

Quoted (line 3098): "The set that every saturated set contains has, besides a variable applied to strongly normalizing arguments, the two constants and every Πv:M.N with M and N strongly normalizing."

Definition 3.1 of the paper closes the base terms under application from every starting point: "If M ∈ B and N ∈ SN, then MN ∈ B". So `⋆ Q1...Qn`, `□ Q1...Qn` and `(Πv:M.N) Q1...Qn` are base terms, and the paper's equivalent form of the definition says it outright: "∀Q⃗, M, N ∈ SN [(Πv:M.N) Q⃗ ∈ X]". Fix: "... has a variable, either of the two constants, or a Πv:M.N with M and N strongly normalizing, each applied to any number of strongly normalizing arguments." (The closure condition, with the annotation N in SN, is reported correctly; it is the fourth clause of the paper's equivalent form. The paper's own Definition 3.3 states it as "M ∈ SN" for the whole term, which is E3 of the page.)

### A9. §43: the limit Geuvers names is small inductive types, not "inductive types whose members can be used to compute a type expression"

Quoted (line 3164): "It does not reach inductive types whose members can be used to compute a type expression, because then P 0 and P 1 can be convertible with two different type expressions".

The paper: "the proof does not scale up to the extension with small inductive types (where the inductive type is of type ⋆)". Its section 5.3 does treat an inductive kind Nat whose members compute type expressions (rule Elim with T a kind, "[[Rec P1 P2]] := the function defined by primitive recursion"), by giving Nat the set-interpretation ℕ. The page knows this (status section: "which Geuvers's paper has for inductive kinds"), so the paraphrase in §43 contradicts the page's own account. Fix: "It does not reach inductive types that are type expressions, so that their members are terms, if those members can be used to compute a type expression, because ...".

### A10. §37: "only the third is made, ∀ over all sets" equivocates

Quoted (line 2853): "of the three demands that §15 lists, only the third is made, ∀ over all sets."

The third demand of §15 is "∀ over all type sets": the recursion on type expressions is circular, so the collection of sets has to be fixed first. In the guide, "for all" ranges over the individuals of the model (Definition 9.3: ‖∀x φ(x)‖ is the union of ‖φ[a/x]‖ over the names a ∈ N), and ‖φ‖ is defined by plain recursion on φ; no collection of sets of terms is quantified over and no circle arises in the definition. "All sets" there means all sets of the model, a different sort of thing from the type sets of §15. Fix: "of the three demands that §15 lists, the first two are not made; the place of the third is taken by a quantifier over the individuals of the model, which are sets of pairs of a name and a stack."

### A11. §37, third point: two small departures from the guide

Quoted (line 2855): "that setting calls a pole coherent if every term that contains no captured stack fails some test ... and the term λx.y of the item passes all has its counterpart there, a term with a captured stack that passes every test."

- The guide's Definition 9.8 calls the realizability algebra coherent, not the pole.
- The guide's footnote 3 gives the counterpart for a realizability model whose pole is not empty; with the empty pole no term passes every test. Add "if the pole is not empty".

### A12. §42: "uses neither subject reduction" needs the paper's own qualification

Quoted (line 3098): "He points out that the proof uses neither subject reduction nor a translation into another system."

The paper, section 4: "we don't require the set of typable terms to be closed under reduction ... The only two properties that are seriously used are ... Classification ... and a strengthened version of Stripping". But section 2.1 obtains that second property for the calculus as defined from subject reduction: "This strengthening of Stripping holds straightforwardly for CC, because ... one has the Subject Reduction property"; only after the conversion rule is changed (Definition 4.1) is it had directly. Fix: "He points out that the proof uses two facts about derivations and no more, and that with the conversion rule taken one step at a time neither rests on subject reduction; nor is there a translation into another system."

### A13. §34: "in one induction"

Quoted (line 2453): "Geuvers's proof for the Calculus of Constructions, which §42 reports, uses both at once, in one induction."

The plain-set reading is set up by its own induction first (Lemma 3.8, "by simultaneous induction on the structure of Q, respectively A"); the soundness theorem (3.13) is a second induction that uses both readings. Fix: "uses both at once, in one soundness theorem."

### A14. §22: "rests on" where the thesis says "motivates"

Quoted (line 1604): "in his thesis induction is what iteration over an inductive type rests on, and extended induction is what primitive recursion rests on".

The thesis: "(lfp-E) ... This will motivate iteration ... I call this rule the principle of extended induction. It motivates primitive recursion." The rules of the term systems are not derived from the lattice facts. Fix: "... is what motivates iteration ..., and extended induction is what motivates primitive recursion".

### Quotations and reports checked and found accurate

Geuvers: "a kind of 'proof-irrelevant' interpretation"; "Type dependency can not anymore be ignored"; "as a real dependent product of saturated sets"; "is carried out in exactly the same structure as where the proof of SN for Fω is usually done"; one language of pseudoterms; the closure condition with the annotation in SN; the two interpretations of a kind; [[⋆]] = SN; P t and P q the same set, λx:σ ignored, Πx:σ.τ the arrow; soundness with the identity valuation. Matthes: "Girard's candidates are nothing but saturated sets which are closed under reduction" (footnote 8, stated without proof); the name and definition of the upper monotonization and "Φ≥ = Φ" for monotone Φ; the name "extended induction"; the names of the two arrows, the inclusion, and the remark that the proof uses only the three rules both satisfy. Van Bakel and Dezani-Honsell-Alessi: the type expressions, rules and ≤ of the system of Barendregt, Coppo and Dezani; completeness for the simple semantics; the filter model as "one model out of the type expressions"; that ≤ was added for completeness; that completeness forces (→-∩) and (η), with the example of §20 (their Proposition 5.11); closure under conversion with ω; the three semantics; Hindley 1983. Matthews: stacks, processes, the four evaluation rules, the pole (6.6), ‖φ → ψ‖ and ‖∀xφ‖ (9.3), the one inclusion (10.2), Proposition 9.6 behind "a negation has a witness", coherence and Theorem 9.9, Definition 11.4 and Propositions 11.6 and 11.8(iv) behind the last paragraph of §40, the fixed-point combinator of Lemma 12.2 (not in SN: its one reduct contains it).

---

## Part B - rule violations

Rule numbers are those of `rules-writing.md` unless marked R (research).

1. Rule 1, notation. `|t|` is the erasure of an annotated term in §42 and `|A|`, `|Γ|` are the forgetful reading in §43; §44 uses both sections. Give the forgetful reading its own notation, for instance A° .
2. Rule 1. "the theorem" for "the two corollaries" in §43, §44 and the front matter (A3).
3. Rule 1. "saturated sets" in §37 for sets with the closure condition only (A5).
4. Rule 1. "Nothing is asked about termination" (§37, line 2853) and "termination" in several rows of the table of §46 (lines 3278 to 3283). The page's rule is "strongly normalizing" or "∈ SN"; here "about normalization, strong or weak" is meant.
5. Rule 7. `T ⇒I U` is defined inside an item of a lemma (§36, "not so for SAT"). The facts "F⊇ is monotone ... F⊇ = F if and only if F is monotone" are claims placed inside a definition (§31). Move the first to a definition before the lemma; make the second a one-line lemma or mark its status.
6. Rule 13 and rule 7. §43 uses "ιx.B, the self type" as a form of type expression and "the two rules for the self type in §27". §27 gives the set and two membership facts; it never writes the form, the clause or the two rules. Write them in §27 (as §28 does for ιx:A.B), or in the definition of the forgetful reading.
7. Rule 3. "By the two lemmas" in the example "Mendler-style natural numbers" (§31): there are three now. Name them.
8. Rule 3. "the two sets that the implication relates there are equal" (§37, line 2855). In the paragraph before, "the first set" and "the second" are the sets that the two sides of the implication name, so this reads as "those two are equal". Meant: the set of terms that pass the tests u, w⃗ and the arrow of the two sets. Say that.
9. Rule 3 and rule 4. Two lemmas of §36 have an item named "not so for SAT", and the remark points to "the item not so for SAT". Also in §36: "The first two conversions enlarge a type set, the last two shrink it." And §37, first remark: "what the lemma proves of P⊥" (which lemma, which item).
10. Rule 5. "takes every term that behaves well when it is applied" (§36, new text); "what remains when a further invariance is asked" (§36 remark); "A different route is open whenever a translation ..." (§13, outside the sections under review).
11. Rule 2. Unexplained: "fixed-point combinator" and "the induction axiom of set theory" (§37); "positive positions" (§45, closing remark; §22, where "occurs positively" is said, is not among the sections §45 uses).
12. Rule 6. §45 does not say that y and z are not declared, which is the hypothesis everything turns on (A1). §22: "if F(μF ∩ C) ⊆ C" needs "for a type set C"; and "Induction" holds for every F, not only "For monotone F".
13. Rule 12. §43, proof of "derivations": the case "∀ out" of §13 needs a fourth fact, `|A[B/X]| = |A|[|B|/X]` for a variable X of type expressions, and the case "∀ in" needs that the names of family variables and of variables of type expressions are kept apart. Both are immediate; neither is said. §45: the three facts are "routine" with one sentence of proof; acceptable, but the case "∧ out" of "abstraction" deserves its line (F ∧ G is not an arrow, so both parts are built from such arrows).
14. Rule 19. The example "What replaces the union" (§37) draws a conclusion about the existential types of §22, which §37 does not use; `POINTER_OK` in `build.py` lists it as "names existential types". It is a use. Same for "as §30 showed" in §45, which carries a claim. Either add the sections to the Uses lines or cut the sentences to pointers.
15. Rules 11 and 18, R12. Status: the points of A6. Also: the five new proofs do not end with the mark ∎ that the other 47 proofs carry, so in the reading copy the proof of the lemma of §37 runs into the example after it; and the header of the theorem of §21 reads "KNOWN, PROOF HERE", which is not one of the four status words the status section lists.

---

## Part C - correct, and could be simpler or more precise

1. §45, "not derivable". With "no true part" proved first, the item needs one fact, not three: a derivation of the whole contains a derivation for the part (fact "application", and for the page's example also "abstraction"), which would be true by the soundness theorem. That makes "no true part" the proof and not a gloss, and it is the form that survives added rules (A2).
2. §31. The item in holds in the stronger form `in ∈ F⊇(Ind(F)) ⇒ Ind(F)`: for u ∈ F(D′) with D′ a type set inside Ind(F), instantiate a at C = D′ and p at D = D′; both proofs go through word for word, because D′ ⊆ Ind(F) ⊆ Fix(F). Then in and out are inverse-shaped, `in : F⊇(Ind(F)) ⇒ Ind(F)` and `out : Ind(F) ⇒ F⊇(Ind(F))`, which is Matthes's rule (lfp⊇-I) beside his predecessor, and "monotone" is exactly the hypothesis that replaces F⊇ by F on both sides.
3. §31, proof of in for any F: "and not at Fix(F) as the proof for monotone F did". The proof for monotone F did not instantiate; it cited the lemma on the Mendler fixed point, whose proof does. Say "as the lemma on the Mendler fixed point did".
4. §31, table, row Price: "F has to be monotone, so positive" reads as "monotone implies positive". The other column has it the right way round: monotone, "which the usual presentations ensure by ... positively".
5. §36. "T ⇒I U takes the abstractions that are built well, and what the closure condition adds": and Base. "into a head-closed type set there is one arrow, and it is a set of values": it is a head-closed type set, which the lemma before identifies with a set of values.
6. §37, proof. "The six claims about p, q, t on a and b": the proof makes four (p a, q b in SN; t a, t b not). The other two, p b and q a not in SN, are true (program) and not used. Say "the four claims, and the two about p b and q a".
7. §37, example "What replaces the union". Two silent steps: the set of tests that every member passes is not empty because it contains the empty test (needed, since P⊥ is defined for nonempty P); and "need not be a member of TT" needs an F, for instance the F that gives Ta at SN and Tb at every other member.
8. §43, remark, "Induction". Nat′ is given in §29 as a set, and the forgetful reading is defined on type expressions. Write the type expression once: with N for ∀X.(X→X)→X→X, Nat′ is named by `ιx:N. ∀P. (∀y:N. P y → P (S y)) → P 0 → P x`, whose forgetful reading is `N ∧ ∀P.(P→P)→P→P`, which names cNat ∩ cNat. Then "which is cNat again" is a computation and not a paraphrase.
9. §43, remark, "The rules β and δ together": "has to be large for a true equation and Min for a false one". The item proves: contains I for a true equation, and is Min for the equation K ≃ K′. Say that.
10. §43, "Measured against this page": "it buys the place where Geuvers's method stops". The page has no rule that computes a type expression from a term; E(u, v) is a type set with two values. "it reaches the place" would claim what is shown.
11. §45, "Measured against this page": "no set inside SN is closed under conversion": no nonempty set (the empty set is; every type set is nonempty, so nothing depends on it).
12. §45, closing remark. The proposed rule is true by two lines that could be given: the term put for t is in SN because every type set is, so applied to z it is in SN by the helper, and y applied to it is in Base. It is also the first rule on the page that lets a free variable into a term from outside the context, which the proof of the addition lemma in §18 says "none on this page does"; C2 survives as stated, because it says "closed". And the helper is the converse of the fact "applied to a variable" of §16; one cross-reference would tie the two uses of "replacing a variable by a variable neither creates nor removes a redex" together.

---

## Verdicts on the re-derived results

1. §37, "Test-defined sets are not closed under union", and the example after it. Correct as stated and proved. By hand: both five-step head runs with their arguments, both runs to Ω, the step "every test that p and q pass, t passes" (n = 0 and n ≥ 1), and the final contradiction. By program: all six memberships; and t passed every one of the 184 one-term and 11036 two-term tests, drawn from a pool of small strongly normalizing terms, that p and q both passed. The example is correct; see C6 and C7.
2. §43, "The theorem does not need the families". All four items correct. Every rule case checked (variable, → in/out, ∀ in/out, ∧ in/out, Π in/out, ∀ in/out for families, term conversion, ι in/out, both self-type rules, ∀ in/out for terms); one easy fact is missing from the list (B13). The claim about β and δ is correct: β puts I into T, δ at Γ = e : {K ≃ K′} and B = ∀X.X forces T ⊆ Min, and I ∉ Min. The forgetful reading of Nat′ is cNat (C8). The remark is correct except for the wording of C9 and C10. The intro, title and three other places misname what is proved (A3).
3. §45, "True, and derivable in no context". All three items correct as stated and proved. The helper is correct (a redex of b[z/a] is a redex of b). The three facts are true of System D and suffice for the argument given. "No true part": u0 is a closed normal form; s_k has k + 1 head steps ending at an abstraction with n - k abstractions before K, never at a member of Base and never at u0 (program, n ≤ 4), so M2 applies; the induction over C′ with "at most n - k arrows" is sound in all three cases, including the count k + 1 ≤ n in the arrow case. The rule of the closing remark is true and derives the judgment (variable rule, the rule, → in). But the item "not derivable" carries no information about completeness beyond §14, because the judgment is false in every context that declares z (A1), and the claims built on the lemma overreach (A1, A2).
4. §31, the upper monotonization and "The inductive part, for any F". Correct. The earlier proofs of type set and induction do not use that F is monotone (the monotonicity used is that of G, which comes from the index set); the new proof of in, instantiating a at C = Ind(F), is correct and uses only Ind(F) ⊆ Fix(F) and Ind(F) = G(Ind(F)); out lands in F⊇(Ind(F)) as stated. The table (rows Induction and Price) and the remark agree with the lemma. Stale: "By the two lemmas" (B7). Sharper form available (C2). The report of Matthes beside the definition is wrong on one point (A4).
5. §36, "The arrow into a head-closed type set, in values". All four items correct, including the example (K ∉ U, so I ∉ W; I has no head step and is not in Base, so I ∉ Gen(W); I ∈ SN ⇒ U). The fourth item and its example are Matthes's (A7).
6. §22, "extended induction". Correct: D = μF ∩ C is a type set, F(D) ⊆ F(μF) = μF by monotonicity and Knaster-Tarski, F(D) ⊆ C by hypothesis, and induction gives μF ⊆ D ⊆ C. Say that C is a type set (B12). Attribution of the name correct; "rests on" should be "motivates" (A14).
7. The three remarks.
   - §37, last paragraph. First point correct: with arbitrary terms in a test the set of pairs is not closed under undoing evaluation, witness (λx.y) Ω; with strongly normalizing ones it is, by R3 for the step that takes an argument and trivially for the step that moves one. Second point correct in content, ambiguous in wording (B8). Third point correct, with the two departures of A11.
   - §40, last paragraph. Accurate against the guide (Definition 11.4, Proposition 11.6 with cc in the direction named, Proposition 11.8(iv) realized by I).
   - §42, closing remark. Accurate except the base terms (A8) and the qualification on subject reduction (A12). "No step is silent" and "one more condition of the same sort as safe" are fair readings of Definition 3.3 and its equivalent form.

Status section: lists all five unreviewed lemmas, the fact of §22 and the second remark of §37. It is inaccurate in the ways of A6.

No restructuring is proposed. The one change that moves text is the choice in A1 between patching the lemma of §45 and replacing its example; both stay inside the lemma and its remark.
