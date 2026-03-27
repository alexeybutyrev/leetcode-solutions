# Problem: Longest Substring Without Repeating Characters
# Language: python3
# Runtime: 144 ms
# Memory: 14.5 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        N = len(s)
        c = Counter()
        i = 0
        j = 0
        while i < N and j < N:
            
            c[s[j]] += 1
            while c[s[j]] > 1:
                c[s[i]] -=1
                i+=1
            
            l = max(1 + j - i, l)
            j+=1
        return l