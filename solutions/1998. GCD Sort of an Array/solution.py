# Problem: GCD Sort of an Array
# Language: python3
# Runtime: 6187 ms
# Memory: 61.1 MB

from math import gcd
class Solution:
    def gcdSort(self, A: List[int]) -> bool:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        def prime_divisors(x):
            d = 2
            while d * d <= x:
                
                prime = x % d == 0
                while x % d == 0:
                    x //= d
                if prime:
                    yield d
                d += 1 + (d & 1)
            
            if x > 1:
                yield x
            
        primes = defaultdict(list)
        for i,a in enumerate(A):
            for p in prime_divisors(a):
                primes[p].append(i)
        
        
        N = len(A)
        
            
        for i,a in enumerate(A):
            union(i,i)
        
        for p in primes:
            a = primes[p][0]
            for i in range(1,len(primes[p])):
                union(a, primes[p][i])
        
        B = [-1] * N
        groups = defaultdict(list)
        for i in range(N):
            groups[find(i)].append(i)
        
        if len(groups) == 1:
            return True
        
        for g in groups:
            vals = [A[i] for i in groups[g]]
            vals.sort()
            for j,i in enumerate(sorted(groups[g])):
                B[i] = vals[j]
        
        return B == sorted(A)
        
        