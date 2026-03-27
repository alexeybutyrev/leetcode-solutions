# Problem: Knight Dialer
# Language: python3
# Runtime: 1404 ms
# Memory: 47 MB

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        
        d = defaultdict(list)
        d[0] = [4,6]
        d[1] = [8,6]
        d[2] = [7,9]
        d[3] = [4,8]
        d[4] = [0,3,9]
        d[6] = [0,1,7]
        d[7] = [6,2]
        d[8] = [1,3]
        d[9] = [2,4]
        
        MOD = 10**9 + 7
        @cache
        def dp(i,x):
            if i == n: return 1
            ans = 0
            for y in d[x]:
                ans += dp(i+1,y)
                ans %= MOD
            return ans
        
        
        ans = 0
        for x in d:
            ans += dp(1,x)
            ans %= MOD
        return ans
        
        