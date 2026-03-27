# Problem: Count the Number of Powerful Integers
# Language: python3
# Runtime: 76 ms
# Memory: 17.7 MB

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, L: int, s: str) -> int:
        def f(x):
            fs = str(x)
            while len(fs) < len(s):
                fs = '0' + fs  
            offset = len(fs) - len(s)
            
            N = len(fs)
            @cache
            def dp(i,b):
                if i == N:
                    return 1
                ub = int(fs[i]) if b else 9
                ans = 0
                for d in range(ub + 1):
                    if i >= offset and str(d) != s[i-offset]: continue
                    if d <= L:
                        ans += dp(i+1, b and d == ub)
                return ans
            
            return dp(0,True)
        
        
        return f(finish) - f(start-1)
                    