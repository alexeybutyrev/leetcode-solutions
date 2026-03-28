# Problem: Longest Nice Substring
# Language: python3
# Runtime: 96 ms
# Memory: 14.2 MB

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        
        ans = ""
        res = ""
        for i in range(N):
            for j in range(N-1, i-1, -1):
                ss = s[i:j+1]
                ans = ""
                for l in ss:
                    if l.upper() in ss and l.lower() in ss:
                        ans += l
                    else:
                        break
                else:
                    if len(ans) > len(res):
                        res = ans
                        
                    
        

        return res
