# Problem: Roman to Integer
# Language: python3
# Runtime: 68 ms
# Memory: 14.4 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100 , 'D': 500 , 'M': 1000}
        
        ans = 0
        i = 0
        N = len(s)
        while i < N:
            if (i < N - 1) and ((s[i] == "I" and s[i+1] in ("V", "X")) or (s[i] == "X" and s[i+1] in ("L", "C")) or (s[i] == "C" and s[i+1] in ("D", "M"))):
                    ans += hm[s[i+1]] - hm[s[i]]
                    i += 2
            else:
                ans += hm[s[i]]
                i+=1
        
        return ans