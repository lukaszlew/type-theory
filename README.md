# The Narrow Path — a semantics of type theory

Lecture notes on one technique for understanding a type system: a type expression is read as the name of a **type set**, a set of untyped λ-terms satisfying three conditions, and a typing rule as a statement about the named sets that is true or false. When every rule is true, every typable term is strongly normalizing and the system is consistent. The notes prove this for System F in a few lines and then follow the same reading to intersection types, dependent types, self types, equality types, inductive types, System Fω, the collections of type sets (Tait's, Girard's, head-closed, test-defined) and the semantics on pairs of terms (parametricity).

**Read it:** https://lukaszlew.github.io/type-theory/

- `docs/index.html` — the notes, one page, with a dependency graph of the sections and a goal selector.
- `docs/sat-or-hc.html` — a side-by-side reading of every definition and lemma that would change if type sets were head-closed instead of Tait's saturated sets.
- `rules-research.md`, `rules-writing.md` — the rules the notes are written and reviewed against.
- `reviews/` — reports of the independent reviews (fresh readers who re-derived the results), kept as the record of what was found and fixed.

## Building

The page is assembled from one file per section.

```
python3 build.py              # src/*.html + plan.py -> docs/index.html (and out/narrow-path.html)
python3 compare/build_cmp.py  # -> docs/sat-or-hc.html
```

Needs Python 3 and Graphviz (`dot`, for the dependency graph). `plan.py` is the single source for the order of sections, the parts, the "Uses" line under each heading, the graph and the goal selector. In a section file, a reference to another section is written `{{slug}}`; the build turns it into a numbered link and checks that every earlier section a text refers to is among the sections it uses.

`tools/` holds the Playwright checks for layout on desktop and phone (`check-layout.js`), for the goal selector (`check-goals.js`), and a plain-text reading copy for reviewers (`reading-copy.js`); `tools/tests/` holds the small λ-calculus evaluator used to check a few claims by brute force.

## Status

Every lemma on the page carries a status word (textbook / quoted / here, reviewed / here, unreviewed), and the closing section lists what is quoted, what is the page's own, what reviews found and fixed, what is open, and what is not on the page.
