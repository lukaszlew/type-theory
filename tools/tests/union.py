import sys
sys.setrecursionlimit(10000)
exec(open('feed.py').read().split('MAXK=')[0])
LIMIT=1500
# tests: tuples of closed normal terms up to size 5 (incl delta), length<=2
args=[]
for s in range(2,6): args+=normals(s,0)
tests=[()]+[(a,) for a in args]+[(a,b) for a in args for b in args]
def passes(t,v):
    cur=t
    for a in v: cur=('a',cur,a)
    return nf(cur,LIMIT)[0] is not None
cands=[]
for s in range(2,8): cands+=normals(s,0)
print(len(cands),'candidate terms',len(tests),'tests')
# orthogonal of a term: tests it passes
import collections
passed={i:frozenset(j for j,v in enumerate(tests) if passes(t,v)) for i,t in enumerate(cands)}
# biorthogonal closure within the candidate set: cl(S) = {t : passed[t] ⊇ ⋂_{s∈S} passed[s]}
def closure(S):
    common=frozenset.intersection(*[passed[i] for i in S]) if S else frozenset()
    return frozenset(i for i in passed if passed[i]>=common)
# check union closure for singletons: cl({a}) ∪ cl({b}) vs cl({a,b})
bad=0
for a in range(len(cands)):
    for b in range(a+1,len(cands)):
        A=closure({a}); B=closure({b}); AB=closure({a,b})
        if AB!=(A|B):
            bad+=1
            if bad<=3:
                extra=AB-(A|B)
                print('union not closed:', show(cands[a]), '|', show(cands[b]), 'extra e.g.', show(cands[next(iter(extra))]))
    if bad>=3: break
print('bad pairs found', bad)
