# Problem: Cherry Pickup II
# Language: python3
# Runtime: 864 ms
# Memory: 55.3 MB

class Solution:
    def cherryPickup(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])
        @cache
        def dp(i,j1,j2):
            if j1 < 0 or j2 < 0 or j1 == M or j2 == M:
                return -inf
            
            if i == N:
                return 0
            
            s = 0
            if j1 == j2:
                s = A[i][j1]
            else:
                s = A[i][j1] + A[i][j2]
            
            ans = 0
            for dx in {-1,0,1}:
                for dy in {-1,0,1}:
                    ans = max(ans, dp(i+1,j1+dx,j2+dy))
            return ans + s
        
        return dp(0,0,M-1)