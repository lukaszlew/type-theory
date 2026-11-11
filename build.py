"""Build the page from one file per section (src/<slug>.html), in the order of plan.py.

Writes docs/index.html (a complete HTML document, served by GitHub Pages) and out/narrow-path.html (the same page
without the document skeleton, for publishing as a claude.ai artifact). Needs Python 3 and Graphviz (dot).

Every cross reference in a part is written {{slug}}; a literal '§' in the text is an error. The lint checks that every
earlier section a part refers to is among the sections it uses, apart from the pointers listed in POINTER_OK.
"""
import re, sys, json, subprocess, os
P = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, P)
from plan import PARTS, SECTIONS, NUM, USES, USEDBY, PARENTS, GOALS, ancestors
D = P + 'src/'
rd = lambda n: open(D + n, encoding='utf8').read()
S = {s[0]: [rd(s[0] + '.html').rstrip('\n')] for s in SECTIONS}
FRONT = [rd('_front.html').rstrip('\n')]
BACK = [rd('_back.html').rstrip('\n')]
head = rd('_head.html')
tail = rd('_tail.html')
missing = [f for f in os.listdir(D) if f.endswith('.html') and not f.startswith('_') and f[:-5] not in NUM]
assert not missing, ('parts without a section', missing)

# =============================================================== lint: every reference against the plan
NPSEC = {1: 'obstacle', 2: 'simpler', 3: 'simpler', 4: 'simpler', 5: 'allsets', 6: 'true', 7: 'allkinds'}
LABELS = [
    (r'\bR[123]\b|Lemma R\b', 'head'), (r'\bM[123]\b|Lemma M\b', 'typeset'), (r'\bE[1-4]\b|\bL[1-4]\b|Lemma E\b|Lemma L\b', 'structure'),
    (r'\bW[1-5]\b', 'obstacle'), (r'\bN[012]\b|Lemma N\b', 'names'), (r'\bN3\b', 'fomega'), (r'\bN4\b', 'dep'), (r'\bC[12]\b', 'rules'),
    (r'arrow lemma|intersection lemma|union lemma', 'ops'), (r'generation lemma', 'gen'), (r'soundness theorem', 'rules'),
    (r'four facts|<i>(?:[Aa]pply|[Aa]bstract|[Gg]eneralize|[Ii]nstantiate)</i>', 'facts'),
    (r'T<sub>[IK]</sub>|Gen\(|\bMin\b|\bBase\b', 'typeset'), (r'\bID\b|\bBOOL\b', 'ops'), (r'EQ\(', 'darrow'), (r'System D\b', 'and'),
    (r'\bfamil(?:y|ies)\b', 'fam'), (r'\bkinds?\b', 'kinds'), (r'[Ll]imit [1-4]\b', 'limits'),
]
# pointers: a section names another section without using a definition or a result of it in a statement or a proof
POINTER_OK = {
    ('families', 'kinds'): 'unused',
    ('cmpsem', 'classical'): 'the row on tests points to the section',
    ('mu', 'structure'): 'the closing remark names lemmas that were not read again', ('mu', 'families'): 'the closing remark names lemmas that were not read again',
    ('cmpsem', 'pairs'): 'one row of the table points to the equality relations',
    ('mu', 'gen'): 'the closing remark names the lemma that was not read again',
    ('classical', 'andsn'): 'the closing remark compares a quoted theorem with it',
    ('good', 'structure'): 'says which lemmas use more about SN',
    ('limits', 'simpler'): 'limit 4 says that narrow point 3 comes back',
    ('more', 'and'): 'says that the rules are read off as for ∧',
    ('allkinds', 'more'): 'one line of the list of new kinds mentions μ',
    ('allkinds', 'fam'): 'one line of the list of new kinds mentions families',
    ('allkinds', 'allsets'): 'narrow point 7 is contrasted with narrow point 5',
    ('cube', 'strength'): 'the table repeats the row for System F',
    ('cube', 'limits'): 'says that limit 4 applies to inductive types',
    ('cube', 'allsets'): 'names narrow point 5',
    ('cube', 'true'): 'names narrow point 6',
    ('cmpsets', 'simpler'): 'names narrow point 2',
    ('cmpsets', 'limits'): 'names limit 4',
    ('cmpsets', 'more'): 'names the existential types',
    ('cmpsets', 'kinds'): 'one paragraph says how kinds were read',
    ('cmpsets', 'allkinds'): 'the same paragraph names narrow point 7',
    ('cmpsets', 'true'): 'says that both sets contain what the rules give',
    ('harper', 'more'): 'compares his exercises',
    ('harper', 'limits'): 'compares his exercises',
    ('darrow', 'allsets'): 'an example names narrow point 5',
    ('andsn', 'andlaws'): 'names the law that is true and not derivable',
    ('andsn', 'allsets'): 'names narrow point 5',
    ('self', 'kinds'): 'the remark on System S speaks of F-omega',
    ('rules', 'allsets'): 'an example names narrow point 5',
    ('equality', 'simpler'): 'names narrow point 2', ('equality', 'dinter'): 'the closing table points to it', ('equality', 'implicit'): 'the closing table points to it',
    ('equalities', 'limits'): 'the closing remark names limit 1', ('equalities', 'dep'): 'lists N4', ('equalities', 'darrow'): 'the table points to EQ', ('equalities', 'fam'): 'recalls the definition of convertible',
    ('cmpsem', 'good'): 'the lineage list names it',
    ('cmpsets', 'fam'): 'the word family in a pointer', ('families', 'and'): 'the closing remark names the additions', ('families', 'allsets'): 'the note on complements names the counting lemma', ('families', 'self'): 'the closing remark names the additions', ('families', 'implicit'): 'the closing remark names the additions', ('cmpsem', 'more'): 'the lineage list names it', ('cmpsem', 'equality'): 'the table points to it',
    ('more', 'andlaws'): 'subtyping points to the laws of the intersection',
    ('cube', 'dinter'): 'the table names the range of sections on dependent types',
    ('fam', 'allsets'): 'an example compares with the counting lemma', ('families', 'limits'): 'the closing remark names limit 3',
    ('cmpsem', 'families'): 'the table points to the chain', ('families', 'and'): 'the closing remark names the additions', ('families', 'allsets'): 'the note on complements names the counting lemma',
    ('equalities', 'families'): 'a note names the evaluation of a term',
    ('induct', 'limits'): 'the closing remark names limit 1', ('induct', 'equality'): 'the closing remark names the rule φ',
    ('hyp', 'induct'): 'one bullet points to casts', ('hyp', 'equalities'): 'the closing remark points to the lemma on E_R',
    ('impred', 'fomega'): 'the table names ∀X:κ and the remark on power sets', ('impred', 'allkinds'): 'names narrow point 7', ('impred', 'cube'): 'names the strength table',
    ('pairs', 'structure'): 'the closing remark names the lemma that type sets tell terms apart', ('pairs', 'and'): 'the closing remark lists the additions',
    ('pairs', 'more'): 'the closing remark lists the additions', ('pairs', 'fam'): 'the closing remark names families', ('pairs', 'equalities'): 'the closing remark names what it turned away',
    ('pairs', 'families'): 'the closing remark names the three collections', ('tests', 'cmpsets'): 'names Riba’s theorem', ('equalities', 'pairs'): 'the closing remark points to the relational reading', ('tests', 'kinds'): 'the word kind', ('cmpsem', 'tests'): 'the table points to the lemma on tests', ('tests', 'typeset'): 'names the closure condition', ('tests', 'lookback'): 'the remark on Krivine’s realizability names the three demands', ('tests', 'equality'): 'the same remark names Stump’s semantics', ('forget', 'kinds'): 'the word kind, in a quotation', ('complete', 'kinds'): 'the word kind', ('complete', 'simpler'): 'names narrow point 2', ('erasure', 'allkinds'): 'the closing remark names the two readings of kinds',
}
report, forward = [], []
for slug in NUM:
    text = '\n'.join(S[slug])
    anc = ancestors(slug)
    refs = set(re.findall(r'\{\{(\w+)\}\}', text))
    text_nt = re.sub(r'\{\{\w+\}\}', '', text)
    for pat, where in LABELS:
        if re.search(pat, text_nt):
            refs.add(where)
    for m in re.finditer(r'[Nn]arrow points? ((?:\d(?:, | and | to )?)+)', text):
        for d in re.findall(r'\d', m.group(1)):
            refs.add(NPSEC[int(d)])
    for r in sorted(refs, key=lambda x: NUM[x]):
        if r == slug or r in anc:
            continue
        if NUM[r] > NUM[slug]:
            forward.append((slug, r))
        elif (slug, r) in POINTER_OK:
            continue
        else:
            report.append((slug, r))
stale = [k for k in POINTER_OK if k[1] in ancestors(k[0])]
print('pointer entries that are now real uses:', stale)
print('LINT: backward references to a section that is not used:', len(report))
for s_, r in report:
    print('   §%d %s -> §%d %s' % (NUM[s_], s_, NUM[r], r))
print('forward pointers:', len(forward))
print('   ' + ', '.join('%d>%d' % (NUM[a], NUM[c]) for a, c in forward))

# =============================================================== the graph
SHORT = {s[0]: s[3] for s in SECTIONS}
TITLE = {s[0]: s[2] for s in SECTIONS}
PART = {s[0]: s[1] for s in SECTIONS}
MAIN = ancestors('rules') | {'rules'}


def graph():
    W_IN, H_IN = 1.56, 0.36
    L = ['digraph G {', 'rankdir=TB; ranksep=0.42; nodesep=0.1; splines=true;',
         'node [shape=box, fixedsize=true, width=%s, height=%s, fontsize=10, margin=0];' % (W_IN, H_IN), 'edge [arrowsize=0.55];']
    for s in SECTIONS:
        L.append('%s [label="%d %s"];' % (s[0], NUM[s[0]], s[3]))
    for s in SECTIONS:
        for u in PARENTS[s[0]]:
            L.append('%s -> %s;' % (u, s[0]))
    L.append('}')
    g = json.loads(subprocess.run(['dot', '-Tjson'], input='\n'.join(L).encode(), capture_output=True, check=True).stdout)
    x0, y0, x1, y1 = [float(v) for v in g['bb'].split(',')]
    PAD = 3
    Wd, Hd = x1 - x0 + 2 * PAD, y1 - y0 + 2 * PAD
    fx = lambda x: round(x - x0 + PAD, 1)
    fy = lambda y: round(y1 - y + PAD, 1)
    names = {o['_gvid']: o['name'] for o in g['objects']}
    out = ['<svg viewBox="0 0 %d %d" role="group" aria-label="The sections of this page and what each one uses. The main line runs from section 1 through sections 2, 4, 5, 8, 9, 10 and 12 to section 13, the soundness theorem. Every other section branches off it.">' % (round(Wd), round(Hd))]
    out.append('<g class="de" fill="none" stroke="currentColor" stroke-width="1">')
    heads = []
    for e in g['edges']:
        pts = None
        for op in e.get('_draw_', []):
            if op['op'] == 'b':
                pts = op['points']
        d = 'M%s %s' % (fx(pts[0][0]), fy(pts[0][1]))
        for k in range(1, len(pts), 3):
            d += 'C' + ' '.join('%s %s' % (fx(p[0]), fy(p[1])) for p in pts[k:k + 3])
        both = names[e['tail']] in MAIN and names[e['head']] in MAIN
        ends = ' data-t="%d" data-h="%d"' % (NUM[names[e['tail']]], NUM[names[e['head']]])
        out.append('<path%s%s d="%s"/>' % (' class="m"' if both else '', ends, d))
        for op in e.get('_hdraw_', []):
            if op['op'] == 'P':
                heads.append('<polygon%s points="%s"/>' % (ends, ' '.join('%s,%s' % (fx(p[0]), fy(p[1])) for p in op['points'])))
    out.append('</g>')
    out.append('<g class="dh" fill="currentColor" stroke="currentColor" stroke-width="1">' + ''.join(heads) + '</g>')
    out.append('<g class="dn">')
    w, h = W_IN * 72, H_IN * 72
    for o in g['objects']:
        slug = o['name']
        cx, cy = [float(v) for v in o['pos'].split(',')]
        x, y = fx(cx - w / 2), fy(cy + h / 2)
        out.append('<a href="#s-%s" data-n="%d"%s><title>§%d %s</title><rect x="%s" y="%s" width="%s" height="%s" rx="2"/><text x="%s" y="%s"><tspan class="num">%d</tspan> %s</text></a>' % (
            slug, NUM[slug], ' class="m"' if slug in MAIN else '', NUM[slug], re.sub(r'<[^>]+>', '', TITLE[slug]), x, y, round(w, 1), round(h, 1), fx(cx), round(fy(cy) + 3.8, 1), NUM[slug], SHORT[slug]))
    out.append('</g></svg>')
    return '\n'.join(out), round(Wd), round(Hd)


SVG, GW, GH = graph()
main_nums = sorted(NUM[s_] for s_ in MAIN)
FIG = ('<figure class="fig dep">\n<div class="tw">' + SVG + '</div>\n'
       '<figcaption>An arrow from one section to another says that the second uses a definition or a result of the first. Arrows that follow from other arrows are left out. '
       'The heavy boxes are the main line: the nine sections that the soundness theorem in {{rules}} needs.</figcaption>\n</figure>')

# =============================================================== assembly
ROMAN = {p: t.replace('ω', '<span class="lc">ω</span>') for p, t in PARTS}


def uses_line(slug):
    u = USES[slug]
    ub = USEDBY[slug]
    u = sorted(u, key=lambda x: NUM[x])
    a = 'Uses nothing before it.' if not u else 'Uses ' + ', '.join('{{%s}} %s' % (x, TITLE[x]) for x in u) + '.'
    c = 'No later section uses it.' if not ub else 'Used by ' + ', '.join('{{%s}}' % x for x in ub) + '.'
    return '<p class="uses">' + a + ' ' + c + '</p>'


GOALSETS = []
for label, targets in GOALS:
    if targets is None:
        GOALSETS.append([label, None])
    else:
        sset = set(targets)
        for t_ in targets:
            sset |= ancestors(t_)
        GOALSETS.append([label, sorted(NUM[x] for x in sset)])
ANC = {NUM[s_]: sorted(NUM[x] for x in ancestors(s_) | {s_}) for s_ in NUM}
SELECT = ('<div class="goal"><label for="goal">I want to learn</label> <select id="goal">' + ''.join('<option value="%d">%s</option>' % (i, g[0]) for i, g in enumerate(GOALSETS)) + '</select> <span class="note" id="goal-list"></span></div>')
INTRO = ['<p class="lab">How the sections depend on each other</p>',
         '<p>The page has %d short sections in eight parts. Under its heading, each section lists the sections that it uses. To read one section, read those first, and the ones that they use. '
         'The proof of the main theorem is the main line of the graph, and everything else branches off it. Pick what you want to learn, and the graph and the contents show the sections it needs.</p>' % len(SECTIONS),
         SELECT, FIG, '<p class="lab">Contents</p>']
toc = []
for p, t in PARTS:
    toc.append('<p class="tocp">Part %s · %s</p>' % (p, ROMAN[p]))
    toc.append('<ol class="toc">\n' + '\n'.join('  <li data-n="%d"><span class="n">§%d</span><span><a href="#s-%s">%s</a></span></li>' % (NUM[s[0]], NUM[s[0]], s[0], s[2]) for s in SECTIONS if s[1] == p) + '\n</ol>')
body = FRONT + INTRO + toc
last = None
for s in SECTIONS:
    slug = s[0]
    if s[1] != last:
        body.append('<p class="part">Part %s · %s</p>' % (s[1], ROMAN[s[1]]))
        last = s[1]
    body.append('<h2 id="s-%s"><span class="sec">§%d</span>%s</h2>' % (slug, NUM[slug], s[2]))
    body.append(uses_line(slug))
    body += S[slug]
body += BACK
html = '\n\n'.join(body)

# ---- no switches: chips and classes go
html = re.sub(r'<span class="fwm">(?:Fω|Π)</span> ?', '', html)


def clean_class(m):
    toks = [t for t in m.group(1).split() if t not in ('fw', 'dp')]
    return ' class="%s"' % ' '.join(toks) if toks else ''


html = re.sub(r' class="([^"]*)"', clean_class, html)
assert 'href="#cube"' not in html and 'class="st ' not in html
# ---- references become links
left = re.findall(r'§\d+', re.sub(r'<span class="(?:sec|n)">§\d+</span>|<title>§\d+', '', html))
assert not left, left[:10]
html = re.sub(r'\{\{(\w+)\}\}', lambda m: '<a class="xr" href="#s-%s">§%d</a>' % (m.group(1), NUM[m.group(1)]), html)
assert '{{' not in html

# ---- tail: regenerate the goal tables
tail = re.sub(r'  var GOALS=.*?;\n', '  var GOALS=' + json.dumps(GOALSETS, ensure_ascii=False) + ';\n', tail, count=1, flags=re.S)
tail = re.sub(r'  var ANC=.*?;\n', '  var ANC=' + json.dumps(ANC) + ';\n', tail, count=1, flags=re.S)
assert tail.count('var GOALS=[') == 1 and tail.count('var ANC={') == 1
out = head + html + '\n\n' + tail
os.makedirs(P + 'out', exist_ok=True); os.makedirs(P + 'docs', exist_ok=True)
open(P + 'out/narrow-path.html', 'w', encoding='utf8').write(out)
# the complete document for GitHub Pages: head elements (title, fonts, style) into <head>, the rest into <body>
m = re.match(r'(.*?</style>\s*)(.*)$', out, re.S)
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
       + m.group(1).replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '') + '</head>\n<body>\n' + m.group(2) + '\n</body>\n</html>\n')
open(P + 'docs/index.html', 'w', encoding='utf8').write(doc)
print('written', len(out), 'chars; graph', GW, 'x', GH)
print('balance', out.count('<section'), out.count('</section>'), out.count('<details'), out.count('</details>'), out.count('<dl'), out.count('</dl>'), out.count('<ul'), out.count('</ul>'), out.count('<ol'), out.count('</ol>'), out.count('<table'), out.count('</table>'), out.count('<figure'), out.count('</figure>'))
if '--words' in sys.argv:
    plain = re.sub(r'<[^>]+>', '', out)
    for w in ('above', 'below', 'this section', 'This section', 'family', 'terminat'):
        hits = [plain[m.start() - 50:m.end() + 40].replace('\n', ' ') for m in re.finditer(re.escape(w), plain)]
        print('==', repr(w), len(hits))
        for h_ in hits[:20]:
            print('     ', h_)
