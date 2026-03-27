# Problem: Delete and Earn
# Language: python3
# Runtime: 91 ms
# Memory: 27.9 MB

class Solution:
    def deleteAndEarn(self, A: List[int]) -> int:
        A = Counter(A)
        N = max(A.keys())
        @cache
        def dp(i):
            if i > N:
                return 0
            return max(dp(i+1), A[i] * i + dp(i+2))
        
        return dp(0)