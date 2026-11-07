# Review 3 of "The Narrow Path" (reading v27)

Fresh reader. All 39 sections read in order, every folded proof opened. The proofs marked "worked out for this page and not reviewed" were re-derived by hand: the generation lemma (§3), the union lemma (§8), the characterization theorem (§21), the Cedille sections (§28–§30), the equalities (§35), and all of §37. Findings are numbered within each part, most important first. Things that are fine are not listed.

Verdict on the re-derived proofs in one line each, before the findings:
- §3 generation lemma: correct.
- §8 union lemma: correct.
- §21 characterization theorem: correct, including both head-step cases and the `∧ in` / `→ out` bookkeeping; the three admitted facts about derivations are the standard admissible rules and are true.
- §28, §29: correct; the Nat′ construction checks out line by line.
- §30: the five-rule analysis and both counterexamples are correct; the derivation of `(λz.I) Ω : ∀X.X→X` is correct.
- §35: the lemma "type sets tell terms apart" is correct; one claim about safe head equivalence is false (A3).
- §37: the commuting lemma, the chain, the four conversions, the bijection with sets of values and "each family carries the theorem" are correct as stated and proved. Two sentences around them are wrong (A1, A2) and one claim is unsupported (A4).

---

## Part A — Errors

**A1. §37, example "Three type sets, one of each kind": the stated reason that ID is a candidate does not prove it.**
Quote: "ID is a candidate, by the lemma in §36 and the closure of ID under steps, which follows from the lemma on preservation below."
Preservation says: if T and U are candidates then T ⇒ U is a candidate, and an intersection of candidates is a candidate. ID is `⋂C (C ⇒ C)` with C over *all* type sets (§8), and for a type set that is not a candidate, C ⇒ C is in general not closed under steps: with C = Gen({I I}), the term λx.I I is in C ⇒ C (it sends everything to I I) and steps to λx.I, which is not in C ⇒ C (it sends I I to I ∉ C). So ID is an intersection of sets most of which are not candidates, and preservation says nothing about it. The conclusion "ID is a candidate" is in fact true, but it needs its own argument (every t ∈ ID satisfies t u →h* u for every value u, and a step in t leaves no residual inside the final copy of u; this uses the commuting lemma and a residual argument that the page does not have). Fix: replace the example by one the section can prove in one line, e.g. "TI = Gen({I}) is a candidate: its only value I has no step (item *candidates* of the lemma on values)", or SN and Min by *same ends*. If ID is kept, give the proof or mark the claim unproved.

**A2. §37, lemma "Each family carries the theorem", last sentence of the statement: the claim about candidates and the dependent arrow is false.**
Quote: "For the dependent arrow of §26, the candidates need the family constant along steps already for the lemma that the dependent arrow is a type set; the other two families do not."
Let T be a candidate and V any function from terms to candidates. Π_{u∈T} V(u) is a type set by §26. It is closed under steps: if t ∈ Π and t → t′, then for every u ∈ T, t u → t′ u and t u ∈ V(u), so t′ u ∈ V(u) by CR2 for V(u). By the lemma of §36 it is therefore a candidate. Constancy of V is never used. (It is needed only when one proves CR3 directly, Girard-style, because then one meets t u′ with u → u′; the page's own lemma makes that route unnecessary.) Delete the sentence here and the echo in the remark ("with the one exception noted above for the dependent arrow"). What *is* true, and worth saying instead: in every family, the self type and the dependent intersection need V constant along safe head steps, and term conversion needs it along all steps.

**A3. §35, definition "The equality type set of a relation": safe head equivalence does not have the first property.**
Quote: "Safe head equivalence has the first and not the second".
The first property reads: if u → u′ then u R v if and only if u′ R v, for any step. Take u = λx.K x, u′ = K, v = K. Then u′ R v holds (K R K), and u R v fails: λx.K x and K have no head step, so they are not joined by safe head steps (the page itself says so three paragraphs earlier). So safe head equivalence has *neither* property, and ER for it is not constant along steps, so the lemma "Every such relation can be added" does not apply to it. Replace by: "Safe head equivalence has neither: λx.K x → K breaks the first, and (λz.y) (x x) with δ for x breaks the second." Convertibility remains the only relation on the page that qualifies; say so.

**A4. §37 asserts as a fact what §36 says was not checked.**
§37: "The sets that type expressions name change with the family, because ∀ ranges over fewer sets. The theorem does not."
§36: "With the two collections a type expression names two sets, because ∀ is an intersection over a different collection in each. This page did not check whether the two sets can differ."
Both cannot stand. No example of a closed type expression naming different sets under SAT, HC and CR is given anywhere, and the obvious candidates do not work: ∀X.X names Min in all three (Min is in each family and is the least member), and ∀X.X→X names the same set in all three (a member of the CR version satisfies t u →h* u for every value u, which already puts it in the SAT version). Whether *any* System F type expression separates the families is, as far as this reviewer can see, open on the page. Write "may change" and list it as unknown in the status section, or produce the example. This matters for rule 11: without an example, the "price" of stepping down the chain ("some instances of ∀") is asserted, not shown.

**A5. §22, §36 and the status section give three different accounts of Riba's result, and the strongest is probably wrong.**
§22: "Riba proved it in 2007 for a general setting, where the opposite had been commonly believed."
§36: "Riba proved this in 2007 for a general setting, where it had been commonly believed false".
Status: "That unions of candidates are candidates in general is Riba's theorem".
Riba's abstract (On the stability by union of reducibility candidates, 2007) states an *if and only if*: candidates are stable by union iff they are exactly the nonempty sets of terminating terms downward-closed under a weak observational preorder; he shows this holds for Curry-style second-order λ-calculus, i.e. exactly this page's setting, and that there the candidates are the saturated sets stable by reduction. "In general" and "for a general setting" say the opposite of an iff whose point is that the property can fail elsewhere. "Commonly believed false" is a claim about the literature with no source. Make the three sentences one, quoting the abstract, and drop the belief claim unless a source is given.

**A6. §7: "No later proof uses Lemma E or Lemma L" is false.**
§35's proof of "Type sets tell terms apart" uses L3 and L2 ("by L3", "by L2 applied in both directions"), and §37's order paragraph uses L1. §7 is correctly listed as used by §35; only the sentence is wrong. Fix the sentence; better, see C4.

**A7. §16: a nontrivial claim about weakly normalizing terms has no proof and no status.**
Quote: "The weakly normalizing terms are another such set."
Property (i), "if t x is in the set then so is t", is not obvious for WN. It is true (a reduction of t x in which x is only ever an argument lifts to a reduction of t, because substituting a variable creates no redex and the head redexes of t x are those of t until t is an abstraction), but it needs that sentence, and the table row "weakly normalizing terms — a normal form exists" is a theorem that rests on it. Mark it "worked out" or "quoted from Gallier/Mitchell" and give the one-line reason.

**A8. §32: a standard fact is asserted inside the theorem's statement without proof or status.**
Quote: "Every type expression in a judgment has the kind ∗, and every type expression along a chain of steps is well formed."
The second half is subject reduction for the kinding rules (the simply typed λ-calculus one level up). The conversion rule needs it: B must have kind ∗ for Γ ⊢ t : B to be a judgment and for ⟦B⟧ρ to be a set at all. Mark it as quoted (textbook) or prove it in two lines in the remark "What was not needed", where the same calculus is discussed.

**A9. §37, commuting lemma: the proof of the second statement skips the induction it needs, and the lemma is textbook.**
Quote: "The second statement follows by induction on k, one step of t → t′ at a time."
The claim is: t →h^k r safe and t →* t′ imply t′ →h^{≤k} r′ with r →* r′. After one step t → t″ the one-step lemma gives t″ →h t1″ with t1 →* t1″, but t1″ is not on the original head reduction, so the remaining steps t″ →* t′ cannot reuse the hypothesis; the proof needs induction on k with an inner induction on the length of t →* t′ (or induction on k applied to the pair t1, t1″ first). Four lines, but the page's standard (writing rule 12) is "no skipped step". Separately: this is the standard fact that head reduction commutes with internal reduction (the core of the standardization theorem, in Barendregt's and Krivine's books). Attribute it as textbook and keep the proof; "worked out for this page" claims more than is true.

**A10. §37, order paragraph: "Min is the smallest open set" is wrong, and the type sets are not all the open sets.**
In the topology whose open sets are the subsets of SN closed upward along safe head steps, ∅ is open and is the smallest open set; the type sets are the open sets that contain Base (equivalently, that contain Min). Say "the open sets that contain Base, and Min is the smallest of them".

**A11. §30, lemma "With β and φ, a closed term that is not in SN is typable": the last clause of the statement overclaims.**
Quote: "no semantics that proves C1 can make φ true."
The derivation uses β as well as φ (or δ, in Stump's version). A semantics that falsifies β (does not put I into every true equation) is not excluded by this lemma. Say "can make both β and φ true" — which is what the proof shows, and what the side-by-side table then correctly says.

**A12. §35, lemma "Every such relation can be added", item *false rules*: the hypothesis is one-sided.**
Quote: "The rules ρ and φ are false, for every R that does not relate K and I."
The ρ counterexample uses ER(K, I) = Min and the φ counterexample uses ER(I, K) = Min. R is not assumed symmetric, so the hypothesis must exclude both orders.

**A13. §25 uses a notation that §29 defines.**
Quote: "StepP = ⋂y∈Nat (P(y) ⇒ P(S y))". The intersection over the members of a type set is defined in §29 ("DEFINITION · INTERSECTION OVER THE MEMBERS OF A TYPE SET"). Writing rules 8 and 13. Either define it in §24 (it is one line and needs only the intersection lemma) or write the §25 example with ⋂C over constant families and say what is lost.

**A14. §37: "The first two names are for this section; the letters SAT and CR are the usual ones" contradicts itself** (SAT is one of the first two). Presumably "HC is this page's; SAT and CR are the usual letters."

**A15. Two garbled sentences.**
§35: "So every type set contains I I if and only if it contains I is false" — should read "So 'every type set that contains I I contains I' is false".
§39: "Reading the two side by side shows which asks for make the definition here more delicate." — missing words.

**A16. §30, remark on Stump's semantics: "The empty set is a type."** Bare "type" (writing rule 1), in a sentence that is the page's own, not a quotation. "names a type set" is false there; write "is allowed as the set a type expression names".

**A17. §1: the exclusion of η is a modeling choice that is not marked as one.**
Quote: "There is one rewrite rule, called β." Its consequences surface only in §35 ("the η step from λx.K x to K is not one of them") and in the remark that extensionality has no home here. Rule 1 and rule 11: mark the choice in §1, name what it costs (λx.K x and K are told apart by type sets; no function extensionality), and say in one line why the page does not add η (the closure condition and Lemma R would have to be redone for η, as limit 4 says for pairs).

**A18. §37, last remark: a theorem is claimed in passing with no proof and no status.**
Quote: "The binary version of the semantics, in which a type expression names a relation between terms, is the same theory run on pairs of terms, and for the head-closed family it is a family of relations between values". Nothing on the page supports "the same theory run on pairs" (it needs that Lemma R, substitution and "a head step survives an argument" hold for pairs, and that the arrow of relations is a relation of the same kind); the status section does not list it. Either mark it "worked out in conversation, not on the page" per rule 12, or reduce it to "that version is not on this page" and nothing more.

**A19. Counts of what needs "constant along steps" disagree.**
§24: "Three things need families to be constant along steps: the self type of §25, the rule of term conversion in §27, and the dependent intersection of §28." §27's remark: "Among the five rules of this section, only term conversion needs it. The price is paid in one more place: '∀ out, for families' has to show that w ↦ ⟦B⟧ρ[x↦w] is constant along steps". §29's lemma also uses N4 for the implicit product. And §25/§28 use constancy only along safe head steps. Make one list, in §24, with the exact hypothesis each user needs.

**A20. "Uses" lines that miss a section whose result is used (writing rule 19).**
- §22 uses "the laws of ∩ in §20" as inclusions for subtyping; §20 is not in §22's Uses and is not reachable from it.
- §30 rests on "Narrow point 2 in §6 showed what that costs"; §6 is reachable only from §15.
- §16 uses "limit 2 in §23" (forward).
- §22's CAUTION uses "the lemma in §36" (forward).
- §37's remark makes a claim about "The additions of §22, §25, §19 and §29"; §19, §25, §29 are not reachable from §37.
- §33's MONOTONE and TERMS rows use §22's μ and §24's families; neither is reachable from §33.
A program checked the Uses lines, per the status section; it evidently counts these as passing mentions. They are not: each is a result being relied on.

**A21. Minor status gaps.** §11's counting lemma, §23's limits 2 and 4, §26's two examples, and the claim in §13's Church-style remark are not in the status list (they are presumably "worked out for this page"). §21's "three routine facts about derivations" should be marked "standard, proofs omitted" rather than left as an IOU.

---

## Part B — The research rules

### Rule 1 (justify or dissolve an arbitrary choice at the foundation)
1. §1, β only: see A17. Not marked, not justified, not dissolved.
2. §24, "A family is defined on all terms, and not only on the members of some type set". A reason is given ("so the families are fixed before any type set is picked") but no trial of the alternative and no statement of what fails if families are defined on a type set only. The price appears two sections later (§25: "In System S a family accepts only the terms it is declared for"). Either show the alternative breaks something (which lemma?) or say it is a presentation choice and the mathematics is the same.
3. §24, "constant along steps". Justified for term conversion (§27's example). For the self type and the dependent intersection, constancy along *safe head steps* suffices (their closure-condition proofs use only s →h s′). So the clause is stronger than two of its three users need and the choice between "head steps" and "all steps" is settled by convenience. Rule 10 as well.
4. §27, "ρ(y) = y for every term variable y that is not in Γ": unexamined. Say why (so that t[ρ] is determined by Γ, and so that C1 can replace every variable by itself) or drop it by requiring FV(t) ⊆ Γ.
5. §30, "E(u, v) is SN if u and v are convertible, and Min otherwise": the two values are not justified. One sentence does it: SN because β needs a closed member and SN is the least committed set with one; Min because δ needs the smallest type set. Without it the reader cannot tell a definition from a choice.
6. §31, kinds as plain sets: dissolved in §33's remark ("Two readings of kinds"), which is good, but two sections after the choice. A one-line pointer in §31 ("§33 gives the other reading and says which question each answers") closes the gap.
7. §5's definition is the model case of this rule: W1–W5, the narrow points, E1–E4 and §37 together justify every clause and dissolve the alternatives. This is the page's best work.

### Rule 2 (define once, derive everywhere)
1. **Four intersections, four definitions, four copies of generalize/instantiate.** ⋂C over type sets (§8), ⋂V over families (§24), ⋂u∈T over the members of a type set (§29), ⋂c∈κ over a kind (§31). §31 says it itself: "No new lemma is needed ... They are still definitions read backwards." Then there should be one definition — the intersection of a nonempty indexed collection of type sets — and one pair of facts. See C1.
2. **Lemma N is extended six times** (§19, §27, §28, §29, §30, §32) and "the soundness theorem and both corollaries hold" is repeated five times, each time with the same three sentences ("N1 ... by the lemma; N0 and N2 unfold the new clause"). §18 states the interface in prose ("One lemma that the new set satisfies the three conditions. One membership fact per rule. One more routine case in Lemma N.") but not as a lemma that can be invoked. See C2.
3. **Arrow and dependent arrow.** §26 proves the dependent arrow by "The proof of the arrow lemma goes through with V(v) in the place of U". That is the right transfer, but the lemma is stated for a family when the proof works for any function from terms to type sets (rule 10), and the four facts are restated.
4. **Two natural-number constructions** (§25 Nat with a least fixed point; §29 Nat′ without). §29 explains the contrast well; but both are full examples with full proofs. See C7.
5. **Reynolds's theorem** is in §36 ("Any set, with all functions", with a proof sketch) and again in §38's table. **The strength table** of §34 restates §17. **§15's first table** restates §4's list and §6's opening paragraph.
6. **E (§30) and ER (§35):** §35's lemma re-proves §30's lemma with R for convertibility ("The proofs of §30 go through with R in the place of convertibility"). Concrete before general is a defensible order, but then §30's lemma should be the instance and §35 the one proof, not two proofs.
7. **§36's side-by-side table and §37's lemmas** say the same things (closed under unions, every variable a member, closed under steps, proves the theorem) in two formats.

### Rule 3 (elegance is evidence, not decoration)
1. §37, the order paragraph ("open sets of a topology ... complete, atomic Boolean algebra up to Min ... CR is the open sets that are also closed downward") and "In standard terms, each of HC and CR is both a reflective and a coreflective subfamily of SAT": no result uses any of it. The rule says one sentence; this is five, with four unexplained terms.
2. §7 Lemma E: four "other words" for the definition, with proofs; only E4 is used (inside L1). Demote E1–E3 to a remark.
3. §20, *largest inside* and *repeat*: properties of ∩ on any two sets, given names and a proof line each.

### Rule 4 (test claims against deliverables; retract what fails)
1. §22, CAUTION: "This lemma depends on the exact conditions chosen in §5. Type sets are closed under union, by a proof of one line." The next sentence shows candidates are closed under union too. So the lemma does not depend on the conditions of §5; the one-line proof does. The advantage is claimed and half-withdrawn in the same box. Withdraw it cleanly: "Both collections are closed under union; for saturated sets the proof is one line, for candidates it goes through the lemma of §36."
2. §37, "The sets that type expressions name change with the family": no deliverable is named that gains or loses from this, and no example exists (A4).
3. §37, remark: "every set that the theorem forces to be present is there" — which theorem forces which set? The narrow points show the *conditions* cannot be weakened in certain ways; they do not show that every type set is "forced to be present". Say "the largest of the three families" and stop.
4. Good examples of the rule applied: §16's table of Good (each row names what the theorem then shows); §36's "Neither is better throughout"; §30's "So the failure is not a defect of this semantics. It is in what the rules ask for."

### Rule 5 (a map, not a monograph)
1. The cut threads are named honestly: annotations (§13, §27, §34), binary semantics and parametricity (§35 remark, §37, §38), CIC (§34), λPω/λC (§34 "sketch"). Good.
2. §30 is the one section written at monograph depth: five rules quoted, two counterexamples, a derivation, Stump's own semantics compared on three points, a table. It earns its place as the payoff of Part V, but §38's eight-row table of other semantics, "from general knowledge of the literature and not checked against sources", is a map drawn from memory; an expert will find a nit in every row (e.g. "Domains and coherence spaces — Girard's version led to linear logic" is a slogan, not a semantics). See C10.
3. The dependency graph is acyclic but the Uses lines under-report (A20).

### Rule 6 (trusted by experts, understood by learners)
1. Status missing or wrong: A4, A7, A8, A9, A18, A21.
2. Attribution: the commuting lemma is textbook (A9). The route of §21 (SN generated by three rules ⇒ typability by induction on the rules) is the route of van Raamsdonk–Severi–Sørensen–Xi and of Valentini's "elementary proof"; "The proof given in §21 was written for this page" is true of the text and should say "the route is known; the text is ours".
3. "head-closed ... We found no name for it in the literature." Honest, and the right form of words. The nearest neighbours should still be named so an expert can place it: sets of the form {t : eval(t) ∈ W} are what biorthogonality-based proofs and ⊤⊤-closure produce on closed terms (Pitts; Krivine's truth values are closed under head expansion, and Riba's observation quoted in §38 is exactly that). One sentence.
4. Learners: §37 uses complete lattice, sublattice, reflective/coreflective, topology, open set, atomic Boolean algebra; §35 uses "Leibniz equality" and "observational equivalence in the sense of Böhm and Morris"; §38 uses biorthogonality, Kripke logical relations, partial equivalence relations, coherence spaces, domains — none explained plainly before use (writing rule 2). The page's own rule is one plain explanation before the term; the three-families section should be the showcase and is the worst offender.
5. "The lemma is a known fact, due to van Raamsdonk and Severi" (§3) and "Girard's reducibility candidates are defined by a different and stronger list" (§5): good; experts will trust these.

### Rule 7 (answer the real question)
Not testable on the page. §37's opening correctly reads "which of Tait's, Girard's and the in-between sets is fundamental?" as "is the choice forced?" and answers it.

### Rule 8 (argue both sides, then neither)
1. §37's remark gives the case for SAT ("the largest ... nothing else is asked") and its price (limit 3); the case for CR ("Candidates keep a term while it runs. And CR3 names no form of term") sits in §36, and the case for HC (it is what programming-language semantics builds; the bijection with sets of values) is implicit in the lemma. The three cases should be in one place, followed by the reading with no side: an operational-semantics reader will take HC, a Girard reader CR, a learner SAT because it asks least; the theorem does not care. Three sentences.
2. §30's "Measured against this page. Three differences, each of which answers one failure above" is the rule done right.
3. §13, Curry style: the case for is given; the case against (nothing a machine can check; annotations uncovered) is scattered over §27 and §34.

### Rule 9 (fit before build)
1. §20 "Laws of the intersection": the two nontrivial laws exist to motivate subtyping ("For this reason presentations of intersection types often add inclusions ... That is subtyping, which §22 adds"). The section is a sideline whose point is made in §22. See C6.
2. §33's list of five new kinds: BOUNDED and PAIRS are never used again; MONOTONE is a restatement of §22; TERMS and LEVELS are used. Keep the two.
3. §38's table: weakly related rows (domains, coherence spaces) are kept as map entries; they would be better as one line under "not treated".

### Rule 10 (the least committed object)
1. §26's lemma asks for a family; any function from terms to type sets works (the proof says so). State the weaker hypothesis.
2. §24 imposes constancy along all steps as part of what a family *is*; §25 and §28 need only safe head steps. The invariance "constant along all steps" is an option that term conversion adds, not an axiom families must carry. See C12.
3. §30: SN is the least committed choice for a true equation; say so (B1.5).
4. §5 and §37: the rule applied as intended — SAT is the largest family, and HC and CR are "that one plus a named condition". This is right and well said.

### Rule 11 (name the price next to the gain)
Prices stated well: ∧ (undecidability, §21), μ (monotone only, limit 2), ∃ (subject reduction, limit 3), E (ρ and φ fail), impredicativity (§17), CR (fewer sets for ∀), HC/CR in the chain remark, kinds (one more power set), the implicit product ("in return asks that t does not use x").
Missing or displaced:
1. §1, β only: no price named (A17).
2. §24, "constant along steps": the gain is stated; the price — functions like "SN if u is the term I itself" are excluded, so ∀P ranges over fewer things and EQ(u, v) is correspondingly weaker — is shown by the example "A function that is not a family" but never called a price.
3. §27, "a family variable takes one term, and a type expression is never abstracted over a term": the price (the hollow corners of the cube) is named in §34, seven sections away.
4. §31, kinds as plain sets: the price (power sets in the metatheory; narrow point 7) is in §32's last paragraph and §33.
5. §13, Curry style: the price (nothing a machine can check; annotated runs covered only by a remark) is named in §27 and §34, not in §13.
6. §37, HC: rule 11 lists "a loss of a literature anchor" as a price. HC has no name in the literature; that is its price and should be stated as one in the chain remark, next to "an invariance of membership".
7. §25, self types: the price — the premise "the type expression is well formed" is dropped, so "nothing a machine could check" — is in the "Worked out" paragraph, not next to the rules.

### Rule 12 (keep the review debt visible)
1. The status section exists, is detailed and is mostly current. Gaps: A7, A18, A21; and §37's "names change with the family" is stated as fact while §36 lists it as unchecked (A4).
2. "Errors found while re-reading are fixed and reported, not silently corrected": the page carries no errata. If earlier reviews found errors (the status section mentions a "last independent review"), list what was fixed; if none were found, say so.
3. The status section groups "The section on equalities was worked out for this page" under "Cedille's constructions"; it belongs under its own heading.

### Writing rules (checked in passing)
- W1: "family" has two meanings in §37 — §24's function from terms to type sets ("the candidates need the family constant along steps") and a collection of type sets ("the family of all type sets", "The three families"). §36's title already uses "collection"; use it. "value" is defined in §37 as a strongly normalizing abstraction, used in §5's picture (defined inline, fine), and used in §36's table as "values of any sort". Bare "type" in §30 (A16).
- W3: pointers — "the lemma above" (§35, §36), "the one exception noted above" (§37), "the lemma on preservation below", "The lemma on values below" (§37).
- W4: E1–E4 and L1–L4 are bare letters; every other lemma's parts have names.
- W7/W16: the family VI is defined inside an example frame in §24 and used in a proof in §30 ("ρ(P) = VI, the family of §24"); §30's proof of φ cites "as the example of §8 shows" for K ∉ ID. Proofs depend on example frames. Make Vv a definition (it is used in §24, §26, §30) and give K ∉ ID a one-line proof where it is used.
- W8/W13: A13; §16 uses limit 2 of §23; §22 uses §36's lemma.
- W12: A9.
- W17: the page explains its apparatus at the top ("Rest on a box to see what that one section needs", "Each box is a link", "FOLD ALL PROOFS") and in §1 ("Copies are shaded, here and in later examples"); §5 explains itself ("That is why this page has many examples, and why several of them build type sets by hand").
- W19: A20.

---

## Part C — Larger factorings

**C1. One intersection.** In §8 define the intersection of a nonempty indexed collection: for a set I ≠ ∅ and a function F from I to type sets, ⋂_{i∈I} F(i). Prove the intersection lemma once. In §9 state generalize and instantiate once, for any I. Then ⋂C (I = all type sets), ⋂V (I = families), ⋂u∈T (I = T), ⋂c∈κ (I = κ) are four instances named in one line each where they first appear. Removes: §24's lemma and its proof, §29's lemma, §31's "No new lemma is needed" paragraph, A13. Rule 2. Cost: §8 is on the main line and gets one more abstract definition; keep ⋂C as the stated instance with the example ID so that the learner sees the concrete case first (writing rule 9). Touches §8, §9, §24, §29, §31. Worth it.

**C2. The addition lemma.** Turn §18 into a lemma. Statement: an addition is a new form of type expression with a clause that builds its set from the sets (or families) its parts name. If (type set) the clause gives a type set from type sets and families, (substitution) the clause commutes with substitution of type expressions and of terms, and (steps) the clause is constant along steps of the terms inside it, then Lemma N holds for the extended language, and if each new rule is true as a statement about the sets, then the soundness theorem and both corollaries hold for the extended system. Proof: the induction of §10 has one more case, which is the hypothesis. Then §19, §22, §25, §28, §29, §30, §32 each discharge the three obligations and the rules in a few lines, and the six repeated paragraphs go. Rule 2 and rule 11 (the price of a rule is stated once, as the lemma's hypotheses). Cost: §18 becomes real mathematics instead of three paragraphs of prose; the notion "clause" has to be made precise (a function on sets/families). Touches eight sections, all by deletion. Worth it; this is the single largest simplification available.

**C3. Reorder Part V.** §25 (self types, a Fu–Stump notion) currently precedes the dependent arrow and dependent types themselves. Since §25 is used only by §28, move it after §27: §24 families, §26 dependent arrow and equality, §27 names and rules, §25 self types, §28, §29, §30. Rule 6 (the standard object first) and writing rule 9. Cost: renumbering only. Worth it.

**C4. Move "type sets tell terms apart" to §7 as L5** (its proof is two lines from L2 and L3), and make §35 a section on equality type sets only (the ER lemma with E as its instance, EQ, "when two type expressions name one set"). §37 then uses §7 and §36, not §35, and A6 disappears. Rule 13 (a fact sits where it is used), rule 5 (one topic per section). Cost: §35 loses its one lemma; §7 gains the fact that explains why Lemma L matters. Worth it.

**C5. Reshape §36–§38.** §36 = reducibility candidates only: definition, the lemma (candidates = type sets closed under steps), the example, "either collection proves the theorem", the union remark with Riba stated once (A5). Move "Plain sets" (both versions), Reynolds, Pitts and the plain-set column of the table to §38, where Reynolds already appears. §37 keeps the chain and absorbs the SAT/CR rows of the side-by-side table (they are its lemmas). Rule 2 (Reynolds once; the table once), rule 5. Cost: §38 grows by one subsection; the reader of §36 loses the three-column overview, which §37's "three readings" replaces. Touches §36, §37, §38. Worth it, medium.

**C6. Merge §20 into §22.** Open the subtyping addition with the two laws that matter (*same input*, *same result*), the example "∧ records which input goes to which result", and "A law that is true and not derivable" as the reason subtyping is added. Drop *largest inside* and *repeat* (or one line). Keep the non-idempotent remark as a remark in §19. Rules 9 and 13. Cost: §22 grows by half a page; §21's reference to "the law that is true and not derivable, in §20" moves. Worth it.

**C7. One Nat.** Keep §29's Nat′ (Stump's, no fixed point) as the worked example; reduce §25's Nat to a remark: "with self types alone, induction needs the least fixed point of §22, because the step function quantifies over Nat itself; §29 removes the circle by quantifying over cNat." Rule 2, rule 5. Cost: §25 loses its only substantial example and becomes short; the reader does not see the fixed point used in anger. Medium — do it only if §25 is also demoted (C3 puts it where it can be short).

**C8. Name the interface once.** §37's proof of "each family carries the theorem" says: "The proofs in §10, §9 and §13 use three things about the family that ∀ ranges over". §16 says the same about SN: "It uses three facts about the set SN". Both are transfer lemmas whose interface is stated inside the proof. State the interface for the range of ∀ as a remark in §11 or §13 ("What ∀ needs of its range: a collection of type sets closed under ⇒ and under nonempty intersections"), so that §37 cites it and so that an expert sees at once that SAT, HC, CR and every "collection closed under ⇒ and ⋂" carry the theorem. Rule 2. Cost: one remark. Worth it.

**C9. Merge §16 and §17**, and move §34's strength table there: "What the proof used of SN, and how strong it has to be". Both are retrospective, both are used by nothing later, and §34 says "§17 treats System F. The same pattern shows across the systems." Rule 2. Cost: one longer section; §34 loses a table it only quotes. Medium.

**C10. Shrink §38** to the rows the page can vouch for and the paragraph "which definition each grows from" folded into the table as a column (rule 2). Rows "domains and coherence spaces" become one sentence under a "not treated" line. Rule 6: a table "not checked against sources" is the least trustworthy thing on an otherwise careful page. Cost: less map. Worth it.

**C11. Cut §33's list of kinds** to TERMS and LEVELS, with BOUNDED, PAIRS, MONOTONE in one sentence ("any nonempty set of members of a kind is a kind, for instance ..."). Writing rule 15. Cheap.

**C12. Make constancy an option, not an axiom.** In §24 define a *dependent type set* (or keep "function from terms to type sets") as the basic object and a *family* as one that is constant along steps. Then: dependent arrow and implicit product for any function; self type and dependent intersection for functions constant along safe head steps; term conversion and "∀ out, for families" for families. Rules 10 and 11 (the invariance is added where it is paid for). Cost: one more notion and five lemma hypotheses to adjust; the reader meets two kinds of object. Verdict: do the hypotheses (state exactly what each lemma needs) without introducing a second name; the name is not worth the weight.

**C13. Per-lemma status tags.** The status section is a wall of prose at the end. Put a one-word tag in each lemma or theorem header (textbook / quoted / here, reviewed / here, unreviewed). Rule 12 and writing rule 11. Cost: visual noise; it does not add a colour, so writing rule 17 is respected. Worth it; it also makes the review debt visible where the reader meets the claim.

**C14. Not recommended: parametrizing the main line.** Rule 2 would be satisfied most fully by stating §10–§13 for an arbitrary collection 𝒞 of type sets closed under ⇒ and ⋂ (with 𝒞 = all type sets as the instance), or by running §5–§13 with Good in place of SN. Either would make the spine a non-standard object (rule 6) and put the general before the concrete at the hardest point of the page (writing rule 9). C8 gets the benefit at no cost.

---

## Part D — Examples and text

**One more example would make a hard point graspable**
1. §21, head-step case: the only place the proof "uses that u is typable" is the discarded argument. One derivation shows it: from y : X ⊢ y : X and ⊢ I I : Y → Y, obtain y : X ⊢ (λx.y) (I I) : X. Three lines, and it is "the safe head step of §2 again" made visible. The δ I example of §19 covers the copied case; the discarded case has none.
2. §27: the only derivation example uses term conversion. A dependent application — f : Πx:X. P x, a : X ⊢ f a : P a — would show N2 at work ("Π out is apply, and then N2 turns ⟦B⟧ρ[x↦u[ρ]] into ⟦B[u/x]⟧ρ"), which is the one step a learner cannot see from the rule table.
3. §37: an example, or an admission, for "the sets that type expressions name change with the family" (A4). The example "What the conversions do to Gen({I I})" is good; what is missing is what the choice does to a *named* set.
4. §24: both families on the page are "SN if convertible with v, Min otherwise". One family not tied to a fixed term — e.g. P(u) = SN if u has a normal form, Min otherwise — would show that families can carry undecidable properties and that ∀P ranges over far more than the rules can name, which is the point of §11 one level up.
5. §33, narrow point 7: say in one line what the rule of U⁻ looks like as syntax (a kind ∀k. H(k)) before the set-theoretic argument, so a reader can see what is being forbidden.

**Examples, remarks, tables and paragraphs that do not carry their weight**
6. §20: "Programming languages with intersection types, such as TypeScript and Scala, use them in this way" — an aside with no consequence. Cut.
7. §15, first table ("What each requirement was for"): restates §4's list and §6's opening paragraph; the narrow-point table and "Where the difficulty comes from" are the section. Cut the first table.
8. §33's BOUNDED, PAIRS, MONOTONE (C11).
9. §34's strength table (C9) and the "Past the cube" paragraph can be two sentences.
10. §37's order paragraph (rule 3; A10).
11. §38's "Which of the two definitions each grows from" — fold into the table (C10).
12. §25's remark "Why Fu and Stump moved away from self types": three paragraphs of reported content for two reasons that are each one quotation. Compress to the two quotations and the pointer to §28–§30.
13. §35, "When two type expressions name one set": three "sufficient conditions" that are N2, N3, N4 restated, followed by the one interesting sentence (∀X.X and ∀X.∀Y.X). Keep the sentence, drop the list.
14. §20's *largest inside* and *repeat* (B3.3).
15. §36's side-by-side table once §37 exists (C5).

**Where the text explains its own apparatus or advertises rather than shows**
16. Top of page: "Rest on a box to see what that one section needs." "Each box is a link." "FOLD ALL PROOFS" is a control and need not be described. Writing rule 17.
17. §1: "Copies are shaded, here and in later examples."
18. §5: "That is why this page has many examples, and why several of them build type sets by hand from a few chosen terms." The examples show it; the sentence announces it.
19. §37 opening: "This section states that relation and proves it. The main line never needs it. It says what the choice made in §5 means, and it makes exact the picture given there" — four sentences of framing before the first definition; two would do ("The main line never needs it. It makes exact the picture of §5.").
20. "WHAT THIS PAGE CLAIMS": "§29 and §30 test the three constructions of Cedille against it, and one of them does not fit." §30's own table says the set fits and two of five rules do not. Say that.

**Text defects**
21. A15's two garbled sentences; the §32 heading is split across three lines in the text ("System F / ω / : names and rules") — check the rendering of the subscript.

---

## Overall judgement

The main line (§1–§14) is correct, tight and unusually well justified: every clause of the definition is forced by a named trial, and the page is honest about what it does not do. The extensions are correct where they were re-derived here; §21 and §29–§30 in particular hold up line by line, and §30's verdict on Cedille's φ is right and sharply stated. The two new comparison sections (§35, §37) contain the page's only mathematical errors, and all three are in the prose around correct lemmas: a justification that does not justify (A1), a false side-claim about candidates and the dependent arrow (A2), a false claim about safe head equivalence (A3), and a claim asserted in §37 that §36 lists as unchecked (A4). The research rules are mostly obeyed in spirit; the one systematically violated is rule 2 — four intersections and six extensions of Lemma N where one indexed intersection and one addition lemma would do (C1, C2) — and the one most often violated locally is the status/attribution discipline of rules 6 and 12 in the wider-view sections. §37 is the right section to have written (it dissolves the choice of §5 exactly as rule 1 asks) and the wrong section to have written in that register: it is where the jargon, the pointers and the unproved asides concentrate.
