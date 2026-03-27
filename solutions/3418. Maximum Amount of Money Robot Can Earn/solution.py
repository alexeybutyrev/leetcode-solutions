# Problem: Maximum Amount of Money Robot Can Earn
# Language: python3
# Runtime: 4901 ms
# Memory: 702.7 MB

class Solution:
    def maximumAmount(self, A: List[List[int]]) -> int:
        N, M = len(A), len(A[0])

        @cache
        def dp(i,j, c1, c2):
            if i == N or j == M: return -inf
            if i == N-1 and j == M-1:
                return max(0, A[i][j]) if (c1 or c2) else A[i][j]

            
            
            s1 = A[i][j] + dp(i+1,j, c1, c2)
            
            if c1:
                s1 = max(s1, dp(i+1,j,not c1,c2))
            else:
                if c2:
                    s1 = max(s1, dp(i+1,j,c1,not c2))
            
            s2 = A[i][j] + dp(i,j+1, c1, c2)
            if c1:
                s2 = max(s2, dp(i,j+1,not c1,c2))
            else:
                if c2:
                    s2 = max(s2, dp(i,j+1,c1,not c2))
            
            
            return max(s1,s2)
        
        return dp(0,0,True, True)