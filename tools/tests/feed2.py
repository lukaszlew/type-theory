import sys, itertools
sys.setrecursionlimit(10000)
exec(open('feed.py').read().split('MAXK=')[0])  # reuse definitions
LIMIT=2000
def wn(t): return nf(t,LIMIT)[0] is not None
# test arguments: closed normal terms up to size S plus delta
S=int(sys.argv[2]); args=[]
for s in range(2,S+1): args+=normals(s,0)
args=[a for a in args]
print('args',len(args))
def survives(t):
    # delta feeding up to 10
    cur=t
    for k in range(10):
        cur=('a',cur,DELTA); n,_=nf(cur,LIMIT)
        if n is None: return False
        cur=n
    # single and double args, then followed by delta feeding
    for a in args:
        n,_=nf(('a',t,a),LIMIT)
        if n is None: return False
        cur=n
        for k in range(4):
            cur=('a',cur,DELTA); n2,_=nf(cur,LIMIT)
            if n2 is None: return False
            cur=n2
    for a in args:
        for b in args:
            n,_=nf(('a',('a',t,a),b),LIMIT)
            if n is None: return False
            cur=n
            for k in range(3):
                cur=('a',cur,DELTA); n2,_=nf(cur,LIMIT)
                if n2 is None: return False
                cur=n2
    return True
surv=[]
for size in range(2,int(sys.argv[1])+1):
    cnt=0
    for t in normals(size,0):
        cnt+=1
        if survives(t): surv.append(show(t))
    print('size',size,'terms',cnt,'survivors',len(surv),flush=True)
for s in surv: print(s)
