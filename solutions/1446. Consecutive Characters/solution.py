# Problem: Consecutive Characters
# Language: python3
# Runtime: 40 ms
# Memory: 14.2 MB

class Solution:
    def maxPower(self, s: str) -> int:
        
        if not s:
            return 0
        
        count = 1
        res = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                count = 1
            res = max(count, res)
        
        return res