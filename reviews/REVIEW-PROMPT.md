# Prompt for an independent review

Use with a fresh agent that has not seen the page. Replace the bracketed parts.

---

You are a fresh, independent reviewer of a mathematical web page, "The Narrow Path" (lecture notes: a type expression names a set of untyped terms, typing rules are statements about sets; strong normalization and consistency for System F, extended to intersection, dependent and inductive types, Fω, the collections of type sets, tests and pairs). You have not seen it before. Read the plain-text reading copy at `[path to out/reading-copy.txt]` in full, in several chunks; every proof is opened in it. Read the two rule files the page is checked against: `rules-research.md` and `rules-writing.md`.

Every lemma carries a status word in its header. Re-derive, line by line and by hand, every result marked "here, unreviewed", and check the sections written since the last review: [list them]. For each, state in one line whether it is correct as stated and proved. Check in particular: [specific points to verify]. Check, for those sections, the writing rules (one word one meaning; no unexplained jargon; names not pointers; every claim's status explicit; nothing used before defined; the Uses line of each section covers what it relies on). Check that the status section lists every unreviewed item and claims nothing as reviewed that is not.

Write your report to `reviews/reviewN.md`: Part A — errors (false statements, gaps in proofs, wrong attributions), numbered, most important first, each with a quotation of the sentence, the reason it is wrong, and a concrete fix; Part B — rule violations; Part C — anything correct that could be said more simply or more precisely; and a one-line verdict per re-derived result. Be concrete and quote. [Say whether larger restructurings are wanted.] Your final message should summarize the five most important findings and the counts.
