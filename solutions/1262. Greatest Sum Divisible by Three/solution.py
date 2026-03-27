# Problem: Greatest Sum Divisible by Three
# Language: python3
# Runtime: 287 ms
# Memory: 142.3 MB

class Solution:
    def maxSumDivThree(self, A: List[int]) -> int:
        N = len(A)
        @cache
        def dp(i,x):
            if i == N:
                if x == 0: 
                    return 0
                else:
                    return -inf

            # take A[i]
            s1 = A[i] + dp(i+1, (x + A[i]) % 3)
            # skip A[i]
            s2 = dp(i+1, x)
            return max(s1,s2)
        return dp(0,0)
