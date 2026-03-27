# Problem: Find the Maximum Length of a Good Subsequence I
# Language: python3
# Runtime: 2024 ms
# Memory: 29.7 MB

class Solution:
    def maximumLength(self, A: List[int], k: int) -> int:
        N = len(A)
        
        @cache
        def dp(i,k):
            if i == N: return 0
            
            c2 = 0
            ans = 0
            for j in range(i+1,N):
                
                if A[i] == A[j]:
                    c2 = 1 + dp(j,k)
                    break
                else:
                    if k:
                        ans = max(ans, 1 + dp(j,k-1))
            return max(ans, c2)
        
        ans = 0
        for i in range(N):
            ans = max(ans, dp(i,k) + 1)
        return ans