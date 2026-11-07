# Review 4 of "The Narrow Path" (reading copy v30)

Fresh reader. Scope: every result marked "here, unreviewed", the sections written after the last review, and the status section. Each lemma in scope was re-derived by hand. Sources checked: Firsov, Blair and Stump, arXiv 1803.02473 (ar5iv), and Stump and Jenkins, Cedille Core, arXiv 1811.01318 (ar5iv).

## Verdict per re-derived result (one line each)

| Where | Result | Verdict |
|---|---|---|
| §18 | Addition lemma, names and rules | Correct as stated and proved. |
| §26 | Addition lemma, parts that are terms | Correct in substance; N2 for a term part rests on a substitution fact for terms that the proof does not name, and "rules" should say the definition of a true judgment has changed (C6). |
| §33 | Addition lemma, parts of higher kind | Correct in substance; "holds as stated" is not literally true, the hypothesis must be read with kinds (C7). |
| §16 | Weakly normalizing terms have (i), (ii), (iii) | Correct; one sentence in the proof of (i) is imprecise (C4). |
| §13 | Church-style erasure remark | Correct; one step is skipped (C13). |
| §13 | What the proof asked of the collection | Incomplete: the collection must be nonempty for Lemma N, and the "for C2 only" is false (A8). |
| §24 | What each construction asks of a function | Wrong for "∀ out, for families" (A1). |
| §24 | "A family that no rule can name" | W is a family and the Church–Rosser step is right; the conclusion "no rule can name" does not follow (A9). |
| §21 | "The discarded argument has to be typable" | Correct line by line; "more variables" is used by the proof, not by the example (C10). |
| §26 | "Applying a dependent function" | Correct. |
| §31 | Mendler fixed point, any F | Correct as stated and proved; head-step counts (2 for in x a, 3 for fold) right. |
| §31 | Inductive part, monotone F | Correct as stated and proved; G monotone, G(C) a type set, PrfAlg index set nonempty, five head steps for out (in x) all verified; two small gaps (B6). |
| §31 | Example, table, remark on casts | Example right (pred (S n) → n in ten head steps). Table's middle column conflates two encodings (A4). Remark on casts misattributes the retyping to the rule φ (A5). |
| §35 | Erasure lemma and table | Lemma correct as stated and proved; rows right; the Cedille sentence overstates what the Cedille Core paper says, and Cedille's convertibility is βη (A14). |
| §37 | Every such relation can be added | Correct as stated; the hypothesis on "false rules" is not needed (A10); the note's "neither" is false (A6). |
| §38 | What a false hypothesis does | Lemma correct as stated and proved; the first bullet's reasoning is wrong (A7); the third bullet's first sentence is too strong (C12). |
| §39 | Every intersection is over a set | Statement omits the index sets that are sets of terms, which the proof and the table both admit (A2); levels and the coding of families are right; table row for §31 wrong (A3) and row for §22 needs "monotone" (A13); closing "that is why" wrong (A13). |
| §41 | Only head-closed type sets have complements | Correct as stated and proved, both halves. |
| §42 | Main line runs on pairs; abstraction theorem; two free theorems | Correct. Interface list is complete for the sections named; no proof needs the trichotomy of §2 or a one-sided head step. One false sentence in the commentary on the definition (A11), one inaccurate sentence in the remark (A12). |
| Status | Unreviewed list | Complete. Two results marked "here, reviewed" in their headers are in neither reviewed list; one proof has no stated status (B5). |

---

## Part A — Errors (most important first)

### A1. §24 remark and §26 remark: "∀ out, for families" also needs families constant along all steps

Quoted (§24): "The rule of term conversion in §26 asks that it is constant along all steps, so that a term inside a type expression can be run without changing what the type expression names."
Quoted (§26): "Among the five rules of this section, only term conversion needs families to be constant along steps."

Why wrong. "∀ out, for families" instantiates the intersection over all families at the function V = w ↦ ⟦B⟧ρ[x↦w], so that function has to be a member of the collection ∀P ranges over. The proof of N4 shows it is constant along steps of w only because ρ(P) is constant along all steps: a step of w inside t[ρ] (for B = P t with x inside an argument of t) is a step of t[ρ] that is not a head step. If families were asked only to be constant along safe head steps, then V would not be one. Counterexample: let ρ(P) = V0 with V0(u) = SN if u reaches y I by safe head steps and Min otherwise. V0 is constant along safe head steps (a term has at most one head step). Take B = P (y x). Then w ↦ ⟦B⟧ρ[x↦w] sends I to V0(y I) = SN and I I to V0(y (I I)) = Min, while I I →h I is a safe head step. So instantiating at it would be illegal, and "∀ out, for families" would be false for that collection. The dependency is even written on the page ("the function ... that '∀ out, for families' instantiates at is a family by N4"), but the two sentences quoted draw the opposite conclusion.

Fix. In §24: "The rule of term conversion in §26 asks that it is constant along all steps, and so does the rule '∀ out, for families', because the function w ↦ ⟦B⟧ρ[x↦w] that it instantiates at is constant along steps of w only if every ρ(P) is constant along all steps (N4)." In §26: "two of the five rules, term conversion and '∀ out, for families', need families to be constant along steps; the other three ask nothing."

### A2. §39 lemma: the statement omits index sets that are sets of terms

Quoted (statement): "Every intersection that this page forms is indexed by one of the following sets, or by a subset of one of them: the collection of all type sets; the collection of all families; a kind of §32."
Quoted (proof): "over the members of a type set, in §27 and §29, which is a subset of the set of all terms".
Quoted (table): "§29, ∀x:A — the members of a type set — no: the index set is a set of terms".

Why wrong. A set of terms is not a subset of the collection of type sets, of the collection of families, or of a kind. The proof and the table both treat the intersections of §27 and §29 as indexed by a set of terms, so the statement is contradicted by its own proof.

Fix. Add a fourth item: "a type set, which is a set of terms". The lemma's point (each index set is a set the metatheory already has) survives unchanged.

### A3. §39 table: the proof-algebra row is wrong

Quoted: "§31, proof algebras — the type sets inside Ind(F) — yes, through the fixed point".

Why wrong. The question of the column is whether the result is among the sets intersected over. PrfAlg(Ind(F), Q) is a type set, and it is not inside Ind(F) in general: §31 shows λf.λy.y ∈ PrfAlg(Ind(F), Q) for the constant family Q, and λf.λy.y ∉ Fix(F) ⊇ Ind(F), because (λf.λy.y) y →h I and I ∉ TK, so λf.λy.y ∉ Alg(F, TK) ⇒ TK. So the result is not one of the R ⊆ Ind(F). The impredicative step in §31 is the least fixed point μG, which is the §22 row, and the intersection over all families Q inside G(C), which is the §24 row.

Fix. Row: "§31, proof algebras — the type sets inside a given C — no: the result is a type set that need not be inside C; the impredicative steps of §31 are the fixed point μG (the row for §22) and the intersection over all families (the row for §24)."

### A4. §31 table: the middle column describes two different encodings

Quoted (column header): "RECURSIVE TYPE, §22 AND §27".
Quoted (row Iteration): "not built in: a member runs no loop by itself".
Quoted (row Predecessor): "a fixed number of steps".
Quoted (row Induction): "the self type, with the fixed point, as the Nat of §27".

Why wrong. The rows "Iteration" and "Predecessor" describe the μF of §22, whose members λz.λs.s n carry their predecessor and run no loop. The row "Induction" describes the Nat of §27, which is built on the Church numerals 0 = λs.λz.z and S = λn.λs.λz.s (n s z): there iteration is built in and the predecessor costs a number of steps that grows with the number, exactly as in the Church column. No type set on the page is both.

Fix. Either split the column into "μF of §22" (iteration not built in; predecessor fixed; induction: not done on the page) and "Nat of §27" (iteration built in; predecessor as for Church; induction: the self type with the fixed point), or relabel the column "μF of §22" and move the Induction entry to a note saying that §27's Nat is the Church encoding under a self type with a fixed point in its definition.

### A5. §31 remark on casts: the cast is not used "through the rule φ" in Firsov, Blair and Stump

Quoted: "A cast is used through the rule φ of §30: a term of type R is retyped at the target of the cast because the cast is equal to the identity."

Why wrong. In arXiv 1803.02473 the cast is applied by elimId, defined as `Λ X. Λ Y. Λ c. λ x. subst x -(π1 c x) -(ρ (π2 c) - β)`, and subst is `Λ X. Λ Y. λ x. Λ y. Λ p. [ x, y {p} ].2`: the introduction of a dependent intersection whose two parts are joined by a proof p that they are equal, followed by the second projection. The symbol φ does not occur in the paper. The rule φ is Cedille Core's later replacement for the annotation {p} on the intersection introduction; it does the same retyping, but the sentence is placed under "Quoted." and names the wrong rule for the paper it quotes. The rest of the paragraph (every R with a cast Id R X, the induction hypothesis used to build a cast into the inductive part, identity mappings in place of functoriality, FixIndM = ι x : FixM. IsIndFixM x with no fixed point) is accurate.

Fix. "A cast is applied by introducing a dependent intersection [x, y {p}] whose two parts are joined by a proof p that the cast is the identity, and projecting; Cedille Core, from which §30 takes its rules, replaced that annotation by the rule φ, which does the same retyping."

### A6. §37 note: being the same term does survive substitution

Quoted: "Being the same term has neither: I I → I breaks the first, since I is the same term as I and I I is not."

Why wrong. The second property is "if u R v, then u[s/x] R v[s/x]". If u and v are the same term, then so are u[s/x] and v[s/x]. So identity has the second property and fails only the first. (The errata list says a wrong example of a non-substitutive relation was already fixed once; this one is wrong again.)

Fix. "Being the same term has the second property and not the first: I I → I breaks the first, since I is the same term as I and I I is not."

### A7. §38 bullet "The Base condition": the reason given is a non sequitur

Quoted: "The Base condition of §5 is the reading applied to the variable rule: x : A ⊢ x : A has to be true, so x has to be in every set that A can name, and then so has x u, by the arrow."

Why wrong. Under the reading defined two paragraphs earlier, x : A ⊨ x : A says that every member of ⟦A⟧ρ is in ⟦A⟧ρ, which is true of any set and forces nothing. What puts the variable into every type set is the instance "x itself" that C1 needs (W5 in §4, and the second paragraph of this very section), and the test argument that W2 needs (narrow point 2).

Fix. "The Base condition of §5 is the reading applied to C1: x : A ⊢ x : A has to be true of the instance 'x itself', so x has to be in every set that A can name, and then so has x u, because the arrow tests its members on x."

### A8. §13 remark on the collection: the list is incomplete

Quoted: "use four things about the collection of all type sets, and nothing else: that every member satisfies the three conditions of §5; that the arrow of two members is a member; that the intersection of a nonempty set of members is a member; and, for C2 (consistency) only, that Min is a member".

Why wrong. The ∀ case of N1 is the intersection lemma applied to the whole collection, which has to be nonempty; an empty collection is vacuously closed under the arrow and under nonempty intersections, and then ⟦∀X.A⟧ρ is the set of all terms and N1 fails. Nonemptiness is a fifth thing, or Min's membership is used by Lemma N and not "for C2 only". (§41 applies the remark correctly because it has Min in the collection.)

Fix. "...that the intersection of a nonempty set of members is a member, and the collection itself is nonempty, so that ∀ is such an intersection; and, for C2 (consistency), that Min is a member, so that ∀X.X names Min."

### A9. §24 example "A family that no rule can name": the conclusion does not follow

Quoted: "No program decides whether a term has a normal form, which is a standard fact, quoted. So ∀P ranges over families that no rule and no program could pick out".

Why wrong. That membership in W(u) is undecidable does not show that no type expression names W: membership in sets that type expressions do name is undecidable too (whether a closed term is in ID, for example). The example proves that W is a family (the two Church–Rosser steps are right) and that no program decides which value it takes; it does not prove the title.

Fix. Either retitle "A family that no program can decide" and end with "no program could pick out", or prove the title by counting as in §11: the constant families alone are as many as the type sets, uncountably many, so almost every family is named by no type expression.

### A10. §37 lemma "false rules": the hypothesis is not needed, and the proof states the wrong reason

Quoted: "The rules ρ and φ are false, for every R that relates K and I in neither order."
Quoted (proof): "The counterexample to ρ uses ER(K, I) = Min, and the counterexample to φ uses ER(I, K) = Min."

Why wrong. The two counterexamples of §30 use only that the variable y is an instance of e, and y ∈ Min ⊆ ER(K, I) for every R, whatever ER(K, I) is. The failure of ρ comes from I ∉ VI(K), and the failure of φ from K ∉ ID; neither looks at the value of ER. So ρ and φ are false for every R with the two properties, including a universal R. The lemma as stated is true but suggests that an R relating K and I might make the rules true, which is false, and the proof's sentence misdescribes what the counterexamples use.

Fix. "The rules ρ and φ are false, for every R." Proof: "The counterexamples to ρ and φ in §30 use only that y ∈ Min ⊆ ER(K, I), which holds for every R."

### A11. §42 commentary on the definition: a false sentence about Base

Quoted: "A pair with a free variable on one side only, or with different variables at the head of its two sides, is in no Base".

Why wrong. (x y, x I) is in Base: same head variable, same number of arguments, both arguments in SN; and y is free on one side only.

Fix. "A pair with a variable at the head on one side only, or with different variables at the head of its two sides, is in no Base".

### A12. §42 remark: a head-closed relation is not in general "a relation between values"

Quoted: "a head-closed relation is, by the same correspondence, a relation between values, which is the form in which parametricity is usually stated."

Why wrong. The correspondence of §41 sends a head-closed type set to its members with no head step outside Base. For pairs, a pair has no joint head step as soon as one side has none, so the generators of a head-closed relation include mixed pairs such as (I, y): Gen({(I, y)}) is a head-closed relation (I has no head step), and (I, y) is not a pair of values. The claim holds for the relations generated by pairs of values only.

Fix. "a head-closed relation is, by the same correspondence, determined by its pairs with no joint head step, which include the pairs of values; restricted to those, it is a relation between values, the form in which parametricity is usually stated."

### A13. §39: two overstatements about strength

Quoted (table): "§22, μF — the type sets C with F(C) ⊆ C — yes: μF is one of them, which is the Knaster–Tarski argument".
Why wrong: F(μF) ⊆ μF is proved in §22 for monotone F only; for other F, μF is a type set but need not be in the collection. Fix: "yes, for monotone F".

Quoted (closing paragraph): "each arrow in a kind is one more power set, as the remark in §33 says, and that is why §36 reports that Fω needs more than arithmetic of any finite order."
Why wrong: that this proof uses one power set per arrow bounds the strength of this proof from above; that no proof in finite-order arithmetic exists is a lower bound, quoted in §36 from the literature, and does not follow from the shape of this proof. Fix: "and that matches what §36 reports, that Fω needs more than arithmetic of any finite order; the lower bound is quoted there and is not a consequence of this proof."

### A14. §35 table, Cedille rows: what the Cedille Core paper says

Quoted: "none. Cedille defines steps on erased terms only, and an annotated term is checked and then erased."
Quoted (§35, end): "What the table is built from is quoted from the paper on Cedille Core".

Why imprecise. The Cedille Core paper defines no steps on annotated terms and compares erased terms; so far the row is right. It does not say that a term is "checked and then erased"; that is a fact about the Cedille tool from general knowledge, not from the paper. Also, its conversion is "the usual relation of βη-equivalence of terms in pure untyped lambda calculus", while the page's convertibility (§24) is β only; so the rules of §30, "quoted ... with the terms erased", differ from Cedille's in η, which §1 removed. The erasures listed (Λx.t, t -u, [t, u], t.1, t.2, β{s}, ρ e − t, φ e − t {t′}) agree with the paper's Figure 2; δ and ς, which erase to the proof, are missing from the last row.

Fix. "none: Cedille Core defines no steps on annotated terms and compares erased terms, under βη-conversion, where this page has β only." Mark "checked and then erased" as general knowledge or drop it. Add "δ T e, ς e — |e|" to the last row.

---

## Part B — Rule violations in the checked sections

B1. Rule 5 ("If … then …", never "whenever" or "X when Y"). §18 addition lemma: "If the operation of the clause gives a type set whenever its inputs are type sets". §26 extension: "gives a type set whenever its inputs are type sets, families and terms". §42: "R ⇒ S relates two functions when they send related arguments to related results"; "A relation relates two terms when the pair is a member"; "a pair takes no head step when only one side has one".

B2. Rule 1 (one word, one meaning).
- §31: "A member of Alg(F, X) is a step of a recursion" and "the step a is run on y" — "step" means a β-reduction step everywhere else.
- §31: "For a type set X" and "with R over all type sets" — X is a variable of type expressions (§10) and R is a relation (§37, §42) elsewhere; use C, D, T, U.
- §31 proof of "in": "Take x ∈ F(Fix(F)) ... in x a" — x is also the bound variable of in = λx.λa.…; use u for the member.
- §35: "A step t ⇒ t′ of the annotated calculus" — ⇒ is the arrow on type sets since §4.
- §35 erasure lemma, second statement: "every typable annotated term is strongly normalizing" — SN was defined for the terms of §1; the first statement's "has no infinite run" is the right phrase.
- §42: "A type set of pairs, also called a relation" — two names for one thing; the section then uses "relation" only.

B3. Rule 3 and rule 4 (names, not pointers or letters).
- §16: "(i)", "(ii)", "(iii)" throughout, where §2 named the same facts "subterms", "variable applied", "safe head step".
- §37: "two properties ... The first property ... The second ..."; name them, for example "constant along steps" and "survives substitution".
- §39: "the strength of the first row"; "the last sentence of §23".
- §26 example: "The step from the first set to the second is the one that the rule table hides" (also "step" in a third meaning).

B4. Rule 13 and rule 19 (nothing used before defined; Uses lines).
- §37: "Two terms with the same evaluation, in the sense of §41" — "evaluation" is defined in §41, a later section.
- §31 (Uses §22, §29): relies on the lemma of §28 ("G(C) is a dependent intersection of §28"), the dependent arrow of §25 and the families of §24 — reachable only through §29's Uses line — and on "§30 showed that φ is false" in the remark, which is not reachable from §22 or §29 at all.
- §39 (Uses §17, §23, §31, §32): the table row for §33 and "as the remark in §33 says" use §33, which is not in its Uses line and not reachable from them.
- §38 (Uses §30): the bullet "Casts in §31" uses §31, not in its Uses line.

B5. Rule 11 and rule 18 (status explicit, and in the page).
- §26: Lemma N "extended to terms inside type expressions" and the theorem "The rules for dependent types" carry "HERE, REVIEWED" in their headers but appear in neither of the two reviewed lists of the status section.
- §41: the lemma "Head steps commute with other steps" is headed TEXTBOOK, and the status section says "the proof given there is this page's" without saying whether that proof was reviewed.
- §3: the generation lemma is headed QUOTED while its proof is the page's and was reviewed; the one-word header cannot say so, and nothing near the header does.

B6. Rule 12 (no skipped step).
- §42, Choice: "If t u v reaches u, then it does not reach v" uses that a term has at most one head step, which the page states only inside narrow point 2 of §6; say "head reduction is deterministic, so if t u v reached both, one of u, v would reach the other".
- §31, "in" for the inductive part: "and the closure condition gives in x p ∈ Q(in x)" — two head steps were undone, so "twice".
- §31, "out": "for any R inside Ind(F), any f and any y ∈ F(R)" — f has to be in Πr∈R Q(r), which is what makes the head step with argument f safe.
- §13 Church-style remark: "So an infinite run with annotations would give an infinite run without them" skips "between two loud steps there are at most as many silent steps as the term has Λs" (which §35 supplies).

B7. Rule 6 (every hypothesis explicit, and why a seemingly missing one is not needed). §38, item "weakening", holds for every B, but sits under "Let the type expression B name Min" without saying the hypothesis is unused. §37, item "false rules": an unused hypothesis (A10).

B8. Rule 7 (one definition per sentence). §42's definition paragraph defines pair, application, abstraction and substitution of pairs in one sentence, and SN, Base and head steps of pairs in the next. §35: "An annotated calculus is a set of annotated terms with a function ... and with steps of its own" defines three things in one sentence.

---

## Part C — Correct, but could be said more simply or more precisely

C1. §31, the open question. G(Fix(F)) — the §31 construction with C = Fix(F) and no fixed point, which is what Cedille's FixIndM is — already satisfies "in" and the induction item for p ∈ PrfAlg(Fix(F), Q), by the same proof (instantiate p at R = G(Fix(F)), which is inside Fix(F)). What the least fixed point buys is only the smaller induction step PrfAlg(Ind(F), Q), and with it "out" into F(Ind(F)). The open item in the status section can be sharpened to that.

C2. §31 example: give the count. pred (S n) reaches n by ten head steps for every n: one for pred, one for out, one for S n →h in (λz.λs.s n), four for in and λf.λy.y, two for the arguments 0 and λm.m, one for (λm.m) n. The sentence "after out has reached λz.λs.s n" hides that S n is not literally in x, so out needs one head step more than the five counted for out (in x).

C3. §31 example: "a member must give Q(in y) for a zero y, and for a successor y carrying r ∈ R" — F(R) has more members than the zero and the successors (every type set contains Base, for one). Say "for every y ∈ F(R), among them the zero and the successors".

C4. §16, property (i): "they end in a term that differs from that normal form only in the name of a variable" — if x is already free in t′, then [x/y] merges two variables rather than renaming one. The conclusion still holds: the term reached has that normal form as its instance under [x/y], and a redex in it would give a redex in the instance. Say that.

C5. §18, proof of N2: "for a part under a bound variable Y, taken not free in B" — also Y ≠ X, or A[B/X] does not go under the binder; the ∀ case of §10 has the same silent convention.

C6. §26 extension: (a) for a term part, N2 needs t[u/x][ρ] = t[ρ[x↦u[ρ]]], a fact about substitution of terms, not an induction on type expressions; name it. (b) "rules": say that §26 changes the definition of a true judgment, and that the five rules of §13 stay true under the new definition by their old proofs, the two → rules being the cases of Π in and Π out.

C7. §33 extension: "holds as stated" — the hypothesis under "names" has to read "gives a member of the form's kind whenever its inputs are members of their kinds", and N1 reads "member of its kind"; say so in one line.

C8. §41 complement lemma: the first half is one line once T′ = TW′ is noted, where W′ is the set of values not in W; the two equations are then the item "operations" with W ∩ W′ = ∅ and W ∪ W′ = all values. The proof says this; the statement could define T′ that way instead of as (SN ∖ T) ∪ Min.

C9. §42. (a) "The abstraction theorem is C1 read for pairs, with each (xi, xi) replaced by itself, in the case of an empty context" — with an empty context there is nothing to replace; drop the clause or state the theorem for any context. (b) "A pair is a pair (t, t′) of terms" — "A pair is two terms (t, t′) in order." (c) The hypothesis "no one of u, v reaches the other by head steps" is enough; it is what makes "reaches u" and "reaches v" exclusive. It is not needed for the dichotomy itself: if u reaches v, pair (u, v) with any unrelated (u′, v′) and read the choice off t u′ v′. Say which, and say whether zero head steps count, that is, whether u = v is excluded.

C10. §21 example: say that in the proof's terms Γ′ is empty and B = Y→Y, so "more variables" is what moves ⊢ I I : Y→Y under the context y : X; the example avoids it by deriving lines 3 to 5 under y : X directly.

C11. §35 table, dependent types row: the family quantifier of §26 has annotated forms too (an abstraction over P and an application to x.B), with a silent step that removes one such abstraction; list them with λx:A.t.

C12. §38, third bullet: "a rule that draws a conclusion from the mere existence of a member of some type set is false" is too strong as a sentence on its own, since δ is such a rule and the same bullet says it is true. "...is false unless the conclusion holds of every member of that type set, as δ's does of Min."

C13. §13 Church-style remark: add "so between two loud steps there are at most as many silent steps as the term has Λs" before "So an infinite run ...".

C14. §39 proof: the list of intersections omits, for §31, the intersection over all families inside G(C) and the intersections over all type sets in Alg and Fix; they fall under the rows already listed, but the lemma says "every intersection".

C15. §18 "rules": C2's proof in §13 also uses "a free variable can enter a derivation only through the variable rule", which a new rule could break; C2 as stated ("No closed term") is unaffected, but the sentence in §13 "The word 'closed' costs nothing here" is a fact about the five rules only. One clause in §18 would close this.
