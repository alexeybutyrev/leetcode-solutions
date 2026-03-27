# Problem: Maximum Number of Points with Cost
# Language: python3
# Runtime: 1569 ms
# Memory: 50.9 MB

class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        
        dp = A[0][:]
        
        for i in range(1,N):
            
            left  = [-inf] * M
            right = [-inf] * M
            for j in range(M):
                if j > 0:
                    left[j] = max(left[j-1], dp[j] + j)
                else:
                    left[j] = dp[j] + j
            
            for j in range(M-1,-1,-1):
                if j < M-1:
                    right[j] = max(right[j+1], dp[j] - j)
                else:
                    right[j] = dp[j] - j
            
            for j in range(M):
                dp[j] = A[i][j] + max(left[j] - j, right[j] + j)
        
        return max(dp)