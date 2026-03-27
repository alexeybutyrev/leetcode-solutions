# Problem: Find K-Length Substrings With No Repeated Characters
# Language: python3
# Runtime: 64 ms
# Memory: 13.9 MB

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = Counter(s[0:k])
        ans = +(max(c.values()) == 1)
        for j in range(k,len(s)):
            c[s[j-k]] -= 1
            c[s[j]] += 1        
            ans += int(max(c.values()) == 1)
        
        return ans
                
        
        
        