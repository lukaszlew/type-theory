"""Regenerate compare/sat.json: the SAT statements that the comparison page shows and diffs against the HC versions."""
import re, json, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
D = P + 'src/'
def boxes(file):
    s = open(D + file, encoding='utf8').read()
    return [(re.sub(r'<[^>]+>', '', m.group(2)), m.group(0)) for m in
            re.finditer(r'<section class="(box[^"]*|aside)"(?: id="[^"]*")?>\s*<p class="tag">(.*?)</p>(.*?)</section>', s, re.S)]
want = {
 'typeset.html': ['Definition · Type set', 'Definition · Gen(S) and Min', 'Lemma M', 'Example · A type set built from two terms', 'Example · A member can leave by running'],
 'structure.html': ['Lemma E', 'Lemma L', 'Lemma · Type sets tell'],
 'ops.html': ['Arrow lemma', 'Intersection lemma', 'Union lemma'],
 'price.html': ['Addition lemma'],
 'limits.html': ['Limit 3'],
 'darrow.html': ['Lemma · The dependent arrow'],
 'self.html': ['Addition · Self types'],
 'dinter.html': ['Lemma · The dependent intersection'],
 'families.html': ['Definition · Value', 'Lemma · The three collections', 'Lemma · Head-closed type sets are sets of values', 'Lemma · Only the head-closed', 'Remark · What the choice'],
 'pairs.html': ['Definition · Pairs'],
 'cmpsets.html': ['Lemma · Candidates'],
}
sat = {}
for f, names in want.items():
    bs = boxes(f)
    for n in names:
        hit = [b for t, b in bs if t.startswith(n)]
        assert hit, (f, n)
        sat[f + '|' + n] = hit[0]
json.dump(sat, open(P + 'compare/sat.json', 'w'), ensure_ascii=False, indent=1)
print('dumped', len(sat))
