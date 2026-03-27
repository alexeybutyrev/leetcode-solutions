# Problem: Can I Win
# Language: python3
# Runtime: 324 ms
# Memory: 26.9 MB

class Solution:
    def canIWin(self, N: int, T: int) -> bool:
        seen = {}
        
        if N * (N + 1) / 2 < T:
            return False
        
        
        if N * (N + 1) / 2 == T:
            return N % 2
        
        def cw(choises,s):
            if choises[-1] >= s:
                return True
            
            t = tuple(choises)
            if t not in seen:  
                for i,c in enumerate(choises):
                    if not cw(choises[:i] + choises[i+1:] ,s - c):
                        seen[t] = True
                        return True

                seen[t] = False
            
            return seen[t]
        
        res = cw(list(range(1,N+1)), T)

        return  res