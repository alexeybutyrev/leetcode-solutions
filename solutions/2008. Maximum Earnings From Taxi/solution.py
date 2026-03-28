# Problem: Maximum Earnings From Taxi
# Language: python3
# Runtime: 3930 ms
# Memory: 185.7 MB

class Solution:
    def maxTaxiEarnings(self, n: int, A: List[List[int]]) -> int:
        route = defaultdict(list)
        for u,v,w in A:
            route[u].append((v,w + v - u))
        
        @cache
        def dp(x):
            if x > n:
                return 0
            
            ans = dp(x+1)
            for u,c in route.get(x,[]):
                ans = max(ans, c + dp(u))
            return ans
            
        return dp(0)
            
                    