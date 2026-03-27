# Problem: Check Digitorial Permutation
# Language: python3
# Runtime: 7586 ms
# Memory: 98 MB

from math import factorial
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        
        @cache
        def fac(x):
            return factorial(x)

        A = [int(x) for x in str(n)]

        def check(p):
            y = 0
            f = 0
            for x in p:
                y = 10 * y + x
                f += fac(x)
            return f == y
        seen = set()
        for p in permutations(A):
            if p[0] and p not in seen:
                seen.add(p)
                if check(p): 
                    return True
        return False
        