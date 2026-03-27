# Problem: Longest Substring with At Most K Distinct Characters
# Language: python3
# Runtime: 92 ms
# Memory: 14.5 MB

from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        c = dict()
        
        ln = 0
        N = len(s)
        
        i = j = 0
        
        while j < N and i < N:
            if s[j] in c:
                c[s[j]] += 1
            else:
                c[s[j]] = 1
            if len(c) > k:
                while len(c) > k:
                    c[s[i]] -= 1
                    if not c[s[i]]:
                        del c[s[i]]
                    i+=1
            
            ln = max(ln, 1 + j - i)
            j+=1
        return ln