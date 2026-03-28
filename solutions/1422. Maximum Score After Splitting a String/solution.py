# Problem: Maximum Score After Splitting a String
# Language: python3
# Runtime: 228 ms
# Memory: 13.9 MB

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        mx = 0
        for i in range(n-1):
            left, right = s[0:i+1], s[i+1:]
            ls, rs = 0, 0
            for e in left:
                if e == '0':
                    ls+=1
            for e in right:
                if e == '1':
                    rs += 1
            mx = max(mx, rs+ls)
            
        return mx
            
            