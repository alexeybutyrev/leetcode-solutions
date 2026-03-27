# Problem: Maximum Length of Repeated Subarray
# Language: python3
# Runtime: 7812 ms
# Memory: 39.2 MB

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        N1 = len(A)
        N2 = len(B)
        
        dp = [[0] * (N2+1) for _ in range(N1+1)]
        ans = 0
        for i in range(1,N1+1):
            for j in range(1,N2+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                
                    
                
        return max(max(x) for x in dp)