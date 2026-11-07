"""Build the comparison page: each affected definition or lemma under SAT (as on the page) and under HC (as it would be)."""
import re, json, difflib, html, sys, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
sys.path.insert(0, P)
from plan import SECTIONS, NUM
TITLE = {s[0]: s[2] for s in SECTIONS}
sat = json.load(open(P + 'compare/sat.json'))

def deref(h):
    "replace {{slug}} by the section number and title"
    return re.sub(r'\{\{(\w+)\}\}', lambda m: '§%d %s' % (NUM[m.group(1)], re.sub(r'<[^>]+>', '', TITLE[m.group(1)])), h)

def strip_st(h):
    return re.sub(r'<span class="st">[^<]*</span>', '', h)

def tokens(h):
    "split html into tags and words; words carry trailing whitespace"
    return [(t.startswith('<'), t) for t in re.findall(r'<[^>]+>|[^<\s]+\s*|\s+', h)]

def diff_html(a, b):
    "render b with words not in a marked <ins>, and words of a missing from b marked <del>"
    ta, tb = tokens(a), tokens(b)
    wa = [t for isTag, t in ta if not isTag and t.strip()]
    wb = [t for isTag, t in tb if not isTag and t.strip()]
    sm = difflib.SequenceMatcher(None, [w.strip() for w in wa], [w.strip() for w in wb], autojunk=False)
    ops = sm.get_opcodes()
    # map each word index of b to (kind) and collect deletions to emit before a given b-word index
    kind = {}
    dels = {}
    for tag, i1, i2, j1, j2 in ops:
        if tag == 'equal':
            for j in range(j1, j2): kind[j] = 'eq'
        elif tag == 'insert':
            for j in range(j1, j2): kind[j] = 'ins'
        elif tag == 'delete':
            dels.setdefault(j1, []).extend(wa[i1:i2])
        elif tag == 'replace':
            dels.setdefault(j1, []).extend(wa[i1:i2])
            for j in range(j1, j2): kind[j] = 'ins'
    out = []
    j = 0
    def emit_dels(j):
        if j in dels:
            out.append('<del>' + html.escape(' '.join(w.strip() for w in dels[j])) + '</del> ')
    for isTag, t in tb:
        if isTag or not t.strip():
            out.append(t); continue
        emit_dels(j)
        if kind.get(j) == 'ins':
            m = re.match(r'(\S+)(\s*)', t)
            out.append('<ins>' + m.group(1) + '</ins>' + m.group(2))
        else:
            out.append(t)
        j += 1
    emit_dels(j)
    res = ''.join(out)
    res = re.sub(r'</ins>(\s+)<ins>', r'\1', res)
    res = re.sub(r'</del> <del>', ' ', res)
    return res

ITEMS = []  # dicts: sec, title, status, sat (html or None), hc (html or None), note

def add(sec, title, status, sat_html, hc_html, note=''):
    ITEMS.append(dict(sec=sec, title=title, status=status, sat=sat_html, hc=hc_html, note=note))

S = lambda k: strip_st(sat[k])

# ---------------------------------------------------------------- §2
add('§2 Head steps', 'Definition · Evaluation, value, stuck', 'added', None,
'''<section class="box def">
  <p class="tag">Definition · Evaluation, value, stuck</p>
  <p>Let <code>t</code> be a strongly normalizing term. Its head steps are steps, so they end, at an abstraction or at a member of <code>Base</code>. That term is the <b>evaluation</b> of <code>t</code>, written <code>eval(t)</code>.</p>
  <p>A <b>value</b> is a strongly normalizing abstraction.</p>
  <p><code>t</code> <b>gets stuck</b> if <code>eval(t)</code> is in <code>Base</code>.</p>
</section>''',
'On the SAT page this definition sits in §36 The three collections, where the head-closed type sets are introduced. Under HC it is needed before the definition of a type set, so it moves to §2 and §36 loses it.')

# ---------------------------------------------------------------- §5 definition
hc_def = S('typeset.html|Definition · Type set')
hc_def = hc_def.replace('<dt>closure</dt><dd><code>cl(T) ⊆ T</code>. Equivalently: if <code>s →<sub>h</sub> s′</code> is safe and <code>s′ ∈ T</code>, then <code>s ∈ T</code>. <span>Needed for W3 (abstraction).',
 '<dt>closure</dt><dd><code>cl(T) ⊆ T</code>, and <code>T</code> is closed under head steps. Equivalently: if <code>s →<sub>h</sub> s′</code> is safe, then <code>s′ ∈ T</code> if and only if <code>s ∈ T</code>. <span>The direction from <code>s′</code> to <code>s</code> is needed for W3 (abstraction). The direction from <code>s</code> to <code>s′</code> is needed by nothing in the proof: it is a modeling choice, which makes a type set exactly a set of values, as the lemma “Type sets are sets of values” says, and narrow point 5 records that the theorem does not ask for it.')
hc_def = hc_def.replace('<p>In short, a type set is a set between <code>Base</code> and <code>SN</code> that is closed under undoing safe head steps.',
 '<p>In short, a type set is a set between <code>Base</code> and <code>SN</code> that is closed under safe head steps in both directions.')
assert hc_def != S('typeset.html|Definition · Type set')
add('§5 Type sets', 'Definition · Type set', 'changed', S('typeset.html|Definition · Type set'), hc_def,
'The one real change. Everything below follows from it.')

add('§5 Type sets', 'The picture to carry through the page', 'changed',
'<p>A picture to carry through the page. A type set is, roughly, a set of <b>values</b>, that is, of strongly normalizing abstractions, together with every term that reaches one of them by safe head steps, together with the terms that get stuck at a variable, which belong to every type set. “Roughly” because a type set may contain a term and not the term that its head step leads to; §36 The three collections makes the picture exact and says what the word hides.</p>',
'<p>A picture to carry through the page, and it is exact. A type set is a set of <b>values</b>, that is, of strongly normalizing abstractions, together with every term that evaluates to one of them, together with the terms that get stuck at a variable, which belong to every type set. The lemma “Type sets are sets of values” below says so.</p>')

add('§5 Type sets', 'Definition · Gen(S) and Min', 'changed', S('typeset.html|Definition · Gen(S) and Min'),
 S('typeset.html|Definition · Gen(S) and Min').replace('<code>Gen(S) = cl(Base ∪ S)</code>. It is called the set generated by <code>S</code>.',
 '<code>Gen(S) = cl(Base ∪ S<sub>h</sub>)</code>, where <code>S<sub>h</sub></code> is <code>S</code> together with every term that a member of <code>S</code> reaches by head steps. It is called the set generated by <code>S</code>.'),
'<code>cl(Base ∪ S)</code> is no longer a type set in general: for <code>S = {I I}</code> it contains <code>I I</code> and not <code>I</code>. The head reducts have to be added first. <code>Min = cl(Base)</code> is unchanged, because a member of <code>Base</code> has no head step.')

hc_M = S('typeset.html|Lemma M').replace('A term <code>t</code> is in it if and only if <code>t ∈ SN</code> and its head steps lead to a member of <code>S</code> or of <code>Base</code>. Zero head steps are allowed.',
 'A term <code>t</code> is in it if and only if <code>t ∈ SN</code>, and <code>t</code> gets stuck or <code>eval(t) = eval(s)</code> for some <code>s ∈ S</code>.')
assert hc_M != S('typeset.html|Lemma M')
add('§5 Type sets', 'Lemma M · Three facts about type sets', 'changed', S('typeset.html|Lemma M'), hc_M,
'M1 and M3 are unchanged. The membership condition in M2 no longer counts head steps: a term and everything on its head reduction stand or fall together.')

add('§5 Type sets', 'Lemma · Type sets are sets of values', 'added', None,
'''<section class="box thm">
  <p class="tag">Lemma · Type sets are sets of values</p>
  <p>Send a type set <code>T</code> to the set of values it contains, and send a set <code>W</code> of values to</p>
  <p class="eq"><code>T<sub>W</sub> = { t ∈ SN : eval(t) ∈ W, or t gets stuck }</code></p>
  <dl class="conds">
    <dt>bijection</dt><dd>The two maps are inverse to each other, between the type sets and the sets of values.</dd>
    <dt>operations</dt><dd>Intersection and union of type sets are intersection and union of their sets of values. For a value <code>v</code>, <code>Gen({v})</code> has the set of values <code>{v}</code>.</dd>
    <dt>tell apart</dt><dd>Two strongly normalizing terms belong to the same type sets if and only if they have the same evaluation, or both get stuck.</dd>
  </dl>
  <p>So a type set is just a choice of which values belong, and <code>Gen(S)</code> is the choice of the values that members of <code>S</code> evaluate to.</p>
</section>''',
'This is the lemma “Head-closed type sets are sets of values” of §36 on the SAT page, now about every type set, and placed where the definition is. Its proof is unchanged.')

hc_G = S('typeset.html|Example · A type set built from two terms')
hc_G = hc_G.replace('<li><code>(λz.z K) y</code>: one head step leads to <code>y K</code>, which is in <code>Base</code>.</li>\n  </ul>',
 '<li><code>(λz.z K) y</code>: one head step leads to <code>y K</code>, which is in <code>Base</code>.</li>\n    <li><code>I</code>: it is the evaluation of the chosen term <code>I I</code>.</li>\n  </ul>')
hc_G = hc_G.replace('    <li><code>I</code>. It is in <code>SN</code> and has no head step, and it is neither chosen nor in <code>Base</code>.</li>\n', '')
hc_G = hc_G.replace('<li><code>K K</code>. Its head step gives <code>λb.K</code>, an abstraction that is not <code>K</code>.</li>', '<li><code>K K</code>. Its evaluation is <code>λb.K</code>, which is neither <code>K</code> nor <code>I</code>.</li>')
hc_G = hc_G.replace('<li><code>λx.K x</code>. It has no head step, although one step inside it gives <code>K</code>.</li>', '<li><code>λx.K x</code>. It is its own evaluation, and it is neither <code>K</code> nor <code>I</code>, although one step inside it gives <code>K</code>.</li>')
assert hc_G != S('typeset.html|Example · A type set built from two terms')
add('§5 Type sets', 'Example · A type set built from two terms', 'changed', S('typeset.html|Example · A type set built from two terms'), hc_G,
'<code>G</code> gains the member <code>I</code>. Its set of values is <code>{K, I}</code>.')

add('§5 Type sets', 'Example · A member can leave by running', 'changed', S('typeset.html|Example · A member can leave by running'),
'''<section class="box ex">
  <p class="tag">Example · A member can leave by a step inside an abstraction</p>
  <p><code>I I</code> is in <code>G</code>, and <code>I I → I</code>, and <code>I</code> is in <code>G</code> too: a type set keeps a term along its head steps, by definition. It need not keep it along other steps. <code>Gen({λx.I x})</code> contains <code>λx.I x</code> and not <code>I</code>, because the step from <code>λx.I x</code> to <code>I</code> is inside the abstraction and is not a head step; §23 Limits and §36 The three collections use that type set. Nothing later needs a type set to keep a term while it runs.</p>
</section>''',
'The example that the SAT page uses in §23 (limit 3), §36 and §37, <code>Gen({I I})</code> with <code>I ∉ Gen({I I})</code>, no longer exists. Its role is taken by <code>Gen({λx.I x})</code>, where the escaping step is inside the abstraction.')

# ---------------------------------------------------------------- §6
add('§6 Could the definition be simpler', 'Narrow point 5 · Closure under head steps is not forced', 'added', None,
'''<section class="box np">
  <p class="tag">Narrow point 5 · Closure under head steps is not forced</p>
  <dl class="rows">
    <dt>Goal</dt><dd>A definition that drops the direction from <code>s</code> to <code>s′</code> of the closure condition, and keeps the other direction.</dd>
    <dt>Try</dt><dd>A set qualifies if it satisfies the SN condition, the Base condition, and <code>cl(T) ⊆ T</code>. These are Tait’s saturated sets.</dd>
    <dt>Holds</dt><dd>Every requirement, W1 to W5. The proofs of §8 to §13 never use the dropped direction, so they go through unchanged for the sets that qualify, and the theorem holds with <code>∀</code> ranging over them.</dd>
    <dt>Lesson</dt><dd>The fourth clause of the definition is not forced by the theorem. It is kept because it makes a type set exactly a set of values, and the page says so wherever the clause is used. The three remaining conditions are the narrow path; this page walks a slightly wider one.</dd>
  </dl>
</section>''',
'The SAT page can say that each of its conditions is forced. The HC page cannot, and honesty requires this narrow point, which is a trial that <em>succeeds</em>. The title “The Narrow Path” then names Tait’s definition, not the page’s own.')

# ---------------------------------------------------------------- §7
hc_E = S('structure.html|Lemma E')
hc_E = hc_E.replace('the closure condition holds if and only if this holds: if <code>s ∈ SN</code>, <code>s →<sub>h</sub> s′</code> and <code>s′ ∈ T</code>, then <code>s ∈ T</code>. <span>“The argument is in <code>SN</code>” becomes “the whole term is in <code>SN</code>”.</span>',
 'the closure condition holds if and only if this holds: if <code>s ∈ SN</code> and <code>s →<sub>h</sub> s′</code>, then <code>s ∈ T</code> if and only if <code>s′ ∈ T</code>. <span>“The argument is in <code>SN</code>” becomes “the whole term is in <code>SN</code>”.</span>')
hc_E = hc_E.replace('<p>Put together: a type set is a set between <code>Min</code> and <code>SN</code> that contains every strongly normalizing term whose head step leads into it.</p>',
 '<p>Put together: a type set is a set between <code>Min</code> and <code>SN</code> in which a strongly normalizing term and its head reduct are members together.</p>')
assert hc_E != S('structure.html|Lemma E')
add('§7 The collection of all type sets', 'Lemma E · The definition in other words', 'changed', S('structure.html|Lemma E'), hc_E, 'E1, E2 and E4 are unchanged in wording; E4 refers to the new <code>Gen</code>.')

hc_L = S('structure.html|Lemma L')
hc_L = hc_L.replace('<code>Gen({a}) ⊆ Gen({b})</code> if and only if <code>a ∈ Min</code> or <code>a</code> reaches <code>b</code> by zero or more head steps. <span>In particular, if <code>a →<sub>h</sub> b</code>, then <code>Gen({a}) ⊆ Gen({b})</code>.</span>',
 '<code>Gen({a}) ⊆ Gen({b})</code> if and only if <code>a ∈ Min</code> or <code>eval(a) = eval(b)</code>. <span>In particular, if <code>a →<sub>h</sub> b</code>, then <code>Gen({a}) = Gen({b})</code>.</span>')
hc_L = hc_L.replace('<dt>L3</dt><dd><b>Chain.</b> If <code>a ∈ Min</code>, then <code>Gen({a}) = Min</code>. If <code>a ∉ Min</code>, let <code>a = a<sub>0</sub> →<sub>h</sub> a<sub>1</sub> →<sub>h</sub> … →<sub>h</sub> a<sub>k</sub></code> be all the head steps of <code>a</code>. Then <code>a<sub>k</sub></code> is an abstraction, and the type sets of the form <code>Gen({c})</code> that contain <code>a</code> are exactly <code>Gen({a<sub>0</sub>}) ⊊ Gen({a<sub>1</sub>}) ⊊ … ⊊ Gen({a<sub>k</sub>})</code>. <span>The smallest type set that contains <code>a</code> grows along the head steps of <code>a</code>. It is largest at the abstraction where the head steps end.</span></dd>',
 '<dt>L3</dt><dd><b>No chain.</b> If <code>a ∈ Min</code>, then <code>Gen({a}) = Min</code>. If <code>a ∉ Min</code>, then <code>Gen({a}) = Gen({eval(a)})</code>, and the type sets of the form <code>Gen({c})</code> that contain <code>a</code> are exactly those with <code>eval(c) = eval(a)</code>, which are all the same set. <span>The smallest type set that contains <code>a</code> is the same at every point of the head steps of <code>a</code>. The chain of the saturated sets, one set per head step, collapses to its last member.</span></dd>')
assert hc_L.count('No chain') == 1
add('§7 The collection of all type sets', 'Lemma L · Type sets generated by one term', 'changed', S('structure.html|Lemma L'), hc_L,
'L1 and L4 are unchanged. L3 is where the two pictures differ most visibly: under SAT the sets <code>Gen({a<sub>i</sub>})</code> along a head reduction form a strictly increasing chain; under HC they are one set. The example “A chain of generated type sets” and the figure of trees of head steps in §7 go with it.')

add('§7 The collection of all type sets', 'Lemma · Type sets tell terms apart', 'changed', S('structure.html|Lemma · Type sets tell'),
'''<section class="box thm">
  <p class="tag">Lemma · Type sets tell evaluations apart</p>
  <p>Let <code>a</code> and <code>b</code> be strongly normalizing terms. Then <code>a</code> and <code>b</code> belong to the same type sets if and only if they have the same evaluation, or both get stuck.</p>
  <p class="note">So <code>I I</code> and <code>I</code> belong to the same type sets, and <code>λx.K x</code> and <code>K</code> do not. The semantics identifies a term with its evaluation and with nothing else: not with its reducts under other steps, and not with the terms it is convertible with. §34 Equality type sets draws the consequence: an equality coarser than “same evaluation” has to be added as a type set.</p>
</section>''',
'This is the item <i>tell apart</i> of the values lemma, stated at the place where the SAT page states its own version. The consequence for equality is weaker by one notch: under SAT nothing is identified, under HC a term is identified with its evaluation.')

# ---------------------------------------------------------------- §8, §15, §18
add('§8 Two operations', 'Arrow lemma, intersection lemma, union lemma', 'unchanged', S('ops.html|Arrow lemma'), S('ops.html|Arrow lemma'),
'Statements unchanged. Each proof gains one paragraph: closure under head steps passes to <code>T ⇒ U</code> because <code>t u →<sub>h</sub> t′ u</code> when <code>t →<sub>h</sub> t′</code> and <code>U</code> is closed under head steps; and it passes to intersections and unions because it is a condition on single members. The same paragraph is added to the dependent arrow (§25), the self type (§27), the dependent intersection (§28), the implicit product (§29), the least fixed point and the existential type (§22) and the Mendler fixed point (§31). Nothing else in those sections changes.')

add('§15 What the proof used', 'Table · What each condition was for', 'changed',
'''<div class="tw"><table class="w34">
  <thead><tr><th>Condition</th><th>Where it is used</th></tr></thead>
  <tbody>
    <tr><td>SN condition</td><td>The arrow keeps the SN condition and the Base condition. <i>Abstract</i>: the argument is in <code>SN</code>, as the closure condition requires. C1 (strong normalization): a member of <code>⟦A⟧<sub>ρ</sub></code> is in <code>SN</code>.</td></tr>
    <tr><td>Base condition</td><td>The arrow keeps the SN condition: a variable is the argument used. The arrow keeps the Base condition: <code>Base ⊆ U</code>. C1 (strong normalization): each variable may be replaced by itself.</td></tr>
    <tr><td>Closure condition</td><td>The arrow keeps the closure condition: one more trailing argument. <i>Abstract</i>: abstractions enter <code>T ⇒ U</code>.</td></tr>
  </tbody>
</table></div>''',
'''<div class="tw"><table class="w34">
  <thead><tr><th>Condition</th><th>Where it is used</th></tr></thead>
  <tbody>
    <tr><td>SN condition</td><td>The arrow keeps the SN condition and the Base condition. <i>Abstract</i>: the argument is in <code>SN</code>, as the closure condition requires. C1 (strong normalization): a member of <code>⟦A⟧<sub>ρ</sub></code> is in <code>SN</code>.</td></tr>
    <tr><td>Base condition</td><td>The arrow keeps the SN condition: a variable is the argument used. The arrow keeps the Base condition: <code>Base ⊆ U</code>. C1 (strong normalization): each variable may be replaced by itself.</td></tr>
    <tr><td>Closure condition, undoing a head step</td><td>The arrow keeps the closure condition: one more trailing argument. <i>Abstract</i>: abstractions enter <code>T ⇒ U</code>.</td></tr>
    <tr><td>Closure condition, taking a head step</td><td>Nowhere. The arrow and the intersection keep it, so that it can be kept at all; no fact and no rule uses it. It is a modeling choice, and narrow point 5 says so.</td></tr>
  </tbody>
</table></div>''',
'The sentence “None of the three conditions is spare” before the table has to go.')

add('§18 The price of a new rule', 'Addition lemma', 'unchanged', S('price.html|Addition lemma'), S('price.html|Addition lemma'),
'Statement unchanged. The obligation “the operation gives type sets” is heavier by one clause, closure under head steps, so every addition on the page pays one more line: §19, §22 (three times), §27, §28, §29, §30, §31.')

# ---------------------------------------------------------------- §23
add('§23 Limits', 'Limit 3 · Only strong normalization is certified', 'changed', S('limits.html|Limit 3'),
'''<section class="aside">
  <p class="tag">Limit 3 · Only strong normalization is certified</p>
  <dl class="rows">
    <dt>Try</dt><dd>Read <code>t ∈ T</code> as all that typing usually promises, including that <code>t</code> stays in <code>T</code> while it runs.</dd>
    <dt>Breaks</dt><dd>Take <code>T = Gen({λx.I x})</code> from §5 Type sets. <code>λx.I x ∈ T</code> and <code>λx.I x → I</code> by a step inside the abstraction, but <code>I ∉ T</code>.</dd>
    <dt>Lesson</dt><dd>Type sets are closed under head steps, in both directions. They are not closed under steps inside abstractions. The statement “if <code>t : A</code> and <code>t → t′</code> then <code>t′ : A</code>”, called subject reduction, is known to hold for plain System F, by a separate proof about derivations. It is known to fail for the rule that uses a member of an existential type, in §22.</dd>
  </dl>
</section>''',
'The limit shrinks but does not disappear: a member can still leave by a step inside an abstraction.')

# ---------------------------------------------------------------- §34
add('§34 Equality type sets', 'Opening paragraph', 'changed',
'<p>The lemma “Type sets tell terms apart” in §7 says that two strongly normalizing terms belong to the same type sets only if they are the same term, or both are in <code>Min</code>. So the semantics identifies no two different terms: not convertible ones, such as <code>I I</code> and <code>I</code>, and not even a term and its head reduct. An equality between terms is therefore never built in. It has to be added as a type set, …</p>',
'<p>The lemma “Type sets tell evaluations apart” in §7 says that two strongly normalizing terms belong to the same type sets only if they have the same evaluation, or both get stuck. So the semantics identifies a term with its evaluation, as <code>I I</code> with <code>I</code>, and with nothing else: not with <code>λx.K x</code> and <code>K</code>, and not with convertible terms in general. Every coarser equality between terms is therefore not built in. It has to be added as a type set, …</p>',
'In the definition of <code>E<sub>R</sub></code> the note changes accordingly: “having the same evaluation” is now the relation the semantics has, and the lemma on <code>E<sub>R</sub></code> is unchanged.')

# ---------------------------------------------------------------- §36 families
add('§36 The three collections', 'Definition · Value, evaluation, head-closed type set', 'deleted', S('families.html|Definition · Value'), None,
'Moved to §2 and §5. The name “head-closed type set” is no longer needed: these are the type sets.')

add('§36 The three collections', 'Lemma · The three collections form a chain', 'changed', S('families.html|Lemma · The three collections'),
'''<section class="box thm">
  <p class="tag">Lemma · The three collections form a chain</p>
  <p>Write <code>SAT</code> for the collection of sets that satisfy the SN condition, the Base condition and the direction from <code>s′</code> to <code>s</code> of the closure condition only; these are Tait’s saturated sets, and narrow point 5 showed that they carry the theorem. Write <code>TS</code> for the type sets of this page, and <code>CR</code> for the candidates.</p>
  <dl class="conds">
    <dt>chain</dt><dd><code>CR ⊆ TS ⊆ SAT</code>.</dd>
    <dt>same operations</dt><dd>Each collection is closed under the intersection and under the union of a nonempty set of its members, computed as sets. So every nonempty set of members has a largest member below it and a smallest member above it, which is what “complete lattice” means in standard terms; and these are computed in the same way in all three.</dd>
    <dt>same ends</dt><dd><code>Min</code> and <code>SN</code> belong to all three collections. <code>Min</code> is the smallest member and <code>SN</code> the largest, in each.</dd>
  </dl>
</section>''',
'The page’s own collection is now the middle one. The four conversions, the commuting lemma and the lemma “Each collection carries the theorem” are unchanged in content; the last one now has to be stated for a larger collection as well as for a smaller one, and its proof is the same.')

add('§36 The three collections', 'Lemma · Head-closed type sets are sets of values', 'deleted', S('families.html|Lemma · Head-closed type sets are sets of values'), None,
'Moved to §5 as “Type sets are sets of values”. The item <i>candidates</i> (a type set is a candidate if and only if its set of values is closed under steps) and the item <i>not so for SAT</i> stay in §36, under the chain lemma.')

hc_C = S('families.html|Lemma · Only the head-closed').replace('Lemma · Only the head-closed type sets have complements', 'Lemma · Type sets have complements, and the two other collections do not')
hc_C = hc_C.replace('<p>In <code>HC</code> every type set <code>T</code> has a complement:', '<p>Every type set <code>T</code> has a complement:')
hc_C = hc_C.replace('is head-closed, <code>T ∩ T′ = Min</code>', 'is a type set, <code>T ∩ T′ = Min</code>')
hc_C = hc_C.replace('<p class="note">So in <code>HC</code> a choice of values can be negated, and in the other two collections it cannot. In standard terms, <code>HC</code> is a power set up to <code>Min</code>, and so a complete Boolean algebra, and the other two are not. No result on this page uses this; it is listed because it is the sharpest way to say what the head-closed type sets are.</p>',
 '<p class="note">So a choice of values can be negated, and in the other two collections it cannot. In standard terms, the type sets form a power set up to <code>Min</code>, and so a complete Boolean algebra, and the other two collections do not. No result on this page uses this; it is listed because it is the sharpest way to say what a type set is.</p>')
hc_C = hc_C.replace('Nor would a complement give a rule even in <code>HC</code>:', 'Nor does a complement give a rule:')
hc_C = hc_C.replace('So the page never needs a complement, and working in the largest collection costs nothing here.', 'So the page never needs a complement.')
assert hc_C != S('families.html|Lemma · Only the head-closed')
add('§36 The three collections', 'Lemma · Only the head-closed type sets have complements', 'changed', S('families.html|Lemma · Only the head-closed'), hc_C,
'The content is the same; the subject is now the page’s own collection.')

add('§36 The three collections', 'Remark · What the choice in §5 means', 'changed', S('families.html|Remark · What the choice'),
'''<section class="aside">
  <p class="tag">Remark · What the choice in §5 Type sets means</p>
  <p>The definition in §5 picks the middle of the three collections. The largest, Tait’s, asks less of a set, and narrow point 5 showed that it carries the theorem with the same proofs; the smallest, Girard’s, asks that a term and all its reducts share their type sets. Limit 3 of §23, that a member can leave a type set by a step inside an abstraction, is the price of stopping in the middle; the candidates remove it altogether.</p>
  <p>The case for each is short. For <code>SAT</code>: it is the largest, every closure proof is one line shorter, and it is the one with a name and a literature; its price is that a type set is only roughly a set of values. For the type sets of this page: a type set is exactly a set of values, with complements, which is the object that the semantics of programming languages works with; the price is one more line in every closure proof, and that the collection has no name in the literature. For <code>CR</code>: a term keeps its type sets while it runs, which is what typing usually promises, and it is Girard’s. The theorem does not care, by the lemma “Each collection carries the theorem”, and nothing in the main line depends on the choice; the main line asks only what the remark in §13 lists. §38 Pairs runs the same theory on pairs of terms, so that a type expression names a relation between values. §37 Tests adds a fourth collection below the candidates, the sets defined by tests.</p>
</section>''',
'The remark changes sides: it now has to explain why the page did not take the largest collection, and the only honest answer is the values picture.')

# ---------------------------------------------------------------- §38 pairs
hc_P = S('pairs.html|Definition · Pairs').replace('read for pairs: inside <code>SN</code>, containing <code>Base</code>, closed under undoing safe head steps.',
 'read for pairs: inside <code>SN</code>, containing <code>Base</code>, closed under safe head steps taken jointly, in both directions.')
assert hc_P != S('pairs.html|Definition · Pairs')
add('§38 Pairs', 'Definition · Pairs, and relations', 'changed', S('pairs.html|Definition · Pairs'), hc_P,
'A relation is then determined by the pairs it contains that take no joint head step; among them the pairs of values, which is the usual form of a parametricity relation, but also mixed pairs such as <code>(I, y)</code>.')

add('§35 Other collections of sets', 'Lemma · Candidates are the type sets that are closed under steps', 'unchanged', S('cmpsets.html|Lemma · Candidates'), S('cmpsets.html|Lemma · Candidates'),
'Unchanged in statement and proof: the candidates are inside the type sets of both pages.')

# ---------------------------------------------------------------- render
def frame(label, body, cls):
    return '<div class="fr %s"><div class="lab">%s</div>%s</div>' % (cls, label, body)

parts = []
for it in ITEMS:
    st = it['status']
    badge = {'changed': 'changed', 'added': 'added under HC', 'deleted': 'deleted under HC', 'unchanged': 'statement unchanged'}[st]
    h = ['<section class="item %s">' % st, '<h2><span class="sec">%s</span> %s <span class="badge">%s</span></h2>' % (html.escape(it['sec']), html.escape(it['title']), badge)]
    if it['sat'] is None:
        h.append(frame('SAT — as on the page', '<p class="empty">absent</p>', 'empty'))
    else:
        h.append(frame('SAT — as on the page', deref(it['sat']), 'sat'))
    if it['hc'] is None:
        h.append(frame('HC — as it would be', '<p class="empty">deleted</p>', 'empty'))
    elif st == 'changed':
        h.append(frame('HC — as it would be, with the differences marked', diff_html(deref(it['sat']), deref(it['hc'])), 'hc'))
    elif st == 'added':
        h.append(frame('HC — as it would be', deref(it['hc']), 'hc'))
    else:
        pass
    if it['note']:
        h.append('<p class="why">%s</p>' % deref(it['note']))
    h.append('</section>')
    parts.append('\n'.join(h))

counts = {k: sum(1 for i in ITEMS if i['status'] == k) for k in ('changed', 'added', 'deleted', 'unchanged')}

head = open(P + 'src/_head.html', encoding='utf8').read()
# take the page's style block only
style = re.search(r'<style>.*?</style>', head, re.S).group(0)
EXTRA = '''<style>
.page{max-width:60rem}
.item{margin:2.4rem 0;padding-top:.4rem;border-top:1px solid var(--rule)}
.item h2{font-size:1.05rem;margin:.6rem 0 .8rem}
.item h2 .sec{color:var(--muted);font-weight:500;margin-right:.4rem}
.badge{display:inline-block;font:600 .68rem/1 system-ui;letter-spacing:.08em;text-transform:uppercase;padding:.3rem .5rem;border-radius:.3rem;margin-left:.5rem;vertical-align:middle;background:var(--chip);color:var(--fg)}
.item.changed .badge{background:#f0dfa0;color:#4a3800}.item.added .badge{background:#cfe8cf;color:#174217}.item.deleted .badge{background:#f3c9c4;color:#5a1a12}.item.unchanged .badge{background:#dfe6ee;color:#2a3a4a}
:root[data-theme="dark"] .item.changed .badge{background:#6a5410;color:#ffe9a8}:root[data-theme="dark"] .item.added .badge{background:#1f4a1f;color:#cfe8cf}:root[data-theme="dark"] .item.deleted .badge{background:#5a1a12;color:#f3c9c4}:root[data-theme="dark"] .item.unchanged .badge{background:#2a3a4a;color:#dfe6ee}
.fr{position:relative;margin:.9rem 0 .9rem;padding:1.6rem .9rem .5rem;border:1px solid var(--rule);border-radius:.5rem}
.fr .lab{position:absolute;top:-.55rem;left:.8rem;padding:0 .4rem;background:var(--bg);font:600 .68rem/1.1 system-ui;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.fr.hc{border-color:#8a6d00}.fr.empty{border-style:dashed;min-height:3.2rem}
.fr .box,.fr .aside{margin:.4rem 0}
.empty{color:var(--muted);font-style:italic;margin:.2rem 0 .4rem}
ins{background:#cfe8cf;color:#174217;text-decoration:none;border-radius:.15rem;padding:0 .08em}
del{background:#f3c9c4;color:#5a1a12;text-decoration:line-through;border-radius:.15rem;padding:0 .08em}
:root[data-theme="dark"] ins{background:#1f4a1f;color:#cfe8cf}:root[data-theme="dark"] del{background:#5a1a12;color:#f3c9c4}
.fr code,.fr del,.fr ins{white-space:normal;overflow-wrap:anywhere}
.item h2{display:flex;flex-wrap:wrap;align-items:center;gap:.3rem .5rem}.badge{white-space:nowrap;margin-left:0}
.fr dl.conds,.fr dl.rows{overflow-wrap:anywhere;min-width:0}.fr dl.conds dd,.fr dl.rows dd{min-width:0}
@media (max-width:480px){.fr{padding-left:.45rem;padding-right:.45rem}.fr dl.conds,.fr dl.rows{grid-template-columns:1fr}.fr dl.conds dt,.fr dl.rows dt{margin-top:.4rem}}
.why{margin:.4rem 0 0;padding-left:.9rem;border-left:3px solid var(--rule);color:var(--muted)}
.sum td,.sum th{padding:.3rem .6rem}
</style>'''
# find css variable names used for bg/rule/muted in the page's style; fall back if different
css_vars = re.findall(r'--([a-z]+):', style)
def pick(*names):
    for n in names:
        if n in css_vars: return '--' + n
    return '--' + names[0]
EXTRA = EXTRA.replace('var(--rule)', 'var(%s)' % pick('rule', 'line', 'border')).replace('var(--muted)', 'var(%s)' % pick('muted', 'dim', 'fg2')).replace('var(--bg)', 'var(%s)' % pick('bg', 'paper')).replace('var(--chip)', 'var(%s)' % pick('chip', 'tagbg', 'bg2')).replace('var(--fg)', 'var(%s)' % pick('fg', 'ink', 'text'))

INTRO = '''<header class="head">
  <p class="eyebrow">A side-by-side reading of The Narrow Path</p>
  <h1>SAT or HC</h1>
  <p class="lede">The page defines a type set with Tait’s three conditions (<code>SAT</code>): inside <code>SN</code>, containing <code>Base</code>, closed under undoing safe head steps. This comparison shows what the page would say if the definition asked, in addition, that a type set is closed under taking head steps (<code>HC</code>, the head-closed type sets of §36). For every definition, lemma, example and remark that would change, the version on the page comes first, and the version under <code>HC</code> below it; in a changed item the words that go are struck through and the words that come are marked. An item that would disappear is followed by an empty frame; an item that would have to be added is preceded by one. Items whose statement does not change are listed once, with what happens to their proofs. Nothing here is on the main page.</p>
</header>
<section class="box">
  <p class="tag">In one paragraph</p>
  <p>The theorem and its proof do not change: no fact and no rule uses the added direction, which is why the SAT page can call its definition the narrow path and the HC page could not (narrow point 5 below is a trial that succeeds). What changes is the picture and the examples. Under <code>HC</code> a type set is exactly a set of values, the lemma that says so moves next to the definition, and the semantics identifies a term with its evaluation; <code>Gen({I I})</code> gains <code>I</code>, the chain of Lemma L collapses, limit 3 shrinks to steps inside abstractions, and <code>Gen({λx.I x})</code> takes over the role of the escaping member. Every addition pays one more line, that its set is closed under head steps. §36 changes sides: the page’s collection becomes the middle one, the complements lemma is about it, and the remark has to explain why the largest collection was not taken.</p>
  <div class="tw"><table class="w34 sum"><thead><tr><th>changed</th><th>added</th><th>deleted</th><th>statement unchanged</th></tr></thead><tbody><tr><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr></tbody></table></div>
</section>
''' % (counts['changed'], counts['added'], counts['deleted'], counts['unchanged'])

doc = '<title>SAT or HC</title>\n' + style + '\n' + EXTRA + '\n<div class="page">\n' + INTRO + '\n'.join(parts) + '\n</div>\n'
# the main page's js is not needed; keep theme attribute handling simple
os.makedirs(P + 'out', exist_ok=True)
open(P + 'out/sat-or-hc.html', 'w', encoding='utf8').write(doc)
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + '<title>SAT or HC</title>\n' + style + '\n' + EXTRA + '\n</head>\n<body>\n<div class="page">\n' + INTRO + '\n'.join(parts) + '\n</div>\n</body>\n</html>\n')
open(P + 'docs/sat-or-hc.html', 'w', encoding='utf8').write(full)
print('items', len(ITEMS), counts, 'chars', len(doc))
