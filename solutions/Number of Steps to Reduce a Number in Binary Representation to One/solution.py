# Problem: Number of Steps to Reduce a Number in Binary Representation to One
# Language: python3
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        ans = 0
        while len(s) > 1:
            i = len(s) - 1
            if s[i] == '1':
                ans += 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i-=1
                if i < 0: return ans + len(s)
                s[i] = '1'
            while len(s) > 1 and s[-1] == '0':
                s.pop()
                ans += 1
            
        return ans