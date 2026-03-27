# Problem: Orderly Queue
# Language: python3
# Runtime: 32 ms
# Memory: 14.3 MB

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))
        ans = s
        for i in range(len(s)):
            s = s[1:] + s[0]
            ans = min(ans, s)
        
        return ans