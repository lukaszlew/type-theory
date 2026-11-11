# Review 8a - §38 "Terms that capture their arguments" and §39 "Classical logic: a name stands for a test"

Reader: fresh, independent, had not seen the page. Read: `out/reading-copy.txt` lines 1-1175 (front, contents, §1-§13), §23 (limit 4), §37 in full, §38 and §39 in full and twice, the status section and the list of sources; `rules-research.md`, `rules-writing.md`; `src/mu.html` and `src/classical.html` for subscripts and cross-references; `plan.py` and the lint table of `build.py` for the Uses lines. Sources read for the checks (pdftotext output, in `/home/lew/agent/tt-papers/pdf/L7/`): `vanbakel-sn-lambdamu.txt` (1-345, 385-494, 612-836), `nour-saber-completeness-lambdamu.txt` (1-300), `nour-realizability-lambdamu.txt` (1-1104, 1196-1216, 1276-1345), `matthes-stabilization.txt` (1-60, 255-300, 396-445, 540-575, 762-812, 840-900, 1370-1440, and the two entries for Parigot in the bibliography), `david-nour-short-sn.txt` (1-200), `irif-classicalded.txt` (1-40, 640-730). The digests were used to find lines only. Quotations are verbatim, except that typographic quotation marks and apostrophes are written in ASCII; line numbers are those of the files named.

The page changed while this review ran. I read the reading copy written at 04:04 UTC on 2026-11-11; `src/classical.html` and `src/tests.html` were changed at 04:35 and `src/_back.html` at 05:00, by someone else. At the end I compared the current `src/mu.html`, `src/classical.html` and `src/_back.html` with that reading copy. §38 is unchanged. §39 has one change: in the closing remark the question about a type set with the μ condition that is closed under steps now stands under "Open on this page", and the rest of that list under "Not on this page". In the status section "six papers on the λμ-calculus" now reads "five papers", and material on other sections was added. Every sentence of §38 and §39 that Parts A and B quote is still in the current sources; the two findings that the changes touch, A7 and B15, say so.

Method. Every result of §38 and §39 was re-derived by hand. The claims about particular terms, the identities behind Lemma R, the item "against a test" and the recipe of "closed terms fail" were also run by program. I wrote a second evaluator with de Bruijn indices (`db.py`) and first compared it with the other reader's `lmu.py`: the sets of one-step reducts agree on all 300,089 terms with at most 8 nodes over one free variable and one free name. Scripts, all in `/home/lew/agent/tt-papers/review8a-scratch/`: `db.py`, `check1_crossval.py`, `check2_closed_fail.py`, `check3_examples.py`, `check4_lemmaR.py`, `check5_against_test.py`, `check6_muprime.py`, `check6b_muprime_retry.py`, `check7_T2.py`, `check8_rename.py`. Nothing under `page-L7` was touched except this file.

Summary. All five results marked "here, unreviewed" are correct as stated. Their proofs are correct with one exception: the case of the rule μ in the soundness proof skips a step about the bound name that is not a matter of convention (A1); the theorem is true, and two sentences close the gap. The other errors are around the lemmas, not in them: a report of Battyányi and Nour that says more than the paper and is contradicted, for typed terms, by a theorem the same paper quotes (A2); an opening sentence that claims more than was checked and is false for at least one earlier lemma (A3); a report of Proposition 2.10 that includes two things the proposition does not state (A4); "must have" for a condition shown to be sufficient (A5); a proof that names R3 where the closure condition is what is used (A6); and a sixth paper that was read, contains the derivation of the example on Peirce's law, and is named nowhere on the page (A7). One finding is positive and belongs with the five most important: the question that the status section lists as open, whether a type set with the μ condition that is closed under steps is test-defined, has the answer no, by a set and a proof of six lines that use only §38 (Part C, item C1). Counts: Part A 7, Part B 15, Part C 13.

The eight particular checks, in short.

1. Appending and the μ step. The side conditions on bound names are enough, in the clauses and in the rule μ. "Appending one term after another is appending the list" is right as stated. The side condition "α is not free in u" is needed only for that identity; §39 then uses appending where it does not hold (A1 a).
2. "By the proof of §N, word for word". No step of an old proof fails for λμ-terms. Three places name less or other than what is used: the proofs of §8 and §9 do not use R3 (A6); R3 for the β head step needs "if u → u′ then t[u/x] reaches t[u′/x]", which the item steps and appending does not state (B9; Part C, item C4); and "→ in" for names is not the "→ in" of §13 (A1 b). The opening sentence of §39 goes further than any of these proofs (A3).
3. MU. It is nonempty (SN), closed under ⇒ (with any type set on the left) and under nonempty intersections. Lemma N and the four facts need nothing else of the collection. C2 (consistency) needs one member with no closed member, which the proof supplies without naming the smallest member; item C3 of Part C names it.
4. "With the three conditions alone the new rule is false". The note under the theorem says exactly what the item proves. The opening paragraph says more: "must have" (A5).
5. Peirce's law. The six lines are instances of the rules as stated; the run with λk.k v and the failing test are right. The term and its derivation are in a paper that was read and is not named (A7).
6. Sources. The one quotation (Nour and Saber) is verbatim, and "stacks" is the paper's word. Right as reported: the form of terms and "structural substitution" (van Bakel, Barbanera and de'Liguoro, Definitions 1.1 to 1.3); the rule μ for arrows (their Definition 3.1, two rules there, one here); their sets of stacks and their theorem (Definitions 2.11 and 2.16, Theorems 2.18 and 2.24, the rule (≤), Lemma 2.23 for "undoing the leftmost step"); David and Nour's Lemma 3.3 as "the like of R3"; Parigot's two papers and C1 (strong normalization) as his theorem (Matthes's bibliography; David and Nour: "for the types of Girard's system F"); all four sentences on Matthes (abstract, Definitions 1 and 6, Remark 3, section 5.3); Battyányi and Nour on the rules that rename and remove and one more (Corollary 4.16) and on the typed term with an infinite run (their lines 1336-1339). Not right: A2, A4, A7; three precisions in Part C, item C9.
7. Writing rules: Part B. No "whenever" and no "X when Y" in the two sections.
8. Status section: it lists every result of the two sections that carries "here, unreviewed" and claims none as reviewed. What it leaves out or has twice is in B15 and A7.

---

## Part A - errors

### A1. §39, soundness, the rule μ: the bound name of the conclusion is treated as the free name of the judgment above the line, and for names that is a step, not a convention

Quoted (proof): "Let m = (μα.[β]t)*; it is μα.([β]t)*, with the bound name α not free in the terms put in. Let v⃗ be a test of ⟦A⟧ρ, with α not free in its terms. Appending v⃗ at α in ([β]t)* gives [β]t after the replacements for Γ and Δ, the latter now with v⃗ for α; write t** for t after these. The judgment above the line is true, so t** ∈ ⟦B⟧ρ."

Quoted (definition of a true judgment): "the term t with every ui put for xi and every v⃗j appended at αj ... The replacements are made all at once, with the bound variables and bound names of t chosen so that they are not free in the terms put in, and nothing is done inside those terms." And §38: "For a term t, a name α and a term u in which α is not free, t[α⇐u] is t with u appended at α".

Why it is a gap. Two things.

(a) The definition. The members ui and the tests v⃗j are arbitrary, so a name αj of Δ may be free in them. For example, send X to the set of the terms that pass the one test μγ.[α]y; that test is a test of ⟦X⟧ρ, it may be chosen for α : X, and α is free in it. §38 defines appending only for terms "in which α is not free", so for such a choice the truth condition uses an operation that §38 does not define. The sentence "nothing is done inside those terms" repairs it in words; it is a second definition, in one pass, of something §38 defined with a side condition. The side condition of §38 is not needed for one term (one pass is well defined); it is needed only for the note "Appending one term after another is appending the list", which is false without it: with t = μδ.[α]x, v1 = με.[α]y, v2 = x one gets t[α⇐v1][α⇐v2] = μδ.[α](x (με.[α](y x)) x), and the list gives μδ.[α](x (με.[α]y) x) (`check4_lemmaR.py`).

(b) The proof. The judgment above the line is about t with the particular name α, which is free in t and listed in Δ. If α is free in a term that is put in, or in a term of v⃗, the bound name of m cannot be α: m is μα′.([β′]t′)* with a new name α′, where t′ is t with α′ for α. The proof then needs "t′ after the replacements, with v⃗ for α′" followed by the test of β in SN, and the judgment above the line gives this for t and α, which is a different term: it has [α] at the places that come from t where the needed term has [α′]. In "→ in" the same move is harmless and §13 is right to pass over it: t′ with u put for x′ is literally t with u put for x, because a substitution removes the variable. Appending leaves the name in place, so the two terms differ.

Concrete instance. Line 4 of the example on Peirce's law, Γ ⊢ y (λx.μγ.[α]x) : X | α:X, with ρ(X) = ρ(Y) = SN. The term u = λk.μδ.[α]k is a member of ⟦(X → Y) → X⟧ρ (u g → μδ.[α]g, and g ∈ SN), and α is free in it. For line 5, m = μα′.[α′](u (λx.μγ.[α′]x)), and already for the empty test the proof has to show u (λx.μγ.[α′]x) ∈ SN. The judgment of line 4, with the empty test for α, gives u (λx.μγ.[α]x) ∈ SN, which is another term.

The literature passes over the same step. Van Bakel, Barbanera and de'Liguoro write, in the case (µ) of their Lemma 2.17, "since α is bound in M, we can assume it does not occur free in the image of ξ" (line 447-448), after a convention that treats the names of ∆ "as binding occurrences over M as well" (221-223); Nour and Saber state their lemma of correctness for every renaming of the free names at once (Definition 3.6 and Lemma 3.3, lines 243-251, and "b is a new variable" in the case µ), which covers it. By rule 12 of the writing rules ("no skipped step") the page should take the step.

The theorem is not affected. Either of two short arguments closes the gap.

Fix 1 (elementary; recommended). Add to Lemma R for λμ-terms one line: "names. Putting a name α for a free name α′ everywhere in a term turns every step into a step, because neither rule looks at a free name. So if the term with α put for α′ is in SN, then the term is in SN." Then in the proof: "If α is free in a term put in or in v⃗, the bound name of m is a new name α′, and the term to be shown in SN is the term r′ built from t with α′ for α. The judgment above the line gives r ∈ SN for the term r built from t itself, and r is r′ with α put for α′; so r′ ∈ SN by the item names." (The item was checked by program on the 14,043 steps of the terms with at most 7 nodes over one free variable and two free names, `check8_rename.py`.)

Fix 2. "The truth of a judgment does not change if two names are exchanged everywhere, in the term, in Δ, in the members and in the tests, because TT and MU are carried to themselves by such an exchange. So the judgment above the line is also true with a new name α′ for α."

With either fix, define appending in §38 in one pass and without the side condition ("nothing is done inside u"), keep "α not free in v1" as the hypothesis of the list identity, and let §39 refer to that definition. See also B8.

### A2. §39, closing remark: "so R2 (variable applied) and the Base condition fail" is not in Battyányi and Nour, and for the typed terms of that paragraph it contradicts a theorem they quote

Quoted: "With the mirror image of μ a variable applied to arguments can have a step at its head, so R2 (variable applied) and the Base condition fail, and they report that the method of candidates does not give strong normalization there".

What the source says. (i) nour-realizability 1212-1213: "Condition (C4) proves to be trivial due to the fact that we have omitted the µ′-reduction, that is, the symmetric counterpart of µ." Their condition (C4) is the counterpart of the Base condition. That says the condition is no longer trivial with μ′, not that it fails; in their section 5 they prove their (C4) with μ′, for the set of weakly normalizing typable terms, and call it "the most difficult one to establish" (1292-1293). (ii) 266-270 and 553-556: techniques based on candidates "fail to establish strong normalization results in the presence of the µ′ rule. The standard technical lemmas usually required in this context do not hold"; which lemmas is not said. (iii) Theorem 2.8 (541-543), in two parts: "The µµ′-reduction is strongly normalizing for the untyped λµ-terms." and "The βµµ′-reduction is strongly normalizing for the typed λµ-terms."

Why the sentence is wrong. The first clause is true: x (μα.c) has a step. What follows from it is that the proof of R2 no longer applies ("no step can change the variable that is applied") and that a member of Base can leave Base by a step. That R2 or the Base condition fails needs strongly normalizing u1,…,un with x u1…un not strongly normalizing, and neither the page nor the paper gives one. For typed terms there is none, by (iii): the paragraph is about "simple types", and there every typable x u1…un is strongly normalizing with β, μ and μ′. For untyped terms I found none: `check6_muprime.py` adds μ′ to the evaluator and finds no counterexample among x u for all 4,760 strongly normalizing u with at most 6 nodes, nor among 41,209 pairs x u1 u2. (140 pairs are undecided at the first fuel limit. 110 of them contain no λ, so their runs are μ and μ′ steps only and stop by the first part of (iii). The other 30 contain a λ; for each of them `check6b_muprime_retry.py` takes 300 random runs: every run ends, the longest after 25 steps, and no β redex occurs on any of them, so that these too are runs of μ and μ′ steps. Random runs are evidence and not a proof.) The argument I can give by hand points the same way: with a variable at the head, μ′ only puts x in front of named terms, and no abstraction comes into function position that was not there in the ui.

The sentence also leaves out (iii), so that a reader takes strong normalization with the mirror image to be open or false; the entry "Strong normalization with the rules that §38 left out" in the list "Not on this page" has the same effect.

Fix. "With the mirror image of μ a variable applied to arguments can have a step at its head, x (μα.c) → μα.c′, so the proof of R2 (variable applied) no longer applies and a member of Base need not stay in Base; they say that their counterpart of the Base condition is trivial only because that rule is left out. They report, from an earlier paper, that the method of candidates does not give strong normalization there, and they quote the theorem that β, μ and the mirror image together are strongly normalizing for typed terms, proved by other means; with the mirror image and the simplifying rules together they give a typed term with an infinite run."

### A3. §39, opening: "what was proved from them stays true" claims more than was checked, and is false for at least one lemma

Quoted: "With the λμ-terms of §38 the definitions of §5, §8 and §37 can be read again, word for word, and what was proved from them stays true."

Why it is wrong. What was checked is the list in the lemma "What carries over to λμ-terms": the arrow, intersection and union lemmas, the four facts, and three items of §37. The page says so itself in two places: "Its last line, about the sets cl(S) of §5, was not read again" (§38, remark), and "that it is the smallest type set of λμ-terms was not checked" (§39, note on T0). And some of what was proved from those definitions does not stay true as it stands:

- L3 (chain) in §7, proved from the definitions of §5: "let a = a0 →h a1 →h … →h ak be all the head steps of a. Then ak is an abstraction". For the λμ-term a = μα.[α]x, which is outside Min, ak is a itself, a μ-abstraction. The lemma "Head-closed type sets are sets of values" in §36 rests on the same step ("they end, at a term with no head step: an abstraction, or a term x u1…un") and fails with it: T0 and the set T2 of Part C, item C1, are both closed under head steps and contain no abstraction, and they differ.
- The item "closed terms fail" of §37, read with "closed" as §1 defines it, is false for μα.[γ]I; that is the page's own item "a free name passes". It is true again after "closed" is redefined, by a new proof; the old proof starts from "A closed normal form is an abstraction", which is false for μα.[α]I.

Fix. "With the λμ-terms of §38 the definitions of §5, §8 and §37 can be read again, word for word. The lemma "What carries over to λμ-terms" lists what was read again with them and stays true by the same proofs. The rest was not read again, and some of it changes: a term that has no head step and is not in Base may now be a μ-abstraction, so the lemmas of §7 and §36 that end at an abstraction do not hold as they stand." The companion sentence in §38, "§39 reads the rest again, and finds the one thing that does not carry over", needs the same care: §39 reads §5, §8, §9, §13 and part of §37, and more than one thing does not carry over.

### A4. §38, note under Lemma R: Proposition 2.10 does not state R1, and states R2 and "named" in one direction only

Quoted: "The items R1 and R2, named and R3 are stated, without proof, as one proposition in the paper of van Bakel, Barbanera and de'Liguoro".

The source (vanbakel-sn-lambdamu 307-312, introduced by "The following is straightforward:"): "1. If SN(xM) and SN(N), then SN(xMN). 2. If SN(M[N/x]P) and SN(N), then SN((λx.M)NP). 3. If SN(M), then SN(µα.[β]M). 4. If SN(µα.[β]M[α⇐N]L) and SN(N), then SN((µα.[β]M)NL). 5. If SN(µα.[α]M[α⇐N]NL), then SN((µα.[α]M)NL)." (Spacing normalised; pdftotext drops the arrows that mark a list of terms.)

So: R3 is there for both sorts (2, 4, 5); R2 is there in the "if" direction, one argument at a time (1); "named" is there in the "if" direction (3); R1 is not there, and neither is the item steps and appending. The digest that the writer worked from has the same reading: its table gives "R1 | unchanged | textbook".

Fix. "R3 for both sorts of head step, and the "if" halves of R2 and of named, are stated, without proof, as one proposition in the paper of van Bakel, Barbanera and de'Liguoro; R1 and the "only if" halves, which follow from R1, are not."

### A5. §39, opening, and §23, limit 4: "what a set must have", "turns out to need a fourth" - the μ condition is shown to be enough, not to be needed

Quoted (§39): "This section asks what a set must have for that rule to be true. The answer is a fourth condition, which every set defined by tests has, and which a type set built from Base and head steps alone has not." Quoted (§23): "the three conditions are read again without a change, and the rule for the new form turns out to need a fourth."

What is proved: the rule is true over TT and over MU (theorem, item soundness), and false over the collection of all type sets (item not over all type sets). Nothing shows that a collection over which the rule is true must consist of sets with the μ condition, and I do not see how to show it: what the truth of the rule forces on a set T of the collection is closure properties such as "μα.[α]u ∈ T for u ∈ T" (from x : X ⊢ x : X | α:X), one for each true judgment above the line, and it is not clear that together they give "every μ-abstraction that passes every test of T".

The note under the theorem is exact and can stay: "with the three conditions of §5 alone, read for λμ-terms as in this section, the new rule is false" is what the item proves, read as "over the collection of all type sets": the judgment above the line, x : X ⊢ x : X | α:X, is true for every collection, and the one below it is false there.

Fix (§39): "This section gives a fourth condition under which the rule is true. Every set defined by tests has it, and the smallest type set has not; with the three conditions alone the rule is false. Whether a weaker fourth condition would do was not examined." Fix (§23): "and the rule for the new form is false with the three conditions alone; a fourth is given under which it is true."

### A6. §39, lemma "What carries over", proof of operations: R3 is named where the closure condition is what the proofs use, and one fact is missing from the list

Quoted: "The proofs in §8 and §9 use, about terms, Lemma R, that a head step survives one more argument, and the β head step of an abstraction applied to an argument. §38 has all three for λμ-terms. Where one of those proofs undoes a safe head step of a term that is applied to more arguments, the head step may now be of either sort, and R3 (safe head step) of §38 covers both."

No proof in §8 or §9 uses R3. The arrow lemma undoes the head step by "the closure condition for U", and abstract by "the closure condition gives (λx.t) u ∈ U". What covers the new sort of head step in those two places is that the closure condition of a type set of λμ-terms is "read for both sorts of head step" (the definition at the head of §39) together with "a head step of either sort survives one more argument". R3 is what makes SN a type set, and it is used in the item tests. Of Lemma R the proofs of §8 and §9 use R1 only. And the Base condition of the arrow lemma uses a fact that the list leaves out: a member of Base applied to a member of SN is in Base (it is in the list of §38's remark).

Fix. "The proofs in §8 and §9 use, about terms, R1 (subterms), that a member of Base applied to a member of SN is in Base, that a head step survives one more argument, and the β head step of an abstraction applied to an argument. §38 has all four for λμ-terms. Where one of those proofs undoes a safe head step, it does so by the closure condition of a type set, which is now read for both sorts of head step."

### A7. A sixth paper was read, the example on Peirce's law is in it, and the page does not name it; Parigot's paper of 1993 is named in §39 and missing from the sources

Quoted (status section, reading copy of 04:04): "from six papers on the λμ-calculus that were read in the place of Parigot's own"; and, in the list of what is quoted: "from the papers of van Bakel, Barbanera and de'Liguoro, of Battyányi and Nour, of Nour and Saber, of David and Nour and of Matthes". The list of sources has those five. The current `src/_back.html` says "five papers", which makes the two lists agree and leaves the finding as it is: a sixth text was read for the page, a digest of it is on disk (`digests/L7-matthes-stabilization-and-roziere.md`), and the page uses what is in it.

The sixth is on disk: Paul Rozière, "Déduction naturelle classique et λµ-calcul", lecture notes, 2003 (`pdf/L7/irif-classicalded.txt`). Its lines 714-721 give the derivation of ((A → B) → A) → A with the term λy.µα.[α](y λx.µδ.[α]x), which is the term of the example "Peirce's law" up to the name δ; line 678 says that in the second-order system "les règles sur la quantification ne sont pas interprétées au niveau des termes", which is the page's "the two rules for ∀ are those of §13, in which the term does not change". The example carries no attribution, so it reads as worked out here.

Also: §39 says "papers of 1993 and 1997"; the list of sources has only the paper of 1997. (Matthes's bibliography has both: "Strong normalization for second order classical natural deduction", 1993, and "Proofs of strong normalisation for second order classical natural deduction", 1997.)

Fix. Add Rozière's notes to the sources and to the sentence of the status section; add to the example "The term is the usual one; it is in Rozière's notes, with this derivation"; add Parigot's paper of 1993 to the sources, "named for the theorem, and not obtained".

---

## Part B - rule violations

B1 (rule 13, nothing used before it is defined; rule 3). §39, proof of C2 (consistency): "By the lemma after this proof it has no closed member." The lemma "Closed λμ-terms fail a test" is used before it is stated, and is pointed at by position. It needs only §38 and the definition of a test. Move it before the theorem, and write "by the item closed terms fail of the lemma "Closed λμ-terms fail a test"".

B2 (rule 3, names not pointers). Parts of lemmas named by position although they have names: "The third item is the whole of what a μ-abstraction does" (against a test); "The first two items were found by three readers ...; the third is the writer's" (tests suffice, not every type set; not only tests); "The last item is the narrow point of this section" (not over all type sets); "The first item was found by three readers" (closed terms fail); "by the second run of the example" (§38). Other pointers: "the theorem of Parigot's that the start of this section names"; "the closing remark" four times, for the remark "What is in the literature, and what was left out"; "a reader of the two papers" in §38, where the paragraph names none.

B3 (rule 3; precision). §39, example on Peirce's law: "The two rules that §38 left out would take that term on to v." §38 left out three rules. Write "The rule that renames and the rule that removes, both left out in §38, ...". The claim also needs "if α is not free in v".

B4 (rule 1). "item" has two meanings inside one lemma and its proof: a part of a lemma ("the item closed terms fail") and a λx. or μα.[β] in front of a normal form ("a list of items", "At an item λy."). Call the second a prefix. In Lemma R the part "named" has the name of a defined thing, the named term [β]t, and states something about a μ-abstraction; call it "under μ".

B5 (rules 1, 7, 13). "free" and "bound" are used of names from the definition of appending on, and are never defined for names; §38 defines only "binds". "closed" is given its new meaning only in §39, inside the frame "Type sets and tests of λμ-terms", a section after names enter. Put both next to the definition of λμ-terms in §38: "A name α is free in a term if it occurs there as the name of a named term outside every μα. A λμ-term is closed if no variable and no name is free in it."

B6 (rule 1). §38 uses "part" beside "subterm" for one thing ("a part of a term, anywhere inside it", "The parts t, u, u1,…,un are in SN" where §2 has "The subterms"), and "hands ... to", "handed to", "takes hold of" beside the defined "appended at" (in a proof: "the μ steps hand vq+1,…,vN to every place named α"). "fails" is used in both directions and never defined ("the empty test fails it", "It fails the test λz.δ, δ"); §37 does the same.

B7 (rule 1). Three notations change meaning without a line that says so, or with one that is easy to miss. TT is the collection of §37 and, from the middle of §39, a collection of sets of other terms. Γ ⊢ t : A | Δ is the judgment itself ("written Γ ⊢ t : A | Δ", then "If Γ ⊢ t : A | Δ is derivable"), where in §13 Γ ⊢ t : A says that the judgment is derivable. "a test of A" for a type expression A in the reading of the rule, where the definition has a test of a type set.

B8 (rules 7, 8). Definitions outside a definition frame or inside a lemma: T0 and T1 are defined in the statement of the lemma on the μ condition; "Write TT for ... and MU for ..." are two definitions in one sentence of running text; the replacement "all at once" of variables by members and names by tests, which the theorem's proof writes t* and t**, is described in one sentence of the frame on judgments and is a different operation from the appending of §38 (A1). It recurs; give it a definition of its own, with a notation.

B9 (rule 6). Hypotheses left out. (i) Lemma R, proof: the identities "c[w/y][u/x] = c[u/x][w[u/x]/y] and c[γ⇐w][u/x] = c[u/x][γ⇐w[u/x]]" need y different from x and not free in u, and γ not free in u; the conditions stated before are for the other pair. (ii) R3 for the β head step also needs: if u → u′ then t[u/x] reaches t[u′/x]; the item steps and appending has that half for appending only. (iii) That t[u/x] renames bound names as well, so that no free name of u becomes bound, is not said; §1 says it for variables. (iv) "Fix a collection of type sets": nonempty, or ⟦∀X.A⟧ρ is not a type set.

B10 (rule 2, no unexplained jargon). In the closing remark of §39: "continuation-passing style" (twice), "simple types", "second-order classical natural deduction". The first can go: "translations that hand every term its continuation".

B11 (rule 11, status of every claim). Claims with no status: the note "Appending one term after another is appending the list", which the proof of against a test uses; the note under the μ condition, "A type set is test-defined exactly if every term that passes every test of the set is a member" (correct; it is a lemma of two lines); "Classical logic has proofs that System F has not" at the head of §38 (general knowledge; not in that list of the status section); the remark "What changed, and what did not", which asserts that four lines of the list of §13 hold.

B12 (rules 1, 17). "The last item is the narrow point of this section". On this page a narrow point is a frame with GOAL, TRY, BREAKS, HENCE. Either make the frame (GOAL: the rule μ true; TRY: all type sets of λμ-terms; BREAKS: x : X ⊢ μα.[α]x : X | with T0 for X; HENCE: the μ condition), or do not use the word.

B13 (rule 19; a wrong pointer). §39: "The arrow T ⇒ U is defined by the words of §8". The arrow is defined in §4; §8 itself says "The arrow was defined in §4."

B14 (rules 9, 15). No example follows the definition of a true judgment with names, where one replaced term would carry the definition (for x : X ⊢ μγ.[α]x : Y | α:X: with u for x and v⃗ for α the term is μγ.[α](u v⃗)), and none follows the definition of the μ condition; its two examples, SN and T0, are inside the lemma.

B15 (research rule 12; rule 18). The status section. (i) It lists the five results of §38 and §39 and the paragraph on μα.I as not reviewed, and lists none of them as reviewed; that part is right. (ii) Not listed: the example "Three runs", the example "Peirce's law" with its run and the example "The proof of Peirce's law fails a test"; the unframed claims of B11; the sentences that carry the results of §39 into §23 (limit 4) and §37 (the opening and the remark "What tests are for"). (iii) "What the closing remarks of §38 and §39 report": in §38 the reports are in three notes (λμ-terms, steps, Lemma R), not in its closing remark, and in §39 also in the opening, in the note on the rule and in the note under the theorem. (iv) One question under two headings: "Whether a type set that has the μ condition and is closed under steps is test-defined" is under "Not on this page" in §39 and under "Open on this page" in the status section. The current `src/classical.html` has already moved it under "Open on this page"; see Part C, item C1, for the answer. (v) "six papers", five named; the current `src/_back.html` says "five papers", and a sixth was read (A7).

On the Uses lines: both are in order by the page's convention (a section and what its sections use). §38 refers to §1, §2, §5, §13, §22, §23 and §3; all but §3 are reached from §2 and §23, and §3 is a registered pointer. §39 refers to §5, §8, §9, §13, §37, §38 and §21; all but §21 are reached from §37 and §38, and §21 is a registered pointer.

---

## Part C - correct, and could be said more simply or more precisely

The items of this part are numbered C1 to C13. The two parts of the page's theorem with the same letters are always written with their names in this report: C1 (strong normalization), C2 (consistency).

C1. The open question has an answer, and the set that gives it is simpler than T1. The status section lists as open "Whether a type set of λμ-terms that has the μ condition of §39 and is closed under steps is test-defined". It need not be. (My derivation; it has had no second reader. `check7_T2.py` checks the invariance below on all 61,101 steps of strongly normalizing terms with at most 8 nodes over one free variable and one free name.)

Let T2 be the set of the strongly normalizing terms whose head steps do not lead to an abstraction λx.s. By the five forms, they lead to a member of Base or to a μ-abstraction.

- T2 is a type set: by the three checks of the item not every type set.
- T2 has the μ condition: a μ-abstraction that passes the empty test is in SN, has no head step, and is not an abstraction. T2 contains every strongly normalizing μ-abstraction.
- T2 is not test-defined: λx.y passes every test, by the proof of the item passes all in §37, which reads word for word, and it is an abstraction.
- T2 is closed under steps. Head steps commute with steps: if t →h s and t → t′, then t′ is s, or t′ →h s′ for a term s′ that s reaches by steps. (If the step is not the head step it is inside the function part, the argument or a later argument; t′ has the same form, and its head step leads to s′; s reaches s′ by both halves of the item steps and appending, and for a β head step by the same two facts for substitution.) Now say that the kind of a strongly normalizing term is the form, abstraction, μ-abstraction or variable applied to arguments, of the term at which its head steps end. Claim: a step does not change the kind. By induction along steps, which is allowed in SN: if t has no head step, a step is inside it and keeps its form. If t →h s and t → t′: either t′ is s, which has the kind of t by definition; or t′ →h s′ with s reaching s′, so the kind of t′ is the kind of s′, which is the kind of s by the induction hypothesis applied along the steps from s, and that is the kind of t.

So T2 is a type set with the μ condition that is closed under steps and is not test-defined. Consequences for the page: the entry leaves "Open on this page" and "Not on this page"; T2 can take the place of T1 in the item not only tests, where it shortens the proof that the set is not test-defined to one line; and the sentence after the lemma can say that MU is not inside TT even among the sets closed under steps.

C2. T0 is Min, and it is the smallest type set of λμ-terms. The note says this "was not checked and is not used". It takes three lines, and M2 (generated) and M3 (smallest) of §5 read word for word: if t ∈ SN, the argument of each head step of either sort on the way is a subterm of the term it is taken from, so it is in SN by R1, and the head steps are safe; so T0 = cl(Base). A member of cl(Base) is in SN by R2 and R3. Every type set contains Base and is closed under undoing safe head steps, so it contains cl(Base). The item not every type set then says more: the smallest type set has not the μ condition. For the same reason the remark of §38 need not say that the last line of the list of §13 "was not read again": that a member of cl(S) reaches S by safe head steps is the definition of cl(S), for either sort of head step.

C3. The smallest member of MU can be named, and with it the set that ∀X.X names over MU. Let T° be the set of the strongly normalizing terms whose head steps lead to a member of Base or to a μ-abstraction that passes every test. It is a type set; every test is a test of T° (a term that reaches by safe head steps a term passing v⃗ passes v⃗, by R3 with the arguments of v⃗ added); so it has the μ condition; and every member of MU contains it. Over MU, ∀X.X names T°, which contains no abstraction at all and, by the item closed terms fail, no closed term. Over TT it names the set of the terms that pass every test, which contains λx.y. So TT and MU give ∀X.X different sets, as TT and the collections of §36 do in §37. (My derivation, not reviewed.) The proof of the item C2 of the theorem can stay as it is.

C4. Lemma R, item steps and appending. State both halves for both operations: "If t → t′, then t[α⇐u] → t′[α⇐u] and t[u/x] → t′[u/x]. If u → u′, then t[α⇐u] reaches t[α⇐u′], and t[u/x] reaches t[u′/x], by zero or more steps." The proof of R3 for β uses the last one (B9).

C5. Lemma R, R3. "safe" is needed for the new head step only if α does not occur, as for β it is needed only if x is not free: if some named term [α]w is in [β]t, the argument u is a subterm of the term after the step. Proposition 2.10 of van Bakel, Barbanera and de'Liguoro has it this way: its item 5, for μα.[α]M, has no hypothesis on the argument. One clause after "The word "safe" matters for the new head step as for the old one" would say it.

C6. §39, example "The proof of Peirce's law fails a test": "The closed term of the example on Peirce's law is in SN, by C1." It is a normal form; C1 (strong normalization) is not needed.

C7. §39, opening: "So classical logic is the first rule on this page that the largest collection of sets does not carry." Classical logic is not a rule, and "does not carry" has to be guessed. Write: "So the rule μ is the first rule on this page that is true over a smaller collection of sets and false over the largest."

C8. §23, limit 4: "There Lemma R gets one more line". It gets three things: the item steps and appending, the item named, and the new sort of head step in R3. Write "Lemma R gets three more lines".

C9. Closing remark of §39, three precisions on the reports. (i) Battyányi and Nour, and Nour and Saber, work with the other form of terms, in which μα stands in front of any term (nour-realizability 323-327; nour-saber 87-89); the paragraph on μα.I describes that form without saying that these are the papers that use it. (ii) "a finite list taken from the orthogonal": in Battyányi and Nour it is an initial part of such a list (Theorem 3.15), and in Nour and Saber the lists may contain names as well as terms (Definition 3.2, the sequences over terms and μ-variables). (iii) "So his sets are sets defined by tests" is the page's inference from two descriptions at second hand; "So, on these accounts, ..." keeps it one.

C10. Closing remark of §39, on van Bakel, Barbanera and de'Liguoro: "Their theorem is the counterpart of §21". The report is exact. One caution that a reader of the paper for this page recorded and that I confirmed by hand: their Lemma 2.17 is false as printed. (ax) gives x : ω→ν ⊢ x : ω→ν |, (abs) with κ = ω gives ⊢ λx.x : (ω→ν)×ω→ν |, and by Definition 2.11 the stack δ : δ is in the set of (ω→ν)×ω, while (λx.x) δ δ is not in SN. The theorem may well stand; the page quotes it without having checked the proof, and could say so.

C11. Front of the page. "The one choice in the definition is dissolved, not defended ... each is closed under the arrow and under intersections, each carries the theorem" is true for the rules of System F. §39 shows a rule for which the choice matters. One clause there, "with the rule μ of §39 the largest collection does not", keeps the front in step with §39, and "What this page claims" does not mention §38 and §39 at all.

C12. §39, definition of the rules. A sentence that a name context may list names that the term does not use, as a context may, would explain line 1 of the example on Peirce's law, where γ : Y is in the name context of x : X before any μ, and how a μα whose name does not occur gets a type expression.

C13. §39, the lemma on closed terms, case "q + 1 is p and m ≥ 1". It is correct. It is the only case in which the run uses a term of the test beyond the place k + 1 (it uses vp+m), which is why N has m in it, and an example would help a reader: for μβ.[β]λx.μα.[β](x x) one has k = 1, m = 1, N = 3, p = 1, q = 0, the test is λz.δ, δ, δ, and the run reaches v1 v1 v1 v2 v3, then δ v1 v2 v3, then v1 v1 v2 v3, then δ δ δ.

---

## Verdicts, one line per re-derived result

§38, Lemma R for λμ-terms.

- steps and appending: correct as stated and proved. Both identities were checked by induction, including the cases [γ]r and [α]r of the second; the β and μ cases of "t → t′" follow from them as written. By program (`check4_lemmaR.py`): no failure in 32,934 and 16,328 instances of the two identities, in 32,789 and 16,328 instances of the pair for t[u/x], in 60,000 instances of the list identity, in 6,379 steps of t and in 3,957 steps of u; the side conditions are needed (a counterexample to the second identity with γ free in u is printed by the script) and as stated they are enough.
- R1 and R2: correct.
- named: correct, for β and μ.
- R3: correct for both sorts; the proof for the μ head step is complete. For β the proof of §2 holds with the two facts for substitution (Part C, item C4).
- The definition of appending and of the μ step: the side conditions on bound names are enough. "Appending one term after another is appending the list" is right as stated, under the standing condition that α is not free in the terms of the list, and false without it (A1).
- Examples: the three runs are right. (The evaluators cannot decide m m ∉ SN, because the run grows and never repeats a term; the page's reason, that the term reached contains m m, is correct.)

§39, What carries over to λμ-terms.

- operations: correct. The proofs of §8 and §9 use only what §38 provides; the proof's last sentence names the wrong fact (A6).
- tests: correct; the three conditions, the arrow, the intersection and the smallest set read word for word, with R3 of §38.
- against a test: correct in both directions, n = 0 included. By program (`check5_against_test.py`, μ-abstractions with a body of at most 5 nodes, tests of at most two terms from a list of eight, some with a free name): 220,491 instances agree (218,934 pass, 1,557 fail), 1,575 undecided, none disagrees.

§39, Which type sets have the μ condition.

- tests suffice: correct.
- not every type set: correct. T0 is a type set, and it is Min (Part C, item C2).
- not only tests: correct. T1 is a type set, has the μ condition for the reason that it contains every strongly normalizing μ-abstraction, and is not test-defined.
- operations: correct, the arrow for any type set T on the left. MU is nonempty, closed under ⇒ and under nonempty intersections; Lemma N and the four facts need nothing else of the collection, and C2 (consistency) needs only that one member has no closed member.

§39, theorem "The rules with μ are true over sets with the μ condition".

- soundness: true. The five rules of §13 are proved as written; the rule μ is proved except for the step of A1.
- C1 (strong normalization): correct.
- C2 (consistency): correct; it uses a lemma that is stated after it (B1).
- not over all type sets: correct, and exactly what the note under the theorem says (A5 is about the opening paragraph).
- The example on Peirce's law: each of the six lines is an instance of the rule named, with the rule μ used once with β = α and B = A (line 5) and once with β different from α (line 2). The run with λk.k v reaches μα.[α](μγ.[α]v) in two steps. The term fails the test λz.δ, δ as described; both by program as well.

§39, Closed λμ-terms fail a test.

- closed terms fail: correct as stated and proved. Followed by hand on six closed normal forms (k, m, N, p, q as in the proof):
  - λx.x: 1, 0, 2, 1, 1; test δ, δ; (λx.x) δ δ → δ δ.
  - λx.λy.x y: 2, 1, 4, 1, 2; test λz.δ, δ, δ, δ; reaches (λz.δ) δ δ δ, then δ δ δ.
  - μα.[α]λx.x: 1, 0, 2, 1, 1, with qα = 0; test δ, δ; reaches μα.[α]((λx.x) δ δ), then μα.[α](δ δ).
  - μβ.[β]λx.μα.[β]x: 1, 0, 2, 1, 0, with qβ = 0, qα = 1; this is the case q + 1 = p and m = 0; test δ, δ; reaches μβ.[β]((λx.μα.[β](x δ δ)) δ δ), then μβ.[β](μα.[β](δ δ δ)).
  - λx.μα.[α](x (λy.y)): 1, 1, 3, 1, 1; test λz.δ, δ, δ; reaches μα.[α]((λz.δ) I δ δ), then μα.[α](δ δ δ).
  - λf.μα.[α](f (λx.μγ.[α]x)): 1, 1, 3, 1, 1; test λz.δ, δ, δ; reaches μα.[α]((λz.δ) (λx.μγ.[α](x δ δ)) δ δ), then μα.[α](δ δ δ).
  By program, on all 1,259,303 closed normal forms with at most 10 nodes: with N distinct variables in the place of the test, the proof's steps end at vp u1′…um′ vq+1…vN with the p and q of the proof, and no λ runs out of arguments; with the proof's test the same steps reach a term containing Ω, in at most 29 steps. The three cases of the proof occur 802,943, 433,811 and 22,549 times. I found no closed normal form on which the recipe fails, and the argument leaves no room for one: q never exceeds the number of λ passed, and p + m ≤ k + m < N.
- a free name passes: correct.
- The paragraph on μα.I in the closing remark: correct for β and μ; (μα.I) v → μα.I for every v. The rule of Battyányi and Nour asks the type expression ⊥ of the term under μα, so μα.I has no type expression there; as the paragraph says, it is the proof of C2 (consistency) that would have to change.
