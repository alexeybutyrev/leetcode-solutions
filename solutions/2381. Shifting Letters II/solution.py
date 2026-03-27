# Problem: Shifting Letters II
# Language: python3
# Runtime: 1843 ms
# Memory: 39.5 MB

from itertools import accumulate
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        d = [0] * (N:=len(s)+1)
        for a,b,c in shifts:
            if c == 1:
                d[a]   += 1
                d[b+1] -= 1
            else:
                d[a]   -= 1
                d[b+1] += 1
        #print(d)
        ans = ""
        curr = 0
        for i,l in enumerate(s):
            curr += d[i]
            
            o = (ord(l) - ord('a') + curr) % 26
            ans += chr(o + ord('a'))
        
        return ans
