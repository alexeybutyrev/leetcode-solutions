# Problem: Stone Game IV
# Language: python3
# Runtime: 1528 ms
# Memory: 169.7 MB

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        
        @lru_cache(maxsize=None)
        def walk(s):
            
            if s == 0:
                return False
            
            sqrt_root = int(s**0.5)
            for i in range(1,sqrt_root+1):
                if not walk(s - i * i):
                    return True
                
            #dp[(s,turn)] = res
            #return dp[(s,turn)]
            return False
        
        return walk(n)