# Problem: Greatest Common Divisor of Strings
# Language: python3
# Runtime: 35 ms
# Memory: 13.8 MB

class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        if len(t) > len(s):
            s,t = t,s
        ans = ""
        for i in range(1,len(t)+1):
            x = t[:i]
            if len(s) % i == 0 and len(t) % i == 0 and  x * (len(s)//i) == s and x * (len(t)//i) == t:
                ans = x
        return ans