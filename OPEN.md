# Open questions and planned work

## Open on the page (listed in its status section)

- Whether some closed type expression names different sets under the collections of §36; for `∀X.X` it does not.
- Whether `G(Fix(F))` and `Ind(F)` in the section on inductive types are the same type set. Known: `Ind(F) = μG ⊆ νG ⊆ G(Fix(F))`, and every fixed point of `G` has constructor, induction and destructor. Open: whether `G(Fix(F))` is a fixed point of `G`, and whether `G` has more than one. Matthes lists the same question for his two fixed points as open.
- Whether the iterator over the recursive type of numbers (a true judgment, by a lemma in the section on inductive types) is derivable by the rules for `μF`.
- Whether, for the test-defined sets of §37, the smallest such set above a union can serve existential types (the union itself cannot: the lemma of §37 shows that it need not be test-defined).

## Not reviewed yet

Review 6 (`reviews/review6.md`) and review 7 (`reviews/review7.md`, `reviews/review7b.md`) re-derived every lemma written after the papers were read, and found them correct, one after a correction to a definition; their other findings are applied and listed in the errata of the status section. Read by no one else: the corrections made after review 7 (the status section lists them), and the older items of the status section's "not reviewed" list.

## Planned

- Move the specialist sections (self types, Cedille's three constructions, Mendler-style encodings) into appendices, or mark them in the contents; the dependency lint will say what else moves with them (§29 is used by §31 and §38).
- A section on classical logic, starting from the tests of §37, where a test becomes a continuation. The comparison with Matthews's guide (arXiv 2307.13563) gives its definitions: terms with an instruction that captures the stack, stacks, processes, a pole; the set of stacks of an implication and of a quantifier; the captured stack as the witness of a negation; coherence. Not given there and to be done: the pole `SN` on stacks of strongly normalizing terms with the two instructions added, and the lemma "every closed term fails some test" for such terms. Parigot's proof of strong normalization for second-order classical natural deduction is the likely source.
- A section in which the type sets are sets of annotated terms, after Geuvers 1994 (the closing remark of the section on erasure reports the method): Lemma R and the three conditions restated for `λx:A.t`, with the annotation in `SN` as one more condition; it would replace the missing argument of the erasure table for the dependent corners.
- Type sets indexed by values that are not terms: a kind of numbers, a type set `Nat(n)` for each number, and the statement that a term in `⋂n (Nat(n) ⇒ Nat(f(n)))` computes `f`. Geuvers has this for inductive kinds and Krivine's realizability for its individuals; on the page a type set depends only on terms. A worked draft, with the sets, the constructors, recursion and the theorem, and a program check, is in `/home/lew/agent/tt-papers/notes_numbers_as_indices.md` (one pass, not reviewed, no rules yet).
- Whether a finite list of true rules of the sort named at the end of the section on completeness derives every true judgment of System D, and how the completeness theorems for restricted classes of type expressions (Kamareddine and Nour; Farkh and Nour; Labib-Sami) read on the page.
- The lemma of the section on completeness that the essential system is complete for expansion-closed sets is re-derived (review 7); check it against Hindley's papers before any wording about novelty.
- From the digest of Matthews's guide, sections 13-21 (proofs there, not checked by a second reader): in Krivine's realizability a fork is the same as a proof of `A -> B -> A ∩ B` for all sets, and closure of the sets under union is the same as every two stacks having a set of stacks for their disjunction; a fork does not give closure under union (forcing models). Open there: whether closure under union gives a fork. Open on the page: whether the smallest test-defined set above a union satisfies the rule that uses a member with the term unchanged; it does if and only if `(⋃F) ⇒ U` and `(closure of ⋃F) ⇒ U` are the same set for test-defined `U`.
- The digests of all papers read so far are in `/home/lew/agent/tt-papers/digests/` (`INDEX.md` is the map); each lists proposals that were not put on the page.
- Comparisons with other papers, in the form of the one with Matthews's guide: Riba on the values of reducibility candidates (for the name of the head-closed collection, §36); Vouillon and Melliès on semantic types (for the union question of §37); Abel and Coquand on failure of normalization with proof-irrelevant equality (for §30).
- Under the pairs reading of §40: function extensionality, quotient types and observational equality worked out as examples; proof irrelevance as a total relation.
- Possibly: a reading guide for the two audiences (learners: the main line; experts: §5, §15, Part VII).
