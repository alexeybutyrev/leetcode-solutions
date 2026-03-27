# Problem: Count Sequences to K
# Language: python3
# Runtime: 2190 ms
# Memory: 44.5 MB

from fractions import Fraction
class Solution:
    def countSequences(self, A: List[int], K: int) -> int:
        ANS = Fraction(K,1)
        N = len(A)
        @cache
        def dp(i,x):
            if i == N:
                return 1 if x == ANS else 0
            c1 = dp(i+1, x * A[i])
            c2 = dp(i+1, x / A[i])
            c3 = dp(i+1, x )
            return c1 + c2 + c3
        return dp(0,Fraction(1,1))
            