# Problem: Reverse Degree of a String
# Language: python3
# Runtime: 4 ms
# Memory: 17.8 MB

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,x in enumerate(s):
            d = 26 - (ord(x) - ord('a'))
            ans += (i+1) * d
        return ans