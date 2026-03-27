# Problem: Minimum Addition to Make Integer Beautiful
# Language: python3
# Runtime: 68 ms
# Memory: 13.9 MB

class Solution:
    def makeIntegerBeautiful(self, n: int, X: int) -> int:
        N = len(str(n))
        def get_tot(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        ans = 0
        c = 0
        while get_tot(n) > X:
            
            d = n % 10
            if d:
                ans += (10 - d) * (10 ** c)
                n //= 10
                n += 1
            else:
                n //= 10    
            c += 1

        return ans