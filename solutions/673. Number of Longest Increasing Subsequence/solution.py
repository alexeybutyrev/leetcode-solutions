# Problem: Number of Longest Increasing Subsequence
# Language: python3
# Runtime: 1079 ms
# Memory: 16.6 MB

class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        N = len(A)
        # find len lic
        
        
        dp = [1] * N
        count = [1] * N
        for i in range(N):
            for j in range(i-1,-1,-1):
                if A[i] > A[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = 0
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                        
                    
        
        L = max(dp)
        
        ans = 0
        for i in range(N):
            if dp[i] == L:
                ans += count[i]
        return ans