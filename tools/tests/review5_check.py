"""Sanity check for review5: every closed normal form t fails some test.

Construction (from the review): write t = \\x1...\\xk. xi u1...um (k >= 1).
Test v1..vk, v_{k+1} with vj = I for j != i, vi = \\z1...\\zm. delta, v_{k+1} = delta.
Then t v1 ... v_{k+1} head-reduces in k + m steps to delta delta = Omega.

Terms use de Bruijn indices: ('v', n) | ('l', body) | ('a', f, x).
"""
import sys
sys.setrecursionlimit(10000)

V, L, A = 'v', 'l', 'a'

def shift(t, d, c=0):
    k = t[0]
    if k == V:
        return (V, t[1] + d) if t[1] >= c else t
    if k == L:
        return (L, shift(t[1], d, c + 1))
    return (A, shift(t[1], d, c), shift(t[2], d, c))

def subst(t, s, j=0):
    """t[s/j] with s shifted appropriately."""
    k = t[0]
    if k == V:
        if t[1] == j:
            return shift(s, j)
        if t[1] > j:
            return (V, t[1] - 1)
        return t
    if k == L:
        return (L, subst(t[1], s, j + 1))
    return (A, subst(t[1], s, j), subst(t[2], s, j))

def beta(body, arg):
    return subst(body, arg, 0)

def head_step(t):
    """One head step in the sense of §2: (\\x.b) u u1..un ->h b[u/x] u1..un. None if no head step."""
    # peel application spine
    args = []
    while t[0] == A:
        args.append(t[2]); t = t[1]
    args.reverse()
    if t[0] == L and args:
        r = beta(t[1], args[0])
        for u in args[1:]:
            r = (A, r, u)
        return r
    return None

def app(*ts):
    r = ts[0]
    for u in ts[1:]:
        r = (A, r, u)
    return r

def lam(n, body):
    for _ in range(n):
        body = (L, body)
    return body

I = (L, (V, 0))
DELTA = (L, (A, (V, 0), (V, 0)))
OMEGA = (A, DELTA, DELTA)

def size(t):
    k = t[0]
    if k == V: return 1
    if k == L: return 1 + size(t[1])
    return 1 + size(t[1]) + size(t[2])

def normal_forms(n, depth):
    """All normal forms of size exactly n with free indices < depth."""
    if n <= 0: return
    # variable
    if n == 1:
        for i in range(depth):
            yield (V, i)
        return
    # abstraction
    for b in normal_forms(n - 1, depth + 1):
        yield (L, b)
    # application spine with variable head: x u1 ... um, all ui normal, m >= 1
    for m in range(1, n):
        # head is a variable (size 1), remaining size n-1 split among m args, each >= 1
        for parts in compositions(n - 1, m):
            for head in range(depth):
                for args in product_nf(parts, depth):
                    yield app((V, head), *args)

def compositions(n, m):
    if m == 1:
        if n >= 1: yield (n,)
        return
    for first in range(1, n - m + 2):
        for rest in compositions(n - first, m - 1):
            yield (first,) + rest

def product_nf(parts, depth):
    if not parts:
        yield ()
        return
    for a in normal_forms(parts[0], depth):
        for rest in product_nf(parts[1:], depth):
            yield (a,) + rest

def peel(t):
    """t = \\x1..\\xk. s with s not an abstraction; return k, s."""
    k = 0
    while t[0] == L:
        k += 1; t = t[1]
    return k, t

def spine(t):
    args = []
    while t[0] == A:
        args.append(t[2]); t = t[1]
    args.reverse()
    return t, args

def check(t):
    k, s = peel(t)
    assert k >= 1, "closed normal form must be an abstraction"
    head, args = spine(s)
    assert head[0] == V and head[1] < k, "head must be a bound variable"
    m = len(args)
    # de Bruijn index head[1] refers to x_{k - head[1]} (innermost = index 0 = x_k)
    i = k - head[1]  # 1-based position among x1..xk
    vs = []
    for j in range(1, k + 1):
        vs.append(lam(m, DELTA) if j == i else I)
    vs.append(DELTA)
    term = app(t, *vs)
    for _ in range(k + m):
        term = head_step(term)
        assert term is not None, "head step expected"
    return term == OMEGA

def main(maxsize):
    total = 0
    for n in range(1, maxsize + 1):
        for t in normal_forms(n, 0):
            total += 1
            if not check(t):
                print("FAILED on", t)
                return
    print("all", total, "closed normal forms of size <=", maxsize, "reach Omega under the constructed test")

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 9)
