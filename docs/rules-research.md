# Rules for research on The Narrow Path

These rules govern how an agent thinks and decides while researching for the book: which object to build on, what to cover, what to claim. The rules for writing the page itself are in `rules-writing.md`. A fresh agent gets both.

## 1. Distrust an arbitrary choice at the foundation. Justify it or dissolve it.

A definition that could have been otherwise is a debt. Either show that it is forced (every clause is needed for the theorem, and a trial without it fails), or show that all the alternatives are readings of one structure, so that the choice becomes a choice of presentation and the mathematics is the same. Do not settle it by taste and do not leave it unexamined.

*Example.* Tait's, the head-closed and Girard's type sets looked like three competing choices. They are one chain with conversions both ways; Tait's is the forced one, the others add a named invariance. The choice of spine became presentation.

## 2. Define once, derive everywhere.

No definition and no lemma is stated twice for two variants. Find the interface the main line actually uses, state it, and obtain each variant by a construction that satisfies the interface, with a transfer lemma. Parallel developments are a sign that the interface has not been found.

*Example.* The unary theory uses only Lemma R, substitution and "a head step survives an argument". Pairs of terms satisfy all three, so the binary (relational) semantics is the same theory on pairs, not a second theory.

## 3. Elegance is evidence, not decoration.

A clean description — a quotient, a powerset, a Boolean algebra, a topology — is a symptom of having found a canonical object, so look for it. But it earns a place in the book only if some result uses it or it explains a choice. If it is only pretty, it gets one sentence. Always ask: which theorem uses this property?

*Example.* "Head-closed type sets form a powerset of values" is the same fact as "they are a quotient"; no result uses complements or atoms beyond one lemma. It is stated in a sentence, not used to move the spine.

## 4. Test claims against the deliverables, and retract what fails.

A property matters only if a deliverable uses it: strong normalization, consistency, parametricity, the additions, the comparisons. When a claim of advantage is made, name the deliverable that gains and show the gain. If none does, say so and withdraw the claim explicitly.

*Example.* "Tait's family gives stronger free theorems" was withdrawn: the extra consequences concern evaluation paths, and the standard free theorems follow from the weaker family plus one syntactic fact.

## 5. A map, not a monograph.

The book covers the landscape of realizability-style semantics: Tait, Girard, Reynolds, Harper, Krivine, Cedille, and the constructions between them. Threads that are not ours are cut honestly: named, placed, and marked as not treated. Clarity of a lecture note outranks completeness; anything that gets complicated gets its own section, and the dependency graph stays acyclic and readable.

## 6. Trusted by experts, understood by learners.

The spine is the canonical object the literature knows, under its standard name. New lenses, structure theorems and comparisons go in their own sections as a payoff, not as a correction. Never claim novelty where the literature has the thing; attribute, and say "we found no name for it" when that is the case. Every statement carries its status: definition, modeling choice, theorem proved here, quoted from a source, worked out here and not reviewed.

## 7. Answer the real question.

A probe such as "is X attractive?", "which is most fundamental?", "can we convert one into the other?" is usually asking "is X canonical?", "can we define once?", "is the choice forced?". Guess the question underneath, say what it is, and answer that; then answer the question as asked if it still needs an answer.

## 8. Argue both sides, then neither.

For any choice, give the case for, the case against, and then a reading with no side, by reader: expert in each neighbouring field, and learner. Expect to be asked for the other side of any case made; do not need to be asked.

## 9. Fit before build.

Before writing a section on a proposed topic, give the verdict: fits the book's thread, sideline, or weakly related — and whether a section on it would be a good read. Build only what fits; place sidelines as remarks or cut them under rule 5.

## 10. Prefer the least committed object when nothing forces more.

Among candidates that all carry the theorem, take the one that asks least, and present the others as that one plus a named condition. The largest family, the weakest assumption, the fewest clauses. Invariances are options the reader can add, not axioms the book imposes.

## 11. Name the price of every step.

Each additional condition, quotient or invariance is paid for somewhere: fewer sets for `∀` to range over, a wart such as a member leaving a set by running, a dependence on an evaluation strategy, a loss of a literature anchor. State the price next to the gain, every time.

## 12. Keep the review debt visible.

Every result worked out in conversation and not yet checked by a fresh reader is listed as such on the page, and the list is kept current. Errors found while re-reading are fixed and reported, not silently corrected.
