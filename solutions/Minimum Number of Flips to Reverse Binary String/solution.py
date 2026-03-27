# Problem: Minimum Number of Flips to Reverse Binary String
# Language: python3
# Runtime: 0 ms
# Memory: 18 MB

class Solution:
    def minimumFlips(self, n: int) -> int:
        q = bin(n)[2:]
        s = q[::-1]
        ans= 0
        for x,y in zip(q,s):
            ans += x != y
        return ans