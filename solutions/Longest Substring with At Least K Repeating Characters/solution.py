# Problem: Longest Substring with At Least K Repeating Characters
# Language: python3
# Runtime: 124 ms
# Memory: 14.4 MB

from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        chrs = set(s)
        n = len(s)
        max_len = 0
        for nc in range(1, len(chrs) + 1):
            
            i = 0
            j = 0
            d = dict()
            count_k = 0 
            n_uniques = 0
            while i < n and j < n:
                
                if s[j] in d:
                    if d[s[j]] == k - 1:
                        count_k += 1
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                    if d[s[j]] == k:
                        count_k += 1
                    n_uniques += 1
                    while n_uniques > nc:
                            d[s[i]] -= 1
                            if d[s[i]] == 0:
                                n_uniques -= 1
                                del d[s[i]]
                            else:
                                if d[s[i]] == k-1:
                                    count_k -= 1
                            i += 1
                if count_k == nc:
                    
                    max_len = max(max_len, 1 + j - i)
                j+= 1
        return max_len