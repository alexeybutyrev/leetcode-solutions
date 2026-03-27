# Problem: Selling Pieces of Wood
# Language: python3
# Runtime: 4918 ms
# Memory: 31.3 MB

class Solution:
    def sellingWood(self, m: int, n: int, A: List[List[int]]) -> int:
        DP = [[0] * (n + 1) for _ in range(m+1)]
        for x,y,p in A:
            DP[x][y] = p
        
        
        c = {}
        @cache
        def dp(W,H):
            #print(W,H)
            if W == 0 or H == 0:
                return 0
            
            
            ans = DP[W][H]
            for w in range(1,W // 2 + 1):
                ans = max(ans, dp(w,H) + dp(W-w,H))
            
            for h in range(1,H // 2 + 1):
                ans = max(ans, dp(W,h) + dp(W,H-h))
            
            return ans
                
        #print("XX",dp(3,2) + dp(5,1))
        return dp(m,n)