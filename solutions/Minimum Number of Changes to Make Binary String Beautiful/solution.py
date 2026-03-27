# Problem: Minimum Number of Changes to Make Binary String Beautiful
# Language: python3
# Runtime: 27 ms
# Memory: 16.9 MB

class Solution:
    def minChanges(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)//2):
            i1 = 2*i
            i2 = 2*i+1
            if s[i1] != s[i2]:
                ans += 1
            
        return ans