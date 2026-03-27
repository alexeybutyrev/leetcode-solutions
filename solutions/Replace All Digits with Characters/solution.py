# Problem: Replace All Digits with Characters
# Language: python3
# Runtime: 68 ms
# Memory: 14.3 MB

class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i, l in enumerate(s):
            if i%2 != 0 and l.isdigit() and i > 0:
                ans += chr(ord(s[i-1]) + int(s[i]) )
            else:
                ans += l
        
        return ans