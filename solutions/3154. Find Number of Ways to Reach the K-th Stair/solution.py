# Problem: Find Number of Ways to Reach the K-th Stair
# Language: python3
# Runtime: 112 ms
# Memory: 18.3 MB

class Solution:
    def waysToReachStair(self, K: int) -> int:
        
        @cache
        def dp(x,b,j):
            # check if can
            possible = (x == K+1) and (not b)
            if x > K and not possible: return 0
            ans = 1 if x == K else 0
            ans += dp(x + (1 << j), False, j + 1)
            if not b:
                ans += dp(x -1, True, j)
            return ans
            
                
        
        return dp(1,False,0)