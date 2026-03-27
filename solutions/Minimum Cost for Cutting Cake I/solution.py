# Problem: Minimum Cost for Cutting Cake I
# Language: python3
# Runtime: 1881 ms
# Memory: 81.8 MB

class Solution:
    def minimumCost(self, m: int, n: int, H: List[int], V: List[int]) -> int:
        
        
        @cache
        def dp(xL,xR, yL, yR):
            #print(xL,xR, yL, yR)
            if xR - xL == 1 and yR - yL == 1: return 0
            ans = inf
            for x in range(xL+1,xR):
                ans = min(ans, dp(xL,x, yL, yR) + dp(x,xR, yL, yR) + V[x-1])
            
            for y in range(yL+1,yR):
                ans = min(ans, dp(xL,xR, yL, y) + dp(xL,xR, y, yR) + H[y-1])
            return ans
        
        return dp(0,n,0,m)
