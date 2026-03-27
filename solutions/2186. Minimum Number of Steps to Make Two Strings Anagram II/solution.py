# Problem: Minimum Number of Steps to Make Two Strings Anagram II
# Language: python3
# Runtime: 342 ms
# Memory: 16.5 MB

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs = Counter(s)
        ct = Counter(t)
        
        ans = 0
        for i in range(26):
            c = chr(ord('a') + i)
            ans += abs(cs[c] - ct[c])
        return ans