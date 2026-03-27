# Problem: Greatest Common Divisor Traversal
# Language: python3
# Runtime: 1666 ms
# Memory: 90.9 MB

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# find prime factors of all intergers before calling it
c = defaultdict(list)
for x in range(2,10**5+1):
    c[x] = prime_factorization(x)

class Solution:
    def canTraverseAllPairs(self, A: List[int]) -> bool:
        N = len(A)
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]


        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        
        hm = {}
        for i,x in enumerate(A):
            union(i,i)
            for y in c[x]:
                if y in hm:
                    # merge with the elemets that have the same primes
                    union(hm[y],i)
                hm[y] = i
        
        s = set()
        for i in range(N):
            s.add(find(i))
        return len(s) == 1
    