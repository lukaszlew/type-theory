# The Narrow Path — notes for the next session

## What this is

Lecture notes on a technique: a type expression names a set of untyped terms (a type set) and a typing rule is a statement about sets. One HTML page, built from one file per section. Written by Lukasz Lew with Claude. Published in two places that must stay in step:

- GitHub Pages: https://lukaszlew.github.io/type-theory/ (from `docs/`, deployed by `.github/workflows/pages.yml`).
- A claude.ai artifact: https://claude.ai/artifact/MLoqTsJrr36yi2rpqYMZ64 — publish `out/narrow-path.html` (the page without the document skeleton) to that URL, with `rules-research.md`, `rules-writing.md` and `docs/sat-or-hc.html` as its files (markdown files need contentType exactly `text/markdown`). The comparison page has its own artifact: https://claude.ai/artifact/WZ3L2wK7R1cKkdFb5DhEFQ.

## The author's working rules

`rules-writing.md` (19 rules) and `rules-research.md` (12 rules) are binding for every edit; read both first. The ones that shape a session most:

- Explanations belong in the page, not in chat. In chat, give fit verdicts (does a concept fit neatly, or is it a sideline) and decisions; put the content on the page.
- Cut a thread by naming it: anything not done goes into the status section's "Not on this page" or "Open on this page" lists, never silently.
- Small sections, in dependency order, each with a Uses line; refactor the order like code when a section grows.
- No jargon: say the thing, then its standard name. The logical status of every claim is explicit (definition, modeling choice, theorem proved here, quoted, worked out and not reviewed).
- Distrust an arbitrary choice at the foundation: justify it or dissolve it (that is how the three collections of §36 and the comparison page came about).
- The author's instructions are not set in stone: if another approach is better, say so and do it. Guess what he really asks before answering.

## How the page is built

- `src/<slug>.html`: one file per section, plus `_front.html`, `_back.html` (status, sources), `_head.html` (title, fonts, CSS), `_tail.html` (scripts).
- `plan.py`: the single source for the order of sections, their parts, titles, the Uses lines, the dependency graph and the goal selector. Reordering the page is editing this list.
- `build.py`: assembles, lints, writes `docs/index.html` (complete document) and `out/narrow-path.html` (artifact version). Needs Python 3 and Graphviz.
- Cross references are written `{{slug}}`; a literal `§` in a section file is an error. The lint reports every backward reference to a section not in the Uses line; a passing mention is allowed by adding it to `POINTER_OK` in `build.py` with a reason; a real dependency goes into the Uses line in `plan.py`.
- The status word in a lemma header is `<span class="st">…</span>` inside the tag: `textbook`, `quoted`, `here, reviewed`, `here, unreviewed`. Every new lemma starts as `here, unreviewed` and is listed in the status section (`src/_back.html`), which also keeps the errata list and the open questions.
- `compare/build_cmp.py` builds the SAT-or-HC comparison from `compare/sat.json` (snapshots of the SAT statements; regenerate with `compare/dump_sat.py` after editing those statements) and the HC versions written in the script.

After any edit: `make check` (build with LINT 0, layout check on desktop and phone with no overflow, goal-selector check). `make reading-copy` writes `out/reading-copy.txt`, the plain text with every proof opened, which reviewers read.

## The review process

Results worked out for the page are re-derived by an independent reader before they are marked reviewed: spawn a fresh agent with `reviews/REVIEW-PROMPT.md`, pointing it at `out/reading-copy.txt`; it writes `reviews/reviewN.md`. Apply the findings, record what was found and fixed in the status section's errata list, flip the status words, and keep the report in `reviews/`. Five reviews have been run; the last three are in `reviews/`.

## Decisions already taken

- The definition of a type set is Tait's (SAT). Girard's candidates, the head-closed type sets and the test-defined sets are collections inside it (§35–§37), and `docs/sat-or-hc.html` shows what the page would be under the head-closed definition. The choice is dissolved, not defended; do not reopen it without the author.
- Terms are untyped, β only, Curry style; each choice names its price (§1, §13).
- Particular systems (Cedille's constructions, Mendler-style encodings, Fu–Stump self types) are tests of the technique, not its subject; the introduction names none of them. The author intends to move the specialist sections into appendices, or mark them, later.
- Verdicts on Cedille that the page states and should keep: the sets of all three constructions fit; ρ and φ are false, and β with φ cannot both hold in any semantics proving strong normalization; casts become side conditions on index sets, at the price of a least fixed point (§31).

## What is open or planned

See `OPEN.md`.
