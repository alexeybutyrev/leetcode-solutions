# Problem: Score of a String
# Language: python3
# Runtime: 42 ms
# Memory: 16.3 MB

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1,len(s)):
            ans += abs(ord(s[i]) - ord(s[i-1]))
        return ans