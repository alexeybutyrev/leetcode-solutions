# Problem: Find the Longest Semi-Repetitive Substring
# Language: python3
# Runtime: 1713 ms
# Memory: 16.4 MB

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        N = len(s)
        ans = 0
        for i in range(N):
            for j in range(i+1,N+1):
                c = s[i:j]
                count = 0
                for k,v in groupby(c):
                    l = len(list(v)) 
                    
                    if l > 2:
                        break
                    elif l == 2:
                        count += 1
                    
                else:
                    if count <= 1:
                        ans = max(ans, j - i)
                    
        return ans