# Problem: Longest Repeating Character Replacement
# Language: python3
# Runtime: 108 ms
# Memory: 14.5 MB

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        i = 0
        count = Counter()
        for j in range(len(s)):
            count[s[j]] +=1
            maxlen = max(maxlen, count[s[j]])
            
            if j - i + 1 > maxlen + k:
                count[s[i]] -= 1
                i += 1
        
        return len(s) - i
            