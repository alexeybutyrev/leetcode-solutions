# Problem: Largest Even Number
# Language: python3
# Runtime: 3 ms
# Memory: 17.3 MB

class Solution:
    def largestEven(self, s: str) -> str:
        if int(s[-1]) & 1:
            while s and int(s[-1]) & 1:
                s = s[:-1]
        return s