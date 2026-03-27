# Problem: Find the Longest Balanced Substring of a Binary String
# Language: python3
# Runtime: 1011 ms
# Memory: 13.8 MB

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        def is_balanced(s):
            if not s: return True
            c = Counter(s)
            return c['0'] == c['1'] and len(s.lstrip('0')) == c['1']
        N = len(s)
        ans = 0
        for i in range(N):
            for j in range(i+1,N+1):
                if is_balanced(s[i:j]):
                    ans = max(ans, len(s[i:j]))
        return ans