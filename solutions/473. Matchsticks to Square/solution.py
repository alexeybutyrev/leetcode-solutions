# Problem: Matchsticks to Square
# Language: python3
# Runtime: 2888 ms
# Memory: 82.5 MB

class Solution:
    def makesquare(self, A: List[int]) -> bool:
        
        c = sum(A)
        if c % 4 != 0:
            return False
        a = c // 4
        
        N = len(A)
        
        @lru_cache(None)
        def dp(mask, c):
            
            s = sum( A[i] if (mask & (1 << i)) else 0 for i in range(N))
            if s == a * 3 and c == 2:
                return True
            
            if s > a * 3:
                return False
            
            if s > 0 and s % a == 0:
                c += 1
                
            for i in range(N):
                if (mask & (1 << i)) == 0:
                    if dp(mask | (1 << i), c):
                        return True
            return False
        
        return dp(0, 0)
                
            
    