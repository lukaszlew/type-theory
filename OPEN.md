# Open questions and planned work

## Open on the page (listed in its status section)

- Whether some closed type expression names different sets under the collections of §36; for `∀X.X` it does not.
- Whether `G(Fix(F))` and `Ind(F)` in §31 are the same type set (`Ind(F) ⊆ G(Fix(F))` holds). The obstacle is the one of §39: a proof algebra with a variable at its head passes every requirement.
- Whether a loop over the members of a recursive type `μF` can be typed (§31, table).
- Whether, for the test-defined sets of §37, the smallest such set above a union can serve existential types (the union itself cannot: the lemma of §37 shows that it need not be test-defined).

## Not reviewed yet

Review 6 (`reviews/review6.md`) re-derived the lemmas on unions of test-defined sets, on forgetting the terms, on the inductive part for any `F`, on the arrow into a head-closed type set, and extended induction, and found them correct; its other findings are applied and listed in the errata of the status section. Written or changed after it and read by no one else: the lemma of the section on completeness (the example is the reviewer's, the text the writer's) and its closing remark; the lemma on equality of type expressions and the cast; the item "encoding" of the existential types; the corrections made after review 6; and the older items of the status section's "not reviewed" list. A seventh review should cover these.

## Planned

- Move the specialist sections (self types, Cedille's three constructions, Mendler-style encodings) into appendices, or mark them in the contents; the dependency lint will say what else moves with them (§29 is used by §31 and §38).
- A section on classical logic, starting from the tests of §37, where a test becomes a continuation. The comparison with Matthews's guide (arXiv 2307.13563) gives its definitions: terms with an instruction that captures the stack, stacks, processes, a pole; the set of stacks of an implication and of a quantifier; the captured stack as the witness of a negation; coherence. Not given there and to be done: the pole `SN` on stacks of strongly normalizing terms with the two instructions added, and the lemma "every closed term fails some test" for such terms. Parigot's proof of strong normalization for second-order classical natural deduction is the likely source.
- A section in which the type sets are sets of annotated terms, after Geuvers 1994 (the closing remark of the section on erasure reports the method): Lemma R and the three conditions restated for `λx:A.t`, with the annotation in `SN` as one more condition; it would replace the missing argument of the erasure table for the dependent corners.
- Type sets indexed by values that are not terms: a kind of numbers, a type set `Nat(n)` for each number, and the statement that a term in `⋂n (Nat(n) ⇒ Nat(f(n)))` computes `f`. Geuvers has this for inductive kinds and Krivine's realizability for its individuals; on the page a type set depends only on terms.
- Whether a finite list of true rules of the sort named at the end of the section on completeness derives every true judgment of System D, and how the completeness theorems for restricted classes of type expressions (Kamareddine and Nour; Farkh and Nour; Labib-Sami) read on the page.
- Comparisons with other papers, in the form of the one with Matthews's guide: Riba on the values of reducibility candidates (for the name of the head-closed collection, §36); Vouillon and Melliès on semantic types (for the union question of §37); Abel and Coquand on failure of normalization with proof-irrelevant equality (for §30).
- Under the pairs reading of §40: function extensionality, quotient types and observational equality worked out as examples; proof irrelevance as a total relation.
- Possibly: a reading guide for the two audiences (learners: the main line; experts: §5, §15, Part VII).
