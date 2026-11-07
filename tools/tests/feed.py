# Enumerate closed normal lambda terms (de Bruijn) up to a size, feed them deltas, and look for terms that survive.
import sys
sys.setrecursionlimit(10000)
# term: ('v',i) | ('l',body) | ('a',f,x)
def shift(t,d,c=0):
    k=t[0]
    if k=='v': return ('v', t[1]+d if t[1]>=c else t[1])
    if k=='l': return ('l', shift(t[1],d,c+1))
    return ('a', shift(t[1],d,c), shift(t[2],d,c))
def subst(t,s,j=0):
    k=t[0]
    if k=='v':
        if t[1]==j: return shift(s,j)
        return ('v', t[1]-1 if t[1]>j else t[1])
    if k=='l': return ('l', subst(t[1],s,j+1))
    return ('a', subst(t[1],s,j), subst(t[2],s,j))
def step(t):
    "leftmost-outermost step; None if normal"
    k=t[0]
    if k=='v': return None
    if k=='l':
        b=step(t[1]); return ('l',b) if b is not None else None
    f,x=t[1],t[2]
    if f[0]=='l': return subst(f[1],x)
    f2=step(f)
    if f2 is not None: return ('a',f2,x)
    x2=step(x)
    if x2 is not None: return ('a',f,x2)
    return None
def nf(t,limit):
    for i in range(limit):
        u=step(t)
        if u is None: return t,i
        t=u
    return None,limit
DELTA=('l',('a',('v',0),('v',0)))
# enumerate closed normal forms with n free vars allowed (depth), size bound
from functools import lru_cache
@lru_cache(None)
def normals(size,depth):
    "all normal terms of given size with free vars < depth"
    out=[]
    if size==1:
        for i in range(depth): out.append(('v',i))
        return out
    # abstraction
    for b in normals(size-1,depth+1): out.append(('l',b))
    # neutral: v a1 ... am  (size = 1 + sum sizes + m?) we count size as nodes: app node adds 1
    out += neutrals(size,depth)
    return out
@lru_cache(None)
def neutrals(size,depth):
    out=[]
    if size==1:
        return [('v',i) for i in range(depth)]
    for s1 in range(1,size-1):
        for f in neutrals(s1,depth):
            for x in normals(size-1-s1,depth):
                out.append(('a',f,x))
    return out
def show(t,names='xyzuvwpqrs'):
    def go(t,d):
        if t[0]=='v': return names[d-1-t[1]] if d-1-t[1]>=0 else '?'
        if t[0]=='l': return 'λ'+names[d]+'.'+go(t[1],d+1)
        f=go(t[1],d); x=go(t[2],d)
        if t[2][0]!='v': x='('+x+')'
        if t[1][0]=='l': f='('+f+')'
        return f+' '+x
    return go(t,0)
MAXK=int(sys.argv[2]) if len(sys.argv)>2 else 8
LIMIT=3000
total=0; survivors=[]
for size in range(2,int(sys.argv[1])+1):
    for t in normals(size,0):
        total+=1
        cur=t; ok=True
        for k in range(1,MAXK+1):
            cur=('a',cur,DELTA)
            n,steps=nf(cur,LIMIT)
            if n is None: ok=False; break
            cur=n
        if ok: survivors.append((size,show(t)))
    print('size',size,'checked',total,'survivors so far',len(survivors),flush=True)
for s in survivors[:40]: print(s)
