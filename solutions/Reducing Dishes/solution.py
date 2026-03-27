# Problem: Reducing Dishes
# Language: python3
# Runtime: 784 ms
# Memory: 186.7 MB

class Solution:
    def maxSatisfaction(self, A: List[int]) -> int:
        A.sort()
        N = len(A)
        @cache
        def dp(i,t):
            if i == N: return 0
            
            c1 = t * A[i] + dp(i+1,t+1) 
            c2 = dp(i+1,t)
            return max(c1,c2)
        
        return dp(0,1)
    