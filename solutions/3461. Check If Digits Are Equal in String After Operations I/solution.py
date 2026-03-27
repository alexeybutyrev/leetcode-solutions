# Problem: Check If Digits Are Equal in String After Operations I
# Language: python3
# Runtime: 95 ms
# Memory: 17.8 MB

class Solution:
    def hasSameDigits(self, s: str) -> bool:

        def change(s):
            s0 = ""
            for i in range(1,len(s)):
                x = (int(s[i]) + int(s[i-1]))%10
                s0 += str(x)
            return s0

        while len(s) > 2:
            s = change(s)
            
        return s[0] == s[1]