# Problem: Paint House III
# Language: python3
# Runtime: 1580 ms
# Memory: 50.1 MB

class Solution:
    def minCost(self, A: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dp(i,b,t):
            if i == m:
                if t == 0:
                    return 0
                return inf
            if t < 0:
                return inf
            
            if A[i] == 0:
                ans = cost[i][b-1] + dp(i+1,b,t) if b > 0 else inf
                for j in range(n):
                    if j+1 != b:
                        ans = min(ans, cost[i][j] + dp(i+1,j+1,t-1))
                return ans
            else:
                return dp(i+1,A[i], t if A[i] == b else t-1)
            
        ans = dp(0,0,target)
        return -1 if ans == inf else ans