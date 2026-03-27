# Problem: Target Sum
# Language: python3
# Runtime: 272 ms
# Memory: 42.5 MB

class Solution:
    def findTargetSumWays(self, A: List[int], target: int) -> int:
        N = len(A)
        @cache
        def dfs(i,t):
            if i == N:
                return int(t == 0)
            s1 = dfs(i+1,t-A[i])
            s2 = dfs(i+1,t+A[i])
            return s1 + s2
        
        return dfs(0,target)
            
            
                