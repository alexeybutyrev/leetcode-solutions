# Problem: Longest Substring with At Most Two Distinct Characters
# Language: python3
# Runtime: 56 ms
# Memory: 14.4 MB

from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c = Counter(s)
        if len(c) <= 2:
            return len(s)
        
        i = 0
        j = 0
        n = len(s)
        maxln = 0
        most_right = dict()
        while j < n and i < n:
            if len(most_right) < 2 or s[j] in most_right:
                most_right[s[j]] = j
                j+=1
            else:
                while most_right[s[i]] != i:
                    i += 1
                del most_right[s[i]]
                i+=1
            maxln = max(maxln, j - i)
            
            
            
        return maxln