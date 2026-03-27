# Problem: Longest Substring with At Most K Distinct Characters
# Language: python3
# Runtime: 93 ms
# Memory: 16.5 MB

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = j = 0
        c = Counter()
        N = len(s)
        ans = 0
        for j in range(N):
            c[s[j]] += 1
            while len(c) > k:
                c[s[i]] -= 1
                if not c[s[i]]:
                    del c[s[i]]
                i += 1
            
            ans = max(ans, j - i + 1)
        return ans