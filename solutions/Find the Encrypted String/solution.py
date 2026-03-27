# Problem: Find the Encrypted String
# Language: python3
# Runtime: 47 ms
# Memory: 16.8 MB

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        N = 26
        k %= len(s)
        ans = ''
        for i,x in enumerate(s):
            ans += s[(i + k) % len(s)]
        return ans