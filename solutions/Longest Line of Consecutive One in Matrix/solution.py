# Problem: Longest Line of Consecutive One in Matrix
# Language: python3
# Runtime: 544 ms
# Memory: 19.3 MB

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        N,M = len(mat), len(mat[0])
        
        dp = defaultdict(dict)
        for i in range(N):
            for j in range(M):
                dp[i][j] = [1] * 4 if mat[i][j] else [0] * 4
        
        ans = 0
        for i in range(N):
            for j in range(M):
                if mat[i][j]:
                    if j > 0:
                        dp[i][j][0] = dp[i][j-1][0] + 1
                        
                    
                    if i > 0:
                        dp[i][j][1] = dp[i-1][j][1] + 1                   
                    if i > 0 and j > 0:
                        dp[i][j][2] = dp[i-1][j-1][2] + 1                    
                    if i > 0 and j < M - 1:
                        dp[i][j][3] = dp[i-1][j+1][3] + 1

                ans = max(ans, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        
        return ans